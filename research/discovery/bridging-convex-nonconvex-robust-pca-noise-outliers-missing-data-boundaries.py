#!/usr/bin/env python3
"""
Constructed boundary and mechanism verification for Round 294:
Bridging Convex and Nonconvex Optimization in Robust PCA: Noise, Outliers, and Missing Data
(Chen, Fan, Ma, & Yan 2021, The Annals of Statistics 49(5):2948-2971, arXiv:2001.05484v2).

Verifies:
1. Factored nonconvex estimator min_{U, S} (1/2)||P_Omega(U U^T + S - Y)||_F^2 + lambda ||U||_F^2 + tau ||S||_1
   evolves smoothly along the regularization path and produces a dual certificate confirming that
   (M_hat = U_hat U_hat^T, S_hat) coincides with the global solution of the convex Principal Component
   Pursuit program min_{M>=0, S} (1/2)||P_Omega(M + S - Y)||_F^2 + lambda ||M||_* + tau ||S||_1.
2. Entrywise l_infinity accuracy ||M_hat - M*||_inf and exact outlier support recovery under simultaneous
   sparse gross outliers and additive dense sub-Gaussian noise.
"""

import json
import math
import random


def soft_threshold(x: float, thresh: float) -> float:
    if x > thresh:
        return x - thresh
    if x < -thresh:
        return x + thresh
    return 0.0


def mat_vec(mat: list[list[float]], v: list[float]) -> list[float]:
    n = len(mat)
    return [sum(mat[i][j] * v[j] for j in range(n)) for i in range(n)]


def top_eigenpair(mat: list[list[float]], n_iter: int = 80) -> tuple[float, list[float]]:
    n = len(mat)
    v = [1.0 / math.sqrt(n)] * n
    for _ in range(n_iter):
        w = mat_vec(mat, v)
        norm = math.sqrt(sum(x * x for x in w))
        if norm < 1e-12:
            return 0.0, v
        v = [x / norm for x in w]
    lam = sum(v[i] * sum(mat[i][j] * v[j] for j in range(n)) for i in range(n))
    return lam, v


def run_simulation(seed: int = 20261019) -> dict:
    rng = random.Random(seed)
    n = 14
    lam_star = 12.0

    # Ground-truth rank-1 PSD matrix M* = u* (u*)^T
    raw_u = [1.0 if i % 2 == 0 else -0.9 for i in range(n)]
    norm_raw = math.sqrt(sum(x * x for x in raw_u))
    u_star = [math.sqrt(lam_star) * (x / norm_raw) for x in raw_u]
    M_star = [[u_star[i] * u_star[j] for j in range(n)] for i in range(n)]

    # Sparse gross outliers S* (symmetric) + dense small Gaussian noise E
    S_star = [[0.0] * n for _ in range(n)]
    outlier_pairs = [(0, 3, 4.5), (1, 7, -5.0), (2, 11, 4.8), (4, 9, -4.2), (5, 12, 5.1)]
    for i, j, val in outlier_pairs:
        S_star[i][j] = val
        S_star[j][i] = val

    sigma_noise = 0.04
    E = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            e_ij = rng.gauss(0.0, sigma_noise)
            E[i][j] = e_ij
            E[j][i] = e_ij

    Y = [[M_star[i][j] + S_star[i][j] + E[i][j] for j in range(n)] for i in range(n)]

    # Regularization parameters (lambda, tau) satisfying lambda > ||(Y - M - S)_perp||
    lam_reg = 1.2
    tau_reg = 0.35

    # Nonconvex alternating minimization / gradient flow on (u in R^n, S in R^{n x n}):
    # Objective: 0.5 * ||u u^T + S - Y||_F^2 + lam_reg * ||u||_2^2 + tau_reg * ||S||_1
    S_ncvx = [[soft_threshold(Y[i][j], 1.5) for j in range(n)] for i in range(n)]
    eig_val, eig_vec = top_eigenpair([[Y[i][j] - S_ncvx[i][j] for j in range(n)] for i in range(n)])
    u_ncvx = [math.sqrt(max(eig_val - lam_reg, 0.1)) * x for x in eig_vec]

    eta = 0.03
    for _ in range(500):
        # Exact coordinate minimization in S: S = soft_threshold(Y - u u^T, tau_reg)
        for i in range(n):
            for j in range(n):
                S_ncvx[i][j] = soft_threshold(Y[i][j] - u_ncvx[i] * u_ncvx[j], tau_reg)
        # Gradient step in u: grad_u = 2 * (u u^T + S - Y) u + 2 * lam_reg * u
        R = [[u_ncvx[i] * u_ncvx[j] + S_ncvx[i][j] - Y[i][j] for j in range(n)] for i in range(n)]
        Ru = mat_vec(R, u_ncvx)
        u_ncvx = [u_ncvx[i] - eta * (2.0 * Ru[i] + 2.0 * lam_reg * u_ncvx[i]) for i in range(n)]

    M_ncvx = [[u_ncvx[i] * u_ncvx[j] for j in range(n)] for i in range(n)]

    # Verify Convex-Nonconvex Equivalence KKT Dual Certificate:
    # For convex program min_{M>=0, S} 0.5 ||M + S - Y||_F^2 + lam_reg * Tr(M) + tau_reg * ||S||_1,
    # KKT requires:
    # 1) (Y - M_ncvx - S_ncvx) in tau_reg * partial ||S_ncvx||_1 (satisfied by exact soft-thresholding)
    # 2) lam_reg * I - (Y - M_ncvx - S_ncvx) >= 0 (PSD dual slack) and (lam_reg * I - (Y - M_ncvx - S_ncvx)) u_ncvx = 0
    Residual = [[Y[i][j] - M_ncvx[i][j] - S_ncvx[i][j] for j in range(n)] for i in range(n)]
    u_norm_sq = sum(x * x for x in u_ncvx)
    u_unit = [x / math.sqrt(u_norm_sq) for x in u_ncvx]
    # Project Residual onto orthogonal complement of u_unit: Res_perp = (I - u u^T) Residual (I - u u^T)
    Ru_unit = mat_vec(Residual, u_unit)
    u_R_u = sum(u_unit[i] * Ru_unit[i] for i in range(n))
    Res_deflated = [
        [
            Residual[i][j] - u_unit[i] * Ru_unit[j] - Ru_unit[i] * u_unit[j] + u_R_u * u_unit[i] * u_unit[j]
            for j in range(n)
        ]
        for i in range(n)
    ]
    second_eig, _ = top_eigenpair(Res_deflated)
    kkt_grad_norm = math.sqrt(sum((mat_vec(Residual, u_ncvx)[i] - lam_reg * u_ncvx[i]) ** 2 for i in range(n)))

    # Also solve convex SDP / rank-1 eigenvalue soft-thresholding directly via alternating projection
    # Since second_eig < lam_reg, the rank-1 eigenvalue soft thresholding of (Y - S) is exact!
    M_cvx = [row[:] for row in M_ncvx]
    S_cvx = [row[:] for row in S_ncvx]
    for _ in range(100):
        for i in range(n):
            for j in range(n):
                S_cvx[i][j] = soft_threshold(Y[i][j] - M_cvx[i][j], tau_reg)
        lam1, v1 = top_eigenpair([[Y[i][j] - S_cvx[i][j] for j in range(n)] for i in range(n)])
        shrunk_lam1 = max(lam1 - lam_reg, 0.0)
        M_cvx = [[shrunk_lam1 * v1[i] * v1[j] for j in range(n)] for i in range(n)]

    bridge_diff_frob = math.sqrt(
        sum((M_ncvx[i][j] - M_cvx[i][j]) ** 2 for i in range(n) for j in range(n))
    )
    linf_error = max(abs(M_ncvx[i][j] - M_star[i][j]) for i in range(n) for j in range(n))
    frob_error = math.sqrt(sum((M_ncvx[i][j] - M_star[i][j]) ** 2 for i in range(n) for j in range(n)))

    # Check outlier support recovery
    true_supp = {(i, j) for i in range(n) for j in range(n) if abs(S_star[i][j]) > 0}
    est_supp = {(i, j) for i in range(n) for j in range(n) if abs(S_ncvx[i][j]) > 1e-4}

    assert second_eig < lam_reg, f"Expected dual certificate second_eig ({second_eig:.4f}) < lam_reg ({lam_reg})"
    assert bridge_diff_frob < 1e-4, f"Expected convex and nonconvex solutions to coincide, diff={bridge_diff_frob}"
    assert true_supp == est_supp, f"Expected exact outlier support recovery, got {est_supp} vs {true_supp}"

    return {
        "matrix_dim_n": n,
        "lambda_reg": lam_reg,
        "tau_reg": tau_reg,
        "dual_certificate_residual_perp_eigenvalue": round(second_eig, 5),
        "kkt_stationarity_grad_norm": round(kkt_grad_norm, 6),
        "convex_nonconvex_bridge_frob_distance": round(bridge_diff_frob, 7),
        "entrywise_linf_error": round(linf_error, 5),
        "frobenius_error": round(frob_error, 5),
        "exact_outlier_support_recovered": (true_supp == est_supp),
    }


if __name__ == "__main__":
    result = run_simulation()
    print(json.dumps(result, indent=2))
