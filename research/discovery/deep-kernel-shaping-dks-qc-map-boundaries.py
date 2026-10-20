#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 569: Deep Kernel Shaping (DKS)."""

import math


def main() -> None:
    # 1. Verify exact closed-form Q and C maps for ReLU (Eq. 15) and Erf (Section 12.2):
    # ReLU C map: C(c) = (sqrt(1 - c^2) + (pi - arccos(c))*c) / pi
    def c_relu(c: float) -> float:
        c_clamped = max(-1.0, min(1.0, c))
        return (
            math.sqrt(max(0.0, 1.0 - c_clamped * c_clamped))
            + (math.pi - math.acos(c_clamped)) * c_clamped
        ) / math.pi

    assert abs(c_relu(1.0) - 1.0) < 1e-12
    assert abs(c_relu(0.0) - 1.0 / math.pi) < 1e-12
    assert abs(c_relu(-1.0) - 0.0) < 1e-12

    # Verify ReLU C map degeneration at depth D = 100 (Section 12.1: maps [-1, 1] to [0.996, 1]):
    c_val = -1.0
    for _ in range(100):
        c_val = c_relu(c_val)
    assert 0.995 < c_val < 0.997, f"Expected C_relu^100(-1) ~ 0.996, got {c_val}"

    # 2. Verify Theorem 13 deviation bounds for a positive definite C map with C(0) = 0:
    # Consider a DKS-transformed layer whose C map has C_f(0) = 0, C_f(1) = 1, and C_f'(1) = psi.
    # For example, C_f(c) = b_1 * c + b_3 * c^3 with b_1, b_3 >= 0, b_1 + b_3 = 1,
    # so C_f(0) = 0, C_f'(0) = b_1, C_f'(1) = b_1 + 3*b_3 = 1 + 2*b_3 = psi.
    # Compose D = 50 layers with global slope bound zeta = 1.5 -> psi = zeta^(1/D).
    D = 50
    zeta = 1.5
    psi = zeta ** (1.0 / D)
    b3 = (psi - 1.0) / 2.0
    b1 = 1.0 - b3

    def c_layer(c: float) -> float:
        return b1 * c + b3 * (c ** 3)

    def c_net(c: float) -> float:
        val = c
        for _ in range(D):
            val = c_layer(val)
        return val

    # Compute C_net'(0) = b1^D and C_net'(1) = psi^D = zeta
    c_net_prime_0 = b1 ** D
    c_net_prime_1 = psi ** D
    assert abs(c_net_prime_1 - zeta) < 1e-12

    grid = [-1.0 + 2.0 * i / 1000 for i in range(1001)]
    max_val_dev = max(abs(c_net(c) - c) for c in grid)
    # Numerical derivative on interior grid
    eps = 1e-7
    max_slope_dev = max(
        abs((c_net(min(1.0, c + eps)) - c_net(max(-1.0, c - eps))) / (min(1.0, c + eps) - max(-1.0, c - eps)) - 1.0)
        for c in grid[1:-1]
    )

    # Verify Theorem 13 inequalities:
    # (1/4)*(1 - C_f'(0)) <= max |C_f(c) - c| <= 2*(1 - C_f'(0)) <= 2*(C_f'(1) - 1)
    # max |C_f'(c) - 1| <= 3*(C_f'(1) - 1)
    assert 0.25 * (1.0 - c_net_prime_0) <= max_val_dev + 1e-9
    assert max_val_dev <= 2.0 * (1.0 - c_net_prime_0) + 1e-9
    assert max_val_dev <= 2.0 * (c_net_prime_1 - 1.0) + 1e-9
    assert max_slope_dev <= 3.0 * (c_net_prime_1 - 1.0) + 1e-5

    # 3. Verify DKS 4-parameter activation transformation equations (Section 18.4)
    # using Gauss-Hermite / midpoint quadrature on [-10, 10] for tanh at D=100, zeta=1.5
    # Table in Section 18.7 gives for tanh (D=100, zeta=1.5):
    # alpha = 0.090438, beta = -0.56011, delta = 0.50500, gamma = 14.9025
    alpha = 0.090438
    beta = -0.56011
    n_quad = 2000
    a_int, b_int = -10.0, 10.0
    dx = (b_int - a_int) / n_quad
    xs = [a_int + (i + 0.5) * dx for i in range(n_quad)]
    weights = [math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi) * dx for x in xs]

    def E_gauss(fn) -> float:
        return sum(w * fn(x) for x, w in zip(xs, weights))

    delta = -E_gauss(lambda x: math.tanh(alpha * x + beta))
    var_phi = E_gauss(lambda x: (math.tanh(alpha * x + beta) + delta) ** 2)
    gamma = 1.0 / math.sqrt(var_phi)

    def phi_hat(x: float) -> float:
        return gamma * (math.tanh(alpha * x + beta) + delta)

    def phi_hat_prime(x: float) -> float:
        t = math.tanh(alpha * x + beta)
        return alpha * gamma * (1.0 - t * t)

    q_1 = E_gauss(lambda x: phi_hat(x) ** 2)
    q_prime_1 = E_gauss(lambda x: phi_hat(x) * phi_hat_prime(x) * x)
    c_0 = E_gauss(phi_hat) ** 2
    c_prime_1 = E_gauss(lambda x: phi_hat_prime(x) ** 2)
    target_psi_100 = 1.5 ** (1.0 / 100.0)

    assert abs(delta - 0.50500) < 1e-3
    assert abs(gamma - 14.9025) < 1e-2
    assert abs(q_1 - 1.0) < 1e-6
    assert abs(c_0 - 0.0) < 1e-10
    assert abs(q_prime_1 - 1.0) < 1e-3
    assert abs(c_prime_1 - target_psi_100) < 1e-4

    # 4. Verify Theorem 27 per-layer NTK bound: |Theta_i(x, x') - c_0| <= 11*(zeta - 1)
    for i_layer in [1, 25, 50]:
        c0 = -0.4
        # Subnetwork g_i has i_layer - 1 layers, h_i has D - i_layer layers
        cg_val = c0
        for _ in range(i_layer - 1):
            cg_val = c_layer(cg_val)
        # Derivative of h_i at cg_val
        ch_prime = 1.0
        cur = cg_val
        for _ in range(D - i_layer):
            ch_prime *= b1 + 3.0 * b3 * (cur ** 2)
            cur = c_layer(cur)
        theta_i = cg_val * ch_prime
        assert abs(theta_i - c0) <= 11.0 * (zeta - 1.0)

    print(
        f"[PASS] Round 569 DKS verified: C_relu^100(-1)={c_val:.4f}, "
        f"max_val_dev={max_val_dev:.4f}<=2*(zeta-1)={2*(zeta-1):.4f}, "
        f"Q(1)={q_1:.4f}, Q'(1)={q_prime_1:.4f}, C'(1)={c_prime_1:.5f}==psi={target_psi_100:.5f}"
    )


if __name__ == "__main__":
    main()
