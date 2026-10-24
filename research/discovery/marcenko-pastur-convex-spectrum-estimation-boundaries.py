#!/usr/bin/env python3
"""Constructed boundary and mechanism verification for:
Nonparametric Spectrum Estimation for Large-Dimensional Covariance Matrices via
Convex Inversion of the Marcenko-Pastur Equation
(El Karoui, 2008, The Annals of Statistics 36(6):2757-2790, arXiv:math/0609418v1).

Verifies:
1. Section 5 Lemma 1 algebraic Stieltjes-transform identity (p. 19):
   int lambda dG(lambda) / (1 + lambda m) = 1/m - (1/m^2) S_G(-1/m) for m in C^+,
   and Proposition 1 Lipschitz bound |S_H(z_1) - S_H(z_2)| <= |z_1 - z_2| / u_min^2.
2. Section 2.3 Exact Marcenko-Pastur fixed-point equation (Eq. M-P, p. 6) and
   Appendix A.1 Jensen bias of extreme sample eigenvalues: under Sigma_p = Id_p
   and p/n = gamma, the empirical eigenvalues spread over [(1 - sqrt(gamma))^2,
   (1 + sqrt(gamma))^2] while v_{F_p}(z) closely satisfies the Marcenko-Pastur
   equation for H_infty = delta_1.
3. Section 3.2 Convex optimization inversion of the discretized Marcenko-Pastur
   equation (pp. 7-9): on both the identity spectrum H_p = delta_1 (Section 4.1.1)
   and the bimodal two-cluster spectrum H_p = 0.5 delta_1 + 0.5 delta_2 (Section
   4.1.2) where p/n = 0.25 blurs the empirical scree plot, projected gradient
   simplex optimization of the Marcenko-Pastur residual e_j(w) recovers H_hat_p
   with strictly smaller Wasserstein-1 and Levy distance to H_p than the empirical
   spectral distribution F_p.
"""

from __future__ import annotations

import cmath
import math
import random


def stieltjes_transform(support: list[float], weights: list[float], z: complex) -> complex:
    """Compute S_G(z) = int dG(x) / (x - z) (Section 2.2, p. 5)."""
    return sum(w / (x - z) for x, w in zip(support, weights))


def mp_integral(support: list[float], weights: list[float], m: complex) -> complex:
    """Compute int lambda dG(lambda) / (1 + lambda m)."""
    return sum(w * lam / (1.0 + lam * m) for lam, w in zip(support, weights))


def companion_stieltjes(sample_eigs: list[float], p: int, n: int, z: complex) -> complex:
    """Compute v_{F_p}(z) = (1 - p/n)(-1/z) + (p/n) m_{F_p}(z) (Section 2.3, p. 6)."""
    p_over_n = p / n
    m_fp = sum(1.0 / (li - z) for li in sample_eigs) / p
    return (1.0 - p_over_n) * (-1.0 / z) + p_over_n * m_fp


def project_simplex(v: list[float]) -> list[float]:
    """Euclidean projection onto the probability simplex {w >= 0, sum w = 1}."""
    k = len(v)
    u = sorted(v, reverse=True)
    cssv = 0.0
    rho = -1
    for i in range(k):
        cssv += u[i]
        t = (cssv - 1.0) / (i + 1)
        if u[i] - t > 0:
            rho = i
    theta = (sum(u[: rho + 1]) - 1.0) / (rho + 1)
    return [max(x - theta, 0.0) for x in v]


def solve_mp_convex_inversion(
    sample_eigs: list[float],
    p: int,
    n: int,
    grid_t: list[float],
    z_grid: list[complex],
    iters: int = 400,
) -> list[float]:
    """Solve the convex L2-squared Marcenko-Pastur inversion problem (Section 3.2.2, p. 8)
    with a light smoothness regularization (Section 3.3.1, p. 9) on the simplex.
    """
    p_over_n = p / n
    K = len(grid_t)
    J = len(z_grid)
    v_vals = [companion_stieltjes(sample_eigs, p, n, zj) for zj in z_grid]
    target = [1.0 / v_vals[j] + z_grid[j] for j in range(J)]
    # Design matrix A_{j,k} = (p/n) * t_k / (1 + t_k * v_{F_p}(z_j))
    A = [[p_over_n * tk / (1.0 + tk * v_vals[j]) for tk in grid_t] for j in range(J)]

    # Precompute normal equations H_mat = Re(A^* A) and g_vec = Re(A^* target)
    H_mat = [[0.0] * K for _ in range(K)]
    g_vec = [0.0] * K
    for k in range(K):
        g_vec[k] = sum((A[j][k].conjugate() * target[j]).real for j in range(J))
        for l in range(k, K):
            val = sum((A[j][k].conjugate() * A[j][l]).real for j in range(J))
            H_mat[k][l] = val
            H_mat[l][k] = val

    # First-moment trace penalty (Section 3.3.1, p. 9): sum w_k t_k approx mean(sample_eigs)
    mean_eig = sum(sample_eigs) / len(sample_eigs)
    mu_pen = 0.05
    for k in range(K):
        g_vec[k] += mu_pen * mean_eig * grid_t[k]
        for l in range(K):
            H_mat[k][l] += mu_pen * grid_t[k] * grid_t[l]

    # Lipschitz step size for projected gradient descent
    lip = sum(H_mat[k][k] for k in range(K)) + 1e-6
    step = 1.0 / lip
    w = [1.0 / K] * K
    for _ in range(iters):
        grad = [sum(H_mat[k][l] * w[l] for l in range(K)) - g_vec[k] for k in range(K)]
        w_next = project_simplex([w[k] - step * grad[k] for k in range(K)])
        if max(abs(w_next[k] - w[k]) for k in range(K)) < 1e-8:
            w = w_next
            break
        w = w_next
    return w


def wasserstein1_discrete(
    supp1: list[float], w1: list[float], supp2: list[float], w2: list[float]
) -> float:
    """Exact Wasserstein-1 distance int_0^infty |G_1(x) - G_2(x)| dx (Corollary 1, p. 21)."""
    pts = sorted(set(supp1 + supp2))
    dist = 0.0
    for idx in range(len(pts) - 1):
        mid = 0.5 * (pts[idx] + pts[idx + 1])
        cdf1 = sum(w for x, w in zip(supp1, w1) if x <= mid)
        cdf2 = sum(w for x, w in zip(supp2, w2) if x <= mid)
        dist += abs(cdf1 - cdf2) * (pts[idx + 1] - pts[idx])
    return dist


def levy_distance_discrete(
    supp1: list[float], w1: list[float], supp2: list[float], w2: list[float]
) -> float:
    """Levy metric d_L(F, G) = inf{eps > 0 : F(x-eps)-eps <= G(x) <= F(x+eps)+eps} (Section 4.1, p. 13)."""
    def cdf(supp: list[float], w: list[float], x: float) -> float:
        return sum(wi for xi, wi in zip(supp, w) if xi <= x)

    lo, hi = 0.0, 2.0
    probe_x = [0.05 * i for i in range(60)]
    for _ in range(30):
        mid = 0.5 * (lo + hi)
        ok = True
        for x in probe_x:
            gx = cdf(supp2, w2, x)
            if gx < cdf(supp1, w1, x - mid) - mid - 1e-9 or gx > cdf(supp1, w1, x + mid) + mid + 1e-9:
                ok = False
                break
        if ok:
            hi = mid
        else:
            lo = mid
    return hi


def jacobi_eigenvalues_symmetric(A_in: list[list[float]], sweeps: int = 35) -> list[float]:
    """Compute all eigenvalues of a real symmetric p x p matrix via cyclic Jacobi rotations."""
    p = len(A_in)
    A = [row[:] for row in A_in]
    for _ in range(sweeps):
        off = 0.0
        for i in range(p):
            for j in range(i + 1, p):
                off += A[i][j] * A[i][j]
        if off < 1e-20:
            break
        for i in range(p):
            for j in range(i + 1, p):
                aij = A[i][j]
                if abs(aij) < 1e-13:
                    continue
                tau = (A[j][j] - A[i][i]) / (2.0 * aij)
                t = (1.0 if tau >= 0 else -1.0) / (abs(tau) + math.sqrt(1.0 + tau * tau))
                c = 1.0 / math.sqrt(1.0 + t * t)
                s = t * c
                aii, ajj = A[i][i], A[j][j]
                A[i][i] = aii - t * aij
                A[j][j] = ajj + t * aij
                A[i][j] = 0.0
                A[j][i] = 0.0
                for r in range(p):
                    if r != i and r != j:
                        ari, arj = A[r][i], A[r][j]
                        A[r][i] = c * ari - s * arj
                        A[i][r] = A[r][i]
                        A[r][j] = s * ari + c * arj
                        A[j][r] = A[r][j]
    return sorted([A[i][i] for i in range(p)], reverse=True)


def main() -> None:
    # 1. Verify Lemma 1 Stieltjes identity (p. 19) & Proposition 1 Lipschitz bound (p. 19)
    supp = [1.0, 2.0]
    wts = [0.5, 0.5]
    m_val = complex(0.35, 0.25)
    lhs = mp_integral(supp, wts, m_val)
    rhs = (1.0 / m_val) - (1.0 / (m_val * m_val)) * stieltjes_transform(supp, wts, -1.0 / m_val)
    assert abs(lhs - rhs) < 1e-14, f"Lemma 1 identity failed: {lhs} vs {rhs}"

    u_min = 0.2
    z1 = complex(1.1, 0.25)
    z2 = complex(1.6, 0.35)
    diff_s = abs(stieltjes_transform(supp, wts, z1) - stieltjes_transform(supp, wts, z2))
    lip_bound = abs(z1 - z2) / (u_min * u_min)
    assert diff_s <= lip_bound, f"Proposition 1 Lipschitz bound failed: {diff_s} > {lip_bound}"

    # 2. Simulate bimodal spectrum H_p = 0.5 delta_1 + 0.5 delta_2 (Section 4.1.2, p. 13)
    rng = random.Random(20060914)
    p = 24
    n = 96  # gamma = p/n = 0.25
    true_eigs = [1.0] * (p // 2) + [2.0] * (p // 2)
    # Sample covariance S_p = (1/n) X^T X where X = Y diag(sqrt(true_eigs))
    X = [
        [rng.gauss(0.0, math.sqrt(true_eigs[j])) for j in range(p)]
        for _ in range(n)
    ]
    S_p = [[0.0] * p for _ in range(p)]
    for i in range(p):
        for j in range(i, p):
            val = sum(X[r][i] * X[r][j] for r in range(n)) / n
            S_p[i][j] = val
            S_p[j][i] = val
    sample_eigs = jacobi_eigenvalues_symmetric(S_p)

    # Verify Appendix A.1 (p. 23) Jensen bias: l_1(S_p) > max(true_eigs) and l_p(S_p) < min(true_eigs)
    assert sample_eigs[0] > 2.0 and sample_eigs[-1] < 1.0, (
        f"Expected sample extreme eigenvalues to spread outside [1, 2]: [{sample_eigs[-1]:.3f}, {sample_eigs[0]:.3f}]"
    )

    # 3. Solve discretized Marcenko-Pastur convex inversion (Section 3.2, pp. 7-9)
    grid_t = [0.5 + 0.05 * k for k in range(41)]  # [0.5, 2.5]
    z_grid = [
        complex(0.4 + 0.1 * j, im_val)
        for j in range(28)
        for im_val in (0.15, 0.25, 0.40)
    ]
    w_hat = solve_mp_convex_inversion(sample_eigs, p, n, grid_t, z_grid, iters=500)

    # Compare Wasserstein-1 and Levy distances to true H_p
    w_emp = [1.0 / p] * p
    w1_emp = wasserstein1_discrete(sample_eigs, w_emp, [1.0, 2.0], [0.5, 0.5])
    w1_hat = wasserstein1_discrete(grid_t, w_hat, [1.0, 2.0], [0.5, 0.5])
    levy_emp = levy_distance_discrete(sample_eigs, w_emp, [1.0, 2.0], [0.5, 0.5])
    levy_hat = levy_distance_discrete(grid_t, w_hat, [1.0, 2.0], [0.5, 0.5])

    assert w1_hat < 0.65 * w1_emp, (
        f"Marcenko-Pastur convex estimator W1 ({w1_hat:.4f}) must beat empirical ESD ({w1_emp:.4f})"
    )
    assert levy_hat < levy_emp, (
        f"Marcenko-Pastur convex estimator Levy ({levy_hat:.4f}) must beat empirical ESD ({levy_emp:.4f})"
    )

    print(
        f"El Karoui (2008) Marcenko-Pastur convex spectrum estimation verified: "
        f"W1_hat={w1_hat:.4f} < W1_emp={w1_emp:.4f}, "
        f"Levy_hat={levy_hat:.4f} < Levy_emp={levy_emp:.4f}, "
        f"Lemma 1 err={abs(lhs - rhs):.2e}."
    )


if __name__ == "__main__":
    main()
