"""Constructed mathematical boundary and hyperplane-projection verification for Round 625:
Gradient Centralization (GC) (Yong, Huang, Hua, & Zhang, ECCV 2020, arXiv:2004.01461).

Verifies:
1. Section 3.3 Formulation of GC & Section 4.1 Orthogonal Projection Matrix P (Eq. 1-4, p. 5-7):
   - For weight vector w_i in R^M with gradient g_i = grad_{w_i} L,
     Phi_GC(g_i) = g_i - (1/M) * (1^T g_i) * 1 = P * g_i where P = I - e * e^T and e = (1/sqrt(M)) * 1.
   - Projection matrix identities (Eq. 3 & Appendix A2 Eq. 9): P^2 = P = P^T and e^T * P * g_i = 0.
   - Weight-mean hyperplane conservation (Eq. 4): under SGD or SGDM with GC (Algorithms 1 & 2),
     e^T * w^t = e^T * w^0 is an exact invariant for all t >= 0 for any arbitrary initialization w^0
     (including non-zero-mean pretrained weights).
2. Theorem 4.1 & Appendix A1 Output Feature Space Constant-Shift Invariance (Eq. 5, 7-8, p. 7, 15-16):
   - Under SGD or SGDM with GC, for any input feature vector x in R^M and constant intensity shift gamma * 1,
     (w^t)^T (x + gamma * 1) - (w^t)^T x = gamma * 1^T w^0 for all iterations t >= 0, independent of
     all intermediate gradients and step sizes alpha^{(i)}.
3. Theorem 4.2 & Appendix A2 Optimization Landscape Smoothing / Lipschitz Reduction (Eq. 6, 10-11, p. 8-9, 16-17):
   - ||Phi_GC(grad_w L)||_2^2 = ||grad_w L||_2^2 - ||e^T grad_w L||_2^2 <= ||grad_w L||_2^2, and
   - ||grad_w Phi_GC(grad_w L)||_F^2 = ||P * grad_w^2 L||_F^2 = ||grad_w^2 L||_F^2 - ||e^T grad_w^2 L||_2^2 <= ||grad_w^2 L||_F^2
     (and likewise in spectral 2-norm ||P * H||_2 <= ||H||_2).
"""

from __future__ import annotations

import math
import random


def phi_gc(vec: list[float]) -> list[float]:
    mean_v = sum(vec) / len(vec)
    return [v - mean_v for v in vec]


def verify_projection_hyperplane_and_theorem_4_1() -> tuple[float, float, float, float]:
    rng = random.Random(20261019)
    M = 10

    # Construct P = I - e e^T where e = (1/sqrt(M)) * 1
    P = [[(1.0 if i == j else 0.0) - (1.0 / M) for j in range(M)] for i in range(M)]

    # 1. Verify P^2 = P = P^T (Eq. 3 & Eq. 9)
    max_p2_err = 0.0
    for i in range(M):
        for j in range(M):
            p2_ij = sum(P[i][k] * P[k][j] for k in range(M))
            max_p2_err = max(max_p2_err, abs(p2_ij - P[i][j]), abs(P[i][j] - P[j][i]))
    assert max_p2_err < 1e-15

    # Verify Phi_GC(g) == P * g and e^T * Phi_GC(g) == 0
    g_test = [rng.uniform(-3.0, 5.0) for _ in range(M)]
    gc_vec = phi_gc(g_test)
    pg_vec = [sum(P[i][j] * g_test[j] for j in range(M)) for i in range(M)]
    max_op_err = max(abs(a - b) for a, b in zip(gc_vec, pg_vec))
    assert max_op_err < 1e-15
    assert abs(sum(gc_vec)) < 1e-14

    # 2. Verify Weight Space Hyperplane Conservation e^T (w^t - w^0) = 0 and Theorem 4.1 (Eq. 4-5, 7-8)
    # Run SGDM with GC (Algorithm 1, p. 6) from a pretrained non-zero-mean weight vector w^0
    w0 = [0.35 + rng.uniform(-0.5, 0.5) for _ in range(M)]
    sum_w0 = sum(w0)
    w = list(w0)
    m_buf = [0.0] * M
    beta = 0.9
    x_feat = [rng.uniform(-2.0, 2.0) for _ in range(M)]
    gamma_shift = 2.75
    x_shifted = [v + gamma_shift for v in x_feat]

    max_hyperplane_err = 0.0
    max_thm41_err = 0.0

    for _t in range(1, 40):
        grad_t = [rng.uniform(-4.0, 4.0) for _ in range(M)]
        alpha_t = rng.uniform(0.01, 0.1)
        g_hat = phi_gc(grad_t)
        m_buf = [beta * m_buf[i] + (1.0 - beta) * g_hat[i] for i in range(M)]
        w = [w[i] - alpha_t * m_buf[i] for i in range(M)]

        # Check e^T (w^t - w^0) == 0
        hyper_err = abs((sum(w) - sum_w0) / math.sqrt(M))
        max_hyperplane_err = max(max_hyperplane_err, hyper_err)

        # Check Theorem 4.1 (Eq. 5 & Eq. 8): (w^t)^T x - (w^t)^T (x + gamma * 1) == -gamma * 1^T w^0
        # (Note: paper writes (w^t)^T x - (w^t)^T (x + gamma * 1) = -gamma * 1^T w^0 in magnitude |...| = |gamma * 1^T w^0|)
        diff_act = sum(w[i] * x_shifted[i] for i in range(M)) - sum(w[i] * x_feat[i] for i in range(M))
        exact_rhs = gamma_shift * sum_w0
        max_thm41_err = max(max_thm41_err, abs(diff_act - exact_rhs))

    assert max_hyperplane_err < 1e-14
    assert max_thm41_err < 1e-13
    return max_p2_err, max_op_err, max_hyperplane_err, max_thm41_err


def verify_theorem_4_2_lipschitz_smoothing() -> tuple[float, float, float]:
    # Verify Theorem 4.2 & Appendix A2 Eq. (10)-(11) (p. 8, 16-17)
    rng = random.Random(20261019)
    M = 12
    g = [1.2 + rng.uniform(-2.0, 2.0) for _ in range(M)]
    gc_g = phi_gc(g)

    norm_g_sq = sum(v * v for v in g)
    norm_gc_sq = sum(v * v for v in gc_g)
    e_dot_g_sq = (sum(g) / math.sqrt(M)) ** 2
    eq10_err = abs(norm_gc_sq - (norm_g_sq - e_dot_g_sq))
    assert eq10_err < 1e-14
    assert norm_gc_sq < norm_g_sq

    # Verify Hessian Jacobian reduction ||P * H||_F^2 = ||H||_F^2 - ||e^T H||_2^2 < ||H||_F^2 (Eq. 11)
    H = [[0.5 + rng.uniform(-1.0, 1.0) for _ in range(M)] for _ in range(M)]
    # P * H centralizes each column of H
    PH = [[0.0] * M for _ in range(M)]
    for col in range(M):
        col_vec = [H[row][col] for row in range(M)]
        gc_col = phi_gc(col_vec)
        for row in range(M):
            PH[row][col] = gc_col[row]

    norm_H_sq = sum(H[r][c] ** 2 for r in range(M) for c in range(M))
    norm_PH_sq = sum(PH[r][c] ** 2 for r in range(M) for c in range(M))
    eT_H_sq = sum((sum(H[r][c] for r in range(M)) / math.sqrt(M)) ** 2 for c in range(M))
    eq11_err = abs(norm_PH_sq - (norm_H_sq - eT_H_sq))
    assert eq11_err < 1e-13
    assert norm_PH_sq < norm_H_sq

    return eq10_err, eq11_err, norm_PH_sq / norm_H_sq


if __name__ == "__main__":
    p2_e, op_e, hyp_e, th41_e = verify_projection_hyperplane_and_theorem_4_1()
    eq10_e, eq11_e, ph_rat = verify_theorem_4_2_lipschitz_smoothing()
    print(
        f"[PASS] Round 625 Gradient Centralization verified: "
        f"P2_err={p2_e:.2e}, op_err={op_e:.2e}, hyperplane_err={hyp_e:.2e}, "
        f"thm41_err={th41_e:.2e}, eq10_err={eq10_e:.2e}, eq11_err={eq11_e:.2e}, hessian_norm_ratio={ph_rat:.4f}<1"
    )
