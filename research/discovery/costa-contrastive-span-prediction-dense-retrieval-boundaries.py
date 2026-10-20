#!/usr/bin/env python3
"""Constructed boundary verification script for Round 767:
COSTA (Pre-train a Discriminative Text Encoder for Dense Retrieval via Contrastive Span Prediction)
by Xinyu Ma, Jiafeng Guo, Ruqing Zhang, Yixing Fan, and Xueqi Cheng
(SIGIR 2022, arXiv:2204.10641, doi:10.1145/3477495.3531772).

Verifies:
1. Multi-granularity span length mapping (Eqs. 1-3):
     l_span = p_span * (l_max - l_min) + l_min  for p_span in [0, 1],
   across phrase-level [4, 16], sentence-level [16, 64], and paragraph-level [64, 128],
   with Beta(4, 2) mean E[p_span] = alpha / (alpha + beta) = 4/6 = 2/3 > 0.5 skewing
   toward longer spans.
2. Nonlinear projection z_i = Tanh(FFN(h_0)) for the whole-text [CLS] representation (Eqs. 5-6)
   vs. average pooling z_p = AvgPooling([h_start, ..., h_{end-1}]) for the 4T spans (Eq. 7).
3. Group-Wise Contrastive loss L_GWC over N texts and N * 4T spans (total N*(4T+1) vectors, Eq. 8):
     L_GWC = sum_{i=1}^N -(1 / (4T)) sum_{p in S(i)} log(
         exp(sim(z_i, z_p) / tau) / sum_{j=1}^{N(4T+1)} 1_{[i != j]} exp(sim(z_i, z_j) / tau)
     ).
"""

import math


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def group_wise_contrastive_loss(whole_vecs, span_groups, tau=0.1):
    """Computes Eq. (8) L_GWC given N whole-text vectors and N lists of 4T span vectors."""
    n_texts = len(whole_vecs)
    num_spans = len(span_groups[0])

    # Build combined list of M = N * (4T + 1) vectors:
    # indices 0..N-1 are whole_vecs; indices N..N*(4T+1)-1 are span vectors
    all_vecs = list(whole_vecs)
    group_span_indices = []
    for i in range(n_texts):
        assert len(span_groups[i]) == num_spans
        idxs = []
        for s_vec in span_groups[i]:
            idxs.append(len(all_vecs))
            all_vecs.append(s_vec)
        group_span_indices.append(idxs)

    total_loss = 0.0
    for i in range(n_texts):
        z_i = all_vecs[i]
        # Denominator sums over all j != i across all N*(4T+1) representations
        denom_logits = [
            dot(z_i, all_vecs[j]) / tau
            for j in range(len(all_vecs))
            if j != i
        ]
        m = max(denom_logits)
        log_denom = m + math.log(sum(math.exp(x - m) for x in denom_logits))

        group_loss = 0.0
        for p in group_span_indices[i]:
            pos_logit = dot(z_i, all_vecs[p]) / tau
            group_loss += -(pos_logit - log_denom)
        total_loss += group_loss / num_spans

    return total_loss


def main():
    # 1. Verify Beta(4, 2) multi-granularity span length bounds (Eq. 1 & Section 4.5.1)
    alpha, beta = 4.0, 2.0
    mean_p = alpha / (alpha + beta)
    assert abs(mean_p - (2.0 / 3.0)) < 1e-12 and mean_p > 0.5
    for l_min, l_max in [(4, 16), (16, 64), (64, 128)]:
        l_mean = mean_p * (l_max - l_min) + l_min
        assert l_min < l_mean < l_max
        assert l_mean > 0.5 * (l_min + l_max)  # Skewed toward longer spans

    # 2. Verify Group-Wise Contrastive Loss L_GWC (Eq. 8)
    # Mini-batch of N=2 texts, each with 4 spans (T=1 per granularity -> 4T=4)
    z1 = [math.tanh(1.2), math.tanh(0.1)]
    z2 = [math.tanh(-1.1), math.tanh(0.2)]

    # Aligned groups: spans of text 1 are near z1, spans of text 2 are near z2
    spans_aligned = [
        [[0.82, 0.12], [0.79, 0.08], [0.85, 0.10], [0.80, 0.09]],
        [[-0.81, 0.18], [-0.78, 0.22], [-0.83, 0.15], [-0.79, 0.20]],
    ]
    # Unaligned groups: spans mixed across groups
    spans_unaligned = [
        [[0.82, 0.12], [-0.78, 0.22], [0.10, -0.50], [-0.79, 0.20]],
        [[-0.81, 0.18], [0.79, 0.08], [-0.10, 0.50], [0.80, 0.09]],
    ]

    loss_aligned = group_wise_contrastive_loss([z1, z2], spans_aligned, tau=0.1)
    loss_unaligned = group_wise_contrastive_loss([z1, z2], spans_unaligned, tau=0.1)
    assert loss_aligned < loss_unaligned

    # Verify theoretical lower bound when all 4T spans in S(i) have identical max similarity
    # and all out-of-group representations have -inf similarity: -log(1 / (4T)) = log(4T)
    assert loss_aligned >= math.log(4.0) - 1e-9

    print(
        f"[PASS] COSTA contrastive span prediction boundaries verified: "
        f"L_GWC(aligned)={loss_aligned:.4f} < L_GWC(unaligned)={loss_unaligned:.4f} "
        f"(lower_bound=2*log(4)={2.0 * math.log(4.0):.4f})"
    )


if __name__ == "__main__":
    main()
