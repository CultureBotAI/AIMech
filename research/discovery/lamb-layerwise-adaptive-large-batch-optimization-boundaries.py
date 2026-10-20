#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 593: LAMB (You et al., ICLR 2020)."""

from __future__ import annotations

import math
import random


def vec_norm(x: list[float]) -> float:
    return math.sqrt(sum(v * v for v in x))


def test_lamb_two_level_normalization_and_signsgd_limit() -> tuple[float, float, float]:
    """Verify Algorithm 2 two-level normalization, SignSGD reduction (beta1=beta2=0), and Eq. (8) bound."""
    rng = random.Random(59301)
    d_i = 16
    x_layer = [rng.gauss(0.0, 2.0) for _ in range(d_i)]
    g_layer = [rng.gauss(0.0, 5.0) for _ in range(d_i)]
    eta = 0.05

    # Case 1: beta1 = 0, beta2 = 0, lambda = 0, eps -> 0 => SignSGD scaled by 1/sqrt(d_i)
    r_sign = [g / (abs(g) + 1e-15) for g in g_layer]
    r_norm = vec_norm(r_sign)
    expected_norm = math.sqrt(d_i)
    sign_norm_err = abs(r_norm - expected_norm)
    assert sign_norm_err < 1e-12, f"Expected ||r^(i)||_2 = sqrt(d_i), got {r_norm} vs {expected_norm}"

    # Verify scale invariance of layerwise step size under arbitrary positive gradient scaling c * g
    lam = 0.01
    beta1, beta2, eps = 0.9, 0.999, 1e-12
    m = [(1.0 - beta1) * g for g in g_layer]
    v = [(1.0 - beta2) * (g * g) for g in g_layer]
    m_hat = [mv / (1.0 - beta1) for mv in m]
    v_hat = [vv / (1.0 - beta2) for vv in v]
    r1 = [mh / (math.sqrt(vh) + eps) for mh, vh in zip(m_hat, v_hat)]
    u1 = [rv + lam * xv for rv, xv in zip(r1, x_layer)]
    u1_norm = vec_norm(u1)
    step1 = [eta * (vec_norm(x_layer) / u1_norm) * uv for uv in u1]

    scale = 1e4
    g_scaled = [scale * g for g in g_layer]
    m_s = [(1.0 - beta1) * g for g in g_scaled]
    v_s = [(1.0 - beta2) * (g * g) for g in g_scaled]
    m_hat_s = [mv / (1.0 - beta1) for mv in m_s]
    v_hat_s = [vv / (1.0 - beta2) for vv in v_s]
    r2 = [mh / (math.sqrt(vh) + eps) for mh, vh in zip(m_hat_s, v_hat_s)]
    u2 = [rv + lam * xv for rv, xv in zip(r2, x_layer)]
    u2_norm = vec_norm(u2)
    step2 = [eta * (vec_norm(x_layer) / u2_norm) * uv for uv in u2]

    invariance_diff = max(abs(a - b) for a, b in zip(step1, step2))
    assert invariance_diff < 1e-9, f"Expected gradient-scale invariance, got {invariance_diff}"

    # Verify Appendix B Eq. (8) bound: ||r_t^(i)||_2 <= sqrt(d_i / (1 - beta2))
    m_seq = [0.0] * d_i
    v_seq = [0.0] * d_i
    max_ratio_to_bound = 0.0
    bound = math.sqrt(d_i / (1.0 - beta2))
    for t in range(1, 40):
        gt = [rng.gauss(0.0, 3.0) for _ in range(d_i)]
        m_seq = [beta1 * mp + (1.0 - beta1) * g for mp, g in zip(m_seq, gt)]
        v_seq = [beta2 * vp + (1.0 - beta2) * (g * g) for vp, g in zip(v_seq, gt)]
        # Uncorrected ratio used in Appendix B Eq. (8): r_t = m_t / sqrt(v_t)
        rt = [mp / (math.sqrt(vp) + 1e-15) for mp, vp in zip(m_seq, v_seq)]
        max_ratio_to_bound = max(max_ratio_to_bound, vec_norm(rt) / bound)
    assert max_ratio_to_bound <= 1.0 + 1e-9
    return sign_norm_err, invariance_diff, max_ratio_to_bound


def test_lamb_vs_lars_and_sgd_multilayer() -> tuple[float, float, float]:
    """Compare LAMB, LARS, and SGD on a multi-layer objective with both layerwise and coordinatewise ill-conditioning."""
    # 3 layers, each of dimension 4; layer smoothness scales L_1=1000, L_2=10, L_3=0.1
    # Within each layer, coordinates have curvature ratios [1.0, 0.1, 0.01, 0.001]
    layer_scales = [1000.0, 10.0, 0.1]
    coord_scales = [1.0, 0.1, 0.01, 0.001]
    x0 = [[2.0, -1.5, 1.0, -0.5] for _ in layer_scales]

    def loss_and_grad(x: list[list[float]]) -> tuple[float, list[list[float]]]:
        val = 0.0
        grads: list[list[float]] = []
        for l_idx, l_scale in enumerate(layer_scales):
            g_l: list[float] = []
            for c_idx, c_scale in enumerate(coord_scales):
                curv = l_scale * c_scale
                xv = x[l_idx][c_idx]
                val += 0.5 * curv * xv * xv
                g_l.append(curv * xv)
            grads.append(g_l)
        return val, grads

    steps = 120
    # 1. Standard SGD with safe step size 1 / L_inf (L_inf = 1000)
    x_sgd = [row[:] for row in x0]
    eta_sgd = 1.0 / 1000.0
    for _ in range(steps):
        _, grads = loss_and_grad(x_sgd)
        for i in range(len(layer_scales)):
            for j in range(4):
                x_sgd[i][j] -= eta_sgd * grads[i][j]
    loss_sgd, _ = loss_and_grad(x_sgd)

    # 2. LARS (Algorithm 1): layerwise normalization without coordinatewise 2nd-moment scaling
    x_lars = [row[:] for row in x0]
    m_lars = [[0.0] * 4 for _ in layer_scales]
    beta1 = 0.9
    eta_lars = 0.15
    for _ in range(steps):
        _, grads = loss_and_grad(x_lars)
        for i in range(len(layer_scales)):
            for j in range(4):
                m_lars[i][j] = beta1 * m_lars[i][j] + (1.0 - beta1) * grads[i][j]
            w_norm = vec_norm(x_lars[i])
            m_norm = vec_norm(m_lars[i])
            if w_norm > 0 and m_norm > 0:
                scale = eta_lars * (w_norm / m_norm)
                for j in range(4):
                    x_lars[i][j] -= scale * m_lars[i][j]
    loss_lars, _ = loss_and_grad(x_lars)

    # 3. LAMB (Algorithm 2): both coordinatewise Adam ratio and layerwise trust ratio
    x_lamb = [row[:] for row in x0]
    m_lamb = [[0.0] * 4 for _ in layer_scales]
    v_lamb = [[0.0] * 4 for _ in layer_scales]
    beta2 = 0.999
    eps = 1e-8
    eta_lamb = 0.15
    for t in range(1, steps + 1):
        _, grads = loss_and_grad(x_lamb)
        for i in range(len(layer_scales)):
            r_i: list[float] = []
            for j in range(4):
                m_lamb[i][j] = beta1 * m_lamb[i][j] + (1.0 - beta1) * grads[i][j]
                v_lamb[i][j] = beta2 * v_lamb[i][j] + (1.0 - beta2) * (grads[i][j] ** 2)
                mh = m_lamb[i][j] / (1.0 - beta1**t)
                vh = v_lamb[i][j] / (1.0 - beta2**t)
                r_i.append(mh / (math.sqrt(vh) + eps))
            w_norm = vec_norm(x_lamb[i])
            r_norm = vec_norm(r_i)
            if w_norm > 0 and r_norm > 0:
                scale = eta_lamb * (w_norm / r_norm)
                for j in range(4):
                    x_lamb[i][j] -= scale * r_i[j]
    loss_lamb, _ = loss_and_grad(x_lamb)

    assert loss_lamb < loss_lars < loss_sgd, (
        f"Expected LAMB ({loss_lamb}) < LARS ({loss_lars}) < SGD ({loss_sgd})"
    )
    return loss_lamb, loss_lars, loss_sgd


def main() -> None:
    sign_err, inv_diff, ratio_bound = test_lamb_two_level_normalization_and_signsgd_limit()
    loss_lamb, loss_lars, loss_sgd = test_lamb_vs_lars_and_sgd_multilayer()
    print(
        f"[PASS] Round 593 LAMB verified: sign_err={sign_err:.2e}, inv_diff={inv_diff:.2e}, "
        f"ratio_bound={ratio_bound:.4f}<=1, loss_lamb={loss_lamb:.4e}<loss_lars={loss_lars:.4e}<loss_sgd={loss_sgd:.4e}"
    )


if __name__ == "__main__":
    main()
