#!/usr/bin/env python3
"""Constructed boundary verification for PARADE (Li et al., 2021, arXiv:2008.09093)."""

import math


def vec_max_pool(passages: list[list[float]]) -> list[float]:
    """Eq. (2): PARADE-Max element-wise max pooling over passage [CLS] representations."""
    d = len(passages[0])
    return [max(p[j] for p in passages) for j in range(d)]


def vec_avg_pool(passages: list[list[float]]) -> list[float]:
    """PARADE-Avg element-wise mean pooling over passage [CLS] representations."""
    n = len(passages)
    d = len(passages[0])
    return [sum(p[j] for p in passages) / n for j in range(d)]


def vec_attn_pool(passages: list[list[float]], w_attn: list[float]) -> tuple[list[float], list[float]]:
    """Eqs. (3)-(4): PARADE-Attn softmax-weighted passage representation aggregation."""
    logits = [sum(w_attn[j] * p[j] for j in range(len(w_attn))) for p in passages]
    m = max(logits)
    exps = [math.exp(x - m) for x in logits]
    z = sum(exps)
    weights = [e / z for e in exps]
    d = len(passages[0])
    d_cls = [sum(weights[i] * passages[i][j] for i in range(len(passages))) for j in range(d)]
    return d_cls, weights


def parade_transformer_cls(emb_cls: list[float], passages: list[list[float]]) -> list[float]:
    """Eqs. (5)-(6): Hierarchical PARADE-Transformer block over x^0 = (emb^cls, p_1^cls, ..., p_n^cls)."""
    seq = [emb_cls, *passages]
    d = len(emb_cls)
    scale = math.sqrt(d)
    # Self-attention from emb_cls (index 0) over all sequence tokens:
    attn_logits = [sum(emb_cls[j] * tok[j] for j in range(d)) / scale for tok in seq]
    m = max(attn_logits)
    exps = [math.exp(x - m) for x in attn_logits]
    z = sum(exps)
    alpha = [e / z for e in exps]
    attn_out = [sum(alpha[i] * seq[i][j] for i in range(len(seq))) for j in range(d)]
    h = [emb_cls[j] + attn_out[j] for j in range(d)]
    # Two-layer FFN with ReLU activation (Eq. 6): detects conjunctive presence of aspect 0 and aspect 1
    relu_conj = max(0.0, h[0] + h[1] - 1.5)
    ffn_out = [relu_conj, relu_conj, 0.0]
    return [h[j] + ffn_out[j] for j in range(d)]


def score_maxp(passages: list[list[float]], w_d: list[float]) -> float:
    """Baseline BERT-MaxP score aggregation: max_i (w_d^T p_i^cls)."""
    return max(sum(w_d[j] * p[j] for j in range(len(w_d))) for p in passages)


def score_parade(d_cls: list[float], w_d: list[float]) -> float:
    """Eq. (7): rel(q, D) = W_d d^cls."""
    return sum(w_d[j] * d_cls[j] for j in range(len(w_d)))


def distillation_loss(z_teacher: float, z_student: float, y_true: float, alpha: float) -> float:
    """Eq. (8): L = alpha * L_CE + (1 - alpha) * ||z^t - z^s||^2."""
    prob_s = 1.0 / (1.0 + math.exp(-z_student))
    l_ce = -(y_true * math.log(prob_s + 1e-12) + (1.0 - y_true) * math.log(1.0 - prob_s + 1e-12))
    l_mse = (z_teacher - z_student) ** 2
    return alpha * l_ce + (1.0 - alpha) * l_mse


def main() -> None:
    # Document A has complementary relevance signals across two passages (broad information need):
    # Passage 1 covers aspect 1, Passage 2 covers aspect 2.
    doc_broad = [
        [2.0, 0.1, 0.0],
        [0.1, 2.2, 0.0],
        [-0.5, -0.4, 0.1],
        [-0.3, -0.2, 0.0],
    ]
    # Document B only matches aspect 1 slightly stronger in one passage, but misses aspect 2 completely.
    doc_single = [
        [2.4, 0.0, 0.0],
        [-0.4, -0.3, 0.0],
        [-0.5, -0.5, 0.0],
        [-0.2, -0.4, 0.0],
    ]
    w_d = [1.0, 1.0, 0.2]
    w_attn = [1.2, 1.2, 0.0]
    emb_cls = [1.0, 1.0, 0.0]

    # 1. Score-MaxP fails to combine complementary passage aspects, ranking doc_single > doc_broad:
    s_maxp_broad = score_maxp(doc_broad, w_d)
    s_maxp_single = score_maxp(doc_single, w_d)
    assert s_maxp_single > s_maxp_broad, "Score-MaxP only sees the single highest-scoring passage"

    # 2. PARADE-Max aggregates passage representations before linear scoring, capturing both aspects:
    d_max_broad = vec_max_pool(doc_broad)
    d_max_single = vec_max_pool(doc_single)
    s_parade_max_broad = score_parade(d_max_broad, w_d)
    s_parade_max_single = score_parade(d_max_single, w_d)
    assert s_parade_max_broad > s_parade_max_single, "PARADE-Max combines aspect features across passages"

    # 3. PARADE-Attn assigns normalized softmax weights summing to 1 and focuses on relevant passages:
    _, weights_broad = vec_attn_pool(doc_broad, w_attn)
    _, weights_single = vec_attn_pool(doc_single, w_attn)
    assert abs(sum(weights_broad) - 1.0) < 1e-9
    assert abs(sum(weights_single) - 1.0) < 1e-9
    assert weights_broad[0] + weights_broad[1] > 0.90

    # 4. PARADE-Transformer hierarchical self-attention + ReLU FFN ranks doc_broad > doc_single:
    d_tf_broad = parade_transformer_cls(emb_cls, doc_broad)
    d_tf_single = parade_transformer_cls(emb_cls, doc_single)
    s_tf_broad = score_parade(d_tf_broad, w_d)
    s_tf_single = score_parade(d_tf_single, w_d)
    assert s_tf_broad > s_tf_single

    # 5. Knowledge distillation Eq. (8) vanishes MSE term when student logit matches teacher logit:
    l_match = distillation_loss(3.0, 3.0, 1.0, alpha=0.5)
    l_mismatch = distillation_loss(3.0, 0.5, 1.0, alpha=0.5)
    assert l_mismatch > l_match > 0.0

    print("PARADE boundary verification passed:")
    print(f"  Score-MaxP:          broad={s_maxp_broad:.4f} < single={s_maxp_single:.4f}")
    print(f"  PARADE-Max:          broad={s_parade_max_broad:.4f} > single={s_parade_max_single:.4f}")
    print(f"  PARADE-Transformer:  broad={s_tf_broad:.4f} > single={s_tf_single:.4f}")
    print(f"  Distill loss:        match={l_match:.4f} < mismatch={l_mismatch:.4f}")


if __name__ == "__main__":
    main()
