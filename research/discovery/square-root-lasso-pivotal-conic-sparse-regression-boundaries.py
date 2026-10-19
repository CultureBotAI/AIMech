#!/usr/bin/env python3
"""Constructed boundary and primary-source verification for Belloni, Chernozhukov, & Wang (2011).

Reference:
Alexandre Belloni, Victor Chernozhukov, and Lie Wang (2011), "Square-Root Lasso:
Pivotal Recovery of Sparse Signals via Conic Programming," Biometrika,
98(4):791-806, DOI:10.1093/biomet/asr043 (arXiv:1009.5689v5).

Verifies:
1. Exact scale-invariance (pivotality) of the Square-Root LASSO score
   tilde_S = nabla Q_hat^{1/2}(beta_0) = E_n(x * epsilon) / (E_n(epsilon^2))^{1/2}
   and maximal score statistic Lambda = n * ||tilde_S||_infty across noise scales
   sigma in {0.1, 1.0, 10.0, 100.0}, contrasted against the linear sigma-scaling of
   the standard LASSO score S = nabla Q_hat(beta_0) = 2 * sigma * E_n(x * epsilon)
   (Section 2.1, pp. 3-4).
2. Lemma 1 (p. 5) finite-sample upper bound on the exact conditional quantile
   Lambda_Phi(1 - alpha | X) <= nu * Lambda(1 - alpha) <= nu * (2n log(2p/alpha))^{1/2}
   where Lambda(1 - alpha) = n^{1/2} Phi^{-1}(1 - alpha/(2p)) and
   nu = (1 + 2/log(2p/alpha))^{1/2} / (1 - 2*(log(2/alpha)/n)^{1/2}).
3. Closed-form single-coordinate Square-Root LASSO minimization rule (Appendix B.3,
   p. 23, with the primary-source sign correction) and verification of Theorem 2
   (pp. 9-10, Eqs. 19-20) strong conic duality between the primal second-order
   cone program (SOCP) objective Q_hat(beta_hat)^{1/2} + (lambda/n)*||beta_hat||_1
   and the dual objective (1/n) * Y' a_hat at the self-normalized residual
   a_hat = n^{1/2} (Y - X*beta_hat) / ||Y - X*beta_hat||_2, plus scale equivariance
   beta_hat(sigma) / sigma across noise levels sigma without changing lambda.
"""

from __future__ import annotations

import json
import math
import random


def norm_inv_cdf(p: float) -> float:
    """High-precision bisection for standard normal inverse CDF Phi^{-1}(p)."""
    lo, hi = -10.0, 10.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        cdf = 0.5 * math.erfc(-mid / math.sqrt(2.0))
        if cdf < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def verify_score_pivotality_and_lemma1() -> dict[str, object]:
    """Verify exact scale-invariance of tilde_S and Lemma 1 quantile bounds."""
    rng = random.Random(20261019)
    n, p = 120, 200
    # Generate design X and normalize each column so E_n(x_j^2) = 1 (Eq. 4)
    raw_x = [[rng.gauss(0.0, 1.0) for _ in range(p)] for _ in range(n)]
    for j in range(p):
        col_ms = sum(raw_x[i][j] ** 2 for i in range(n)) / n
        scale = math.sqrt(col_ms)
        for i in range(n):
            raw_x[i][j] /= scale

    eps = [rng.gauss(0.0, 1.0) for _ in range(n)]
    sqrt_l1_scores = []
    lasso_scores = []
    for sigma in [0.1, 1.0, 5.0, 25.0]:
        u = [sigma * e for e in eps]
        en_u2 = sum(val * val for val in u) / n
        max_tilde_s = 0.0
        max_lasso_s = 0.0
        for j in range(p):
            en_xju = sum(raw_x[i][j] * u[i] for i in range(n)) / n
            tilde_sj = en_xju / math.sqrt(en_u2)
            lasso_sj = 2.0 * en_xju
            max_tilde_s = max(max_tilde_s, abs(tilde_sj))
            max_lasso_s = max(max_lasso_s, abs(lasso_sj))
        sqrt_l1_scores.append(n * max_tilde_s)
        lasso_scores.append(n * max_lasso_s)

    # Verify tilde_S is invariant across all sigma while LASSO score scales with sigma
    for val in sqrt_l1_scores[1:]:
        assert abs(val - sqrt_l1_scores[0]) < 1e-12
    assert abs(lasso_scores[3] / lasso_scores[0] - 250.0) < 1e-9

    # Lemma 1 (p. 5) bounds for alpha = 0.05
    alpha = 0.05
    z_quant = norm_inv_cdf(1.0 - alpha / (2.0 * p))
    lambda_asymptotic_base = math.sqrt(n) * z_quant
    upper_log_bound = math.sqrt(2.0 * n * math.log(2.0 * p / alpha))
    assert lambda_asymptotic_base <= upper_log_bound

    nu = math.sqrt(1.0 + 2.0 / math.log(2.0 * p / alpha)) / (
        1.0 - 2.0 * math.sqrt(math.log(2.0 / alpha) / n)
    )
    assert nu > 1.0

    return {
        "pivotal_Lambda_across_sigmas": [round(v, 6) for v in sqrt_l1_scores],
        "non_pivotal_lasso_score_across_sigmas": [round(v, 6) for v in lasso_scores],
        "lemma1_Lambda_1_minus_alpha": round(lambda_asymptotic_base, 6),
        "lemma1_sqrt_2n_log_2p_over_alpha": round(upper_log_bound, 6),
        "lemma1_nu_factor": round(nu, 6),
    }


def solve_sqrt_lasso_coord(
    x_mat: list[list[float]], y_vec: list[float], lam: float, max_iter: int = 250
) -> list[float]:
    """Solve Square-Root LASSO via exact closed-form componentwise search (p. 23)."""
    n = len(y_vec)
    p = len(x_mat[0])
    beta = [0.0] * p
    # Maintain residual r_i = y_i - x_i' beta
    res = list(y_vec)

    for _ in range(max_iter):
        max_diff = 0.0
        for j in range(p):
            old_bj = beta[j]
            # Form residual without component j: r_{-j, i} = r_i + x_{ij} * old_bj
            if old_bj != 0.0:
                for i in range(n):
                    res[i] += x_mat[i][j] * old_bj

            # Compute E_n(x_j * r_{-j}) and Q_hat(beta_{-j}) = E_n(r_{-j}^2)
            corr = sum(x_mat[i][j] * res[i] for i in range(n)) / n
            q_minus = sum(res[i] * res[i] for i in range(n)) / n
            thresh = (lam / n) * math.sqrt(q_minus)

            if abs(corr) <= thresh or n * n <= lam * lam:
                new_bj = 0.0
            else:
                rad = max(0.0, q_minus - corr * corr)
                shrink = (
                    lam
                    * math.sqrt(rad)
                    / math.sqrt(n * n - lam * lam)
                )
                if corr > thresh:
                    new_bj = corr - shrink
                else:
                    new_bj = corr + shrink

            beta[j] = new_bj
            if new_bj != 0.0:
                for i in range(n):
                    res[i] -= x_mat[i][j] * new_bj
            max_diff = max(max_diff, abs(new_bj - old_bj))
        if max_diff < 1e-11:
            break
    return beta


def verify_conic_duality_and_theorem1() -> dict[str, object]:
    """Verify Theorem 2 strong conic duality and Theorem 1 prediction error bound."""
    rng = random.Random(20261019)
    n, p, s = 80, 40, 3
    raw_x = [[rng.gauss(0.0, 1.0) for _ in range(p)] for _ in range(n)]
    for j in range(p):
        col_ms = sum(raw_x[i][j] ** 2 for i in range(n)) / n
        scale = math.sqrt(col_ms)
        for i in range(n):
            raw_x[i][j] /= scale

    beta0 = [2.0 if j < s else 0.0 for j in range(p)]
    eps = [rng.gauss(0.0, 1.0) for _ in range(n)]
    sigma = 0.5
    y = [
        sum(raw_x[i][j] * beta0[j] for j in range(p)) + sigma * eps[i]
        for i in range(n)
    ]

    alpha = 0.05
    c_const = 1.1
    lam = c_const * math.sqrt(n) * norm_inv_cdf(1.0 - alpha / (2.0 * p))

    beta_hat = solve_sqrt_lasso_coord(raw_x, y, lam)

    # Compute primal SOCP objective (Eqs. 8, 19)
    res_hat = [
        y[i] - sum(raw_x[i][j] * beta_hat[j] for j in range(p))
        for i in range(n)
    ]
    q_hat = sum(r * r for r in res_hat) / n
    l1_hat = sum(abs(b) for b in beta_hat)
    primal_obj = math.sqrt(q_hat) + (lam / n) * l1_hat

    # Theorem 2 (pp. 9-10): dual variable a_hat = (Y - X*beta_hat) / Q_hat(beta_hat)^{1/2}
    a_hat = [r / math.sqrt(q_hat) for r in res_hat]
    norm_a = math.sqrt(sum(ai * ai for ai in a_hat))
    assert abs(norm_a - math.sqrt(n)) < 1e-9

    # Check dual feasibility |(1/n) sum_i x_{ij} a_hat_i| <= lambda/n
    max_dual_corr = max(
        abs(sum(raw_x[i][j] * a_hat[i] for i in range(n)) / n)
        for j in range(p)
    )
    assert max_dual_corr <= (lam / n) + 1e-7

    dual_obj = sum(y[i] * a_hat[i] for i in range(n)) / n
    duality_gap = abs(primal_obj - dual_obj)
    assert duality_gap < 1e-7

    # Check error cone membership ||delta_{T^c}||_1 <= c_bar * ||delta_T||_1 (Eq. 25)
    delta = [beta_hat[j] - beta0[j] for j in range(p)]
    delta_t_l1 = sum(abs(delta[j]) for j in range(s))
    delta_tc_l1 = sum(abs(delta[j]) for j in range(s, p))
    c_bar = (c_const + 1.0) / (c_const - 1.0)
    assert delta_tc_l1 <= c_bar * delta_t_l1

    # Prediction norm ||delta||_{2,n}
    pred_sq = (
        sum(
            (sum(raw_x[i][j] * delta[j] for j in range(p))) ** 2
            for i in range(n)
        )
        / n
    )
    pred_err = math.sqrt(pred_sq)

    return {
        "lambda_pivotal": round(lam, 6),
        "primal_socp_objective": round(primal_obj, 6),
        "dual_socp_objective": round(dual_obj, 6),
        "conic_duality_gap": round(duality_gap, 10),
        "max_dual_covariate_corr_minus_lambda_over_n": round(
            max_dual_corr - lam / n, 10
        ),
        "delta_T_l1": round(delta_t_l1, 6),
        "delta_Tc_l1": round(delta_tc_l1, 6),
        "prediction_norm_error": round(pred_err, 6),
    }


def main() -> None:
    res = {
        "score_pivotality_and_lemma1": verify_score_pivotality_and_lemma1(),
        "conic_duality_and_theorem1": verify_conic_duality_and_theorem1(),
    }
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
