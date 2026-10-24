#!/usr/bin/env python3
"""Constructed boundary verification for SLEDGE (MacAvaney, Cohan, & Goharian, EMNLP 2020, arXiv:2005.02365)."""

import math


def bm25_score(
    query_terms: list[str],
    doc_tf: dict[str, int],
    doc_len: int,
    avg_dl: float,
    idf_map: dict[str, float],
    k1: float,
    b: float,
) -> float:
    """Section 3.1 & 5.1: Tuned BM25 (k1=3.9, b=0.55) vs default BM25 (k1=0.9, b=0.4)."""
    score = 0.0
    for term in query_terms:
        tf = doc_tf.get(term, 0)
        if tf <= 0:
            continue
        idf = idf_map.get(term, 0.0)
        denom = tf + k1 * (1.0 - b + b * (doc_len / avg_dl))
        score += idf * (tf * (k1 + 1.0)) / denom
    return score


def pairwise_cross_entropy_loss(r_pos: float, r_neg: float, eps: float = 1e-12) -> float:
    """Eq. (1): L(q, d^+, d^-) = -log(R(q, d^+)) - log(1 - R(q, d^-))."""
    rp = min(max(r_pos, eps), 1.0 - eps)
    rn = min(max(r_neg, eps), 1.0 - eps)
    return -math.log(rp) - math.log(1.0 - rn)


def filter_med_msmarco_queries(
    queries: list[tuple[int, str]],
    medsyn_lexicon: set[str],
    excluded_common_terms: set[str],
) -> list[int]:
    """Section 5.2: Filter MS-MARCO queries using MedSyn lexicon minus excluded common terms."""
    active_lexicon = medsyn_lexicon - excluded_common_terms
    kept_ids: list[int] = []
    for qid, text in queries:
        tokens = {tok.lower().strip("?,.") for tok in text.split()}
        if tokens & active_lexicon:
            kept_ids.append(qid)
    return kept_ids


def main() -> None:
    # 1. Verify high-k1 BM25 (k1=3.9, b=0.55) rewards repeated query term occurrences in full-text
    # scientific articles more strongly than default BM25 (k1=0.9, b=0.4) (Section 5.1 & 5.3):
    q_terms = ["coronavirus", "hypertension"]
    idf_map = {"coronavirus": 2.0, "hypertension": 3.5}
    doc_incidental = {"coronavirus": 2, "hypertension": 1}
    doc_repeated = {"coronavirus": 2, "hypertension": 8}

    ratio_default = (
        bm25_score(q_terms, doc_repeated, 1000, 1000.0, idf_map, k1=0.9, b=0.4)
        / bm25_score(q_terms, doc_incidental, 1000, 1000.0, idf_map, k1=0.9, b=0.4)
    )
    ratio_tuned = (
        bm25_score(q_terms, doc_repeated, 1000, 1000.0, idf_map, k1=3.9, b=0.55)
        / bm25_score(q_terms, doc_incidental, 1000, 1000.0, idf_map, k1=3.9, b=0.55)
    )
    assert ratio_tuned > ratio_default > 1.0

    # 2. Verify Eq. (1) cross-entropy loss monotonicity:
    l_good = pairwise_cross_entropy_loss(r_pos=0.92, r_neg=0.08)
    l_bad = pairwise_cross_entropy_loss(r_pos=0.55, r_neg=0.45)
    assert l_good < l_bad

    # 3. Verify MedSyn lexicon filtering with excluded common ambiguity terms (Section 5.2 footnote 5):
    medsyn = {"pneumonia", "hypertension", "coronavirus", "gas", "card", "bing", "died", "map", "fall"}
    excluded = {"gas", "card", "bing", "died", "map", "fall"}
    sample_queries = [
        (1, "what causes viral pneumonia in adults"),
        (2, "how to pay credit card bill online"),
        (3, "coronavirus response to weather changes"),
        (4, "bing map directions"),
    ]
    kept = filter_med_msmarco_queries(sample_queries, medsyn, excluded)
    assert kept == [1, 3]

    print("SLEDGE boundary verification passed:")
    print(f"  Tuned BM25 repetition gain ratio: {ratio_tuned:.4f} > default {ratio_default:.4f}")
    print(f"  Pairwise CE loss: good={l_good:.4f} < bad={l_bad:.4f}")
    print(f"  Med-MSMARCO filtered query IDs: {kept}")


if __name__ == "__main__":
    main()
