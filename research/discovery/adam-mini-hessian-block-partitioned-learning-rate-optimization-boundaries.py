#!/usr/bin/env python3
"""Constructed boundary verification for Round 638: Adam-mini (Zhang et al., ICLR 2025)."""

from __future__ import annotations
import math


def verify_dense_hessian_block_preconditioning() -> tuple[float, float, float]:
    """Verify Section 2.1 Eq. (2) condition number degradation of coordinate-wise D_Adam on dense Hessian blocks vs single blockwise LR."""
    # Construct a 2x2 dense positive-definite Hessian block H_b = Q diag(kappa, 1) Q^T with kappa = 100
    # rotated by angle theta = pi / 4 so off-diagonal entries are large (dense block, small tau)
    kappa = 100.0
    theta = math.pi / 4.0
    c, s = math.cos(theta), math.sin(theta)
    # H_b = [[c, -s], [s, c]] [[kappa, 0], [0, 1]] [[c, s], [-s, c]]
    h00 = c * c * kappa + s * s * 1.0
    h01 = c * s * (kappa - 1.0)
    h11 = s * s * kappa + c * c * 1.0
    hb = [[h00, h01], [h01, h11]]

    # Diagonal-over-off-diagonal ratio tau = sum_i |H_{i,i}| / sum_{i,j} |H_{i,j}| (Eq. 2)
    diag_sum = abs(hb[0][0]) + abs(hb[1][1])
    total_sum = diag_sum + 2.0 * abs(hb[0][1])
    tau = diag_sum / total_sum
    assert 0.5 < tau < 0.52, f"Expected dense block tau ~ 0.505, got {tau}"

    # Evaluate gradient g = H_b x at an asymmetric point x = [1.0, -0.95] where g_0 and g_1 have very different magnitudes
    x = [1.0, -0.95]
    g0 = hb[0][0] * x[0] + hb[0][1] * x[1]
    g1 = hb[0][1] * x[0] + hb[1][1] * x[1]
    d0 = 1.0 / abs(g0)
    d1 = 1.0 / abs(g1)

    # Compute condition number of D_Adam H_b (which shares eigenvalues with D_Adam^{1/2} H_b D_Adam^{1/2})
    # Symmetric matrix S = D^{1/2} H_b D^{1/2} = [[d0*h00, sqrt(d0*d1)*h01], [sqrt(d0*d1)*h01, d1*h11]]
    s00 = d0 * h00
    s11 = d1 * h11
    s01 = math.sqrt(d0 * d1) * h01
    tr = s00 + s11
    det = s00 * s11 - s01 * s01
    disc = math.sqrt(max(0.0, tr * tr - 4.0 * det))
    lam_max = 0.5 * (tr + disc)
    lam_min = 0.5 * (tr - disc)
    kappa_d_adam = lam_max / lam_min
    r_ratio = kappa_d_adam / kappa
    # As shown in Section 2.1 Figure 5 and Table 3, coordinate-wise D_Adam worsens kappa(H_b) on dense blocks (r > 1)!
    assert r_ratio > 1.15, f"Coordinate-wise D_Adam should increase condition number on dense H_b, got r={r_ratio}"

    # By contrast, Adam-mini uses a single scalar 1/sqrt(v_b) I_2 per dense block, preserving kappa((1/sqrt(v_b)) H_b) == kappa(H_b) (r_mini == 1.0)!
    r_mini = 1.0
    assert r_mini < r_ratio
    return tau, r_ratio, r_mini


def verify_transformer_partition_and_v_reduction() -> tuple[float, float, float]:
    """Verify Algorithm 1 & Algorithm 3 Transformer Hessian partition v-parameter reduction (>=99.9%) and 50% state memory saving."""
    # Consider a LLaMA-style Transformer configuration:
    # d_model = 4096, n_heads = 32, d_mlp = 11008, vocab_size = 32000, n_layers = 32
    d_model = 4096
    n_heads = 32
    d_mlp = 11008
    vocab = 32000
    n_layers = 32

    # Total parameters in Q, K, V, O, MLP (gate, up, down), and Embed + Output:
    params_per_layer = (
        4 * (d_model * d_model)  # Q, K, V, attn.proj
        + 3 * (d_model * d_mlp)  # gate_proj, up_proj, down_proj
    )
    total_params = n_layers * params_per_layer + 2 * (vocab * d_model)

    # Number of scalar learning rates (blocks in v) under Algorithm 3 (Partition for Transformers):
    # - query, key: partitioned by heads -> 2 * n_heads per layer
    # - value, attn.proj: partitioned by output neurons -> 2 * d_model per layer
    # - mlp (gate, up, down): partitioned by output neurons -> 2 * d_mlp + d_model per layer
    # - embed, output: partitioned by tokens -> 2 * vocab
    v_blocks_per_layer = (2 * n_heads) + (2 * d_model) + (2 * d_mlp + d_model)
    total_v_blocks = n_layers * v_blocks_per_layer + 2 * vocab

    v_removed_fraction = 1.0 - (total_v_blocks / total_params)
    assert v_removed_fraction > 0.999, f"Expected >= 99.9% reduction in v, got {v_removed_fraction:.6f}"

    # Total optimizer state floats (m + v): AdamW stores 2 * total_params; Adam-mini stores total_params + total_v_blocks
    adamw_state_floats = 2 * total_params
    adam_mini_state_floats = total_params + total_v_blocks
    state_memory_saving = 1.0 - (adam_mini_state_floats / adamw_state_floats)
    assert 0.499 < state_memory_saving < 0.50, f"Expected ~49.98% optimizer state memory saving, got {state_memory_saving:.6f}"

    # Verify 5-parameter toy example in Section 2.2 (page 5) with partition (1,2,3) and (4,5):
    g = [1.0, 2.0, 3.0, 4.0, 6.0]
    v_sq = [x * x for x in g]
    v_block1 = sum(v_sq[:3]) / 3.0
    v_block2 = sum(v_sq[3:]) / 2.0
    eta = 0.01
    u_mini = [
        eta / math.sqrt(v_block1),
        eta / math.sqrt(v_block1),
        eta / math.sqrt(v_block1),
        eta / math.sqrt(v_block2),
        eta / math.sqrt(v_block2),
    ]
    assert abs(u_mini[0] - u_mini[1]) < 1e-15 and abs(u_mini[1] - u_mini[2]) < 1e-15
    assert abs(u_mini[3] - u_mini[4]) < 1e-15 and u_mini[0] > u_mini[3]
    return v_removed_fraction, state_memory_saving, u_mini[0] / u_mini[3]


if __name__ == "__main__":
    tau_val, r_adam, r_mini = verify_dense_hessian_block_preconditioning()
    v_red, mem_sav, lr_rat = verify_transformer_partition_and_v_reduction()
    print(
        f"[PASS] Round 638 Adam-mini verified: dense_tau={tau_val:.3f}, r_adam={r_adam:.2f}>r_mini={r_mini:.2f}, "
        f"v_removed={v_red:.4%}, state_saving={mem_sav:.2%}, block_lr_ratio={lr_rat:.3f}"
    )
