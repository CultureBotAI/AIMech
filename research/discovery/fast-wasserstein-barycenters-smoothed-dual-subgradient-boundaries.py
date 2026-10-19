#!/usr/bin/env python3
"""Boundary and regime verification for Cuturi & Doucet (2014)
Fast Computation of Wasserstein Barycenters (ICML 2014 / arXiv:1310.4375v3).
"""

import json
import math


def algorithm3_smoothed_primal_dual(M, lam, a, b, max_iter=500, tol=1e-14):
    """Algorithm 3 (p. 7) & Proposition 2 (p. 6): Smoothed Primal T_lam^* and Dual alpha_lam^*."""
    n = len(a)
    m = len(b)
    K = [[math.exp(-lam * M[i][j]) for j in range(m)] for i in range(n)]
    K_tilde = [[K[i][j] / a[i] for j in range(m)] for i in range(n)]
    u = [1.0 / n] * n
    for _ in range(max_iter):
        KT_u = [sum(K[i][j] * u[i] for i in range(n)) for j in range(m)]
        b_div = [b[j] / KT_u[j] for j in range(m)]
        denom = [sum(K_tilde[i][j] * b_div[j] for j in range(m)) for i in range(n)]
        u_next = [1.0 / denom[i] for i in range(n)]
        if max(abs(u_next[i] - u[i]) for i in range(n)) < tol:
            u = u_next
            break
        u = u_next
    KT_u = [sum(K[i][j] * u[i] for i in range(n)) for j in range(m)]
    v = [b[j] / KT_u[j] for j in range(m)]
    T_star = [[u[i] * K[i][j] * v[j] for j in range(m)] for i in range(n)]
    log_u = [math.log(u[i]) for i in range(n)]
    mean_log_u = sum(log_u) / n
    # By Proposition 2 (Eq. 9-10): T^* = diag(e^{lam * alpha^*}) K diag(e^{lam * beta^*}) = diag(u) K diag(v),
    # so alpha^* = +(log(u) - mean(log(u)) * 1_n) / lam is the zero-sum tangent gradient of p_lam(a, b; M).
    alpha_star = [(log_u[i] - mean_log_u) / lam for i in range(n)]

    # Smoothed primal objective p_lam(a, b; M) = <T^*, M> - (1/lam) h(T^*)
    # Note: In Cuturi & Doucet (2014, Sec. 5.1, p. 6) and Cuturi (2013),
    # d_lam(a, b; M) = alpha^T a + beta^T b - sum_{i,j} exp(-lam(m_{ij} - alpha_i - beta_j)) / lam
    # where beta_j = -log(v_j)/lam - const, corresponding to entropy penalty -sum T_{ij} (log T_{ij} - 1)/lam.
    p_val = 0.0
    for i in range(n):
        for j in range(m):
            t_ij = T_star[i][j]
            if t_ij > 0:
                p_val += t_ij * M[i][j] + (1.0 / lam) * t_ij * (math.log(t_ij) - 1.0)
    return T_star, alpha_star, p_val


def main():
    # 1. Verify Proposition 2 & Algorithm 3: Smoothed dual optimum alpha_lam^* is the exact
    # zero-sum tangent gradient of p_lam(a, b; M) with respect to a.
    grid = [0.0, 1.0, 2.0, 3.0, 4.0]
    n = len(grid)
    M = [[(grid[i] - grid[j]) ** 2 for j in range(n)] for i in range(n)]
    a0 = [0.15, 0.25, 0.20, 0.25, 0.15]
    b0 = [0.30, 0.10, 0.20, 0.10, 0.30]
    lam = 3.0

    T_star, alpha_star, _ = algorithm3_smoothed_primal_dual(M, lam, a0, b0)
    row_err = max(abs(sum(T_star[i]) - a0[i]) for i in range(n))
    col_err = max(abs(sum(T_star[i][j] for i in range(n)) - b0[j]) for j in range(n))
    assert row_err < 1e-12
    assert col_err < 1e-12
    assert abs(sum(alpha_star)) < 1e-14

    # Finite-difference check along tangent directions e_i - (1/n) 1_n on the simplex
    eps = 1e-7
    fd_grad = []
    for i in range(n):
        a_plus = [a0[k] + (eps if k == i else 0.0) - eps / n for k in range(n)]
        a_minus = [a0[k] - (eps if k == i else 0.0) + eps / n for k in range(n)]
        _, _, p_plus = algorithm3_smoothed_primal_dual(M, lam, a_plus, b0)
        _, _, p_minus = algorithm3_smoothed_primal_dual(M, lam, a_minus, b0)
        fd_grad.append((p_plus - p_minus) / (2.0 * eps))
    grad_err = max(abs(fd_grad[i] - alpha_star[i]) for i in range(n))
    assert grad_err < 1e-6

    # 2. Verify Algorithm 1 (Fixed-Support Wasserstein Barycenter via Entropic Mirror Descent):
    # Target measures nu_1 concentrated near x=0 and nu_2 concentrated near x=4.
    b1 = [0.92, 0.05, 0.01, 0.01, 0.01]
    b2 = [0.01, 0.01, 0.01, 0.05, 0.92]
    targets = [b1, b2]

    # Euclidean / L2 mean histogram simply averages bin weights (bimodal at x=0 and x=4, 0.01 at midpoint x=2)
    eucl_mean = [0.5 * (b1[i] + b2[i]) for i in range(n)]
    assert abs(eucl_mean[2] - 0.01) < 1e-12

    # Run Algorithm 1 (Sec. 4.2, p. 5) with smoothed dual gradients (Sec. 5.2, p. 7)
    a_tilde = [1.0 / n] * n
    a_hat = list(a_tilde)
    lam_bary = 5.0
    t0 = 0.5
    for t in range(1, 80):
        beta = (t + 1.0) / 2.0
        a_curr = [(1.0 - 1.0 / beta) * a_hat[i] + (1.0 / beta) * a_tilde[i] for i in range(n)]
        alphas = [algorithm3_smoothed_primal_dual(M, lam_bary, a_curr, b_k)[1] for b_k in targets]
        alpha_bar = [sum(alphas[k][i] for k in range(len(targets))) / len(targets) for i in range(n)]
        # KL proximal update on simplex: a_tilde <- a_tilde o exp(-t0 * beta * alpha_bar)
        step = t0 * 1.5
        unnorm = [a_tilde[i] * math.exp(-step * alpha_bar[i]) for i in range(n)]
        s_unnorm = sum(unnorm)
        a_tilde = [u / s_unnorm for u in unnorm]
        a_hat = [(1.0 - 1.0 / beta) * a_hat[i] + (1.0 / beta) * a_tilde[i] for i in range(n)]

    # Verify the 2-Wasserstein barycenter places its dominant mode at the geometric midpoint x_2 = 2.0
    assert a_hat[2] > 0.75
    assert a_hat[2] > max(a_hat[0], a_hat[1], a_hat[3], a_hat[4])

    # 3. Verify Section 4.3 Eq. (8) & Algorithm 2 (Free-Support Newton Update):
    # X <- (1/N) sum_{i=1}^N Y_i (T_i^*)^T diag(a^{-1})
    Y1 = [-2.0, 0.0]
    Y2 = [2.0, 4.0]
    a_free = [0.5, 0.5]
    # Optimal transport from X to Y1 and Y2 matches atom 0 -> atom 0 and atom 1 -> atom 1 with mass 0.5
    T1_opt = [[0.5, 0.0], [0.0, 0.5]]
    T2_opt = [[0.5, 0.0], [0.0, 0.5]]
    X_newton = [
        0.5 * (sum(Y1[j] * T1_opt[k][j] for j in range(2)) + sum(Y2[j] * T2_opt[k][j] for j in range(2))) / a_free[k]
        for k in range(2)
    ]
    assert abs(X_newton[0] - 0.0) < 1e-12
    assert abs(X_newton[1] - 2.0) < 1e-12

    summary = {
        "concept": "FastWassersteinBarycentersAndSmoothedDualSubgradientDescent",
        "prop2_dual_tangent_grad_err": round(grad_err, 9),
        "marginal_feasibility_err": max(row_err, col_err),
        "wasserstein_barycenter_midpoint_mass": round(a_hat[2], 6),
        "euclidean_mean_midpoint_mass": round(eucl_mean[2], 6),
        "free_support_newton_locations": X_newton,
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
