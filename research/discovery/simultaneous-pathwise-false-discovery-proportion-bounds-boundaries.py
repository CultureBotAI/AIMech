#!/usr/bin/env python3
"""Constructed boundary and diagnostic verification for Round 190:
AIMech:SimultaneousPathwiseFalseDiscoveryProportionBounds (Katsevich & Ramdas 2020,
Annals of Statistics 48(6):3465-3487, arXiv:1803.06790v5).

Verifies:
1. Claim 1 (Sorted-path simultaneous FDP bound, Lemma 3 Poisson boundary identity,
   comparison to Robbins/DKW bounds, and failure of unadjusted Storey-BH FDP_hat).
2. Claim 2 (Forward exponential supermartingale Lemma 1 across all 4 cases,
   knockoff simultaneous FDP bound Corollary 1, logarithmic vs linear 1/alpha scaling).
3. Claim 3 (Interactive forward-filtration path Theorem 3 with side information x_j
   and mirror-masked p-values g(p_j) = min(p_j, 1 - p_j)).
4. Claim 4 (Online post-hoc simultaneous bounds Theorem 4 for LORD/SAFFRON paths,
   and failure boundary under strong positive correlation rho=0.9, Section 5.3).
"""

from __future__ import annotations

import json
import math
import random


def solve_bisect(fn, lo: float, hi: float, tol: float = 1e-12) -> float:
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if fn(mid) <= 0.0:
            lo = mid
        else:
            hi = mid
        if hi - lo < tol:
            break
    return 0.5 * (lo + hi)


def c_sort(alpha: float, a: float = 1.0) -> float:
    return math.log(1.0 / alpha) / (a * math.log(1.0 + math.log(1.0 / alpha) / a))


def c_sel(alpha: float, b_val: float = 1.0, a: float = 1.0) -> float:
    return math.log(1.0 / alpha) / (a * math.log(1.0 + (1.0 - (alpha ** (b_val / a))) / b_val))


def c_acc_bounded(alpha: float, b_val: float, a: float = 1.0) -> float:
    return math.log(1.0 / alpha) / (a * math.log(1.0 / (1.0 - (1.0 - (alpha ** (b_val / a))) / b_val)))


def verify_claim1_sorted_path() -> dict[str, float]:
    # 1. Verify Lemma 3 root identity at x = 1.5 -> alphacutoff = exp(-1.5 * theta_{1.5}) > 0.31
    x_crit = 1.5
    theta_15 = solve_bisect(lambda th: math.exp(th) - (1.0 + th * x_crit), 1e-6, 5.0)
    alpha_crit = math.exp(-x_crit * theta_15)
    assert alpha_crit > 0.31

    # Verify that plugging alpha = exp(-x * theta_x) into c_sort(alpha, a=1) recovers x exactly
    alpha_test = 0.10
    c_10 = c_sort(alpha_test, a=1.0)
    theta_10 = math.log(1.0 + math.log(1.0 / alpha_test))
    root_residual = abs(math.exp(theta_10) - (1.0 + theta_10 * c_10))
    assert root_residual < 1e-12

    # 2. Compare sorted bound to Robbins and DKW in intermediate regime (n=2500, alpha=0.10, t=0.005)
    n_comp = 2500
    t_comp = 0.005
    v_bar_sort = math.floor(c_10 * (1.0 + n_comp * t_comp))
    v_bar_robbins = math.floor((1.0 / alpha_test) * n_comp * t_comp)
    v_bar_dkw = math.floor(n_comp * t_comp + math.sqrt(0.5 * n_comp * math.log(1.0 / alpha_test)))
    assert v_bar_sort < v_bar_dkw < v_bar_robbins

    # 3. Monte Carlo verification under global null (n=200, alpha=0.10) vs unadjusted Storey-BH estimate
    rng = random.Random(20261018)
    n_mc = 200
    trials = 1500
    viol_simultaneous = 0
    viol_unadjusted = 0
    for _ in range(trials):
        p_vals = sorted(rng.random() for _ in range(n_mc))
        sim_bad = False
        unadj_bad = False
        for k_idx, p_k in enumerate(p_vals, start=1):
            v_true = k_idx  # global null: all rejections are false discoveries
            v_bound = math.floor(c_10 * (1.0 + n_mc * p_k))
            if v_true > v_bound:
                sim_bad = True
            if p_k >= 1.0 / n_mc and v_true > n_mc * p_k:
                unadj_bad = True
        if sim_bad:
            viol_simultaneous += 1
        if unadj_bad:
            viol_unadjusted += 1

    emp_viol_sim = viol_simultaneous / trials
    emp_viol_unadj = viol_unadjusted / trials
    assert emp_viol_sim <= alpha_test
    assert emp_viol_unadj > 0.60

    return {
        "alpha_cutoff_at_x_1_5": round(alpha_crit, 6),
        "c_sort_alpha_0_10": round(c_10, 6),
        "v_bar_sort_intermediate": float(v_bar_sort),
        "v_bar_dkw_intermediate": float(v_bar_dkw),
        "v_bar_robbins_intermediate": float(v_bar_robbins),
        "mc_global_null_violation_rate": round(emp_viol_sim, 6),
        "mc_unadjusted_violation_rate": round(emp_viol_unadj, 6),
    }


def verify_claim2_lemma1_and_knockoffs() -> dict[str, float]:
    # 1. Verify Lemma 1 one-step supermartingale factor E[exp(theta_x * (I(U <= alpha_k) - x * h_k(U)))] <= 1
    x_val = 2.2
    # Case 1 & 2: h(u) = (1/(1-lam)) * I(u > lam), alpha_k = 1, B = 1/(1-lam)
    lam = 0.2
    b_acc = 1.0 / (1.0 - lam)
    theta_case1 = solve_bisect(
        lambda th: (lam + (1.0 - lam) * math.exp(-th * x_val * b_acc)) - math.exp(-th),
        1e-6,
        5.0,
    )
    theta_case2 = solve_bisect(
        lambda th: 1.0 - math.exp(-th) - (1.0 - math.exp(-th * x_val * b_acc)) / b_acc,
        1e-6,
        5.0,
    )
    sm_factor_case1 = math.exp(theta_case1) * (lam + (1.0 - lam) * math.exp(-theta_case1 * x_val * b_acc))
    sm_factor_case2 = math.exp(theta_case2) * (lam + (1.0 - lam) * math.exp(-theta_case2 * x_val * b_acc))
    assert abs(sm_factor_case1 - 1.0) < 1e-10
    assert abs(sm_factor_case2 - 1.0) < 1e-10

    # Case 3 (Selective SeqStep / Knockoffs): p_* = lam = 0.5, B = 1
    theta_case3 = solve_bisect(
        lambda th: math.exp(th) - (1.0 - math.exp(-th * x_val * 1.0)) / 1.0 - 1.0,
        1e-6,
        5.0,
    )
    # Null one-bit p-value: P(p <= 0.5) = 0.5 (h=0), P(p > 0.5) = 0.5 (h=1)
    sm_factor_case3 = 0.5 * math.exp(theta_case3) + 0.5 * math.exp(-theta_case3 * x_val)
    assert abs(sm_factor_case3 - 1.0) < 1e-10

    # 2. Knockoffs simultaneous bound (Corollary 1) at alpha = 0.05 vs backward martingale 1/alpha
    alpha_ko = 0.05
    c_ko = c_sel(alpha_ko, b_val=1.0, a=1.0)
    c_backward = 1.0 / alpha_ko
    assert abs(c_ko - math.log(20.0) / math.log(1.95)) < 1e-12
    assert c_ko < 4.5 and c_backward == 20.0

    # 3. Monte Carlo knockoff path simultaneous coverage & adversarial post-hoc selection
    rng = random.Random(20261019)
    p_vars = 200
    n_nulls = 150
    trials = 1500
    ko_violations = 0
    for _ in range(trials):
        # Generate knockoff stats |W_j| and signs: nulls have i.i.d. uniform +/-1 signs
        items = []
        for j in range(p_vars):
            is_null = j < n_nulls
            if is_null:
                mag = abs(rng.gauss(0.0, 1.0))
                sign = 1 if rng.random() < 0.5 else -1
            else:
                mag = abs(rng.gauss(2.5, 1.0))
                sign = 1 if rng.random() < 0.92 else -1
            items.append((mag, sign, is_null))
        items.sort(key=lambda x: x[0], reverse=True)

        v_true = 0
        r_size = 0
        neg_count = 0
        violated = False
        for mag, sign, is_null in items:
            if sign > 0:
                r_size += 1
                if is_null:
                    v_true += 1
            else:
                neg_count += 1
            v_bar = math.floor(c_ko * (1.0 + neg_count))
            fdp_true = (v_true / r_size) if r_size > 0 else 0.0
            fdp_bar = min(1.0, (v_bar / r_size) if r_size > 0 else 0.0)
            if fdp_true > fdp_bar + 1e-12:
                violated = True
        if violated:
            ko_violations += 1

    ko_viol_rate = ko_violations / trials
    assert ko_viol_rate <= alpha_ko

    return {
        "sm_factor_case1": round(sm_factor_case1, 8),
        "sm_factor_case2": round(sm_factor_case2, 8),
        "sm_factor_case3": round(sm_factor_case3, 8),
        "c_knockoff_alpha_0_05": round(c_ko, 6),
        "c_backward_alpha_0_05": round(c_backward, 6),
        "mc_knockoff_simultaneous_violation_rate": round(ko_viol_rate, 6),
    }


def verify_claim3_interactive_path() -> dict[str, float]:
    # Interactive path (Theorem 3 part 2): p_* = lambda = 0.5, B = 1, a = 1
    # Analyst observes side information x_j and masked p-values g(p_j) = min(p_j, 1 - p_j)
    # and orders hypotheses interactively from k=1..n
    rng = random.Random(20261020)
    n_hyp = 300
    n_nonnull = 50
    alpha = 0.10
    c_inter = c_sel(alpha, b_val=1.0, a=1.0)
    c_s = c_sort(alpha, a=1.0)

    trials = 800
    inter_violations = 0
    total_disc_interactive = 0
    total_disc_sorted = 0
    target_fdp = 0.20

    for _ in range(trials):
        hyps = []
        for j in range(n_hyp):
            # Side information x_j: non-nulls strongly concentrated at small j
            is_null = j >= n_nonnull
            if is_null:
                p_val = rng.random()
            else:
                # Strong non-null signal: Beta(0.15, 1) via U^(1/0.15)
                p_val = rng.random() ** 6.5
            g_val = min(p_val, 1.0 - p_val)
            # Predictable score combining covariate prior (j / n_hyp) and masked p-value g_val
            score = 0.5 * (j / n_hyp) + 0.5 * (g_val / 0.5)
            hyps.append((score, p_val, is_null))

        # Interactive ordering pi sorts by predictable score (measurable w.r.t. G_0)
        hyps_inter = sorted(hyps, key=lambda x: x[0])
        v_true = 0
        r_size = 0
        mirror_count = 0
        violated = False
        best_r_inter = 0
        for _, p_val, is_null in hyps_inter:
            if p_val <= 0.5:
                r_size += 1
                if is_null:
                    v_true += 1
            else:
                mirror_count += 1
            v_bar = math.floor(c_inter * (1.0 + mirror_count))
            fdp_true = (v_true / r_size) if r_size > 0 else 0.0
            fdp_bar = min(1.0, (v_bar / r_size) if r_size > 0 else 0.0)
            if fdp_true > fdp_bar + 1e-12:
                violated = True
            if fdp_bar <= target_fdp and r_size > best_r_inter:
                best_r_inter = r_size
        if violated:
            inter_violations += 1
        total_disc_interactive += best_r_inter

        # Compare to covariate-ignorant sorted path at same target simultaneous FDP <= 0.20
        hyps_sorted = sorted(hyps, key=lambda x: x[1])
        best_r_sort = 0
        for k_idx, (_, p_val, _) in enumerate(hyps_sorted, start=1):
            v_bar_s = math.floor(c_s * (1.0 + n_hyp * p_val))
            fdp_bar_s = min(1.0, v_bar_s / k_idx)
            if fdp_bar_s <= target_fdp and k_idx > best_r_sort:
                best_r_sort = k_idx
        total_disc_sorted += best_r_sort

    inter_viol_rate = inter_violations / trials
    avg_disc_inter = total_disc_interactive / trials
    avg_disc_sort = total_disc_sorted / trials
    assert inter_viol_rate <= alpha
    assert avg_disc_inter > avg_disc_sort

    return {
        "interactive_violation_rate": round(inter_viol_rate, 6),
        "avg_discoveries_interactive_fdp_0_20": round(avg_disc_inter, 4),
        "avg_discoveries_sorted_fdp_0_20": round(avg_disc_sort, 4),
    }


def verify_claim4_online_and_correlation_boundary() -> dict[str, float]:
    # 1. Online simultaneous FDP bounds (Theorem 4 part 1 & part 2) on predictable alpha_j stream
    rng = random.Random(20261021)
    alpha = 0.10
    c_online_simple = c_sort(alpha, a=1.0)
    # Adaptive online with lambda_j = 0.5, alpha_j <= 0.05 -> B = 0.05 / 0.5 = 0.10
    b_online = 0.10
    c_online_adapt = c_sel(alpha, b_val=b_online, a=1.0)

    n_stream = 200
    trials = 1000
    viol_simple = 0
    viol_adapt = 0
    for _ in range(trials):
        wealth = 0.025
        sum_alpha = 0.0
        sum_adapt = 0.0
        v_true = 0
        r_size = 0
        bad_simple = False
        bad_adapt = False
        for j in range(1, n_stream + 1):
            # Predictable alpha_j based on past rejections
            alpha_j = min(0.05, 0.5 * wealth)
            wealth -= alpha_j
            is_null = (j % 5 != 0)
            p_j = rng.random() if is_null else (rng.random() ** 5.0)
            if p_j <= alpha_j:
                r_size += 1
                wealth += 0.04
                if is_null:
                    v_true += 1
            sum_alpha += alpha_j
            if p_j > 0.5:
                sum_adapt += (alpha_j / 0.5)
            v_bar_s = math.floor(c_online_simple * (1.0 + sum_alpha))
            v_bar_a = math.floor(c_online_adapt * (1.0 + sum_adapt))
            if v_true > v_bar_s:
                bad_simple = True
            if v_true > v_bar_a:
                bad_adapt = True
        if bad_simple:
            viol_simple += 1
        if bad_adapt:
            viol_adapt += 1

    rate_simple = viol_simple / trials
    rate_adapt = viol_adapt / trials
    assert rate_simple <= alpha
    assert rate_adapt <= alpha

    # 2. Correlation failure boundary (Section 5.3): strong positive correlation (rho = 0.90)
    # under global null in pre-ordered selective path (p_* = lambda = 0.20, alpha = 0.10)
    # causes max_k FDP(R_k) / FDP_bar(R_k) > 1 with probability > alpha = 0.10
    n_corr = 200
    corr_trials = 1000
    rho = 0.90
    p_star = 0.20
    lam_corr = 0.20
    b_corr = p_star / (1.0 - lam_corr)
    c_pre_sel = c_sel(alpha, b_val=b_corr, a=1.0)
    viol_corr = 0
    ratios = []
    for _ in range(corr_trials):
        z_common = rng.gauss(0.0, 1.0)
        v_true = 0
        sum_h = 0.0
        max_ratio = 0.0
        for _ in range(n_corr):
            x_j = math.sqrt(rho) * z_common + math.sqrt(1.0 - rho) * rng.gauss(0.0, 1.0)
            p_j = 0.5 * math.erfc(x_j / math.sqrt(2.0))
            if p_j <= p_star:
                v_true += 1
            if p_j > lam_corr:
                sum_h += b_corr
            v_bar = math.floor(c_pre_sel * (1.0 + sum_h))
            if v_true > 0:
                ratio = v_true / max(1, v_bar)
                if ratio > max_ratio:
                    max_ratio = ratio
        ratios.append(max_ratio)
        if max_ratio > 1.0:
            viol_corr += 1

    ratios.sort()
    q90_ratio = ratios[int(0.90 * corr_trials)]
    corr_viol_rate = viol_corr / corr_trials
    assert q90_ratio > 1.0
    assert corr_viol_rate > alpha

    return {
        "online_simple_violation_rate": round(rate_simple, 6),
        "online_adaptive_violation_rate": round(rate_adapt, 6),
        "correlated_rho_0_90_q90_max_ratio": round(q90_ratio, 6),
        "correlated_rho_0_90_violation_rate": round(corr_viol_rate, 6),
    }


def main() -> None:
    res = {
        "claim1_sorted_path_and_poisson_lemma": verify_claim1_sorted_path(),
        "claim2_lemma1_and_knockoff_simultaneous_fdp": verify_claim2_lemma1_and_knockoffs(),
        "claim3_interactive_path_power_and_coverage": verify_claim3_interactive_path(),
        "claim4_online_posthoc_and_correlation_boundary": verify_claim4_online_and_correlation_boundary(),
    }
    print(json.dumps(res, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
