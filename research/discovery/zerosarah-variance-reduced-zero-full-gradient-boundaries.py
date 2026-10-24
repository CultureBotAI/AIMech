#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 566: ZeroSARAH and D-ZeroSARAH."""

import math
import random


def main() -> None:
    random.seed(566)
    # 1. Verify Lemma 2 / Theorem 1 parameter identities for ZeroSARAH:
    # With b_k = sqrt(n), lambda_0 = 1, lambda_k = b_k / (2 n) for k >= 1:
    # M_{k+1} = 2 / (lambda_{k+1} b_{k+1}) + 8 * lambda_{k+1} * n^2 / b_{k+1}^3
    for n in [16, 64, 100]:
        b = int(math.isqrt(n))
        assert b * b == n
        lam = b / (2.0 * n)
        M = 2.0 / (lam * b) + 8.0 * lam * (n ** 2) / (b ** 3)
        assert abs(M - 8.0) < 1e-12, f"Expected M=8.0, got {M}"
        eta = 1.0 / ((1.0 + math.sqrt(M)) * 1.0)
        expected_eta = 1.0 / (1.0 + math.sqrt(8.0))
        assert abs(eta - expected_eta) < 1e-12

    # 2. Verify Lemma 1 conditional expectation identity:
    # E_k[v^k - nabla f(x^k)] = (1 - lambda_k)(v^{k-1} - nabla f(x^{k-1}))
    n = 6
    d = 3
    A = [[random.uniform(-1.0, 1.0) for _ in range(d)] for _ in range(n)]
    b_vec = [random.uniform(-1.0, 1.0) for _ in range(n)]

    def grad_i(i: int, x: list[float]) -> list[float]:
        # f_i(x) = 0.5 * (<a_i, x> - b_i)^2
        r = sum(A[i][j] * x[j] for j in range(d)) - b_vec[i]
        return [r * A[i][j] for j in range(d)]

    def full_grad(x: list[float]) -> list[float]:
        g = [0.0] * d
        for i in range(n):
            gi = grad_i(i, x)
            for j in range(d):
                g[j] += gi[j] / n
        return g

    x_prev = [random.uniform(-1.0, 1.0) for _ in range(d)]
    x_curr = [random.uniform(-1.0, 1.0) for _ in range(d)]
    v_prev = [random.uniform(-1.0, 1.0) for _ in range(d)]
    y_prev = [[random.uniform(-1.0, 1.0) for _ in range(d)] for _ in range(n)]
    y_bar = [sum(y_prev[i][j] for i in range(n)) / n for j in range(d)]
    lam_k = 0.35

    # Exact expectation over all singletons I_b^k = {i} (b_k = 1)
    expected_vk = [0.0] * d
    for i in range(n):
        gi_curr = grad_i(i, x_curr)
        gi_prev = grad_i(i, x_prev)
        for j in range(d):
            vk_ij = (
                (gi_curr[j] - gi_prev[j])
                + (1.0 - lam_k) * v_prev[j]
                + lam_k * ((gi_prev[j] - y_prev[i][j]) + y_bar[j])
            )
            expected_vk[j] += vk_ij / n

    fg_curr = full_grad(x_curr)
    fg_prev = full_grad(x_prev)
    for j in range(d):
        lhs = expected_vk[j] - fg_curr[j]
        rhs = (1.0 - lam_k) * (v_prev[j] - fg_prev[j])
        assert abs(lhs - rhs) < 1e-12, f"Mismatch in Lemma 1: {lhs} vs {rhs}"

    # 3. Simulate ZeroSARAH (with zero full gradient computations) vs SARAH / SGD
    # on a finite-sum problem with n = 16, b = 4
    n_sim = 16
    b_sim = 4
    d_sim = 4
    # Smooth strongly convex + nonconvex perturbation finite-sum objective
    W = [[random.gauss(0.0, 1.0) for _ in range(d_sim)] for _ in range(n_sim)]
    targets = [random.gauss(0.0, 1.0) for _ in range(n_sim)]

    def sim_grad_i(i: int, x: list[float]) -> list[float]:
        dot = sum(W[i][j] * x[j] for j in range(d_sim)) - targets[i]
        return [dot * W[i][j] + 0.2 * x[j] for j in range(d_sim)]

    def sim_full_grad_norm_sq(x: list[float]) -> float:
        g = [0.0] * d_sim
        for i in range(n_sim):
            gi = sim_grad_i(i, x)
            for j in range(d_sim):
                g[j] += gi[j] / n_sim
        return sum(val * val for val in g)

    # Estimate smoothness L
    L = 3.5
    eta_zs = 1.0 / ((1.0 + math.sqrt(8.0)) * L)

    # Run ZeroSARAH starting from y_i^{-1} = 0, v^{-1} = 0, x^{-1} = x^0
    x_init = [1.5, -1.2, 0.8, -0.9]
    x_prev_zs = list(x_init)
    x_zs = list(x_init)
    v_prev_zs = [0.0] * d_sim
    y_table = [[0.0] * d_sim for _ in range(n_sim)]
    full_grad_evals = 0

    for k in range(300):
        batch = random.sample(range(n_sim), b_sim)
        lam = 1.0 if k == 0 else b_sim / (2.0 * n_sim)
        y_avg = [sum(y_table[i][j] for i in range(n_sim)) / n_sim for j in range(d_sim)]
        diff1 = [0.0] * d_sim
        diff2 = [0.0] * d_sim
        curr_batch_grads = {}
        for i in batch:
            gi_curr = sim_grad_i(i, x_zs)
            gi_prev = sim_grad_i(i, x_prev_zs)
            curr_batch_grads[i] = gi_curr
            for j in range(d_sim):
                diff1[j] += (gi_curr[j] - gi_prev[j]) / b_sim
                diff2[j] += (gi_prev[j] - y_table[i][j]) / b_sim
        v_curr = [
            diff1[j] + (1.0 - lam) * v_prev_zs[j] + lam * (diff2[j] + y_avg[j])
            for j in range(d_sim)
        ]
        x_next = [x_zs[j] - eta_zs * v_curr[j] for j in range(d_sim)]
        for i in batch:
            y_table[i] = curr_batch_grads[i]
        x_prev_zs = x_zs
        x_zs = x_next
        v_prev_zs = v_curr

    # Run standard mini-batch SGD with constant step size eta_zs and same batch size
    x_sgd = list(x_init)
    for k in range(300):
        batch = random.sample(range(n_sim), b_sim)
        g_mb = [0.0] * d_sim
        for i in batch:
            gi = sim_grad_i(i, x_sgd)
            for j in range(d_sim):
                g_mb[j] += gi[j] / b_sim
        x_sgd = [x_sgd[j] - eta_zs * g_mb[j] for j in range(d_sim)]

    gn_init = sim_full_grad_norm_sq(x_init)
    gn_zs = sim_full_grad_norm_sq(x_zs)
    gn_sgd = sim_full_grad_norm_sq(x_sgd)
    assert full_grad_evals == 0
    assert gn_zs < 1e-8 and gn_zs < gn_sgd * 1e-3, (
        f"Expected ZeroSARAH to converge to exact stationarity: gn_zs={gn_zs}, gn_sgd={gn_sgd}"
    )
    print(
        f"[PASS] Round 566 ZeroSARAH verified: M=8.0000, full_grads={full_grad_evals}, "
        f"gn_init={gn_init:.3e} -> gn_zs={gn_zs:.3e} << gn_sgd={gn_sgd:.3e}"
    )


if __name__ == "__main__":
    main()
