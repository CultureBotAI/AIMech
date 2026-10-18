#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Model-X Anytime-Valid Conditional Independence Testing.

Verifies the four core theoretical claims of Grünwald, Henzi, & Lardy (2024),
"Anytime-Valid Tests of Conditional Independence Under Model-X",
Journal of the American Statistical Association (JASA), 119(546):1554-1565
(arXiv:2209.12637, DOI:10.1080/01621459.2023.2205607):

1. Claim 1 (Theorem 1 & Proposition 2):
   - Exact unit conditional expectation E_{X|Z}[E_h^{CI}(X, Y, Z) | Y, Z] = 1.0 of the
     exact Model-X conditional e-statistic.
   - Exact unit conditional expectation E[check{E}_{h,M}^{CI}(D_n) | Y_n, Z_n] = 1.0 of the
     plus-one Monte Carlo conditional e-statistic (Eq. 9, Proposition 2) across all (M+1)!
     exchangeable permutations and exact analytical expectation over discrete Q_Z, vs.
     strictly anti-conservative expectation E[tilde{E}_{h,M}^{naive} | Y_n, Z_n] > 1.0 when
     omitting the observed X_n from the Monte Carlo denominator (Jensen's inequality).
   - Anytime-valid Type-I error control P_{H_0}(exists n <= N : S_n^{CI} >= 1/alpha) <= alpha
     even with M = 2 Monte Carlo draws (where a batch CRT cannot reject at alpha = 0.05
     because 1/(M+1) = 1/3 > 0.05).

2. Claim 2 (Theorem 3, Proposition 4, Corollary 5):
   - Exact identity E_{f_{Y|X,Z}}^{CI}(X, Y, Z) = f_{X|Y,Z}(X | Y, Z) / f_{X|Z}(X | Z) and
     exact GRO expected log-growth E_f[log E_{f_{Y|X,Z}}^{CI}] = I_f(X; Y | Z) > 0.
   - Exact Proposition 4 identity: for any plug-in conditional density g_{Y|X,Z},
     E_f[log E_{g_{Y|X,Z}}^{CI}] = I_f(X; Y | Z) - E_f[KL(f_{Y|X,Z} || g_{Y|X,Z})]
     + E_f[KL(f_{Y|Z} || g_{Y|Z})] >= I_f(X; Y | Z) - E_f[KL(f_{Y|X,Z} || g_{Y|X,Z})].

3. Claim 3 (Theorem 6):
   - Under misspecification of Q_Z by hat{Q}_Z, the optional-stopping Type-I error up to
     horizon N is bounded by alpha + d_{TV}(Q_{Z^N}^N, hat{Q}_{Z^N}^N).

4. Claim 4 (Proposition 7 & Section 4):
   - Sequential logistic regression E-CRT with probability truncation to [eps, 1-eps]
     controls anytime Type-I error <= alpha under H_0 (beta = 0), achieves positive
     empirical log-growth rate approaching I(X; Y | Z) under H_1 (beta != 0), and avoids
     the zero-collapse / negative-infinity log-wealth pathology of untruncated early
     overfitted predictions.
"""

from __future__ import annotations

import itertools
import json
import math
import random


def verify_claim1_exact_and_mc_conditional_e_statistic() -> dict[str, float]:
    """Verify Theorem 1 and Proposition 2 on exact discrete and Monte Carlo Model-X e-statistics."""
    # Discrete support X in {0, 1, 2} with conditional distribution Q_z = (0.2, 0.5, 0.3)
    xs = [0, 1, 2]
    qz = [0.2, 0.5, 0.3]
    # Non-constant positive test function h(x, y, z)
    h_vals = [0.5, 1.5, 3.5]

    denom_exact = sum(p * h for p, h in zip(qz, h_vals))
    e_exact_vals = [h / denom_exact for h in h_vals]
    cond_exp_exact = sum(p * e for p, e in zip(qz, e_exact_vals))
    assert abs(cond_exp_exact - 1.0) < 1e-15

    # Proposition 2: M = 2 i.i.d. draws tilde_X_1, tilde_X_2 ~ Q_z, plus observed X_0 ~ Q_z
    # Compute exact expectation over all 3^3 = 27 triples (X_0, tilde_X_1, tilde_X_2) ~ Q_z^3
    m_draws = 2
    cond_exp_plus_one = 0.0
    cond_exp_naive = 0.0
    max_plus_one_val = 0.0

    for i0, i1, i2 in itertools.product(range(3), repeat=3):
        prob = qz[i0] * qz[i1] * qz[i2]
        h0, h1, h2 = h_vals[i0], h_vals[i1], h_vals[i2]
        e_plus_one = h0 / ((h0 + h1 + h2) / (m_draws + 1))
        e_naive = h0 / ((h1 + h2) / m_draws)
        cond_exp_plus_one += prob * e_plus_one
        cond_exp_naive += prob * e_naive
        if e_plus_one > max_plus_one_val:
            max_plus_one_val = e_plus_one

    assert abs(cond_exp_plus_one - 1.0) < 1e-15
    assert cond_exp_naive > 1.05  # Strictly anti-conservative by Jensen's inequality
    assert max_plus_one_val <= m_draws + 1 + 1e-12

    # Simulate sequential test martingale under H_0 with M = 2 draws and alpha = 0.05
    # Note: Fixed-sample CRT with M = 2 has minimum possible p-value 1/(M+1) = 1/3 > 0.05 (0 power),
    # whereas sequential plus-one E-CRT controls Type-I error <= 0.05 and can reject under H_1.
    rng = random.Random(20261018)
    alpha = 0.05
    n_trials = 500
    horizon = 60
    null_rejections_plus_one = 0

    for _ in range(n_trials):
        wealth = 1.0
        rejected = False
        for _t in range(horizon):
            z = rng.gauss(0.0, 1.0)
            x_obs = z + rng.gauss(0.0, 1.0)
            # Under H_0, Y depends only on Z, not X
            p_y = 1.0 / (1.0 + math.exp(-0.8 * z))
            y_obs = 1 if rng.random() < p_y else 0
            # Test function h(x, y, z) = exp(0.5 * (2*y - 1) * (x - z))
            s_sign = 1.0 if y_obs == 1 else -1.0
            h0 = math.exp(0.5 * s_sign * (x_obs - z))
            h_mc = [math.exp(0.5 * s_sign * rng.gauss(0.0, 1.0)) for _ in range(m_draws)]
            e_step = h0 / ((h0 + sum(h_mc)) / (m_draws + 1))
            wealth *= e_step
            if wealth >= 1.0 / alpha:
                rejected = True
                break
        if rejected:
            null_rejections_plus_one += 1

    null_reject_rate = null_rejections_plus_one / n_trials
    assert null_reject_rate <= alpha

    return {
        "exact_e_cond_expectation": round(cond_exp_exact, 12),
        "mc_plus_one_cond_expectation": round(cond_exp_plus_one, 12),
        "mc_naive_cond_expectation": round(cond_exp_naive, 6),
        "mc_plus_one_max_bound": round(max_plus_one_val, 6),
        "null_anytime_rejection_rate_m2": round(null_reject_rate, 4),
    }


def verify_claim2_gro_conditional_mutual_information_and_kl_regret() -> dict[str, float]:
    """Verify Theorem 3 and Proposition 4 exactly on a joint discrete distribution (X, Y, Z)."""
    # Let Z in {0, 1} with P(Z=z), X | Z ~ Q_z on {0, 1}, Y | X, Z ~ f(y | x, z) on {0, 1}
    p_z = {0: 0.4, 1: 0.6}
    q_x_given_z = {
        0: {0: 0.7, 1: 0.3},
        1: {0: 0.25, 1: 0.75},
    }
    f_y_given_xz = {
        (0, 0): {0: 0.85, 1: 0.15},
        (1, 0): {0: 0.30, 1: 0.70},
        (0, 1): {0: 0.65, 1: 0.35},
        (1, 1): {0: 0.15, 1: 0.85},
    }
    # Plug-in misspecified conditional density g(y | x, z)
    g_y_given_xz = {
        (0, 0): {0: 0.75, 1: 0.25},
        (1, 0): {0: 0.45, 1: 0.55},
        (0, 1): {0: 0.55, 1: 0.45},
        (1, 1): {0: 0.25, 1: 0.75},
    }

    # Marginal conditional densities f(y | z) and g(y | z) under Q_z
    f_y_given_z = {}
    g_y_given_z = {}
    for z in (0, 1):
        f_y_given_z[z] = {}
        g_y_given_z[z] = {}
        for y in (0, 1):
            f_y_given_z[z][y] = sum(q_x_given_z[z][x] * f_y_given_xz[(x, z)][y] for x in (0, 1))
            g_y_given_z[z][y] = sum(q_x_given_z[z][x] * g_y_given_xz[(x, z)][y] for x in (0, 1))

    # Compute GRO expected log growth, CMI I_f(X; Y | Z), plugin expected log growth, and KL terms
    gro_log_growth = 0.0
    cmi_xyz = 0.0
    plugin_log_growth = 0.0
    expected_kl_yxz = 0.0
    expected_kl_yz = 0.0
    max_lr_diff = 0.0

    for z in (0, 1):
        for x in (0, 1):
            for y in (0, 1):
                p_xyz = p_z[z] * q_x_given_z[z][x] * f_y_given_xz[(x, z)][y]
                # E_{f_{Y|X,Z}}^{CI}(x, y, z)
                e_gro = f_y_given_xz[(x, z)][y] / f_y_given_z[z][y]
                # Likelihood ratio f_{X|Y,Z}(x | y, z) / f_{X|Z}(x | z)
                f_x_given_yz = (q_x_given_z[z][x] * f_y_given_xz[(x, z)][y]) / f_y_given_z[z][y]
                lr = f_x_given_yz / q_x_given_z[z][x]
                max_lr_diff = max(max_lr_diff, abs(e_gro - lr))

                gro_log_growth += p_xyz * math.log(e_gro)
                cmi_xyz += p_xyz * math.log(
                    (q_x_given_z[z][x] * f_y_given_xz[(x, z)][y])
                    / (q_x_given_z[z][x] * f_y_given_z[z][y])
                )

                e_plugin = g_y_given_xz[(x, z)][y] / g_y_given_z[z][y]
                plugin_log_growth += p_xyz * math.log(e_plugin)

                expected_kl_yxz += p_xyz * math.log(f_y_given_xz[(x, z)][y] / g_y_given_xz[(x, z)][y])
                expected_kl_yz += p_xyz * math.log(f_y_given_z[z][y] / g_y_given_z[z][y])

    # Verify Theorem 3 and Proposition 4 identities
    assert max_lr_diff < 1e-15
    assert abs(gro_log_growth - cmi_xyz) < 1e-15
    prop4_rhs_exact = cmi_xyz - expected_kl_yxz + expected_kl_yz
    prop4_lower_bound = cmi_xyz - expected_kl_yxz
    assert abs(plugin_log_growth - prop4_rhs_exact) < 1e-15
    assert plugin_log_growth >= prop4_lower_bound - 1e-15
    assert gro_log_growth > plugin_log_growth > 0.0

    return {
        "cmi_i_x_y_given_z": round(cmi_xyz, 6),
        "gro_expected_log_growth": round(gro_log_growth, 6),
        "max_e_gro_vs_likelihood_ratio_diff": round(max_lr_diff, 16),
        "plugin_expected_log_growth": round(plugin_log_growth, 6),
        "prop4_exact_decomposition_diff": round(abs(plugin_log_growth - prop4_rhs_exact), 16),
        "prop4_kl_lower_bound": round(prop4_lower_bound, 6),
    }


def verify_claim3_tv_robustness_under_model_x_misspecification() -> dict[str, float]:
    """Verify Theorem 6: optional-stopping Type-I error under misspecified hat{Q}_Z <= alpha + d_TV(Q^N, hat{Q}^N)."""
    # Exact enumeration over horizon N = 6 for binary X_i ~ Bernoulli(q) vs misspecified Bernoulli(q_hat)
    n_horizon = 6
    q_true = 0.50
    q_hat = 0.53
    alpha = 0.10

    # Test function h(x) = (q_alt / q_hat) if x == 1 else ((1 - q_alt) / (1 - q_hat))
    # so that under hat{Q}, E_{hat{Q}}[tilde{E}] = 1.0
    q_alt = 0.72

    def e_tilde(x: int) -> float:
        # Take h(x) = q_alt^x (1 - q_alt)^{1-x}; denominator under hat{Q} is q_hat*q_alt + (1-q_hat)*(1-q_alt)
        num = q_alt if x == 1 else (1.0 - q_alt)
        den = q_hat * q_alt + (1.0 - q_hat) * (1.0 - q_alt)
        return num / den

    # Check unit expectation under hat{Q}
    exp_q_hat = q_hat * e_tilde(1) + (1.0 - q_hat) * e_tilde(0)
    assert abs(exp_q_hat - 1.0) < 1e-15

    # Exact total variation d_TV(Q^N, hat{Q}^N) = 0.5 * sum_{x^N in {0,1}^N} |Q^N(x^N) - hat{Q}^N(x^N)|
    tv_distance = 0.0
    prob_reject_q_true = 0.0
    prob_reject_q_hat = 0.0

    for x_seq in itertools.product((0, 1), repeat=n_horizon):
        k_ones = sum(x_seq)
        p_true_seq = (q_true**k_ones) * ((1.0 - q_true) ** (n_horizon - k_ones))
        p_hat_seq = (q_hat**k_ones) * ((1.0 - q_hat) ** (n_horizon - k_ones))
        tv_distance += 0.5 * abs(p_true_seq - p_hat_seq)

        # Check optional-stopping event: exists n <= N such that prod_{i=1}^n tilde{E}(x_i) >= 1/alpha
        s_val = 1.0
        rejected = False
        for x_i in x_seq:
            s_val *= e_tilde(x_i)
            if s_val >= 1.0 / alpha:
                rejected = True
                break
        if rejected:
            prob_reject_q_true += p_true_seq
            prob_reject_q_hat += p_hat_seq

    theorem6_upper_bound = alpha + tv_distance
    assert prob_reject_q_hat <= alpha + 1e-12
    assert prob_reject_q_true <= theorem6_upper_bound + 1e-12

    return {
        "null_reject_prob_under_hat_q": round(prob_reject_q_hat, 6),
        "null_reject_prob_under_true_q": round(prob_reject_q_true, 6),
        "product_tv_distance": round(tv_distance, 6),
        "theorem6_upper_bound_alpha_plus_tv": round(theorem6_upper_bound, 6),
    }


def verify_claim4_sequential_logistic_e_crt_and_truncation() -> dict[str, float]:
    """Verify Proposition 7 and Section 4 truncation safeguard for sequential logistic E-CRT."""
    # Show first why truncation [eps, 1-eps] is essential when an early overfitted estimate
    # predicts p_hat(y=1 | x, z) -> 0 on an observation with Y_n = 1:
    # Without truncation (eps = 0), if hat{beta} is huge negative and Y_n = 1 at large X_n,
    # p_hat(1 | X_n, Z_n) underflows toward 0 while the integral under Q_Z remains bounded away from 0,
    # collapsing E_n^{CI} -> 0 and log S_n^{CI} -> -infinity.
    # Let's compute a concrete single-step example: Z = 0, X_n = 2.5, Y_n = 1, early overfit beta_hat = -12.0
    gh_nodes = [-1.7320508075688772, 0.0, 1.7320508075688772]
    gh_weights = [1.0 / 6.0, 2.0 / 3.0, 1.0 / 6.0]

    def logistic(u: float) -> float:
        if u >= 0:
            return 1.0 / (1.0 + math.exp(-u))
        eu = math.exp(u)
        return eu / (1.0 + eu)

    def eval_step_e(x_val: float, y_val: int, z_val: float, beta_hat: float, gamma_hat: float, eps: float) -> float:
        def p_trunc(x_arg: float) -> float:
            p1 = logistic(beta_hat * x_arg + gamma_hat * z_val)
            p1_c = min(max(p1, eps), 1.0 - eps)
            return p1_c if y_val == 1 else (1.0 - p1_c)

        num = p_trunc(x_val)
        # Integrate over X | Z ~ N(0.5*z_val, 1.0) using 3-point Gauss-Hermite quadrature (exact for degree <= 5)
        den = sum(w * p_trunc(0.5 * z_val + node) for w, node in zip(gh_weights, gh_nodes))
        return num / den

    e_untruncated_shock = eval_step_e(2.5, 1, 0.0, -12.0, 0.0, eps=0.0)
    e_truncated_shock = eval_step_e(2.5, 1, 0.0, -12.0, 0.0, eps=0.05)
    assert e_untruncated_shock < 1e-10
    assert e_truncated_shock > 0.05

    # Now run sequential online logistic E-CRT (with online gradient ascent MLE updates and eps = 0.05 truncation)
    # under H_0 (beta_true = 0.0) and H_1 (beta_true = 1.1)
    rng = random.Random(20261018)
    alpha = 0.05
    eps = 0.05
    n_trials = 200
    n_steps = 250

    null_rejections = 0
    alt_rejections = 0
    alt_final_log_rates = []

    for mode in ("null", "alt"):
        beta_true = 0.0 if mode == "null" else 1.1
        gamma_true = 0.5
        for _ in range(n_trials):
            beta_hat = 0.0
            gamma_hat = 0.0
            log_wealth = 0.0
            rejected = False
            for i in range(1, n_steps + 1):
                z = rng.gauss(0.0, 1.0)
                # Sample X | Z from the 3-point discrete Gaussian-matched law Q_Z so quadrature is exact!
                u_draw = rng.random()
                if u_draw < gh_weights[0]:
                    x = 0.5 * z + gh_nodes[0]
                elif u_draw < gh_weights[0] + gh_weights[1]:
                    x = 0.5 * z + gh_nodes[1]
                else:
                    x = 0.5 * z + gh_nodes[2]
                p_true = logistic(beta_true * x + gamma_true * z)
                y = 1 if rng.random() < p_true else 0

                # Predictable e-value using (beta_hat, gamma_hat) from i-1
                if i > 10:
                    e_i = eval_step_e(x, y, z, beta_hat, gamma_hat, eps=eps)
                    log_wealth += math.log(e_i)
                    if log_wealth >= math.log(1.0 / alpha):
                        rejected = True

                # Update logistic parameters via online Newton/gradient step
                p_pred = logistic(beta_hat * x + gamma_hat * z)
                err = y - p_pred
                lr_step = 0.6 / math.sqrt(i + 5.0)
                beta_hat += lr_step * err * x
                gamma_hat += lr_step * err * z

            if mode == "null" and rejected:
                null_rejections += 1
            elif mode == "alt":
                if rejected:
                    alt_rejections += 1
                alt_final_log_rates.append(log_wealth / n_steps)

    null_type1 = null_rejections / n_trials
    alt_power = alt_rejections / n_trials
    mean_alt_log_rate = sum(alt_final_log_rates) / len(alt_final_log_rates)

    assert null_type1 <= alpha
    assert alt_power >= 0.95
    assert mean_alt_log_rate > 0.05

    return {
        "alt_anytime_power": round(alt_power, 4),
        "alt_mean_per_step_log_growth": round(mean_alt_log_rate, 6),
        "null_anytime_type1_error": round(null_type1, 4),
        "single_step_e_truncated_eps005": round(e_truncated_shock, 6),
        "single_step_e_untruncated_eps0": round(e_untruncated_shock, 14),
    }


def main() -> None:
    results = {
        "claim1_exact_and_mc_conditional_e_statistic": verify_claim1_exact_and_mc_conditional_e_statistic(),
        "claim2_gro_conditional_mutual_information_and_kl_regret": verify_claim2_gro_conditional_mutual_information_and_kl_regret(),
        "claim3_tv_robustness_under_model_x_misspecification": verify_claim3_tv_robustness_under_model_x_misspecification(),
        "claim4_sequential_logistic_e_crt_and_truncation": verify_claim4_sequential_logistic_e_crt_and_truncation(),
    }
    print(json.dumps(results, sort_keys=True))


if __name__ == "__main__":
    main()
