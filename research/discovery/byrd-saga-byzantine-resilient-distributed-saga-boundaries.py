"""Constructed boundary verification for Round 544: Byrd-SAGA (Wu, Ling, Chen, & Giannakis, IEEE TSP 2020)."""

from __future__ import annotations

import math
import random


def norm2(v: list[float]) -> float:
    return math.sqrt(sum(x * x for x in v))


def geomed_weiszfeld(points: list[list[float]], iters: int = 40) -> list[float]:
    d = len(points[0])
    m = len(points)
    y = [sum(p[j] for p in points) / m for j in range(d)]
    for _ in range(iters):
        weights = []
        for p in points:
            dist = max(norm2([y[j] - p[j] for j in range(d)]), 1e-10)
            weights.append(1.0 / dist)
        w_sum = sum(weights)
        y = [sum(weights[i] * points[i][j] for i in range(m)) / w_sum for j in range(d)]
    return y


def main() -> None:
    rng = random.Random(544)
    # 2D strongly convex finite-sum problem across W = 7 workers (5 honest, B = 2 Byzantine < 7/2)
    # Honest workers share identical local dataset of J = 6 distinct noisy samples (outer variation delta^2 = 0,
    # inner variation sigma^2 > 0), testing Theorem 1 vs Theorem 2 (p. 6, Fig. 5).
    W = 7
    B = 2
    H = W - B  # 5 honest workers
    J = 6
    x_star = [1.5, -1.0]
    # Sample offsets e_j with zero mean across j=0..J-1 but non-zero variance sigma^2 > 0
    offsets = [
        [2.0, -1.5],
        [-2.0, 1.5],
        [1.5, 2.0],
        [-1.5, -2.0],
        [1.0, -1.0],
        [-1.0, 1.0],
    ]
    # f_{w,j}(x) = 0.5 * ||x - (x_star + offsets[j])||^2  => grad f_{w,j}(x) = x - x_star - offsets[j]
    # True average gradient over j=1..J is grad f_w(x) = x - x_star (so minimizer is x_star, mu=L=1)

    def sample_grad(x: list[float], j: int) -> list[float]:
        return [x[0] - x_star[0] - offsets[j][0], x[1] - x_star[1] - offsets[j][1]]

    # 1. Verify Lemma 1 / Theorem 1 vs Theorem 2 asymptotic error formulas (Eq. 22, 25, p. 6)
    alpha = B / W
    c_alpha = (2.0 - 2.0 * alpha) / (1.0 - 2.0 * alpha)
    sigma_sq = sum(offsets[j][0] ** 2 + offsets[j][1] ** 2 for j in range(J)) / J
    delta_sq = 0.0
    mu = 1.0
    asymp_byrd_saga = (10.0 / (mu ** 2)) * (c_alpha ** 2) * delta_sq
    asymp_byrd_sgd = (4.0 / (mu ** 2)) * (c_alpha ** 2) * (sigma_sq + delta_sq)
    assert asymp_byrd_saga == 0.0
    assert asymp_byrd_sgd > 10.0

    # 2. Simulate (a) Distributed SAGA + Mean under attack, (b) Byrd-SGD (SGD + geomed), (c) Byrd-SAGA (Algorithm 1)
    gamma = 0.04
    steps = 350

    x_saga_mean = [0.0, 0.0]
    x_byrd_sgd = [0.0, 0.0]
    x_byrd_saga = [0.0, 0.0]

    # SAGA tables for (a) and (c): table[w][j] stores f'_{w,j}(phi_{w,j})
    table_mean = [[sample_grad(x_saga_mean, j) for j in range(J)] for _ in range(H)]
    avg_mean = [
        [sum(table_mean[w][j][d] for j in range(J)) / J for d in range(2)]
        for w in range(H)
    ]

    table_byrd = [[sample_grad(x_byrd_saga, j) for j in range(J)] for _ in range(H)]
    avg_byrd = [
        [sum(table_byrd[w][j][d] for j in range(J)) / J for d in range(2)]
        for w in range(H)
    ]

    for _ in range(steps):
        # Sample indices i_w^k in {0, ..., J-1} for each honest worker
        idxs = [rng.randrange(J) for _ in range(H)]

        # (a) SAGA + Mean with sign-flipping / bias Byzantine attack
        msgs_mean = []
        for w in range(H):
            j = idxs[w]
            g_new = sample_grad(x_saga_mean, j)
            g_old = table_mean[w][j]
            m_w = [g_new[d] - g_old[d] + avg_mean[w][d] for d in range(2)]
            msgs_mean.append(m_w)
            for d in range(2):
                avg_mean[w][d] += (g_new[d] - g_old[d]) / J
            table_mean[w][j] = g_new
        for _ in range(B):
            msgs_mean.append([15.0, -15.0])
        agg_mean = [sum(m[d] for m in msgs_mean) / W for d in range(2)]
        x_saga_mean = [x_saga_mean[d] - gamma * agg_mean[d] for d in range(2)]

        # (b) Byrd-SGD (Geometric median of raw stochastic gradients)
        msgs_sgd = []
        for w in range(H):
            j = idxs[w]
            msgs_sgd.append(sample_grad(x_byrd_sgd, j))
        for _ in range(B):
            msgs_sgd.append([15.0, -15.0])
        agg_sgd = geomed_weiszfeld(msgs_sgd)
        x_byrd_sgd = [x_byrd_sgd[d] - gamma * agg_sgd[d] for d in range(2)]

        # (c) Byrd-SAGA (Algorithm 1, p. 4: Geometric median of SAGA variance-reduced gradients)
        msgs_byrd = []
        for w in range(H):
            j = idxs[w]
            g_new = sample_grad(x_byrd_saga, j)
            g_old = table_byrd[w][j]
            m_w = [g_new[d] - g_old[d] + avg_byrd[w][d] for d in range(2)]
            msgs_byrd.append(m_w)
            for d in range(2):
                avg_byrd[w][d] += (g_new[d] - g_old[d]) / J
            table_byrd[w][j] = g_new
        for _ in range(B):
            msgs_byrd.append([15.0, -15.0])
        agg_byrd = geomed_weiszfeld(msgs_byrd)
        x_byrd_saga = [x_byrd_saga[d] - gamma * agg_byrd[d] for d in range(2)]

    err_saga_mean = norm2([x_saga_mean[d] - x_star[d] for d in range(2)]) ** 2
    err_byrd_sgd = norm2([x_byrd_sgd[d] - x_star[d] for d in range(2)]) ** 2
    err_byrd_saga = norm2([x_byrd_saga[d] - x_star[d] for d in range(2)]) ** 2

    assert err_byrd_saga < 1e-4, f"Expected Byrd-SAGA to converge to x*, got {err_byrd_saga}"
    assert err_byrd_sgd > 20 * err_byrd_saga, f"Expected Byrd-SGD error > Byrd-SAGA: {err_byrd_sgd}"
    assert err_saga_mean > 1.0, f"Expected unguarded SAGA-mean to fail under attack: {err_saga_mean}"

    print(
        f"[PASS] Round 544 Byrd-SAGA verified: "
        f"err_Byrd_SAGA={err_byrd_saga:.2e} << err_Byrd_SGD={err_byrd_sgd:.4f} << err_SAGA_Mean={err_saga_mean:.2f}"
    )


if __name__ == "__main__":
    main()
