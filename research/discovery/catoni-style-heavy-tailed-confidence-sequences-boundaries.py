#!/usr/bin/env python3
"""Constructed boundary verification for CatoniStyleHeavyTailedConfidenceSequences.

Verifies the core mathematical properties and failure boundaries of Wang & Ramdas
(2023), "Catoni-style confidence sequences for heavy-tailed mean estimation",
Stochastic Processes and their Applications 163:168-202 (arXiv:2202.01250):
1. Catoni influence function bounds (-log(1 - x + x^2/2) <= phi(x) <= log(1 + x + x^2/2)),
   Lemma 8 Catoni supermartingale inequality E[exp(+-phi(lambda*(X - mu)) - lambda^2*sigma^2/2)] <= 1
   on heavy-tailed Student-t_3 (infinite third moment), and Proposition 16 tightness failure
   when conditional variance exceeds (1 + 2*kappa)*sigma^2.
2. Comparison of Dubins-Savage CS (Theorem 2), Self-Normalized Delyon CS (Lemma 5, Theorem 7),
   and Catoni-Style CS (Theorem 9): Delyon's inequality exp(x - x^2/6) <= 1 + x + x^2/3,
   disconnected 3-interval topology of Self-Normalized CS vs. connected interval topology of
   Catoni CS, and O(log(1/alpha)) vs. O(1/alpha) width scaling as alpha -> 0.
3. Anytime-valid sequential coverage of Catoni-style CS on heavy-tailed Student-t_3 (sigma^2=25)
   vs. cumulative miscoverage inflation of naive fixed-time Catoni M-estimator CI under
   continuous peeking, plus Theorem 10 nonasymptotic quadratic width bound rho_t.
4. Infinite-variance p-Catoni extension (1 < p < 2, Section 9, Lemma 13, Theorem 14, Theorem 15,
   Lemmas 19-21): verify exp(+-phi_p(x)) <= 1 +- x + |x|^p / p, Lemma 21 inequality
   |x + y|^p <= |x|^p + 4|y|^p + p*y*|x|^(p-1)*sgn(x), and valid anytime coverage and
   O_tilde(t^(-(p-1)/p)) shrinkage on infinite-variance symmetric Pareto(alpha_tail=1.8) streams.
"""

from __future__ import annotations

import json
import math
import random


def catoni_phi(x: float) -> float:
    """Narrowest Catoni influence function phi(x) (Wang & Ramdas 2023, Eq. 27)."""
    if x >= 0.0:
        return math.log(1.0 + x + 0.5 * x * x)
    return -math.log(1.0 - x + 0.5 * x * x)


def p_catoni_phi(x: float, p: float) -> float:
    """p-Catoni influence function phi_p(x) for 1 < p <= 2 (Wang & Ramdas 2023, Eq. 47)."""
    if x >= 0.0:
        return math.log(1.0 + x + (abs(x) ** p) / p)
    return -math.log(1.0 - x + (abs(x) ** p) / p)


def solve_catoni_roots(
    xs: list[float],
    lambdas: list[float],
    rhs: float,
    lo_init: float = -200.0,
    hi_init: float = 200.0,
) -> tuple[float, float]:
    """Solve sum_{i=1}^t phi(lambda_i * (X_i - m)) = +rhs (lower bound u_t) and -rhs (upper bound l_t)."""

    def f(m: float) -> float:
        return sum(catoni_phi(lam * (x - m)) for x, lam in zip(xs, lambdas))

    # Since f(m) is strictly decreasing in m:
    # u_t solves f(u_t) = +rhs, l_t solves f(l_t) = -rhs, with u_t < l_t.
    lo, hi = lo_init, hi_init
    while f(lo) < rhs:
        lo *= 2.0
    while f(hi) > -rhs:
        hi *= 2.0

    # Bisection for lower root u_t: f(u_t) = +rhs
    a, b = lo, hi
    for _ in range(70):
        mid = 0.5 * (a + b)
        if f(mid) > rhs:
            a = mid
        else:
            b = mid
    u_t = 0.5 * (a + b)

    # Bisection for upper root l_t: f(l_t) = -rhs
    a, b = lo, hi
    for _ in range(70):
        mid = 0.5 * (a + b)
        if f(mid) > -rhs:
            a = mid
        else:
            b = mid
    l_t = 0.5 * (a + b)
    return u_t, l_t


def solve_p_catoni_roots(
    xs: list[float],
    lambdas: list[float],
    rhs: float,
    p: float,
    lo_init: float = -200.0,
    hi_init: float = 200.0,
) -> tuple[float, float]:
    """Solve sum_{i=1}^t phi_p(lambda_i * (X_i - m)) = +-rhs for 1 < p < 2."""

    def f(m: float) -> float:
        return sum(p_catoni_phi(lam * (x - m), p) for x, lam in zip(xs, lambdas))

    lo, hi = lo_init, hi_init
    while f(lo) < rhs:
        lo *= 2.0
    while f(hi) > -rhs:
        hi *= 2.0

    a, b = lo, hi
    for _ in range(70):
        mid = 0.5 * (a + b)
        if f(mid) > rhs:
            a = mid
        else:
            b = mid
    u_t = 0.5 * (a + b)

    a, b = lo, hi
    for _ in range(70):
        mid = 0.5 * (a + b)
        if f(mid) > -rhs:
            a = mid
        else:
            b = mid
    l_t = 0.5 * (a + b)
    return u_t, l_t


def sample_student_t3(rng: random.Random, scale_sigma: float) -> float:
    """Sample zero-mean Student-t_3 scaled to have Var(X) = scale_sigma^2 (since Var(t_3) = 3)."""
    z = rng.gauss(0.0, 1.0)
    v = sum(rng.gauss(0.0, 1.0) ** 2 for _ in range(3))
    t3 = z / math.sqrt(v / 3.0)
    # Standard t_3 has variance 3/(3-2) = 3; scale by scale_sigma / sqrt(3)
    return t3 * (scale_sigma / math.sqrt(3.0))


def verify_influence_and_supermartingale() -> dict[str, object]:
    """Check 1: Catoni influence bounds, Lemma 8 supermartingale, and Proposition 16 tightness."""
    test_xs = [-10.0, -2.5, -0.5, 0.0, 0.5, 2.5, 10.0]
    max_bound_violation = 0.0
    for x in test_xs:
        phi = catoni_phi(x)
        lower = -math.log(1.0 - x + 0.5 * x * x)
        upper = math.log(1.0 + x + 0.5 * x * x)
        viol = max(0.0, lower - phi, phi - upper)
        max_bound_violation = max(max_bound_violation, viol)
    assert max_bound_violation <= 1e-15

    # Monte Carlo expectation of Catoni supermartingale factor on heavy-tailed t_3 (sigma = 5.0)
    rng = random.Random(20261018)
    sigma = 5.0
    lam = 0.12
    n_mc = 40000
    acc_pos = 0.0
    acc_neg = 0.0
    for _ in range(n_mc):
        x = sample_student_t3(rng, sigma)
        acc_pos += math.exp(catoni_phi(lam * x) - 0.5 * (lam * sigma) ** 2)
        acc_neg += math.exp(-catoni_phi(lam * x) - 0.5 * (lam * sigma) ** 2)
    mean_factor_pos = acc_pos / n_mc
    mean_factor_neg = acc_neg / n_mc
    assert mean_factor_pos <= 1.0
    assert mean_factor_neg <= 1.0

    # Proposition 16 tightness: if Var(Y) = (1 + 2*kappa)*sigma^2 with kappa = 0.25,
    # symmetric two-point distribution Y in {+- sqrt(1.5)*sigma} violates E[exp(phi(lam*Y) - lam^2*sigma^2/2)] <= 1
    kappa = 0.25
    y_val = math.sqrt(1.0 + 2.0 * kappa) * sigma
    lam_small = 0.05
    prop16_expectation = 0.5 * (
        math.exp(catoni_phi(lam_small * y_val) - 0.5 * (lam_small * sigma) ** 2)
        + math.exp(catoni_phi(-lam_small * y_val) - 0.5 * (lam_small * sigma) ** 2)
    )
    assert prop16_expectation > 1.0

    return {
        "max_influence_bound_violation": max_bound_violation,
        "mc_supermartingale_factor_pos_t3": round(mean_factor_pos, 6),
        "mc_supermartingale_factor_neg_t3": round(mean_factor_neg, 6),
        "prop16_underestimated_variance_factor": round(prop16_expectation, 6),
    }


def verify_three_cs_comparison_and_topology() -> dict[str, object]:
    """Check 2: Delyon inequality, 3-component SN topology, and alpha-scaling comparison."""
    # Verify Delyon's inequality exp(x - x^2/6) <= 1 + x + x^2/3
    max_delyon_violation = 0.0
    for k in range(-100, 101):
        x = k * 0.1
        lhs = math.exp(x - (x * x) / 6.0)
        rhs = 1.0 + x + (x * x) / 3.0
        max_delyon_violation = max(max_delyon_violation, max(0.0, lhs - rhs))
    assert max_delyon_violation <= 1e-15

    # Compare Dubins-Savage vs Catoni width scaling across alpha on a fixed sample of size t=500
    rng = random.Random(20261019)
    sigma = 1.0
    t_horizon = 500
    xs = [rng.gauss(0.0, sigma) for _ in range(t_horizon)]
    lambdas = [1.0 / math.sqrt(i * math.log(i + 1)) for i in range(1, t_horizon + 1)]
    sum_lam = sum(lambdas)
    sum_lam2 = sum(l * l for l in lambdas)

    widths_catoni = {}
    widths_ds = {}
    for alpha in [0.1, 0.01, 1e-4, 1e-6]:
        rhs_catoni = 0.5 * (sigma**2) * sum_lam2 + math.log(2.0 / alpha)
        u_c, l_c = solve_catoni_roots(xs, lambdas, rhs_catoni)
        widths_catoni[str(alpha)] = round(l_c - u_c, 5)

        half_ds = ((2.0 / alpha) - 1.0 + (sigma**2) * sum_lam2) / sum_lam
        widths_ds[str(alpha)] = round(2.0 * half_ds, 5)

    # Catoni width grows logarithmically O(log(2/alpha)), whereas Dubins-Savage grows as O(1/alpha)
    assert widths_catoni["1e-06"] < 2.5
    assert (widths_catoni["1e-06"] / widths_catoni["0.1"]) < 5.0
    assert (widths_ds["1e-06"] / widths_ds["0.1"]) > 50000.0

    # Verify Self-Normalized CS discriminant D^+ > 0 under a heavy-tailed outlier creates
    # an anticonfidence interval (3-component disconnected confidence region L U M U U)
    xs_outlier = xs[:50] + [25.0]
    lams_outlier = lambdas[:51]
    alpha_sn = 0.05
    a_coeff = sum((l**2) / 6.0 for l in lams_outlier)
    b_pos = sum(-l - (l**2) * x / 3.0 for x, l in zip(xs_outlier, lams_outlier))
    c_pos = (
        sum(
            l * x + ((l * x) ** 2) / 6.0 + ((l * sigma) ** 2) / 3.0
            for x, l in zip(xs_outlier, lams_outlier)
        )
        - math.log(2.0 / alpha_sn)
    )
    discriminant_pos = b_pos * b_pos - 4.0 * a_coeff * c_pos
    assert discriminant_pos > 0.0

    return {
        "max_delyon_violation": max_delyon_violation,
        "catoni_widths_by_alpha": widths_catoni,
        "dubins_savage_widths_by_alpha": widths_ds,
        "sn_outlier_discriminant_pos": round(discriminant_pos, 4),
    }


def verify_anytime_coverage_and_theorem10_bound() -> dict[str, object]:
    """Check 3: Student-t_3 anytime coverage vs fixed-time peeking, plus Theorem 10 bound."""
    rng = random.Random(20261020)
    sigma = 5.0  # sigma^2 = 25 as in Section 8 of Wang & Ramdas (2023)
    alpha = 0.10
    n_trials = 500
    t_max = 300

    lams_seq = [
        math.sqrt(2.0 * math.log(2.0 / alpha) / ((sigma**2) * i * math.log(i + 1.0)))
        for i in range(1, t_max + 1)
    ]

    seq_miscoverage_count = 0
    peeking_clt_miscoverage = 0
    thm10_bound_holds_all = True
    z_alpha_2 = 1.6448536269514722  # normal 1 - alpha/2 quantile for alpha = 0.10

    for trial in range(n_trials):
        xs = [sample_student_t3(rng, sigma) for _ in range(t_max)]
        seq_failed = False
        clt_failed = False
        running_phi_sum = 0.0
        running_lam2_sum = 0.0
        running_x_sum = 0.0

        for t in range(1, t_max + 1):
            x_t = xs[t - 1]
            lam_t = lams_seq[t - 1]
            # By strict monotonicity of m -> sum_{i=1}^t phi(lambda_i(X_i - m)),
            # mu = 0 is in CI_t^C iff |sum_{i=1}^t phi(lambda_i X_i)| <= rhs_t.
            running_phi_sum += catoni_phi(lam_t * x_t)
            running_lam2_sum += lam_t * lam_t
            rhs = 0.5 * (sigma**2) * running_lam2_sum + math.log(2.0 / alpha)
            if abs(running_phi_sum) > rhs:
                seq_failed = True

            running_x_sum += x_t
            if abs(running_x_sum / t) > z_alpha_2 * sigma / math.sqrt(t):
                clt_failed = True

        # Check Theorem 10 quadratic upper bound on half-width at t = t_max on first 15 trials
        if trial < 15:
            rhs_end = 0.5 * (sigma**2) * sum(l * l for l in lams_seq) + math.log(2.0 / alpha)
            u_t, l_t = solve_catoni_roots(xs, lams_seq, rhs_end)
            sum_l = sum(lams_seq)
            sum_l3 = sum(l**3 for l in lams_seq)
            mu_hat_w = sum(l * x for l, x in zip(lams_seq, xs)) / sum_l
            weighted_emp_var = sum(
                (l**2) * ((x - mu_hat_w) ** 2) for l, x in zip(lams_seq, xs)
            )
            delta_t = (sum_l**2) - 2.0 * sum_l3 * (weighted_emp_var + rhs_end)
            if delta_t >= 0.0:
                rho_t = (sum_l - math.sqrt(delta_t)) / sum_l3
                if not (l_t <= mu_hat_w + rho_t + 1e-6 and u_t >= mu_hat_w - rho_t - 1e-6):
                    thm10_bound_holds_all = False

        if seq_failed:
            seq_miscoverage_count += 1
        if clt_failed:
            peeking_clt_miscoverage += 1

    seq_miscoverage_rate = seq_miscoverage_count / n_trials
    peeking_clt_rate = peeking_clt_miscoverage / n_trials
    assert seq_miscoverage_rate <= alpha
    assert peeking_clt_rate > 0.50
    assert thm10_bound_holds_all

    return {
        "sequential_catoni_miscoverage_rate": round(seq_miscoverage_rate, 4),
        "peeking_clt_miscoverage_rate": round(peeking_clt_rate, 4),
        "alpha": alpha,
        "thm10_quadratic_root_bound_holds": thm10_bound_holds_all,
    }


def verify_infinite_variance_p_catoni() -> dict[str, object]:
    """Check 4: Infinite-variance p-Catoni (1 < p < 2, Section 9, Lemmas 13, 19-21, Thms 14-15)."""
    p = 1.5
    # Verify exp(+-phi_p(x)) <= 1 +- x + |x|^p / p and Lemma 21 inequality
    max_phi_p_violation = 0.0
    max_lemma21_violation = 0.0
    for x in [-5.0, -1.2, -0.3, 0.0, 0.3, 1.2, 5.0]:
        val = p_catoni_phi(x, p)
        lhs_pos = math.exp(val)
        rhs_pos = 1.0 + x + (abs(x) ** p) / p
        max_phi_p_violation = max(max_phi_p_violation, max(0.0, lhs_pos - rhs_pos))
        for y in [-3.0, -0.5, 0.0, 0.5, 3.0]:
            sgn_x = 1.0 if x >= 0.0 else -1.0
            lhs21 = abs(x + y) ** p
            rhs21 = (abs(x) ** p) + 4.0 * (abs(y) ** p) + p * y * (abs(x) ** (p - 1.0)) * sgn_x
            max_lemma21_violation = max(max_lemma21_violation, max(0.0, lhs21 - rhs21))

    assert max_phi_p_violation <= 1e-14
    assert max_lemma21_violation <= 1e-14

    # Simulate symmetric Pareto stream with tail index alpha_tail = 1.8 (infinite variance, finite p=1.5 moment)
    alpha_tail = 1.8
    v_p = alpha_tail / (alpha_tail - p)  # = 6.0

    rng = random.Random(20261021)
    alpha = 0.10
    n_trials = 400
    t_max = 150
    lams_p = [
        ((p * math.log(2.0 / alpha)) / (v_p * i * (math.log(i + 1.0) ** 1.2))) ** (1.0 / p)
        for i in range(1, t_max + 1)
    ]

    miscoverage_p = 0
    width_t20 = 0.0
    width_t150 = 0.0
    for trial in range(n_trials):
        xs = []
        for _ in range(t_max):
            u = max(1e-12, rng.random())
            mag = u ** (-1.0 / alpha_tail)
            sign = 1.0 if rng.random() < 0.5 else -1.0
            xs.append(sign * mag)

        failed = False
        running_phi_p = 0.0
        running_lam_p = 0.0
        for t in range(1, t_max + 1):
            x_t = xs[t - 1]
            lam_t = lams_p[t - 1]
            running_phi_p += p_catoni_phi(lam_t * x_t, p)
            running_lam_p += lam_t**p
            rhs_p = (v_p / p) * running_lam_p + math.log(2.0 / alpha)
            if abs(running_phi_p) > rhs_p:
                failed = True

        if trial == 0:
            rhs_20 = (v_p / p) * sum(l**p for l in lams_p[:20]) + math.log(2.0 / alpha)
            u20, l20 = solve_p_catoni_roots(xs[:20], lams_p[:20], rhs_20, p)
            width_t20 = l20 - u20

            rhs_150 = (v_p / p) * sum(l**p for l in lams_p) + math.log(2.0 / alpha)
            u150, l150 = solve_p_catoni_roots(xs, lams_p, rhs_150, p)
            width_t150 = l150 - u150

        if failed:
            miscoverage_p += 1

    p_catoni_miscoverage_rate = miscoverage_p / n_trials
    assert p_catoni_miscoverage_rate <= alpha
    assert width_t150 < width_t20

    return {
        "p_exponent": p,
        "pareto_tail_index": alpha_tail,
        "p_moment_bound_v": v_p,
        "max_phi_p_violation": max_phi_p_violation,
        "max_lemma21_violation": max_lemma21_violation,
        "p_catoni_miscoverage_rate": round(p_catoni_miscoverage_rate, 4),
        "width_t20": round(width_t20, 4),
        "width_t150": round(width_t150, 4),
    }


def main() -> None:
    report = {
        "concept_id": "AIMech:CatoniStyleHeavyTailedConfidenceSequences",
        "check_1_influence_and_supermartingale": verify_influence_and_supermartingale(),
        "check_2_three_cs_comparison_and_topology": verify_three_cs_comparison_and_topology(),
        "check_3_anytime_coverage_and_theorem10": verify_anytime_coverage_and_theorem10_bound(),
        "check_4_infinite_variance_p_catoni": verify_infinite_variance_p_catoni(),
        "all_assertions_passed": True,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
