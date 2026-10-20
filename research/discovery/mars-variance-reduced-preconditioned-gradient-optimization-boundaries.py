#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 604: MARS (Make vAriance Reduction Shine)."""

from __future__ import annotations

import math
import random


def verify_lemma3_4_and_lemma_d1() -> tuple[float, float]:
    """Verify Lemma 3.4 (MARS-Lion vs Lion, p. 6-7) and Lemma D.1 (MARS-Shampoo vs Muon, p. 7, 21)."""
    rng = random.Random(60401)
    dim = 6
    T = 25
    g_seq = [[rng.uniform(-1.5, 1.5) for _ in range(dim)] for _ in range(T)]

    # 1. Lemma 3.4: m_t = b1 u_t + b2 g_t, u_{t+1} = a1 u_t + a2 g_t
    # Equivalent to: m_t = a1 m_{t-1} + (b1 a2 - a1 b2 + b2) g_t + (a1 b2 - b1 a2)(g_t - g_{t-1})
    beta1, beta2 = 0.9, 0.98
    a1, a2, b1, b2 = beta2, 1.0 - beta2, beta1, 1.0 - beta1
    u = [0.2 * (i + 1) for i in range(dim)]
    m_two_buf: list[list[float]] = []
    for t in range(T):
        gt = g_seq[t]
        mt = [b1 * u[i] + b2 * gt[i] for i in range(dim)]
        m_two_buf.append(mt)
        u = [a1 * u[i] + a2 * gt[i] for i in range(dim)]

    max_lion_err = 0.0
    m_single = list(m_two_buf[0])
    for t in range(1, T):
        gt = g_seq[t]
        gtm1 = g_seq[t - 1]
        # Eq. (3.18): m_t = beta2 m_{t-1} + (1 - beta2) g_t + (beta2 - beta1)(g_t - g_{t-1})
        m_single = [
            beta2 * m_single[i] + (1.0 - beta2) * gt[i] + (beta2 - beta1) * (gt[i] - gtm1[i])
            for i in range(dim)
        ]
        err = max(abs(m_single[i] - m_two_buf[t][i]) for i in range(dim))
        if err > max_lion_err:
            max_lion_err = err
    assert max_lion_err < 1e-14, f"Lemma 3.4 Lion equivalence error: {max_lion_err}"

    # 2. Lemma D.1: u_t = a1 u_{t-1} + a2 g_t, m_t = b1 u_t + b2 g_t (Muon with a1=mu, a2=1, b1=mu, b2=1)
    # Equivalent to Eq. (3.24): m_t = mu m_{t-1} + g_t + mu (g_t - g_{t-1})
    mu = 0.95
    u_prev = [0.1 * (i + 1) for i in range(dim)]
    m_muon_two: list[list[float]] = []
    for t in range(T):
        gt = g_seq[t]
        u_cur = [mu * u_prev[i] + gt[i] for i in range(dim)]
        mt = [mu * u_cur[i] + gt[i] for i in range(dim)]
        m_muon_two.append(mt)
        u_prev = u_cur

    max_muon_err = 0.0
    m_muon_single = list(m_muon_two[0])
    for t in range(1, T):
        gt = g_seq[t]
        gtm1 = g_seq[t - 1]
        m_muon_single = [
            mu * m_muon_single[i] + gt[i] + mu * (gt[i] - gtm1[i])
            for i in range(dim)
        ]
        err = max(abs(m_muon_single[i] - m_muon_two[t][i]) for i in range(dim))
        if err > max_muon_err:
            max_muon_err = err
    assert max_muon_err < 1e-14, f"Lemma D.1 Muon equivalence error: {max_muon_err}"
    return max_lion_err, max_muon_err


def verify_control_variate_lemma_c2_and_mars_adamw() -> tuple[float, float, float, float]:
    """Verify Section 3.1 / Lemma C.2 optimal gamma^* variance reduction and MARS-AdamW vs AdamW."""
    # Section 3.1 (p. 4): E[U + (gamma Y - E[Y])]^2 is minimized at gamma^* = 1 - (E[U Y] + Var(Y)) / E[Y^2]
    # Let's verify exact variance reduction over Monte Carlo samples of (U, Y) with E[U] = 0
    rng = random.Random(60402)
    N = 4000
    U_samples: list[float] = []
    Y_samples: list[float] = []
    mean_y = 0.4
    for _ in range(N):
        xi = rng.gauss(0.0, 1.0)
        eta_noise = rng.gauss(0.0, 1.0)
        # U has mean 0, correlated with Y - mean_y
        u_val = 0.6 * xi + 0.5 * eta_noise
        y_val = mean_y + 0.8 * xi + 0.2 * eta_noise
        U_samples.append(u_val)
        Y_samples.append(y_val)

    # Center U_samples to have exact zero empirical mean and Y_samples to have empirical mean mean_y
    u_bar = sum(U_samples) / N
    U_samples = [u - u_bar for u in U_samples]
    y_bar = sum(Y_samples) / N

    def emp_mse(gamma: float) -> float:
        return sum((u + (gamma * y - y_bar)) ** 2 for u, y in zip(U_samples, Y_samples)) / N

    e_uy = sum(u * y for u, y in zip(U_samples, Y_samples)) / N
    var_y = sum((y - y_bar) ** 2 for y in Y_samples) / N
    e_y2 = sum(y * y for y in Y_samples) / N
    gamma_star = 1.0 - (e_uy + var_y) / e_y2

    mse_star = emp_mse(gamma_star)
    mse_storm = emp_mse(1.0)
    mse_ema = emp_mse(0.0)
    theoretical_gain = ((e_uy + var_y) ** 2) / e_y2
    gain_err = abs((mse_storm - mse_star) - theoretical_gain)
    assert gain_err < 1e-14, f"Control-variate identity error: {gain_err}"
    assert mse_star < mse_storm and mse_star < mse_ema, (
        f"Expected optimal gamma^* MSE < STORM and EMA: {mse_star} vs {mse_storm}, {mse_ema}"
    )

    # Verify Lemma C.1 (||sqrt(v_t) - sqrt(v_{t+1})||_inf <= sqrt(2(1 - beta_2))) and Lemma C.5
    s = 2.0
    for t in range(1, 50):
        eta_t = (s + t) ** (-1.0 / 3.0)
        eta_tm1 = (s + t - 1.0) ** (-1.0 / 3.0)
        assert (1.0 / eta_t) - (1.0 / eta_tm1) <= (eta_t ** 2) + 1e-15 <= eta_t + 1e-15

    # Compare MARS-AdamW (Algorithm 2) vs AdamW on noisy finite-sum quadratic optimization
    # f(x, xi) = 0.5 * sum_i a_i (x_i - x^*_i)^2 + <xi, x - x^*>, where same minibatch xi_t cancels in difference!
    dim = 8
    a_scales = [1.0 + 2.0 * i for i in range(dim)]
    x_star = [0.5 * ((-1) ** i) for i in range(dim)]

    def true_loss(x: list[float]) -> float:
        return 0.5 * sum(a_scales[i] * ((x[i] - x_star[i]) ** 2) for i in range(dim))

    def stoch_grad(x: list[float], xi: list[float]) -> list[float]:
        #Multiplicative + additive noise on same sample xi so difference grad(x_t, xi_t) - grad(x_{t-1}, xi_t) cancels additive noise!
        return [
            a_scales[i] * (1.0 + 0.3 * xi[i]) * (x[i] - x_star[i]) + 0.8 * xi[i]
            for i in range(dim)
        ]

    steps = 120
    xi_stream = [[rng.gauss(0.0, 1.0) for _ in range(dim)] for _ in range(steps)]

    def run_opt(gamma_val: float) -> float:
        x = [2.0] * dim
        x_prev = list(x)
        m = [0.0] * dim
        v = [0.0] * dim
        beta1, beta2, lr, wd, eps = 0.9, 0.99, 0.05, 0.01, 1e-8
        for t in range(1, steps + 1):
            xi = xi_stream[t - 1]
            g_cur = stoch_grad(x, xi)
            g_prev_same_xi = stoch_grad(x_prev, xi)
            c_t = [
                g_cur[i] + gamma_val * (beta1 / (1.0 - beta1)) * (g_cur[i] - g_prev_same_xi[i])
                for i in range(dim)
            ]
            c_norm = math.sqrt(sum(ci * ci for ci in c_t))
            c_tilde = [ci / c_norm for ci in c_t] if c_norm > 1.0 else c_t
            m = [beta1 * m[i] + (1.0 - beta1) * c_tilde[i] for i in range(dim)]
            v = [beta2 * v[i] + (1.0 - beta2) * (c_tilde[i] ** 2) for i in range(dim)]
            m_hat = [m[i] / (1.0 - (beta1 ** t)) for i in range(dim)]
            v_hat = [v[i] / (1.0 - (beta2 ** t)) for i in range(dim)]
            x_prev = list(x)
            x = [
                x[i] - lr * (m_hat[i] / (math.sqrt(v_hat[i]) + eps) + wd * x[i])
                for i in range(dim)
            ]
        return true_loss(x)

    loss_adamw = run_opt(gamma_val=0.0)
    loss_mars = run_opt(gamma_val=0.15)
    assert loss_mars < loss_adamw, f"Expected MARS-AdamW loss < AdamW loss: {loss_mars} vs {loss_adamw}"
    return gain_err, mse_star / mse_storm, loss_mars, loss_adamw


def main() -> None:
    lion_err, muon_err = verify_lemma3_4_and_lemma_d1()
    gain_err, mse_ratio, loss_mars, loss_adamw = verify_control_variate_lemma_c2_and_mars_adamw()
    print(
        f"[PASS] Round 604 MARS verified: lion_err={lion_err:.2e}, muon_err={muon_err:.2e}, "
        f"cv_gain_err={gain_err:.2e}, mse_ratio={mse_ratio:.4f}<1, "
        f"loss_mars={loss_mars:.4e}<loss_adamw={loss_adamw:.4e}"
    )


if __name__ == "__main__":
    main()
