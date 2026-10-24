#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 655: ReFT / LoReFT (Wu et al., NeurIPS 2024)."""

import math
import random


def gram_schmidt_rows(mat: list[list[float]]) -> list[list[float]]:
    """Orthonormalize rows of an r x d matrix R so that R R^T = I_r."""
    ortho: list[list[float]] = []
    for row in mat:
        v = list(row)
        for u in ortho:
            proj = sum(vi * ui for vi, ui in zip(v, u))
            v = [vi - proj * ui for vi, ui in zip(v, u)]
        norm = math.sqrt(sum(vi * vi for vi in v))
        assert norm > 1e-10
        ortho.append([vi / norm for vi in v])
    return ortho


def verify_loreft_subspace_invariance_and_projection() -> None:
    """Verify Equation (2): Phi_LoReFT(h) = h + R^T (W h + b - R h) edits only the row-space of R."""
    rng = random.Random(20240403)
    d, r = 16, 4
    r_raw = [[rng.gauss(0.0, 1.0) for _ in range(d)] for _ in range(r)]
    r_mat = gram_schmidt_rows(r_raw)
    w_mat = [[rng.gauss(0.0, 0.5) for _ in range(d)] for _ in range(r)]
    b_vec = [rng.gauss(0.0, 0.2) for _ in range(r)]
    h = [rng.gauss(0.0, 1.0) for _ in range(d)]

    # Verify R R^T = I_r
    for i in range(r):
        for j in range(r):
            dot = sum(r_mat[i][k] * r_mat[j][k] for k in range(d))
            target = 1.0 if i == j else 0.0
            assert abs(dot - target) < 1e-12

    # Compute target subspace coordinates z_target = W h + b in R^r
    z_target = [sum(w_mat[i][k] * h[k] for k in range(d)) + b_vec[i] for i in range(r)]
    # Current subspace coordinates z_orig = R h in R^r
    z_orig = [sum(r_mat[i][k] * h[k] for k in range(d)) for i in range(r)]
    diff = [z_target[i] - z_orig[i] for i in range(r)]

    # Phi_LoReFT(h) = h + R^T (W h + b - R h)
    h_edit = [
        h[k] + sum(r_mat[i][k] * diff[i] for i in range(r))
        for k in range(d)
    ]

    # Property 1: In the subspace spanned by R, R * Phi_LoReFT(h) == W h + b exactly!
    z_after = [sum(r_mat[i][k] * h_edit[k] for k in range(d)) for i in range(r)]
    for i in range(r):
        assert abs(z_after[i] - z_target[i]) < 1e-12, f"Subspace replacement failed: {z_after[i]} vs {z_target[i]}"

    # Property 2: Orthogonal complement (I - R^T R) h is completely invariant under Phi_LoReFT!
    # Pick any vector v_perp orthogonal to all rows of R:
    v_rand = [rng.gauss(0.0, 1.0) for _ in range(d)]
    v_perp = list(v_rand)
    for row in r_mat:
        proj = sum(vk * rk for vk, rk in zip(v_perp, row))
        v_perp = [vk - proj * rk for vk, rk in zip(v_perp, row)]

    dot_before = sum(v_perp[k] * h[k] for k in range(d))
    dot_after = sum(v_perp[k] * h_edit[k] for k in range(d))
    assert abs(dot_before - dot_after) < 1e-12, "Orthogonal complement must be strictly preserved by LoReFT"


def verify_reft_parameter_efficiency_vs_lora() -> None:
    """Verify parameter count comparison between tied LoReFT and LoRA across a Transformer layer."""
    # LLaMA-7B style dimensions: d = 4096, r = 4, 32 layers
    # Tied LoReFT intervention at a layer has R in R^{r x d}, W in R^{r x d}, b in R^r -> 2*r*d + r parameters
    d = 4096
    r = 4
    n_layers = 32
    params_loreft = n_layers * (2 * r * d + r)
    # LoRA at rank r=8 across 4 attention + 3 MLP projections (7 matrices per layer, simplified square d x d)
    r_lora = 8
    params_lora = n_layers * 7 * (2 * r_lora * d)
    ratio = params_lora / params_loreft
    assert ratio > 10.0, f"Expected >10x parameter reduction, got {ratio:.2f}x"


if __name__ == "__main__":
    verify_loreft_subspace_invariance_and_projection()
    verify_reft_parameter_efficiency_vs_lora()
    print("[PASS] Round 655 ReFT/LoReFT boundary and mathematical verification succeeded.")
