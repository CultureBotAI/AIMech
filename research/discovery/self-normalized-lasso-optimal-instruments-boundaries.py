#!/usr/bin/env python3
"""Constructed boundary & verification script for Round 266:
Self-Normalized Heteroscedastic Lasso and Post-Lasso Optimal Instrumental Variables
and Weak-Identification Sup-Score Inference
(Belloni, Chen, Chernozhukov, & Hansen 2012, Econometrica 80(6):2369-2429,
DOI:10.3982/ECTA9626, arXiv:1010.4345v5).

Verifies:
1. Section 2.3 (Eq. 2.4-2.7), Section 3.2 (Eq. 3.13), Algorithm A.1 (Eq. A.21), and Lemma 5:
   - Self-normalized score vector S_l = 2 E_n[(Upsilon_hat^0_l)^{-1} f_i v_{il}] and moderate-deviation
     penalty level lambda = 2 c sqrt(n) Phi^{-1}(1 - gamma / (2 k_e p)).
   - Iterative refinement of feasible penalty loadings gamma_hat_{lj} (Algorithm A.1) converging
     to the ideal heteroscedasticity-robust loadings gamma_hat^0_{lj} = sqrt(E_n[f_{ij}^2 v_{il}^2]).
2. Lemma 6 (Eq. C.22-C.25) and Lemma 8 (p. 39-40):
   - Exact KKT pre-sparsity identity sqrt(m_hat_l) lambda = 2 ||(Upsilon_hat_l^{-1} F'(d_l - F beta_hat_{lL}))_{T_hat_l \\ T_l}||_2.
   - Deterministic prediction-norm and weighted l_1 error bounds under approximate sparsity
     (Condition AS, Eq. 2.2), and Post-Lasso bias reduction over Lasso.
3. Section 2.4 & Theorem 3 (Eq. 2.10-2.11):
   - Optimal-instrument Post-Lasso IV estimator alpha_hat = E_n[D_hat_i d_i']^{-1} E_n[D_hat_i y_i]
     and heteroscedasticity-consistent variance estimator Q_hat^{-1} Omega_hat Q_hat^{-1},
     outperforming naive many-instrument 2SLS under endogeneity.
4. Section 4.2 & Theorem 5 (Eq. 4.19, p. 22-23):
   - Weak-identification-robust Sup-Score statistic Lambda_a and exact Inverse Lasso equivalence:
     {a : Lambda_a <= Lambda(1 - gamma)} == {a : beta_hat_a(2 Lambda(1 - gamma)) == 0}.
"""

from __future__ import annotations

import json
import math
import random


def norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def norm_ppf(p: float) -> float:
    lo, hi = -8.0, 8.0
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if norm_cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def solve_weighted_lasso_cd(
    F: list[list[float]],
    d_vec: list[float],
    lam_over_n: float,
    loadings: list[float],
    max_iter: int = 1500,
    tol: float = 1e-11,
) -> list[float]:
    """Minimize E_n[(d_i - f_i' beta)^2] + (lam/n) sum_j loadings[j] |beta_j|
    via coordinate descent.
    First-order optimality for beta_j != 0:
    2 E_n[f_{ij} (d_i - f_i' beta)] = (lam/n) loadings[j] sgn(beta_j)."""
    n = len(F)
    p = len(F[0])
    F_sq_n = [sum(F[i][j] ** 2 for i in range(n)) / n for j in range(p)]
    beta = [0.0] * p
    r = d_vec[:]

    for _ in range(max_iter):
        max_diff = 0.0
        for j in range(p):
            if F_sq_n[j] < 1e-15:
                continue
            # Partial residual correlation c_j = E_n[f_{ij} (r_i + f_{ij} beta_j)]
            corr_j = sum(F[i][j] * r[i] for i in range(n)) / n + F_sq_n[j] * beta[j]
            thresh = 0.5 * lam_over_n * loadings[j]
            if corr_j > thresh:
                b_new = (corr_j - thresh) / F_sq_n[j]
            elif corr_j < -thresh:
                b_new = (corr_j + thresh) / F_sq_n[j]
            else:
                b_new = 0.0
            diff = b_new - beta[j]
            if abs(diff) > max_diff:
                max_diff = abs(diff)
            if diff != 0.0:
                for i in range(n):
                    r[i] -= F[i][j] * diff
                beta[j] = b_new
        if max_diff < tol:
            break
    return beta


def ols_on_support(
    F: list[list[float]], d_vec: list[float], support: list[int]
) -> list[float]:
    n = len(F)
    p = len(F[0])
    if not support:
        return [0.0] * p
    k = len(support)
    G = [
        [sum(F[i][support[a]] * F[i][support[b]] for i in range(n)) / n for b in range(k)]
        for a in range(k)
    ]
    rhs = [sum(F[i][support[a]] * d_vec[i] for i in range(n)) / n for a in range(k)]
    # Gauss-Jordan elimination
    A = [G[a][:] + [rhs[a]] for a in range(k)]
    for col in range(k):
        piv = max(range(col, k), key=lambda r: abs(A[r][col]))
        A[col], A[piv] = A[piv], A[col]
        div = A[col][col]
        for j in range(col, k + 1):
            A[col][j] /= div
        for r in range(k):
            if r != col:
                fac = A[r][col]
                for j in range(col, k + 1):
                    A[r][j] -= fac * A[col][j]
    beta = [0.0] * p
    for a, j_idx in enumerate(support):
        beta[j_idx] = A[a][k]
    return beta


def verify_algorithm_a1_lemma6_8_and_theorem3_5() -> dict[str, object]:
    rng = random.Random(201211)
    n, p = 90, 70
    # Generate instrument matrix F with toeplitz-like correlation
    F = [[0.0] * p for _ in range(n)]
    for i in range(n):
        z_prev = 0.0
        for j in range(p):
            z_curr = 0.4 * z_prev + math.sqrt(1.0 - 0.16) * rng.gauss(0.0, 1.0)
            F[i][j] = z_curr
            z_prev = z_curr

    # Normalize columns so E_n[f_{ij}^2] = 1
    for j in range(p):
        msq = sum(F[i][j] ** 2 for i in range(n)) / n
        scale = 1.0 / math.sqrt(msq)
        for i in range(n):
            F[i][j] *= scale

    # Approximately sparse optimal instrument (Condition AS, Eq. 2.2):
    # D_i = f_i' beta_0 + a_i with support T = {0, 1, 2}, s = 3, and small tail a_i
    T_true = [0, 1, 2]
    T_set = set(T_true)
    s_card = len(T_true)
    beta_0 = [0.0] * p
    beta_0[0] = 1.0
    beta_0[1] = 0.85
    beta_0[2] = 0.70
    a_approx = [
        sum(0.02 * (0.5 ** m) * F[i][3 + m] for m in range(5)) for i in range(n)
    ]
    c_s = math.sqrt(sum(a_i * a_i for a_i in a_approx) / n)
    D_true = [
        sum(F[i][j] * beta_0[j] for j in range(p)) + a_approx[i] for i in range(n)
    ]

    # Generate heteroscedastic, correlated endogenous first-stage error v_i and structural error eps_i
    alpha_0 = 1.5
    v_err = []
    eps_err = []
    for i in range(n):
        het_scale = 0.65 * math.sqrt(1.0 + 0.35 * (F[i][0] ** 2 + F[i][1] ** 2))
        u_common = rng.gauss(0.0, 1.0)
        v_i = het_scale * (0.75 * u_common + math.sqrt(1.0 - 0.75 ** 2) * rng.gauss(0.0, 1.0))
        e_i = het_scale * (0.75 * u_common + math.sqrt(1.0 - 0.75 ** 2) * rng.gauss(0.0, 1.0))
        v_err.append(v_i)
        eps_err.append(e_i)

    d_endog = [D_true[i] + v_err[i] for i in range(n)]
    y_resp = [alpha_0 * d_endog[i] + eps_err[i] for i in range(n)]

    # Ideal penalty loadings Upsilon^0 (Section 2.3): gamma^0_j = sqrt(E_n[f_{ij}^2 v_i^2])
    gamma_ideal = [
        math.sqrt(sum((F[i][j] ** 2) * (v_err[i] ** 2) for i in range(n)) / n)
        for j in range(p)
    ]

    # Self-normalized score vector S = 2 E_n[(Upsilon^0)^{-1} f_i v_i]
    score_S = [
        2.0 * (sum(F[i][j] * v_err[i] for i in range(n)) / n) / gamma_ideal[j]
        for j in range(p)
    ]
    score_inf = max(abs(x) for x in score_S)

    # Penalty level (Eq. 2.7): lambda = 2 * c * sqrt(n) * Phi^{-1}(1 - gamma / (2 * p))
    c_pen = 1.1
    gamma_conf = 0.1 / math.log(max(p, n))
    lam = 2.0 * c_pen * math.sqrt(n) * norm_ppf(1.0 - gamma_conf / (2.0 * p))
    lam_over_n = lam / n

    # Algorithm A.1 (Eq. A.21): initial and K=3 refined penalty loadings
    d_mean = sum(d_endog) / n
    gamma_init = [
        math.sqrt(sum((F[i][j] ** 2) * ((d_endog[i] - d_mean) ** 2) for i in range(n)) / n)
        for j in range(p)
    ]
    gamma_curr = gamma_init[:]
    beta_L = [0.0] * p
    beta_PL = [0.0] * p

    gamma_used = gamma_init[:]
    for _ in range(4):
        gamma_used = gamma_curr[:]
        beta_L = solve_weighted_lasso_cd(F, d_endog, lam_over_n, gamma_used)
        supp_L = [j for j in range(p) if abs(beta_L[j]) > 1e-7]
        beta_PL = ols_on_support(F, d_endog, supp_L)
        v_hat = [
            d_endog[i] - sum(F[i][j] * beta_PL[j] for j in range(p)) for i in range(n)
        ]
        gamma_curr = [
            math.sqrt(sum((F[i][j] ** 2) * (v_hat[i] ** 2) for i in range(n)) / n)
            for j in range(p)
        ]

    # Check asymptotic validity condition (3.13): l <= gamma_curr[j] / gamma_ideal[j] <= u
    ratios_refined = [gamma_curr[j] / gamma_ideal[j] for j in range(p)]
    ratios_init = [gamma_init[j] / gamma_ideal[j] for j in range(p)]
    l_load = min(1.0, min(ratios_refined))
    u_load = max(1.0, max(ratios_refined))
    max_dev_init = max(abs(r - 1.0) for r in ratios_init)
    max_dev_refined = max(abs(r - 1.0) for r in ratios_refined)

    # Check Lemma 8 exact KKT pre-sparsity identity on T_hat \ T:
    # sqrt(m_hat) * lambda = 2 * || (Upsilon_hat^{-1} F'(d - F beta_L))_{T_hat \ T} ||_2
    supp_L = [j for j in range(p) if abs(beta_L[j]) > 1e-7]
    false_pos = [j for j in supp_L if j not in T_set]
    m_hat = len(false_pos)
    res_L = [d_endog[i] - sum(F[i][j] * beta_L[j] for j in range(p)) for i in range(n)]
    kkt_lhs = math.sqrt(m_hat) * lam_over_n
    kkt_rhs = 2.0 * math.sqrt(
        sum(
            ((sum(F[i][j] * res_L[i] for i in range(n)) / n) / gamma_used[j]) ** 2
            for j in false_pos
        )
    )
    lemma8_kkt_identity_err = abs(kkt_lhs - kkt_rhs)

    # Prediction norm errors ||D_hat - D||_{2,n} for Lasso and Post-Lasso
    D_hat_L = [sum(F[i][j] * beta_L[j] for j in range(p)) for i in range(n)]
    D_hat_PL = [sum(F[i][j] * beta_PL[j] for j in range(p)) for i in range(n)]
    pred_err_L = math.sqrt(sum((D_hat_L[i] - D_true[i]) ** 2 for i in range(n)) / n)
    pred_err_PL = math.sqrt(sum((D_hat_PL[i] - D_true[i]) ** 2 for i in range(n)) / n)

    # Verify Lemma 6 bound (Eq. C.24):
    # ||f_i'(beta_L - beta_0)||_{2,n} <= (u + 1/c) * lam * sqrt(s) / (n * kappa_{c0}) + 2 * c_s
    delta_L = [beta_L[j] - beta_0[j] for j in range(p)]
    f_delta_norm = math.sqrt(
        sum((sum(F[i][j] * delta_L[j] for j in range(p))) ** 2 for i in range(n)) / n
    )
    weighted_l1_T = sum(gamma_ideal[j] * abs(delta_L[j]) for j in T_true)
    # Empirical restricted eigenvalue at delta_L
    kappa_emp = math.sqrt(s_card) * f_delta_norm / max(weighted_l1_T, 1e-12)
    lemma6_rhs = (u_load + 1.0 / c_pen) * lam_over_n * math.sqrt(s_card) / kappa_emp + 2.0 * c_s

    # Section 2.4 & Theorem 3: Compare Post-Lasso IV estimator alpha_hat_PL vs naive all-40 2SLS
    alpha_hat_PL = (sum(D_hat_PL[i] * y_resp[i] for i in range(n)) / n) / (
        sum(D_hat_PL[i] * d_endog[i] for i in range(n)) / n
    )
    # Naive 2SLS using all p=70 instruments
    beta_ols_all = ols_on_support(F, d_endog, list(range(p)))
    D_hat_2sls = [sum(F[i][j] * beta_ols_all[j] for j in range(p)) for i in range(n)]
    pred_err_2sls = math.sqrt(
        sum((D_hat_2sls[i] - D_true[i]) ** 2 for i in range(n)) / n
    )
    alpha_hat_2sls = (sum(D_hat_2sls[i] * y_resp[i] for i in range(n)) / n) / (
        sum(D_hat_2sls[i] * d_endog[i] for i in range(n)) / n
    )
    alpha_hat_ols = (sum(d_endog[i] * y_resp[i] for i in range(n)) / n) / (
        sum(d_endog[i] ** 2 for i in range(n)) / n
    )

    # Heteroscedasticity-consistent variance estimator (Eq. 2.11): Q_hat^{-1} Omega_hat Q_hat^{-1}
    eps_hat_PL = [y_resp[i] - d_endog[i] * alpha_hat_PL for i in range(n)]
    Q_hat = sum(D_hat_PL[i] ** 2 for i in range(n)) / n
    Omega_hat = sum((eps_hat_PL[i] ** 2) * (D_hat_PL[i] ** 2) for i in range(n)) / n
    se_hat_PL = math.sqrt((Omega_hat / (Q_hat ** 2)) / n)
    t_stat_alpha0 = abs(alpha_hat_PL - alpha_0) / se_hat_PL

    # Section 4.2 & Theorem 5 (p. 22-23): Sup-Score statistic Lambda_a and Inverse Lasso equivalence
    # Test over a grid of candidate values a: check that Lambda_a <= Lambda_crit iff beta_hat_a == 0
    lam_crit = c_pen * math.sqrt(n) * norm_ppf(1.0 - gamma_conf / (2.0 * p))
    inv_lasso_lam_over_n = 2.0 * lam_crit / n

    def compute_sup_score_and_inv_lasso(a_val: float) -> tuple[float, float]:
        u_a = [y_resp[i] - d_endog[i] * a_val for i in range(n)]
        gamma_a = [
            math.sqrt(sum((u_a[i] ** 2) * (F[i][j] ** 2) for i in range(n)) / n)
            for j in range(p)
        ]
        sup_score = max(
            abs(sum(u_a[i] * F[i][j] for i in range(n))) / (n * gamma_a[j])
            for j in range(p)
        ) * n
        beta_a = solve_weighted_lasso_cd(F, u_a, inv_lasso_lam_over_n, gamma_a)
        max_beta_a = max(abs(b) for b in beta_a)
        return sup_score, max_beta_a

    sup_score_true, max_beta_true = compute_sup_score_and_inv_lasso(alpha_0)
    sup_score_false, max_beta_false = compute_sup_score_and_inv_lasso(alpha_0 + 0.8)

    # Check exact equivalence across 25 grid points around the boundary
    equivalence_mismatches = 0
    for step in range(25):
        a_cand = alpha_0 - 0.6 + step * 0.05
        sc, mb = compute_sup_score_and_inv_lasso(a_cand)
        in_conf_region = sc <= lam_crit
        is_zero_lasso = mb < 1e-8
        if in_conf_region != is_zero_lasso:
            equivalence_mismatches += 1

    return {
        "score_dominated_by_lambda": lam_over_n > c_pen * score_inf,
        "l_load": l_load,
        "u_load": u_load,
        "refinement_improves_loadings": max_dev_refined < max_dev_init,
        "lemma8_kkt_identity_err": lemma8_kkt_identity_err,
        "pred_err_PL": pred_err_PL,
        "pred_err_L": pred_err_L,
        "pred_err_2sls": pred_err_2sls,
        "post_lasso_reduces_pred_err": pred_err_PL < pred_err_L,
        "post_lasso_beats_naive_2sls_first_stage": pred_err_PL < 0.3 * pred_err_2sls,
        "lemma6_bound_holds": f_delta_norm <= lemma6_rhs + 1e-12,
        "iv_err_post_lasso": abs(alpha_hat_PL - alpha_0),
        "t_stat_alpha0": t_stat_alpha0,
        "true_alpha0_in_sup_score_ci": sup_score_true <= lam_crit,
        "true_alpha0_inverse_lasso_zero": max_beta_true == 0.0,
        "false_alpha_excluded_from_ci": sup_score_false > lam_crit,
        "false_alpha_inverse_lasso_nonzero": max_beta_false > 0.0,
        "inverse_lasso_equivalence_mismatches": equivalence_mismatches,
    }


def main() -> None:
    res = verify_algorithm_a1_lemma6_8_and_theorem3_5()
    summary = {k: round(v, 8) if isinstance(v, float) else v for k, v in res.items()}
    print(json.dumps(summary, indent=2))

    assert res["score_dominated_by_lambda"] is True
    assert 0.85 < res["l_load"] <= 1.0 <= res["u_load"] < 1.2
    assert res["refinement_improves_loadings"] is True
    assert res["lemma8_kkt_identity_err"] < 1e-9
    assert res["post_lasso_reduces_pred_err"] is True
    assert res["post_lasso_beats_naive_2sls_first_stage"] is True
    assert res["lemma6_bound_holds"] is True
    assert res["iv_err_post_lasso"] < 0.12
    assert res["t_stat_alpha0"] < 1.96
    assert res["true_alpha0_in_sup_score_ci"] is True
    assert res["true_alpha0_inverse_lasso_zero"] is True
    assert res["false_alpha_excluded_from_ci"] is True
    assert res["false_alpha_inverse_lasso_nonzero"] is True
    assert res["inverse_lasso_equivalence_mismatches"] == 0


if __name__ == "__main__":
    main()
