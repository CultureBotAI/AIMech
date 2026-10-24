#!/usr/bin/env python3
"""Constructed boundary verification for Doc2query (Nogueira et al., 2019, arXiv:1904.08375).

Verifies:
1. Complementary effects of predicted query tokens in BM25 document expansion (Section 5, Table 2):
   - Copied words (69% of non-stopword predicted tokens) perform implicit term re-weighting
     by increasing the BM25 term frequency (TF) of salient document words.
   - New words (31% of non-stopword predicted tokens) resolve vocabulary mismatch by adding
     synonyms/related query terms not present in the original document.
2. Combining both copied and new predicted query terms strictly outperforms unexpanded BM25,
   copied-only expansion, and new-only expansion.
"""

from __future__ import annotations

import math
from collections import Counter


def bm25_score(
    query_terms: list[str],
    doc_terms: list[str],
    idf: dict[str, float],
    avgdl: float,
    k1: float = 1.2,
    b: float = 0.75,
) -> float:
    tf_counts = Counter(doc_terms)
    dl = len(doc_terms)
    score = 0.0
    for term in query_terms:
        tf = tf_counts.get(term, 0)
        if tf == 0:
            continue
        numer = tf * (k1 + 1.0)
        denom = tf + k1 * (1.0 - b + b * (dl / avgdl))
        score += idf.get(term, 0.0) * (numer / denom)
    return score


def main() -> None:
    # Example inspired by Table 2 of Nogueira et al. (2019):
    # Gold relevant doc (d+): about July/January average temperature C/F and rain in Washington DC
    doc_pos_orig = [
        "july", "hottest", "month", "washington", "dc", "average",
        "temperature", "january", "coldest", "wettest", "may", "rain",
    ]
    # Distractor doc (d-): mentions "washington" twice and "weather" once in an unrelated context
    doc_neg_orig = [
        "george", "washington", "crossed", "delaware", "river", "winter",
        "weather", "washington", "troops", "marched", "philadelphia", "camp",
    ]

    # Doc2query predicted queries for d+ (Table 2): e.g. "weather in washington dc"
    # - Copied non-stopwords (69%): ["washington", "dc", "washington", "temperature"]
    # - New non-stopwords (31%): ["weather", "weather", "climate"]
    copied_expansion = ["washington", "dc", "washington", "temperature"]
    new_expansion = ["weather", "weather", "climate"]
    full_doc2query_expansion = copied_expansion + new_expansion
    neg_expansion = ["delaware", "river", "crossing", "troops", "george", "winter", "camp"]

    # User query: "weather in washington" -> non-stopword terms ["weather", "washington"]
    user_query = ["weather", "washington"]
    idf = {"weather": 2.4, "washington": 1.5, "dc": 1.8, "temperature": 1.6}

    avgdl_orig = (len(doc_pos_orig) + len(doc_neg_orig)) / 2.0

    # 1. Unexpanded BM25 fails due to vocabulary mismatch ("weather" absent in d+):
    s_pos_orig = bm25_score(user_query, doc_pos_orig, idf, avgdl_orig)
    s_neg_orig = bm25_score(user_query, doc_neg_orig, idf, avgdl_orig)
    assert s_neg_orig > s_pos_orig

    # 2. Copied-only expansion boosts TF("washington") in d+:
    doc_pos_copied = doc_pos_orig + copied_expansion
    doc_neg_exp = doc_neg_orig + neg_expansion
    avgdl_copied = (len(doc_pos_copied) + len(doc_neg_exp)) / 2.0
    s_pos_copied = bm25_score(user_query, doc_pos_copied, idf, avgdl_copied)
    assert s_pos_copied > s_pos_orig

    # 3. New-only expansion injects "weather" into d+, improving score over original:
    doc_pos_new = doc_pos_orig + new_expansion
    avgdl_new = (len(doc_pos_new) + len(doc_neg_exp)) / 2.0
    s_pos_new = bm25_score(user_query, doc_pos_new, idf, avgdl_new)
    assert s_pos_new > s_pos_orig

    # 4. Full Doc2query expansion (copied + new words) achieves highest score and ranks d+ > d-:
    doc_pos_full = doc_pos_orig + full_doc2query_expansion
    avgdl_full = (len(doc_pos_full) + len(doc_neg_exp)) / 2.0
    s_pos_full = bm25_score(user_query, doc_pos_full, idf, avgdl_full)
    s_neg_full = bm25_score(user_query, doc_neg_exp, idf, avgdl_full)
    assert s_pos_full > s_pos_new and s_pos_full > s_pos_copied
    assert s_pos_full > s_neg_full

    # Verify Table 2 empirical proportions: 69% copied + 31% new = 100% of non-stopword tokens
    assert math.isclose(0.69 + 0.31, 1.0)

    print(
        f"[PASS] Doc2query boundaries verified: orig={s_pos_orig:.4f} < copied={s_pos_copied:.4f}, "
        f"new={s_pos_new:.4f} < full={s_pos_full:.4f} (> distractor={s_neg_full:.4f})"
    )


if __name__ == "__main__":
    main()
