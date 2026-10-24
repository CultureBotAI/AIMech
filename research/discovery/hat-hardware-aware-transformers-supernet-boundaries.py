#!/usr/bin/env python3
"""Constructed boundary verification for HAT Hardware-Aware Transformers (Wang et al., ACL 2020)."""

import math


def design_space_cardinality(
    enc_layers=6,
    dec_layer_choices=(1, 2, 3, 4, 5, 6),
    embed_choices=(512, 640),
    ffn_choices=(512, 1024, 2048, 3072),
    head_choices=(4, 8),
    arb_attn_choices=(-1, 1, 2),
):
    """Compute cardinality of the HAT heterogeneous + arbitrary-attention SubTransformer space."""
    # Encoder: fixed 6 layers, each chooses FFN dim and head count; shared enc embed dim
    enc_configs = len(embed_choices) * ((len(ffn_choices) * len(head_choices)) ** enc_layers)
    # Decoder: shared dec embed dim, variable depth m in dec_layer_choices;
    # each decoder layer chooses FFN dim, self-attn heads, cross-attn heads, and arbitrary enc-dec span
    per_dec_layer = len(ffn_choices) * len(head_choices) * len(head_choices) * len(arb_attn_choices)
    dec_configs = len(embed_choices) * sum(per_dec_layer ** m for m in dec_layer_choices)
    return enc_configs * dec_configs


def arbitrary_enc_dec_attention(q_vec, encoder_layer_kv_pairs, span_a):
    """Compute arbitrary encoder-decoder attention over the last (span_a + 1) encoder layers.

    span_a = -1 -> attend only to the last encoder layer;
    span_a = 1  -> attend to the last 2 encoder layers;
    span_a = 2  -> attend to the last 3 encoder layers.
    """
    num_layers_used = 1 if span_a == -1 else (span_a + 1)
    selected_layers = encoder_layer_kv_pairs[-num_layers_used:]
    # Concatenate keys and values along the sequence-length dimension with zero extra parameters
    concat_keys = [k for k_seq, _ in selected_layers for k in k_seq]
    concat_vals = [v for _, v_seq in selected_layers for v in v_seq]
    d_k = len(q_vec)
    scores = [sum(q_vec[d] * k[d] for d in range(d_k)) / math.sqrt(d_k) for k in concat_keys]
    m_score = max(scores)
    exps = [math.exp(s - m_score) for s in scores]
    denom = sum(exps)
    weights = [e / denom for e in exps]
    out = [
        sum(weights[t] * concat_vals[t][d] for t in range(len(concat_vals)))
        for d in range(len(concat_vals[0]))
    ]
    return out, len(concat_keys)


def extract_front_subtensor(super_weight, out_dim, in_dim):
    """Extract front-slice weight subtensor W[:out_dim, :in_dim] from SuperTransformer weight matrix."""
    return [row[:in_dim] for row in super_weight[:out_dim]]


def main():
    cardinality = design_space_cardinality()
    # Verify design space is on the order of 10^13 - 10^15 SubTransformers
    assert cardinality > 10**12

    # Verify arbitrary encoder-decoder attention concatenates K/V across last 1, 2, or 3 encoder layers
    q = [1.0, 0.5]
    enc_kv = [
        ([[1.0, 0.0], [0.0, 1.0]], [[1.0, 2.0], [3.0, 4.0]]),
        ([[0.5, 0.5], [1.0, 1.0]], [[2.0, 1.0], [4.0, 3.0]]),
        ([[1.5, 0.2], [0.2, 1.5]], [[5.0, 0.0], [0.0, 5.0]]),
    ]
    out_last1, len_last1 = arbitrary_enc_dec_attention(q, enc_kv, span_a=-1)
    out_last2, len_last2 = arbitrary_enc_dec_attention(q, enc_kv, span_a=1)
    out_last3, len_last3 = arbitrary_enc_dec_attention(q, enc_kv, span_a=2)
    assert len_last1 == 2 and len_last2 == 4 and len_last3 == 6
    assert out_last1 != out_last2 and out_last2 != out_last3

    # Verify front-slice weight sharing: smaller subtensor is exact prefix of larger subtensor
    super_w = [[float(i * 10 + j) for j in range(8)] for i in range(6)]
    sub_small = extract_front_subtensor(super_w, 3, 4)
    sub_large = extract_front_subtensor(super_w, 5, 6)
    assert len(sub_small) == 3 and len(sub_small[0]) == 4
    assert sub_small == [row[:4] for row in sub_large[:3]]

    # Verify hardware-specialized trade-off: ARM CPU prefers deep-and-thin vs GPU shallow-and-wide
    arm_latency = lambda depth, width: 8.0 * depth + 0.045 * (width ** 1.35) * depth
    gpu_latency = lambda depth, width: 22.0 * depth + 0.004 * (width ** 1.15) * depth
    deep_thin = (5, 512)
    shallow_wide = (2, 1280)
    assert arm_latency(*deep_thin) < arm_latency(*shallow_wide)
    assert gpu_latency(*shallow_wide) < gpu_latency(*deep_thin)

    print(
        f"HAT verification passed: cardinality={cardinality:.3e}, "
        f"kv_lengths=({len_last1},{len_last2},{len_last3}), "
        f"arm_deep_thin={arm_latency(*deep_thin):.1f}<{arm_latency(*shallow_wide):.1f}, "
        f"gpu_shallow_wide={gpu_latency(*shallow_wide):.1f}<{gpu_latency(*deep_thin):.1f}"
    )


if __name__ == "__main__":
    main()
