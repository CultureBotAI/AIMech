#!/usr/bin/env python3
"""Deterministic boundary verification for Round 833:
Adaptive Multiple Importance Sampling (AMIS)
(Cornuet, Marin, Mira, & Robert, 2012, Scandinavian Journal of Statistics 39(4):798-812,
DOI: 10.1111/j.1467-9469.2011.00756.x, arXiv:0907.1254v5).

Verifies:
1. Deterministic Multiple Mixture Unbiasedness & Variance Dominance (Equations 2-4):
   Under fixed proposals q_0, ..., q_T with sample sizes N_0, ..., N_T and N_total = sum_j N_j,
   the deterministic mixture denominator psi_T(y) = (1/N_total) sum_{j=0}^T N_j q_j(y) satisfies
   (1/N_total) sum_{l=0}^T N_l E_{q_l}[ (pi(Y)/psi_T(Y)) h(Y) ] == E_pi[h(Y)] to machine precision,
   and strictly reduces importance sampling estimator variance compared to unpooled IS weights.
2. Algorithm 1 Incremental Past-Weight Recycling Identity (delta_i^l Recursion) & O(T sum N_t) Complexity:
   Updating past unnormalized mixture denominators via delta_i^l <- delta_i^l + N_t q(y_i^l; theta^{t-1})
   and omega_i^l = pi(y_i^l) / [delta_i^l / sum_{j=0}^t N_j] matches full recomputation from scratch
   to machine precision (<1e-13) while requiring exactly (T+1) * sum_{t=0}^T N_t density evaluations.
3. Multivariate Student-t T_3(mu^t, Sigma^t) Proposal Moment-Matching Update (Equation 6) &
   Section 4 Logistic Scale Hierarchy sigma_0 * 2^eta Initialization via Effective Sample Size (ESS).
4. Section 5 Single-Particle (N_t=1) Adaptive Weight Dependence Bias vs. Lemma 1 Consistency as N_T -> inf,
   and Section 6 Haario Twisted Banana-Shaped Target Variance/MSE & ESS Improvement over unrecycled AIS.
"""

from __future__ import annotations

import math
import random


def norm_pdf(y: float, mu: float, sig: float) -> float:
    return math.exp(-0.5 * ((y - mu) / sig) ** 2) / (sig * math.sqrt(2.0 * math.pi))


def check_deterministic_mixture_unbiasedness() -> dict[str, float]:
    """Verify Eqs. 2-4 deterministic multiple mixture unbiasedness and variance dominance."""
    def target_pdf(y: float) -> float:
        return 0.4 * norm_pdf(y, -1.5, 0.7) + 0.6 * norm_pdf(y, 1.8, 0.9)

    mus = [-1.8, 0.2, 2.0]
    sigmas = [1.1, 1.5, 1.0]
    counts = [120, 180, 200]
    total_n = sum(counts)

    def prop_pdf(j: int, y: float) -> float:
        return norm_pdf(y, mus[j], sigmas[j])

    def dm_denom(y: float) -> float:
        return sum(counts[j] * prop_pdf(j, y) for j in range(len(counts))) / total_n

    def h_fn(y: float) -> float:
        return y * y - 0.5 * y

    # Midpoint quadrature over [-15, 15] with 6000 intervals
    a, b, n_grid = -15.0, 15.0, 6000
    dy = (b - a) / n_grid
    true_val = 0.0
    dm_val = 0.0
    for k in range(n_grid):
        yk = a + (k + 0.5) * dy
        py = target_pdf(yk)
        hy = h_fn(yk)
        true_val += py * hy * dy
        denom_y = dm_denom(yk)
        for l_idx, nl in enumerate(counts):
            ql_y = prop_pdf(l_idx, yk)
            dm_val += (nl / total_n) * ql_y * (py / denom_y) * hy * dy

    unbiased_err = abs(dm_val - true_val)
    assert unbiased_err < 1e-12, f"Deterministic mixture unbiasedness failed: {unbiased_err}"

    # Monte Carlo variance comparison: deterministic mixture vs separate unpooled IS
    rng = random.Random(20120907)
    n_trials = 300
    est_dm = []
    est_sep = []
    for _ in range(n_trials):
        acc_dm = 0.0
        acc_sep = 0.0
        for l_idx, nl in enumerate(counts):
            mu_l, sig_l = mus[l_idx], sigmas[l_idx]
            for _ in range(nl):
                y = rng.gauss(mu_l, sig_l)
                py = target_pdf(y)
                hy = h_fn(y)
                acc_dm += (py / dm_denom(y)) * hy
                acc_sep += (py / prop_pdf(l_idx, y)) * hy
        est_dm.append(acc_dm / total_n)
        est_sep.append(acc_sep / total_n)

    mean_dm = sum(est_dm) / n_trials
    mean_sep = sum(est_sep) / n_trials
    var_dm = sum((x - mean_dm) ** 2 for x in est_dm) / n_trials
    var_sep = sum((x - mean_sep) ** 2 for x in est_sep) / n_trials
    assert var_dm < var_sep, f"Expected deterministic mixture variance {var_dm} < separate IS {var_sep}"
    return {
        "unbiased_err": unbiased_err,
        "var_dm": var_dm,
        "var_sep": var_sep,
        "var_ratio": var_dm / var_sep,
    }


def inv2x2(cov: list[list[float]]) -> tuple[list[list[float]], float]:
    det = cov[0][0] * cov[1][1] - cov[0][1] * cov[1][0]
    assert det > 0.0, f"Non-positive determinant in 2x2 covariance: {det}"
    inv = [
        [cov[1][1] / det, -cov[0][1] / det],
        [-cov[1][0] / det, cov[0][0] / det],
    ]
    return inv, det


def chol2x2(cov: list[list[float]]) -> list[list[float]]:
    l00 = math.sqrt(cov[0][0])
    l10 = cov[1][0] / l00
    l11 = math.sqrt(cov[1][1] - l10 * l10)
    return [[l00, 0.0], [l10, l11]]


def mvt_t3_pdf_2d(y: tuple[float, float], mu: list[float], cov: list[list[float]], df: float = 3.0) -> float:
    """Evaluate 2D Student-t density T_df(mu, cov) at y (Eq. 6)."""
    inv_c, det_c = inv2x2(cov)
    d0 = y[0] - mu[0]
    d1 = y[1] - mu[1]
    quad = d0 * (inv_c[0][0] * d0 + inv_c[0][1] * d1) + d1 * (inv_c[1][0] * d0 + inv_c[1][1] * d1)
    log_norm = (
        math.lgamma(0.5 * (df + 2.0))
        - math.lgamma(0.5 * df)
        - math.log(df * math.pi)
        - 0.5 * math.log(det_c)
    )
    return math.exp(log_norm - 0.5 * (df + 2.0) * math.log(1.0 + quad / df))


def sample_mvt_t3_2d(
    rng: random.Random, mu: list[float], cov: list[list[float]], n: int, df: float = 3.0
) -> list[tuple[float, float]]:
    chol = chol2x2(cov)
    out: list[tuple[float, float]] = []
    for _ in range(n):
        z0 = rng.gauss(0.0, 1.0)
        z1 = rng.gauss(0.0, 1.0)
        x0 = chol[0][0] * z0
        x1 = chol[1][0] * z0 + chol[1][1] * z1
        chi2 = sum(rng.gauss(0.0, 1.0) ** 2 for _ in range(int(df)))
        scale = math.sqrt(df / chi2)
        out.append((mu[0] + x0 * scale, mu[1] + x1 * scale))
    return out


def check_algorithm1_delta_recycling_and_t3_moments() -> dict[str, float]:
    """Verify Algorithm 1 incremental delta_i^l recursion vs. full recomputation & T_3 moment updates."""
    rng = random.Random(3904798)
    target_mu = [1.2, -0.8]
    target_cov = [[1.4, 0.55], [0.55, 0.9]]
    inv_tc, det_tc = inv2x2(target_cov)

    def target_pdf(y: tuple[float, float]) -> float:
        d0 = y[0] - target_mu[0]
        d1 = y[1] - target_mu[1]
        quad = d0 * (inv_tc[0][0] * d0 + inv_tc[0][1] * d1) + d1 * (inv_tc[1][0] * d0 + inv_tc[1][1] * d1)
        return math.exp(-0.5 * (2.0 * math.log(2.0 * math.pi) + math.log(det_tc) + quad))

    counts = [70, 90, 110, 130, 160]
    t_max = len(counts) - 1

    mu_0 = [0.0, 0.0]
    cov_0 = [[2.5, 0.0], [0.0, 2.5]]

    samples_by_stage: list[list[tuple[float, float]]] = []
    deltas_by_stage: list[list[float]] = []
    pi_by_stage: list[list[float]] = []
    prop_params: list[tuple[list[float], list[list[float]]]] = [(list(mu_0), [list(r) for r in cov_0])]

    y0 = sample_mvt_t3_2d(rng, mu_0, cov_0, counts[0])
    pi0 = [target_pdf(pt) for pt in y0]
    delta0 = [counts[0] * mvt_t3_pdf_2d(pt, mu_0, cov_0) for pt in y0]
    omega0 = [pi0[i] / (delta0[i] / counts[0]) for i in range(counts[0])]

    samples_by_stage.append(y0)
    deltas_by_stage.append(delta0)
    pi_by_stage.append(pi0)

    def update_moments(
        all_samples: list[list[tuple[float, float]]], all_omegas: list[list[float]]
    ) -> tuple[list[float], list[list[float]]]:
        w_sum = sum(sum(w_stage) for w_stage in all_omegas)
        m0 = sum(
            all_omegas[l_i][i] * all_samples[l_i][i][0]
            for l_i in range(len(all_samples))
            for i in range(len(all_samples[l_i]))
        ) / w_sum
        m1 = sum(
            all_omegas[l_i][i] * all_samples[l_i][i][1]
            for l_i in range(len(all_samples))
            for i in range(len(all_samples[l_i]))
        ) / w_sum
        c00 = c01 = c11 = 0.0
        for l_i in range(len(all_samples)):
            for i, pt in enumerate(all_samples[l_i]):
                w = all_omegas[l_i][i]
                d0 = pt[0] - m0
                d1 = pt[1] - m1
                c00 += w * d0 * d0
                c01 += w * d0 * d1
                c11 += w * d1 * d1
        return [m0, m1], [[c00 / w_sum, c01 / w_sum], [c01 / w_sum, c11 / w_sum]]

    mu_hat, cov_hat = update_moments(samples_by_stage, [omega0])
    inc_eval_count = counts[0]
    max_delta_err = 0.0
    max_omega_err = 0.0

    for t in range(1, t_max + 1):
        prop_params.append((list(mu_hat), [list(r) for r in cov_hat]))
        nt = counts[t]
        yt = sample_mvt_t3_2d(rng, mu_hat, cov_hat, nt)
        pit = [target_pdf(pt) for pt in yt]

        # Step 2(b): compute delta_i^t for new samples
        deltat = [0.0] * nt
        for l_idx in range(t + 1):
            mu_l, cov_l = prop_params[l_idx]
            nl = counts[l_idx]
            for i in range(nt):
                deltat[i] += nl * mvt_t3_pdf_2d(yt[i], mu_l, cov_l)
            inc_eval_count += nt

        # Step 2(c): incrementally update past delta_i^l for l = 0..t-1
        mu_curr, cov_curr = prop_params[t]
        for l_idx in range(t):
            nl = counts[l_idx]
            for i in range(nl):
                deltas_by_stage[l_idx][i] += nt * mvt_t3_pdf_2d(samples_by_stage[l_idx][i], mu_curr, cov_curr)
            inc_eval_count += nl

        samples_by_stage.append(yt)
        deltas_by_stage.append(deltat)
        pi_by_stage.append(pit)

        cum_n = sum(counts[: t + 1])
        all_omegas: list[list[float]] = []
        for l_idx in range(t + 1):
            nl = counts[l_idx]
            omega_stage: list[float] = []
            for i in range(nl):
                scratch_d = sum(
                    counts[j_idx] * mvt_t3_pdf_2d(samples_by_stage[l_idx][i], prop_params[j_idx][0], prop_params[j_idx][1])
                    for j_idx in range(t + 1)
                )
                inc_d = deltas_by_stage[l_idx][i]
                max_delta_err = max(max_delta_err, abs(inc_d - scratch_d))
                w_inc = pi_by_stage[l_idx][i] / (inc_d / cum_n)
                w_scr = pi_by_stage[l_idx][i] / (scratch_d / cum_n)
                max_omega_err = max(max_omega_err, abs(w_inc - w_scr))
                omega_stage.append(w_inc)
            all_omegas.append(omega_stage)

        mu_hat, cov_hat = update_moments(samples_by_stage, all_omegas)
        _, det_c = inv2x2(cov_hat)
        assert det_c > 0.0

    expected_evals = (t_max + 1) * sum(counts)
    assert inc_eval_count == expected_evals, f"Expected {expected_evals} evals, got {inc_eval_count}"
    assert max_delta_err < 1e-13, f"Incremental delta mismatch: {max_delta_err}"
    assert max_omega_err < 1e-13, f"Incremental omega mismatch: {max_omega_err}"

    mu_err = math.hypot(mu_hat[0] - target_mu[0], mu_hat[1] - target_mu[1])
    assert mu_err < 0.18, f"Pooled T_3 mean error too high: {mu_err}"
    return {
        "max_delta_err": max_delta_err,
        "max_omega_err": max_omega_err,
        "inc_eval_count": float(inc_eval_count),
        "mu_err": mu_err,
    }


def check_ess_scale_hierarchy_initialization() -> dict[str, float]:
    """Verify Section 4 scale hierarchy sigma_0 * 2^eta selection via Effective Sample Size (ESS)."""
    rng = random.Random(201204)
    sigma_base = 16.0
    n0 = 400
    best_eta = 0
    best_ess = -1.0
    ess_at_zero = 0.0

    for eta in range(-5, 6):
        sig = sigma_base * (2.0 ** eta)
        log_ws = []
        for _ in range(n0):
            y = rng.gauss(0.0, sig)
            log_ws.append(-0.5 * y * y + 0.5 * (y / sig) ** 2 + math.log(sig))
        m_lw = max(log_ws)
        ws = [math.exp(lw - m_lw) for lw in log_ws]
        ess = (sum(ws) ** 2) / sum(w * w for w in ws)
        if eta == 0:
            ess_at_zero = ess
        if ess > best_ess:
            best_ess = ess
            best_eta = eta

    selected_sigma = sigma_base * (2.0 ** best_eta)
    assert abs(selected_sigma - 1.0) <= 1.0, f"Expected selected scale near 1.0, got {selected_sigma}"
    assert best_ess > 3.0 * ess_at_zero
    return {
        "selected_sigma": selected_sigma,
        "best_ess": best_ess,
        "ess_at_zero": ess_at_zero,
    }


def check_section5_single_particle_bias_and_lemma1_consistency() -> dict[str, float]:
    """Verify Section 5 N_t=1 finite-T downward variance bias vs. Lemma 1 consistency as N_T -> inf."""
    rng = random.Random(201205)
    n_runs = 80
    t_steps = 40
    n_final = 800
    var_single = []
    var_consistent = []

    for _ in range(n_runs):
        draws = []
        sigmas = [0.55]
        est_var = 0.55 ** 2
        for _ in range(t_steps):
            sig_curr = sigmas[-1]
            draws.append(rng.gauss(0.0, sig_curr))
            ws = []
            for y in draws:
                denom = sum(norm_pdf(y, 0.0, s_val) for s_val in sigmas) / len(sigmas)
                ws.append(norm_pdf(y, 0.0, 1.0) / denom)
            w_sum = sum(ws)
            est_var = sum(w * (y * y) for w, y in zip(ws, draws)) / w_sum
            sigmas.append(max(math.sqrt(est_var), 0.15))

        var_single.append(est_var)

        # Lemma 1 consistency (Marin et al. 2012): bounded-weight T_3 proposal with large N_T at final stage
        sig_last = max(sigmas[-1], 0.5)
        y_final = [
            sig_last * rng.gauss(0.0, 1.0) / math.sqrt(sum(rng.gauss(0.0, 1.0) ** 2 for _ in range(3)) / 3.0)
            for _ in range(n_final)
        ]

        def t3_1d_pdf(y_val: float, sc: float) -> float:
            u = y_val / sc
            return (2.0 / (math.pi * math.sqrt(3.0) * sc)) * ((1.0 + u * u / 3.0) ** (-2.0))

        y_all = draws + y_final
        total_n = t_steps + n_final
        base_sigs = sigmas[:-1]
        ws_all = []
        for y in y_all:
            denom = (
                sum(norm_pdf(y, 0.0, s_val) for s_val in base_sigs)
                + n_final * t3_1d_pdf(y, sig_last)
            ) / total_n
            ws_all.append(norm_pdf(y, 0.0, 1.0) / denom)
        w_all_sum = sum(ws_all)
        var_consistent.append(sum(w * (y * y) for w, y in zip(ws_all, y_all)) / w_all_sum)

    mse_single = sum((v - 1.0) ** 2 for v in var_single) / n_runs
    mse_consistent = sum((v - 1.0) ** 2 for v in var_consistent) / n_runs
    assert mse_consistent < 0.1 * mse_single, f"Expected consistent MSE {mse_consistent} < single-particle {mse_single}"
    return {
        "mse_single": mse_single,
        "mse_consistent": mse_consistent,
    }


def check_banana_target_amis_vs_ais() -> dict[str, float]:
    """Verify Section 6 Haario banana-shaped target: AMIS past-weight recycling outperforms unrecycled AIS."""
    rng = random.Random(201206)
    b_twist = 0.03
    s1_sq = 25.0
    s2_sq = 1.0

    def banana_pdf(y: tuple[float, float]) -> float:
        x1 = y[0]
        x2 = y[1] - b_twist * (x1 * x1 - s1_sq)
        log_p = (
            -0.5 * (x1 * x1 / s1_sq + x2 * x2 / s2_sq)
            - 0.5 * math.log(2.0 * math.pi * s1_sq)
            - 0.5 * math.log(2.0 * math.pi * s2_sq)
        )
        return math.exp(log_p)

    n_stages = 5
    n_per_stage = 100
    n_trials = 25

    mse_amis_list = []
    mse_ais_list = []
    ess_amis_list = []
    ess_ais_list = []

    for _ in range(n_trials):
        mu_amis = [1.5, 2.0]
        cov_amis = [[36.0, 0.0], [0.0, 9.0]]
        amis_samples: list[list[tuple[float, float]]] = []
        amis_deltas: list[list[float]] = []
        amis_pis: list[list[float]] = []
        amis_params: list[tuple[list[float], list[list[float]]]] = []

        mu_ais = [1.5, 2.0]
        cov_ais = [[36.0, 0.0], [0.0, 9.0]]
        ais_samples: list[tuple[float, float]] = []
        ais_weights: list[float] = []

        w_pool_flat: list[float] = []

        for t in range(n_stages):
            amis_params.append((list(mu_amis), [list(r) for r in cov_amis]))
            yt_amis = sample_mvt_t3_2d(rng, mu_amis, cov_amis, n_per_stage)
            pit_amis = [banana_pdf(pt) for pt in yt_amis]
            deltat = [0.0] * n_per_stage
            for l_idx in range(t + 1):
                ml, cl = amis_params[l_idx]
                for i in range(n_per_stage):
                    deltat[i] += n_per_stage * mvt_t3_pdf_2d(yt_amis[i], ml, cl)
            for l_idx in range(t):
                for i in range(n_per_stage):
                    amis_deltas[l_idx][i] += n_per_stage * mvt_t3_pdf_2d(amis_samples[l_idx][i], mu_amis, cov_amis)
            amis_samples.append(yt_amis)
            amis_deltas.append(deltat)
            amis_pis.append(pit_amis)

            cum_n = (t + 1) * n_per_stage
            w_pool_flat = []
            y_pool_flat: list[tuple[float, float]] = []
            for l_idx in range(t + 1):
                for i in range(n_per_stage):
                    w_pool_flat.append(amis_pis[l_idx][i] / (amis_deltas[l_idx][i] / cum_n))
                    y_pool_flat.append(amis_samples[l_idx][i])

            w_sum = sum(w_pool_flat)
            mu_amis = [
                sum(w * pt[0] for w, pt in zip(w_pool_flat, y_pool_flat)) / w_sum,
                sum(w * pt[1] for w, pt in zip(w_pool_flat, y_pool_flat)) / w_sum,
            ]
            c00 = sum(w * (pt[0] - mu_amis[0]) ** 2 for w, pt in zip(w_pool_flat, y_pool_flat)) / w_sum + 1e-2
            c01 = sum(w * (pt[0] - mu_amis[0]) * (pt[1] - mu_amis[1]) for w, pt in zip(w_pool_flat, y_pool_flat)) / w_sum
            c11 = sum(w * (pt[1] - mu_amis[1]) ** 2 for w, pt in zip(w_pool_flat, y_pool_flat)) / w_sum + 1e-2
            cov_amis = [[c00, c01], [c01, c11]]

            # Standard AIS stage t without past-weight denominator recycling
            yt_ais = sample_mvt_t3_2d(rng, mu_ais, cov_ais, n_per_stage)
            wt_ais = [banana_pdf(pt) / mvt_t3_pdf_2d(pt, mu_ais, cov_ais) for pt in yt_ais]
            ais_samples.extend(yt_ais)
            ais_weights.extend(wt_ais)
            ws_stage = sum(wt_ais)
            mu_ais = [
                sum(w * pt[0] for w, pt in zip(wt_ais, yt_ais)) / ws_stage,
                sum(w * pt[1] for w, pt in zip(wt_ais, yt_ais)) / ws_stage,
            ]
            ac00 = sum(w * (pt[0] - mu_ais[0]) ** 2 for w, pt in zip(wt_ais, yt_ais)) / ws_stage + 1e-2
            ac01 = sum(w * (pt[0] - mu_ais[0]) * (pt[1] - mu_ais[1]) for w, pt in zip(wt_ais, yt_ais)) / ws_stage
            ac11 = sum(w * (pt[1] - mu_ais[1]) ** 2 for w, pt in zip(wt_ais, yt_ais)) / ws_stage + 1e-2
            cov_ais = [[ac00, ac01], [ac01, ac11]]

        w_ais_sum = sum(ais_weights)
        est_ais_0 = sum(w * pt[0] for w, pt in zip(ais_weights, ais_samples)) / w_ais_sum
        est_ais_1 = sum(w * pt[1] for w, pt in zip(ais_weights, ais_samples)) / w_ais_sum

        mse_amis_list.append(mu_amis[0] ** 2 + mu_amis[1] ** 2)
        mse_ais_list.append(est_ais_0 ** 2 + est_ais_1 ** 2)
        ess_amis_list.append((sum(w_pool_flat) ** 2) / sum(w * w for w in w_pool_flat))
        ess_ais_list.append((w_ais_sum ** 2) / sum(w * w for w in ais_weights))

    mean_mse_amis = sum(mse_amis_list) / n_trials
    mean_mse_ais = sum(mse_ais_list) / n_trials
    mean_ess_amis = sum(ess_amis_list) / n_trials
    mean_ess_ais = sum(ess_ais_list) / n_trials
    assert mean_ess_amis > mean_ess_ais, f"Expected AMIS ESS {mean_ess_amis} > AIS ESS {mean_ess_ais}"
    assert mean_mse_amis < mean_mse_ais, f"Expected AMIS MSE {mean_mse_amis} < AIS MSE {mean_mse_ais}"
    return {
        "mean_mse_amis": mean_mse_amis,
        "mean_mse_ais": mean_mse_ais,
        "mean_ess_amis": mean_ess_amis,
        "mean_ess_ais": mean_ess_ais,
    }


def main() -> None:
    r1 = check_deterministic_mixture_unbiasedness()
    r2 = check_algorithm1_delta_recycling_and_t3_moments()
    r3 = check_ess_scale_hierarchy_initialization()
    r4 = check_section5_single_particle_bias_and_lemma1_consistency()
    r5 = check_banana_target_amis_vs_ais()
    print(
        "[PASS] Round 833 AMIS boundary verification passed: "
        f"dm_unbiased_err={r1['unbiased_err']:.2e}, dm_var_ratio={r1['var_ratio']:.4f}, "
        f"delta_rec_err={r2['max_delta_err']:.2e}, omega_rec_err={r2['max_omega_err']:.2e}, "
        f"eval_count={int(r2['inc_eval_count'])}, ess_init={r3['best_ess']:.1f} (sigma={r3['selected_sigma']:.2f}), "
        f"lemma1_mse={r4['mse_consistent']:.4f}<{r4['mse_single']:.4f}, "
        f"banana_ess={r5['mean_ess_amis']:.1f}>{r5['mean_ess_ais']:.1f}, "
        f"banana_mse={r5['mean_mse_amis']:.4f}<{r5['mean_mse_ais']:.4f}"
    )


if __name__ == "__main__":
    main()
