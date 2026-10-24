#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 198:
AIMech:OptimalSpjotvollAndSieveGroupedPValueWeighting
(Kathryn Roeder & Larry Wasserman 2009, 'Genome-Wide Significance Levels and
Weighted Hypothesis Testing', Statistical Science 24(4):398-413,
arXiv:1010.4637v1, DOI:10.1214/09-STS289).
"""
from __future__ import annotations

import json
import math


def phi_cdf(x: float) -> float:
    """Standard normal CDF Phi(x)."""
    return 0.5 * math.erfc(-x / math.sqrt(2.0))


def phi_bar(x: float) -> float:
    """Standard normal upper-tail survival function Phi_bar(x) = 1 - Phi(x)."""
    return 0.5 * math.erfc(x / math.sqrt(2.0))


def phi_pdf(x: float) -> float:
    """Standard normal density phi(x)."""
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def z_upper_quantile(u: float) -> float:
    """Upper-tail normal quantile z_u satisfying Phi_bar(z_u) = u for u in (0, 1)."""
    if u <= 0.0:
        return 38.0
    if u >= 1.0:
        return -38.0
    lo, hi = -38.0, 38.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if phi_bar(mid) > u:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def verify_theorem_3_1_and_lemma_3_2() -> dict[str, object]:
    """Verify Theorem 3.1 (one-parameter optimal Spjotvoll weights rho_c(xi_j))
    and Lemma 3.2 (oracle power Phi_bar(c/xi_j - xi_j/2)).
    """
    m = 100
    alpha = 0.05
    # 20 non-null tests with heterogeneous positive effect sizes, 80 null tests (xi_j = 0)
    xi_signals = [1.5 + 0.15 * j for j in range(20)]
    xi_all = xi_signals + [0.0] * 80

    # Solve m^{-1} sum_{j=1}^m rho_c(xi_j) = 1 where rho_c(xi) = (m/alpha) Phi_bar(xi/2 + c/xi)
    def avg_weight(c_val: float) -> float:
        total = 0.0
        for xi in xi_signals:
            total += (m / alpha) * phi_bar(0.5 * xi + c_val / xi)
        return total / m

    lo, hi = -20.0, 40.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if avg_weight(mid) > 1.0:
            lo = mid
        else:
            hi = mid
    c_star = 0.5 * (lo + hi)

    weights = [
        (m / alpha) * phi_bar(0.5 * xi + c_star / xi) if xi > 0.0 else 0.0
        for xi in xi_all
    ]
    budget_err = abs(sum(weights) / m - 1.0)

    # Check KKT stationarity: d/dw_j Phi_bar(z_{alpha w_j / m} - xi_j)
    # = (alpha / m) * phi(z_{alpha w_j / m} - xi_j) / phi(z_{alpha w_j / m})
    # = (alpha / m) * exp(xi_j * z_{alpha w_j / m} - xi_j^2 / 2) = (alpha / m) * exp(c_star)
    target_kkt = (alpha / m) * math.exp(c_star)
    max_kkt_err = 0.0
    max_lemma_3_2_err = 0.0
    oracle_powers = []
    unweighted_powers = []
    z_unweighted = z_upper_quantile(alpha / m)

    for xi, w in zip(xi_signals, weights[:20]):
        z_w = z_upper_quantile(alpha * w / m)
        kkt_deriv = (alpha / m) * (phi_pdf(z_w - xi) / phi_pdf(z_w))
        max_kkt_err = max(max_kkt_err, abs(kkt_deriv - target_kkt))

        p_direct = phi_bar(z_w - xi)
        p_lemma_3_2 = phi_bar(c_star / xi - 0.5 * xi)
        max_lemma_3_2_err = max(max_lemma_3_2_err, abs(p_direct - p_lemma_3_2))
        oracle_powers.append(p_lemma_3_2)
        unweighted_powers.append(phi_bar(z_unweighted - xi))

    avg_oracle_power = sum(oracle_powers) / len(oracle_powers)
    avg_unweighted_power = sum(unweighted_powers) / len(unweighted_powers)

    assert budget_err < 1e-13
    assert max_kkt_err < 1e-11
    assert max_lemma_3_2_err < 1e-11
    assert avg_oracle_power > avg_unweighted_power

    return {
        "c_star": round(c_star, 10),
        "budget_error": float(f"{budget_err:.3e}"),
        "max_kkt_stationarity_error": float(f"{max_kkt_err:.3e}"),
        "max_lemma_3_2_power_identity_error": float(f"{max_lemma_3_2_err:.3e}"),
        "avg_oracle_power": round(avg_oracle_power, 8),
        "avg_unweighted_bonferroni_power": round(avg_unweighted_power, 8),
        "oracle_beats_bonferroni": avg_oracle_power > avg_unweighted_power,
    }


def verify_sparse_weight_robustness_theorems_3_4_and_lemma_3_5() -> dict[str, object]:
    """Verify Theorem 3.4 & Lemma 3.5:
    R_{B,b}(xi) = [pi(xi, B) - pi(xi, 1)] - [pi(xi, 1) - pi(xi, b)]
    = Phi_bar(z_{B alpha/m} - xi) + Phi_bar(z_{b alpha/m} - xi) - 2 Phi_bar(z_{alpha/m} - xi).
    Even when b = 0 (downweighted tests have 0 power) and B >= 2, R_{B,0}(xi) > 0 on (0, xi_*).
    """
    m = 10000
    alpha = 0.05
    B = 4.0
    z_1 = z_upper_quantile(alpha / m)
    z_B = z_upper_quantile(B * alpha / m)

    def r_b0(xi: float) -> float:
        return phi_bar(z_B - xi) - 2.0 * phi_bar(z_1 - xi)

    # Find exact positive root xi_* of R_{B,0}(xi_*) = 0
    lo, hi = 0.5, z_1
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if r_b0(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    xi_star_exact = 0.5 * (lo + hi)

    # Lemma 3.5 Mill's-ratio sufficient threshold: z_{alpha/m} - 1 / (z_{alpha/m} - z_{B alpha/m})
    xi_suff_lemma_3_5 = z_1 - 1.0 / (z_1 - z_B)
    r_at_lemma_3_5_threshold = r_b0(xi_suff_lemma_3_5)

    # Check positivity at midpoint xi = 0.5 * xi_star_exact and at Lemma 3.5 threshold
    r_mid = r_b0(0.5 * xi_star_exact)
    r_above = r_b0(xi_star_exact + 0.5)

    assert r_mid > 0.0
    assert r_at_lemma_3_5_threshold > 0.0
    assert r_above < 0.0
    assert 0.0 < xi_suff_lemma_3_5 < xi_star_exact < z_1

    return {
        "B": B,
        "z_alpha_over_m": round(z_1, 8),
        "z_B_alpha_over_m": round(z_B, 8),
        "xi_star_exact_root": round(xi_star_exact, 8),
        "lemma_3_5_mills_ratio_threshold": round(xi_suff_lemma_3_5, 8),
        "R_B0_at_lemma_3_5_threshold": round(r_at_lemma_3_5_threshold, 8),
        "R_B0_at_half_xi_star": round(r_mid, 8),
        "R_B0_above_xi_star": round(r_above, 8),
        "safe_zone_positive_at_b_zero": r_mid > 0.0 and r_at_lemma_3_5_threshold > 0.0 and r_above < 0.0,
    }


def verify_ks_discontinuity_and_theorem_3_8_worst_case_power() -> dict[str, object]:
    """Verify Lemma 3.6 (Kolmogorov-Smirnov discontinuity of optimal weight map rho_Q(xi))
    and Theorems 3.7-3.8 (worst-case power inf_{u>=0} pi_u(xi) achieved at u_* = sqrt(2 c_*)).
    """
    # Exact parameters from Section 3 Property II numerical example (lines 360-390)
    m = 1000
    alpha = 0.05
    a = 0.1
    gamma = 0.1
    K = 1000.0
    c_example = 0.1

    # True distribution Q = (1-a) delta_0 + a delta_xi -> true optimal weight rho(xi) = 1/a = 10
    rho_true = 1.0 / a

    # In Section 3 Property II (lines 116-117) & Lemma 3.6:
    # We want w_0 / w_1 = K and gamma * w_0 + a * w_1 = 1, so:
    # w_1 = 1 / (K * gamma + a), w_0 = K / (K * gamma + a)
    w1_target = 1.0 / (K * gamma + a)
    w0_target = K / (K * gamma + a)
    A_quant = z_upper_quantile(alpha * w1_target / m)
    B_quant = z_upper_quantile(alpha * w0_target / m)
    xi_lemma_3_6 = A_quant + math.sqrt(A_quant * A_quant - 2.0 * c_example)
    u_lemma_3_6 = B_quant - math.sqrt(B_quant * B_quant - 2.0 * c_example)

    # Under perturbed distribution Q_tilde = (1-a-gamma) delta_0 + gamma delta_u + a delta_xi,
    # verify that c = c_example satisfies gamma * rho_c(u) + a * rho_c(xi) = 1
    rho_tilde_u = (m / alpha) * phi_bar(0.5 * u_lemma_3_6 + c_example / u_lemma_3_6)
    rho_tilde_xi = (m / alpha) * phi_bar(0.5 * xi_lemma_3_6 + c_example / xi_lemma_3_6)
    perturbed_budget = gamma * rho_tilde_u + a * rho_tilde_xi
    weight_ratio = rho_tilde_xi / rho_true
    expected_ratio = 1.0 / (K + 1.0)  # Since a = gamma = 0.1

    assert abs(perturbed_budget - 1.0) < 1e-11
    assert abs(weight_ratio - expected_ratio) < 1e-11

    # Now verify Theorem 3.8 worst-case power inf_{u >= 0} pi_u(xi) at xi = 4.2:
    # Least-favorable false-positive location is u_* = sqrt(2 c_*) where c_* solves
    # gamma * Phi_bar(sqrt(2 c_*)) + a * Phi_bar(xi/2 + c_*/xi) = alpha / m
    xi_test = 4.2

    def thm_3_8_lhs(c_val: float) -> float:
        return gamma * phi_bar(math.sqrt(2.0 * c_val)) + a * phi_bar(0.5 * xi_test + c_val / xi_test)

    lo, hi = 1e-8, 30.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if thm_3_8_lhs(mid) > alpha / m:
            lo = mid
        else:
            hi = mid
    c_star_thm38 = 0.5 * (lo + hi)
    u_star_thm38 = math.sqrt(2.0 * c_star_thm38)
    worst_case_power_thm38 = phi_bar(c_star_thm38 / xi_test - 0.5 * xi_test)

    # Grid search over u > 0 to confirm u_* = sqrt(2 c_*) truly minimizes pi_u(xi_test)
    min_grid_power = 1.0
    for u_grid in [0.2 * k for k in range(1, 40)]:
        lo_c, hi_c = -10.0, 40.0
        for _ in range(80):
            mid_c = 0.5 * (lo_c + hi_c)
            val = gamma * phi_bar(0.5 * u_grid + mid_c / u_grid) + a * phi_bar(0.5 * xi_test + mid_c / xi_test)
            if val > alpha / m:
                lo_c = mid_c
            else:
                hi_c = mid_c
        c_u = 0.5 * (lo_c + hi_c)
        pow_u = phi_bar(c_u / xi_test - 0.5 * xi_test)
        if pow_u < min_grid_power:
            min_grid_power = pow_u

    unweighted_power_xi_test = phi_bar(z_upper_quantile(alpha / m) - xi_test)

    # Verify Theorem 3.7 threshold xi_* = z_{alpha/m} + sqrt(z_{alpha/m}^2 - z_q^2)
    # where q = alpha * (1 - a) / (m * gamma) (line 145)
    q_thm37 = alpha * (1.0 - a) / (m * gamma)
    z_am = z_upper_quantile(alpha / m)
    z_q = z_upper_quantile(q_thm37)
    xi_star_thm37 = z_am + math.sqrt(z_am * z_am - z_q * z_q)

    assert worst_case_power_thm38 <= min_grid_power + 1e-6
    assert worst_case_power_thm38 > unweighted_power_xi_test
    assert xi_test < xi_star_thm37

    return {
        "ks_distance_gamma": gamma,
        "rho_true": rho_true,
        "u_lemma_3_6": round(u_lemma_3_6, 6),
        "xi_lemma_3_6": round(xi_lemma_3_6, 6),
        "rho_tilde_xi": round(rho_tilde_xi, 8),
        "weight_ratio_tilde_over_true": round(weight_ratio, 8),
        "expected_ratio_1_over_K_plus_1": round(expected_ratio, 8),
        "thm_3_8_xi_test": xi_test,
        "thm_3_8_c_star": round(c_star_thm38, 8),
        "thm_3_8_u_star": round(u_star_thm38, 8),
        "thm_3_8_worst_case_power": round(worst_case_power_thm38, 8),
        "min_grid_power_over_u": round(min_grid_power, 8),
        "unweighted_bonferroni_power_at_xi_test": round(unweighted_power_xi_test, 8),
        "thm_3_7_xi_star_threshold": round(xi_star_thm37, 8),
        "worst_case_still_beats_bonferroni": worst_case_power_thm38 > unweighted_power_xi_test,
    }


def verify_theorems_4_1_4_2_and_section_5_sieve_grouping() -> dict[str, object]:
    """Verify Theorem 4.1 (unimodality of R(B, eps) at marginal effect xi_0 = z_{alpha/m}),
    Theorem 4.2 (maximin binary external weights), and Section 5 Equation (12)
    (sieve-principle method-of-moments grouped weighting with linear smoothing).
    """
    m = 5000
    alpha = 0.05
    eps_thm41 = 0.10  # Matches Figure 5 bottom panel (line 229)
    xi_0 = z_upper_quantile(alpha / m)

    def r_binary(B_val: float) -> float:
        w1 = B_val / (eps_thm41 * B_val + 1.0 - eps_thm41)
        w0 = 1.0 / (eps_thm41 * B_val + 1.0 - eps_thm41)
        p1 = phi_bar(z_upper_quantile(w1 * alpha / m) - xi_0)
        p0 = phi_bar(z_upper_quantile(w0 * alpha / m) - xi_0)
        return p1 + p0 - 1.0

    # Golden-section search for unique maximizer B^*(eps) of R(B, eps) on (1, 30)
    a_g, b_g = 1.001, 30.0
    gr = (math.sqrt(5.0) - 1.0) / 2.0
    for _ in range(80):
        c_g = b_g - gr * (b_g - a_g)
        d_g = a_g + gr * (b_g - a_g)
        if r_binary(c_g) > r_binary(d_g):
            b_g = d_g
        else:
            a_g = c_g
    B_star_thm41 = 0.5 * (a_g + b_g)
    R_max_thm41 = r_binary(B_star_thm41)

    # Turnaround point B_0(eps) > B^*(eps) where R(B_0, eps) = 0
    lo_b0, hi_b0 = B_star_thm41, 200.0
    for _ in range(80):
        mid_b0 = 0.5 * (lo_b0 + hi_b0)
        if r_binary(mid_b0) > 0.0:
            lo_b0 = mid_b0
        else:
            hi_b0 = mid_b0
    B_0_turnaround = 0.5 * (lo_b0 + hi_b0)

    # Theorem 4.2: Maximin binary weights for target power 1 - beta = 0.70 at xi_m = z_{alpha/m}
    # with eps = 0.05 (so eps * w_1 < 1 and w_0 > 0)
    eps = 0.05
    one_minus_beta = 0.70
    z_one_minus_beta = z_upper_quantile(one_minus_beta)
    c_thm42 = phi_bar(xi_0 + z_one_minus_beta)
    B_thm42 = c_thm42 * m * (1.0 - eps) / (alpha - eps * c_thm42 * m)
    w1_thm42 = B_thm42 / (eps * B_thm42 + 1.0 - eps)
    w0_thm42 = 1.0 / (eps * B_thm42 + 1.0 - eps)
    power_w1_thm42 = phi_bar(z_upper_quantile(w1_thm42 * alpha / m) - xi_0)
    power_w0_thm42 = phi_bar(z_upper_quantile(w0_thm42 * alpha / m) - xi_0)
    budget_thm42 = eps * w1_thm42 + (1.0 - eps) * w0_thm42

    assert R_max_thm41 > 0.0
    assert 1.0 < B_star_thm41 < B_0_turnaround < 190.0
    assert B_thm42 > 1.0 and 0.0 < w0_thm42 < 1.0 < w1_thm42
    assert abs(power_w1_thm42 - one_minus_beta) < 1e-10
    assert abs(budget_thm42 - 1.0) < 1e-13

    # Section 5 Equation (12): Sieve-principle grouped method-of-moments estimation
    # Suppose K = 4 equal-sized groups with true mixture parameters (pi_k, xi_k)
    # Population moments of T_{ik} ~ (1 - pi_k) N(0, 1) + pi_k N(xi_k, 1):
    # E[T_{ik}] = pi_k * xi_k, Var(T_{ik}) = 1 + pi_k * (1 - pi_k) * xi_k^2 (in paper Eq. 12:
    # moment equations E(Y_k) = pi_k xi_k and S_k^2 - 1 = pi_k(1 - pi_k) xi_k^2 + pi_k^2 xi_k^2 = pi_k xi_k^2
    # Wait: let's check Eq. 12 exact algebraic formula in the paper:
    # pi_hat_k = Y_k^2 / (Y_k^2 + S_k^2 - 1), xi_hat_k = Y_k / pi_hat_k,
    # which derives from E[Y_k] = pi_k xi_k and E[S_k^2] = 1 + pi_k(1 - pi_k) xi_k^2!)
    true_groups = [
        (0.40, 3.2),
        (0.25, 2.6),
        (0.10, 2.0),
        (0.00, 0.0),
    ]
    max_mom_pi_err = 0.0
    max_mom_xi_err = 0.0
    xi_hats = []
    for pi_k, xi_k in true_groups:
        y_k = pi_k * xi_k
        s2_k = 1.0 + pi_k * (1.0 - pi_k) * (xi_k * xi_k)
        if y_k == 0.0:
            pi_hat = 0.0
            xi_hat = 0.0
        else:
            pi_hat = (y_k * y_k) / (y_k * y_k + s2_k - 1.0)
            xi_hat = y_k / pi_hat
        if pi_k > 0.0:
            max_mom_pi_err = max(max_mom_pi_err, abs(pi_hat - pi_k))
            max_mom_xi_err = max(max_mom_xi_err, abs(xi_hat - xi_k))
        xi_hats.append(xi_hat)

    # Compute plug-in Spjotvoll group weights and linearly smoothed weights (gamma_smooth = 0.05)
    K_groups = len(xi_hats)
    lo_c, hi_c = -10.0, 30.0
    for _ in range(100):
        mid_c = 0.5 * (lo_c + hi_c)
        avg_w = sum(
            (m / alpha) * phi_bar(0.5 * xh + mid_c / xh) if xh > 0.0 else 0.0
            for xh in xi_hats
        ) / K_groups
        if avg_w > 1.0:
            lo_c = mid_c
        else:
            hi_c = mid_c
    c_group = 0.5 * (lo_c + hi_c)
    raw_group_w = [
        (m / alpha) * phi_bar(0.5 * xh + c_group / xh) if xh > 0.0 else 0.0
        for xh in xi_hats
    ]
    gamma_smooth = 0.05
    mean_raw = sum(raw_group_w) / K_groups
    smoothed_group_w = [
        (1.0 - gamma_smooth) * w_k + gamma_smooth * mean_raw
        for w_k in raw_group_w
    ]

    assert max_mom_pi_err < 1e-14
    assert max_mom_xi_err < 1e-14
    assert abs(sum(smoothed_group_w) / K_groups - 1.0) < 1e-13
    assert smoothed_group_w[-1] > 0.0  # smoothing gives positive floor weight to null group

    return {
        "thm_4_1_B_star": round(B_star_thm41, 6),
        "thm_4_1_max_robustness_R": round(R_max_thm41, 8),
        "thm_4_1_turnaround_B0": round(B_0_turnaround, 6),
        "thm_4_2_B_maximin": round(B_thm42, 6),
        "thm_4_2_w1": round(w1_thm42, 6),
        "thm_4_2_w0": round(w0_thm42, 6),
        "thm_4_2_power_w1": round(power_w1_thm42, 8),
        "thm_4_2_power_w0": round(power_w0_thm42, 8),
        "section_5_mom_max_pi_error": float(f"{max_mom_pi_err:.3e}"),
        "section_5_mom_max_xi_error": float(f"{max_mom_xi_err:.3e}"),
        "section_5_smoothed_group_weights": [round(w, 6) for w in smoothed_group_w],
        "section_5_smoothed_null_group_weight_positive": smoothed_group_w[-1] > 0.0,
    }


def main() -> None:
    res = {
        "theorem_3_1_and_lemma_3_2_oracle_weights": verify_theorem_3_1_and_lemma_3_2(),
        "theorems_3_4_and_lemma_3_5_sparse_robustness": verify_sparse_weight_robustness_theorems_3_4_and_lemma_3_5(),
        "lemma_3_6_and_theorems_3_7_3_8_ks_discontinuity_vs_power": verify_ks_discontinuity_and_theorem_3_8_worst_case_power(),
        "theorems_4_1_4_2_and_section_5_sieve_grouped_weights": verify_theorems_4_1_4_2_and_section_5_sieve_grouping(),
    }
    print(json.dumps(res, sort_keys=True))


if __name__ == "__main__":
    main()
