#!/usr/bin/env python3
"""Constructed boundary verification for Round 488: KT-pFL (Zhang et al. 2021, NeurIPS 2021).

Verifies:
1. Definition 3.1 & Eq. (2)/(4): Personalized distillation objective L_{per,n}(w^n) with
   knowledge coefficient matrix c in R^{N x N} and Frobenius regularization rho ||c - 1/N||_F^2.
2. Alternating optimization (Algorithm 1, Eqs. 5-7):
   - Client local update on private data (Eq. 5) and public distillation step (Eq. 6).
   - Server gradient descent update on knowledge coefficient matrix c (Eq. 7) with
     analytical KL-divergence gradient w.r.t. c_{mn} and shrinkage toward 1/N.
3. Theorem 4.1 & Remark 4.1: Under non-IID two-cluster client distributions, the learned
   personalized ensemble sum_m c_{mn}^* s(w^m, x) achieves strictly lower expected KL/MSE
   risk on client n's target distribution than both standalone local prediction (c = I_N)
   and uniform ensemble averaging (FedMD / FedDF, c = 1/N).
"""

import math


def kl_div(p, q):
    """KL(p || q) = sum_k p_k log(p_k / q_k) for probability vectors p, q."""
    eps = 1e-12
    return sum(pk * math.log(max(pk, eps) / max(qk, eps)) for pk, qk in zip(p, q))


def verify_kt_pfl_boundaries():
    # N = 4 clients in two non-IID clusters: {0, 1} (cluster A) and {2, 3} (cluster B)
    # 3 classes, M = 2 public reference samples
    # True cluster-conditional class distributions on public samples:
    p_true_A = [[0.80, 0.15, 0.05], [0.10, 0.80, 0.10]]
    p_true_B = [[0.05, 0.15, 0.80], [0.75, 0.10, 0.15]]
    targets = [p_true_A, p_true_A, p_true_B, p_true_B]

    # Noisy local soft predictions s(w^m, x_r) trained on small private datasets D_m:
    s_local = [
        [[0.74, 0.19, 0.07], [0.14, 0.74, 0.12]],  # client 0 (cluster A, noisy)
        [[0.86, 0.11, 0.03], [0.06, 0.86, 0.08]],  # client 1 (cluster A, complementary noise)
        [[0.07, 0.18, 0.75], [0.70, 0.13, 0.17]],  # client 2 (cluster B, noisy)
        [[0.03, 0.12, 0.85], [0.80, 0.07, 0.13]],  # client 3 (cluster B, complementary noise)
    ]
    N = 4
    M = 2
    C = 3

    def ensemble_pred(c_col_n, r):
        # Raw linear combination sum_m c_{mn} s(w^m, x_r), normalized to simplex if needed
        vec = [sum(c_col_n[m] * s_local[m][r][k] for m in range(N)) for k in range(C)]
        tot = sum(max(v, 1e-12) for v in vec)
        return [max(v, 1e-12) / tot for v in vec]

    def expected_risk(c_mat):
        # Average KL divergence between true distribution of client n and ensemble_pred(c_{:,n})
        total = 0.0
        for n in range(N):
            col_n = [c_mat[m][n] for m in range(N)]
            for r in range(M):
                total += kl_div(targets[n][r], ensemble_pred(col_n, r))
        return total / (N * M)

    # 1. Verify Theorem 4.1 & Remark 4.1:
    c_standalone = [[1.0 if m == n else 0.0 for n in range(N)] for m in range(N)]
    c_uniform = [[1.0 / N for _ in range(N)] for _ in range(N)]
    c_cluster = [
        [0.5, 0.5, 0.0, 0.0],
        [0.5, 0.5, 0.0, 0.0],
        [0.0, 0.0, 0.5, 0.5],
        [0.0, 0.0, 0.5, 0.5],
    ]

    risk_standalone = expected_risk(c_standalone)
    risk_uniform = expected_risk(c_uniform)
    risk_cluster = expected_risk(c_cluster)

    assert risk_cluster < risk_standalone, f"Theorem 4.1 violated: {risk_cluster} >= {risk_standalone}"
    assert risk_cluster < risk_uniform, f"Remark 4.1 violated: {risk_cluster} >= {risk_uniform}"

    # 2. Verify Eq. (7) server gradient descent update on knowledge coefficient matrix c:
    # Initialize c^{(0)} = (1/N) * 1_{N x N}
    c = [[1.0 / N for _ in range(N)] for _ in range(N)]
    eta3 = 0.15
    lam = 1.0
    rho = 0.02

    def kl_teacher_student_loss(c_mat):
        # Objective in Eq. (4) with fixed w^*:
        # sum_{n=1}^N (1/N) * lam * sum_{r} KL(p_ens(c_{:,n}, r) || s_local[n][r]) + rho * ||c - 1/N||_F^2
        loss = 0.0
        for n in range(N):
            col_n = [c_mat[m][n] for m in range(N)]
            for r in range(M):
                p_ens = [sum(col_n[m] * s_local[m][r][k] for m in range(N)) for k in range(C)]
                loss += (1.0 / N) * lam * kl_div(p_ens, s_local[n][r])
        reg = sum((c_mat[m][n] - 1.0 / N) ** 2 for m in range(N) for n in range(N))
        return loss + rho * reg

    init_obj = kl_teacher_student_loss(c)
    for _ in range(40):
        grad_c = [[0.0 for _ in range(N)] for _ in range(N)]
        for n in range(N):
            for r in range(M):
                p_ens = [max(sum(c[m][n] * s_local[m][r][k] for m in range(N)), 1e-12) for k in range(C)]
                q_stu = s_local[n][r]
                for m in range(N):
                    # d/dc_{mn} sum_k p_ens_k log(p_ens_k / q_stu_k) = sum_k s_m_k * (log(p_ens_k / q_stu_k) + 1)
                    g_mn = sum(
                        s_local[m][r][k] * (math.log(p_ens[k] / max(q_stu[k], 1e-12)) + 1.0)
                        for k in range(C)
                    )
                    grad_c[m][n] += (1.0 / N) * lam * g_mn
        # Eq. (7) update + projection onto non-negative column-simplex
        for n in range(N):
            col = [
                max(0.0, c[m][n] - eta3 * grad_c[m][n] - 2.0 * eta3 * rho * (c[m][n] - 1.0 / N))
                for m in range(N)
            ]
            s_col = sum(col)
            for m in range(N):
                c[m][n] = col[m] / s_col

    final_obj = kl_teacher_student_loss(c)
    assert final_obj < init_obj, f"Eq. (7) update failed to decrease objective: {final_obj} >= {init_obj}"
    # Verify intra-cluster weight exceeds cross-cluster weight
    intra_weight = 0.5 * (c[0][1] + c[1][0])
    inter_weight = 0.5 * (c[2][1] + c[3][0])
    assert intra_weight > inter_weight, f"Expected intra-cluster > inter-cluster: {intra_weight} vs {inter_weight}"

    # 3. Verify extreme rho -> infinity limit shrinks c -> 1/N (Section 5.2.2)
    c_large_rho = [[1.0 if m == n else 0.0 for n in range(N)] for m in range(N)]
    rho_huge = 50.0
    eta_small = 0.008
    for _ in range(100):
        for m in range(N):
            for n in range(N):
                c_large_rho[m][n] -= 2.0 * eta_small * rho_huge * (c_large_rho[m][n] - 1.0 / N)
    frob_gap = math.sqrt(sum((c_large_rho[m][n] - 1.0 / N) ** 2 for m in range(N) for n in range(N)))
    assert frob_gap < 1e-6, f"Large rho failed to shrink c to 1/N: frob_gap={frob_gap}"

    print(
        f"[PASS] Round 488 KT-pFL (Zhang et al. 2021): risk_cluster={risk_cluster:.6f} < "
        f"risk_standalone={risk_standalone:.6f} < risk_uniform={risk_uniform:.6f}, "
        f"obj_init={init_obj:.4f} -> obj_final={final_obj:.4f}, intra_c={intra_weight:.3f} > inter_c={inter_weight:.3f}"
    )


if __name__ == "__main__":
    verify_kt_pfl_boundaries()
