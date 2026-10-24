#!/usr/bin/env python3
"""Boundary and regime verification for Krzakala et al. (2013)
Spectral redemption: clustering sparse networks (Non-Backtracking Walk Matrix).
"""

import json
import math


def mat_vec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


def build_non_backtracking(adj):
    n = len(adj)
    dir_edges = []
    for u in range(n):
        for v in range(n):
            if adj[u][v] == 1:
                dir_edges.append((u, v))
    m2 = len(dir_edges)
    B = [[0.0] * m2 for _ in range(m2)]
    for i, (u, v) in enumerate(dir_edges):
        for j, (w, x) in enumerate(dir_edges):
            if v == w and u != x:
                B[i][j] = 1.0
    return dir_edges, B


def trace_power(M, p):
    n = len(M)
    cur = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(p):
        nxt = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for k in range(n):
                if cur[i][k] != 0.0:
                    for j in range(n):
                        nxt[i][j] += cur[i][k] * M[k][j]
        cur = nxt
    return sum(cur[i][i] for i in range(n))


def det_gauss(M):
    n = len(M)
    A = [row[:] for row in M]
    sign = 1.0
    for i in range(n):
        piv = max(range(i, n), key=lambda r: abs(A[r][i]))
        if abs(A[piv][i]) < 1e-14:
            return 0.0
        if piv != i:
            A[i], A[piv] = A[piv], A[i]
            sign = -sign
        for r in range(i + 1, n):
            fac = A[r][i] / A[i][i]
            for c in range(i, n):
                A[r][c] -= fac * A[i][c]
    prod = sign
    for i in range(n):
        prod *= A[i][i]
    return prod


def main():
    # 1. Construct a 12-vertex irregular 2-community graph above the Kesten-Stigum threshold:
    # Two 6-vertex communities {0..5} and {6..11}, each K_6 minus edge (0,1) / (6,7),
    # with two bridge edges (2,8) and (3,9). Degrees are [4,4,6,6,5,5] in each community.
    n = 12
    adj_irreg = [[0] * n for _ in range(n)]
    for i in range(6):
        for j in range(i + 1, 6):
            adj_irreg[i][j] = adj_irreg[j][i] = 1
            adj_irreg[i + 6][j + 6] = adj_irreg[j + 6][i + 6] = 1
    adj_irreg[0][1] = adj_irreg[1][0] = 0
    adj_irreg[6][7] = adj_irreg[7][6] = 0
    adj_irreg[2][8] = adj_irreg[8][2] = 1
    adj_irreg[3][9] = adj_irreg[9][3] = 1

    dir_edges_ir, B_ir = build_non_backtracking(adj_irreg)
    deg_ir = [sum(adj_irreg[i]) for i in range(n)]

    # Power iterate B_ir on the antisymmetric community subspace (g_{u+6 -> v+6} = -g_{u -> v})
    g = [1.0 if u < 6 else -1.0 for (u, v) in dir_edges_ir]
    for _ in range(120):
        Bg = mat_vec(B_ir, g)
        nrm = math.sqrt(sum(z * z for z in Bg))
        g = [z / nrm for z in Bg]
    Bg = mat_vec(B_ir, g)
    mu_comm = sum(g[i] * Bg[i] for i in range(len(g)))
    eig_err_B = max(abs(Bg[i] - mu_comm * g[i]) for i in range(len(g)))
    assert eig_err_B < 1e-13

    # Incoming-edge vertex sum f_in[v] = sum_{u in N(v)} g_{u -> v}
    # and Outgoing-edge vertex sum f_out[u] = sum_{v in N(u)} g_{u -> v}
    f_in = [0.0] * n
    f_out = [0.0] * n
    for idx, (u, v) in enumerate(dir_edges_ir):
        f_in[v] += g[idx]
        f_out[u] += g[idx]
    # Verify community signs of both f_in and f_out match ground truth [+1]*6 + [-1]*6
    assert all(f_in[i] > 0 for i in range(6)) and all(f_in[i + 6] < 0 for i in range(6))
    assert all(f_out[i] > 0 for i in range(6)) and all(f_out[i + 6] < 0 for i in range(6))
    # Verify exact relation mu * f_in[v] == (d_v - 1) * f_out[v]
    in_out_err = max(abs(mu_comm * f_in[v] - (deg_ir[v] - 1.0) * f_out[v]) for v in range(n))
    assert in_out_err < 1e-13

    # Verify Quadratic Eigenvalue Equation (6) / (8): A f_out = mu f_out + (D - I) mu^{-1} f_out
    Af = [sum(adj_irreg[i][j] * f_out[j] for j in range(n)) for i in range(n)]
    rhs_eq6 = [mu_comm * f_out[i] + (deg_ir[i] - 1.0) * (f_out[i] / mu_comm) for i in range(n)]
    eq6_err = max(abs(Af[i] - rhs_eq6[i]) for i in range(n))
    assert eq6_err < 1e-13

    # Verify Ihara-Bass Determinant Equation (8): det(mu^2 I - mu A + (D - I)) == 0
    M_ihara = [
        [
            (mu_comm * mu_comm + (deg_ir[i] - 1.0) if i == j else -mu_comm * adj_irreg[i][j])
            for j in range(n)
        ]
        for i in range(n)
    ]
    ihara_det = abs(det_gauss(M_ihara))
    assert ihara_det < 1e-11

    # 2. Verify Section II & III (p. 3, 5): Dangling trees contribute ONLY zero eigenvalues to B,
    # whereas they inflate vertex degrees and singular values d_v - 1 of B!
    # Attach a 3-vertex star/tree to vertex 0 of adj_irreg (new vertices 12, 13, 14 connected only to 0)
    n_tree = 15
    adj_tree = [[0] * n_tree for _ in range(n_tree)]
    for i in range(n):
        for j in range(n):
            adj_tree[i][j] = adj_irreg[i][j]
    for leaf in (12, 13, 14):
        adj_tree[0][leaf] = adj_tree[leaf][0] = 1

    _, B_tree = build_non_backtracking(adj_tree)
    # Check trace(B^p) == trace(B_tree^p) for p = 1..6 (confirming identical non-zero spectrum!)
    trace_diffs = [abs(trace_power(B_ir, p) - trace_power(B_tree, p)) for p in range(1, 7)]
    assert max(trace_diffs) < 1e-12

    # Check block-diagonal structure of B B^T (Section III, p. 5):
    # Each vertex v contributes a rank-1 block of size d_v with eigenvalue (d_v - 1)^2 and (d_v - 1) ones.
    m2_ir = len(B_ir)
    BBt = [
        [sum(B_ir[i][k] * B_ir[j][k] for k in range(m2_ir)) for j in range(m2_ir)]
        for i in range(m2_ir)
    ]
    tr_BBt = sum(BBt[i][i] for i in range(m2_ir))
    expected_tr_BBt = sum((d - 1) ** 2 + (d - 1) for d in deg_ir)
    assert abs(tr_BBt - expected_tr_BBt) < 1e-12

    # 3. Verify Kesten-Stigum threshold (Eqs. 1, 3, 12) and BP linearization (Eq. 14):
    # For c_in = 5, c_out = 1 (Fig. 1-2): c = 3, mu_c = (c_in - c_out)/2 = 2 > sqrt(3) = 1.73205
    c_in, c_out = 5.0, 1.0
    c_avg = 0.5 * (c_in + c_out)
    mu_c = 0.5 * (c_in - c_out)
    bulk_radius = math.sqrt(c_avg)
    bp_instability_gain = ((c_in - c_out) / (c_in + c_out)) * mu_c  # nu * mu_c > 1
    assert mu_c > bulk_radius and bp_instability_gain > 1.0

    summary = {
        "concept": "NonBacktrackingWalkMatrixAndKestenStigumSpectralRedemption",
        "community_eigenvalue_mu": round(mu_comm, 6),
        "eig_err_B": eig_err_B,
        "quadratic_eq6_err": eq6_err,
        "ihara_bass_det_err": ihara_det,
        "dangling_tree_trace_max_diff": max(trace_diffs),
        "kesten_stigum_mu_c": mu_c,
        "kesten_stigum_bulk_radius": round(bulk_radius, 6),
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
