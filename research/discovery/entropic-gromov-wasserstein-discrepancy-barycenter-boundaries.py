#!/usr/bin/env python3
"""Boundary and regime verification for Peyre, Cuturi, & Solomon (2016)
Gromov-Wasserstein Averaging of Kernel and Distance Matrices (ICML 2016, PMLR 48:2664-2672).
"""

import json
import math


def sinkhorn_ot(cost, p, q, eps, max_iter=400, tol=1e-13):
    """Equation (3): Sinkhorn projections for T(c, p, q) = diag(a) K diag(b)."""
    n1, n2 = len(p), len(q)
    K = [[math.exp(-cost[i][j] / eps) for j in range(n2)] for i in range(n1)]
    a = [1.0] * n1
    b = [1.0] * n2
    for _ in range(max_iter):
        Kb = [sum(K[i][j] * b[j] for j in range(n2)) for i in range(n1)]
        a_next = [p[i] / max(Kb[i], 1e-300) for i in range(n1)]
        KTa = [sum(K[i][j] * a_next[i] for i in range(n1)) for j in range(n2)]
        b_next = [q[j] / max(KTa[j], 1e-300) for j in range(n2)]
        if max(abs(a_next[i] - a[i]) for i in range(n1)) < tol:
            a, b = a_next, b_next
            break
        a, b = a_next, b_next
    return [[a[i] * K[i][j] * b[j] for j in range(n2)] for i in range(n1)]


def mat_mul(A, B):
    m, k, n = len(A), len(B), len(B[0])
    return [[sum(A[i][r] * B[r][j] for r in range(k)) for j in range(n)] for i in range(m)]


def mat_T(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def main():
    # 1. Verify Proposition 1 & Remarks 1-2 (Fast Tensor-Matrix Contraction L(C, C_bar) otimes T):
    C = [
        [0.1, 0.4, 0.9],
        [0.4, 0.2, 0.6],
        [0.9, 0.6, 0.3],
    ]
    C_bar = [
        [0.2, 0.5, 0.8, 1.1],
        [0.5, 0.1, 0.7, 0.4],
        [0.8, 0.7, 0.3, 0.9],
        [1.1, 0.4, 0.9, 0.2],
    ]
    n1, n2 = len(C), len(C_bar)
    p = [0.3, 0.3, 0.4]
    q = [0.25, 0.25, 0.25, 0.25]
    # Valid coupling T in C_{p,q}: outer product p q^T
    T = [[p[i] * q[j] for j in range(n2)] for i in range(n1)]

    # (a) Squared loss L2(a, b) = 0.5 * (a - b)^2 -> f1(a)=0.5*a^2, f2(b)=0.5*b^2, h1(a)=a, h2(b)=b
    naive_l2 = [
        [
            sum(
                0.5 * ((C[i][k] - C_bar[j][l]) ** 2) * T[k][l]
                for k in range(n1)
                for l in range(n2)
            )
            for j in range(n2)
        ]
        for i in range(n1)
    ]
    f1_C_p = [sum(0.5 * (C[i][k] ** 2) * p[k] for k in range(n1)) for i in range(n1)]
    f2_Cbar_q = [sum(0.5 * (C_bar[j][l] ** 2) * q[l] for l in range(n2)) for j in range(n2)]
    h1_T_h2T = mat_mul(mat_mul(C, T), mat_T(C_bar))
    fast_l2 = [
        [f1_C_p[i] + f2_Cbar_q[j] - h1_T_h2T[i][j] for j in range(n2)]
        for i in range(n1)
    ]
    prop1_l2_err = max(abs(naive_l2[i][j] - fast_l2[i][j]) for i in range(n1) for j in range(n2))
    assert prop1_l2_err < 1e-14

    # (b) KL loss KL(a|b) = a log(a/b) - a + b -> f1(a)=a log a - a, f2(b)=b, h1(a)=a, h2(b)=log b
    naive_kl = [
        [
            sum(
                (C[i][k] * math.log(C[i][k] / C_bar[j][l]) - C[i][k] + C_bar[j][l]) * T[k][l]
                for k in range(n1)
                for l in range(n2)
            )
            for j in range(n2)
        ]
        for i in range(n1)
    ]
    f1_kl_p = [
        sum((C[i][k] * math.log(C[i][k]) - C[i][k]) * p[k] for k in range(n1))
        for i in range(n1)
    ]
    f2_kl_q = [sum(C_bar[j][l] * q[l] for l in range(n2)) for j in range(n2)]
    log_Cbar = [[math.log(C_bar[j][l]) for l in range(n2)] for j in range(n2)]
    h1_T_h2T_kl = mat_mul(mat_mul(C, T), mat_T(log_Cbar))
    fast_kl = [
        [f1_kl_p[i] + f2_kl_q[j] - h1_T_h2T_kl[i][j] for j in range(n2)]
        for i in range(n1)
    ]
    prop1_kl_err = max(abs(naive_kl[i][j] - fast_kl[i][j]) for i in range(n1) for j in range(n2))
    assert prop1_kl_err < 1e-14

    # 2. Verify Proposition 2 (Entropic GW Sinkhorn Iteration Eq. 9) on Isometric Permutation:
    # Points x = [0, 1, 3] vs permuted points y = [1, 3, 0] (permutation pi = [1, 2, 0])
    pts1 = [0.0, 1.0, 3.0]
    perm = [1, 2, 0]
    pts2 = [pts1[idx] for idx in perm]
    D1 = [[(pts1[i] - pts1[j]) ** 2 for j in range(3)] for i in range(3)]
    D2 = [[(pts2[i] - pts2[j]) ** 2 for j in range(3)] for i in range(3)]
    p_unif = [1.0 / 3.0] * 3
    # Initialize T near identity + small asymmetry
    T_gw = [
        [1.0 / 9.0 + (0.01 if j == perm.index(i) else -0.005) for j in range(3)]
        for i in range(3)
    ]
    eps_gw = 0.05
    for _ in range(40):
        f1_p = [sum(0.5 * (D1[i][k] ** 2) * p_unif[k] for k in range(3)) for i in range(3)]
        f2_q = [sum(0.5 * (D2[j][l] ** 2) * p_unif[l] for l in range(3)) for j in range(3)]
        cross = mat_mul(mat_mul(D1, T_gw), mat_T(D2))
        cost_gw = [[f1_p[i] + f2_q[j] - cross[i][j] for j in range(3)] for i in range(3)]
        T_gw = sinkhorn_ot(cost_gw, p_unif, p_unif, eps_gw)

    # True isometric coupling maps i=0->j=2, i=1->j=0, i=2->j=1 with mass 1/3 each
    expected_T = [[1.0 / 3.0 if pts1[i] == pts2[j] else 0.0 for j in range(3)] for i in range(3)]
    perm_alignment_err = max(abs(T_gw[i][j] - expected_T[i][j]) for i in range(3) for j in range(3))
    assert perm_alignment_err < 1e-4

    # 3. Verify Propositions 3 & 4 (Closed-form L2 Barycenter Update Eq. 14 preserves PSD cone):
    # Two 2x2 PSD kernel matrices C1, C2 and couplings T1, T2
    C1 = [[2.0, 0.8], [0.8, 1.5]]
    C2 = [[1.2, -0.5], [-0.5, 2.5]]
    p_b = [0.4, 0.6]
    p1 = [0.5, 0.5]
    p2 = [0.3, 0.7]
    T1 = [[0.35, 0.05], [0.15, 0.45]]
    T2 = [[0.25, 0.15], [0.05, 0.55]]
    lam1, lam2 = 0.5, 0.5
    M1 = mat_mul(mat_mul(T1, C1), mat_T(T1))
    M2 = mat_mul(mat_mul(T2, C2), mat_T(T2))
    C_bary_l2 = [
        [(lam1 * M1[i][j] + lam2 * M2[i][j]) / (p_b[i] * p_b[j]) for j in range(2)]
        for i in range(2)
    ]
    # Verify C_bary_l2 is symmetric positive definite (trace > 0 and determinant > 0)
    tr_bary = C_bary_l2[0][0] + C_bary_l2[1][1]
    det_bary = C_bary_l2[0][0] * C_bary_l2[1][1] - C_bary_l2[0][1] * C_bary_l2[1][0]
    assert tr_bary > 0.0 and det_bary > 0.0

    # Verify Proposition 5 (Closed-form KL Barycenter Update Eq. 15 preserves infinitely divisible kernels):
    # For Gaussian kernels K_s = exp(-D_s / sigma^2), U_s = log(K_s) = -D_s / sigma^2 is conditionally PSD on 1^perp
    K1 = [[1.0, math.exp(-1.0)], [math.exp(-1.0), 1.0]]
    K2 = [[1.0, math.exp(-2.0)], [math.exp(-2.0), 1.0]]
    logK1 = [[math.log(K1[i][j]) for j in range(2)] for i in range(2)]
    logK2 = [[math.log(K2[i][j]) for j in range(2)] for i in range(2)]
    L1 = mat_mul(mat_mul(T1, logK1), mat_T(T1))
    L2 = mat_mul(mat_mul(T2, logK2), mat_T(T2))
    C_bary_kl = [
        [math.exp((lam1 * L1[i][j] + lam2 * L2[i][j]) / (p_b[i] * p_b[j])) for j in range(2)]
        for i in range(2)
    ]
    # Check conditional positive semidefiniteness of U = log(C_bary_kl) for x = [1, -1] orthogonal to [1, 1]
    U_kl = [[math.log(C_bary_kl[i][j]) for j in range(2)] for i in range(2)]
    x_orth = [1.0, -1.0]
    cond_psd_val = sum(x_orth[i] * U_kl[i][j] * x_orth[j] for i in range(2) for j in range(2))
    assert cond_psd_val >= -1e-12

    summary = {
        "concept": "EntropicGromovWassersteinDiscrepancyAndBarycenterAveraging",
        "prop1_l2_contraction_err": prop1_l2_err,
        "prop1_kl_contraction_err": prop1_kl_err,
        "prop2_isometric_perm_alignment_err": round(perm_alignment_err, 8),
        "prop4_psd_barycenter_det": round(det_bary, 6),
        "prop5_cond_psd_quadratic_form": round(cond_psd_val, 6),
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
