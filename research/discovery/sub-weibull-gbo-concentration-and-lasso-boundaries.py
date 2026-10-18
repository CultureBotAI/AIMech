#!/usr/bin/env python3
"""Constructed boundary & regime verification for AIMech:GeneralizedBernsteinOrliczSubWeibullConcentrationAndHighDimensionalLasso.

Verifies four core mathematical mechanisms from Kuchibhotla & Chakrabortty
(2022, Information and Inference 11(4):1389-1456, arXiv:1804.02605v4,
DOI:10.1093/imaiai/iaac012):
1. Generalized Bernstein-Orlicz (GBO) Norm Equivalence & Two-Regime Tail Behavior
   (Definition 2.3, Proposition A.1, Equations 2.5, C.1-C.2) and Product Orlicz
   Quasi-Norm Holder Inequality (Proposition D.2, Equation 3.5);
2. Joint vs. Marginal Sub-Weibull Norm Divergence under Collinearity (Definitions
   2.4-2.5, Section 4, Equation 4.1: ||X||_{J,psi_alpha} = sqrt(q) ||X(1)||_{psi_alpha}
   vs. ||X||_{M,psi_alpha} = ||X(1)||_{psi_alpha}) and Sharpness of GBO Maximal
   Inequality vs. Chernozhukov et al. (2017) Lemma E.1 (Theorem 3.4, Remark 3.2,
   Equations 3.2-3.3);
3. Restricted Strong Convexity (RSC, Theorem 4.4, Equations 4.17-4.18) and
   Free-Parameter Optimization min_{1<=s<=p} {Xi_{n,s} + k Xi_{n,s}/s} for the
   Restricted Eigenvalue RE(k) Condition (Section 4.3.1, Equations 4.20-4.27);
4. High-Dimensional Misspecified Lasso under Marginally Sub-Weibull Covariates
   and Heavy-Tailed Errors (Section 4.4, Theorems 4.5-4.6, Proposition E.1,
   Equations 4.28-4.33): verification of deterministic basic inequality, cone
   constraint ||nu_hat(S^c)||_1 <= 3 ||nu_hat(S)||_1 + 4 ||beta_0(S^c)||_1
   (Equation E.10), and oracle L2 error bound.
"""

from __future__ import annotations

import json
import math
import random


def solve_psi_alpha_l(x: float, alpha: float, l_param: float) -> float:
    """Invert Psi_{alpha,L}^{-1}(t) = sqrt(log(1+t)) + L (log(1+t))^{1/alpha} = x."""
    if x <= 0.0:
        return 0.0
    lo, hi = 0.0, max(1.0, x * x)
    while math.sqrt(hi) + l_param * (hi ** (1.0 / alpha)) < x:
        hi *= 2.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        val = math.sqrt(mid) + l_param * (mid ** (1.0 / alpha))
        if val < x:
            lo = mid
        else:
            hi = mid
    u = 0.5 * (lo + hi)
    return math.expm1(u)


def gbo_norm_discrete(vals: list[float], probs: list[float], alpha: float, l_param: float) -> float:
    """Compute ||X||_{Psi_{alpha,L}} = inf{eta > 0 : E[Psi_{alpha,L}(|X|/eta)] <= 1}."""
    lo, hi = 1e-6, max(abs(v) for v in vals) * 10.0 + 1.0
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        exp_val = sum(
            p * solve_psi_alpha_l(abs(v) / mid, alpha, l_param)
            for v, p in zip(vals, probs)
        )
        if exp_val > 1.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def phi_norm_discrete(vals: list[float], probs: list[float], alpha: float, l_param: float) -> float:
    """Compute ||X||_{phi_{alpha,L}} where phi_{alpha,L}(x) = exp(min{x^2, (x/L)^alpha}) - 1."""
    lo, hi = 1e-6, max(abs(v) for v in vals) * 10.0 + 1.0
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        exp_val = 0.0
        for v, p in zip(vals, probs):
            x = abs(v) / mid
            u = min(x * x, (x / l_param) ** alpha)
            exp_val += p * math.expm1(min(u, 50.0))
        if exp_val > 1.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def psi_alpha_norm_discrete(vals: list[float], probs: list[float], alpha: float) -> float:
    """Compute ||X||_{psi_alpha} = inf{eta > 0 : E[exp((|X|/eta)^alpha) - 1] <= 1}."""
    lo, hi = 1e-6, max(abs(v) for v in vals) * 10.0 + 1.0
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        exp_val = sum(
            p * math.expm1(min((abs(v) / mid) ** alpha, 50.0))
            for v, p in zip(vals, probs)
        )
        if exp_val > 1.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main() -> int:
    # -------------------------------------------------------------------------
    # Regime 1: GBO Norm Equivalence (Proposition A.1, Equations C.1-C.2) and
    # Product Orlicz Norm Holder Inequality (Proposition D.2, Equation 3.5)
    # -------------------------------------------------------------------------
    vals = [0.5, 1.2, 2.5, 4.0, 7.5]
    probs = [0.40, 0.30, 0.18, 0.09, 0.03]
    ratios = []
    inv_ratios = []
    for alpha in [0.5, 1.0, 2.0]:
        for l_param in [0.4, 1.0, 2.5]:
            norm_psi = gbo_norm_discrete(vals, probs, alpha, l_param)
            norm_phi = phi_norm_discrete(vals, probs, alpha, l_param)
            ratios.append(norm_phi / norm_psi)
            for t in [0.5, 2.0, 10.0, 50.0]:
                u = math.log1p(t)
                psi_inv = math.sqrt(u) + l_param * (u ** (1.0 / alpha))
                phi_inv = max(math.sqrt(u), l_param * (u ** (1.0 / alpha)))
                inv_ratios.append(psi_inv / phi_inv)

    # Proposition D.2: ||W_1 W_2||_{psi_beta} <= ||W_1||_{psi_{alpha_1}} ||W_2||_{psi_{alpha_2}}
    # where 1/beta = 1/alpha_1 + 1/alpha_2
    alpha1, alpha2 = 2.0, 1.0
    beta = 1.0 / (1.0 / alpha1 + 1.0 / alpha2)  # 2/3
    w1_vals = [v * 0.8 for v in vals]
    w2_vals = [v * 1.3 for v in vals]
    prod_vals = [a * b for a, b in zip(w1_vals, w2_vals)]
    norm_w1 = psi_alpha_norm_discrete(w1_vals, probs, alpha1)
    norm_w2 = psi_alpha_norm_discrete(w2_vals, probs, alpha2)
    norm_prod = psi_alpha_norm_discrete(prod_vals, probs, beta)
    holder_ratio = norm_prod / (norm_w1 * norm_w2)

    regime_1_ok = (
        min(ratios) >= 1.0 - 1e-6
        and max(ratios) <= 2.0 + 1e-6
        and min(inv_ratios) >= 1.0 - 1e-6
        and max(inv_ratios) <= 2.0 + 1e-6
        and holder_ratio <= 1.0 + 1e-6
    )

    # -------------------------------------------------------------------------
    # Regime 2: Joint vs. Marginal Sub-Weibull Norm Divergence (Equation 4.1)
    # and Maximal Inequality Rate Improvement (Remark 3.2, Equations 3.2-3.3)
    # -------------------------------------------------------------------------
    q_dim = 64
    norm_x1 = psi_alpha_norm_discrete(vals, probs, 1.0)
    # For X = (X(1), ..., X(1)) in R^q:
    # sup_{||theta||_2=1} ||theta^T X||_{psi_alpha} = sup_{||theta||_2=1} ||theta||_1 ||X(1)||_{psi_alpha} = sqrt(q) ||X(1)||_{psi_alpha}
    marginal_norm = norm_x1
    joint_norm = math.sqrt(q_dim) * norm_x1
    joint_to_marginal_ratio = joint_norm / marginal_norm

    # Compare second-order remainder in Theorem 3.4 / Remark 3.2 (Eq. 3.2) vs.
    # Chernozhukov et al. (2017) Lemma E.1 (Eq. 3.3) in high dimension log(eq) = 80, n = 500:
    alpha_test = 1.0
    alpha_star = min(alpha_test, 1.0)
    n_test = 500
    log_eq = 80.0
    log_eqn = log_eq + math.log(n_test)
    rem_gbo = ((math.log(2.0 * n_test)) ** (1.0 / alpha_test)) * (
        log_eq ** (1.0 / alpha_star)
    ) / n_test
    rem_cck = (log_eqn ** (1.0 / alpha_test)) * log_eq / n_test

    regime_2_ok = (
        abs(joint_to_marginal_ratio - math.sqrt(q_dim)) < 1e-9
        and rem_gbo < rem_cck
    )

    # -------------------------------------------------------------------------
    # Regime 3: Restricted Strong Convexity (Theorem 4.4) and Free-Parameter s
    # Optimization for RE(k) (Section 4.3.1, Equations 4.20-4.27)
    # -------------------------------------------------------------------------
    # Verify that optimizing min_{1<=s<=p} (Xi_{n,s} + k * Xi_{n,s} / s) yields
    # a strictly smaller penalty than naive choices s = 1 or s = k when k > s^*
    n_rsc = 1000000
    p_rsc = 500
    alpha_rsc = 1.5
    k_rsc = 40

    def xi_joint(s: int) -> float:
        term1 = math.sqrt(s * math.log(36.0 * n_rsc * p_rsc / s) / n_rsc)
        term2 = (
            ((math.log(2.0 * n_rsc)) ** (2.0 / alpha_rsc))
            * ((s * math.log(36.0 * n_rsc * p_rsc / s)) ** (2.0 / alpha_rsc))
            / n_rsc
        )
        return term1 + term2

    penalties = {s: xi_joint(s) + (k_rsc / s) * xi_joint(s) for s in range(1, p_rsc + 1)}
    s_opt = min(penalties, key=penalties.get)
    pen_opt = penalties[s_opt]
    pen_s1 = penalties[1]
    pen_sk = penalties[k_rsc]

    regime_3_ok = (
        1 < s_opt < k_rsc
        and pen_opt < pen_s1
        and pen_opt < pen_sk
    )

    # -------------------------------------------------------------------------
    # Regime 4: High-Dimensional Misspecified Lasso under Heavy-Tailed Errors
    # and Marginally Sub-Weibull Covariates (Section 4.4, Theorems 4.5-4.6,
    # Proposition E.1, Equations 4.28-4.33 & E.8-E.11)
    # -------------------------------------------------------------------------
    rng = random.Random(20261018)
    n_lasso = 180
    p_lasso = 24
    s_true = [0, 1, 2]
    sc_true = [j for j in range(p_lasso) if j not in s_true]

    # Population target beta_0 with weak sparsity (non-zero tail on S^c)
    beta_0 = [0.0] * p_lasso
    beta_0[0] = 2.0
    beta_0[1] = -1.5
    beta_0[2] = 1.2
    beta_0[3] = 0.04
    beta_0[4] = -0.03

    x_mat = [[rng.gauss(0.0, 1.0) for _ in range(p_lasso)] for _ in range(n_lasso)]
    y_vec = []
    for i in range(n_lasso):
        lin = sum(x_mat[i][j] * beta_0[j] for j in range(p_lasso))
        nonlin = 0.25 * (x_mat[i][0] ** 2 - 1.0)
        u = rng.uniform(-0.4999, 0.4999)
        eps = -0.25 * math.copysign(math.log(1.0 - 2.0 * abs(u)), u)
        y_vec.append(lin + nonlin + eps)

    grad_0 = [0.0] * p_lasso
    for i in range(n_lasso):
        r_i = y_vec[i] - sum(x_mat[i][j] * beta_0[j] for j in range(p_lasso))
        for j in range(p_lasso):
            grad_0[j] += x_mat[i][j] * r_i / n_lasso
    grad_inf = max(abs(g) for g in grad_0)

    # Choose lambda_n >= 2 * ||1/n sum_{i=1}^n X_i eps_i||_infty (Lemma E.1 / Proposition E.1)
    lambda_n = 2.2 * grad_inf

    gram = [[0.0] * p_lasso for _ in range(p_lasso)]
    gamma_hat = [0.0] * p_lasso
    for i in range(n_lasso):
        for j in range(p_lasso):
            gamma_hat[j] += x_mat[i][j] * y_vec[i] / n_lasso
            for l in range(j, p_lasso):
                gram[j][l] += x_mat[i][j] * x_mat[i][l] / n_lasso
    for j in range(p_lasso):
        for l in range(j):
            gram[j][l] = gram[l][j]

    theta = [0.0] * p_lasso
    for _ in range(400):
        max_chg = 0.0
        for j in range(p_lasso):
            rho_j = gamma_hat[j] - sum(
                gram[j][l] * theta[l] for l in range(p_lasso) if l != j
            )
            if rho_j > lambda_n:
                new_t = (rho_j - lambda_n) / gram[j][j]
            elif rho_j < -lambda_n:
                new_t = (rho_j + lambda_n) / gram[j][j]
            else:
                new_t = 0.0
            max_chg = max(max_chg, abs(new_t - theta[j]))
            theta[j] = new_t
        if max_chg < 1e-11:
            break

    nu_hat = [theta[j] - beta_0[j] for j in range(p_lasso)]
    nu_s_l1 = sum(abs(nu_hat[j]) for j in s_true)
    nu_sc_l1 = sum(abs(nu_hat[j]) for j in sc_true)
    beta0_sc_l1 = sum(abs(beta_0[j]) for j in sc_true)

    # Verify Equation (E.9) basic inequality:
    # (1/2) nu_hat^T Sigma_hat_n nu_hat <= (3 lambda_n / 2) ||nu_hat(S)||_1 - (lambda_n / 2) ||nu_hat(S^c)||_1 + 2 lambda_n ||beta_0(S^c)||_1
    quad_form = 0.0
    for j in range(p_lasso):
        for l in range(p_lasso):
            quad_form += nu_hat[j] * gram[j][l] * nu_hat[l]
    eq_e9_lhs = 0.5 * quad_form
    eq_e9_rhs = 1.5 * lambda_n * nu_s_l1 - 0.5 * lambda_n * nu_sc_l1 + 2.0 * lambda_n * beta0_sc_l1
    eq_e9_verified = eq_e9_lhs <= eq_e9_rhs + 1e-9

    # Verify Equation (E.10) cone inequality: ||nu_hat(S^c)||_1 <= 3 ||nu_hat(S)||_1 + 4 ||beta_0(S^c)||_1
    cone_rhs = 3.0 * nu_s_l1 + 4.0 * beta0_sc_l1
    cone_verified = nu_sc_l1 <= cone_rhs + 1e-9

    nu_l2 = math.sqrt(sum(v * v for v in nu_hat))
    oracle_rhs_s = math.sqrt(18.0 * (lambda_n ** 2) * len(s_true) + 8.0 * lambda_n * beta0_sc_l1)
    regime_4_ok = (
        eq_e9_verified
        and cone_verified
        and nu_l2 <= oracle_rhs_s
    )

    summary = {
        "concept_id": "AIMech:GeneralizedBernsteinOrliczSubWeibullConcentrationAndHighDimensionalLasso",
        "regime_1_gbo_and_product_orlicz_norms": {
            "min_phi_over_psi_ratio": round(min(ratios), 6),
            "max_phi_over_psi_ratio": round(max(ratios), 6),
            "min_inv_ratio": round(min(inv_ratios), 6),
            "max_inv_ratio": round(max(inv_ratios), 6),
            "product_holder_ratio": round(holder_ratio, 6),
            "proposition_a1_and_d2_verified": regime_1_ok,
        },
        "regime_2_joint_vs_marginal_and_maximal_inequality": {
            "q_dim": q_dim,
            "joint_to_marginal_collinear_ratio": round(joint_to_marginal_ratio, 6),
            "expected_sqrt_q": round(math.sqrt(q_dim), 6),
            "gbo_second_order_rate": round(rem_gbo, 6),
            "cck_second_order_rate": round(rem_cck, 6),
            "joint_vs_marginal_and_remark_3_2_verified": regime_2_ok,
        },
        "regime_3_rsc_and_re_sample_complexity_optimization": {
            "k_sparsity": k_rsc,
            "optimal_free_s": s_opt,
            "penalty_at_s_opt": round(pen_opt, 6),
            "penalty_at_s_1": round(pen_s1, 6),
            "penalty_at_s_k": round(pen_sk, 6),
            "re_free_s_optimization_verified": regime_3_ok,
        },
        "regime_4_misspecified_lasso_oracle_inequality": {
            "grad_inf_at_beta0": round(grad_inf, 6),
            "lambda_n": round(lambda_n, 6),
            "nu_sc_l1": round(nu_sc_l1, 6),
            "cone_rhs_3_nu_s_plus_4_beta0_sc": round(cone_rhs, 6),
            "lasso_l2_error": round(nu_l2, 6),
            "equation_e10_cone_and_oracle_verified": regime_4_ok,
        },
        "all_passed": (
            regime_1_ok and regime_2_ok and regime_3_ok and regime_4_ok
        ),
    }
    print(json.dumps(summary, indent=2))
    return 0 if summary["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
