#!/usr/bin/env python3
"""Constructed boundary & regime verification for Cai, Liu, & Luo (2011) CLIME.

Paper: "A Constrained l1 Minimization Approach to Sparse Precision Matrix
Estimation", Journal of the American Statistical Association 106(494):594-607
(2011), arXiv:1102.2233v1, DOI:10.1198/jasa.2011.tm10155.

Verifies:
1. Columnwise convex decomposition (Lemma 1, Eqs. 1-3) and minimum-magnitude
   symmetrization (Eq. 2) on a constructed 4x4 sparse precision matrix Omega_0
   that VIOLATES the Ravikumar et al. (2011) log-determinant edge-Hessian
   irrepresentable condition ||Gamma_{S^c S} (Gamma_{SS})^{-1}||_{L1} > 1
   (4-node diamond precision matrix with rho = 0.22 > (sqrt(2)-1)/2 = 0.2071),
   demonstrating that CLIME requires no edge-Hessian mutual incoherence.
2. Exact deterministic master perturbation chain (Theorem 6, Eqs. 13-15 and
   23-27): when |Sigma_n - Sigma_0|_infty <= lambda_n / ||Omega_0||_{L1},
   verify feasibility |I - Sigma_n Omega_0|_infty <= lambda_n (Eq. 24),
   column l1 optimality ||Omega_hat_1||_{L1} <= ||Omega_0||_{L1} (Eq. 25),
   residual bound |Sigma_n(Omega_hat_1 - Omega_0)|_infty <= 2*lambda_n (Eq. 26),
   population-scaled residual |Sigma_0(Omega_hat_1 - Omega_0)|_infty <= 4*lambda_n,
   elementwise l_infty bound |Omega_hat - Omega_0|_infty <= 4*||Omega_0||_{L1}*lambda_n
   (Eq. 13), cone-like decomposition |h_j^2|_1 <= |h_j^1|_1 and
   |h_j|_1 <= 2*(1 + 2^{1-q} + 3^{1-q})*t_n^{1-q}*s_0(p) (Eqs. 14 & 27),
   Frobenius bound p^{-1} ||Omega_hat - Omega_0||_F^2 <= C_5 s_0(p) lambda_n^{2-q}
   (Eq. 15), and Theorem 7 signed support recovery M(Omega_tilde) = M(Omega_0)
   at threshold tau_n = 4*M*lambda_n when theta_min > 2*tau_n.
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


def mat_inv(a: list[list[float]]) -> list[list[float]]:
    n = len(a)
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(a)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(aug[r][col]))
        aug[col], aug[piv] = aug[piv], aug[col]
        div = aug[col][col]
        for j in range(2 * n):
            aug[col][j] /= div
        for r in range(n):
            if r != col:
                fac = aug[r][col]
                for j in range(2 * n):
                    aug[r][j] -= fac * aug[col][j]
    return [row[n:] for row in aug]


def mat_sub(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def eye(n: int) -> list[list[float]]:
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def norm_inf_elem(a: list[list[float]]) -> float:
    """Elementwise l_infty norm |A|_infty = max_{i,j} |a_{ij}| (p. 6)."""
    return max(abs(x) for row in a for x in row)


def norm_l1_mat(a: list[list[float]]) -> float:
    """Matrix L1 norm ||A||_{L1} = max_j sum_i |a_{ij}| (p. 6)."""
    p = len(a)
    return max(sum(abs(a[i][j]) for i in range(p)) for j in range(p))


def norm_frob_sq(a: list[list[float]]) -> float:
    return sum(x * x for row in a for x in row)


def symmetrize_clime(omega_1: list[list[float]]) -> list[list[float]]:
    """Minimum-magnitude symmetrization (Eq. 2, p. 6)."""
    p = len(omega_1)
    out = [[0.0] * p for _ in range(p)]
    for i in range(p):
        for j in range(p):
            w_ij = omega_1[i][j]
            w_ji = omega_1[j][i]
            out[i][j] = w_ij if abs(w_ij) <= abs(w_ji) else w_ji
    return out


def solve_clime_column_coordinate_search(
    sigma_n: list[list[float]],
    omega_0_col: list[float],
    col_idx: int,
    lambda_n: float,
) -> list[float]:
    """Find a feasible column beta_hat_i with |beta_hat_i|_1 <= |omega_0_i|_1
    and |Sigma_n beta_hat_i - e_i|_infty <= lambda_n by coordinate shrinkage."""
    p = len(sigma_n)
    # Start from omega_0_col (which is guaranteed feasible by Eq. 24) and
    # perform coordinate shrinkage toward zero while preserving feasibility
    beta = omega_0_col[:]
    for step_scale in [0.002, 0.0005, 0.0001]:
        improved = True
        while improved:
            improved = False
            for j in range(p):
                if abs(beta[j]) < step_scale:
                    cand_val = 0.0
                else:
                    cand_val = beta[j] - math.copysign(step_scale, beta[j])
                if cand_val == beta[j]:
                    continue
                old_val = beta[j]
                beta[j] = cand_val
                # Check feasibility |Sigma_n beta - e_i|_infty <= lambda_n
                feas = True
                for k in range(p):
                    res_k = sum(sigma_n[k][m] * beta[m] for m in range(p)) - (
                        1.0 if k == col_idx else 0.0
                    )
                    if abs(res_k) > lambda_n + 1e-12:
                        feas = False
                        break
                if feas and sum(abs(x) for x in beta) < sum(abs(x) for x in beta) - old_val + abs(old_val):
                    improved = True
                elif not feas:
                    beta[j] = old_val
    return beta


def main() -> int:
    # 1. Construct a 4-node diamond graph covariance/precision model where
    # the log-determinant edge-Hessian irrepresentable condition (Eq. 17, p. 15)
    # FAILS: for rho = 0.22 > (sqrt(2)-1)/2 = 0.20710678,
    # 4 * |rho| * (|rho| + 1) = 4 * 0.22 * 1.22 = 1.0736 > 1.
    rho = 0.22
    glasso_incoherence_param = 4.0 * abs(rho) * (abs(rho) + 1.0)
    sigma_0 = [
        [1.0, rho, rho, 2.0 * rho * rho],
        [rho, 1.0, 0.0, rho],
        [rho, 0.0, 1.0, rho],
        [2.0 * rho * rho, rho, rho, 1.0],
    ]
    omega_0 = mat_inv(sigma_0)
    p = 4
    # Clean near-zero entries (0,3) and (1,2) in omega_0 due to floating point
    for i in range(p):
        for j in range(p):
            if abs(omega_0[i][j]) < 1e-14:
                omega_0[i][j] = 0.0

    m_l1 = norm_l1_mat(omega_0)
    # Sparsity s_0(p) for q = 0 (exact max row support size, which is 3 on diamond graph)
    s0_q0 = max(sum(1 for j in range(p) if abs(omega_0[i][j]) > 0.0) for i in range(p))

    # 2. Construct perturbed sample covariance Sigma_n with |Sigma_n - Sigma_0|_infty = eps_cov
    eps_cov = 0.002
    sigma_n = [[0.0] * p for _ in range(p)]
    for i in range(p):
        for j in range(p):
            pert = eps_cov * math.sin(1.7 * i + 2.3 * j + 0.5)
            sigma_n[i][j] = sigma_0[i][j] + pert
    for i in range(p):
        for j in range(i + 1, p):
            avg = 0.5 * (sigma_n[i][j] + sigma_n[j][i])
            sigma_n[i][j] = avg
            sigma_n[j][i] = avg

    actual_cov_err = norm_inf_elem(mat_sub(sigma_n, sigma_0))
    # Set lambda_n = ||Omega_0||_{L1} * actual_cov_err (exact threshold in Theorem 6)
    lambda_n = m_l1 * actual_cov_err

    # Check Eq. (24): |I - Sigma_n Omega_0|_infty <= lambda_n
    eye_p = eye(p)
    eq24_lhs = norm_inf_elem(mat_sub(eye_p, mat_mul(sigma_n, omega_0)))

    # Solve each column problem (Lemma 1, Eq. 3)
    cols_hat = []
    for col_idx in range(p):
        omega_0_col = [omega_0[r][col_idx] for r in range(p)]
        beta_hat = solve_clime_column_coordinate_search(
            sigma_n, omega_0_col, col_idx, lambda_n
        )
        cols_hat.append(beta_hat)

    omega_hat_1 = [[cols_hat[j][i] for j in range(p)] for i in range(p)]
    omega_hat = symmetrize_clime(omega_hat_1)

    # Check Eq. (25): ||Omega_hat_1||_{L1} <= ||Omega_0||_{L1}
    l1_omega_hat_1 = norm_l1_mat(omega_hat_1)
    l1_omega_hat = norm_l1_mat(omega_hat)

    # Check Eq. (26): |Sigma_n (Omega_hat_1 - Omega_0)|_infty <= 2 * lambda_n
    diff_1 = mat_sub(omega_hat_1, omega_0)
    eq26_lhs = norm_inf_elem(mat_mul(sigma_n, diff_1))

    # Check population-scaled residual: |Sigma_0 (Omega_hat_1 - Omega_0)|_infty <= 4 * lambda_n
    pop_res_lhs = norm_inf_elem(mat_mul(sigma_0, diff_1))

    # Check Eq. (13): |Omega_hat - Omega_0|_infty <= 4 * ||Omega_0||_{L1} * lambda_n
    diff_sym = mat_sub(omega_hat, omega_0)
    t_n = norm_inf_elem(diff_sym)
    eq13_rhs = 4.0 * m_l1 * lambda_n

    # Check cone-like decomposition |h_j^2|_1 <= |h_j^1|_1 and Eq. (27) for q = 0
    cone_holds = True
    eq27_holds = True
    max_col_l1_err = 0.0
    for j in range(p):
        h_j = [omega_hat[i][j] - omega_0[i][j] for i in range(p)]
        h_j_1 = [
            (omega_hat[i][j] if abs(omega_hat[i][j]) >= 2.0 * t_n else 0.0)
            - omega_0[i][j]
            for i in range(p)
        ]
        h_j_2 = [h_j[i] - h_j_1[i] for i in range(p)]
        norm_hj1 = sum(abs(x) for x in h_j_1)
        norm_hj2 = sum(abs(x) for x in h_j_2)
        norm_hj = sum(abs(x) for x in h_j)
        max_col_l1_err = max(max_col_l1_err, norm_hj)
        if norm_hj2 > norm_hj1 + 1e-12:
            cone_holds = False
        if norm_hj1 > (1.0 + 2.0 + 3.0) * t_n * s0_q0 + 1e-12:
            eq27_holds = False

    # Check Eq. (14) and Eq. (15) (Theorem 6 spectral/L1 and Frobenius bounds for q = 0)
    c4_q0 = 2.0 * (1.0 + 2.0 + 3.0) * (4.0 * m_l1)
    c5_q0 = 4.0 * m_l1 * c4_q0
    eq14_rhs = c4_q0 * s0_q0 * lambda_n
    frob_avg = norm_frob_sq(diff_sym) / p
    eq15_rhs = c5_q0 * s0_q0 * (lambda_n ** 2)

    # Check Theorem 7 signed support recovery M(Omega_tilde) = M(Omega_0)
    tau_n = 4.0 * m_l1 * lambda_n
    theta_min = min(
        abs(omega_0[i][j])
        for i in range(p)
        for j in range(p)
        if abs(omega_0[i][j]) > 0.0
    )
    omega_tilde = [
        [
            omega_hat[i][j] if abs(omega_hat[i][j]) >= tau_n else 0.0
            for j in range(p)
        ]
        for i in range(p)
    ]

    def sgn(x: float) -> int:
        if x > 0.0:
            return 1
        if x < 0.0:
            return -1
        return 0

    sign_match = all(
        sgn(omega_tilde[i][j]) == sgn(omega_0[i][j])
        for i in range(p)
        for j in range(p)
    )

    checks = {
        "glasso_incoherence_violated_gt_1": glasso_incoherence_param > 1.0,
        "eq24_omega0_feasible": eq24_lhs <= lambda_n + 1e-12,
        "eq25_column_l1_optimality": (
            l1_omega_hat <= l1_omega_hat_1 + 1e-12 <= m_l1 + 1e-12
        ),
        "eq26_sample_residual_bound": eq26_lhs <= 2.0 * lambda_n + 1e-12,
        "pop_residual_bound_4lambda": pop_res_lhs <= 4.0 * lambda_n + 1e-12,
        "eq13_linf_bound_holds": t_n <= eq13_rhs + 1e-12,
        "cone_decomposition_hj2_le_hj1": cone_holds,
        "eq27_hj1_bound_holds": eq27_holds,
        "eq14_l1_bound_holds": max_col_l1_err <= eq14_rhs + 1e-12,
        "eq15_frob_bound_holds": frob_avg <= eq15_rhs + 1e-12,
        "thm7_theta_min_gt_2tau_n": theta_min > 2.0 * tau_n,
        "thm7_exact_signed_support_recovery": sign_match,
    }
    all_passed = all(checks.values())

    summary = {
        "rho_diamond": rho,
        "glasso_incoherence_param": round(glasso_incoherence_param, 6),
        "omega0_l1_norm_M": round(m_l1, 8),
        "sparsity_s0_q0": s0_q0,
        "actual_cov_err": round(actual_cov_err, 8),
        "lambda_n": round(lambda_n, 8),
        "eq24_lhs": round(eq24_lhs, 8),
        "l1_omega_hat_1": round(l1_omega_hat_1, 8),
        "l1_omega_hat": round(l1_omega_hat, 8),
        "eq26_lhs": round(eq26_lhs, 8),
        "pop_res_lhs": round(pop_res_lhs, 8),
        "linf_err_tn": round(t_n, 8),
        "eq13_rhs": round(eq13_rhs, 8),
        "max_col_l1_err": round(max_col_l1_err, 8),
        "eq14_rhs": round(eq14_rhs, 8),
        "frob_avg": round(frob_avg, 10),
        "eq15_rhs": round(eq15_rhs, 8),
        "tau_n": round(tau_n, 8),
        "theta_min": round(theta_min, 8),
        "checks": checks,
        "all_passed": all_passed,
    }
    print(json.dumps(summary, sort_keys=True))
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
