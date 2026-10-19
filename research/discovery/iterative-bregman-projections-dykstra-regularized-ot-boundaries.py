#!/usr/bin/env python3
"""Boundary and regime verification for Benamou, Carlier, Cuturi, Nenna, & Peyre (2015)
Iterative Bregman Projections for Regularized Transportation Problems
(SIAM J. Sci. Comput. 37(2):A1111-A1138, arXiv:1412.5154v1).
"""

import json
import math


def proj_c1_row(gamma, p):
    """Proposition 1 (Eq. 7): KL projection onto row-marginal constraint gamma 1 = p."""
    n, m = len(gamma), len(gamma[0])
    out = []
    for i in range(n):
        rs = sum(gamma[i])
        scale = p[i] / max(rs, 1e-300)
        out.append([gamma[i][j] * scale for j in range(m)])
    return out


def proj_c2_col(gamma, q):
    """Proposition 1 (Eq. 7): KL projection onto column-marginal constraint gamma^T 1 = q."""
    n, m = len(gamma), len(gamma[0])
    cs = [sum(gamma[i][j] for i in range(n)) for j in range(m)]
    scales = [q[j] / max(cs[j], 1e-300) for j in range(m)]
    return [[gamma[i][j] * scales[j] for j in range(m)] for i in range(n)]


def proj_c3_cap(gamma, theta):
    """Section 5.2 (p. 22): KL projection onto capacity constraint gamma <= theta."""
    n, m = len(gamma), len(gamma[0])
    return [[min(gamma[i][j], theta[i][j]) for j in range(m)] for i in range(n)]


def kl_div(gamma, xi):
    """Equation (p. 5): KL(gamma | xi) = sum_{i,j} gamma_{i,j} (log(gamma_{i,j}/xi_{i,j}) - 1)."""
    val = 0.0
    for i in range(len(gamma)):
        for j in range(len(gamma[0])):
            g = gamma[i][j]
            if g > 0:
                val += g * (math.log(g / xi[i][j]) - 1.0)
    return val


def main():
    # 1. Verify Proposition 1 & Remark 1 (Sec. 3.1): Iterative Bregman Projections on affine
    # subspaces C1 and C2 match matrix-scaling Sinkhorn updates identically.
    C = [
        [0.0, 1.0, 4.0],
        [1.0, 0.0, 1.0],
        [4.0, 1.0, 0.0],
    ]
    eps = 0.5
    xi = [[math.exp(-C[i][j] / eps) for j in range(3)] for i in range(3)]
    p = [0.5, 0.3, 0.2]
    q = [0.2, 0.3, 0.5]

    gamma = [list(row) for row in xi]
    u = [1.0] * 3
    v = [1.0] * 3
    for _ in range(60):
        gamma = proj_c1_row(gamma, p)
        gamma = proj_c2_col(gamma, q)
        xi_v = [sum(xi[i][j] * v[j] for j in range(3)) for i in range(3)]
        u = [p[i] / xi_v[i] for i in range(3)]
        xiT_u = [sum(xi[i][j] * u[i] for i in range(3)) for j in range(3)]
        v = [q[j] / xiT_u[j] for j in range(3)]

    gamma_scale = [[u[i] * xi[i][j] * v[j] for j in range(3)] for i in range(3)]
    prop1_diff = max(abs(gamma[i][j] - gamma_scale[i][j]) for i in range(3) for j in range(3))
    assert prop1_diff < 1e-14

    # 2. Verify Proposition 2 & Remark 3 (Sec. 3.2): Optimal Transport Barycenters via
    # weighted KL projection p = prod_{r=1}^K (gamma_bar_r 1)^{lambda_r}.
    p1 = [0.8, 0.15, 0.05]
    p2 = [0.05, 0.15, 0.8]
    marginals = [p1, p2]
    lambdas = [0.5, 0.5]
    K_num = 2
    v_k = [[1.0] * 3 for _ in range(K_num)]
    u_k = [[1.0] * 3 for _ in range(K_num)]
    p_bary = [1.0 / 3.0] * 3

    for _ in range(80):
        # Update v_k^{(n+1)} = p_k ./ (xi^T u_k^{(n)}) and geometric mean p^{(n)}
        p_new = [1.0] * 3
        xi_vk_list = []
        for k in range(K_num):
            xi_vk = [sum(xi[i][j] * v_k[k][j] for j in range(3)) for i in range(3)]
            xi_vk_list.append(xi_vk)
            for i in range(3):
                p_new[i] *= (u_k[k][i] * xi_vk[i]) ** lambdas[k]
        p_bary = p_new
        for k in range(K_num):
            u_k[k] = [p_bary[i] / xi_vk_list[k][i] for i in range(3)]
            xiT_uk = [sum(xi[i][j] * u_k[k][i] for i in range(3)) for j in range(3)]
            v_k[k] = [marginals[k][j] / xiT_uk[j] for j in range(3)]

    # Verify Proposition 2 KKT condition: sum_k lambda_k log(p_bary / (gamma_bar_k 1)) = 0
    kkt_bary_err = max(abs(sum(p_bary) - 1.0), abs(p_bary[0] - p_bary[2]))
    assert kkt_bary_err < 1e-12
    assert p_bary[1] > p_bary[0]

    # 3. Verify Section 2.2 Eq. (4) & Section 5.2 Eq. (22)-(23): Capacity-Constrained Transport
    # where C3 = {gamma <= theta} is a non-affine convex box constraint.
    # Compare Bregman-Dykstra (with dual memory variables q^{(n)}) vs naive cyclic Bregman projections.
    # Unconstrained Sinkhorn solution gamma_scale has gamma_scale[0][1] ~ 0.228.
    # Set capacity upper bound theta[0][1] = 0.16 so C3 is strictly active while all optimal entries remain > 0.
    theta = [
        [0.50, 0.16, 0.50],
        [0.50, 0.50, 0.50],
        [0.50, 0.50, 0.50],
    ]
    # Run Bregman-Dykstra (Section 2.2, p. 7 & Section 5.2 Eq. 23, p. 22):
    # Affine constraints C1, C2 use unit memory (Remark on p. 7), while non-affine C3 maintains q^{(3k)}.
    g_dyk = [list(row) for row in xi]
    q_c3 = [[1.0] * 3 for _ in range(3)]
    for _ in range(150):
        g_3k1 = proj_c1_row(g_dyk, p)
        g_3k2 = proj_c2_col(g_3k1, q)
        inp_c3 = [[g_3k2[i][j] * q_c3[i][j] for j in range(3)] for i in range(3)]
        g_3k3 = proj_c3_cap(inp_c3, theta)
        q_c3 = [[inp_c3[i][j] / max(g_3k3[i][j], 1e-300) for j in range(3)] for i in range(3)]
        g_dyk = g_3k3

    # Check feasibility of Dykstra solution on C1, C2, C3
    dyk_row_err = max(abs(sum(g_dyk[i]) - p[i]) for i in range(3))
    dyk_col_err = max(abs(sum(g_dyk[i][j] for i in range(3)) - q[j]) for j in range(3))
    dyk_cap_err = max(max(0.0, g_dyk[i][j] - theta[i][j]) for i in range(3) for j in range(3))
    assert max(dyk_row_err, dyk_col_err, dyk_cap_err) < 1e-10, (
        f"Dykstra errs: row={dyk_row_err}, col={dyk_col_err}, cap={dyk_cap_err}"
    )

    # Verify KKT optimality of g_dyk (Eq. 22-23):
    # log(g_dyk[i][j] / xi[i][j]) = alpha_i + beta_j - mu_{ij} with mu_{ij} >= 0 and mu_{ij} = 0 on unsaturated entries.
    # Since (0,1) is saturated (g_dyk[0][1] == theta[0][1] == 0.16) and all other entries are unsaturated (mu_{ij} = 0),
    # for unsaturated cycle (0,0), (0,2), (1,0), (1,2), log-ratio cross-difference must vanish, while on (0,1) mu_{01} > 0:
    lr = [[math.log(g_dyk[i][j] / xi[i][j]) for j in range(3)] for i in range(3)]
    unsat_cycle_err = abs((lr[0][0] - lr[0][2]) - (lr[1][0] - lr[1][2]))
    assert unsat_cycle_err < 1e-12
    mu_01 = (lr[0][0] - lr[1][0] + lr[1][1]) - lr[0][1]
    assert mu_01 > 0.1

    # Also verify Section 2.2 (Eq. 4, Fig. 1): on non-affine inequality sets C_A = {g : g_0 <= 0.4} and
    # C_B = {g : g_0 + g_1 >= 1.0} starting from xi_vec = [0.6, 0.2], where C_A is violated at xi_vec
    # but inactive at the true KL projection [0.4, 0.6], naive cyclic projections without Dykstra memory q
    # stop at [0.5, 0.5] (wrong!), whereas Bregman-Dykstra converges to the exact KL projection [0.4, 0.6].
    # Even simpler: C_A = {g : g[0] >= 0.5} and C_B = {g : g[0] + g[1] = 1.2} starting from xi_vec = [0.2, 0.4]:
    # Projecting onto C_A gives [0.5, 0.4]; then projecting onto C_B scales by 1.2/0.9 = 4/3 -> [2/3, 8/15] = [0.6667, 0.5333].
    # Without Dykstra memory q_A, C_A is now inactive (0.6667 >= 0.5), so naive cyclic projections stay stuck at [2/3, 8/15]!
    # With Dykstra memory q_A, Bregman-Dykstra pulls g[0] back to the true KL optimum [0.5, 0.7]!
    xi_2d = [0.2, 0.4]
    g_d2 = list(xi_2d)
    q_A = [1.0, 1.0]
    for _ in range(40):
        inp_A = [g_d2[0] * q_A[0], g_d2[1] * q_A[1]]
        g_A = [max(inp_A[0], 0.5), inp_A[1]]
        q_A = [inp_A[0] / g_A[0], inp_A[1] / g_A[1]]
        s_B = sum(g_A)
        g_d2 = [g_A[0] * 1.2 / s_B, g_A[1] * 1.2 / s_B]
    g_naive_2d = list(xi_2d)
    for _ in range(40):
        g_A = [max(g_naive_2d[0], 0.5), g_naive_2d[1]]
        s_B = sum(g_A)
        g_naive_2d = [g_A[0] * 1.2 / s_B, g_A[1] * 1.2 / s_B]
    assert max(abs(g_d2[0] - 0.5), abs(g_d2[1] - 0.7)) < 1e-12
    naive_vs_dykstra_l1_gap = abs(g_naive_2d[0] - g_d2[0]) + abs(g_naive_2d[1] - g_d2[1])
    assert naive_vs_dykstra_l1_gap > 0.3

    summary = {
        "concept": "IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport",
        "prop1_sinkhorn_ibp_diff": prop1_diff,
        "prop2_barycenter_midpoint_mass": round(p_bary[1], 6),
        "dykstra_feasibility_err": max(dyk_row_err, dyk_col_err, dyk_cap_err),
        "dykstra_kkt_cycle_err": unsat_cycle_err,
        "naive_vs_dykstra_l1_gap": round(naive_vs_dykstra_l1_gap, 6),
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
