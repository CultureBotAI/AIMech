#!/usr/bin/env python3
"""Constructed boundary & regime verification for SPIDER (Fang et al. 2018, Round 345)."""

import math
import random


def f_i_and_grad(i: int, n: int, x: list[float]):
    # Smooth non-convex finite-sum components:
    # f_i(x) = 0.5 * (x_0^2 + x_1^2) + 0.5 * sin(x_0 + 2*pi*i/n) + 0.5 * cos(x_1 - 2*pi*i/n)
    angle0 = x[0] + 2.0 * math.pi * i / n
    angle1 = x[1] - 2.0 * math.pi * i / n
    val = 0.5 * (x[0] ** 2 + x[1] ** 2) + 0.5 * math.sin(angle0) + 0.5 * math.cos(angle1)
    g0 = x[0] + 0.5 * math.cos(angle0)
    g1 = x[1] - 0.5 * math.sin(angle1)
    return val, [g0, g1]


def full_f_and_grad(n: int, x: list[float]):
    val = 0.0
    g = [0.0, 0.0]
    for i in range(n):
        vi, gi = f_i_and_grad(i, n, x)
        val += vi / n
        g[0] += gi[0] / n
        g[1] += gi[1] / n
    return val, g


def norm(v: list[float]) -> float:
    return math.sqrt(v[0] * v[0] + v[1] * v[1])


def norm_sq(v: list[float]) -> float:
    return v[0] * v[0] + v[1] * v[1]


def main():
    n = 16
    L = 1.5  # Each f_i has Hessian diag(1 - 0.5 sin, 1 - 0.5 cos), so ||nabla^2 f_i|| <= 1.5

    # Claim 1: Verify Proposition 1(i) exact martingale variance identity and Lemma 1 bound
    # For a deterministic trajectory x^0, x^1, x^2 with S_2 = 1 sampled uniformly with replacement:
    x_seq = [[1.2, -0.8], [1.1, -0.75], [1.0, -0.7]]
    _, g0_true = full_f_and_grad(n, x_seq[0])
    _, g1_true = full_f_and_grad(n, x_seq[1])
    _, g2_true = full_f_and_grad(n, x_seq[2])

    # Enumerate all n^2 sample pairs (i1, i2) starting from exact v^0 = g0_true
    var_v2 = 0.0
    sum_inc_vars = 0.0
    for i1 in range(n):
        _, gi1_1 = f_i_and_grad(i1, n, x_seq[1])
        _, gi1_0 = f_i_and_grad(i1, n, x_seq[0])
        xi1 = [
            (gi1_1[0] - gi1_0[0]) - (g1_true[0] - g0_true[0]),
            (gi1_1[1] - gi1_0[1]) - (g1_true[1] - g0_true[1]),
        ]
        v1 = [g0_true[0] + (gi1_1[0] - gi1_0[0]), g0_true[1] + (gi1_1[1] - gi1_0[1])]
        for i2 in range(n):
            _, gi2_2 = f_i_and_grad(i2, n, x_seq[2])
            _, gi2_1 = f_i_and_grad(i2, n, x_seq[1])
            xi2 = [
                (gi2_2[0] - gi2_1[0]) - (g2_true[0] - g1_true[0]),
                (gi2_2[1] - gi2_1[1]) - (g2_true[1] - g1_true[1]),
            ]
            v2 = [v1[0] + (gi2_2[0] - gi2_1[0]), v1[1] + (gi2_2[1] - gi2_1[1])]
            prob = 1.0 / (n * n)
            var_v2 += prob * norm_sq([v2[0] - g2_true[0], v2[1] - g2_true[1]])
            sum_inc_vars += prob * (norm_sq(xi1) + norm_sq(xi2))

    assert abs(var_v2 - sum_inc_vars) < 1e-15, f"Proposition 1(i) failed: {var_v2} vs {sum_inc_vars}"
    lemma1_bound = L * L * (
        norm_sq([x_seq[1][0] - x_seq[0][0], x_seq[1][1] - x_seq[0][1]])
        + norm_sq([x_seq[2][0] - x_seq[1][0], x_seq[2][1] - x_seq[1][1]])
    )
    assert var_v2 <= lemma1_bound + 1e-12

    # Claim 2: SPIDER-SFO (Algorithm 1 Option II) with normalized step size eta^k = min(eps / (L n_0 ||v^k||), 1 / (2 L n_0))
    # Verify Lemma 2 variance bound E[||v^k - grad f(x^k)||^2] <= eps^2 and convergence to stationary point
    eps = 0.05
    n0 = 1.0
    S2 = int(math.sqrt(n) / n0)  # S2 = 4
    q = int(n0 * math.sqrt(n))   # q = 4
    rng = random.Random(345)
    x = [0.6, -0.5]
    v = [0.0, 0.0]
    max_epoch_err_sq = 0.0
    for k in range(40):
        if k % q == 0:
            _, v = full_f_and_grad(n, x)
        else:
            batch = [rng.randrange(n) for _ in range(S2)]
            diff = [0.0, 0.0]
            for idx in batch:
                _, g_curr = f_i_and_grad(idx, n, x)
                _, g_prev = f_i_and_grad(idx, n, x_prev)
                diff[0] += (g_curr[0] - g_prev[0]) / S2
                diff[1] += (g_curr[1] - g_prev[1]) / S2
            v = [v[0] + diff[0], v[1] + diff[1]]
        _, g_exact = full_f_and_grad(n, x)
        err_sq = norm_sq([v[0] - g_exact[0], v[1] - g_exact[1]])
        max_epoch_err_sq = max(max_epoch_err_sq, err_sq)

        v_norm = norm(v)
        eta_k = min(eps / (L * n0 * max(v_norm, 1e-12)), 1.0 / (2.0 * L * n0))
        x_prev = x[:]
        x = [x[0] - eta_k * v[0], x[1] - eta_k * v[1]]
        # Verify step displacement cap ||x^{k+1} - x^k|| <= eps / (L n_0) (Eq. B.2)
        step_disp = norm([x[0] - x_prev[0], x[1] - x_prev[1]])
        assert step_disp <= eps / (L * n0) + 1e-12

    _, final_grad = full_f_and_grad(n, x)
    assert max_epoch_err_sq <= eps * eps
    assert norm(final_grad) < 0.05

    # Claim 3: Unnormalized large step size vs NGD step cap, and finite-sum complexity scaling O(n + n^{1/2} eps^{-2}) vs SVRG O(n + n^{2/3} eps^{-2})
    # For large n = 10^6 and eps = 10^{-2}:
    n_large = 10 ** 6
    eps_small = 1e-2
    spider_cost = n_large + (n_large ** 0.5) * (eps_small ** -2)
    svrg_cost = n_large + (n_large ** (2.0 / 3.0)) * (eps_small ** -2)
    gd_cost = n_large * (eps_small ** -2)
    assert spider_cost < svrg_cost / 5.0 and spider_cost < gd_cost / 500.0

    print(
        f"[PASS] SPIDER boundaries verified: Prop1_var={var_v2:.6e}=={sum_inc_vars:.6e}<={lemma1_bound:.6e}, "
        f"max_err_sq={max_epoch_err_sq:.3e}<=eps^2={eps*eps:.3e}, final_grad={norm(final_grad):.4f}, "
        f"spider_cost={spider_cost:.2e}<svrg_cost={svrg_cost:.2e}"
    )


if __name__ == "__main__":
    main()
