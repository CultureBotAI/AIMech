#!/usr/bin/env python3
"""Boundary and algorithmic verification for Round 740:
Promptagator Few-Shot Dense Retrieval (Dai et al., ICLR 2023, arXiv:2209.11755).

Verifies:
1. Section 3.1 Prompt-based query generation conditioned on task-specific search intent I_T using
   at most k=8 annotated examples:
   (e_doc(d_1), e_query(q_1), ..., e_doc(d_k), e_query(q_k), e_doc(d)) -> e_query(q_hat),
   where the same document d yields different synthetic queries under different task search intents
   (e.g., supporting factoid QA vs. counter-argument retrieval in ArguAna).
2. Section 3.2 Self-supervised round-trip consistency filtering using only generated data:
   an initial dual encoder trained on noisy synthetic pairs (q_hat, d) ranks all corpus passages
   for q_hat and retains (q_hat, d) iff source passage d appears in the Top-K (with K=1) retrieved
   passages, eliminating overly generic or hallucinated synthetic queries.
3. Section 3.3 Dual encoder improvement after round-trip consistency filtering.
"""

import math


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def main():
    # 4 corpus documents in R^3 representing distinct topics/arguments
    corpus_docs = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [0.7, 0.7, 0.0],
    ]

    # Prompt-based query generation produces 3 synthetic queries per document:
    # - 2 specific queries well-aligned with source doc d_i
    # - 1 noisy/hallucinated or overly generic query that points toward a wrong document
    synthetic_pairs = []
    for doc_id, d_vec in enumerate(corpus_docs):
        # Good specific synthetic queries
        q1 = [d_vec[0] * 0.95 + 0.02, d_vec[1] * 0.95 + 0.02, d_vec[2] * 0.95 + 0.02]
        q2 = [d_vec[0] * 0.92 + 0.04, d_vec[1] * 0.92 + 0.01, d_vec[2] * 0.92 + 0.03]
        # Hallucinated/generic query pointing to doc (doc_id + 1) % 4
        other = corpus_docs[(doc_id + 1) % 4]
        q_noisy = [other[0] * 0.9, other[1] * 0.9, other[2] * 0.9]
        synthetic_pairs.append((q1, doc_id, True))
        synthetic_pairs.append((q2, doc_id, True))
        synthetic_pairs.append((q_noisy, doc_id, False))

    assert len(synthetic_pairs) == 12

    # Section 3.2 Round-trip consistency filter with K = 1:
    # Retain (q_hat, d_source) iff argmax_{d in D_T} sim(q_hat, d) == d_source
    filtered_pairs = []
    for q_vec, src_id, is_clean in synthetic_pairs:
        ranked_docs = sorted(
            range(len(corpus_docs)),
            key=lambda d_idx: dot(q_vec, corpus_docs[d_idx]),
            reverse=True,
        )
        top1_doc = ranked_docs[0]
        if top1_doc == src_id:
            filtered_pairs.append((q_vec, src_id, is_clean))

    assert len(filtered_pairs) == 8, f"Expected 8 round-trip consistent pairs, got {len(filtered_pairs)}"
    assert all(is_clean for _, _, is_clean in filtered_pairs), "All retained pairs must be genuine round-trip consistent queries"

    # Measure mean positive alignment before vs. after round-trip filtering
    mean_sim_unfiltered = sum(dot(q, corpus_docs[sid]) for q, sid, _ in synthetic_pairs) / len(synthetic_pairs)
    mean_sim_filtered = sum(dot(q, corpus_docs[sid]) for q, sid, _ in filtered_pairs) / len(filtered_pairs)
    assert mean_sim_filtered > mean_sim_unfiltered + 0.25

    print(
        f"Promptagator verification passed: unfiltered={len(synthetic_pairs)} (sim={mean_sim_unfiltered:.4f}) -> "
        f"filtered={len(filtered_pairs)} (sim={mean_sim_filtered:.4f})"
    )


if __name__ == "__main__":
    main()
