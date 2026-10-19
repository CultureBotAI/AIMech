#!/usr/bin/env python3
r"""
Boundary and mathematical verification script for Round 329:
AIMech:SubsampledRandomizedHadamardTransformSubspaceEmbedding
Primary reference: Joel A. Tropp (2011),
"Improved Analysis of the Subsampled Randomized Hadamard Transform",
Advances in Adaptive Data Analysis 3(1-2):115-126 (arXiv:1011.1595v4).

Verifies:
1. Definition & Orthonormality of Walsh-Hadamard Transform + Diagonal Rademacher Sign Modulation:
   For n = 2^q, H_n in R^{n x n} scaled by 1/sqrt(n) satisfies H_n^T H_n = I_n, and for any
   n x k matrix V with orthonormal columns (V^T V = I_k), W = H_n D V also has orthonormal
   columns (W^T W = I_k, ||W||_F^2 = k).
2. Lemma 3.3 (Flattening of Row Norms / Coherence):
   Even for the worst-case maximally coherent basis V = [e_1, ..., e_k] where max_j ||e_j^T V||_2 = 1,
   applying the randomized Walsh-Hadamard transform W = H_n D V flattens every row norm
   ||e_j^T W||_2 to concentrically cluster around sqrt(k/n), strictly bounded away from 1.
   Specifically, for k = 1, ||e_j^T (H_n D e_1)||_2 = 1/sqrt(n) deterministically for every row j!
3. Theorem 3.1 & Section 3.3 (Subspace Embedding vs. Coupon-Collector Dimension Barrier):
   When l >= k rows are sampled uniformly without replacement via R in R^{l x n} and scaled by
   sqrt(n/l) so \Phi = sqrt(n/l) R H_n D, \Phi V preserves all k singular values bounded away
   from zero (\sigma_k(\Phi V) > 0), whereas unpreconditioned uniform row sampling sqrt(n/l) R V
   on a spike basis V = [e_1, ..., e_k] suffers catastrophic rank collapse (\sigma_k = 0) whenever
   any of the k spike rows is missed, and when l < k, rank(\Phi V) <= l < k implies \sigma_k(\Phi V) = 0.
"""

import math
import random
import sys


def build_hadamard(n):
    """Recursively construct normalized n x n Walsh-Hadamard matrix H_n with H_n^T H_n = I_n."""
    if n == 1:
        return [[1.0]]
    H_half = build_hadamard(n // 2)
    m = n // 2
    scale = 1.0 / math.sqrt(2.0)
    H = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        for j in range(m):
            val = H_half[i][j] * scale
            H[i][j] = val
            H[i][j + m] = val
            H[i + m][j] = val
            H[i + m][j + m] = -val
    return H


def mat_mul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)] for i in range(m)]


def mat_T(A):
    m, n = len(A), len(A[0])
    return [[A[i][j] for i in range(m)] for j in range(n)]


def sym_eigh_evals(M):
    """Jacobi eigenvalue solver returning eigenvalues sorted descending."""
    n = len(M)
    A = [row[:] for row in M]
    for _ in range(100 * n * n):
        max_val = 0.0
        p, q = 0, 1
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i][j]) > max_val:
                    max_val = abs(A[i][j])
                    p, q = i, j
        if max_val < 1e-14:
            break
        diff = A[q][q] - A[p][p]
        theta = math.pi / 4.0 if abs(diff) < 1e-15 else 0.5 * math.atan2(2.0 * A[p][q], diff)
        c, s = math.cos(theta), math.sin(theta)
        app, aqq, apq = A[p][p], A[q][q], A[p][q]
        A[p][p] = c * c * app - 2.0 * s * c * apq + s * s * aqq
        A[q][q] = s * s * app + 2.0 * s * c * apq + c * c * aqq
        A[p][q] = A[q][p] = 0.0
        for i in range(n):
            if i != p and i != q:
                aip, aiq = A[i][p], A[i][q]
                A[i][p] = A[p][i] = c * aip - s * aiq
                A[i][q] = A[q][i] = s * aip + c * aiq
    return sorted([A[i][i] for i in range(n)], reverse=True)


def row_norm(M, r):
    return math.sqrt(sum(x * x for x in M[r]))


def verify_lemma33_row_norm_flattening():
    """Verify Lemma 3.3: W = H_n D V flattens adversarial unit-spike row norms from 1 down to O(sqrt(k/n))."""
    n = 32
    k = 4
    H = build_hadamard(n)

    # Check H^T H = I_n
    HtH = mat_mul(mat_T(H), H)
    for i in range(n):
        for j in range(n):
            assert abs(HtH[i][j] - (1.0 if i == j else 0.0)) < 1e-12

    # Worst-case maximally coherent orthonormal matrix V = [e_1, ..., e_k]
    V = [[1.0 if i == j else 0.0 for j in range(k)] for i in range(n)]
    max_raw_row_norm = max(row_norm(V, r) for r in range(n))
    assert abs(max_raw_row_norm - 1.0) < 1e-12

    # For k = 1, ||e_r^T H D e_1||_2 == 1/sqrt(n) deterministically for every row r
    rng = random.Random(2011)
    signs = [1.0 if rng.random() < 0.5 else -1.0 for _ in range(n)]
    DV = [[signs[i] * V[i][j] for j in range(k)] for i in range(n)]
    W = mat_mul(H, DV)

    # Check W^T W = I_k and ||W||_F^2 = k
    WtW = mat_mul(mat_T(W), W)
    for i in range(k):
        for j in range(k):
            assert abs(WtW[i][j] - (1.0 if i == j else 0.0)) < 1e-12
    frob_sq = sum(row_norm(W, r) ** 2 for r in range(n))
    assert abs(frob_sq - k) < 1e-12

    # Because V = [e_1, ..., e_k] has only 1 non-zero entry per column, each entry of W = H D V
    # in row r and column j has magnitude |H_{r,j} * sign_j| = 1/sqrt(n), so EVERY row norm of W
    # is deterministically sqrt(k / n)! And even for general dense V, Lemma 3.3 bounds max row norm
    # by sqrt(k/n) + sqrt(8 log(n/\delta) / n).
    expected_flat_norm = math.sqrt(k / n)
    for r in range(n):
        assert abs(row_norm(W, r) - expected_flat_norm) < 1e-12

    # Also test a general coherent V combining spikes and dense vectors
    V_mixed = [[0.0 for _ in range(k)] for _ in range(n)]
    V_mixed[0][0] = 1.0
    V_mixed[1][1] = math.sqrt(0.5)
    V_mixed[2][1] = math.sqrt(0.5)
    for r in range(3, 7):
        V_mixed[r][2] = 0.5
    for r in range(7, 15):
        V_mixed[r][3] = 1.0 / math.sqrt(8.0)

    signs2 = [1.0 if rng.random() < 0.5 else -1.0 for _ in range(n)]
    W_mixed = mat_mul(H, [[signs2[i] * V_mixed[i][j] for j in range(k)] for i in range(n)])
    bound_lemma33 = math.sqrt(k / n) + math.sqrt(8.0 * math.log(n / 0.05) / n)
    max_w_mixed_row = max(row_norm(W_mixed, r) for r in range(n))
    assert max_w_mixed_row <= bound_lemma33
    assert max_w_mixed_row < 0.70 * max(row_norm(V_mixed, r) for r in range(n))


def verify_theorem31_subspace_embedding_and_dimension_barrier():
    """Verify Theorem 3.1 subspace embedding for l >= k and rank deficiency when l < k or without HD."""
    n = 32
    k = 4
    H = build_hadamard(n)
    V = [[1.0 if i == j else 0.0 for j in range(k)] for i in range(n)]

    rng = random.Random(31415)
    l = 16  # Sample size l in [k, n]
    scale = math.sqrt(n / l)

    srht_full_rank_count = 0
    raw_full_rank_count = 0
    trials = 40
    for _ in range(trials):
        signs = [1.0 if rng.random() < 0.5 else -1.0 for _ in range(n)]
        DV = [[signs[i] * V[i][j] for j in range(k)] for i in range(n)]
        W = mat_mul(H, DV)
        sampled_rows = rng.sample(range(n), l)

        Phi_V = [[scale * W[r][j] for j in range(k)] for r in sampled_rows]
        Gram_srht = mat_mul(mat_T(Phi_V), Phi_V)
        evals_srht = sym_eigh_evals(Gram_srht)
        sigma_min_srht = math.sqrt(max(0.0, evals_srht[-1]))
        sigma_max_srht = math.sqrt(max(0.0, evals_srht[0]))
        if sigma_min_srht > 0.35 and sigma_max_srht < 1.85:
            srht_full_rank_count += 1

        Raw_V = [[scale * V[r][j] for j in range(k)] for r in sampled_rows]
        Gram_raw = mat_mul(mat_T(Raw_V), Raw_V)
        evals_raw = sym_eigh_evals(Gram_raw)
        if evals_raw[-1] > 1e-8:
            raw_full_rank_count += 1

    # SRHT preserves full column rank and bounded singular values in 100% of trials,
    # whereas unpreconditioned uniform row sampling misses at least one coordinate spike in ~95% of trials!
    assert srht_full_rank_count == trials, f"Expected SRHT to succeed in all {trials} trials, got {srht_full_rank_count}"
    assert raw_full_rank_count <= 6, f"Expected raw row sampling on spike basis to fail most trials, got {raw_full_rank_count}"

    # Boundary check: when l < k (e.g. l = 3 < k = 4), \Phi V in R^{3 x 4} has rank at most l < k,
    # so \sigma_k(\Phi V) == 0 deterministically.
    l_small = k - 1
    Phi_V_small = [[W[r][j] for j in range(k)] for r in range(l_small)]
    Gram_small = mat_mul(mat_T(Phi_V_small), Phi_V_small)
    evals_small = sym_eigh_evals(Gram_small)
    assert abs(evals_small[-1]) < 1e-12


if __name__ == "__main__":
    verify_lemma33_row_norm_flattening()
    verify_theorem31_subspace_embedding_and_dimension_barrier()
    print("[PASS] Round 329 Subsampled Randomized Hadamard Transform (SRHT) boundary checks succeeded.")
    sys.exit(0)
