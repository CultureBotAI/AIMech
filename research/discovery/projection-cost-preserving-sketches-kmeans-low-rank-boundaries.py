#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 364:
Projection-Cost Preserving Sketches for k-Means Clustering and Low-Rank Approximation
(Cohen, Elder, Musco, Musco, & Persu 2015, STOC 2015, arXiv:1410.6801).
"""

import math
import random


def mat_transpose(A):
    return [list(col) for col in zip(*A)]


def mat_mul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)] for i in range(m)]


def mat_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mat_trace(A):
    return sum(A[i][i] for i in range(len(A)))


def frob_sq(A):
    return sum(x * x for row in A for x in row)


def jacobi_eig_sym(S, max_iter=300, tol=1e-14):
    d = len(S)
    A = [row[:] for row in S]
    V = [[1.0 if i == j else 0.0 for j in range(d)] for i in range(d)]
    for _ in range(max_iter):
        best_val = 0.0
        p, q = 0, 1
        for i in range(d):
            for j in range(i + 1, d):
                if abs(A[i][j]) > best_val:
                    best_val = abs(A[i][j])
                    p, q = i, j
        if best_val < tol:
            break
        diff = A[q][q] - A[p][p]
        if abs(A[p][q]) < tol * abs(diff):
            t = A[p][q] / diff
        else:
            phi = diff / (2.0 * A[p][q])
            t = 1.0 / (abs(phi) + math.sqrt(phi * phi + 1.0))
            if phi < 0:
                t = -t
        c = 1.0 / math.sqrt(1.0 + t * t)
        s = t * c
        tau = s / (1.0 + c)
        h = t * A[p][q]
        A[p][p] -= h
        A[q][q] += h
        A[p][q] = 0.0
        A[q][p] = 0.0
        for r in range(d):
            if r != p and r != q:
                arp, arq = A[r][p], A[r][q]
                A[r][p] = A[p][r] = arp - s * (arq + tau * arp)
                A[r][q] = A[q][r] = arq + s * (arp - tau * arq)
        for r in range(d):
            vrp, vrq = V[r][p], V[r][q]
            V[r][p] = vrp - s * (vrq + tau * vrp)
            V[r][q] = vrq + s * (vrp - tau * vrq)
    eigs = [A[i][i] for i in range(d)]
    order = sorted(range(d), key=lambda i: -eigs[i])
    sorted_eigs = [eigs[i] for i in order]
    sorted_V = [[V[r][i] for i in order] for r in range(d)]
    return sorted_eigs, sorted_V


def cluster_indicator_matrix(n, clusters):
    """Construct X_C in R^{n x k} with X_C(i, j) = 1 / sqrt(|C_j|) if i in C_j (Section 2.3, p. 6)."""
    k = len(clusters)
    X = [[0.0] * k for _ in range(n)]
    for j, cl in enumerate(clusters):
        scale = 1.0 / math.sqrt(len(cl))
        for i in cl:
            X[i][j] = scale
    return X


def kmeans_cost_direct(A, clusters):
    d = len(A[0])
    total = 0.0
    for cl in clusters:
        mu = [sum(A[i][col] for i in cl) / len(cl) for col in range(d)]
        for i in cl:
            total += sum((A[i][col] - mu[col]) ** 2 for col in range(d))
    return total


def kmeans_cost_pairwise(A, clusters):
    """Pairwise squared distance identity (Section 9, p. 23):
    sum_{i=1}^k (1/|C_i|) sum_{j != l in C_i} ||a_j - a_l||_2^2 / 2
    Wait: in paper p. 23: sum_{b_j, b_k in C_i, j!=k} ||b_j - b_k||^2 counts each ordered pair (j,k) and (k,j),
    Wait: sum_{j=1}^{|C_i|} ||b_j - mu_i||^2 = (1/(2|C_i|)) sum_{j,k in C_i} ||b_j - b_k||^2
    = (1/|C_i|) sum_{j < k in C_i} ||b_j - b_k||^2.
    """
    d = len(A[0])
    total = 0.0
    for cl in clusters:
        cl_list = list(cl)
        sub = 0.0
        for idx1 in range(len(cl_list)):
            for idx2 in range(idx1 + 1, len(cl_list)):
                i1, i2 = cl_list[idx1], cl_list[idx2]
                sub += sum((A[i1][col] - A[i2][col]) ** 2 for col in range(d))
        total += sub / len(cl_list)
    return total


def main():
    rng = random.Random(20261019)
    n, d, k = 12, 8, 2
    # Construct A in R^{12 x 8} with 2 well-separated clusters + decaying spectrum
    A = []
    for i in range(n):
        center = 2.5 if i < 6 else -2.5
        row = [
            center + 0.4 * rng.gauss(0, 1),
            -0.8 * center + 0.4 * rng.gauss(0, 1),
            0.9 * math.sin(i + 1),
            0.7 * math.cos(i + 1),
            0.4 * rng.gauss(0, 1),
            0.3 * rng.gauss(0, 1),
            0.2 * rng.gauss(0, 1),
            0.15 * rng.gauss(0, 1),
        ]
        A.append(row)

    # 1. Verify Section 2.3 k-Means as Constrained Low-Rank Approximation (Page 6)
    C_opt = [list(range(0, 6)), list(range(6, 12))]
    C_alt = [list(range(0, 4)) + [6, 7], [4, 5] + list(range(8, 12))]
    for cl in (C_opt, C_alt):
        X_C = cluster_indicator_matrix(n, cl)
        P_C = mat_mul(X_C, mat_transpose(X_C))
        # Verify P_C is a rank-k orthogonal projection
        P_C_sq = mat_mul(P_C, P_C)
        assert frob_sq(mat_sub(P_C_sq, P_C)) < 1e-24
        assert abs(mat_trace(P_C) - k) < 1e-12
        # Verify ||A - X_C X_C^T A||_F^2 == direct k-means cost == pairwise distance cost
        PA = mat_mul(P_C, A)
        cost_proj = frob_sq(mat_sub(A, PA))
        cost_dir = kmeans_cost_direct(A, cl)
        cost_pw = kmeans_cost_pairwise(A, cl)
        assert abs(cost_proj - cost_dir) < 1e-11
        assert abs(cost_dir - cost_pw) < 1e-11

    # 2. Verify Lemma 5 & Theorem 7: One-Sided Projection-Cost Preserving Sketch via Top m = ceil(k/eps) SVD (Pages 8-12)
    # Compute SVD of A via A^T A
    AtA = mat_mul(mat_transpose(A), A)
    eigs_A, V_A = jacobi_eig_sym(AtA)
    # Best rank-k residual ||A_{r \ k}||_F^2 = sum_{i=k+1}^d sigma_i^2(A)
    rem_k_frob_sq = sum(eigs_A[k:])
    eps = 0.5  # m = ceil(k / eps) = ceil(2 / 0.5) = 4
    m = int(math.ceil(k / eps))
    assert m == 4
    # Sketch A_tilde = A V_m in R^{n x m}
    V_m = [[V_A[row][col] for col in range(m)] for row in range(d)]
    A_tilde = mat_mul(A, V_m)
    c_const = sum(eigs_A[m:])  # c = -tr(E) = ||A_{r \ m}||_F^2 >= 0

    # Verify Equation (15)-(16) (Page 12): sum_{i=m+1}^{m+k} sigma_i^2(A) <= eps * ||A_{r \ k}||_F^2
    sum_top_k_err = sum(eigs_A[m : m + k])
    assert sum_top_k_err <= eps * rem_k_frob_sq + 1e-12

    # Check Definition 2 one-sided PCP guarantee across C_opt, C_alt, and 20 random rank-k projections P
    max_rel_err = 0.0
    min_one_sided_diff = 1e9
    test_projections = [
        mat_mul(cluster_indicator_matrix(n, C_opt), mat_transpose(cluster_indicator_matrix(n, C_opt))),
        mat_mul(cluster_indicator_matrix(n, C_alt), mat_transpose(cluster_indicator_matrix(n, C_alt))),
    ]
    for _ in range(20):
        # Generate random n x k orthonormal matrix Q via Gram-Schmidt
        Q_cols = []
        for _ in range(k):
            v = [rng.gauss(0, 1) for _ in range(n)]
            for q_prev in Q_cols:
                dot = sum(v[idx] * q_prev[idx] for idx in range(n))
                v = [v[idx] - dot * q_prev[idx] for idx in range(n)]
            norm = math.sqrt(sum(x * x for x in v))
            Q_cols.append([x / norm for x in v])
        Q = mat_transpose(Q_cols)
        test_projections.append(mat_mul(Q, mat_transpose(Q)))

    for P in test_projections:
        true_cost = frob_sq(mat_sub(A, mat_mul(P, A)))
        sketch_cost = frob_sq(mat_sub(A_tilde, mat_mul(P, A_tilde))) + c_const
        one_sided_diff = sketch_cost - true_cost
        rel_err = (sketch_cost - true_cost) / true_cost
        min_one_sided_diff = min(min_one_sided_diff, one_sided_diff)
        max_rel_err = max(max_rel_err, rel_err)
        assert true_cost - 1e-11 <= sketch_cost <= (1.0 + eps) * true_cost + 1e-11

    # 3. Verify Lemma 6 & Lemma 10 Four-Term Error Decomposition C_tilde - C = E_1 + E_2 + E_3 + E_4 (Pages 9-15)
    # Split A = A_k + A_{r\k} = W_1 B + W_2 B using Z = V_k
    V_k = [[V_A[row][col] for col in range(k)] for row in range(d)]
    ZZt = mat_mul(V_k, mat_transpose(V_k))
    A_k_mat = mat_mul(A, ZZt)
    A_rem_mat = mat_sub(A, A_k_mat)
    # Sketch matrix R in R^{d x m_rp} (dense JL random projection)
    m_rp = 16
    R_jl = [[(1.0 if rng.random() < 0.5 else -1.0) / math.sqrt(m_rp) for _ in range(m_rp)] for _ in range(d)]
    RRt = mat_mul(R_jl, mat_transpose(R_jl))
    I_d = [[1.0 if i == j else 0.0 for j in range(d)] for i in range(d)]
    Delta_R = mat_sub(RRt, I_d)

    E1 = mat_mul(mat_mul(A_k_mat, Delta_R), mat_transpose(A_k_mat))
    E2 = mat_mul(mat_mul(A_rem_mat, Delta_R), mat_transpose(A_rem_mat))
    E3 = mat_mul(mat_mul(A_k_mat, Delta_R), mat_transpose(A_rem_mat))
    E4 = mat_mul(mat_mul(A_rem_mat, Delta_R), mat_transpose(A_k_mat))

    C_mat = mat_mul(A, mat_transpose(A))
    AR_mat = mat_mul(A, R_jl)
    C_tilde = mat_mul(AR_mat, mat_transpose(AR_mat))
    P_test = test_projections[0]
    I_n = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    Y_test = mat_sub(I_n, P_test)

    lhs_eq10 = mat_trace(mat_mul(mat_mul(Y_test, C_tilde), Y_test))
    rhs_eq10 = (
        mat_trace(mat_mul(mat_mul(Y_test, C_mat), Y_test))
        + mat_trace(mat_mul(mat_mul(Y_test, E1), Y_test))
        + mat_trace(mat_mul(mat_mul(Y_test, E2), Y_test))
        + mat_trace(mat_mul(mat_mul(Y_test, E3), Y_test))
        + mat_trace(mat_mul(mat_mul(Y_test, E4), Y_test))
    )
    eq10_err = abs(lhs_eq10 - rhs_eq10)
    assert eq10_err < 1e-10, f"Equation (10) four-term decomposition error: {eq10_err}"

    # 4. Verify Theorem 19 Equation (27) (Page 22): B = P^* A, B_bar = (I - P^*) A
    # ||A - P_tilde A||_F <= ||B - P_tilde B||_F + ||B_bar||_F
    P_star = test_projections[0]
    P_tilde = test_projections[1]
    B_part = mat_mul(P_star, A)
    B_bar = mat_sub(A, B_part)
    lhs_eq27 = math.sqrt(frob_sq(mat_sub(A, mat_mul(P_tilde, A))))
    rhs_eq27 = math.sqrt(frob_sq(mat_sub(B_part, mat_mul(P_tilde, B_part)))) + math.sqrt(frob_sq(B_bar))
    assert lhs_eq27 <= rhs_eq27 + 1e-12

    print(
        f"[PASS] Round 364 Projection-Cost Preserving Sketches (Cohen et al. 2015): "
        f"min_one_sided_diff={min_one_sided_diff:.2e}>=0, max_rel_err={max_rel_err:.4f}<={eps:.2f}, "
        f"eq10_err={eq10_err:.2e}, eq27_margin={rhs_eq27 - lhs_eq27:.4f}>=0"
    )


if __name__ == "__main__":
    main()
