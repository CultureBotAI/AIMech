#!/usr/bin/env python3
"""Constructed boundary and mechanism verification for Round 277:
Decorrelated Score Function and One-Step Estimator for Sparse High-Dimensional Inference
(Ning & Liu 2017, Annals of Statistics 45(1):158-195, DOI:10.1214/16-AOS1448, arXiv:1412.8765v2).
"""

import json
import math
import random


def mat_vec(A, x):
    return [sum(aij * xj for aij, xj in zip(row, x)) for row in A]


def vec_dot(u, v):
    return sum(ui * vi for ui, vi in zip(u, v))


def solve_linear(A, b):
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for k in range(n):
        piv = max(range(k, n), key=lambda i: abs(M[i][k]))
        M[k], M[piv] = M[piv], M[k]
        diag = M[k][k]
        for j in range(k, n + 1):
            M[k][j] /= diag
        for i in range(n):
            if i != k:
                factor = M[i][k]
                if factor != 0.0:
                    for j in range(k, n + 1):
                        M[i][j] -= factor * M[k][j]
    return [M[i][n] for i in range(n)]


def soft_threshold(z, lam):
    if z > lam:
        return z - lam
    if z < -lam:
        return z + lam
    return 0.0


def solve_weighted_lasso(X, y, weights, lam, max_iter=300, tol=1e-9):
    """Minimize (1/(2n)) sum_i w_i (y_i - x_i^T b)^2 + lam ||b||_1 via coordinate descent."""
    n = len(y)
    p = len(X[0])
    b = [0.0] * p
    r = y[:]
    col_sq = [
        sum(weights[i] * X[i][j] * X[i][j] for i in range(n)) / n for j in range(p)
    ]
    for _ in range(max_iter):
        max_diff = 0.0
        for j in range(p):
            if col_sq[j] < 1e-14:
                continue
            old_bj = b[j]
            rho = (
                sum(weights[i] * X[i][j] * r[i] for i in range(n)) / n
                + col_sq[j] * old_bj
            )
            new_bj = soft_threshold(rho, lam) / col_sq[j]
            diff = new_bj - old_bj
            if abs(diff) > 1e-15:
                for i in range(n):
                    r[i] -= X[i][j] * diff
                b[j] = new_bj
                if abs(diff) > max_diff:
                    max_diff = abs(diff)
        if max_diff < tol:
            break
    return b


def verify_hilbert_projection_and_taylor_product():
    """Verify population score decorrelation (Eq. 2.4) and partial Fisher information identity."""
    d = 8
    rho = 0.6
    # Toeplitz Fisher information I^*
    I_star = [[rho ** abs(j - k) for k in range(d)] for j in range(d)]
    I_tt = I_star[0][0]
    I_tg = I_star[0][1:]
    I_gg = [row[1:] for row in I_star[1:]]

    # w^* = (I^*_{gg})^{-1} I^*_{g,theta}
    w_star = solve_linear(I_gg, I_tg)
    # Check orthogonality: I_{\gamma\theta} - I_{\gamma\gamma} w^* = 0
    orth_residual = [
        I_tg[j] - sum(I_gg[j][k] * w_star[k] for k in range(d - 1))
        for j in range(d - 1)
    ]
    max_orth_err = max(abs(x) for x in orth_residual)

    # Partial information I^*_{\theta|\gamma} = I_{\theta\theta} - w^{*T} I_{\gamma\theta}
    I_partial = I_tt - vec_dot(w_star, I_tg)
    # Closed-form AR(1)/Toeplitz inverse (1,1) entry is 1 / (1 - rho^2) => partial info = 1 - rho^2
    exact_partial = 1.0 - rho * rho
    # Also check quadratic form (1, -w^{*T}) I^* (1, -w^{*T})^T
    v_star = [1.0] + [-wj for wj in w_star]
    quad_var = vec_dot(v_star, mat_vec(I_star, v_star))

    assert max_orth_err < 1e-14, f"Orthogonality failed: {max_orth_err}"
    assert abs(I_partial - exact_partial) < 1e-14
    assert abs(quad_var - I_partial) < 1e-14

    return {
        "d": d,
        "rho": rho,
        "w_star_first3": [round(w_star[0], 6), round(w_star[1], 6), round(w_star[2], 6)],
        "max_orthogonality_error": max_orth_err,
        "partial_information_I_theta_given_gamma": round(I_partial, 6),
        "quadratic_score_variance": round(quad_var, 6),
    }


def verify_linear_and_glm_decorrelated_score():
    """Verify Algorithm 1, Eq. 2.9 one-step estimator equivalence, and logistic GLM Eq. 5.2."""
    rng = random.Random(20261019)
    n = 180
    d = 45
    rho = 0.6

    # Generate AR(1) / Toeplitz Gaussian covariates Q_i = (Z_i, X_i^T)^T
    Q = []
    for _ in range(n):
        row = [0.0] * d
        row[0] = rng.gauss(0.0, 1.0)
        scale = math.sqrt(1.0 - rho * rho)
        for j in range(1, d):
            row[j] = rho * row[j - 1] + scale * rng.gauss(0.0, 1.0)
        Q.append(row)

    Z = [row[0] for row in Q]
    X = [row[1:] for row in Q]

    # True parameter under H_0: theta^* = 0.0, and active nuisance gamma^* = (1.2, 1.0, 0.8, 0, ...)
    theta_true = 0.5
    gamma_true = [1.2, 1.0, 0.8] + [0.0] * (d - 4)
    beta_true = [theta_true] + gamma_true

    # 1. Linear model with theta^* = 0.5 (and also evaluate score at theta = 0.5 vs naive plug-in)
    sigma = 1.0
    eps = [rng.gauss(0.0, sigma) for _ in range(n)]
    Y = [vec_dot(Q[i], beta_true) + eps[i] for i in range(n)]

    lam = 1.6 * math.sqrt(math.log(d) / n)
    lam_w = 1.4 * math.sqrt(math.log(d) / n)
    ones = [1.0] * n

    beta_hat = solve_weighted_lasso(Q, Y, ones, lam)
    theta_hat = beta_hat[0]
    gamma_hat = beta_hat[1:]

    # Estimate w via Lasso projection (Eq. 2.7 / Eq. 4.5)
    w_tilde = solve_weighted_lasso(X, Z, ones, lam_w)

    # Naive score at true theta_true = 0.5 using gamma_hat:
    # S_naive(theta_true, gamma_hat) = -(1/n) sum_i (Y_i - theta_true Z_i - X_i^T gamma_hat) Z_i
    s_naive = -sum(
        (Y[i] - theta_true * Z[i] - vec_dot(X[i], gamma_hat)) * Z[i] for i in range(n)
    ) / n

    # Decorrelated score at theta_true = 0.5:
    # S_hat(theta_true, gamma_hat) = -(1/n) sum_i (Y_i - theta_true Z_i - X_i^T gamma_hat)(Z_i - X_i^T w_tilde)
    z_res = [Z[i] - vec_dot(X[i], w_tilde) for i in range(n)]
    s_decorr_at_true = -sum(
        (Y[i] - theta_true * Z[i] - vec_dot(X[i], gamma_hat)) * z_res[i]
        for i in range(n)
    ) / n

    # Evaluate S_hat(beta_hat) at beta_hat = (theta_hat, gamma_hat):
    s_hat_at_betahat = -sum(
        (Y[i] - theta_hat * Z[i] - vec_dot(X[i], gamma_hat)) * z_res[i]
        for i in range(n)
    ) / n
    I_hat_partial = sum(Z[i] * z_res[i] for i in range(n)) / n

    # One-step estimator Eq. (2.9): theta_tilde = theta_hat - S_hat(beta_hat) / I_hat_{theta|gamma}
    theta_onestep_eq29 = theta_hat - s_hat_at_betahat / I_hat_partial

    # Exact root of S_hat(theta, gamma_hat) = 0 (Section 4.1 page 18):
    theta_exact_root = sum(
        (Y[i] - vec_dot(X[i], gamma_hat)) * z_res[i] for i in range(n)
    ) / sum(Z[i] * z_res[i] for i in range(n))

    linear_root_diff = abs(theta_onestep_eq29 - theta_exact_root)
    assert linear_root_diff < 1e-14, f"One-step vs root diff: {linear_root_diff}"

    # Estimate sigma_hat^2 (Section 4.3)
    sigma_hat_sq = sum((Y[i] - vec_dot(Q[i], beta_hat)) ** 2 for i in range(n)) / n
    se_onestep = math.sqrt(sigma_hat_sq / (n * I_hat_partial))
    ci_95 = [
        theta_onestep_eq29 - 1.95996 * se_onestep,
        theta_onestep_eq29 + 1.95996 * se_onestep,
    ]
    covers_true = ci_95[0] <= theta_true <= ci_95[1]

    # Verify that decorrelated score eliminates regularization bias relative to naive score
    assert abs(theta_onestep_eq29 - theta_true) < abs(theta_hat - theta_true)
    assert abs(s_decorr_at_true) < abs(s_naive) * 0.35
    assert covers_true

    # 2. Logistic GLM verification (Section 5, Eq. 5.2) under H_0: theta^* = 0
    rng_glm = random.Random(20261020)
    gamma_glm = [1.0, 0.8, -0.6] + [0.0] * (d - 4)
    Y_glm = []
    for i in range(n):
        eta = vec_dot(X[i], gamma_glm)
        prob = 1.0 / (1.0 + math.exp(-eta))
        Y_glm.append(1.0 if rng_glm.random() < prob else 0.0)

    # Fit penalized logistic regression via IRLS + weighted Lasso under H_0 (nuisance gamma)
    gamma_hat_glm = [0.0] * (d - 1)
    lam_glm = 0.25 * math.sqrt(math.log(d) / n)
    for _ in range(12):
        w_irls = []
        z_working = []
        for i in range(n):
            eta = max(-8.0, min(8.0, vec_dot(X[i], gamma_hat_glm)))
            mu = 1.0 / (1.0 + math.exp(-eta))
            wi = max(1e-4, mu * (1.0 - mu))
            w_irls.append(wi)
            z_working.append(eta + (Y_glm[i] - mu) / wi)
        gamma_hat_glm = solve_weighted_lasso(X, z_working, w_irls, lam_glm)

    # Compute b''(Q_i^T beta_hat) = mu_i(1 - mu_i) at (0, gamma_hat_glm)
    b_dd = []
    mu_hat = []
    for i in range(n):
        eta = max(-8.0, min(8.0, vec_dot(X[i], gamma_hat_glm)))
        mu = 1.0 / (1.0 + math.exp(-eta))
        mu_hat.append(mu)
        b_dd.append(mu * (1.0 - mu))

    # Weighted Lasso estimator w_tilde in Eq. (5.2)
    w_tilde_glm = solve_weighted_lasso(X, Z, b_dd, lam_glm)
    s_hat_glm = -sum(
        (Y_glm[i] - mu_hat[i]) * (Z[i] - vec_dot(X[i], w_tilde_glm)) for i in range(n)
    ) / n
    I_hat_glm = sum(
        b_dd[i] * Z[i] * (Z[i] - vec_dot(X[i], w_tilde_glm)) for i in range(n)
    ) / n
    U_hat_glm = math.sqrt(n) * s_hat_glm / math.sqrt(I_hat_glm)
    s_naive_glm = -sum((Y_glm[i] - mu_hat[i]) * Z[i] for i in range(n)) / n
    U_naive_glm = math.sqrt(n) * s_naive_glm / math.sqrt(
        sum(b_dd[i] * Z[i] * Z[i] for i in range(n)) / n
    )

    assert abs(U_hat_glm) < 1.96, f"GLM decorrelated score rejected true H0: {U_hat_glm}"
    assert abs(U_hat_glm) < abs(U_naive_glm)

    return {
        "n": n,
        "d": d,
        "theta_true": theta_true,
        "theta_lasso_biased": round(theta_hat, 6),
        "theta_onestep_eq29": round(theta_onestep_eq29, 6),
        "theta_exact_root": round(theta_exact_root, 6),
        "onestep_vs_exact_root_diff": linear_root_diff,
        "naive_score_at_true_theta": round(s_naive, 6),
        "decorrelated_score_at_true_theta": round(s_decorr_at_true, 6),
        "ci_95_onestep": [round(ci_95[0], 6), round(ci_95[1], 6)],
        "covers_true_theta": covers_true,
        "glm_U_hat_under_H0": round(U_hat_glm, 6),
        "glm_U_naive_under_H0": round(U_naive_glm, 6),
    }


def verify_misspecification_and_multiplier_bootstrap():
    """Verify Section 6.1 multiplier bootstrap and Section 6.2 sandwich variance under misspecification."""
    rng = random.Random(20261021)
    n = 200
    d0 = 4
    d1 = 26
    d = d0 + d1
    rho = 0.5

    # Generate covariates Q_i = (Z_{i,1..d0}, X_{i,1..d1})
    Q = []
    for _ in range(n):
        row = [0.0] * d
        row[0] = rng.gauss(0.0, 1.0)
        scale = math.sqrt(1.0 - rho * rho)
        for j in range(1, d):
            row[j] = rho * row[j - 1] + scale * rng.gauss(0.0, 1.0)
        Q.append(row)

    Z = [row[:d0] for row in Q]
    X = [row[d0:] for row in Q]
    gamma_true = [1.0, -0.8, 0.6] + [0.0] * (d1 - 3)

    # Heteroscedastic / misspecified noise: eps_i = (1 + 1.2 * Z_{i,0}^2) * N(0,1)
    # Under H_0^o: theta^o = 0, E^*[eps_i | Q_i] = 0, so oracle parameter has theta^o = 0,
    # but E^*[eps_i^2 Z_{i,0}^2] != sigma^2 E^*[Z_{i,0}^2] (Bartlett identity fails!).
    Y = [
        vec_dot(X[i], gamma_true) + (1.0 + 0.9 * Z[i][0] * Z[i][0]) * rng.gauss(0.0, 1.0)
        for i in range(n)
    ]

    ones = [1.0] * n
    lam = 1.5 * math.sqrt(math.log(d) / n)
    gamma_hat = solve_weighted_lasso(X, Y, ones, lam)

    # Estimate W_{*j} for j = 1..d0 via column-wise projection (Section 6.1 Eq. 6.1)
    W_hat = []
    for j in range(d0):
        zj_col = [Z[i][j] for i in range(n)]
        wj = solve_weighted_lasso(X, zj_col, ones, lam)
        W_hat.append(wj)

    # Compute individual decorrelated score vectors S_hat_{i,j} = -(Y_i - X_i^T gamma_hat)(Z_{ij} - X_i^T W_{*j})
    S_mat = []
    for i in range(n):
        res_y = Y[i] - vec_dot(X[i], gamma_hat)
        row_s = [
            -res_y * (Z[i][j] - vec_dot(X[i], W_hat[j])) for j in range(d0)
        ]
        S_mat.append(row_s)

    T_hat = [
        math.sqrt(n) * sum(S_mat[i][j] for i in range(n)) / n for j in range(d0)
    ]
    T_inf = max(abs(t) for t in T_hat)

    # Multiplier bootstrap critical value c'_N(0.95) with B = 400 draws (Eq. 6.2)
    B = 400
    boot_maxima = []
    for _ in range(B):
        e = [rng.gauss(0.0, 1.0) for _ in range(n)]
        ne = [
            sum(e[i] * S_mat[i][j] for i in range(n)) / math.sqrt(n)
            for j in range(d0)
        ]
        boot_maxima.append(max(abs(val) for val in ne))
    boot_maxima.sort()
    c_prime_95 = boot_maxima[int(0.95 * B)]

    # Section 6.2: Compare sandwich variance v_hat^T Sigma_hat v_hat vs homoscedastic sigma_hat^2 I_hat_{theta|gamma}
    # For coordinate j=0:
    sandwich_var_0 = sum(S_mat[i][0] * S_mat[i][0] for i in range(n)) / n
    sigma_hat_sq = sum((Y[i] - vec_dot(X[i], gamma_hat)) ** 2 for i in range(n)) / n
    I_hat_0 = sum(
        Z[i][0] * (Z[i][0] - vec_dot(X[i], W_hat[0])) for i in range(n)
    ) / n
    homoscedastic_var_0 = sigma_hat_sq * I_hat_0

    assert T_inf <= c_prime_95, f"Multiplier bootstrap rejected true H0: {T_inf} > {c_prime_95}"
    assert sandwich_var_0 > 1.8 * homoscedastic_var_0, (
        "Sandwich variance should exceed naive homoscedastic variance under heavy heteroscedasticity"
    )

    return {
        "n": n,
        "d0": d0,
        "d1": d1,
        "T_hat_sup_norm": round(T_inf, 6),
        "multiplier_bootstrap_c95": round(c_prime_95, 6),
        "bootstrap_accepts_true_H0": T_inf <= c_prime_95,
        "misspecified_sandwich_variance_coord0": round(sandwich_var_0, 6),
        "naive_homoscedastic_variance_coord0": round(homoscedastic_var_0, 6),
        "variance_ratio_sandwich_to_naive": round(
            sandwich_var_0 / homoscedastic_var_0, 4
        ),
    }


def main():
    res1 = verify_hilbert_projection_and_taylor_product()
    res2 = verify_linear_and_glm_decorrelated_score()
    res3 = verify_misspecification_and_multiplier_bootstrap()
    out = {
        "concept": "AIMech:DecorrelatedScoreFunctionAndOneStepEstimatorForSparseHighDimensionalInference",
        "source": "Ning & Liu (2017), Annals of Statistics 45(1):158-195, arXiv:1412.8765v2",
        "hilbert_projection_and_partial_information": res1,
        "linear_and_glm_decorrelated_score": res2,
        "misspecification_and_multiplier_bootstrap": res3,
        "all_assertions_passed": True,
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
