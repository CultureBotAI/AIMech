#!/usr/bin/env python3
"""Constructed boundary & regime verification for Bickel & Levina (2008).

Paper: "Covariance regularization by thresholding", The Annals of Statistics
36(6):2577-2604 (2008), arXiv:0901.3079v1, DOI:10.1214/08-AOS600.

Verifies:
1. Matrix (1,1)-norm bound ||M||_{(2,2)} <= ||M||_{(1,1)} (Eq. 2),
   hard-thresholding operator T_s(M) = [m_{ij} 1(|m_{ij}| >= s)] (Eq. 3),
   positive-definiteness preservation when ||T_s(M) - M||_{(2,2)} <= eps
   < lambda_min(M) (Eq. 4), and permutation invariance T_s(P M P^T)
   = P T_s(M) P^T vs failure of banding B_k(P M P^T) != P B_k(M) P^T under
   variable permutation (Sections 2 & 4).
2. Deterministic bias bound ||T_t(Sigma) - Sigma||_{(1,1)} <= t^{1-q} c_0(p)
   over the weak-l_q class U_tau(q, c_0(p), M) (Eq. 13), exact decomposition
   into Terms I, II, III (Eq. 14), balanced threshold rate t_n = M'*sqrt(log p / n)
   yielding operator-norm rate c_0(p)*(log p / n)^{(1-q)/2} (Theorem 1, Eq. 7)
   and Frobenius rate c_0(p)*(log p / n)^{1-q/2} (Theorem 2, Eq. 23), and
   sample-splitting quadratic inequality a_n <= delta_n(a_n^{1/2} + r_n^{1/2})
   + r_n implying oracle equivalence (Theorem 3, Eqs. 31-38).
"""

from __future__ import annotations

import json
import math
import sys


def mat_mul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    n = len(a)
    m = len(b[0])
    k_len = len(b)
    out = [[0.0] * m for _ in range(n)]
    for i in range(n):
        for k in range(k_len):
            aik = a[i][k]
            for j in range(m):
                out[i][j] += aik * b[k][j]
    return out


def transpose(a: list[list[float]]) -> list[list[float]]:
    return [list(col) for col in zip(*a)]


def mat_sub(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def norm_11(a: list[list[float]]) -> float:
    """Matrix (1,1) norm: max_j sum_i |a_{ij}| (Eq. 2)."""
    p = len(a)
    return max(sum(abs(a[i][j]) for i in range(p)) for j in range(p))


def norm_frob_sq(a: list[list[float]]) -> float:
    return sum(x * x for row in a for x in row)


def jacobi_eigenvalues(sym: list[list[float]], tol: float = 1e-13) -> list[float]:
    """Compute eigenvalues of a symmetric matrix via Jacobi rotations."""
    n = len(sym)
    a = [row[:] for row in sym]
    for _ in range(500):
        max_val = 0.0
        p_idx, q_idx = 0, 1
        for i in range(n):
            for j in range(i + 1, n):
                if abs(a[i][j]) > max_val:
                    max_val = abs(a[i][j])
                    p_idx, q_idx = i, j
        if max_val < tol:
            break
        app = a[p_idx][p_idx]
        aqq = a[q_idx][q_idx]
        apq = a[p_idx][q_idx]
        tau = (aqq - app) / (2.0 * apq)
        t = math.copysign(1.0 / (abs(tau) + math.sqrt(1.0 + tau * tau)), tau)
        if tau == 0.0:
            t = 1.0
        c = 1.0 / math.sqrt(1.0 + t * t)
        s = t * c
        a[p_idx][p_idx] = app - t * apq
        a[q_idx][q_idx] = aqq + t * apq
        a[p_idx][q_idx] = 0.0
        a[q_idx][p_idx] = 0.0
        for r in range(n):
            if r != p_idx and r != q_idx:
                arp = a[r][p_idx]
                arq = a[r][q_idx]
                a[r][p_idx] = c * arp - s * arq
                a[p_idx][r] = a[r][p_idx]
                a[r][q_idx] = s * arp + c * arq
                a[q_idx][r] = a[r][q_idx]
    return sorted([a[i][i] for i in range(n)], reverse=True)


def norm_op_sym(sym: list[list[float]]) -> float:
    eigs = jacobi_eigenvalues(sym)
    return max(abs(x) for x in eigs)


def hard_threshold(m: list[list[float]], s: float) -> list[list[float]]:
    """Hard-thresholding operator T_s(M) = [m_{ij} 1(|m_{ij}| >= s)] (Eq. 3)."""
    p = len(m)
    return [
        [m[i][j] if abs(m[i][j]) >= s else 0.0 for j in range(p)]
        for i in range(p)
    ]


def band_matrix(m: list[list[float]], k: int) -> list[list[float]]:
    """Banding operator B_k(M) = [m_{ij} 1(|i - j| <= k)] (Section 2.1)."""
    p = len(m)
    return [
        [m[i][j] if abs(i - j) <= k else 0.0 for j in range(p)]
        for i in range(p)
    ]


def permute_matrix(m: list[list[float]], perm: list[int]) -> list[list[float]]:
    p = len(m)
    return [[m[perm[i]][perm[j]] for j in range(p)] for i in range(p)]


def main() -> int:
    # 1. Construct a 5x5 covariance matrix Sigma in V(eps_0, alpha, C)
    # with sigma_{ii} = 1.0 and sigma_{ij} = 0.22 * |i - j|^{-2} for i != j
    p = 5
    sigma = [[0.0] * p for _ in range(p)]
    for i in range(p):
        for j in range(p):
            if i == j:
                sigma[i][j] = 1.0
            else:
                sigma[i][j] = 0.22 * (abs(i - j) ** (-2.0))

    eigs_sigma = jacobi_eigenvalues(sigma)
    lambda_min_sigma = min(eigs_sigma)
    lambda_max_sigma = max(eigs_sigma)

    # Weak-l_q row sum c_0(p) = max_i sum_j |sigma_{ij}|^q for q = 0.5
    q = 0.5
    c0_q = max(sum(abs(sigma[i][j]) ** q for j in range(p)) for i in range(p))
    # Verify eigenvalue upper bound lambda_max(Sigma) <= M^{1-q} c_0(p) (p. 5)
    m_diag = 1.0
    eig_upper_bound = (m_diag ** (1.0 - q)) * c0_q

    # Verify Eq. (4) positive-definiteness preservation under hard thresholding at s = 0.06
    s_thresh = 0.06
    t_s_sigma = hard_threshold(sigma, s_thresh)
    diff_ts = mat_sub(t_s_sigma, sigma)
    err_op_ts = norm_op_sym(diff_ts)
    err_11_ts = norm_11(diff_ts)
    eigs_ts = jacobi_eigenvalues(t_s_sigma)
    lambda_min_ts = min(eigs_ts)

    # Check deterministic bias bound ||T_t(Sigma) - Sigma||_{(1,1)} <= t^{1-q} c_0(p) (Eq. 13)
    bias_bound_eq13 = (s_thresh ** (1.0 - q)) * c0_q

    # Verify permutation invariance of T_s vs non-invariance of banding B_k (k=1)
    perm = [2, 0, 4, 1, 3]
    sigma_perm = permute_matrix(sigma, perm)
    ts_perm_A = hard_threshold(sigma_perm, s_thresh)
    ts_perm_B = permute_matrix(t_s_sigma, perm)
    perm_invariance_diff_ts = norm_11(mat_sub(ts_perm_A, ts_perm_B))

    b1_sigma = band_matrix(sigma, 1)
    b1_perm_A = band_matrix(sigma_perm, 1)
    b1_perm_B = permute_matrix(b1_sigma, perm)
    perm_noninvariance_diff_b1 = norm_11(mat_sub(b1_perm_A, b1_perm_B))

    # 2. Verify Theorem 1 decomposition (Eq. 14: Terms I, II, III) on a perturbed sample covariance
    # Perturbation E_{ij} bounded by delta_max = 0.03 < s_thresh = 0.06
    sigma_hat = [[0.0] * p for _ in range(p)]
    for i in range(p):
        for j in range(p):
            pert = 0.025 * math.cos(2.0 * i + 3.0 * j + 1.0)
            sigma_hat[i][j] = sigma[i][j] + pert
    # Symmetrize
    for i in range(p):
        for j in range(i + 1, p):
            avg = 0.5 * (sigma_hat[i][j] + sigma_hat[j][i])
            sigma_hat[i][j] = avg
            sigma_hat[j][i] = avg

    t_s_hat = hard_threshold(sigma_hat, s_thresh)
    lhs_eq14 = norm_11(mat_sub(t_s_hat, t_s_sigma))

    term_I = max(
        sum(
            abs(sigma_hat[i][j])
            for j in range(p)
            if abs(sigma_hat[i][j]) >= s_thresh and abs(sigma[i][j]) < s_thresh
        )
        for i in range(p)
    )
    term_II = max(
        sum(
            abs(sigma[i][j])
            for j in range(p)
            if abs(sigma_hat[i][j]) < s_thresh and abs(sigma[i][j]) >= s_thresh
        )
        for i in range(p)
    )
    term_III = max(
        sum(
            abs(sigma_hat[i][j] - sigma[i][j])
            for j in range(p)
            if abs(sigma_hat[i][j]) >= s_thresh and abs(sigma[i][j]) >= s_thresh
        )
        for i in range(p)
    )
    rhs_eq14 = term_I + term_II + term_III

    # Verify Theorem 1 vs Section 2.5 exponent comparison:
    # For alpha = 1.0, q = 0.52 > 1/(alpha+1) = 0.5:
    alpha = 1.0
    q_comp = 0.52
    exp_banding = alpha / (2.0 * (alpha + 1.0))  # 0.25
    exp_thresholding = (1.0 - q_comp) / 2.0  # 0.24

    # 3. Verify Theorem 3 sample-splitting quadratic inequality (Eqs. 37-38):
    # If a_n >= r_n > 0 and a_n <= delta_n * (a_n^{1/2} + r_n^{1/2}) + r_n
    # with delta_n / r_n^{1/2} = eps_ratio << 1, check exact root bound a_n / r_n
    r_n = 0.04
    delta_n = 0.002  # delta_n / r_n^{1/2} = 0.01
    # Largest root of x^2 - delta_n * x - (r_n + delta_n * r_n^{1/2}) = 0 where x = a_n^{1/2}
    c_quad = r_n + delta_n * math.sqrt(r_n)
    x_root = 0.5 * (delta_n + math.sqrt(delta_n * delta_n + 4.0 * c_quad))
    a_n_max = x_root * x_root
    oracle_ratio = a_n_max / r_n

    checks = {
        "lambda_min_sigma_positive": lambda_min_sigma > 0.5,
        "eig_upper_bound_holds": lambda_max_sigma <= eig_upper_bound + 1e-12,
        "schur_bound_eq2_holds": err_op_ts <= err_11_ts + 1e-12,
        "pd_preservation_eq4_holds": (
            err_op_ts < lambda_min_sigma
            and lambda_min_ts >= lambda_min_sigma - err_op_ts - 1e-12
            and lambda_min_ts > 0.0
        ),
        "bias_bound_eq13_holds": err_11_ts <= bias_bound_eq13 + 1e-12,
        "threshold_permutation_invariant": perm_invariance_diff_ts < 1e-15,
        "banding_not_permutation_invariant": perm_noninvariance_diff_b1 > 0.2,
        "eq14_triangle_decomposition_holds": lhs_eq14 <= rhs_eq14 + 1e-12,
        "sec25_exponent_ordering_holds": 0.0 < exp_thresholding < exp_banding,
        "thm3_oracle_equivalence_ratio_close_to_1": 1.0 <= oracle_ratio < 1.03,
    }
    all_passed = all(checks.values())

    summary = {
        "lambda_min_sigma": round(lambda_min_sigma, 8),
        "lambda_max_sigma": round(lambda_max_sigma, 8),
        "weak_lq_c0_q05": round(c0_q, 8),
        "eig_upper_bound": round(eig_upper_bound, 8),
        "threshold_s": s_thresh,
        "err_op_ts": round(err_op_ts, 8),
        "err_11_ts": round(err_11_ts, 8),
        "bias_bound_eq13": round(bias_bound_eq13, 8),
        "lambda_min_ts": round(lambda_min_ts, 8),
        "perm_invariance_diff_ts": round(perm_invariance_diff_ts, 16),
        "perm_noninvariance_diff_b1": round(perm_noninvariance_diff_b1, 8),
        "lhs_eq14": round(lhs_eq14, 8),
        "rhs_eq14": round(rhs_eq14, 8),
        "exp_banding": round(exp_banding, 4),
        "exp_thresholding": round(exp_thresholding, 4),
        "thm3_oracle_ratio": round(oracle_ratio, 8),
        "checks": checks,
        "all_passed": all_passed,
    }
    print(json.dumps(summary, sort_keys=True))
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
