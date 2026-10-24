#!/usr/bin/env python3
"""Constructed analytic and numerical boundary checks for AIMech:SequentialScoreDiscrepancyConflictDiagnostic.

Verifies:
1. Exact conditional posterior-expectation score vs. single-draw score estimator in the
   two-stage normal DAG (Yang, Nott, & Presanis 2026, Section 3.1, Algorithm 1, p. 16,
   and Appendix D.2, p. 43):
   - Exact score variance under conditional prior predictive: tau^4 / (2 * (sigma^2 + tau^2)^2).
   - Single-draw score marginal variance under joint replicate + posterior-draw law: 1/2.
   - Conditional Monte Carlo variance inflation factor ((sigma^2 + tau^2) / tau^2)^2 when
     a single draw theta_2^{(m)} ~ p(theta_2 | y_ch, theta_1^{(m)}) is used instead of
     the exact conditional posterior expectation.
2. Dependent p-value aggregation via Half-Cauchy Combination Test (HCCT) vs. minimum
   order-statistic bound (Section 2.4, p. 13; Section 3.1, pp. 15-16):
   - Exact comonotonic invariance of HCCT (p^(1)=...=p^(M)=u => p_HCCT = u) versus
     M-fold conservatism of minimum order-statistic bound min(1, M*u).
   - Single-extreme dominance of HCCT when one conditional draw exhibits severe conflict
     while others are moderate.
"""
from __future__ import annotations

import json
import math


def check_single_draw_vs_exact_score_scaling() -> dict[str, float]:
    # Conditional prior: theta_2 | theta_1, alpha ~ N(theta_1, alpha * tau^2) at alpha_0 = 1
    # Child likelihood: y_ch | theta_2 ~ N(theta_2, sigma^2)
    theta_1 = 0.0
    tau2 = 1.0
    sigma2 = 1.0
    y_ch_obs = 3.0

    v_post = (1.0 / tau2 + 1.0 / sigma2) ** -1
    mu_post = v_post * (theta_1 / tau2 + y_ch_obs / sigma2)

    # Exact conditional posterior expectation of d/dalpha log p(theta_2 | theta_1, alpha)|_{alpha=1}
    # = -1/2 + E[(theta_2 - theta_1)^2 | y_ch, theta_1] / (2 * tau^2)
    s_exact_obs = -0.5 + (v_post + (mu_post - theta_1) ** 2) / (2.0 * tau2)
    s_exact_formula = -tau2 / (2.0 * (sigma2 + tau2)) + (
        tau2 / (2.0 * (sigma2 + tau2) ** 2)
    ) * ((y_ch_obs - theta_1) ** 2)
    assert math.isclose(s_exact_obs, s_exact_formula, rel_tol=1e-12)

    # Prior-predictive variance of exact score S_exact(Y_ch; theta_1) where Y_ch ~ N(theta_1, sigma^2 + tau^2):
    # S_exact = (tau^2 / (2*(sigma^2+tau^2))) * (Z^2 - 1), Var(Z^2 - 1) = 2
    var_s_exact = (tau2**2) / (2.0 * (sigma2 + tau2) ** 2)

    # Single-draw estimator S_single(Y_ch, tilde_theta_2; theta_1) = -1/2 + (tilde_theta_2 - theta_1)^2 / (2*tau^2)
    # Under Y_ch ~ p(y_ch | theta_1) and tilde_theta_2 ~ p(theta_2 | Y_ch, theta_1),
    # marginally tilde_theta_2 | theta_1 ~ N(theta_1, tau^2), so Var(S_single) = 1/2.
    var_s_single_marginal = 0.5

    # Conditional on y_ch_obs, tilde_theta_2 ~ N(mu_post, v_post), so (tilde_theta_2 - theta_1)^2
    # has conditional variance 2*v_post^2 + 4*v_post*(mu_post - theta_1)^2
    cond_var_single_given_y = (
        2.0 * (v_post**2) + 4.0 * v_post * ((mu_post - theta_1) ** 2)
    ) / (4.0 * (tau2**2))

    # Law of total variance check: Var(S_single) = E[Var(S_single | Y_ch)] + Var(E[S_single | Y_ch])
    # E[(mu_post - theta_1)^2] = (tau^2 / (sigma^2 + tau^2))^2 * (sigma^2 + tau^2) = tau^4 / (sigma^2 + tau^2)
    expected_cond_var = (
        2.0 * (v_post**2) + 4.0 * v_post * (tau2**2 / (sigma2 + tau2))
    ) / (4.0 * (tau2**2))
    total_var_check = expected_cond_var + var_s_exact
    assert math.isclose(total_var_check, var_s_single_marginal, rel_tol=1e-12)

    variance_inflation_ratio = var_s_single_marginal / var_s_exact
    expected_ratio = ((sigma2 + tau2) / tau2) ** 2
    assert math.isclose(variance_inflation_ratio, expected_ratio, rel_tol=1e-12)

    return {
        "s_exact_obs": round(s_exact_obs, 8),
        "var_s_exact": round(var_s_exact, 8),
        "var_s_single_marginal": round(var_s_single_marginal, 8),
        "cond_var_single_given_y_obs": round(cond_var_single_given_y, 8),
        "expected_cond_var": round(expected_cond_var, 8),
        "variance_inflation_ratio": round(variance_inflation_ratio, 8),
    }


def hcct_pvalue(p_values: list[float]) -> tuple[float, float]:
    t_stat = sum(math.tan(0.5 * math.pi * (1.0 - p)) for p in p_values) / len(p_values)
    p_comb = 1.0 - (2.0 / math.pi) * math.atan(t_stat)
    return t_stat, p_comb


def min_order_pvalue(p_values: list[float]) -> float:
    return min(1.0, len(p_values) * min(p_values))


def check_dependent_pvalue_combinations() -> dict[str, float]:
    # 1. Comonotonic (perfectly dependent) p-values across M=10 parent draws
    u = 0.04
    comonotonic_ps = [u] * 10
    t_como, p_hcct_como = hcct_pvalue(comonotonic_ps)
    p_ord_como = min_order_pvalue(comonotonic_ps)
    assert math.isclose(p_hcct_como, u, rel_tol=1e-12)
    assert math.isclose(p_ord_como, 0.40, rel_tol=1e-12)

    # 2. Heterogeneous conditional p-values across M=5 parent posterior draws
    hetero_ps = [0.002, 0.05, 0.12, 0.25, 0.40]
    t_het, p_hcct_het = hcct_pvalue(hetero_ps)
    p_ord_het = min_order_pvalue(hetero_ps)
    assert 0.0 < p_hcct_het < 0.05
    assert math.isclose(p_ord_het, 0.01, rel_tol=1e-12)

    # 3. Null-like conditional p-values including p=1.0 boundary (tan(0)=0)
    null_ps = [0.50, 0.75, 1.0]
    t_null, p_hcct_null = hcct_pvalue(null_ps)
    assert math.isclose(
        t_null,
        (math.tan(0.25 * math.pi) + math.tan(0.125 * math.pi) + 0.0) / 3.0,
        rel_tol=1e-12,
    )

    return {
        "comonotonic_u": u,
        "comonotonic_hcct_p": round(p_hcct_como, 8),
        "comonotonic_min_order_p": round(p_ord_como, 8),
        "heterogeneous_hcct_t": round(t_het, 8),
        "heterogeneous_hcct_p": round(p_hcct_het, 8),
        "heterogeneous_min_order_p": round(p_ord_het, 8),
        "null_boundary_hcct_p": round(p_hcct_null, 8),
    }


def main() -> None:
    results = {
        "single_draw_vs_exact_score_scaling": check_single_draw_vs_exact_score_scaling(),
        "dependent_pvalue_combinations": check_dependent_pvalue_combinations(),
        "limits": (
            "Constructed analytic two-stage normal DAG and closed-form p-value combination checks only; "
            "no MCMC, real-data epidemic model fit, or empirical repeated-data calibration simulation."
        ),
    }
    print(json.dumps(results, sort_keys=True))


if __name__ == "__main__":
    main()
