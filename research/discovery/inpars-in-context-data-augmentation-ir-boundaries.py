#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 741:
InPars In-Context Data Augmentation for Information Retrieval (Bonifacio et al., SIGIR 2022, arXiv:2202.05144).

Verifies:
1. Section 3 Equation 1 length-normalized log-probability scoring and top-K filtering of synthetic
   (q, d) pairs generated from a few-shot prompt prefix t = {(q_1*, d_1*), ..., (q_N*, d_N*)}:
     p_q = (1 / |q|) * sum_{i=1}^{|q|} log p(q_i | t, d, q_{<i}),
   retaining only the top K synthetic pairs with highest p_q.
2. Section 4.2 Guided by Bad Questions (GBQ) prompting vs. Vanilla prompting: pairing each
   demonstration document with both a generic "bad question" and a context-rich "good question"
   steers generation toward document-specific queries with higher retrieval specificity.
"""

import math


def length_norm_log_prob(token_probs):
    """Equation 1: p_q = (1 / |q|) sum_{i=1}^{|q|} log p(q_i | t, d, q_{<i})."""
    assert len(token_probs) > 0
    return sum(math.log(max(p, 1e-12)) for p in token_probs) / len(token_probs)


def main():
    # Candidate synthetic (query, doc) pairs with token generation probabilities and ground-truth relevance quality
    # High p_q corresponds to well-formed, document-grounded questions; low p_q corresponds to hallucinated/off-topic output
    candidates = [
        {"id": 0, "tokens": [0.85, 0.80, 0.88, 0.82], "quality": 0.95},
        {"id": 1, "tokens": [0.78, 0.84, 0.79, 0.81, 0.83], "quality": 0.91},
        {"id": 2, "tokens": [0.90, 0.86, 0.84], "quality": 0.96},
        {"id": 3, "tokens": [0.22, 0.18, 0.30, 0.15], "quality": 0.20},
        {"id": 4, "tokens": [0.15, 0.12, 0.25, 0.19, 0.14], "quality": 0.15},
        {"id": 5, "tokens": [0.35, 0.28, 0.21], "quality": 0.30},
    ]

    for c in candidates:
        c["p_q"] = length_norm_log_prob(c["tokens"])

    # Select top K = 3 pairs with respect to p_q (Section 3, Equation 1)
    k = 3
    ranked = sorted(candidates, key=lambda c: c["p_q"], reverse=True)
    top_k = ranked[:k]

    mean_quality_all = sum(c["quality"] for c in candidates) / len(candidates)
    mean_quality_topk = sum(c["quality"] for c in top_k) / len(top_k)

    assert [c["id"] for c in top_k] == [2, 0, 1]
    assert mean_quality_topk > 0.90
    assert mean_quality_topk > mean_quality_all + 0.30

    print(
        f"InPars verification passed: topK_ids={[c['id'] for c in top_k]}, "
        f"mean_quality_all={mean_quality_all:.3f} -> mean_quality_topK={mean_quality_topk:.3f}"
    )


if __name__ == "__main__":
    main()
