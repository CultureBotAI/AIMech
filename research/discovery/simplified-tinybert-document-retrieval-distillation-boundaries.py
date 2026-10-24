#!/usr/bin/env python3
"""Constructed boundary verification for Simplified TinyBERT (Chen et al., ECIR 2021, arXiv:2009.07531)."""

import math


def mse_matrix(student_mat: list[list[float]], teacher_mat: list[list[float]]) -> float:
    r = len(student_mat)
    c = len(student_mat[0])
    return sum(
        (student_mat[i][j] - teacher_mat[i][j]) ** 2
        for i in range(r)
        for j in range(c)
    ) / (r * c)


def bce_probs(student_prob: float, target_prob: float, eps: float = 1e-12) -> float:
    sp = min(max(student_prob, eps), 1.0 - eps)
    return -(target_prob * math.log(sp) + (1.0 - target_prob) * math.log(1.0 - sp))


def simplified_tinybert_loss(
    s_attn: list[list[float]],
    t_attn: list[list[float]],
    s_hidn: list[list[float]],
    t_hidn: list[list[float]],
    s_emb: list[list[float]],
    t_emb: list[list[float]],
    s_prob: float,
    t_prob: float,
    hard_label: float,
) -> tuple[float, float]:
    """Eqs. (1)-(2): L = L_attn + L_hidn + L_emb + L_soft, L_h = L + L_hard."""
    l_attn = mse_matrix(s_attn, t_attn)
    l_hidn = mse_matrix(s_hidn, t_hidn)
    l_emb = mse_matrix(s_emb, t_emb)
    l_soft = bce_probs(s_prob, t_prob)
    l_hard = bce_probs(s_prob, hard_label)
    l_one_step = l_attn + l_hidn + l_emb + l_soft
    l_h = l_one_step + l_hard
    return l_one_step, l_h


def bert_maxp_document_score(passage_scores: list[float]) -> float:
    """Section 2: Document relevance score produced by its best passage (BERT-MaxP)."""
    return max(passage_scores)


def filter_positive_passages_by_teacher(
    passage_ids_and_scores: list[tuple[int, float]],
    top_k: int = 5,
) -> list[int]:
    """Section 4.1: Reserve top-5 teacher-ranked passages from relevant documents as positive samples."""
    ranked = sorted(passage_ids_and_scores, key=lambda pair: pair[1], reverse=True)
    return [pid for pid, _ in ranked[:top_k]]


def main() -> None:
    s_attn = [[0.6, 0.4], [0.3, 0.7]]
    t_attn = [[0.65, 0.35], [0.25, 0.75]]
    s_hidn = [[0.1, -0.2, 0.5], [0.4, 0.3, -0.1]]
    t_hidn = [[0.12, -0.18, 0.48], [0.38, 0.32, -0.12]]
    s_emb = [[0.5, 0.2, -0.3], [0.1, 0.4, 0.2]]
    t_emb = [[0.52, 0.19, -0.28], [0.09, 0.41, 0.22]]

    # 1. Verify unified one-step loss Eq. (1) and hard-label augmented loss Eq. (2):
    # Suppose teacher slightly under-scores a relevant passage (t_prob = 0.75, hard_label = 1.0).
    # Student 1 matches teacher soft label (0.75), while Student 2 is closer to hard label 1.0 (0.88):
    _, l_h_s1 = simplified_tinybert_loss(s_attn, t_attn, s_hidn, t_hidn, s_emb, t_emb, 0.75, 0.75, 1.0)
    _, l_h_s2 = simplified_tinybert_loss(s_attn, t_attn, s_hidn, t_hidn, s_emb, t_emb, 0.88, 0.75, 1.0)
    assert l_h_s2 < l_h_s1, "Hard label term L_hard rewards higher confidence on ground-truth positive passage"

    # 2. Verify teacher top-5 positive passage filtering and BERT-MaxP document aggregation:
    passages = [(10, 0.12), (11, 0.91), (12, 0.84), (13, 0.45), (14, 0.77), (15, 0.68), (16, 0.63)]
    top5 = filter_positive_passages_by_teacher(passages, top_k=5)
    assert top5 == [11, 12, 14, 15, 16]
    assert abs(bert_maxp_document_score([s for _, s in passages]) - 0.91) < 1e-12

    # 3. Verify second-stage training time reduction (Table 3):
    tinybert_hours = [29.95, 20.45, 18.93, 15.87]
    simplified_hours = [14.37, 11.30, 10.05, 9.22]
    savings = [(t - s) / t for t, s in zip(tinybert_hours, simplified_hours)]
    assert all(0.41 < sv < 0.53 for sv in savings)

    print("Simplified TinyBERT boundary verification passed:")
    print(f"  L_h(student=0.88)={l_h_s2:.4f} < L_h(student=0.75)={l_h_s1:.4f}")
    print(f"  Top-5 teacher-filtered positive passages: {top5}")
    print(f"  Second-stage training time savings: {[round(100 * s, 1) for s in savings]}%")


if __name__ == "__main__":
    main()
