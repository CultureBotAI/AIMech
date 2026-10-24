#!/usr/bin/env python3
"""Constructed boundary verification for Round 585: Schedule-Free Optimization (Defazio et al., NeurIPS 2024)."""

from __future__ import annotations

import math


def main() -> None:
    # 1. Verify Theorem 5 (Appendix C, Equations 27-30, pp. 21-23):
    # Exact Bregman divergence identity for Schedule-Free online-to-batch conversion:
    # w_{1:t} F(x_t) - w_{1:t-1} F(x_{t-1}) - w_t F(x_*)
    # == w_t <grad F(y_t), z_t - x_*>
    #    - (w_t / alpha_t) B_F(y_t, x_t) - (w_t (1 - alpha_t) / alpha_t) B_F(x_t, y_t)
    #    - w_{1:t-1} B_F(x_{t-1}, x_t) - w_t B_F(x_*, y_t)
    # Test on a non-quadratic convex function F(u, v) = u^4 + 0.5*v^2 + exp(0.3*u - 0.2*v).
    def f_val(p: list[float]) -> float:
        u, v = p[0], p[1]
        return (u**4) + 0.5 * (v**2) + math.exp(0.3 * u - 0.2 * v)

    def f_grad(p: list[float]) -> list[float]:
        u, v = p[0], p[1]
        e = math.exp(0.3 * u - 0.2 * v)
        return [4.0 * (u**3) + 0.3 * e, v - 0.2 * e]

    def dot(a: list[float], b: list[float]) -> float:
        return a[0] * b[0] + a[1] * b[1]

    def sub(a: list[float], b: list[float]) -> list[float]:
        return [a[0] - b[0], a[1] - b[1]]

    def bregman(a: list[float], b: list[float]) -> float:
        return f_val(a) - f_val(b) - dot(f_grad(b), sub(a, b))

    x_star = [-0.4, 0.2]
    z_seq = [[1.2, -0.8], [0.7, -0.3], [0.2, 0.1], [-0.1, 0.25], [-0.3, 0.18]]
    w_seq = [1.0, 1.5, 2.0, 2.5, 3.0]
    alpha_seq = [0.2, 0.15, 0.1, 0.25, 0.05]  # alpha_t = 1 - beta_t

    w_cum = 0.0
    x_prev = z_seq[0][:]
    lhs_total = 0.0
    rhs_total = 0.0

    for t_idx in range(len(z_seq)):
        wt = w_seq[t_idx]
        w_prev = w_cum
        w_cum += wt
        zt = z_seq[t_idx]
        ct = wt / w_cum
        xt = [(1.0 - ct) * x_prev[j] + ct * zt[j] for j in range(2)]
        at = alpha_seq[t_idx]
        yt = [(1.0 - at) * xt[j] + at * zt[j] for j in range(2)]

        # Step identity Eq. (28)
        lhs_step = w_cum * f_val(xt) - w_prev * f_val(x_prev) - wt * f_val(x_star)
        rhs_step = (
            wt * dot(f_grad(yt), sub(zt, x_star))
            - (wt / at) * bregman(yt, xt)
            - (wt * (1.0 - at) / at) * bregman(xt, yt)
            - w_prev * bregman(x_prev, xt)
            - wt * bregman(x_star, yt)
        )
        assert abs(lhs_step - rhs_step) < 1e-13, f"Step {t_idx} Eq. (28) mismatch: {lhs_step} vs {rhs_step}"
        lhs_total += lhs_step
        rhs_total += rhs_step
        x_prev = xt

    # Verify telescoped Theorem 5 equality
    telescoped_lhs = w_cum * (f_val(x_prev) - f_val(x_star))
    assert abs(telescoped_lhs - rhs_total) < 1e-12
    assert abs(lhs_total - telescoped_lhs) < 1e-12

    # 2. Verify Appendix B.1 (Recovering Linear Decay Schedule from Schedule-Free interpolation):
    # When w_t = 1 and alpha_t = (T - t)/T (so beta_t = t/T), the coefficient of m_t in
    # u_t = y_{t+1} - y_t = (1 - alpha_t + t*(alpha_{t+1} - alpha_t)) m_t + alpha_t Delta_t
    # vanishes identically, reducing y_{t+1} - y_t = ((T - t)/T) (z_{t+1} - z_t) and y_T = x_T!
    cap_t = 12
    z_ld = 2.0
    x_ld = z_ld
    for t in range(1, cap_t + 1):
        c_t = 1.0 / t
        x_ld = (1.0 - c_t) * x_ld + c_t * z_ld
        alpha_t = (cap_t - t) / cap_t
        beta_t = t / cap_t
        y_ld = (1.0 - beta_t) * z_ld + beta_t * x_ld
        if t < cap_t:
            alpha_next = (cap_t - (t + 1)) / cap_t
            m_coeff = 1.0 - alpha_t + t * (alpha_next - alpha_t)
            assert abs(m_coeff) < 1e-15
            # Apply arbitrary step Delta_t
            delta_t = -0.3 * math.cos(t)
            z_next = z_ld + delta_t
            x_next = (1.0 - 1.0 / (t + 1)) * x_ld + (1.0 / (t + 1)) * z_next
            beta_next = (t + 1) / cap_t
            y_next = (1.0 - beta_next) * z_next + beta_next * x_next
            assert abs((y_next - y_ld) - alpha_t * delta_t) < 1e-14
            z_ld = z_next
        else:
            assert abs(y_ld - x_ld) < 1e-15

    # 3. Verify Theorem 1 & Section 2.2 (Figure 3): Schedule-Free SGD with beta in (0, 1) converges
    # on a quadratic objective at a large step size gamma where Polyak-Ruppert / Primal Averaging underperform:
    # Consider f(x) = 0.5 * 4.0 * (x - 3.0)^2 (L = 4.0, x_* = 3.0) with gamma = 0.45 (< 2/L = 0.5)
    gamma = 0.45
    z_sf = 0.0
    x_sf = 0.0
    beta_sf = 0.9
    for t in range(1, 81):
        y_sf = (1.0 - beta_sf) * z_sf + beta_sf * x_sf
        g_sf = 4.0 * (y_sf - 3.0)
        z_sf = z_sf - gamma * g_sf
        c_t = 1.0 / (t + 1)
        x_sf = (1.0 - c_t) * x_sf + c_t * z_sf

    # Primal averaging (beta = 1.0) vs Schedule-Free (beta = 0.9)
    z_pa = 0.0
    x_pa = 0.0
    for t in range(1, 81):
        g_pa = 4.0 * (x_pa - 3.0)
        z_pa = z_pa - gamma * g_pa
        c_t = 1.0 / (t + 1)
        x_pa = (1.0 - c_t) * x_pa + c_t * z_pa

    err_sf = abs(x_sf - 3.0)
    err_pa = abs(x_pa - 3.0)
    assert err_sf < err_pa

    print(
        f"[PASS] Round 585 Schedule-Free verified: bregman_diff={abs(telescoped_lhs - rhs_total):.2e}, "
        f"ld_yT_xT_diff={abs(y_ld - x_ld):.2e}, err_sf={err_sf:.4e}<err_pa={err_pa:.4e}"
    )


if __name__ == "__main__":
    main()
