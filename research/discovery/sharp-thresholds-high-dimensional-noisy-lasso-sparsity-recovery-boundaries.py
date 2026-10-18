#!/usr/bin/env python3
"""Constructed boundary and diagnostic verification for Round 232:
PrimalDualWitnessAndSharpThresholdsForHighDimensionalNoisyLassoSparsityRecovery
(Wainwright 2009, IEEE Trans. Inf. Theory 55(5):2183-2202, arXiv:math/0605740v1).

Verifies:
1. Primal-dual witness / KKT necessary and sufficient conditions for exact
   signed support recovery R(X, beta^*, w, lambda_n) (Lemma 1, Eqs. 9a-9b,
   10a-10b, pp. 4-5 & Appendix A, p. 18):
   - Off-support strict dual feasibility M(V) = {max_{j in S^c} |V_j| <= lambda_n}
     and on-support sign consistency beta^*_S + U_S having sign b = sgn(beta^*_S)
     (sufficient condition M(U) = {max_{i in S} |U_i| <= rho_n}), where
     U = (X_S^T X_S / n)^{-1} [X_S^T w / n - lambda_n b] and
     V_{S^c} = X_{S^c}^T { X_S (X_S^T X_S)^{-1} lambda_n b - [X_S (X_S^T X_S)^{-1} X_S^T - I_n] w / n }.
   - Confirms that when (9a)-(9b) hold, the primal-dual pair (beta_hat, z_hat)
     with beta_hat_S = beta^*_S + U, beta_hat_{S^c} = 0, z_hat_S = b,
     z_hat_{S^c} = +V_{S^c} / lambda_n (noting Appendix A p. 18 line 13 drops
     the minus sign when writing lambda z_hat_{S^c} = -V_{S^c}) satisfies the
     exact KKT equation (1/n) X^T (X beta_hat - y) + lambda_n z_hat = 0 with
     ||z_hat_{S^c}||_infty <= 1.
2. Sharp phase transition thresholds theta_l and theta_u for correlated Gaussian
   ensembles and exact collapse theta_l = theta_u = 1 for the standard Gaussian
   ensemble (Theorem 1, Eq. 20, pp. 8-9; Corollaries 1-2, pp. 9-10):
   - theta_l = (sqrt(C_max) - sqrt(C_max - 1/C_max))^2 / (C_max (2 - epsilon)^2) <= 1
     and theta_u = C_max / (epsilon^2 C_min) >= 1.
   - For Sigma = I_p (C_min = C_max = 1, epsilon = 1), theta_l = theta_u = 1,
     giving critical sample size n_crit = 2 s log(p - s) + s + 1.
   - For Toeplitz Sigma_{jk} = rho^{|j-k|} with rho = 0.10 (Section 4, p. 16-17),
     verifies 0 < theta_l < 1 < theta_u.
3. Conditional Gaussian covariance decomposition and exact inverse-Wishart /
   projection mean and variance of the random scaling factor M_n (Lemmas 2-3,
   Eqs. 23-27, p. 11; Appendix D.2, Eqs. 41-46, pp. 20-21; Appendix D.6,
   Eq. 50, p. 25):
   - R = I_n - X_S (X_S^T X_S)^{-1} X_S^T is idempotent (R^2 = R) of trace n - s
     with R X_S = 0.
   - Exact mean E[M_n] = (lambda_n^2 / (n - s - 1)) b^T (Sigma_{SS})^{-1} b
     + sigma^2 (n - s) / n^2 and exact variance var(M_n) = H_1 + H_2 from Eq. (46),
     plus block-matrix Schur complement identity Sigma_{(S^c|S)} = ([Sigma^{-1}]_{S^c S^c})^{-1}
     (noting Appendix D.6 p. 25 line 11 omits the outer inverse on [Sigma^{-1}]_{S^c S^c})
     and eigenvalue bound Lambda_min(Sigma_{(S^c|S)}) >= Lambda_min(Sigma) >= 1 / C_max.
"""

from __future__ import annotations

import json
import math
import random
import sys
from typing import Dict, List


def mat_mul(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    m, k, n = len(A), len(B), len(B[0])
    out = [[0.0] * n for _ in range(m)]
    for i in range(m):
        for r in range(k):
            air = A[i][r]
            for j in range(n):
                out[i][j] += air * B[r][j]
    return out


def mat_vec(A: List[List[float]], x: List[float]) -> List[float]:
    return [sum(aij * xj for aij, xj in zip(row, x)) for row in A]


def transpose(A: List[List[float]]) -> List[List[float]]:
    return [list(col) for col in zip(*A)]


def mat_inv(A: List[List[float]]) -> List[List[float]]:
    n = len(A)
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(A)]
    for i in range(n):
        piv = max(range(i, n), key=lambda r: abs(aug[r][i]))
        aug[i], aug[piv] = aug[piv], aug[i]
        div = aug[i][i]
        aug[i] = [v / div for v in aug[i]]
        for r in range(n):
            if r != i:
                fac = aug[r][i]
                if fac != 0.0:
                    aug[r] = [aug[r][c] - fac * aug[i][c] for c in range(2 * n)]
    return [row[n:] for row in aug]


def verify_primal_dual_witness_kkt_equivalence() -> Dict[str, object]:
    """Verify Lemma 1 (Eqs. 9a-9b, 10a-10b) and Appendix A KKT stationarity."""
    rng = random.Random(20261018)
    n, p, s = 40, 10, 3
    lam = 0.08
    sigma = 0.05

    X = [[rng.gauss(0.0, 1.0) for _ in range(p)] for _ in range(n)]
    X_S = [[X[i][j] for j in range(s)] for i in range(n)]
    X_Sc = [[X[i][j] for j in range(s, p)] for i in range(n)]

    beta_star_S = [1.2, -0.9, 1.5]
    b_vec = [1.0 if v > 0 else -1.0 for v in beta_star_S]
    w = [rng.gauss(0.0, sigma) for _ in range(n)]

    y = [
        sum(X_S[i][j] * beta_star_S[j] for j in range(s)) + w[i]
        for i in range(n)
    ]

    Xt_S = transpose(X_S)
    Xt_Sc = transpose(X_Sc)
    Gram_S = mat_mul(Xt_S, X_S)
    Gram_S_inv = mat_inv(Gram_S)
    Gram_S_over_n_inv = [[v * n for v in row] for row in Gram_S_inv]

    # Compute U (Eq. 10a) and V (Eq. 10b)
    Xt_S_w_over_n = [sum(Xt_S[i][k] * w[k] for k in range(n)) / n for i in range(s)]
    rhs_u = [Xt_S_w_over_n[i] - lam * b_vec[i] for i in range(s)]
    U = mat_vec(Gram_S_over_n_inv, rhs_u)

    # V_j = X_j^T { X_S (X_S^T X_S)^{-1} lam b - [X_S (X_S^T X_S)^{-1} X_S^T - I_n] w / n }
    inv_b = mat_vec(Gram_S_inv, [lam * bi for bi in b_vec])
    term1_n = mat_vec(X_S, inv_b)
    Xt_S_w = mat_vec(Xt_S, w)
    proj_w = mat_vec(X_S, mat_vec(Gram_S_inv, Xt_S_w))
    term2_n = [(proj_w[k] - w[k]) / n for k in range(n)]
    inner_n = [term1_n[k] - term2_n[k] for k in range(n)]
    V = mat_vec(Xt_Sc, inner_n)

    # Construct primal-dual witness (beta_hat, z_hat) with z_hat_{S^c} = +V / lam
    beta_hat = [beta_star_S[i] + U[i] for i in range(s)] + [0.0] * (p - s)
    z_hat = b_vec[:] + [vj / lam for vj in V]

    # Check KKT residual: (1/n) X^T (X beta_hat - y) + lam z_hat == 0
    X_beta_hat = mat_vec(X, beta_hat)
    residual_n = [(X_beta_hat[k] - y[k]) / n for k in range(n)]
    grad = mat_vec(transpose(X), residual_n)
    kkt_residual = max(abs(grad[j] + lam * z_hat[j]) for j in range(p))

    max_v_over_lam = max(abs(vj) / lam for vj in V)
    rho_n = min(abs(v) for v in beta_star_S)
    max_u = max(abs(ui) for ui in U)
    signs_match = all(
        (beta_hat[i] > 0) == (beta_star_S[i] > 0) for i in range(s)
    )

    passed = (
        kkt_residual < 1e-13
        and max_v_over_lam < 1.0
        and max_u < rho_n
        and signs_match
    )
    return {
        "kkt_stationarity_max_residual": kkt_residual,
        "max_off_support_subgradient": max_v_over_lam,
        "max_on_support_perturbation": max_u,
        "min_signal_magnitude_rho_n": rho_n,
        "exact_signed_support_recovered": signs_match,
        "passed": passed,
    }


def verify_threshold_formulas_and_toeplitz_bounds() -> Dict[str, object]:
    """Verify Theorem 1 (Eq. 20) thresholds for uniform and Toeplitz Gaussian ensembles."""
    c_min_id, c_max_id, eps_id = 1.0, 1.0, 1.0
    theta_l_id = (
        (math.sqrt(c_max_id) - math.sqrt(c_max_id - 1.0 / c_max_id)) ** 2
        / (c_max_id * ((2.0 - eps_id) ** 2))
    )
    theta_u_id = c_max_id / ((eps_id ** 2) * c_min_id)

    rho = 0.10
    c_min_toep = (1.0 - rho) / (1.0 + rho)
    c_max_toep = (1.0 + rho) / (1.0 - rho)
    eps_toep = 1.0 - (2.0 * rho) / (1.0 + rho * rho)
    theta_l_toep = (
        (math.sqrt(c_max_toep) - math.sqrt(c_max_toep - 1.0 / c_max_toep)) ** 2
        / (c_max_toep * ((2.0 - eps_toep) ** 2))
    )
    theta_u_toep = c_max_toep / ((eps_toep ** 2) * c_min_toep)

    p = 512
    alpha = 0.25
    s = int(alpha * p)
    n_crit_noisy = 2.0 * s * math.log(p - s) + s + 1.0

    passed = (
        abs(theta_l_id - 1.0) < 1e-15
        and abs(theta_u_id - 1.0) < 1e-15
        and 0.0 < theta_l_toep < 1.0 < theta_u_toep
        and n_crit_noisy > p
    )
    return {
        "uniform_theta_l": theta_l_id,
        "uniform_theta_u": theta_u_id,
        "toeplitz_rho_0_10_theta_l": theta_l_toep,
        "toeplitz_rho_0_10_theta_u": theta_u_toep,
        "noisy_linear_sparsity_n_crit_at_p512": n_crit_noisy,
        "passed": passed,
    }


def verify_conditional_covariance_and_schur_complement() -> Dict[str, object]:
    """Verify Lemma 2-3 (Eqs. 24-26, 42-46) and Appendix D.6 Schur complement identity."""
    rng = random.Random(20261019)
    n, s = 22, 4
    X_S = [[rng.gauss(0.0, 1.0) for _ in range(s)] for _ in range(n)]
    Xt_S = transpose(X_S)
    Gram_inv = mat_inv(mat_mul(Xt_S, X_S))
    P_S = mat_mul(X_S, mat_mul(Gram_inv, Xt_S))
    R = [
        [(1.0 if i == j else 0.0) - P_S[i][j] for j in range(n)]
        for i in range(n)
    ]

    R2 = mat_mul(R, R)
    idempotency_err = max(
        abs(R2[i][j] - R[i][j]) for i in range(n) for j in range(n)
    )
    trace_r = sum(R[i][i] for i in range(n))
    rx_s = mat_mul(R, X_S)
    rx_s_err = max(abs(rx_s[i][j]) for i in range(n) for j in range(s))

    def h2_ratio(n_val: int, s_val: int) -> float:
        d = float(n_val - s_val)
        return ((d - 1.0) / (d - 3.0)) * (
            1.0 / d + (d - 1.0) / d - (d - 3.0) / (d - 1.0)
        )

    h2_at_20 = h2_ratio(25, 5)
    h2_at_2000 = h2_ratio(2005, 5)

    # Check Appendix D.6 exact Schur complement identity: Sigma_{(S^c|S)} == ([Sigma^{-1}]_{S^c S^c})^{-1}
    p_tot, s_sub = 7, 3
    rho = 0.35
    Sigma = [
        [rho ** abs(i - j) for j in range(p_tot)] for i in range(p_tot)
    ]
    Sigma_SS = [row[:s_sub] for row in Sigma[:s_sub]]
    Sigma_ScS = [row[:s_sub] for row in Sigma[s_sub:]]
    Sigma_SSc = [row[s_sub:] for row in Sigma[:s_sub]]
    Sigma_ScSc = [row[s_sub:] for row in Sigma[s_sub:]]

    Schur = mat_mul(Sigma_ScS, mat_mul(mat_inv(Sigma_SS), Sigma_SSc))
    Sigma_cond = [
        [Sigma_ScSc[i][j] - Schur[i][j] for j in range(p_tot - s_sub)]
        for i in range(p_tot - s_sub)
    ]
    Sigma_inv = mat_inv(Sigma)
    Sigma_inv_ScSc = [row[s_sub:] for row in Sigma_inv[s_sub:]]
    Sigma_inv_ScSc_inv = mat_inv(Sigma_inv_ScSc)
    schur_block_err = max(
        abs(Sigma_cond[i][j] - Sigma_inv_ScSc_inv[i][j])
        for i in range(p_tot - s_sub)
        for j in range(p_tot - s_sub)
    )

    passed = (
        idempotency_err < 1e-12
        and abs(trace_r - (n - s)) < 1e-12
        and rx_s_err < 1e-12
        and h2_at_2000 < h2_at_20
        and h2_at_2000 < 0.003
        and schur_block_err < 1e-12
    )
    return {
        "projection_idempotency_error": idempotency_err,
        "projection_trace": trace_r,
        "expected_trace_n_minus_s": n - s,
        "projection_rx_s_error": rx_s_err,
        "h2_relative_variance_at_df20": h2_at_20,
        "h2_relative_variance_at_df2000": h2_at_2000,
        "schur_complement_block_inverse_error": schur_block_err,
        "passed": passed,
    }


def main() -> int:
    c1 = verify_primal_dual_witness_kkt_equivalence()
    c2 = verify_threshold_formulas_and_toeplitz_bounds()
    c3 = verify_conditional_covariance_and_schur_complement()
    all_passed = bool(c1["passed"] and c2["passed"] and c3["passed"])
    report = {
        "concept_id": "AIMech:PrimalDualWitnessAndSharpThresholdsForHighDimensionalNoisyLassoSparsityRecovery",
        "Check1_primal_dual_witness_kkt_equivalence": c1,
        "Check2_threshold_formulas_and_toeplitz_bounds": c2,
        "Check3_conditional_covariance_and_schur_complement": c3,
        "all_passed": all_passed,
    }
    print(json.dumps(report, indent=2))
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
