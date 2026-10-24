#!/usr/bin/env python3
"""Boundary and verification script for Round 331:
CountSketch Input-Sparsity Subspace Embedding for Low-Rank Approximation and Regression
(Clarkson & Woodruff, STOC 2013 / J. ACM 2017, arXiv:1207.6365v4).
"""

import itertools
import math
import random
import sys


def matmul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [
        [sum(A[i][r] * B[r][j] for r in range(k)) for j in range(n)]
        for i in range(m)
    ]


def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def frob_sq(A):
    return sum(x * x for row in A for x in row)


def vec_norm_sq(v):
    return sum(x * x for x in v)


def solve_spd(G, rhs):
    n = len(G)
    M = [row[:] + [rhs[i]] for i, row in enumerate(G)]
    for i in range(n):
        piv = i
        for r in range(i + 1, n):
            if abs(M[r][i]) > abs(M[piv][i]):
                piv = r
        M[i], M[piv] = M[piv], M[i]
        diag = M[i][i]
        for c in range(i, n + 1):
            M[i][c] /= diag
        for r in range(n):
            if r != i:
                f = M[r][i]
                for c in range(i, n + 1):
                    M[r][c] -= f * M[i][c]
    return [M[i][n] for i in range(n)]


def apply_countsketch_matrix(h, signs, A):
    """Apply sparse embedding S = Phi * D in O(nnz(A)) operations."""
    n = len(A)
    d = len(A[0])
    t = max(h) + 1
    SA = [[0.0] * d for _ in range(t)]
    nnz_ops = 0
    for i in range(n):
        b = h[i]
        s = signs[i]
        row = A[i]
        for j in range(d):
            val = row[j]
            if val != 0.0:
                SA[b][j] += s * val
                nnz_ops += 1
    return SA, nnz_ops


def main():
    # 1. Exact expectation E_D[||Phi D A||_F^2] = ||A||_F^2 for any hash h (Lemma 40 Eq. 13)
    # and O(nnz(A)) sparse application count
    n_small, d_small, t_small = 8, 3, 4
    A_small = [
        [1.5, 0.0, -0.5],
        [0.0, 2.0, 0.0],
        [-1.0, 0.5, 0.0],
        [0.0, 0.0, 1.2],
        [0.8, 0.0, 0.0],
        [0.0, -1.1, 0.4],
        [0.3, 0.0, -0.9],
        [0.0, 0.7, 0.0],
    ]
    true_nnz = sum(1 for row in A_small for v in row if v != 0.0)
    h_fixed = [0, 1, 2, 3, 0, 2, 1, 3]
    total_frob_sq = 0.0
    num_sign_configs = 1 << n_small
    for mask in range(num_sign_configs):
        signs = [1.0 if ((mask >> i) & 1) else -1.0 for i in range(n_small)]
        SA, ops = apply_countsketch_matrix(h_fixed, signs, A_small)
        assert ops == true_nnz, f"Expected {true_nnz} ops, got {ops}"
        total_frob_sq += frob_sq(SA)
    mean_frob_sq = total_frob_sq / num_sign_configs
    exact_frob_sq = frob_sq(A_small)
    exp_frob_err = abs(mean_frob_sq - exact_frob_sq)

    # 2. Lemma 5 Heavy-Coordinate Perfect Hashing Isometry & Subspace Embedding / Regression
    # Construct n x d matrix A (n=60, d=3) with 2 heavy spiky rows (leverage score ~ 1)
    # and 58 light rows
    rng = random.Random(20261019)
    n, d = 60, 3
    A = [[0.0] * d for _ in range(n)]
    # Heavy rows 0 and 1
    A[0] = [10.0, 0.0, 0.0]
    A[1] = [0.0, 8.0, 0.0]
    for i in range(2, n):
        A[i] = [
            0.05 * rng.gauss(0, 1),
            0.05 * rng.gauss(0, 1),
            1.0 * math.sin(0.3 * i) + 0.1 * rng.gauss(0, 1),
        ]

    # Verify Lemma 5: when h(0) != h(1), for any vector y supported on heavy rows {0, 1},
    # ||Phi D y_H||_2^2 == ||y_H||_2^2 identically for EVERY sign vector D
    t = 24
    h = [rng.randrange(t) for _ in range(n)]
    h[0] = 0
    h[1] = 1  # distinct buckets for heavy coordinates
    signs = [1.0 if rng.random() < 0.5 else -1.0 for _ in range(n)]
    y_H = [[A[i][0] * 0.7 - A[i][1] * 0.4] if i < 2 else [0.0] for i in range(n)]
    Sy_H, _ = apply_countsketch_matrix(h, signs, y_H)
    heavy_isometry_err = abs(frob_sq(Sy_H) - frob_sq(y_H))

    # Birthday-collision failure boundary: if h(0) == h(1) and signs cancel on equal heavy coords,
    # a heavy subspace vector [1, 1, 0, ...] is annihilated!
    h_collide = h[:]
    h_collide[0] = 0
    h_collide[1] = 0
    signs_collide = signs[:]
    signs_collide[0] = 1.0
    signs_collide[1] = -1.0
    y_cancel = [[1.0] if i < 2 else [0.0] for i in range(n)]
    Sy_cancel, _ = apply_countsketch_matrix(h_collide, signs_collide, y_cancel)
    collision_preserved_ratio = frob_sq(Sy_cancel) / frob_sq(y_cancel)  # 0.0

    # 3. Theorem 30 / Theorem 36 Least-Squares Regression & Section 7.7 Iterative Refinement
    b = [1.2 * A[i][0] - 0.8 * A[i][1] + 0.5 * A[i][2] + 0.08 * math.cos(i) for i in range(n)]
    AT = transpose(A)
    ATA = matmul(AT, A)
    ATb = [sum(AT[j][i] * b[i] for i in range(n)) for j in range(d)]
    x_star = solve_spd(ATA, ATb)
    opt_res_sq = sum(
        (sum(A[i][j] * x_star[j] for j in range(d)) - b[i]) ** 2 for i in range(n)
    )

    # Sketched regression min_x ||S(Ax - b)||_2
    SA, _ = apply_countsketch_matrix(h, signs, A)
    b_col = [[b[i]] for i in range(n)]
    Sb_col, _ = apply_countsketch_matrix(h, signs, b_col)
    Sb = [row[0] for row in Sb_col]
    SAT = transpose(SA)
    SAT_SA = matmul(SAT, SA)
    SAT_Sb = [sum(SAT[j][i] * Sb[i] for i in range(t)) for j in range(d)]
    x_sketch = solve_spd(SAT_SA, SAT_Sb)
    sketch_res_sq = sum(
        (sum(A[i][j] * x_sketch[j] for j in range(d)) - b[i]) ** 2 for i in range(n)
    )
    rel_res_ratio = math.sqrt(sketch_res_sq / opt_res_sq)

    # Section 7.7 / Theorem 43 preconditioned iterative improvement:
    # Using (SA)^T (SA) as preconditioner M = R R^T = (SA^T SA)^{-1},
    # iterate x^{(m+1)} = x^{(m)} + (SA^T SA)^{-1} A^T (b - A x^{(m)})
    x_iter = x_sketch[:]
    for _ in range(25):
        grad = [
            sum(A[i][j] * (b[i] - sum(A[i][c] * x_iter[c] for c in range(d))) for i in range(n))
            for j in range(d)
        ]
        step = solve_spd(SAT_SA, grad)
        x_iter = [x_iter[j] + step[j] for j in range(d)]
    iter_err = math.sqrt(sum((x_iter[j] - x_star[j]) ** 2 for j in range(d)))

    ok = (
        exp_frob_err < 1e-13
        and heavy_isometry_err < 1e-14
        and collision_preserved_ratio == 0.0
        and 1.0 <= rel_res_ratio <= 1.25
        and iter_err < 1e-10
    )
    if not ok:
        print(
            f"Verification failed: exp={exp_frob_err}, heavy={heavy_isometry_err}, "
            f"coll={collision_preserved_ratio}, rel={rel_res_ratio}, iter={iter_err}",
            file=sys.stderr,
        )
        sys.exit(1)

    print(
        f"[PASS] Round 331 CountSketch Input-Sparsity Subspace Embedding: "
        f"exp_frob_err={exp_frob_err:.2e}, heavy_isometry_err={heavy_isometry_err:.2e}, "
        f"collision_preserved_ratio={collision_preserved_ratio:.2f}, "
        f"rel_res_ratio={rel_res_ratio:.4f}, precond_iter_err={iter_err:.2e}"
    )


if __name__ == "__main__":
    main()
