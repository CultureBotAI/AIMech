#!/usr/bin/env python3
"""Constructed boundary verification for Lite Transformer with Long-Short Range Attention (Wu et al., ICLR 2020)."""


def transformer_block_mult_adds(seq_len_n, d_model, d_ffn):
    """Compute Mult-Adds for standard Transformer block: Attention O(4 N d^2 + N^2 d) and FFN O(2 d d_ffn N) (Section 3)."""
    attn_macs = 4 * seq_len_n * (d_model ** 2) + (seq_len_n ** 2) * d_model
    ffn_macs = 2 * seq_len_n * d_model * d_ffn
    return attn_macs, ffn_macs


def lsra_dual_branch_mult_adds(seq_len_n, d_model, conv_kernels=(3, 5, 7, 31)):
    """Compute Mult-Adds for Long-Short Range Attention (LSRA) with channel split d/2 (Section 4 & 5.3).

    Left branch (Global Attention on d_att = d/2):
      Q, K, V projections + output projection on d/2 channels + attention scores on d/2.
    Right branch (Local LightConv on d_conv = d/2):
      GLU input linear (d/2 -> d) + depthwise separable conv with kernels + output linear (d/2 -> d/2).
    """
    d_half = d_model // 2
    # Global branch: 4 * N * d_half^2 + N^2 * d_half
    global_attn_macs = 4 * seq_len_n * (d_half ** 2) + (seq_len_n ** 2) * d_half
    # Local branch: GLU linear (d_half * 2*d_half) + output linear (d_half * d_half) + depthwise conv
    avg_k = sum(conv_kernels) / len(conv_kernels)
    local_conv_macs = seq_len_n * (2 * (d_half ** 2) + (d_half ** 2) + int(avg_k * d_half))
    return global_attn_macs + local_conv_macs, global_attn_macs, local_conv_macs


def lsra_forward_split_and_concat(x_seq):
    """Verify channel-wise split into global attention branch and local depthwise-conv branch followed by concatenation."""
    seq_len = len(x_seq)
    d_model = len(x_seq[0])
    assert d_model % 2 == 0
    d_half = d_model // 2
    left_branch = [row[:d_half] for row in x_seq]
    right_branch = [row[d_half:] for row in x_seq]

    # Global branch: uniform global average pooling proxy (captures long-range tokens)
    global_out = [
        [sum(left_branch[t][c] for t in range(seq_len)) / seq_len for c in range(d_half)]
        for _ in range(seq_len)
    ]
    # Local branch: 1D window-3 moving average proxy (captures diagonal neighborhood)
    local_out = []
    for t in range(seq_len):
        t_prev = max(0, t - 1)
        t_next = min(seq_len - 1, t + 1)
        local_out.append([
            (right_branch[t_prev][c] + right_branch[t][c] + right_branch[t_next][c]) / 3.0
            for c in range(d_half)
        ])
    merged = [global_out[t] + local_out[t] for t in range(seq_len)]
    assert len(merged) == seq_len and len(merged[0]) == d_model
    return merged


def main():
    # 1. Verify Section 3 observation: for short NLP sequence N=30 and 1:4 bottleneck (d=512, d_ffn=2048),
    # FFN Mult-Adds exceed 1D Self-Attention Mult-Adds
    attn_base, ffn_base = transformer_block_mult_adds(seq_len_n=30, d_model=512, d_ffn=2048)
    assert ffn_base > attn_base

    # 2. Flattening the bottleneck (d_model=512, d_ffn=512) makes Attention the dominant component
    attn_flat, ffn_flat = transformer_block_mult_adds(seq_len_n=30, d_model=512, d_ffn=512)
    assert attn_flat > ffn_flat

    # 3. Replacing full-width attention with channel-split LSRA cuts context-extractor MACs by > 2x
    lsra_total, lsra_glob, lsra_loc = lsra_dual_branch_mult_adds(seq_len_n=30, d_model=512)
    assert lsra_total < 0.5 * attn_flat

    # 4. Verify channel split and parallel global/local branch concatenation preserves tensor shape
    x_in = [[float(t + c) for c in range(8)] for t in range(6)]
    out = lsra_forward_split_and_concat(x_in)
    assert len(out) == 6 and len(out[0]) == 8

    print(
        f"Lite Transformer LSRA verification passed: ffn_base={ffn_base} > attn_base={attn_base}, "
        f"attn_flat={attn_flat} > ffn_flat={ffn_flat}, lsra_total={lsra_total} < 0.5*attn_flat={int(0.5*attn_flat)}"
    )


if __name__ == "__main__":
    main()
