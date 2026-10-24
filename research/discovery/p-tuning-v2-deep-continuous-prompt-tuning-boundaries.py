#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 717: P-Tuning v2 (Liu et al., ACL 2022)."""

import math


def verify_p_tuning_v2() -> None:
    # Compare single-layer input prompt tuning (Lester et al., 2021) vs.
    # multi-layer deep continuous prompt tuning (P-Tuning v2, Liu et al., 2022)
    # across L transformer layers with hidden dimension d_model and prompt length l_p.
    n_layers = 24
    d_model = 1024
    l_p = 20
    seq_len = 64
    num_classes = 3

    # Single-layer prompt tuning tunes only l_p * d_model input prompt parameters:
    params_single_layer = l_p * d_model
    # P-Tuning v2 prepends independent trainable prefix key/value prompts (2 * l_p * d_model) at every layer
    # plus a linear classification head (d_model * num_classes) over token representations (no verbalizer):
    params_pt2 = n_layers * 2 * l_p * d_model + d_model * num_classes

    # Total BERT-large backbone parameters (~335M)
    backbone_params = 335_000_000
    ratio_single = params_single_layer / backbone_params
    ratio_pt2 = params_pt2 / backbone_params

    # P-Tuning v2 increases tunable capacity from ~0.006% to ~0.29% (within 0.1% - 3% range)
    assert ratio_single < 0.0001
    assert 0.001 <= ratio_pt2 <= 0.03
    assert params_pt2 > 20 * params_single_layer

    # Token-level sequence tagging compatibility:
    # Single-layer verbalizer over [MASK] predicts a single label token, whereas P-Tuning v2
    # projects each of the seq_len token hidden states h_i in R^{d_model} via W_cls in R^{num_classes x d_model}:
    hidden_states = [[math.sin(t + j * 0.01) for j in range(d_model)] for t in range(seq_len)]
    w_cls = [[math.cos(c + j * 0.01) * 0.05 for j in range(d_model)] for c in range(num_classes)]
    token_logits = [
        [sum(w_cls[c][j] * hidden_states[t][j] for j in range(d_model)) for c in range(num_classes)]
        for t in range(seq_len)
    ]
    assert len(token_logits) == seq_len
    assert all(len(logits_t) == num_classes for logits_t in token_logits)
    print("P-Tuning v2 verification passed.")


if __name__ == "__main__":
    verify_p_tuning_v2()
