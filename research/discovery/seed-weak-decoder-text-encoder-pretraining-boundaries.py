#!/usr/bin/env python3
"""Constructed boundary verification script for Round 760:
SEED (Pre-training a Strong Text Encoder Using a Weak Decoder / SEED-Encoder)
by Shuqi Lu, Di He, Chenyan Xiong, Guolin Ke, Waleed Malik, Zhicheng Dou,
Paul Bennett, Tie-Yan Liu, and Arnold Overwijk (EMNLP 2021, arXiv:2102.09206).

Verifies:
1. Information bottleneck interface between deep encoder f_enc and weak decoder f_dec:
   the decoder receives the encoder's dense [CLS] representation h_enc^[CLS]
   and can only attend to at most k contiguous preceding tokens via restricted
   attention span mask M_span(i, j):
     M_span(i, j) = 0 if (i - k <= j <= i) or j == 0 ([CLS]), else -inf.
2. Autoregressive document recovery loss with restricted span k forces the gradient
   w.r.t. h_enc^[CLS] to carry global bag-of-words / long-range semantic information
   whenever target token x_i depends on context outside window [i-k, i-1].
"""

import math


def restricted_attention_mask(seq_len, span_k):
    """Returns an (seq_len x seq_len) boolean visibility matrix where position 0 is
    the encoder [CLS] representation and positions 1..seq_len-1 are decoder tokens.
    For decoder position i >= 1, visible positions j are:
      - j == 0 (the encoder [CLS] vector, always visible), or
      - max(1, i - span_k + 1) <= j <= i (at most span_k local tokens up to i).
    """
    mask = []
    for i in range(seq_len):
        row = []
        for j in range(seq_len):
            if i == 0:
                visible = (j == 0)
            else:
                visible = (j == 0) or (max(1, i - span_k + 1) <= j <= i)
            row.append(visible)
        mask.append(row)
    return mask


def main():
    seq_len = 8  # pos 0 = [CLS], pos 1..7 = tokens
    span_k = 3

    mask_weak = restricted_attention_mask(seq_len, span_k=span_k)
    mask_full = restricted_attention_mask(seq_len, span_k=seq_len)

    # 1. Verify [CLS] (j=0) is visible at every decoding step i
    for i in range(seq_len):
        assert mask_weak[i][0] is True

    # 2. Verify causal masking: future tokens j > i are never visible
    for i in range(seq_len):
        for j in range(i + 1, seq_len):
            assert mask_weak[i][j] is False

    # 3. Verify restricted attention span k=3: at position i=6, local tokens j=1, 2, 3
    # are masked out in the weak decoder (only j=0 ([CLS]) and j=4, 5, 6 are visible),
    # whereas in a full causal decoder j=1, 2, 3 are visible.
    assert mask_weak[6] == [True, False, False, False, True, True, True, False]
    assert mask_full[6] == [True, True, True, True, True, True, True, False]

    # 4. Verify bottleneck effect on predicting a long-range dependency at i=6 that depends on token j=1:
    # Let token 1 have feature value v_1 = 2.5, local tokens 4..6 have value 0.0,
    # and encoder [CLS] vector have scalar summary c_cls.
    # Logit for target token at i=6 is (sum of visible token values) + c_cls.
    v_tokens = [0.0, 2.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    c_cls = 0.2

    # Under full causal attention (span_k = seq_len), token 1 is directly visible:
    logit_full = c_cls + sum(v_tokens[j] for j in range(1, 7) if mask_full[6][j])
    prob_full = 1.0 / (1.0 + math.exp(-logit_full))
    grad_cls_full = -(1.0 - prob_full)  # d(-log sigmoid(logit))/d(c_cls)

    # Under restricted span (span_k = 3), token 1 is NOT visible to decoder self-attention,
    # so the decoder must rely on c_cls, producing a much stronger gradient signal on c_cls!
    logit_weak = c_cls + sum(v_tokens[j] for j in range(1, 7) if mask_weak[6][j])
    prob_weak = 1.0 / (1.0 + math.exp(-logit_weak))
    grad_cls_weak = -(1.0 - prob_weak)

    assert abs(grad_cls_weak) > 5.0 * abs(grad_cls_full)

    print(
        f"[PASS] SEED weak-decoder text encoder pre-training boundaries verified: "
        f"|grad_cls_weak|={abs(grad_cls_weak):.4f} > |grad_cls_full|={abs(grad_cls_full):.4f}"
    )


if __name__ == "__main__":
    main()
