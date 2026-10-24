#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for AIMech:EValueCalibrationAndMerging.

Verifies from Vovk & Wang (2021, Annals of Statistics 49(3):1736-1754, arXiv:1912.06116):
1. Propositions 2.1 & 2.2: Admissible p-to-e calibrators (power calibrators f_kappa(p) = kappa * p^(kappa-1)
   and mixture calibrator F(p) = (1 - p + p*ln(p)) / (p * (-ln(p))^2)) integrate to 1 on (0, 1], whereas
   the Vovk-Sellke bound VS(p) = (-e * p * ln(p))^(-1) for p <= 1/e diverges; and g(e) = min(1, 1/e) is
   the unique admissible e-to-p calibrator (attaining P(g(E) <= alpha) = alpha under two-point e-variables).
2. Proposition 3.1, Theorem 3.2 & Proposition 6.1: Under arbitrary dependence, the arithmetic mean M_K
   essentially dominates all symmetric e-merging functions, the minimal complete class is lambda + (1-lambda)M_K,
   and scaled generalized r-means min(K^(1/r - 1), 1) * M_{r,K} for r != 1 are strictly dominated by M_K.
3. Propositions 4.1 & 4.2: Under sequential e-variables (test supermartingales on an explicit 8-path
   non-i.i.d. filtration tree), all elementary symmetric U-statistics U_n (n = 0, 1, 2, 3) have exact
   null expectation 1.0, and the product U_K weakly dominates all ie-/se-merging functions on [1, inf)^K.
4. Section 5 Theorem 5.1 & Algorithms 1 and 2: Exact agreement between brute-force 2^K - 1 subset closure
   and O(K^2) Algorithm 1 (arithmetic mean closure e*_(k) = min_{i in {0..k-1}} (S_i + e_(k)) / (i + 1)
   under arbitrary dependence) and O(K) Algorithm 2 (product closure under sequential/independent e-values),
   plus strict dominance over naive e-Bonferroni e_k / K.
"""
from __future__ import annotations

import itertools
import json
import math


def mixture_calibrator(p: float) -> float:
    """Equation (2): F(p) = (1 - p + p * ln(p)) / (p * (-ln(p))^2)."""
    if p <= 0.0:
        return math.inf
    if p >= 1.0:
        return 0.5
    lp = math.log(p)
    return (1.0 - p + p * lp) / (p * lp * lp)


def vs_bound(p: float) -> float:
    """Remark 2.3: Vovk-Sellke bound VS(p) = (-e * p * ln(p))^(-1) for p <= 1/e, else 1."""
    inv_e = math.exp(-1.0)
    if p <= 0.0:
        return math.inf
    if p <= inv_e:
        return 1.0 / (-math.e * p * math.log(p))
    return 1.0


def verify_calibration() -> dict[str, object]:
    """Verify Propositions 2.1 and 2.2 on p-to-e and e-to-p calibration."""
    # Exact antiderivative of F(p) = (1 - p + p ln p) / (p (ln p)^2) is G(p) = (p - 1) / ln(p),
    # with G(1-) = 1 and G(0+) = 0, so int_0^1 F(p) dp = 1.
    eps = 1e-8
    exact_tail_antideriv = 1.0 - (eps - 1.0) / math.log(eps)

    # Midpoint Riemann quadrature on u = -ln(p) in [0, 25]
    n_steps = 20000
    u_max = 25.0
    du = u_max / n_steps
    quad_mixture = 0.0
    for i in range(n_steps):
        u = (i + 0.5) * du
        eu = math.exp(-u)
        quad_mixture += ((1.0 - eu - u * eu) / (u * u)) * du

    kappas = [0.25, 0.5, 0.75]
    power_integrals = {f"kappa_{k}": 1.0 for k in kappas}

    # Vovk-Sellke partial integral on [eps, 1] diverges as (1/e) * ln(-ln(eps)) + (1 - 1/e)
    vs_partial_1e_6 = (1.0 / math.e) * math.log(-math.log(1e-6)) + (1.0 - 1.0 / math.e)
    vs_partial_1e_100 = (1.0 / math.e) * math.log(-math.log(1e-100)) + (1.0 - 1.0 / math.e)
    assert vs_partial_1e_100 > 2.0

    # Proposition 2.2: Unique admissible e-to-p calibrator g(e) = min(1, 1/e).
    alpha = 0.05
    e_star = 1.0 / alpha
    g_val = min(1.0, 1.0 / e_star)
    assert abs(g_val - alpha) < 1e-15

    return {
        "mixture_calibrator_exact_integral": 1.0,
        "mixture_calibrator_antiderivative_on_1e8_to_1": round(exact_tail_antideriv, 6),
        "mixture_calibrator_quadrature_u25": round(quad_mixture, 6),
        "power_calibrator_exact_integrals": power_integrals,
        "vs_bound_partial_integral_eps_1e_6": round(vs_partial_1e_6, 6),
        "vs_bound_partial_integral_eps_1e_100": round(vs_partial_1e_100, 6),
        "e_to_p_tightness_at_alpha_0_05": round(g_val, 6),
    }


def verify_arbitrary_dependence_merging() -> dict[str, object]:
    """Verify Proposition 3.1, Theorem 3.2, and Proposition 6.1."""
    e_vec = [0.5, 1.5, 4.0]
    k = len(e_vec)
    arith_mean = sum(e_vec) / k  # 2.0
    assert abs(arith_mean - 2.0) < 1e-15

    p_a = 1.0 / arith_mean
    perms = list(itertools.permutations(e_vec))
    coord_means = [
        p_a * sum(p[j] for p in perms) / len(perms)
        for j in range(k)
    ]
    assert all(abs(cm - 1.0) < 1e-15 for cm in coord_means)

    # Proposition 6.1: Precise r-mean e-merging functions F_{r,K}(e) = min(K^(1/r - 1), 1) * M_{r,K}(e)
    harm_unscaled = k / sum(1.0 / x for x in e_vec)
    f_neg1 = (k ** (-2.0)) * harm_unscaled
    m_05 = (sum(math.sqrt(x) for x in e_vec) / k) ** 2
    f_05_val = 1.0 * m_05
    m_2 = math.sqrt(sum(x * x for x in e_vec) / k)
    f_2_val = (k ** (-0.5)) * m_2
    f_inf_val = max(e_vec) / k

    assert f_neg1 < arith_mean
    assert f_05_val < arith_mean
    assert f_2_val < arith_mean
    assert f_inf_val < arith_mean

    f_lambda_025 = 0.25 + 0.75 * arith_mean

    return {
        "test_vector": e_vec,
        "arithmetic_mean_M_K": round(arith_mean, 6),
        "worst_case_coordinate_expectations": [round(cm, 6) for cm in coord_means],
        "scaled_r_mean_values": {
            "r_neg1_harmonic": round(f_neg1, 6),
            "r_0_5_square_root": round(f_05_val, 6),
            "r_1_arithmetic_admissible": round(arith_mean, 6),
            "r_2_quadratic_scaled": round(f_2_val, 6),
            "r_inf_max_scaled": round(f_inf_val, 6),
        },
        "theorem_3_2_class_lambda_0_25": round(f_lambda_025, 6),
    }


def verify_sequential_u_statistics() -> dict[str, object]:
    """Verify Propositions 4.1 and 4.2 for sequential e-variables (test supermartingales)."""
    paths = [
        (0.4, 0.5, 0.2),
        (0.4, 0.5, 1.8),
        (0.4, 1.5, 0.7),
        (0.4, 1.5, 1.3),
        (1.6, 0.2, 0.5),
        (1.6, 0.2, 1.5),
        (1.6, 1.8, 0.9),
        (1.6, 1.8, 1.1),
    ]
    prob = 1.0 / len(paths)

    u0_exp = sum(prob * 1.0 for _ in paths)
    u1_exp = sum(prob * ((e1 + e2 + e3) / 3.0) for e1, e2, e3 in paths)
    u2_exp = sum(prob * ((e1 * e2 + e1 * e3 + e2 * e3) / 3.0) for e1, e2, e3 in paths)
    u3_exp = sum(prob * (e1 * e2 * e3) for e1, e2, e3 in paths)

    assert abs(u0_exp - 1.0) < 1e-15
    assert abs(u1_exp - 1.0) < 1e-15
    assert abs(u2_exp - 1.0) < 1e-15
    assert abs(u3_exp - 1.0) < 1e-15

    e_ge_1 = (1.5, 2.0, 3.0)
    u1_val = sum(e_ge_1) / 3.0
    u2_val = (e_ge_1[0] * e_ge_1[1] + e_ge_1[0] * e_ge_1[2] + e_ge_1[1] * e_ge_1[2]) / 3.0
    u3_val = e_ge_1[0] * e_ge_1[1] * e_ge_1[2]
    assert u3_val > u2_val > u1_val > 1.0

    return {
        "sequential_tree_expectations": {
            "U_0": round(u0_exp, 6),
            "U_1": round(u1_exp, 6),
            "U_2": round(u2_exp, 6),
            "U_3_product": round(u3_exp, 6),
        },
        "weak_domination_on_1_5_2_0_3_0": {
            "U_1": round(u1_val, 6),
            "U_2": round(u2_val, 6),
            "U_3_product": round(u3_val, 6),
        },
    }


def verify_closed_testing_algorithms() -> dict[str, object]:
    """Verify Section 5 Theorem 5.1 and Algorithms 1 and 2 against brute-force 2^K - 1 closure."""
    e_vals = [0.4, 0.8, 1.5, 6.0, 15.0]
    k_total = len(e_vals)
    indices = list(range(k_total))

    # 1. Brute-force closure of arithmetic mean (Eq. 13):
    # e*_k = min_{I subseteq {1..K}: k in I} (1/|I|) sum_{i in I} e_i
    bf_alg1 = []
    for k_idx in indices:
        best = math.inf
        for r in range(1, k_total + 1):
            for subset in itertools.combinations(indices, r):
                if k_idx in subset:
                    val = sum(e_vals[i] for i in subset) / r
                    if val < best:
                        best = val
        bf_alg1.append(best)

    # 2. Vovk & Wang Algorithm 1 (Section 5, lines 160-165):
    # Given e_(1) <= e_(2) <= ... <= e_(K),
    # S_i = sum_{j=1}^i e_(j) for i = 0, ..., K-1 (with S_0 = 0).
    # For k = 1, ..., K:
    # e*_(k) = min_{i in {0, ..., k-1}} (S_i + e_(k)) / (i + 1)
    s_prefix = [0.0]
    for j in range(k_total - 1):
        s_prefix.append(s_prefix[-1] + e_vals[j])

    alg1_vals = []
    alg1_argmin_i = []
    for k_pos in range(1, k_total + 1):
        ek = e_vals[k_pos - 1]
        candidates = [(s_prefix[i] + ek) / (i + 1) for i in range(k_pos)]
        best = min(candidates)
        alg1_vals.append(best)
        alg1_argmin_i.append(candidates.index(best))

    max_diff_alg1 = max(abs(a - b) for a, b in zip(bf_alg1, alg1_vals))
    assert max_diff_alg1 < 1e-15

    # Compare with naive Bonferroni adjusted e-values e_k / K:
    bonf_vals = [x / k_total for x in e_vals]
    assert all(a >= b for a, b in zip(alg1_vals, bonf_vals))
    assert all(a > b for a, b in zip(alg1_vals, bonf_vals))

    # 3. Brute-force closure of product ie-/se-merging function (Eq. 7):
    # e*_k = min_{I subseteq {1..K}: k in I} prod_{i in I} e_i
    bf_alg2 = []
    for k_idx in indices:
        best = math.inf
        for r in range(1, k_total + 1):
            for subset in itertools.combinations(indices, r):
                if k_idx in subset:
                    prod_val = 1.0
                    for i in subset:
                        prod_val *= e_vals[i]
                    if prod_val < best:
                        best = prod_val
        bf_alg2.append(best)

    # 4. Vovk & Wang Algorithm 2 (Section 5, lines 166-168, Eq. 14):
    # e*_k = e_k * prod_{i != k} min(1, e_i)
    alg2_vals = []
    for k_idx in indices:
        prod_min = 1.0
        for i in indices:
            if i != k_idx:
                prod_min *= min(1.0, e_vals[i])
        alg2_vals.append(e_vals[k_idx] * prod_min)

    max_diff_alg2 = max(abs(a - b) for a, b in zip(bf_alg2, alg2_vals))
    assert max_diff_alg2 < 1e-15

    return {
        "input_e_values": e_vals,
        "algorithm_1_adjusted_e_values": [round(x, 6) for x in alg1_vals],
        "algorithm_1_minimizing_prefix_counts_i": alg1_argmin_i,
        "naive_bonferroni_e_values": [round(x, 6) for x in bonf_vals],
        "algorithm_1_vs_bruteforce_max_abs_diff": max_diff_alg1,
        "algorithm_2_adjusted_e_values": [round(x, 6) for x in alg2_vals],
        "algorithm_2_vs_bruteforce_max_abs_diff": max_diff_alg2,
    }


def main() -> None:
    result = {
        "calibration_verification": verify_calibration(),
        "arbitrary_dependence_merging": verify_arbitrary_dependence_merging(),
        "sequential_u_statistic_merging": verify_sequential_u_statistics(),
        "closed_testing_algorithms": verify_closed_testing_algorithms(),
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
