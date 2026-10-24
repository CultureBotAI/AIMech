#!/usr/bin/env python3
"""Constructed boundary verification for DeepImpact (Mallia et al., SIGIR 2021, arXiv:2104.12016).

Verifies:
1. First-occurrence unique-term extraction over [orig_doc ; [SEP] ; DocT5Query_expansion]
   and 2-layer ReLU MLP impact score encoding (Section 2, Figure 1).
2. Sum-of-impacts scoring over intersecting query-document terms score(q, d) = sum_{t in q cap d} s_{t,d}
   and pairwise softmax cross-entropy loss over (q, d+, d-) triples (Section 2).
3. Linear quantization of real-valued impact scores into b-bit integers in [1, 2^b - 1] (b = 8 -> [1, 255]).
"""

from __future__ import annotations

import math


def relu(x: float) -> float:
    return max(0.0, x)


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def first_occurrence_positions(tokens: list[str], sep_token: str = "[SEP]") -> dict[str, int]:
    """Returns the index of the first occurrence of each unique non-SEP term in the expanded sequence."""
    first_pos: dict[str, int] = {}
    for idx, tok in enumerate(tokens):
        if tok == sep_token:
            continue
        if tok not in first_pos:
            first_pos[tok] = idx
    return first_pos


def two_layer_relu_mlp(
    h_vec: list[float],
    w1: list[list[float]],
    b1: list[float],
    w2: list[float],
    b2: float,
) -> float:
    """Two-layer MLP with ReLU activations producing a single non-negative scalar impact score."""
    hidden = [relu(dot(w1_row, h_vec) + b1_i) for w1_row, b1_i in zip(w1, b1)]
    return relu(dot(w2, hidden) + b2)


def compute_document_impacts(
    tokens: list[str],
    token_embs: list[list[float]],
    w1: list[list[float]],
    b1: list[float],
    w2: list[float],
    b2: float,
) -> dict[str, float]:
    """Computes DeepImpact real-valued impact scores for each unique term via its first occurrence."""
    first_pos = first_occurrence_positions(tokens)
    impacts: dict[str, float] = {}
    for term, pos in first_pos.items():
        score = two_layer_relu_mlp(token_embs[pos], w1, b1, w2, b2)
        if score > 0.0:
            impacts[term] = round(score, 3)  # 3 digits of precision (Section 2)
    return impacts


def quantize_impacts_linear(
    doc_impacts: dict[str, float],
    max_impact: float,
    bits: int = 8,
) -> dict[str, int]:
    """Implements Section 2 linear quantization into [1, 2^b - 1] (for b = 8, [1, 255])."""
    upper = (1 << bits) - 1
    quantized: dict[str, int] = {}
    for term, val in doc_impacts.items():
        if val <= 0.0:
            continue
        scaled = int(round(1.0 + (val / max_impact) * (upper - 1.0)))
        q_val = max(1, min(upper, scaled))
        quantized[term] = q_val
    return quantized


def sum_of_impacts_score(query_terms: set[str], doc_impacts: dict[str, float | int]) -> float:
    """Implements score(q, d) = sum_{t in q cap d} impact(t, d)."""
    return float(sum(doc_impacts[t] for t in (query_terms & doc_impacts.keys())))


def pairwise_softmax_ce_loss(score_pos: float, score_neg: float) -> float:
    """Pairwise softmax cross-entropy loss over (q, d+, d-) triple (Section 2)."""
    m = max(score_pos, score_neg)
    p_pos = math.exp(score_pos - m) / (math.exp(score_pos - m) + math.exp(score_neg - m))
    return -math.log(p_pos)


def main() -> None:
    # Expanded document sequence: [t1, t2, t3, [SEP], t1, t3, t4, t5] (Figure 1)
    doc_pos_tokens = ["cinnamon", "reduces", "glucose", "[SEP]", "cinnamon", "glucose", "blood", "sugar"]
    doc_pos_embs = [
        [0.9, 0.8, 0.4],   # 0: cinnamon (1st occurrence - used!)
        [0.4, 0.5, 0.2],   # 1: reduces (1st occurrence - used!)
        [0.8, 0.7, 0.5],   # 2: glucose (1st occurrence - used!)
        [0.0, 0.0, 0.0],   # 3: [SEP]
        [0.1, 0.1, 0.1],   # 4: cinnamon (2nd occurrence - ignored!)
        [0.1, 0.1, 0.1],   # 5: glucose (2nd occurrence - ignored!)
        [0.85, 0.6, 0.4],  # 6: blood (injected expansion term, 1st occurrence - used!)
        [0.9, 0.75, 0.5],  # 7: sugar (injected expansion term, 1st occurrence - used!)
    ]
    doc_neg_tokens = ["baking", "pie", "recipe", "[SEP]", "cinnamon", "apple"]
    doc_neg_embs = [
        [0.2, 0.1, 0.1],
        [0.1, 0.2, 0.1],
        [0.2, 0.2, 0.1],
        [0.0, 0.0, 0.0],
        [0.35, 0.2, 0.1],  # cinnamon in baking context has lower contextual impact
        [0.2, 0.1, 0.2],
    ]

    w1 = [[1.0, 0.8, 0.5], [0.5, 1.0, 0.6]]
    b1 = [-0.2, -0.1]
    w2 = [1.2, 1.1]
    b2 = -0.3

    first_pos = first_occurrence_positions(doc_pos_tokens)
    assert first_pos == {"cinnamon": 0, "reduces": 1, "glucose": 2, "blood": 6, "sugar": 7}

    imp_pos = compute_document_impacts(doc_pos_tokens, doc_pos_embs, w1, b1, w2, b2)
    imp_neg = compute_document_impacts(doc_neg_tokens, doc_neg_embs, w1, b1, w2, b2)

    # Query: "does cinnamon lower blood sugar" -> terms {"cinnamon", "blood", "sugar"}
    query_terms = {"cinnamon", "blood", "sugar"}
    s_pos = sum_of_impacts_score(query_terms, imp_pos)
    s_neg = sum_of_impacts_score(query_terms, imp_neg)
    assert s_pos > s_neg

    # Verify Inject contribution: without injected terms {"blood", "sugar"}, score is lower
    imp_pos_no_inject = {k: v for k, v in imp_pos.items() if k in {"cinnamon", "reduces", "glucose"}}
    s_pos_no_inject = sum_of_impacts_score(query_terms, imp_pos_no_inject)
    assert s_pos > s_pos_no_inject

    # Verify 8-bit quantization in [1, 255] preserves ranking order:
    max_imp = max(max(imp_pos.values()), max(imp_neg.values()))
    q_imp_pos = quantize_impacts_linear(imp_pos, max_impact=max_imp, bits=8)
    q_imp_neg = quantize_impacts_linear(imp_neg, max_impact=max_imp, bits=8)
    assert all(1 <= v <= 255 for v in q_imp_pos.values())
    assert all(1 <= v <= 255 for v in q_imp_neg.values())

    q_s_pos = sum_of_impacts_score(query_terms, q_imp_pos)
    q_s_neg = sum_of_impacts_score(query_terms, q_imp_neg)
    assert q_s_pos > q_s_neg

    loss = pairwise_softmax_ce_loss(s_pos, s_neg)
    assert loss < 0.05

    print(
        f"[PASS] DeepImpact boundaries verified: s_pos={s_pos:.3f} (quantized={int(q_s_pos)}) > "
        f"s_neg={s_neg:.3f} (quantized={int(q_s_neg)}), loss={loss:.4f}"
    )


if __name__ == "__main__":
    main()
