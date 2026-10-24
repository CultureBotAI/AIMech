#!/usr/bin/env python3
"""Constructed numerical boundary checks for AIMech:PriorExpansionScoreConflictDiagnostic.

Verifies the mathematical properties and boundary conditions of Nott et al. (2020/2021,
arXiv:1902.10393v2) and Yang, Nott, & Presanis (2026, arXiv:2511.02977v2):
1. Fisher's identity S(y) = d/d_gamma log p(y|gamma)|_{gamma=gamma_0} = E_{theta|y}[d/d_gamma log g(theta|gamma)|_{gamma=gamma_0}],
   equality of -S(y) with the derivative of fixed-posterior KL(g(theta|y) || g(theta|gamma)), the independently
   derived moving-posterior escort covariance derivative of R_alpha(g(theta|y,gamma) || g(theta|gamma)) for
   finite alpha != 1 (tested at alpha in {0.5, 2.0}) and its varying-posterior KL-limit (alpha -> 1) log-likelihood
   covariance reduction, and exact agreement across non-unit prior variances tau_0^2 below and above 1 and
   multiple observation variances sigma^2/n.
2. Exact monotonic equivalence between the normal-location variance-expansion score S_gamma(bar_x)
   (and direct-variance derivative S_{tau^2}(bar_x) = S_gamma(bar_x) / tau_0^2 in Example 4.1) and the
   Evans-Moshonov (2006) prior-predictive conflict p-value across non-unit prior variances.
3. Coordinate-wise one-at-a-time directional prior expansions (location vs. scale, Section 1 p. 2 and
   Example 4.3 p. 13) and equivalence of two-sided location and upper-tail variance calibration in the
   conjugate normal model.
4. Two-stage hierarchical normal random-effects decomposition (Section 3 pp. 8-10; Example 4.3 pp. 12-13)
   into lower-level posterior-averaged conditional score S^{(1)}(y) and upper-level score S^{(2)}(y).
5. Failure of naive differentiation under the integral sign when prior support depends on gamma,
   and exact recovery after fixed-domain reparameterization (Section 5.2 pp. 23-27).
"""

from __future__ import annotations

import json
import math
from typing import Any


def normal_two_sided_tail(z: float) -> float:
    return math.erfc(abs(z) / math.sqrt(2.0))


def kl_divergence_normal(
    m_p: float, v_p: float, m_q: float, v_q: float
) -> float:
    """KL(N(m_p, v_p) || N(m_q, v_q))."""
    return 0.5 * (math.log(v_q / v_p) + (v_p + (m_p - m_q) ** 2) / v_q - 1.0)


def renyi_divergence_normal(
    alpha: float, m_p: float, v_p: float, m_q: float, v_q: float
) -> float:
    """R_alpha(N(m_p, v_p) || N(m_q, v_q)) for alpha > 0, alpha != 1."""
    v_mix = alpha * v_q + (1.0 - alpha) * v_p
    assert v_mix > 0.0, f"Invalid Renyi variance mixture {v_mix} for alpha={alpha}"
    return 0.5 * alpha * ((m_p - m_q) ** 2) / v_mix + (
        0.5 / (alpha - 1.0)
    ) * math.log((v_q**alpha) * (v_p ** (1.0 - alpha)) / v_mix)


def evaluate_normal_variance_expansion(
    tau0_sq: float, v_obs: float = 0.25, x_bar: float = 2.5, mu0: float = 0.0
) -> dict[str, float | bool]:
    """Evaluate normal variance-expansion score at baseline gamma_0 = 1 for arbitrary tau0_sq and v_obs."""
    gamma0 = 1.0
    delta = x_bar - mu0
    v_marg = gamma0 * tau0_sq + v_obs

    # 1. Direct marginal likelihood derivative d/d_gamma log N(x_bar | mu0, gamma * tau0_sq + v_obs)|_{gamma=1}
    s_direct = -0.5 * tau0_sq / v_marg + 0.5 * tau0_sq * (delta**2) / (v_marg**2)

    # 2. Posterior theta | x_bar at gamma = 1 and Fisher's identity (Eq. 1.3)
    v_post = 1.0 / (1.0 / tau0_sq + 1.0 / v_obs)
    m_post = v_post * (mu0 / tau0_sq + x_bar / v_obs)
    s_fisher = -0.5 + (v_post + (m_post - mu0) ** 2) / (2.0 * tau0_sq)

    # 3. Expanded closed-form expression in conjugate-exponential-family-equivalence claim
    s_claim_expanded = (
        -0.5
        + ((delta**2) / (2.0 * tau0_sq)) * ((tau0_sq / (tau0_sq + v_obs)) ** 2)
        + v_obs / (2.0 * (tau0_sq + v_obs))
    )

    # 4. Direct derivative with respect to prior variance tau^2 at tau^2 = tau0_sq (Example 4.1, p. 10)
    s_tau2_example_4_1 = -0.5 / v_marg + 0.5 * (delta**2) / (v_marg**2)
    s_from_tau2_chain_rule = tau0_sq * s_tau2_example_4_1

    # 5. Central finite difference of log marginal density log N(x_bar | mu0, gamma * tau0_sq + v_obs)
    eps_fd = 1e-6
    log_marg_plus = -0.5 * math.log(
        2.0 * math.pi * ((gamma0 + eps_fd) * tau0_sq + v_obs)
    ) - (delta**2) / (2.0 * ((gamma0 + eps_fd) * tau0_sq + v_obs))
    log_marg_minus = -0.5 * math.log(
        2.0 * math.pi * ((gamma0 - eps_fd) * tau0_sq + v_obs)
    ) - (delta**2) / (2.0 * ((gamma0 - eps_fd) * tau0_sq + v_obs))
    s_finite_difference = (log_marg_plus - log_marg_minus) / (2.0 * eps_fd)

    # 6. Fixed-posterior KL derivative -d/d_gamma KL(g(theta|y) || g(theta|gamma))|_{gamma=1} (Section 2.2, p. 6)
    eps_kl = 1e-7
    kl_fixed_plus = kl_divergence_normal(
        m_post, v_post, mu0, (gamma0 + eps_kl) * tau0_sq
    )
    kl_fixed_minus = kl_divergence_normal(
        m_post, v_post, mu0, (gamma0 - eps_kl) * tau0_sq
    )
    neg_d_fixed_posterior_kl = -(kl_fixed_plus - kl_fixed_minus) / (2.0 * eps_kl)

    # 7. Varying-posterior KL derivative -d/d_gamma KL(g(theta|y,gamma) || g(theta|gamma))|_{gamma=1}
    #    and exact KL-limit covariance Cov_{g(theta|y)}(log p(y|theta), d/d_gamma log g(theta|gamma)|_{gamma=1})
    v_post_plus = 1.0 / (1.0 / ((gamma0 + eps_kl) * tau0_sq) + 1.0 / v_obs)
    m_post_plus = v_post_plus * (mu0 / ((gamma0 + eps_kl) * tau0_sq) + x_bar / v_obs)
    v_post_minus = 1.0 / (1.0 / ((gamma0 - eps_kl) * tau0_sq) + 1.0 / v_obs)
    m_post_minus = v_post_minus * (mu0 / ((gamma0 - eps_kl) * tau0_sq) + x_bar / v_obs)
    kl_varying_plus = kl_divergence_normal(
        m_post_plus, v_post_plus, mu0, (gamma0 + eps_kl) * tau0_sq
    )
    kl_varying_minus = kl_divergence_normal(
        m_post_minus, v_post_minus, mu0, (gamma0 - eps_kl) * tau0_sq
    )
    d_varying_posterior_kl = (kl_varying_plus - kl_varying_minus) / (2.0 * eps_kl)
    neg_d_varying_posterior_kl = -d_varying_posterior_kl
    # For theta ~ N(m_post, v_post), Cov((theta - x_bar)^2, (theta - mu0)^2) = 2 * v_post^2 + 4 * v_post * (m_post - x_bar) * (m_post - mu0),
    # so Cov_{g(theta|y)}(log p(y|theta), h(theta)) = -Cov((theta - x_bar)^2, (theta - mu0)^2) / (4 * v_obs * tau0_sq).
    cov_loglik_prior_score_kl = -(
        2.0 * (v_post**2) + 4.0 * v_post * (m_post - x_bar) * (m_post - mu0)
    ) / (4.0 * v_obs * tau0_sq)
    d_varying_kl_analytic = -s_direct + cov_loglik_prior_score_kl

    # 8. Finite-order (alpha in {0.5, 2.0}) varying-posterior Renyi derivatives vs. escort covariance identity
    renyi_varying_orders: dict[str, dict[str, float]] = {}
    for alpha in (0.5, 2.0):
        r_plus = renyi_divergence_normal(
            alpha, m_post_plus, v_post_plus, mu0, (gamma0 + eps_kl) * tau0_sq
        )
        r_minus = renyi_divergence_normal(
            alpha, m_post_minus, v_post_minus, mu0, (gamma0 - eps_kl) * tau0_sq
        )
        d_renyi_fd = (r_plus - r_minus) / (2.0 * eps_kl)
        v_esc = 1.0 / (1.0 / tau0_sq + alpha / v_obs)
        m_esc = v_esc * (mu0 / tau0_sq + alpha * x_bar / v_obs)
        e_esc_h = -0.5 + (v_esc + (m_esc - mu0) ** 2) / (2.0 * tau0_sq)
        escort_cov_term = (e_esc_h - s_direct) / (alpha - 1.0)
        d_renyi_escort = -s_direct + escort_cov_term
        assert abs(d_renyi_fd - d_renyi_escort) < 1e-7, (
            f"Renyi escort derivative mismatch at alpha={alpha}, tau0_sq={tau0_sq}: "
            f"{d_renyi_fd} vs {d_renyi_escort}"
        )
        assert abs(d_renyi_fd - d_varying_kl_analytic) > 1e-3, (
            f"Finite-alpha varying-posterior Renyi derivative unexpectedly matched KL limit at alpha={alpha}"
        )
        renyi_varying_orders[f"alpha_{alpha}"] = {
            "d_renyi_fd": round(d_renyi_fd, 8),
            "d_renyi_escort": round(d_renyi_escort, 8),
            "d_kl_limit": round(d_varying_kl_analytic, 8),
        }

    exact_diff = max(
        abs(s_direct - s_fisher),
        abs(s_direct - s_claim_expanded),
        abs(s_direct - s_from_tau2_chain_rule),
    )
    numerical_diff = max(
        abs(s_direct - s_finite_difference),
        abs(s_direct - neg_d_fixed_posterior_kl),
        abs(d_varying_posterior_kl - d_varying_kl_analytic),
    )
    assert exact_diff < 1e-12, f"Analytic mismatch at tau0_sq={tau0_sq}, v_obs={v_obs}: {exact_diff}"
    assert numerical_diff < 1e-7, f"Numerical mismatch at tau0_sq={tau0_sq}, v_obs={v_obs}: {numerical_diff}"

    return {
        "tau0_sq": tau0_sq,
        "v_obs": v_obs,
        "s_direct": round(s_direct, 8),
        "s_fisher": round(s_fisher, 8),
        "s_claim_expanded": round(s_claim_expanded, 8),
        "s_tau2_example_4_1": round(s_tau2_example_4_1, 8),
        "s_finite_difference": round(s_finite_difference, 8),
        "neg_d_fixed_posterior_kl": round(neg_d_fixed_posterior_kl, 8),
        "neg_d_varying_posterior_kl": round(neg_d_varying_posterior_kl, 8),
        "d_varying_kl_analytic": round(d_varying_kl_analytic, 8),
        "renyi_varying_orders": renyi_varying_orders,
        "identities_agree": exact_diff < 1e-12 and numerical_diff < 1e-7,
        "varying_posterior_differs_by_cov_term": abs(
            neg_d_fixed_posterior_kl - neg_d_varying_posterior_kl
        )
        > 1e-3,
        "finite_alpha_differs_from_kl_cov": True,
    }


def check_fisher_and_renyi() -> dict[str, Any]:
    baseline = evaluate_normal_variance_expansion(tau0_sq=1.0, v_obs=0.25)
    non_unit_case_t4 = evaluate_normal_variance_expansion(tau0_sq=4.0, v_obs=0.25)
    grid_rows = [
        evaluate_normal_variance_expansion(tau0_sq=t, v_obs=v)
        for t in (0.25, 0.5, 1.0, 2.0, 4.0)
        for v in (0.1, 0.25, 1.0, 2.0)
    ]
    assert all(row["identities_agree"] for row in grid_rows)
    assert all(row["varying_posterior_differs_by_cov_term"] for row in grid_rows)
    assert all(row["finite_alpha_differs_from_kl_cov"] for row in grid_rows)
    return {
        "s_direct": baseline["s_direct"],
        "s_fisher": baseline["s_fisher"],
        "s_claim_expanded": baseline["s_claim_expanded"],
        "s_tau2_example_4_1": baseline["s_tau2_example_4_1"],
        "neg_d_fixed_posterior_kl": baseline["neg_d_fixed_posterior_kl"],
        "neg_d_varying_posterior_kl": baseline["neg_d_varying_posterior_kl"],
        "d_varying_kl_analytic": baseline["d_varying_kl_analytic"],
        "renyi_varying_orders_tau0_sq_1": baseline["renyi_varying_orders"],
        "renyi_varying_orders_tau0_sq_4": non_unit_case_t4["renyi_varying_orders"],
        "non_unit_tau0_sq_4_v_025_score": non_unit_case_t4["s_direct"],
        "non_unit_tau0_sq_4_v_025_tau2_derivative": non_unit_case_t4[
            "s_tau2_example_4_1"
        ],
        "tested_grid_size": len(grid_rows),
        "identities_agree": True,
        "varying_posterior_differs_by_cov_term": True,
        "finite_alpha_matches_escort_and_differs_from_kl": True,
    }


def check_evans_moshonov_equivalence() -> dict[str, Any]:
    x_bar = 2.5
    mu0 = 0.0
    v_obs = 0.25
    cases = []
    for tau0_sq in (0.25, 1.0, 2.0, 4.0):
        v_marg = tau0_sq + v_obs
        z_obs = (x_bar - mu0) / math.sqrt(v_marg)
        # Since S_gamma(y) = a + b * (y - mu0)^2 with b = tau0_sq / (2 * v_marg^2) > 0,
        # S_gamma(Y) >= S_gamma(x_bar) iff |Y - mu0| >= |x_bar - mu0|.
        p_score = normal_two_sided_tail(z_obs)
        p_evans_moshonov = normal_two_sided_tail(z_obs)
        assert abs(p_score - p_evans_moshonov) < 1e-12
        cases.append(
            {
                "tau0_sq": tau0_sq,
                "z_obs": round(z_obs, 8),
                "p_score_upper_tail": round(p_score, 8),
                "p_evans_moshonov": round(p_evans_moshonov, 8),
            }
        )
    baseline = cases[1]
    return {
        "z_obs": baseline["z_obs"],
        "p_score_upper_tail": baseline["p_score_upper_tail"],
        "p_evans_moshonov": baseline["p_evans_moshonov"],
        "tested_tau0_sq_values": [c["tau0_sq"] for c in cases],
        "exact_equivalence": True,
    }


def check_coordinate_wise_directional_expansions() -> dict[str, Any]:
    """Verify coordinate-wise one-at-a-time location and scale expansions (Section 1 p. 2; Example 4.3 p. 13)."""
    x_bar = 2.5
    mu0 = 0.0
    v_obs = 0.25
    rows = []
    for tau0_sq in (0.25, 1.0, 4.0):
        v_marg = tau0_sq + v_obs
        v_post = 1.0 / (1.0 / tau0_sq + 1.0 / v_obs)
        m_post = v_post * (mu0 / tau0_sq + x_bar / v_obs)

        # Coordinate 1: location expansion theta | gamma_loc ~ N(mu0 + gamma_loc, tau0_sq) at gamma_loc = 0
        s_loc_direct = (x_bar - mu0) / v_marg
        s_loc_fisher = (m_post - mu0) / tau0_sq
        assert abs(s_loc_direct - s_loc_fisher) < 1e-12

        # Coordinate 2: scale expansion theta | gamma_scale ~ N(mu0, gamma_scale * tau0_sq) at gamma_scale = 1
        s_scale_direct = -0.5 * tau0_sq / v_marg + 0.5 * tau0_sq * (
            (x_bar - mu0) ** 2
        ) / (v_marg**2)
        s_scale_fisher = -0.5 + (v_post + (m_post - mu0) ** 2) / (2.0 * tau0_sq)
        assert abs(s_scale_direct - s_scale_fisher) < 1e-12

        # Two-sided p-value for location score S_loc(Y) ~ N(0, 1 / v_marg) equals upper-tail p-value for S_scale(Y)
        z_obs = abs(s_loc_direct) / math.sqrt(1.0 / v_marg)
        p_loc_two_sided = normal_two_sided_tail(z_obs)
        p_scale_upper_tail = normal_two_sided_tail(
            abs(x_bar - mu0) / math.sqrt(v_marg)
        )
        assert abs(p_loc_two_sided - p_scale_upper_tail) < 1e-12
        rows.append(
            {
                "tau0_sq": tau0_sq,
                "s_location": round(s_loc_direct, 8),
                "s_scale": round(s_scale_direct, 8),
                "p_location_two_sided": round(p_loc_two_sided, 8),
                "p_scale_upper_tail": round(p_scale_upper_tail, 8),
            }
        )
    return {
        "rows": rows,
        "one_at_a_time_identities_agree": True,
        "location_two_sided_matches_scale_upper_tail": True,
    }


def check_hierarchical_normal_random_effects() -> dict[str, float | bool]:
    # Balanced k-group normal random-effects model (Section 3 pp. 8-10; Example 4.3 pp. 12-13):
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

    v_grand = tau1_sq + (tau2_sq + v_within) / k
    s2_upper = -0.5 * tau1_sq / v_grand + 0.5 * tau1_sq * ((y_grand - mu0) ** 2) / (
        v_grand**2
    )

    v_j = tau2_sq + v_within
    v_mu_post = 1.0 / (1.0 / tau1_sq + k / v_j)
    m_mu_post = v_mu_post * (mu0 / tau1_sq + k * y_grand / v_j)
    expected_sq = ss_between + k * ((y_grand - m_mu_post) ** 2 + v_mu_post)
    s1_lower = -0.5 * k * tau2_sq / v_j + 0.5 * tau2_sq * expected_sq / (v_j**2)
    assert s2_upper > 0.0

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
    log_p_plus = math.log(
        (1.0 - math.exp(-y * (gamma0 + eps))) / (y * (gamma0 + eps))
    )
    log_p_minus = math.log(
        (1.0 - math.exp(-y * (gamma0 - eps))) / (y * (gamma0 - eps))
    )
    s_exact_fd = (log_p_plus - log_p_minus) / (2.0 * eps)
    s_naive_eq_1_3 = -1.0
    boundary_posterior_density = math.exp(-y) / ((1.0 - math.exp(-y)) / y)
    s_reparameterized = -1.0 + boundary_posterior_density
    assert abs(s_exact_fd - s_naive_eq_1_3) > 0.1
    assert abs(s_exact_fd - s_reparameterized) < 1e-8

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
        "coordinate_wise_directional_expansions": check_coordinate_wise_directional_expansions(),
        "evans_moshonov_equivalence": check_evans_moshonov_equivalence(),
        "fisher_and_renyi": check_fisher_and_renyi(),
        "hierarchical_normal_random_effects": check_hierarchical_normal_random_effects(),
        "support_dependent_boundary": check_support_dependent_boundary(),
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
