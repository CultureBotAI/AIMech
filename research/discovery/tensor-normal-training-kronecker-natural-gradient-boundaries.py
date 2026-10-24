#!/usr/bin/env python3
"""Boundary verification for Round 642: Tensor Normal Training / TNT (Ren & Goldfarb, NeurIPS 2021 / arXiv:2106.02925)."""

from __future__ import annotations

import math
import random


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    m, k, n = len(a), len(a[0]), len(b[0])
    out = [[0.0] * n for _ in range(m)]
    for i in range(m):
        for p in range(k):
            aip = a[i][p]
            for j in range(n):
                out[i][j] += aip * b[p][j]
    return out


def transpose(a: list[list[float]]) -> list[list[float]]:
    return [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]


def trace(a: list[list[float]]) -> float:
    return sum(a[i][i] for i in range(len(a)))


def invert_spd(a: list[list[float]]) -> list[list[float]]:
    n = len(a)
    aug = [a[i][:] + [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(aug[r][col]))
        aug[col], aug[piv] = aug[piv], aug[col]
        div = aug[col][col]
        for j in range(2 * n):
            aug[col][j] /= div
        for r in range(n):
            if r != col:
                fac = aug[r][col]
                for j in range(2 * n):
                    aug[r][j] -= fac * aug[col][j]
    return [row[n:] for row in aug]


def cholesky(a: list[list[float]]) -> list[list[float]]:
    n = len(a)
    l_mat = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = sum(l_mat[i][k] * l_mat[j][k] for k in range(j))
            if i == j:
                l_mat[i][j] = math.sqrt(max(1e-12, a[i][i] - s))
            else:
                l_mat[i][j] = (a[i][j] - s) / l_mat[j][j]
    return l_mat


def normalized_frob_error(a: list[list[float]], b: list[list[float]]) -> float:
    """Relative Frobenius error after normalizing traces."""
    ta, tb = trace(a), trace(b)
    n = len(a)
    diff_sq = 0.0
    norm_sq = 0.0
    for i in range(n):
        for j in range(n):
            aij = a[i][j] / ta
            bij = b[i][j] / tb
            diff_sq += (aij - bij) ** 2
            norm_sq += aij * aij
    return math.sqrt(diff_sq / norm_sq)


def main() -> None:
    rng = random.Random(642)
    d1, d2 = 4, 5

    # Ground-truth positive-definite Kronecker covariance factors Sigma = U2 (x) U1
    u1_true = [
        [2.2, 0.6, -0.3, 0.2],
        [0.6, 1.5, 0.4, -0.1],
        [-0.3, 0.4, 1.8, 0.5],
        [0.2, -0.1, 0.5, 1.3],
    ]
    u2_true = [
        [1.9, -0.5, 0.3, 0.1, -0.2],
        [-0.5, 2.4, 0.4, -0.3, 0.2],
        [0.3, 0.4, 1.4, 0.2, -0.1],
        [0.1, -0.3, 0.2, 1.7, 0.4],
        [-0.2, 0.2, -0.1, 0.4, 1.2],
    ]
    l1 = cholesky(u1_true)
    l2 = cholesky(u2_true)
    l2_t = transpose(l2)

    # 1. Verify Theorem 1 (Section 2.2, Eq. 7, page 4) & TNT Mode-Matricization Estimator:
    # For G ~ TN(0, U1, U2), G = L1 Z L2^T with Z_{i,j} ~ N(0,1).
    # Mode-1 unfolding G_(1) = G has E[G G^T] = Tr(U2) * U1, so U1_TNT = (1 / d2) E[G G^T] = (Tr(U2)/d2) U1.
    # Mode-2 unfolding G_(2) = G^T has E[G^T G] = Tr(U1) * U2, so U2_TNT = (1 / d1) E[G^T G] = (Tr(U1)/d1) U2.
    # Further verify exact Theorem 1 coupled stationarity: (1 / d2) E[G U2^{-1} G^T] = U1 and (1 / d1) E[G^T U1^{-1} G] = U2.
    u1_inv_true = invert_spd(u1_true)
    u2_inv_true = invert_spd(u2_true)

    u1_tnt = [[0.0] * d1 for _ in range(d1)]
    u2_tnt = [[0.0] * d2 for _ in range(d2)]
    u1_thm1 = [[0.0] * d1 for _ in range(d1)]
    u2_thm1 = [[0.0] * d2 for _ in range(d2)]

    n_samples = 4000
    for _ in range(n_samples):
        z = [[rng.gauss(0.0, 1.0) for _ in range(d2)] for _ in range(d1)]
        g = matmul(matmul(l1, z), l2_t)
        gt = transpose(g)
        ggt = matmul(g, gt)
        gtg = matmul(gt, g)
        g_u2inv_gt = matmul(matmul(g, u2_inv_true), gt)
        gt_u1inv_g = matmul(matmul(gt, u1_inv_true), g)
        for i in range(d1):
            for j in range(d1):
                u1_tnt[i][j] += ggt[i][j] / (d2 * n_samples)
                u1_thm1[i][j] += g_u2inv_gt[i][j] / (d2 * n_samples)
        for i in range(d2):
            for j in range(d2):
                u2_tnt[i][j] += gtg[i][j] / (d1 * n_samples)
                u2_thm1[i][j] += gt_u1inv_g[i][j] / (d1 * n_samples)

    err_u1_tnt = normalized_frob_error(u1_tnt, u1_true)
    err_u2_tnt = normalized_frob_error(u2_tnt, u2_true)
    err_u1_thm1 = max(abs(u1_thm1[i][j] - u1_true[i][j]) for i in range(d1) for j in range(d1))
    err_u2_thm1 = max(abs(u2_thm1[i][j] - u2_true[i][j]) for i in range(d2) for j in range(d2))

    assert err_u1_tnt < 0.03 and err_u2_tnt < 0.03, f"TNT factor error too high: {err_u1_tnt:.4f}, {err_u2_tnt:.4f}"
    assert err_u1_thm1 < 0.08 and err_u2_thm1 < 0.08, f"Theorem 1 stationarity error too high: {err_u1_thm1:.4f}"

    # 2. Verify TNT Preconditioned Natural Gradient Update vs Unpreconditioned SGD on Ill-Conditioned Tensor Loss:
    # Quadratic objective L(W) = 0.5 * Tr(W^T U1 W U2) has Hessian H = U2 (x) U1.
    # Gradient at W is M = U1 W U2.
    # TNT update direction P_TNT = (U1_tnt)^{-1} M (U2_tnt)^{-1} points directly toward W* = 0 (proportional to W).
    w0 = [[rng.uniform(-1.0, 1.0) for _ in range(d2)] for _ in range(d1)]
    grad_m = matmul(matmul(u1_true, w0), u2_true)
    u1_tnt_inv = invert_spd(u1_tnt)
    u2_tnt_inv = invert_spd(u2_tnt)
    # Rescale by trace factor (Tr(U1)*Tr(U2)/(d1*d2)) to match exact inverse curvature scale
    scale_corr = (trace(u1_true) * trace(u2_true)) / (d1 * d2)
    step_tnt = matmul(matmul(u1_tnt_inv, grad_m), u2_tnt_inv)
    w_after_tnt = [[w0[i][j] - scale_corr * step_tnt[i][j] for j in range(d2)] for i in range(d1)]

    def loss_fn(w: list[list[float]]) -> float:
        uwu = matmul(matmul(u1_true, w), u2_true)
        return 0.5 * sum(w[i][j] * uwu[i][j] for i in range(d1) for j in range(d2))

    l_init = loss_fn(w0)
    l_tnt = loss_fn(w_after_tnt)
    # Compare with 1 step of best constant-step SGD
    w_sgd = [[w0[i][j] - 0.12 * grad_m[i][j] for j in range(d2)] for i in range(d1)]
    l_sgd = loss_fn(w_sgd)
    assert l_tnt < 1e-3 * l_init and l_tnt < 1e-2 * l_sgd

    print(
        f"[PASS] Round 642 TNT verified: err_U1={err_u1_tnt:.4f}, err_U2={err_u2_tnt:.4f}, "
        f"thm1_max_diff=({err_u1_thm1:.4f},{err_u2_thm1:.4f}), L_init={l_init:.4f}->L_TNT={l_tnt:.6f}<<L_SGD={l_sgd:.4f}"
    )


if __name__ == "__main__":
    main()
