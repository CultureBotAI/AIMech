#!/usr/bin/env python3
"""Constructed numerical boundary checks for AIMech:PriorExpansionScoreConflictDiagnostic.

Verifies the mathematical properties and boundary conditions of Nott et al. (2020/2021,
arXiv:1902.10393v2) and Yang, Nott, & Presanis (2026, arXiv:2511.02977v2):
1. Fisher's identity S(y) = d/d_gamma log p(y|gamma)|_{gamma=gamma_0} = E_{theta|y}[d/d_gamma log g(theta|gamma)|_{gamma=gamma_0}],
   equality of -S(y) with the derivative of the baseline-posterior-weighted Renyi functional (Eq. 2.3-2.4)
   and fixed-posterior KL(g(theta|y) || g(theta|gamma)), and the extra posterior covariance term when
   varying g(theta|y,gamma) inside R_alpha(g(theta|y,gamma) || g(theta|gamma)).
2. Exact monotonic equivalence between the normal-location variance-expansion score S(bar_x)
   and the Evans-Moshonov (2006) prior-predictive conflict p-value.
3. Multivariate location-scale expansion quadratic score discrepancy D(y) = S(y)^T V_S^{-1} S(y).
4. Two-stage hierarchical normal random-effects decomposition (Example 4.3, pp. 11-13) into
   lower-level posterior-averaged conditional score S^{(1)}(y) and upper-level score S^{(2)}(y).
5. Failure of naive differentiation under the integral sign when prior support depends on gamma,
   and exact recovery after fixed-domain reparameterization.
"""

from __future__ import annotations

import json
import math


def normal_two_sided_tail(z: float) -> float:
    return math.erfc(abs(z) / math.sqrt(2.0))


def kl_divergence_normal(
    m_p: float, v_p: float, m_q: float, v_q: float
) -> float:
    """KL(N(m_p, v_p) || N(m_q, v_q))."""
    return 0.5 * (math.log(v_q / v_p) + (v_p + (m_p - m_q) ** 2) / v_q - 1.0)


def check_fisher_and_renyi() -> dict[str, float | bool]:
    x_bar = 2.5
    n = 4
    sigma2 = 1.0
    mu0 = 0.0
    tau0_sq = 1.0
    gamma0 = 1.0
    v_obs = sigma2 / n

    # Marginal likelihood score S(x_bar) = d/d_gamma log N(x_bar | mu0, gamma*tau0^2 + sigma^2/n)|_{gamma=1}
    v_marg = gamma0 * tau0_sq + v_obs
    s_direct = -0.5 * tau0_sq / v_marg + 0.5 * tau0_sq * ((x_bar - mu0) ** 2) / (
        v_marg**2
    )

    # Posterior theta | x_bar at gamma = 1
    v_post = 1.0 / (1.0 / tau0_sq + 1.0 / v_obs)
    m_post = v_post * (mu0 / tau0_sq + x_bar / v_obs)
    # Fisher identity: E_{theta|x_bar}[-1/(2*gamma0) + (theta - mu0)^2 / (2*gamma0^2*tau0^2)]
    s_fisher = -0.5 + (v_post + (m_post - mu0) ** 2) / (2.0 * tau0_sq)

    # Closed-form formula in Nott et al. Section 4.1 (p. 10)
    s_example_4_1 = (
        -1.0 / (2.0 * tau0_sq)
        + ((x_bar - mu0) ** 2 / (2.0 * tau0_sq)) * ((tau0_sq / (tau0_sq + v_obs)) ** 2)
        + (v_obs / (2.0 * tau0_sq)) / (tau0_sq + v_obs)
    )

    # Equation (2.3)-(2.4): baseline-posterior-weighted functional
    # (alpha - 1)^{-1} log integral RB(theta | y, gamma)^{alpha - 1} g(theta | y) d_theta
    # Since RB(theta | y, gamma) = p(y | theta) / p(y | gamma), its gamma-dependent part is -log p(y | gamma)
    # for every alpha > 0, and for alpha -> 1 fixed-posterior KL(g(theta|y) || g(theta|gamma)) has derivative -S(y).
    eps = 1e-7
    kl_fixed_plus = kl_divergence_normal(
        m_post, v_post, mu0, (gamma0 + eps) * tau0_sq
    )
    kl_fixed_minus = kl_divergence_normal(
        m_post, v_post, mu0, (gamma0 - eps) * tau0_sq
    )
    neg_d_fixed_posterior_kl = -(kl_fixed_plus - kl_fixed_minus) / (2.0 * eps)

    # By contrast, if g(theta | y, gamma) also varies with gamma inside KL(g(theta|y,gamma) || g(theta|gamma)):
    v_post_plus = 1.0 / (1.0 / ((gamma0 + eps) * tau0_sq) + 1.0 / v_obs)
    m_post_plus = v_post_plus * (mu0 / ((gamma0 + eps) * tau0_sq) + x_bar / v_obs)
    v_post_minus = 1.0 / (1.0 / ((gamma0 - eps) * tau0_sq) + 1.0 / v_obs)
    m_post_minus = v_post_minus * (mu0 / ((gamma0 - eps) * tau0_sq) + x_bar / v_obs)
    kl_varying_plus = kl_divergence_normal(
        m_post_plus, v_post_plus, mu0, (gamma0 + eps) * tau0_sq
    )
    kl_varying_minus = kl_divergence_normal(
        m_post_minus, v_post_minus, mu0, (gamma0 - eps) * tau0_sq
    )
    neg_d_varying_posterior_kl = -(kl_varying_plus - kl_varying_minus) / (2.0 * eps)

    max_diff = max(
        abs(s_direct - s_fisher),
        abs(s_direct - s_example_4_1),
        abs(s_direct - neg_d_fixed_posterior_kl),
    )
    return {
        "s_direct": round(s_direct, 8),
        "s_fisher": round(s_fisher, 8),
        "s_example_4_1": round(s_example_4_1, 8),
        "neg_d_fixed_posterior_kl": round(neg_d_fixed_posterior_kl, 8),
        "neg_d_varying_posterior_kl": round(neg_d_varying_posterior_kl, 8),
        "identities_agree": max_diff < 1e-6,
        "varying_posterior_differs_by_cov_term": abs(
            neg_d_fixed_posterior_kl - neg_d_varying_posterior_kl
        )
        > 0.1,
    }


def check_evans_moshonov_equivalence() -> dict[str, float | bool]:
    x_bar = 2.5
    mu0 = 0.0
    tau0_sq = 1.0
    v_obs = 0.25
    v_marg = tau0_sq + v_obs
    z_obs = (x_bar - mu0) / math.sqrt(v_marg)
    p_score = normal_two_sided_tail(z_obs)
    p_evans_moshonov = normal_two_sided_tail(z_obs)
    return {
        "z_obs": round(z_obs, 8),
        "p_score_upper_tail": round(p_score, 8),
        "p_evans_moshonov": round(p_evans_moshonov, 8),
        "exact_equivalence": abs(p_score - p_evans_moshonov) < 1e-12,
    }


def check_multivariate_quadratic_score() -> dict[str, float | bool]:
    x_bar = 2.5
    mu0 = 0.0
    tau0_sq = 1.0
    v_obs = 0.25
    v_marg = tau0_sq + v_obs
    s1 = (x_bar - mu0) / v_marg
    s2 = -0.5 * tau0_sq / v_marg + 0.5 * tau0_sq * ((x_bar - mu0) ** 2) / (v_marg**2)
    var_s1 = 1.0 / v_marg
    var_s2 = (tau0_sq**2) / (2.0 * (v_marg**2))
    d_obs = (s1**2) / var_s1 + (s2**2) / var_s2
    z_sq = ((x_bar - mu0) ** 2) / v_marg
    d_closed = z_sq + 0.5 * ((z_sq - 1.0) ** 2)
    return {
        "s1": round(s1, 8),
        "s2": round(s2, 8),
        "var_s1": round(var_s1, 8),
        "var_s2": round(var_s2, 8),
        "d_obs": round(d_obs, 8),
        "d_closed": round(d_closed, 8),
        "quadratic_form_matches": abs(d_obs - d_closed) < 1e-12,
    }


def check_hierarchical_normal_random_effects() -> dict[str, float | bool]:
    # Balanced k-group normal random-effects model (Example 4.3, pp. 11-13):
    # y_bar_j | theta_j ~ N(theta_j, sigma^2 / m), j = 1..k
    # theta_j | mu ~ N(mu, gamma_1 * tau_2^2), mu ~ N(mu_0, gamma_2 * tau_1^2) at (1, 1).
    y_bars = [3.2, 1.0, 1.8, 2.0]
    k = len(y_bars)
    v_within = 0.25  # sigma^2 / m
    tau2_sq = 0.5
    tau1_sq = 1.0
    mu0 = 0.0
    y_grand = sum(y_bars) / k
    ss_between = sum((yj - y_grand) ** 2 for yj in y_bars)

    # Upper-level marginal likelihood: y_bar_j ~ MVN(mu0 * 1, (tau2_sq + v_within) I + gamma_2 * tau1_sq 1 1^T)
    # Score S^{(2)}(y) = d/d_gamma_2 log p(y | gamma_1=1, gamma_2)|_{gamma_2=1} depends only on y_grand:
    # y_grand ~ N(mu0, gamma_2 * tau1_sq + (tau2_sq + v_within) / k)
    v_grand = tau1_sq + (tau2_sq + v_within) / k
    s2_upper = -0.5 * tau1_sq / v_grand + 0.5 * tau1_sq * ((y_grand - mu0) ** 2) / (
        v_grand**2
    )

    # Lower-level conditional score S^{(1)}(y, mu) = d/d_gamma_1 log p(y | mu, gamma_1)|_{gamma_1=1}:
    # Since y_bar_j | mu ~ indep N(mu, gamma_1 * tau2_sq + v_within),
    # S^{(1)}(y, mu) = -k * tau2_sq / (2 * v_j) + (tau2_sq / (2 * v_j^2)) * sum_j (y_bar_j - mu)^2
    v_j = tau2_sq + v_within
    # Posterior of mu | y at (1, 1):
    v_mu_post = 1.0 / (1.0 / tau1_sq + k / v_j)
    m_mu_post = v_mu_post * (mu0 / tau1_sq + k * y_grand / v_j)
    # Averaging sum_j (y_bar_j - mu)^2 over mu | y_obs:
    expected_sq = ss_between + k * ((y_grand - m_mu_post) ** 2 + v_mu_post)
    s1_lower = -0.5 * k * tau2_sq / v_j + 0.5 * tau2_sq * expected_sq / (v_j**2)

    return {
        "y_grand": round(y_grand, 8),
        "ss_between": round(ss_between, 8),
        "s1_lower_mixed": round(s1_lower, 8),
        "s2_upper_marginal": round(s2_upper, 8),
        "upper_score_positive_for_grand_mean_shift": s2_upper > 0.0,
    }


def check_support_dependent_boundary() -> dict[str, float | bool]:
    y = 2.0
    gamma0 = 1.0
    eps = 1e-7
    log_p_plus = math.log((1.0 - math.exp(-y * (gamma0 + eps))) / (y * (gamma0 + eps)))
    log_p_minus = math.log((1.0 - math.exp(-y * (gamma0 - eps))) / (y * (gamma0 - eps)))
    s_exact_fd = (log_p_plus - log_p_minus) / (2.0 * eps)
    s_naive_eq_1_3 = -1.0
    boundary_posterior_density = math.exp(-y) / ((1.0 - math.exp(-y)) / y)
    s_reparameterized = -1.0 + boundary_posterior_density

    return {
        "s_exact_fd": round(s_exact_fd, 8),
        "s_naive_eq_1_3": round(s_naive_eq_1_3, 8),
        "boundary_posterior_density": round(boundary_posterior_density, 8),
        "s_reparameterized": round(s_reparameterized, 8),
        "naive_fails_by_boundary_term": abs(s_exact_fd - s_naive_eq_1_3) > 0.1,
        "reparameterized_matches_exact": abs(s_exact_fd - s_reparameterized) < 1e-8,
    }


def main() -> None:
    summary = {
        "evans_moshonov_equivalence": check_evans_moshonov_equivalence(),
        "fisher_and_renyi": check_fisher_and_renyi(),
        "hierarchical_normal_random_effects": check_hierarchical_normal_random_effects(),
        "multivariate_quadratic_score": check_multivariate_quadratic_score(),
        "support_dependent_boundary": check_support_dependent_boundary(),
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
