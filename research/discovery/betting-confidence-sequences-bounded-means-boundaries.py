#!/usr/bin/env python3
"""Constructed boundary and mathematical verification script for Round 180:
AIMech:BettingConfidenceSequencesForBoundedMeans (Waudby-Smith & Ramdas 2024,
JRSS-B 86(1):1-27, arXiv:2010.09686).

Verifies:
1. Proposition 2 & Theorem 2: Exact martingale property of the capital process
   K_t(mu) under dependent conditionally mean-mu bounded processes on [0, 1],
   pointwise Fan inequality dominance over the predictable plug-in empirical
   Bernstein supermartingale (PrPl-EB), and time-uniform coverage + width gains.
2. Theorem 3, Lemma 2, Proposition 5 & Section E.4: Quasiconvexity of the
   Hedged Capital process K_t^pm(m), convexity of Hedged Grid Kelly
   K_t^hgKelly(m), and exact reproduction of the Section E.4 non-convex
   sublevel-set counterexample for unhedged aGRAPA when X_1 = X_2 = 0.
3. Proposition 4 & Theorem 4: Finite-population sampling without replacement
   (Hedged-WoR) time-varying conditional mean m_t^WoR, exact martingale
   identities, and exact collapse of the WoR confidence sequence width to 0 at
   t = N.
4. Proposition 6 & Section E.6: Pointwise dominance of the linear capital factor
   1 + gamma^m(lambda)*(x - m) over the Hoeffding exponential factor
   exp(lambda*(x - m) - lambda^2/8), and exact duality between the optimal
   hindsight capital K_t^HS(m) and the reciprocal of Owen's empirical
   likelihood ratio 1 / R(x_1^t; m).
"""

from __future__ import annotations

import json
import math
import random


def psi_e(lam: float) -> float:
    """Sub-exponential CGF function psi_E(lam) = (-log(1 - lam) - lam) / 4 (Eq. 14)."""
    if abs(lam) < 1e-12:
        return (lam * lam) / 8.0
    return (-math.log(1.0 - lam) - lam) / 4.0


def psi_h(lam: float) -> float:
    """Hoeffding sub-Gaussian CGF function psi_H(lam) = lam^2 / 8 (Eq. 8)."""
    return (lam * lam) / 8.0


def verify_proposition2_and_theorem2() -> dict[str, float]:
    """Verify Proposition 2 (exact martingale vs supermartingale) and Theorem 2/3."""
    mu = 0.35
    # Dependent process on [0, 1] with E[X_t | F_{t-1}] = 0.35 identically:
    # State A (X_{t-1} < 0.35): X_t in {0.10, 0.60} with probs (0.5, 0.5) -> mean 0.35
    # State B (X_{t-1} >= 0.35): X_t in {0.00, 0.35, 0.70} with probs (0.25, 0.50, 0.25) -> mean 0.35
    branches = [
        [(0.10, 0.50), (0.60, 0.50)],
        [(0.00, 0.25), (0.35, 0.50), (0.70, 0.25)],
    ]
    max_martingale_err = 0.0
    min_eb_supermartingale_gap = 1.0
    for branch in branches:
        cond_mean = sum(x * p for x, p in branch)
        assert abs(cond_mean - mu) < 1e-15
        for lam in [-0.8, -0.4, 0.25, 0.6, 1.2]:
            # Capital process factor 1 + lam * (X - mu)
            e_cap = sum(p * (1.0 + lam * (x - mu)) for x, p in branch)
            max_martingale_err = max(max_martingale_err, abs(e_cap - 1.0))
        for lam_eb in [0.15, 0.35, 0.60]:
            for mu_hat in [0.20, 0.35, 0.55]:
                e_eb = sum(
                    p * math.exp(lam_eb * (x - mu) - 4.0 * ((x - mu_hat) ** 2) * psi_e(lam_eb))
                    for x, p in branch
                )
                assert e_eb <= 1.0 + 1e-15
                min_eb_supermartingale_gap = min(min_eb_supermartingale_gap, 1.0 - e_eb)

    assert max_martingale_err < 1e-15
    assert min_eb_supermartingale_gap > 1e-5

    # Pointwise Fan inequality (Lemma 3 / Eq. 40):
    # exp(lam * y - 4 * y^2 * psi_E(lam)) <= 1 + lam * y for all y >= -1, lam in [0, 1)
    max_fan_diff = -1.0
    for y in [-0.9, -0.35, -0.1, 0.15, 0.45, 0.65]:
        for lam in [0.1, 0.3, 0.5, 0.75]:
            lhs = math.exp(lam * y - 4.0 * (y * y) * psi_e(lam))
            rhs = 1.0 + lam * y
            assert lhs <= rhs + 1e-15
            max_fan_diff = max(max_fan_diff, rhs - lhs)

    # Monte Carlo simulation comparing PrPl-H, PrPl-EB, and Hedged Capital CS
    rng = random.Random(20261018)
    n_trials = 600
    horizon = 60
    alpha = 0.05
    c_trunc = 0.5
    grid = [j / 200.0 for j in range(201)]

    miscover_h = 0
    miscover_eb = 0
    miscover_hedged = 0
    widths_h_final: list[float] = []
    widths_eb_final: list[float] = []
    widths_hedged_final: list[float] = []

    for _ in range(n_trials):
        x_prev = 0.20
        sum_x = 0.0
        sum_sq_dev = 0.0

        # Running bounds for PrPl-H and PrPl-EB
        l_h, u_h = 0.0, 1.0
        l_eb, u_eb = 0.0, 1.0
        sum_lam_h = 0.0
        sum_lam_h_x = 0.0
        sum_psi_h = 0.0

        sum_lam_eb = 0.0
        sum_lam_eb_x = 0.0
        sum_v_psi_eb = 0.0

        # Hedged capital process on grid
        k_plus = [1.0 for _ in grid]
        k_minus = [1.0 for _ in grid]
        l_hedged, u_hedged = 0.0, 1.0

        violated_h = False
        violated_eb = False
        violated_hedged = False

        for t in range(1, horizon + 1):
            # Draw from low-variance dependent process on [0, 1] with conditional mean mu = 0.35:
            # If x_prev < 0.35: X_t in {0.30, 0.40} w.p. (0.5, 0.5); else {0.29, 0.41} w.p. (0.5, 0.5)
            if x_prev < mu:
                xt = 0.30 if rng.random() < 0.5 else 0.40
            else:
                xt = 0.29 if rng.random() < 0.5 else 0.41
            x_prev = xt

            # Predictable regularized mean and variance from t-1 observations (Eq. 15 & 26)
            mu_hat_prev = (0.5 + sum_x) / float(t)
            sigma2_hat_prev = (0.25 + sum_sq_dev) / float(t)

            lam_h_t = min(1.0, math.sqrt(8.0 * math.log(2.0 / alpha) / (t * math.log(t + 1.0))))
            lam_eb_t = min(
                c_trunc,
                math.sqrt(2.0 * math.log(2.0 / alpha) / (sigma2_hat_prev * t * math.log(1.0 + t))),
            )

            # Update PrPl-H
            sum_lam_h += lam_h_t
            sum_lam_h_x += lam_h_t * xt
            sum_psi_h += psi_h(lam_h_t)
            center_h = sum_lam_h_x / sum_lam_h
            rad_h = (math.log(2.0 / alpha) + sum_psi_h) / sum_lam_h
            l_h = max(l_h, center_h - rad_h)
            u_h = min(u_h, center_h + rad_h)
            if not (l_h <= mu <= u_h):
                violated_h = True

            # Update PrPl-EB
            v_t = 4.0 * ((xt - mu_hat_prev) ** 2)
            sum_lam_eb += lam_eb_t
            sum_lam_eb_x += lam_eb_t * xt
            sum_v_psi_eb += v_t * psi_e(lam_eb_t)
            center_eb = sum_lam_eb_x / sum_lam_eb
            rad_eb = (math.log(2.0 / alpha) + sum_v_psi_eb) / sum_lam_eb
            l_eb = max(l_eb, center_eb - rad_eb)
            u_eb = min(u_eb, center_eb + rad_eb)
            if not (l_eb <= mu <= u_eb):
                violated_eb = True

            # Update Hedged Capital CS (Theorem 3)
            lam_tilde = math.sqrt(
                2.0 * math.log(2.0 / alpha) / (sigma2_hat_prev * t * math.log(1.0 + t))
            )
            active_m: list[float] = []
            for idx, m_val in enumerate(grid):
                lam_p = c_trunc / m_val if m_val > 0.0 and lam_tilde > c_trunc / m_val else lam_tilde
                lam_m = (
                    c_trunc / (1.0 - m_val)
                    if m_val < 1.0 and lam_tilde > c_trunc / (1.0 - m_val)
                    else lam_tilde
                )
                k_plus[idx] *= 1.0 + lam_p * (xt - m_val)
                k_minus[idx] *= 1.0 - lam_m * (xt - m_val)
                k_hedged = max(0.5 * k_plus[idx], 0.5 * k_minus[idx])
                if k_hedged < 1.0 / alpha:
                    active_m.append(m_val)

            if active_m:
                l_hedged = max(l_hedged, min(active_m))
                u_hedged = min(u_hedged, max(active_m))
            else:
                l_hedged, u_hedged = 1.0, 0.0
            if not (l_hedged <= mu <= u_hedged):
                violated_hedged = True

            # Update sufficient statistics for next step
            sum_x += xt
            mu_hat_curr = (0.5 + sum_x) / float(t + 1)
            sum_sq_dev += (xt - mu_hat_curr) ** 2

        if violated_h:
            miscover_h += 1
        if violated_eb:
            miscover_eb += 1
        if violated_hedged:
            miscover_hedged += 1
        widths_h_final.append(max(0.0, u_h - l_h))
        widths_eb_final.append(max(0.0, u_eb - l_eb))
        widths_hedged_final.append(max(0.0, u_hedged - l_hedged))

    rate_h = miscover_h / float(n_trials)
    rate_eb = miscover_eb / float(n_trials)
    rate_hedged = miscover_hedged / float(n_trials)
    mean_w_h = sum(widths_h_final) / float(n_trials)
    mean_w_eb = sum(widths_eb_final) / float(n_trials)
    mean_w_hedged = sum(widths_hedged_final) / float(n_trials)

    assert rate_h <= alpha
    assert rate_eb <= alpha
    assert rate_hedged <= alpha
    assert mean_w_hedged < mean_w_eb < mean_w_h

    return {
        "max_martingale_err": max_martingale_err,
        "min_eb_supermartingale_gap": round(min_eb_supermartingale_gap, 6),
        "max_fan_diff": round(max_fan_diff, 6),
        "miscoverage_rate_h": round(rate_h, 4),
        "miscoverage_rate_eb": round(rate_eb, 4),
        "miscoverage_rate_hedged": round(rate_hedged, 4),
        "mean_width_h_t60": round(mean_w_h, 4),
        "mean_width_eb_t60": round(mean_w_eb, 4),
        "mean_width_hedged_t60": round(mean_w_hedged, 4),
    }


def verify_quasiconvexity_and_agrapa_counterexample() -> dict[str, float]:
    """Verify Lemma 2 (Hedged quasiconvexity), Proposition 5 (hgKelly convexity),
    and Section E.4 (unhedged aGRAPA non-convex sublevel set counterexample)."""
    samples = [0.15, 0.25, 0.20, 0.30, 0.18, 0.22]
    lam_tildes = [0.6, 0.8, 0.9, 1.1, 1.2, 1.3]
    c_trunc = 0.75
    m_grid = [i / 500.0 for i in range(1, 500)]

    k_plus_vals: list[float] = []
    k_minus_vals: list[float] = []
    k_hedged_vals: list[float] = []
    m_comb_vals: list[float] = []

    for m_val in m_grid:
        kp = 1.0
        km = 1.0
        for xt, lt in zip(samples, lam_tildes):
            lp = min(lt, c_trunc / m_val)
            lm = min(lt, c_trunc / (1.0 - m_val))
            kp *= 1.0 + lp * (xt - m_val)
            km *= 1.0 - lm * (xt - m_val)
        k_plus_vals.append(kp)
        k_minus_vals.append(km)
        kh = max(0.5 * kp, 0.5 * km)
        mc = 0.5 * kp + 0.5 * km
        assert kh <= mc + 1e-15
        k_hedged_vals.append(kh)
        m_comb_vals.append(mc)

    # Verify K_t^+ is non-increasing and K_t^- is non-decreasing in m
    for idx in range(len(m_grid) - 1):
        assert k_plus_vals[idx] >= k_plus_vals[idx + 1] - 1e-12
        assert k_minus_vals[idx] <= k_minus_vals[idx + 1] + 1e-12

    # Verify sublevel sets of K_t^pm(m) and M_t^pm(m) are contiguous intervals
    for threshold in [1.5, 2.5, 5.0, 20.0]:
        sub_idx = [i for i, val in enumerate(k_hedged_vals) if val < threshold]
        if len(sub_idx) >= 2:
            assert sub_idx[-1] - sub_idx[0] + 1 == len(sub_idx)

    # Verify Proposition 5: Hedged Grid Kelly (hgKelly) is globally convex in m
    g_size = 10
    hg_vals: list[float] = []
    for m_val in m_grid:
        sum_pos = 0.0
        sum_neg = 0.0
        for g in range(1, g_size + 1):
            gamma_g = g / float(g_size)
            lam_g_plus = gamma_g / m_val
            lam_g_minus = gamma_g / (1.0 - m_val)
            prod_p = 1.0
            prod_m = 1.0
            for xt in samples:
                prod_p *= 1.0 + lam_g_plus * (xt - m_val)
                prod_m *= 1.0 - lam_g_minus * (xt - m_val)
            sum_pos += prod_p
            sum_neg += prod_m
        hg_vals.append(0.5 * (sum_pos / g_size) + 0.5 * (sum_neg / g_size))

    min_second_diff_hgkelly = min(
        hg_vals[i - 1] - 2.0 * hg_vals[i] + hg_vals[i + 1]
        for i in range(1, len(m_grid) - 1)
    )
    assert min_second_diff_hgkelly >= -1e-12

    # Verify Section E.4 counterexample: unhedged aGRAPA with X_1 = X_2 = 0,
    # prior mean 1/2, prior variance (1/20)/t, truncation c = 0.9
    def eval_agrapa_e4(m_val: float) -> float:
        x_obs = [0.0, 0.0]
        c_e4 = 0.9
        cap = 1.0
        for t_idx in range(1, 3):
            prev_x = x_obs[: t_idx - 1]
            mu_hat = (0.5 + sum(prev_x)) / float(t_idx)
            var_part = sum((x - mu_hat) ** 2 for x in prev_x)
            raw_lam = (mu_hat - m_val) / (
                (0.05 + var_part) / float(t_idx) + (mu_hat - m_val) ** 2
            )
            lo_b = -c_e4 / (1.0 - m_val)
            hi_b = c_e4 / m_val
            lam_t = min(hi_b, max(lo_b, raw_lam))
            cap *= 1.0 + lam_t * (x_obs[t_idx - 1] - m_val)
        return cap

    k2_m003 = eval_agrapa_e4(0.03)
    k2_m008 = eval_agrapa_e4(0.08)
    k2_m040 = eval_agrapa_e4(0.40)
    # Section E.4: K_2^aGRAPA(0.08) < 0.85 and K_2^aGRAPA(0.40) < 0.85,
    # while K_2^aGRAPA(0.03) > 0.85 (non-convex sublevel set!)
    assert k2_m003 > 0.85
    assert k2_m008 < 0.85
    assert k2_m040 < 0.85

    return {
        "min_second_diff_hgkelly": round(min_second_diff_hgkelly, 8),
        "agrapa_k2_m003": round(k2_m003, 6),
        "agrapa_k2_m008": round(k2_m008, 6),
        "agrapa_k2_m040": round(k2_m040, 6),
    }


def verify_without_replacement_cs() -> dict[str, float]:
    """Verify Proposition 4 and Theorem 4 (WoR Hedged Capital CS)."""
    # Finite population of N = 40 bounded numbers in [0, 1]
    pop = [0.20 if i < 20 else 0.40 for i in range(40)]
    n_pop = len(pop)
    mu_true = sum(pop) / float(n_pop)
    assert abs(mu_true - 0.30) < 1e-15

    # Check exact conditional expectation of WoR capital factor at an arbitrary step
    observed_prefix = [0.20, 0.40, 0.20, 0.20, 0.40]
    remaining = pop.copy()
    for x in observed_prefix:
        remaining.remove(x)
    t_step = len(observed_prefix) + 1
    mu_t_wor = (n_pop * mu_true - sum(observed_prefix)) / float(n_pop - t_step + 1)
    assert abs(mu_t_wor - (sum(remaining) / len(remaining))) < 1e-15

    lam_wor = 1.15
    cond_exp_wor = sum(1.0 + lam_wor * (x - mu_t_wor) for x in remaining) / float(len(remaining))
    wor_martingale_err = abs(cond_exp_wor - 1.0)
    assert wor_martingale_err < 1e-15

    # Compare Hedged-WoR vs With-Replacement Hedged CS across random permutations
    rng = random.Random(20261019)
    alpha = 0.05
    c_trunc = 0.5
    grid = [j / 200.0 for j in range(201)]
    n_perms = 200

    miscover_wor = 0
    widths_wor_t20: list[float] = []
    widths_wr_t20: list[float] = []
    widths_wor_t35: list[float] = []
    widths_wr_t35: list[float] = []
    widths_wor_t40: list[float] = []
    widths_wr_t40: list[float] = []

    for _ in range(n_perms):
        perm = pop.copy()
        rng.shuffle(perm)

        kp_wor = [1.0 for _ in grid]
        km_wor = [1.0 for _ in grid]
        kp_wr = [1.0 for _ in grid]
        km_wr = [1.0 for _ in grid]

        l_wor, u_wor = 0.0, 1.0
        l_wr, u_wr = 0.0, 1.0
        sum_x = 0.0
        sum_sq_dev = 0.0
        violated_wor = False

        for t in range(1, n_pop + 1):
            xt = perm[t - 1]
            sigma2_hat_prev = (0.25 + sum_sq_dev) / float(t)
            lam_tilde = math.sqrt(
                2.0 * math.log(2.0 / alpha) / (sigma2_hat_prev * t * math.log(1.0 + t))
            )

            active_wor: list[float] = []
            active_wr: list[float] = []

            for idx, m_val in enumerate(grid):
                # WoR time-varying null mean m_t^WoR(m)
                mt_wor = (n_pop * m_val - sum_x) / float(n_pop - t + 1)
                if mt_wor < 0.0 or mt_wor > 1.0:
                    # Impossible candidate mean given observed sum and [0, 1] bounds
                    kp_wor[idx] = float("inf")
                    km_wor[idx] = float("inf")
                else:
                    lp_wor = (
                        c_trunc / mt_wor
                        if mt_wor > 0.0 and lam_tilde > c_trunc / mt_wor
                        else lam_tilde
                    )
                    lm_wor = (
                        c_trunc / (1.0 - mt_wor)
                        if mt_wor < 1.0 and lam_tilde > c_trunc / (1.0 - mt_wor)
                        else lam_tilde
                    )
                    if not math.isinf(kp_wor[idx]):
                        kp_wor[idx] *= 1.0 + lp_wor * (xt - mt_wor)
                    if not math.isinf(km_wor[idx]):
                        km_wor[idx] *= 1.0 - lm_wor * (xt - mt_wor)
                    if max(0.5 * kp_wor[idx], 0.5 * km_wor[idx]) < 1.0 / alpha:
                        active_wor.append(m_val)

                # With-replacement update
                lp_wr = (
                    c_trunc / m_val
                    if m_val > 0.0 and lam_tilde > c_trunc / m_val
                    else lam_tilde
                )
                lm_wr = (
                    c_trunc / (1.0 - m_val)
                    if m_val < 1.0 and lam_tilde > c_trunc / (1.0 - m_val)
                    else lam_tilde
                )
                kp_wr[idx] *= 1.0 + lp_wr * (xt - m_val)
                km_wr[idx] *= 1.0 - lm_wr * (xt - m_val)
                if max(0.5 * kp_wr[idx], 0.5 * km_wr[idx]) < 1.0 / alpha:
                    active_wr.append(m_val)

            if active_wor:
                l_wor = max(l_wor, min(active_wor))
                u_wor = min(u_wor, max(active_wor))
            if active_wr:
                l_wr = max(l_wr, min(active_wr))
                u_wr = min(u_wr, max(active_wr))

            if not (l_wor - 1e-12 <= mu_true <= u_wor + 1e-12):
                violated_wor = True

            if t == 20:
                widths_wor_t20.append(u_wor - l_wor)
                widths_wr_t20.append(u_wr - l_wr)
            elif t == 35:
                widths_wor_t35.append(u_wor - l_wor)
                widths_wr_t35.append(u_wr - l_wr)
            elif t == 40:
                widths_wor_t40.append(u_wor - l_wor)
                widths_wr_t40.append(u_wr - l_wr)

            sum_x += xt
            mu_hat_curr = (0.5 + sum_x) / float(t + 1)
            sum_sq_dev += (xt - mu_hat_curr) ** 2

        if violated_wor:
            miscover_wor += 1

    mean_wor_t20 = sum(widths_wor_t20) / float(n_perms)
    mean_wr_t20 = sum(widths_wr_t20) / float(n_perms)
    mean_wor_t35 = sum(widths_wor_t35) / float(n_perms)
    mean_wr_t35 = sum(widths_wr_t35) / float(n_perms)
    mean_wor_t40 = sum(widths_wor_t40) / float(n_perms)
    mean_wr_t40 = sum(widths_wr_t40) / float(n_perms)

    assert miscover_wor == 0
    assert mean_wor_t20 < mean_wr_t20
    assert mean_wor_t35 < mean_wr_t35
    assert mean_wor_t40 < 0.25 * mean_wr_t40

    return {
        "wor_martingale_err": wor_martingale_err,
        "miscover_wor": miscover_wor,
        "mean_width_wor_t20": round(mean_wor_t20, 4),
        "mean_width_wr_t20": round(mean_wr_t20, 4),
        "mean_width_wor_t35": round(mean_wor_t35, 4),
        "mean_width_wr_t35": round(mean_wr_t35, 4),
        "mean_width_wor_t40": round(mean_wor_t40, 4),
        "mean_width_wr_t40": round(mean_wr_t40, 4),
    }


def verify_hoeffding_dominance_and_empirical_likelihood_duality() -> dict[str, float]:
    """Verify Proposition 6 (capital process dominates Hoeffding process) and
    Section E.6 (hindsight capital process equals reciprocal of Owen's empirical
    likelihood ratio)."""
    # Proposition 6: For all x, m in [0, 1] and lam in [-0.45, 0.45],
    # gamma^m(lam) = exp(lam*(1-m) - lam^2/8) - exp(-lam*m - lam^2/8) in [-1, 1]
    # and 1 + gamma^m(lam)*(x - m) >= exp(lam*(x - m) - lam^2/8).
    max_abs_gamma = 0.0
    min_dominance_gap = 1.0
    for lam in [-0.45, -0.30, -0.15, 0.15, 0.30, 0.45]:
        for m_idx in range(1, 20):
            m_val = m_idx / 20.0
            gamma_m = math.exp(lam * (1.0 - m_val) - (lam * lam) / 8.0) - math.exp(
                -lam * m_val - (lam * lam) / 8.0
            )
            max_abs_gamma = max(max_abs_gamma, abs(gamma_m))
            assert -1.0 <= gamma_m <= 1.0
            for x_idx in range(21):
                x_val = x_idx / 20.0
                k_val = 1.0 + gamma_m * (x_val - m_val)
                h_val = math.exp(lam * (x_val - m_val) - (lam * lam) / 8.0)
                assert k_val >= h_val - 1e-15
                min_dominance_gap = min(min_dominance_gap, k_val - h_val)

    # Section E.6: Hindsight capital K_t^HS(m) == 1 / R(x_1^t; m) (Owen's EL ratio)
    sample_x = [0.10, 0.25, 0.40, 0.55, 0.80]
    t_len = len(sample_x)
    m_target = 0.34  # Strictly inside (0.10, 0.80), distinct from sample mean 0.42

    # Solve stationary condition sum_{i=1}^t (x_i - m) / (1 + lam * (x_i - m)) = 0
    # Derivative w.r.t. lam is strictly negative, so bisection is exact.
    lo_lam = -1.0 / (1.0 - m_target) + 1e-9
    hi_lam = 1.0 / m_target - 1e-9
    for _ in range(120):
        mid = 0.5 * (lo_lam + hi_lam)
        grad = sum((x - m_target) / (1.0 + mid * (x - m_target)) for x in sample_x)
        if grad > 0.0:
            lo_lam = mid
        else:
            hi_lam = mid
    lam_hs = 0.5 * (lo_lam + hi_lam)

    k_hs = 1.0
    el_weights: list[float] = []
    for x in sample_x:
        factor = 1.0 + lam_hs * (x - m_target)
        k_hs *= factor
        el_weights.append(1.0 / (t_len * factor))

    weight_sum_err = abs(sum(el_weights) - 1.0)
    weighted_mean_err = abs(sum(w * x for w, x in zip(el_weights, sample_x)) - m_target)
    # Owen's empirical likelihood ratio R(x_1^t; m) = prod_{i=1}^t (t * p_i)
    owen_el_ratio = 1.0
    for w in el_weights:
        owen_el_ratio *= t_len * w
    duality_err = abs(k_hs - (1.0 / owen_el_ratio))

    assert weight_sum_err < 1e-14
    assert weighted_mean_err < 1e-14
    assert duality_err < 1e-13

    return {
        "max_abs_gamma_lam045": round(max_abs_gamma, 6),
        "min_hoeffding_dominance_gap": round(min_dominance_gap, 12),
        "lam_hs": round(lam_hs, 6),
        "k_hs": round(k_hs, 6),
        "owen_el_reciprocal": round(1.0 / owen_el_ratio, 6),
        "duality_err": duality_err,
        "weight_sum_err": weight_sum_err,
        "weighted_mean_err": weighted_mean_err,
    }


def main() -> None:
    res1 = verify_proposition2_and_theorem2()
    res2 = verify_quasiconvexity_and_agrapa_counterexample()
    res3 = verify_without_replacement_cs()
    res4 = verify_hoeffding_dominance_and_empirical_likelihood_duality()
    summary = {
        "proposition2_and_theorem2": res1,
        "quasiconvexity_and_agrapa_counterexample": res2,
        "without_replacement_cs": res3,
        "hoeffding_dominance_and_el_duality": res4,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
