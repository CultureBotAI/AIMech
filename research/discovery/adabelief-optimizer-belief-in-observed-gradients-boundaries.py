#!/usr/bin/env python3
"""Constructed boundary verification for Round 582: AdaBelief Optimizer (Zhuang et al., NeurIPS 2020)."""

from __future__ import annotations

import math


def main() -> None:
    # 1. Verify Figure 2 / Equations (2)-(4) on f(x, y) = |x| + |y| with oscillating y-gradient:
    # Sequence of gradients: g_{t,x} = 1 for all t; g_{t,y} = (-1)^t for t = 1..T
    beta1, beta2, eps = 0.9, 0.999, 1e-8
    mx, my = 0.0, 0.0
    vx, vy = 0.0, 0.0
    sx, sy = 0.0, 0.0
    steps = 500
    for t in range(1, steps + 1):
        gx = 1.0
        gy = -1.0 if t % 2 == 1 else 1.0
        mx = beta1 * mx + (1.0 - beta1) * gx
        my = beta1 * my + (1.0 - beta1) * gy
        # Adam second moment
        vx = beta2 * vx + (1.0 - beta2) * (gx * gx)
        vy = beta2 * vy + (1.0 - beta2) * (gy * gy)
        # AdaBelief prediction-residual second moment
        sx = beta2 * sx + (1.0 - beta2) * ((gx - mx) ** 2) + eps
        sy = beta2 * sy + (1.0 - beta2) * ((gy - my) ** 2) + eps

    vx_hat = vx / (1.0 - (beta2**steps))
    vy_hat = vy / (1.0 - (beta2**steps))
    sx_hat = sx / (1.0 - (beta2**steps))
    sy_hat = sy / (1.0 - (beta2**steps))

    # In Adam, v_x == v_y == 1.0, so denominator is identical in consistent x and oscillating y directions!
    assert abs(vx_hat - 1.0) < 1e-12 and abs(vy_hat - 1.0) < 1e-12
    # In AdaBelief, s_x << s_y (since g_x - m_x -> 0 while g_y - m_y oscillates around +-1),
    # so effective stepsize multiplier 1 / sqrt(s_x_hat) >> 1 / sqrt(s_y_hat)!
    step_mult_x = 1.0 / (math.sqrt(sx_hat) + eps)
    step_mult_y = 1.0 / (math.sqrt(sy_hat) + eps)
    assert sx_hat < 1e-2 * sy_hat
    assert step_mult_x > 10.0 * step_mult_y

    # 2. Verify Equation (5) & Figure 3(d): Low-variance regime on anisotropic linear region f(x, y) = 0.1 |x| + |y|
    # In region x > 0, y > 0 with tiny noise, true gradient is g = (0.1, 1.0) (slope ratio dy/dx = 10.0).
    # Adam's update degenerates to sign(g) = (1, 1) (45-degree angle, dy/dx = 1.0), whereas AdaBelief
    # with isotropic gradient variance sigma^2 preserves the true gradient ratio dy/dx = 10.0!
    b1_low, b2_low = 0.3, 0.3
    mx2, my2 = 0.0, 0.0
    vx2, vy2 = 0.0, 0.0
    sx2, sy2 = 0.0, 0.0
    sigma = 1e-3
    for t in range(1, 200):
        noise = sigma if t % 2 == 0 else -sigma
        gx = 0.1 + noise
        gy = 1.0 + noise
        mx2 = b1_low * mx2 + (1.0 - b1_low) * gx
        my2 = b1_low * my2 + (1.0 - b1_low) * gy
        vx2 = b2_low * vx2 + (1.0 - b2_low) * (gx * gx)
        vy2 = b2_low * vy2 + (1.0 - b2_low) * (gy * gy)
        sx2 = b2_low * sx2 + (1.0 - b2_low) * ((gx - mx2) ** 2) + eps
        sy2 = b2_low * sy2 + (1.0 - b2_low) * ((gy - my2) ** 2) + eps

    adam_dx = (mx2 / (1.0 - b1_low**199)) / (math.sqrt(vx2 / (1.0 - b2_low**199)) + eps)
    adam_dy = (my2 / (1.0 - b1_low**199)) / (math.sqrt(vy2 / (1.0 - b2_low**199)) + eps)
    adabelief_dx = (mx2 / (1.0 - b1_low**199)) / (math.sqrt(sx2 / (1.0 - b2_low**199)) + eps)
    adabelief_dy = (my2 / (1.0 - b1_low**199)) / (math.sqrt(sy2 / (1.0 - b2_low**199)) + eps)

    adam_ratio = adam_dy / adam_dx
    adabelief_ratio = adabelief_dy / adabelief_dx
    assert abs(adam_ratio - 1.0) < 1e-3, f"Adam should degenerate to sign update ratio 1.0: {adam_ratio}"
    assert abs(adabelief_ratio - 10.0) < 0.1, f"AdaBelief should preserve true gradient ratio 10.0: {adabelief_ratio}"

    # 3. Verify Case 3 in Table 1 ("large gradient, small curvature"):
    # Compare trajectory distance to optimum on ill-conditioned smooth quadratic f(x, y) = 0.05 x^2 + 5.0 y^2
    x_ab, y_ab = 10.0, 2.0
    x_ad, y_ad = 10.0, 2.0
    m_ab = [0.0, 0.0]
    s_ab = [0.0, 0.0]
    m_ad = [0.0, 0.0]
    v_ad = [0.0, 0.0]
    lr = 0.05
    for t in range(1, 400):
        # AdaBelief
        g_ab = [0.1 * x_ab, 10.0 * y_ab]
        m_ab = [0.9 * m_ab[i] + 0.1 * g_ab[i] for i in range(2)]
        s_ab = [0.999 * s_ab[i] + 0.001 * ((g_ab[i] - m_ab[i]) ** 2) + 1e-8 for i in range(2)]
        mh_ab = [m_ab[i] / (1.0 - 0.9**t) for i in range(2)]
        sh_ab = [s_ab[i] / (1.0 - 0.999**t) for i in range(2)]
        x_ab -= lr * mh_ab[0] / (math.sqrt(sh_ab[0]) + 1e-8)
        y_ab -= lr * mh_ab[1] / (math.sqrt(sh_ab[1]) + 1e-8)

        # Adam
        g_ad = [0.1 * x_ad, 10.0 * y_ad]
        m_ad = [0.9 * m_ad[i] + 0.1 * g_ad[i] for i in range(2)]
        v_ad = [0.999 * v_ad[i] + 0.001 * (g_ad[i] ** 2) for i in range(2)]
        mh_ad = [m_ad[i] / (1.0 - 0.9**t) for i in range(2)]
        vh_ad = [v_ad[i] / (1.0 - 0.999**t) for i in range(2)]
        x_ad -= lr * mh_ad[0] / (math.sqrt(vh_ad[0]) + 1e-8)
        y_ad -= lr * mh_ad[1] / (math.sqrt(vh_ad[1]) + 1e-8)

    err_ab = math.hypot(x_ab, y_ab)
    err_ad = math.hypot(x_ad, y_ad)
    assert err_ab < 1e-6 and err_ab < 1e-3 * err_ad

    print(
        f"[PASS] Round 582 AdaBelief verified: step_mult_ratio={step_mult_x/step_mult_y:.1f}, "
        f"adabelief_ratio={adabelief_ratio:.2f} vs adam_ratio={adam_ratio:.4f}, err_ab={err_ab:.3e}<<err_ad={err_ad:.3e}"
    )


if __name__ == "__main__":
    main()
