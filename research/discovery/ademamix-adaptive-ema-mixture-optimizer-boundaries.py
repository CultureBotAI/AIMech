#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 597: AdEMAMix (Pagliardini, Ablin, & Grangier, ICLR 2025)."""

from __future__ import annotations

import math


def t_half(beta: float) -> float:
    """Return EMA half-life f(beta) = ln(0.5)/ln(beta) - 1 (Section 3, p. 4 & Appendix A.1, p. 18)."""
    return math.log(0.5) / math.log(beta) - 1.0


def beta3_scheduler(t: int, beta3: float, beta_start: float, t_warmup: int) -> float:
    """Return scheduled beta_3^{(t)} from Equation (f_{beta_3}) on p. 6."""
    if t >= t_warmup:
        return beta3
    mu = t / t_warmup
    num = math.log(beta_start) * math.log(beta3)
    den = (1.0 - mu) * math.log(beta3) + mu * math.log(beta_start)
    return min(math.exp(num / den), beta3)


def test_beta3_scheduler_linear_halflife() -> tuple[float, float, float]:
    """Verify Appendix A.1 (p. 18): the beta_3 scheduler increases EMA half-life t_half linearly with mu=t/T."""
    beta_start = 0.9
    beta_end = 0.9999
    T = 1000
    f_start = t_half(beta_start)
    f_end = t_half(beta_end)

    max_linearity_err = 0.0
    for step in range(0, T + 1, 50):
        mu = step / T
        b_t = beta3_scheduler(step, beta_end, beta_start, T)
        f_actual = t_half(b_t)
        f_expected = (1.0 - mu) * f_start + mu * f_end
        max_linearity_err = max(max_linearity_err, abs(f_actual - f_expected) / f_expected)

    assert max_linearity_err < 1e-11, f"Expected exact linear half-life schedule, got rel_err={max_linearity_err}"

    # Verify cumulative geometric sum up to t_half equals 0.5: (1 - beta) * sum_{i=0}^{t_half} beta^i == 0.5
    # Exact continuous identity: 1 - beta^{t_half + 1} == 0.5
    half_mass_err = abs((1.0 - beta_end ** (f_end + 1.0)) - 0.5)
    assert half_mass_err < 1e-12
    return max_linearity_err, f_start, f_end


def test_ademamix_vs_large_beta1_adam_canyon() -> tuple[float, float]:
    """Verify Appendix C.1.6 Fig. 18 (p. 32): AdEMAMix dampens initial momentum overshoot where large-beta1 Adam fails."""
    # Toy 2D function from Appendix C.1.6 (p. 32):
    # f(x, y) = 8 (x - 1)^2 * (1.3 x^2 + 2 x + 1) + 0.5 (y - 4)^2, global optimum at (1.0, 4.0)
    def grad_f(x: float, y: float) -> tuple[float, float]:
        # d/dx [8(x-1)^2 (1.3x^2 + 2x + 1)] = 16(x-1)(1.3x^2 + 2x + 1) + 8(x-1)^2 (2.6x + 2)
        gx = 16.0 * (x - 1.0) * (1.3 * x * x + 2.0 * x + 1.0) + 8.0 * ((x - 1.0) ** 2) * (2.6 * x + 2.0)
        gy = y - 4.0
        return gx, gy

    steps = 400
    lr = 0.02
    beta2 = 0.999
    eps = 1e-8

    # 1. Adam with single large beta1 = 0.999 and initial momentum m^(0) = [-3.0, 0.0] (Appendix C.1.6 Fig. 18a)
    x_adam, y_adam = 0.3, 1.5
    m1_ax, m1_ay = -3.0, 0.0
    v_ax, v_ay = 0.0, 0.0
    for t in range(1, steps + 1):
        gx, gy = grad_f(x_adam, y_adam)
        m1_ax = 0.999 * m1_ax + 0.001 * gx
        m1_ay = 0.999 * m1_ay + 0.001 * gy
        v_ax = beta2 * v_ax + (1.0 - beta2) * (gx * gx)
        v_ay = beta2 * v_ay + (1.0 - beta2) * (gy * gy)
        mh_x = m1_ax / (1.0 - 0.999**t)
        mh_y = m1_ay / (1.0 - 0.999**t)
        vh_x = v_ax / (1.0 - beta2**t)
        vh_y = v_ay / (1.0 - beta2**t)
        x_adam -= lr * mh_x / (math.sqrt(vh_x) + eps)
        y_adam -= lr * mh_y / (math.sqrt(vh_y) + eps)
    dist_adam = math.hypot(x_adam - 1.0, y_adam - 4.0)

    # 2. AdEMAMix (Algorithm 1) with fast beta1 = 0.9, slow beta3 = 0.999, alpha = 2.0, same initial m1=m2=[-3.0, 0.0]
    x_ade, y_ade = 0.3, 1.5
    m1_ex, m1_ey = -3.0, 0.0
    m2_ex, m2_ey = -3.0, 0.0
    v_ex, v_ey = 0.0, 0.0
    alpha = 2.0
    lr_ade = lr / (1.0 + alpha)
    for t in range(1, steps + 1):
        gx, gy = grad_f(x_ade, y_ade)
        m1_ex = 0.9 * m1_ex + 0.1 * gx
        m1_ey = 0.9 * m1_ey + 0.1 * gy
        m2_ex = 0.999 * m2_ex + 0.001 * gx
        m2_ey = 0.999 * m2_ey + 0.001 * gy
        v_ex = beta2 * v_ex + (1.0 - beta2) * (gx * gx)
        v_ey = beta2 * v_ey + (1.0 - beta2) * (gy * gy)
        mh1_x = m1_ex / (1.0 - 0.9**t)
        mh1_y = m1_ey / (1.0 - 0.9**t)
        vh_x = v_ex / (1.0 - beta2**t)
        vh_y = v_ey / (1.0 - beta2**t)
        x_ade -= lr_ade * (mh1_x + alpha * m2_ex) / (math.sqrt(vh_x) + eps)
        y_ade -= lr_ade * (mh1_y + alpha * m2_ey) / (math.sqrt(vh_y) + eps)
    dist_ade = math.hypot(x_ade - 1.0, y_ade - 4.0)

    assert dist_ade < 0.1 * dist_adam, f"Expected AdEMAMix dist ({dist_ade}) << large-beta1 Adam dist ({dist_adam})"
    return dist_ade, dist_adam


def main() -> None:
    lin_err, f_start, f_end = test_beta3_scheduler_linear_halflife()
    dist_ade, dist_adam = test_ademamix_vs_large_beta1_adam_canyon()
    print(
        f"[PASS] Round 597 AdEMAMix verified: halflife_lin_err={lin_err:.2e} "
        f"(t_half: {f_start:.1f}->{f_end:.1f}), dist_ade={dist_ade:.4e}<<dist_adam={dist_adam:.4e}"
    )


if __name__ == "__main__":
    main()
