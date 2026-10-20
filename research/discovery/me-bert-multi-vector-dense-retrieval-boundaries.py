#!/usr/bin/env python3
"""Constructed boundary verification for ME-BERT (Luan et al., TACL 2021, arXiv:2005.00181).

Verifies:
1. Normalized margin Definition 2.1: mu(q, d1, d2) = <q, d1 - d2> / (||q|| * ||d1 - d2||)
   and Lemma 1 dimension bound k >= 2 * (eps^2 / 2 - eps^3 / 3)^(-1) * ln(4 / beta).
2. Theorem 1 (Orthogonal Multi-Vector Margin Increase): decomposing long documents d1, d2
   into m orthogonal segments d1 = sum_{i=1}^m d1^(i), d2 = sum_{i=1}^m d2^(i) where query q
   aligns with segment i strictly increases the normalized margin mu(q, d1^(i), d2^(i)) > mu(q, d1, d2)
   and lowers the required encoding dimension k*.
3. Single-query MIPS decomposition (Section 3): argmax_{y in D} max_{j=1..m} <f^(1)(x), f_j^(m)(y)>
   is recovered exactly by finding the single vector entry (y*, j*) maximizing inner product in a
   flat m * |D| MIPS index.
"""

from __future__ import annotations

import math


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def norm(a: list[float]) -> float:
    return math.sqrt(dot(a, a))


def normalized_margin(q: list[float], d1: list[float], d2: list[float]) -> float:
    """Implements Definition 2.1: mu(q, d1, d2) = <q, d1 - d2> / (||q|| * ||d1 - d2||)."""
    diff = [x - y for x, y in zip(d1, d2)]
    return dot(q, diff) / (norm(q) * norm(diff))


def lemma1_min_dimension(eps: float, beta: float = 0.05) -> float:
    """Implements Eq. (2): k >= 2 * (eps^2 / 2 - eps^3 / 3)^(-1) * ln(4 / beta)."""
    assert 0.0 < eps <= 1.0
    return 2.0 * ((eps ** 2) / 2.0 - (eps ** 3) / 3.0) ** (-1.0) * math.log(4.0 / beta)


def me_bert_score(q_vec: list[float], doc_multi_vecs: list[list[float]]) -> float:
    """Implements Section 3: psi^(m)(x, y) = max_{j=1..m} <f^(1)(x), f_j^(m)(y)>."""
    return max(dot(q_vec, f_j) for f_j in doc_multi_vecs)


def main() -> None:
    # 1. Verify Theorem 1 and Lemma 1 (Sections 2-3, Appendix A.5):
    # Vocabulary of size v = 6 partitioned into m = 2 orthogonal segments (dims 0..2 and dims 3..5):
    q = [1.0, 1.0, 0.0, 0.0, 0.0, 0.0]  # Query refers to segment 1 (dims 0..2)
    # Segment 1 of d1 and d2:
    d1_seg1 = [3.0, 2.0, 0.0, 0.0, 0.0, 0.0]
    d2_seg1 = [2.0, 1.0, 0.0, 0.0, 0.0, 0.0]
    # Segment 2 of d1 and d2 (orthogonal to segment 1 and to query q; represents long-document background):
    d1_seg2 = [0.0, 0.0, 0.0, 4.0, 1.0, 5.0]
    d2_seg2 = [0.0, 0.0, 0.0, 1.0, 5.0, 1.0]

    # Check orthogonality between segment 1 and segment 2:
    assert dot(d1_seg1, d1_seg2) == 0.0
    assert dot(d2_seg1, d2_seg2) == 0.0
    assert dot([a - b for a, b in zip(d1_seg1, d2_seg1)], [a - b for a, b in zip(d1_seg2, d2_seg2)]) == 0.0

    # Full single-vector document representations d1 = d1_seg1 + d1_seg2, d2 = d2_seg1 + d2_seg2:
    d1_full = [a + b for a, b in zip(d1_seg1, d1_seg2)]
    d2_full = [a + b for a, b in zip(d2_seg1, d2_seg2)]

    mu_single = normalized_margin(q, d1_full, d2_full)
    mu_multi = normalized_margin(q, d1_seg1, d2_seg1)
    # Theorem 1: mu(q, d1^(1), d2^(1)) >= mu(q, d1, d2) (strictly greater when ||d1^(-1) - d2^(-1)|| > 0):
    assert mu_multi > mu_single > 0.0

    # Lemma 1: required random projection dimension k* is strictly smaller for multi-vector segment:
    k_single = lemma1_min_dimension(mu_single, beta=0.05)
    k_multi = lemma1_min_dimension(mu_multi, beta=0.05)
    assert k_multi < k_single

    # 2. Verify ME-BERT single-query MIPS index search equivalence (Section 3):
    q_cls = [0.8, 0.6, -0.2]
    corpus_multi_vecs = {
        "doc_0": [[0.2, 0.1, 0.5], [0.9, 0.7, -0.1], [-0.3, 0.2, 0.4]],  # m = 3 vectors
        "doc_1": [[0.5, 0.4, 0.1], [0.3, 0.2, -0.4], [0.1, -0.2, 0.3]],
    }
    # Build flat MIPS index of m * |D| entries:
    flat_mips_index: list[tuple[str, int, list[float]]] = [
        (doc_id, j, vec)
        for doc_id, vecs in corpus_multi_vecs.items()
        for j, vec in enumerate(vecs)
    ]
    best_entry = max(flat_mips_index, key=lambda item: dot(q_cls, item[2]))
    best_doc_by_mips = best_entry[0]
    best_score_by_mips = dot(q_cls, best_entry[2])

    # Compare against per-document ME-BERT max-over-m scoring:
    doc_scores = {doc_id: me_bert_score(q_cls, vecs) for doc_id, vecs in corpus_multi_vecs.items()}
    best_doc_by_def = max(doc_scores, key=lambda d: doc_scores[d])
    assert best_doc_by_mips == best_doc_by_def == "doc_0"
    assert abs(best_score_by_mips - doc_scores["doc_0"]) < 1e-12

    print(
        f"[PASS] ME-BERT boundaries verified: mu_multi={mu_multi:.4f} > mu_single={mu_single:.4f}, "
        f"k_multi={k_multi:.1f} < k_single={k_single:.1f}, best_doc={best_doc_by_mips!r} ({best_score_by_mips:.4f})"
    )


if __name__ == "__main__":
    main()
