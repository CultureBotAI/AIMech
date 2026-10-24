#!/usr/bin/env python3
"""Constructed boundary verification for AIMech:LeftTruncatedCauchyCombinationTest.

Verifies:
1. Unification and boundary limits of the conditional left-truncated Cauchy
   quantile transformation Q(1 - p; p0) = tan(pi * (0.5 - p0 * p)) (Gui, Jiang,
   & Wang 2023, Section 2.2 & Table 1) and the Winsorized/point-mass
   left-truncated Cauchy transformation g^tr(p; delta) = tan(pi * (0.5 - min(p, 1 - delta)))
   (Fang, Chang, Park, & Tseng 2023, Section 2.2):
   - p0 = 0.5 recovers HalfCauchyCombinationTest: tan(pi * (0.5 - 0.5*p)) = cot(pi*p/2) >= 0.
   - p0 -> 1 (or delta -> 0) recovers standard CauchyCombinationTest: tan(pi * (0.5 - p)).
   - For p0 = 0.9 (Gui et al. 2023) and delta = 0.01 (Fang et al. 2023), the
     lower support bound is finite: c = tan(pi * (0.5 - p0)) = -3.0776835 and
     nu_delta = tan(pi * (delta - 0.5)) = -31.820516, preventing unbounded
     negative divergence as p -> 1.
2. Elimination of catastrophic negative score cancellation: when combining
   p_1 = 1e-4 (strong true signal) and p_2 = 1 - 1e-6 (near-one p-value from
   discrete test or anti-correlated one-sided test), standard CCT yields
   T_CCT = -157588.6 < 0 (combined p = 0.999998, complete power collapse),
   whereas both conditional left-truncated Cauchy (p0 = 0.9) and Winsorized
   left-truncated Cauchy (delta = 0.01) preserve high positive test statistics
   and reject at alpha = 1e-3 (combined p < 2.3e-4).
3. Fang et al. (2023) Proposition 4 analytical lower and upper tail bounds and
   Proposition 3 Generalized Central Limit Theorem (GCLT) location-shift
   parameters (f_1n, f_2n, theta_n) for the Winsorized left-truncated Cauchy
   null distribution.
"""

from __future__ import annotations

import json
import math
import random


def standard_cauchy_transform(p: float) -> float:
    return math.tan(math.pi * (0.5 - p))


def cond_left_truncated_cauchy_transform(p: float, p0: float = 0.9) -> float:
    """Gui, Jiang, & Wang (2023), Section 2.2 & Table 1:
    F^{trunc}(x; c) = (F(x) - F(c)) / (1 - F(c)) for x >= c, where 1 - F(c) = p0.
    The inverse survival transformation is Q_F(1 - p0 * p) = tan(pi * (0.5 - p0 * p)).
    """
    if not (0.0 < p0 <= 1.0):
        raise ValueError("p0 must lie in (0, 1].")
    return math.tan(math.pi * (0.5 - p0 * p))


def winsorized_left_truncated_cauchy_transform(p: float, delta: float = 0.01) -> float:
    """Fang, Chang, Park, & Tseng (2023), Section 2.2:
    p^{tr} = min(p, 1 - delta), g^{tr}(p) = tan(pi * (0.5 - p^{tr})).
    """
    if not (0.0 <= delta < 1.0):
        raise ValueError("delta must lie in [0, 1).")
    p_tr = min(p, 1.0 - delta)
    return math.tan(math.pi * (0.5 - p_tr))


def gclt_theta_n(n: int, delta: float = 0.01, n_steps: int = 4000) -> dict[str, float]:
    """Fang, Chang, Park, & Tseng (2023), Proposition 3 GCLT parameters.
    Uses the exact substitution x = tan(u) for u in (pi*(delta - 0.5), pi/2),
    where dx / (1 + x^2) = du.
    """
    nu_delta = math.tan(math.pi * (delta - 0.5))
    u_min = math.pi * (delta - 0.5)
    u_max = 0.5 * math.pi - 1e-9
    h = (u_max - u_min) / n_steps
    f1n = 0.0
    f2n = 0.0
    for k in range(n_steps + 1):
        u = u_min + k * h
        x = math.tan(u)
        w = 1.0 if (k == 0 or k == n_steps) else (4.0 if k % 2 == 1 else 2.0)
        f1n += w * math.cos(x / n)
        f2n += w * math.sin(x / n)
    f1n *= h / 3.0
    f2n *= h / 3.0
    num = delta * math.sin(nu_delta / n) + ((1.0 - delta) / math.pi) * f2n
    den = delta * math.cos(nu_delta / n) + ((1.0 - delta) / math.pi) * f1n
    theta_n = math.atan(num / den)
    return {
        "nu_delta": nu_delta,
        "f1n": f1n,
        "f2n": f2n,
        "theta_n": theta_n,
        "n_theta_n": n * theta_n,
    }


def main() -> None:
    p_grid = [1e-5, 1e-4, 1e-3, 0.01, 0.1, 0.5, 0.9, 0.99, 1.0 - 1e-6]

    # 1. Boundary verification: p0 = 0.5 matches Half-Cauchy; p0 = 1.0 matches standard Cauchy
    max_rel_diff_half_cauchy = max(
        abs(
            cond_left_truncated_cauchy_transform(p, p0=0.5)
            - (1.0 / math.tan(math.pi * p / 2.0))
        )
        / max(1.0, abs(1.0 / math.tan(math.pi * p / 2.0)))
        for p in p_grid
    )
    assert max_rel_diff_half_cauchy < 1e-10

    max_rel_diff_cct = max(
        abs(cond_left_truncated_cauchy_transform(p, p0=1.0) - standard_cauchy_transform(p))
        / max(1.0, abs(standard_cauchy_transform(p)))
        for p in p_grid
    )
    assert max_rel_diff_cct < 1e-10

    c_p09 = cond_left_truncated_cauchy_transform(1.0, p0=0.9)
    nu_delta001 = winsorized_left_truncated_cauchy_transform(1.0, delta=0.01)
    assert -3.1 < c_p09 < -3.07
    assert -31.83 < nu_delta001 < -31.81

    # 2. Elimination of negative penalty cancellation on (p1 = 1e-4, p2 = 1 - 1e-6)
    p_pair = [1e-4, 1.0 - 1e-6]
    t_cct = sum(standard_cauchy_transform(p) for p in p_pair) / len(p_pair)
    p_cct_combined = 0.5 - math.atan(t_cct) / math.pi

    # Conditional left-truncated Cauchy (p0 = 0.9, Gui et al. 2023)
    p0 = 0.9
    t_cond_sum = sum(cond_left_truncated_cauchy_transform(p, p0=p0) for p in p_pair)
    p_cond_combined = min(1.0, 2.0 * (0.5 - math.atan(t_cond_sum) / math.pi) / p0)

    # Winsorized left-truncated Cauchy (delta = 0.01, Fang et al. 2023)
    delta = 0.01
    t_wins_mean = (
        sum(winsorized_left_truncated_cauchy_transform(p, delta=delta) for p in p_pair)
        / len(p_pair)
    )
    p_wins_combined = 0.5 - math.atan(t_wins_mean) / math.pi

    assert t_cct < -1.5e5 and p_cct_combined > 0.99999
    assert t_cond_sum > 3500.0 and p_cond_combined < 2.5e-4
    assert t_wins_mean > 1550.0 and p_wins_combined < 2.5e-4

    # 3. Proposition 4 tail bounds & Monte Carlo verification (n = 10, delta = 0.01)
    rng = random.Random(20261017)
    n_mc = 100000
    n_tests = 10
    t_thresh = 100.0
    hits = 0
    for _ in range(n_mc):
        s = 0.0
        for _ in range(n_tests):
            s += winsorized_left_truncated_cauchy_transform(rng.random(), delta=delta)
        if s / n_tests >= t_thresh:
            hits += 1
    emp_prob = hits / n_mc

    lower_bound_prop4 = 0.5 - math.atan(t_thresh) / math.pi
    sharp_upper_bound_prop4 = 0.0
    for j in range(n_tests):
        shifted_t = (n_tests * t_thresh - j * nu_delta001) / (n_tests - j)
        cauchy_tail = 0.5 - math.atan(shifted_t) / math.pi
        sharp_upper_bound_prop4 += math.comb(n_tests, j) * (delta**j) * cauchy_tail
    binomial_upper_bound_prop4 = (((1.0 + delta) ** n_tests) - (delta**n_tests)) * lower_bound_prop4

    assert lower_bound_prop4 <= sharp_upper_bound_prop4 <= binomial_upper_bound_prop4
    assert abs(emp_prob - lower_bound_prop4) < 5e-4

    # Proposition 3 GCLT parameters for n = 50, delta = 0.01
    gclt_info = gclt_theta_n(n=50, delta=delta)
    assert gclt_info["theta_n"] > 0.0

    summary = {
        "concept_id": "AIMech:LeftTruncatedCauchyCombinationTest",
        "boundary_limits": {
            "max_rel_diff_p0_05_vs_half_cauchy": max_rel_diff_half_cauchy,
            "max_rel_diff_p0_10_vs_standard_cauchy": max_rel_diff_cct,
            "cond_lower_bound_p0_09": c_p09,
            "winsorized_lower_bound_delta_001": nu_delta001,
        },
        "cancellation_immunity_p1_1e-4_p2_1-1e-6": {
            "standard_cct_mean_stat": t_cct,
            "standard_cct_combined_p": p_cct_combined,
            "cond_left_truncated_sum_stat_p0_09": t_cond_sum,
            "cond_left_truncated_combined_p_p0_09": p_cond_combined,
            "winsorized_left_truncated_mean_stat_delta_001": t_wins_mean,
            "winsorized_left_truncated_combined_p_delta_001": p_wins_combined,
        },
        "fang_prop3_prop4_verification": {
            "n_tests": n_tests,
            "t_thresh": t_thresh,
            "prop4_lower_bound": lower_bound_prop4,
            "prop4_sharp_upper_bound": sharp_upper_bound_prop4,
            "prop4_binomial_upper_bound": binomial_upper_bound_prop4,
            "mc_empirical_tail_prob": emp_prob,
            "prop3_gclt_n50_delta001": gclt_info,
        },
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
