#!/usr/bin/env python3
"""Constructed boundary verification for Round 660:
LongLoRA and Shifted Sparse Attention (S^2-Attn)
(Chen, Qian, Tang, Lai, Liu, Han, & Jia, ICLR 2024, arXiv:2309.12307).

Verifies:
1. Algorithm 1 (Shifted Sparse Attention / S^2-Attn): splitting H heads into two halves,
   rolling the second half by -G/2 along sequence length S, partitioning into M = S/G
   groups of size G, applying group-local attention, and rolling back by +G/2.
2. Quadratic complexity reduction per layer: M * G^2 = S^2 / M attention pairs per head
   (e.g., 4x reduction for M = 4 groups).
3. Cross-group information flow boundary: unshifted short attention (Pattern 1 only)
   keeps all M groups strictly isolated even across multiple layers (zero cross-group
   sensitivity), whereas S^2-Attn propagates token information across all neighboring
   groups within 2 layers while remaining compatible with full attention at inference.
"""

from __future__ import annotations
import math
import random


def softmax_row(scores: list[float]) -> list[float]:
    m = max(scores)
    exps = [math.exp(s - m) for s in scores]
    total = sum(exps)
    return [e / total for e in exps]


def group_local_attention(
    Q: list[list[float]],
    K: list[list[float]],
    V: list[list[float]],
    G: int,
) -> list[list[float]]:
    """Compute local self-attention inside disjoint groups of length G."""
    S = len(Q)
    D = len(Q[0])
    scale = 1.0 / math.sqrt(D)
    out = [[0.0] * D for _ in range(S)]
    for g_start in range(0, S, G):
        g_end = g_start + G
        for i in range(g_start, g_end):
            scores = [
                sum(Q[i][d] * K[j][d] for d in range(D)) * scale
                for j in range(g_start, g_end)
            ]
            probs = softmax_row(scores)
            for d in range(D):
                out[i][d] = sum(probs[idx] * V[g_start + idx][d] for idx in range(G))
    return out


def roll_seq(X: list[list[float]], shift: int) -> list[list[float]]:
    """Roll sequence tensor X of shape (S, D) by `shift` positions along axis 0
    (matching PyTorch tensor.roll(shift, 1) in Algorithm 1)."""
    S = len(X)
    return [X[(i - shift) % S] for i in range(S)]


def s2_attn_layer(
    X: list[list[float]],
    W_O: list[list[float]],
    G: int,
    use_shift: bool,
) -> list[list[float]]:
    """Two-head attention block where Head 0 uses Pattern 1 (no shift) and
    Head 1 uses Pattern 2 (shift by G//2) if use_shift=True, followed by output mixing W_O."""
    S = len(X)
    D_total = len(X[0])
    D_head = D_total // 2
    # Split into 2 heads along feature dimension (Algorithm 1, line 1)
    h0 = [row[:D_head] for row in X]
    h1 = [row[D_head:] for row in X]

    out0 = group_local_attention(h0, h0, h0, G)
    if use_shift:
        # Roll by -G//2, attend in groups of G, then roll back by +G//2
        h1_shifted = roll_seq(h1, -(G // 2))
        out1_shifted = group_local_attention(h1_shifted, h1_shifted, h1_shifted, G)
        out1 = roll_seq(out1_shifted, +(G // 2))
    else:
        out1 = group_local_attention(h1, h1, h1, G)

    # Concatenate heads and project via W_O in R^{D_total x D_total}
    concat = [out0[i] + out1[i] for i in range(S)]
    proj = [
        [sum(concat[i][k] * W_O[k][d] for k in range(D_total)) for d in range(D_total)]
        for i in range(S)
    ]
    return proj


def main() -> None:
    rng = random.Random(20230912)
    S = 16
    G = 4
    M = S // G  # 4 groups
    D_total = 4

    # 1. Verify quadratic attention complexity savings
    full_attn_pairs = S * S
    s2_attn_pairs = M * (G * G)
    assert full_attn_pairs == 256
    assert s2_attn_pairs == 64
    assert full_attn_pairs // s2_attn_pairs == M == 4

    # 2. Verify cross-group information flow vs. unshifted Pattern-1-only attention
    X_base = [[rng.uniform(-1.0, 1.0) for _ in range(D_total)] for _ in range(S)]
    W_O = [[rng.uniform(-0.5, 0.5) for _ in range(D_total)] for _ in range(D_total)]

    # Perturb token at index 3 (inside Group 0: indices 0..3)
    X_pert = [list(row) for row in X_base]
    for d in range(D_total):
        X_pert[3][d] += 2.0

    # Two layers of unshifted short attention (Pattern 1 only)
    u_base = s2_attn_layer(s2_attn_layer(X_base, W_O, G, use_shift=False), W_O, G, use_shift=False)
    u_pert = s2_attn_layer(s2_attn_layer(X_pert, W_O, G, use_shift=False), W_O, G, use_shift=False)

    # Check sensitivity in Group 1 (indices 4..7): must be identically 0 for unshifted short attention
    unshifted_cross_group_diff = max(
        abs(u_base[i][d] - u_pert[i][d]) for i in range(4, 8) for d in range(D_total)
    )
    assert unshifted_cross_group_diff == 0.0, (
        f"Expected 0 cross-group flow for unshifted short attention, got {unshifted_cross_group_diff}"
    )

    # Two layers of S^2-Attn (Pattern 1 in Head 0, Pattern 2 shifted by G/2=2 in Head 1)
    s_base = s2_attn_layer(s2_attn_layer(X_base, W_O, G, use_shift=True), W_O, G, use_shift=True)
    s_pert = s2_attn_layer(s2_attn_layer(X_pert, W_O, G, use_shift=True), W_O, G, use_shift=True)

    s2_cross_group_diff = max(
        abs(s_base[i][d] - s_pert[i][d]) for i in range(4, 8) for d in range(D_total)
    )
    assert s2_cross_group_diff > 1e-3, (
        f"Expected positive cross-group information flow in S^2-Attn, got {s2_cross_group_diff}"
    )

    print(
        f"[PASS] Round 660 LongLoRA / S^2-Attn (Chen et al. 2024): "
        f"attn_pairs_ratio={full_attn_pairs}/{s2_attn_pairs}={M}x, "
        f"unshifted_cross_group_diff={unshifted_cross_group_diff:.2e}, "
        f"s2_cross_group_diff={s2_cross_group_diff:.4f}"
    )


if __name__ == "__main__":
    main()
