#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 595: AdGD (Malitsky & Mishchenko, ICML 2020)."""

from __future__ import annotations

import math


def test_adgd_lemma1_lyapunov_and_locally_smooth_convex() -> tuple[float, float, float]:
    """Verify Algorithm 1, Lemma 1 Eq. (5) Lyapunov decrease, and Theorem 1 ergodic rate on locally smooth f."""
    # Locally smooth convex function with global smoothness L = infinity:
    # f(x) = exp(x) - x - 1 + 0.25 * x^4, unique minimum at x* = 0 with f* = 0.
    def f(x: float) -> float:
        return math.exp(x) - x - 1.0 + 0.25 * (x**4)

    def grad_f(x: float) -> float:
        return math.exp(x) - 1.0 + x**3

    x0 = 2.5
    lam0 = 1e-4
    x1 = x0 - lam0 * grad_f(x0)

    xs = [x0, x1]
    lams = [lam0]
    thetas = [float("inf")]

    max_lyapunov_diff = 0.0
    prev_energy = None

    for k in range(1, 80):
        xk = xs[k]
        xk_prev = xs[k - 1]
        gk = grad_f(xk)
        gk_prev = grad_f(xk_prev)
        dg = abs(gk - gk_prev)
        lip_est = abs(xk - xk_prev) / (2.0 * dg) if dg > 0.0 else float("inf")
        if k == 1:
            lam_k = lip_est
        else:
            lam_k = min(math.sqrt(1.0 + thetas[-1]) * lams[-1], lip_est)
        theta_k = lam_k / lams[-1]
        xk_next = xk - lam_k * gk

        # Lemma 1 Eq. (5):
        # LHS = ||x^{k+1} - x*||^2 + 0.5 ||x^{k+1} - x^k||^2 + 2 lam_k (1 + theta_k) (f(x^k) - f*)
        # RHS = ||x^k - x*||^2 + 0.5 ||x^k - x^{k-1}||^2 + 2 lam_k theta_k (f(x^{k-1}) - f*)
        lhs = (xk_next**2) + 0.5 * ((xk_next - xk) ** 2) + 2.0 * lam_k * (1.0 + theta_k) * f(xk)
        rhs = (xk**2) + 0.5 * ((xk - xk_prev) ** 2) + 2.0 * lam_k * theta_k * f(xk_prev)
        assert lhs <= rhs + 1e-12, f"Lemma 1 violated at k={k}: lhs={lhs} > rhs={rhs}"
        max_lyapunov_diff = max(max_lyapunov_diff, lhs - rhs)

        if prev_energy is not None:
            # Because lam_k * theta_k = lam_k^2 / lam_{k-1} <= (1 + theta_{k-1}) lam_{k-1},
            # rhs <= prev_energy!
            assert rhs <= prev_energy + 1e-12
        prev_energy = lhs

        xs.append(xk_next)
        lams.append(lam_k)
        thetas.append(theta_k)

    # Verify Theorem 1 ergodic rate f(x_hat^k) - f* <= D / (2 S_k)
    k_final = len(lams) - 1
    lam1 = lams[1]
    theta1 = thetas[1]
    D = (xs[1] ** 2) + 0.5 * ((xs[1] - xs[0]) ** 2) + 2.0 * lam1 * theta1 * f(xs[0])
    weights = [
        lams[i] * (1.0 + thetas[i]) - lams[i + 1] * thetas[i + 1]
        for i in range(1, k_final)
    ]
    assert all(w >= -1e-12 for w in weights), "Expected nonnegative ergodic weights"
    S_k = lams[k_final] * (1.0 + thetas[k_final]) + sum(weights)
    x_hat = (
        lams[k_final] * (1.0 + thetas[k_final]) * xs[k_final]
        + sum(w * xs[i] for i, w in enumerate(weights, start=1))
    ) / S_k
    ergodic_val = f(x_hat)
    bound_val = D / (2.0 * S_k)
    assert ergodic_val <= bound_val + 1e-12, f"Expected {ergodic_val} <= {bound_val}"
    assert abs(xs[-1]) < 1e-8, f"Expected last iterate near 0, got {xs[-1]}"
    return max_lyapunov_diff, ergodic_val, bound_val


def test_adgd_vs_fixed_gd_ill_conditioned() -> tuple[float, float]:
    """Compare AdGD (Algorithm 1) against fixed-step GD on cubic-regularized objective (Section 4, p. 9)."""
    delta = 0.05
    M = 20.0
    x0 = [2.0, 2.0]
    steps = 250

    def grad(p: list[float]) -> list[float]:
        r = math.hypot(p[0], p[1])
        return [p[0] + 0.5 * M * r * p[0], delta * p[1] + 0.5 * M * r * p[1]]

    def loss(p: list[float]) -> float:
        r = math.hypot(p[0], p[1])
        return 0.5 * (p[0] ** 2) + 0.5 * delta * (p[1] ** 2) + (M / 6.0) * (r**3)

    # Fixed-step GD using initial sublevel smoothness L_0 = 1 + M * ||x^0||
    L_init = 1.0 + M * math.hypot(x0[0], x0[1])
    p_gd = x0[:]
    for _ in range(steps):
        g = grad(p_gd)
        p_gd = [p_gd[0] - (1.0 / L_init) * g[0], p_gd[1] - (1.0 / L_init) * g[1]]
    loss_gd = loss(p_gd)

    # AdGD starting from tiny lam0 = 1e-10 (Section 2.1, p. 4)
    p_prev = x0[:]
    lam_prev = 1e-10
    theta_prev = float("inf")
    g_prev = grad(p_prev)
    p_curr = [p_prev[0] - lam_prev * g_prev[0], p_prev[1] - lam_prev * g_prev[1]]
    max_lam = lam_prev

    for k in range(1, steps):
        g_curr = grad(p_curr)
        dx = math.hypot(p_curr[0] - p_prev[0], p_curr[1] - p_prev[1])
        dg = math.hypot(g_curr[0] - g_prev[0], g_curr[1] - g_prev[1])
        lip_step = dx / (2.0 * dg) if dg > 0 else float("inf")
        lam_curr = lip_step if k == 1 else min(math.sqrt(1.0 + theta_prev) * lam_prev, lip_step)
        max_lam = max(max_lam, lam_curr)
        theta_curr = lam_curr / lam_prev
        p_next = [p_curr[0] - lam_curr * g_curr[0], p_curr[1] - lam_curr * g_curr[1]]
        p_prev, p_curr = p_curr, p_next
        g_prev = g_curr
        lam_prev, theta_prev = lam_curr, theta_curr

    loss_adgd = loss(p_curr)
    assert max_lam > 20.0 * (1.0 / L_init), f"Expected AdGD stepsize >> 1/L_init, got {max_lam}"
    assert loss_adgd < 1e-6 * loss_gd, f"Expected AdGD ({loss_adgd}) << fixed GD ({loss_gd})"
    return loss_adgd, loss_gd


def main() -> None:
    lyap_diff, erg_val, bound_val = test_adgd_lemma1_lyapunov_and_locally_smooth_convex()
    loss_adgd, loss_gd = test_adgd_vs_fixed_gd_ill_conditioned()
    print(
        f"[PASS] Round 595 AdGD verified: lyap_diff={lyap_diff:.2e}<=0, "
        f"ergodic=({erg_val:.4e}<={bound_val:.4e}), loss_adgd={loss_adgd:.4e}<<loss_gd={loss_gd:.4e}"
    )


if __name__ == "__main__":
    main()
