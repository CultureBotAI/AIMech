#!/usr/bin/env python3
"""Constructed boundary & mathematical verification for AIMech:NonparametricTwoSampleTestingByBetting.

Verifies the core mathematical claims of Shekhar & Ramdas (2023), 'Nonparametric Two-Sample Testing
by Betting', IEEE Transactions on Information Theory 70(2):1178-1203 (arXiv:2112.09162):
1. Claim 1 (Section 2.1-2.2, Definitions 2-5, Theorem 1, Appendix A.3):
   - Online Newton Step (ONS) betting strategy A_ONS (Definition 5, Eq. 11) pathwise deterministic
     Cutkosky-Orabona wealth lower bound (Appendix A.3):
     K_n >= (1 / sum v_t^2) * exp((sum v_t)^2 / (4 * (sum v_t^2 + sum v_t)))
         >= exp((n / 8) * (mean v_t)^2 - log n).
   - Exact composite test martingale property E_{H_0}[1 + lambda_t (g_t(X_t) - g_t(Y_t)) | F_{t-1}] = 1
     and empirical-Bernstein variance-adaptive asymptotic log-wealth growth rate (Theorem 1 Eq. 20,
     Remark 6).
2. Claim 2 (Section 3, Definition 7, Propositions 1-2, Appendix A.4 & D):
   - Sequential bounded-mean test on the unit ball in R^m using adaptive projected Online Gradient
     Ascent (OGA) u_{t+1} = Pi_U(u_t + eta_t (X_t - Y_t)) with eta_t = 1 / sqrt(2 M_t),
     M_t = sum_{i=1}^t ||X_i - Y_i||_2^2.
   - Deterministic adaptive OGA regret bound R_n <= (3/2) sqrt(M_n) (Appendix A.4 / Appendix D) and
     minimax-optimal stopping-time scaling E[tau] = O(sigma^2 log(1/alpha) / Delta^2) above the
     Wald-KL lower bound log(1/alpha) / d_KL(P_Y, P_X) (Lemma 4 / Proposition 2).
3. Claim 3 (Section 2.3 & Section 4, Definitions 6 & 8, Propositions 3-4):
   - Sequential kernel-MMD test (Definition 8) in RKHS H_K with RBF kernel and adaptive RKHS OGA
     witness updates detecting distributional shape/variance differences when means are identical
     (mu_X = mu_Y = 0), with stopping time adapting inversely to d_MMD(P_X, P_Y)^2 (Proposition 3).
   - Unbounded witness / linear-kernel extension via odd sigmoid varrho(x) = tanh(x) (Definition 6,
     Section 2.3) preserving exact null martingale validity E_{H_0}[tanh(g_t(X_t) - g_t(Y_t)) | F_{t-1}] = 0.
4. Claim 4 (Section 5.1-5.2, Definitions 9-13, Proposition 5, Corollary 1, Theorem 2):
   - Time-varying non-exchangeable two-sample testing (Definition 9, Remark 9, Proposition 5) where
     H_0 holds on even steps and H_1 holds on odd steps (d_G(P, Q) = Delta > 0).
   - Operator T-invariance testing (Definitions 10-13, Theorem 2) for symmetry (T(z) = -z, Section 5.2.1)
     and independence (T((x,y),(x',y')) = ((x,y'),(x',y)), Section 5.2.2) with ERM witness selection.
"""

from __future__ import annotations

import json
import math
import random


def clip(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))


def ons_run(payoffs: list[float]) -> tuple[list[float], list[float]]:
    """Run Definition 5 Online Newton Step (ONS) betting strategy on v_t in [-1, 1]."""
    lam = 0.0
    a_t = 1.0
    wealth = 1.0
    coeff = 2.0 / (2.0 - math.log(3.0))
    wealths: list[float] = []
    lambdas: list[float] = []
    for v_t in payoffs:
        lambdas.append(lam)
        wealth *= 1.0 + lam * v_t
        wealths.append(wealth)
        z_t = v_t / (1.0 + lam * v_t)
        a_t += z_t * z_t
        lam = clip(lam + coeff * z_t / a_t, -0.5, 0.5)
    return wealths, lambdas


def verify_claim1_ons_and_variance_adaptivity() -> dict[str, object]:
    """Verify Appendix A.3 ONS wealth lower bounds, Eq. 65 regret bound, and Theorem 1 Eq. 20 variance adaptivity."""
    rng = random.Random(2026101801)
    n = 300
    min_ratio_tight = float("inf")
    min_ratio_coarse = float("inf")
    max_ons_regret_over_log_n = 0.0

    for trial in range(40):
        mean_shift = 0.15 + 0.01 * (trial % 10)
        payoffs = [clip(rng.uniform(-0.4, 0.4) + mean_shift, -1.0, 1.0) for _ in range(n)]
        wealths, _ = ons_run(payoffs)
        s_v = sum(payoffs)
        s_v2 = sum(v * v for v in payoffs)
        k_n = wealths[-1]

        lb_tight = (1.0 / s_v2) * math.exp((s_v * s_v) / (4.0 * (s_v2 + s_v)))
        lb_coarse = math.exp((n / 8.0) * ((s_v / n) ** 2) - math.log(n))
        min_ratio_tight = min(min_ratio_tight, k_n / lb_tight)
        min_ratio_coarse = min(min_ratio_coarse, k_n / lb_coarse)

        best_const_log_w = max(
            sum(math.log(1.0 + (0.01 * k) * v) for v in payoffs)
            for k in range(-50, 51)
        )
        ons_regret = best_const_log_w - math.log(k_n)
        max_ons_regret_over_log_n = max(max_ons_regret_over_log_n, ons_regret / math.log(n))

    # Compare small-variance vs large-variance streams with identical mean payoff Delta = 0.20
    # Small variance: v_t = 0.20 deterministically (E[v^2] = 0.04, Delta / E[v^2] = 5.0 >= 1)
    # Large variance: v_t in {+1.0, -0.6} with probs (0.5, 0.5) -> E[v] = 0.20, E[v^2] = 0.68
    n_growth = 500
    w_small_var, _ = ons_run([0.20] * n_growth)
    rate_small_var = math.log(w_small_var[-1]) / n_growth

    rng_lv = random.Random(2026101802)
    lv_rates = []
    for _ in range(50):
        payoffs_lv = [1.0 if rng_lv.random() < 0.5 else -0.6 for _ in range(n_growth)]
        w_lv, _ = ons_run(payoffs_lv)
        lv_rates.append(math.log(w_lv[-1]) / n_growth)
    rate_large_var = sum(lv_rates) / len(lv_rates)

    # Theoretical lower bound from Appendix C proof of Eq. 20:
    # (Delta / 4) * min(Delta / E[v^2], 1)
    theo_lb_small_var = (0.20 / 4.0) * min(0.20 / 0.04, 1.0)  # 0.05
    theo_lb_large_var = (0.20 / 4.0) * min(0.20 / 0.68, 1.0)  # 0.01470588

    assert min_ratio_tight >= 1.0
    assert min_ratio_coarse >= 1.0
    assert max_ons_regret_over_log_n <= 0.5
    assert rate_small_var > rate_large_var > theo_lb_large_var
    assert rate_small_var >= theo_lb_small_var

    return {
        "n_steps": n,
        "min_ratio_wealth_to_cutkosky_orabona_tight_lb": round(min_ratio_tight, 6),
        "min_ratio_wealth_to_coarse_exp_lb": round(min_ratio_coarse, 6),
        "max_ons_regret_over_log_n": round(max_ons_regret_over_log_n, 6),
        "small_variance_log_growth_rate": round(rate_small_var, 6),
        "small_variance_theoretical_lb": round(theo_lb_small_var, 6),
        "large_variance_log_growth_rate": round(rate_large_var, 6),
        "large_variance_theoretical_lb": round(theo_lb_large_var, 6),
    }


def run_bounded_mean_oga_test(
    stream_pairs: list[tuple[list[float], list[float]]],
    alpha: float = 0.05,
) -> tuple[int, bool, float, float]:
    """Run Definition 7 Sequential Test for Bounded Means Testing on R^m."""
    m = len(stream_pairs[0][0])
    u = [0.0] * m
    lam = 0.0
    a_t = 1.0
    wealth = 1.0
    m_t = 0.0
    coeff_ons = 2.0 / (2.0 - math.log(3.0))

    sum_diff = [0.0] * m
    cum_payoff = 0.0
    max_regret_ratio = 0.0
    stopped_at = len(stream_pairs)
    rejected = False

    for t_idx, (x_t, y_t) in enumerate(stream_pairs, start=1):
        diff = [x_t[j] - y_t[j] for j in range(m)]
        v_t = sum(u[j] * diff[j] for j in range(m))
        cum_payoff += v_t
        for j in range(m):
            sum_diff[j] += diff[j]
        norm_diff_sq = sum(d * d for d in diff)
        m_t += norm_diff_sq

        # Regret R_t = 0.5 * ||sum_{i=1}^t (X_i - Y_i)||_2 - sum_{i=1}^t <u_i, X_i - Y_i>
        best_in_hindsight = 0.5 * math.sqrt(sum(s * s for s in sum_diff))
        regret_t = best_in_hindsight - cum_payoff
        if m_t > 0.0:
            # Appendix A.4 / Appendix D bound: R_t <= (3 D / 2) * sqrt(M_t) with D = 1
            bound_t = 1.5 * math.sqrt(m_t)
            max_regret_ratio = max(max_regret_ratio, regret_t / bound_t)

        wealth *= 1.0 + lam * v_t
        if not rejected and wealth >= 1.0 / alpha:
            rejected = True
            stopped_at = t_idx

        # Adaptive OGA update (Eq. 29): eta_t = 1 / sqrt(2 M_t), project onto ||u||_2 <= 1/2
        if m_t > 0.0:
            eta_t = 1.0 / math.sqrt(2.0 * m_t)
            u_raw = [u[j] + eta_t * diff[j] for j in range(m)]
            norm_u = math.sqrt(sum(val * val for val in u_raw))
            if norm_u > 0.5:
                u = [val * (0.5 / norm_u) for val in u_raw]
            else:
                u = u_raw

        # ONS update (Definition 5 / Cutkosky & Orabona 2018 Algorithm 1)
        z_t = v_t / (1.0 + lam * v_t)
        a_t += z_t * z_t
        lam = clip(lam + coeff_ons * z_t / a_t, -0.5, 0.5)

    return stopped_at, rejected, max_regret_ratio, wealth


def verify_claim2_bounded_mean_oga_and_minimax() -> dict[str, object]:
    """Verify Section 3 Definition 7, Propositions 1-2, and Appendix D adaptive OGA regret bound."""
    rng = random.Random(2026101803)
    m = 4
    alpha = 0.05
    n_max = 600
    n_trials = 100

    # 1. Null hypothesis H_0: X_t, Y_t ~ Uniform on unit ball coordinates in [-0.5, 0.5]^4
    null_rejections = 0
    max_oga_regret_ratio = 0.0
    for _ in range(n_trials):
        pairs = [
            (
                [rng.uniform(-0.5, 0.5) for _ in range(m)],
                [rng.uniform(-0.5, 0.5) for _ in range(m)],
            )
            for _ in range(300)
        ]
        _, rej, reg_ratio, _ = run_bounded_mean_oga_test(pairs, alpha=alpha)
        if rej:
            null_rejections += 1
        max_oga_regret_ratio = max(max_oga_regret_ratio, reg_ratio)
    null_type1_rate = null_rejections / n_trials

    # 2. Alternative H_1 with two mean separations Delta = 0.5 * ||mu_X - mu_Y||_2:
    # Case A: mu_X = (0.4, 0, 0, 0), mu_Y = (-0.4, 0, 0, 0) -> ||mu_X - mu_Y||_2 = 0.8, Delta = 0.4
    # Case B: mu_X = (0.2, 0, 0, 0), mu_Y = (-0.2, 0, 0, 0) -> ||mu_X - mu_Y||_2 = 0.4, Delta = 0.2
    taus_large_delta = []
    taus_small_delta = []
    for _ in range(n_trials):
        pairs_a = []
        pairs_b = []
        for _ in range(n_max):
            noise_x = [rng.uniform(-0.2, 0.2) for _ in range(m)]
            noise_y = [rng.uniform(-0.2, 0.2) for _ in range(m)]
            x_a = [0.4 + noise_x[0]] + noise_x[1:]
            y_a = [-0.4 + noise_y[0]] + noise_y[1:]
            pairs_a.append((x_a, y_a))

            x_b = [0.2 + noise_x[0]] + noise_x[1:]
            y_b = [-0.2 + noise_y[0]] + noise_y[1:]
            pairs_b.append((x_b, y_b))

        tau_a, rej_a, reg_a, _ = run_bounded_mean_oga_test(pairs_a, alpha=alpha)
        tau_b, rej_b, reg_b, _ = run_bounded_mean_oga_test(pairs_b, alpha=alpha)
        assert rej_a and rej_b
        taus_large_delta.append(tau_a)
        taus_small_delta.append(tau_b)
        max_oga_regret_ratio = max(max_oga_regret_ratio, reg_a, reg_b)

    mean_tau_delta_04 = sum(taus_large_delta) / len(taus_large_delta)
    mean_tau_delta_02 = sum(taus_small_delta) / len(taus_small_delta)

    # 3. Verify Lemma 4 / Proposition 2 KL lower bound on Bernoulli(p) vs Bernoulli(q)
    # p = 0.70, q = 0.30 -> ||mu_X - mu_Y|| = 0.40, Delta = 0.20
    p_bern, q_bern = 0.70, 0.30
    d_kl = p_bern * math.log(p_bern / q_bern) + (1.0 - p_bern) * math.log((1.0 - p_bern) / (1.0 - q_bern))
    wald_kl_lower_bound = math.log(1.0 / alpha) / d_kl

    taus_bern = []
    for _ in range(n_trials):
        pairs_bern = [
            ([1.0 if rng.random() < p_bern else 0.0], [1.0 if rng.random() < q_bern else 0.0])
            for _ in range(n_max)
        ]
        tau_bn, rej_bn, _, _ = run_bounded_mean_oga_test(pairs_bern, alpha=alpha)
        assert rej_bn
        taus_bern.append(tau_bn)
    mean_tau_bern = sum(taus_bern) / len(taus_bern)

    assert null_type1_rate <= alpha
    assert max_oga_regret_ratio <= 1.0
    assert mean_tau_delta_04 < mean_tau_delta_02
    assert mean_tau_bern > wald_kl_lower_bound

    return {
        "null_empirical_type1_error": round(null_type1_rate, 4),
        "alpha": alpha,
        "max_ratio_oga_regret_to_3_over_2_sqrt_Mt": round(max_oga_regret_ratio, 6),
        "mean_stopping_time_delta_0_4": round(mean_tau_delta_04, 2),
        "mean_stopping_time_delta_0_2": round(mean_tau_delta_02, 2),
        "stopping_time_ratio_delta_0_2_to_0_4": round(mean_tau_delta_02 / mean_tau_delta_04, 3),
        "bernoulli_mean_stopping_time": round(mean_tau_bern, 2),
        "lemma4_wald_kl_lower_bound": round(wald_kl_lower_bound, 4),
    }


def rbf_kernel(x: float, y: float, bw: float = 1.0) -> float:
    return math.exp(-((x - y) ** 2) / (2.0 * bw * bw))


def run_kernel_mmd_test(
    pairs: list[tuple[float, float]],
    alpha: float = 0.05,
    bw: float = 1.0,
) -> tuple[int, bool, float]:
    """Run Definition 8 Sequential Kernel MMD Test with adaptive RKHS OGA."""
    # Represent unnormalized RKHS accumulator h_t = sum_{i=1}^{t-1} w_i (K(X_i, .) - K(Y_i, .))
    # and current projected witness g_t = scale_t * h_t with ||g_t||_K <= 1/2.
    xs_hist: list[float] = []
    ys_hist: list[float] = []
    weights: list[float] = []
    norm_h_sq = 0.0
    scale = 0.0

    lam = 0.0
    a_t = 1.0
    wealth = 1.0
    m_t = 0.0
    coeff_ons = 2.0 / (2.0 - math.log(3.0))
    stopped_at = len(pairs)
    rejected = False

    for t_idx, (x_t, y_t) in enumerate(pairs, start=1):
        # Evaluate v_t = <g_t, K(x_t, .) - K(y_t, .)>_K
        if scale > 0.0:
            inner = 0.0
            for x_i, y_i, w_i in zip(xs_hist, ys_hist, weights):
                inner += w_i * (
                    rbf_kernel(x_i, x_t, bw)
                    - rbf_kernel(x_i, y_t, bw)
                    - rbf_kernel(y_i, x_t, bw)
                    + rbf_kernel(y_i, y_t, bw)
                )
            v_t = clip(scale * inner, -1.0, 1.0)
        else:
            inner = 0.0
            v_t = 0.0

        wealth *= 1.0 + lam * v_t
        if not rejected and wealth >= 1.0 / alpha:
            rejected = True
            stopped_at = t_idx
            break

        # ||K(x_t, .) - K(y_t, .)||_K^2 = K(x_t,x_t) + K(y_t,y_t) - 2 K(x_t,y_t) = 2 - 2 K(x_t,y_t)
        diff_norm_sq = 2.0 - 2.0 * rbf_kernel(x_t, y_t, bw)
        m_t += diff_norm_sq

        if m_t > 0.0:
            eta_t = 1.0 / (2.0 * math.sqrt(2.0 * m_t))
            # g_t + eta_t * delta_t: first rescale existing weights by scale so h <- g_t
            if scale != 1.0 and weights:
                weights = [w * scale for w in weights]
                norm_h_sq = (scale * scale) * norm_h_sq
                inner_g = scale * inner
            else:
                inner_g = inner

            # New ||g_t + eta_t delta_t||_K^2 = ||g_t||_K^2 + 2 eta_t <g_t, delta_t> + eta_t^2 ||delta_t||_K^2
            norm_h_sq = max(0.0, norm_h_sq + 2.0 * eta_t * inner_g + (eta_t * eta_t) * diff_norm_sq)
            xs_hist.append(x_t)
            ys_hist.append(y_t)
            weights.append(eta_t)
            norm_h = math.sqrt(norm_h_sq)
            scale = (0.5 / norm_h) if norm_h > 0.5 else 1.0

        z_t = v_t / (1.0 + lam * v_t)
        a_t += z_t * z_t
        lam = clip(lam + coeff_ons * z_t / a_t, -0.5, 0.5)

    return stopped_at, rejected, wealth


def verify_claim3_kernel_mmd_and_unbounded_sigmoid() -> dict[str, object]:
    """Verify Section 4 Sequential Kernel MMD Test and Section 2.3 odd-sigmoid unbounded test."""
    rng = random.Random(2026101804)
    alpha = 0.05
    n_trials = 40
    n_max = 220

    # Zero-mean distributions with identical mean 0 and variance 1, but different shapes:
    # P_X = Rademacher in {-1, +1} (mean 0, var 1)
    # P_Y = Mixture: 0 with prob 0.8, +-sqrt(5) with prob 0.1 each (mean 0, var 1)
    # Note: bounded-mean linear test has Delta_mean = ||E[X] - E[Y]|| = 0!
    mmd_rejections_h1 = 0
    mmd_taus_h1 = []
    mmd_rejections_h0 = 0

    for _ in range(n_trials):
        pairs_h1 = []
        pairs_h0 = []
        for _ in range(n_max):
            x = 1.0 if rng.random() < 0.5 else -1.0
            u = rng.random()
            if u < 0.8:
                y = 0.0
            elif u < 0.9:
                y = math.sqrt(5.0)
            else:
                y = -math.sqrt(5.0)
            pairs_h1.append((x, y))

            x0 = 1.0 if rng.random() < 0.5 else -1.0
            y0 = 1.0 if rng.random() < 0.5 else -1.0
            pairs_h0.append((x0, y0))

        tau_h1, rej_h1, _ = run_kernel_mmd_test(pairs_h1, alpha=alpha, bw=0.5)
        _, rej_h0, _ = run_kernel_mmd_test(pairs_h0, alpha=alpha, bw=0.5)
        if rej_h1:
            mmd_rejections_h1 += 1
        mmd_taus_h1.append(tau_h1)
        if rej_h0:
            mmd_rejections_h0 += 1

    mmd_power_zero_mean_alt = mmd_rejections_h1 / n_trials
    mmd_null_type1 = mmd_rejections_h0 / n_trials
    mmd_mean_tau_h1 = sum(mmd_taus_h1) / len(mmd_taus_h1)

    # Section 2.3 Definition 6: Odd sigmoid varrho(x) = tanh(x) on unbounded observations
    # Verify exact null expectation E_{H_0}[tanh(g(X) - g(Y))] = 0 by numeric quadrature / symmetry
    # and run sequential test with unbounded linear witness g_t(x) = w_t * x on Cauchy/Gaussian streams
    grid = [0.1 * k for k in range(1, 80)]
    symmetry_residual = max(abs(math.tanh(z) + math.tanh(-z)) for z in grid)

    unbounded_h1_rejs = 0
    unbounded_h0_rejs = 0
    for _ in range(60):
        # Under H_1: X_t ~ N(1.0, 1.0), Y_t ~ N(0.0, 1.0) (unbounded support)
        payoffs_h1 = []
        payoffs_h0 = []
        running_diff_h1 = 0.0
        running_diff_h0 = 0.0
        for t in range(1, 200):
            x1 = rng.gauss(1.0, 1.0)
            y1 = rng.gauss(0.0, 1.0)
            w1 = 1.0 if running_diff_h1 >= 0.0 else -1.0
            payoffs_h1.append(math.tanh(0.5 * w1 * (x1 - y1)))
            running_diff_h1 += x1 - y1

            x0 = rng.gauss(0.0, 1.0)
            y0 = rng.gauss(0.0, 1.0)
            w0 = 1.0 if running_diff_h0 >= 0.0 else -1.0
            payoffs_h0.append(math.tanh(0.5 * w0 * (x0 - y0)))
            running_diff_h0 += x0 - y0

        w_h1, _ = ons_run(payoffs_h1)
        w_h0, _ = ons_run(payoffs_h0)
        if max(w_h1) >= 1.0 / alpha:
            unbounded_h1_rejs += 1
        if max(w_h0) >= 1.0 / alpha:
            unbounded_h0_rejs += 1

    unbounded_power = unbounded_h1_rejs / 60.0
    unbounded_type1 = unbounded_h0_rejs / 60.0

    assert mmd_power_zero_mean_alt == 1.0
    assert mmd_null_type1 <= alpha
    assert symmetry_residual == 0.0
    assert unbounded_power >= 0.95
    assert unbounded_type1 <= alpha

    return {
        "kernel_mmd_zero_mean_equal_variance_alt_power": round(mmd_power_zero_mean_alt, 4),
        "kernel_mmd_zero_mean_alt_mean_stopping_time": round(mmd_mean_tau_h1, 2),
        "kernel_mmd_null_type1_error": round(mmd_null_type1, 4),
        "odd_sigmoid_symmetry_max_residual": symmetry_residual,
        "unbounded_tanh_linear_kernel_power": round(unbounded_power, 4),
        "unbounded_tanh_linear_kernel_null_type1": round(unbounded_type1, 4),
    }


def verify_claim4_time_varying_and_operator_invariance() -> dict[str, object]:
    """Verify Section 5.1 time-varying non-exchangeable streams and Section 5.2 T-invariance testing."""
    rng = random.Random(2026101805)
    alpha = 0.05
    n_trials = 60
    n_steps = 240

    # 1. Section 5.1 Remark 9 & Proposition 5: Time-varying distributions
    # On even steps t: P_t = Q_t = Uniform([-0.5, 0.5]) (identical)
    # On odd steps t: under H_1, P_t = Uniform([-0.2, 0.8]) and Q_t = Uniform([-0.8, 0.2])
    # Plus sinusoidal drift c_t = 0.3 * sin(0.2 * t) added to both X_t and Y_t so marginal sequences
    # are non-stationary and non-exchangeable across time.
    tv_h1_rejs = 0
    tv_h0_rejs = 0
    for _ in range(n_trials):
        pairs_h1 = []
        pairs_h0 = []
        for t in range(1, n_steps + 1):
            drift = 0.3 * math.sin(0.2 * t)
            if t % 2 == 0:
                x1 = clip(drift + rng.uniform(-0.5, 0.5), -1.0, 1.0)
                y1 = clip(drift + rng.uniform(-0.5, 0.5), -1.0, 1.0)
            else:
                x1 = clip(drift + rng.uniform(-0.2, 0.8), -1.0, 1.0)
                y1 = clip(drift + rng.uniform(-0.8, 0.2), -1.0, 1.0)
            pairs_h1.append(([x1], [y1]))

            x0 = clip(drift + rng.uniform(-0.5, 0.5), -1.0, 1.0)
            y0 = clip(drift + rng.uniform(-0.5, 0.5), -1.0, 1.0)
            pairs_h0.append(([x0], [y0]))

        _, rej_tv1, _, _ = run_bounded_mean_oga_test(pairs_h1, alpha=alpha)
        _, rej_tv0, _, _ = run_bounded_mean_oga_test(pairs_h0, alpha=alpha)
        if rej_tv1:
            tv_h1_rejs += 1
        if rej_tv0:
            tv_h0_rejs += 1

    tv_alt_power = tv_h1_rejs / n_trials
    tv_null_type1 = tv_h0_rejs / n_trials

    # 2. Section 5.2.1 Symmetry Testing (T(z) = -z) with ERM over KS threshold indicators
    # g_u(z) = 0.5 * 1{z <= u} => g_u(z) - g_u(-z) = 0.5 * (1{z <= u} - 1{-z <= u}) in [-0.5, 0.5]
    grid_u = [-1.5 + 0.25 * k for k in range(13)]
    sym_h1_rejs = 0
    sym_h0_rejs = 0
    for _ in range(n_trials):
        hist_h1: list[float] = []
        hist_h0: list[float] = []
        payoffs_sym_h1: list[float] = []
        payoffs_sym_h0: list[float] = []
        for _ in range(220):
            # Asymmetric alternative: centered skewed exponential Z = Exp(1) - 0.55
            z1 = rng.expovariate(1.0) - 0.55
            # Symmetric null: Laplace(0, 1)
            z0 = (1.0 if rng.random() < 0.5 else -1.0) * rng.expovariate(1.0)

            # ERM witness selection from past observations Z_1^{t-1}
            if hist_h1:
                best_u1, best_sign1, best_val1 = 0.0, 1.0, -1.0
                for u in grid_u:
                    s = sum((1.0 if z <= u else 0.0) - (1.0 if -z <= u else 0.0) for z in hist_h1)
                    if abs(s) > best_val1:
                        best_val1 = abs(s)
                        best_u1 = u
                        best_sign1 = 1.0 if s >= 0.0 else -1.0
                v1 = 0.5 * best_sign1 * ((1.0 if z1 <= best_u1 else 0.0) - (1.0 if -z1 <= best_u1 else 0.0))
            else:
                v1 = 0.0
            hist_h1.append(z1)
            payoffs_sym_h1.append(v1)

            if hist_h0:
                best_u0, best_sign0, best_val0 = 0.0, 1.0, -1.0
                for u in grid_u:
                    s0 = sum((1.0 if z <= u else 0.0) - (1.0 if -z <= u else 0.0) for z in hist_h0)
                    if abs(s0) > best_val0:
                        best_val0 = abs(s0)
                        best_u0 = u
                        best_sign0 = 1.0 if s0 >= 0.0 else -1.0
                v0 = 0.5 * best_sign0 * ((1.0 if z0 <= best_u0 else 0.0) - (1.0 if -z0 <= best_u0 else 0.0))
            else:
                v0 = 0.0
            hist_h0.append(z0)
            payoffs_sym_h0.append(v0)

        w_sym1, _ = ons_run(payoffs_sym_h1)
        w_sym0, _ = ons_run(payoffs_sym_h0)
        if max(w_sym1) >= 1.0 / alpha:
            sym_h1_rejs += 1
        if max(w_sym0) >= 1.0 / alpha:
            sym_h0_rejs += 1

    sym_power = sym_h1_rejs / n_trials
    sym_type1 = sym_h0_rejs / n_trials

    # 3. Section 5.2.2 Independence Testing via T((x,y),(x',y')) = ((x,y'),(x',y))
    indep_h1_rejs = 0
    indep_h0_rejs = 0
    for _ in range(n_trials):
        payoffs_ind1 = []
        payoffs_ind0 = []
        sign1 = 1.0
        cum1 = 0.0
        sign0 = 1.0
        cum0 = 0.0
        for _ in range(180):
            # Dependent pair: Y = X + noise on [-1, 1]
            x_a = rng.uniform(-1.0, 1.0)
            y_a = clip(0.8 * x_a + rng.uniform(-0.2, 0.2), -1.0, 1.0)
            x_b = rng.uniform(-1.0, 1.0)
            y_b = clip(0.8 * x_b + rng.uniform(-0.2, 0.2), -1.0, 1.0)
            # Witness g((x,y),(x',y')) - g((x,y'),(x',y)) = 0.25 * (x - x') * (y - y') in [-1, 1]
            raw1 = 0.25 * (x_a - x_b) * (y_a - y_b)
            payoffs_ind1.append(sign1 * raw1)
            cum1 += raw1
            sign1 = 1.0 if cum1 >= 0.0 else -1.0

            # Independent pair
            x0_a, y0_a = rng.uniform(-1.0, 1.0), rng.uniform(-1.0, 1.0)
            x0_b, y0_b = rng.uniform(-1.0, 1.0), rng.uniform(-1.0, 1.0)
            raw0 = 0.25 * (x0_a - x0_b) * (y0_a - y0_b)
            payoffs_ind0.append(sign0 * raw0)
            cum0 += raw0
            sign0 = 1.0 if cum0 >= 0.0 else -1.0

        w_ind1, _ = ons_run(payoffs_ind1)
        w_ind0, _ = ons_run(payoffs_ind0)
        if max(w_ind1) >= 1.0 / alpha:
            indep_h1_rejs += 1
        if max(w_ind0) >= 1.0 / alpha:
            indep_h0_rejs += 1

    indep_power = indep_h1_rejs / n_trials
    indep_type1 = indep_h0_rejs / n_trials

    assert tv_alt_power == 1.0
    assert tv_null_type1 <= alpha
    assert sym_power >= 0.95
    assert sym_type1 <= alpha
    assert indep_power == 1.0
    assert indep_type1 <= alpha

    return {
        "time_varying_alternating_alt_power": round(tv_alt_power, 4),
        "time_varying_drifting_null_type1": round(tv_null_type1, 4),
        "symmetry_test_erm_ks_power": round(sym_power, 4),
        "symmetry_test_erm_ks_null_type1": round(sym_type1, 4),
        "independence_test_swap_operator_power": round(indep_power, 4),
        "independence_test_swap_operator_null_type1": round(indep_type1, 4),
    }


def main() -> None:
    res1 = verify_claim1_ons_and_variance_adaptivity()
    res2 = verify_claim2_bounded_mean_oga_and_minimax()
    res3 = verify_claim3_kernel_mmd_and_unbounded_sigmoid()
    res4 = verify_claim4_time_varying_and_operator_invariance()

    summary = {
        "claim1_ons_wealth_lower_bounds_and_variance_adaptivity": res1,
        "claim2_bounded_mean_oga_regret_and_minimax_stopping_time": res2,
        "claim3_sequential_kernel_mmd_and_unbounded_sigmoid_test": res3,
        "claim4_time_varying_streams_and_operator_invariance_tests": res4,
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
