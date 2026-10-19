#!/usr/bin/env python3
"""Boundary and verification script for Round 341:
Regularized Nonlinear Acceleration (RNA)
(Scieur, d'Aspremont, & Bach, NeurIPS 2016 pp. 712-720, arXiv:1606.04133v3; Mathematical Programming 2020).
"""

import math
import sys


def matmul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][r] * B[r][j] for r in range(k)) for j in range(n)] for i in range(m)]


def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def vec_norm(v):
    return math.sqrt(sum(x * x for x in v))


def solve_linear(A, b):
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for i in range(n):
        piv = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[piv] = M[piv], M[i]
        diag = M[i][i]
        for c in range(i, n + 1):
            M[i][c] /= diag
        for r in range(n):
            if r != i:
                f = M[r][i]
                for c in range(i, n + 1):
                    M[r][c] -= f * M[i][c]
    return [M[i][n] for i in range(n)]


def spectral_norm_sym(S):
    n = len(S)
    A = [row[:] for row in S]
    for _ in range(60):
        p, q = 0, 1
        mx = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i][j]) > mx:
                    mx = abs(A[i][j])
                    p, q = i, j
        if mx < 1e-15:
            break
        phi = (A[q][q] - A[p][p]) / (2.0 * A[p][q])
        t = 1.0 / (abs(phi) + math.sqrt(phi * phi + 1.0))
        if phi < 0:
            t = -t
        c = 1.0 / math.sqrt(1.0 + t * t)
        s = t * c
        tau = s / (1.0 + c)
        h = t * A[p][q]
        A[p][p] -= h
        A[q][q] += h
        A[p][q] = A[q][p] = 0.0
        for r in range(n):
            if r != p and r != q:
                arp, arq = A[r][p], A[r][q]
                A[r][p] = A[p][r] = arp - s * (arq + tau * arp)
                A[r][q] = A[q][r] = arq + s * (arp - tau * arq)
    return max(abs(A[i][i]) for i in range(n))


def rna_weights(R_cols, lam):
    """Algorithm 2 & Proposition 3.2 (Equation 22, p. 9):
    Solve (R^T R + lam I) z = 1, return c_lam^* = z / (1^T z).
    """
    k_plus_1 = len(R_cols)
    d = len(R_cols[0])
    G = [
        [
            sum(R_cols[i][r] * R_cols[j][r] for r in range(d)) + (lam if i == j else 0.0)
            for j in range(k_plus_1)
        ]
        for i in range(k_plus_1)
    ]
    z = solve_linear(G, [1.0] * k_plus_1)
    s = sum(z)
    return [zi / s for zi in z], G


def main():
    # 1. Verify Proposition 2.1, Corollary 2.2, Proposition 2.3, and Proposition 2.4 (pp. 3-7):
    # Linear fixed-point iteration x_{i+1} - x* = G(x_i - x*) with m=4 distinct eigenvalues in [0, sigma]
    eigs_G = [0.1, 0.4, 0.7, 0.9]
    sigma = max(eigs_G)  # = 0.9, so mu/L = 0.1
    beta = (1.0 - math.sqrt(1.0 - sigma)) / (1.0 + math.sqrt(1.0 - sigma))
    x0 = [2.0, -1.5, 1.2, -3.0]
    x0_norm = vec_norm(x0)

    # Generate k+2 iterates for k=3 < m=4 and k=4 == m=4
    X_lin = [x0[:]]
    for _ in range(6):
        prev = X_lin[-1]
        X_lin.append([eigs_G[j] * prev[j] for j in range(4)])
    R_lin = [[X_lin[i + 1][j] - X_lin[i][j] for j in range(4)] for i in range(5)]

    # For k = 3 < m = 4 (4 residuals r_0..r_3): verify Proposition 2.3 & Equation 40 Chebyshev bound
    c_k3, _ = rna_weights(R_lin[:4], 0.0)
    x_extr_k3 = [sum(c_k3[i] * X_lin[i][j] for i in range(4)) for j in range(4)]
    err_k3 = vec_norm(x_extr_k3)
    cheb_bound_k3 = (1.0 / (1.0 - sigma)) * ((2.0 * (beta ** 3)) / (1.0 + (beta ** 6))) * x0_norm

    # For k = 4 == m = 4 (5 residuals r_0..r_4): by Cayley-Hamilton (Proposition 2.1 Eq. 5), exact zero error!
    c_k4, _ = rna_weights(R_lin[:5], 1e-16)
    x_extr_k4 = [sum(c_k4[i] * X_lin[i][j] for i in range(5)) for j in range(4)]
    err_k4_cayley_hamilton = vec_norm(x_extr_k4)

    # 2. Verify Proposition 3.2 (Equations 20-23, pp. 9-10) under Perturbed LFPI:
    # Generate perturbed sequence x_tilde_{i+1} = G x_tilde_i + e_i
    X_pert = [x0[:]]
    for i in range(5):
        prev = X_pert[-1]
        noise = [0.02 * math.sin(1.7 * (i + 1) + j) for j in range(4)]
        X_pert.append([eigs_G[j] * prev[j] + noise[j] for j in range(4)])
    R_pert = [[X_pert[i + 1][j] - X_pert[i][j] for j in range(4)] for i in range(4)]

    lam = 0.05
    c_lam_clean, G_clean = rna_weights(R_lin[:4], lam)
    c_lam_pert, G_pert = rna_weights(R_pert, lam)

    # Perturbation matrix P = R_tilde^T R_tilde - R^T R (Equation 17)
    P_mat = [[G_pert[i][j] - G_clean[i][j] for j in range(4)] for i in range(4)]
    norm_P = spectral_norm_sym(P_mat)
    norm_R_tilde_sq = spectral_norm_sym([[G_pert[i][j] - (lam if i == j else 0.0) for j in range(4)] for i in range(4)])

    # Verify Exact Perturbation Identity (Equation 23, p. 9):
    Pc = [sum(P_mat[i][j] * c_lam_clean[j] for j in range(4)) for i in range(4)]
    Ginv_Pc = solve_linear(G_pert, Pc)
    Ginv_1 = solve_linear(G_pert, [1.0] * 4)
    denom_1 = sum(Ginv_1)
    sum_Ginv_Pc = sum(Ginv_Pc)
    delta_c_formula = [-(Ginv_Pc[i] - Ginv_1[i] * (sum_Ginv_Pc / denom_1)) for i in range(4)]
    delta_c_actual = [c_lam_pert[i] - c_lam_clean[i] for i in range(4)]
    eq23_err = vec_norm([delta_c_actual[i] - delta_c_formula[i] for i in range(4)])

    # Verify Stability Bounds (Equations 20 and 21, p. 9):
    bound_eq20 = math.sqrt((lam + norm_R_tilde_sq) / (4.0 * lam))
    bound_eq21 = (norm_P / lam) * vec_norm(c_lam_clean)
    eq20_holds = vec_norm(c_lam_pert) <= bound_eq20 + 1e-14
    eq21_holds = vec_norm(delta_c_actual) <= bound_eq21 + 1e-14

    # 3. Verify Proposition A.1 (Equation 41, Appendix A.1, p. 28):
    # max_{x in [0, sqrt(a/lam)]} (kappa * sqrt(a - lam * x^2) + b * x) == sqrt(a) * sqrt(kappa^2 + b^2 / lam)
    a_val, b_val, kap_val = 2.3, 0.7, 1.8
    x_opt = (b_val * math.sqrt(a_val)) / math.sqrt((lam ** 2) * (kap_val ** 2) + lam * (b_val ** 2))
    f_at_opt = kap_val * math.sqrt(a_val - lam * (x_opt ** 2)) + b_val * x_opt
    f_closed = math.sqrt(a_val) * math.sqrt(kap_val ** 2 + (b_val ** 2) / lam)
    prop_a1_err = abs(f_at_opt - f_closed)

    # 4. Verify Krylov Ill-Conditioning Failure Boundary of Unregularized Acceleration (Section 3.1, p. 8):
    # At k = 4 (5 residuals, where noiseless R^T R has rank 4 and is singular!),
    # unregularized extrapolation on noisy iterates amplifies ||c^*||_2, whereas RNA stabilizes ||c_lam^*||_2.
    R_pert_5 = [[X_pert[i + 1][j] - X_pert[i][j] for j in range(4)] for i in range(5)]
    c_unreg_5, _ = rna_weights(R_pert_5, 1e-12)
    c_reg_5, _ = rna_weights(R_pert_5, 1e-1)

    ok = (
        err_k3 <= cheb_bound_k3 + 1e-12
        and err_k4_cayley_hamilton < 1e-5
        and eq23_err < 1e-13
        and eq20_holds
        and eq21_holds
        and prop_a1_err < 1e-15
        and vec_norm(c_unreg_5) > 5.0 * vec_norm(c_reg_5)
    )
    if not ok:
        print(
            f"Verification failed: err_k3={err_k3} <= {cheb_bound_k3}, err_k4={err_k4_cayley_hamilton}, "
            f"eq23={eq23_err}, eq20={eq20_holds} ({vec_norm(c_lam_pert)} vs {bound_eq20}), "
            f"eq21={eq21_holds} ({vec_norm(delta_c_actual)} vs {bound_eq21}), "
            f"prop_a1={prop_a1_err}, c_unreg={vec_norm(c_unreg_5)} vs c_reg={vec_norm(c_reg_5)}",
            file=sys.stderr,
        )
        sys.exit(1)

    print(
        f"[PASS] Round 341 Regularized Nonlinear Acceleration (Scieur, d'Aspremont, & Bach 2016): "
        f"err_k3={err_k3:.4e} <= {cheb_bound_k3:.4e}, err_k4_CH={err_k4_cayley_hamilton:.2e}, "
        f"eq23_err={eq23_err:.2e}, prop_a1_err={prop_a1_err:.2e}, "
        f"norm_c_unreg={vec_norm(c_unreg_5):.2f} vs norm_c_reg={vec_norm(c_reg_5):.2f}"
    )


if __name__ == "__main__":
    main()
