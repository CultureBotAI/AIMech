#!/usr/bin/env python3
"""Constructed boundary verification for TART (Asai et al., Findings of ACL 2023, arXiv:2211.09260).

Verifies:
1. Retrieval with instructions formulation (Section 3 & Section 5.1, Eq. 1-2):
   - TART-dual bi-encoder score: s(t, q, d) = E([t; q])^T E(d), conditioning query representation on
     explicit instruction t (specifying intent, domain, and unit).
   - TART-full cross-encoder score: s(t, q, d) = FFN(E([t; q; d])) in (0, 1).
2. Negative sampling with denoised hard negatives d^HD and instruction-unfollowing negatives d^UF
   (Section 4.2 & Section 5.2):
   - Denoised hard negatives d^HD: top retrieved documents from the same task corpus whose cross-encoder
     relevance score is below threshold tau_CE = 0.1.
   - Instruction-unfollowing negatives d^UF: top retrieved documents for query q from a different task's
     corpus (which match the query topic lexically/semantically but violate the domain/intent/unit in t).
3. Cross-task cross-domain retrieval (X^2-Retrieval, Section 6.2 & Table 11):
   for identical query q across a pooled multi-domain corpus, changing the instruction t flips the
   top-ranked document between a code implementation, a duplicate question, and an answer passage.
"""

from __future__ import annotations
import math


def dot(u: list[float], v: list[float]) -> float:
    return sum(a * b for a, b in zip(u, v))


def tart_dual_inbatch_loss(
    pos_score: float, neg_scores: list[float], temperature: float = 0.05
) -> float:
    """Compute TART-dual InfoNCE loss L = -log(exp(s(q, d^+, t)/T) / sum_{d in B} exp(s(q, d, t)/T))."""
    scaled = [pos_score / temperature] + [s / temperature for s in neg_scores]
    m = max(scaled)
    exps = [math.exp(x - m) for x in scaled]
    return -(scaled[0] - m - math.log(sum(exps)))


def tart_full_bce_loss(pos_probs: list[float], neg_probs: list[float]) -> float:
    """Compute TART-full cross-entropy loss (Section 5.2): -sum_{d^+} log s - sum_{d^-} log(1 - s)."""
    return -sum(math.log(p) for p in pos_probs) - sum(math.log(1.0 - p) for p in neg_probs)


def filter_denoised_hard_negatives(
    candidates: list[tuple[str, float, str]], target_domain: str, ce_threshold: float = 0.1
) -> tuple[list[str], list[str]]:
    """Partition retrieved candidates into denoised hard negatives d^HD and instruction-unfollowing d^UF."""
    d_hd: list[str] = []
    d_uf: list[str] = []
    for doc_id, ce_prob, doc_domain in candidates:
        if doc_domain == target_domain:
            if ce_prob < ce_threshold:
                d_hd.append(doc_id)
        else:
            d_uf.append(doc_id)
    return d_hd, d_uf


def main() -> None:
    # 4-dimensional embedding space: [topic_batchnorm, intent_code, intent_dup_question, intent_answer_passage]
    docs = {
        "d_code": [0.8, 1.0, -0.3, -0.3],
        "d_dup_q": [0.8, -0.3, 1.0, -0.3],
        "d_answer": [0.8, -0.3, -0.3, 1.0],
    }

    # Instruction-conditioned query encodings E([t_i; q]) for identical query q ("batch normalization in Python")
    q_no_inst = [1.0, 0.0, 0.0, 0.0]
    q_code_inst = [0.8, 0.9, -0.2, -0.2]
    q_dup_inst = [0.8, -0.2, 0.9, -0.2]
    q_ans_inst = [0.8, -0.2, -0.2, 0.9]

    # 1. Without instruction, all three documents tie on topic similarity (ambiguous user intent)
    scores_no_inst = {k: round(dot(q_no_inst, v), 6) for k, v in docs.items()}
    assert scores_no_inst["d_code"] == scores_no_inst["d_dup_q"] == scores_no_inst["d_answer"]

    # 2. With explicit instructions t_1, t_2, t_3, TART-dual routes the same query to the matching intent/unit
    top_code = max(docs, key=lambda k: dot(q_code_inst, docs[k]))
    top_dup = max(docs, key=lambda k: dot(q_dup_inst, docs[k]))
    top_ans = max(docs, key=lambda k: dot(q_ans_inst, docs[k]))
    assert (top_code, top_dup, top_ans) == ("d_code", "d_dup_q", "d_answer")

    # 3. Verify denoised hard negative (CE < 0.1 in same domain) and instruction-unfollowing negative (cross-corpus)
    candidates = [
        ("so_false_neg", 0.82, "stackoverflow_q"),
        ("so_hard_neg", 0.04, "stackoverflow_q"),
        ("wiki_unfollowing", 0.65, "wikipedia_paragraph"),
    ]
    d_hd, d_uf = filter_denoised_hard_negatives(candidates, target_domain="stackoverflow_q", ce_threshold=0.1)
    assert d_hd == ["so_hard_neg"]
    assert d_uf == ["wiki_unfollowing"]

    # 4. Verify training losses decrease when instruction-unfollowing negative score is suppressed
    loss_before = tart_dual_inbatch_loss(pos_score=1.42, neg_scores=[1.35, 0.20])
    loss_after = tart_dual_inbatch_loss(pos_score=1.42, neg_scores=[0.30, 0.20])
    assert loss_after < loss_before

    bce_good = tart_full_bce_loss([0.92], [0.05, 0.03])
    bce_bad = tart_full_bce_loss([0.92], [0.75, 0.03])
    assert bce_good < bce_bad

    print("TART boundary verification passed:", {"loss_before": round(loss_before, 4), "loss_after": round(loss_after, 4)})


if __name__ == "__main__":
    main()
