#!/usr/bin/env python3
"""Boundary and verification script for Round 339:
Soft-Impute: Spectral Regularization Algorithms for Learning Large Incomplete Matrices
(Mazumder, Hastie, & Tibshirani, JMLR 2010, 11:2287-2322).
"""

import math
import sys


def matmul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][r] * B[r][j] for r in range(k)) for j in range(n)] for i in range(m)]


def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def frob_sq(A):
    return sum(x * x for row in A for x in row)


def thin_svd(A):
    """Exact thin SVD A = U diag(sigmas) V^T for m x n matrix A (m >= n)."""
    m, n = len(A), len(A[0])
    ATA = matmul(transpose(A), A)
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    G = [row[:] for row in ATA]
    for _ in range(80):
        p, q = 0, 1
        mx = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(G[i][j]) > mx:
                    mx = abs(G[i][j])
                    p, q = i, j
        if mx < 1e-15:
            break
        phi = (G[q][q] - G[p][p]) / (2.0 * G[p][q])
        t = 1.0 / (abs(phi) + math.sqrt(phi * phi + 1.0))
        if phi < 0:
            t = -t
        c = 1.0 / math.sqrt(1.0 + t * t)
        s = t * c
        tau = s / (1.0 + c)
        h = t * G[p][q]
        G[p][p] -= h
        G[q][q] += h
        G[p][q] = G[q][p] = 0.0
        for r in range(n):
            if r != p and r != q:
                grp, grq = G[r][p], G[r][q]
                G[r][p] = G[p][r] = grp - s * (grq + tau * grp)
                G[r][q] = G[q][r] = grq + s * (grp - tau * grq)
        for r in range(n):
            vrp, vrq = V[r][p], V[r][q]
            V[r][p] = vrp - s * (vrq + tau * vrp)
            V[r][q] = vrq + s * (vrp - tau * vrq)
    cols = []
    for j in range(n):
        vj = [V[i][j] for i in range(n)]
        Avj = [sum(A[i][r] * vj[r] for r in range(n)) for i in range(m)]
        sig = math.sqrt(sum(x * x for x in Avj))
        cols.append((sig, vj, Avj))
    cols.sort(key=lambda item: item[0], reverse=True)
    sigmas = [c[0] for c in cols]
    V_sorted = [[cols[j][1][i] for j in range(n)] for i in range(n)]
    U_cols = []
    for j in range(n):
        sig, _, Avj = cols[j]
        if sig > 1e-13:
            U_cols.append([x / sig for x in Avj])
        else:
            for cand_idx in range(m):
                u = [1.0 if i == cand_idx else 0.0 for i in range(m)]
                for prev in U_cols:
                    dot = sum(u[i] * prev[i] for i in range(m))
                    u = [u[i] - dot * prev[i] for i in range(m)]
                nrm = math.sqrt(sum(x * x for x in u))
                if nrm > 1e-7:
                    U_cols.append([x / nrm for x in u])
                    break
    U_sorted = [[U_cols[j][i] for j in range(n)] for i in range(m)]
    return U_sorted, sigmas, V_sorted


def soft_threshold_svd(W, lam):
    """Lemma 1 (Equation 9, p. 2291): S_lam(W) = U D_lam V^T."""
    m, n = len(W), len(W[0])
    U, sigmas, V = thin_svd(W)
    d_lam = [max(0.0, s - lam) for s in sigmas]
    Z = [
        [sum(U[i][r] * d_lam[r] * V[j][r] for r in range(n)) for j in range(n)]
        for i in range(m)
    ]
    nuc = sum(d_lam)
    return Z, nuc, U, d_lam, V


def nuclear_norm(Z):
    _, sigmas, _ = thin_svd(Z)
    return sum(sigmas)


def proj_omega(M, omega_set):
    m, n = len(M), len(M[0])
    return [[M[i][j] if (i, j) in omega_set else 0.0 for j in range(n)] for i in range(m)]


def proj_omega_perp(M, omega_set):
    m, n = len(M), len(M[0])
    return [[0.0 if (i, j) in omega_set else M[i][j] for j in range(n)] for i in range(m)]


def mat_add(A, B, scale_b=1.0):
    return [[A[i][j] + scale_b * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def f_lambda(Z, X, omega_set, lam):
    """Equation 10 (p. 2292): f_lam(Z) = 0.5 ||P_Omega(X) - P_Omega(Z)||_F^2 + lam ||Z||_*."""
    diff = proj_omega(mat_add(X, Z, -1.0), omega_set)
    return 0.5 * frob_sq(diff) + lam * nuclear_norm(Z)


def Q_surrogate(Z, Z_tilde, X, omega_set, lam):
    """Equation 11 (p. 2292): Q_lam(Z | Z_tilde) = 0.5 ||P_Omega(X) + P_Omega^perp(Z_tilde) - Z||_F^2 + lam ||Z||_*."""
    W = mat_add(proj_omega(X, omega_set), proj_omega_perp(Z_tilde, omega_set), 1.0)
    diff = mat_add(W, Z, -1.0)
    return 0.5 * frob_sq(diff) + lam * nuclear_norm(Z)


def main():
    m, n = 5, 4
    # Construct low-rank + noise matrix X and observed index set Omega
    X = [
        [2.5, 1.8, -0.9, 1.2],
        [1.9, 1.4, -0.7, 0.9],
        [-1.1, -0.8, 0.4, -0.5],
        [3.0, 2.2, -1.1, 1.5],
        [0.8, 0.6, -0.3, 0.4],
    ]
    omega_set = {
        (0, 0), (0, 1), (0, 3),
        (1, 0), (1, 1), (1, 2),
        (2, 1), (2, 2), (2, 3),
        (3, 0), (3, 2), (3, 3),
        (4, 0), (4, 1), (4, 2), (4, 3),
    }
    lam = 0.6

    # 1. Verify Lemma 3 (Non-expansiveness of S_lam, p. 2293):
    # ||S_lam(W_1) - S_lam(W_2)||_F^2 <= ||W_1 - W_2||_F^2
    W1 = proj_omega(X, omega_set)
    W2 = X
    Z1, _, _, _, _ = soft_threshold_svd(W1, lam)
    Z2, _, _, _, _ = soft_threshold_svd(W2, lam)
    lhs_lemma3 = frob_sq(mat_add(Z1, Z2, -1.0))
    rhs_lemma3 = frob_sq(mat_add(W1, W2, -1.0))

    # 2. Verify Lemma 6 & Theorem 3 (Variational Nuclear Norm & MMMF Equivalence, pp. 2300-2301, 2318):
    # ||Z||_* == min_{Z = U V^T} 0.5 (||U||_F^2 + ||V||_F^2), attained at U = L Sigma^{1/2}, V = R Sigma^{1/2}
    Z_test, nuc_test, U_t, d_t, V_t = soft_threshold_svd(W2, lam)
    U_mmmf = [[U_t[i][r] * math.sqrt(d_t[r]) for r in range(n)] for i in range(m)]
    V_mmmf = [[V_t[j][r] * math.sqrt(d_t[r]) for r in range(n)] for j in range(n)]
    mmmf_penalty = 0.5 * (frob_sq(U_mmmf) + frob_sq(V_mmmf))
    lemma6_err = abs(nuc_test - mmmf_penalty)

    # 3. Run Algorithm 1 (SOFT-IMPUTE, p. 2292) and verify Lemma 2, Lemma 4, Theorem 1, Theorem 2, and Eq. 22
    Z_seq = [[[0.0] * n for _ in range(m)]]
    max_eq13_err = 0.0
    max_eq22_err = 0.0
    monotone_f = True
    for k in range(120):
        Z_k = Z_seq[-1]
        # Verify Sparse + Low-Rank identity (Equation 22, p. 2295):
        # P_Omega(X) + P_Omega^perp(Z_k) == (P_Omega(X) - P_Omega(Z_k)) + Z_k
        W_k = mat_add(proj_omega(X, omega_set), proj_omega_perp(Z_k, omega_set), 1.0)
        W_sparse_lr = mat_add(proj_omega(mat_add(X, Z_k, -1.0), omega_set), Z_k, 1.0)
        max_eq22_err = max(max_eq22_err, math.sqrt(frob_sq(mat_add(W_k, W_sparse_lr, -1.0))))

        Z_next, _, _, _, _ = soft_threshold_svd(W_k, lam)
        # Verify Lemma 2 Equation 13 (p. 2293):
        # Q_lam(Z_{k+1} | Z_k) == f_lam(Z_{k+1}) + 0.5 ||P_Omega^perp(Z_k - Z_{k+1})||_F^2
        q_val = Q_surrogate(Z_next, Z_k, X, omega_set, lam)
        f_next = f_lambda(Z_next, X, omega_set, lam)
        f_curr = f_lambda(Z_k, X, omega_set, lam)
        perp_diff_sq = frob_sq(proj_omega_perp(mat_add(Z_k, Z_next, -1.0), omega_set))
        max_eq13_err = max(max_eq13_err, abs(q_val - (f_next + 0.5 * perp_diff_sq)))
        if not (f_next <= q_val + 1e-13 and q_val <= f_curr + 1e-13):
            monotone_f = False
        Z_seq.append(Z_next)

    Z_inf = Z_seq[-1]
    f_inf = f_lambda(Z_inf, X, omega_set, lam)

    # Verify Lemma 4 (Eq. 15): ||Z^{k+1} - Z^k||_F^2 <= ||Z^k - Z^{k-1}||_F^2
    step_diffs = [frob_sq(mat_add(Z_seq[k + 1], Z_seq[k], -1.0)) for k in range(40)]
    lemma4_holds = all(step_diffs[k + 1] <= step_diffs[k] + 1e-14 for k in range(len(step_diffs) - 1))

    # Verify Theorem 1 (Eq. 19): ||Z^inf - Z^k||_F^2 <= ||Z^inf - Z^{k-1}||_F^2
    dist_to_inf = [frob_sq(mat_add(Z_inf, Z_seq[k], -1.0)) for k in range(40)]
    thm1_fejer_holds = all(dist_to_inf[k + 1] <= dist_to_inf[k] + 1e-14 for k in range(len(dist_to_inf) - 1))

    # Verify Theorem 2 (Eq. 20, p. 2295): f_lam(Z^k) - f_lam(Z^inf) <= 2 ||Z^0 - Z^inf||_F^2 / (k + 1)
    d0_sq = dist_to_inf[0]
    thm2_rate_holds = all(
        (f_lambda(Z_seq[k], X, omega_set, lam) - f_inf) <= (2.0 * d0_sq) / (k + 1) + 1e-13
        for k in range(1, 40)
    )

    ok = (
        lhs_lemma3 <= rhs_lemma3 + 1e-14
        and lemma6_err < 1e-14
        and max_eq13_err < 1e-13
        and max_eq22_err < 1e-15
        and monotone_f
        and lemma4_holds
        and thm1_fejer_holds
        and thm2_rate_holds
    )
    if not ok:
        print("Verification failed!", file=sys.stderr)
        sys.exit(1)

    print(
        f"[PASS] Round 339 Soft-Impute (Mazumder, Hastie, & Tibshirani 2010): "
        f"lemma6_err={lemma6_err:.2e}, max_eq13_err={max_eq13_err:.2e}, "
        f"max_eq22_err={max_eq22_err:.2e}, f_inf={f_inf:.6f}, final_step_diff={step_diffs[-1]:.2e}"
    )


if __name__ == "__main__":
    main()
