#!/usr/bin/env python3
"""Boundary verification for Round 697: Convpass (Jie & Deng, 2022, arXiv:2207.07039)."""

import math


def gelu(x: float) -> float:
    return 0.5 * x * (1.0 + math.erf(x / math.sqrt(2.0)))


def main() -> int:
    # 1. Verify exact trainable parameter formula (Section 3.2, p. 4):
    # Total trainable parameters across L ViT layers (2 Convpass modules per layer: alongside MHSA and MLP):
    # P = 2 * L * ((2h + 1)d + 9h^2 + 2h)
    L, d, h = 12, 768, 8
    params_1x1_down = d * h + h
    params_3x3_conv = 9 * (h ** 2) + h
    params_1x1_up = h * d + d
    params_one_module = params_1x1_down + params_3x3_conv + params_1x1_up
    formula_one_module = (2 * h + 1) * d + 9 * (h ** 2) + 2 * h
    assert params_one_module == formula_one_module
    total_params = 2 * L * formula_one_module
    assert total_params == 327_552  # ~0.33M parameters reported in Section 1 (p. 2) and Table 1 (p. 4)

    # 2. Verify Section 3.2 (Figure 3, p. 3) & Section 4.4 (Table 5, p. 7):
    # Convpass reshapes the 1D sequence of N = H * W patch tokens back into a 2D H x W spatial grid
    # and applies a 3x3 convolution (while treating [cls] as an individual 1x1 image),
    # whereas a language-oriented 1x1 bottleneck adapter ("1x1 @MLP & 1x1 @MHSA" in Table 5)
    # is invariant to spatial permutations of patch tokens.
    H, W = 3, 3
    # Construct two 1D token sequences (N=9 patch tokens + 1 [cls] token, d=1, h=1) with identical token multisets:
    # Image A has a contiguous 2x2 bright block at top-left ((0,0),(0,1),(1,0),(1,1));
    # Image B scatters those exact 4 bright tokens to the 4 isolated corners ((0,0),(0,2),(2,0),(2,2)).
    cls_tok = 0.5
    grid_A = [
        [1.0, 1.0, 0.0],
        [1.0, 1.0, 0.0],
        [0.0, 0.0, 0.0],
    ]
    grid_B = [
        [1.0, 0.0, 1.0],
        [0.0, 0.0, 0.0],
        [1.0, 0.0, 1.0],
    ]
    seq_A = [cls_tok] + [grid_A[r][c] for r in range(H) for c in range(W)]
    seq_B = [cls_tok] + [grid_B[r][c] for r in range(H) for c in range(W)]
    assert sorted(seq_A) == sorted(seq_B)

    # Language-oriented 1x1 bottleneck (3x3 replaced by 1x1, Table 5 row 1):
    def convpass_1x1_only(seq: list[float]) -> list[float]:
        # Token-wise 1x1 down -> GELU -> 1x1 mid -> GELU -> 1x1 up
        return [gelu(gelu(x * 0.8) * 1.2) * 0.9 for x in seq]

    # Vision-oriented Convpass with 3x3 spatial kernel (center weight=1.0, 8-neighbor weight=0.5):
    def convpass_3x3(seq: list[float]) -> list[float]:
        # Step 1: 1x1 down + GELU
        down = [gelu(x * 0.8) for x in seq]
        cls_feat = down[0]
        patches = down[1:]
        # Step 2: Restore 2D structure for patches; [cls] treated as 1x1 image (zero-padded neighbors = 0)
        cls_conv = gelu(1.0 * cls_feat)
        grid = [[patches[r * W + c] for c in range(W)] for r in range(H)]
        conv_patches = []
        for r in range(H):
            for c in range(W):
                acc = 0.0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < H and 0 <= nc < W:
                            w = 1.0 if (dr == 0 and dc == 0) else 0.5
                            acc += w * grid[nr][nc]
                conv_patches.append(gelu(acc))
        # Step 3: Flatten and 1x1 up
        return [0.9 * cls_conv] + [0.9 * p for p in conv_patches]

    out_1x1_A = convpass_1x1_only(seq_A)
    out_1x1_B = convpass_1x1_only(seq_B)
    # Pooled patch representation under 1x1-only adapter is completely blind to 2D spatial layout:
    mean_1x1_A = sum(out_1x1_A[1:]) / 9.0
    mean_1x1_B = sum(out_1x1_B[1:]) / 9.0
    assert abs(mean_1x1_A - mean_1x1_B) < 1e-15

    # Convpass 3x3 captures 2D neighborhood clustering and produces strictly stronger activation for contiguous 2x2 object:
    out_3x3_A = convpass_3x3(seq_A)
    out_3x3_B = convpass_3x3(seq_B)
    mean_3x3_A = sum(out_3x3_A[1:]) / 9.0
    mean_3x3_B = sum(out_3x3_B[1:]) / 9.0
    assert mean_3x3_A > mean_3x3_B + 0.15
    assert abs(out_3x3_A[0] - out_3x3_B[0]) < 1e-15  # [cls] processed as isolated 1x1 image

    print(
        f"[PASS] Round 697 Convpass (Jie & Deng, 2022): total_params(L=12,d=768,h=8)={total_params}, "
        f"1x1_spatial_diff={abs(mean_1x1_A - mean_1x1_B):.2e}, "
        f"3x3_contiguous={mean_3x3_A:.4f} > 3x3_scattered={mean_3x3_B:.4f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
