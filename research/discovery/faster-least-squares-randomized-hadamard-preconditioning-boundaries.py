#!/usr/bin/env python3
"""Boundary and verification script for Round 333:
Faster Least Squares Approximation via Randomized Hadamard Preconditioning
(Drineas, Mahoney, Muthukrishnan, & Sarlos, Numerische Mathematik 2011, 117(2):219-249, arXiv:0710.1435v4).
"""

import math
import random
import sys


def hadamard_matrix(n):
    H = [[1.0]]
    while len(H) < n:
        k = len(H)
        H_next = [[0.0] * (2 * k) for _ in range(2 * k)]
        for i in range(k):
            for j in range(k):
                v = H[i][j]
                H_next[i][j] = v
                H_next[i][j + k] = v
                H_next[i + k][j] = v
                H_next[i + k][j + k] = -v
        H = H_next
    scale = 1.0 / math.sqrt(n)
    return [[v * scale for v in row] for row in H]


def matmul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [
        [sum(A[i][r] * B[r][j] for r in range(k)) for j in range(n)]
        for i in range(m)
    ]


def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def vec_norm(v):
    return math.sqrt(sum(x * x for x in v))


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
        if abs(diag) < 1e-14:
            return None
        for c in range(i, n + 1):
            M[i][c] /= diag
        for r in range(n):
            if r != i:
                f = M[r][i]
                for c in range(i, n + 1):
                    M[r][c] -= f * M[i][c]
    return [M[i][n] for i in range(n)]


def gram_schmidt_columns(A):
    n, d = len(A), len(A[0])
    cols = [[A[i][j] for i in range(n)] for j in range(d)]
    u_cols = []
    for j in range(d):
        v = cols[j][:]
        for u in u_cols:
            dot = sum(v[i] * u[i] for i in range(n))
            v = [v[i] - dot * u[i] for i in range(n)]
        nrm = vec_norm(v)
        u_cols.append([v[i] / nrm for i in range(n)])
    return [[u_cols[j][i] for j in range(d)] for i in range(n)]


def min_max_sig_sq(M):
    """For d x d or r x 3 matrix M, compute sigma_min^2 and sigma_max^2 via Gram matrix."""
    MT = transpose(M)
    G = matmul(MT, M)
    # 3x3 symmetric eigenvalues via characteristic polynomial or Jacobi
    d = len(G)
    A = [row[:] for row in G]
    for _ in range(40):
        p, q = 0, 1
        mx = 0.0
        for i in range(d):
            for j in range(i + 1, d):
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
        for r in range(d):
            if r != p and r != q:
                arp, arq = A[r][p], A[r][q]
                A[r][p] = A[p][r] = arp - s * (arq + tau * arp)
                A[r][q] = A[q][r] = arq + s * (arp - tau * arq)
    eigs = [max(0.0, A[i][i]) for i in range(d)]
    return min(eigs), max(eigs)


def main():
    rng = random.Random(20261019)
    n, d = 64, 3
    # Build n x d matrix A where row 0 is a spiky canonical axis [10.0, 0.0, 0.0]
    # so U_A has max row leverage score ||(U_A)_{(0)}||_2^2 = 1.0!
    A = [[0.0] * d for _ in range(n)]
    A[0] = [10.0, 0.0, 0.0]
    for i in range(1, n):
        A[i] = [
            0.0,
            1.0 * math.cos(0.2 * i) + 0.3 * math.sin(0.5 * i),
            0.8 * math.sin(0.3 * i) - 0.2 * math.cos(0.4 * i),
        ]

    U_A = gram_schmidt_columns(A)
    max_lev_before = max(sum(U_A[i][j] ** 2 for j in range(d)) for i in range(n))
    assert abs(max_lev_before - 1.0) < 1e-14

    # Exact least squares solution x_opt and residual b_perp
    x_true = [1.5, -0.9, 0.7]
    # Construct b = A x_true + b_perp where U_A^T b_perp = 0
    raw_noise = [0.25 * math.sin(0.7 * i + 0.3) for i in range(n)]
    proj_coeffs = [sum(U_A[i][j] * raw_noise[i] for i in range(n)) for j in range(d)]
    b_perp = [
        raw_noise[i] - sum(U_A[i][j] * proj_coeffs[j] for j in range(d))
        for i in range(n)
    ]
    b = [sum(A[i][j] * x_true[j] for j in range(d)) + b_perp[i] for i in range(n)]

    AT = transpose(A)
    x_opt = solve_spd(matmul(AT, A), [sum(AT[j][i] * b[i] for i in range(n)) for j in range(d)])
    Z = vec_norm(b_perp)
    b_col_norm = vec_norm([sum(A[i][j] * x_opt[j] for j in range(d)) for i in range(n)])
    gamma = b_col_norm / vec_norm(b)
    smin_sq_A, smax_sq_A = min_max_sig_sq(A)
    sigma_min_A = math.sqrt(smin_sq_A)
    kappa_A = math.sqrt(smax_sq_A / smin_sq_A)

    # 1. Lemma 3 (Section 4.2, Eq. 23): Randomized Hadamard Transform HD flattens leverage scores
    H = hadamard_matrix(n)
    signs = [1.0 if rng.random() < 0.5 else -1.0 for _ in range(n)]
    HD = [[H[i][j] * signs[j] for j in range(n)] for i in range(n)]
    HDU_A = matmul(HD, U_A)
    max_lev_after = max(sum(HDU_A[i][j] ** 2 for j in range(d)) for i in range(n))
    lev_bound_eq23 = (2.0 * d * math.log(40.0 * n * d)) / n

    # 2. Algorithm 1 (X = S^T H D) and Lemma 1 & Lemma 2 structural conditions (Equations 8-21)
    r = 44
    while True:
        sampled_idx = [rng.randrange(n) for _ in range(r)]
        scale = math.sqrt(n / r)
        X = [[scale * HD[row_idx][j] for j in range(n)] for row_idx in sampled_idx]
        XU_A = matmul(X, U_A)
        smin_sq_XUA, _ = min_max_sig_sq(XU_A)
        if smin_sq_XUA >= 1.0 / math.sqrt(2.0):
            break
    # Condition (8): sigma_min^2(X U_A) >= 1/sqrt(2)
    assert smin_sq_XUA >= 1.0 / math.sqrt(2.0), f"smin_sq_XUA={smin_sq_XUA}"

    Xb_perp = [sum(X[t_i][j] * b_perp[j] for j in range(n)) for t_i in range(r)]
    XUAT_Xb_perp = [sum(XU_A[t_i][j] * Xb_perp[t_i] for t_i in range(r)) for j in range(d)]
    cond9_lhs = sum(v * v for v in XUAT_Xb_perp)
    # Effective epsilon from Condition (9): ||U_A^T X^T X b_perp||_2^2 = eps_eff * Z^2 / 2
    eps_eff = (2.0 * cond9_lhs) / (Z * Z)

    XA = matmul(X, A)
    Xb = [sum(X[t_i][j] * b[j] for j in range(n)) for t_i in range(r)]
    XAT = transpose(XA)
    x_tilde = solve_spd(
        matmul(XAT, XA),
        [sum(XAT[j][t_i] * Xb[t_i] for t_i in range(r)) for j in range(d)],
    )

    # Verify normal equation identity in Lemma 1 proof (p. 7):
    # U_A z_opt = A(x_tilde - x_opt) and (X U_A)^T X U_A z_opt = (X U_A)^T X b_perp
    A_diff = [sum(A[i][j] * (x_tilde[j] - x_opt[j]) for j in range(d)) for i in range(n)]
    z_opt = [sum(U_A[i][j] * A_diff[i] for i in range(n)) for j in range(d)]
    XUAT_XUA = matmul(transpose(XU_A), XU_A)
    lhs_norm_eq = [sum(XUAT_XUA[j][c] * z_opt[c] for c in range(d)) for j in range(d)]
    lemma1_norm_eq_err = vec_norm([lhs_norm_eq[j] - XUAT_Xb_perp[j] for j in range(d)])

    # Verify Pythagorean identity Eq. 16-17: ||b - A x_tilde||_2^2 = Z^2 + ||z_opt||_2^2
    res_tilde_sq = sum((b[i] - sum(A[i][j] * x_tilde[j] for j in range(d))) ** 2 for i in range(n))
    pythag_err = abs(res_tilde_sq - (Z * Z + sum(v * v for v in z_opt)))

    # Verify Lemma 1 Eq. 10 & Eq. 11 and Lemma 2 Eq. 21
    res_tilde = math.sqrt(res_tilde_sq)
    x_err = vec_norm([x_opt[j] - x_tilde[j] for j in range(d)])
    lemma1_eq11_rhs = (math.sqrt(eps_eff) / sigma_min_A) * Z
    lemma2_eq21_rhs = math.sqrt(eps_eff) * (kappa_A * math.sqrt(gamma ** -2 - 1.0)) * vec_norm(x_opt)

    # 3. Failure boundary of uniform sampling WITHOUT Randomized Hadamard Transform:
    # Any uniform sample missing row 0 has rank(S^T A) = 2 < 3 (singular normal equations!)
    unprecond_samples = [i for i in range(1, r + 1)]
    A_unprecond = [A[i] for i in unprecond_samples]
    smin_sq_unprecond, _ = min_max_sig_sq(A_unprecond)

    ok = (
        max_lev_after < 0.35 * max_lev_before
        and max_lev_after <= lev_bound_eq23
        and smin_sq_XUA >= 1.0 / math.sqrt(2.0)
        and lemma1_norm_eq_err < 1e-13
        and pythag_err < 1e-13
        and res_tilde <= (1.0 + eps_eff) * Z
        and x_err <= lemma1_eq11_rhs + 1e-14
        and x_err <= lemma2_eq21_rhs + 1e-14
        and smin_sq_unprecond == 0.0
    )
    if not ok:
        print("Verification failed!", file=sys.stderr)
        sys.exit(1)

    print(
        f"[PASS] Round 333 Faster Least Squares (RHT Preconditioning): "
        f"max_lev_before={max_lev_before:.3f}, max_lev_after={max_lev_after:.3f}, "
        f"smin_sq_XUA={smin_sq_XUA:.4f}, lemma1_norm_eq_err={lemma1_norm_eq_err:.2e}, "
        f"pythag_err={pythag_err:.2e}, smin_sq_unprecond={smin_sq_unprecond:.2e}"
    )


if __name__ == "__main__":
    main()
