#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 594: LARS (You, Gitman, & Ginsburg, 2017)."""

from __future__ import annotations

import math


def vec_norm(x: list[float]) -> float:
    return math.sqrt(sum(v * v for v in x))


def test_lars_layerwise_trust_ratio_bound() -> tuple[float, float, float]:
    """Verify Section 4 Eqs. (4)-(6) and Table 2: LARS bounds relative layer weight update by gamma * eta."""
    # Table 2 (p. 4) AlexNet-BN 1st iteration weight and gradient norms for conv1.w and fc6.w:
    # conv1.w: ||w|| = 0.098, ||grad|| = 0.017 -> ratio 5.76
    # fc6.w:   ||w|| = 6.4,   ||grad|| = 0.005 -> ratio 1345 (approx 1280)
    w_conv1 = [0.098, 0.0, 0.0]
    g_conv1 = [0.017, 0.0, 0.0]
    w_fc6 = [6.4, 0.0, 0.0]
    g_fc6 = [0.005, 0.0, 0.0]

    # Under standard SGD with large LR gamma = 10.0:
    # conv1.w update norm = 10.0 * 0.017 = 0.17 > ||w_conv1|| = 0.098 (relative update > 1.73 -> divergence)
    gamma = 10.0
    rel_sgd_conv1 = (gamma * vec_norm(g_conv1)) / vec_norm(w_conv1)
    rel_sgd_fc6 = (gamma * vec_norm(g_fc6)) / vec_norm(w_fc6)
    assert rel_sgd_conv1 > 1.5, f"Expected standard SGD relative step > 1 on conv1.w, got {rel_sgd_conv1}"

    # Under LARS (Eq. 6) with trust coefficient eta = 0.02 and weight decay beta = 0.0005:
    eta = 0.02
    beta = 0.0005
    for w_l, g_l in [(w_conv1, g_conv1), (w_fc6, g_fc6)]:
        w_n = vec_norm(w_l)
        g_n = vec_norm(g_l)
        lam_l = eta * w_n / (g_n + beta * w_n)
        # Update vector before momentum: delta_w = gamma * lam_l * (g_l + beta * w_l)
        delta_w = [gamma * lam_l * (gv + beta * wv) for gv, wv in zip(g_l, w_l)]
        rel_lars = vec_norm(delta_w) / w_n
        assert rel_lars <= gamma * eta + 1e-12, f"Expected relative update <= {gamma * eta}, got {rel_lars}"

    return rel_sgd_conv1, rel_sgd_fc6, gamma * eta


def test_lars_stability_and_convergence_vs_sgd() -> tuple[float, float]:
    """Verify Algorithm 1 (SGD with LARS, momentum, weight decay, polynomial decay) vs standard SGD."""
    # 4-layer problem with layer curvatures [500.0, 50.0, 5.0, 0.5]
    curvatures = [500.0, 50.0, 5.0, 0.5]
    w0 = [[1.5, -1.0, 0.5] for _ in curvatures]
    beta_wd = 1e-4
    mom = 0.9
    eta_trust = 0.05
    gamma0 = 2.0
    T = 100

    # Standard SGD with momentum at large base LR gamma0 = 2.0 diverges on layer 0 (L_0 = 500)
    w_sgd = [row[:] for row in w0]
    v_sgd = [[0.0] * 3 for _ in curvatures]
    diverged_sgd = False
    for t in range(T):
        gamma_t = gamma0 * ((1.0 - t / T) ** 2)
        for l_idx, curv in enumerate(curvatures):
            g_l = [curv * wv for wv in w_sgd[l_idx]]
            for j in range(3):
                v_sgd[l_idx][j] = mom * v_sgd[l_idx][j] + gamma_t * (g_l[j] + beta_wd * w_sgd[l_idx][j])
                w_sgd[l_idx][j] -= v_sgd[l_idx][j]
        if any(vec_norm(layer) > 1e6 for layer in w_sgd):
            diverged_sgd = True
            break
    assert diverged_sgd, "Expected standard momentum SGD to diverge under large base LR gamma0=2.0"

    # LARS (Algorithm 1, p. 4) at the exact same large base LR gamma0 = 2.0 converges smoothly across all layers
    w_lars = [row[:] for row in w0]
    v_lars = [[0.0] * 3 for _ in curvatures]
    init_loss = sum(0.5 * c * sum(v * v for v in layer) for c, layer in zip(curvatures, w_lars))
    for t in range(T):
        gamma_t = gamma0 * ((1.0 - t / T) ** 2)
        for l_idx, curv in enumerate(curvatures):
            g_l = [curv * wv for wv in w_lars[l_idx]]
            w_n = vec_norm(w_lars[l_idx])
            g_n = vec_norm(g_l)
            lam_l = eta_trust * (w_n / (g_n + beta_wd * w_n)) if (g_n + beta_wd * w_n) > 0 else 0.0
            for j in range(3):
                v_lars[l_idx][j] = mom * v_lars[l_idx][j] + gamma_t * lam_l * (g_l[j] + beta_wd * w_lars[l_idx][j])
                w_lars[l_idx][j] -= v_lars[l_idx][j]
    final_loss = sum(0.5 * c * sum(v * v for v in layer) for c, layer in zip(curvatures, w_lars))
    assert final_loss < 1e-2 * init_loss, f"Expected LARS loss << init_loss, got {final_loss} vs {init_loss}"
    return init_loss, final_loss


def main() -> None:
    rel_conv1, rel_fc6, target_rel = test_lars_layerwise_trust_ratio_bound()
    init_loss, final_loss = test_lars_stability_and_convergence_vs_sgd()
    print(
        f"[PASS] Round 594 LARS verified: sgd_rel=({rel_conv1:.2f}, {rel_fc6:.4f}) vs lars_rel={target_rel:.4f}, "
        f"lars_loss={final_loss:.4e}<<init_loss={init_loss:.4e}"
    )


if __name__ == "__main__":
    main()
