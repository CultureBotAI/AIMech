#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 602: Adan (Adaptive Nesterov Momentum Algorithm)."""

from __future__ import annotations

import math
import random


def verify_lemma1_agd_nme_equivalence() -> float:
    """Verify Lemma 1 (p. 4, 18): exact trajectory equivalence between vanilla AGD and AGD-II (NME)."""
    # Objective f(theta) = 0.5 * sum_i a_i (theta_i - b_i)^2 + 0.1 * sum_i sin(theta_i)
    dim = 6
    a = [1.5, 2.5, 0.8, 3.2, 1.1, 2.0]
    b = [0.4, -0.7, 1.2, -0.3, 0.9, -1.1]

    def grad_f(theta: list[float]) -> list[float]:
        return [a[i] * (theta[i] - b[i]) + 0.1 * math.cos(theta[i]) for i in range(dim)]

    eta = 0.05
    beta1 = 0.1
    alpha = 1.0 - beta1
    steps = 30

    theta_agd = [1.0, -1.0, 0.5, -0.5, 1.5, -1.2]
    m_agd = [0.0] * dim

    # Initialize AGD-II at step k = 1 from AGD's extrapolation point theta_bar_1 = theta_1 - eta * alpha * m_0
    # Step 0 of AGD:
    theta_ext_0 = [theta_agd[i] - eta * alpha * m_agd[i] for i in range(dim)]
    g0 = grad_f(theta_ext_0)
    m_agd = [alpha * m_agd[i] + g0[i] for i in range(dim)]
    theta_agd = [theta_agd[i] - eta * m_agd[i] for i in range(dim)]

    # Corresponding AGD-II state after step k = 0 (with m_{-1} = 0 => m_bar_0 = (1 + alpha) g_0):
    theta_bar = [theta_agd[i] - eta * alpha * m_agd[i] for i in range(dim)]
    g_bar_prev = list(g0)
    m_bar = [(1.0 + alpha) * g0[i] for i in range(dim)]

    max_equiv_err = 0.0
    for _ in range(1, steps):
        # Vanilla AGD step
        theta_ext = [theta_agd[i] - eta * alpha * m_agd[i] for i in range(dim)]
        gk = grad_f(theta_ext)
        m_agd = [alpha * m_agd[i] + gk[i] for i in range(dim)]
        theta_agd = [theta_agd[i] - eta * m_agd[i] for i in range(dim)]
        target_theta_bar = [theta_agd[i] - eta * alpha * m_agd[i] for i in range(dim)]

        # AGD-II (NME) step (Eq. 9-10, p. 18): evaluates gradient only at current iterate theta_bar
        g_bar = grad_f(theta_bar)
        g_prime = [g_bar[i] + alpha * (g_bar[i] - g_bar_prev[i]) for i in range(dim)]
        m_bar = [alpha * m_bar[i] + g_prime[i] for i in range(dim)]
        theta_bar = [theta_bar[i] - eta * m_bar[i] for i in range(dim)]
        g_bar_prev = g_bar

        err = max(abs(theta_bar[i] - target_theta_bar[i]) for i in range(dim))
        if err > max_equiv_err:
            max_equiv_err = err

    assert max_equiv_err < 1e-14, f"Lemma 1 AGD vs AGD-II equivalence error too large: {max_equiv_err}"
    return max_equiv_err


def verify_decoupled_moments_and_proximal_decay() -> tuple[float, float, float, float, float]:
    """Verify Eq. (4)-(5), Proposition 2-3 bounds, and Adan vs AdamW optimization."""
    rng = random.Random(60201)
    dim = 8
    T = 25
    beta1, beta2, beta3 = 0.08, 0.12, 0.05
    eps = 1e-4
    c_inf = 3.0  # ||g_k||_inf <= c_inf / 3 = 1.0 (Assumption 2, p. 5)

    g0 = [rng.uniform(-1.0, 1.0) for _ in range(dim)]
    m = list(g0)
    v = [0.0] * dim
    n = [gi * gi for gi in g0]
    eta = 0.02
    eta_vec_prev = [eta / (math.sqrt(ni) + eps) for ni in n]
    g_prev = list(g0)
    g_hist = [list(g0)]

    max_eq4_err = 0.0
    max_prop3_ratio = 0.0
    prop3_bound = math.sqrt(2.0 * beta3) * c_inf / eps

    for k in range(1, T + 1):
        gk = [rng.uniform(-1.0, 1.0) for _ in range(dim)]
        g_hist.append(list(gk))
        m = [(1.0 - beta1) * m[i] + beta1 * gk[i] for i in range(dim)]
        v = [(1.0 - beta2) * v[i] + beta2 * (gk[i] - g_prev[i]) for i in range(dim)]
        g_prime = [gk[i] + (1.0 - beta2) * (gk[i] - g_prev[i]) for i in range(dim)]
        n = [(1.0 - beta3) * n[i] + beta3 * (g_prime[i] ** 2) for i in range(dim)]
        eta_vec = [eta / (math.sqrt(ni) + eps) for ni in n]

        # Check Eq. (4) explicit weighted sum identity
        for i in range(dim):
            explicit_sum = 0.0
            for t in range(k + 1):
                c_kt = ((1.0 - beta1) ** k) if t == 0 else beta1 * ((1.0 - beta1) ** (k - t))
                cp_kt = ((1.0 - beta2) ** k) if t == 0 else beta2 * ((1.0 - beta2) ** (k - t))
                diff_t = 0.0 if t == 0 else (g_hist[t][i] - g_hist[t - 1][i])
                explicit_sum += c_kt * g_hist[t][i] + (1.0 - beta2) * cp_kt * diff_t
            err = abs((m[i] + (1.0 - beta2) * v[i]) - explicit_sum)
            if err > max_eq4_err:
                max_eq4_err = err

        # Check Proposition 2: ||m_k||_inf <= c_inf, ||n_k||_inf <= c_inf^2
        assert max(abs(mi) for mi in m) <= c_inf + 1e-12
        assert max(ni for ni in n) <= (c_inf ** 2) + 1e-12

        # Check Proposition 3: ||(eta_k - eta_{k-1}) / eta_{k-1}||_inf <= sqrt(2 beta_3) c_inf / eps
        rel_eta = max(abs((eta_vec[i] - eta_vec_prev[i]) / eta_vec_prev[i]) for i in range(dim))
        assert rel_eta <= prop3_bound + 1e-12
        if rel_eta / prop3_bound > max_prop3_ratio:
            max_prop3_ratio = rel_eta / prop3_bound

        eta_vec_prev = eta_vec
        g_prev = gk

    assert max_eq4_err < 1e-14, f"Eq. (4) expansion mismatch: {max_eq4_err}"

    # Verify Eq. (5) proximal weight decay optimality condition (Eq. 11, p. 19)
    theta_k = [0.7, -1.2, 0.3, 1.5, -0.8, 0.4, -0.6, 1.1]
    u_k = [m[i] + (1.0 - beta2) * v[i] for i in range(dim)]
    lam_k = 0.05
    theta_next = [(theta_k[i] - eta_vec_prev[i] * u_k[i]) / (1.0 + lam_k * eta) for i in range(dim)]
    # First-order optimality of argmin_theta { (lam_k/2) ||theta||^2_{sqrt(n_k)} + <u_k, theta - theta_k> + (1/(2 eta)) ||theta - theta_k||^2_{sqrt(n_k)} }
    prox_grad_err = max(
        abs(
            lam_k * (math.sqrt(n[i]) + eps) * theta_next[i]
            + u_k[i]
            + ((math.sqrt(n[i]) + eps) / eta) * (theta_next[i] - theta_k[i])
        )
        for i in range(dim)
    )
    assert prox_grad_err < 1e-12, f"Eq. (5) proximal optimality error: {prox_grad_err}"

    # Compare Adan vs AdamW on ill-conditioned quartic + quadratic regularized objective
    scales = [1.0 + 3.0 * i for i in range(dim)]

    def loss_and_grad(th: list[float]) -> tuple[float, list[float]]:
        val = 0.0
        g = [0.0] * dim
        for i in range(dim):
            d_i = th[i] - 1.0
            val += 0.5 * scales[i] * (d_i ** 2) + 0.1 * (d_i ** 4)
            g[i] = scales[i] * d_i + 0.4 * (d_i ** 3)
        return val, g

    # Run Adan (Algorithm 1 with bias correction)
    th_adan = [-1.5] * dim
    _, g0_a = loss_and_grad(th_adan)
    m_a = [0.0] * dim
    v_a = [0.0] * dim
    n_a = [0.0] * dim
    g_prev_a = list(g0_a)
    b1, b2, b3, lr_a, wd = 0.08, 0.08, 0.01, 0.08, 0.001
    for t in range(1, 151):
        _, g = loss_and_grad(th_adan)
        diff = [g[i] - g_prev_a[i] for i in range(dim)] if t > 1 else [0.0] * dim
        m_a = [(1.0 - b1) * m_a[i] + b1 * g[i] for i in range(dim)]
        v_a = [(1.0 - b2) * v_a[i] + b2 * diff[i] for i in range(dim)]
        gp = [g[i] + (1.0 - b2) * diff[i] for i in range(dim)]
        n_a = [(1.0 - b3) * n_a[i] + b3 * (gp[i] ** 2) for i in range(dim)]
        m_hat = [m_a[i] / (1.0 - (1.0 - b1) ** t) for i in range(dim)]
        v_hat = [v_a[i] / (1.0 - (1.0 - b2) ** t) for i in range(dim)]
        n_hat = [n_a[i] / (1.0 - (1.0 - b3) ** t) for i in range(dim)]
        for i in range(dim):
            step_i = lr_a / (math.sqrt(n_hat[i]) + 1e-8)
            th_adan[i] = (th_adan[i] - step_i * (m_hat[i] + (1.0 - b2) * v_hat[i])) / (1.0 + wd * lr_a)
        g_prev_a = g

    # Run AdamW with same lr and comparable decay rates
    th_adamw = [-1.5] * dim
    m_w = [0.0] * dim
    n_w = [0.0] * dim
    for t in range(1, 151):
        _, g = loss_and_grad(th_adamw)
        m_w = [(1.0 - b1) * m_w[i] + b1 * g[i] for i in range(dim)]
        n_w = [(1.0 - b3) * n_w[i] + b3 * (g[i] ** 2) for i in range(dim)]
        m_hat = [m_w[i] / (1.0 - (1.0 - b1) ** t) for i in range(dim)]
        n_hat = [n_w[i] / (1.0 - (1.0 - b3) ** t) for i in range(dim)]
        for i in range(dim):
            step_i = lr_a / (math.sqrt(n_hat[i]) + 1e-8)
            th_adamw[i] = th_adamw[i] * (1.0 - wd * lr_a) - step_i * m_hat[i]

    loss_adan, _ = loss_and_grad(th_adan)
    loss_adamw, _ = loss_and_grad(th_adamw)
    assert loss_adan < loss_adamw, f"Expected Adan loss < AdamW loss: {loss_adan} vs {loss_adamw}"
    return max_eq4_err, prox_grad_err, max_prop3_ratio, loss_adan, loss_adamw


def main() -> None:
    lemma1_err = verify_lemma1_agd_nme_equivalence()
    eq4_err, prox_err, prop3_ratio, loss_adan, loss_adamw = verify_decoupled_moments_and_proximal_decay()
    print(
        f"[PASS] Round 602 Adan verified: lemma1_err={lemma1_err:.2e}, "
        f"eq4_err={eq4_err:.2e}, prox_err={prox_err:.2e}, prop3_ratio={prop3_ratio:.4f}<=1, "
        f"loss_adan={loss_adan:.4e}<loss_adamw={loss_adamw:.4e}"
    )


if __name__ == "__main__":
    main()
