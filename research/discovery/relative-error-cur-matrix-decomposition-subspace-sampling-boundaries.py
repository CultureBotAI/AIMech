#!/usr/bin/env python3
"""Boundary and verification script for Round 332:
Relative-Error CUR Matrix Decomposition via Subspace Leverage Score Sampling
(Drineas, Mahoney, & Muthukrishnan, SIMAX 2008, 30(2):844-881, arXiv:0708.3696v1).
"""

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


def frob_norm(A):
    return math.sqrt(sum(x * x for row in A for x in row))


def mat_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def sym_jacobi_eig(S, max_sweeps=500):
    n = len(S)
    A = [row[:] for row in S]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(max_sweeps):
        max_val = 0.0
        p, q = 0, 1
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i][j]) > max_val:
                    max_val = abs(A[i][j])
                    p, q = i, j
        if max_val < 1e-15:
            break
        diff = A[q][q] - A[p][p]
        if abs(A[p][q]) < 1e-30:
            t = 0.0
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
        A[p][q] = A[q][p] = 0.0
        for r in range(n):
            if r != p and r != q:
                arp, arq = A[r][p], A[r][q]
                A[r][p] = A[p][r] = arp - s * (arq + tau * arp)
                A[r][q] = A[q][r] = arq + s * (arp - tau * arq)
        for r in range(n):
            vrp, vrq = V[r][p], V[r][q]
            V[r][p] = vrp - s * (vrq + tau * vrp)
            V[r][q] = vrq + s * (vrp - tau * vrq)
    vals = [A[i][i] for i in range(n)]
    order = sorted(range(n), key=lambda i: -vals[i])
    vals_sorted = [max(0.0, vals[i]) for i in order]
    V_sorted = [[V[r][order[c]] for c in range(n)] for r in range(n)]
    return vals_sorted, V_sorted


def thin_svd(A, tol=1e-10):
    m, n = len(A), len(A[0])
    AT = transpose(A)
    ATA = matmul(AT, A)
    eigvals, V = sym_jacobi_eig(ATA)
    max_sigma = math.sqrt(max(0.0, eigvals[0])) if eigvals else 0.0
    sigmas = []
    U_cols = []
    V_cols = []
    for j in range(n):
        v_col = [V[i][j] for i in range(n)]
        u_raw = [sum(A[i][r] * v_col[r] for r in range(n)) for i in range(m)]
        sigma = math.sqrt(sum(x * x for x in u_raw))
        if sigma > tol * max(1.0, max_sigma):
            u_col = [x / sigma for x in u_raw]
            sigmas.append(sigma)
            U_cols.append(u_col)
            V_cols.append(v_col)
    U = [[U_cols[c][r] for c in range(len(sigmas))] for r in range(m)]
    V_mat = [[V_cols[c][r] for c in range(len(sigmas))] for r in range(n)]
    return U, sigmas, V_mat


def pinv(A, rank_trunc=None):
    U, sigmas, V = thin_svd(A)
    r = len(sigmas) if rank_trunc is None else min(rank_trunc, len(sigmas))
    m, n = len(A), len(A[0])
    res = [[0.0] * m for _ in range(n)]
    for k in range(r):
        inv_s = 1.0 / sigmas[k]
        for i in range(n):
            for j in range(m):
                res[i][j] += V[i][k] * inv_s * U[j][k]
    return res


def spectral_norm(A):
    _, sigmas, _ = thin_svd(A)
    return sigmas[0] if sigmas else 0.0


def main():
    # Construct m x n matrix A (m=10, n=8) with k=2 dominant singular directions:
    # Direction 1 has large singular value sigma_1 = 50 on columns 0..5,
    # Direction 2 has smaller singular value sigma_2 = 2.0 concentrated on columns 6,7,
    # plus small tail noise on k > 2.
    m, n, k = 10, 8, 2
    U_full, _, _ = thin_svd(
        [[math.sin((i + 1) * (j + 1) * 0.7) + (1.5 if i == j else 0.0) for j in range(m)] for i in range(m)]
    )
    # Build V_true (n x n orthogonal) where column 0 is spread over 0..5 and column 1 is on 6,7
    V0 = [1.0 / math.sqrt(6.0) if j < 6 else 0.0 for j in range(n)]
    V1 = [0.0 if j < 6 else 1.0 / math.sqrt(2.0) for j in range(n)]
    V2 = [1.0 / math.sqrt(2.0) if j == 0 else (-1.0 / math.sqrt(2.0) if j == 1 else 0.0) for j in range(n)]
    V3 = [0.0, 0.0, 1.0 / math.sqrt(2.0), -1.0 / math.sqrt(2.0), 0.0, 0.0, 0.0, 0.0]
    V_basis = [V0, V1, V2, V3]
    sigmas_true = [50.0, 2.0, 0.08, 0.05]

    A = [[0.0] * n for _ in range(m)]
    for r_idx, s_val in enumerate(sigmas_true):
        for i in range(m):
            for j in range(n):
                A[i][j] += s_val * U_full[i][r_idx] * V_basis[r_idx][j]

    U_A, sig_A, V_A = thin_svd(A)
    # Best rank-k approximation A_k
    A_k = [[sum(sig_A[r] * U_A[i][r] * V_A[j][r] for r in range(k)) for j in range(n)] for i in range(m)]
    opt_err_f = frob_norm(mat_sub(A, A_k))

    # 1. Verify Equation 4 & 13: subspace sampling probabilities p_j = ||(V_{A,k})_{(j)}||_2^2 / k sum to 1
    p_col = [sum(V_A[j][r] ** 2 for r in range(k)) / k for j in range(n)]
    prob_sum_err = abs(sum(p_col) - 1.0)

    # 2. Verify Section 6.3.1 Lemma 1 (Equations 25-28):
    # For row-sampled S U_{A,k}, rank(S U_{A,k}) = k,
    # (S A_k)^+ = V_{A,k} Sigma_{A,k}^{-1} (S U_{A,k})^+,
    # and ||(S U_{A,k})^+ - (S U_{A,k})^T||_2 = ||Sigma_{S U_{A,k}}^{-1} - Sigma_{S U_{A,k}}||_2
    p_row_U = [sum(U_A[i][r] ** 2 for r in range(k)) / k for i in range(m)]
    sampled_rows = [0, 1, 2, 4, 6, 8]
    r_samp = len(sampled_rows)
    # Form S U_{A,k} and S A_k
    SU_k = [
        [U_A[i][c_idx] / math.sqrt(r_samp * p_row_U[i]) for c_idx in range(k)]
        for i in sampled_rows
    ]
    SA_k = [
        [A_k[i][j] / math.sqrt(r_samp * p_row_U[i]) for j in range(n)]
        for i in sampled_rows
    ]
    _, sig_SU, _ = thin_svd(SU_k)
    assert len(sig_SU) == k
    SU_k_pinv = pinv(SU_k)
    SA_k_pinv = pinv(SA_k)
    # V_{A,k} Sigma_{A,k}^{-1} (S U_{A,k})^+
    V_k_Sig_inv = [[V_A[j][r] / sig_A[r] for r in range(k)] for j in range(n)]
    rhs_lemma1_eq27 = matmul(V_k_Sig_inv, SU_k_pinv)
    lemma1_eq27_err = frob_norm(mat_sub(SA_k_pinv, rhs_lemma1_eq27))

    Omega = mat_sub(SU_k_pinv, transpose(SU_k))
    omega_norm = spectral_norm(Omega)
    expected_omega_norm = max(abs(1.0 / s - s) for s in sig_SU)
    lemma1_eq26_err = abs(omega_norm - expected_omega_norm)

    # 3. Compare Subspace Sampling (Algorithm 1 & 2) vs Naive Column-Norm Sampling
    # Under column-norm sampling, columns 6 and 7 have tiny norm (4.0 vs 2500/6 ~ 416.7),
    # so top-4 norm columns {0,1,2,3} completely miss singular direction 2!
    col_norms_sq = [sum(A[i][j] ** 2 for i in range(m)) for j in range(n)]
    naive_cols = sorted(range(n), key=lambda j: -col_norms_sq[j])[:4]
    C_naive = [[A[i][j] for j in naive_cols] for i in range(m)]
    CX_naive = matmul(C_naive, matmul(pinv(C_naive), A))
    naive_rel_err = frob_norm(mat_sub(A, CX_naive)) / opt_err_f

    # Under subspace leverage sampling p_col, columns 6 and 7 each have p_j = 0.25 (3x higher than 0..5!)
    subspace_cols = [0, 1, 6, 7]
    c_sub = len(subspace_cols)
    C_sub = [
        [A[i][j] / math.sqrt(c_sub * p_col[j]) for j in subspace_cols]
        for i in range(m)
    ]
    CX_sub = matmul(C_sub, matmul(pinv(C_sub), A))
    cx_rel_err = frob_norm(mat_sub(A, CX_sub)) / opt_err_f

    # Algorithm 2 CUR decomposition: R = D_R S_R^T A, W = D_R S_R^T C, U = W^+
    U_C, sig_C, _ = thin_svd(C_sub)
    c_rank = len(sig_C)
    p_row_C = [sum(U_C[i][r] ** 2 for r in range(c_rank)) / c_rank for i in range(m)]
    cur_rows = [0, 1, 2, 3, 5, 7]
    r_cur = len(cur_rows)
    R_cur = [
        [A[i][j] / math.sqrt(r_cur * p_row_C[i]) for j in range(n)]
        for i in cur_rows
    ]
    W_cur = [
        [C_sub[i][j] / math.sqrt(r_cur * p_row_C[i]) for j in range(c_sub)]
        for i in cur_rows
    ]
    U_cur = pinv(W_cur)
    CUR = matmul(C_sub, matmul(U_cur, R_cur))
    cur_rel_err = frob_norm(mat_sub(A, CUR)) / opt_err_f

    # Exact rank-k recovery when A = A_k
    C_exact = [[A_k[i][j] / math.sqrt(c_sub * p_col[j]) for j in subspace_cols] for i in range(m)]
    R_exact = [[A_k[i][j] / math.sqrt(r_cur * p_row_C[i]) for j in range(n)] for i in cur_rows]
    W_exact = [[C_exact[i][j] / math.sqrt(r_cur * p_row_C[i]) for j in range(c_sub)] for i in cur_rows]
    CUR_exact = matmul(C_exact, matmul(pinv(W_exact), R_exact))
    exact_rank_k_err = frob_norm(mat_sub(A_k, CUR_exact))

    ok = (
        prob_sum_err < 1e-14
        and lemma1_eq27_err < 1e-12
        and lemma1_eq26_err < 1e-13
        and cx_rel_err <= 1.15
        and cur_rel_err <= 1.35
        and naive_rel_err > 15.0
        and exact_rank_k_err < 1e-11
    )
    if not ok:
        print(
            f"Verification failed: prob={prob_sum_err}, eq27={lemma1_eq27_err}, "
            f"eq26={lemma1_eq26_err}, cx={cx_rel_err}, cur={cur_rel_err}, "
            f"naive={naive_rel_err}, exact={exact_rank_k_err}",
            file=sys.stderr,
        )
        sys.exit(1)

    print(
        f"[PASS] Round 332 Relative-Error CUR Matrix Decomposition: "
        f"prob_sum_err={prob_sum_err:.2e}, lemma1_eq27_err={lemma1_eq27_err:.2e}, "
        f"lemma1_eq26_err={lemma1_eq26_err:.2e}, cx_rel_err={cx_rel_err:.4f}, "
        f"cur_rel_err={cur_rel_err:.4f}, naive_colnorm_rel_err={naive_rel_err:.2f}, "
        f"exact_rank_k_err={exact_rank_k_err:.2e}"
    )


if __name__ == "__main__":
    main()
