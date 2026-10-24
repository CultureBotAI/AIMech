#!/usr/bin/env python3
"""Constructed boundary verification for LightConv and DynamicConv (Wu et al., ICLR 2019, arXiv:1901.10430)."""

import math


def conv_parameter_counts(d_model, kernel_k, num_heads_h):
    """Compare parameter counts of standard conv (d^2 * k), depthwise conv (d * k), and LightConv (H * k) (Section 3)."""
    std_conv = (d_model ** 2) * kernel_k
    dw_conv = d_model * kernel_k
    light_conv = num_heads_h * kernel_k
    return std_conv, dw_conv, light_conv


def temporal_softmax(kernel_row):
    """Normalize kernel weights across temporal dimension k via softmax (Section 3)."""
    m = max(kernel_row)
    exps = [math.exp(w - m) for w in kernel_row]
    s = sum(exps)
    return [e / s for e in exps]


def lightconv_step(x_seq, w_heads, i_pos, c_channel, d_model):
    """Compute LightConv(X, W_{ceil(cH/d), :}, i, c) = DepthwiseConv(X, softmax(W_h), i, c) (Section 3)."""
    num_heads_h = len(w_heads)
    kernel_k = len(w_heads[0])
    # 1-indexed channel formula ceil((c+1)*H/d) - 1 in 0-indexed Python
    h_idx = (c_channel * num_heads_h) // d_model
    norm_w = temporal_softmax(w_heads[h_idx])
    half_k = (kernel_k + 1) // 2
    n_seq = len(x_seq)
    acc = 0.0
    for j in range(1, kernel_k + 1):
        src_pos = i_pos + j - half_k
        if 0 <= src_pos < n_seq:
            acc += norm_w[j - 1] * x_seq[src_pos][c_channel]
    return acc, norm_w


def dynamicconv_step(x_seq, w_q_tensor, i_pos, c_channel, d_model):
    """Compute DynamicConv(X, i, c) = LightConv(X, f(X_i)_{h, :}, i, c) where f(X_i) = W^Q X_i (Section 4)."""
    num_heads_h = len(w_q_tensor)
    kernel_k = len(w_q_tensor[0])
    # Predict time-step dependent kernel f(X_i) in R^{H x k} from current token X_i only
    f_xi = [
        [sum(w_q_tensor[h][j][c] * x_seq[i_pos][c] for c in range(d_model)) for j in range(kernel_k)]
        for h in range(num_heads_h)
    ]
    return lightconv_step(x_seq, f_xi, i_pos, c_channel, d_model)


def main():
    # 1. Verify Section 3 parameter reduction illustration: d=1024, k=7, H=16 -> 7,340,032 vs 7,168 vs 112
    std_p, dw_p, lc_p = conv_parameter_counts(d_model=1024, kernel_k=7, num_heads_h=16)
    assert std_p == 7340032 and dw_p == 7168 and lc_p == 112

    # 2. Verify LightConv reuses identical softmax-normalized kernel across all time steps i
    x_seq = [
        [1.0, 2.0, -1.0, 0.5],
        [0.5, -1.0, 2.0, 1.5],
        [2.0, 0.5, 1.0, -0.5],
        [-1.0, 1.5, 0.5, 2.0],
    ]
    w_heads = [[0.2, 1.1, -0.4], [-0.5, 0.8, 0.3]]  # H=2, k=3, d=4
    out_lc_1, ker_lc_1 = lightconv_step(x_seq, w_heads, i_pos=1, c_channel=0, d_model=4)
    out_lc_2, ker_lc_2 = lightconv_step(x_seq, w_heads, i_pos=2, c_channel=0, d_model=4)
    assert ker_lc_1 == ker_lc_2  # Time-invariant kernel in LightConv
    assert abs(sum(ker_lc_1) - 1.0) < 1e-12

    # 3. Verify DynamicConv generates distinct softmax-normalized kernels at different time steps i
    w_q = [
        [[0.1 * (h + 1) * (j + 1) * (c - 1.5) for c in range(4)] for j in range(3)]
        for h in range(2)
    ]
    out_dc_1, ker_dc_1 = dynamicconv_step(x_seq, w_q, i_pos=1, c_channel=0, d_model=4)
    out_dc_2, ker_dc_2 = dynamicconv_step(x_seq, w_q, i_pos=2, c_channel=0, d_model=4)
    assert ker_dc_1 != ker_dc_2  # Position-dependent kernel in DynamicConv
    assert abs(sum(ker_dc_1) - 1.0) < 1e-12 and abs(sum(ker_dc_2) - 1.0) < 1e-12

    # 4. Verify boundary case W^Q = 0: DynamicConv collapses to uniform moving-average kernel 1/k
    w_q_zero = [[[0.0 for _ in range(4)] for _ in range(3)] for _ in range(2)]
    _, ker_zero = dynamicconv_step(x_seq, w_q_zero, i_pos=1, c_channel=0, d_model=4)
    assert all(abs(w - 1.0 / 3.0) < 1e-12 for w in ker_zero)

    print(
        f"LightConv/DynamicConv verification passed: params=({std_p}, {dw_p}, {lc_p}), "
        f"ker_dc_1={[round(x, 3) for x in ker_dc_1]} != ker_dc_2={[round(x, 3) for x in ker_dc_2]}"
    )


if __name__ == "__main__":
    main()
