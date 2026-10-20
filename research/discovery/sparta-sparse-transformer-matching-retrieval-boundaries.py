#!/usr/bin/env python3
"""Constructed boundary verification for SPARTA (Zhao et al., NAACL 2021, arXiv:2009.13013).

Verifies:
1. Token-level max-pooling term matching y_i = max_{j in [1, |c|]} (e_i^T s_j) (Eq. 4),
   sparse feature activation phi(y_i) = ReLU(y_i + b) (Eq. 5), and log-regularized
   summation f(q, (a, c)) = sum_{i=1}^{|q|} log(phi(y_i) + 1) (Eq. 6).
2. Exact algebraic equivalence between online neural scoring (Eqs. 4-6) and offline
   vocabulary-wide Inverted Index O(1) lookup + summation (Eqs. 8-9).
3. Cross-entropy learning-to-rank objective J = f(q, (a+, c+)) - log sum_{k in K-} exp(f(q, (a_k, c_k))) (Eq. 7).
"""

from __future__ import annotations

import math


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def sparta_term_score(
    e_term: list[float],
    answer_context_embs: list[list[float]],
    bias: float,
) -> float:
    """Implements Eqs. (4)-(6) & (8) for a single query/vocabulary term t."""
    y_i = max(dot(e_term, s_j) for s_j in answer_context_embs)
    phi_y = max(0.0, y_i + bias)
    return math.log(phi_y + 1.0)


def sparta_online_score(
    query_terms: list[str],
    vocab_embs: dict[str, list[float]],
    answer_context_embs: list[list[float]],
    bias: float,
) -> float:
    """Implements Eqs. (4)-(6) online for query q = [t_1, ..., t_|q|]."""
    return sum(
        sparta_term_score(vocab_embs[t], answer_context_embs, bias)
        for t in query_terms
    )


def build_sparta_inverted_index(
    vocab_embs: dict[str, list[float]],
    candidates: dict[str, list[list[float]]],
    bias: float,
) -> dict[str, dict[str, float]]:
    """Implements Eq. (8): precomputes non-zero LOOKUP(t, (a, c)) across vocabulary V."""
    inverted_index: dict[str, dict[str, float]] = {t: {} for t in vocab_embs}
    for cand_id, s_embs in candidates.items():
        for t, e_t in vocab_embs.items():
            score = sparta_term_score(e_t, s_embs, bias)
            if score > 0.0:
                inverted_index[t][cand_id] = score
    return inverted_index


def sparta_index_lookup_score(
    query_terms: list[str],
    inverted_index: dict[str, dict[str, float]],
    cand_id: str,
) -> float:
    """Implements Eq. (9): O(1) lookup + summation over query terms."""
    return sum(inverted_index.get(t, {}).get(cand_id, 0.0) for t in query_terms)


def sparta_ltr_objective(
    pos_score: float,
    neg_scores: list[float],
) -> float:
    """Implements Eq. (7): J = f(q, (a+, c+)) - log sum_{k in K-} exp(f(q, (a_k, c_k)))."""
    m = max(neg_scores)
    log_sum_exp_neg = m + math.log(sum(math.exp(s - m) for s in neg_scores))
    return pos_score - log_sum_exp_neg


def main() -> None:
    # Vocabulary embeddings E(V) (non-contextualized query word embeddings, Eq. 2):
    vocab_embs = {
        "who": [0.90, 0.20, 0.10],
        "founded": [0.20, 0.90, 0.20],
        "microsoft": [0.10, 0.25, 0.95],
        "irrelevant": [-0.80, -0.70, -0.60],
        "utah": [0.40, -0.50, 0.10],
    }
    bias = -0.35

    # Candidate answers H(a, c) (contextualized BERT token embeddings, Eq. 3):
    # Answer 0 (a+, c+): "Bill Gates founded Microsoft" (matches "who" semantically even without literal word "who")
    # Answer 1 (nearby sentence hard negative): mentions Microsoft product but not founder
    # Answer 2 (random negative): unrelated sentence
    candidates = {
        "ans_pos": [
            [0.88, 0.25, 0.15],  # "Bill Gates" contextualized token (aligns with "who")
            [0.22, 0.92, 0.25],  # "founded"
            [0.15, 0.28, 0.96],  # "Microsoft"
        ],
        "ans_nearby_neg": [
            [0.10, 0.20, 0.85],  # "Windows"
            [0.12, 0.25, 0.90],  # "Microsoft"
            [-0.20, 0.10, 0.20], # "operating system"
        ],
        "ans_rand_neg": [
            [-0.40, 0.10, -0.20],
            [0.05, -0.30, 0.10],
        ],
    }

    inverted_index = build_sparta_inverted_index(vocab_embs, candidates, bias)

    # Verify sparsity control (ReLU(y_i + b) == 0 for "irrelevant" and "utah" on ans_pos):
    assert "ans_pos" not in inverted_index["irrelevant"]
    assert "ans_pos" not in inverted_index["utah"]
    # Verify latent conversational term "who" is indexed for ans_pos with non-zero weight:
    assert inverted_index["who"]["ans_pos"] > 0.0

    # Verify exact equivalence between online neural scoring (Eq. 6) and inverted-index lookup (Eq. 9):
    query = ["who", "founded", "microsoft", "irrelevant"]
    for cand_id, s_embs in candidates.items():
        s_online = sparta_online_score(query, vocab_embs, s_embs, bias)
        s_lookup = sparta_index_lookup_score(query, inverted_index, cand_id)
        assert abs(s_online - s_lookup) < 1e-12

    s_pos = sparta_index_lookup_score(query, inverted_index, "ans_pos")
    s_nearby = sparta_index_lookup_score(query, inverted_index, "ans_nearby_neg")
    s_rand = sparta_index_lookup_score(query, inverted_index, "ans_rand_neg")
    assert s_pos > s_nearby > s_rand

    j_obj = sparta_ltr_objective(s_pos, [s_nearby, s_rand])
    assert j_obj > 0.0

    print(
        f"[PASS] SPARTA boundaries verified: s_pos={s_pos:.4f} > s_nearby={s_nearby:.4f} > "
        f"s_rand={s_rand:.4f}, J_ltr={j_obj:.4f}"
    )


if __name__ == "__main__":
    main()
