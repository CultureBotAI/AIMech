#!/usr/bin/env python3
r"""
Boundary and mathematical verification script for Round 330:
AIMech:FrequentDirectionsDeterministicStreamingMatrixSketching
Primary reference: Edo Liberty (2013),
"Simple and Deterministic Matrix Sketching",
Proceedings of the 19th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD 2013),
pp. 581-588 (arXiv:1206.0594v4, DOI:10.1145/2487575.2487623).

Verifies:
1. Algorithm 1 (Frequent-Directions): Deterministic streaming sketch B in R^{l x m} of A in R^{n x m}
   that inserts rows into zero rows of B, computes SVD B = U \Sigma V^T when full, shrinks squared
   singular values by \delta_i = \sigma_l^2 so \bar{\Sigma} = \sqrt{\Sigma^2 - I_l \delta_i}, and sets
   B <- \bar{\Sigma} V^T (guaranteeing the last row of B is all zeros).
2. Claim 1 (Exact Frobenius Norm Loss Accounting, p. 583):
   In every step i, ||C_i||_F^2 - ||B_i||_F^2 = l * \delta_i, and summing over all n steps yields the
   exact telescoping identity:
   \sum_{i=1}^n \delta_i = (||A||_F^2 - ||B||_F^2) / l <= ||A||_F^2 / l.
3. Claim 2 & Theorem 4.1 (Loewner Positive Semidefinite Ordering and Additive Covariance Bound, p. 583):
   For every unit vector x in R^m (||x||_2 = 1):
   0 <= ||A x||_2^2 - ||B x||_2^2 <= \sum_{i=1}^n \delta_i <= ||A||_F^2 / l,
   which guarantees both A^T A - B^T B >= 0 (PSD Loewner ordering) and
   ||A^T A - B^T B||_2 <= (||A||_F^2 - ||B||_F^2) / l <= \varepsilon ||A||_F^2 for l = \lceil 1/\varepsilon \rceil.
4. Theorem 3.1 / Section 4.1 (Space-Saving Diagonal Reduction):
   When the input rows are weighted basis indicator vectors a_i = \sqrt{w_i} e_{j_i}, B remains
   strictly diagonal and Frequent-Directions reduces exactly to the Misra-Gries / Space-Saving
   heavy-hitters counter decrement rule.
"""

import math
import random
import sys


def mat_mul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)] for i in range(m)]


def mat_T(A):
    m, n = len(A), len(A[0])
    return [[A[i][j] for i in range(m)] for j in range(n)]


def mat_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def frob_norm_sq(A):
    return sum(A[i][j] ** 2 for i in range(len(A)) for j in range(len(A[0])))


def sym_eigh(M):
    """Jacobi eigenvalue solver for symmetric matrix M (returns eigenvalues desc, eigenvectors as columns)."""
    n = len(M)
    A = [row[:] for row in M]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(120 * n * n):
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
        for i in range(n):
            vip, viq = V[i][p], V[i][q]
            V[i][p] = c * vip - s * viq
            V[i][q] = s * vip + c * viq
    evals = [A[i][i] for i in range(n)]
    order = sorted(range(n), key=lambda idx: evals[idx], reverse=True)
    sorted_evals = [evals[idx] for idx in order]
    sorted_V = [[V[i][idx] for idx in order] for i in range(n)]
    return sorted_evals, sorted_V


def frequent_directions_step(B, row_a):
    """Perform one step of Algorithm 1 (Frequent-Directions) on sketch B in R^{l x m}."""
    l, m = len(B), len(B[0])
    # Find an all-zero row in B (guaranteed to exist at index l-1 after shrinkage)
    zero_idx = None
    for r in range(l):
        if sum(x * x for x in B[r]) < 1e-24:
            zero_idx = r
            break
    assert zero_idx is not None, "Sketch B must always contain at least one all-zero row before insertion"

    B_work = [row[:] for row in B]
    B_work[zero_idx] = row_a[:]

    # Compute right singular vectors V and squared singular values \sigma_j^2 of B_work via eigendecomposition of B_work^T B_work
    BtB = mat_mul(mat_T(B_work), B_work)
    evals, V = sym_eigh(BtB)
    # Since B_work is l x m (with l <= m), the l-th squared singular value is evals[l - 1]
    delta = max(0.0, evals[l - 1])

    # Construct B_next = \bar{\Sigma} V^T in R^{l x m} where \bar{\sigma}_j = \sqrt{\max(0, \sigma_j^2 - \delta)}
    B_next = [[0.0 for _ in range(m)] for _ in range(l)]
    for j in range(l - 1):
        sigma_bar = math.sqrt(max(0.0, evals[j] - delta))
        for col in range(m):
            B_next[j][col] = sigma_bar * V[col][j]
    # Row l-1 is identically zero since \sigma_l^2 - \delta = 0
    return B_next, B_work, delta


def verify_claims_1_2_and_theorem_41():
    """Verify Claim 1 (Frobenius accounting), Claim 2 (PSD ordering), and Theorem 4.1 (covariance bound)."""
    rng = random.Random(2013)
    n, m, l = 25, 6, 4
    # Construct streaming matrix A with skewed spectrum + noise
    A = []
    for i in range(n):
        row = [
            3.0 * math.sin(0.4 * i) + 0.2 * rng.gauss(0.0, 1.0),
            2.2 * math.cos(0.3 * i) + 0.2 * rng.gauss(0.0, 1.0),
            1.4 * ((-1) ** i) + 0.2 * rng.gauss(0.0, 1.0),
            0.3 * rng.gauss(0.0, 1.0),
            0.25 * rng.gauss(0.0, 1.0),
            0.2 * rng.gauss(0.0, 1.0),
        ]
        A.append(row)

    B = [[0.0 for _ in range(m)] for _ in range(l)]
    deltas = []
    for row_a in A:
        B_next, C_i, delta_i = frequent_directions_step(B, row_a)
        # Stepwise Frobenius identity: ||C_i||_F^2 - ||B_next||_F^2 == l * delta_i
        step_loss = frob_norm_sq(C_i) - frob_norm_sq(B_next)
        assert abs(step_loss - l * delta_i) < 1e-10
        # Last row of B_next must be identically zero
        assert sum(x * x for x in B_next[l - 1]) < 1e-24
        deltas.append(delta_i)
        B = B_next

    # Claim 1: \sum_{i=1}^n \delta_i = (||A||_F^2 - ||B||_F^2) / l <= ||A||_F^2 / l
    total_delta = sum(deltas)
    frob_A_sq = frob_norm_sq(A)
    frob_B_sq = frob_norm_sq(B)
    assert abs(total_delta - (frob_A_sq - frob_B_sq) / l) < 1e-10
    assert total_delta <= frob_A_sq / l + 1e-12

    # Claim 2 & Theorem 4.1: Check eigenvalues of \Delta = A^T A - B^T B
    AtA = mat_mul(mat_T(A), A)
    BtB = mat_mul(mat_T(B), B)
    diff_cov = mat_sub(AtA, BtB)
    evals_diff, _ = sym_eigh(diff_cov)

    min_eval = evals_diff[-1]
    max_eval = evals_diff[0]
    # Loewner PSD ordering: A^T A - B^T B >= 0 (min eigenvalue >= 0 up to numerical precision)
    assert min_eval >= -1e-10, f"Expected PSD residual A^T A - B^T B >= 0, got min_eval={min_eval}"
    # Tight covariance spectral bound: ||A^T A - B^T B||_2 <= \sum \delta_i = (||A||_F^2 - ||B||_F^2)/l <= ||A||_F^2 / l
    assert max_eval <= total_delta + 1e-10, f"Expected max_eval={max_eval} <= total_delta={total_delta}"
    assert max_eval <= frob_A_sq / l + 1e-10


def verify_space_saving_item_frequency_reduction():
    """Verify Section 3 / 4.1: Frequent-Directions on indicator rows a_i = sqrt(w_i) e_{j_i} matches Space-Saving."""
    # Stream of items from universe {0, 1, 2, 3} with weights, using l = 3 counters (at most l-1 = 2 active)
    m, l = 4, 3
    stream = [(0, 5.0), (1, 3.0), (2, 2.0), (0, 4.0), (3, 1.0)]
    true_totals = [0.0] * m
    B = [[0.0 for _ in range(m)] for _ in range(l)]
    for item_idx, weight in stream:
        true_totals[item_idx] += weight
        row_a = [math.sqrt(weight) if j == item_idx else 0.0 for j in range(m)]
        B, _, _ = frequent_directions_step(B, row_a)

    # Diagonal of B^T B estimates item frequencies f'_j with 0 <= f_j - f'_j <= ||A||_F^2 / l = (\sum w_i) / l
    BtB = mat_mul(mat_T(B), B)
    total_weight = sum(true_totals)
    for j in range(m):
        est_j = BtB[j][j]
        err_j = true_totals[j] - est_j
        assert -1e-10 <= err_j <= total_weight / l + 1e-10
        # Off-diagonal entries must vanish for orthogonal basis stream
        for k in range(m):
            if j != k:
                assert abs(BtB[j][k]) < 1e-10


if __name__ == "__main__":
    verify_claims_1_2_and_theorem_41()
    verify_space_saving_item_frequency_reduction()
    print("[PASS] Round 330 Frequent-Directions deterministic matrix sketching boundary checks succeeded.")
    sys.exit(0)
