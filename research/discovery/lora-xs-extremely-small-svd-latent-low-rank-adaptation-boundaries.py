#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 676: LoRA-XS (Balazy et al., ECAI 2025)."""

import math
import random


def matmul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)] for i in range(m)]


def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def frob_inner(X, Y):
    return sum(X[i][j] * Y[i][j] for i in range(len(X)) for j in range(len(X[0])))


def frob_diff(X, Y):
    return math.sqrt(sum((X[i][j] - Y[i][j]) ** 2 for i in range(len(X)) for j in range(len(X[0]))))


def random_orthonormal_cols(m, r, rng):
    cols = []
    for _ in range(r):
        v = [rng.gauss(0.0, 1.0) for _ in range(m)]
        for u in cols:
            dot = sum(v[i] * u[i] for i in range(m))
            v = [v[i] - dot * u[i] for i in range(m)]
        norm = math.sqrt(sum(x * x for x in v))
        cols.append([x / norm for x in v])
    return [[cols[j][i] for j in range(r)] for i in range(m)]


def proj_subspace(U_r, V_r, X):
    # p_{U_r, V_r}(X) = U_r (U_r^T X V_r) V_r^T
    core = matmul(matmul(transpose(U_r), X), V_r)
    return matmul(matmul(U_r, core), transpose(V_r))


def main():
    rng = random.Random(676)

    # 1. Verify Appendix C parameter-count decoupling from hidden dimension n (Equations 7-12, p. 11):
    # RoBERTa-large example: L=24, q=2, n=1024, r=16
    L, q, n, r = 24, 2, 1024, 16
    p_lora = L * q * r * 2 * n
    p_vera = L * q * (n + r)
    p_lora_xs = L * q * (r * r)
    assert p_lora == 1572864, f"Expected 1572864, got {p_lora}"
    assert p_vera == 49920, f"Expected 49920, got {p_vera}"
    assert p_lora_xs == 12288, f"Expected 12288, got {p_lora_xs}"
    assert p_lora // p_lora_xs == (2 * n) // r == 128

    # 2. Verify Appendix B orthogonal projection onto r^2-dimensional subspace S^r_{U_r, V_r} (Eq. 5-6, p. 10):
    m_dim, n_dim, r_dim = 10, 10, 3
    U_r = random_orthonormal_cols(m_dim, r_dim, rng)
    V_r = random_orthonormal_cols(n_dim, r_dim, rng)
    X = [[rng.gauss(0.0, 1.0) for _ in range(n_dim)] for _ in range(m_dim)]
    Y = [[rng.gauss(0.0, 1.0) for _ in range(n_dim)] for _ in range(m_dim)]

    pX = proj_subspace(U_r, V_r, X)
    ppX = proj_subspace(U_r, V_r, pX)
    idemp_err = frob_diff(pX, ppX)
    assert idemp_err < 1e-13, f"Projection idempotence p^2 == p failed: {idemp_err}"

    pY = proj_subspace(U_r, V_r, Y)
    lhs = frob_inner(pX, Y)
    rhs = frob_inner(X, pY)
    adj_err = abs(lhs - rhs)
    assert adj_err < 1e-13, f"Self-adjointness <p(X), Y> == <X, p(Y)> failed: {adj_err}"

    # 3. Verify Theorem 1 (Section 3.2, p. 4):
    # Truncated SVD (U_r, V_r) of mean gradient G minimizes d(G, S^r_{A, B}) over all r-orthonormal (A, B).
    U_full = random_orthonormal_cols(m_dim, m_dim, rng)
    V_full = random_orthonormal_cols(n_dim, n_dim, rng)
    sigmas = [15.0, 10.0, 6.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.01]
    G = [[0.0 for _ in range(n_dim)] for _ in range(m_dim)]
    for k, s in enumerate(sigmas):
        for i in range(m_dim):
            for j in range(n_dim):
                G[i][j] += s * U_full[i][k] * V_full[j][k]

    U_svd = [[U_full[i][k] for k in range(r_dim)] for i in range(m_dim)]
    V_svd = [[V_full[j][k] for k in range(r_dim)] for j in range(n_dim)]
    pG_svd = proj_subspace(U_svd, V_svd, G)
    dist_svd = frob_diff(G, pG_svd)
    expected_tail = math.sqrt(sum(s * s for s in sigmas[r_dim:]))
    assert abs(dist_svd - expected_tail) < 1e-12

    # Compare against bottom-r singular vectors (Appendix H) and random orthonormal subspace (Appendix G)
    U_bot = [[U_full[i][m_dim - r_dim + k] for k in range(r_dim)] for i in range(m_dim)]
    V_bot = [[V_full[j][n_dim - r_dim + k] for k in range(r_dim)] for j in range(n_dim)]
    dist_bot = frob_diff(G, proj_subspace(U_bot, V_bot, G))
    dist_rand = frob_diff(G, proj_subspace(U_r, V_r, G))
    assert dist_svd < dist_rand < dist_bot, (
        f"Expected dist_svd={dist_svd} < dist_rand={dist_rand} < dist_bot={dist_bot}"
    )

    print(
        f"[PASS] Round 676 LoRA-XS (Balazy et al., ECAI 2025): "
        f"param_ratio_lora_vs_xs={p_lora // p_lora_xs}x, idemp_err={idemp_err:.2e}, "
        f"dist_svd={dist_svd:.4f}<dist_rand={dist_rand:.4f}<dist_bot={dist_bot:.4f}"
    )


if __name__ == "__main__":
    main()
