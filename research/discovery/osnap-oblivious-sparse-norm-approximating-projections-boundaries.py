#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 365:
OSNAP Oblivious Sparse Norm-Approximating Projections (Nelson & Nguyen 2013, FOCS 2013, arXiv:1211.1002).
"""

import itertools
import math
import random


def mat_transpose(A):
    return [list(col) for col in zip(*A)]


def mat_mul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)] for i in range(m)]


def frob_sq(A):
    return sum(x * x for row in A for x in row)


def make_orthonormal_U(n, d, rng):
    cols = []
    for _ in range(d):
        v = [rng.gauss(0, 1) for _ in range(n)]
        for prev in cols:
            dot = sum(v[i] * prev[i] for i in range(n))
            v = [v[i] - dot * prev[i] for i in range(n)]
        norm = math.sqrt(sum(x * x for x in v))
        cols.append([x / norm for x in v])
    return mat_transpose(cols)


def sample_osnap(m, n, s, rng):
    """Blocked OSNAP construction (Section 1.2, p. 5):
    m rows partitioned into s blocks of m/s rows; for each column i in [n] and block b in [s],
    pick one row uniformly in block b and assign random sign +/- 1/sqrt(s).
    Returns (Pi, delta_matrix, sigma_matrix).
    """
    block_size = m // s
    Pi = [[0.0] * n for _ in range(m)]
    delta = [[0] * n for _ in range(m)]
    sigma = [[0] * n for _ in range(m)]
    scale = 1.0 / math.sqrt(s)
    for col in range(n):
        for b in range(s):
            r = b * block_size + rng.randrange(block_size)
            sgn = 1 if rng.random() < 0.5 else -1
            delta[r][col] = 1
            sigma[r][col] = sgn
            Pi[r][col] = sgn * scale
    return Pi, delta, sigma


def main():
    rng = random.Random(20261019)
    n, d = 16, 3
    U = make_orthonormal_U(n, d, rng)

    # 1. Verify Lemma 4 & Lemma 5 (Page 8): U^T U = I_d and row norms ||u_i||^2 <= 1, sum_i ||u_i||^2 = d
    UtU = mat_mul(mat_transpose(U), U)
    I_d = [[1.0 if k == kp else 0.0 for kp in range(d)] for k in range(d)]
    assert frob_sq([[UtU[k][kp] - I_d[k][kp] for kp in range(d)] for k in range(d)]) < 1e-24
    row_norms_sq = [sum(U[i][k] ** 2 for k in range(d)) for i in range(n)]
    assert all(rn <= 1.0 + 1e-12 for rn in row_norms_sq)
    assert abs(sum(row_norms_sq) - d) < 1e-12

    # 2. Verify Equation (3) exact Gram error expansion (Page 7):
    # For any OSNAP Pi with column sparsity s, S = (Pi U)^T (Pi U) satisfies
    # (S - I)_{k,k'} = (1/s) sum_{r=1}^m sum_{i != j} delta_{r,i} delta_{r,j} sigma_{r,i} sigma_{r,j} u_i^k u_j^{k'}
    m, s = 12, 3
    Pi, delta, sigma = sample_osnap(m, n, s, rng)
    PiU = mat_mul(Pi, U)
    S_gram = mat_mul(mat_transpose(PiU), PiU)
    max_eq3_err = 0.0
    for k in range(d):
        for kp in range(d):
            lhs = S_gram[k][kp] - (1.0 if k == kp else 0.0)
            rhs = 0.0
            for r in range(m):
                for i in range(n):
                    if delta[r][i] == 0:
                        continue
                    for j in range(n):
                        if i == j or delta[r][j] == 0:
                            continue
                        rhs += (
                            delta[r][i]
                            * delta[r][j]
                            * sigma[r][i]
                            * sigma[r][j]
                            * U[i][k]
                            * U[j][kp]
                        )
            rhs /= float(s)
            max_eq3_err = max(max_eq3_err, abs(lhs - rhs))
    assert max_eq3_err < 1e-13, f"Equation (3) error: {max_eq3_err}"

    # 3. Verify Theorem 3 exact analytical expectation E||S - I||_F^2 <= (d^2 + d)/m (Pages 7-8)
    # Note: for blocked OSNAP with general s, E||S - I||_F^2 = (1 / (s * m)) * [
    #   sum_k 2 sum_{i != j} (u_i^k)^2 (u_j^k)^2 + sum_{k != k'} sum_{i != j} ((u_i^k)^2 (u_j^{k'})^2 + u_i^k u_i^{k'} u_j^k u_j^{k'})
    # ] <= (d^2 + d) / (s * m)!
    diag_exact_unit_m = 0.0
    for k in range(d):
        for i in range(n):
            for j in range(n):
                if i != j:
                    diag_exact_unit_m += 2.0 * (U[i][k] ** 2) * (U[j][k] ** 2)
    assert diag_exact_unit_m <= 2.0 * d + 1e-12

    off_diag_exact_unit_m = 0.0
    for k in range(d):
        for kp in range(d):
            if k == kp:
                continue
            # Verify negative cross-term property: sum_{i != j} u_i^k u_i^{k'} u_j^k u_j^{k'} == - sum_i (u_i^k)^2 (u_i^{k'})^2 <= 0
            cross_sum = sum(
                U[i][k] * U[i][kp] * U[j][k] * U[j][kp]
                for i in range(n)
                for j in range(n)
                if i != j
            )
            diag_sq_sum = sum((U[i][k] ** 2) * (U[i][kp] ** 2) for i in range(n))
            assert abs(cross_sum + diag_sq_sum) < 1e-13
            assert cross_sum <= 1e-13

            term_kkp = sum(
                (U[i][k] ** 2) * (U[j][kp] ** 2) + U[i][k] * U[i][kp] * U[j][k] * U[j][kp]
                for i in range(n)
                for j in range(n)
                if i != j
            )
            assert term_kkp <= 1.0 + 1e-12
            off_diag_exact_unit_m += term_kkp

    total_exact_unit_m = diag_exact_unit_m + off_diag_exact_unit_m
    assert total_exact_unit_m <= float(d * d + d) + 1e-12

    # Compare empirical E||S - I||_F^2 (l=2, where b=2 so s^{-l} s^b = 1) and 4th moment E[tr((S-I)^4)] (l=4, where b<l gives (1/s)^{l-b} decay, Eq. 7 & 20)
    m_test = 16
    trials = 600
    emp_s1 = 0.0
    emp_s4 = 0.0
    for _ in range(trials):
        Pi1, _, _ = sample_osnap(m_test, n, 1, rng)
        S1 = mat_mul(mat_transpose(mat_mul(Pi1, U)), mat_mul(Pi1, U))
        emp_s1 += frob_sq([[S1[k][kp] - (1.0 if k == kp else 0.0) for kp in range(d)] for k in range(d)])

        Pi4, _, _ = sample_osnap(m_test, n, 4, rng)
        S4 = mat_mul(mat_transpose(mat_mul(Pi4, U)), mat_mul(Pi4, U))
        emp_s4 += frob_sq([[S4[k][kp] - (1.0 if k == kp else 0.0) for kp in range(d)] for k in range(d)])

    emp_s1 /= trials
    emp_s4 /= trials
    theo_l2 = total_exact_unit_m / m_test
    assert abs(emp_s1 - theo_l2) < 0.06
    assert abs(emp_s4 - theo_l2) < 0.06
    assert emp_s1 <= (d * d + d) / float(m_test)

    # On coherent/spiky U_spiky = [I_d; 0] (Section 1.2, p. 4-5), s=1 has off-diagonal collision size 1
    # whereas s=4 has off-diagonal collision size 1/s = 1/4, strictly reducing the 4th trace moment E[tr((S-I)^4)] (Eq. 20)!
    U_spiky = [[1.0 if i == k else 0.0 for k in range(d)] for i in range(n)]
    m4_s1 = 0.0
    m4_s4 = 0.0
    for _ in range(trials):
        Pi1, _, _ = sample_osnap(m_test, n, 1, rng)
        S1 = mat_mul(mat_transpose(mat_mul(Pi1, U_spiky)), mat_mul(Pi1, U_spiky))
        E1 = [[S1[k][kp] - (1.0 if k == kp else 0.0) for kp in range(d)] for k in range(d)]
        E1_sq = mat_mul(E1, E1)
        m4_s1 += frob_sq(E1_sq)

        Pi4, _, _ = sample_osnap(m_test, n, 4, rng)
        S4 = mat_mul(mat_transpose(mat_mul(Pi4, U_spiky)), mat_mul(Pi4, U_spiky))
        E4 = [[S4[k][kp] - (1.0 if k == kp else 0.0) for kp in range(d)] for k in range(d)]
        E4_sq = mat_mul(E4, E4)
        m4_s4 += frob_sq(E4_sq)
    m4_s1 /= trials
    m4_s4 /= trials
    assert m4_s4 < 0.5 * m4_s1

    # 4. Verify Exact Negative Correlation Property (Section 1.2, p. 5) for subset of rows in same column
    # For random s-subset of [m] in a single column j, E[delta_{r1,j} delta_{r2,j}] = (s/m) * ((s-1)/(m-1)) < (s/m)^2
    m_nc, s_nc = 10, 3
    all_subsets = list(itertools.combinations(range(m_nc), s_nc))
    prob_pair = sum(1 for sub in all_subsets if 0 in sub and 1 in sub) / float(len(all_subsets))
    assert prob_pair < (s_nc / float(m_nc)) ** 2

    print(
        f"[PASS] Round 365 OSNAP Sparse Subspace Embeddings (Nelson & Nguyen 2013): "
        f"max_eq3_err={max_eq3_err:.2e}, theo_l2={theo_l2:.4f}<={(d*d+d)/m_test:.4f}, "
        f"emp_s1={emp_s1:.4f}, m4_s4={m4_s4:.4f}<<m4_s1={m4_s1:.4f}"
    )


if __name__ == "__main__":
    main()
