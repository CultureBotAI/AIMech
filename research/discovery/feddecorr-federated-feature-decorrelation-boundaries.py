#!/usr/bin/env python3
"""Constructed boundary verification for FedDecorr (Shi et al., ICLR 2023, arXiv:2210.00226)."""

import math
import random

def jacobi_eigenvalues_symmetric(A, tol=1e-12, max_iter=500):
    n = len(A)
    M = [row[:] for row in A]
    for _ in range(max_iter):
        max_val = 0.0
        p, q = 0, 1
        for i in range(n):
            for j in range(i + 1, n):
                if abs(M[i][j]) > max_val:
                    max_val = abs(M[i][j])
                    p, q = i, j
        if max_val < tol:
            break
        if abs(M[p][p] - M[q][q]) < 1e-15:
            theta = math.pi / 4.0
        else:
            theta = 0.5 * math.atan2(2.0 * M[p][q], M[p][p] - M[q][q])
        c = math.cos(theta)
        s = math.sin(theta)
        for i in range(n):
            if i != p and i != q:
                mip = M[i][p]
                miq = M[i][q]
                M[i][p] = M[p][i] = c * mip + s * miq
                M[i][q] = M[q][i] = -s * mip + c * miq
        mpp, mqq, mpq = M[p][p], M[q][q], M[p][q]
        M[p][p] = c * c * mpp + 2.0 * s * c * mpq + s * s * mqq
        M[q][q] = s * s * mpp - 2.0 * s * c * mpq + c * c * mqq
        M[p][q] = M[q][p] = 0.0
    return sorted([max(0.0, M[i][i]) for i in range(n)], reverse=True)

def compute_correlation_matrix(Z):
    N = len(Z)
    d = len(Z[0])
    means = [sum(Z[i][j] for i in range(N)) / N for j in range(d)]
    stds = [math.sqrt(sum((Z[i][j] - means[j]) ** 2 for i in range(N)) / N) for j in range(d)]
    Z_hat = [[(Z[i][j] - means[j]) / stds[j] for j in range(d)] for i in range(N)]
    K = [[sum(Z_hat[i][a] * Z_hat[i][b] for i in range(N)) / N for b in range(d)] for a in range(d)]
    return K, Z_hat, means, stds

def main():
    rng = random.Random(20261019)
    N = 24
    d = 4
    # Construct rank-deficient / highly correlated representations (simulating dimensional collapse)
    Z = []
    for _ in range(N):
        u1 = rng.gauss(0.0, 1.0)
        u2 = rng.gauss(0.0, 0.25)
        Z.append([
            u1 + 0.05 * rng.gauss(0.0, 1.0),
            0.92 * u1 + 0.15 * u2 + 0.05 * rng.gauss(0.0, 1.0),
            -0.88 * u1 + 0.20 * u2 + 0.05 * rng.gauss(0.0, 1.0),
            0.50 * u1 + 0.80 * u2 + 0.05 * rng.gauss(0.0, 1.0),
        ])

    # 1. Verify Proposition 1 (Eq. 7 & Eq. 48-51): sum_{i=1}^d (lambda_i - mean(lambda))^2 == ||K||_F^2 - d
    K_init, _, _, _ = compute_correlation_matrix(Z)
    lambdas_init = jacobi_eigenvalues_symmetric(K_init)
    mean_lam = sum(lambdas_init) / d
    assert abs(sum(lambdas_init) - d) < 1e-10, f"tr(K) must equal d={d}, got {sum(lambdas_init)}"
    sv_var_init = sum((lam - mean_lam) ** 2 for lam in lambdas_init)
    frob_sq_init = sum(K_init[a][b] ** 2 for a in range(d) for b in range(d))
    assert abs(sv_var_init - (frob_sq_init - d)) < 1e-10, f"{sv_var_init} != {frob_sq_init - d}"

    # 2. Minimize L_FedDecorr(Z) = (1/d^2) ||K||_F^2 via gradient descent on Z and verify tail singular values rise
    lr = 0.35
    for _ in range(120):
        K, Z_hat, _, stds = compute_correlation_matrix(Z)
        # Gradient of (1/d^2) ||K||_F^2 w.r.t. Z_hat is (4 / (N * d^2)) * Z_hat * (K - diag(K))
        for i in range(N):
            for j in range(d):
                grad_zh = sum(Z_hat[i][b] * (K[j][b] if j != b else 0.0) for b in range(d)) * (4.0 / (N * d * d))
                Z[i][j] -= lr * grad_zh / stds[j]

    K_final, _, _, _ = compute_correlation_matrix(Z)
    lambdas_final = jacobi_eigenvalues_symmetric(K_final)
    sv_var_final = sum((lam - 1.0) ** 2 for lam in lambdas_final)
    frob_sq_final = sum(K_final[a][b] ** 2 for a in range(d) for b in range(d))
    assert abs(sv_var_final - (frob_sq_final - d)) < 1e-10
    assert sv_var_final < 0.05 * sv_var_init, f"Variance did not decrease: {sv_var_init} -> {sv_var_final}"
    assert lambdas_final[-1] > 10.0 * lambdas_init[-1], f"Tail singular value did not expand: {lambdas_init[-1]} -> {lambdas_final[-1]}"

    print(
        f"[PASS] Round 459 FedDecorr verified: Prop1_diff={abs(sv_var_init - (frob_sq_init - d)):.2e}, "
        f"sv_var={sv_var_init:.4f}->{sv_var_final:.4f}, min_sv={lambdas_init[-1]:.4f}->{lambdas_final[-1]:.4f}"
    )

if __name__ == "__main__":
    main()
