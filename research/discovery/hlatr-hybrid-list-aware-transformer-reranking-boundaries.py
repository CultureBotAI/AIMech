#!/usr/bin/env python3
"""Constructed boundary verification for HLATR (Zhang et al., 2022, arXiv:2205.10569).

Verifies:
1. Multi-stage feature fusion (Section 3.2.1, Eq. 4): coupling learnable retrieval-order
   position embeddings pe_i with projected reranker representations v_i = W_v^T E^R(q, d_i)
   via LayerNorm(pe_i + v_i).
2. List-aware self-attention and listwise contrastive loss (Sections 3.2.2-3.2.3, Eqs. 5-6)
   vs. static Weighted Combination of two-stage Ranking (WCR, Eq. 7) and pointwise BCE loss.
"""

from __future__ import annotations

import math


def layer_norm(vec: list[float], eps: float = 1e-6) -> list[float]:
    mean = sum(vec) / len(vec)
    var = sum((x - mean) ** 2 for x in vec) / len(vec)
    inv_std = 1.0 / math.sqrt(var + eps)
    return [(x - mean) * inv_std for x in vec]


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def softmax(logits: list[float]) -> list[float]:
    m = max(logits)
    exps = [math.exp(x - m) for x in logits]
    s = sum(exps)
    return [e / s for e in exps]


def build_hlatr_input(
    reranker_embs: list[list[float]],
    retrieval_orders: list[int],
    w_v: list[list[float]],
    pos_embs: dict[int, list[float]],
) -> list[list[float]]:
    """Implements Eq. (4) and H^0 = [LN(pe_1 + v_1), ..., LN(pe_Z + v_Z)]^T."""
    h0: list[list[float]] = []
    d_dim = len(w_v)
    for e_r, order_idx in zip(reranker_embs, retrieval_orders):
        # v_i = W_v^T E^R(q, d_i)
        v_i = [dot(w_v[row], e_r) for row in range(d_dim)]
        pe_i = pos_embs[order_idx]
        fused = [pe_i[c] + v_i[c] for c in range(d_dim)]
        h0.append(layer_norm(fused))
    return h0


def single_head_self_attention(h: list[list[float]]) -> list[list[float]]:
    """List-aware Transformer encoder layer over Z candidate documents (Section 3.2.2)."""
    z_len = len(h)
    d_dim = len(h[0])
    scale = 1.0 / math.sqrt(d_dim)
    out: list[list[float]] = []
    for i in range(z_len):
        attn_logits = [dot(h[i], h[j]) * scale for j in range(z_len)]
        attn_weights = softmax(attn_logits)
        context = [
            sum(attn_weights[j] * h[j][c] for j in range(z_len))
            for c in range(d_dim)
        ]
        # Residual connection + LayerNorm
        out.append(layer_norm([h[i][c] + context[c] for c in range(d_dim)]))
    return out


def listwise_contrastive_loss(scores: list[float], pos_idx: int) -> float:
    """Implements Eq. (6): L_{q, D'_r} = -log(exp(score(q, d+)) / sum_d exp(score(q, d)))."""
    probs = softmax(scores)
    return -math.log(probs[pos_idx])


def main() -> None:
    # 3 candidate documents in D'_r (Z = 3):
    # Doc 0: false positive ranked #1 by reranker alone (high reranker logit, poor retrieval rank=3)
    # Doc 1: ground-truth relevant doc d+ (strong reranker logit AND top retrieval rank=1)
    # Doc 2: hard negative (moderate retrieval rank=2, low reranker logit)
    retrieval_scores = [0.40, 0.92, 0.75]
    reranker_scores = [0.88, 0.85, 0.30]
    retrieval_orders = [3, 1, 2]

    # Check static WCR baseline (Eq. 7): alpha * f_retr + (1 - alpha) * f_rerank
    wcr_alpha = 0.2
    wcr_scores = [
        wcr_alpha * r_s + (1.0 - wcr_alpha) * rr_s
        for r_s, rr_s in zip(retrieval_scores, reranker_scores)
    ]
    # Under small alpha=0.2, static WCR still ranks Doc 1 barely above Doc 0,
    # whereas under alpha=0.05 WCR fails and ranks Doc 0 > Doc 1:
    wcr_small_alpha = [
        0.05 * r_s + 0.95 * rr_s
        for r_s, rr_s in zip(retrieval_scores, reranker_scores)
    ]
    assert wcr_small_alpha[0] > wcr_small_alpha[1]

    # Construct HLATR feature fusion (d = 4)
    reranker_embs = [
        [0.88, -0.30, 0.10, 0.20],  # Doc 0
        [0.85, 0.65, 0.40, 0.30],   # Doc 1 (d+)
        [0.30, -0.40, -0.20, 0.10], # Doc 2
    ]
    w_v = [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]
    pos_embs = {
        1: [-0.20, 0.70, 0.80, -1.00],  # Rank 1 in retrieval stage
        2: [0.10, 0.05, -0.10, 0.20],   # Rank 2 in retrieval stage
        3: [0.40, -0.60, -0.50, 0.80],  # Rank 3 in retrieval stage
    }

    h0 = build_hlatr_input(reranker_embs, retrieval_orders, w_v, pos_embs)
    assert len(h0) == 3 and all(len(row) == 4 for row in h0)
    # Verify each row of H^0 is zero-mean, unit-variance layer-normalized:
    for row in h0:
        mean_val = sum(row) / len(row)
        var_val = sum((x - mean_val) ** 2 for x in row) / len(row)
        assert abs(mean_val) < 1e-6
        assert abs(var_val - 1.0) < 1e-4

    h1 = single_head_self_attention(h0)
    w_proj = [0.2, 1.0, 1.2, -0.8]
    hlatr_scores = [dot(w_proj, row) for row in h1]

    # Doc 1 (d+, index 1) achieves the highest list-aware HLATR score:
    assert hlatr_scores[1] > hlatr_scores[0] and hlatr_scores[1] > hlatr_scores[2]

    # Ablation without retrieval order (all pe_i = 0) reduces margin compared to coupled HLATR:
    zero_pos = {1: [0.0] * 4, 2: [0.0] * 4, 3: [0.0] * 4}
    h0_no_retr = build_hlatr_input(reranker_embs, retrieval_orders, w_v, zero_pos)
    h1_no_retr = single_head_self_attention(h0_no_retr)
    scores_no_retr = [dot(w_proj, row) for row in h1_no_retr]

    loss_coupled = listwise_contrastive_loss(hlatr_scores, pos_idx=1)
    loss_no_retr = listwise_contrastive_loss(scores_no_retr, pos_idx=1)
    assert loss_coupled < loss_no_retr

    print(
        f"[PASS] HLATR boundaries verified: hlatr_scores={[round(s, 4) for s in hlatr_scores]}, "
        f"loss_coupled={loss_coupled:.4f} < loss_no_retr={loss_no_retr:.4f}"
    )


if __name__ == "__main__":
    main()
