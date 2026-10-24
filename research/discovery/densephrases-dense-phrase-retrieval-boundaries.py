#!/usr/bin/env python3
"""Constructed boundary verification for DensePhrases (Lee et al., 2021, arXiv:2012.12624).

Verifies:
1. Decomposed token-endpoint phrase representation E_s(s_(i,j), p) = [h_i, h_j] in R^{2d}
   and constrained MIPS search (Eqs. 3, 4, 10): argmax_{1 <= i <= j < i + L} (H q^start)_i + (H q^end)_j,
   storing only |W(D)| token vectors instead of O(|W(D)| * L) phrase vectors.
2. FIFO pre-batch negatives (Section 4.3, Eq. 8): augmenting B - 1 in-batch negatives with
   B * C detached phrase-endpoint negatives from the preceding C mini-batches.
3. Query-side fine-tuning marginal log-likelihood loss over top-k retrieved phrases
   matching gold answer string TEXT(s) == a* (Section 6, Eq. 11).
"""

from __future__ import annotations

import math


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def softmax(logits: list[float]) -> list[float]:
    m = max(logits)
    exps = [math.exp(x - m) for x in logits]
    s = sum(exps)
    return [e / s for e in exps]


def constrained_mips_phrase_search(
    h_dump: list[list[float]],
    q_start: list[float],
    q_end: list[float],
    max_phrase_len: int,
) -> tuple[tuple[int, int], float]:
    """Implements Eq. (10): argmax_{1 <= i <= j < i + L} (H q^start)_i + (H q^end)_j."""
    start_scores = [dot(h_i, q_start) for h_i in h_dump]
    end_scores = [dot(h_j, q_end) for h_j in h_dump]
    n_tokens = len(h_dump)
    best_span = (0, 0)
    best_score = -float("inf")
    for i in range(n_tokens):
        upper_j = min(n_tokens, i + max_phrase_len)
        for j in range(i, upper_j):
            score = start_scores[i] + end_scores[j]
            if score > best_score:
                best_score = score
                best_span = (i, j)
    return best_span, best_score


def prebatch_negative_loss(
    q_start_batch: list[list[float]],
    q_end_batch: list[list[float]],
    g_start_batch: list[list[float]],
    g_end_batch: list[list[float]],
    fifo_g_start: list[list[float]],
    fifo_g_end: list[list[float]],
) -> tuple[float, int]:
    """Implements Section 4.2-4.3 (Eq. 8) with B - 1 in-batch and B * C pre-batch negatives."""
    b_size = len(q_start_batch)
    all_g_start = g_start_batch + fifo_g_start
    all_g_end = g_end_batch + fifo_g_end
    num_negatives_per_item = len(all_g_start) - 1

    total_loss = 0.0
    for i in range(b_size):
        s_start = [dot(q_start_batch[i], g_s) for g_s in all_g_start]
        s_end = [dot(q_end_batch[i], g_e) for g_e in all_g_end]
        p_start = softmax(s_start)[i]
        p_end = softmax(s_end)[i]
        total_loss += -(math.log(p_start) + math.log(p_end)) / 2.0
    return total_loss / b_size, num_negatives_per_item


def query_side_finetuning_loss(
    top_k_phrases: list[tuple[str, float]],
    gold_answer: str,
) -> float:
    """Implements Eq. (11): -log(sum_{s in S~(q), TEXT(s)=a*} exp(f(s)) / sum_{s in S~(q)} exp(f(s)))."""
    scores = [score for _, score in top_k_phrases]
    m = max(scores)
    denom = sum(math.exp(s - m) for s in scores)
    numer = sum(
        math.exp(score - m)
        for text, score in top_k_phrases
        if text == gold_answer
    )
    assert numer > 0.0, "At least one retrieved phrase must match gold_answer"
    return -math.log(numer / denom)


def main() -> None:
    # 1. Verify decomposed endpoint MIPS equivalence (Eq. 3, 4, 10)
    # Passage tokens: ["Don't", "Stand", "by", "the", "Police", "in", "1980"]
    tokens = ["Don't", "Stand", "by", "the", "Police", "in", "1980"]
    h_dump = [
        [0.8, -0.2, 0.1],  # 0: Don't
        [0.3, 0.4, -0.1],  # 1: Stand
        [-0.2, 0.1, 0.2],  # 2: by
        [0.9, 0.8, 0.1],   # 3: the (gold start)
        [0.2, 0.9, 0.85],  # 4: Police (gold end)
        [-0.3, 0.1, -0.2], # 5: in
        [0.7, -0.4, 0.6],  # 6: 1980
    ]
    q_start = [0.85, 0.75, 0.05]
    q_end = [0.15, 0.85, 0.80]
    best_span, best_score = constrained_mips_phrase_search(
        h_dump, q_start, q_end, max_phrase_len=3
    )
    assert best_span == (3, 4)
    assert " ".join(tokens[best_span[0] : best_span[1] + 1]) == "the Police"

    # Verify decomposed dot product equals concatenated 2d dot product [h_i, h_j]^T [q^start, q^end]:
    concat_phrase = h_dump[3] + h_dump[4]
    concat_query = q_start + q_end
    assert abs(best_score - dot(concat_phrase, concat_query)) < 1e-9

    # 2. Verify pre-batch negatives count B * C + B - 1 (B = 2, C = 2 -> 2*2 + 2 - 1 = 5 negatives)
    q_s_batch = [[0.9, 0.8, 0.1], [0.1, 0.2, 0.9]]
    q_e_batch = [[0.2, 0.9, 0.8], [0.8, 0.1, 0.7]]
    g_s_batch = [[0.9, 0.8, 0.1], [0.1, 0.2, 0.9]]
    g_e_batch = [[0.2, 0.9, 0.8], [0.8, 0.1, 0.7]]
    fifo_s = [[-0.5, 0.2, 0.1], [0.2, -0.4, 0.3], [-0.3, -0.2, 0.4], [0.3, -0.5, -0.2]]
    fifo_e = [[-0.4, 0.1, 0.2], [0.1, -0.3, 0.2], [-0.2, -0.4, 0.1], [0.2, -0.4, -0.3]]
    neg_loss, num_negs = prebatch_negative_loss(
        q_s_batch, q_e_batch, g_s_batch, g_e_batch, fifo_s, fifo_e
    )
    assert num_negs == 2 * 2 + 2 - 1 == 5
    assert neg_loss > 0.0

    # 3. Verify query-side fine-tuning marginal log-likelihood over multiple surface occurrences (Eq. 11)
    top_k_single_occurrence = [
        ("the Police", 3.2),
        ("Sting", 2.9),
        ("Duke Ellington", 1.8),
    ]
    top_k_multi_occurrence = [
        ("the Police", 3.2),
        ("Sting", 2.9),
        ("the Police", 2.7),  # Second occurrence of gold answer in another passage
    ]
    loss_single_occ = query_side_finetuning_loss(top_k_single_occurrence, "the Police")
    loss_multi_occ = query_side_finetuning_loss(top_k_multi_occurrence, "the Police")
    assert loss_multi_occ < loss_single_occ

    print(
        f"[PASS] DensePhrases boundaries verified: best_span={best_span} ('the Police'), "
        f"num_negs={num_negs}, qs_loss_multi={loss_multi_occ:.4f} < qs_loss_single={loss_single_occ:.4f}"
    )


if __name__ == "__main__":
    main()
