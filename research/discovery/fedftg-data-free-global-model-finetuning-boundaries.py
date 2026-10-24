#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 480:
FedFTG (Fine-Tuning Global Model via Data-Free Knowledge Distillation for Non-IID Federated Learning,
Zhang, Shen, Ding, Tao, & Duan 2022, CVPR 2022, arXiv:2203.09249).

Verifies:
1. Customized label sampling distribution p_t(y) (Equation 9) and class-level
   ensemble importance weights alpha_t^{k,y} (Equation 10):
   - p_t(y) = (sum_{k in S_t} n_k^y) / (sum_{y'} sum_{k in S_t} n_k^{y'}),
     ensuring sum_y p_t(y) == 1 and zero probability on classes absent from active clients S_t.
   - alpha_t^{k,y} = n_k^y / sum_{i in S_t} n_i^y, ensuring sum_{k in S_t} alpha_t^{k,y} == 1
     for every active class y and weighting each local teacher k's KL discrepancy L_{md}^k
     (Equation 4) and semantic cross-entropy L_{cls}^k (Equation 6) in proportion to its
     class-y sample count rather(than uniform 1/|S_t|).
2. Diversity loss L_{dis} (Equation 7):
   L_{dis} = exp( (1 / Q^2) sum_{i,j in {1..Q}} (- ||x_tilde_i - x_tilde_j||_2 * ||z_i - z_j||_2) ),
   which achieves its maximum 1.0 under generator mode collapse (x_tilde_i == x_tilde_j for all i, j)
   and strictly decreases when distinct latent codes z_i != z_j produce dispersed pseudo-inputs x_tilde_i != x_tilde_j.
3. Minimax hard-sample mining objective (Equation 8, Algorithm 2):
   min_omega max_theta E_{z, y} [ L_{md} - lambda_{cls} L_{cls} - lambda_{dis} L_{dis} ].
"""

from __future__ import annotations
import math


def softmax(logits: list[float]) -> list[float]:
    m = max(logits)
    exps = [math.exp(v - m) for v in logits]
    s = sum(exps)
    return [e / s for e in exps]


def kl_div(p: list[float], q: list[float]) -> float:
    return sum(pi * math.log(max(pi, 1e-15) / max(qi, 1e-15)) for pi, qi in zip(p, q))


def diversity_loss(x_tildes: list[list[float]], zs: list[list[float]]) -> float:
    q = len(x_tildes)
    total = 0.0
    for i in range(q):
        for j in range(q):
            dx = math.sqrt(sum((x_tildes[i][d] - x_tildes[j][d]) ** 2 for d in range(len(x_tildes[0]))))
            dz = math.sqrt(sum((zs[i][d] - zs[j][d]) ** 2 for d in range(len(zs[0]))))
            total += -dx * dz
    return math.exp(total / (q * q))


def main() -> None:
    # Active client set S_t = {0, 1, 2} with skewed class counts n_k^y over C=3 classes
    n_ky = [
        [90, 10, 0],   # Client 0 dominates class 0
        [5, 85, 10],   # Client 1 dominates class 1
        [5, 5, 40],    # Client 2 dominates class 2
    ]
    K_active = len(n_ky)
    C = len(n_ky[0])

    # 1. Verify Eq (9) customized label sampling distribution p_t(y) and Eq (10) class-level weights alpha_t^{k,y}
    class_totals = [sum(n_ky[k][y] for k in range(K_active)) for y in range(C)]
    grand_total = sum(class_totals)
    p_t = [ct / grand_total for ct in class_totals]
    assert abs(sum(p_t) - 1.0) < 1e-15
    assert p_t[0] == 100 / 250 and p_t[1] == 100 / 250 and p_t[2] == 50 / 250

    alpha_t = [
        [n_ky[k][y] / class_totals[y] for y in range(C)]
        for k in range(K_active)
    ]
    for y in range(C):
        assert abs(sum(alpha_t[k][y] for k in range(K_active)) - 1.0) < 1e-15
    # Client 0 has zero weight on class 2 because n_0^2 == 0
    assert alpha_t[0][2] == 0.0 and alpha_t[0][0] == 0.90

    # 2. Verify Eq (7) diversity loss penalizes mode collapse
    zs = [[-1.0, 0.5], [0.8, -0.7], [0.2, 1.2]]
    collapsed_x = [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]
    dispersed_x = [[-1.2, 0.6], [0.9, -0.8], [0.3, 1.4]]
    l_dis_collapsed = diversity_loss(collapsed_x, zs)
    l_dis_dispersed = diversity_loss(dispersed_x, zs)
    assert abs(l_dis_collapsed - 1.0) < 1e-15
    assert l_dis_dispersed < 0.35 * l_dis_collapsed

    # 3. Verify hard sample mining (max_theta L_{md}) vs student distillation (min_omega L_{md}, Eqs 3-4 & 8)
    # Local teacher logits on a candidate pseudo-sample for class y=0
    teacher_logits = [
        [2.4, -0.5, -1.2],  # Client 0 (expert on class 0, alpha_t[0][0]=0.90)
        [0.8, 0.4, -0.5],   # Client 1 (alpha_t[1][0]=0.05)
        [0.6, -0.2, 0.5],   # Client 2 (alpha_t[2][0]=0.05)
    ]
    teacher_probs = [softmax(tl) for tl in teacher_logits]

    # Global model logits initially drifted away from class-0 expert
    omega_logits = [0.5, 0.5, 0.0]

    def l_md_class0(student_logits: list[float]) -> float:
        p_global = softmax(student_logits)
        return sum(alpha_t[k][0] * kl_div(p_global, teacher_probs[k]) for k in range(K_active))

    l_md_init = l_md_class0(omega_logits)
    # Exact closed-form minimizer of sum_k alpha_k KL(p_global || p_k) is log-linear pool:
    # star_logits[c] = sum_k alpha_t[k][0] * teacher_logits[k][c]
    star_logits = [
        sum(alpha_t[k][0] * teacher_logits[k][c] for k in range(K_active))
        for c in range(C)
    ]
    l_md_opt = l_md_class0(star_logits)

    # Student inner loop (Algorithm 2 lines 9-11): gradient descent on omega to minimize L_md
    eps = 1e-6
    lr_d = 0.8
    curr_logits = omega_logits[:]
    for _ in range(100):
        base = l_md_class0(curr_logits)
        grad = []
        for c in range(C):
            pert = curr_logits[:]
            pert[c] += eps
            grad.append((l_md_class0(pert) - base) / eps)
        curr_logits = [curr_logits[c] - lr_d * grad[c] for c in range(C)]
    l_md_final = l_md_class0(curr_logits)
    assert l_md_final < l_md_init and abs(l_md_final - l_md_opt) < 1e-4

    # Generator outer step (Algorithm 2 line 8): gradient ascent on L_md to mine harder discrepancy
    # Perturbing input features toward region where global student disagrees with expert teacher increases L_md
    hard_omega_logits = [-0.5, 1.2, 0.8]
    assert l_md_class0(hard_omega_logits) > l_md_init

    print(
        f"[PASS] FedFTG boundary verification passed: L_dis(collapsed)={l_dis_collapsed:.3f} -> "
        f"L_dis(dispersed)={l_dis_dispersed:.3f}, L_md_init={l_md_init:.4f} -> L_md_final={l_md_final:.4f} (opt={l_md_opt:.4f})"
    )


if __name__ == "__main__":
    main()
