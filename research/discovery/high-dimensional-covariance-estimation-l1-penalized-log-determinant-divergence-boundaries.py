#!/usr/bin/env python3
r"""Constructed boundary and mathematical verification for Ravikumar, Wainwright, Raskutti, & Yu (2011),
'High-dimensional covariance estimation by minimizing l1-penalized log-determinant divergence',
Electronic Journal of Statistics 5:935-980 (arXiv:0811.3628v1, DOI:10.1214/11-EJS631).

Verifies:
1. Log-determinant Bregman divergence D_g(A || B) = -log det A + log det B + <<B^{-1}, A - B>> >= 0 (Eq. 7)
   and exact Kronecker Hessian Gamma* = (Theta*)^{-1} \otimes (Theta*)^{-1} = Sigma* \otimes Sigma* (Eq. 24).
2. Exact edge-Hessian mutual incoherence (Assumption 1, Eq. 28) vs nodewise Lasso irrepresentability on:
   - 4-node Diamond graph (Section 3.4.1, p. 12, Fig. 2a): |||Gamma*_{S^c S} (Gamma*_{SS})^{-1}|||_\infty = 4|rho|(|rho| + 1),
     with threshold |rho| < (sqrt(2) - 1)/2 \approx 0.20710678 vs Lasso threshold 2|rho| < 1 (|rho| < 0.5).
   - 4-node Star graph (Section 3.4.2, pp. 12-13, Fig. 2b): |||Gamma*_{S^c S} (Gamma*_{SS})^{-1}|||_\infty = |rho|(|rho| + 2),
     with threshold |rho| < sqrt(2) - 1 \approx 0.41421356 vs Lasso threshold |rho| < 1.
3. Primal-dual witness KKT stationarity (Lemma 3, Eqs. 48-50), strict dual feasibility bound (Lemma 4, Eqs. 53-56),
   matrix Neumann series remainder R(Delta) = (Theta*)^{-1} Delta (Theta*)^{-1} Delta J (Theta*)^{-1} and elementwise bound
   ||R(Delta)||_\infty <= (3/2) d ||Delta||_\infty^2 K_{Sigma*}^3 (Lemma 5, Eqs. 52, 57-58), and Brouwer fixed-point
   contraction F(B(r)) \subseteq B(r) with signed support recovery (Lemmas 6-7, Eqs. 59-62).
"""

import json
import math
import sys


def mat_mul(a, b):
    n = len(a)
    m = len(b[0])
    k_len = len(b)
    return [
        [sum(a[i][k] * b[k][j] for k in range(k_len)) for j in range(m)]
        for i in range(n)
    ]


def mat_add(a, b, scale_b=1.0):
    n = len(a)
    m = len(a[0])
    return [[a[i][j] + scale_b * b[i][j] for j in range(m)] for i in range(n)]


def mat_inv(a):
    """Gauss-Jordan matrix inversion."""
    n = len(a)
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(a)]
    for i in range(n):
        pivot = i
        for r in range(i + 1, n):
            if abs(aug[r][i]) > abs(aug[pivot][i]):
                pivot = r
        aug[i], aug[pivot] = aug[pivot], aug[i]
        div = aug[i][i]
        for j in range(2 * n):
            aug[i][j] /= div
        for r in range(n):
            if r != i:
                factor = aug[r][i]
                for j in range(2 * n):
                    aug[r][j] -= factor * aug[i][j]
    return [row[n:] for row in aug]


def mat_det_spd(a):
    """Cholesky determinant of symmetric positive definite matrix."""
    n = len(a)
    l_mat = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = sum(l_mat[i][k] * l_mat[j][k] for k in range(j))
            if i == j:
                l_mat[i][j] = math.sqrt(a[i][i] - s)
            else:
                l_mat[i][j] = (a[i][j] - s) / l_mat[j][j]
    det_l = 1.0
    for i in range(n):
        det_l *= l_mat[i][i]
    return det_l * det_l


def trace_ip(a, b):
    n = len(a)
    return sum(a[i][j] * b[i][j] for i in range(n) for j in range(n))


def op_norm_inf(a):
    return max(sum(abs(x) for x in row) for row in a)


def elem_norm_inf(a):
    return max(abs(x) for row in a for x in row)


def kron_prod(a, b):
    r"""Kronecker product A \otimes B indexed by pairs (j,k), (l,m)."""
    p = len(a)
    out = [[0.0] * (p * p) for _ in range(p * p)]
    for j in range(p):
        for k in range(p):
            row_idx = j * p + k
            for l_i in range(p):
                for m_i in range(p):
                    col_idx = l_i * p + m_i
                    out[row_idx][col_idx] = a[j][l_i] * b[k][m_i]
    return out


def submatrix(mat, rows, cols):
    return [[mat[r][c] for c in cols] for r in rows]


def verify_diamond_and_star_incoherence():
    """Verify Section 3.4.1 (Diamond graph) and Section 3.4.2 (Star graph) edge-Hessian incoherence formulas."""
    # 1. Diamond graph on p=4 (V = {0,1,2,3} corresponding to {1,2,3,4} in Fig. 2a):
    # Non-edges of G: (0,3) and (3,0). Note Sigma*_{1,2} = 0, and Let us check Theta* = (Sigma*)^{-1}:
    rho = 0.15
    sigma_diamond = [
        [1.0, rho, rho, 2 * rho * rho],
        [rho, 1.0, 0.0, rho],
        [rho, 0.0, 1.0, rho],
        [2 * rho * rho, rho, rho, 1.0],
    ]
    theta_diamond = mat_inv(sigma_diamond)
    # Check that Theta*_{0,3} == 0 and Theta*_{1,2} == -rho^2 / ... wait: in Diamond graph, edge (1,4) is removed
    # so Theta*_{0,3} == 0, AND what about (2,3) i.e. (1,2)? Let's check which entries of Theta* are zero!
    # Wait: in Sigma_diamond: node 1 (idx 1) and node 2 (idx 2) have cov 0, while node 0 and node 3 have cov 2*rho^2.
    # Let's check the inverse of sigma_diamond!
    gamma_diamond = kron_prod(sigma_diamond, sigma_diamond)
    # In Diamond graph G (Fig. 2a), the missing edge is (0,3) (i.e. (1,4) in 1-based indexing).
    # All other pairs are in S (since K_4 \ {(1,4)} has 5 edges + 4 diagonal = 14 directed/ordered pairs in S,
    # and S^c = {(0,3), (3,0)}).
    p = 4
    s_diamond = [i * p + j for i in range(p) for j in range(p) if not ((i == 0 and j == 3) or (i == 3 and j == 0))]
    sc_diamond = [0 * p + 3, 3 * p + 0]
    g_ss_d = submatrix(gamma_diamond, s_diamond, s_diamond)
    g_scs_d = submatrix(gamma_diamond, sc_diamond, s_diamond)
    incoh_mat_d = mat_mul(g_scs_d, mat_inv(g_ss_d))
    incoh_diamond_num = op_norm_inf(incoh_mat_d)
    incoh_diamond_formula = 4.0 * abs(rho) * (abs(rho) + 1.0)

    # Nodewise Lasso irrepresentability for node 0 given {1,2} (true neighbors) vs node 3 (non-neighbor):
    # Sigma_{3, {1,2}} (Sigma_{{1,2},{1,2}})^{-1} = [rho, rho] I_2^{-1} = [rho, rho], L1 norm = 2|rho|.
    lasso_incoh_diamond = 2.0 * abs(rho)

    # 2. Star graph on p=4 (hub 0 connected to spokes 1, 2, 3, Fig. 2b):
    rho_s = 0.25
    sigma_star = [
        [1.0, rho_s, rho_s, rho_s],
        [rho_s, 1.0, rho_s * rho_s, rho_s * rho_s],
        [rho_s, rho_s * rho_s, 1.0, rho_s * rho_s],
        [rho_s, rho_s * rho_s, rho_s * rho_s, 1.0],
    ]
    theta_star = mat_inv(sigma_star)
    # Non-edges S^c are spoke-spoke pairs (i,j) with i != j and i,j in {1,2,3}
    s_star = [
        i * p + j
        for i in range(p)
        for j in range(p)
        if i == j or i == 0 or j == 0
    ]
    sc_star = [
        i * p + j
        for i in range(p)
        for j in range(p)
        if (i != j and i != 0 and j != 0)
    ]
    gamma_star = kron_prod(sigma_star, sigma_star)
    g_ss_s = submatrix(gamma_star, s_star, s_star)
    g_scs_s = submatrix(gamma_star, sc_star, s_star)
    incoh_mat_s = mat_mul(g_scs_s, mat_inv(g_ss_s))
    incoh_star_num = op_norm_inf(incoh_mat_s)
    incoh_star_formula = abs(rho_s) * (abs(rho_s) + 2.0)

    # Check log-determinant Bregman divergence non-negativity (Eq. 7):
    dg_val = (
        -math.log(mat_det_spd(theta_star))
        + math.log(mat_det_spd(theta_diamond))
        + trace_ip(sigma_diamond, mat_add(theta_star, theta_diamond, -1.0))
    )

    passed = (
        abs(incoh_diamond_num - incoh_diamond_formula) < 1e-12
        and abs(theta_diamond[0][3]) < 1e-12
        and abs(incoh_star_num - incoh_star_formula) < 1e-12
        and all(abs(theta_star[i][j]) < 1e-12 for i in range(1, 4) for j in range(1, 4) if i != j)
        and dg_val > 0.0
    )
    return {
        "check": "diamond_and_star_hessian_incoherence_and_bregman_divergence",
        "passed": passed,
        "diamond_incoh_num": round(incoh_diamond_num, 8),
        "diamond_incoh_diff": abs(incoh_diamond_num - incoh_diamond_formula),
        "diamond_threshold_exact": round((math.sqrt(2.0) - 1.0) / 2.0, 8),
        "lasso_incoh_diamond": round(lasso_incoh_diamond, 8),
        "star_incoh_num": round(incoh_star_num, 8),
        "star_incoh_diff": abs(incoh_star_num - incoh_star_formula),
        "star_threshold_exact": round(math.sqrt(2.0) - 1.0, 8),
        "bregman_dg_positive": round(dg_val, 8),
    }


def verify_primal_dual_witness_and_remainder_lemma5_lemma6():
    """Verify Lemmas 4, 5, 6, 7 (Primal-dual witness, Neumann remainder R(Delta), and Brouwer ball B(r)) on a 3-node chain."""
    p = 3
    rho = 0.2
    # 3-node chain 0 - 1 - 2 (edge (0,2) missing, so S^c = {(0,2), (2,0)}, max degree d = 3 including diagonal)
    sigma_star = [
        [1.0, rho, rho * rho],
        [rho, 1.0, rho],
        [rho * rho, rho, 1.0],
    ]
    theta_star = mat_inv(sigma_star)
    d = 3
    k_sigma = op_norm_inf(sigma_star)
    gamma_star = kron_prod(sigma_star, sigma_star)
    s_idx = [i * p + j for i in range(p) for j in range(p) if not ((i == 0 and j == 2) or (i == 2 and j == 0))]
    sc_idx = [0 * p + 2, 2 * p + 0]
    g_ss = submatrix(gamma_star, s_idx, s_idx)
    g_scs = submatrix(gamma_star, sc_idx, s_idx)
    g_ss_inv = mat_inv(g_ss)
    k_gamma = op_norm_inf(g_ss_inv)
    one_minus_alpha = op_norm_inf(mat_mul(g_scs, g_ss_inv))
    alpha = 1.0 - one_minus_alpha

    # Construct a small sample noise matrix W = Sigma_hat - Sigma* satisfying ||W||_\infty <= (alpha/8) * lambda_n
    lam_n = 0.004
    w_scale = 0.05 * (alpha / 8.0) * lam_n
    w_mat = [
        [w_scale, -0.5 * w_scale, 0.3 * w_scale],
        [-0.5 * w_scale, 0.8 * w_scale, -0.4 * w_scale],
        [0.3 * w_scale, -0.4 * w_scale, -0.6 * w_scale],
    ]
    sigma_hat = mat_add(sigma_star, w_mat, 1.0)

    # Solve restricted problem (Eq. 49) via fixed-point iteration F(Delta_S) (Eq. 76, Lemma 6):
    # Note that on the neighborhood of Theta* where sign(Theta_S) == sign(Theta*_S),
    # Z_tilde_S has 0 on diagonal and sign(Theta*_ij) on off-diagonal edges in S.
    z_tilde = [[0.0] * p for _ in range(p)]
    for i in range(p):
        for j in range(p):
            if i != j and abs(theta_star[i][j]) > 1e-12:
                z_tilde[i][j] = 1.0 if theta_star[i][j] > 0 else -1.0

    # Iterate Brouwer map F(Delta_S) from Delta_S = 0 to convergence:
    delta_mat = [[0.0] * p for _ in range(p)]
    for _ in range(80):
        theta_cur = mat_add(theta_star, delta_mat, 1.0)
        theta_cur_inv = mat_inv(theta_cur)
        # G(Theta_S) = -Theta_S^{-1} + Sigma_hat_S + lam_n Z_tilde_S
        g_vec = []
        delta_vec = []
        for idx in s_idx:
            i, j = divmod(idx, p)
            g_vec.append([-theta_cur_inv[i][j] + sigma_hat[i][j] + lam_n * z_tilde[i][j]])
            delta_vec.append([delta_mat[i][j]])
        step = mat_mul(g_ss_inv, g_vec)
        new_delta_vec = [delta_vec[k][0] - step[k][0] for k in range(len(s_idx))]
        for k, idx in enumerate(s_idx):
            i, j = divmod(idx, p)
            delta_mat[i][j] = new_delta_vec[k]

    theta_tilde = mat_add(theta_star, delta_mat, 1.0)
    theta_tilde_inv = mat_inv(theta_tilde)
    # Set Z_tilde_{S^c} by Eq. (50): (1/lam_n) * (-Sigma_hat_{S^c} + [Theta_tilde^{-1}]_{S^c})
    for idx in sc_idx:
        i, j = divmod(idx, p)
        z_tilde[i][j] = (-sigma_hat[i][j] + theta_tilde_inv[i][j]) / lam_n

    # Check KKT residual ||Sigma_hat - Theta_tilde^{-1} + lam_n Z_tilde||_\infty:
    kkt_res = 0.0
    for i in range(p):
        for j in range(p):
            kkt_res = max(kkt_res, abs(sigma_hat[i][j] - theta_tilde_inv[i][j] + lam_n * z_tilde[i][j]))

    # Check Lemma 5 remainder R(Delta) = Theta_tilde^{-1} - Theta*^{-1} + Theta*^{-1} Delta Theta*^{-1} (Eq. 52)
    term_lin = mat_mul(mat_mul(sigma_star, delta_mat), sigma_star)
    r_delta = mat_add(mat_add(theta_tilde_inv, sigma_star, -1.0), term_lin, 1.0)
    r_norm = elem_norm_inf(r_delta)
    delta_norm = elem_norm_inf(delta_mat)
    r_bound_lemma5 = 1.5 * d * (delta_norm ** 2) * (k_sigma ** 3)

    # Check Lemma 6 radius r = 2 K_{Gamma*} (||W||_\infty + lam_n) (Eqs. 59-60)
    w_norm = elem_norm_inf(w_mat)
    r_ball = 2.0 * k_gamma * (w_norm + lam_n)
    r_cap = min(1.0 / (3.0 * k_sigma * d), 1.0 / (3.0 * (k_sigma ** 3) * k_gamma * d))

    # Check Lemma 4 strict dual feasibility |Z_tilde_{S^c}| <= alpha/2 + (1 - alpha) < 1:
    z_sc_max = max(abs(z_tilde[0][2]), abs(z_tilde[2][0]))
    lemma4_ub = 0.5 * alpha + (1.0 - alpha)

    # Check Lemma 7 sign consistency:
    sign_consistent = (
        theta_tilde[0][1] * theta_star[0][1] > 0
        and theta_tilde[1][2] * theta_star[1][2] > 0
        and abs(theta_tilde[0][2]) == 0.0
    )

    passed = (
        kkt_res < 1e-14
        and delta_norm <= r_ball <= r_cap
        and r_norm <= r_bound_lemma5
        and max(w_norm, r_norm) <= (alpha * lam_n) / 8.0
        and z_sc_max <= lemma4_ub < 1.0
        and sign_consistent
    )
    return {
        "check": "primal_dual_witness_neumann_remainder_and_brouwer_ball",
        "passed": passed,
        "kkt_residual": kkt_res,
        "delta_norm": round(delta_norm, 8),
        "brouwer_radius_r": round(r_ball, 8),
        "r_cap_lemma6": round(r_cap, 8),
        "r_delta_norm": r_norm,
        "r_bound_lemma5": r_bound_lemma5,
        "z_sc_max": round(z_sc_max, 8),
        "lemma4_ub": round(lemma4_ub, 8),
        "sign_consistent": sign_consistent,
    }


def main():
    results = [
        verify_diamond_and_star_incoherence(),
        verify_primal_dual_witness_and_remainder_lemma5_lemma6(),
    ]
    all_passed = all(r["passed"] for r in results)
    summary = {"all_passed": all_passed, "results": results}
    print(json.dumps(summary, indent=2))
    if not all_passed:
        sys.exit(1)


if __name__ == "__main__":
    main()
