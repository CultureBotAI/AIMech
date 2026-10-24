#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 571: ProxSkip-VR and ProxSkip-HUB."""

import math
import random


def main() -> None:
    random.seed(571)
    # 1. Verify Lemma 3 minibatch expected smoothness constant L(tau) and Equation (15) Cost Ratio:
    # L(tau) = ((m - tau) / (tau * (m - 1))) * L_max + (m * (tau - 1) / (tau * (m - 1))) * L
    m = 64
    L = 1.0
    L_max = 4.0
    mu = 1e-3

    # Check boundary cases tau = 1 -> L(1) = L_max, tau = m -> L(m) = L, and monotonicity in tau:
    def L_tau(tau: int) -> float:
        return ((m - tau) / (tau * (m - 1))) * L_max + (
            m * (tau - 1) / (tau * (m - 1))
        ) * L

    assert abs(L_tau(1) - L_max) < 1e-12
    assert abs(L_tau(m) - L) < 1e-12
    for tau in range(1, m):
        assert L_tau(tau) >= L_tau(tau + 1) >= L

    # Check Equation (15) Cost ratio(delta) = (sqrt(mu*L) + m*L*delta) / (sqrt(mu*L(tau)) + (2*m*mu + (2*L(tau) - 2*mu)*tau)*delta)
    tau = 4
    lt = L_tau(tau)

    def cost_ratio(delta: float) -> float:
        num = math.sqrt(mu * L) + m * L * delta
        den = math.sqrt(mu * lt) + (2.0 * m * mu + (2.0 * lt - 2.0 * mu) * tau) * delta
        return num / den

    r0 = cost_ratio(0.0)
    r_high = cost_ratio(0.1)
    r_inf = (m * L) / (2.0 * (m * mu + (lt - mu) * tau))
    assert abs(r0 - math.sqrt(L / lt)) < 1e-12
    assert r0 < 1.0 < r_high < r_inf
    assert r_high > 2.5, f"Expected substantial speedup for delta=0.1, got {r_high}"

    # 2. Verify Theorem 9 (ProxSkip-HUB) Assumption 4 parameters and Lyapunov contraction:
    # A = 4 * (L(tau) + (omega / tau) * L_max), B = 4 * (1 + omega / tau), C = 0
    # A_tilde = q * L_max, B_tilde = 1 - q, C_tilde = 0
    # W = 2 * B / (1 - B_tilde) = 8 * (1 + omega / tau) / q -> beta = (B + W * B_tilde) / W = 1 - q / 2
    omega = 1.0
    q = 0.2
    A_hub = 4.0 * (lt + (omega / tau) * L_max)
    B_hub = 4.0 * (1.0 + omega / tau)
    A_tilde = q * L_max
    B_tilde = 1.0 - q
    W = 2.0 * B_hub / (1.0 - B_tilde)
    beta = (B_hub + W * B_tilde) / W
    assert abs(beta - (1.0 - 0.5 * q)) < 1e-12
    gamma_max = min(1.0 / mu, 1.0 / (A_hub + W * A_tilde))
    assert gamma_max > 0.0

    # 3. Simulate ProxSkip-HUB (Algorithm 2) on a consensus problem with M = 3 hubs, m = 4 clients per hub, d = 4
    M = 3
    m_clients = 4
    tau_sim = 2
    d = 4
    mu_s = 0.4
    L_s = 1.6
    # Construct local client functions phi_{i,j}(x_i) = 0.5 * mu_s ||x_i||^2 + <b_{i,j}, x_i>
    # with sum_{i=1}^M sum_{j=1}^m_clients b_{i,j} = 0 so consensus optimum is x* = 0,
    # and h*_i = nabla phi_i(0) != 0
    raw_b = [
        [[random.uniform(-1.5, 1.5) for _ in range(d)] for _ in range(m_clients)]
        for _ in range(M)
    ]
    global_mean = [
        sum(raw_b[i][j][k] for i in range(M) for j in range(m_clients))
        / (M * m_clients)
        for k in range(d)
    ]
    b_ij = [
        [
            [raw_b[i][j][k] - global_mean[k] for k in range(d)]
            for j in range(m_clients)
        ]
        for i in range(M)
    ]
    h_star = [
        [sum(b_ij[i][j][k] for j in range(m_clients)) / m_clients for k in range(d)]
        for i in range(M)
    ]

    def grad_ij(i: int, j: int, xi: list[float]) -> list[float]:
        return [mu_s * xi[k] + b_ij[i][j][k] for k in range(d)]

    def grad_hub(i: int, xi: list[float]) -> list[float]:
        return [mu_s * xi[k] + h_star[i][k] for k in range(d)]

    # Unbiased Rand-2 compressor on R^4 (omega = d/k - 1 = 1.0)
    def rand2_compress(vec: list[float]) -> list[float]:
        chosen = random.sample(range(d), 2)
        out = [0.0] * d
        for k in chosen:
            out[k] = 2.0 * vec[k]
        return out

    gamma = 0.08
    p_comm = 0.35
    q_vr = 0.25

    x_hubs = [[1.5, -1.0, 0.8, -0.5] for _ in range(M)]
    y_hubs = [list(x_hubs[i]) for i in range(M)]
    h_hubs = [[0.0] * d for _ in range(M)]

    for t in range(1200):
        x_hat = []
        for i in range(M):
            subset = random.sample(range(m_clients), tau_sim)
            delta_hat = [0.0] * d
            for j in subset:
                g_x = grad_ij(i, j, x_hubs[i])
                g_y = grad_ij(i, j, y_hubs[i])
                comp = rand2_compress([g_x[k] - g_y[k] for k in range(d)])
                for k in range(d):
                    delta_hat[k] += comp[k] / tau_sim
            g_y_full = grad_hub(i, y_hubs[i])
            g_hat_i = [delta_hat[k] + g_y_full[k] for k in range(d)]
            x_hat.append(
                [x_hubs[i][k] - gamma * (g_hat_i[k] - h_hubs[i][k]) for k in range(d)]
            )

        # Coin flip theta_t ~ Bernoulli(p_comm) for consensus prox step
        if random.random() < p_comm:
            # prox of consensus indicator r is averaging (x_hat_i - (gamma/p) h_i) across hubs
            avg_vec = [
                sum(x_hat[i][k] - (gamma / p_comm) * h_hubs[i][k] for i in range(M)) / M
                for k in range(d)
            ]
            x_next = [list(avg_vec) for _ in range(M)]
        else:
            x_next = [list(x_hat[i]) for i in range(M)]

        for i in range(M):
            h_hubs[i] = [
                h_hubs[i][k] + (p_comm / gamma) * (x_next[i][k] - x_hat[i][k])
                for k in range(d)
            ]

        # Coin flip for control vector y_{t+1}
        if random.random() < q_vr:
            y_hubs = [list(x_next[i]) for i in range(M)]

        x_hubs = x_next

    err_x = sum(sum(v * v for v in x_hubs[i]) for i in range(M)) / M
    err_h = (
        sum(
            sum((h_hubs[i][k] - h_star[i][k]) ** 2 for k in range(d))
            for i in range(M)
        )
        / M
    )
    assert err_x < 1e-10 and err_h < 1e-8, (
        f"Expected ProxSkip-HUB to converge linearly to exact consensus optimum: err_x={err_x}, err_h={err_h}"
    )
    print(
        f"[PASS] Round 571 ProxSkip-VR/HUB verified: cost_ratio(0)={r0:.4f}<1<{r_high:.2f}<{r_inf:.2f}, "
        f"err_x={err_x:.3e}, err_h={err_h:.3e}"
    )


if __name__ == "__main__":
    main()
