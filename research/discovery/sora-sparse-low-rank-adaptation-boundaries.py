#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 689: SoRA (Ding et al., EMNLP 2023 / arXiv:2311.11696)."""

from __future__ import annotations

import math
import random


def soft_threshold(x: float, xi: float) -> float:
    """Section 3.1, Eq. 11: T_xi(x) soft-thresholding operator for proximal gradient of l1 norm."""
    if x > xi:
        return x - xi
    if x <= -xi:
        return x + xi
    return 0.0


def matvec(M: list[list[float]], x: list[float]) -> list[float]:
    return [sum(row[j] * x[j] for j in range(len(x))) for row in M]


def sora_forward(Wu: list[list[float]], g: list[float], Wd: list[list[float]], x: list[float]) -> list[float]:
    """Section 3.1, Eq. 6-9: h = W_d x, h' = g o h, z = W_u h'."""
    h = matvec(Wd, x)
    h_prime = [g[i] * h[i] for i in range(len(g))]
    return matvec(Wu, h_prime)


def post_prune_sora(
    Wu: list[list[float]], g: list[float], Wd: list[list[float]]
) -> tuple[list[list[float]], list[list[float]], int]:
    """Section 3.1, Eq. 12: Drop zeroed-out ranks I^(k) = {i | g_i == 0} and absorb g_tilde into Wu_tilde * diag(g_tilde)."""
    kept = [i for i, gi in enumerate(g) if abs(gi) > 0.0]
    p = len(Wu)
    Wd_tilde = [Wd[i][:] for i in kept]
    Wu_absorbed = [[Wu[row][i] * g[i] for i in kept] for row in range(p)]
    return Wu_absorbed, Wd_tilde, len(kept)


def main() -> None:
    rng = random.Random(689)
    p, q, r_max = 8, 8, 6

    # 1. Verify proximal-gradient optimality identity (Section 3.2, Eq. 10, 11, 13):
    # For any v in R^{r_max} and xi = eta_t * lambda > 0, g* = T_xi(v) uniquely minimizes
    # J(g) = xi * ||g||_1 + 0.5 * ||g - v||_2^2.
    xi = 0.15
    v = [0.42, -0.08, 0.15, -0.35, 0.02, 0.28]
    g_star = [soft_threshold(vi, xi) for vi in v]
    assert g_star[1] == 0.0 and g_star[2] == 0.0 and g_star[4] == 0.0

    def obj_j(cand: list[float]) -> float:
        return xi * sum(abs(ci) for ci in cand) + 0.5 * sum((ci - vi) ** 2 for ci, vi in zip(cand, v))

    j_star = obj_j(g_star)
    for _ in range(200):
        pert = [gi + rng.gauss(0.0, 0.05) for gi in g_star]
        assert j_star <= obj_j(pert) + 1e-12

    # 2. Verify SoRA training + post-pruning equivalence (Section 3.1, Eq. 6-12):
    # Suppose target adaptation Delta_star has true rank 2, while r_max = 6.
    Wu = [[rng.gauss(0.0, 0.5) for _ in range(r_max)] for _ in range(p)]
    Wd = [[rng.gauss(0.0, 0.5) for _ in range(q)] for _ in range(r_max)]
    g_true = [1.4, 0.0, -1.1, 0.0, 0.0, 0.0]

    # Optimize gate g from dense initialization via proximal gradient descent (Eq. 10)
    g_t = [0.5] * r_max
    eta = 0.08
    lmbda = 0.25
    samples = [[rng.gauss(0.0, 1.0) for _ in range(q)] for _ in range(24)]

    for _step in range(160):
        grad_g = [0.0] * r_max
        for x in samples:
            z_pred = sora_forward(Wu, g_t, Wd, x)
            z_true = sora_forward(Wu, g_true, Wd, x)
            diff = [z_pred[row] - z_true[row] for row in range(p)]
            h = matvec(Wd, x)
            # d/dg_i (0.5 ||Wu(g o h) - z_true||^2) = (Wu^T diff)_i * h_i
            for i in range(r_max):
                wut_diff_i = sum(Wu[row][i] * diff[row] for row in range(p))
                grad_g[i] += (wut_diff_i * h[i]) / len(samples)
        g_t = [soft_threshold(g_t[i] - eta * grad_g[i], eta * lmbda) for i in range(r_max)]

    # Verify that inactive components are exactly zeroed out and active components survive
    Wu_pruned, Wd_pruned, r_eff = post_prune_sora(Wu, g_t, Wd)
    assert r_eff == 2 < r_max

    # Verify exact mathematical equivalence between unpruned SoRA forward pass and pruned LoRA forward pass
    max_prune_diff = 0.0
    for x in samples:
        z_unpruned = sora_forward(Wu, g_t, Wd, x)
        z_pruned = matvec(Wu_pruned, matvec(Wd_pruned, x))
        max_prune_diff = max(max_prune_diff, max(abs(a - b) for a, b in zip(z_unpruned, z_pruned)))
    assert max_prune_diff < 1e-15

    # Verify parameter savings: r_eff * (p + q) vs r_max * (p + q)
    assert r_eff * (p + q) * 3 == r_max * (p + q)

    print(
        f"[PASS] Round 689 SoRA (Ding et al., EMNLP 2023): "
        f"r_max={r_max}->r_eff={r_eff}, max_prune_diff={max_prune_diff:.2e}, "
        f"g_t={[round(val, 3) for val in g_t]}"
    )


if __name__ == "__main__":
    main()
