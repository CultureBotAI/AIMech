#!/usr/bin/env python3
"""Constructed boundary verification for AIMech:BayesOptimalPValueWeightingUnderGaussianPrior.

Verifies the four core theoretical and empirical properties of Dobriban, Fortney,
Kim, and Owen (2015), 'Optimal multiple testing under a Gaussian prior on the
effect sizes', Biometrika 102(4):753-766 (arXiv:1504.02935v1):
1. Proposition 3.1: Exact two-regime optimal weights in the sparse means model
   (all weight on large means when pi_1 * Phi(-|M|/2) > q vs shared positive weight
   w_0 > 0 on zero means when pi_1 * Phi(-|M|/2) <= q) and >3x power gain hotspot.
2. Theorem 3.2 & Proposition 3.3: Exact Bayes weights for small q when Condition (5)
   holds (lambda >= 1), global optimality despite non-concavity of the objective,
   and convergence to Spjotvoll weights as sigma -> 0+.
3. Section 3.3, Lemma 9.2, & Theorem 3.5: Symmetry breaking as sigma -> infinity
   ((J + floor(Jq))/2 > J/2) and general-case jump-discontinuity solver when
   Condition (5) fails (lambda in (0, 1)) achieving |q* - q| <= 1/(2J).
4. Sections 4.1, 4.2, & 5.3: Worst-case maximin power/regret advantage of Bayes
   weights over Spjotvoll weights across sigma in {0, 1} and exact frequentist
   PFER/FWER control under prior misspecification.
"""

from __future__ import annotations

import json
import math
import random


def phi(x: float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def Phi(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def inv_Phi(p: float) -> float:
    if p <= 0.0:
        return -12.0
    if p >= 1.0:
        return 12.0
    lo, hi = -12.0, 12.0
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if Phi(mid) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def c1_func(eta: float, gamma: float, lam: float) -> float:
    """Smaller root c_1(eta, gamma; lam) from Lemma 9.1 / Eq. (4)."""
    g2_minus_1 = gamma * gamma - 1.0
    disc = eta * eta + 2.0 * g2_minus_1 * math.log(gamma * lam)
    disc = max(0.0, disc)
    return (-eta - gamma * math.sqrt(disc)) / g2_minus_1


def spjotvoll_c(eta: float, lam: float) -> float:
    """Limit of c_1(eta, gamma; lam) as sigma -> 0 (gamma -> 1) for eta < 0."""
    return 0.5 * eta + math.log(lam) / eta


def solve_spjotvoll_weights(etas: list[float], q: float) -> tuple[list[float], float]:
    J = len(etas)
    lo, hi = 1e-12, 1e12
    for _ in range(90):
        mid = math.sqrt(lo * hi)
        total = sum(min(1.0 / q, Phi(spjotvoll_c(eta, mid)) / q) for eta in etas)
        if total > J:
            lo = mid
        else:
            hi = mid
    lam = math.sqrt(lo * hi)
    weights = [min(1.0 / q, Phi(spjotvoll_c(eta, lam)) / q) for eta in etas]
    return weights, lam


def solve_bayes_small_q(
    etas: list[float], sigmas: list[float], q: float
) -> tuple[list[float], float, bool]:
    J = len(etas)
    gammas = [math.sqrt(s * s + 1.0) for s in sigmas]
    sum_at_lam1 = sum(Phi(c1_func(e, g, 1.0)) for e, g in zip(etas, gammas))
    cond5_holds = sum_at_lam1 >= J * q
    lo, hi = 1.0, 1e12
    for _ in range(90):
        mid = 0.5 * (lo + hi) if hi < 1e4 else math.sqrt(lo * hi)
        total = sum(Phi(c1_func(e, g, mid)) / q for e, g in zip(etas, gammas))
        if total > J:
            lo = mid
        else:
            hi = mid
    lam = 0.5 * (lo + hi)
    weights = [Phi(c1_func(e, g, lam)) / q for e, g in zip(etas, gammas)]
    return weights, lam, cond5_holds


def find_k_threshold(eta: float, gamma: float) -> float:
    """Unique root k(eta, gamma) in [l(eta, gamma), 1] from Lemma 9.2."""
    g2_minus_1 = gamma * gamma - 1.0
    l_val = math.exp(-0.5 * eta * eta / g2_minus_1) / gamma
    lo, hi = l_val, 1.0
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        c_val = c1_func(eta, gamma, mid)
        p1 = Phi((c_val - eta) / gamma) - mid * Phi(c_val)
        p_inf = 1.0 - mid
        if p1 - p_inf < 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def verify_proposition_3_1_sparse_means() -> dict[str, object]:
    q = 1e-3
    M_small = -1.5  # Phi(-0.75) = 0.2266
    pi1_reg1 = 0.02  # pi1 * Phi(-0.75) = 0.00453 > q = 0.001 -> Regime 1 (w0 = 0)
    thresh_reg1 = pi1_reg1 * Phi(-abs(M_small) / 2.0)

    M_large = -7.0  # Phi(-3.5) = 0.0002326
    pi1_reg2 = 0.002  # pi1 * Phi(-3.5) = 4.65e-7 <= q = 0.001 -> Regime 2 (w0 > 0)
    thresh_reg2 = pi1_reg2 * Phi(-abs(M_large) / 2.0)
    pi0_reg2 = 1.0 - pi1_reg2
    w1_reg2 = Phi(-abs(M_large) / 2.0) / q
    w0_reg2 = (1.0 - pi1_reg2 * w1_reg2) / pi0_reg2
    p_star_reg2 = q + pi1_reg2 * (Phi(abs(M_large) / 2.0) - Phi(-abs(M_large) / 2.0))
    w1_all = min(1.0 / q, 1.0 / pi1_reg2)
    w0_all = (1.0 - pi1_reg2 * w1_all) / pi0_reg2
    p_all_on_M = pi0_reg2 * q * w0_all + pi1_reg2 * Phi(inv_Phi(q * w1_all) - M_large)

    pi1_hot = 0.05
    pi0_hot = 0.95
    M_hot = -2.0
    p_star_hot = pi1_hot * Phi(inv_Phi(q / pi1_hot) + abs(M_hot))
    p_unif_hot = pi0_hot * q + pi1_hot * Phi(inv_Phi(q) + abs(M_hot))
    power_ratio_hot = p_star_hot / p_unif_hot

    return {
        "regime1_thresh_gt_q": thresh_reg1 > q,
        "regime2_thresh_le_q": thresh_reg2 <= q,
        "regime2_w0_positive": round(w0_reg2, 6),
        "regime2_p_star": round(p_star_reg2, 6),
        "regime2_p_all_on_M": round(p_all_on_M, 6),
        "regime2_strictly_beats_all_on_M": p_star_reg2 > p_all_on_M,
        "hotspot_power_ratio": round(power_ratio_hot, 4),
        "hotspot_exceeds_3x": power_ratio_hot > 3.0,
    }


def verify_theorem_3_2_and_proposition_3_3() -> dict[str, object]:
    etas = [-2.5, -1.8, -1.2, -0.7, -0.3, -0.1]
    sigmas = [0.8, 1.1, 0.6, 1.4, 0.9, 1.2]
    q = 0.01
    J = len(etas)
    weights, lam_star, cond5 = solve_bayes_small_q(etas, sigmas, q)
    budget_error = abs(sum(weights) - J)

    gammas = [math.sqrt(s * s + 1.0) for s in sigmas]
    grid_c = [-6.0 + 0.05 * k for k in range(241)]
    global_max_holds = True
    for e, g, w in zip(etas, gammas, weights):
        c_opt = inv_Phi(q * w)
        f_opt = Phi((c_opt - e) / g) - lam_star * Phi(c_opt)
        f_inf = 1.0 - lam_star
        max_grid = max(Phi((c - e) / g) - lam_star * Phi(c) for c in grid_c)
        if f_opt + 1e-12 < max(max_grid, f_inf):
            global_max_holds = False

    w_spj, _ = solve_spjotvoll_weights(etas, q)
    diffs = {}
    for s_val in [1.0, 0.1, 0.01, 1e-4]:
        w_b, _, _ = solve_bayes_small_q(etas, [s_val] * J, q)
        max_diff = max(abs(wb - ws) for wb, ws in zip(w_b, w_spj))
        diffs[f"sigma={s_val}"] = round(max_diff, 9)

    return {
        "cond5_holds": cond5,
        "lambda_star": round(lam_star, 6),
        "budget_error": budget_error,
        "global_lagrangian_maximum_holds": global_max_holds,
        "spjotvoll_convergence_max_diffs": diffs,
        "converges_to_spjotvoll": (
            diffs["sigma=1.0"] > diffs["sigma=0.1"] > diffs["sigma=0.01"] > diffs["sigma=0.0001"]
            and diffs["sigma=0.0001"] < 1e-6
        ),
    }


def verify_theorem_3_5_and_symmetry_breaking() -> dict[str, object]:
    J = 10
    q = 0.25  # J*q = 2.5 (non-integer), floor(Jq) = 2
    k_full = int(math.floor(J * q))
    w_rem = (J - k_full * (1.0 / q)) / (J - k_full)
    w_sym = [1.0 / q] * k_full + [w_rem] * (J - k_full)
    w_unif = [1.0] * J
    sigma_large = 1e4
    gamma_large = math.sqrt(sigma_large * sigma_large + 1.0)
    eta = -1.0

    def bayes_power(weights: list[float]) -> float:
        total = 0.0
        for w in weights:
            if q * w >= 1.0:
                total += 1.0
            else:
                total += Phi((inv_Phi(q * w) - eta) / gamma_large)
        return total

    pow_sym = bayes_power(w_sym)
    pow_unif = bayes_power(w_unif)
    theoretical_sym_limit = 0.5 * (J + k_full)

    # General case (Theorem 3.5 & Lemma 9.2) when Condition (5) fails (q = 0.35)
    etas_gen = [-0.4, -0.35, -0.3, -0.25, -0.2, -0.15, -0.1, -0.05]
    sigmas_gen = [1.5] * len(etas_gen)
    gammas_gen = [math.sqrt(s * s + 1.0) for s in sigmas_gen]
    Jg = len(etas_gen)
    qg = 0.35
    sum_at_lam1 = sum(Phi(c1_func(e, g, 1.0)) for e, g in zip(etas_gen, gammas_gen))
    cond5_fails = sum_at_lam1 < Jg * qg

    k_vals = [find_k_threshold(e, g) for e, g in zip(etas_gen, gammas_gen)]
    max_d_err = 0.0
    for e, g, kv in zip(etas_gen, gammas_gen, k_vals):
        c_val = c1_func(e, g, kv)
        d_val = (Phi((c_val - e) / g) - kv * Phi(c_val)) - (1.0 - kv)
        max_d_err = max(max_d_err, abs(d_val))

    def W_total(lam: float) -> float:
        tot = 0.0
        for e, g, kv in zip(etas_gen, gammas_gen, k_vals):
            if lam < kv:
                tot += 1.0 / qg
            else:
                tot += Phi(c1_func(e, g, lam)) / qg
        return tot

    # Follow Section 9.5.2 (Case 1 / Case 2): check continuous intervals (k_(i), k_(i+1))
    # and jump points k_(i), picking the closest candidate to Jg.
    sorted_k = sorted(k_vals)
    boundaries = [1e-6] + sorted_k + [1.0]
    best_W_star = None
    best_gap = float("inf")
    for idx in range(len(boundaries) - 1):
        left_k = boundaries[idx] + 1e-11
        right_k = boundaries[idx + 1] - 1e-11
        if left_k >= right_k:
            continue
        w_left = W_total(left_k)
        w_right = W_total(right_k)
        if w_right <= Jg <= w_left:
            lo, hi = left_k, right_k
            for _ in range(60):
                mid = 0.5 * (lo + hi)
                if W_total(mid) > Jg:
                    lo = mid
                else:
                    hi = mid
            w_mid = W_total(0.5 * (lo + hi))
            if abs(w_mid - Jg) < best_gap:
                best_gap = abs(w_mid - Jg)
                best_W_star = w_mid
        for cand_w in (w_left, w_right):
            if abs(cand_w - Jg) < best_gap:
                best_gap = abs(cand_w - Jg)
                best_W_star = cand_w

    assert best_W_star is not None
    q_star = best_W_star * qg / Jg
    q_star_gap = abs(q_star - qg)

    return {
        "symmetry_breaking_power": round(pow_sym, 6),
        "uniform_power_large_sigma": round(pow_unif, 6),
        "theoretical_symmetry_limit": theoretical_sym_limit,
        "symmetry_breaking_beats_uniform": pow_sym > pow_unif + 0.99,
        "cond5_fails_for_large_q": cond5_fails,
        "max_lemma_9_2_root_error": max_d_err,
        "W_star": round(best_W_star, 6),
        "q_star": round(q_star, 6),
        "q_star_gap": round(q_star_gap, 6),
        "q_star_bound": round(1.0 / (2.0 * Jg), 6),
        "theorem_3_5_bound_holds": q_star_gap <= 1.0 / (2.0 * Jg) + 1e-9,
    }


def verify_section_4_2_and_fwer_robustness() -> dict[str, object]:
    # Section 4.2 sparse means worst-case maximin comparison:
    # J = 1000, pi1 = 0.08 (80 large means M = -2.0, 920 small means m = -1e-3), q = 0.01
    J = 1000
    n1 = 80
    n0 = J - n1
    M = -2.0
    m = -1e-3
    q = 0.01
    etas = [M] * n1 + [m] * n0

    w_spj, _ = solve_spjotvoll_weights(etas, q)
    w_bayes, _, _ = solve_bayes_small_q(etas, [1.0] * J, q)

    def eval_objective(weights: list[float], sigma_true: float) -> float:
        gamma_true = math.sqrt(sigma_true * sigma_true + 1.0)
        total = 0.0
        for e, w in zip(etas, weights):
            if q * w <= 0.0:
                continue
            if q * w >= 1.0:
                total += 1.0
            else:
                total += Phi((inv_Phi(q * w) - e) / gamma_true)
        return total / J

    pow_spj_sigma0 = eval_objective(w_spj, 0.0)
    pow_bayes_sigma0 = eval_objective(w_bayes, 0.0)
    pow_unif_sigma0 = eval_objective([1.0] * J, 0.0)
    pow_spj_sigma1 = eval_objective(w_spj, 1.0)
    pow_bayes_sigma1 = eval_objective(w_bayes, 1.0)
    pow_unif_sigma1 = eval_objective([1.0] * J, 1.0)

    regret_bayes_sigma0 = pow_spj_sigma0 - pow_bayes_sigma0
    regret_spj_sigma1 = pow_bayes_sigma1 - pow_spj_sigma1
    min_relative_eff_bayes = min(pow_bayes_sigma0 / pow_spj_sigma0, 1.0)
    min_relative_eff_spj = min(1.0, pow_spj_sigma1 / pow_bayes_sigma1)

    # Verify exact frequentist PFER & FWER control under severe prior misspecification
    rng = random.Random(20261018)
    J_mc = 50
    q_mc = 0.001  # alpha = J_mc * q_mc = 0.05
    alpha_mc = J_mc * q_mc
    etas_mc = [-2.5 + 0.04 * i for i in range(J_mc)]
    w_mc, _, _ = solve_bayes_small_q(etas_mc, [1.0] * J_mc, q_mc)
    n_null = 40
    n_trials = 5000
    false_rejections = 0
    fwer_events = 0
    for _ in range(n_trials):
        any_false = False
        for i in range(n_null):
            t_i = rng.gauss(0.0, 1.0)
            p_i = Phi(t_i)
            if p_i <= q_mc * w_mc[i]:
                false_rejections += 1
                any_false = True
        if any_false:
            fwer_events += 1
    pfer_mc = false_rejections / n_trials
    fwer_mc = fwer_events / n_trials

    return {
        "pow_spj_sigma0": round(pow_spj_sigma0, 6),
        "pow_bayes_sigma0": round(pow_bayes_sigma0, 6),
        "pow_unif_sigma0": round(pow_unif_sigma0, 6),
        "pow_spj_sigma1": round(pow_spj_sigma1, 6),
        "pow_bayes_sigma1": round(pow_bayes_sigma1, 6),
        "pow_unif_sigma1": round(pow_unif_sigma1, 6),
        "spj_weight_on_small_mean": round(w_spj[-1], 6),
        "bayes_weight_on_small_mean": round(w_bayes[-1], 6),
        "regret_bayes_at_sigma0": round(regret_bayes_sigma0, 6),
        "regret_spj_at_sigma1": round(regret_spj_sigma1, 6),
        "min_relative_eff_bayes": round(min_relative_eff_bayes, 6),
        "min_relative_eff_spj": round(min_relative_eff_spj, 6),
        "bayes_has_maximin_advantage": (
            regret_bayes_sigma0 < regret_spj_sigma1
            and min_relative_eff_bayes > min_relative_eff_spj
            and pow_spj_sigma1 < pow_unif_sigma1 < pow_bayes_sigma1
        ),
        "alpha_mc": alpha_mc,
        "pfer_mc_misspecified": round(pfer_mc, 5),
        "fwer_mc_misspecified": round(fwer_mc, 5),
        "fwer_controlled_under_misspecification": fwer_mc <= alpha_mc,
    }


def main() -> None:
    p31 = verify_proposition_3_1_sparse_means()
    t32 = verify_theorem_3_2_and_proposition_3_3()
    t35 = verify_theorem_3_5_and_symmetry_breaking()
    s42 = verify_section_4_2_and_fwer_robustness()

    all_passed = bool(
        p31["regime1_thresh_gt_q"]
        and p31["regime2_thresh_le_q"]
        and p31["regime2_strictly_beats_all_on_M"]
        and p31["hotspot_exceeds_3x"]
        and t32["cond5_holds"]
        and t32["budget_error"] < 1e-9
        and t32["global_lagrangian_maximum_holds"]
        and t32["converges_to_spjotvoll"]
        and t35["symmetry_breaking_beats_uniform"]
        and t35["cond5_fails_for_large_q"]
        and t35["max_lemma_9_2_root_error"] < 1e-9
        and t35["theorem_3_5_bound_holds"]
        and s42["bayes_has_maximin_advantage"]
        and s42["fwer_controlled_under_misspecification"]
    )
    summary = {
        "concept_id": "AIMech:BayesOptimalPValueWeightingUnderGaussianPrior",
        "proposition_3_1_sparse_means": p31,
        "theorem_3_2_and_proposition_3_3": t32,
        "theorem_3_5_and_symmetry_breaking": t35,
        "section_4_2_maximin_and_fwer": s42,
        "all_checks_passed": all_passed,
    }
    print(json.dumps(summary, indent=2))
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
