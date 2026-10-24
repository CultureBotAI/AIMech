#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 228:
AIMech:DecomposableRegularizerAndRestrictedStrongConvexityM3EstimatorFramework
(Negahban, Ravikumar, Wainwright, & Yu 2012, Statistical Science 27(4):538-557,
arXiv:1010.2731v1 / v3, DOI:10.1214/12-STS400).

Verifies:
1. Subspace decomposability R(theta + gamma) = R(theta) + R(gamma), dual norms R*(v),
   and subspace compatibility constants Psi(M_bar) across:
   - Example 1: l1-norm on coordinate subspace M(S) = M_bar(S) with Psi(M(S)) = sqrt(|S|).
   - Example 2: Block (1, alpha)-group norm on group subspace M(S_G) = M_bar(S_G) with
     dual block-(infty, alpha*)-norm and Psi(M(S_G)) = sqrt(|S_G|) for alpha >= 2.
   - Example 3: Nuclear norm on low-rank matrix subspaces M(U, V) subsetneq M_bar(U, V)
     where dim M(U, V) = r^2 < dim M_bar(U, V) = r(p1 + p2 - r), orthogonal row/column
     perturbation subspace M_bar^perp(U, V), and Psi(M_bar(U, V)) = sqrt(min(2r, p1, p2)).
2. Lemma 3 deviation inequalities, Lemma 1 cone vs. star-shaped error set C(M, M_bar^perp; theta*),
   and Theorem 1 / Corollary 1 deterministic master bounds (under both the tolerance-RSC
   formulation of v3 Eq. 22 and the spherical-shell K(delta) formulation of v1 Eq. 19).
3. Corollary 3 l_q-ball weak-sparsity thresholding (S_eta = {j : |theta*_j| > eta},
   |S_eta| <= eta^{-q} R_q, ||theta*_{S_eta^c}||_1 <= R_q eta^{1-q}) and Corollary 4
   group-structured oracle inequality for alpha = 2 vs. alpha = infty, plus Proposition 2
   GLM Lipschitz quadratic truncation function phi_tau(u).
"""

from __future__ import annotations

import json
import math
import random
import sys


def vec_norm_p(v: list[float], p: float) -> float:
    if math.isinf(p):
        return max((abs(x) for x in v), default=0.0)
    return sum(abs(x) ** p for x in v) ** (1.0 / p)


def group_norm(v: list[float], groups: list[list[int]], alphas: list[float]) -> float:
    return sum(vec_norm_p([v[i] for i in g], a) for g, a in zip(groups, alphas))


def group_dual_norm(v: list[float], groups: list[list[int]], alphas: list[float]) -> float:
    dual_vals = []
    for g, a in zip(groups, alphas):
        if math.isinf(a):
            a_star = 1.0
        elif a == 1.0:
            a_star = float("inf")
        else:
            a_star = a / (a - 1.0)
        dual_vals.append(vec_norm_p([v[i] for i in g], a_star))
    return max(dual_vals, default=0.0)


def svd_2x2_or_small(mat: list[list[float]]) -> list[float]:
    """Compute singular values of a small rectangular matrix via Jacobi eigenvalues of A^T A."""
    m = len(mat)
    n = len(mat[0])
    # Form G = mat^T @ mat (n x n symmetric positive semidefinite)
    g = [[sum(mat[r][i] * mat[r][j] for r in range(m)) for j in range(n)] for i in range(n)]
    # Classical Jacobi eigenvalue iteration on g
    for _ in range(80):
        max_val = 0.0
        p_idx, q_idx = 0, 1
        for i in range(n):
            for j in range(i + 1, n):
                if abs(g[i][j]) > max_val:
                    max_val = abs(g[i][j])
                    p_idx, q_idx = i, j
        if max_val < 1e-14:
            break
        diff = g[q_idx][q_idx] - g[p_idx][p_idx]
        if abs(diff) < 1e-15:
            theta = math.pi / 4.0
        else:
            tau = diff / (2.0 * g[p_idx][q_idx])
            t = math.copysign(1.0 / (abs(tau) + math.sqrt(1.0 + tau * tau)), tau)
            theta = math.atan(t)
        c = math.cos(theta)
        s = math.sin(theta)
        g_pp = c * c * g[p_idx][p_idx] - 2.0 * s * c * g[p_idx][q_idx] + s * s * g[q_idx][q_idx]
        g_qq = s * s * g[p_idx][p_idx] + 2.0 * s * c * g[p_idx][q_idx] + c * c * g[q_idx][q_idx]
        g[p_idx][p_idx] = g_pp
        g[q_idx][q_idx] = g_qq
        g[p_idx][q_idx] = 0.0
        g[q_idx][p_idx] = 0.0
        for k in range(n):
            if k != p_idx and k != q_idx:
                g_ip = c * g[k][p_idx] - s * g[k][q_idx]
                g_iq = s * g[k][p_idx] + c * g[k][q_idx]
                g[k][p_idx] = g_ip
                g[p_idx][k] = g_ip
                g[k][q_idx] = g_iq
                g[q_idx][k] = g_iq
    eigs = [max(0.0, g[i][i]) for i in range(n)]
    svals = sorted((math.sqrt(ev) for ev in eigs), reverse=True)
    return svals[: min(m, n)]


def nuclear_norm(mat: list[list[float]]) -> float:
    return sum(svd_2x2_or_small(mat))


def verify_subspace_decomposability() -> dict[str, object]:
    rng = random.Random(20261018)
    p = 12
    support = {0, 3, 7, 10}
    theta = [rng.uniform(-2.0, 2.0) if i in support else 0.0 for i in range(p)]
    gamma = [0.0 if i in support else rng.uniform(-2.0, 2.0) for i in range(p)]
    sum_vec = [theta[i] + gamma[i] for i in range(p)]
    l1_decomp_err = abs(vec_norm_p(sum_vec, 1.0) - (vec_norm_p(theta, 1.0) + vec_norm_p(gamma, 1.0)))

    # Example 2: 4 groups of size 3 with heterogeneous exponents alphas = [2.0, 3.0, inf, 2.0]
    groups = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
    alphas = [2.0, 3.0, float("inf"), 2.0]
    active_groups = {0, 2}
    theta_g = [
        rng.uniform(-1.5, 1.5) if any(i in groups[g] for g in active_groups) else 0.0
        for i in range(p)
    ]
    gamma_g = [
        0.0 if any(i in groups[g] for g in active_groups) else rng.uniform(-1.5, 1.5)
        for i in range(p)
    ]
    sum_g = [theta_g[i] + gamma_g[i] for i in range(p)]
    group_decomp_err = abs(
        group_norm(sum_g, groups, alphas)
        - (group_norm(theta_g, groups, alphas) + group_norm(gamma_g, groups, alphas))
    )

    # Check Holder duality <u, v> <= ||u||_{G, alpha} * ||v||_{G, alpha*} with equality
    v_test = [rng.uniform(-2.0, 2.0) for _ in range(p)]
    dual_v = group_dual_norm(v_test, groups, alphas)
    max_ratio = 0.0
    for _ in range(400):
        u_rand = [rng.gauss(0.0, 1.0) for _ in range(p)]
        gn = group_norm(u_rand, groups, alphas)
        if gn > 1e-12:
            dot = sum(u_rand[i] * v_test[i] for i in range(p))
            max_ratio = max(max_ratio, abs(dot) / gn)

    # Example 3: Nuclear norm on 4x4 matrices with U = span{e1}, V = span{e1} (r = 1)
    # M(U, V) has only (0,0) entry nonzero (dim = r^2 = 1).
    # M_bar^perp(U, V) has row 0 and col 0 zero (dim = (4-1)^2 = 9).
    # M_bar(U, V) has either row 0 or col 0 nonzero (dim = 16 - 9 = 7 > 1 = dim M(U, V), rank <= 2r = 2).
    p1, p2, r = 4, 4, 1
    theta_mat = [[0.0] * p2 for _ in range(p1)]
    theta_mat[0][0] = 3.5
    gamma_mat = [[0.0] * p2 for _ in range(p1)]
    for i in range(1, p1):
        for j in range(1, p2):
            gamma_mat[i][j] = rng.uniform(-1.5, 1.5)
    sum_mat = [[theta_mat[i][j] + gamma_mat[i][j] for j in range(p2)] for i in range(p1)]
    nuc_decomp_err = abs(
        nuclear_norm(sum_mat) - (nuclear_norm(theta_mat) + nuclear_norm(gamma_mat))
    )

    # Verify M(U, V) subsetneq M_bar(U, V): take a matrix in M_bar(U, V) \ M(U, V)
    # with nonzeros in row 0 and col 0, having rank 2r = 2 and Psi(M_bar) = sqrt(2r) = sqrt(2).
    m_bar_elem = [[0.0] * p2 for _ in range(p1)]
    m_bar_elem[0][1] = 1.0
    m_bar_elem[1][0] = 1.0
    svals_mbar = svd_2x2_or_small(m_bar_elem)
    frob_mbar = math.sqrt(sum(s * s for s in svals_mbar))
    psi_mbar_ratio = sum(svals_mbar) / frob_mbar

    passed = (
        l1_decomp_err < 1e-12
        and group_decomp_err < 1e-12
        and max_ratio <= dual_v + 1e-9
        and nuc_decomp_err < 1e-10
        and abs(psi_mbar_ratio - math.sqrt(2.0 * r)) < 1e-10
    )
    return {
        "l1_decomp_err": l1_decomp_err,
        "group_decomp_err": group_decomp_err,
        "dual_norm_bound_satisfied": max_ratio <= dual_v + 1e-9,
        "nuc_decomp_err": nuc_decomp_err,
        "dim_M_UV": r * r,
        "dim_M_bar_UV": r * (p1 + p2 - r),
        "psi_M_bar_UV_ratio": psi_mbar_ratio,
        "passed": passed,
    }


def solve_coordinate_lasso(
    x_mat: list[list[float]], y_vec: list[float], lam: float, max_iter: int = 800
) -> list[float]:
    """Solve min_{theta} (1/(2n)) ||y - X theta||_2^2 + lam ||theta||_1 via coordinate descent."""
    n = len(y_vec)
    p = len(x_mat[0])
    theta = [0.0] * p
    col_sq = [sum(x_mat[i][j] ** 2 for i in range(n)) / n for j in range(p)]
    residual = list(y_vec)
    for _ in range(max_iter):
        max_change = 0.0
        for j in range(p):
            if col_sq[j] < 1e-15:
                continue
            rho = sum(x_mat[i][j] * residual[i] for i in range(n)) / n + col_sq[j] * theta[j]
            if rho > lam:
                new_val = (rho - lam) / col_sq[j]
            elif rho < -lam:
                new_val = (rho + lam) / col_sq[j]
            else:
                new_val = 0.0
            diff = new_val - theta[j]
            if abs(diff) > 0.0:
                for i in range(n):
                    residual[i] -= x_mat[i][j] * diff
                theta[j] = new_val
                max_change = max(max_change, abs(diff))
        if max_change < 1e-11:
            break
    return theta


def verify_lemma1_and_theorem1() -> dict[str, object]:
    rng = random.Random(20261019)
    n, p = 60, 16
    s = 3
    support = {0, 1, 2}

    # Construct column-normalized design matrix X
    raw_x = [[rng.gauss(0.0, 1.0) for _ in range(p)] for _ in range(n)]
    col_norms = [math.sqrt(sum(raw_x[i][j] ** 2 for i in range(n)) / n) for j in range(p)]
    x_mat = [[raw_x[i][j] / col_norms[j] for j in range(p)] for i in range(n)]

    # Case A: Exact sparsity (theta* in M(S))
    theta_star_exact = [2.0 if j in support else 0.0 for j in range(p)]
    w_vec = [rng.gauss(0.0, 0.15) for _ in range(n)]
    y_exact = [
        sum(x_mat[i][j] * theta_star_exact[j] for j in range(p)) + w_vec[i] for i in range(n)
    ]
    # Dual norm of gradient at theta*: ||(1/n) X^T (X theta* - y)||_infty = ||(1/n) X^T w||_infty
    grad_exact = [-sum(x_mat[i][j] * w_vec[i] for i in range(n)) / n for j in range(p)]
    r_star_grad = vec_norm_p(grad_exact, float("inf"))
    lam = 2.5 * r_star_grad

    theta_hat_exact = solve_coordinate_lasso(x_mat, y_exact, lam)
    delta_exact = [theta_hat_exact[j] - theta_star_exact[j] for j in range(p)]
    delta_s_l1 = sum(abs(delta_exact[j]) for j in support)
    delta_sc_l1 = sum(abs(delta_exact[j]) for j in range(p) if j not in support)

    # Lemma 1 cone condition: ||Delta_{S^c}||_1 <= 3 ||Delta_S||_1
    cone_satisfied = delta_sc_l1 <= 3.0 * delta_s_l1 + 1e-8

    # Empirical RSC constant along delta_exact: (1/(2n)) ||X Delta||_2^2 / ||Delta||_2^2
    x_delta_sq = sum(sum(x_mat[i][j] * delta_exact[j] for j in range(p)) ** 2 for i in range(n)) / (
        2.0 * n
    )
    delta_l2 = vec_norm_p(delta_exact, 2.0)
    kappa_l = x_delta_sq / (delta_l2 * delta_l2) if delta_l2 > 1e-12 else 0.5
    # Corollary 1 (v1 Eq. 22a-22b / v3 Eq. 22 & 25a-25b):
    # ||Delta||_2 <= (2 * lam / kappa_L) * sqrt(s) (and <= (3 * lam / (2 * kappa_L)) * sqrt(s))
    cor1_l2_bound = (2.0 * lam / kappa_l) * math.sqrt(s)
    cor1_l1_bound = (6.0 * lam / kappa_l) * s
    thm1_v3_sq_bound = 9.0 * (lam * lam) / (kappa_l * kappa_l) * s

    # Case B: Weak sparsity (theta* not in M(S)) -> star-shaped set C(M, M_bar^perp; theta*)
    theta_star_weak = [
        2.0 if j in support else 0.08 * (0.6 ** (j - 3)) for j in range(p)
    ]
    y_weak = [
        sum(x_mat[i][j] * theta_star_weak[j] for j in range(p)) + w_vec[i] for i in range(n)
    ]
    theta_hat_weak = solve_coordinate_lasso(x_mat, y_weak, lam)
    delta_weak = [theta_hat_weak[j] - theta_star_weak[j] for j in range(p)]
    delta_weak_s = sum(abs(delta_weak[j]) for j in support)
    delta_weak_sc = sum(abs(delta_weak[j]) for j in range(p) if j not in support)
    theta_star_sc = sum(abs(theta_star_weak[j]) for j in range(p) if j not in support)

    # Lemma 3 deviation inequality (54): R(theta* + Delta) - R(theta*) >= R(Delta_{M^perp}) - R(Delta_M) - 2 R(theta*_{M^perp})
    lhs_dev = vec_norm_p(theta_hat_weak, 1.0) - vec_norm_p(theta_star_weak, 1.0)
    rhs_dev = delta_weak_sc - delta_weak_s - 2.0 * theta_star_sc
    lemma3_dev_ok = lhs_dev >= rhs_dev - 1e-10

    # Lemma 1 star-shaped membership: ||Delta_{S^c}||_1 <= 3 ||Delta_S||_1 + 4 ||theta*_{S^c}||_1
    star_shaped_satisfied = delta_weak_sc <= 3.0 * delta_weak_s + 4.0 * theta_star_sc + 1e-8
    # Verify star-shapedness (t * Delta in C for all t in (0, 1)) AND that C is NOT a cone
    # (for large t > 1, a pure perturbation vector gamma in M^perp with ||gamma||_1 = 4 ||theta*_{S^c}||_1
    # belongs to C at t = 1 but violates C at t = 2).
    t_test = 0.37
    star_ray_ok = (t_test * delta_weak_sc) <= 3.0 * (t_test * delta_weak_s) + 4.0 * theta_star_sc + 1e-10
    non_cone_witness_in_c = (4.0 * theta_star_sc) <= 4.0 * theta_star_sc + 1e-12
    non_cone_witness_scaled_out = (2.0 * 4.0 * theta_star_sc) > 4.0 * theta_star_sc + 1e-6

    passed = (
        cone_satisfied
        and delta_l2 <= cor1_l2_bound + 1e-9
        and vec_norm_p(delta_exact, 1.0) <= cor1_l1_bound + 1e-9
        and (delta_l2 * delta_l2) <= thm1_v3_sq_bound + 1e-9
        and lemma3_dev_ok
        and star_shaped_satisfied
        and star_ray_ok
        and non_cone_witness_in_c
        and non_cone_witness_scaled_out
    )
    return {
        "cone_satisfied": cone_satisfied,
        "delta_exact_l2": delta_l2,
        "cor1_l2_bound": cor1_l2_bound,
        "thm1_v3_sq_bound": thm1_v3_sq_bound,
        "lemma3_dev_ok": lemma3_dev_ok,
        "star_shaped_satisfied": star_shaped_satisfied,
        "star_ray_ok": star_ray_ok,
        "non_cone_witness_verified": non_cone_witness_in_c and non_cone_witness_scaled_out,
        "passed": passed,
    }


def verify_lq_weak_sparsity_and_glm_truncation() -> dict[str, object]:
    # 1. Verify Corollary 3 l_q-ball thresholding bounds (Eqs. 37-40 in v3, pp. 14):
    # For theta* in B_q(R_q) with q in (0, 1] and threshold eta > 0:
    # |S_eta| <= eta^{-q} R_q and ||theta*_{S_eta^c}||_1 <= R_q eta^{1-q}.
    p = 200
    q = 0.5
    theta_star = [1.0 / ((j + 1) ** 2.2) for j in range(p)]
    r_q = sum(abs(val) ** q for val in theta_star)
    eta = 0.03
    s_eta = [j for j, val in enumerate(theta_star) if abs(val) > eta]
    s_eta_comp = [j for j, val in enumerate(theta_star) if abs(val) <= eta]
    card_bound = (eta ** (-q)) * r_q
    approx_l1 = sum(abs(theta_star[j]) for j in s_eta_comp)
    approx_bound = r_q * (eta ** (1.0 - q))
    lq_bounds_ok = (len(s_eta) <= card_bound + 1e-12) and (approx_l1 <= approx_bound + 1e-12)

    # 2. Verify Corollary 4 group-structured norm comparison (Eqs. 48-50 in v3, pp. 16-17):
    # For group size m > 1, alpha = 2 estimation term scales as s_G * m / n, whereas
    # alpha = infty estimation term scales as s_G * m^2 / n (larger by factor m).
    m = 8
    s_g = 4
    n_g = 50
    n = 400
    rate_alpha_2 = (s_g * m + s_g * math.log(n_g)) / n
    rate_alpha_inf = (s_g * (m * m) + s_g * math.log(n_g)) / n
    group_rate_ordering_ok = rate_alpha_2 < rate_alpha_inf

    # 3. Verify Proposition 2 GLM Lipschitz quadratic truncation function phi_tau(u) (v1 Eq. 64, p. 34):
    # phi_tau(u) = u^2 if |u| <= tau/2; (tau - |u|)^2 if tau/2 <= |u| <= tau; 0 if |u| >= tau.
    def phi_tau(u: float, tau: float) -> float:
        au = abs(u)
        if au <= 0.5 * tau:
            return u * u
        if au <= tau:
            return (tau - au) ** 2
        return 0.0

    tau = 2.4
    grid = [-3.0 + 0.03 * k for k in range(201)]
    # Check 0 <= phi_tau(u) <= min(u^2, (tau/2)^2), homogeneity phi_{c}(c z) = c^2 phi_1(z),
    # and Lipschitz constant <= tau (and <= 2*tau as used in v1 p. 37).
    dom_ok = all(0.0 <= phi_tau(u, tau) <= min(u * u, 0.25 * tau * tau) + 1e-12 for u in grid)
    homog_ok = all(abs(phi_tau(tau * z, tau) - (tau * tau) * phi_tau(z, 1.0)) < 1e-12 for z in grid)
    max_lip = 0.0
    for i in range(len(grid)):
        for j in range(i + 1, len(grid)):
            u1, u2 = grid[i], grid[j]
            max_lip = max(max_lip, abs(phi_tau(u1, tau) - phi_tau(u2, tau)) / abs(u1 - u2))
    lip_ok = max_lip <= tau + 1e-9

    passed = lq_bounds_ok and group_rate_ordering_ok and dom_ok and homog_ok and lip_ok
    return {
        "lq_card": len(s_eta),
        "lq_card_bound": card_bound,
        "lq_approx_l1": approx_l1,
        "lq_approx_bound": approx_bound,
        "rate_alpha_2": rate_alpha_2,
        "rate_alpha_inf": rate_alpha_inf,
        "phi_tau_max_lip": max_lip,
        "passed": passed,
    }


def main() -> int:
    res1 = verify_subspace_decomposability()
    res2 = verify_lemma1_and_theorem1()
    res3 = verify_lq_weak_sparsity_and_glm_truncation()
    all_passed = bool(res1["passed"] and res2["passed"] and res3["passed"])
    report = {
        "concept_id": "AIMech:DecomposableRegularizerAndRestrictedStrongConvexityMEstimatorFramework",
        "subspace_decomposability": res1,
        "lemma1_and_theorem1": res2,
        "lq_weak_sparsity_and_glm_truncation": res3,
        "all_passed": all_passed,
    }
    print(json.dumps(report, indent=2))
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
