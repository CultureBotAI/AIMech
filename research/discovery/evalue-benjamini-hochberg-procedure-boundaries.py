#!/usr/bin/env python3
"""Constructed boundary verification for AIMech:EValueBenjaminiHochbergProcedure.

Verifies the mathematical properties of the e-BH procedure from:
  Wang, R. and Ramdas, A. (2022). False discovery rate control with e-values.
  Journal of the Royal Statistical Society: Series B (Statistical Methodology),
  84(3):822-852. (arXiv:2009.02824).

Specifically checks:
  1. Base e-BH step-down rejection rule (Eq. 5) and threshold equivalence t_alpha
     (Eq. 6, Proposition 1), plus self-consistent post-selection e-BH (Section 5.1).
  2. Arbitrary-dependence FDR bound alpha * K_0 / K (Theorem 2, Proposition 2)
     and exact attainment on the Example 4 extremal configuration.
  3. Truncation function T(x) (Eq. 7) and boosting factors b_k under arbitrary
     dependence (Eq. 9, Theorem 3, Examples 2 & 3) vs. PRDS (Eq. 8, Theorem 4,
     Proposition 3, Examples 5 & 6).
  4. Optimality of base e-BH among monotone transform procedures G(phi)
     (Theorem 5) and unification of BH and BY via p-to-e calibration
     (Proposition 4).
"""

from __future__ import annotations

import json
import math


def std_norm_cdf(z: float) -> float:
    """Standard Gaussian cumulative distribution function Phi(z)."""
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def truncation_T(x: float, k_total: int) -> float:
    """Grid truncation T(x) = max{K/k : k in {1,...,K}, K/k <= x} (Eq. 7)."""
    if x < 1.0:
        return 0.0
    if x >= float(k_total):
        return float(k_total)
    # Largest K/k <= x corresponds to smallest integer k >= K/x
    k_idx = math.ceil(k_total / x - 1e-15)
    k_idx = max(1, min(k_total, k_idx))
    val = k_total / k_idx
    if val > x + 1e-12 and k_idx < k_total:
        k_idx += 1
        val = k_total / k_idx
    return val


def base_ebh_stepdown(e_values: list[float], alpha: float) -> tuple[int, list[int], float]:
    """Run base e-BH (Eq. 5) and compute threshold t_alpha (Eq. 6, Proposition 1)."""
    k_total = len(e_values)
    indexed = sorted(enumerate(e_values), key=lambda item: item[1], reverse=True)
    k_star = 0
    for rank_1based, (_, val) in enumerate(indexed, start=1):
        if rank_1based * val / k_total >= 1.0 / alpha - 1e-12:
            k_star = rank_1based
    rejected_stepdown = sorted(idx for idx, _ in indexed[:k_star])

    # Proposition 1 threshold t_alpha = inf{t >= 0 : t * R(t) / K >= 1 / alpha}
    # Since R(t) = max(sum 1_{e'_k >= t}, 1) is piecewise constant on intervals,
    # t_alpha equals K / (alpha * max(k_star, 1)).
    r_at_threshold = max(k_star, 1)
    t_alpha = k_total / (alpha * r_at_threshold)
    rejected_threshold = sorted(
        idx for idx, val in enumerate(e_values) if val >= t_alpha - 1e-12
    )
    assert rejected_stepdown == rejected_threshold
    return k_star, rejected_stepdown, t_alpha


def verify_stepdown_and_postselection() -> dict[str, object]:
    """Verify Proposition 1 equivalence and Section 5.1 post-selection e-BH."""
    alpha = 0.05
    e_vec = [0.5, 18.0, 26.0, 35.0, 120.0]
    k_star, rejected, t_alpha = base_ebh_stepdown(e_vec, alpha)
    # K = 5, alpha = 0.05 => K/alpha = 100.
    # Sorted: 120.0 (k=1, thresh=100), 35.0 (k=2, thresh=50), 26.0 (k=3, thresh=33.33),
    # 18.0 (k=4, thresh=25). Wait: let's also test a vector where k_star = 3!
    e_vec_2 = [0.8, 12.0, 34.0, 55.0, 90.0]
    # Sorted: 90.0 (<100), 55.0 (>=50, k=2), 34.0 (>=33.333, k=3), 12.0 (<25, k=4)
    # Notice k=1 has 90 < 100, while k=3 has 34 >= 33.333! Step-down rejects k=1,2,3!
    k_star_2, rejected_2, t_alpha_2 = base_ebh_stepdown(e_vec_2, alpha)
    assert k_star_2 == 3
    assert rejected_2 == [2, 3, 4]
    assert abs(t_alpha_2 - (5.0 / (0.05 * 3))) < 1e-9

    # Post-selection e-BH on screened subset S = {1, 2, 3, 4} (|S| = 4 out of K = 5)
    s_indices = [1, 2, 3, 4]
    alpha_tilde = alpha * len(s_indices) / len(e_vec_2)
    s_evalues = [e_vec_2[i] for i in s_indices]
    k_star_s, rej_s_local, _ = base_ebh_stepdown(s_evalues, alpha_tilde)
    rej_s_global = [s_indices[i] for i in rej_s_local]
    # Check self-consistency condition e_k >= K / (alpha * R) for all rejected
    for idx in rej_s_global:
        assert e_vec_2[idx] >= len(e_vec_2) / (alpha * k_star_s) - 1e-12

    return {
        "test_vector": e_vec_2,
        "alpha": alpha,
        "k_star": k_star_2,
        "rejected_0based": rejected_2,
        "t_alpha": round(t_alpha_2, 6),
        "post_selection_subset_size": len(s_indices),
        "post_selection_amended_alpha": round(alpha_tilde, 6),
        "post_selection_rejected_0based": rej_s_global,
    }


def verify_example_4_sharpness() -> dict[str, object]:
    """Verify Example 4 sharpness of Theorem 2/3 arbitrary-dependence FDR bound."""
    k_total = 5
    k_null = 3
    alpha = 0.05
    prob_a = alpha * k_null / k_total  # 0.03
    e_null_on_a = k_total / (k_null * alpha)  # 100 / 3 = 33.333333...

    # State 1: event A occurs with probability prob_a
    e_vec_a = [e_null_on_a] * k_null + [0.0] * (k_total - k_null)
    k_star_a, rej_a, _ = base_ebh_stepdown(e_vec_a, alpha)
    fdp_a = sum(1 for idx in rej_a if idx < k_null) / max(len(rej_a), 1)

    # State 2: complement A^c occurs with probability 1 - prob_a
    e_vec_ac = [0.0] * k_total
    k_star_ac, rej_ac, _ = base_ebh_stepdown(e_vec_ac, alpha)
    fdp_ac = 0.0

    null_expectation = prob_a * e_null_on_a + (1.0 - prob_a) * 0.0
    exact_fdr = prob_a * fdp_a + (1.0 - prob_a) * fdp_ac
    theoretical_bound = alpha * k_null / k_total

    assert abs(null_expectation - 1.0) < 1e-12
    assert k_star_a == k_null
    assert k_star_ac == 0
    assert abs(exact_fdr - theoretical_bound) < 1e-12

    return {
        "K": k_total,
        "K0": k_null,
        "alpha": alpha,
        "null_e_value_expectation": round(null_expectation, 6),
        "exact_fdr": round(exact_fdr, 6),
        "theoretical_upper_bound": round(theoretical_bound, 6),
    }


def verify_boosting_examples() -> dict[str, object]:
    """Verify boosting factors in Examples 2, 3, 5, and 6."""
    alpha = 0.05
    lam = 0.5

    # Example 2: power calibrator E_k = lambda * P_k^{lambda - 1} under arbitrary dependence
    # y_bar(b) = (lambda^lambda * alpha * b)^{1/(1-lambda)} = (alpha * b)^2 / 2 = alpha
    b_ex2_ad = math.sqrt(2.0 / alpha)
    y_bar_ex2 = 0.5 * (alpha * b_ex2_ad) ** 2
    assert abs(y_bar_ex2 - alpha) < 1e-12

    # Also verify exact K-dependent y_alpha(b) = E[T(alpha * b * E_k)] <= y_bar(b) for K = 100
    k_grid = 100
    # E_k = 0.5 * P^{-0.5} >= K / (alpha * b * j) <=> P <= (0.5 * alpha * b * j / K)^2
    y_exact_k100 = 0.0
    for j in range(1, k_grid + 1):
        p_upper = min(1.0, (0.5 * alpha * b_ex2_ad * j / k_grid) ** 2)
        p_lower = (
            min(1.0, (0.5 * alpha * b_ex2_ad * (j - 1) / k_grid) ** 2)
            if j > 1
            else 0.0
        )
        y_exact_k100 += (k_grid / j) * (p_upper - p_lower)
    assert y_exact_k100 <= y_bar_ex2 + 1e-12

    # Example 5: power calibrator under PRDS (Proposition 3)
    # b = lambda^{-1} * alpha^{-lambda}
    b_ex5_prds = (1.0 / lam) * (alpha ** (-lam))
    q_1_minus_alpha = lam * (alpha ** (lam - 1.0))
    z_ex5 = (lam * alpha * b_ex5_prds) ** (1.0 / (1.0 - lam))
    y_bar_at_b_ex5 = ((lam**lam) * alpha * b_ex5_prds) ** (1.0 / (1.0 - lam))
    assert abs(b_ex5_prds - 1.0 / (alpha * q_1_minus_alpha)) < 1e-12
    assert abs(z_ex5 - alpha) < 1e-12
    assert abs(z_ex5 / y_bar_at_b_ex5 - lam) < 1e-12

    # Example 3: Gaussian likelihood ratio E_k = exp(delta * X_k - delta^2 / 2) under AD
    # By Girsanov change of measure to N(delta, 1):
    # y_bar(b) = alpha * b * E[E_k 1_{alpha * b * E_k >= 1}]
    #          = alpha * b * Phi(delta/2 + ln(alpha * b)/delta) = alpha
    # <=> b * Phi(delta/2 + ln(alpha * b)/delta) = 1 (Eq. 20)
    ex3_ad_results = {}
    for delta in (3.0, 4.0):
        lo, hi = 1.0, 20.0
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            lhs = mid * std_norm_cdf(0.5 * delta + math.log(alpha * mid) / delta)
            if lhs < 1.0:
                lo = mid
            else:
                hi = mid
        ex3_ad_results[f"delta_{int(delta)}"] = round(0.5 * (lo + hi), 6)

    # Example 6: Gaussian likelihood ratio under PRDS
    # z_bar(b) = sup_{x >= 1} x * P(alpha * b * E_k >= x)
    #          = sup_{x >= 1} x * (1 - Phi(delta/2 + ln(x / (alpha * b)) / delta)) = alpha
    ex6_prds_results = {}
    for delta in (3.0, 4.0):
        lo, hi = 1.0, 30.0
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            # Evaluate sup_{x >= 1} over a dense log-grid of x in [1, 500]
            sup_val = 0.0
            for idx in range(2001):
                x_val = math.exp(idx * math.log(500.0) / 2000.0)
                z_arg = 0.5 * delta + math.log(x_val / (alpha * mid)) / delta
                val = x_val * (1.0 - std_norm_cdf(z_arg))
                if val > sup_val:
                    sup_val = val
            if sup_val < alpha:
                lo = mid
            else:
                hi = mid
        ex6_prds_results[f"delta_{int(delta)}"] = round(0.5 * (lo + hi), 6)

    assert abs(ex3_ad_results["delta_3"] - 1.37) < 0.01
    assert abs(ex3_ad_results["delta_4"] - 1.11) < 0.01
    assert abs(ex6_prds_results["delta_3"] - 7.88) < 0.02
    assert abs(ex6_prds_results["delta_4"] - 10.31) < 0.02

    return {
        "example_2_power_ad_b": round(b_ex2_ad, 6),
        "example_2_exact_y_alpha_K100": round(y_exact_k100, 6),
        "example_5_power_prds_b": round(b_ex5_prds, 6),
        "example_3_gaussian_ad_b": ex3_ad_results,
        "example_6_gaussian_prds_b": ex6_prds_results,
    }


def verify_optimality_and_calibration() -> dict[str, object]:
    """Verify Theorem 5 optimality counterexample and Proposition 4 BH/BY unification."""
    k_total = 6
    alpha = 0.05
    # Suppose an increasing transform phi violates phi^{-1}(K/k0) >= K/(k0 * alpha) at k0 = 2.
    # Standard e-BH has threshold K/(k0 * alpha) = 6 / (2 * 0.05) = 60.0.
    # If phi^{-1}(3) = 40.0 < 60.0, take m' = 45.0 in [40.0, 60.0).
    k0 = 2
    ebh_threshold_k0 = k_total / (k0 * alpha)
    m_prime = 45.0
    prob_a = k_total / (k0 * m_prime)  # 6 / 90 = 1/15 = 0.066667 > 0.05
    # Each null E_k takes value m' with probability 1/m' (since k0/K * P(A) = 1/m')
    null_mean = m_prime * (1.0 / m_prime)
    assert abs(null_mean - 1.0) < 1e-12
    assert prob_a > alpha

    # Proposition 4: psi(p) = alpha / p gives BH procedure D(alpha)
    # y_psi = E[T(alpha / P)] for P ~ Unif[0, 1]
    # T(alpha / p) = K / k when K / k <= alpha / p < K / (k - 1), i.e.,
    # p in (alpha * (k - 1) / K, alpha * k / K].
    y_psi = 0.0
    for k in range(1, k_total + 1):
        p_interval_len = (alpha * k / k_total) - (alpha * (k - 1) / k_total)
        y_psi += (k_total / k) * p_interval_len
    harmonic_lk = sum(1.0 / k for k in range(1, k_total + 1))
    assert abs(y_psi - alpha * harmonic_lk) < 1e-12

    return {
        "theorem_5_k0": k0,
        "theorem_5_ebh_threshold": round(ebh_threshold_k0, 6),
        "theorem_5_violating_m_prime": m_prime,
        "theorem_5_induced_fdr": round(prob_a, 6),
        "proposition_4_K": k_total,
        "proposition_4_harmonic_l_K": round(harmonic_lk, 6),
        "proposition_4_y_psi": round(y_psi, 6),
        "proposition_4_alpha_times_l_K": round(alpha * harmonic_lk, 6),
    }


def main() -> None:
    report = {
        "stepdown_and_postselection": verify_stepdown_and_postselection(),
        "example_4_sharpness": verify_example_4_sharpness(),
        "boosting_examples": verify_boosting_examples(),
        "optimality_and_calibration": verify_optimality_and_calibration(),
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
