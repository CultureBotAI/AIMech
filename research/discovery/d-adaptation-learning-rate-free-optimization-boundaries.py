#!/usr/bin/env python3
"""Constructed boundary verification for Round 586: D-Adaptation (Defazio & Mishchenko, ICML 2023)."""

from __future__ import annotations

import math


def main() -> None:
    # 1. Verify Lemma 5, Lemma 6, Theorem 7, and Section 4.1 (Option I <= Option II <= D):
    # Consider a 2D convex Lipschitz objective f(x_1, x_2) = 1.5 * |x_1 - 3.0| + 2.0 * |x_2 + 4.0|
    # with unique minimizer x_* = (3.0, -4.0) and x_0 = (0.0, 0.0), so exact initial distance is
    # D = ||x_0 - x_*||_2 = sqrt(3^2 + (-4)^2) = 5.0!
    x_star = [3.0, -4.0]
    x0 = [0.0, 0.0]
    d_true = math.hypot(x0[0] - x_star[0], x0[1] - x_star[1])
    assert abs(d_true - 5.0) < 1e-15

    def f_val(x: list[float]) -> float:
        return 1.5 * abs(x[0] - 3.0) + 2.0 * abs(x[1] + 4.0)

    def f_subgrad(x: list[float]) -> list[float]:
        g0 = 1.5 if x[0] > 3.0 else (-1.5 if x[0] < 3.0 else 0.0)
        g1 = 2.0 if x[1] > -4.0 else (-2.0 if x[1] < -4.0 else 0.0)
        return [g0, g1]

    # Run Algorithm 1 (Dual Averaging with D-Adaptation) starting from d_0 = 0.1 << D = 5.0 (cf. Figure 1, p. 6)
    d_k = 0.1
    xk = x0[:]
    sk = [0.0, 0.0]
    sum_g_norm_sq = 0.0
    sum_gamma_d2_g2 = 0.0
    sum_d_gamma_gs = 0.0
    sum_dk = 0.0
    weighted_x = [0.0, 0.0]

    # Also track quantities for Lemma 5 exact telescoping identity:
    # -sum_{i=0}^k gamma_i d_i <g_i, s_i> == -(gamma_{k+1}/2)||s_{k+1}||^2
    #   + sum_{i=0}^k (gamma_i/2) d_i^2 ||g_i||^2 + 0.5 * sum_{i=0}^k (gamma_{i+1} - gamma_i) ||s_{i+1}||^2
    sum_gamma_diff_s2 = 0.0
    gamma_k = 1.0 / math.hypot(*f_subgrad(x0))  # gamma_0 = 1 / ||g_0||

    for k in range(200):
        gk = f_subgrad(xk)
        g_norm_sq = gk[0] ** 2 + gk[1] ** 2
        if g_norm_sq == 0.0:
            break

        sum_dk += d_k
        weighted_x[0] += d_k * xk[0]
        weighted_x[1] += d_k * xk[1]

        gs_dot = gk[0] * sk[0] + gk[1] * sk[1]
        sum_d_gamma_gs += d_k * gamma_k * gs_dot
        sum_gamma_d2_g2 += 0.5 * gamma_k * (d_k**2) * g_norm_sq

        s_next = [sk[0] + d_k * gk[0], sk[1] + d_k * gk[1]]
        s_next_norm_sq = s_next[0] ** 2 + s_next[1] ** 2
        s_next_norm = math.sqrt(s_next_norm_sq)

        sum_g_norm_sq += g_norm_sq
        gamma_next = 1.0 / math.sqrt(sum_g_norm_sq)

        sum_gamma_diff_s2 += 0.5 * (gamma_next - gamma_k) * s_next_norm_sq

        # Check Lemma 5 exact identity at step k
        lhs_lem5 = -sum_d_gamma_gs
        rhs_lem5 = -0.5 * gamma_next * s_next_norm_sq + sum_gamma_d2_g2 + sum_gamma_diff_s2
        assert abs(lhs_lem5 - rhs_lem5) < 1e-12, f"Lemma 5 failed at k={k}: {lhs_lem5} vs {rhs_lem5}"

        # Option I and Option II lower bounds on D
        d_hat_opt1 = (0.5 * gamma_next * s_next_norm_sq - sum_gamma_d2_g2) / s_next_norm
        d_hat_opt2 = sum_d_gamma_gs / s_next_norm

        # Verify Section 4.1 inequality: d_hat_opt1 <= d_hat_opt2 <= D (Theorem 7 & Appendix E.1)
        assert d_hat_opt1 <= d_hat_opt2 + 1e-12
        assert d_hat_opt2 <= d_true + 1e-10, f"Lower bound exceeded true D={d_true}: {d_hat_opt2}"

        d_k = max(d_k, d_hat_opt1)
        xk = [x0[0] - gamma_next * s_next[0], x0[1] - gamma_next * s_next[1]]
        sk = s_next
        gamma_k = gamma_next

    x_hat = [weighted_x[0] / sum_dk, weighted_x[1] / sum_dk]
    # Verify Theorem 24 asymptotic bound: d_n >= D / (1 + sqrt(3)) ~ 1.8301
    asymp_lb = d_true / (1.0 + math.sqrt(3.0))
    g_lip = math.hypot(1.5, 2.0)  # G = 2.5
    thm1_bound = 12.0 * d_true * g_lip / math.sqrt(201.0) + 8.0 * d_true * g_lip / 201.0
    assert d_k >= asymp_lb and d_k <= d_true
    assert f_val(x_hat) < 0.05 * f_val(x0) and f_val(x_hat) <= thm1_bound

    # 2. Verify Lemma 25 (Appendix F, p. 44) EMA-to-weighted-sum equivalence used in D-Adapted Adam:
    # u_{k+1} = u_k + c^{-k} g_k and u_hat_{k+1} = c u_hat_k + (1 - c) g_k satisfy u_hat_{k+1} = c^k (1 - c) u_{k+1}.
    c_val = 0.95
    u_k = 0.0
    u_hat_k = 0.0
    for k in range(30):
        g_scalar = math.sin(k + 1.0)
        u_k = u_k + (c_val ** (-k)) * g_scalar
        u_hat_k = c_val * u_hat_k + (1.0 - c_val) * g_scalar
        assert abs(u_hat_k - (c_val**k) * (1.0 - c_val) * u_k) < 1e-13

    print(
        f"[PASS] Round 586 D-Adaptation verified: d0=1e-4->d_final={d_k:.4f} in [{asymp_lb:.4f}, {d_true:.4f}], "
        f"f(x_hat)={f_val(x_hat):.4f}"
    )


if __name__ == "__main__":
    main()
