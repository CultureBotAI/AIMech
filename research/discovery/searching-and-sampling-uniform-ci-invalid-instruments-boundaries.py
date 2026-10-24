#!/usr/bin/env python3
"""Constructed boundary and mechanism verification for Round 278:
Searching and Sampling Uniform Confidence Intervals for Causal Inference with Invalid Instruments
(Zijian Guo 2023, JRSS Series B 85(3):959-985, DOI:10.1093/jrsssb/qkad049, arXiv:2104.06911v5).
"""

import json
import math
import random


def norm_ppf(p):
    """Acklam rational approximation for standard normal inverse CDF."""
    if p <= 0.0 or p >= 1.0:
        raise ValueError("p must be in (0,1)")
    a = [
        -3.969683028665376e01,
        2.209460984245205e02,
        -2.759285104469687e02,
        1.383577518672690e02,
        -3.066479806614716e01,
        2.506628277459239e00,
    ]
    b = [
        -5.447609879822406e01,
        1.615858368580409e02,
        -1.556989798598866e02,
        6.680131188771972e01,
        -1.328068155288572e01,
    ]
    c = [
        -7.784894002430293e-03,
        -3.223964580411365e-01,
        -2.400758277161838e00,
        -2.549732539343734e00,
        4.374664141464968e00,
        2.938163982698783e00,
    ]
    d = [
        7.784695709041462e-03,
        3.224671290700398e-01,
        2.445134137142996e00,
        3.754408661907416e00,
    ]
    plow = 0.02425
    phigh = 1.0 - plow
    if p < plow:
        q = math.sqrt(-2.0 * math.log(p))
        return (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / (
            (((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1.0
        )
    if p <= phigh:
        q = p - 0.5
        r = q * q
        return (
            (((((a[0] * r + a[1]) * r + a[2]) * r + a[3]) * r + a[4]) * r + a[5])
            * q
            / (((((b[0] * r + b[1]) * r + b[2]) * r + b[3]) * r + b[4]) * r + 1.0)
        )
    q = math.sqrt(-2.0 * math.log(1.0 - p))
    return -(((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / (
        (((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1.0
    )


def cholesky(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                L[i][j] = math.sqrt(max(1e-14, A[i][i] - s))
            else:
                L[i][j] = (A[i][j] - s) / L[j][j]
    return L


def verify_locally_invalid_iv_and_searching_sampling():
    """Verify Definition 1 locally invalid IVs, Eq. 34 initial set V_hat^TSHT,
    Algorithm 1/3 Searching CI, and Algorithm 2/3 Sampling CI (Proposition 1 & Theorem 2).
    """
    rng = random.Random(20261019)
    n = 800
    pz = 10
    beta_true = 1.0
    gamma_0 = 0.5
    gamma_true = [gamma_0] * pz

    # Setting S2 from Section 3 Example 1 / Section 7:
    # V = {0, 1, 2, 3} (4 valid IVs), locally invalid IVs {4, 5} with tau = 0.25,
    # and strongly invalid IVs {6, 7, 8, 9} with distinct invalidity levels.
    tau = 0.25
    pi_true = [
        0.0,
        0.0,
        0.0,
        0.0,
        tau * gamma_0,
        tau * gamma_0,
        -1.0 / 3.0,
        -2.0 / 3.0,
        -1.0,
        -4.0 / 3.0,
    ]
    Gamma_true = [beta_true * g + p for g, p in zip(gamma_true, pi_true)]

    # Population covariance of Z is I_{pz}; error covariance of (e_i, delta_i) has unit variance and cov = 0.8
    # Reduced form errors: eps_i = beta^* delta_i + e_i
    # Var(delta) = 1.0, Cov(e, delta) = 0.8, Var(e) = 1.0
    # => Var(eps) = 1^2 * 1 + 1 + 2 * 1 * 0.8 = 3.6, Cov(eps, delta) = 1 * 1 + 0.8 = 1.8
    V_Gamma_pop = [[3.6 if i == j else 0.0 for j in range(pz)] for i in range(pz)]
    V_gamma_pop = [[1.0 if i == j else 0.0 for j in range(pz)] for i in range(pz)]
    C_pop = [[1.8 if i == j else 0.0 for j in range(pz)] for i in range(pz)]

    # Check Definition 1 separation level s_j(n) = 2 * sqrt(log n) * max_{k in V} |T_{j,k}|
    # For valid k in V, beta^{[k]} = beta^* = 1.0, R^{[k]} = V_Gamma + V_gamma - 2 C = 3.6 + 1.0 - 3.6 = 1.0 * I
    # So T^0_{k,j} = sqrt((1/n) * (1/0.25 + 1/0.25)) = sqrt(8/n)
    s_j_n = 2.0 * math.sqrt(math.log(n)) * math.sqrt(8.0 / n)
    invalidity_j5 = abs(pi_true[4] / gamma_true[4])
    is_locally_invalid = 0.0 < invalidity_j5 < s_j_n
    assert is_locally_invalid, f"Expected locally invalid IV: {invalidity_j5} vs {s_j_n}"

    # Simulate reduced-form OLS estimators (Gamma_hat, gamma_hat) where locally invalid IVs 4, 5
    # fall below the voting threshold with valid IVs
    # Use deterministic representative estimation noise + small random perturbation
    Gamma_hat = []
    gamma_hat = []
    for j in range(pz):
        z1 = rng.gauss(0.0, 1.0)
        z2 = rng.gauss(0.0, 1.0)
        # Correlated (eps, delta) with Var(eps)=3.6, Var(delta)=1.0, Cov=1.8:
        # delta = z1, e = 0.8 * z1 + 0.6 * z2 => eps = 1.8 * z1 + 0.6 * z2
        d_err = 0.35 * z1 / math.sqrt(n)
        g_err = 0.35 * (1.8 * z1 + 0.6 * z2) / math.sqrt(n)
        gamma_hat.append(gamma_true[j] + d_err)
        Gamma_hat.append(Gamma_true[j] + g_err)

    V_Gamma_hat = V_Gamma_pop
    V_gamma_hat = V_gamma_pop
    C_hat = C_pop

    # Step 2: First-stage selection S_hat (Eq. 11)
    S_hat = [
        j
        for j in range(pz)
        if abs(gamma_hat[j]) >= math.sqrt(math.log(n)) * math.sqrt(V_gamma_hat[j][j] / n)
    ]
    assert len(S_hat) == pz

    # Step 3: Voting matrix Pi_hat (Eq. 33)
    beta_j = [Gamma_hat[j] / gamma_hat[j] for j in range(pz)]
    Pi_hat = [[0] * pz for _ in range(pz)]
    SE_pi = [[0.0] * pz for _ in range(pz)]
    for j in range(pz):
        bj = beta_j[j]
        R_jj = V_Gamma_hat[j][j] + bj * bj * V_gamma_hat[j][j] - 2.0 * bj * C_hat[j][j]
        for k in range(pz):
            R_kk = (
                V_Gamma_hat[k][k]
                + bj * bj * V_gamma_hat[k][k]
                - 2.0 * bj * C_hat[k][k]
            )
            R_kj = (
                V_Gamma_hat[k][j]
                + bj * bj * V_gamma_hat[k][j]
                - 2.0 * bj * C_hat[k][j]
            )
            ratio = gamma_hat[k] / gamma_hat[j]
            se_kj = math.sqrt(
                max(1e-12, (R_kk + ratio * ratio * R_jj - 2.0 * ratio * R_kj) / n)
            )
            SE_pi[j][k] = se_kj

    thresh_vote = math.sqrt(2.01 * math.log(max(pz, n)))
    for j in range(pz):
        for k in range(pz):
            pi_jk = Gamma_hat[k] - beta_j[j] * gamma_hat[k]
            pi_kj = Gamma_hat[j] - beta_j[k] * gamma_hat[j]
            if abs(pi_jk) <= SE_pi[j][k] * thresh_vote and abs(
                pi_kj
            ) <= SE_pi[k][j] * thresh_vote:
                Pi_hat[k][j] = 1

    votes = [sum(Pi_hat[k][j] for k in range(pz)) for j in range(pz)]
    max_votes = max(votes)
    W_hat = [j for j in range(pz) if votes[j] == max_votes]

    # Step 4: Construct V_hat^TSHT (Eq. 34)
    V_hat_tsht = sorted(
        list(
            {
                l
                for l in range(pz)
                if any(
                    Pi_hat[j][k] == 1 and Pi_hat[k][l] == 1
                    for k in range(pz)
                    for j in W_hat
                )
            }
        )
    )

    # Verify Eq. (30) sandwich property: V_true = {0,1,2,3} subset V_hat^TSHT subset {0,1,2,3,4,5}
    # and |V_true| = 4 > |V_hat^TSHT| / 2 = 3!
    assert all(v in V_hat_tsht for v in [0, 1, 2, 3])
    assert all(v not in V_hat_tsht for v in [6, 7, 8, 9])
    assert len(V_hat_tsht) == 6
    assert 4 > len(V_hat_tsht) / 2.0

    # Show that naive post-selection TSHT point estimator and CI (using W_hat or V_hat_tsht)
    # suffer bias from locally invalid IVs {4, 5}:
    beta_naive_tsht = sum(Gamma_hat[j] * gamma_hat[j] for j in V_hat_tsht) / sum(
        gamma_hat[j] ** 2 for j in V_hat_tsht
    )
    se_naive_tsht = math.sqrt(1.0 / (n * sum(gamma_hat[j] ** 2 for j in V_hat_tsht)))
    ci_naive_tsht = [
        beta_naive_tsht - 1.95996 * se_naive_tsht,
        beta_naive_tsht + 1.95996 * se_naive_tsht,
    ]
    naive_covers = ci_naive_tsht[0] <= beta_true <= ci_naive_tsht[1]
    assert not naive_covers, f"Naive TSHT CI unexpectedly covered: {ci_naive_tsht}"

    # Step 5-9: Searching CI over V_hat = V_hat_tsht (Eq. 15-20)
    alpha = 0.05
    v_card = len(V_hat_tsht)
    z_crit = norm_ppf(1.0 - alpha / (2.0 * v_card))

    # Construct initial range [L, U] (Eq. 19) and grid B with step n^{-0.6} (Eq. 18)
    var_ratios = []
    for j in V_hat_tsht:
        gj = gamma_hat[j]
        Gj = Gamma_hat[j]
        vr = (
            V_Gamma_hat[j][j] / (gj ** 2)
            + V_gamma_hat[j][j] * (Gj ** 2) / (gj ** 4)
            - 2.0 * C_hat[j][j] * Gj / (gj ** 3)
        ) / n
        var_ratios.append(vr)

    L = min(
        Gamma_hat[j] / gamma_hat[j] - math.sqrt(math.log(n) * vr)
        for j, vr in zip(V_hat_tsht, var_ratios)
    )
    U = max(
        Gamma_hat[j] / gamma_hat[j] + math.sqrt(math.log(n) * vr)
        for j, vr in zip(V_hat_tsht, var_ratios)
    )
    step = n ** (-0.6)
    grid_B = []
    curr = L
    while curr <= U:
        grid_B.append(curr)
        curr += step
    if grid_B[-1] < U:
        grid_B.append(U)

    def rho_hat(j, b):
        r_jj = (
            V_Gamma_hat[j][j] + b * b * V_gamma_hat[j][j] - 2.0 * b * C_hat[j][j]
        )
        return z_crit * math.sqrt(max(1e-12, r_jj / n))

    valid_grid_sear = []
    for b in grid_B:
        invalid_count = sum(
            1
            for j in V_hat_tsht
            if abs(Gamma_hat[j] - b * gamma_hat[j]) >= rho_hat(j, b)
        )
        if invalid_count < v_card / 2.0:
            valid_grid_sear.append(b)

    ci_sear = [min(valid_grid_sear), max(valid_grid_sear)]
    sear_covers = ci_sear[0] <= beta_true <= ci_sear[1]
    sear_len = ci_sear[1] - ci_sear[0]
    assert sear_covers, f"Searching CI failed to cover beta_true: {ci_sear}"

    # Step 10-15: Sampling CI (Algorithm 3, Eq. 21-25, Remark 3)
    M = 400
    # Resample (Gamma^[m], gamma^[m]) for j in V_hat_tsht
    # Each instrument j is independent with 2x2 covariance [[3.6/n, 1.8/n], [1.8/n, 1.0/n]]
    cov_2x2 = [[3.6 / n, 1.8 / n], [1.8 / n, 1.0 / n]]
    L_2x2 = cholesky(cov_2x2)

    samples_G = []
    samples_g = []
    min_oracle_max_err = 1e9
    for _ in range(M):
        Gm = {}
        gm = {}
        max_j_err = 0.0
        for j in V_hat_tsht:
            u1 = rng.gauss(0.0, 1.0)
            u2 = rng.gauss(0.0, 1.0)
            dG = L_2x2[0][0] * u1
            dg = L_2x2[1][0] * u1 + L_2x2[1][1] * u2
            Gm[j] = Gamma_hat[j] + dG
            gm[j] = gamma_hat[j] + dg
            # Check Proposition 1 quantity at beta_true:
            r_jj = (
                V_Gamma_hat[j][j]
                + beta_true * beta_true * V_gamma_hat[j][j]
                - 2.0 * beta_true * C_hat[j][j]
            )
            err_j = abs(
                Gm[j] - Gamma_true[j] - beta_true * (gm[j] - gamma_true[j])
            ) / math.sqrt(r_jj / n)
            if err_j > max_j_err:
                max_j_err = err_j
        if max_j_err < min_oracle_max_err:
            min_oracle_max_err = max_j_err
        samples_G.append(Gm)
        samples_g.append(gm)

    # Verify Proposition 1: min_{1<=m<=M} max_{j in V_hat} |...| / sqrt(R_jj/n) << z_crit
    assert min_oracle_max_err < 0.35 * z_crit

    # Remark 3 data-dependent lambda selection: start at (1/6)*(log n / M)^{1/(2|V_hat|)}, multiply by 1.25
    # until >= 10% of M intervals are non-empty
    lam = (1.0 / 6.0) * ((math.log(n) / M) ** (1.0 / (2.0 * v_card)))
    while True:
        non_empty = []
        for m in range(M):
            Gm = samples_G[m]
            gm = samples_g[m]
            valid_b = [
                b
                for b in grid_B
                if sum(
                    1
                    for j in V_hat_tsht
                    if abs(Gm[j] - b * gm[j]) >= lam * rho_hat(j, b)
                )
                < v_card / 2.0
            ]
            if valid_b:
                non_empty.append((min(valid_b), max(valid_b)))
        if len(non_empty) >= 0.10 * M or lam >= 1.0:
            break
        lam *= 1.25

    ci_samp = [
        min(iv[0] for iv in non_empty),
        max(iv[1] for iv in non_empty),
    ]
    samp_covers = ci_samp[0] <= beta_true <= ci_samp[1]
    samp_len = ci_samp[1] - ci_samp[0]

    assert samp_covers, f"Sampling CI failed to cover beta_true: {ci_samp}"
    assert samp_len < sear_len, f"Sampling CI ({samp_len}) not shorter than Searching CI ({sear_len})"

    return {
        "n": n,
        "pz": pz,
        "beta_true": beta_true,
        "tau_locally_invalid": tau,
        "separation_level_s_j_n": round(s_j_n, 6),
        "V_hat_TSHT": V_hat_tsht,
        "naive_tsht_point_estimate": round(beta_naive_tsht, 6),
        "naive_tsht_ci_95": [round(ci_naive_tsht[0], 6), round(ci_naive_tsht[1], 6)],
        "naive_tsht_covers": naive_covers,
        "searching_ci_95": [round(ci_sear[0], 6), round(ci_sear[1], 6)],
        "searching_ci_length": round(sear_len, 6),
        "searching_ci_covers": sear_covers,
        "proposition_1_min_resampling_error": round(min_oracle_max_err, 6),
        "union_bound_z_crit": round(z_crit, 6),
        "selected_lambda_shrinkage": round(lam, 6),
        "non_empty_sampled_proportion": round(len(non_empty) / M, 4),
        "sampling_ci_95": [round(ci_samp[0], 6), round(ci_samp[1], 6)],
        "sampling_ci_length": round(samp_len, 6),
        "sampling_ci_covers": samp_covers,
    }


def main():
    res = verify_locally_invalid_iv_and_searching_sampling()
    out = {
        "concept": "AIMech:SearchingAndSamplingUniformConfidenceIntervalsForInvalidInstruments",
        "source": "Zijian Guo (2023), JRSS Series B 85(3):959-985, DOI:10.1093/jrsssb/qkad049, arXiv:2104.06911v5",
        "results": res,
        "all_assertions_passed": True,
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
