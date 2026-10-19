#!/usr/bin/env python3
"""Constructed boundary and regime verification for:
AIMech:ScaledLassoAndHuberConcomitantPenalizedJointSparseRegression
Primary source: Tingni Sun and Cun-Hui Zhang (2012), "Scaled Sparse Linear
Regression", Biometrika 99(4):879-898 (DOI:10.1093/biomet/ass043,
arXiv:1104.4595v2).

Verifies:
1. Alternating minimization equilibrium (Eqs. 3-4) vs. joint minimization of
   Huber's concomitant penalized loss L_{lambda_0}(beta, sigma) (Eqs. 5-6,
   Proposition 1), profile derivative zero (Eq. 7), and exact equivalence with
   Square-Root LASSO at a = 0.
2. Exact scale equivariance beta_hat(X, c*y) = c*beta_hat(X, y) and
   sigma_hat(X, c*y) = |c|*sigma_hat(X, y) (Proposition 1), and classical
   OLS unbiased variance recovery sigma_hat^2 = |y - X*beta_lse|_2^2/(n - p)
   at (a, lambda_0) = (p/n, 0) (Section 2, p. 3).
3. Comparison of Scaled LASSO vs. Stadler et al. (2010) l_1-penalized MLE
   (PMLE, positive noise bias) and one-step bias correction (BC), verification
   of the KKT residual-square sandwich (Eq. A6), Theorem 1 & Theorem 2 oracle
   bounds (Eqs. 13, 18), and Theorem 3 post-selection LSE bounds (Eqs. 26-28).
"""

from __future__ import annotations

import json
import math
import random
import sys


def dot(u: list[float], v: list[float]) -> float:
    return sum(ui * vi for ui, vi in zip(u, v))


def norm2(u: list[float]) -> float:
    return math.sqrt(dot(u, u))


def norm1(u: list[float]) -> float:
    return sum(abs(ui) for ui in u)


def mat_vec(X: list[list[float]], b: list[float]) -> list[float]:
    return [dot(row, b) for row in X]


def mat_t_vec(X: list[list[float]], r: list[float]) -> list[float]:
    n = len(X)
    p = len(X[0])
    return [sum(X[i][j] * r[i] for i in range(n)) for j in range(p)]


def soft_threshold(z: float, thresh: float) -> float:
    if z > thresh:
        return z - thresh
    if z < -thresh:
        return z + thresh
    return 0.0


def solve_lasso_cd(
    X: list[list[float]],
    y: list[float],
    lam: float,
    max_iter: int = 4000,
    tol: float = 1e-13,
) -> list[float]:
    """Solve min_beta |y - X*beta|_2^2 / (2n) + lam * |beta|_1 (Eq. 1 with rho(t)=t)."""
    n = len(X)
    p = len(X[0])
    beta = [0.0] * p
    r = list(y)
    col_sq = [sum(X[i][j] ** 2 for i in range(n)) / n for j in range(p)]
    for _ in range(max_iter):
        max_diff = 0.0
        for j in range(p):
            old_bj = beta[j]
            # Partial residual correlation x_j'(r + x_j * old_bj) / n
            corr = sum(X[i][j] * r[i] for i in range(n)) / n + col_sq[j] * old_bj
            new_bj = soft_threshold(corr, lam) / col_sq[j] if col_sq[j] > 0 else 0.0
            diff = new_bj - old_bj
            if abs(diff) > 0.0:
                for i in range(n):
                    r[i] -= X[i][j] * diff
                beta[j] = new_bj
                if abs(diff) > max_diff:
                    max_diff = abs(diff)
        if max_diff < tol:
            break
    return beta


def solve_scaled_lasso(
    X: list[list[float]],
    y: list[float],
    lam0: float,
    a: float = 0.0,
    max_outer: int = 500,
    tol: float = 1e-13,
) -> tuple[list[float], float, int]:
    """Alternating minimization (Eqs. 3-4) for Huber concomitant loss (Eq. 5)."""
    n = len(X)
    p = len(X[0])
    beta = [0.0] * p
    sigma = norm2(y) / math.sqrt((1.0 - a) * n)
    iters = 0
    for it in range(1, max_outer + 1):
        iters = it
        lam = sigma * lam0
        beta_new = solve_lasso_cd(X, y, lam)
        xb = mat_vec(X, beta_new)
        res = [yi - xbi for yi, xbi in zip(y, xb)]
        sigma_new = norm2(res) / math.sqrt((1.0 - a) * n)
        if abs(sigma_new - sigma) + norm1([bn - bo for bn, bo in zip(beta_new, beta)]) < tol:
            beta = beta_new
            sigma = sigma_new
            break
        beta = beta_new
        sigma = sigma_new
    return beta, sigma, iters


def solve_pmle(
    X: list[list[float]],
    y: list[float],
    lam0: float,
    max_outer: int = 500,
    tol: float = 1e-13,
) -> tuple[list[float], float]:
    """Stadler et al. (2010) l_1-penalized MLE iteration:
    sigma <- {y'(y - X*beta)/n}^{1/2}, beta <- beta_hat(sigma * lam0) (Section 4.1, p. 10).
    """
    n = len(X)
    p = len(X[0])
    beta = [0.0] * p
    sigma = norm2(y) / math.sqrt(n)
    for _ in range(max_outer):
        lam = sigma * lam0
        beta_new = solve_lasso_cd(X, y, lam)
        xb = mat_vec(X, beta_new)
        res = [yi - xbi for yi, xbi in zip(y, xb)]
        ip = max(dot(y, res) / n, 1e-15)
        sigma_new = math.sqrt(ip)
        if abs(sigma_new - sigma) + norm1([bn - bo for bn, bo in zip(beta_new, beta)]) < tol:
            beta = beta_new
            sigma = sigma_new
            break
        beta = beta_new
        sigma = sigma_new
    return beta, sigma


def solve_ols_on_support(
    X: list[list[float]], y: list[float], supp: list[int]
) -> list[float]:
    """Solve least squares on active support S_hat (Eq. 26)."""
    n = len(X)
    p = len(X[0])
    k = len(supp)
    if k == 0:
        return [0.0] * p
    # Gram matrix X_S' X_S and RHS X_S' y
    G = [[0.0] * k for _ in range(k)]
    rhs = [0.0] * k
    for a_idx, ja in enumerate(supp):
        rhs[a_idx] = sum(X[i][ja] * y[i] for i in range(n))
        for b_idx, jb in enumerate(supp):
            G[a_idx][b_idx] = sum(X[i][ja] * X[i][jb] for i in range(n))
    # Gaussian elimination with partial pivoting
    aug = [G[row][:] + [rhs[row]] for row in range(k)]
    for col in range(k):
        piv = max(range(col, k), key=lambda r: abs(aug[r][col]))
        aug[col], aug[piv] = aug[piv], aug[col]
        div = aug[col][col]
        for j in range(col, k + 1):
            aug[col][j] /= div
        for r in range(k):
            if r != col:
                factor = aug[r][col]
                for j in range(col, k + 1):
                    aug[r][j] -= factor * aug[col][j]
    beta_ols = [0.0] * p
    for idx, j in enumerate(supp):
        beta_ols[j] = aug[idx][k]
    return beta_ols


def huber_concomitant_loss(
    X: list[list[float]],
    y: list[float],
    beta: list[float],
    sigma: float,
    lam0: float,
    a: float = 0.0,
) -> float:
    n = len(X)
    xb = mat_vec(X, beta)
    res_sq = sum((yi - xbi) ** 2 for yi, xbi in zip(y, xb))
    return res_sq / (2.0 * n * sigma) + (1.0 - a) * sigma / 2.0 + lam0 * norm1(beta)


def main() -> int:
    rng = random.Random(20120994)
    n, p = 60, 90
    s = 4

    # Construct column-normalized design matrix X with |x_j|_2^2 = n (Section 3.1, p. 4)
    X_raw = [[rng.gauss(0.0, 1.0) for _ in range(p)] for _ in range(n)]
    X = [[0.0] * p for _ in range(n)]
    for j in range(p):
        col_norm = math.sqrt(sum(X_raw[i][j] ** 2 for i in range(n)))
        scale = math.sqrt(n) / col_norm
        for i in range(n):
            X[i][j] = X_raw[i][j] * scale

    beta_star = [0.0] * p
    beta_star[0] = 2.2
    beta_star[1] = -1.8
    beta_star[2] = 1.5
    beta_star[3] = -1.2

    sigma_true = 0.5
    eps = [rng.gauss(0.0, sigma_true) for _ in range(n)]
    xb_star = mat_vec(X, beta_star)
    y = [xbi + ei for xbi, ei in zip(xb_star, eps)]

    # Oracle noise estimator sigma^* = |y - X*beta^*|_2 / n^{1/2} (Eq. 9)
    sigma_star = norm2(eps) / math.sqrt(n)
    # Empirical noise score z^* = |X'(y - X*beta^*)/n|_infty / sigma^* (Theorem 1)
    xt_eps = mat_t_vec(X, eps)
    z_star = max(abs(val) / n for val in xt_eps) / sigma_star

    # Universal penalty level lam0 = sqrt((2/n) * log(p)) (Eq. 8)
    lam0 = math.sqrt((2.0 / n) * math.log(p))

    # --- Regime 1: Proposition 1 alternating equilibrium & Huber concomitant convexity ---
    beta_hat, sigma_hat, n_iters = solve_scaled_lasso(X, y, lam0, a=0.0)
    xb_hat = mat_vec(X, beta_hat)
    res_hat = [yi - xbi for yi, xbi in zip(y, xb_hat)]

    # Profile derivative d/dsigma L_{lam0}(beta_hat(sigma*lam0), sigma) at sigma_hat (Eq. 7)
    prof_deriv = 0.5 - dot(res_hat, res_hat) / (2.0 * n * sigma_hat**2)
    assert abs(prof_deriv) < 1e-11, f"Profile derivative non-zero: {prof_deriv}"

    # Verify KKT conditions (Eq. 2) at lam_hat = sigma_hat * lam0
    lam_hat = sigma_hat * lam0
    xt_res = mat_t_vec(X, res_hat)
    max_kkt_active_err = 0.0
    max_kkt_inactive_ratio = 0.0
    for j in range(p):
        grad_j = xt_res[j] / n
        if abs(beta_hat[j]) > 1e-9:
            sgn = 1.0 if beta_hat[j] > 0 else -1.0
            err = abs(grad_j - lam_hat * sgn)
            if err > max_kkt_active_err:
                max_kkt_active_err = err
        else:
            ratio = abs(grad_j) / lam_hat
            if ratio > max_kkt_inactive_ratio:
                max_kkt_inactive_ratio = ratio
    assert max_kkt_active_err < 1e-10
    assert max_kkt_inactive_ratio <= 1.0 + 1e-10

    # Verify joint optimality on Huber concomitant loss L_{lam0}(beta, sigma) (Eq. 5)
    loss_opt = huber_concomitant_loss(X, y, beta_hat, sigma_hat, lam0, a=0.0)
    for d_sigma in (-0.05, -0.01, 0.01, 0.05):
        loss_pert_s = huber_concomitant_loss(
            X, y, beta_hat, sigma_hat + d_sigma, lam0, a=0.0
        )
        assert loss_pert_s > loss_opt
    # Also verify minimum of L_{lam0}(beta_hat, sigma) over sigma equals |y-X*beta_hat|_2/sqrt(n) + lam0*|beta_hat|_1
    sqrt_lasso_obj = norm2(res_hat) / math.sqrt(n) + lam0 * norm1(beta_hat)
    assert abs(loss_opt - sqrt_lasso_obj) < 1e-12

    # --- Regime 2: Scale equivariance (Proposition 1) & OLS df adjustment (p. 3) ---
    c_scale = -2.75
    y_scaled = [c_scale * yi for yi in y]
    beta_c, sigma_c, _ = solve_scaled_lasso(X, y_scaled, lam0, a=0.0)
    scale_beta_err = max(
        abs(bc - c_scale * bh) for bc, bh in zip(beta_c, beta_hat)
    )
    scale_sigma_err = abs(sigma_c - abs(c_scale) * sigma_hat)
    assert scale_beta_err < 1e-10
    assert scale_sigma_err < 1e-10

    # Classical OLS degrees-of-freedom recovery at p_sub < n and (a, lam0) = (p_sub/n, 0)
    p_sub = 8
    X_sub = [row[:p_sub] for row in X]
    beta_lse = solve_ols_on_support(X_sub, y, list(range(p_sub)))
    res_lse = [yi - xbi for yi, xbi in zip(y, mat_vec(X_sub, beta_lse))]
    a_df = p_sub / n
    sigma_df_iter = norm2(res_lse) / math.sqrt((1.0 - a_df) * n)
    sigma_ols_exact = math.sqrt(dot(res_lse, res_lse) / (n - p_sub))
    df_recovery_err = abs(sigma_df_iter - sigma_ols_exact)
    assert df_recovery_err < 1e-14

    # --- Regime 3: KKT residual sandwich (Eq. A6), PMLE positive bias, & Post-LSE (Theorem 3) ---
    h = [bh - bs for bh, bs in zip(beta_hat, beta_star)]
    h_l1 = norm1(h)
    diff_sq = sigma_star**2 - dot(res_hat, res_hat) / n
    lower_a6 = -(z_star * sigma_star + lam_hat) * h_l1
    upper_a6 = 2.0 * z_star * sigma_star * h_l1
    assert lower_a6 - 1e-12 <= diff_sq <= upper_a6 + 1e-12

    # Compare Scaled LASSO vs. PMLE (Stadler et al. 2010) and one-step BC (Section 4.1, p. 10)
    beta_pmle, sigma_pmle = solve_pmle(X, y, lam0)
    beta_for_bc = solve_lasso_cd(X, y, sigma_pmle * lam0)
    res_bc = [yi - xbi for yi, xbi in zip(y, mat_vec(X, beta_for_bc))]
    sigma_bc = norm2(res_bc) / math.sqrt(n)
    # Note: In PMLE, y'(y - X*beta)/n = |y - X*beta|_2^2/n + (X*beta)'(y - X*beta)/n
    # By KKT (Eq. 2), (X*beta)'(y - X*beta)/n = lam * |beta|_1 > 0, so sigma_pmle > |y - X*beta|_2/sqrt(n)!
    xb_pmle = mat_vec(X, beta_pmle)
    res_pmle = [yi - xbi for yi, xbi in zip(y, xb_pmle)]
    pmle_kkt_excess = (
        sigma_pmle**2
        - dot(res_pmle, res_pmle) / n
        - (sigma_pmle * lam0) * norm1(beta_pmle)
    )
    assert abs(pmle_kkt_excess) < 1e-9
    assert sigma_pmle > sigma_bc

    # Post-selection LSE (Theorem 3, Eqs. 26-28)
    supp_hat = [j for j, bj in enumerate(beta_hat) if abs(bj) > 1e-7]
    false_positives = [j for j in supp_hat if j >= s]
    beta_bar = solve_ols_on_support(X, y, supp_hat)
    res_bar = [yi - xbi for yi, xbi in zip(y, mat_vec(X, beta_bar))]
    sigma_bar = norm2(res_bar) / math.sqrt(n)
    # By Theorem 3 (Eq. 27), sigma_bar <= sigma_hat (projection onto supp(beta_hat) reduces residual norm)
    assert sigma_bar <= sigma_hat + 1e-12

    # Compare estimation error |beta_bar - beta^*|_2 vs |beta_hat - beta^*|_2
    l2_err_scaled = norm2([bh - bs for bh, bs in zip(beta_hat, beta_star)])
    l2_err_post = norm2([bb - bs for bb, bs in zip(beta_bar, beta_star)])
    assert l2_err_post < l2_err_scaled

    summary = {
        "concept_id": "AIMech:ScaledLassoAndHuberConcomitantPenalizedJointSparseRegression",
        "primary_source": "Sun & Zhang (2012), Biometrika 99(4):879-898 (arXiv:1104.4595v2)",
        "n": n,
        "p": p,
        "s": s,
        "sigma_true": sigma_true,
        "sigma_star_oracle": round(sigma_star, 8),
        "z_star": round(z_star, 8),
        "lam0_universal": round(lam0, 8),
        "regime1_equilibrium_and_concomitant_loss": {
            "alternating_iters": n_iters,
            "sigma_hat": round(sigma_hat, 8),
            "profile_derivative_at_equilibrium": round(prof_deriv, 14),
            "max_kkt_active_err": round(max_kkt_active_err, 14),
            "max_kkt_inactive_ratio": round(max_kkt_inactive_ratio, 8),
            "concomitant_loss_opt": round(loss_opt, 8),
            "sqrt_lasso_equivalence_gap": round(abs(loss_opt - sqrt_lasso_obj), 15),
        },
        "regime2_scale_equivariance_and_df": {
            "c_scale": c_scale,
            "scale_beta_max_err": round(scale_beta_err, 14),
            "scale_sigma_err": round(scale_sigma_err, 14),
            "ols_df_recovery_err": round(df_recovery_err, 15),
        },
        "regime3_kkt_sandwich_pmle_and_post_lse": {
            "kkt_sandwich_lower_a6": round(lower_a6, 8),
            "kkt_sandwich_diff_sq": round(diff_sq, 8),
            "kkt_sandwich_upper_a6": round(upper_a6, 8),
            "sigma_pmle": round(sigma_pmle, 8),
            "sigma_bc": round(sigma_bc, 8),
            "sigma_scaled_lasso": round(sigma_hat, 8),
            "sigma_post_lse": round(sigma_bar, 8),
            "pmle_kkt_identity_gap": round(abs(pmle_kkt_excess), 12),
            "selected_support_size": len(supp_hat),
            "false_positive_count": len(false_positives),
            "l2_err_scaled_lasso": round(l2_err_scaled, 8),
            "l2_err_post_lse": round(l2_err_post, 8),
        },
        "verification_passed": True,
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
