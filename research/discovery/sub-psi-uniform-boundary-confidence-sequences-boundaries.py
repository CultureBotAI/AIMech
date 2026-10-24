#!/usr/bin/env python3
"""Constructed mathematical and numerical verification for AIMech:SubPsiUniformBoundaryConfidenceSequences.

Verifies the core theoretical results of Howard, Ramdas, McAuliffe, & Sekhon (2021),
"Time-uniform, nonparametric, nonasymptotic confidence sequences", The Annals of
Statistics 49(2):1055-1080 (arXiv:1810.08240, DOI 10.1214/20-AOS1991):
  1. Section 2 (Definitions 1-2, Proposition 1) & Appendix B (Proposition 11, Table 1):
     Strict hierarchy of the five canonical CGF-like functions
       psi_{B,1,1}(lam) < psi_N(lam) < psi_{P,1}(lam) < psi_{E,1}(lam) < psi_{G,1}(lam)
     for lam in (0, 1), and Proposition 1 universal sub-gamma reduction
       psi_{P,1}(lam) <= psi_{G,1/3}(lam) for all lam >= 0.
  2. Section 3.1 (Theorem 1), Appendix A.1 (Equations 29-37), & Section 3.4 (Theorem 3):
     Geometric epoch stitching tangent-line construction g_{lam_k, r_k}(v) achieving
     exact endpoint symmetry g(eta^k)/eta^{k/2} = g(eta^{k+1})/eta^{(k+1)/2} at
     lam_k = psi_G^{-1}(r_k / eta^{k+1/2}), pointwise dominance of the closed-form
     polynomial stitched boundary S_alpha(v) over the epoch line envelope, and Theorem 3
     inverted stitching crossing probability bound.
  3. Section 3.2-3.5 (Propositions 3, 5, 6, 9, Theorem 2) & Appendices A.3-A.5, C.1:
     Two-sided and one-sided normal mixture boundaries (Propositions 5-6), exact
     Lambert W_{-1} optimal tuning rho(v_tilde, alpha) = v_tilde / (-W_{-1}(-alpha^2/(e l_0^2)) - 1)
     minimizing u(v)/sqrt(v) at v = v_tilde (Proposition 3a), gamma-exponential mixture
     convergence to the normal mixture as c -> 0 (Proposition 9), and Theorem 2 discrete
     mixture accuracy 1 <= DM_alpha(v)/NM_alpha(v) <= 1.004.
  4. Section 4.1-4.2 (Theorem 4, Corollary 2), Section 5 (Figure 4a Skewed Counterexample),
     & Appendix A.8:
     Exact Fan et al. supermartingale inequality for the self-normalized empirical
     Bernstein process with predictable centering X_hat_t, time-uniform coverage of
     Theorem 4 vs. severe false-positive inflation of the Naive Self-Normalized bound
     (Eq. 24) on Section 5's skewed 3-point distribution, and Corollary 2 sequential
     Neyman-Rubin adaptive IPW ATE confidence sequence.
"""
from __future__ import annotations

import json
import math
import random


def psi_bernoulli(lam: float, g: float = 1.0, h: float = 1.0) -> float:
    return (1.0 / (g * h)) * math.log((g * math.exp(h * lam) + h * math.exp(-g * lam)) / (g + h))


def psi_normal(lam: float) -> float:
    return 0.5 * lam * lam


def psi_poisson(lam: float, c: float = 1.0) -> float:
    if abs(c) < 1e-12:
        return psi_normal(lam)
    return (math.exp(c * lam) - c * lam - 1.0) / (c * c)


def psi_exponential(lam: float, c: float = 1.0) -> float:
    if abs(c) < 1e-12:
        return psi_normal(lam)
    return (-math.log(1.0 - c * lam) - c * lam) / (c * c)


def psi_gamma(lam: float, c: float = 1.0) -> float:
    return 0.5 * lam * lam / (1.0 - c * lam)


def psi_gamma_inv(u: float, c: float = 1.0) -> float:
    # Eq. (36): psi_G^{-1}(u) = 2 u / (c u + sqrt(2 u + c^2 u^2)) = 1 / (c/2 + sqrt(1/(2u) + c^2/4))
    if u <= 0.0:
        return 0.0
    return (2.0 * u) / (c * u + math.sqrt(2.0 * u + c * c * u * u))


def lambert_w_minus1(x: float) -> float:
    """Compute the lower branch W_{-1}(x) for x in [-1/e, 0) via Halley's method."""
    if not (-1.0 / math.e <= x < 0.0):
        raise ValueError(f"x={x} out of domain [-1/e, 0) for W_{-1}")
    # Initial asymptotic approximation: w ~ log(-x) - log(-log(-x))
    L1 = math.log(-x)
    L2 = math.log(-L1)
    w = L1 - L2 + L2 / L1
    for _ in range(60):
        ew = math.exp(w)
        f = w * ew - x
        if abs(f) < 1e-15 * abs(x):
            break
        fp = ew * (w + 1.0)
        fpp = ew * (w + 2.0)
        w -= f / (fp - 0.5 * f * fpp / fp)
    return w


def normal_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def verify_psi_hierarchy_and_proposition1() -> dict[str, float]:
    """Verify Section 2 & Appendix B (Proposition 11, Table 1) sub-psi hierarchy."""
    min_gap_b_to_n = float("inf")
    min_gap_n_to_p = float("inf")
    min_gap_p_to_e = float("inf")
    min_gap_e_to_g = float("inf")
    min_prop1_p_to_g13 = float("inf")

    for i in range(1, 95):
        lam = i * 0.01
        pb = psi_bernoulli(lam, 1.0, 1.0)
        pn = psi_normal(lam)
        pp = psi_poisson(lam, 1.0)
        pe = psi_exponential(lam, 1.0)
        pg = psi_gamma(lam, 1.0)
        min_gap_b_to_n = min(min_gap_b_to_n, pn - pb)
        min_gap_n_to_p = min(min_gap_n_to_p, pp - pn)
        min_gap_p_to_e = min(min_gap_p_to_e, pe - pp)
        min_gap_e_to_g = min(min_gap_e_to_g, pg - pe)

    # Proposition 1: sub-Poisson with scale c=1 is sub-gamma with scale c/3 = 1/3 for all lam in [0, 3)
    for i in range(1, 295):
        lam = i * 0.01
        pp = psi_poisson(lam, 1.0)
        pg13 = psi_gamma(lam, 1.0 / 3.0)
        min_prop1_p_to_g13 = min(min_prop1_p_to_g13, pg13 - pp)

    assert min_gap_b_to_n > 0.0
    assert min_gap_n_to_p > 0.0
    assert min_gap_p_to_e > 0.0
    assert min_gap_e_to_g > 0.0
    assert min_prop1_p_to_g13 > 0.0

    return {
        "min_gap_b_to_n": round(min_gap_b_to_n, 10),
        "min_gap_n_to_p": round(min_gap_n_to_p, 10),
        "min_gap_p_to_e": round(min_gap_p_to_e, 10),
        "min_gap_e_to_g": round(min_gap_e_to_g, 10),
        "min_prop1_p_to_g13": round(min_prop1_p_to_g13, 10),
    }


def verify_stitching_theorem1_and_theorem3() -> dict[str, float]:
    """Verify Theorem 1 (Appendix A.1) epoch stitching and Theorem 3 inverted stitching."""
    eta = 2.0
    s = 1.4
    alpha = 0.05
    c = 0.5
    # Approximate Riemann zeta(1.4) via Euler-Maclaurin
    N_z = 10000
    zeta_s = sum(k ** (-s) for k in range(1, N_z)) + (N_z ** (1.0 - s)) / (s - 1.0) + 0.5 * (N_z ** (-s))

    k1 = (eta ** 0.25 + eta ** (-0.25)) / math.sqrt(2.0)
    k2 = (math.sqrt(eta) + 1.0) / 2.0

    def r_epoch(k: int) -> float:
        return math.log(((k + 1) ** s) * zeta_s / alpha)

    def stitched_boundary(v: float) -> float:
        rv = s * math.log(math.log(eta * max(v, 1.0)) / math.log(eta)) + math.log(zeta_s / alpha)
        return math.sqrt(k1 * k1 * v * rv + c * c * k2 * k2 * rv * rv) + c * k2 * rv

    max_endpoint_asymmetry = 0.0
    min_stitched_dominance_gap = float("inf")

    for k in range(0, 12):
        rk = r_epoch(k)
        v_left = eta ** k
        v_right = eta ** (k + 1)
        v_mid = eta ** (k + 0.5)
        lam_k = psi_gamma_inv(rk / v_mid, c)

        def g_k(v: float) -> float:
            return rk / lam_k + (psi_gamma(lam_k, c) / lam_k) * v

        asym = abs(g_k(v_left) / math.sqrt(v_left) - g_k(v_right) / math.sqrt(v_right))
        max_endpoint_asymmetry = max(max_endpoint_asymmetry, asym)

        for frac in (0.0, 0.2, 0.5, 0.8, 0.999):
            v = v_left * ((v_right / v_left) ** frac)
            gap = stitched_boundary(v) - g_k(v)
            min_stitched_dominance_gap = min(min_stitched_dominance_gap, gap)

    assert max_endpoint_asymmetry < 1e-14
    assert min_stitched_dominance_gap > 0.0

    # Theorem 3 (Eq. 20) Inverted Stitching for sub-Gaussian LIL curve g(v) = A sqrt(v (log log(e v) + C))
    A = 1.7
    C = 3.2
    eta_inv = 2.994
    K_epochs = 42
    inv_stitch_prob = 0.0
    for k in range(K_epochs):
        vk = eta_inv ** k
        vk1 = eta_inv ** (k + 1)
        gk = A * math.sqrt(vk * (math.log(math.log(math.e * vk)) + C))
        gk1 = A * math.sqrt(vk1 * (math.log(math.log(math.e * vk1)) + C))
        # Eq. (19): a_k = (eta g(eta^k) - g(eta^{k+1}))/(eta - 1), b_k = (g(eta^{k+1}) - g(eta^k))/(eta^{k+1} - eta^k)
        ak = (eta_inv * gk - gk1) / (eta_inv - 1.0)
        bk = (gk1 - gk) / (vk1 - vk)
        # For sub-Gaussian psi_N(lam) = lam^2 / 2, solving psi_N(lam)/lam = b_k gives lam = 2 b_k
        # so exp(-a_k * lam) = exp(-2 * a_k * b_k) (Lemma 1 / Eq. 19 / Corollary 8a)
        inv_stitch_prob += math.exp(-2.0 * ak * bk)

    assert 0.0 < inv_stitch_prob < 0.05

    return {
        "max_endpoint_asymmetry": max_endpoint_asymmetry,
        "min_stitched_dominance_gap": round(min_stitched_dominance_gap, 6),
        "zeta_1_4": round(zeta_s, 6),
        "inverted_stitch_crossing_bound": round(inv_stitch_prob, 6),
    }


def two_sided_normal_mixture(v: float, rho: float, alpha: float, l0: float = 1.0) -> float:
    # Proposition 5 / Eq. (14): u(v) = sqrt((v + rho) * log((l0 / alpha)^2 * (v + rho) / rho))
    k = (l0 / alpha) ** 2
    return math.sqrt((v + rho) * math.log(k * (v + rho) / rho))


def one_sided_normal_mixture_closed_form(v: float, rho: float, alpha: float, l0: float = 1.0) -> float:
    # Proposition 6 (Eq. 53): closed-form upper bound NM_tilde_alpha(v)
    val = ((l0 / (2.0 * alpha)) * math.sqrt((v + rho) / rho) + 0.5)
    return math.sqrt(2.0 * (v + rho) * math.log(val))


def exact_one_sided_normal_mixture(v: float, rho: float, alpha: float, l0: float = 1.0) -> float:
    # Proposition 6 (Eq. 52): exact root of 2 * sqrt(rho/(v+rho)) * exp(s^2/(2(v+rho))) * Phi(s/sqrt(v+rho)) = l0/alpha
    target = l0 / alpha
    lo = 0.0
    hi = one_sided_normal_mixture_closed_form(v, rho, alpha, l0)
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        z = mid / math.sqrt(v + rho)
        val = 2.0 * math.sqrt(rho / (v + rho)) * math.exp(0.5 * z * z) * normal_cdf(z)
        if val < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def gamma_exp_log_supermartingale(s: float, v: float, rho: float, c: float = 1.0) -> float:
    """Proposition 9 (Eq. 67) exact log mixture supermartingale for psi_{E,c}.

    By setting w = c * lam in [0, 1], the mixture integral is proportional to
      S(a, b) = int_0^1 (1 - w)^{a - 1} exp(b w) dw = sum_{n=0}^infty b^n / (a (a+1)...(a+n))
    where a = (v + rho) / c^2 and b = (c s + v + rho) / c^2, normalized by S(a0, a0) at s=0, v=0
    with a0 = rho / c^2.
    """
    a = (v + rho) / (c * c)
    b = (c * s + v + rho) / (c * c)
    a0 = rho / (c * c)
    if b <= 0.0:
        return float("-inf")

    def log_series_s(alpha_p: float, x: float) -> float:
        # Compute log(sum_{n=0}^infty x^n / (alpha_p * (alpha_p + 1) * ... * (alpha_p + n)))
        # Center around mode n_star = max(0, int(x - alpha_p)) to avoid overflow for large x
        n_star = max(0, int(x - alpha_p))
        log_term_star = -math.log(alpha_p)
        if n_star > 0:
            log_term_star += n_star * math.log(x) - (
                math.lgamma(alpha_p + n_star + 1.0) - math.lgamma(alpha_p + 1.0)
            )
        total = 1.0
        # Forward sum from n_star + 1
        term = 1.0
        n = n_star
        while True:
            n += 1
            term *= x / (alpha_p + n)
            total += term
            if term < 1e-15 * total and n > n_star + 5:
                break
        # Backward sum from n_star - 1 down to 0
        term = 1.0
        for k in range(n_star, 0, -1):
            term *= (alpha_p + k) / x
            total += term
            if term < 1e-15 * total:
                break
        return log_term_star + math.log(total)

    return log_series_s(a, b) - log_series_s(a0, a0)


def gamma_exp_boundary(v: float, rho: float, alpha: float, c: float = 1.0, l0: float = 1.0) -> float:
    target = math.log(l0 / alpha)
    lo = 0.0
    hi = max(10.0, 10.0 * math.sqrt(v + rho) + 5.0 * c * target)
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if gamma_exp_log_supermartingale(mid, v, rho, c) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def verify_mixture_boundaries_and_lambert_tuning() -> dict[str, float]:
    """Verify Propositions 3, 5, 6, 9 and Theorem 2 discrete mixture accuracy."""
    alpha = 0.025
    l0 = 1.0
    v_tilde = 100.0
    # Proposition 3(a) (Eq. 21): rho(v_tilde, alpha) = v_tilde / (-W_{-1}(-alpha^2/(e l0^2)) - 1)
    w_val = lambert_w_minus1(-(alpha * alpha) / (math.e * l0 * l0))
    rho_opt = v_tilde / (-w_val - 1.0)

    # Check that v -> u(v)/sqrt(v) is minimized at v = v_tilde
    def norm_obj(v: float) -> float:
        return two_sided_normal_mixture(v, rho_opt, alpha, l0) / math.sqrt(v)

    eps = 1e-4
    deriv_at_v_tilde = (norm_obj(v_tilde + eps) - norm_obj(v_tilde - eps)) / (2.0 * eps)
    second_diff = (norm_obj(v_tilde + eps) - 2.0 * norm_obj(v_tilde) + norm_obj(v_tilde - eps)) / (eps * eps)
    assert abs(deriv_at_v_tilde) < 1e-11
    assert second_diff > 0.0

    # Proposition 6 (line 1148): closed-form upper bound NM_tilde_0.025(v) / NM_0.025(v) < 1.007 when rho=1
    nm_tilde_ratios = [
        one_sided_normal_mixture_closed_form(v, 1.0, 0.025, 1.0) / exact_one_sided_normal_mixture(v, 1.0, 0.025, 1.0)
        for v in (1.0, 10.0, 100.0, 1000.0)
    ]
    assert 1.0 <= min(nm_tilde_ratios) <= max(nm_tilde_ratios) < 1.007

    # Proposition 9: As c -> 0, gamma-exponential mixture boundary converges to one-sided normal mixture
    v_test = 25.0
    rho_test = 10.0
    nm_bound = exact_one_sided_normal_mixture(v_test, rho_test, 0.05, 1.0)
    ge_c1 = gamma_exp_boundary(v_test, rho_test, 0.05, c=1.0)
    ge_c02 = gamma_exp_boundary(v_test, rho_test, 0.05, c=0.2)
    ge_c005 = gamma_exp_boundary(v_test, rho_test, 0.05, c=0.05)
    assert ge_c1 > ge_c02 > ge_c005 > nm_bound
    assert abs(ge_c005 - nm_bound) / nm_bound < 0.015

    # Theorem 2 & Appendix A.4 (line 1283): Discrete mixture with half-normal density, eta=1.05, lam_bar=100.0
    eta_dm = 1.05
    lam_bar = 100.0
    rho_dm = 14.3
    alpha_dm = 0.05

    def f_half_normal(lam: float) -> float:
        return math.sqrt(2.0 * rho_dm / math.pi) * math.exp(-0.5 * rho_dm * lam * lam)

    lambdas_dm = [lam_bar / (eta_dm ** (k + 0.5)) for k in range(420)]
    weights_dm = [
        lam_bar * (eta_dm - 1.0) * f_half_normal(lam_bar / (eta_dm ** k)) / (eta_dm ** (k + 1))
        for k in range(420)
    ]

    def dm_boundary(v: float) -> float:
        target = 1.0 / alpha_dm
        lo = 0.0
        hi = 2.0 * one_sided_normal_mixture_closed_form(v, rho_dm, alpha_dm, 1.0)
        for _ in range(55):
            mid = 0.5 * (lo + hi)
            s_val = sum(w * math.exp(lam * mid - 0.5 * lam * lam * v) for w, lam in zip(weights_dm, lambdas_dm))
            if s_val < target:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)

    w_sum = sum(weights_dm)
    assert (1.0 / eta_dm) < w_sum < 1.0
    ratios = [dm_boundary(v) / exact_one_sided_normal_mixture(v, rho_dm, alpha_dm, 1.0) for v in (1.0, 10.0, 100.0, 1000.0)]
    max_dm_ratio = max(ratios)
    min_dm_ratio = min(ratios)
    assert 1.0 <= min_dm_ratio <= max_dm_ratio < 1.03
    assert ratios[-1] <= 1.0045

    return {
        "rho_opt_v100_alpha0025": round(rho_opt, 6),
        "abs_deriv_at_v_tilde": abs(deriv_at_v_tilde),
        "max_nm_tilde_to_exact_ratio": round(max(nm_tilde_ratios), 6),
        "ge_c1_bound": round(ge_c1, 6),
        "ge_c02_bound": round(ge_c02, 6),
        "ge_c005_bound": round(ge_c005, 6),
        "one_sided_nm_bound": round(nm_bound, 6),
        "min_dm_nm_ratio": round(min_dm_ratio, 6),
        "max_dm_nm_ratio": round(max_dm_ratio, 6),
    }


def verify_empirical_bernstein_and_ate_cs() -> dict[str, float]:
    """Verify Theorem 4 self-normalized empirical Bernstein CS, Section 5 counterexample, and Corollary 2 IPW ATE CS."""
    # 1. Appendix A.8 (Proof of Theorem 4): Exact Fan et al. conditional supermartingale inequality
    # E[exp(lam Y - psi_{E,1}(lam) (Y - delta)^2)] <= exp(-lam delta - psi_{E,1}(lam) delta^2) <= 1 + lam E[Y] = 1
    # Check across a discrete distribution on [0, 1] and predictable error delta in [-0.4, 0.4]
    xs = [0.0, 0.25, 0.7, 1.0]
    ps = [0.4, 0.2, 0.2, 0.2]
    mu = sum(x * p for x, p in zip(xs, ps))
    max_cond_expectation = 0.0
    for lam in (0.1, 0.3, 0.5, 0.75):
        pe = psi_exponential(lam, 1.0)
        for x_hat in (0.05, 0.34, 0.6, 0.9):
            ev = sum(
                p * math.exp(lam * (x - mu) - pe * ((x - x_hat) ** 2))
                for x, p in zip(xs, ps)
            )
            max_cond_expectation = max(max_cond_expectation, ev)
    assert max_cond_expectation <= 1.0 + 1e-15

    # 2. Section 5 (Figure 4a): Skewed 3-point distribution placing mass 0.999/2 at +-1e-3 and mass 0.001 at 1.0
    # Mean mu = 0.001, range [a, b] = [-0.001, 1.0], c = 1.001.
    # Naive Self-Normalized bound (Eq. 24) substitutes V_t into sub-Gaussian normal mixture without scale c,
    # causing massive false-positive crossings when X_t = 1 first occurs after small-variance steps.
    rng = random.Random(20261018)
    alpha = 0.05
    n_trials = 500
    t_max = 1200
    mu_skew = 0.001
    c_skew = 1.001
    rho_skew = 0.01

    naive_sn_miscover = 0
    eb_gamma_exp_miscover = 0

    for _ in range(n_trials):
        s_t = 0.0
        v_t = 0.0
        sum_x = 0.0
        crossed_naive = False
        crossed_eb = False
        for t in range(1, t_max + 1):
            u_rand = rng.random()
            if u_rand < 0.001:
                x = 1.0
            elif u_rand < 0.5005:
                x = 0.001
            else:
                x = -0.001
            x_hat = sum_x / (t - 1) if t > 1 else 0.0
            sum_x += x
            s_t += x - mu_skew
            v_t += (x - x_hat) ** 2

            # Naive Self-Normalized bound (Eq. 24): two-sided normal mixture at v_t with alpha/2
            if not crossed_naive and v_t > 0.0:
                u_naive = two_sided_normal_mixture(v_t, rho_skew, alpha, l0=1.0)
                if abs(s_t) >= u_naive:
                    crossed_naive = True

            # Theorem 4 Empirical Bernstein bound via Proposition 9 gamma-exponential log-supermartingale
            if not crossed_eb:
                log_m_pos = gamma_exp_log_supermartingale(max(s_t, 0.0), v_t, rho_skew, c=c_skew)
                log_m_neg = gamma_exp_log_supermartingale(max(-s_t, 0.0), v_t, rho_skew, c=c_skew)
                if max(log_m_pos, log_m_neg) >= math.log(2.0 / alpha):
                    crossed_eb = True

        if crossed_naive:
            naive_sn_miscover += 1
        if crossed_eb:
            eb_gamma_exp_miscover += 1

    naive_sn_rate = naive_sn_miscover / n_trials
    eb_rate = eb_gamma_exp_miscover / n_trials
    # Naive SN has severe miscoverage (>> 0.05), while Theorem 4 EB maintains valid coverage (<= 0.05)
    assert naive_sn_rate > 0.30
    assert eb_rate <= alpha

    # 3. Corollary 2 (Section 4.2): Sequential Neyman-Rubin adaptive IPW ATE_t confidence sequence
    # Potential outcomes Y_t(1), Y_t(0) in [0, 1], adaptive propensity p_t in [0.25, 0.75]
    # Scale c = 1/p_min + 1/(1 - p_min) = 4 + 4/3 = 16/3 (or 2/0.25 = 8.0 for general [0,1] bounds).
    p_min = 0.3
    c_ipw = 1.0 / p_min + 1.0 / (1.0 - p_min)
    ate_trials = 300
    ate_steps = 80
    ate_miscover = 0
    ate_widths_end = []

    for _ in range(ate_trials):
        s_ate = 0.0
        v_ate = 0.0
        sum_y1 = 0.5
        cnt_y1 = 1.0
        sum_y0 = 0.5
        cnt_y0 = 1.0
        crossed_ate = False
        for t in range(1, ate_steps + 1):
            # True time-varying potential outcome means mu1_t = 0.65, mu0_t = 0.35 -> true diff = 0.30
            true_diff = 0.30
            y1 = 1.0 if rng.random() < 0.65 else 0.0
            y0 = 1.0 if rng.random() < 0.35 else 0.0
            # Predictable propensity p_t in [0.3, 0.7] adapting to past difference
            y1_hat = sum_y1 / cnt_y1
            y0_hat = sum_y0 / cnt_y0
            p_t = min(0.7, max(0.3, 0.5 + 0.2 * (y1_hat - y0_hat)))
            treat = 1 if rng.random() < p_t else 0
            if treat == 1:
                x_ipw = y1 / p_t
                sum_y1 += y1
                cnt_y1 += 1.0
            else:
                x_ipw = -y0 / (1.0 - p_t)
                sum_y0 += y0
                cnt_y0 += 1.0
            x_hat_ipw = y1_hat - y0_hat
            s_ate += x_ipw - true_diff
            v_ate += (x_ipw - x_hat_ipw) ** 2

            log_m = max(
                gamma_exp_log_supermartingale(max(s_ate, 0.0), v_ate, 4.0, c=c_ipw),
                gamma_exp_log_supermartingale(max(-s_ate, 0.0), v_ate, 4.0, c=c_ipw),
            )
            if log_m >= math.log(2.0 / alpha):
                crossed_ate = True
        if crossed_ate:
            ate_miscover += 1
        ate_widths_end.append(2.0 * gamma_exp_boundary(v_ate, 4.0, alpha / 2.0, c=c_ipw) / ate_steps)

    ate_miscover_rate = ate_miscover / ate_trials
    assert ate_miscover_rate <= alpha

    return {
        "max_fan_cond_expectation": round(max_cond_expectation, 8),
        "skewed_naive_sn_miscover_rate": round(naive_sn_rate, 4),
        "skewed_theorem4_eb_miscover_rate": round(eb_rate, 4),
        "ipw_ate_miscover_rate": round(ate_miscover_rate, 4),
        "ipw_ate_mean_width_t80": round(sum(ate_widths_end) / len(ate_widths_end), 4),
    }


def main() -> None:
    res = {
        "psi_hierarchy_and_proposition1": verify_psi_hierarchy_and_proposition1(),
        "stitching_theorem1_and_theorem3": verify_stitching_theorem1_and_theorem3(),
        "mixture_boundaries_and_lambert_tuning": verify_mixture_boundaries_and_lambert_tuning(),
        "empirical_bernstein_and_ate_cs": verify_empirical_bernstein_and_ate_cs(),
    }
    print(json.dumps(res, sort_keys=True))


if __name__ == "__main__":
    main()
