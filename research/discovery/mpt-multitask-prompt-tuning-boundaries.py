#!/usr/bin/env python3
"""Constructed boundary and algebraic verification for Round 702:
Multitask Prompt Tuning Enables Parameter-Efficient Transfer Learning (MPT)
(Wang et al., ICLR 2023, arXiv:2303.02861).
"""

import math
import random


def outer_product(u, v):
    """Rank-one matrix W_k = u_k (x) v_k^T in R^{l x d} (Section 3.1, Eq. 2)."""
    return [[u_i * v_j for v_j in v] for u_i in u]


def hadamard_product(A, B):
    """Element-wise Hadamard product P_hat_k = P^* o W_k (Section 3.1, Eq. 2)."""
    assert len(A) == len(B) and len(A[0]) == len(B[0])
    return [[A[i][j] * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def prompt_decompose(P_star, u_k, v_k):
    """Eq. 2: P_hat_k = P^* o (u_k (x) v_k^T)."""
    W_k = outer_product(u_k, v_k)
    return hadamard_product(P_star, W_k)


def softmax_temp(logits, T=1.0):
    """Section 3.1: Temperature-smoothed output probability distribution p_j = exp(z_j / T) / Z."""
    assert T > 0.0
    scaled = [z / T for z in logits]
    m = max(scaled)
    exps = [math.exp(s - m) for s in scaled]
    Z = sum(exps)
    return [e / Z for e in exps]


def kl_divergence(p_teacher, p_student):
    """Section 3.1 Eq. 3: KL(P(y | x; Theta, P_k^(teacher)) || P(y | x; Theta, P_hat_k))."""
    kl = 0.0
    for pt, ps in zip(p_teacher, p_student):
        if pt > 0.0:
            kl += pt * math.log(pt / max(ps, 1e-15))
    return kl


def hidden_mse_loss(H_student, H_teacher):
    """Section 3.1 Eq. 4: L_Hidden = sum (H_{k,i} - H_{k,i}^(teacher))^2."""
    return sum(
        (H_student[r][c] - H_teacher[r][c]) ** 2
        for r in range(len(H_student))
        for c in range(len(H_student[0]))
    )


def main():
    rng = random.Random(2023)

    # 1. Verify parameter efficiency formulas (Section 3.2 & Table 1):
    # For T5-Base (220M params), prompt length l = 100, embedding dimension d = 768:
    l_len = 100
    d_emb = 768
    t5_base_params = 220_000_000
    single_task_params = (l_len * d_emb) + (l_len + d_emb)  # 76,800 + 868 = 77,668 (~77.6K)
    pct_of_plm = (single_task_params / t5_base_params) * 100.0
    assert single_task_params == 77668
    assert abs(pct_of_plm - 0.0353) < 0.001

    # Multitask target adaptation (MPT* on tau = 8 GLUE tasks, Table 1 bottom):
    tau_tasks = 8
    mpt_star_params_per_task = (l_len * d_emb) / tau_tasks + (l_len + d_emb)  # 9,600 + 868 = 10,468 (~10.5K)
    assert abs(mpt_star_params_per_task - 10468.0) < 1e-9

    # 2. Verify Eq. 2 multiplicative rank-one decomposition and post-training matrix compression:
    l_small, d_small = 6, 8
    P_star = [[rng.gauss(0.0, 1.0) for _ in range(d_small)] for _ in range(l_small)]
    u_1 = [1.0] * l_small
    v_1 = [1.0] * d_small
    # All-ones task vectors recover the shared prompt P^* exactly:
    P_hat_identity = prompt_decompose(P_star, u_1, v_1)
    assert P_hat_identity == P_star

    # Post-training compression: P_hat_k is a single l x d matrix acting identically to (P^*, u_k, v_k):
    u_k = [rng.gauss(1.0, 0.3) for _ in range(l_small)]
    v_k = [rng.gauss(1.0, 0.3) for _ in range(d_small)]
    P_hat_k = prompt_decompose(P_star, u_k, v_k)
    for i in range(l_small):
        for j in range(d_small):
            assert abs(P_hat_k[i][j] - P_star[i][j] * u_k[i] * v_k[j]) < 1e-15

    # 3. Verify Prompt Distillation loss properties (Eqs. 3-5):
    teacher_logits = [2.1, -0.5, 0.8, -1.2]
    p_teach = softmax_temp(teacher_logits, T=2.0)
    # When P_hat_k == P_k^(teacher), L_Logits == 0 and L_Hidden == 0:
    kl_exact = kl_divergence(p_teach, p_teach)
    assert abs(kl_exact) < 1e-15

    student_logits_init = [0.1, 0.2, -0.1, 0.0]
    p_stud_init = softmax_temp(student_logits_init, T=2.0)
    kl_init = kl_divergence(p_teach, p_stud_init)
    assert kl_init > 0.1

    # Verify distillation optimization of (P^*, u_k, v_k) reduces L_Hidden + L_Logits across 2 source tasks:
    u_a_true = [1.2, 0.8, 1.1, 0.9, 1.3, 0.7]
    v_a_true = [0.9, 1.1, 0.8, 1.2, 1.0, 0.7, 1.3, 0.85]
    u_b_true = [0.7, 1.3, 0.9, 1.1, 0.8, 1.2]
    v_b_true = [1.2, 0.8, 1.1, 0.9, 0.75, 1.25, 0.8, 1.15]
    P_teach_a = prompt_decompose(P_star, u_a_true, v_a_true)
    P_teach_b = prompt_decompose(P_star, u_b_true, v_b_true)

    # Student initialized with perturbed shared prompt and unit task vectors
    P_stud = [[P_star[i][j] + rng.gauss(0.0, 0.3) for j in range(d_small)] for i in range(l_small)]
    u_a = [1.0] * l_small
    v_a = [1.0] * d_small
    u_b = [1.0] * l_small
    v_b = [1.0] * d_small

    def dist_loss():
        Pa = prompt_decompose(P_stud, u_a, v_a)
        Pb = prompt_decompose(P_stud, u_b, v_b)
        return hidden_mse_loss(Pa, P_teach_a) + hidden_mse_loss(Pb, P_teach_b)

    loss_init = dist_loss()
    lr = 0.05
    for _ in range(150):
        Pa = prompt_decompose(P_stud, u_a, v_a)
        Pb = prompt_decompose(P_stud, u_b, v_b)
        for i in range(l_small):
            for j in range(d_small):
                diff_a = 2.0 * (Pa[i][j] - P_teach_a[i][j])
                diff_b = 2.0 * (Pb[i][j] - P_teach_b[i][j])
                g_P = diff_a * u_a[i] * v_a[j] + diff_b * u_b[i] * v_b[j]
                P_stud[i][j] -= lr * g_P
        Pa = prompt_decompose(P_stud, u_a, v_a)
        Pb = prompt_decompose(P_stud, u_b, v_b)
        for i in range(l_small):
            g_ua = sum(2.0 * (Pa[i][j] - P_teach_a[i][j]) * P_stud[i][j] * v_a[j] for j in range(d_small))
            g_ub = sum(2.0 * (Pb[i][j] - P_teach_b[i][j]) * P_stud[i][j] * v_b[j] for j in range(d_small))
            u_a[i] -= lr * g_ua
            u_b[i] -= lr * g_ub
        Pa = prompt_decompose(P_stud, u_a, v_a)
        Pb = prompt_decompose(P_stud, u_b, v_b)
        for j in range(d_small):
            g_va = sum(2.0 * (Pa[i][j] - P_teach_a[i][j]) * P_stud[i][j] * u_a[i] for i in range(l_small))
            g_vb = sum(2.0 * (Pb[i][j] - P_teach_b[i][j]) * P_stud[i][j] * u_b[i] for i in range(l_small))
            v_a[j] -= lr * g_va
            v_b[j] -= lr * g_vb

    loss_final = dist_loss()
    assert loss_final < 1e-4 and loss_final < loss_init * 1e-4

    print(
        f"[PASS] MPT boundary verification passed: "
        f"single_task_params={single_task_params:,} ({pct_of_plm:.3f}%), "
        f"mpt_star_params={mpt_star_params_per_task:,.0f}, "
        f"distill_loss: {loss_init:.4f} -> {loss_final:.6f}"
    )


if __name__ == "__main__":
    main()
