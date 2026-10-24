#!/usr/bin/env python3
"""Constructed boundary verification script for Round 769:
GAR (Generation-Augmented Retrieval for Open-Domain Question Answering)
by Yuning Mao, Pengcheng He, Xiaodong Liu, Yelong Shen, Jianfeng Gao,
Jiawei Han, and Weizhu Chen (ACL 2021, arXiv:2009.08553).

Verifies:
1. Multi-context query augmentation (Section 3.2-3.3): expanding question q with
   three complementary PLM-generated contexts—Answer c_ans(q), Sentence c_sent(q),
   and Title c_title(q)—to form generation-augmented queries q^{(m)} = q union c_m(q)
   and fusing their top-retrieved passage rankings. Even when one generated context
   (e.g., Answer) is hallucinated/incorrect, complementary Sentence and Title contexts
   recover the ground-truth passage (Table 2 examples).
2. Passage-level Span Voting for extractive reading (Section 4.1):
     p(S_i[j]) = softmax(D)[i] * softmax(S_i)[j],
     Score(surface_form) = sum_{(i, j): norm(S_i[j]) == surface_form} p(S_i[j]),
   which allows a consistent correct answer span appearing across multiple retrieved
   passages to outvote a single noisy top-1 span.
"""

import math


def softmax(scores):
    m = max(scores)
    exps = [math.exp(s - m) for s in scores]
    total = sum(exps)
    return [e / total for e in exps]


def passage_level_span_voting(passage_logits, span_logits_per_passage, span_texts_per_passage):
    """Implements Section 4.1 Passage-level Span Voting:
    p(S_i[j]) = softmax(D)[i] * softmax(S_i)[j], aggregated by surface form."""
    p_passage = softmax(passage_logits)
    independent_best = None
    independent_best_prob = -1.0
    voted_scores = {}

    for i, (s_logits, s_texts) in enumerate(zip(span_logits_per_passage, span_texts_per_passage)):
        p_spans = softmax(s_logits)
        for j, (prob_j, text_j) in enumerate(zip(p_spans, s_texts)):
            joint_p = p_passage[i] * prob_j
            voted_scores[text_j] = voted_scores.get(text_j, 0.0) + joint_p
            if joint_p > independent_best_prob:
                independent_best_prob = joint_p
                independent_best = text_j

    voted_best = max(voted_scores.items(), key=lambda kv: kv[1])[0]
    return independent_best, voted_best, voted_scores


def main():
    # 1. Verify complementary multi-target query expansion (Table 2: "who sings does he love me with reba?")
    q_terms = {"sings", "does", "love", "reba"}
    # Ground-truth passage contains {"does", "love", "reba", "mcentire", "linda", "davis", "duet", "greatest", "hits"}
    gt_passage = {"does", "love", "reba", "mcentire", "linda", "davis", "duet", "greatest", "hits"}
    distractor_passage = {"sings", "does", "love", "reba", "brooks", "dunn"}

    # Suppose generated Answer is wrong ("brooks", "dunn"), but generated Sentence ("linda", "davis", "mcentire")
    # and generated Title ("mcentire", "linda", "davis") are relevant:
    q_ans = q_terms | {"brooks", "dunn"}
    q_sent = q_terms | {"linda", "davis", "mcentire", "duet"}
    q_title = q_terms | {"mcentire", "linda", "davis"}

    # Lexical overlap with ground-truth passage increases substantially under Sentence and Title expansion,
    # and fusing top-1 from each context source (Answer, Sentence, Title) recalls gt_passage!
    assert len(q_sent & gt_passage) > len(q_terms & gt_passage)
    assert len(q_title & gt_passage) > len(q_terms & gt_passage)

    top1_ans = "distractor" if len(q_ans & distractor_passage) > len(q_ans & gt_passage) else "gt"
    top1_sent = "gt" if len(q_sent & gt_passage) > len(q_sent & distractor_passage) else "distractor"
    top1_title = "gt" if len(q_title & gt_passage) > len(q_title & distractor_passage) else "distractor"
    fused_candidates = {top1_ans, top1_sent, top1_title}
    assert top1_ans == "distractor"
    assert top1_sent == "gt" and top1_title == "gt"
    assert "gt" in fused_candidates

    # 2. Verify Passage-level Span Voting (Section 4.1)
    # 3 retrieved passages with passage logits D:
    passage_logits = [2.0, 1.8, 1.7]
    # Passage 0 has a slightly higher single-span score for wrong answer "Brooks & Dunn",
    # but "Linda Davis" is consistently extracted across all 3 passages:
    span_logits = [
        [2.8, 1.2],  # Passage 0
        [1.8, 0.5],  # Passage 1
        [1.8, 0.2],  # Passage 2
    ]
    span_texts = [
        ["Brooks & Dunn", "Linda Davis"],
        ["Linda Davis", "Reba McEntire"],
        ["Linda Davis", "Sandy Knox"],
    ]

    ind_best, voted_best, voted_scores = passage_level_span_voting(
        passage_logits, span_logits, span_texts
    )
    assert ind_best == "Brooks & Dunn"
    assert voted_best == "Linda Davis"
    assert voted_scores["Linda Davis"] > voted_scores["Brooks & Dunn"]

    print(
        f"[PASS] GAR boundaries verified: fused_candidates={sorted(fused_candidates)}, "
        f"voted_best={voted_best!r} ({voted_scores['Linda Davis']:.4f}) > "
        f"independent_best={ind_best!r} ({voted_scores['Brooks & Dunn']:.4f})"
    )


if __name__ == "__main__":
    main()
