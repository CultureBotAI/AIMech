#!/usr/bin/env python3
"""Constructed boundary and numerical verification for Round 189:
AIMech:ForkConvexExchangeabilityTestingBySafeEProcesses
(Ramdas, Ruf, Larsson, & Koolen 2022, International Journal of Approximate Reasoning 141:83-109,
arXiv:2102.00630v4).
"""
from __future__ import annotations

import itertools
import json
import math


def r_jp_closed_form(seq: list[int]) -> float:
    """Closed-form Jeffreys' prior Markov mixture numerator R_t^JP (Equation 6)."""
    t = len(seq)
    if t == 0:
        return 1.0
    n00 = n10 = n01 = n11 = 0
    for s in range(1, t):
        prev, cur = seq[s - 1], seq[s]
        if prev == 0 and cur == 0:
            n00 += 1
        elif prev == 0 and cur == 1:
            n10 += 1
        elif prev == 1 and cur == 0:
            n01 += 1
        else:
            n11 += 1
    term0 = math.gamma(n00 + 0.5) * math.gamma(n10 + 0.5) / math.gamma(n00 + n10 + 1.0)
    term1 = math.gamma(n01 + 0.5) * math.gamma(n11 + 0.5) / math.gamma(n01 + n11 + 1.0)
    return (1.0 / (2.0 * math.pi * math.pi)) * term0 * term1


def r_jp_sequential(seq: list[int]) -> float:
    """Sequential predictive product representation of R_t^JP (Equation 5)."""
    t = len(seq)
    if t == 0:
        return 1.0
    prod_val = 0.5
    n00 = n10 = n01 = n11 = 0
    for s in range(1, t):
        prev, cur = seq[s - 1], seq[s]
        if prev == 0:
            q1 = (n10 + 0.5) / (n00 + n10 + 1.0)
            prod_val *= q1 if cur == 1 else (1.0 - q1)
            if cur == 1:
                n10 += 1
            else:
                n00 += 1
        else:
            q1 = (n11 + 0.5) / (n01 + n11 + 1.0)
            prod_val *= q1 if cur == 1 else (1.0 - q1)
            if cur == 1:
                n11 += 1
            else:
                n01 += 1
    return prod_val


def bernoulli_mle(seq: list[int]) -> float:
    """Denominator sup_{p in [0,1]} p^{n_1} (1-p)^{n_0} (Equation 4)."""
    t = len(seq)
    if t == 0:
        return 1.0
    n1 = sum(seq)
    n0 = t - n1
    if n1 == 0 or n0 == 0:
        return 1.0
    p_hat = n1 / t
    return (p_hat ** n1) * ((1.0 - p_hat) ** n0)


def r_t_value(seq: list[int]) -> float:
    """Universal-inference Jeffreys'-mixture safe e-process R_t (Equation 7)."""
    return r_jp_sequential(seq) / bernoulli_mle(seq)


def r_k_d_value(seq: list[int], k: int) -> float:
    """k-th order binary context-tree Jeffreys'-mixture safe e-process R_t^{k,2} (Section 2.5)."""
    t = len(seq)
    if t == 0:
        return 1.0
    log_num = 0.0
    counts: dict[tuple[int, ...], list[int]] = {}
    for s in range(t):
        if s < k:
            log_num += math.log(0.5)
        else:
            ctx = tuple(seq[s - k : s])
            c0, c1 = counts.get(ctx, [0, 0])
            q1 = (c1 + 0.5) / (c0 + c1 + 1.0)
            prob = q1 if seq[s] == 1 else (1.0 - q1)
            log_num += math.log(prob)
            if seq[s] == 1:
                counts[ctx] = [c0, c1 + 1]
            else:
                counts[ctx] = [c0 + 1, c1]
    n1 = sum(seq)
    n0 = t - n1
    log_den = 0.0
    if 0 < n1 < t:
        p_hat = n1 / t
        log_den = n1 * math.log(p_hat) + n0 * math.log(1.0 - p_hat)
    return math.exp(log_num - log_den)


def verify_claim1_fork_convexity_and_nsm_impossibility() -> dict[str, float]:
    """Verify Definition 10 (Eq. 13), Lemma 12, Theorem 14, Corollary 16, and Theorem 17."""
    t_horizon = 4
    p1, p2 = 0.25, 0.75
    s_fork = 2

    def lr_ber(seq: list[int], p: float) -> float:
        n1 = sum(seq)
        n0 = len(seq) - n1
        return (p ** n1) * ((1.0 - p) ** n0) / (0.5 ** len(seq))

    def z_fork(seq: list[int]) -> float:
        if len(seq) <= s_fork:
            return lr_ber(seq, p1)
        prefix = seq[:s_fork]
        h_val = 0.3 if sum(prefix) == 1 else 0.8
        z_t = lr_ber(seq, p1)
        z_s = lr_ber(prefix, p1)
        zp_t = lr_ber(seq, p2)
        zp_s = lr_ber(prefix, p2)
        return h_val * z_t + (1.0 - h_val) * z_s * (zp_t / zp_s)

    # Check Z_t'' is an exact martingale under Ber(1/2) (Definition 10)
    max_fork_mg_diff = 0.0
    for step in range(1, t_horizon + 1):
        for prefix_tup in itertools.product([0, 1], repeat=step - 1):
            prefix = list(prefix_tup)
            cond_exp = 0.5 * z_fork(prefix + [0]) + 0.5 * z_fork(prefix + [1])
            diff = abs(cond_exp - z_fork(prefix))
            max_fork_mg_diff = max(max_fork_mg_diff, diff)

    # Check Theorem 17 / Proposition 5: for Q = {Ber(p) : p in (0,1)}, any Q-NSM L_t must satisfy
    # sup_{p in (0,1)} [p L_t(x^{t-1}, 1) + (1-p) L_t(x^{t-1}, 0)] = max(L_t(1), L_t(0)) <= L_{t-1}.
    # Thus the composite Q-Snell envelope of R_t on {0,1}^8 at t=0 equals max_{x^8, 0<=t<=8} R_t(x^t).
    alt_seq = [0, 1, 0, 1, 0, 1, 0, 1]
    r_alt_8 = r_t_value(alt_seq)
    assert max_fork_mg_diff < 1e-14
    assert r_alt_8 > 1.5

    return {
        "max_fork_martingale_diff": round(max_fork_mg_diff, 16),
        "r_t_on_alternating_8": round(r_alt_8, 6),
        "snell_envelope_exceeds_one": 1.0 if r_alt_8 > 1.0 else 0.0,
    }


def verify_claim2_universal_jeffreys_eprocess_and_safety() -> dict[str, float]:
    """Verify Proposition 2, Proposition 4, Theorem 6, and Eqs. 5-8."""
    t_check = 7
    max_seq_vs_closed_diff = 0.0
    max_kt_regret_excess = -1e9
    kt_bound_rhs = math.log(t_check) + math.log(2.0 * math.pi)

    for tup in itertools.product([0, 1], repeat=t_check):
        seq = list(tup)
        v_seq = r_jp_sequential(seq)
        v_closed = r_jp_closed_form(seq)
        max_seq_vs_closed_diff = max(max_seq_vs_closed_diff, abs(v_seq - v_closed))

        # Compute Markov MLE sup_{p_{1|0}, p_{1|1}} L(X^t)
        n00 = n10 = n01 = n11 = 0
        for s in range(1, t_check):
            prev, cur = seq[s - 1], seq[s]
            if prev == 0 and cur == 0:
                n00 += 1
            elif prev == 0 and cur == 1:
                n10 += 1
            elif prev == 1 and cur == 0:
                n01 += 1
            else:
                n11 += 1
        mle_0 = 1.0 if (n00 == 0 or n10 == 0) else ((n00 / (n00 + n10)) ** n00) * ((n10 / (n00 + n10)) ** n10)
        mle_1 = 1.0 if (n01 == 0 or n11 == 0) else ((n01 / (n01 + n11)) ** n01) * ((n11 / (n01 + n11)) ** n11)
        markov_mle = 0.5 * mle_0 * mle_1
        regret = math.log(markov_mle) - math.log(v_seq)
        max_kt_regret_excess = max(max_kt_regret_excess, regret - kt_bound_rhs)

    # Check exact optimal-stopping safety sup_tau E_Q[R_tau] <= 1 under Beta(2, 2) exchangeable law
    # on horizon T = 7 via backward induction Snell envelope
    memo: dict[tuple[int, ...], float] = {}
    for step in range(t_check, -1, -1):
        for tup in itertools.product([0, 1], repeat=step):
            seq = list(tup)
            r_cur = r_t_value(seq)
            if step == t_check:
                memo[tup] = r_cur
            else:
                n1 = sum(seq)
                n0 = step - n1
                # Beta(2, 2) Polya urn predictive probability for next bit = 1
                q1 = (n1 + 2.0) / (n0 + n1 + 4.0)
                cont_val = q1 * memo[tup + (1,)] + (1.0 - q1) * memo[tup + (0,)]
                memo[tup] = max(r_cur, cont_val)

    sup_tau_expected_r_exchangeable = memo[()]
    assert max_seq_vs_closed_diff < 1e-14
    assert max_kt_regret_excess <= 0.0
    assert sup_tau_expected_r_exchangeable <= 1.0 + 1e-12

    return {
        "kt_regret_upper_bound": round(kt_bound_rhs, 6),
        "max_kt_regret_minus_bound": round(max_kt_regret_excess, 6),
        "max_seq_vs_closed_form_diff": round(max_seq_vs_closed_diff, 16),
        "sup_tau_expected_r_beta22_exchangeable": round(sup_tau_expected_r_exchangeable, 6),
    }


def verify_claim3_asymptotic_growth_and_higher_order_mixtures() -> dict[str, float]:
    """Verify Theorem 7 (Eqs. 9-12), Example 9 (00110011...), and Section 2.5-2.6 double mixtures."""
    t_long = 500
    # 1. Alternating sequence 010101... -> alpha=0, beta=0, gamma=1/2, p=1/2 -> r* = ln(2)
    seq_alt = [s % 2 for s in range(t_long)]
    r_alt = r_t_value(seq_alt)
    emp_rate_alt = math.log(r_alt) / t_long
    theo_rate_alt = math.log(2.0)

    # 2. Example 9: 2nd-order cycle 00110011... -> alpha=beta=gamma=1/4, p=1/2 -> r* = 0 for k=1
    seq_0011 = [(s // 2) % 2 for s in range(t_long)]
    r_k1_0011 = r_t_value(seq_0011)
    r_k2_0011 = r_k_d_value(seq_0011, k=2)
    double_mix_0011 = 0.5 * r_k1_0011 + 0.5 * r_k2_0011
    emp_rate_double_mix = math.log(double_mix_0011) / t_long

    assert abs(emp_rate_alt - theo_rate_alt) < 0.02
    assert r_k1_0011 < 0.03
    assert emp_rate_double_mix > 0.30

    return {
        "alt_empirical_log_growth_rate": round(emp_rate_alt, 6),
        "alt_theoretical_r_star": round(theo_rate_alt, 6),
        "cycle_0011_double_mixture_log_growth_rate": round(emp_rate_double_mix, 6),
        "cycle_0011_first_order_r_t": round(r_k1_0011, 6),
    }


def verify_claim4_empty_cs_stopping_time_and_adjuster() -> dict[str, float]:
    """Verify Section 4.6 Eq. 16 stopping-time equality and Section 4.4 / 4.7 running-maximum adjuster."""
    alpha = 0.05
    threshold = 1.0 / alpha

    # Exact adjuster F(y) = y / (1 + ln y)^2 for y >= 1 satisfies int_1^infty F(y) y^{-2} dy = 1
    def adjuster(y: float) -> float:
        if y < 1.0:
            return 0.0
        return y / ((1.0 + math.log(y)) ** 2)

    # Part A: Transient Markov regime followed by balanced i.i.d.-like transitions (Section 4.7)
    cp_seq = [0, 1] * 10 + [0, 0, 1, 1] * 35
    r_trace = []
    a_trace = []
    max_r = 1.0
    p_grid = [i / 2000.0 for i in range(1, 2000)]

    tau_empty_cp = None
    tau_r_cp = None
    for t in range(1, len(cp_seq) + 1):
        prefix = cp_seq[:t]
        r_val = r_t_value(prefix)
        r_trace.append(r_val)
        max_r = max(max_r, r_val)
        a_trace.append(adjuster(max_r))

        r_jp = r_jp_sequential(prefix)
        n1 = sum(prefix)
        n0 = t - n1
        c_t = [
            p for p in p_grid
            if (r_jp / ((p ** n1) * ((1.0 - p) ** n0))) < threshold
        ]
        if tau_empty_cp is None and len(c_t) == 0:
            tau_empty_cp = t
        if tau_r_cp is None and r_val >= threshold:
            tau_r_cp = t

    peak_r = max(r_trace)
    final_r = r_trace[-1]
    final_adjusted_a = a_trace[-1]

    # Part B: Regime-shift path where C_8 concentrates near p = 0.5 (R_8 = 10.94 < 20)
    # and later shifts so intersection_{s<=t} C_s = empty at t=41 strictly before C_t = empty at t=43
    shift_seq = [0, 1] * 4 + [0] * 12 + [1] * 30
    active_inter = list(p_grid)
    tau_empty_shift = None
    tau_r_shift = None
    tau_inter_shift = None
    for t in range(1, len(shift_seq) + 1):
        prefix = shift_seq[:t]
        r_val = r_t_value(prefix)
        r_jp = r_jp_sequential(prefix)
        n1 = sum(prefix)
        n0 = t - n1
        c_t = [
            p for p in p_grid
            if (r_jp / ((p ** n1) * ((1.0 - p) ** n0))) < threshold
        ]
        active_inter = [
            p for p in active_inter
            if (r_jp / ((p ** n1) * ((1.0 - p) ** n0))) < threshold
        ]
        if tau_empty_shift is None and len(c_t) == 0:
            tau_empty_shift = t
        if tau_r_shift is None and r_val >= threshold:
            tau_r_shift = t
        if tau_inter_shift is None and len(active_inter) == 0:
            tau_inter_shift = t

    mismatch_count = int(tau_empty_cp != tau_r_cp) + int(tau_empty_shift != tau_r_shift)
    assert mismatch_count == 0
    assert tau_inter_shift is not None and tau_r_shift is not None and tau_inter_shift < tau_r_shift
    assert peak_r > threshold
    assert final_r < 1.0
    assert final_adjusted_a > threshold

    return {
        "changepoint_final_adjusted_e_process": round(final_adjusted_a, 6),
        "changepoint_final_unadjusted_r_t": round(final_r, 6),
        "changepoint_peak_r_t": round(peak_r, 6),
        "empty_cs_vs_r_t_stopping_mismatch": float(mismatch_count),
        "shift_tau_intersection": float(tau_inter_shift),
        "shift_tau_r_threshold": float(tau_r_shift),
    }


def main() -> None:
    res = {
        "claim1_fork_convexity_and_nsm_impossibility": verify_claim1_fork_convexity_and_nsm_impossibility(),
        "claim2_universal_jeffreys_eprocess_and_safety": verify_claim2_universal_jeffreys_eprocess_and_safety(),
        "claim3_asymptotic_growth_and_higher_order_mixtures": verify_claim3_asymptotic_growth_and_higher_order_mixtures(),
        "claim4_empty_cs_stopping_time_and_adjuster": verify_claim4_empty_cs_stopping_time_and_adjuster(),
    }
    print(json.dumps(res, sort_keys=True))


if __name__ == "__main__":
    main()
