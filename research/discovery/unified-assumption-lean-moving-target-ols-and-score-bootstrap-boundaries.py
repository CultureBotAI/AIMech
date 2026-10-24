#!/usr/bin/env python3
"""Constructed boundary verification for Unified Assumption-Lean Moving-Target
OLS Linear Regression, Conservative Sandwich Variance, Score Bootstrap, and
Deterministic Master Inequality (Kuchibhotla, Brown, & Buja 2018,
arXiv:1809.10538v1).

Verifies using pure Python standard library:
1. Moving-Target Normal Equations and Score Covariance Gap K_n^* - K_n >= 0
   under i.n.i.d. / Fixed vs. i.i.d. Covariates (Sections 3-6.1, Equations 3-18):
   - In the unified independent non-identically distributed (i.n.i.d.) setting,
     the moving target beta_n = Sigma_n^(-1) Gamma_n satisfies the average
     normal equation (1/n) sum_{i=1}^n E[X_i (Y_i - X_i^T beta_n)] = 0, but
     individual summand means m_i = E[X_i (Y_i - X_i^T beta_n)] are non-zero
     under nonlinearity, creating a strictly positive semi-definite gap
     K_n^* - K_n = (1/n) sum_{i=1}^n m_i m_i^T >= 0.
   - In the i.i.d. random covariate setting, m_i = 0 for every i, so K_n^* = K_n.
2. Conservative Sandwich Estimator K_check_n ->_p K_n^* and Anderson's Lemma
   Coverage Conservativeness (Sections 6.1-6.3,7, Lemmas 6.1-6.2, Equations 18-27):
   - K_check_n = (1/n) sum_{i=1}^n X_i X_i^T (Y_i - X_i^T beta_hat_n)^2
     approximates K_n^* >= K_n, yielding conservative confidence intervals
     (coverage > 1 - alpha) in the i.n.i.d. nonlinear regime by Anderson's
     Lemma (Lemma 6.2) and asymptotically exact coverage in the i.i.d. regime.
3. Multiplier Score Bootstrap T_n^* and m-of-n Resampling Score Bootstrap T_m^*
   Bypassing Singular Pairs-Bootstrap Systems (Sections 6.2-6.4, Equations 20-28):
   - The estimated scores S_hat_i = X_i (Y_i - X_i^T beta_hat_n) satisfy
     sum_{i=1}^n S_hat_i = 0 identically.
   - Conditional on the data Z_n, both the Gaussian multiplier score bootstrap
     T_n^* = n^(-1/2) sum_{i=1}^n W_i S_hat_i and the m-of-n resampling score
     bootstrap T_m^* = m^(-1/2) sum_{j=1}^m S_hat_{I_j} have exact conditional
     mean 0 and covariance K_check_n without ever inverting a resampled design
     matrix (whereas x-y pairs bootstrap on a sparse binary indicator design
     suffers a non-zero singular matrix rate).
4. Deterministic Master Inequality for Linear Regression (Section 8, Theorem 8.1,
   Equations 30-32):
   - Whenever D_{2n}^Sigma = ||Sigma_hat_n - Sigma_n||_op <= Lambda_n / 2 with
     Lambda_n = lambda_min(Sigma_n), the estimator beta_hat_n satisfies both
     (1/2) ||L_n||_2 <= ||beta_hat_n - beta_n||_2 <= 2 ||L_n||_2 (Equation 30)
     and ||beta_hat_n - beta_n - L_n||_2 <= 2 D_{2n}^Sigma ||L_n||_2 / Lambda_n
     (Equation 31), where L_n = Sigma_n^(-1) (Gamma_hat_n - Sigma_hat_n beta_n).
"""

import json
import math
import random


def mat2_inv(m: list[list[float]]) -> list[list[float]]:
    det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    if abs(det) < 1e-12:
        raise ZeroDivisionError("Singular 2x2 matrix")
    return [
        [m[1][1] / det, -m[0][1] / det],
        [-m[1][0] / det, m[0][0] / det],
    ]


def mat2_vec(m: list[list[float]], v: list[float]) -> list[float]:
    return [
        m[0][0] * v[0] + m[0][1] * v[1],
        m[1][0] * v[0] + m[1][1] * v[1],
    ]


def mat2_mul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [
        [
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ],
        [
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ],
    ]


def sym2_eigvals(m: list[list[float]]) -> tuple[float, float]:
    tr = m[0][0] + m[1][1]
    det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    disc = max(0.0, tr * tr - 4.0 * det)
    s = math.sqrt(disc)
    return (0.5 * (tr - s), 0.5 * (tr + s))


def sym2_op_norm(m: list[list[float]]) -> float:
    l1, l2 = sym2_eigvals(m)
    return max(abs(l1), abs(l2))


def vec2_norm(v: list[float]) -> float:
    return math.sqrt(v[0] * v[0] + v[1] * v[1])


def main() -> None:
    rng = random.Random(20261018)

    # 1. Regime 1 & 2: Unified i.n.i.d. fixed-covariate nonlinear setting vs. i.i.d. setting
    n = 80
    xs_fixed = [[1.0, -2.0 + 4.0 * i / (n - 1)] for i in range(n)]
    # True nonlinear mean mu_i = 1.0 + 1.5 * x_i2 + 0.8 * (x_i2^2 - 1.3) and heteroskedastic variance sigma_i^2
    mus_fixed = [1.0 + 1.5 * x[1] + 0.8 * (x[1] * x[1] - 1.3) for x in xs_fixed]
    sig2_fixed = [0.25 + 0.1 * (x[1] * x[1]) for x in xs_fixed]

    sigma_n = [[0.0, 0.0], [0.0, 0.0]]
    gamma_n = [0.0, 0.0]
    for x, mu in zip(xs_fixed, mus_fixed):
        for r in range(2):
            gamma_n[r] += x[r] * mu / n
            for c in range(2):
                sigma_n[r][c] += x[r] * x[c] / n

    sigma_n_inv = mat2_inv(sigma_n)
    beta_n = mat2_vec(sigma_n_inv, gamma_n)

    # Individual score means m_i = x_i * (mu_i - x_i^T beta_n)
    m_vecs = []
    avg_m = [0.0, 0.0]
    k_n = [[0.0, 0.0], [0.0, 0.0]]
    k_n_star = [[0.0, 0.0], [0.0, 0.0]]
    for x, mu, s2 in zip(xs_fixed, mus_fixed, sig2_fixed):
        fit = x[0] * beta_n[0] + x[1] * beta_n[1]
        bias_i = mu - fit
        m_i = [x[0] * bias_i, x[1] * bias_i]
        m_vecs.append(m_i)
        avg_m[0] += m_i[0] / n
        avg_m[1] += m_i[1] / n
        # Var(X_i (Y_i - X_i^T beta_n)) = x_i x_i^T s2
        # E[X_i X_i^T (Y_i - X_i^T beta_n)^2] = x_i x_i^T (s2 + bias_i^2)
        for r in range(2):
            for c in range(2):
                k_n[r][c] += x[r] * x[c] * s2 / n
                k_n_star[r][c] += x[r] * x[c] * (s2 + bias_i * bias_i) / n

    assert vec2_norm(avg_m) < 1e-12, "Average normal equation must vanish"
    max_indiv_score_mean = max(vec2_norm(m) for m in m_vecs)
    assert max_indiv_score_mean > 0.5, "Individual score expectations must be non-zero under i.n.i.d. nonlinearity"

    gap_k = [
        [k_n_star[0][0] - k_n[0][0], k_n_star[0][1] - k_n[0][1]],
        [k_n_star[1][0] - k_n[1][0], k_n_star[1][1] - k_n[1][1]],
    ]
    gap_eig_min, gap_eig_max = sym2_eigvals(gap_k)
    assert gap_eig_min > 0.1, f"Expected K_n^* - K_n strictly PD, got min eig {gap_eig_min}"

    # True asymptotic variance AV_n = Sigma_n^(-1) K_n Sigma_n^(-1) vs conservative AV_n^* = Sigma_n^(-1) K_n^* Sigma_n^(-1)
    av_true = mat2_mul(mat2_mul(sigma_n_inv, k_n), sigma_n_inv)
    av_star = mat2_mul(mat2_mul(sigma_n_inv, k_n_star), sigma_n_inv)
    var_ratio_slope = av_true[1][1] / av_star[1][1]
    assert var_ratio_slope < 0.65, f"Expected AV_n(2,2)/AV_n^*(2,2) < 1, got {var_ratio_slope}"

    # Monte Carlo check of conservative t_2 test / CI coverage under i.n.i.d. fixed covariates
    n_mc = 800
    cov_95_inid = 0
    k_check_diffs = []
    for _ in range(n_mc):
        ys = [mu + rng.gauss(0.0, math.sqrt(s2)) for mu, s2 in zip(mus_fixed, sig2_fixed)]
        gamma_hat = [0.0, 0.0]
        for x, y in zip(xs_fixed, ys):
            gamma_hat[0] += x[0] * y / n
            gamma_hat[1] += x[1] * y / n
        beta_hat = mat2_vec(sigma_n_inv, gamma_hat)
        k_check = [[0.0, 0.0], [0.0, 0.0]]
        for x, y in zip(xs_fixed, ys):
            res = y - (x[0] * beta_hat[0] + x[1] * beta_hat[1])
            for r in range(2):
                for c in range(2):
                    k_check[r][c] += x[r] * x[c] * (res * res) / n
        k_check_diffs.append(sym2_op_norm([
            [k_check[0][0] - k_n_star[0][0], k_check[0][1] - k_n_star[0][1]],
            [k_check[1][0] - k_n_star[1][0], k_check[1][1] - k_n_star[1][1]],
        ]))
        av_tilde = mat2_mul(mat2_mul(sigma_n_inv, k_check), sigma_n_inv)
        t_stat = abs(math.sqrt(n) * (beta_hat[1] - beta_n[1]) / math.sqrt(av_tilde[1][1]))
        if t_stat <= 1.95996:
            cov_95_inid += 1

    emp_cov_inid = cov_95_inid / n_mc
    mean_k_check_diff = sum(k_check_diffs) / n_mc
    assert emp_cov_inid >= 0.965, f"Expected strictly conservative coverage (> 0.965) by Anderson's Lemma, got {emp_cov_inid}"

    # 3. Regime 3: Multiplier Score Bootstrap & Resampling Score Bootstrap vs Singular Pairs Bootstrap
    # Construct a dataset with a rare binary dummy covariate (3 out of 40 observations have x_i2 = 1)
    n_sparse = 40
    xs_sparse = [[1.0, 1.0 if i < 3 else 0.0] for i in range(n_sparse)]
    ys_sparse = [1.2 + 2.0 * x[1] + rng.gauss(0.0, 0.5) for x in xs_sparse]
    sig_sp = [[0.0, 0.0], [0.0, 0.0]]
    gam_sp = [0.0, 0.0]
    for x, y in zip(xs_sparse, ys_sparse):
        gam_sp[0] += x[0] * y / n_sparse
        gam_sp[1] += x[1] * y / n_sparse
        for r in range(2):
            for c in range(2):
                sig_sp[r][c] += x[r] * x[c] / n_sparse
    beta_hat_sp = mat2_vec(mat2_inv(sig_sp), gam_sp)
    s_hats = []
    k_check_sp = [[0.0, 0.0], [0.0, 0.0]]
    for x, y in zip(xs_sparse, ys_sparse):
        res = y - (x[0] * beta_hat_sp[0] + x[1] * beta_hat_sp[1])
        s_i = [x[0] * res, x[1] * res]
        s_hats.append(s_i)
        for r in range(2):
            for c in range(2):
                k_check_sp[r][c] += s_i[r] * s_i[c] / n_sparse

    sum_s_hat = [sum(s[0] for s in s_hats), sum(s[1] for s in s_hats)]
    assert vec2_norm(sum_s_hat) < 1e-12, "Estimated scores must sum to zero"

    # Check pairs bootstrap singularity rate vs score bootstrap zero singularity rate
    n_boot = 4000
    pairs_singular_count = 0
    mult_cov = [[0.0, 0.0], [0.0, 0.0]]
    resamp_cov = [[0.0, 0.0], [0.0, 0.0]]
    m_resamp = 60
    for _ in range(n_boot):
        # Pairs draw of size n_sparse
        idxs = [rng.randrange(n_sparse) for _ in range(n_sparse)]
        if sum(int(xs_sparse[idx][1]) for idx in idxs) == 0:
            pairs_singular_count += 1

        # Multiplier score bootstrap T_n^* = n^(-1/2) sum W_i S_hat_i
        t_mult = [0.0, 0.0]
        for s_i in s_hats:
            w_i = rng.gauss(0.0, 1.0)
            t_mult[0] += w_i * s_i[0] / math.sqrt(n_sparse)
            t_mult[1] += w_i * s_i[1] / math.sqrt(n_sparse)
        for r in range(2):
            for c in range(2):
                mult_cov[r][c] += t_mult[r] * t_mult[c] / n_boot

        # Resampling score bootstrap T_m^* = m^(-1/2) sum_{j=1}^m S_hat_{I_j}
        t_res = [0.0, 0.0]
        for _ in range(m_resamp):
            s_j = s_hats[rng.randrange(n_sparse)]
            t_res[0] += s_j[0] / math.sqrt(m_resamp)
            t_res[1] += s_j[1] / math.sqrt(m_resamp)
        for r in range(2):
            for c in range(2):
                resamp_cov[r][c] += t_res[r] * t_res[c] / n_boot

    pairs_singular_rate = pairs_singular_count / n_boot
    assert pairs_singular_rate > 0.02, f"Expected positive pairs-bootstrap singularity rate, got {pairs_singular_rate}"
    mult_cov_rel_err = sym2_op_norm([
        [mult_cov[0][0] - k_check_sp[0][0], mult_cov[0][1] - k_check_sp[0][1]],
        [mult_cov[1][0] - k_check_sp[1][0], mult_cov[1][1] - k_check_sp[1][1]],
    ]) / sym2_op_norm(k_check_sp)
    resamp_cov_rel_err = sym2_op_norm([
        [resamp_cov[0][0] - k_check_sp[0][0], resamp_cov[0][1] - k_check_sp[0][1]],
        [resamp_cov[1][0] - k_check_sp[1][0], resamp_cov[1][1] - k_check_sp[1][1]],
    ]) / sym2_op_norm(k_check_sp)
    assert mult_cov_rel_err < 0.06, f"mult_cov_rel_err={mult_cov_rel_err}"
    assert resamp_cov_rel_err < 0.06, f"resamp_cov_rel_err={resamp_cov_rel_err}"

    # 4. Regime 4: Deterministic Master Inequality (Theorem 8.1, Equations 30-32)
    lambda_n, _ = sym2_eigvals(sigma_n)
    assert lambda_n > 0.5
    max_ratio_eq30 = 0.0
    min_ratio_eq30 = 10.0
    max_lhs_over_rhs_eq31 = 0.0
    n_checked_det = 0
    for _ in range(300):
        # Perturb X_i slightly around xs_fixed so 0 < D_{2n}^Sigma <= Lambda_n / 2
        xs_real = [[1.0, x[1] + rng.uniform(-0.25, 0.25)] for x in xs_fixed]
        ys_real = [mu + rng.uniform(-0.8, 0.8) for mu in mus_fixed]
        sig_hat = [[0.0, 0.0], [0.0, 0.0]]
        gam_hat = [0.0, 0.0]
        for x, y in zip(xs_real, ys_real):
            gam_hat[0] += x[0] * y / n
            gam_hat[1] += x[1] * y / n
            for r in range(2):
                for c in range(2):
                    sig_hat[r][c] += x[r] * x[c] / n
        d2n_sigma = sym2_op_norm([
            [sig_hat[0][0] - sigma_n[0][0], sig_hat[0][1] - sigma_n[0][1]],
            [sig_hat[1][0] - sigma_n[1][0], sig_hat[1][1] - sigma_n[1][1]],
        ])
        if 1e-6 < d2n_sigma <= 0.5 * lambda_n:
            n_checked_det += 1
            beta_hat = mat2_vec(mat2_inv(sig_hat), gam_hat)
            diff_beta = [beta_hat[0] - beta_n[0], beta_hat[1] - beta_n[1]]
            norm_diff = vec2_norm(diff_beta)

            # Linearized term L_n = Sigma_n^(-1) (Gamma_hat_n - Sigma_hat_n beta_n)
            sig_hat_beta_n = mat2_vec(sig_hat, beta_n)
            score_avg = [gam_hat[0] - sig_hat_beta_n[0], gam_hat[1] - sig_hat_beta_n[1]]
            lin_term = mat2_vec(sigma_n_inv, score_avg)
            norm_lin = vec2_norm(lin_term)

            # Check Equation (30): 0.5 * norm_lin <= norm_diff <= 2.0 * norm_lin
            assert 0.5 * norm_lin - 1e-12 <= norm_diff <= 2.0 * norm_lin + 1e-12
            ratio_30 = norm_diff / norm_lin
            max_ratio_eq30 = max(max_ratio_eq30, ratio_30)
            min_ratio_eq30 = min(min_ratio_eq30, ratio_30)

            # Check Equation (31): ||beta_hat - beta_n - L_n||_2 <= 2 * d2n_sigma * norm_lin / lambda_n
            rem_vec = [diff_beta[0] - lin_term[0], diff_beta[1] - lin_term[1]]
            lhs_31 = vec2_norm(rem_vec)
            rhs_31 = 2.0 * d2n_sigma * norm_lin / lambda_n
            assert lhs_31 <= rhs_31 + 1e-12
            max_lhs_over_rhs_eq31 = max(max_lhs_over_rhs_eq31, lhs_31 / rhs_31)

    assert n_checked_det >= 250

    summary = {
        "concept_id": "AIMech:UnifiedAssumptionLeanMovingTargetLinearRegressionAndScoreBootstrap",
        "regime_1_moving_target_and_score_gap": {
            "average_normal_equation_norm": round(vec2_norm(avg_m), 12),
            "max_individual_score_mean_norm": round(max_indiv_score_mean, 6),
            "k_star_minus_k_min_eig": round(gap_eig_min, 6),
            "k_star_minus_k_max_eig": round(gap_eig_max, 6),
            "true_to_conservative_var_ratio_slope": round(var_ratio_slope, 6),
            "moving_target_gap_verified": True,
        },
        "regime_2_conservative_sandwich_and_anderson_lemma": {
            "mean_k_check_to_k_star_op_diff": round(mean_k_check_diff, 6),
            "empirical_95_coverage_inid": round(emp_cov_inid, 4),
            "conservative_coverage_verified": True,
        },
        "regime_3_score_bootstraps_vs_pairs_singularity": {
            "estimated_score_sum_norm": round(vec2_norm(sum_s_hat), 12),
            "pairs_bootstrap_singular_rate": round(pairs_singular_rate, 4),
            "score_bootstrap_singular_rate": 0.0,
            "multiplier_score_bootstrap_cov_rel_err": round(mult_cov_rel_err, 6),
            "resampling_score_bootstrap_cov_rel_err": round(resamp_cov_rel_err, 6),
            "score_bootstraps_verified": True,
        },
        "regime_4_deterministic_master_inequality": {
            "realizations_checked": n_checked_det,
            "lambda_min_sigma_n": round(lambda_n, 6),
            "min_ratio_eq30": round(min_ratio_eq30, 6),
            "max_ratio_eq30": round(max_ratio_eq30, 6),
            "max_lhs_over_rhs_eq31": round(max_lhs_over_rhs_eq31, 6),
            "theorem_8_1_verified": True,
        },
        "all_passed": True,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
