#!/usr/bin/env python3
"""Boundary verification for Round 646: DyLoRA (Valipour et al., EACL 2023 / arXiv:2210.07558)."""

from __future__ import annotations

import math
import random


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    m, k, n = len(a), len(a[0]), len(b[0])
    out = [[0.0] * n for _ in range(m)]
    for i in range(m):
        for p in range(k):
            aip = a[i][p]
            for j in range(n):
                out[i][j] += aip * b[p][j]
    return out


def transpose(a: list[list[float]]) -> list[list[float]]:
    return [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]


def frob_sq(a: list[list[float]], b: list[list[float]]) -> float:
    return sum((a[i][j] - b[i][j]) ** 2 for i in range(len(a)) for j in range(len(a[0])))


def dylora_forward(
    w0: list[list[float]],
    w_up: list[list[float]],
    w_dw: list[list[float]],
    x: list[list[float]],
    b: int,
    alpha: float,
) -> list[list[float]]:
    """Equation (5) & (7) (page 4): h = W_0 x + (alpha / b) W_{up downarrow b} W_{dw downarrow b} x."""
    m, d = len(w0), len(w0[0])
    n_batch = len(x[0])
    w_up_b = [row[:b] for row in w_up]  # m x b
    w_dw_b = [row[:] for row in w_dw[:b]]  # b x d
    delta_b = matmul(matmul(w_up_b, w_dw_b), x)
    base = matmul(w0, x)
    scale = alpha / float(b)
    return [[base[i][j] + scale * delta_b[i][j] for j in range(n_batch)] for i in range(m)]


def main() -> None:
    rng = random.Random(646)
    m, d, r_max = 6, 6, 4
    alpha = 4.0

    # Construct a target task adaptation Delta_W* of rank 4 with decaying singular values [3.0, 1.8, 0.8, 0.3]
    w0 = [[0.0] * d for _ in range(m)]
    target_sv = [3.0, 1.8, 0.8, 0.3]
    delta_star = [[0.0] * d for _ in range(m)]
    for k in range(r_max):
        delta_star[k][k] = target_sv[k]

    # Identity batch X = I_d
    x_batch = [[1.0 if i == j else 0.0 for j in range(d)] for i in range(d)]
    y_target = dylora_forward(delta_star, [[0.0] * r_max for _ in range(m)], [[0.0] * d for _ in range(r_max)], x_batch, 1, 0.0)

    # 1. Train Static LoRA (fixed rank b = r_max = 4) vs DyLoRA (sampling b ~ Uniform{1, ..., r_max})
    def init_lora(seed: int) -> tuple[list[list[float]], list[list[float]]]:
        r_local = random.Random(seed)
        w_up = [[0.0] * r_max for _ in range(m)]
        w_dw = [[r_local.gauss(0.0, 0.2) for _ in range(d)] for _ in range(r_max)]
        return w_up, w_dw

    w_up_static, w_dw_static = init_lora(101)
    w_up_dylora, w_dw_dylora = init_lora(101)

    lr = 0.04
    for step in range(900):
        # Static LoRA always trains with b = r_max
        b_stat = r_max
        pred_s = dylora_forward(w0, w_up_static, w_dw_static, x_batch, b_stat, alpha)
        err_s = [[pred_s[i][j] - y_target[i][j] for j in range(d)] for i in range(m)]
        scale_s = alpha / b_stat
        # Gradients wrt w_up[:, :b_stat] and w_dw[:b_stat, :]
        g_up_s = matmul(err_s, transpose(w_dw_static[:b_stat]))
        g_dw_s = matmul(transpose([row[:b_stat] for row in w_up_static]), err_s)
        for i in range(m):
            for k in range(b_stat):
                w_up_static[i][k] -= lr * scale_s * g_up_s[i][k]
        for k in range(b_stat):
            for j in range(d):
                w_dw_static[k][j] -= lr * scale_s * g_dw_s[k][j]

        # DyLoRA samples b ~ Uniform{1, ..., r_max} at each iteration (Algorithm 1)
        b_dy = (step % r_max) + 1
        pred_d = dylora_forward(w0, w_up_dylora, w_dw_dylora, x_batch, b_dy, alpha)
        err_d = [[pred_d[i][j] - y_target[i][j] for j in range(d)] for i in range(m)]
        scale_d = alpha / b_dy
        g_up_d = matmul(err_d, transpose(w_dw_dylora[:b_dy]))
        g_dw_d = matmul(transpose([row[:b_dy] for row in w_up_dylora]), err_d)
        for i in range(m):
            for k in range(b_dy):
                w_up_dylora[i][k] -= lr * scale_d * g_up_d[i][k]
        for k in range(b_dy):
            for j in range(d):
                w_dw_dylora[k][j] -= lr * scale_d * g_dw_d[k][j]

    # Evaluate across all truncated inference ranks b in {1, 2, 3, 4} (Table 2 property)
    losses_static = [frob_sq(dylora_forward(w0, w_up_static, w_dw_static, x_batch, b, alpha), y_target) for b in range(1, r_max + 1)]
    losses_dylora = [frob_sq(dylora_forward(w0, w_up_dylora, w_dw_dylora, x_batch, b, alpha), y_target) for b in range(1, r_max + 1)]

    # DyLoRA must achieve monotonically decreasing loss as rank b increases 1 -> 2 -> 3 -> 4
    assert losses_dylora[0] > losses_dylora[1] > losses_dylora[2] > losses_dylora[3]
    # And DyLoRA's average loss across low ranks b=1,2,3 must be substantially lower than static LoRA trained only at b=4
    avg_low_dylora = sum(losses_dylora[:3]) / 3.0
    avg_low_static = sum(losses_static[:3]) / 3.0
    assert avg_low_dylora < 0.55 * avg_low_static, (
        f"Expected DyLoRA low-rank loss < 0.55 * static LoRA, got {avg_low_dylora:.4f} vs {avg_low_static:.4f}"
    )

    # 2. Verify Algorithm 1 FROZEN Mode Non-Forgetting Property (Equation 10, page 5):
    # Updating only W_dw^b = W_dw[b-1, :] and W_up^b = W_up[:, b-1] for b = 4 leaves rank 1..3 outputs strictly unchanged!
    pred_rank2_before = dylora_forward(w0, w_up_dylora, w_dw_dylora, x_batch, 2, alpha)
    b_sel = 4
    for i in range(m):
        w_up_dylora[i][b_sel - 1] += 0.5
    for j in range(d):
        w_dw_dylora[b_sel - 1][j] -= 0.5
    pred_rank2_after = dylora_forward(w0, w_up_dylora, w_dw_dylora, x_batch, 2, alpha)
    frozen_prefix_diff = frob_sq(pred_rank2_before, pred_rank2_after)
    assert frozen_prefix_diff == 0.0

    print(
        f"[PASS] Round 646 DyLoRA verified: losses_dylora={[round(x, 4) for x in losses_dylora]}, "
        f"avg_low_dylora={avg_low_dylora:.4f}<<avg_low_static={avg_low_static:.4f}, frozen_prefix_diff={frozen_prefix_diff:.1e}"
    )


if __name__ == "__main__":
    main()
