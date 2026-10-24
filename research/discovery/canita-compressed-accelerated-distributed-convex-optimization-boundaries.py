#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 560: CANITA (Li & Richtarik, NeurIPS 2021)."""

import math
import random


def rand_k_compress(vec, k, rng):
    d = len(vec)
    chosen = set(rng.sample(range(d), k))
    scale = d / k
    return [scale * v if idx in chosen else 0.0 for idx, v in enumerate(vec)]


def vec_add(u, v):
    return [a + b for a, b in zip(u, v)]


def vec_sub(u, v):
    return [a - b for a, b in zip(u, v)]


def vec_scale(u, c):
    return [c * a for a in u]


def sq_norm(u):
    return sum(a * a for a in u)


def main():
    rng = random.Random(20210720)
    n, d, k = 8, 6, 2
    omega = (d / k) - 1.0  # Example 1: Rand-k has omega = d/k - 1 = 2.0

    # 1. Verify Theorem 2 parameter relations (Equations 10-12 & Appendix B Equations 27-32)
    b = min(omega, math.sqrt(omega * ((1.0 + omega) ** 2) / n))
    L = 2.0
    beta_0 = 9.0 * ((1.0 + b + omega) ** 2) / ((1.0 + b) * L)
    beta = 48.0 * omega * (1.0 + omega) * (1.0 + b + 2.0 * (1.0 + omega)) / (n * ((1.0 + b) ** 2))
    gamma = ((1.0 + b) ** 2) / (8.0 * (1.0 + b + 2.0 * (1.0 + omega)))
    p_t = 1.0 / (1.0 + b)
    alpha_t = 1.0 / (1.0 + omega)

    # Equation (27): 4 * p_t * gamma_t * (1 + 2 * p_t / alpha_t) == 1/2
    eq27 = 4.0 * p_t * gamma * (1.0 + 2.0 * p_t / alpha_t)
    assert abs(eq27 - 0.5) < 1e-12

    eta_prev = 1.0 / (L * (beta_0 + 1.5))
    theta_prev = 3.0 * (1.0 + b) / (0.0 + 9.0 * (1.0 + b + omega))
    for t in range(1, 60):
        theta_t = 3.0 * (1.0 + b) / (t + 9.0 * (1.0 + b + omega))
        eta_t = min(
            (1.0 + 1.0 / (t + 9.0 * (1.0 + b + omega))) * eta_prev,
            1.0 / (L * (beta + 1.5)),
        )
        # Verify Theorem 1 conditions (5) and (6)
        assert alpha_t <= 1.0 / (1.0 + omega) + 1e-12
        assert eta_t <= 1.0 / (L * (1.0 + beta + eq27)) + 1e-12
        assert (2.0 * omega / (beta * n)) + eq27 <= 1.0 - theta_t + 1e-12
        lhs1 = (1.0 - p_t * theta_t) * eta_t / (p_t * (theta_t ** 2))
        rhs1 = eta_prev / (p_t * (theta_prev ** 2))
        assert lhs1 <= rhs1 + 1e-9
        lhs2 = ((omega / (beta * n)) + (1.0 - 0.5 * alpha_t) * gamma) * eta_t / (theta_t ** 2)
        rhs2 = gamma * eta_prev / (theta_prev ** 2)
        assert lhs2 <= rhs2 + 1e-9
        eta_prev, theta_prev = eta_t, theta_t

    # 2. Compare CANITA (Algorithm 1) vs non-accelerated DIANA on smooth convex optimization
    # with decaying curvature spectrum lambda_c = L / (c + 1)^2 (ill-conditioned / non-strongly-convex regime)
    lambdas = [L / ((c + 1) ** 2) for c in range(d)]
    targets = [[(i - 3.5) * 1.2 + 0.4 * c for c in range(d)] for i in range(n)]
    x_star = [sum(targets[i][c] for i in range(n)) / n for c in range(d)]

    def f_global(x):
        return 0.5 * sum(lambdas[c] * ((x[c] - x_star[c]) ** 2) for c in range(d))

    def grad_i(i, x):
        return [lambdas[c] * (x[c] - targets[i][c]) for c in range(d)]

    x0 = [4.0] * d
    # Run CANITA (Algorithm 1) with step size eta = 1 / (L * (1 + 6 * omega / n))
    eta_step = 1.0 / (L * (1.0 + 6.0 * omega / n))
    x_c = x0[:]
    w_c = x0[:]
    z_c = x0[:]
    h_workers = [grad_i(i, x0) for i in range(n)]
    h_bar = [sum(h_workers[i][c] for i in range(n)) / n for c in range(d)]

    for t in range(150):
        theta_t = 2.0 / (t + 2.0)
        y_t = [theta_t * x_c[c] + (1.0 - theta_t) * w_c[c] for c in range(d)]
        c_y_list = []
        c_w_list = []
        for i in range(n):
            c_y = rand_k_compress(vec_sub(grad_i(i, y_t), h_workers[i]), k, rng)
            c_w = rand_k_compress(vec_sub(grad_i(i, w_c), h_workers[i]), k, rng)
            h_workers[i] = vec_add(h_workers[i], vec_scale(c_w, alpha_t))
            c_y_list.append(c_y)
            c_w_list.append(c_w)
        g_t = [h_bar[c] + sum(c_y_list[i][c] for i in range(n)) / n for c in range(d)]
        h_bar = [h_bar[c] + alpha_t * sum(c_w_list[i][c] for i in range(n)) / n for c in range(d)]
        x_c = [x_c[c] - (eta_step / theta_t) * g_t[c] for c in range(d)]
        z_c = [theta_t * x_c[c] + (1.0 - theta_t) * w_c[c] for c in range(d)]
        w_c = z_c[:] if p_t >= 0.5 else [p_t * z_c[c] + (1.0 - p_t) * w_c[c] for c in range(d)]

    # Run non-accelerated DIANA with identical base step size eta_step
    x_d = x0[:]
    h_d = [grad_i(i, x0) for i in range(n)]
    h_d_bar = [sum(h_d[i][c] for i in range(n)) / n for c in range(d)]
    for _ in range(150):
        c_list = [rand_k_compress(vec_sub(grad_i(i, x_d), h_d[i]), k, rng) for i in range(n)]
        g_d = [h_d_bar[c] + sum(c_list[i][c] for i in range(n)) / n for c in range(d)]
        for i in range(n):
            h_d[i] = vec_add(h_d[i], vec_scale(c_list[i], alpha_t))
        h_d_bar = [h_d_bar[c] + alpha_t * sum(c_list[i][c] for i in range(n)) / n for c in range(d)]
        x_d = [x_d[c] - eta_step * g_d[c] for c in range(d)]

    err_canita = f_global(z_c)
    err_diana = f_global(x_d)
    assert err_canita < 1e-4 * f_global(x0)
    assert err_canita < 0.05 * err_diana

    print(
        f"[PASS] Round 560 CANITA verified: eq27={eq27:.4f}, b={b:.4f}, "
        f"err_canita={err_canita:.3e} < err_diana={err_diana:.3e}"
    )


if __name__ == "__main__":
    main()
