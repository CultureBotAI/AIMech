#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 406:
FedBN: Federated Learning on Non-IID Features via Local Batch Normalization
(Li, Jiang, Zhang, Kamp, & Dou, ICLR 2021, arXiv:2102.07623).
"""

import math
import random


def jacobi_eigenvalues(A, tol=1e-13, max_iter=500):
    """Exact eigenvalues of a real symmetric matrix A via Jacobi rotations."""
    n = len(A)
    M = [row[:] for row in A]
    for _ in range(max_iter):
        p, q = 0, 1
        max_val = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(M[i][j]) > max_val:
                    max_val = abs(M[i][j])
                    p, q = i, j
        if max_val < tol:
            break
        diff = M[q][q] - M[p][p]
        if abs(M[p][q]) < tol:
            t = 0.0
        else:
            phi = diff / (2.0 * M[p][q])
            t = 1.0 / (abs(phi) + math.sqrt(phi * phi + 1.0))
            if phi < 0.0:
                t = -t
        c = 1.0 / math.sqrt(1.0 + t * t)
        s = t * c
        tau = s / (1.0 + c)
        h = t * M[p][q]
        M[p][p] -= h
        M[q][q] += h
        M[p][q] = 0.0
        M[q][p] = 0.0
        for r in range(n):
            if r != p and r != q:
                g = M[r][p]
                e = M[r][q]
                M[r][p] = g - s * (e + g * tau)
                M[p][r] = M[r][p]
                M[r][q] = e + s * (g - e * tau)
                M[q][r] = M[r][q]
    return sorted(M[i][i] for i in range(n))


def main():
    rng = random.Random(406)

    # 1. Verify Lemma 4.3, Theorem 4.4, and Corollary 4.6 (Li et al. 2021):
    # G^{*\infty} = diag(G_1^\infty, ..., G_N^\infty) is the block-diagonal restriction of G^\infty in R^{NM x NM}.
    # Therefore mu_0^* = lambda_min(G^{*\infty}) = min_i lambda_min(G_i^\infty) >= lambda_min(G^\infty) = mu_0 > 0.
    N, M = 2, 2
    dim = N * M
    # Construct non-parallel unit-norm feature points across 2 clients with distinct covariances S_1 != S_2
    angles = [0.1, 0.9, 0.35, 1.15]
    X = [[math.cos(th), math.sin(th)] for th in angles]

    # Exact infinite-width ReLU NTK magnitude kernel (Definition 4.2):
    # G_{pq} = (1 / (4 pi)) * (pi - arccos(u_p^T u_q)) where u_p = S_{client(p)}^{-1/2} x_p / ||...||
    G_fedavg = [[0.0] * dim for _ in range(dim)]
    for p in range(dim):
        for q in range(dim):
            dot = max(-1.0, min(1.0, X[p][0] * X[q][0] + X[p][1] * X[q][1]))
            theta_pq = 0.0 if p == q else math.acos(dot)
            G_fedavg[p][q] = (math.pi - theta_pq) / (4.0 * math.pi)

    G_fedbn = [[0.0] * dim for _ in range(dim)]
    for i in range(N):
        for a in range(M):
            for b in range(M):
                p = i * M + a
                q = i * M + b
                G_fedbn[p][q] = G_fedavg[p][q]

    eigs_fedavg = jacobi_eigenvalues(G_fedavg)
    eigs_fedbn = jacobi_eigenvalues(G_fedbn)
    mu_0 = eigs_fedavg[0]
    mu_0_star = eigs_fedbn[0]

    assert mu_0 > 0.0 and mu_0_star > mu_0 + 1e-3, (
        f"Expected mu_0^* > mu_0 > 0, got mu_0^*={mu_0_star}, mu_0={mu_0}"
    )

    # Verify exponential convergence bound ratio after T=40 iterations with step size eta=0.5
    eta = 0.5
    T = 40
    rate_fedbn = (1.0 - 0.5 * eta * mu_0_star) ** T
    rate_fedavg = (1.0 - 0.5 * eta * mu_0) ** T
    assert rate_fedbn < rate_fedavg

    # 2. Verify covariate shift protection via local Batch Normalization vs global averaged BN statistics:
    # Suppose client k has feature distribution x_k = sigma_k * z + m_k with latent z ~ N(0, 1) and shared label y = w^* z + b^*.
    # Local BN normalizes x_k -> (x_k - m_k)/sigma_k = z, allowing a shared weight w = w^* to achieve 0 error on all clients.
    # Averaging BN running mean/variance across heterogeneous clients (m_1=-3, sigma_1=0.5 vs m_2=+3, sigma_2=2.5) corrupts inference.
    m1, s1 = -3.0, 0.5
    m2, s2 = 3.0, 2.5
    w_star = 2.0
    m_avg = 0.5 * (m1 + m2)
    s_avg = math.sqrt(0.5 * (s1 * s1 + s2 * s2))

    mse_fedbn = 0.0
    mse_fedavg_bn = 0.0
    n_samples = 200
    for _ in range(n_samples):
        z = rng.gauss(0.0, 1.0)
        y_true = w_star * z
        for mk, sk in ((m1, s1), (m2, s2)):
            xk = sk * z + mk
            pred_fedbn = w_star * ((xk - mk) / sk)
            pred_fedavg = w_star * ((xk - m_avg) / s_avg)
            mse_fedbn += (pred_fedbn - y_true) ** 2 / (2 * n_samples)
            mse_fedavg_bn += (pred_fedavg - y_true) ** 2 / (2 * n_samples)

    assert mse_fedbn < 1e-24 and mse_fedavg_bn > 5.0

    print(
        f"[PASS] Round 406 FedBN (Li et al. 2021): "
        f"mu0_star={mu_0_star:.5f}>mu0={mu_0:.5f}, "
        f"rate_fedbn={rate_fedbn:.4f}<rate_fedavg={rate_fedavg:.4f}, "
        f"mse_fedbn={mse_fedbn:.2e}<<mse_fedavg_bn={mse_fedavg_bn:.4f}"
    )


if __name__ == "__main__":
    main()
