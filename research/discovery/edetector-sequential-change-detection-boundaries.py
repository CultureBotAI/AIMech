#!/usr/bin/env python3
"""Constructed boundary & mathematical verification script for Round 179:
AIMech:EDetectorSequentialChangeDetection (E-Detector Nonparametric Sequential Change Detection).

Verifies four core mathematical properties from Shin, Ramdas, & Rinaldo (2024),
'E-detectors: A Nonparametric Framework for Sequential Change Detection',
The New England Journal of Statistics in Data Science 2(2):229-260 (arXiv:2203.03532):
  1. Nonasymptotic optional-stopping inequality E_{P,inf}[M_tau] <= E_{P,inf}[tau]
     and ARL control E_{P,inf}[N^*] >= 1/alpha under non-stationary composite pre-change
     distributions, plus exact equivalence of recursive and cumulative baseline updates
     (Definitions 2.2, 2.6, 2.8, 2.11, and Theorem 2.4).
  2. Exact equivalence of O(K(n)) recursive updates and double-sum definitions for
     adaptive infinite-mixture e-detectors M_n^{aSR} and M_n^{aCU} with scheduling
     function K(n) and adaptive renormalization factor gamma_j = 1 / sum_{k=1}^{K(j)} omega_k,
     together with the pathwise telescoping identity sum_{k=1}^{K(tau)} omega_k sum_{j=K^{-1}(k)}^tau gamma_j = tau
     (Section 3.1, Equations 29-32, and Proposition 3.3).
  3. Convex-conjugate divergence identity D(Q || P) = sigma^2 * psi^*(Delta^{op}) for
     exponential baseline increments (Proposition 4.2) and pointwise dominance of the
     variational KL_inf bounded-mean betting increment L^lambda(x) = 1 + lambda*(x/m - 1)
     over its sub-exponential lower bound L_tilde^lambda(x) (Section 5.2, Equations 69-76).
  4. Collaborative evidence pooling of e-SR vs. e-CUSUM / Generalized Lorden reduction
     (N_{SR}^* <= N_{CU}^* = N_{Lorden}^* deterministically at threshold 1/alpha, Section 6.2
     & Lemma 6.1) and invalidity of unpenalized supremum over lambda (Remark 3.1).
"""

from __future__ import annotations

import json
import math
import random


def check_1_nonstationary_arl_and_baseline_recursion() -> dict[str, float | int | bool]:
    """Verify Theorem 2.4 & Definition 2.11 under a non-stationary composite pre-change process."""
    p0 = 0.40
    lam = 0.80
    psi_b = math.log(1.0 - p0 + p0 * math.exp(lam)) - lam * p0

    # Verify one-step baseline increment condition E[L_n | F_{n-1}] <= 1 for all p_n <= p0
    max_cond_exp = 0.0
    for p_n in [0.05, 0.15, 0.25, 0.35, 0.40]:
        l_at_1 = math.exp(lam * (1.0 - p0) - psi_b)
        l_at_0 = math.exp(lam * (0.0 - p0) - psi_b)
        cond_exp = p_n * l_at_1 + (1.0 - p_n) * l_at_0
        max_cond_exp = max(max_cond_exp, cond_exp)
    assert max_cond_exp <= 1.0 + 1e-12, f"Expected cond_exp <= 1, got {max_cond_exp}"

    # Verify exact equivalence of O(1) recursive updates and O(n) cumulative definitions
    rng = random.Random(20261018)
    n_steps = 40
    xs = [1 if rng.random() < 0.45 else 0 for _ in range(n_steps)]
    ls = [math.exp(lam * (x - p0) - psi_b) for x in xs]

    m_sr_rec = 0.0
    m_cu_rec = 0.0
    max_rec_diff = 0.0
    for n in range(1, n_steps + 1):
        l_n = ls[n - 1]
        m_sr_rec = (m_sr_rec + 1.0) * l_n
        m_cu_rec = max(m_cu_rec, 1.0) * l_n

        # Explicit Definition 2.6 sums/maxima over start times j = 1..n
        e_procs = []
        for j in range(1, n + 1):
            prod = 1.0
            for i in range(j, n + 1):
                prod *= ls[i - 1]
            e_procs.append(prod)
        m_sr_explicit = sum(e_procs)
        m_cu_explicit = max(e_procs)
        max_rec_diff = max(
            max_rec_diff,
            abs(m_sr_rec - m_sr_explicit),
            abs(m_cu_rec - m_cu_explicit),
        )
        assert m_cu_rec <= m_sr_rec + 1e-12
    assert max_rec_diff < 1e-12, f"Recursive vs explicit mismatch: {max_rec_diff}"

    # Monte Carlo simulation under non-stationary dependent pre-change process:
    # p_n = 0.25 + 0.15 * I(X_{n-1} == 0) <= 0.40 = p0
    alpha = 0.05
    threshold = 1.0 / alpha  # 20.0
    n_trials = 3000
    fixed_tau = 15
    sum_m_sr_at_fixed_tau = 0.0
    sum_n_sr = 0.0
    sum_n_cu = 0.0

    for _ in range(n_trials):
        m_sr = 0.0
        m_cu = 0.0
        prev_x = 0
        n = 0
        stopped_sr = False
        stopped_cu = False
        n_sr_val = 0
        n_cu_val = 0
        while not (stopped_sr and stopped_cu):
            n += 1
            p_n = 0.25 + (0.15 if prev_x == 0 else 0.0)
            x_n = 1 if rng.random() < p_n else 0
            prev_x = x_n
            l_n = math.exp(lam * (x_n - p0) - psi_b)
            m_sr = (m_sr + 1.0) * l_n
            m_cu = max(m_cu, 1.0) * l_n
            if n == fixed_tau:
                sum_m_sr_at_fixed_tau += m_sr
            if (not stopped_sr) and m_sr >= threshold:
                stopped_sr = True
                n_sr_val = n
            if (not stopped_cu) and m_cu >= threshold:
                stopped_cu = True
                n_cu_val = n
            if n >= 500:
                if not stopped_sr:
                    stopped_sr = True
                    n_sr_val = 500
                if not stopped_cu:
                    stopped_cu = True
                    n_cu_val = 500
        assert n_sr_val <= n_cu_val
        sum_n_sr += n_sr_val
        sum_n_cu += n_cu_val

    mean_m_sr_tau = sum_m_sr_at_fixed_tau / n_trials
    arl_sr = sum_n_sr / n_trials
    arl_cu = sum_n_cu / n_trials
    assert mean_m_sr_tau <= fixed_tau, f"Expected E[M_tau] <= {fixed_tau}, got {mean_m_sr_tau}"
    assert arl_sr >= threshold, f"Expected ARL_SR >= {threshold}, got {arl_sr}"
    assert arl_cu >= arl_sr, f"Expected ARL_CU >= ARL_SR, got {arl_cu} vs {arl_sr}"

    return {
        "max_one_step_cond_exp": round(max_cond_exp, 12),
        "max_recursive_vs_explicit_diff": max_rec_diff,
        "fixed_tau": fixed_tau,
        "mc_mean_m_sr_at_tau": round(mean_m_sr_tau, 4),
        "target_arl": threshold,
        "mc_arl_sr": round(arl_sr, 4),
        "mc_arl_cu": round(arl_cu, 4),
    }


def check_2_adaptive_infinite_mixture_and_scheduling() -> dict[str, float | int | bool]:
    """Verify Section 3.1 Equations 29-32 and Proposition 3.3 telescoping identity."""
    def k_sched(n: int) -> int:
        return int(1 + 2 * math.floor(math.log2(n)))

    max_n = 32
    max_k = k_sched(max_n)
    # Geometric weights summing to 1 over k >= 1
    omegas = {k: 0.5**k for k in range(1, max_k + 1)}

    # Generalized inverse K^{-1}(k) = inf{j >= 1 : K(j) >= k}
    k_inv = {}
    for k in range(1, max_k + 1):
        for j in range(1, max_n + 1):
            if k_sched(j) >= k:
                k_inv[k] = j
                break

    # Adaptive re-weighting factor gamma_j = 1 / sum_{k=1}^{K(j)} omega_k
    gammas = {}
    for j in range(1, max_n + 1):
        gammas[j] = 1.0 / sum(omegas[k] for k in range(1, k_sched(j) + 1))
        assert gammas[j] > 1.0

    # 1. Verify combinatorial telescoping identity in proof of Proposition 3.3:
    # For every tau in 1..max_n, sum_{k=1}^{K(tau)} omega_k * sum_{j=K^{-1}(k)}^tau gamma_j == tau
    max_telescoping_err = 0.0
    for tau in range(1, max_n + 1):
        lhs = 0.0
        for k in range(1, k_sched(tau) + 1):
            lhs += omegas[k] * sum(gammas[j] for j in range(k_inv[k], tau + 1))
        max_telescoping_err = max(max_telescoping_err, abs(lhs - float(tau)))
    assert max_telescoping_err < 1e-12, f"Telescoping error: {max_telescoping_err}"

    # 2. Verify exact equivalence between Equations 29-30 (double sum) and Equations 31-32 (recursive)
    rng = random.Random(20261019)
    p0 = 0.45
    lambdas = {k: 0.15 * k for k in range(1, max_k + 1)}
    xs = [1 if rng.random() < 0.55 else 0 for _ in range(max_n)]

    def l_val(n_idx: int, k: int) -> float:
        lam = lambdas[k]
        psi = math.log(1.0 - p0 + p0 * math.exp(lam)) - lam * p0
        return math.exp(lam * (xs[n_idx - 1] - p0) - psi)

    m_asr_k = {k: 0.0 for k in range(1, max_k + 1)}
    m_acu_k = {k: 0.0 for k in range(1, max_k + 1)}
    max_adaptive_diff = 0.0

    for n in range(1, max_n + 1):
        for k in range(1, k_sched(n) + 1):
            if n >= k_inv[k]:
                ln_k = l_val(n, k)
                m_asr_k[k] = (m_asr_k[k] + gammas[n]) * ln_k
                m_acu_k[k] = max(m_acu_k[k], gammas[n]) * ln_k

        m_asr_rec = sum(omegas[k] * m_asr_k[k] for k in range(1, k_sched(n) + 1))
        m_acu_rec = sum(omegas[k] * m_acu_k[k] for k in range(1, k_sched(n) + 1))

        # Double-sum Equations 29-30
        m_asr_dbl = 0.0
        m_acu_dbl = 0.0
        for k in range(1, k_sched(n) + 1):
            sr_inner = 0.0
            cu_inner = 0.0
            for j in range(k_inv[k], n + 1):
                prod = 1.0
                for i in range(j, n + 1):
                    prod *= l_val(i, k)
                term = gammas[j] * prod
                sr_inner += term
                cu_inner = max(cu_inner, term)
            m_asr_dbl += omegas[k] * sr_inner
            m_acu_dbl += omegas[k] * cu_inner

        max_adaptive_diff = max(
            max_adaptive_diff,
            abs(m_asr_rec - m_asr_dbl),
            abs(m_acu_rec - m_acu_dbl),
        )
        assert m_acu_rec <= m_asr_rec + 1e-12

    assert max_adaptive_diff < 1e-11, f"Adaptive recursion diff: {max_adaptive_diff}"

    return {
        "max_telescoping_identity_err": max_telescoping_err,
        "max_adaptive_recursive_vs_doublesum_diff": max_adaptive_diff,
        "k_sched_at_32": k_sched(32),
        "gamma_1": round(gammas[1], 6),
        "gamma_32": round(gammas[32], 6),
    }


def check_3_convex_conjugate_and_bounded_betting_dominance() -> dict[str, float | bool]:
    """Verify Proposition 4.2 and Section 5.2 Equations 69-76 (betting vs sub-exponential)."""
    # Part A: Bernoulli exponential baseline increment (Section 5.1, Eq. 65-67)
    p0 = 0.49
    q = 0.65
    delta_op_bern = q - p0
    # Oracle lambda^{op} = log(q(1-p0) / (p0(1-q)))
    lam_op_bern = math.log((q * (1.0 - p0)) / (p0 * (1.0 - q)))
    psi_b_op = math.log(1.0 - p0 + p0 * math.exp(lam_op_bern)) - lam_op_bern * p0
    d_q_p_bern = lam_op_bern * delta_op_bern - psi_b_op
    kl_bern = q * math.log(q / p0) + (1.0 - q) * math.log((1.0 - q) / (1.0 - p0))
    bern_kl_diff = abs(d_q_p_bern - kl_bern)
    assert bern_kl_diff < 1e-14, f"Bernoulli conjugate KL mismatch: {bern_kl_diff}"

    # Part B: Bounded random variable on [0, 1] (Section 5.2, Eq. 70-75)
    # Compare betting increment L^lambda(x) = 1 + lambda*(x/m - 1)
    # against sub-exponential lower bound L_tilde^lambda(x) = exp(lambda*s(x) - psi_E(lambda)*v(x))
    m = 0.40
    min_ratio = float("inf")
    for x_int in range(0, 101):
        x = x_int / 100.0
        s_x = x / m - 1.0
        v_x = s_x * s_x
        for lam in [0.05, 0.20, 0.50, 0.80]:
            psi_e = -math.log(1.0 - lam) - lam
            l_bet = 1.0 + lam * s_x
            l_subexp = math.exp(lam * s_x - psi_e * v_x)
            assert l_bet >= l_subexp - 1e-14, f"Dominance violated: {l_bet} < {l_subexp}"
            min_ratio = min(min_ratio, l_bet / l_subexp)

    # Under post-change Q supported on {0.1, 0.5, 0.9} with probabilities (0.2, 0.3, 0.5),
    # mean under Q is 0.02 + 0.15 + 0.45 = 0.62 > m = 0.40
    q_support = [(0.1, 0.2), (0.5, 0.3), (0.9, 0.5)]
    mu_q = sum(prob * (x / m - 1.0) for x, prob in q_support)
    sigma2_q = sum(prob * ((x / m - 1.0) ** 2) for x, prob in q_support)
    delta_op = mu_q / sigma2_q
    # Sub-exponential conjugate psi_E^*(u) = u - log(1 + u), attained at lambda^{op} = u / (1 + u)
    lam_op_subexp = delta_op / (1.0 + delta_op)
    psi_e_op = -math.log(1.0 - lam_op_subexp) - lam_op_subexp
    e_log_l_tilde = lam_op_subexp * mu_q - psi_e_op * sigma2_q
    conj_formula = sigma2_q * (delta_op - math.log(1.0 + delta_op))
    assert abs(e_log_l_tilde - conj_formula) < 1e-14

    # Expected log-growth of betting increment at the same lambda^{op} and at its own optimum
    e_log_l_bet_at_subexp_lam = sum(
        prob * math.log(1.0 + lam_op_subexp * (x / m - 1.0)) for x, prob in q_support
    )
    assert e_log_l_bet_at_subexp_lam > e_log_l_tilde

    return {
        "bernoulli_kl_conjugate_diff": bern_kl_diff,
        "min_pointwise_betting_over_subexp_ratio": round(min_ratio, 6),
        "post_change_subexp_drift": round(e_log_l_tilde, 6),
        "post_change_betting_drift": round(e_log_l_bet_at_subexp_lam, 6),
        "betting_strictly_dominates_subexp": e_log_l_bet_at_subexp_lam > e_log_l_tilde,
    }


def check_4_lorden_reduction_and_supremum_invalidity() -> dict[str, float | int | bool]:
    """Verify Section 6.2 (e-SR vs e-CUSUM = Lorden reduction at 1/alpha) & Remark 3.1."""
    rng = random.Random(20261020)
    p0 = 0.40
    q = 0.65
    lam = math.log((q * (1.0 - p0)) / (p0 * (1.0 - q)))
    psi_b = math.log(1.0 - p0 + p0 * math.exp(lam)) - lam * p0

    alpha = 0.005
    threshold = 1.0 / alpha  # 200.0
    changepoint_nu = 40
    n_trials = 1000

    delays_sr = []
    delays_lorden_cu = []
    sr_strictly_faster_count = 0

    for _ in range(n_trials):
        m_sr = 0.0
        m_cu = 0.0
        n = 0
        n_sr = None
        n_cu = None
        while n_sr is None or n_cu is None:
            n += 1
            prob = p0 if n <= changepoint_nu else q
            x_n = 1 if rng.random() < prob else 0
            l_n = math.exp(lam * (x_n - p0) - psi_b)
            m_sr = (m_sr + 1.0) * l_n
            m_cu = max(m_cu, 1.0) * l_n
            if n_sr is None and m_sr >= threshold:
                n_sr = n
            if n_cu is None and m_cu >= threshold:
                n_cu = n
        assert n_sr <= n_cu, f"Pathwise inequality violated: {n_sr} > {n_cu}"
        if n_sr >= changepoint_nu and n_cu >= changepoint_nu:
            delays_sr.append(n_sr - changepoint_nu)
            delays_lorden_cu.append(n_cu - changepoint_nu)
            if n_sr < n_cu:
                sr_strictly_faster_count += 1

    mean_delay_sr = sum(delays_sr) / len(delays_sr)
    mean_delay_lorden = sum(delays_lorden_cu) / len(delays_lorden_cu)
    assert mean_delay_sr < mean_delay_lorden

    # Verify Remark 3.1: Taking unpenalized supremum over lambda in Lambda_grid violates
    # E_{P0,inf}[M_tau] <= tau and inflates false alarms relative to mixture e-SR.
    lam_grid = [0.1, 0.25, 0.5, 0.8, 1.2, 1.6, 2.0, 2.5]
    psi_grid = [math.log(1.0 - p0 + p0 * math.exp(l_val)) - l_val * p0 for l_val in lam_grid]
    fixed_tau = 20
    sup_sum_at_tau = 0.0
    mix_sum_at_tau = 0.0
    n_null_trials = 2000

    for _ in range(n_null_trials):
        m_sr_grid = [0.0 for _ in lam_grid]
        for _step in range(fixed_tau):
            x_n = 1 if rng.random() < p0 else 0
            for idx, l_val in enumerate(lam_grid):
                inc = math.exp(l_val * (x_n - p0) - psi_grid[idx])
                m_sr_grid[idx] = (m_sr_grid[idx] + 1.0) * inc
        sup_sum_at_tau += max(m_sr_grid)
        mix_sum_at_tau += sum(m_sr_grid) / len(m_sr_grid)

    mean_sup_at_tau = sup_sum_at_tau / n_null_trials
    mean_mix_at_tau = mix_sum_at_tau / n_null_trials
    # Unpenalized supremum strictly exceeds tau = 20, violating Definition 2.2
    assert mean_sup_at_tau > fixed_tau * 1.35, f"Expected sup > {fixed_tau*1.35}, got {mean_sup_at_tau}"

    return {
        "mean_post_change_delay_sr": round(mean_delay_sr, 4),
        "mean_post_change_delay_lorden_cu": round(mean_delay_lorden, 4),
        "sr_strictly_faster_fraction": round(sr_strictly_faster_count / len(delays_sr), 4),
        "null_fixed_tau": fixed_tau,
        "mean_mixture_sr_at_tau": round(mean_mix_at_tau, 4),
        "mean_unpenalized_sup_sr_at_tau": round(mean_sup_at_tau, 4),
    }


def main() -> None:
    res1 = check_1_nonstationary_arl_and_baseline_recursion()
    res2 = check_2_adaptive_infinite_mixture_and_scheduling()
    res3 = check_3_convex_conjugate_and_bounded_betting_dominance()
    res4 = check_4_lorden_reduction_and_supremum_invalidity()

    summary = {
        "concept_id": "AIMech:EDetectorSequentialChangeDetection",
        "check_1_nonstationary_arl_and_recursion": res1,
        "check_2_adaptive_infinite_mixture": res2,
        "check_3_convex_conjugate_and_betting": res3,
        "check_4_lorden_reduction_and_supremum": res4,
        "all_checks_passed": True,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
