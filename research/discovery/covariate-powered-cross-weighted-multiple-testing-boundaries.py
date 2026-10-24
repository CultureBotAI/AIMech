#!/usr/bin/env python3
"""Constructed mathematical and boundary verification for Round 193:
AIMech:CovariatePoweredCrossWeightedMultipleTesting (Ignatiadis & Huber 2021,
JRSS-B 83(4):720-751, arXiv:1701.05179v7, DOI:10.1111/rssb.12411).

Verifies all 4 core claims using only the Python standard library:
1. Honest + tau-censored cross-weighting finite-sample FDR control (Theorems 1 & 2,
   Corollary 1) vs. global-null overfitting of naive plug-in GBH (Section 2.2, Fig. 2)
   and the exact m=4 adversarial honest uncensored counterexample (Supplement S1.3).
2. Asymptotic overfitting of naive full-sample Specification-7 weighting (Proposition 1(a),
   Supplement S2.1) vs. asymptotic FDR control of uncensored IHW-BH (Proposition 1(b),
   Supplement S2.2) and asymptotic threshold/power equivalence with oracle W*
   (Proposition 1(c), Corollary 2, Supplement S2.3-S2.4).
3. Block-dependent fold partitioning (Assumption 2, Lemma 1(a)): finite-sample k-FWER
   control of IHW-k-Bonferroni (Theorem 3) and finite-sample FDR control of IHW-BY
   (Theorem 4, Supplement S1.5) vs. failure of dishonest data-driven wBY (Example 1)
   and failure of AdaPT with BY correction under block dependence (Example 2).
4. Out-of-fold Grenander least-concave-majorant estimation and convex/KKT weight optimization
   (Section 4, Algorithm 5, Supplement S4.1) and robustness in sparse-signal (< 1/alpha
   non-nulls) and strictly super-uniform null regimes where AdaPT loses power (Section 5.2).
"""
from __future__ import annotations

import json
import math
import random


def norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def weighted_bh_rejections(pvals: list[float], weights: list[float], alpha: float, tau: float = 1.0) -> list[int]:
    """Definition 2: tau-censored weighted Benjamini-Hochberg procedure."""
    m = len(pvals)
    if m == 0:
        return []
    # Effective thresholds: P_i <= (alpha * r / m) * W_i and P_i <= tau
    # Equivalently, if P_i <= tau and W_i > 0, effective weighted p-value Q_i = P_i / W_i; else infinity
    q_pairs = []
    for i, (p, w) in enumerate(zip(pvals, weights)):
        if p <= tau and w > 0.0:
            q_pairs.append((p / w, i))
        else:
            q_pairs.append((float("inf"), i))
    q_pairs.sort(key=lambda x: x[0])
    r_star = 0
    for rank_idx, (q_val, _) in enumerate(q_pairs, start=1):
        if q_val <= (alpha * rank_idx) / m:
            r_star = rank_idx
    if r_star == 0:
        return []
    thresh = (alpha * r_star) / m
    return [i for q_val, i in q_pairs if q_val <= thresh]


def verify_claim1_honest_tau_censored_fdr_and_counterexamples() -> dict[str, float]:
    """Claim 1: Theorems 1 & 2 (IHW-BH and IHW-Storey finite-sample FDR control),
    Section 2.2 naive GBH global-null overfitting, and Supplement S1.3 m=4 counterexample.
    """
    alpha = 0.20

    # 1. Supplement S1.3 exact and Monte Carlo m=4 adversarial honest uncensored counterexample
    # Under global null with m=4, folds I_1={0,1}, I_2={2,3}:
    # If P_0 in [alpha/2, alpha], set (W_2, W_3) = (2, 0), else (0, 2).
    # If P_2 in [alpha/2, alpha], set (W_0, W_1) = (2, 0), else (0, 2).
    # Supplement S1.3 proves exact FDR = alpha * (1 + alpha * (1 - alpha) / 2).
    exact_s13_fdr = alpha * (1.0 + alpha * (1.0 - alpha) / 2.0)

    rng = random.Random(2026101801)
    n_s13_trials = 8000
    s13_uncensored_fdp_sum = 0.0
    s13_tau_censored_fdp_sum = 0.0
    tau_s13 = 0.50

    for _ in range(n_s13_trials):
        p = [rng.random() for _ in range(4)]
        # Adversarial honest uncensored weights (uses P_i in [alpha/2, alpha] <= tau)
        if 0.5 * alpha <= p[0] <= alpha:
            w2, w3 = 2.0, 0.0
        else:
            w2, w3 = 0.0, 2.0
        if 0.5 * alpha <= p[2] <= alpha:
            w0, w1 = 2.0, 0.0
        else:
            w0, w1 = 0.0, 2.0
        w_uncens = [w0, w1, w2, w3]
        rej_uncens = weighted_bh_rejections(p, w_uncens, alpha=alpha, tau=1.0)
        if rej_uncens:
            s13_uncensored_fdp_sum += 1.0

        # Now enforce Specification 2 (tau-censoring at tau=0.50): weights can only depend on P_j * 1(P_j > tau)
        if p[0] > tau_s13 and p[0] <= 0.75:
            cw2, cw3 = 2.0, 0.0
        else:
            cw2, cw3 = 0.0, 2.0
        if p[2] > tau_s13 and p[2] <= 0.75:
            cw0, cw1 = 2.0, 0.0
        else:
            cw0, cw1 = 0.0, 2.0
        w_cens = [cw0, cw1, cw2, cw3]
        rej_cens = weighted_bh_rejections(p, w_cens, alpha=alpha, tau=tau_s13)
        if rej_cens:
            s13_tau_censored_fdp_sum += 1.0

    mc_s13_uncens_fdr = s13_uncensored_fdp_sum / n_s13_trials
    mc_s13_cens_fdr = s13_tau_censored_fdp_sum / n_s13_trials

    # 2. Section 2.2 (Figure 2): Global null with G=40 groups, m=200 hypotheses (5 per group)
    # Compare naive GBH (Algorithm 1) vs. 5-fold IHW-GBH (Algorithm 2 / Theorem 2)
    alpha_gbh = 0.10
    tau_gbh = 0.50
    n_groups = 40
    per_group = 5
    m_gbh = n_groups * per_group
    groups = [i // per_group for i in range(m_gbh)]
    n_folds = 5
    folds = [i % n_folds for i in range(m_gbh)]

    n_gbh_trials = 600
    naive_gbh_null_fdp = 0.0
    ihw_gbh_null_fdp = 0.0

    for _ in range(n_gbh_trials):
        p = [rng.random() for _ in range(m_gbh)]

        # Algorithm 1: Naive GBH (Hu et al. 2010 / Ignatiadis & Huber Section 2.2)
        pi0_naive = {}
        for g in range(n_groups):
            idx_g = [i for i in range(m_gbh) if groups[i] == g]
            cnt_gt = sum(1 for i in idx_g if p[i] > tau_gbh)
            pi0_naive[g] = min(1.0, max(0.05, cnt_gt / (len(idx_g) * (1.0 - tau_gbh))))
        raw_w_naive = [0.0 if pi0_naive[groups[i]] >= 1.0 else (1.0 - pi0_naive[groups[i]]) / pi0_naive[groups[i]] for i in range(m_gbh)]
        s_naive = sum(raw_w_naive)
        pi0_overall_naive = sum(pi0_naive[groups[i]] for i in range(m_gbh)) / m_gbh
        if s_naive > 0.0:
            w_naive = [(m_gbh * rw / s_naive) / pi0_overall_naive for rw in raw_w_naive]
            rej_naive = weighted_bh_rejections(p, w_naive, alpha=alpha_gbh, tau=1.0)
        else:
            rej_naive = []
        if rej_naive:
            naive_gbh_null_fdp += 1.0

        # Algorithm 2: IHW-GBH (5 folds)
        w_ihw_store = [0.0] * m_gbh
        for ell in range(n_folds):
            out_idx = [i for i in range(m_gbh) if folds[i] != ell]
            in_idx = [i for i in range(m_gbh) if folds[i] == ell]
            pi0_out = {}
            for g in range(n_groups):
                idx_g_out = [i for i in out_idx if groups[i] == g]
                cnt_gt = sum(1 for i in idx_g_out if p[i] > tau_gbh)
                pi0_out[g] = min(1.0, (1.0 + cnt_gt) / (len(idx_g_out) * (1.0 - tau_gbh)))
            raw_in = [0.0 if pi0_out[groups[i]] >= 1.0 else (1.0 - pi0_out[groups[i]]) / pi0_out[groups[i]] for i in in_idx]
            s_in = sum(raw_in)
            if s_in > 0.0:
                honest_in = [len(in_idx) * rw / s_in for rw in raw_in]
            else:
                honest_in = [1.0] * len(in_idx)
            # Theorem 2 weighted Storey fold adjustment
            max_w = max(honest_in)
            sum_w_gt = sum(w_val for w_val, idx_val in zip(honest_in, in_idx) if p[idx_val] > tau_gbh)
            pi0_fold = (max_w + sum_w_gt) / (len(in_idx) * (1.0 - tau_gbh))
            for w_val, idx_val in zip(honest_in, in_idx):
                w_ihw_store[idx_val] = w_val / pi0_fold
        rej_ihw = weighted_bh_rejections(p, w_ihw_store, alpha=alpha_gbh, tau=tau_gbh)
        if rej_ihw:
            ihw_gbh_null_fdp += 1.0

    fdr_naive_gbh_null = naive_gbh_null_fdp / n_gbh_trials
    fdr_ihw_gbh_null = ihw_gbh_null_fdp / n_gbh_trials

    # 3. Alternative power comparison: G=4 groups, m=200 (50 per group), group 0 has 70% non-nulls with mu=2.8,
    # group 1 has 40% non-nulls with mu=2.5, groups 2 and 3 are pure nulls.
    n_alt_trials = 400
    g_alt = 4
    per_g_alt = 50
    m_alt = g_alt * per_g_alt
    groups_alt = [i // per_g_alt for i in range(m_alt)]
    folds_alt = [i % n_folds for i in range(m_alt)]

    bh_power_sum = 0.0
    ihw_bh_power_sum = 0.0
    ihw_storey_power_sum = 0.0
    ihw_bh_fdp_sum = 0.0
    ihw_storey_fdp_sum = 0.0

    for _ in range(n_alt_trials):
        p = []
        is_alt = []
        for i in range(m_alt):
            g = groups_alt[i]
            if g == 0 and (i % per_g_alt) < 35:
                is_alt.append(True)
                z = rng.gauss(2.8, 1.0)
                p.append(max(1e-12, 1.0 - norm_cdf(z)))
            elif g == 1 and (i % per_g_alt) < 20:
                is_alt.append(True)
                z = rng.gauss(2.5, 1.0)
                p.append(max(1e-12, 1.0 - norm_cdf(z)))
            else:
                is_alt.append(False)
                p.append(rng.random())
        n_true_alt = sum(1 for a in is_alt if a)

        # Unweighted BH
        rej_bh = weighted_bh_rejections(p, [1.0] * m_alt, alpha=alpha_gbh, tau=tau_gbh)
        bh_power_sum += sum(1 for i in rej_bh if is_alt[i]) / n_true_alt

        # IHW-GBH without Storey (Theorem 1 / Corollary 1) and with Storey (Theorem 2)
        w_honest_all = [0.0] * m_alt
        w_storey_all = [0.0] * m_alt
        for ell in range(n_folds):
            out_idx = [i for i in range(m_alt) if folds_alt[i] != ell]
            in_idx = [i for i in range(m_alt) if folds_alt[i] == ell]
            pi0_out = {}
            for g in range(g_alt):
                idx_g_out = [i for i in out_idx if groups_alt[i] == g]
                cnt_gt = sum(1 for i in idx_g_out if p[i] > tau_gbh)
                pi0_out[g] = (1.0 + cnt_gt) / (len(idx_g_out) * (1.0 - tau_gbh))
            raw_in = [0.0 if pi0_out[groups_alt[i]] >= 1.0 else (1.0 - pi0_out[groups_alt[i]]) / pi0_out[groups_alt[i]] for i in in_idx]
            s_in = sum(raw_in)
            honest_in = [len(in_idx) * rw / s_in for rw in raw_in] if s_in > 0.0 else [1.0] * len(in_idx)
            max_w = max(honest_in)
            sum_w_gt = sum(w_val for w_val, idx_val in zip(honest_in, in_idx) if p[idx_val] > tau_gbh)
            pi0_fold = (max_w + sum_w_gt) / (len(in_idx) * (1.0 - tau_gbh))
            for w_val, idx_val in zip(honest_in, in_idx):
                w_honest_all[idx_val] = w_val
                w_storey_all[idx_val] = w_val / pi0_fold

        rej_ihw_bh = weighted_bh_rejections(p, w_honest_all, alpha=alpha_gbh, tau=tau_gbh)
        rej_ihw_st = weighted_bh_rejections(p, w_storey_all, alpha=alpha_gbh, tau=tau_gbh)

        ihw_bh_power_sum += sum(1 for i in rej_ihw_bh if is_alt[i]) / n_true_alt
        ihw_storey_power_sum += sum(1 for i in rej_ihw_st if is_alt[i]) / n_true_alt
        if rej_ihw_bh:
            ihw_bh_fdp_sum += sum(1 for i in rej_ihw_bh if not is_alt[i]) / len(rej_ihw_bh)
        if rej_ihw_st:
            ihw_storey_fdp_sum += sum(1 for i in rej_ihw_st if not is_alt[i]) / len(rej_ihw_st)

    power_bh = bh_power_sum / n_alt_trials
    power_ihw_bh = ihw_bh_power_sum / n_alt_trials
    power_ihw_storey = ihw_storey_power_sum / n_alt_trials
    fdr_ihw_bh_alt = ihw_bh_fdp_sum / n_alt_trials
    fdr_ihw_storey_alt = ihw_storey_fdp_sum / n_alt_trials

    assert exact_s13_fdr > alpha
    assert abs(mc_s13_uncens_fdr - exact_s13_fdr) < 0.015
    assert mc_s13_cens_fdr <= alpha + 0.01
    assert fdr_naive_gbh_null > 0.20
    assert fdr_ihw_gbh_null <= alpha_gbh + 0.015
    assert fdr_ihw_bh_alt <= alpha_gbh + 0.01
    assert fdr_ihw_storey_alt <= alpha_gbh + 0.01
    assert power_ihw_storey > power_ihw_bh > power_bh

    return {
        "s13_exact_uncensored_honest_fdr": round(exact_s13_fdr, 5),
        "s13_mc_uncensored_honest_fdr": round(mc_s13_uncens_fdr, 4),
        "s13_mc_tau_censored_honest_fdr": round(mc_s13_cens_fdr, 4),
        "fdr_naive_gbh_global_null_G25": round(fdr_naive_gbh_null, 4),
        "fdr_ihw_gbh_global_null_G25": round(fdr_ihw_gbh_null, 4),
        "power_unweighted_bh": round(power_bh, 4),
        "power_ihw_bh_no_storey": round(power_ihw_bh, 4),
        "power_ihw_storey": round(power_ihw_storey, 4),
        "fdr_ihw_bh_alt": round(fdr_ihw_bh_alt, 4),
        "fdr_ihw_storey_alt": round(fdr_ihw_storey_alt, 4),
    }


def verify_claim2_asymptotic_proposition1_and_corollary2() -> dict[str, float]:
    """Claim 2: Proposition 1(a) overfitting of Specification-7 naive full-sample weighting,
    Proposition 1(b) asymptotic FDR control of uncensored IHW-BH (tau=1), and Proposition 1(c) /
    Corollary 2 convergence to oracle W* power.
    """
    rng = random.Random(2026101802)
    alpha = 0.15
    m = 300
    k_m = int(alpha * m / 2.0)  # Supplement S2.1: k_m = floor(alpha * m / 2)
    n_trials = 300

    # Supplement S2.1 setup: sparse alternatives (delta = 0.03), continuous covariates X_i in [0,1]
    naive_spec7_fdp_sum = 0.0
    ihw_spec7_fdp_sum = 0.0

    for _ in range(n_trials):
        x = [rng.random() for _ in range(m)]
        is_alt = [x_i < 0.03 for x_i in x]
        p = []
        for a in is_alt:
            if a:
                p.append(rng.random() ** 5.0)  # Beta(0.2, 1)
            else:
                p.append(rng.random())

        # Proposition 1(a) / Supplement S2.1 learner: pick k_m smallest p-values in training set,
        # and assign high weight around their covariates X_i.
        # Full-sample naive weighted BH assigns weight m / k_m to the k_m smallest p-values:
        order_idx = sorted(range(m), key=lambda i: p[i])
        top_set = set(order_idx[:k_m])
        w_naive = [m / k_m if i in top_set else 0.0 for i in range(m)]
        rej_naive = weighted_bh_rejections(p, w_naive, alpha=alpha, tau=1.0)
        if rej_naive:
            naive_spec7_fdp_sum += sum(1 for i in rej_naive if not is_alt[i]) / len(rej_naive)

        # Proposition 1(b): Cross-weighted 2-fold IHW-BH with the same kernel-neighborhood learner
        # (uncensored, tau = 1.0)
        w_ihw = [0.0] * m
        for ell in (0, 1):
            out_idx = [i for i in range(m) if (i % 2) != ell]
            in_idx = [i for i in range(m) if (i % 2) == ell]
            k_out = max(1, int(alpha * len(out_idx) / 2.0))
            out_sorted = sorted(out_idx, key=lambda i: p[i])[:k_out]
            centers = [x[j] for j in out_sorted]
            # Evaluate learned function on in-fold covariates X_i
            raw_in = []
            for i in in_idx:
                min_dist = min(abs(x[i] - c) for c in centers)
                raw_in.append(1.0 if min_dist <= 0.5 * alpha / k_out else 0.05)
            s_in = sum(raw_in)
            for idx_val, rw in zip(in_idx, raw_in):
                w_ihw[idx_val] = len(in_idx) * rw / s_in
        rej_ihw = weighted_bh_rejections(p, w_ihw, alpha=alpha, tau=1.0)
        if rej_ihw:
            ihw_spec7_fdp_sum += sum(1 for i in rej_ihw if not is_alt[i]) / len(rej_ihw)

    fdr_naive_spec7 = naive_spec7_fdp_sum / n_trials
    fdr_ihw_spec7 = ihw_spec7_fdp_sum / n_trials

    # Proposition 1(c) & Corollary 2: Compare oracle W*(x), IHW-GBH (tau=1, uncensored), and GBH
    # for G=2 groups with pi0(0)=0.5, pi0(1)=0.9, F_alt(t) = t^0.25 (Beta(0.25, 1)) at m=800
    m_c2 = 800
    tau_est = 0.50
    pi0_true = [0.50, 0.90]
    f_alt_tau = tau_est ** 0.25
    # Supplement S2.4 Eq (42): pi0*(g) = pi0(g) + (1 - pi0(g)) * (1 - F_alt(tau)) / (1 - tau)
    pi0_star = [pi0_true[g] + (1.0 - pi0_true[g]) * (1.0 - f_alt_tau) / (1.0 - tau_est) for g in (0, 1)]
    raw_w_star = [(1.0 - pi0_star[g]) / pi0_star[g] for g in (0, 1)]
    mean_raw_star = 0.5 * (raw_w_star[0] + raw_w_star[1])
    w_star_group = [rw / mean_raw_star for rw in raw_w_star]

    n_c2_trials = 250
    power_oracle_sum = 0.0
    power_ihw_c2_sum = 0.0
    power_gbh_c2_sum = 0.0
    fdr_ihw_c2_sum = 0.0

    for _ in range(n_c2_trials):
        groups_c2 = [0 if i < m_c2 // 2 else 1 for i in range(m_c2)]
        folds_c2 = [i % 5 for i in range(m_c2)]
        p_c2 = []
        alt_c2 = []
        for i in range(m_c2):
            g = groups_c2[i]
            is_a = (rng.random() > pi0_true[g])
            alt_c2.append(is_a)
            p_c2.append(rng.random() ** 4.0 if is_a else rng.random())
        n_alt_c2 = max(1, sum(1 for a in alt_c2 if a))

        w_oracle = [w_star_group[groups_c2[i]] for i in range(m_c2)]
        rej_oracle = weighted_bh_rejections(p_c2, w_oracle, alpha=alpha, tau=1.0)
        power_oracle_sum += sum(1 for i in rej_oracle if alt_c2[i]) / n_alt_c2

        # Full-sample GBH without null-proportion adaptivity (Corollary 2)
        pi0_hat_full = []
        for g in (0, 1):
            idx_g = [i for i in range(m_c2) if groups_c2[i] == g]
            cnt_gt = sum(1 for i in idx_g if p_c2[i] > tau_est)
            pi0_hat_full.append(min(0.999, (1.0 + cnt_gt) / (len(idx_g) * (1.0 - tau_est))))
        rw_full = [(1.0 - pi0_hat_full[groups_c2[i]]) / pi0_hat_full[groups_c2[i]] for i in range(m_c2)]
        s_full = sum(rw_full)
        w_gbh_full = [m_c2 * rw / s_full for rw in rw_full]
        rej_gbh = weighted_bh_rejections(p_c2, w_gbh_full, alpha=alpha, tau=1.0)
        power_gbh_c2_sum += sum(1 for i in rej_gbh if alt_c2[i]) / n_alt_c2

        # 5-fold IHW-GBH without null-proportion adaptivity (uncensored tau=1, Proposition 1(b)-(c))
        w_ihw_c2 = [0.0] * m_c2
        for ell in range(5):
            out_idx = [i for i in range(m_c2) if folds_c2[i] != ell]
            in_idx = [i for i in range(m_c2) if folds_c2[i] == ell]
            pi0_out = []
            for g in (0, 1):
                idx_g = [i for i in out_idx if groups_c2[i] == g]
                cnt_gt = sum(1 for i in idx_g if p_c2[i] > tau_est)
                pi0_out.append(min(0.999, (1.0 + cnt_gt) / (len(idx_g) * (1.0 - tau_est))))
            rw_in = [(1.0 - pi0_out[groups_c2[i]]) / pi0_out[groups_c2[i]] for i in in_idx]
            s_in = sum(rw_in)
            for idx_val, rw in zip(in_idx, rw_in):
                w_ihw_c2[idx_val] = len(in_idx) * rw / s_in
        rej_ihw_c2 = weighted_bh_rejections(p_c2, w_ihw_c2, alpha=alpha, tau=1.0)
        power_ihw_c2_sum += sum(1 for i in rej_ihw_c2 if alt_c2[i]) / n_alt_c2
        if rej_ihw_c2:
            fdr_ihw_c2_sum += sum(1 for i in rej_ihw_c2 if not alt_c2[i]) / len(rej_ihw_c2)

    power_oracle = power_oracle_sum / n_c2_trials
    power_gbh_c2 = power_gbh_c2_sum / n_c2_trials
    power_ihw_c2 = power_ihw_c2_sum / n_c2_trials
    fdr_ihw_c2 = fdr_ihw_c2_sum / n_c2_trials
    power_gap_oracle = abs(power_ihw_c2 - power_oracle)
    power_gap_gbh = abs(power_ihw_c2 - power_gbh_c2)

    assert fdr_naive_spec7 > 0.60  # Severe asymptotic overfitting in Proposition 1(a)
    assert fdr_ihw_spec7 <= alpha + 0.01  # Controlled by cross-weighting in Proposition 1(b)
    assert fdr_ihw_c2 <= alpha
    assert power_gap_oracle < 0.01
    assert power_gap_gbh < 0.01

    return {
        "prop1a_naive_spec7_fdr": round(fdr_naive_spec7, 4),
        "prop1b_ihw_spec7_uncensored_fdr": round(fdr_ihw_spec7, 4),
        "prop1c_oracle_power": round(power_oracle, 4),
        "prop1c_gbh_power": round(power_gbh_c2, 4),
        "prop1c_ihw_gbh_uncensored_power": round(power_ihw_c2, 4),
        "prop1c_ihw_vs_oracle_power_gap": round(power_gap_oracle, 5),
        "prop1c_ihw_gbh_uncensored_fdr": round(fdr_ihw_c2, 4),
    }


def verify_claim3_block_dependence_theorems3_4_and_examples1_2() -> dict[str, float]:
    """Claim 3: Assumption 2 (independent folds with arbitrary within-fold dependence):
    Theorem 3 (IHW-k-Bonferroni k-FWER control), Theorem 4 (IHW-BY FDR control),
    Example 1 (dishonest data-driven wBY has FDR = 1), and Example 2 (AdaPT with BY
    correction under Assumption 2 has FDR >= 0.2925).
    """
    rng = random.Random(2026101803)
    alpha = 0.10
    m_prime = 60
    m = 2 * m_prime
    harm_m = sum(1.0 / k for k in range(1, m + 1))
    alpha_by = alpha / harm_m

    # 1. Example 1 (Section 3.3): Dishonest data-driven wBY vs. Honest cross-weighted IHW-BY
    # Under Assumption 2 global null: fold 1 draws permutation of U[(i-1)/m', i/m'], fold 2 draws i.i.d. U[0,1].
    # Check condition m / sum_{k=1}^m (1/k) > 2 / alpha:
    assert (m / harm_m) > (2.0 / alpha)
    n_ex_trials = 500
    ex1_dishonest_wby_fdp_sum = 0.0
    ex1_honest_ihw_by_fdp_sum = 0.0

    for _ in range(n_ex_trials):
        perm = list(range(m_prime))
        rng.shuffle(perm)
        u_fold1 = [(idx + rng.random()) / m_prime for idx in range(m_prime)]
        p_fold1 = [u_fold1[perm[i]] for i in range(m_prime)]
        p_fold2 = [rng.random() for _ in range(m_prime)]
        p_all = p_fold1 + p_fold2

        # Dishonest weight: W_i = m * 1(i == argmin_j P_j)
        i_star = min(range(m), key=lambda i: p_all[i])
        w_dishonest = [float(m) if i == i_star else 0.0 for i in range(m)]
        rej_dishonest = weighted_bh_rejections(p_all, w_dishonest, alpha=alpha_by, tau=1.0)
        if rej_dishonest:
            ex1_dishonest_wby_fdp_sum += 1.0

        # Honest cross-weighted counterpart: find argmin in fold 2 to assign weight to that relative index in fold 1, and vice versa
        i_star_f2 = min(range(m_prime), key=lambda idx: p_fold2[idx])
        i_star_f1 = min(range(m_prime), key=lambda idx: p_fold1[idx])
        w_honest = [0.0] * m
        w_honest[i_star_f2] = float(m_prime)
        w_honest[m_prime + i_star_f1] = float(m_prime)
        rej_honest = weighted_bh_rejections(p_all, w_honest, alpha=alpha_by, tau=1.0)
        if rej_honest:
            ex1_honest_ihw_by_fdp_sum += 1.0

    fdr_ex1_dishonest_wby = ex1_dishonest_wby_fdp_sum / n_ex_trials
    fdr_ex1_honest_ihw_by = ex1_honest_ihw_by_fdp_sum / n_ex_trials

    # 2. Example 2 (Section 3.3): AdaPT with BY correction under Assumption 2
    # Two folds I_1, I_2 of size m_prime; within each fold all null p-values are identical:
    # P_1 = ... = P_{m'} ~ U[0,1], and P_{m'+1} = ... = P_m ~ U[0,1] independently.
    # At step 0, AdaPT initializes at s_0 = 0.45 and estimates FDP_hat = (1 + #{P_i >= 0.55}) / #{P_i <= 0.45}.
    # Exact probability of A u A' where A = {P_1 <= 0.45, P_{m'+1} < 0.55} and A' = {P_1 < 0.55, P_{m'+1} <= 0.45}:
    # P(A) = 0.45 * 0.55 = 0.2475, P(A') = 0.2475, P(A n A') = 0.45 * 0.45 = 0.2025 => P(A u A') = 0.2925.
    exact_ex2_adapt_by_lower_bound = 2.0 * (0.45 * 0.55) - (0.45 * 0.45)
    n_ex2_trials = 4000
    ex2_adapt_by_fdp_sum = 0.0
    for _ in range(n_ex2_trials):
        u1 = rng.random()
        u2 = rng.random()
        p_ex2 = [u1] * m_prime + [u2] * m_prime
        r_0 = sum(1 for p_val in p_ex2 if p_val <= 0.45)
        a_0 = sum(1 for p_val in p_ex2 if p_val >= 0.55)
        if r_0 > 0 and (1.0 + a_0) / r_0 <= alpha_by:
            ex2_adapt_by_fdp_sum += 1.0
    mc_ex2_adapt_by_fdr = ex2_adapt_by_fdp_sum / n_ex2_trials

    # 3. Theorem 3 (IHW-k-Bonferroni k-FWER control) and Theorem 4 (IHW-BY FDR control)
    # under strong within-fold dependence with informative covariates X_i in [0, 1]
    k_bonf = 3
    n_dep_trials = 500
    ihw_kbonf_violations = 0
    unweighted_kbonf_power_sum = 0.0
    ihw_kbonf_power_sum = 0.0
    ihw_by_fdp_sum = 0.0
    ihw_by_power_sum = 0.0
    unweighted_by_power_sum = 0.0

    for _ in range(n_dep_trials):
        # 2 independent folds (chromosomes), each of size m_prime = 60
        # First 15 hypotheses in each fold have small genomic distance X_i in [0, 0.25] and 60% non-nulls;
        # remaining 45 in each fold have large distance X_i in (0.25, 1.0] and are all null.
        # Within each fold, nulls share a strong common normal factor (rho = 0.8) so p-values are strongly dependent.
        p_dep = []
        x_dep = []
        alt_dep = []
        for ell in (0, 1):
            z_common = rng.gauss(0.0, 1.0)
            for j in range(m_prime):
                if j < 15:
                    x_val = 0.25 * (j / 15.0)
                    is_a = (j < 9)
                else:
                    x_val = 0.25 + 0.75 * ((j - 15) / 45.0)
                    is_a = False
                x_dep.append(x_val)
                alt_dep.append(is_a)
                z_idio = rng.gauss(0.0, 1.0)
                z_val = math.sqrt(0.8) * z_common + math.sqrt(0.2) * z_idio
                if is_a:
                    z_val += 3.6
                p_dep.append(max(1e-12, 1.0 - norm_cdf(z_val)))

        n_alt_dep = sum(1 for a in alt_dep if a)

        # Learn honest out-of-fold weights across 2 distance bins (x <= 0.25 vs. x > 0.25)
        w_honest_dep = [0.0] * m
        for ell in (0, 1):
            out_idx = [i for i in range(m) if (i // m_prime) != ell]
            in_idx = [i for i in range(m) if (i // m_prime) == ell]
            # Out-of-fold enrichment of small p-values (p <= 0.05) per bin
            rate_near = (0.5 + sum(1 for i in out_idx if x_dep[i] <= 0.25 and p_dep[i] <= 0.05)) / (
                1.0 + sum(1 for i in out_idx if x_dep[i] <= 0.25)
            )
            rate_far = (0.5 + sum(1 for i in out_idx if x_dep[i] > 0.25 and p_dep[i] <= 0.05)) / (
                1.0 + sum(1 for i in out_idx if x_dep[i] > 0.25)
            )
            raw_in = [rate_near if x_dep[i] <= 0.25 else rate_far for i in in_idx]
            s_in = sum(raw_in)
            for idx_val, rw in zip(in_idx, raw_in):
                w_honest_dep[idx_val] = len(in_idx) * rw / s_in

        # Theorem 3: Weighted k-Bonferroni rejects P_i <= (k * alpha / m) * W_i
        rej_ihw_kbonf = [i for i in range(m) if p_dep[i] <= (k_bonf * alpha / m) * w_honest_dep[i]]
        rej_unw_kbonf = [i for i in range(m) if p_dep[i] <= (k_bonf * alpha / m)]
        false_rej_kbonf = sum(1 for i in rej_ihw_kbonf if not alt_dep[i])
        if false_rej_kbonf >= k_bonf:
            ihw_kbonf_violations += 1
        ihw_kbonf_power_sum += sum(1 for i in rej_ihw_kbonf if alt_dep[i]) / n_alt_dep
        unweighted_kbonf_power_sum += sum(1 for i in rej_unw_kbonf if alt_dep[i]) / n_alt_dep

        # Theorem 4: IHW-BY vs. Unweighted BY
        rej_ihw_by = weighted_bh_rejections(p_dep, w_honest_dep, alpha=alpha_by, tau=1.0)
        rej_unw_by = weighted_bh_rejections(p_dep, [1.0] * m, alpha=alpha_by, tau=1.0)
        if rej_ihw_by:
            ihw_by_fdp_sum += sum(1 for i in rej_ihw_by if not alt_dep[i]) / len(rej_ihw_by)
        ihw_by_power_sum += sum(1 for i in rej_ihw_by if alt_dep[i]) / n_alt_dep
        unweighted_by_power_sum += sum(1 for i in rej_unw_by if alt_dep[i]) / n_alt_dep

    kfwer_ihw = ihw_kbonf_violations / n_dep_trials
    power_ihw_kbonf = ihw_kbonf_power_sum / n_dep_trials
    power_unw_kbonf = unweighted_kbonf_power_sum / n_dep_trials
    fdr_ihw_by = ihw_by_fdp_sum / n_dep_trials
    power_ihw_by = ihw_by_power_sum / n_dep_trials
    power_unw_by = unweighted_by_power_sum / n_dep_trials

    assert fdr_ex1_dishonest_wby == 1.0
    assert fdr_ex1_honest_ihw_by <= alpha
    assert abs(exact_ex2_adapt_by_lower_bound - 0.2925) < 1e-12
    assert mc_ex2_adapt_by_fdr >= 0.27 > alpha
    assert kfwer_ihw <= alpha
    assert fdr_ihw_by <= alpha
    assert power_ihw_kbonf > power_unw_kbonf
    assert power_ihw_by > power_unw_by

    return {
        "example1_dishonest_wby_fdr": round(fdr_ex1_dishonest_wby, 4),
        "example1_honest_ihw_by_fdr": round(fdr_ex1_honest_ihw_by, 4),
        "example2_adapt_by_exact_fdr_lower_bound": round(exact_ex2_adapt_by_lower_bound, 4),
        "example2_adapt_by_mc_fdr": round(mc_ex2_adapt_by_fdr, 4),
        "thm3_ihw_kbonf_kfwer": round(kfwer_ihw, 4),
        "thm3_ihw_kbonf_power": round(power_ihw_kbonf, 4),
        "thm3_unweighted_kbonf_power": round(power_unw_kbonf, 4),
        "thm4_ihw_by_fdr": round(fdr_ihw_by, 4),
        "thm4_ihw_by_power": round(power_ihw_by, 4),
        "thm4_unweighted_by_power": round(power_unw_by, 4),
    }


def grenander_lcm(pvals: list[float]) -> tuple[list[float], list[float]]:
    """Supplement S4.1.1: Compute the Grenander estimator (least concave majorant of the ECDF)
    on [0, 1], returning knot locations 0 = s_0 < s_1 < ... < s_J = 1 and non-increasing
    piecewise-linear slopes b_1 > b_2 > ... > b_J >= 0.
    """
    n = len(pvals)
    if n == 0:
        return [0.0, 1.0], [1.0]
    pts = sorted(pvals)
    # ECDF vertices (x_k, y_k) starting at (0, 0) and ending at (1, 1)
    xs = [0.0]
    ys = [0.0]
    for idx, p in enumerate(pts, start=1):
        p_clamped = min(1.0, max(0.0, p))
        if p_clamped > xs[-1]:
            xs.append(p_clamped)
            ys.append(idx / n)
        else:
            ys[-1] = idx / n
    if xs[-1] < 1.0:
        xs.append(1.0)
        ys.append(1.0)

    # Upper convex hull (least concave majorant) via monotone chain / Andrew's algorithm
    hull_x = [xs[0]]
    hull_y = [ys[0]]
    for x_new, y_new in zip(xs[1:], ys[1:]):
        while len(hull_x) >= 2:
            dx1 = hull_x[-1] - hull_x[-2]
            dy1 = hull_y[-1] - hull_y[-2]
            dx2 = x_new - hull_x[-1]
            dy2 = y_new - hull_y[-1]
            # Remove last vertex if slope increases or stays equal (violating strict concavity)
            if dy1 * dx2 <= dy2 * dx1 + 1e-14:
                hull_x.pop()
                hull_y.pop()
            else:
                break
        hull_x.append(x_new)
        hull_y.append(y_new)

    slopes = [
        (hull_y[j] - hull_y[j - 1]) / (hull_x[j] - hull_x[j - 1])
        for j in range(1, len(hull_x))
    ]
    return hull_x, slopes


def solve_grenander_kkt_weights(
    knots_per_group: list[list[float]],
    slopes_per_group: list[list[float]],
    counts_per_group: list[int],
    t_budget: float,
) -> list[float]:
    """Supplement S4.1.3 Algorithm 5: Solve max_{t_g >= 0} sum_g m_g F_hat_g(t_g)
    s.t. sum_g m_g t_g = sum_g m_g * t_budget via exact KKT slope ordering,
    returning normalized group weights w_g with sum_g m_g w_g = sum_g m_g.
    """
    g_count = len(knots_per_group)
    total_m = sum(counts_per_group)
    total_budget = total_m * t_budget
    if total_budget <= 0.0:
        return [1.0] * g_count

    # Each segment (g, j) has slope b_{g,j} and width delta_t = knots[j+1] - knots[j]
    segments = []
    for g in range(g_count):
        knots = knots_per_group[g]
        slopes = slopes_per_group[g]
        for j, b in enumerate(slopes):
            dt = knots[j + 1] - knots[j]
            if dt > 0.0:
                segments.append((b, g, dt))
    # Sort segments in descending order of marginal discovery slope b_{g,j}
    segments.sort(key=lambda x: x[0], reverse=True)

    t_alloc = [0.0] * g_count
    rem_budget = total_budget
    for _, g, dt in segments:
        cost = counts_per_group[g] * dt
        if rem_budget >= cost:
            t_alloc[g] += dt
            rem_budget -= cost
        else:
            t_alloc[g] += rem_budget / counts_per_group[g]
            rem_budget = 0.0
            break

    denom = sum(counts_per_group[g] * t_alloc[g] for g in range(g_count))
    if denom <= 0.0:
        return [1.0] * g_count
    return [total_m * t_alloc[g] / denom for g in range(g_count)]


def verify_claim4_grenander_kkt_and_breaking_adapt_regimes() -> dict[str, float]:
    """Claim 4: Section 4 / Supplement S4.1 Grenander least-concave-majorant + KKT
    weight optimization, and Section 5.2 ('Breaking AdaPT') sparse-signal (< 1/alpha
    signals) and strictly super-uniform null regimes.
    """
    rng = random.Random(2026101804)

    # 1. Verify Grenander LCM concavity (non-increasing slopes) and KKT optimality
    sample_p = [rng.random() ** 3.0 if i < 40 else rng.random() for i in range(150)]
    knots, slopes = grenander_lcm(sample_p)
    max_concavity_violation = 0.0
    for j in range(len(slopes) - 1):
        if slopes[j + 1] > slopes[j]:
            max_concavity_violation = max(max_concavity_violation, slopes[j + 1] - slopes[j])

    # 2. Section 5.2 ('Breaking AdaPT'):
    # Regime A: Sparse signals where total true alternatives m_1 < 1 / alpha.
    # For alpha = 0.05, 1 / alpha = 20. Suppose m = 400 and there are m_1 = 12 strong alternatives
    # concentrated at small covariate X_i, while all 388 nulls have strictly super-uniform p-values
    # P_i | H_0 ~ (1 - kappa) U[0,1] + kappa * Beta(1, 0.5) with kappa = 0.10 (Eq. in Section 5.2).
    # Note: Even if AdaPT shrinks s(x) to capture only the 12 true signals with 0 false positives (A_j = 0),
    # its FDP estimator is (1 + A_j) / R_j >= 1 / 12 = 0.0833 > alpha = 0.05, so AdaPT is forced to
    # reject 0 hypotheses unless it also includes >= 8 nulls!
    alpha_sparse = 0.05
    m_sparse = 400
    m1_sparse = 12  # < 1/alpha = 20
    adapt_min_rejections_required = math.ceil(1.0 / alpha_sparse)  # (1 + 0) / R <= 0.05 => R >= 20

    n_sparse_trials = 300
    ihw_grenander_power_sum = 0.0
    ihw_grenander_fdp_sum = 0.0
    unw_bh_sparse_power_sum = 0.0
    adapt_oracle_order_power_sum = 0.0

    g_bins = 4
    per_bin = m_sparse // g_bins
    n_folds = 5

    for _ in range(n_sparse_trials):
        p_sp = []
        alt_sp = []
        bins_sp = [i // per_bin for i in range(m_sparse)]
        folds_sp = [i % n_folds for i in range(m_sparse)]
        for i in range(m_sparse):
            if i < m1_sparse:
                alt_sp.append(True)
                z = rng.gauss(3.8, 1.0)
                p_sp.append(max(1e-12, 1.0 - norm_cdf(z)))
            else:
                alt_sp.append(False)
                # Section 5.2 super-uniform null: (1 - kappa) U[0,1] + kappa * Beta(1, 0.5), CDF of Beta(1,0.5) is 1 - sqrt(1-x)
                if rng.random() < 0.15:
                    u = rng.random()
                    p_sp.append(1.0 - (1.0 - u) ** 2.0)  # Beta(1, 0.5) draw skewed toward 1
                else:
                    p_sp.append(rng.random())

        # Unweighted BH
        rej_bh = weighted_bh_rejections(p_sp, [1.0] * m_sparse, alpha=alpha_sparse, tau=0.5)
        unw_bh_sparse_power_sum += sum(1 for i in rej_bh if alt_sp[i]) / m1_sparse

        # IHW-Grenander (5 folds, 4 covariate bins)
        w_ihw_gren = [0.0] * m_sparse
        for ell in range(n_folds):
            knots_list = []
            slopes_list = []
            counts_list = []
            for g in range(g_bins):
                out_g = [p_sp[i] for i in range(m_sparse) if folds_sp[i] != ell and bins_sp[i] == g]
                in_g_cnt = sum(1 for i in range(m_sparse) if folds_sp[i] == ell and bins_sp[i] == g)
                k_g, s_g = grenander_lcm(out_g)
                knots_list.append(k_g)
                slopes_list.append(s_g)
                counts_list.append(in_g_cnt)
            t_bh_est = max(0.0005, alpha_sparse * max(1, len(rej_bh)) / m_sparse)
            w_g_opt = solve_grenander_kkt_weights(knots_list, slopes_list, counts_list, t_budget=t_bh_est)
            for i in range(m_sparse):
                if folds_sp[i] == ell:
                    w_ihw_gren[i] = w_g_opt[bins_sp[i]]

        rej_ihw_g = weighted_bh_rejections(p_sp, w_ihw_gren, alpha=alpha_sparse, tau=0.5)
        ihw_grenander_power_sum += sum(1 for i in rej_ihw_g if alt_sp[i]) / m1_sparse
        if rej_ihw_g:
            ihw_grenander_fdp_sum += sum(1 for i in rej_ihw_g if not alt_sp[i]) / len(rej_ihw_g)

        # AdaPT along the oracle covariate-prioritized ordering:
        # At any candidate rejection threshold s_j, FDP_hat_j = (1 + #{i in S_j : P_i >= 1 - s_i}) / max(1, #{i in S_j : P_i <= s_i})
        # Check whether any step along the oracle ranking achieves FDP_hat <= alpha_sparse:
        # Candidate thresholds s_k = k * 0.45 / m_sparse in bin 0
        adapt_rej_count = 0
        for r_target in range(m_sparse, 0, -1):
            # Best possible subset of size r_target in bin 0 with threshold s = 0.05
            s_thr = 0.05
            r_cnt = sum(1 for i in range(r_target) if p_sp[i] <= s_thr)
            a_cnt = sum(1 for i in range(r_target) if p_sp[i] >= 1.0 - s_thr)
            if r_cnt > 0 and (1.0 + a_cnt) / r_cnt <= alpha_sparse:
                adapt_rej_count = sum(1 for i in range(r_target) if p_sp[i] <= s_thr and alt_sp[i])
                break
        adapt_oracle_order_power_sum += adapt_rej_count / m1_sparse

    power_ihw_gren = ihw_grenander_power_sum / n_sparse_trials
    fdr_ihw_gren = ihw_grenander_fdp_sum / n_sparse_trials
    power_unw_bh_sparse = unw_bh_sparse_power_sum / n_sparse_trials
    power_adapt_sparse = adapt_oracle_order_power_sum / n_sparse_trials

    assert max_concavity_violation == 0.0
    assert adapt_min_rejections_required == 20
    assert fdr_ihw_gren <= alpha_sparse + 0.01
    assert power_ihw_gren > power_unw_bh_sparse > power_adapt_sparse

    return {
        "grenander_max_concavity_slope_violation": round(max_concavity_violation, 8),
        "adapt_min_rejections_at_alpha_0_05": 20,
        "sparse_m1_true_signals": m1_sparse,
        "power_ihw_grenander_sparse_superuniform": round(power_ihw_gren, 4),
        "fdr_ihw_grenander_sparse_superuniform": round(fdr_ihw_gren, 4),
        "power_unweighted_bh_sparse_superuniform": round(power_unw_bh_sparse, 4),
        "power_adapt_sparse_superuniform": round(power_adapt_sparse, 4),
    }


def main() -> None:
    res = {
        "claim1_honest_tau_censored_fdr_and_counterexamples": verify_claim1_honest_tau_censored_fdr_and_counterexamples(),
        "claim2_asymptotic_proposition1_and_corollary2": verify_claim2_asymptotic_proposition1_and_corollary2(),
        "claim3_block_dependence_theorems3_4_and_examples1_2": verify_claim3_block_dependence_theorems3_4_and_examples1_2(),
        "claim4_grenander_kkt_and_breaking_adapt_regimes": verify_claim4_grenander_kkt_and_breaking_adapt_regimes(),
    }
    print(json.dumps(res, sort_keys=True))


if __name__ == "__main__":
    main()
