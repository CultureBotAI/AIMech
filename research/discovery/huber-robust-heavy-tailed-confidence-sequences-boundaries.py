#!/usr/bin/env python3
"""Constructed boundary verification for AIMech:HuberRobustHeavyTailedConfidenceSequences.

Verifies the mathematical properties of Huber-Robust Confidence Sequences
from Wang & Ramdas (2023), 'Huber-Robust Confidence Sequences', Proceedings of
the 26th International Conference on Artificial Intelligence and Statistics
(AISTATS), PMLR 206:9662-9679 (arXiv:2301.09573):

1. Lemma 1, Lemma 6 & Lemma 3:
   - Information-theoretic width lower bound sigma * sqrt(varepsilon) for any
     (varepsilon, 1-alpha)-RCI or RCS over the TV ball B_TV(P, varepsilon) around
     P in M_{sigma^2}^2 via the two-point witness P_1 = delta_0 and
     P_2 = (1 - varepsilon)*delta_0 + varepsilon*delta_{sigma / sqrt(varepsilon)}.
   - Narrowest bounded Catoni influence function phi(x) in [-log 2, log 2]
     (exp(+-phi(x)) in [1/2, 2], range 1.5) and supermartingale property
     E_Q[exp(+-phi(lambda*(X - mu(P)))) / (1 + 0.5*lambda^2*sigma^2 + 1.5*varepsilon)] <= 1
     under adversarial TV contamination Q in B_TV(P, varepsilon), contrasted with
     unbounded/wide Catoni supermartingale blowup.
2. Theorem 1, Theorem 2, Lemma 4, Theorem 3 & Lemma 7:
   - Lemma 7 algebraic bounds A(x) <= 6.5*x and B(x) <= 7*x on (0, 1/7], and
     non-trivial finite breakdown point varepsilon < 8/13 under constant tuning
     lambda = sqrt(varepsilon)/(2*sigma).
   - Anytime coverage and O(sigma*sqrt(varepsilon)) width (< 28*sigma*sqrt(varepsilon),
     strictly tighter than Lugosi-Mendelson's 96*sqrt(2)*sigma*sqrt(varepsilon))
     under varepsilon = 1/9 adversarial outlier contamination at +1000, where
     non-robust Catoni CS (AIMech:CatoniStyleHeavyTailedConfidenceSequences)
     and sub-Gaussian CS suffer 100% miscoverage.
3. Section 3.3 & Corollary 1:
   - Constant tuning lambda_t = 0.5*sqrt(varepsilon)/sigma*(t^u) with u = 0 vs.
     polynomially decaying (u = -0.5) or growing (u = +0.25) tuning schedules,
     demonstrating that only u = 0 maintains bounded width under varepsilon > 0.
   - Corollary 1 exponential growth rate of the robust Catoni test
     supermartingale M_t^{RC}(mu_0) when mu(P) - mu_0 > 14*sigma*sqrt(varepsilon).
4. Section 5.2 & Section 5.3:
   - Infinite-variance p-moment Huber-robust CS (1 < p < 2, Lemma 5, Theorems 4-5,
     Lemma 11) with phi_p(x) in [-log p, log p] (exp(+-phi_p(x)) in [1/p, p],
     range p - 1/p) under contaminated infinite-variance Pareto observations.
   - Bounded-data Huber-robust Kelly betting supermartingale (Theorem 6)
     L_t = prod_{i=1}^t (1 + lambda_i*(X_i - mu(P)) - varepsilon*|lambda_i|) on [0, 1].
"""

from __future__ import annotations

import json
import math
import random


def phi_narrow(x: float) -> float:
    """Narrowest bounded Catoni influence function phi(x) in [-log 2, log 2] (Eq. 13)."""
    if x >= 1.0:
        return math.log(2.0)
    if x >= 0.0:
        return -math.log(1.0 - x + 0.5 * x * x)
    if x >= -1.0:
        return math.log(1.0 + x + 0.5 * x * x)
    return -math.log(2.0)


def phi_wide_unclipped(x: float) -> float:
    """Unclipped wide Catoni influence function (Wang & Ramdas 2023 SPA Eq. 11)."""
    if x >= 0.0:
        return math.log(1.0 + x + 0.5 * x * x)
    return -math.log(1.0 - x + 0.5 * x * x)


def phi_p_clipped(x: float, p: float) -> float:
    """Bounded p-Catoni influence function phi_p(x) in [-log p, log p] (Eq. 36)."""
    if x >= 1.0:
        return math.log(p)
    if x >= 0.0:
        return -math.log(1.0 - x + (x ** p) / p)
    if x >= -1.0:
        ax = -x
        return math.log(1.0 - ax + (ax ** p) / p)
    return -math.log(p)


def solve_monotone_root(
    fn,
    lo: float,
    hi: float,
    target: float,
    iters: int = 60,
) -> float:
    """Bisection solver for strictly decreasing fn(m) = target on [lo, hi]."""
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if fn(mid) > target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def verify_lemma1_and_lemma3_supermartingale() -> dict[str, object]:
    """Verify Lemma 1/6 lower bound witness and Lemma 3 supermartingale inequality."""
    sigma = 3.0
    eps = 1.0 / 9.0
    # Two-point witness in Lemma 6: P1 = delta_0, P2 = (1 - eps)*delta_0 + eps*delta_{sigma/sqrt(eps)}
    atom_p2 = sigma / math.sqrt(eps)
    mu_p1 = 0.0
    mu_p2 = eps * atom_p2
    var_p1 = 0.0
    var_p2 = (1.0 - eps) * (0.0 - mu_p2) ** 2 + eps * (atom_p2 - mu_p2) ** 2
    tv_dist = eps
    lower_bound_diam = abs(mu_p2 - mu_p1)
    assert math.isclose(lower_bound_diam, sigma * math.sqrt(eps), rel_tol=1e-12)
    assert var_p2 <= sigma * sigma + 1e-12

    # Verify phi_narrow bounds and range of exp(+-phi)
    grid = [-5.0 + 0.05 * k for k in range(201)]
    max_exp = max(math.exp(phi_narrow(x)) for x in grid)
    min_exp = min(math.exp(phi_narrow(x)) for x in grid)
    assert math.isclose(max_exp, 2.0, rel_tol=1e-12)
    assert math.isclose(min_exp, 0.5, rel_tol=1e-12)
    for x in grid:
        lower_cat = -math.log(1.0 - x + 0.5 * x * x)
        upper_cat = math.log(1.0 + x + 0.5 * x * x)
        val = phi_narrow(x)
        assert lower_cat - 1e-12 <= val <= upper_cat + 1e-12

    # Numerical expectation under Q = (1 - eps)*N(0, sigma^2) + eps*delta_{1000}
    lam = 0.5 * math.sqrt(eps) / sigma
    # Gauss-Hermite-like dense midpoint integration over [-8*sigma, 8*sigma]
    n_pts = 4000
    a, b = -8.0 * sigma, 8.0 * sigma
    dx = (b - a) / n_pts
    exp_pos_p = 0.0
    exp_neg_p = 0.0
    exp_wide_p = 0.0
    for i in range(n_pts):
        x = a + (i + 0.5) * dx
        pdf = math.exp(-0.5 * (x / sigma) ** 2) / (sigma * math.sqrt(2.0 * math.pi))
        exp_pos_p += math.exp(phi_narrow(lam * x)) * pdf * dx
        exp_neg_p += math.exp(-phi_narrow(lam * x)) * pdf * dx
        exp_wide_p += math.exp(phi_wide_unclipped(lam * x)) * pdf * dx

    outlier = 1000.0
    exp_pos_q = (1.0 - eps) * exp_pos_p + eps * math.exp(phi_narrow(lam * outlier))
    exp_neg_q = (1.0 - eps) * exp_neg_p + eps * math.exp(-phi_narrow(lam * outlier))
    denom_robust = 1.0 + 0.5 * (lam ** 2) * (sigma ** 2) + 1.5 * eps
    ratio_pos_robust = exp_pos_q / denom_robust
    ratio_neg_robust = exp_neg_q / denom_robust

    exp_wide_q = (1.0 - eps) * exp_wide_p + eps * math.exp(phi_wide_unclipped(lam * outlier))
    denom_nonrobust = 1.0 + 0.5 * (lam ** 2) * (sigma ** 2)
    ratio_wide_nonrobust = exp_wide_q / denom_nonrobust

    assert ratio_pos_robust <= 1.0
    assert ratio_neg_robust <= 1.0
    assert ratio_wide_nonrobust > 100.0

    return {
        "sigma": sigma,
        "varepsilon": round(eps, 6),
        "minimax_lower_bound_sigma_sqrt_eps": round(lower_bound_diam, 6),
        "var_p2_witness": round(var_p2, 6),
        "tv_distance_witness": round(tv_dist, 6),
        "exp_phi_min": round(min_exp, 6),
        "exp_phi_max": round(max_exp, 6),
        "exp_phi_range": round(max_exp - min_exp, 6),
        "robust_supermartingale_factor_pos": round(ratio_pos_robust, 6),
        "robust_supermartingale_factor_neg": round(ratio_neg_robust, 6),
        "nonrobust_wide_catoni_factor_under_outlier": round(ratio_wide_nonrobust, 4),
    }


def verify_theorem1_theorem2_and_lemma7() -> dict[str, object]:
    """Verify Lemma 7 algebraic bounds, breakdown point < 8/13, and Theorem 1/2 CS under outliers."""
    # Check Lemma 7 on (0, 1/7]:
    # A(x) = 3.25*x*(1.625*x + 2)/(1.625*x + 1) <= 6.5*x <= 1
    # B(x) = 3.25*x - 2*exp(-x/4)/(1.625*x + 1) + 2 <= 7*x <= 1
    max_a_ratio = 0.0
    max_b_ratio = 0.0
    for k in range(1, 1001):
        x = (1.0 / 7.0) * (k / 1000.0)
        a_x = 3.25 * x * (1.625 * x + 2.0) / (1.625 * x + 1.0)
        b_x = 3.25 * x - 2.0 * math.exp(-0.25 * x) / (1.625 * x + 1.0) + 2.0
        assert 0.0 < a_x <= 6.5 * x <= 1.0
        assert 0.0 < b_x <= 7.0 * x <= 1.0 + 1e-12
        max_a_ratio = max(max_a_ratio, a_x / x)
        max_b_ratio = max(max_b_ratio, b_x / x)

    # Breakdown point under lambda^2 = eps / (4*sigma^2):
    # per-step threshold is log(1 + eps/8 + 1.5*eps) = log(1 + 13*eps/8) < log 2 iff eps < 8/13
    breakdown_eps = 8.0 / 13.0
    assert math.isclose(1.0 + (13.0 / 8.0) * breakdown_eps, 2.0, rel_tol=1e-12)

    # Monte Carlo simulation under Q = (1 - eps)*N(0, 9) + eps*delta_{1000}
    rng = random.Random(20261018)
    sigma = 3.0
    eps = 1.0 / 9.0
    alpha = 0.05
    horizon = 400
    n_trials = 200
    lam = 0.5 * math.sqrt(eps) / sigma
    per_step_log = math.log(1.0 + 0.5 * (lam ** 2) * (sigma ** 2) + 1.5 * eps)

    robust_miscoverage = 0
    nonrobust_catoni_miscoverage = 0
    hoeffding_miscoverage = 0
    terminal_widths_robust: list[float] = []

    for _ in range(n_trials):
        xs: list[float] = []
        rob_failed = False
        cat_failed = False
        hoef_failed = False
        sum_phi_rob_0 = 0.0
        sum_phi_cat_0 = 0.0
        sum_log_cat = 0.0
        sum_x = 0.0

        for t in range(1, horizon + 1):
            if rng.random() < eps:
                x_t = 1000.0
            else:
                x_t = rng.gauss(0.0, sigma)
            xs.append(x_t)

            # Robust Catoni test at true mean mu(P) = 0
            sum_phi_rob_0 += phi_narrow(lam * x_t)
            thresh_rob = t * per_step_log + math.log(2.0 / alpha)
            if abs(sum_phi_rob_0) > thresh_rob:
                rob_failed = True

            # Non-robust Catoni CS (time-decaying lambda_t) at mu(P) = 0
            lam_t_cat = math.sqrt(2.0 * math.log(2.0 / alpha) / ((sigma ** 2) * t * math.log(t + 1.0)))
            sum_phi_cat_0 += phi_wide_unclipped(lam_t_cat * x_t)
            sum_log_cat += 0.5 * (lam_t_cat ** 2) * (sigma ** 2)
            if abs(sum_phi_cat_0) > sum_log_cat + math.log(2.0 / alpha):
                cat_failed = True

            # Sub-Gaussian Hoeffding-style CS at mu(P) = 0
            sum_x += x_t
            rad_hoef = sigma * math.sqrt(2.0 * (t * 0.05 + math.log(2.0 / alpha))) / t
            if abs(sum_x / t) > rad_hoef:
                hoef_failed = True

        if rob_failed:
            robust_miscoverage += 1
        if cat_failed:
            nonrobust_catoni_miscoverage += 1
        if hoef_failed:
            hoeffding_miscoverage += 1

        # Compute terminal robust CI width at t = horizon by bisection
        target_T = horizon * per_step_log + math.log(2.0 / alpha)

        def f_sum(m: float) -> float:
            return sum(phi_narrow(lam * (x - m)) for x in xs)

        lower_m = solve_monotone_root(f_sum, -50.0, 50.0, target_T)
        upper_m = solve_monotone_root(f_sum, -50.0, 1050.0, -target_T)
        terminal_widths_robust.append(upper_m - lower_m)

    emp_miscov_rob = robust_miscoverage / n_trials
    emp_miscov_cat = nonrobust_catoni_miscoverage / n_trials
    emp_miscov_hoef = hoeffding_miscoverage / n_trials
    mean_width_rob = sum(terminal_widths_robust) / len(terminal_widths_robust)
    thm2_bound = 28.0 * sigma * math.sqrt(eps)
    lugosi_mendelson_bound = 96.0 * math.sqrt(2.0) * sigma * math.sqrt(eps)

    assert emp_miscov_rob <= alpha
    assert emp_miscov_cat == 1.0
    assert emp_miscov_hoef == 1.0
    assert mean_width_rob < thm2_bound < lugosi_mendelson_bound

    return {
        "lemma7_max_A_over_x": round(max_a_ratio, 6),
        "lemma7_max_u_over_x": round(max_b_ratio, 6),
        "breakdown_point_varepsilon": round(breakdown_eps, 6),
        "robust_cs_anytime_miscoverage": round(emp_miscov_rob, 4),
        "nonrobust_catoni_cs_anytime_miscoverage": round(emp_miscov_cat, 4),
        "subgaussian_cs_anytime_miscoverage": round(emp_miscov_hoef, 4),
        "mean_terminal_robust_cs_width": round(mean_width_rob, 4),
        "theorem2_high_prob_width_bound": round(thm2_bound, 4),
        "lugosi_mendelson_rci_width_bound": round(lugosi_mendelson_bound, 4),
    }


def verify_section33_tuning_and_corollary1_power() -> dict[str, object]:
    """Compare constant tuning (u=0) vs decaying (u=-0.5, -0.25) and growing (u=+0.5), and verify Corollary 1."""
    rng = random.Random(20261019)
    sigma = 3.0
    eps = 1.0 / 9.0
    alpha = 0.05
    horizon = 600

    xs = [1000.0 if rng.random() < eps else rng.gauss(0.0, sigma) for _ in range(horizon)]

    widths_by_u: dict[str, object] = {}
    for u in (-0.5, -0.25, 0.0, 0.5):
        lams = [0.5 * (math.sqrt(eps) / sigma) * ((i + 1) ** u) for i in range(horizon)]
        target = sum(
            math.log(1.0 + 0.5 * (lams[i] ** 2) * (sigma ** 2) + 1.5 * eps)
            for i in range(horizon)
        ) + math.log(2.0 / alpha)

        if target >= horizon * math.log(2.0):
            widths_by_u[f"u_{u}"] = float("inf")
        else:
            def f_u(m: float) -> float:
                return sum(phi_narrow(lams[i] * (xs[i] - m)) for i in range(horizon))

            lo_m = solve_monotone_root(f_u, -5000.0, 5000.0, target, iters=70)
            hi_m = solve_monotone_root(f_u, -5000.0, 5000.0, -target, iters=70)
            widths_by_u[f"u_{u}"] = hi_m - lo_m

    assert float(widths_by_u["u_0.0"]) < float(widths_by_u["u_-0.25"]) < float(widths_by_u["u_-0.5"])
    assert math.isinf(float(widths_by_u["u_0.5"]))

    # Corollary 1: exponential growth of log M_t^{RC}(mu_0) when mu(P) - mu_0 > 14*sigma*sqrt(eps)
    delta = 0.05
    mu_true = 15.0 * sigma * math.sqrt(eps)
    mu_0 = 0.0
    lam_const = 0.5 * math.sqrt(eps) / sigma
    denom_log = math.log(1.0 + 0.5 * (lam_const ** 2) * (sigma ** 2) + 1.5 * eps)
    log_mart = 0.0
    for i in range(horizon):
        x_shifted = xs[i] + mu_true
        log_mart += phi_narrow(lam_const * (x_shifted - mu_0)) - denom_log
    emp_growth_rate = log_mart / horizon
    cor1_lower_bound = 0.25 * eps - math.log(2.0 / delta) / horizon

    assert emp_growth_rate >= cor1_lower_bound > 0.0

    return {
        "width_u_neg_0_5_decaying": round(float(widths_by_u["u_-0.5"]), 4),
        "width_u_neg_0_25_decaying": round(float(widths_by_u["u_-0.25"]), 4),
        "width_u_0_0_constant": round(float(widths_by_u["u_0.0"]), 4),
        "width_u_pos_0_5_growing_saturated": "infinite_width_target_exceeds_t_log_2",
        "corollary1_empirical_growth_rate": round(emp_growth_rate, 6),
        "corollary1_theoretical_lower_bound": round(cor1_lower_bound, 6),
    }


def verify_section5_extensions() -> dict[str, object]:
    """Verify Section 5.2 infinite-variance p-moment RCS and Section 5.3 bounded Kelly RCS."""
    # Section 5.2: p = 1.5 in (1, 2)
    p = 1.5
    kappa = 4.0
    eps_p = 1.0 / 25.0  # <= (p - 1)/(7*p) = 1/21
    assert eps_p <= (p - 1.0) / (7.0 * p)
    range_p = p - (1.0 / p)
    assert math.isclose(range_p, 5.0 / 6.0, rel_tol=1e-12)

    # Check Lemma 11 bound C < 7*eps_p <= (p - 1)/p for t >= eps_p^{-1}*log(4/(alpha*delta))
    alpha = 0.05
    delta = 0.05
    t_min = math.ceil((1.0 / eps_p) * math.log(4.0 / (alpha * delta))) + 10
    frak_c = (
        1.0
        + 4.0 * eps_p / p
        + (p - 1.0 / p) * eps_p
        - ((4.0 / (alpha * delta)) ** (-1.0 / t_min)) / (1.0 + eps_p / p + (p - 1.0 / p) * eps_p)
    )
    assert 0.0 < frak_c < 7.0 * eps_p <= (p - 1.0) / p
    thm5_width_bound = (14.0 * p / (p - 1.0)) * (kappa ** (1.0 / p)) * (eps_p ** ((p - 1.0) / p))

    # Empirical check of Lemma 5 supermartingale inequality under symmetric Pareto(1.8) + outlier at +500
    rng = random.Random(20261020)
    lam_p = (eps_p / kappa) ** (1.0 / p)
    denom_p = 1.0 + (lam_p ** p) * kappa / p + (p - 1.0 / p) * eps_p
    n_mc = 10000
    acc_p = 0.0
    alpha_tail = 1.8
    for _ in range(n_mc):
        if rng.random() < eps_p:
            x = 500.0
        else:
            u = rng.random()
            pareto_val = (1.0 - u) ** (-1.0 / alpha_tail) - 1.0
            sign = 1.0 if rng.random() < 0.5 else -1.0
            x = sign * pareto_val
        acc_p += math.exp(phi_p_clipped(lam_p * x, p)) / denom_p
    mean_factor_p = acc_p / n_mc
    assert mean_factor_p <= 1.0

    # Section 5.3: Theorem 6 Huber-robust Kelly betting supermartingale on [0, 1]
    # True P = Bernoulli(0.3), contaminated Q = (1 - eps_b)*P + eps_b*delta_1
    mu_b = 0.3
    eps_b = 0.05
    lam_b = 0.8  # inside [-(1 - mu_b + eps_b)^{-1}, (mu_b + eps_b)^{-1}] = [-1.333, 2.857]
    assert -(1.0 / (1.0 - mu_b + eps_b)) <= lam_b <= (1.0 / (mu_b + eps_b))

    # Exact expectation under Q = (1 - eps_b)*Bern(0.3) + eps_b*delta_1
    q_prob_1 = (1.0 - eps_b) * mu_b + eps_b * 1.0
    q_prob_0 = 1.0 - q_prob_1
    factor_at_1 = 1.0 + lam_b * (1.0 - mu_b) - eps_b * abs(lam_b)
    factor_at_0 = 1.0 + lam_b * (0.0 - mu_b) - eps_b * abs(lam_b)
    assert factor_at_0 >= 0.0 and factor_at_1 >= 0.0
    expected_kelly_robust = q_prob_1 * factor_at_1 + q_prob_0 * factor_at_0
    expected_kelly_unadjusted = q_prob_1 * (1.0 + lam_b * (1.0 - mu_b)) + q_prob_0 * (1.0 + lam_b * (0.0 - mu_b))
    assert expected_kelly_robust <= 1.0 + 1e-12
    assert expected_kelly_unadjusted > 1.0

    return {
        "p_moment_exponent": p,
        "p_catoni_exp_range": round(range_p, 6),
        "lemma11_frak_c": round(frak_c, 6),
        "lemma11_seven_eps_bound": round(7.0 * eps_p, 6),
        "theorem5_width_bound": round(thm5_width_bound, 4),
        "p_catoni_supermartingale_factor_mc": round(mean_factor_p, 6),
        "bounded_kelly_robust_expected_factor": round(expected_kelly_robust, 6),
        "bounded_kelly_unadjusted_expected_factor": round(expected_kelly_unadjusted, 6),
    }


def main() -> None:
    report = {
        "concept_id": "AIMech:HuberRobustHeavyTailedConfidenceSequences",
        "lemma1_and_lemma3_verification": verify_lemma1_and_lemma3_supermartingale(),
        "theorem1_theorem2_and_lemma7_verification": verify_theorem1_theorem2_and_lemma7(),
        "section33_and_corollary1_verification": verify_section33_tuning_and_corollary1_power(),
        "section5_extensions_verification": verify_section5_extensions(),
        "all_assertions_passed": True,
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
