#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 677: Tied-LoRA (Renduchintala et al., NAACL 2024)."""

import math
import random


def matvec(M, x):
    return [sum(M[i][j] * x[j] for j in range(len(x))) for i in range(len(M))]


def main():
    rng = random.Random(677)

    # 1. Verify Table 1 parameter formulas across L=32 layers, hidden size d=4096, rank r=8:
    L, d, r = 32, 4096, 8
    p_lora_joint_qkv = 4 * L * d * r  # 4,194,304 (~4.2M, Section 2.2)
    p_vera = L * (r + 3 * d)  # 393,472
    p_tl1 = d * r  # 32,768
    p_tl2 = d * r + L * (r + 3 * d)  # 426,240
    p_tl3 = 3 * d * r  # 98,304
    p_tl4 = (L + 3 * d) * r  # 98,560
    p_tl5 = 4 * d * r  # 131,072 (~131K, exact 96.875% reduction vs LoRA!)
    p_tl6 = 4 * d * r + L * (r + 3 * d)  # 524,544 (exact 12.506% of LoRA at r=8)

    reduction_tl5 = (p_lora_joint_qkv - p_tl5) / p_lora_joint_qkv
    assert abs(reduction_tl5 - (1.0 - 1.0 / L)) < 1e-12
    assert abs(reduction_tl5 - 0.96875) < 1e-12, f"Expected 96.875% reduction for TL5, got {reduction_tl5}"
    assert p_tl1 < p_tl3 < p_tl4 < p_tl5 < p_vera < p_tl2 < p_tl6 < p_lora_joint_qkv

    # At higher rank r=64, TL6 parameter percentage P% relative to LoRA drops to 4.30%:
    r_high = 64
    p_lora_r64 = 4 * L * d * r_high
    p_tl6_r64 = 4 * d * r_high + L * (r_high + 3 * d)
    pct_tl6_r64 = 100.0 * p_tl6_r64 / p_lora_r64
    assert abs(pct_tl6_r64 - 4.30) < 0.05, f"Expected ~4.3% at r=64 (Table 2), got {pct_tl6_r64:.2f}%"

    # 2. Verify Eq. (1) forward pass and exact linear weight merging across layers:
    # z_l = W_l x + (alpha/r) Lambda_{v_l} B Lambda_{u_l} A x  (with alpha = r)
    d_small, r_small, L_small = 6, 3, 4
    A_tied = [[rng.gauss(0.0, 0.4) for _ in range(d_small)] for _ in range(r_small)]  # r x d (acting on x in R^d)
    B_tied = [[rng.gauss(0.0, 0.4) for _ in range(r_small)] for _ in range(3 * d_small)]  # 3d x r

    max_merge_err = 0.0
    for _ in range(L_small):
        W_l = [[rng.gauss(0.0, 0.5) for _ in range(d_small)] for _ in range(3 * d_small)]
        u_l = [rng.gauss(1.0, 0.2) for _ in range(r_small)]
        v_l = [rng.gauss(1.0, 0.2) for _ in range(3 * d_small)]
        x = [rng.gauss(0.0, 1.0) for _ in range(d_small)]

        # Unmerged Eq. (1) computation:
        ax = matvec(A_tied, x)
        u_ax = [u_l[k] * ax[k] for k in range(r_small)]
        b_u_ax = matvec(B_tied, u_ax)
        delta_z = [v_l[i] * b_u_ax[i] for i in range(3 * d_small)]
        w_x = matvec(W_l, x)
        z_unmerged = [w_x[i] + delta_z[i] for i in range(3 * d_small)]

        # Merged weight matrix W'_l = W_l + diag(v_l) B_tied diag(u_l) A_tied:
        W_merged = [
            [
                W_l[i][j] + v_l[i] * sum(B_tied[i][k] * u_l[k] * A_tied[k][j] for k in range(r_small))
                for j in range(d_small)
            ]
            for i in range(3 * d_small)
        ]
        z_merged = matvec(W_merged, x)
        err = math.sqrt(sum((z_unmerged[i] - z_merged[i]) ** 2 for i in range(3 * d_small)))
        max_merge_err = max(max_merge_err, err)

    assert max_merge_err < 1e-14, f"Tied-LoRA merge error too large: {max_merge_err}"

    print(
        f"[PASS] Round 677 Tied-LoRA (Renduchintala et al., NAACL 2024): "
        f"tl5_reduction={reduction_tl5*100:.3f}%, tl6_r64_pct={pct_tl6_r64:.2f}%, "
        f"max_merge_err={max_merge_err:.2e}"
    )


if __name__ == "__main__":
    main()
