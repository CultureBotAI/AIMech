#!/usr/bin/env python3
"""Constructed boundary verification for DRAGON (Lin et al., Findings of EMNLP 2023, arXiv:2302.07452).

Verifies:
1. Progressive label augmentation schedule (Section 3.2 & Appendix A.2, Figure 2):
   at training iteration T in {1, ..., N}, DRAGON uniformly samples a teacher retriever n ~ U(1, T)
   ordered from simpler to more generalizable teachers (e.g., uniCOIL -> Contriever -> GTR-XXL ->
   ColBERTv2 -> SPLADE++), and samples positives from top-k (k = 10) and hard negatives from ranks 46..50
   of ranking list P_q^n.
2. Appendix A.2 consensus sampling probability and union diversity:
   - Under uniform sampling across T teachers where each teacher marks its top-k passages as positive,
     a passage retrieved in the top-k of m <= T teachers is sampled with probability m / (T * k)
     (reaching 1/k when m = T), naturally up-weighting multi-perspective consensus positives without
     requiring score normalization or linear fusion weight tuning.
   - Progressive supervision strictly increases the union size of positive passages |U_{n=1}^T TopK(P_q^n)|
     across iterations T = 1, 2, ..., N while preserving consensus priority.
"""

from __future__ import annotations


def progressive_positive_sampling_distribution(
    teacher_top_k_lists: list[list[str]], iteration_t: int
) -> tuple[dict[str, float], dict[str, float]]:
    """Compute exact positive sampling probabilities and reciprocal-rank tie-breakers at iteration T <= N."""
    assert 1 <= iteration_t <= len(teacher_top_k_lists)
    active_lists = teacher_top_k_lists[:iteration_t]
    k = len(active_lists[0])
    probs: dict[str, float] = {}
    rr_sums: dict[str, float] = {}

    for r_list in active_lists:
        assert len(r_list) == k
        for idx, doc_id in enumerate(r_list):
            rank = idx + 1
            probs[doc_id] = probs.get(doc_id, 0.0) + 1.0 / (iteration_t * k)
            rr_sums[doc_id] = rr_sums.get(doc_id, 0.0) + 1.0 / rank

    return probs, rr_sums


def main() -> None:
    # Three diverse teachers (sparse uniCOIL, dense Contriever, multi-vector ColBERTv2) with k=4 top passages
    t1_unicoil = ["p_consensus", "p_lex1", "p_shared12", "p_lex2"]
    t2_contriever = ["p_sem1", "p_consensus", "p_shared12", "p_sem2"]
    t3_colbertv2 = ["p_consensus", "p_mv1", "p_mv2", "p_mv3"]
    teachers = [t1_unicoil, t2_contriever, t3_colbertv2]
    k = 4

    # 1. Verify progressive expansion of positive supervision diversity |Union_{n=1}^T TopK(P_q^n)|
    p1, _ = progressive_positive_sampling_distribution(teachers, iteration_t=1)
    p2, _ = progressive_positive_sampling_distribution(teachers, iteration_t=2)
    p3, rr3 = progressive_positive_sampling_distribution(teachers, iteration_t=3)

    assert len(p1) < len(p2) < len(p3)
    assert abs(sum(p1.values()) - 1.0) < 1e-12
    assert abs(sum(p2.values()) - 1.0) < 1e-12
    assert abs(sum(p3.values()) - 1.0) < 1e-12

    # 2. Verify Appendix A.2 identity: a passage in top-k of all 3 teachers has sampling probability
    # (1/3)*(1/k + 1/k + 1/k) == 1/k, strictly higher than 2-teacher (2/(3k)) or 1-teacher (1/(3k)) positives
    assert abs(p3["p_consensus"] - (1.0 / k)) < 1e-12
    assert abs(p3["p_shared12"] - (2.0 / (3.0 * k))) < 1e-12
    assert abs(p3["p_mv1"] - (1.0 / (3.0 * k))) < 1e-12
    assert p3["p_consensus"] > p3["p_shared12"] > p3["p_mv1"]

    # 3. Verify reciprocal-rank tie-breaking among equal-frequency passages (Appendix A.2):
    # p_lex1 is rank 2 in teacher 1 (RR = 1/2), whereas p_lex2 is rank 4 in teacher 1 (RR = 1/4)
    assert abs(p3["p_lex1"] - p3["p_lex2"]) < 1e-12
    assert rr3["p_lex1"] > rr3["p_lex2"]

    print(
        "DRAGON boundary verification passed:",
        {"union_sizes": [len(p1), len(p2), len(p3)], "p_consensus": round(p3["p_consensus"], 4)},
    )


if __name__ == "__main__":
    main()
