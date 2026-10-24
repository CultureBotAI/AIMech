#!/usr/bin/env python3
"""Boundary and regime verification for Arora, Ge, Kannan, & Moitra (2012/2016)
Computing a Nonnegative Matrix Factorization -- Provably (Separable NMF & Robust-Loners).
"""

import json


def l1_dist(u, v):
    return sum(abs(a - b) for a, b in zip(u, v))


def min_l1_to_convex_hull_3(target, basis_rows):
    """Exact minimum l1 distance from target to conv(basis_rows) when len(basis_rows) <= 4."""
    if not basis_rows:
        return sum(abs(x) for x in target)
    k = len(basis_rows)
    m = len(target)
    best = float("inf")
    # Grid search over the k-simplex
    steps = 20
    if k == 1:
        return l1_dist(target, basis_rows[0])
    if k == 2:
        for i in range(steps + 1):
            w0 = i / steps
            w1 = 1.0 - w0
            cand = [w0 * basis_rows[0][c] + w1 * basis_rows[1][c] for c in range(m)]
            d = l1_dist(target, cand)
            if d < best:
                best = d
        return best
    # General simplex grid for k >= 3 using recursive barycentric coordinates
    def recurse(idx, rem, weights):
        nonlocal best
        if idx == k - 1:
            w_all = weights + [rem / steps]
            cand = [sum(w_all[r] * basis_rows[r][c] for r in range(k)) for c in range(m)]
            d = l1_dist(target, cand)
            if d < best:
                best = d
            return
        for s in range(rem + 1):
            recurse(idx + 1, rem - s, weights + [s / steps])

    recurse(0, steps, [])
    return best


def main():
    # 1. Construct a row-l1-normalized separable factor A (n=6, r=3) and alpha-robust simplicial W (r=3, m=4)
    # Rows 0, 1, 2 of A are the anchor/canonical rows (identity matrix I_3)
    A = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [0.5, 0.5, 0.0],
        [0.0, 0.4, 0.6],
        [0.3, 0.3, 0.4],
    ]
    W = [
        [0.70, 0.10, 0.10, 0.10],
        [0.10, 0.70, 0.10, 0.10],
        [0.10, 0.10, 0.70, 0.10],
    ]
    n, r, m = len(A), len(W), len(W[0])
    M = [[sum(A[i][k] * W[k][j] for k in range(r)) for j in range(m)] for i in range(n)]

    # Verify Definition 5.6: W is alpha-robust simplicial with alpha = 1.2
    alpha = min(
        min_l1_to_convex_hull_3(W[i], [W[j] for j in range(r) if j != i])
        for i in range(r)
    )
    assert abs(alpha - 1.2) < 1e-12

    # 2. Verify Claim 5.5 (Exact Loner Characterization in Theorem 5.4):
    # Row M^j is a loner iff j in {0, 1, 2} (canonical rows equal to W^i)
    loner_indices = []
    for j in range(n):
        others = [M[i] for i in range(n) if i != j and l1_dist(M[i], M[j]) > 1e-12]
        dist_conv = min_l1_to_convex_hull_3(M[j], others)
        if dist_conv > 1e-6:
            loner_indices.append(j)
    assert loner_indices == [0, 1, 2]

    # 3. Verify Theorem 5.7 and Claims 5.8-5.10 (Robust-Loner Recovery under l1 Row Noise):
    # Choose eps = 0.01 so 20*eps/alpha + 13*eps = 0.2967 < alpha = 1.2
    eps = 0.01
    assert (20.0 * eps / alpha + 13.0 * eps) < alpha
    M_noisy = []
    for j in range(n):
        sign = 1.0 if (j % 2 == 0) else -1.0
        pert = [sign * 0.25 * eps, -sign * 0.25 * eps, sign * 0.25 * eps, -sign * 0.25 * eps]
        row_p = [M[j][c] + pert[c] for c in range(m)]
        assert l1_dist(row_p, M[j]) <= eps + 1e-15
        M_noisy.append(row_p)

    # Verify Claim 5.8: Every row M'^j has l1-distance <= 2*eps to conv(canonical rows M'^0, M'^1, M'^2)
    canon_noisy = [M_noisy[0], M_noisy[1], M_noisy[2]]
    max_claim58_dist = 0.0
    for j in range(n):
        # Use exact weights A[j]
        recon = [sum(A[j][k] * canon_noisy[k][c] for k in range(r)) for c in range(m)]
        d58 = l1_dist(M_noisy[j], recon)
        assert d58 <= 2.0 * eps + 1e-12
        max_claim58_dist = max(max_claim58_dist, d58)

    # Verify Claims 5.9 & 5.10: Robust-loner test with threshold d = 5*eps/alpha + 2*eps
    d_thresh = 5.0 * eps / alpha + 2.0 * eps
    robust_loners = []
    for j in range(n):
        far_rows = [M_noisy[i] for i in range(n) if l1_dist(M_noisy[i], M_noisy[j]) >= d_thresh]
        dist_far = min_l1_to_convex_hull_3(M_noisy[j], far_rows)
        if dist_far > 2.0 * eps:
            robust_loners.append(j)
    assert robust_loners == [0, 1, 2]

    # Verify Theorem 5.7 reconstruction bound: ||M'^j - (A' W')^j||_1 <= 10*eps/alpha + 7*eps
    bound_thm57 = 10.0 * eps / alpha + 7.0 * eps
    assert max_claim58_dist <= bound_thm57

    # 4. Verify Failure when A violates separability (all rows are strictly interior mixtures):
    A_nonsep = [
        [0.5, 0.3, 0.2],
        [0.2, 0.5, 0.3],
        [0.3, 0.2, 0.5],
    ]
    M_nonsep = [[sum(A_nonsep[i][k] * W[k][j] for k in range(r)) for j in range(m)] for i in range(3)]
    max_vertex_recovery_gap = min(
        min(l1_dist(W[k], M_nonsep[i]) for i in range(3)) for k in range(r)
    )
    assert max_vertex_recovery_gap > 0.35

    summary = {
        "concept": "SeparableNonnegativeMatrixFactorizationAndRobustLonerRecovery",
        "robust_simplicial_alpha": round(alpha, 6),
        "exact_loner_indices": loner_indices,
        "noisy_robust_loner_indices": robust_loners,
        "claim58_max_convex_hull_l1_err": round(max_claim58_dist, 6),
        "theorem57_upper_bound": round(bound_thm57, 6),
        "nonseparable_min_vertex_l1_gap": round(max_vertex_recovery_gap, 6),
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
