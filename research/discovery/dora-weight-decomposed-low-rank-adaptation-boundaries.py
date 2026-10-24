#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 651:
DoRA (Weight-Decomposed Low-Rank Adaptation)
Primary source: Liu et al. (ICML 2024, PMLR v235:32100-32121, arXiv:2402.09353).
"""

import math


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def norm2(u):
    return math.sqrt(dot(u, u))


def verify_dora_initialization_and_zero_latency_merge_eq_5():
    """Verify Eq. (5): Initializing m = ||W_0||_c, V = W_0, and B = 0 yields W' = W_0 at t=0,
    and after updating m and Delta_V = B A, the merged matrix W' = m * (V + B A) / ||V + B A||_c
    produces identical linear layer outputs x^T W' as applying decomposed magnitude and direction."""
    W_0 = [
        [0.6, -0.3, 0.2],
        [0.8, 0.4, -0.5],
        [-0.2, 0.5, 0.3],
        [0.1, -0.2, 0.4],
    ]  # 4 x 3 (d=4, k=3)
    d, k = 4, 3
    cols_0 = [[W_0[i][j] for i in range(d)] for j in range(k)]
    m_init = [norm2(col) for col in cols_0]

    # At initialization Delta_V = 0 -> W' == W_0
    for j in range(k):
        n_c = norm2(cols_0[j])
        for i in range(d):
            w_prime_ij = m_init[j] * (cols_0[j][i] / n_c)
            assert abs(w_prime_ij - W_0[i][j]) < 1e-12

    # Non-zero low-rank directional update B (4x2) * A (2x3) and updated magnitude m
    B = [[0.1, -0.2], [0.05, 0.1], [-0.15, 0.05], [0.2, 0.1]]
    A = [[0.3, -0.1, 0.2], [-0.2, 0.4, 0.1]]
    m_tuned = [1.15 * m_init[0], 0.92 * m_init[1], 1.08 * m_init[2]]

    V_prime_cols = []
    for j in range(k):
        col = [
            W_0[i][j] + sum(B[i][r] * A[r][j] for r in range(2))
            for i in range(d)
        ]
        V_prime_cols.append(col)

    W_merged = [[0.0] * k for _ in range(d)]
    for j in range(k):
        c_norm = norm2(V_prime_cols[j])
        for i in range(d):
            W_merged[i][j] = m_tuned[j] * V_prime_cols[j][i] / c_norm

    x = [0.5, -0.4, 0.7, 0.2]
    y_merged = [sum(x[i] * W_merged[i][j] for i in range(d)) for j in range(k)]
    y_decomposed = [
        m_tuned[j] * (sum(x[i] * V_prime_cols[i_col][i] for i in range(d)) / norm2(V_prime_cols[j]))
        for i_col, j in enumerate(range(k))
    ]
    for a, b in zip(y_merged, y_decomposed):
        assert abs(a - b) < 1e-12


def verify_dora_orthogonal_gradient_projection_and_negative_slope_eqs_6_10():
    """Verify Section 4.2 (Eqs. 6-10):
    (1) Exact differentiation of w'(m, v') = m * v' / ||v'||_2 matches Eqs. (6) and (7):
        grad_{v'} L = (m / ||v'||_2) * (I - v' v'^T / ||v'||_2^2) grad_{w'} L, which is orthogonal to v'.
    (2) Under equal gradient norm ||grad_{w'} L||_2, a smaller directional update scenario S1
        (|cos(grad_{w'}^{S1} L, v)| > |cos(grad_{w'}^{S2} L, v)|) produces a strictly larger magnitude
        gradient |grad_m^{S1} L| > |grad_m^{S2} L| (Eqs. 8-10)."""
    v_prime = [0.6, -0.8, 0.5]
    m = 1.5
    grad_w = [0.4, 0.3, -0.2]
    norm_v = norm2(v_prime)

    # Analytical formulas Eqs. (6)-(7)
    proj_coeff = dot(v_prime, grad_w) / (norm_v ** 2)
    grad_v = [(m / norm_v) * (grad_w[i] - proj_coeff * v_prime[i]) for i in range(3)]
    grad_m = dot(grad_w, v_prime) / norm_v

    # 1. Verify orthogonality of directional gradient to current direction v'
    assert abs(dot(grad_v, v_prime)) < 1e-12

    # 2. Verify against finite differences of L(w') = grad_w^T w'(m, v')
    eps = 1e-7
    for i in range(3):
        vp_plus = v_prime[:]
        vp_minus = v_prime[:]
        vp_plus[i] += eps
        vp_minus[i] -= eps
        w_plus = [m * x / norm2(vp_plus) for x in vp_plus]
        w_minus = [m * x / norm2(vp_minus) for x in vp_minus]
        fd_vi = (dot(grad_w, w_plus) - dot(grad_w, w_minus)) / (2.0 * eps)
        assert abs(grad_v[i] - fd_vi) < 1e-7

    # 3. Verify Eq. (9)-(10): S1 (smaller directional change -> larger |cos|) has larger |grad_m L|
    v = [1.0, 0.0, 0.0]
    grad_w_s1 = [0.8, 0.6, 0.0]  # norm = 1.0, cos = 0.8 (smaller directional change)
    grad_w_s2 = [0.28, 0.96, 0.0]  # norm = 1.0, cos = 0.28 (larger directional change)
    assert abs(norm2(grad_w_s1) - norm2(grad_w_s2)) < 1e-12

    delta_d_s1 = 1.0 - abs(dot(grad_w_s1, v) / (norm2(grad_w_s1) * norm2(v)))
    delta_d_s2 = 1.0 - abs(dot(grad_w_s2, v) / (norm2(grad_w_s2) * norm2(v)))
    assert delta_d_s1 < delta_d_s2

    grad_m_s1 = abs(dot(grad_w_s1, v) / norm2(v))
    grad_m_s2 = abs(dot(grad_w_s2, v) / norm2(v))
    assert grad_m_s1 > grad_m_s2


if __name__ == "__main__":
    verify_dora_initialization_and_zero_latency_merge_eq_5()
    verify_dora_orthogonal_gradient_projection_and_negative_slope_eqs_6_10()
    print("[PASS] Round 651 DoRA boundary and mathematical verification succeeded.")
