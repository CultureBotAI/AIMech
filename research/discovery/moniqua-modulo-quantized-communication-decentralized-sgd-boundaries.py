#!/usr/bin/env python3
"""Constructed boundary verification for Moniqua (Lu & De Sa, ICML 2020 / arXiv:2002.11787).

Verifies:
1. Lemma 1 exact modular identity:
   For z mod a in [-a/2, a/2), if |x - y| < theta, then
   (x mod 2*theta - y mod 2*theta) mod 2*theta + y == x.
2. Lemma 2 quantized modular recovery error bound (Equation 5):
   If |x - y| < theta, delta < 1/2, B_theta = 2*theta / (1 - 2*delta), and
   x_hat = (B_theta * Q_delta((x / B_theta) mod 1) - y) mod B_theta + y,
   then |x_hat - x| <= delta * B_theta = theta * 2*delta / (1 - 2*delta) regardless of how large |x| is!
3. Theorem 1 failure of naive direct quantization Q_delta(x_{k,j}) vs Moniqua exact convergence
   to x* on f(x) = 0.5 * (x - delta/2)^2 with zero additional memory state.
"""

import math


def sym_mod(z, a):
    """Symmetric modulo in [-a/2, a/2) as defined in Equation (1) of Lu & De Sa (ICML 2020)."""
    r = (z + 0.5 * a) % a
    return r - 0.5 * a


def quantize_linear_delta(val, delta):
    """Deterministic nearest-grid quantizer on [-1/2, 1/2) with grid spacing 2*delta (error <= delta)."""
    step = 2.0 * delta
    q = round(val / step) * step
    if q >= 0.5:
        q = 0.5 - step / 2.0
    if q < -0.5:
        q = -0.5 + step / 2.0
    assert abs(q - val) <= delta + 1e-12
    return q


def moniqua_recover(x, y, theta, delta):
    B_theta = (2.0 * theta) / (1.0 - 2.0 * delta)
    scaled_mod = sym_mod(x / B_theta, 1.0)
    q = quantize_linear_delta(scaled_mod, delta)
    return sym_mod(B_theta * q - y, B_theta) + y


def verify_moniqua_boundaries():
    # 1. Verify Lemma 1 exact unquantized modular recovery for large coordinates x, y with |x - y| < theta
    theta = 0.15
    for x, y in [(1000.42, 1000.31), (-543.20, -543.09), (0.05, -0.07)]:
        assert abs(x - y) < theta
        rec = sym_mod(sym_mod(x, 2.0 * theta) - sym_mod(y, 2.0 * theta), 2.0 * theta) + y
        assert abs(rec - x) < 1e-12, f"Lemma 1 failed for ({x}, {y}): got {rec}"

    # 2. Verify Lemma 2 quantized modular recovery bound |x_hat - x| <= delta * B_theta
    delta = 0.10  # coarse quantizer (delta < 0.5)
    B_theta = (2.0 * theta) / (1.0 - 2.0 * delta)
    max_bound = delta * B_theta
    for x, y in [(1000.42, 1000.31), (-543.20, -543.09), (25.123, 25.001), (-0.08, 0.04)]:
        assert abs(x - y) < theta
        x_hat = moniqua_recover(x, y, theta, delta)
        err = abs(x_hat - x)
        assert err <= max_bound + 1e-12, f"Lemma 2 violated: err={err} > bound={max_bound}"

    # 3. Verify Theorem 1 (naive quantization stalls away from x*=50.25) vs Moniqua convergence
    # Objective f_i(x) = 0.5 * (x - x_star)^2 where x_star = 50.25 (off grid of step=1.0)
    x_star = 50.25
    # 3-node connected ring with W_ij = 1/3
    n = 3
    x_naive = [50.0, 50.4, 50.2]
    x_moniqua = [50.0, 50.4, 50.2]

    for k in range(1, 120):
        alpha_k = 0.25 / (1.0 + 0.05 * k)
        theta_k = max(0.02, 1.5 * alpha_k)

        # Naive quantization directly quantizes x_{k,j} to nearest integer (grid spacing 1.0, delta=0.5)
        q_naive = [round(v) for v in x_naive]
        next_naive = []
        for i in range(n):
            comm = (x_naive[i] + sum(q_naive[j] for j in range(n) if j != i)) / n
            grad = x_naive[i] - x_star
            next_naive.append(comm - alpha_k * grad)
        x_naive = next_naive

        # MoniquaAlgorithm 1 with delta = 0.125 (2-bit quantizer on [-1/2, 1/2))
        B_th = (2.0 * theta_k) / (1.0 - 2.0 * 0.125)
        q_mon = [quantize_linear_delta(sym_mod(x_moniqua[i] / B_th, 1.0), 0.125) for i in range(n)]
        x_hat_self = [
            q_mon[i] * B_th - sym_mod(x_moniqua[i], B_th) + x_moniqua[i] for i in range(n)
        ]
        next_mon = []
        for i in range(n):
            avg_diff = 0.0
            for j in range(n):
                if j != i:
                    xh_j = sym_mod(q_mon[j] * B_th - x_moniqua[i], B_th) + x_moniqua[i]
                    avg_diff += (xh_j - x_hat_self[i]) / n
            x_half_i = x_moniqua[i] + avg_diff
            grad_i = x_moniqua[i] - x_star
            next_mon.append(x_half_i - alpha_k * grad_i)
        x_moniqua = next_mon

    err_naive = max(abs(v - x_star) for v in x_naive)
    err_moniqua = max(abs(v - x_star) for v in x_moniqua)
    assert err_moniqua < 1e-2, f"Moniqua failed to converge: {err_moniqua}"
    assert err_naive > 0.15, f"Naive quantization unexpectedly converged: {err_naive}"

    print(
        f"[PASS] Moniqua boundaries verified: Lemma 1&2 exact, "
        f"err_moniqua={err_moniqua:.4f} << err_naive={err_naive:.4f}"
    )


if __name__ == "__main__":
    verify_moniqua_boundaries()
