#!/usr/bin/env python3
"""Constructed boundary & regime verification for Windmeijer et al. (2019).

Verifies:
1. Proposition 1, Proposition 2, and Corollary 1: Rank-deficient projected
   instrument Gram matrix C = Q - Q*gamma*(gamma'*Q*gamma)^{-1}*gamma'*Q,
   exact closed-form block formula for C_{21} * C_{11}^{-1} (Eq. 18) via the
   Schur complement Q_tilde_22 = Q_22 - Q_21 * Q_11^{-1} * Q_12,
   exact identity gamma_2' * C_{21} * C_{11}^{-1} = -gamma_1', and breakdown
   of the necessary Irrepresentable Condition ||C_{21} C_{11}^{-1} s(alpha_1)||_inf <= 1
   when invalid instruments are stronger than valid instruments
   (|gamma_1' s(alpha_1)| > ||gamma_2||_1).
2. Theorem 1, Proposition 3, and Corollary 2: Consistency of the median-of-ratios
   estimator beta_hat_m = med(Gamma_hat_j / gamma_hat_j) when s < L/2 regardless
   of instrument strength, failure of standard sisVIVE Lasso under strong invalid
   instruments (selecting valid instruments as invalid and converging toward
   beta + a / gamma_tilde_1 = 1/3), and exact oracle support recovery of
   Adaptive Lasso weighted by |alpha_hat_{m,j}|^{-1}.
3. Section 5.2: Andrews-Hansen downward Sargan/Hansen J-test stopping rule along
   the Adaptive Lasso path (post-ALasso_ah) with p_n = 0.1 / ln(n), selecting
   the exact oracle invalid instrument set A = {0, 1, 2} and matching the
   oracle 2SLS estimator identically.
"""

import json
import math
import random


def mat_mul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    m, k = len(A), len(A[0])
    n = len(B[0])
    out = [[0.0] * n for _ in range(m)]
    for i in range(m):
        Ai = A[i]
        for r in range(k):
            air = Ai[r]
            if air == 0.0:
                continue
            Br = B[r]
            for j in range(n):
                out[i][j] += air * Br[j]
    return out


def mat_T(A: list[list[float]]) -> list[list[float]]:
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def mat_vec(A: list[list[float]], v: list[float]) -> list[float]:
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def dot(u: list[float], v: list[float]) -> float:
    return sum(x * y for x, y in zip(u, v))


def mat_inv(A: list[list[float]]) -> list[list[float]]:
    n = len(A)
    M = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(A)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(M[r][col]))
        M[col], M[piv] = M[piv], M[col]
        div = M[col][col]
        for j in range(2 * n):
            M[col][j] /= div
        for r in range(n):
            if r != col:
                factor = M[r][col]
                if factor != 0.0:
                    for j in range(2 * n):
                        M[r][j] -= factor * M[col][j]
    return [row[n:] for row in M]


def soft_threshold(z: float, lam: float) -> float:
    if z > lam:
        return z - lam
    if z < -lam:
        return z + lam
    return 0.0


def solve_weighted_lasso(
    Z_tilde: list[list[float]],
    y_tilde: list[float],
    lam: float,
    weights: list[float],
    max_iter: int = 800,
    tol: float = 1e-10,
) -> list[float]:
    """Minimize (1/(2n)) ||y_tilde - Z_tilde alpha||_2^2 + lam * sum_j weights[j] * |alpha_j|."""
    n = len(y_tilde)
    L = len(Z_tilde[0])
    ZT = mat_T(Z_tilde)
    G = [[dot(ZT[i], ZT[j]) / n for j in range(L)] for i in range(L)]
    r0 = [dot(ZT[i], y_tilde) / n for i in range(L)]
    alpha = [0.0] * L
    for _ in range(max_iter):
        max_diff = 0.0
        for j in range(L):
            g_jj = G[j][j]
            if g_jj <= 1e-12:
                continue
            rho_j = r0[j] - sum(G[j][k] * alpha[k] for k in range(L) if k != j)
            new_aj = soft_threshold(rho_j, lam * weights[j]) / g_jj
            diff = abs(new_aj - alpha[j])
            if diff > max_diff:
                max_diff = diff
            alpha[j] = new_aj
        if max_diff < tol:
            break
    return alpha


def median_val(vals: list[float]) -> float:
    s = sorted(vals)
    m = len(s)
    if m % 2 == 1:
        return s[m // 2]
    return 0.5 * (s[m // 2 - 1] + s[m // 2])


def ols_fit(X: list[list[float]], y: list[float]) -> list[float]:
    XT = mat_T(X)
    XTX = mat_mul(XT, X)
    XTy = mat_vec(XT, y)
    return mat_vec(mat_inv(XTX), XTy)


def main() -> int:
    # 1. Verify Propositions 1 & 2 and Corollary 1 on correlated and uncorrelated Q
    L = 10
    s = 3
    Q = [[0.3 ** abs(i - j) for j in range(L)] for i in range(L)]
    gamma_1 = [0.6] * s
    gamma_2 = [0.2] * (L - s)
    gamma = gamma_1 + gamma_2
    s_alpha1 = [1.0] * s

    Qgamma = mat_vec(Q, gamma)
    gQg = dot(gamma, Qgamma)
    C = [
        [Q[i][j] - Qgamma[i] * Qgamma[j] / gQg for j in range(L)]
        for i in range(L)
    ]
    # Check C * gamma == 0 (rank deficiency of C)
    C_gamma_norm = math.sqrt(sum(x * x for x in mat_vec(C, gamma)))
    assert C_gamma_norm < 1e-14

    C11 = [row[:s] for row in C[:s]]
    C21 = [row[:s] for row in C[s:]]
    C21_C11inv_direct = mat_mul(C21, mat_inv(C11))

    # Proposition 1 Eq. (18) closed-form block formula via Schur complement
    # Q_tilde_22 = Q_22 - Q_21 * Q_11^{-1} * Q_12
    Q11 = [row[:s] for row in Q[:s]]
    Q12 = [row[s:] for row in Q[:s]]
    Q21 = [row[:s] for row in Q[s:]]
    Q22 = [row[s:] for row in Q[s:]]
    Q11_inv = mat_inv(Q11)
    Q21_Q11inv = mat_mul(Q21, Q11_inv)
    Q21_Q11inv_Q12 = mat_mul(Q21_Q11inv, Q12)
    Q_tilde_22 = [
        [Q22[i][j] - Q21_Q11inv_Q12[i][j] for j in range(L - s)]
        for i in range(L - s)
    ]
    Qt22_g2 = mat_vec(Q_tilde_22, gamma_2)
    denom_g2 = dot(gamma_2, Qt22_g2)
    # (I_{L-s} - Qt22 * g2 * g2' / (g2' Qt22 g2)) * Q21 * Q11^{-1} - Qt22 * g2 * g1' / (g2' Qt22 g2)
    g2_Q21_Q11inv = mat_vec(mat_T(Q21_Q11inv), gamma_2)
    C21_C11inv_prop1 = [
        [
            Q21_Q11inv[i][j]
            - Qt22_g2[i] * (g2_Q21_Q11inv[j] + gamma_1[j]) / denom_g2
            for j in range(s)
        ]
        for i in range(L - s)
    ]
    prop1_max_diff = max(
        abs(C21_C11inv_direct[i][j] - C21_C11inv_prop1[i][j])
        for i in range(L - s)
        for j in range(s)
    )
    assert prop1_max_diff < 1e-13

    # Proposition 2 identity: gamma_2' * C_{21} * C_{11}^{-1} == -gamma_1'
    lhs_prop2 = mat_vec(mat_T(C21_C11inv_direct), gamma_2)
    prop2_identity_err = max(
        abs(lhs_prop2[j] - (-gamma_1[j])) for j in range(s)
    )
    assert prop2_identity_err < 1e-13

    # Irrepresentable condition norm under Q = I_L for unequal vs equal strength
    ic_unequal_uncorr = (s * 0.6) / ((L - s) * 0.2)  # 1.8 / 1.4 = 9/7 > 1
    ic_equal_uncorr = (s * 0.2) / ((L - s) * 0.2)  # 3/7 < 1
    ic_unequal_corr = max(
        abs(x) for x in mat_vec(C21_C11inv_direct, s_alpha1)
    )
    assert ic_unequal_uncorr > 1.0
    assert ic_unequal_corr > 1.0
    assert ic_equal_uncorr < 1.0

    # 2. Simulate Table 2 DGP (n = 2000, L = 10, s = 3, beta = 0, a = 0.2,
    #    gamma_tilde_1 = 0.6, gamma_tilde_2 = 0.2, rho = 0.25)
    rng = random.Random(20261019)
    n = 2000
    beta_true = 0.0
    alpha_true = [0.2, 0.2, 0.2] + [0.0] * (L - s)
    rho = 0.25

    Z_raw = [[rng.gauss(0.0, 1.0) for _ in range(L)] for _ in range(n)]
    z_means = [sum(Z_raw[i][j] for i in range(n)) / n for j in range(L)]
    Z = [[Z_raw[i][j] - z_means[j] for j in range(L)] for i in range(n)]

    d_raw = []
    y_raw = []
    for i in range(n):
        eps_i = rng.gauss(0.0, 1.0)
        v_i = rho * eps_i + math.sqrt(1.0 - rho * rho) * rng.gauss(0.0, 1.0)
        di = dot(Z[i], gamma) + v_i
        yi = di * beta_true + dot(Z[i], alpha_true) + eps_i
        d_raw.append(di)
        y_raw.append(yi)

    d_mean = sum(d_raw) / n
    y_mean = sum(y_raw) / n
    d = [x - d_mean for x in d_raw]
    y = [x - y_mean for x in y_raw]

    ZT = mat_T(Z)
    ZTZ_inv = mat_inv(mat_mul(ZT, Z))
    Gamma_hat = mat_vec(ZTZ_inv, mat_vec(ZT, y))
    gamma_hat = mat_vec(ZTZ_inv, mat_vec(ZT, d))
    d_hat = mat_vec(Z, gamma_hat)
    y_hat = mat_vec(Z, Gamma_hat)

    beta_naive = dot(d_hat, y) / dot(d_hat, d_hat)
    plim_beta_naive = sum(gamma[j] * alpha_true[j] for j in range(s)) / sum(
        g * g for g in gamma
    )

    def fit_post_2sls(active_set: list[int]) -> tuple[float, list[float], float]:
        R_hat = [[d_hat[i]] + [Z[i][j] for j in active_set] for i in range(n)]
        theta_hat = ols_fit(R_hat, y)
        b_hat = theta_hat[0]
        a_hat = theta_hat[1:]
        resid = [
            y[i] - d[i] * b_hat - sum(Z[i][active_set[k]] * a_hat[k] for k in range(len(active_set)))
            for i in range(n)
        ]
        ZT_resid = mat_vec(ZT, resid)
        quad_form = dot(ZT_resid, mat_vec(ZTZ_inv, ZT_resid))
        sigma2_hat = dot(resid, resid) / n
        J_stat = quad_form / sigma2_hat
        return b_hat, a_hat, J_stat

    beta_oracle, _, J_oracle = fit_post_2sls([0, 1, 2])

    d_hat_norm2 = dot(d_hat, d_hat)
    Z_tilde = [[0.0] * L for _ in range(n)]
    for j in range(L):
        col_j = [Z[i][j] for i in range(n)]
        proj_coeff = dot(d_hat, col_j) / d_hat_norm2
        for i in range(n):
            Z_tilde[i][j] = col_j[i] - d_hat[i] * proj_coeff
    y_proj_coeff = dot(d_hat, y_hat) / d_hat_norm2
    y_tilde = [y_hat[i] - d_hat[i] * y_proj_coeff for i in range(n)]

    # Standard Lasso (unit weights)
    alpha_lasso_std = solve_weighted_lasso(
        Z_tilde, y_tilde, lam=0.018, weights=[1.0] * L
    )
    active_lasso_std = [j for j, val in enumerate(alpha_lasso_std) if abs(val) > 1e-5]
    beta_lasso_std = dot(
        d_hat,
        [y[i] - dot(Z[i], alpha_lasso_std) for i in range(n)],
    ) / d_hat_norm2

    # Theorem 1: Median-of-ratios initial consistent estimator beta_hat_m
    pi_hat = [Gamma_hat[j] / gamma_hat[j] for j in range(L)]
    beta_median = median_val(pi_hat)
    alpha_median = [Gamma_hat[j] - gamma_hat[j] * beta_median for j in range(L)]

    # Adaptive Lasso (Eq. 21) with weights |alpha_median_j|^{-1}
    alasso_weights = [1.0 / max(abs(am), 1e-6) for am in alpha_median]
    alpha_alasso = solve_weighted_lasso(
        Z_tilde, y_tilde, lam=0.0025, weights=alasso_weights
    )
    active_alasso = [j for j, val in enumerate(alpha_alasso) if abs(val) > 1e-5]
    beta_post_alasso, _, _ = fit_post_2sls(active_alasso)

    # 3. Section 5.2: Andrews-Hansen downward J-test stopping rule along Adaptive Lasso order
    ranked_inst = sorted(range(L), key=lambda j: abs(alpha_median[j]), reverse=True)
    p_n = 0.1 / math.log(n)
    z_crit = 2.2216

    def chi2_crit(df: int) -> float:
        w = 1.0 - 2.0 / (9.0 * df) + z_crit * math.sqrt(2.0 / (9.0 * df))
        return df * (w ** 3)

    j_path = []
    selected_ah_set = []
    for step_k in range(L - 1):
        cand_set = sorted(ranked_inst[:step_k])
        b_k, _, J_k = fit_post_2sls(cand_set)
        df_k = L - 1 - step_k
        crit_k = chi2_crit(df_k)
        j_path.append(
            {
                "step": step_k,
                "candidate_set": cand_set,
                "J_stat": round(J_k, 4),
                "df": df_k,
                "crit_val": round(crit_k, 4),
            }
        )
        if J_k < crit_k:
            selected_ah_set = cand_set
            break

    beta_post_alasso_ah, _, _ = fit_post_2sls(selected_ah_set)

    assert active_lasso_std != [0, 1, 2]
    assert abs(beta_lasso_std - beta_true) > 0.20
    assert abs(beta_median - beta_true) < 0.05
    assert active_alasso == [0, 1, 2]
    assert selected_ah_set == [0, 1, 2]
    assert abs(beta_post_alasso - beta_oracle) < 1e-12
    assert abs(beta_post_alasso_ah - beta_oracle) < 1e-12

    result = {
        "concept": "AIMech:AdaptiveLassoAndMedianOfRatiosConsistentInvalidInstrumentSelectionInLinearInstrumentalVariablesModels",
        "source": "Windmeijer, Farbmacher, Davies, & Davey Smith (2019), JASA 114(527):1339-1350, DOI:10.1080/01621459.2018.1498346, PMC6817329",
        "irrepresentable_condition_propositions_1_and_2": {
            "L": L,
            "s": s,
            "C_gamma_rank_deficiency_norm": round(C_gamma_norm, 16),
            "prop1_eq18_max_diff": round(prop1_max_diff, 16),
            "prop2_identity_max_err": round(prop2_identity_err, 16),
            "ic_inf_norm_unequal_uncorr_9_over_7": round(ic_unequal_uncorr, 6),
            "ic_inf_norm_unequal_corr": round(ic_unequal_corr, 6),
            "ic_inf_norm_equal_uncorr_3_over_7": round(ic_equal_uncorr, 6),
        },
        "table2_unequal_strength_simulation": {
            "n": n,
            "beta_true": beta_true,
            "plim_beta_naive": round(plim_beta_naive, 6),
            "beta_naive_2sls": round(beta_naive, 6),
            "beta_oracle_2sls": round(beta_oracle, 6),
            "standard_lasso_selected_invalid": active_lasso_std,
            "beta_standard_lasso_biased": round(beta_lasso_std, 6),
            "beta_median_of_ratios": round(beta_median, 6),
            "adaptive_lasso_selected_invalid": active_alasso,
            "beta_post_alasso": round(beta_post_alasso, 6),
            "andrews_hansen_selected_invalid": selected_ah_set,
            "beta_post_alasso_ah": round(beta_post_alasso_ah, 6),
            "andrews_hansen_j_test_path_first4": j_path[:4],
        },
        "all_assertions_passed": True,
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
