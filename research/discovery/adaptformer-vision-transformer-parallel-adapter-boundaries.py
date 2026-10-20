#!/usr/bin/env python3
"""Boundary verification for Round 696: AdaptFormer (Chen et al., NeurIPS 2022, arXiv:2205.13535)."""

import math


def relu(v: list[float]) -> list[float]:
    return [max(0.0, x) for x in v]


def main() -> int:
    # 1. Verify Equations (3)-(4) (Section 3.2, pp. 4-5) & Algorithm 1 (Appendix A.8, p. 21):
    # x_tilde_l = ReLU(LN(x'_l) W_down + b_down) W_up + b_up
    # x_l = MLP(LN(x'_l)) + s * x_tilde_l + x'_l
    # At initialization: W_down ~ Kaiming, W_up = 0, b_down = 0, b_up = 0 => x_tilde_l = 0 => exact identity match
    d = 6
    d_hat = 2
    s = 0.10
    x_prime = [0.8, -0.4, 1.2, -0.6, 0.3, -0.5]
    ln_x = [0.75, -0.45, 1.15, -0.65, 0.25, -0.55]
    mlp_out = [0.3, -0.2, 0.5, 0.1, -0.4, 0.2]

    W_down = [
        [0.5, -0.3],
        [-0.2, 0.4],
        [0.6, 0.1],
        [-0.4, 0.5],
        [0.2, -0.6],
        [-0.1, 0.3],
    ]
    b_down_init = [0.0, 0.0]
    W_up_init = [[0.0] * d for _ in range(d_hat)]
    b_up_init = [0.0] * d

    down_init = relu(
        [sum(ln_x[i] * W_down[i][j] for i in range(d)) + b_down_init[j] for j in range(d_hat)]
    )
    up_init = [
        sum(down_init[j] * W_up_init[j][i] for j in range(d_hat)) + b_up_init[i] for i in range(d)
    ]
    x_l_pretrained = [mlp_out[i] + x_prime[i] for i in range(d)]
    x_l_adapt_init = [mlp_out[i] + s * up_init[i] + x_prime[i] for i in range(d)]
    init_diff = max(abs(x_l_pretrained[i] - x_l_adapt_init[i]) for i in range(d))
    assert init_diff == 0.0, f"Zero initialization of W_up/biases must preserve identity: {init_diff}"

    # 2. Verify tunable parameter formula per layer: 2 * d * d_hat + d_hat + d (Section 3.3, p. 5)
    d_vit, L_vit, d_hat_vit = 768, 12, 64
    params_per_layer = 2 * d_vit * d_hat_vit + d_hat_vit + d_vit
    total_adapter_params = L_vit * params_per_layer
    vit_base_params = 86_040_000
    pct_params = 100.0 * total_adapter_params / vit_base_params
    assert params_per_layer == 99_136
    assert pct_params < 2.0

    # 3. Verify Parallel vs Sequential insertion (Section 4.5, Figure 6 & Table 3b, pp. 8-9):
    # Suppose frozen pre-trained MLP projects out coordinates (0, 1) of LN(x'_l) that carry downstream video motion signal,
    # i.e. MLP(LN(x'_l)) depends only on coordinates 2..5.
    # Then Sequential insertion (which feeds MLP(LN(x'_l)) into AdaptMLP) loses access to coordinates (0, 1),
    # whereas Parallel insertion feeds LN(x'_l) directly into AdaptMLP and recovers the target downstream residual.
    samples_ln = [
        [1.5, 0.0, 0.2, -0.1, 0.3, 0.1],
        [0.0, 1.5, -0.2, 0.1, -0.1, 0.2],
        [1.2, 1.2, 0.1, 0.2, -0.2, -0.1],
    ]
    # Frozen MLP zeroes coordinates 0 and 1:
    frozen_mlp_outputs = [[0.0, 0.0, row[2], row[3], row[4], row[5]] for row in samples_ln]
    # Downstream target requires adding s * [row[0], row[1], 0, 0, 0, 0] to frozen_mlp(row) + x_prime:
    W_down_task = [
        [1.0, 0.0],
        [0.0, 1.0],
        [0.0, 0.0],
        [0.0, 0.0],
        [0.0, 0.0],
        [0.0, 0.0],
    ]
    W_up_task = [
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
    ]

    def adapt_branch(inp: list[float]) -> list[float]:
        h = relu([sum(inp[i] * W_down_task[i][j] for i in range(d)) for j in range(d_hat)])
        return [sum(h[j] * W_up_task[j][i] for j in range(d_hat)) for i in range(d)]

    err_parallel = 0.0
    err_sequential = 0.0
    for row, mlp_y in zip(samples_ln, frozen_mlp_outputs):
        target_delta = [s * row[0], s * row[1], 0.0, 0.0, 0.0, 0.0]
        par_delta = [s * v for v in adapt_branch(row)]
        seq_delta = [s * v for v in adapt_branch(mlp_y)]
        err_parallel += sum((par_delta[i] - target_delta[i]) ** 2 for i in range(d))
        err_sequential += sum((seq_delta[i] - target_delta[i]) ** 2 for i in range(d))

    assert err_parallel < 1e-16
    assert err_parallel < err_sequential

    print(
        f"[PASS] Round 696 AdaptFormer (Chen et al., NeurIPS 2022): init_diff={init_diff:.1e}, "
        f"layer_params={params_per_layer} ({pct_params:.2f}% of ViT-B), "
        f"err_parallel={err_parallel:.2e} << err_sequential={err_sequential:.4f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
