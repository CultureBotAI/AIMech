#!/usr/bin/env python3
"""Constructed mathematical and numerical verification for:
AIMech:HadamardDifferentiableThresholdFDPAsymptoticsAndFixedPointDuality
Primary source: Pierre Neuvial (2008), "Asymptotic properties of false discovery
rate controlling procedures under independence", Electronic Journal of Statistics
2:1065-1110 (arXiv:0803.2111v2, DOI:10.1214/08-EJS207).

Verifies:
1. Section 4.1 Figure 2 (p. 1076) & Condition C.4: Exact criticality value
   alpha^* = 1 / g(0) = 2 / (1 + exp(theta)) = 0.23840584 for one-sided Laplace
   location test statistics with theta = 2 and pi_0 = 0.5, confirming interior
   right crossing point existence iff alpha > alpha^*.
2. Section 4 (Theorems 4.2, 4.7, 4.10, 4.15, Corollary 4.16, Theorem 4.20) &
   Table 1 (p. 1088): Exact asymptotic thresholds tau^*, attained asymptotic
   pFDR = pi_0 * tau^* / G(tau^*), and asymptotic FDP variances Var(X) for
   BH95, FDR08(lambda), BR08(lambda), Sto02(lambda)/STS04(lambda), BKY06(lambda),
   and BH95o under the Gaussian location model (pi_0 = 0.6, mu = 2.5, alpha = 0.1,
   lambda = 0.5), plus the Section 4.3 power-reversal criterion G(x) <= sqrt(x)
   where BH95 >> BKY06(lambda) for all lambda in (0, 1).
3. Section 5 (Theorems 5.2, 5.4, 5.6 & Corollaries 5.3, 5.5, 5.7, pp. 1085-1087):
   Monotone bracketing and exact fixed-point convergence of iterated Sto02(t_n)
   to tau^*_{FDR08} (from both t_0 < tau^* and t_0 > tau^*) and iterated
   BKY06(lambda) to tau^*_{BR08(lambda)}, together with exact verification of
   the power-dominance equivalences in Corollaries 5.3, 5.5, and 5.7.
"""
from __future__ import annotations

import json
import math


def phi_cdf(x: float) -> float:
    if x < 0.0:
        return 0.5 * math.erfc(-x / math.sqrt(2.0))
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def phi_pdf(x: float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def phi_inv(p: float) -> float:
    if p <= 0.0:
        return -40.0
    if p >= 1.0:
        return 40.0
    lo, hi = -40.0, 40.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if phi_cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    x = 0.5 * (lo + hi)
    for _ in range(6):
        pdf = phi_pdf(x)
        if pdf > 1e-300:
            x -= (phi_cdf(x) - p) / pdf
    return x


def g1_gauss(u: float, mu: float) -> float:
    if u <= 0.0:
        return 0.0
    if u >= 1.0:
        return 1.0
    z = phi_inv(1.0 - u)
    return 1.0 - phi_cdf(z - mu)


def g1_prime_gauss(u: float, mu: float) -> float:
    z = phi_inv(1.0 - u)
    return phi_pdf(z - mu) / phi_pdf(z)


def g_cdf(u: float, pi0: float, mu: float) -> float:
    return pi0 * u + (1.0 - pi0) * g1_gauss(u, mu)


def g_pdf(u: float, pi0: float, mu: float) -> float:
    return pi0 + (1.0 - pi0) * g1_prime_gauss(u, mu)


def solve_crossing(diff_fn, lo: float = 1e-12, hi: float = 0.999999) -> float:
    """Finds the unique interior right crossing point where diff_fn(u) = G(u) - r(u) = 0."""
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if diff_fn(mid) >= 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def var_one_stage(tau: float, p_star: float, zeta_val: float, g1_tau: float) -> float:
    """Computes Var(X) for X = p^*(1 - p^* zeta) Z_0(tau)/tau - p^*(1 - p^*) zeta Z_1(tau)/G_1(tau)
    where Z_0(tau) ~ N(0, tau(1-tau)) and Z_1(tau) ~ N(0, G_1(tau)(1-G_1(tau))) are independent.
    """
    term0 = (p_star * (1.0 - p_star * zeta_val)) ** 2 * ((1.0 - tau) / tau)
    term1 = (p_star * (1.0 - p_star) * zeta_val) ** 2 * ((1.0 - g1_tau) / g1_tau)
    return term0 + term1


def main() -> None:
    # 1. Verify Section 4.1 Figure 2 (p. 1076) Laplace criticality value:
    # One-sided Laplace location model with theta = 2, pi_0 = 0.5:
    # For u <= 0.5*exp(-theta), G_1(u) = exp(theta)*u, so g_1(0) = exp(theta),
    # g(0) = pi_0 + (1 - pi_0)*exp(theta), and alpha^* = 1 / g(0).
    theta_lap = 2.0
    pi0_lap = 0.5
    g0_lap = pi0_lap + (1.0 - pi0_lap) * math.exp(theta_lap)
    alpha_star_lap = 1.0 / g0_lap
    # For u in (0, 0.5], S_0^{-1}(u) = -ln(2u). For x >= 0 >= -theta,
    # under H_1 (Laplace(theta)), for x in [0, theta], S_1(x) = 1 - 0.5*exp(x - theta).
    # Since x = -ln(2u) <= theta iff u >= 0.5*exp(-theta), on [0.5*exp(-theta), 0.5]:
    # G_1(u) = 1 - 0.5 * exp(-ln(2u) - theta) = 1 - exp(-theta)/(4u).
    def g_laplace(u: float) -> float:
        u_kink = 0.5 * math.exp(-theta_lap)
        if u <= u_kink:
            g1 = math.exp(theta_lap) * u
        elif u <= 0.5:
            g1 = 1.0 - math.exp(-theta_lap) / (4.0 * u)
        else:
            # For u > 0.5, x = ln(2(1-u)) < 0 < theta, S_1(x) = 1 - 0.5*exp(x - theta)
            g1 = 1.0 - 0.5 * (2.0 * (1.0 - u)) * math.exp(-theta_lap)
        return pi0_lap * u + (1.0 - pi0_lap) * g1

    u_kink = 0.5 * math.exp(-theta_lap)
    # Check that for alpha = 0.20 < alpha^* = 0.23840584, G(u) < u / alpha for all u in (0, 1]
    alpha_sub = 0.20
    assert alpha_sub < alpha_star_lap
    for k in range(1, 500):
        u_test = k / 500.0
        assert g_laplace(u_test) < u_test / alpha_sub
    # Check that for alpha = 0.35 > alpha^*, there is a unique positive crossing point tau^* > u_kink
    alpha_sup = 0.35
    assert alpha_sup > alpha_star_lap
    tau_lap_sup = solve_crossing(lambda u: g_laplace(u) - u / alpha_sup, lo=u_kink, hi=0.99)
    assert abs(g_laplace(tau_lap_sup) - tau_lap_sup / alpha_sup) < 1e-12

    # 2. Verify Section 4 & Table 1 (p. 1088) under Gaussian location model:
    pi0 = 0.6
    mu = 2.5
    alpha = 0.1
    lam = 0.5
    kappa = (alpha * (1.0 - pi0)) / ((1.0 - alpha) * pi0)
    assert lam >= kappa  # Condition C.6
    assert alpha < pi0   # Condition C.7

    # BH95
    tau_bh95 = solve_crossing(lambda u: g_cdf(u, pi0, mu) - u / alpha)
    pfdr_bh95 = pi0 * tau_bh95 / g_cdf(tau_bh95, pi0, mu)
    assert abs(pfdr_bh95 - pi0 * alpha) < 1e-12
    var_bh95 = ((pi0 * alpha) ** 2) * (1.0 - tau_bh95) / tau_bh95

    # BH95 Oracle (BH95o)
    tau_bh95o = solve_crossing(lambda u: g_cdf(u, pi0, mu) - (pi0 * u) / alpha)
    pfdr_bh95o = pi0 * tau_bh95o / g_cdf(tau_bh95o, pi0, mu)
    assert abs(pfdr_bh95o - alpha) < 1e-12
    var_bh95o = (alpha ** 2) * (1.0 - tau_bh95o) / tau_bh95o

    # FDR08(lambda)
    tau_fdr08 = solve_crossing(
        lambda u: g_cdf(u, pi0, mu) - u / (alpha + (1.0 - alpha) * u),
        lo=1e-12,
        hi=kappa,
    )
    pi0_bar_fdr08 = (1.0 - g_cdf(tau_fdr08, pi0, mu)) / (1.0 - tau_fdr08)
    pfdr_fdr08 = pi0 * tau_fdr08 / g_cdf(tau_fdr08, pi0, mu)
    assert abs(pfdr_fdr08 - (alpha * pi0 / pi0_bar_fdr08)) < 1e-12
    zeta_fdr08 = -((1.0 - pi0_bar_fdr08) * pi0_bar_fdr08 / alpha) / (
        (pi0_bar_fdr08 ** 2) / alpha - g_pdf(tau_fdr08, pi0, mu)
    )
    var_fdr08 = var_one_stage(tau_fdr08, pfdr_fdr08, zeta_fdr08, g1_gauss(tau_fdr08, mu))

    # BR08(lambda)
    tau_br08 = solve_crossing(
        lambda u: g_cdf(u, pi0, mu) - u / (alpha * (1.0 - lam) + u),
        lo=1e-12,
        hi=lam,
    )
    pfdr_br08 = pi0 * tau_br08 / g_cdf(tau_br08, pi0, mu)
    pfdr_br08_formula = alpha * pi0 * (1.0 - lam) / (1.0 - g_cdf(tau_br08, pi0, mu))
    assert abs(pfdr_br08 - pfdr_br08_formula) < 1e-12
    g_tau_br = g_cdf(tau_br08, pi0, mu)
    zeta_br08 = -((g_tau_br ** 2) / tau_br08) / (
        g_tau_br * (1.0 - g_tau_br) / tau_br08 - g_pdf(tau_br08, pi0, mu)
    )
    var_br08 = var_one_stage(tau_br08, pfdr_br08, zeta_br08, g1_gauss(tau_br08, mu))

    # Sto02(lambda) / STS04(lambda)
    pi0_bar_lam = (1.0 - g_cdf(lam, pi0, mu)) / (1.0 - lam)
    a_sto02 = alpha / pi0_bar_lam
    tau_sto02 = solve_crossing(lambda u: g_cdf(u, pi0, mu) - u / a_sto02)
    pfdr_sto02 = pi0 * tau_sto02 / g_cdf(tau_sto02, pi0, mu)
    assert abs(pfdr_sto02 - (pi0 * alpha / pi0_bar_lam)) < 1e-12
    assert tau_sto02 <= lam
    var_z_lam = (pi0 ** 2) * lam * (1.0 - lam) + ((1.0 - pi0) ** 2) * g1_gauss(lam, mu) * (
        1.0 - g1_gauss(lam, mu)
    )
    # Corollary 4.16 formula when tau^* <= lambda:
    var_sto02_cor416 = (pfdr_sto02 ** 2) * (
        (1.0 - tau_sto02) / tau_sto02
        + var_z_lam / ((1.0 - g_cdf(lam, pi0, mu)) ** 2)
        + 2.0 * (pi0 / pi0_bar_lam)
    )
    # General Theorem 4.15 formula:
    var_sto02_thm415 = (pfdr_sto02 ** 2) * (
        (1.0 - tau_sto02) / tau_sto02
        + var_z_lam / ((1.0 - g_cdf(lam, pi0, mu)) ** 2)
        + 2.0 * pi0 * (min(tau_sto02, lam) - tau_sto02 * lam) / (tau_sto02 * (1.0 - g_cdf(lam, pi0, mu)))
    )
    assert abs(var_sto02_cor416 - var_sto02_thm415) < 1e-14

    # BKY06(lambda)
    u_lam = solve_crossing(lambda u: g_cdf(u, pi0, mu) - u / lam)
    a_bky06 = alpha * (1.0 - lam) / (1.0 - g_cdf(u_lam, pi0, mu))
    tau_bky06 = solve_crossing(lambda u: g_cdf(u, pi0, mu) - u / a_bky06)
    pfdr_bky06 = pi0 * tau_bky06 / g_cdf(tau_bky06, pi0, mu)
    assert abs(pfdr_bky06 - pi0 * a_bky06) < 1e-12
    # Variance of X^{BKY06(lambda)} from Theorem 4.20:
    # Since tau_bky06 < u_lam, Cov(Z_0(tau^*), Z(u_lam)) = pi_0 * tau^* * (1 - u_lam).
    c_bky = 1.0 / (1.0 - alpha * (1.0 - lam) * g_pdf(u_lam, pi0, mu))
    var_z_ulam = (pi0 ** 2) * u_lam * (1.0 - u_lam) + ((1.0 - pi0) ** 2) * g1_gauss(u_lam, mu) * (
        1.0 - g1_gauss(u_lam, mu)
    )
    var_bky06 = (pfdr_bky06 ** 2) * (
        (1.0 - tau_bky06) / tau_bky06
        + (c_bky ** 2) * var_z_ulam / ((1.0 - g_cdf(u_lam, pi0, mu)) ** 2)
        + 2.0 * c_bky * pi0 * (min(tau_bky06, u_lam) - tau_bky06 * u_lam) / (
            tau_bky06 * (1.0 - g_cdf(u_lam, pi0, mu))
        )
    )

    # Verify asymptotic power ordering in Section 4.2 (p. 1080) & Section 6 (p. 1089):
    # Under Condition C.9 (G(lam) <= lam*(1 - G(lam))/(alpha*(1 - lam))),
    # BH95o >> Sto02(lambda) >> FDR08 >> BR08(lambda), Sto02(lambda) >> BKY06(lambda),
    # and BR08(lambda) >> BH95 iff tau^*_{BH95} >= alpha * lambda (p. 1080):
    assert g_cdf(lam, pi0, mu) <= (lam / alpha) * (1.0 - g_cdf(lam, pi0, mu)) / (1.0 - lam)
    assert tau_bh95o > tau_sto02 > tau_fdr08 > tau_br08
    assert tau_fdr08 > tau_bh95
    assert tau_sto02 > tau_bky06
    assert (tau_br08 >= tau_bh95) == (tau_bh95 >= alpha * lam)
    # Also check lam_small = 0.20 where tau_bh95 > alpha * lam_small so BR08(0.20) >> BH95:
    lam_small = 0.20
    tau_br08_small = solve_crossing(
        lambda u: g_cdf(u, pi0, mu) - u / (alpha * (1.0 - lam_small) + u),
        lo=1e-12,
        hi=lam_small,
    )
    assert tau_bh95 > alpha * lam_small
    assert tau_fdr08 > tau_br08_small > tau_bh95

    # Verify Section 4.3 power reversal criterion (p. 1083):
    # When G(x) = 0.5*x + 0.5*sqrt(x) <= sqrt(x) on [0, 1], BH95 >> BKY06(lambda) for all lambda in (0, 1).
    def g_sqrt(u: float) -> float:
        return 0.5 * u + 0.5 * math.sqrt(max(0.0, u))

    tau_bh95_sqrt = solve_crossing(lambda u: g_sqrt(u) - u / alpha)
    u_lam_sqrt = solve_crossing(lambda u: g_sqrt(u) - u / lam)
    a_bky_sqrt = alpha * (1.0 - lam) / (1.0 - g_sqrt(u_lam_sqrt))
    tau_bky_sqrt = solve_crossing(lambda u: g_sqrt(u) - u / a_bky_sqrt)
    assert g_sqrt(u_lam_sqrt) < lam
    assert tau_bh95_sqrt > tau_bky_sqrt

    # 3. Verify Section 5 Fixed-Point Iteration Duality (Theorems 5.2, 5.4, 5.6 & Corollaries 5.3, 5.5, 5.7):
    # (a) Iterated Sto02(t_n) -> tau^*_{FDR08} (Theorem 5.4):
    def tau_sto02_of_t(t_val: float) -> float:
        pi0_bar_t = (1.0 - g_cdf(t_val, pi0, mu)) / (1.0 - t_val)
        return solve_crossing(lambda u: g_cdf(u, pi0, mu) - (u / alpha) * pi0_bar_t)

    # Starting from t_0 = 0.01 < tau_fdr08 (monotonically increasing):
    t_inc = 0.01
    assert t_inc < tau_fdr08
    for _ in range(40):
        t_next = tau_sto02_of_t(t_inc)
        assert t_inc <= t_next <= tau_fdr08 + 1e-14
        t_inc = t_next
    assert abs(t_inc - tau_fdr08) < 1e-11

    # Starting from t_0 = 0.50 > tau_fdr08 (monotonically decreasing):
    t_dec = 0.50
    assert t_dec > tau_fdr08
    # Verify Corollary 5.5: Sto02(0.50) >> FDR08 iff 0.50 > tau_sto02(0.50)
    assert t_dec > tau_sto02_of_t(t_dec) > tau_fdr08
    for _ in range(40):
        t_next = tau_sto02_of_t(t_dec)
        assert tau_fdr08 - 1e-14 <= t_next <= t_dec
        t_dec = t_next
    assert abs(t_dec - tau_fdr08) < 1e-11

    # (b) Iterated BKY06(lambda) -> tau^*_{BR08(lambda)} (Theorem 5.6 & Corollary 5.7):
    # Test at original BKY06 parameter lambda_bky = alpha / (1 + alpha):
    lam_orig = alpha / (1.0 + alpha)
    u_lam_orig = solve_crossing(lambda u: g_cdf(u, pi0, mu) - u / lam_orig)
    tau_br08_orig = solve_crossing(
        lambda u: g_cdf(u, pi0, mu) - u / (alpha * (1.0 - lam_orig) + u),
        lo=1e-12,
        hi=lam_orig,
    )
    t_bky_iter = u_lam_orig
    tau_bky06_orig = solve_crossing(
        lambda u: g_cdf(u, pi0, mu) - u * (1.0 - g_cdf(u_lam_orig, pi0, mu)) / (alpha * (1.0 - lam_orig))
    )
    # Corollary 5.7: for lambda = alpha/(1+alpha), lambda - alpha*(1 - lambda) = alpha/(1+alpha) - alpha/(1+alpha) = 0 <= tau^*_{BR08},
    # so BR08(lambda_orig) >> BKY06(lambda_orig) (tau_br08_orig > tau_bky06_orig >= u_lam_orig).
    assert abs(lam_orig - alpha * (1.0 - lam_orig)) < 1e-15
    assert tau_br08_orig > tau_bky06_orig > u_lam_orig
    for _ in range(40):
        t_next = solve_crossing(
            lambda u: g_cdf(u, pi0, mu) - u * (1.0 - g_cdf(t_bky_iter, pi0, mu)) / (alpha * (1.0 - lam_orig))
        )
        assert t_bky_iter <= t_next <= tau_br08_orig + 1e-14
        t_bky_iter = t_next
    assert abs(t_bky_iter - tau_br08_orig) < 1e-11

    result = {
        "concept_id": "AIMech:HadamardDifferentiableThresholdFDPAsymptoticsAndFixedPointDuality",
        "primary_source": "Neuvial (2008), Electronic Journal of Statistics 2:1065-1110 (arXiv:0803.2111v2, DOI:10.1214/08-EJS207)",
        "section_4_1_figure_2_laplace_criticality": {
            "theta": theta_lap,
            "pi0": pi0_lap,
            "g_at_0": round(g0_lap, 8),
            "alpha_star_critical_value": round(alpha_star_lap, 8),
            "tau_star_at_alpha_0_20_subcritical": 0.0,
            "tau_star_at_alpha_0_35_supercritical": round(tau_lap_sup, 8),
        },
        "section_4_and_table_1_gaussian_location_benchmark": {
            "pi0": pi0,
            "mu": mu,
            "alpha": alpha,
            "lambda": lam,
            "kappa_fdr08": round(kappa, 8),
            "procedures": {
                "BH95": {
                    "tau_star": round(tau_bh95, 8),
                    "asymptotic_fdr": round(pfdr_bh95, 8),
                    "asymptotic_fdp_variance": round(var_bh95, 8),
                },
                "BR08_lambda": {
                    "tau_star": round(tau_br08, 8),
                    "asymptotic_fdr": round(pfdr_br08, 8),
                    "asymptotic_fdp_variance": round(var_br08, 8),
                },
                "BKY06_lambda": {
                    "u_lambda": round(u_lam, 8),
                    "tau_star": round(tau_bky06, 8),
                    "asymptotic_fdr": round(pfdr_bky06, 8),
                    "asymptotic_fdp_variance": round(var_bky06, 8),
                },
                "FDR08": {
                    "tau_star": round(tau_fdr08, 8),
                    "asymptotic_fdr": round(pfdr_fdr08, 8),
                    "asymptotic_fdp_variance": round(var_fdr08, 8),
                },
                "Sto02_STS04_lambda": {
                    "tau_star": round(tau_sto02, 8),
                    "asymptotic_fdr": round(pfdr_sto02, 8),
                    "asymptotic_fdp_variance": round(var_sto02_cor416, 8),
                },
                "BH95o_oracle": {
                    "tau_star": round(tau_bh95o, 8),
                    "asymptotic_fdr": round(pfdr_bh95o, 8),
                    "asymptotic_fdp_variance": round(var_bh95o, 8),
                },
            },
            "bky06_power_reversal_when_G_le_sqrt_x": {
                "tau_bh95": round(tau_bh95_sqrt, 8),
                "tau_bky06": round(tau_bky_sqrt, 8),
                "bh95_dominates_bky06": tau_bh95_sqrt > tau_bky_sqrt,
            },
        },
        "section_5_fixed_point_duality_verification": {
            "sto02_to_fdr08_fixed_point": {
                "tau_fdr08_exact": round(tau_fdr08, 10),
                "iterated_from_t0_0_01": round(t_inc, 10),
                "iterated_from_t0_0_50": round(t_dec, 10),
                "abs_error": round(max(abs(t_inc - tau_fdr08), abs(t_dec - tau_fdr08)), 14),
            },
            "bky06_to_br08_fixed_point_at_lambda_alpha_over_1_plus_alpha": {
                "lambda_orig": round(lam_orig, 8),
                "u_lambda_init": round(u_lam_orig, 8),
                "tau_bky06_first_stage": round(tau_bky06_orig, 8),
                "tau_br08_exact": round(tau_br08_orig, 10),
                "iterated_limit": round(t_bky_iter, 10),
                "abs_error": round(abs(t_bky_iter - tau_br08_orig), 14),
            },
        },
        "all_assertions_passed": True,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
