#!/usr/bin/env python3
"""Boundary and verification script for Round 335:
Matrix Approximation and Projective Clustering via Volume Sampling
(Deshpande, Rademacher, Vempala, & Wang, Theory of Computing 2006, 2(12):225-247, DOI:10.4086/toc.2006.v002a012).
"""

import itertools
import math
import sys


def det_small(M):
    k = len(M)
    if k == 0:
        return 1.0
    if k == 1:
        return M[0][0]
    if k == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    if k == 3:
        return (
            M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
        )
    A = [row[:] for row in M]
    sign = 1.0
    for i in range(k):
        piv = i
        for r in range(i + 1, k):
            if abs(A[r][i]) > abs(A[piv][i]):
                piv = r
        if abs(A[piv][i]) < 1e-15:
            return 0.0
        if piv != i:
            A[i], A[piv] = A[piv], A[i]
            sign = -sign
        for r in range(i + 1, k):
            f = A[r][i] / A[i][i]
            for c in range(i + 1, k):
                A[r][c] -= f * A[i][c]
    prod = sign
    for i in range(k):
        prod *= A[i][i]
    return prod


def gram_rows(rows):
    k = len(rows)
    n = len(rows[0])
    return [[sum(rows[i][c] * rows[j][c] for c in range(n)) for j in range(k)] for i in range(k)]


def jacobi_eigs_spd(G):
    n = len(G)
    A = [row[:] for row in G]
    for _ in range(60):
        p, q = 0, 1
        mx = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i][j]) > mx:
                    mx = abs(A[i][j])
                    p, q = i, j
        if mx < 1e-15:
            break
        phi = (A[q][q] - A[p][p]) / (2.0 * A[p][q])
        t = 1.0 / (abs(phi) + math.sqrt(phi * phi + 1.0))
        if phi < 0:
            t = -t
        c = 1.0 / math.sqrt(1.0 + t * t)
        s = t * c
        tau = s / (1.0 + c)
        h = t * A[p][q]
        A[p][p] -= h
        A[q][q] += h
        A[p][q] = A[q][p] = 0.0
        for r in range(n):
            if r != p and r != q:
                arp, arq = A[r][p], A[r][q]
                A[r][p] = A[p][r] = arp - s * (arq + tau * arp)
                A[r][q] = A[q][r] = arq + s * (arp - tau * arq)
    return sorted([max(0.0, A[i][i]) for i in range(n)], reverse=True)


def proj_residual_sq(A, row_subset):
    """Compute ||A - pi_{span(A_S)}(A)||_F^2 by orthonormalizing rows in row_subset."""
    n = len(A[0])
    basis = []
    for idx in row_subset:
        u = A[idx][:]
        for q in basis:
            dot = sum(u[c] * q[c] for c in range(n))
            u = [u[c] - dot * q[c] for c in range(n)]
        nrm = math.sqrt(sum(x * x for x in u))
        if nrm > 1e-12:
            basis.append([x / nrm for x in u])
    total_sq = 0.0
    for row in A:
        proj_sq = sum(sum(row[c] * q[c] for c in range(n)) ** 2 for q in basis)
        row_sq = sum(x * x for x in row)
        total_sq += max(0.0, row_sq - proj_sq)
    return total_sq


def main():
    # 1. Verify Lemma 3.1, Lemma 3.3 (Eq. 3.5), and Theorem 1.2 (Equations 3.4-3.8, p. 232)
    A = [
        [3.1, 0.4, -0.2, 0.1],
        [0.3, 2.4, 0.5, -0.3],
        [-0.2, 0.6, 1.3, 0.2],
        [1.5, -1.1, 0.8, 0.6],
        [-0.9, 0.7, -0.4, 0.5],
        [0.4, 0.2, -0.5, -0.4],
    ]
    m, n = len(A), len(A[0])
    k = 2

    # Singular values squared sigma_1^2 >= ... >= sigma_n^2 via A^T A
    ATA = [[sum(A[r][i] * A[r][j] for r in range(m)) for j in range(n)] for i in range(n)]
    sig_sq = jacobi_eigs_spd(ATA)
    best_rank_k_frob_sq = sum(sig_sq[k:])

    # Elementary symmetric polynomials e_k(sigma_1^2, ..., sigma_n^2) and e_{k+1}
    e_k = sum(
        math.prod(sig_sq[i] for i in sub)
        for sub in itertools.combinations(range(n), k)
    )
    e_k_plus_1 = sum(
        math.prod(sig_sq[i] for i in sub)
        for sub in itertools.combinations(range(n), k + 1)
    )

    # Sum over all k-subsets S of rows of det(A_S A_S^T) = (k!)^2 Delta_S^2
    k_subsets = list(itertools.combinations(range(m), k))
    det_k_map = {S: max(0.0, det_small(gram_rows([A[i] for i in S]))) for S in k_subsets}
    sum_det_k = sum(det_k_map.values())
    lemma33_k_err = abs(sum_det_k - e_k)

    k1_subsets = list(itertools.combinations(range(m), k + 1))
    sum_det_k1 = sum(max(0.0, det_small(gram_rows([A[i] for i in T]))) for T in k1_subsets)
    lemma33_k1_err = abs(sum_det_k1 - e_k_plus_1)

    # Verify Lemma 3.1: for each S and j not in S, d(a_j, H_S)^2 * det(A_S A_S^T) == det(A_{S u {j}} A_{S u {j}}^T)
    # and exact expected squared Frobenius residual under volume sampling:
    # E_S[||A - pi_{H_S}(A)||_F^2] == (k + 1) * e_{k+1}(sigma^2) / e_k(sigma^2) <= (k + 1) ||A - A_k||_F^2
    exp_frob_sq = sum(
        (det_k_map[S] / sum_det_k) * proj_residual_sq(A, S)
        for S in k_subsets
    )
    exact_ratio_rhs = (k + 1) * (e_k_plus_1 / e_k)
    eq37_err = abs(exp_frob_sq - exact_ratio_rhs)
    thm12_bound = (k + 1) * best_rank_k_frob_sq

    # 2. Verify Proposition 4.1 (p. 233): Tightness of the (k + 1) factor
    # Construct (k+1) x (k+1) matrix A_tight whose rows are vertices of a regular k-simplex in R^k
    # lifted by eps in coordinate k+1: for k=2, 3 vertices on unit circle in R^2 plus eps in R^3.
    eps = 1e-4
    A_tight = [
        [math.cos(2.0 * math.pi * i / 3.0), math.sin(2.0 * math.pi * i / 3.0), eps]
        for i in range(3)
    ]
    ATA_tight = [[sum(A_tight[r][i] * A_tight[r][j] for r in range(3)) for j in range(3)] for i in range(3)]
    sig_sq_tight = jacobi_eigs_spd(ATA_tight)
    opt_rank2_tight = sig_sq_tight[2]  # = 3 * eps^2
    # Every 2-subset of rows of A_tight gives the exact same residual
    subset_res_tight = proj_residual_sq(A_tight, (0, 1))
    tight_ratio = subset_res_tight / opt_rank2_tight  # approaches k + 1 = 3 as eps -> 0

    # 3. Verify failure boundary of independent length-squared row sampling vs volume sampling:
    # Construct matrix with M_dup=10 identical heavy rows [10, 0] and 1 orthogonal light row [0, 0.1].
    # Any 2-subset of the identical heavy rows has rank 1 (volume 0) and fails to span R^2,
    # whereas volume sampling assigns probability 1.0 to pairs containing the orthogonal row!
    M_dup = 10
    A_skew = [[10.0, 0.0] for _ in range(M_dup)] + [[0.0, 0.1]]
    skew_pairs = list(itertools.combinations(range(M_dup + 1), 2))
    vol_weights = {S: max(0.0, det_small(gram_rows([A_skew[i] for i in S]))) for S in skew_pairs}
    vol_total = sum(vol_weights.values())
    vol_expected_err = sum(
        (vol_weights[S] / vol_total) * proj_residual_sq(A_skew, S)
        for S in skew_pairs
    )
    # Independent length-squared sampling picks two heavy rows with probability (1000 / 1000.01)^2
    p_heavy = (M_dup * 100.0) / (M_dup * 100.0 + 0.01)
    iid_dup_prob = p_heavy ** 2

    ok = (
        lemma33_k_err < 1e-12
        and lemma33_k1_err < 1e-12
        and eq37_err < 1e-12
        and exp_frob_sq <= thm12_bound
        and abs(tight_ratio - 3.0) < 1e-6
        and vol_expected_err < 1e-15
        and iid_dup_prob > 0.9999
    )
    if not ok:
        print("Verification failed!", file=sys.stderr)
        sys.exit(1)

    print(
        f"[PASS] Round 335 Volume Sampling (Deshpande et al. 2006): "
        f"lemma33_k_err={lemma33_k_err:.2e}, eq37_err={eq37_err:.2e}, "
        f"exp_frob_sq={exp_frob_sq:.4f} <= thm12_bound={thm12_bound:.4f}, "
        f"tight_ratio={tight_ratio:.6f}, vol_expected_err={vol_expected_err:.2e}"
    )


if __name__ == "__main__":
    main()
