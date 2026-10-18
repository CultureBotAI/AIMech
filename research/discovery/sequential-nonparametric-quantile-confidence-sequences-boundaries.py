#!/usr/bin/env python3
"""Constructed mathematical boundary checks for SequentialNonparametricQuantileConfidenceSequences.

Verifies the four core methodological pillars of Howard & Ramdas (2022,
Bernoulli 28(3):1704-1728, arXiv:1906.09712):
1. Exact Galois inversion equivalences between empirical CDFs (F_hat_t, F_hat_t^-)
   and order-statistic quantile functions (Q_hat_t, Q_hat_t^-), plus the
   interpolated quantile martingale S_t(p) and sub-Bernoulli / sub-gamma CGF dominance
   on distributions with point masses.
2. Fixed-quantile polynomial-stitched sub-gamma CS f_t(p) (Theorem 1a, Eq. 41)
   and beta-binomial conjugate mixture CS f_tilde_t(p) (Theorem 1b, Eqs. 45-46)
   with Lambert W_{-1} tuning (Eq. 21), tail-quantile tightness vs. sub-Gaussian
   normal-mixture bounds, and anytime coverage on heavy-tailed Cauchy streams.
3. Time-uniform empirical process finite LIL / DKW bound (Theorem 2, Theorem 4,
   Corollary 2) vs. union-bounded DKW bounds, plus Lemma 10 log-odds grid spacing
   inequality for double-stitched quantile-uniform bands (Theorem 5).
4. Two-sample sequential quantile test product supermartingale lower bound
   (Theorem 6, Section C.5) and QLUCB quantile best-arm identification sample
   savings (Theorem 3, Section 6).
"""

from __future__ import annotations

import bisect
import functools
import json
import math
import random


@functools.lru_cache(maxsize=None)
def riemann_zeta(s: float, n_terms: int = 10000) -> float:
    """Compute Riemann zeta(s) for s > 1 via Euler-Maclaurin tail."""
    total = sum(k ** (-s) for k in range(1, n_terms))
    total += (n_terms ** (1.0 - s)) / (s - 1.0) + 0.5 * (n_terms ** (-s))
    return total


def lambert_w_minus1(x: float) -> float:
    """Compute the lower branch W_{-1}(x) for x in (-1/e, 0) via Halley's method."""
    if not (-1.0 / math.e < x < 0.0):
        raise ValueError(f"x={x} out of domain (-1/e, 0)")
    L1 = math.log(-x)
    L2 = math.log(-L1)
    w = L1 - L2 + L2 / L1
    for _ in range(40):
        ew = math.exp(w)
        f = w * ew - x
        fp = ew * (w + 1.0)
        fpp = ew * (w + 2.0)
        denom = fp - (f * fpp) / (2.0 * fp)
        step = f / denom
        w -= step
        if abs(step) < 1e-15:
            break
    return w


def stitched_sp(t: float, p: float, alpha: float, eta: float = 2.04, s: float = 1.4, m: float = 1.0) -> float:
    """Compute S_p(t) in Eq. (41) of Howard & Ramdas (2022)."""
    t_eff = max(t, m)
    zeta_s = riemann_zeta(s)
    ell = s * math.log(math.log(eta * t_eff / m)) + math.log(2.0 * zeta_s / (alpha * (math.log(eta) ** s)))
    k1 = (eta ** 0.25 + eta ** (-0.25)) / math.sqrt(2.0)
    k2 = (math.sqrt(eta) + 1.0) / 2.0
    cp = (1.0 - 2.0 * p) / 3.0
    return math.sqrt((k1 ** 2) * p * (1.0 - p) * t_eff * ell + (k2 ** 2) * (cp ** 2) * (ell ** 2)) + cp * k2 * ell


@functools.lru_cache(maxsize=None)
def ft_stitched(t: float, p: float, alpha: float, eta: float = 2.04, s: float = 1.4, m: float = 1.0) -> float:
    """Compute fixed-quantile stitched radius f_t(p) = S_p(t vee m) / t."""
    return stitched_sp(t, p, alpha, eta=eta, s=s, m=m) / t


def log_beta(a: float, b: float) -> float:
    """Compute log B(a, b) = lgamma(a) + lgamma(b) - lgamma(a + b)."""
    return math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)


def log_m_pr(s: float, v: float, p: float, r: float) -> float:
    """Compute log M_{p,r}(s, v) from Eq. (46) of Howard & Ramdas (2022)."""
    a = (r + v) / p - s
    b = (r + v) / (1.0 - p) + s
    if a <= 0.0 or b <= 0.0:
        return float("inf")
    term1 = -(v / (1.0 - p) + s) * math.log(p) - (v / p - s) * math.log(1.0 - p)
    term2 = log_beta(a, b) - log_beta(r / p, r / (1.0 - p))
    return term1 + term2


def f_tilde_beta_binomial(t: float, p: float, alpha: float, r: float) -> float:
    """Compute f_tilde_t(p) from Eq. (45) via bisection on s in [0, (r + v)/p)."""
    v = p * (1.0 - p) * t
    target = math.log(1.0 / alpha)
    s_max = (r + v) / p
    lo = 0.0
    hi = s_max * (1.0 - 1e-12)
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if log_m_pr(mid, v, p, r) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi) / t


def normal_mixture_SubG(t: float, alpha: float, r: float) -> float:
    """Sub-Gaussian normal-mixture quantile radius from Eq. (12)."""
    return math.sqrt((t + r) / (4.0 * (t ** 2)) * math.log((t + r) / (r * (alpha ** 2))))


def verify_galois_inversion_and_martingale() -> dict[str, float]:
    """Verify Eq. (35) Galois inversions and sub-Bernoulli quantile martingale S_t(p)."""
    # Sample with ties/atoms to test strict vs non-strict inequalities in Eq. (35)
    samples = [-2.0, -1.0, -1.0, 0.0, 0.5, 0.5, 0.5, 1.2, 3.0, 3.0]
    t = len(samples)
    sorted_x = sorted(samples)

    def f_hat(x: float) -> float:
        return sum(1 for v in sorted_x if v <= x) / t

    def f_hat_minus(x: float) -> float:
        return sum(1 for v in sorted_x if v < x) / t

    def q_hat(p: float) -> float:
        if p < 0.0:
            return -float("inf")
        if p >= 1.0:
            return float("inf")
        idx = int(math.floor(t * p))  # 0-based index for floor(tp) + 1 order statistic
        return sorted_x[idx]

    def q_hat_minus(p: float) -> float:
        if p <= 0.0:
            return -float("inf")
        if p > 1.0:
            return float("inf")
        idx = int(math.ceil(t * p)) - 1  # 0-based index for ceil(tp) order statistic
        return sorted_x[idx]

    x_grid = [-2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.25, 0.5, 1.0, 1.2, 2.0, 3.0, 3.5]
    p_grid = [k / 40.0 for k in range(1, 40)]
    inversion_mismatches = 0
    for x in x_grid:
        for p in p_grid:
            lhs1 = f_hat_minus(x) <= p + 1e-15
            rhs1 = x <= q_hat(p)
            lhs2 = f_hat(x) + 1e-15 >= p
            rhs2 = q_hat_minus(p) <= x
            if lhs1 != rhs1 or lhs2 != rhs2:
                inversion_mismatches += 1
    assert inversion_mismatches == 0

    # Discrete distribution with atom at Q(p): X in {0, 1, 2} with probs (0.2, 0.5, 0.3)
    # For p = 0.45: Q(p) = Q^-(p) = 1, F^-(1) = 0.2, F(1) = 0.7 -> pi(p) = (0.45 - 0.2)/0.5 = 0.5
    p = 0.45
    f_minus_q = 0.2
    f_q = 0.7
    pi_p = (p - f_minus_q) / (f_q - f_minus_q)
    # Possible increments Delta S_t(p) = 1_{X < 1} + pi(p) 1_{X == 1} - p
    inc_vals = [1.0 - p, pi_p - p, 0.0 - p]
    inc_probs = [0.2, 0.5, 0.3]
    mean_inc = sum(v * pr for v, pr in zip(inc_vals, inc_probs))
    assert abs(mean_inc) < 1e-15

    # Check sub-Bernoulli and sub-gamma CGF dominance
    max_cgf_gap_b = -float("inf")
    max_b_to_g_gap = -float("inf")
    c_p = (1.0 - 2.0 * p) / 3.0
    for k in range(1, 80):
        lam = 0.03 * k
        mgf = sum(pr * math.exp(lam * v) for v, pr in zip(inc_vals, inc_probs))
        cgf = math.log(mgf)
        psi_b = p * (1.0 - p) * (1.0 / (p * (1.0 - p))) * math.log(
            (p * math.exp((1.0 - p) * lam) + (1.0 - p) * math.exp(-p * lam))
        )
        psi_g = p * (1.0 - p) * (lam ** 2) / (2.0 * (1.0 - c_p * lam))
        max_cgf_gap_b = max(max_cgf_gap_b, cgf - psi_b)
        max_b_to_g_gap = max(max_b_to_g_gap, psi_b - psi_g)
    assert max_cgf_gap_b <= 1e-12
    assert max_b_to_g_gap <= 1e-12

    return {
        "inversion_mismatches": float(inversion_mismatches),
        "atom_martingale_mean_abs_err": round(abs(mean_inc), 16),
        "max_cgf_minus_psi_b": round(max_cgf_gap_b, 10),
        "max_psi_b_minus_psi_g": round(max_b_to_g_gap, 10),
    }


def verify_fixed_quantile_bounds_and_cauchy_coverage() -> dict[str, float]:
    """Verify Theorem 1a/1b tail tightness, Lambert W_{-1} tuning, and Cauchy CS coverage."""
    alpha = 0.05
    m = 32.0

    # Appendix D explicit beta-binomial tuning parameters (lines 1056-1057):
    # r = 0.145 for p = 0.05/0.95, r = 0.758 for p = 0.5 at m = 32, alpha = 0.05,
    # compared with Proposition 3 Lambert W_{-1} tuning ratio v_m / rho = -W_{-1}(-alpha^2/(2*pi*e)) - 1.
    w_ratio = -lambert_w_minus1(-(alpha ** 2) / (2.0 * math.pi * math.e)) - 1.0
    rho_prop3_p05 = 0.05 * 0.95 * m / w_ratio
    rho_prop3_p50 = 0.50 * 0.50 * m / w_ratio
    r_p05 = 0.145
    r_p50 = 0.758
    assert abs(rho_prop3_p05 - r_p05) < 0.005
    assert abs(rho_prop3_p50 - r_p50) < 0.025

    # Compare tail quantile (p = 0.05) radii at t = 200
    t_eval = 200.0
    f_stitch_p05 = ft_stitched(t_eval, 0.05, alpha, eta=2.04, s=1.4, m=m)
    f_bb_p05 = f_tilde_beta_binomial(t_eval, 0.05, alpha, r=r_p05)
    f_subg_p05 = normal_mixture_SubG(t_eval, alpha, r=0.504)
    tail_tightness_ratio = f_subg_p05 / f_bb_p05
    assert tail_tightness_ratio > 1.85
    assert f_bb_p05 < f_stitch_p05

    # Monte Carlo coverage on heavy-tailed standard Cauchy(0, 1) stream for median p = 0.5
    rng = random.Random(20261018)
    n_trials = 500
    horizon = 200
    cs_miscover = 0
    clt_miscover = 0
    z_975 = 1.959963984540054

    # Precompute radii for t = 1..horizon
    u_cs = [ft_stitched(t, 0.5, alpha, eta=2.04, s=1.4, m=1.0) for t in range(1, horizon + 1)]
    u_clt = [z_975 * 0.5 / math.sqrt(t) for t in range(1, horizon + 1)]

    for _ in range(n_trials):
        ordered: list[float] = []
        cs_failed = False
        clt_failed = False
        for t in range(1, horizon + 1):
            u = rng.random()
            x = math.tan(math.pi * (u - 0.5))  # Cauchy(0, 1), true median Q(0.5) = 0.0
            bisect.insort(ordered, x)

            if not cs_failed:
                p_lo = 0.5 - u_cs[t - 1]
                p_hi = 0.5 + u_cs[t - 1]
                lo_val = ordered[int(math.ceil(t * p_lo)) - 1] if p_lo > 0.0 else -float("inf")
                hi_val = ordered[int(math.floor(t * p_hi))] if p_hi < 1.0 else float("inf")
                if not (lo_val <= 0.0 <= hi_val):
                    cs_failed = True

            if not clt_failed and t >= 5:
                p_lo_c = 0.5 - u_clt[t - 1]
                p_hi_c = 0.5 + u_clt[t - 1]
                lo_c = ordered[int(math.ceil(t * p_lo_c)) - 1] if p_lo_c > 0.0 else -float("inf")
                hi_c = ordered[int(math.floor(t * p_hi_c))] if p_hi_c < 1.0 else float("inf")
                if not (lo_c <= 0.0 <= hi_c):
                    clt_failed = True

        if cs_failed:
            cs_miscover += 1
        if clt_failed:
            clt_miscover += 1

    cs_miscover_rate = cs_miscover / n_trials
    clt_miscover_rate = clt_miscover / n_trials
    assert cs_miscover_rate <= alpha
    assert clt_miscover_rate > 0.30

    return {
        "r_tuned_p05_m32": round(r_p05, 6),
        "r_tuned_p50_m32": round(r_p50, 6),
        "f_bb_p05_t200": round(f_bb_p05, 6),
        "f_stitch_p05_t200": round(f_stitch_p05, 6),
        "f_subg_p05_t200": round(f_subg_p05, 6),
        "tail_tightness_ratio_subg_to_bb": round(tail_tightness_ratio, 6),
        "cauchy_cs_miscover_rate": round(cs_miscover_rate, 4),
        "cauchy_naive_clt_miscover_rate": round(clt_miscover_rate, 4),
    }


def verify_empirical_process_lil_and_lemma10() -> dict[str, float]:
    """Verify Theorem 2 / Theorem 4 finite LIL constants, Corollary 2, and Lemma 10."""
    A = 0.85
    C = 7.0
    eta = 1.01
    gamma_val = math.sqrt(2.0 / eta) * (A - math.sqrt(2.0 * (eta - 1.0) / C))
    gamma_sq = gamma_val ** 2
    assert gamma_sq >= 1.25
    prefactor_125 = 4.0 * (1.0 + 1.0 / ((1.25 - 1.0) * math.log(eta)))
    assert prefactor_125 <= 1612.0

    # Compare Corollary 2 (m=32, C=8.123) vs Szorenyi et al. (2015) and Darling-Robbins (1968)
    m = 32.0
    c_cor2 = 8.123
    t_check = 1000.0
    g_cor2 = 0.85 * math.sqrt((math.log(math.log(math.e * t_check / m)) + c_cor2) / t_check)
    u_szorenyi = math.sqrt((math.log(t_check - 31.0) + 2.093) / t_check)
    u_dr68 = math.sqrt(((t_check + 1.0) / (t_check ** 2)) * (2.0 * math.log(t_check) + 0.601))
    u_dkw_fixed = math.sqrt(math.log(2.0 / 0.05) / (2.0 * t_check))
    assert g_cor2 < u_szorenyi < u_dr68
    ratio_to_fixed_dkw = g_cor2 / u_dkw_fixed
    assert 1.5 < ratio_to_fixed_dkw < 2.2

    # Verify Lemma 10: q_p - p <= tanh(a/2) sqrt(p(1-p)) <= (a/2) sqrt(p(1-p))
    max_lemma10_diff = -float("inf")
    for a_idx in range(1, 41):
        a = 0.05 * a_idx
        for p_idx in range(50, 100):
            p = p_idx / 100.0
            odds = math.exp(a) * p / (1.0 - p)
            q_p = odds / (1.0 + odds)
            rhs_tanh = math.tanh(0.5 * a) * math.sqrt(p * (1.0 - p))
            rhs_linear = 0.5 * a * math.sqrt(p * (1.0 - p))
            assert q_p - p <= rhs_tanh + 1e-15
            assert rhs_tanh <= rhs_linear + 1e-15
            max_lemma10_diff = max(max_lemma10_diff, (q_p - p) - rhs_linear)
    assert max_lemma10_diff <= 0.0

    return {
        "gamma_sq_A085_C7_eta101": round(gamma_sq, 6),
        "prefactor_at_gamma_sq_125": round(prefactor_125, 4),
        "cor2_radius_t1000": round(g_cor2, 6),
        "szorenyi_radius_t1000": round(u_szorenyi, 6),
        "dr68_radius_t1000": round(u_dr68, 6),
        "cor2_to_fixed_dkw_ratio_t1000": round(ratio_to_fixed_dkw, 6),
        "max_lemma10_violation": round(max_lemma10_diff, 8),
    }


def verify_two_sample_and_qlucb() -> dict[str, float]:
    """Verify Theorem 6 product supermartingale bound and Theorem 3 QLUCB vs QPAC."""
    # 1. Verify Theorem 6: for two arms with identical distribution under H_0: Q_2(p) - Q_1(p) = 0,
    # G_{1,t}(x) + G_{2,t}(x) <= log L_{1,t} + log L_{2,t} at x = Q_1(p) = Q_2(p).
    p = 0.5
    r = 0.758
    rng = random.Random(20261018)
    arm1 = sorted(rng.gauss(0.0, 1.0) for _ in range(40))
    arm2 = sorted(rng.gauss(0.0, 1.0) for _ in range(40))

    def g_kt(sorted_obs: list[float], x: float) -> float:
        n = len(sorted_obs)
        f_minus = sum(1 for v in sorted_obs if v < x) / n
        f_plus = sum(1 for v in sorted_obs if v <= x) / n
        s_lo = n * (f_minus - p)
        s_hi = n * (f_plus - p)
        if s_lo <= 0.0 <= s_hi:
            return 0.0  # minimum of log M_{0.5, r}(s, v) is at s = 0 where M = 1
        s_eval = s_lo if s_lo > 0.0 else s_hi
        return log_m_pr(s_eval, p * (1.0 - p) * n, p, r)

    true_q = 0.0
    s1_true = sum(1.0 if v <= true_q else 0.0 for v in arm1) - len(arm1) * p
    s2_true = sum(1.0 if v <= true_q else 0.0 for v in arm2) - len(arm2) * p
    log_l_tilde_true = (
        log_m_pr(s1_true, p * (1.0 - p) * len(arm1), p, r)
        + log_m_pr(s2_true, p * (1.0 - p) * len(arm2), p, r)
    )
    cand_x = sorted(set(arm1 + arm2 + [0.0]))
    min_profile_g = min(g_kt(arm1, x) + g_kt(arm2, x) for x in cand_x)
    assert min_profile_g <= log_l_tilde_true + 1e-12

    # 2. Simulate 4-arm median bandit (pi = 0.5, eps = 0.05, delta = 0.05):
    # Arm 0 has median 0.60, Arms 1..3 have median 0.0 (Uniform[-0.5, 0.5] shifted)
    k_arms = 4
    pi_q = 0.5
    eps = 0.05
    delta = 0.05
    alpha_arm = 2.0 * delta / k_arms
    medians = [0.60, 0.0, 0.0, 0.0]

    def sample_arm(arm_idx: int, gen: random.Random) -> float:
        return medians[arm_idx] + (gen.random() - 0.5)

    def bounds_for_arm(obs: list[float]) -> tuple[float, float]:
        n = len(obs)
        u_rad = ft_stitched(n, pi_q - eps, alpha_arm, eta=2.04, s=1.4, m=1.0)
        l_rad = ft_stitched(n, 1.0 - (pi_q + eps), alpha_arm, eta=2.04, s=1.4, m=1.0)
        p_hi = (pi_q - eps) + u_rad
        p_lo = (pi_q + eps) - l_rad
        u_val = obs[int(math.floor(n * p_hi))] if p_hi < 1.0 else 10.0
        l_val = obs[int(math.ceil(n * p_lo)) - 1] if p_lo > 0.0 else -10.0
        return l_val, u_val

    n_bandit_runs = 25
    qlucb_samples = []
    qpac_samples = []
    qlucb_correct = 0

    for run_idx in range(n_bandit_runs):
        gen1 = random.Random(5000 + run_idx)
        obs_arms = [[sample_arm(k, gen1)] for k in range(k_arms)]
        total_pulls = k_arms
        while True:
            lu = [bounds_for_arm(obs_arms[k]) for k in range(k_arms)]
            h_t = max(range(k_arms), key=lambda k: lu[k][0])
            l_ht = lu[h_t][0]
            contenders = [k for k in range(k_arms) if k != h_t and lu[k][1] > l_ht]
            if not contenders:
                if h_t == 0:
                    qlucb_correct += 1
                qlucb_samples.append(total_pulls)
                break
            max_u = max(lu[k][1] for k in contenders)
            l_set = [k for k in contenders if lu[k][1] == max_u]
            for k in [h_t] + l_set:
                bisect.insort(obs_arms[k], sample_arm(k, gen1))
                total_pulls += 1

        # Compare with round-robin uniform sampling using the same stopping criterion
        gen2 = random.Random(5000 + run_idx)
        obs_rr = [[sample_arm(k, gen2)] for k in range(k_arms)]
        rr_pulls = k_arms
        while True:
            lu_rr = [bounds_for_arm(obs_rr[k]) for k in range(k_arms)]
            h_rr = max(range(k_arms), key=lambda k: lu_rr[k][0])
            cont_rr = [k for k in range(k_arms) if k != h_rr and lu_rr[k][1] > lu_rr[h_rr][0]]
            if not cont_rr:
                qpac_samples.append(rr_pulls)
                break
            for k in range(k_arms):
                bisect.insort(obs_rr[k], sample_arm(k, gen2))
                rr_pulls += 1

    mean_qlucb = sum(qlucb_samples) / len(qlucb_samples)
    mean_qpac = sum(qpac_samples) / len(qpac_samples)
    assert qlucb_correct == n_bandit_runs
    assert mean_qlucb < mean_qpac

    return {
        "min_profile_g_minus_true_log_l": round(min_profile_g - log_l_tilde_true, 6),
        "qlucb_accuracy": round(qlucb_correct / n_bandit_runs, 4),
        "qlucb_mean_samples": round(mean_qlucb, 2),
        "uniform_rr_mean_samples": round(mean_qpac, 2),
        "sample_reduction_ratio": round(mean_qpac / mean_qlucb, 4),
    }


def main() -> None:
    results = {
        "galois_inversion_and_martingale": verify_galois_inversion_and_martingale(),
        "fixed_quantile_bounds_and_cauchy_coverage": verify_fixed_quantile_bounds_and_cauchy_coverage(),
        "empirical_process_lil_and_lemma10": verify_empirical_process_lil_and_lemma10(),
        "two_sample_and_qlucb": verify_two_sample_and_qlucb(),
    }
    print(json.dumps(results, sort_keys=True))


if __name__ == "__main__":
    main()
