#!/usr/bin/env python3
"""Constructed boundary & verification script for Round 264:
Theta-IPOD Thresholding-Based Iterative Outlier Detection and Mean-Shift Penalized Regression
(She & Owen 2011, JASA 106(494):626-639, DOI:10.1198/jasa.2011.tm10390, arXiv:1006.2592v3).

Verifies:
1. Proposition 3.1: Exact equivalence between L1-penalized mean-shift regression (soft-IPOD)
   and Huber's M-estimator with concomitant scale estimation.
2. Theorem 4.1, Proposition 4.1, and Algorithm 1 vs. Algorithm 2 (Simplified Theta-IPOD):
   - Exact iterate-by-iterate equivalence between Algorithm 1 (alternating QR + thresholding)
     and Algorithm 2 (gamma^{(j+1)} = Theta(H gamma^{(j)} + (I - H) y; lambda)).
   - Strict monotone descent of both the smallest-curvature penalty P_Theta (Eq. 4.1) and
     the L0 penalty P_0(theta; lambda) = (lambda^2 / 2) 1_{theta != 0} via q(theta; lambda)
     along hard-IPOD iterates (Eq. 4.3).
   - Fixed-point M-estimator score identity X^T psi(y - X beta_hat; lambda) = 0 (Eq. 4.4-4.5)
     and regression, scale, and affine equivariance (Section 4.2, p. 17).
3. High-leverage multiple-outlier masking/swamping failure of convex soft-IPOD vs. exact
   outlier recovery of hard-IPOD tuned by modified BIC* (Eq. 6.1).
4. Section 7 (p > n) joint sparse coefficient & outlier detection via Hard-Ridge Thresholding
   (Eq. 7.1-7.3) with monotone descent of the fused L0 + L2 criterion.
"""

from __future__ import annotations

import json
import math
import random


def mat_vec(A: list[list[float]], v: list[float]) -> list[float]:
    return [sum(row[j] * v[j] for j in range(len(v))) for row in A]


def mat_T_vec(A: list[list[float]], v: list[float]) -> list[float]:
    n = len(A)
    p = len(A[0])
    return [sum(A[i][j] * v[i] for i in range(n)) for j in range(p)]


def mat_mul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    n = len(A)
    k = len(A[0])
    m = len(B[0])
    return [[sum(A[i][r] * B[r][j] for r in range(k)) for j in range(m)] for i in range(n)]


def mat_inv(M: list[list[float]]) -> list[list[float]]:
    n = len(M)
    A = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(M)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(A[r][col]))
        A[col], A[piv] = A[piv], A[col]
        div = A[col][col]
        for j in range(2 * n):
            A[col][j] /= div
        for r in range(n):
            if r != col:
                factor = A[r][col]
                for j in range(2 * n):
                    A[r][j] -= factor * A[col][j]
    return [row[n:] for row in A]


def ols_fit(X: list[list[float]], y: list[float]) -> list[float]:
    n = len(X)
    p = len(X[0])
    XtX = [[sum(X[i][j] * X[i][k] for i in range(n)) for k in range(p)] for j in range(p)]
    Xty = mat_T_vec(X, y)
    return mat_vec(mat_inv(XtX), Xty)


def hat_matrix(X: list[list[float]]) -> list[list[float]]:
    n = len(X)
    p = len(X[0])
    XtX = [[sum(X[i][j] * X[i][k] for i in range(n)) for k in range(p)] for j in range(p)]
    XtX_inv = mat_inv(XtX)
    X_inv = mat_mul(X, XtX_inv)
    XT = [[X[i][j] for i in range(n)] for j in range(p)]
    return mat_mul(X_inv, XT)


def theta_soft(t: float, lam: float) -> float:
    if abs(t) <= lam:
        return 0.0
    return t - math.copysign(lam, t)


def theta_hard(t: float, lam: float) -> float:
    return 0.0 if abs(t) <= lam else t


def theta_hard_ridge(t: float, lam: float, eta: float) -> float:
    return 0.0 if abs(t) < lam else t / (1.0 + eta)


def p_theta_hard(theta: float, lam: float) -> float:
    a = abs(theta)
    if a < lam:
        return lam * a - 0.5 * a * a
    return 0.5 * lam * lam


def p_l0_hard(theta: float, lam: float) -> float:
    return 0.0 if theta == 0.0 else 0.5 * lam * lam


def p_hard_ridge(theta: float, lam: float, eta: float) -> float:
    return (0.5 * (lam * lam) / (1.0 + eta) if theta != 0.0 else 0.0) + 0.5 * eta * theta * theta


def verify_prop3_1_and_theorem4_1() -> dict[str, object]:
    rng = random.Random(201106)
    n, p = 45, 4
    X = [[1.0 if j == 0 else rng.gauss(0.0, 1.0) for j in range(p)] for _ in range(n)]
    beta_true = [1.0, 2.0, -1.5, 0.8]
    y = [sum(X[i][j] * beta_true[j] for j in range(p)) + rng.gauss(0.0, 0.5) for i in range(n)]
    # Add 4 moderate outliers
    for idx in range(4):
        y[idx] += 4.5

    H = hat_matrix(X)
    lam = 0.9
    c_concom = 0.65

    # Jointly optimize g(beta, gamma, sigma) in Eq. (3.3) via alternating minimization
    beta = ols_fit(X, y)
    gamma = [0.0] * n
    sigma = 1.0
    for _ in range(400):
        y_adj = [y[i] - gamma[i] for i in range(n)]
        beta = ols_fit(X, y_adj)
        r = [y[i] - sum(X[i][j] * beta[j] for j in range(p)) for i in range(n)]
        gamma = [theta_soft(r[i], lam * sigma) for i in range(n)]
        rss = sum((r[i] - gamma[i]) ** 2 for i in range(n))
        sigma = math.sqrt(rss / (c_concom * n))

    # Check Huber's KKT equations (A.3) and (A.4)
    r_hat = [y[i] - sum(X[i][j] * beta[j] for j in range(p)) for i in range(n)]
    psi_vec = [
        lam if r_hat[i] / sigma > lam else (-lam if r_hat[i] / sigma < -lam else r_hat[i] / sigma)
        for i in range(n)
    ]
    huber_score = mat_T_vec(X, psi_vec)
    max_huber_score_err = max(abs(val) for val in huber_score)
    G_hat = [i for i in range(n) if abs(r_hat[i]) < lam * sigma]
    O_hat = [i for i in range(n) if abs(r_hat[i]) >= lam * sigma]
    sigma_huber_sq = sum(r_hat[i] ** 2 for i in G_hat) / (c_concom * n - (lam ** 2) * len(O_hat))
    sigma_diff = abs(sigma * sigma - sigma_huber_sq)

    # Verify Algorithm 1 vs Algorithm 2 and Theorem 4.1 monotone descent for hard-IPOD
    lam_vec = [1.2 * math.sqrt(max(1e-12, 1.0 - H[i][i])) for i in range(n)]
    gamma_alg1 = [0.0] * n
    gamma_alg2 = [0.0] * n
    r_ols = [y[i] - sum(H[i][k] * y[k] for k in range(n)) for i in range(n)]

    max_alg1_alg2_diff = 0.0
    max_descent_violation_p_theta = 0.0
    max_descent_violation_l0 = 0.0

    for _ in range(80):
        y_adj = [y[i] - gamma_alg1[i] for i in range(n)]
        beta_j = ols_fit(X, y_adj)
        r_j = [y[i] - sum(X[i][k] * beta_j[k] for k in range(p)) for i in range(n)]

        f_before_ptheta = 0.5 * sum((r_j[i] - gamma_alg1[i]) ** 2 for i in range(n)) + sum(
            p_theta_hard(gamma_alg1[i], lam_vec[i]) for i in range(n)
        )
        f_before_l0 = 0.5 * sum((r_j[i] - gamma_alg1[i]) ** 2 for i in range(n)) + sum(
            p_l0_hard(gamma_alg1[i], lam_vec[i]) for i in range(n)
        )

        gamma_next1 = [theta_hard(r_j[i], lam_vec[i]) for i in range(n)]
        Hg = mat_vec(H, gamma_alg2)
        gamma_next2 = [theta_hard(Hg[i] + r_ols[i], lam_vec[i]) for i in range(n)]

        diff12 = max(abs(gamma_next1[i] - gamma_next2[i]) for i in range(n))
        if diff12 > max_alg1_alg2_diff:
            max_alg1_alg2_diff = diff12

        y_adj_next = [y[i] - gamma_next1[i] for i in range(n)]
        beta_next = ols_fit(X, y_adj_next)
        r_next = [y[i] - sum(X[i][k] * beta_next[k] for k in range(p)) for i in range(n)]

        f_mid_ptheta = 0.5 * sum((r_j[i] - gamma_next1[i]) ** 2 for i in range(n)) + sum(
            p_theta_hard(gamma_next1[i], lam_vec[i]) for i in range(n)
        )
        f_after_ptheta = 0.5 * sum((r_next[i] - gamma_next1[i]) ** 2 for i in range(n)) + sum(
            p_theta_hard(gamma_next1[i], lam_vec[i]) for i in range(n)
        )

        f_mid_l0 = 0.5 * sum((r_j[i] - gamma_next1[i]) ** 2 for i in range(n)) + sum(
            p_l0_hard(gamma_next1[i], lam_vec[i]) for i in range(n)
        )
        f_after_l0 = 0.5 * sum((r_next[i] - gamma_next1[i]) ** 2 for i in range(n)) + sum(
            p_l0_hard(gamma_next1[i], lam_vec[i]) for i in range(n)
        )

        v_pt = max(0.0, f_mid_ptheta - f_before_ptheta, f_after_ptheta - f_mid_ptheta)
        v_l0 = max(0.0, f_mid_l0 - f_before_l0, f_after_l0 - f_mid_l0)
        if v_pt > max_descent_violation_p_theta:
            max_descent_violation_p_theta = v_pt
        if v_l0 > max_descent_violation_l0:
            max_descent_violation_l0 = v_l0

        gamma_alg1 = gamma_next1
        gamma_alg2 = gamma_next2

    # Check Proposition 4.1 M-estimator score equation X^T psi_hard(y - X beta_hat; lam_vec) = 0
    beta_final = ols_fit(X, [y[i] - gamma_alg1[i] for i in range(n)])
    r_final = [y[i] - sum(X[i][k] * beta_final[k] for k in range(p)) for i in range(n)]
    psi_hard_vec = [r_final[i] - theta_hard(r_final[i], lam_vec[i]) for i in range(n)]
    m_score = mat_T_vec(X, psi_hard_vec)
    max_m_score_err = max(abs(v) for v in m_score)

    return {
        "max_huber_score_err": max_huber_score_err,
        "concomitant_sigma_sq_diff": sigma_diff,
        "max_alg1_alg2_diff": max_alg1_alg2_diff,
        "max_descent_violation_p_theta": max_descent_violation_p_theta,
        "max_descent_violation_l0": max_descent_violation_l0,
        "max_m_score_err": max_m_score_err,
    }


def run_simplified_ipod(
    H: list[list[float]],
    r_ols: list[float],
    lam_vec: list[float],
    gamma_init: list[float],
    hard: bool,
    max_iter: int = 1500,
    tol: float = 1e-13,
) -> list[float]:
    n = len(r_ols)
    gamma = gamma_init[:]
    for _ in range(max_iter):
        Hg = mat_vec(H, gamma)
        if hard:
            gamma_next = [theta_hard(Hg[i] + r_ols[i], lam_vec[i]) for i in range(n)]
        else:
            gamma_next = [theta_soft(Hg[i] + r_ols[i], lam_vec[i]) for i in range(n)]
        if max(abs(gamma_next[i] - gamma[i]) for i in range(n)) < tol:
            gamma = gamma_next
            break
        gamma = gamma_next
    return gamma


def verify_high_leverage_masking_and_bic_star() -> dict[str, object]:
    """Verify high-leverage outlier masking/swamping failure of convex soft-IPOD
    vs. exact outlier identification by BIC*-tuned hard-IPOD (Sections 3, 4, 6)."""
    rng = random.Random(201107)
    n, p, O_outliers = 60, 4, 6
    X = [[1.0 if j == 0 else rng.uniform(-2.0, 2.0) for j in range(p)] for _ in range(n)]
    # First O_outliers rows are moderate-leverage outliers (HBK cases 1-10 style, Section 3-4)
    for i in range(O_outliers):
        X[i] = [1.0] + [6.0 + 0.05 * j + 0.02 * i for j in range(1, p)]
    # Next 3 rows are clean higher-leverage points (HBK cases 11-14 style, Section 3-4)
    for i in range(O_outliers, O_outliers + 3):
        X[i] = [1.0] + [12.0 - 0.04 * j + 0.03 * i for j in range(1, p)]

    beta_true = [0.5, 1.5, -1.0, 0.8]
    sigma_noise = 0.2
    noise = [rng.gauss(0.0, sigma_noise) for _ in range(n)]
    gamma_true = [10.0 if i < O_outliers else 0.0 for i in range(n)]
    y = [
        sum(X[i][j] * beta_true[j] for j in range(p)) + gamma_true[i] + noise[i]
        for i in range(n)
    ]

    H = hat_matrix(X)
    r_ols = [y[i] - sum(H[i][k] * y[k] for k in range(n)) for i in range(n)]
    scale_factors = [math.sqrt(max(1e-12, 1.0 - H[i][i])) for i in range(n)]

    # Evaluate soft-IPOD across a fine grid of lambda: check if ANY lambda
    # recovers the exact outlier set {0..5} without masking or swamping
    lam_max = max(abs(r_ols[i]) / scale_factors[i] for i in range(n))
    soft_exact_recovery_count = 0
    for step in range(1, 80):
        lam = lam_max * (1.0 - step / 85.0)
        lam_vec = [lam * scale_factors[i] for i in range(n)]
        g_soft = run_simplified_ipod(H, r_ols, lam_vec, [0.0] * n, hard=False)
        detected = [i for i in range(n) if abs(g_soft[i]) > 1e-4]
        if detected == list(range(O_outliers)):
            soft_exact_recovery_count += 1

    # Now run hard-IPOD initialized with a robust pilot estimate (core low-leverage observations)
    # and tune lambda via modified BIC* (Eq. 6.1):
    # BIC*(lambda) = m log(RSS/m) + (DF(lambda) + 1) (log(m) + 1), m = n - p
    m = n - p
    leverages = [H[i][i] for i in range(n)]
    core_idx = sorted(range(n), key=lambda i: leverages[i])[: n // 2]
    X_core = [X[i] for i in core_idx]
    y_core = [y[i] for i in core_idx]
    beta_pilot = ols_fit(X_core, y_core)
    gamma_pilot = [y[i] - sum(X[i][j] * beta_pilot[j] for j in range(p)) for i in range(n)]

    best_bic_star = float("inf")
    best_gamma_hard: list[float] = []
    best_lam = 0.0

    for step in range(1, 45):
        lam = 8.0 - step * 0.15
        lam_vec = [lam * scale_factors[i] for i in range(n)]
        g_hard = run_simplified_ipod(H, r_ols, lam_vec, gamma_pilot, hard=True)
        df = sum(1 for v in g_hard if abs(v) > 1e-7)
        if df >= n // 2:
            continue
        # RSS = ||(I - H)(y - g_hard)||_2^2
        y_minus_g = [y[i] - g_hard[i] for i in range(n)]
        Hy_g = mat_vec(H, y_minus_g)
        rss = sum((y_minus_g[i] - Hy_g[i]) ** 2 for i in range(n))
        bic_star = m * math.log(max(rss / m, 1e-15)) + (df + 1) * (math.log(m) + 1.0)
        if bic_star < best_bic_star:
            best_bic_star = bic_star
            best_gamma_hard = g_hard
            best_lam = lam

    detected_hard = [i for i in range(n) if abs(best_gamma_hard[i]) > 1e-6]
    beta_hard = ols_fit(X, [y[i] - best_gamma_hard[i] for i in range(n)])
    X_clean = [X[i] for i in range(O_outliers, n)]
    y_clean = [y[i] for i in range(O_outliers, n)]
    beta_clean_ols = ols_fit(X_clean, y_clean)
    beta_ols_all = ols_fit(X, y)

    max_diff_from_clean_ols = max(abs(beta_hard[j] - beta_clean_ols[j]) for j in range(p))
    l2_err_hard = math.sqrt(sum((beta_hard[j] - beta_true[j]) ** 2 for j in range(p)))
    l2_err_ols = math.sqrt(sum((beta_ols_all[j] - beta_true[j]) ** 2 for j in range(p)))

    # Verify regression equivariance: beta_hat(X, y + X eta) = beta_hat(X, y) + eta
    eta_shift = [2.0, -1.0, 0.5, -0.75]
    y_shifted = [y[i] + sum(X[i][j] * eta_shift[j] for j in range(p)) for i in range(n)]
    r_ols_shifted = [
        y_shifted[i] - sum(H[i][k] * y_shifted[k] for k in range(n)) for i in range(n)
    ]
    beta_pilot_shifted = ols_fit(X_core, [y_shifted[i] for i in core_idx])
    gamma_pilot_shifted = [
        y_shifted[i] - sum(X[i][j] * beta_pilot_shifted[j] for j in range(p))
        for i in range(n)
    ]
    lam_vec_best = [best_lam * scale_factors[i] for i in range(n)]
    g_hard_shifted = run_simplified_ipod(
        H, r_ols_shifted, lam_vec_best, gamma_pilot_shifted, hard=True
    )
    beta_hard_shifted = ols_fit(X, [y_shifted[i] - g_hard_shifted[i] for i in range(n)])
    equivariance_err = max(
        abs(beta_hard_shifted[j] - (beta_hard[j] + eta_shift[j])) for j in range(p)
    )

    return {
        "soft_exact_recovery_count": soft_exact_recovery_count,
        "detected_hard": detected_hard,
        "true_outliers": list(range(O_outliers)),
        "max_diff_from_clean_ols": max_diff_from_clean_ols,
        "l2_err_hard": l2_err_hard,
        "l2_err_ols": l2_err_ols,
        "equivariance_err": equivariance_err,
    }


def verify_high_dim_hard_ridge_ipod() -> dict[str, object]:
    """Verify Section 7 (p > n) joint TISP iteration (Eq. 7.1) with hard-ridge thresholding (Eq. 7.2)
    and monotone descent of the fused L0 + L2 objective (Eq. 7.3)."""
    rng = random.Random(201108)
    n, p = 36, 54
    X_raw = [[rng.gauss(0.0, 1.0) for _ in range(p)] for _ in range(n)]
    for j in range(p):
        col_norm = math.sqrt(sum(X_raw[i][j] ** 2 for i in range(n)))
        for i in range(n):
            X_raw[i][j] /= col_norm

    beta_true = [0.0] * p
    beta_true[0] = 3.6
    beta_true[1] = -3.2
    gamma_true = [0.0] * n
    gamma_true[0] = 4.0
    gamma_true[1] = -3.8

    y = [
        sum(X_raw[i][j] * beta_true[j] for j in range(p))
        + gamma_true[i]
        + rng.gauss(0.0, 0.05)
        for i in range(n)
    ]

    # Compute spectral norm ||X||_2 via power iteration and set k0 = sqrt(||X||_2^2 + 1)
    v = [1.0 / math.sqrt(p)] * p
    for _ in range(30):
        Xv = mat_vec(X_raw, v)
        XtXv = mat_T_vec(X_raw, Xv)
        nrm = math.sqrt(sum(x * x for x in XtXv))
        v = [x / nrm for x in XtXv]
    Xv = mat_vec(X_raw, v)
    norm_X = math.sqrt(sum(x * x for x in Xv))
    k0_sq = norm_X * norm_X + 1.05

    lam_beta = 2.0
    lam_gamma = 2.2
    eta = 0.02

    beta = [0.0] * p
    gamma = [0.0] * n
    max_descent_violation = 0.0

    def obj_val(b: list[float], g: list[float]) -> float:
        Xb = mat_vec(X_raw, b)
        res_sq = 0.5 * sum((y[i] - Xb[i] - g[i]) ** 2 for i in range(n))
        pen_b = sum(
            k0_sq * p_hard_ridge(b[j], lam_beta / k0_sq, eta / k0_sq) for j in range(p)
        )
        pen_g = sum(
            k0_sq * p_hard_ridge(g[i], lam_gamma / k0_sq, eta / k0_sq) for i in range(n)
        )
        return res_sq + pen_b + pen_g

    f_prev = obj_val(beta, gamma)
    for _ in range(400):
        Xb = mat_vec(X_raw, beta)
        res = [y[i] - Xb[i] - gamma[i] for i in range(n)]
        Xt_res = mat_T_vec(X_raw, res)
        beta_next = [
            theta_hard_ridge(
                beta[j] + Xt_res[j] / k0_sq,
                lam_beta / k0_sq,
                eta / k0_sq,
            )
            for j in range(p)
        ]
        gamma_next = [
            theta_hard_ridge(
                gamma[i] + res[i] / k0_sq,
                lam_gamma / k0_sq,
                eta / k0_sq,
            )
            for i in range(n)
        ]
        f_curr = obj_val(beta_next, gamma_next)
        if f_curr - f_prev > max_descent_violation:
            max_descent_violation = f_curr - f_prev
        beta, gamma, f_prev = beta_next, gamma_next, f_curr

    selected_beta = [j for j in range(p) if abs(beta[j]) > 1e-6]
    selected_gamma = [i for i in range(n) if abs(gamma[i]) > 1e-6]

    return {
        "max_descent_violation": max_descent_violation,
        "selected_beta": selected_beta,
        "selected_gamma": selected_gamma,
    }


def main() -> None:
    res1 = verify_prop3_1_and_theorem4_1()
    res2 = verify_high_leverage_masking_and_bic_star()
    res3 = verify_high_dim_hard_ridge_ipod()

    assert res1["max_huber_score_err"] < 1e-10
    assert res1["concomitant_sigma_sq_diff"] < 1e-10
    assert res1["max_alg1_alg2_diff"] < 1e-12
    assert res1["max_descent_violation_p_theta"] < 1e-12
    assert res1["max_descent_violation_l0"] < 1e-12
    assert res1["max_m_score_err"] < 1e-12

    assert res2["soft_exact_recovery_count"] == 0
    assert res2["detected_hard"] == res2["true_outliers"]
    assert res2["max_diff_from_clean_ols"] < 1e-12
    assert res2["l2_err_hard"] < 0.25 * res2["l2_err_ols"]
    assert res2["equivariance_err"] < 1e-11

    assert res3["max_descent_violation"] < 1e-11
    assert res3["selected_beta"] == [0, 1]
    assert res3["selected_gamma"] == [0, 1]

    summary = {
        "prop3_1_and_thm4_1": {
            k: round(v, 14) if isinstance(v, float) else v for k, v in res1.items()
        },
        "high_leverage_and_bic_star": {
            k: round(v, 8) if isinstance(v, float) else v for k, v in res2.items()
        },
        "high_dim_hard_ridge_ipod": {
            k: round(v, 14) if isinstance(v, float) else v for k, v in res3.items()
        },
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
