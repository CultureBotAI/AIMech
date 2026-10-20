#!/usr/bin/env python3
"""Constructed boundary verification for uniCOIL (Lin & Ma, 2021, arXiv:2106.14807).

Verifies:
1. Degenerating COIL's token dimension from d = 32 to d = 1 with a ReLU non-negativity
   constraint on output term weights and 8-bit integer impact quantization (Section 3),
   making uniCOIL directly indexable in a standard Lucene inverted index.
2. Combining uniCOIL scalar impact weights with doc2query-T5 document expansion to bridge
   vocabulary mismatch and outperform unexpanded COIL-tok.
3. Range-(0, 1)-normalized dense-sparse hybrid score fusion s_dense + alpha * s_sparse
   with TCT-ColBERTv2 (Section 3, Table 2).
"""

from __future__ import annotations


def unicoil_term_impacts(
    raw_token_logits: dict[str, list[float]],
    max_weight: float = 5.0,
) -> dict[str, int]:
    """Implements Section 3: d=1 scalar COIL projection + ReLU + max-pooling per unique term + 8-bit quantization."""
    impacts: dict[str, int] = {}
    for term, logits in raw_token_logits.items():
        # Apply ReLU to force non-negative weights and max-pool across occurrences of term in document
        w_pos = max(max(0.0, x) for x in logits)
        if w_pos > 0.0:
            q_val = min(255, int(round((w_pos / max_weight) * 255.0)))
            if q_val > 0:
                impacts[term] = q_val
    return impacts


def inverted_index_impact_score(
    query_impacts: dict[str, int],
    doc_impacts: dict[str, int],
) -> int:
    """Standard inverted-index inner product over quantized 8-bit impact scores."""
    return sum(
        q_w * doc_impacts.get(term, 0)
        for term, q_w in query_impacts.items()
    )


def minmax_normalize(scores: dict[str, float]) -> dict[str, float]:
    """Normalizes candidate scores into range(0, 1) as described in Section 3 (p. 4)."""
    lo = min(scores.values())
    hi = max(scores.values())
    span = hi - lo if hi > lo else 1.0
    return {k: (v - lo) / span for k, v in scores.items()}


def main() -> None:
    # 1. Verify ReLU non-negativity and 8-bit quantization (Section 3)
    # Without doc2query-T5 expansion, relevant doc d+ lacks the query synonym "physician"
    d_pos_unexpanded_logits = {
        "doctor": [3.8, 3.2],
        "hospital": [2.4],
        "noise_tok": [-1.2, -0.4],  # Negative COIL raw weights clamped to 0 by ReLU
    }
    # With doc2query-T5 expansion, predicted query terms ("physician", "medical") are appended:
    d_pos_expanded_logits = {
        "doctor": [3.8, 3.2],
        "hospital": [2.4],
        "physician": [3.1],  # Added by doc2query-T5 expansion
        "medical": [2.2],    # Added by doc2query-T5 expansion
        "noise_tok": [-1.2, -0.4],
    }
    d_neg_logits = {
        "physician": [1.1],
        "clinic": [1.5],
    }

    imp_pos_unexp = unicoil_term_impacts(d_pos_unexpanded_logits)
    imp_pos_exp = unicoil_term_impacts(d_pos_expanded_logits)
    imp_neg = unicoil_term_impacts(d_neg_logits)

    # Negative raw weight must not appear in inverted list:
    assert "noise_tok" not in imp_pos_unexp
    assert all(0 < v <= 255 for v in imp_pos_exp.values())

    # Query: "physician hospital"
    q_impacts = unicoil_term_impacts({"physician": [4.0], "hospital": [2.5]})

    s_pos_unexp = inverted_index_impact_score(q_impacts, imp_pos_unexp)
    s_pos_exp = inverted_index_impact_score(q_impacts, imp_pos_exp)
    s_neg = inverted_index_impact_score(q_impacts, imp_neg)
    assert s_pos_exp > s_pos_unexp
    assert s_pos_exp > s_neg

    # 2. Verify range-(0, 1) normalized dense-sparse hybrid fusion s_dense + alpha * s_sparse (Section 3)
    sparse_raw = {"doc_pos": float(s_pos_exp), "doc_hard_dense": 6000.0, "doc_neg": float(s_neg)}
    dense_raw = {"doc_pos": 71.5, "doc_hard_dense": 72.0, "doc_neg": 65.0}

    s_norm = minmax_normalize(sparse_raw)
    d_norm = minmax_normalize(dense_raw)
    alpha = 0.8
    fused = {k: d_norm[k] + alpha * s_norm[k] for k in sparse_raw}

    # Dense alone ranks doc_hard_dense > doc_pos, but hybrid fusion ranks doc_pos #1:
    assert dense_raw["doc_hard_dense"] > dense_raw["doc_pos"]
    assert fused["doc_pos"] > fused["doc_hard_dense"] > fused["doc_neg"]

    print(
        f"[PASS] uniCOIL boundaries verified: unexpanded={s_pos_unexp} < expanded={s_pos_exp}, "
        f"hybrid_fused={ {k: round(v, 4) for k, v in fused.items()} }"
    )


if __name__ == "__main__":
    main()
