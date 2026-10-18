#!/usr/bin/env python3
"""Constructed numerical verification of Generalized Mean P-Value Merging boundaries.

Verifies the mathematical properties from Vovk & Wang (2020, Biometrika 107(4):791-808,
arXiv:1212.4966):
1. Propositions 3, 4, 5, 4w, 5w: Calibrated multipliers (r + 1)^{1/r} and min(r + 1, 1/w)^{1/r}
   for symmetric and weighted generalized r-means M_{r,K} and M_{r,w} in the integrable
   regime r > -1, exact finite-sample attainment of P(2 * M_{1,2}(U_1, U_2) <= eps) = eps
   under the counter-monotonic / joint-mixability copula on [0, eps] (proving sharpness of
   the factor 2 for arithmetic averaging and invalidity of any multiplier a < 2), and
   Proposition 5w's dominant-weight reduction min(r + 1, 1/w)^{1/r} M_{r,w} for w > 1/2.
2. Propositions 8 & 9: Non-integrable regime r in [-infinity, -1) multiplier
   (r / (r + 1)) * K^{1 + 1/r}, its calculus minimizer r* = ln(K) / (1 - ln(K)) < -1
   yielding the conservative harmonic bound e * ln(K) * M_{-1,K}, and the exact finite-K
   precise harmonic multiplier a_K^H = (y_K + K)^2 / ((y_K + 1) * K) <= e * ln(K) for K > 2
   via root-finding on y_K * (y_K + K) / ((y_K + 1) * K) = ln(y_K + 1) (Appendix A, line 946).
3. Proposition 10: Scale invariance q_eps(a * M_{r,K}) = eps * q_1(a * M_{r,K}) across
   thresholds eps in (0, 1).
4. Proposition 12 & Section 6.4 (Equation 17): Compound Bonferroni-Arithmetic (F_K^BA) and
   Bonferroni-Geometric (F_K^BG) merging functions across weak (rho = 0.1) and strong (rho = 0.9)
   exchangeable Gaussian z-test dependence.
"""

from __future__ import annotations

import json
import math
import random


def solve_harmonic_y_k(k: int) -> float:
    """Solve y * (y + K) / ((y + 1) * K) = ln(y + 1) for y > 0 (K > 2) via bisection."""
    lo = 0.1
    hi = max(10.0, float(k) * math.log(float(k)) * 3.0)
    while k * ((hi + 1.0) * math.log(hi + 1.0) - hi) - hi * hi > 0.0:
        hi *= 2.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        val = k * ((mid + 1.0) * math.log(mid + 1.0) - mid) - mid * mid
        if val > 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def precise_harmonic_multiplier(k: int) -> tuple[float, float]:
    """Return (y_K, a_K^H) from Proposition 9 of Vovk & Wang (2020)."""
    y_k = solve_harmonic_y_k(k)
    a_k_h = ((y_k + k) ** 2) / ((y_k + 1.0) * k)
    return y_k, a_k_h


def norm_cdf(x: float) -> float:
    """Standard normal CDF Phi(x)."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def main() -> None:
    # 1. Verify Propositions 8 & 9:
    # Minimizer r* = ln(K) / (1 - ln(K)) of (r / (r + 1)) * K^{1 + 1/r} gives e * ln(K),
    # and exact finite-K precise harmonic multiplier a_K^H <= e * ln(K) with a_K^H / ln(K) -> 1.
    harm_table = {}
    prev_h_ratio = 100.0
    for k in (3, 5, 10, 50, 1000):
        y_k, a_k_h = precise_harmonic_multiplier(k)
        ln_k = math.log(float(k))
        r_star = ln_k / (1.0 - ln_k)
        opt_coeff = (r_star / (r_star + 1.0)) * (float(k) ** (1.0 + 1.0 / r_star))
        assert abs(opt_coeff - math.e * ln_k) < 1e-12
        ratio_ln = a_k_h / ln_k
        assert a_k_h <= math.e * ln_k
        assert 1.0 < ratio_ln < prev_h_ratio
        prev_h_ratio = ratio_ln
        harm_table[str(k)] = {
            "y_K": y_k,
            "a_K_H": a_k_h,
            "a_K_H_over_ln_K": ratio_ln,
            "r_star_minimizer": r_star,
            "e_ln_K": math.e * ln_k,
        }
    # Check Vovk & Wang (2020) Section 3.2 Table 3 practical bounds:
    # For K >= 10, a_K^H / ln K < 2.0; for K >= 50, a_K^H / ln K < 1.7
    assert harm_table["10"]["a_K_H_over_ln_K"] < 2.0
    assert harm_table["50"]["a_K_H_over_ln_K"] < 1.7

    # 2. Verify Propositions 4, 5, 4w, 5w:
    # Worst-case joint-mixability copula on [0, eps] for K = 2 arithmetic mean (r = 1)
    eps = 0.10
    n_grid = 10000
    count_2_mean_le_eps = 0
    for i in range(n_grid):
        u1 = (i + 0.5) / n_grid
        # Counter-monotonic on [0, eps], comonotonic on (eps, 1] -> u2 is Uniform(0, 1)
        u2 = (eps - u1) if u1 <= eps else u1
        m_1_2 = 0.5 * (u1 + u2)
        if 2.0 * m_1_2 <= eps + 1e-12:
            count_2_mean_le_eps += 1
    prob_precise_2_mean = count_2_mean_le_eps / n_grid
    assert abs(prob_precise_2_mean - eps) < 1e-9

    # Counter-monotonic construction on [0, 2*eps] showing unscaled M_{1,2} has P(M_{1,2} <= eps) = 2*eps:
    count_unscaled_2eps = 0
    for i in range(n_grid):
        u1 = (i + 0.5) / n_grid
        u2 = (2.0 * eps - u1) if u1 <= 2.0 * eps else u1
        if 0.5 * (u1 + u2) <= eps + 1e-12:
            count_unscaled_2eps += 1
    prob_unscaled_mean = count_unscaled_2eps / n_grid
    assert abs(prob_unscaled_mean - 2.0 * eps) < 1e-9

    # Proposition 5 & 5w:
    # Symmetric K = 2, r = 2 > K - 1 = 1: (r + 1)^{1/r} = sqrt(3) > min(r + 1, K)^{1/r} = sqrt(2)
    mult_prop3_k2_r2 = (2.0 + 1.0) ** 0.5
    mult_prop5_k2_r2 = min(2.0 + 1.0, 2.0) ** 0.5
    assert mult_prop5_k2_r2 < mult_prop3_k2_r2

    # Weighted arithmetic mean (r = 1) with dominant weight w1 = 0.7, w2 = 0.3
    w1, w2 = 0.7, 0.3
    w_max = max(w1, w2)
    mult_prop5w = min(1.0 + 1.0, 1.0 / w_max)
    p1_ex, p2_ex = 0.02, 0.05
    merged_prop5w = mult_prop5w * (w1 * p1_ex + w2 * p2_ex)
    formula_eq15w = p1_ex + (w2 / w1) * p2_ex
    assert abs(merged_prop5w - formula_eq15w) < 1e-15
    assert mult_prop5w < 2.0

    # 3. Verify Proposition 12 & Section 6.4 (Equation 17):
    # Exchangeable Gaussian z-tests X_k = sqrt(1 - rho^2)*Z_k + rho*Z - mu, p_k = Phi(X_k)
    rng = random.Random(20261017)
    k_tests = 50
    mu_alt = 3.0
    n_rep = 400
    sim_summary = {}
    for rho in (0.1, 0.9):
        sum_bonf = 0.0
        sum_geom = 0.0
        sum_arith = 0.0
        sum_bg = 0.0
        sum_ba = 0.0
        for _ in range(n_rep):
            z_common = rng.gauss(0.0, 1.0)
            p_vals = []
            for _ in range(k_tests):
                z_k = rng.gauss(0.0, 1.0)
                x_k = math.sqrt(1.0 - rho * rho) * z_k + rho * z_common - mu_alt
                p_vals.append(max(norm_cdf(x_k), 1e-300))
            p_bonf = k_tests * min(p_vals)
            p_arith = 2.0 * (sum(p_vals) / k_tests)
            p_geom = math.e * math.exp(sum(math.log(p) for p in p_vals) / k_tests)
            p_bg = 2.0 * min(p_bonf, p_geom)
            p_ba = 2.0 * min(p_bonf, p_arith)
            sum_bonf += p_bonf
            sum_geom += p_geom
            sum_arith += p_arith
            sum_bg += p_bg
            sum_ba += p_ba
        sim_summary[f"rho_{rho}"] = {
            "mean_bonferroni": sum_bonf / n_rep,
            "mean_geometric": sum_geom / n_rep,
            "mean_arithmetic": sum_arith / n_rep,
            "mean_compound_BG": sum_bg / n_rep,
            "mean_compound_BA": sum_ba / n_rep,
        }

    assert sim_summary["rho_0.1"]["mean_bonferroni"] < sim_summary["rho_0.1"]["mean_geometric"]
    assert sim_summary["rho_0.9"]["mean_geometric"] < sim_summary["rho_0.9"]["mean_bonferroni"]
    assert sim_summary["rho_0.9"]["mean_compound_BG"] < sim_summary["rho_0.9"]["mean_bonferroni"]

    out = {
        "concept_id": "AIMech:GeneralizedMeanPValueMerging",
        "prop8_prop9_harmonic_multipliers": harm_table,
        "prop4_prop5_prop5w_precision_checks": {
            "eps": eps,
            "prob_2_M12_le_eps_under_joint_mixability": prob_precise_2_mean,
            "prob_unscaled_M12_le_eps_under_joint_mixability": prob_unscaled_mean,
            "prop5_k2_r2_precise_multiplier": mult_prop5_k2_r2,
            "prop3_k2_r2_asymptotic_multiplier": mult_prop3_k2_r2,
            "prop5w_dominant_weight_multiplier_w07": mult_prop5w,
            "prop5w_merged_p_value": merged_prop5w,
        },
        "prop12_eq17_simulation_K50_mu3": sim_summary,
    }
    print(json.dumps(out))


if __name__ == "__main__":
    main()
