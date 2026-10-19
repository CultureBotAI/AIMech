#!/usr/bin/env python3
"""Boundary and regime verification for Cuturi (2013)
Sinkhorn Distances: Lightspeed Computation of Optimal Transportation Distances.
"""

import json
import math


def entropy_vec(p):
    return -sum(x * math.log(x) for x in p if x > 0.0)


def entropy_mat(P):
    return -sum(x * math.log(x) for row in P for x in row if x > 0.0)


def kl_div_mat(P, Q):
    s = 0.0
    for i in range(len(P)):
        for j in range(len(P[0])):
            if P[i][j] > 0.0:
                s += P[i][j] * math.log(P[i][j] / Q[i][j])
    return s


def sinkhorn_knopp(M, lam, r, c, max_iter=300, tol=1e-13):
    """Algorithm 1: Sinkhorn-Knopp fixed-point matrix scaling for P^lambda = diag(u) e^{-lam M} diag(v)."""
    d = len(r)
    K = [[math.exp(-lam * M[i][j]) for j in range(d)] for i in range(d)]
    u = [1.0 / d] * d
    v = [1.0 / d] * d
    for _ in range(max_iter):
        Kv = [sum(K[i][j] * v[j] for j in range(d)) for i in range(d)]
        u_new = [r[i] / Kv[i] for i in range(d)]
        Ktu = [sum(K[i][j] * u_new[i] for i in range(d)) for j in range(d)]
        v_new = [c[j] / Ktu[j] for j in range(d)]
        diff = max(abs(u_new[i] - u[i]) for i in range(d)) + max(abs(v_new[j] - v[j]) for j in range(d))
        u, v = u_new, v_new
        if diff < tol:
            break
    P = [[u[i] * K[i][j] * v[j] for j in range(d)] for i in range(d)]
    cost = sum(P[i][j] * M[i][j] for i in range(d) for j in range(d))
    return P, u, v, cost


def main():
    d = 3
    # Metric ground cost matrix M on {0, 1, 2}
    M = [
        [0.0, 1.0, 2.0],
        [1.0, 0.0, 1.0],
        [2.0, 1.0, 0.0],
    ]
    x = [0.5, 0.3, 0.2]
    y = [0.2, 0.5, 0.3]
    z = [0.1, 0.3, 0.6]

    # 1. Verify Algorithm 1 (Sinkhorn-Knopp Scaling) & Section 4.1 Equation (3):
    P_xy, u_xy, v_xy, d_xy = sinkhorn_knopp(M, 3.0, x, y)
    row_err = max(abs(sum(P_xy[i]) - x[i]) for i in range(d))
    col_err = max(abs(sum(P_xy[i][j] for i in range(d)) - y[j]) for j in range(d))
    assert row_err < 1e-12 and col_err < 1e-12

    # 2. Verify Section 3.1 Equation (1): h(P) <= h(r) + h(c) and KL(P || r c^T) = h(r) + h(c) - h(P) >= 0
    indep_xy = [[x[i] * y[j] for j in range(d)] for i in range(d)]
    kl_xy = kl_div_mat(P_xy, indep_xy)
    mi_xy = entropy_vec(x) + entropy_vec(y) - entropy_mat(P_xy)
    assert abs(kl_xy - mi_xy) < 1e-13 and kl_xy >= 0.0

    # 3. Verify Lemma 1 (Gluing Lemma with Entropic Constraint) & Theorem 1 (Triangle Inequality):
    P_yz, _, _, d_yz = sinkhorn_knopp(M, 3.0, y, z)
    indep_yz = [[y[j] * z[k] for k in range(d)] for j in range(d)]
    kl_yz = kl_div_mat(P_yz, indep_yz)
    alpha = max(kl_xy, kl_yz)

    # Glued coupling S_{ik} = sum_j P_{ij} Q_{jk} / y_j
    S = [[sum(P_xy[i][j] * P_yz[j][k] / y[j] for j in range(d)) for k in range(d)] for i in range(d)]
    s_row_err = max(abs(sum(S[i]) - x[i]) for i in range(d))
    s_col_err = max(abs(sum(S[i][k] for i in range(d)) - z[k]) for k in range(d))
    assert s_row_err < 1e-12 and s_col_err < 1e-12

    indep_xz = [[x[i] * z[k] for k in range(d)] for i in range(d)]
    kl_xz_glued = kl_div_mat(S, indep_xz)
    # By Data Processing Inequality on X -> Y -> Z, I(X; Z) <= min(I(X; Y), I(Y; Z)) <= alpha
    assert kl_xz_glued <= min(kl_xy, kl_yz) + 1e-12
    glued_cost = sum(S[i][k] * M[i][k] for i in range(d) for k in range(d))
    assert abs(glued_cost - (d_xy + d_yz)) < 1e-12 or glued_cost <= d_xy + d_yz + 1e-12

    # 4. Verify Section 4.2 Monotonicity of Entropy h(P^lambda) and Cost d_M^lambda as lambda increases:
    entropies = []
    costs = []
    for lam in (0.5, 2.0, 5.0, 12.0):
        P_lam, _, _, c_lam = sinkhorn_knopp(M, lam, x, z)
        entropies.append(entropy_mat(P_lam))
        costs.append(c_lam)
    assert all(entropies[i] > entropies[i + 1] for i in range(len(entropies) - 1))
    assert all(costs[i] > costs[i + 1] for i in range(len(costs) - 1))

    # 5. Verify Section 3.2 Failure of Coincidence Axiom without 1_{r != c} factor:
    # For r = c = x (with h(x) > 0) and finite lambda, d_M^lambda(x, x) > 0!
    _, _, _, self_dist = sinkhorn_knopp(M, 2.0, x, x)
    assert self_dist > 0.05

    summary = {
        "concept": "SinkhornDistancesAndEntropicRegularizedOptimalTransport",
        "marginal_feasibility_err": max(row_err, col_err),
        "kl_mutual_info_xy": round(kl_xy, 6),
        "kl_glued_xz": round(kl_xz_glued, 6),
        "entropy_trajectory_vs_lambda": [round(e, 6) for e in entropies],
        "cost_trajectory_vs_lambda": [round(c, 6) for c in costs],
        "non_coincidence_self_distance": round(self_dist, 6),
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
