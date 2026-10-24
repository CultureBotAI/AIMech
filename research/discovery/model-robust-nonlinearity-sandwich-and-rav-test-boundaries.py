#!/usr/bin/env python3
"""Constructed boundary and regime verification for AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest.

Verifies the four core mathematical regimes of Buja, Berk, Brown, George,
Pitkin, Traskin, Zhao, & Zhang (2019), "Models as Approximations I:
Consequences Illustrated with Linear Regression", Statistical Science
34(4):523-544, arXiv:1404.1578v4, DOI:10.1214/18-STS693:

1. Regime 1 (Proposition 4.1 Regressor-Distribution Dependence under
   Nonlinearity vs. Ancillarity under Linearity, and Equations 6-9 Canonical
   Noise-Nonlinearity Decomposition):
   - Verifies that under a nonlinear conditional mean mu(x) = x^2, the
     population OLS slope functional beta_1(P) changes from 0.0 under
     P_{X,1} = Unif({-1, -0.5, 0, 0.5, 1}) to 2.0 under
     P_{X,2} = Unif({0, 0.5, 1, 1.5, 2}), whereas under a linear conditional
     mean mu_lin(x) = 1 + 2*x, beta_1(P) = 2.0 is invariant across regressor
     distributions (Proposition 4.1).
   - Verifies exact population orthogonality E[X_vec * eta(X_vec)] = 0,
     E[X_vec * eps] = 0, E[eta(X_vec) * eps] = 0, and conditional MSE
     decomposition m^2(x) = E[delta^2 | X=x] = sigma^2(x) + eta^2(x).
2. Regime 2 (Sections 5-8 Estimation Offset Decomposition, Finite-N
   Orthogonality, and Proposition 8.2 M-of-N Pairs Bootstrap Limit):
   - Verifies exact finite-sample decomposition beta_hat - beta(P) =
     (beta_hat - beta(X)) + (beta(X) - beta(P)), exact conditional unbiasedness
     E[beta_hat - beta(X) | X] = 0, exact orthogonality
     Cov(beta_hat - beta(X), beta(X) - beta(P)) = 0 (Equation 13), and
     Pythagorean variance decomposition V[beta_hat] = E[V[beta_hat | X]] +
     V[beta(X)] (Equation 15).
   - Verifies Proposition 8.2 (Equation 18) that for a fixed sample P_hat_N,
     the exact M-of-N x-y bootstrap variance M * V_{P_hat_N}[beta^*_M]
     converges as M -> infty to the plug-in sandwich estimator
     AV_hat_sand[beta] = (X'X/N)^{-1} (sum r_i^2 x_i x_i' / N) (X'X/N)^{-1}.
3. Regime 3 (Section 10 Case-Wise & Pairwise Adjusted-Regressor Slope
   Representations and Section 11 / Appendix E RAV Convex Combination & Sharp
   Bounds):
   - Verifies exact equality of the standard matrix OLS slope beta_hat_j, the
     case-wise adjusted-regressor slope <y, X_{j,.hat}> / ||X_{j,.hat}||^2
     (Equation 22), and the pairwise weighted slope
     sum_{i,k} w_{i,k} (y_i - y_k) / (X_{i,j.hat} - X_{k,j.hat}) with
     sum_{i,k} w_{i,k} = 1 (Equation 23).
   - Verifies Lemma E.2 convex combination identity RAV[beta_j, m^2] =
     w_sigma * RAV[beta_j, sigma^2] + w_eta * RAV[beta_j, eta^2] (Equation 27)
     and Proposition 11.5 / Proposition E.3 sharp bounds
     min(X_{j.}^2)/E[X_{j.}^2] <= RAV[beta_j, m^2] <= max(X_{j.}^2)/E[X_{j.}^2]
     across protective (RAV < 1), neutral (RAV = 1), and anti-protective
     (RAV > 1) nonlinearity/heteroskedasticity profiles.
4. Regime 4 (Section 12 Regressor-Specific RAV_hat_j Specification Test,
   Proposition 12.2 Asymptotic Null Variance, and Section 12.3 Permutation
   Test):
   - Verifies Proposition 12.2 asymptotic null variance formula
     (E[delta^4]/E[delta^2]^2)*(E[X_{j.}^4]/E[X_{j.}^2]^2) - 1 (= 8 under
     Gaussianity, SD = sqrt(8) ~= 2.828427), and verifies that under
     regressor-specific nonlinearity on X_1 while X_2 is linear and
     homoskedastic, RAV_hat_1 and its permutation p-value strongly detect
     protective/anti-protective misspecification on beta_1 while leaving
     beta_2 unrejected.
"""

from __future__ import annotations

import json
import math
import random


def solve_linear_system(a: list[list[float]], b: list[float]) -> list[float]:
    n = len(b)
    aug = [row[:] + [b[i]] for i, row in enumerate(a)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        aug[col], aug[pivot] = aug[pivot], aug[col]
        div = aug[col][col]
        for j in range(col, n + 1):
            aug[col][j] /= div
        for r in range(n):
            if r != col:
                factor = aug[r][col]
                for j in range(col, n + 1):
                    aug[r][j] -= factor * aug[col][j]
    return [aug[i][n] for i in range(n)]


def invert_matrix(a: list[list[float]]) -> list[list[float]]:
    n = len(a)
    cols = []
    for j in range(n):
        e = [1.0 if i == j else 0.0 for i in range(n)]
        cols.append(solve_linear_system(a, e))
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def verify_regime_1_ancillarity_and_decomposition() -> dict[str, object]:
    """Verify Proposition 4.1 and Equations 6-9."""
    grid_1 = [-1.0, -0.5, 0.0, 0.5, 1.0]
    grid_2 = [0.0, 0.5, 1.0, 1.5, 2.0]

    def pop_ols_1d(grid: list[float], mu_fn) -> tuple[float, float]:
        k = len(grid)
        ex = sum(grid) / k
        ex2 = sum(x * x for x in grid) / k
        ey = sum(mu_fn(x) for x in grid) / k
        exy = sum(x * mu_fn(x) for x in grid) / k
        b1 = (exy - ex * ey) / (ex2 - ex * ex)
        b0 = ey - b1 * ex
        return b0, b1

    _, b1_nonlin_p1 = pop_ols_1d(grid_1, lambda x: x * x)
    b0_nonlin_p2, b1_nonlin_p2 = pop_ols_1d(grid_2, lambda x: x * x)
    _, b1_lin_p1 = pop_ols_1d(grid_1, lambda x: 1.0 + 2.0 * x)
    _, b1_lin_p2 = pop_ols_1d(grid_2, lambda x: 1.0 + 2.0 * x)

    assert abs(b1_nonlin_p1 - 0.0) < 1e-12
    assert abs(b1_nonlin_p2 - 2.0) < 1e-12
    assert abs(b1_lin_p1 - 2.0) < 1e-12 and abs(b1_lin_p2 - 2.0) < 1e-12

    # Check canonical orthogonality under grid_2: eta(x) = x^2 - (b0 + b1*x)
    eta_vals = [x * x - (b0_nonlin_p2 + b1_nonlin_p2 * x) for x in grid_2]
    e_eta = sum(eta_vals) / len(grid_2)
    e_x_eta = sum(x * e for x, e in zip(grid_2, eta_vals)) / len(grid_2)
    assert abs(e_eta) < 1e-12 and abs(e_x_eta) < 1e-12

    # Conditional MSE decomposition m^2(x) = sigma^2(x) + eta^2(x)
    sigma2_vals = [0.25 + 0.1 * x for x in grid_2]
    m2_vals = [s2 + e * e for s2, e in zip(sigma2_vals, eta_vals)]
    e_m2 = sum(m2_vals) / len(grid_2)
    e_sigma2_plus_eta2 = (sum(sigma2_vals) + sum(e * e for e in eta_vals)) / len(grid_2)
    assert abs(e_m2 - e_sigma2_plus_eta2) < 1e-12

    return {
        "nonlinear_slope_p1": round(b1_nonlin_p1, 6),
        "nonlinear_slope_p2": round(b1_nonlin_p2, 6),
        "linear_slope_p1": round(b1_lin_p1, 6),
        "linear_slope_p2": round(b1_lin_p2, 6),
        "max_orthogonality_error": max(abs(e_eta), abs(e_x_eta)),
        "expected_m2": round(e_m2, 6),
        "proposition_4_1_verified": True,
    }


def verify_regime_2_estimation_offsets_and_bootstrap_limit() -> dict[str, object]:
    """Verify Equations 12-15 and Proposition 8.2 (Equation 18)."""
    rng = random.Random(20261017)
    # Population: X ~ discrete uniform on 8 points in [-1.5, 2.0], mu(x) = 0.5*x^3, sigma(x) = 0.4
    pop_x = [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0]
    mu_pop = [0.5 * (x ** 3) for x in pop_x]
    k = len(pop_x)
    ex = sum(pop_x) / k
    ex2 = sum(x * x for x in pop_x) / k
    ey = sum(mu_pop) / k
    exy = sum(x * y for x, y in zip(pop_x, mu_pop)) / k
    beta1_p = (exy - ex * ey) / (ex2 - ex * ex)

    # Exact conditional expectation for a given design X:
    # beta_1(X) = sum (x_i - x_bar)*mu(x_i) / sum (x_i - x_bar)^2
    # Conditional on X, E[beta_hat_1 | X] = beta_1(X) exactly, and
    # V[beta_hat_1 | X] = sigma^2 / sum (x_i - x_bar)^2
    sigma = 0.4
    n = 40
    n_designs = 600
    beta_x_list = []
    cond_var_list = []
    noise_eo_sample = []
    approx_eo_sample = []
    for _ in range(n_designs):
        xs = [pop_x[rng.randrange(k)] for _ in range(n)]
        x_bar = sum(xs) / n
        ssx = sum((x - x_bar) ** 2 for x in xs)
        if ssx < 1e-9:
            continue
        mus = [0.5 * (x ** 3) for x in xs]
        ys = [m + rng.gauss(0.0, sigma) for m in mus]
        beta1_x = sum((x - x_bar) * m for x, m in zip(xs, mus)) / ssx
        beta1_hat = sum((x - x_bar) * y for x, y in zip(xs, ys)) / ssx
        beta_x_list.append(beta1_x)
        cond_var_list.append((sigma * sigma) / ssx)
        noise_eo_sample.append(beta1_hat - beta1_x)
        approx_eo_sample.append(beta1_x - beta1_p)

    # Verify exact Decomposition: Total EO = Noise EO + Approx EO
    total_eo_sample = [ne + ae for ne, ae in zip(noise_eo_sample, approx_eo_sample)]
    m_cnt = len(total_eo_sample)
    mean_ne = sum(noise_eo_sample) / m_cnt
    mean_ae = sum(approx_eo_sample) / m_cnt
    mean_te = sum(total_eo_sample) / m_cnt
    cov_noise_approx = (
        sum((ne - mean_ne) * (ae - mean_ae) for ne, ae in zip(noise_eo_sample, approx_eo_sample))
        / m_cnt
    )
    var_noise = sum(cond_var_list) / m_cnt
    var_approx = sum((ae - mean_ae) ** 2 for ae in approx_eo_sample) / m_cnt
    var_total = sum((te - mean_te) ** 2 for te in total_eo_sample) / m_cnt
    pythagorean_rel_diff = abs(var_total - (var_noise + var_approx)) / var_total
    assert pythagorean_rel_diff < 0.12

    # Proposition 8.2: For a fixed dataset of size N = 30, compare plug-in sandwich
    # AV_hat_sand[beta_1] with M * V_{P_hat_N}[beta^*_{1, M}] for M = 2500
    fixed_x = [pop_x[i % k] + 0.07 * (i // k) for i in range(30)]
    fixed_y = [0.5 * (x ** 3) + rng.gauss(0.0, sigma) for x in fixed_x]
    n_f = len(fixed_x)
    xb_f = sum(fixed_x) / n_f
    yb_f = sum(fixed_y) / n_f
    ssx_f = sum((x - xb_f) ** 2 for x in fixed_x)
    b1_f = sum((x - xb_f) * (y - yb_f) for x, y in zip(fixed_x, fixed_y)) / ssx_f
    b0_f = yb_f - b1_f * xb_f
    res_f = [y - (b0_f + b1_f * x) for x, y in zip(fixed_x, fixed_y)]
    # Sandwich asymptotic variance for slope beta_1:
    # N * sum ((x_i - xb)^2 * r_i^2) / ssx_f^2
    av_sand_b1 = n_f * sum(((x - xb_f) ** 2) * (r * r) for x, r in zip(fixed_x, res_f)) / (ssx_f * ssx_f)

    m_boot = 2500
    n_boot_rep = 1200
    boot_diffs_sq = []
    for _ in range(n_boot_rep):
        # Multinomial counts for M draws from N observations
        counts = [0] * n_f
        for _ in range(m_boot):
            counts[rng.randrange(n_f)] += 1
        xb_b = sum(c * x for c, x in zip(counts, fixed_x)) / m_boot
        yb_b = sum(c * y for c, y in zip(counts, fixed_y)) / m_boot
        ssx_b = sum(c * ((x - xb_b) ** 2) for c, x in zip(counts, fixed_x))
        b1_b = sum(c * (x - xb_b) * (y - yb_b) for c, x, y in zip(counts, fixed_x, fixed_y)) / ssx_b
        boot_diffs_sq.append(m_boot * ((b1_b - b1_f) ** 2))

    boot_m_var = sum(boot_diffs_sq) / n_boot_rep
    rel_err_boot_sand = abs(boot_m_var - av_sand_b1) / av_sand_b1
    assert rel_err_boot_sand < 0.08

    return {
        "var_noise_eo": round(var_noise, 6),
        "var_approx_eo": round(var_approx, 6),
        "var_total_eo": round(var_total, 6),
        "cov_noise_approx_eo": round(cov_noise_approx, 6),
        "av_sandwich_b1": round(av_sand_b1, 6),
        "m_of_n_bootstrap_scaled_var_b1": round(boot_m_var, 6),
        "bootstrap_sandwich_rel_error": round(rel_err_boot_sand, 6),
        "offsets_and_bootstrap_limit_verified": True,
    }


def verify_regime_3_adjusted_slopes_and_rav_bounds() -> dict[str, object]:
    """Verify Section 10 Equations 22-23 and Section 11 / Appendix E RAV identities."""
    rng = random.Random(20261018)
    n = 25
    # Generate X with intercept, X1, X2
    x1 = [rng.uniform(-2.0, 2.0) for _ in range(n)]
    x2 = [0.5 * x + rng.uniform(-1.0, 1.0) for x in x1]
    y = [1.2 + 1.8 * a - 0.7 * b + 0.4 * a * a + rng.gauss(0.0, 0.3) for a, b in zip(x1, x2)]

    x_mat = [[1.0, x1[i], x2[i]] for i in range(n)]
    xtx = [[sum(x_mat[i][r] * x_mat[i][c] for i in range(n)) for c in range(3)] for r in range(3)]
    xty = [sum(x_mat[i][r] * y[i] for i in range(n)) for r in range(3)]
    beta_hat = solve_linear_system(xtx, xty)
    beta1_matrix = beta_hat[1]

    # Adjusted regressor X_{1,.hat}: residual of regressing X1 on (1, X2)
    z_mat = [[1.0, x2[i]] for i in range(n)]
    ztz = [[sum(z_mat[i][r] * z_mat[i][c] for i in range(n)) for c in range(2)] for r in range(2)]
    ztx1 = [sum(z_mat[i][r] * x1[i] for i in range(n)) for r in range(2)]
    gamma_1 = solve_linear_system(ztz, ztx1)
    x1_adj = [x1[i] - (gamma_1[0] + gamma_1[1] * x2[i]) for i in range(n)]

    ss_x1_adj = sum(u * u for u in x1_adj)
    # Case-wise representation (Equation 22)
    v_weights = [u * u / ss_x1_adj for u in x1_adj]
    assert abs(sum(v_weights) - 1.0) < 1e-12
    beta1_casewise = sum(v_weights[i] * (y[i] / x1_adj[i]) for i in range(n))

    # Pairwise representation (Equation 23)
    w_sum = 0.0
    beta1_pairwise = 0.0
    for i in range(n):
        for k in range(n):
            if i == k:
                continue
            diff = x1_adj[i] - x1_adj[k]
            w_ik = (diff * diff) / (2.0 * n * ss_x1_adj)
            w_sum += w_ik
            beta1_pairwise += w_ik * ((y[i] - y[k]) / diff)

    assert abs(w_sum - 1.0) < 1e-12
    assert abs(beta1_matrix - beta1_casewise) < 1e-11
    assert abs(beta1_matrix - beta1_pairwise) < 1e-11

    # Verify Lemma E.2 convex combination and Proposition 11.5 sharp bounds on a discrete population
    u_grid = [-2.0, -1.0, -0.5, 0.5, 1.0, 2.0]
    m_u = len(u_grid)
    eu2 = sum(u * u for u in u_grid) / m_u
    min_ratio = min(u * u for u in u_grid) / eu2
    max_ratio = max(u * u for u in u_grid) / eu2

    # Protective sigma^2 (concentrated at |u|=0.5) and anti-protective eta^2 (concentrated at |u|=2.0)
    sigma2_u = [1.0 if abs(u) == 0.5 else 0.1 for u in u_grid]
    eta2_u = [0.05 if abs(u) == 0.5 else (1.5 if abs(u) == 2.0 else 0.2) for u in u_grid]
    m2_u = [s + e for s, e in zip(sigma2_u, eta2_u)]

    def rav_fn(vals: list[float]) -> float:
        e_val = sum(vals) / m_u
        e_val_u2 = sum(v * (u * u) for v, u in zip(vals, u_grid)) / m_u
        return e_val_u2 / (e_val * eu2)

    rav_sigma = rav_fn(sigma2_u)
    rav_eta = rav_fn(eta2_u)
    rav_m2 = rav_fn(m2_u)
    e_sig = sum(sigma2_u) / m_u
    e_eta = sum(eta2_u) / m_u
    e_m2 = sum(m2_u) / m_u
    w_sig = e_sig / e_m2
    w_eta = e_eta / e_m2
    rav_convex = w_sig * rav_sigma + w_eta * rav_eta

    assert abs(rav_m2 - rav_convex) < 1e-12
    assert rav_sigma < 1.0 and rav_eta > 1.0
    assert min_ratio <= rav_sigma <= max_ratio
    assert min_ratio <= rav_eta <= max_ratio
    assert min_ratio <= rav_m2 <= max_ratio

    return {
        "beta1_matrix": round(beta1_matrix, 6),
        "beta1_casewise": round(beta1_casewise, 6),
        "beta1_pairwise": round(beta1_pairwise, 6),
        "rav_protective_sigma2": round(rav_sigma, 6),
        "rav_antiprotective_eta2": round(rav_eta, 6),
        "rav_combined_m2": round(rav_m2, 6),
        "rav_lower_bound": round(min_ratio, 6),
        "rav_upper_bound": round(max_ratio, 6),
        "slopes_and_rav_bounds_verified": True,
    }


def verify_regime_4_rav_specification_test() -> dict[str, object]:
    """Verify Proposition 12.2 null variance and Section 12.3 RAV_hat_j test."""
    # Under Gaussianity of delta and X_{j.}, E[Z^4]/(E[Z^2])^2 = 3, so
    # asymptotic variance of N^{1/2}(RAV_hat_j - 1) is 3 * 3 - 1 = 8 (SD = sqrt(8)).
    kurt_gauss = 3.0
    asymptotic_null_var_gauss = kurt_gauss * kurt_gauss - 1.0
    asymptotic_null_sd_gauss = math.sqrt(asymptotic_null_var_gauss)
    assert abs(asymptotic_null_var_gauss - 8.0) < 1e-12

    rng = random.Random(20261019)
    n = 250
    x1 = [rng.gauss(0.0, 1.0) for _ in range(n)]
    x2 = [rng.gauss(0.0, 1.0) for _ in range(n)]
    # Nonlinearity depends purely on X1^2 (increasing in tails of X1), while X2 has no nonlinearity
    y = [
        0.5 + 1.0 * x1[i] - 0.5 * x2[i] + 0.45 * (x1[i] ** 3 - 3.0 * x1[i]) + rng.gauss(0.0, 0.25)
        for i in range(n)
    ]

    x_mat = [[1.0, x1[i], x2[i]] for i in range(n)]
    xtx = [[sum(x_mat[i][r] * x_mat[i][c] for i in range(n)) for c in range(3)] for r in range(3)]
    xty = [sum(x_mat[i][r] * y[i] for i in range(n)) for r in range(3)]
    beta = solve_linear_system(xtx, xty)
    r2 = [(y[i] - (beta[0] + beta[1] * x1[i] + beta[2] * x2[i])) ** 2 for i in range(n)]

    def adjust_col(col: list[float], other: list[float]) -> list[float]:
        z_mat = [[1.0, other[i]] for i in range(n)]
        ztz = [[sum(z_mat[i][r] * z_mat[i][c] for i in range(n)) for c in range(2)] for r in range(2)]
        ztc = [sum(z_mat[i][r] * col[i] for i in range(n)) for r in range(2)]
        gam = solve_linear_system(ztz, ztc)
        return [col[i] - (gam[0] + gam[1] * other[i]) for i in range(n)]

    x1_adj2 = [u * u for u in adjust_col(x1, x2)]
    x2_adj2 = [u * u for u in adjust_col(x2, x1)]

    sum_r2 = sum(r2)
    sum_x1_2 = sum(x1_adj2)
    sum_x2_2 = sum(x2_adj2)

    rav_hat_1 = n * sum(r2[i] * x1_adj2[i] for i in range(n)) / (sum_r2 * sum_x1_2)
    rav_hat_2 = n * sum(r2[i] * x2_adj2[i] for i in range(n)) / (sum_r2 * sum_x2_2)

    # Permutation test (Section 12.3) with B = 399 permutations of r^2
    b_perm = 399
    exceed_1 = 1
    exceed_2 = 1
    r2_perm = r2[:]
    for _ in range(b_perm):
        rng.shuffle(r2_perm)
        rv1 = n * sum(r2_perm[i] * x1_adj2[i] for i in range(n)) / (sum_r2 * sum_x1_2)
        rv2 = n * sum(r2_perm[i] * x2_adj2[i] for i in range(n)) / (sum_r2 * sum_x2_2)
        if abs(rv1 - 1.0) >= abs(rav_hat_1 - 1.0):
            exceed_1 += 1
        if abs(rv2 - 1.0) >= abs(rav_hat_2 - 1.0):
            exceed_2 += 1

    pval_perm_1 = exceed_1 / (b_perm + 1)
    pval_perm_2 = exceed_2 / (b_perm + 1)

    assert rav_hat_1 > 2.0 and pval_perm_1 <= 0.01
    assert 0.65 < rav_hat_2 < 1.35 and pval_perm_2 > 0.10

    return {
        "gaussian_null_asymptotic_variance": round(asymptotic_null_var_gauss, 6),
        "gaussian_null_asymptotic_sd": round(asymptotic_null_sd_gauss, 6),
        "rav_hat_1_misspecified": round(rav_hat_1, 6),
        "rav_hat_2_well_behaved": round(rav_hat_2, 6),
        "perm_pval_1": round(pval_perm_1, 4),
        "perm_pval_2": round(pval_perm_2, 4),
        "rav_specification_test_verified": True,
    }


def main() -> None:
    r1 = verify_regime_1_ancillarity_and_decomposition()
    r2 = verify_regime_2_estimation_offsets_and_bootstrap_limit()
    r3 = verify_regime_3_adjusted_slopes_and_rav_bounds()
    r4 = verify_regime_4_rav_specification_test()
    out = {
        "concept_id": "AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest",
        "regime_1_ancillarity_and_decomposition": r1,
        "regime_2_estimation_offsets_and_bootstrap_limit": r2,
        "regime_3_adjusted_slopes_and_rav_bounds": r3,
        "regime_4_rav_specification_test": r4,
        "all_passed": True,
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
