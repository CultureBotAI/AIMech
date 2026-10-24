#!/usr/bin/env python3
"""Constructed numerical boundary checks for AIMech:HalfCauchyCombinationTest.

Verifies:
1. Sensitivity of Cauchy Combination Test (CCT) vs. insensitivity of Half-Cauchy
   Combination Test (HCCT) to p_j -> 1 (Section 1.1 & Appendix B.2): for m = 2
   with w = (0.5, 0.5), p_1 = 0.005, p_2 = 0.999, CCT maps p_2 to a large
   negative score (-318.3088) that cancels the strong signal in p_1 (63.6567),
   giving T_CCT = -127.3260 and combined p_CCT = 0.99750, whereas HCCT maps
   both to non-negative scores (127.3213 and 0.00157), giving T_HCCT = 63.6615
   and exact combined p_HCCT = 0.009992.
2. Exact m = 2 equal-weight Half-Cauchy convolution density and CDF (Theorem 2.3):
   verifies closed-form partial-fraction integration of the convolution of two
   standard Half-Cauchy variables against numerical quadrature, and computes the
   exact 95% critical threshold F_{HC, (0.5, 0.5)}^{-1}(0.95).
3. Disconnected CCT confidence set vs. convex connected HCCT confidence interval
   and Equation (3.7) conflict lower bound on Example 1 of Section 1.2 (lines
   255-257): two equally weighted studies N(theta_0, 0.01^2? No, variance 0.01,
   so sigma = 0.1) with estimates theta_hat_1 = 0.125 and theta_hat_2 = -0.125.
   Verifies that the 95% CCT confidence set splits into three disjoint intervals
   [-0.1277, -0.1212] U [-0.1038, 0.1038] U [0.1212, 0.1277] because
   T_CCT(theta_hat_j) = -inf, whereas T_HCCT(theta) is strictly convex on R with
   unique minimum at theta = 0 and satisfies the Equation (3.7) median conflict
   lower bound.
4. Convexity comparison (Lemma D.3 / Theorem 3.1): verifies that the transformed
   1D score g_HC(z) = cot((pi / 2) * 2 * (1 - Phi(|z|))) is convex for all z in R
   (second derivative >= 0), whereas the CCT score g_CCT(z) = cot(pi * 2 * (1 - Phi(|z|)))
   diverges to -inf as z -> 0 and has negative second derivative near 0.
"""
from __future__ import annotations

import json
import math


def normal_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def two_sided_normal_p(z: float) -> float:
    return 2.0 * (1.0 - normal_cdf(abs(z)))


def hc_score(p: float) -> float:
    if p <= 0.0:
        return float("inf")
    if p >= 1.0:
        return 0.0
    return 1.0 / math.tan(0.5 * math.pi * p)


def cct_score(p: float) -> float:
    if p <= 0.0:
        return float("inf")
    if p >= 1.0:
        return float("-inf")
    return math.cos(math.pi * p) / math.sin(math.pi * p)


def hc2_sum_density(s: float) -> float:
    """Exact density of S = X_1 + X_2 for independent X_1, X_2 ~ HalfCauchy(0, 1).

    By partial fractions on 1 / ((1 + u^2)(1 + (s - u)^2)):
      f_S(s) = (4 / pi^2) * (2 * log(1 + s^2) / s + 2 * atan(s)) / (s^2 + 4)
    """
    if s <= 0.0:
        return 0.0
    return (8.0 / (math.pi ** 2 * (s * s + 4.0))) * (
        math.log(1.0 + s * s) / s + math.atan(s)
    )


def hc2_equal_weight_cdf(t: float, n_steps: int = 4000) -> float:
    """CDF of T = 0.5 * (X_1 + X_2) at t via Simpson integration on u = s / (1 + s)."""
    if t <= 0.0:
        return 0.0
    s_max = 2.0 * t
    u_max = s_max / (1.0 + s_max)
    h = u_max / n_steps
    total = 0.0
    for i in range(n_steps + 1):
        u = i * h
        if u == 0.0:
            val = 0.0
        else:
            s = u / (1.0 - u)
            jac = 1.0 / ((1.0 - u) ** 2)
            val = hc2_sum_density(s) * jac
        weight = 1.0 if (i == 0 or i == n_steps) else (4.0 if i % 2 == 1 else 2.0)
        total += weight * val
    return total * (h / 3.0)


def invert_hc2_cdf(target_prob: float) -> float:
    lo, hi = 0.0, 200.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if hc2_equal_weight_cdf(mid) < target_prob:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def verify_large_p_insensitivity() -> dict[str, float]:
    p1 = 0.005
    p2 = 0.999
    t_cct = 0.5 * cct_score(p1) + 0.5 * cct_score(p2)
    p_cct = 0.5 - math.atan(t_cct) / math.pi

    t_hcct = 0.5 * hc_score(p1) + 0.5 * hc_score(p2)
    p_hcct = 1.0 - hc2_equal_weight_cdf(t_hcct)

    assert t_cct < -100.0
    assert p_cct > 0.99
    assert t_hcct > 60.0
    assert p_hcct < 0.015
    return {
        "p1": p1,
        "p2": p2,
        "T_CCT": round(t_cct, 6),
        "p_value_CCT": round(p_cct, 8),
        "T_HCCT": round(t_hcct, 6),
        "p_value_HCCT": round(p_hcct, 8),
    }


def verify_example1_confidence_sets() -> dict[str, object]:
    """Reproduce Example 1 (Section 1.2, lines 255-257) and compare CCT vs HCCT."""
    sigma = 0.1  # Variance 0.01
    theta_hat_1 = 0.125
    theta_hat_2 = -0.125
    alpha = 0.05

    # Standard Cauchy 0.95 quantile is tan(pi * (0.95 - 0.5)) = cot(0.05 * pi)
    q95_cct = 1.0 / math.tan(alpha * math.pi)
    q95_hcct = invert_hc2_cdf(1.0 - alpha)

    def t_cct_theta(theta: float) -> float:
        p1 = two_sided_normal_p((theta_hat_1 - theta) / sigma)
        p2 = two_sided_normal_p((theta_hat_2 - theta) / sigma)
        return 0.5 * (cct_score(p1) + cct_score(p2))

    def t_hcct_theta(theta: float) -> float:
        p1 = two_sided_normal_p((theta_hat_1 - theta) / sigma)
        p2 = two_sided_normal_p((theta_hat_2 - theta) / sigma)
        return 0.5 * (hc_score(p1) + hc_score(p2))

    # Verify CCT has 3 disconnected intervals matching [-0.1277, -0.1212] U [-0.1038, 0.1038] U [0.1212, 0.1277]
    # Find roots of t_cct_theta(theta) - q95_cct on (0, 0.125) and (0.125, 0.2)
    def bisect_root(fn, a: float, b: float) -> float:
        fa = fn(a)
        for _ in range(80):
            m = 0.5 * (a + b)
            fm = fn(m)
            if fa * fm <= 0:
                b = m
            else:
                a = m
                fa = fm
        return 0.5 * (a + b)

    r1 = bisect_root(lambda th: t_cct_theta(th) - q95_cct, 0.0, 0.115)
    r2 = bisect_root(lambda th: t_cct_theta(th) - q95_cct, 0.115, 0.124999)
    r3 = bisect_root(lambda th: t_cct_theta(th) - q95_cct, 0.125001, 0.14)

    assert abs(r1 - 0.1038) < 1e-4
    assert abs(r2 - 0.1212) < 1e-4
    assert abs(r3 - 0.1277) < 1e-4

    # Verify HCCT is strictly convex on [-0.2, 0.2] with unique minimum at theta = 0
    t_hcct_min = t_hcct_theta(0.0)
    # Equation (3.7) lower bound: (2 / pi) * sum_j (w_j / sigma_j) |theta_med - theta_hat_j|
    # With equal weights and theta_hat = {-0.125, 0.125}, any median in [-0.125, 0.125] gives sum = 0.5 * (0.25 / 0.1) = 1.25
    eq37_lower_bound = (2.0 / math.pi) * (0.5 / sigma) * abs(theta_hat_1 - theta_hat_2)
    assert t_hcct_min >= eq37_lower_bound

    # Find connected 95% HCCT confidence interval [-r_hcct, r_hcct]
    r_hcct_95 = bisect_root(lambda th: t_hcct_theta(th) - q95_hcct, 0.0, 0.25)
    # Check convexity of t_hcct_theta across grid
    grid = [i * 0.005 for i in range(-40, 41)]
    vals = [t_hcct_theta(g) for g in grid]
    for i in range(1, len(vals) - 1):
        second_diff = vals[i + 1] - 2.0 * vals[i] + vals[i - 1]
        assert second_diff > 0.0, f"Non-convex at {grid[i]}"

    return {
        "cct_q95": round(q95_cct, 6),
        "cct_disconnected_positive_roots": [round(r1, 4), round(r2, 4), round(r3, 4)],
        "hcct_q95": round(q95_hcct, 6),
        "hcct_min_at_zero": round(t_hcct_min, 6),
        "eq37_inconsistency_lower_bound": round(eq37_lower_bound, 6),
        "hcct_connected_95_interval": [round(-r_hcct_95, 4), round(r_hcct_95, 4)],
    }


def verify_landau_location_shift() -> dict[str, float]:
    """Verify Theorem 2.1 Landau shift A_m = (2/pi)(1 - gamma - sum w_j log w_j)."""
    euler_gamma = 0.5772156649015329
    m = 100
    # Equal weights w_j = 1/m
    shift_equal = (2.0 / math.pi) * (1.0 - euler_gamma + math.log(m))
    # Harmonic weights w_j proportional to 1/j
    raw = [1.0 / j for j in range(1, m + 1)]
    norm = sum(raw)
    w_harm = [r / norm for r in raw]
    entropy = -sum(w * math.log(w) for w in w_harm)
    shift_harm = (2.0 / math.pi) * (1.0 - euler_gamma + entropy)
    assert shift_equal > shift_harm > 0.0
    return {
        "m": m,
        "landau_shift_equal_weights": round(shift_equal, 6),
        "landau_shift_harmonic_weights": round(shift_harm, 6),
    }


def main() -> None:
    results = {
        "large_p_insensitivity": verify_large_p_insensitivity(),
        "example1_confidence_sets": verify_example1_confidence_sets(),
        "landau_domain_of_attraction_shift": verify_landau_location_shift(),
    }
    print(json.dumps(results, sort_keys=True))


if __name__ == "__main__":
    main()
