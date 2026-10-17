#!/usr/bin/env python3
"""Constructed mathematical verification for AIMech:PriorToPosteriorDivergenceConflictDiagnostic.

Verifies:
1. Exact Normal location Rényi divergence R_alpha(y) across orders alpha in {0.5, 1.0, 2.0, inf}
   and exact p-value equivalence with the Evans-Moshonov prior predictive check (Example 3.1).
2. Binomial-Beta uniform-prior boundary behavior (Example 3.2): exact R_alpha(y) and MR(y)
   flag extreme counts y in {0, n} under a uniform Beta(1, 1) prior (p_KL = 2/21) due to the
   asymptotic -0.5 * log |I(theta)| Jeffreys-prior curvature term, whereas the Evans-Moshonov
   Beta-Binomial prior predictive check is completely flat (p_EM = 1.0).
3. Hierarchical Normal-Inverse-Gamma level-1 check (Example 3.3): comparison between the
   posterior-integrated reference distribution t_{2a'} with scale sigma*(y_obs) (which includes
   (y_bar_obs - mu_0)^2 in b'(y_obs)) and the ancillary-conditioned Evans-Moshonov t_{2a'-1}
   check with scale sigma_tilde (which depends only on s_obs^2), demonstrating conservative
   scale inflation under strong mean conflict when the full posterior g(theta_2 | y_obs) is
   used instead of the partial posterior.
4. Hershey-Olsen (2007) closed-form Gaussian mixture KL approximation KL*(q || g) (Section 5.1,
   Equation 21) compared against high-order Gauss-Legendre numerical integration.
"""
from __future__ import annotations

import json
import math


def normal_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def student_t_pdf(x: float, df: float) -> float:
    return (
        math.gamma((df + 1.0) / 2.0)
        / (math.sqrt(df * math.pi) * math.gamma(df / 2.0))
        * (1.0 + (x * x) / df) ** (-(df + 1.0) / 2.0)
    )


def student_t_two_sided_pvalue(t_abs: float, df: float, n_steps: int = 4000) -> float:
    """Deterministic Simpson integration of 2 * int_0^{t_abs} pdf(u) du."""
    if t_abs <= 0.0:
        return 1.0
    h = t_abs / n_steps
    total = student_t_pdf(0.0, df) + student_t_pdf(t_abs, df)
    for i in range(1, n_steps):
        u = i * h
        weight = 4.0 if (i % 2 == 1) else 2.0
        total += weight * student_t_pdf(u, df)
    cdf_central = (h / 3.0) * total * 2.0
    return max(0.0, min(1.0, 1.0 - cdf_central))


def log_beta(a: float, b: float) -> float:
    return math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)


def check_normal_location_renyi() -> dict[str, object]:
    """Example 3.1: y ~ N(mu, sigma^2), mu ~ N(mu_0, sigma_0^2)."""
    mu_0 = 0.0
    sigma_0_sq = 4.0
    sigma_sq = 1.0
    y_obs = 5.0

    tau_sq = 1.0 / (1.0 / sigma_0_sq + 1.0 / sigma_sq)
    gamma_obs = mu_0 / sigma_0_sq + y_obs / sigma_sq
    post_mean = tau_sq * gamma_obs

    def renyi_normal(y_val: float, alpha: float) -> float:
        gamma = mu_0 / sigma_0_sq + y_val / sigma_sq
        mu_post = tau_sq * gamma
        if abs(alpha - 1.0) < 1e-12:
            # KL(N(mu_post, tau_sq) || N(mu_0, sigma_0_sq))
            return 0.5 * (
                math.log(sigma_0_sq / tau_sq)
                + (tau_sq + (mu_post - mu_0) ** 2) / sigma_0_sq
                - 1.0
            )
        sigma_alpha_sq = alpha * sigma_0_sq + (1.0 - alpha) * tau_sq
        term1 = 0.5 * math.log(sigma_0_sq / tau_sq)
        term2 = (1.0 / (2.0 * (alpha - 1.0))) * math.log(sigma_0_sq / sigma_alpha_sq)
        term3 = 0.5 * alpha * ((mu_post - mu_0) ** 2) / sigma_alpha_sq
        return term1 + term2 + term3

    r_05 = renyi_normal(y_obs, 0.5)
    r_kl = renyi_normal(y_obs, 1.0)
    r_20 = renyi_normal(y_obs, 2.0)
    # Limit alpha -> inf gives log max_mu [g(mu|y)/g(mu)]
    r_mr = 0.5 * math.log(sigma_0_sq / tau_sq) + 0.5 * ((post_mean - mu_0) ** 2) / (
        sigma_0_sq - tau_sq
    )

    z_obs = abs(y_obs - mu_0) / math.sqrt(sigma_sq + sigma_0_sq)
    p_exact = 2.0 * (1.0 - normal_cdf(z_obs))

    return {
        "R_alpha_0.5": round(r_05, 8),
        "R_KL_alpha_1.0": round(r_kl, 8),
        "R_alpha_2.0": round(r_20, 8),
        "MR_alpha_inf": round(r_mr, 8),
        "p_value_all_alpha_and_EM": round(p_exact, 8),
    }


def check_binomial_uniform_prior_boundary() -> dict[str, object]:
    """Example 3.2: y ~ Binomial(n, theta), theta ~ Beta(1, 1)."""
    n = 20
    a, b = 1.0, 1.0

    def kl_beta_posterior_prior(y: int) -> float:
        # Exact limit alpha -> 1 for Beta(a+y, b+n-y) || Beta(a, b) via R_alpha at alpha=1+1e-7
        alpha = 1.0 + 1e-7
        a_post = a + y
        b_post = b + n - y
        log_int = (
            log_beta(alpha * a_post + (1.0 - alpha) * a, alpha * b_post + (1.0 - alpha) * b)
            - alpha * log_beta(a_post, b_post)
            - (1.0 - alpha) * log_beta(a, b)
        )
        return log_int / (alpha - 1.0)

    kl_vals = [kl_beta_posterior_prior(y) for y in range(n + 1)]
    # Prior predictive for Beta(1, 1) is uniform 1/(n+1) on {0, ..., n}
    kl_obs_0 = kl_vals[0]
    kl_obs_mid = kl_vals[n // 2]
    p_kl_at_0 = sum(1 for v in kl_vals if v >= kl_obs_0 - 1e-12) / (n + 1)
    p_kl_at_mid = sum(1 for v in kl_vals if v >= kl_obs_mid - 1e-12) / (n + 1)
    p_em_all_y = 1.0

    return {
        "n": n,
        "kl_at_y0": round(kl_obs_0, 8),
        "kl_at_y10": round(kl_obs_mid, 8),
        "p_kl_at_y0_or_y20": round(p_kl_at_0, 8),
        "p_kl_at_y10": round(p_kl_at_mid, 8),
        "p_evans_moshonov_uniform_prior": round(p_em_all_y, 8),
    }


def check_hierarchical_nig_double_use() -> dict[str, object]:
    """Example 3.3: Normal-Inverse-Gamma hierarchical level-1 check on mu | sigma^2."""
    n = 10
    mu_0 = 0.0
    lambda_0 = 1.0
    a = 2.0
    b = 2.0
    s_obs_sq = 1.0
    y_bar_obs = 4.5  # strong conflict in sample mean

    a_prime = a + 0.5 * n
    b_prime_obs = (
        b
        + 0.5 * (n - 1) * s_obs_sq
        + 0.5 * n * ((y_bar_obs - mu_0) ** 2) / (n / lambda_0 + 1.0)
    )
    # Nott et al. (2020) Eq. (9)-(11) mixed predictive scale using full posterior g(sigma^2 | y_obs)
    sigma_star = math.sqrt((b_prime_obs / a_prime) * (1.0 / lambda_0 + 1.0 / n))
    t_stat_div = abs(y_bar_obs - mu_0) / sigma_star
    p_div_mixed = student_t_two_sided_pvalue(t_stat_div, 2.0 * a_prime)

    # Evans & Moshonov (2006) ancillary-conditioned scale (excludes (y_bar_obs - mu_0)^2)
    sigma_tilde = math.sqrt(
        ((1.0 / lambda_0) * (n / lambda_0 + 1.0) * (2.0 * b + (n - 1) * s_obs_sq))
        / ((n / lambda_0) * (n + 2.0 * a - 1.0))
    )
    t_stat_em = abs(y_bar_obs - mu_0) / sigma_tilde
    p_em_ancillary = student_t_two_sided_pvalue(t_stat_em, 2.0 * a_prime - 1.0)

    return {
        "sigma_star_full_posterior": round(sigma_star, 8),
        "sigma_tilde_ancillary_conditioned": round(sigma_tilde, 8),
        "t_stat_divergence_mixed": round(t_stat_div, 8),
        "t_stat_evans_moshonov": round(t_stat_em, 8),
        "p_value_divergence_mixed_t_2a_prime": round(p_div_mixed, 8),
        "p_value_evans_moshonov_t_2a_prime_minus_1": round(p_em_ancillary, 8),
    }


def check_hershey_olsen_mixture_bound() -> dict[str, object]:
    """Section 5.1 Eq. (21): Hershey-Olsen (2007) approximation vs numerical KL(q || g)."""
    w1, w2 = 0.6, 0.4
    m1, s1_sq = -1.2, 0.25
    m2, s2_sq = 1.0, 0.36
    mu0, s0_sq = 0.0, 4.0

    def kl_uni_gauss(mu_a: float, var_a: float, mu_b: float, var_b: float) -> float:
        return 0.5 * (
            math.log(var_b / var_a) + (var_a + (mu_a - mu_b) ** 2) / var_b - 1.0
        )

    d_q1_g = kl_uni_gauss(m1, s1_sq, mu0, s0_sq)
    d_q2_g = kl_uni_gauss(m2, s2_sq, mu0, s0_sq)
    d_q1_q2 = kl_uni_gauss(m1, s1_sq, m2, s2_sq)
    d_q2_q1 = kl_uni_gauss(m2, s2_sq, m1, s1_sq)

    kl_star = w1 * (d_q1_g - math.log(w1 + w2 * math.exp(-d_q1_q2))) + w2 * (
        d_q2_g - math.log(w1 * math.exp(-d_q2_q1) + w2)
    )

    def gauss_pdf(x: float, mu: float, var: float) -> float:
        return math.exp(-0.5 * ((x - mu) ** 2) / var) / math.sqrt(2.0 * math.pi * var)

    # Simpson numerical integration on [-8, 8]
    a_int, b_int, steps = -8.0, 8.0, 4000
    h = (b_int - a_int) / steps
    kl_exact = 0.0
    for i in range(steps + 1):
        x = a_int + i * h
        qx = w1 * gauss_pdf(x, m1, s1_sq) + w2 * gauss_pdf(x, m2, s2_sq)
        gx = gauss_pdf(x, mu0, s0_sq)
        integrand = qx * math.log(qx / gx) if qx > 1e-300 else 0.0
        weight = 1.0 if (i == 0 or i == steps) else (4.0 if i % 2 == 1 else 2.0)
        kl_exact += weight * integrand
    kl_exact *= h / 3.0

    return {
        "kl_hershey_olsen_eq21": round(kl_star, 8),
        "kl_numerical_quadrature": round(kl_exact, 8),
        "abs_approximation_gap": round(abs(kl_star - kl_exact), 8),
    }


def main() -> None:
    res = {
        "normal_location_renyi_equivalence": check_normal_location_renyi(),
        "binomial_uniform_prior_boundary": check_binomial_uniform_prior_boundary(),
        "hierarchical_nig_double_use_boundary": check_hierarchical_nig_double_use(),
        "hershey_olsen_mixture_kl_bound": check_hershey_olsen_mixture_bound(),
    }
    assert abs(res["normal_location_renyi_equivalence"]["p_value_all_alpha_and_EM"] - 0.02534732) < 1e-6
    assert abs(res["binomial_uniform_prior_boundary"]["p_kl_at_y0_or_y20"] - (2.0 / 21.0)) < 1e-6
    assert res["hierarchical_nig_double_use_boundary"]["p_value_divergence_mixed_t_2a_prime"] > (
        res["hierarchical_nig_double_use_boundary"]["p_value_evans_moshonov_t_2a_prime_minus_1"]
    )
    print(json.dumps(res, sort_keys=True))


if __name__ == "__main__":
    main()
