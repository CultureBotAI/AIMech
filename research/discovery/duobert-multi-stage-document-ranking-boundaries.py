#!/usr/bin/env python3
"""Constructed boundary verification for monoBERT/duoBERT Multi-Stage Ranking (Nogueira et al., 2019, arXiv:1910.14424).

Verifies:
1. Three-stage cascading latency/inference count: total BERT inferences = k_0 (monoBERT) + k_1 * (k_1 - 1) (duoBERT)
   (or k_0 + k_1 * m for SAMPLE aggregation, Section 3.3 & Figures 3-4).
2. Antisymmetric pairwise classification loss L_duo = -sum_{i in J_pos, j in J_neg} log(p_{i,j}) - sum_{i in J_neg, j in J_pos} log(1 - p_{i,j}) (Eq. 2).
3. Pairwise aggregation operators (Section 3.3, Eqs. 3-6): SUM, BINARY (Condorcet), MIN, and MAX,
   demonstrating how SUM and BINARY promote the true relevant passage above a distractor when
   MAX fails due to a single noisy high-probability pairwise comparison against a weak candidate.
"""

from __future__ import annotations

import math


def mono_bert_loss(probs: list[float], pos_indices: set[int], neg_indices: set[int]) -> float:
    """Implements Eq. (1): L_mono = -sum_{j in J_pos} log(s_j) - sum_{j in J_neg} log(1 - s_j)."""
    loss = 0.0
    for j in pos_indices:
        loss += -math.log(max(probs[j], 1e-12))
    for j in neg_indices:
        loss += -math.log(max(1.0 - probs[j], 1e-12))
    return loss


def duo_bert_loss(
    pairwise_probs: dict[tuple[int, int], float],
    pos_indices: set[int],
    neg_indices: set[int],
) -> float:
    """Implements Eq. (2): L_duo over ordered pairs (i, j) where one is relevant and the other is not."""
    loss = 0.0
    for i in pos_indices:
        for j in neg_indices:
            p_ij = pairwise_probs[(i, j)]
            p_ji = pairwise_probs[(j, i)]
            loss += -math.log(max(p_ij, 1e-12))
            loss += -math.log(max(1.0 - p_ji, 1e-12))
    return loss


def aggregate_duobert_scores(
    k1: int,
    pairwise_probs: dict[tuple[int, int], float],
    method: str,
) -> list[float]:
    """Implements Eqs. (3)-(6): SUM, BINARY, MIN, MAX over J_i = {0 <= j < k1, j != i}."""
    scores: list[float] = []
    for i in range(k1):
        j_vals = [pairwise_probs[(i, j)] for j in range(k1) if j != i]
        if method == "SUM":
            scores.append(sum(j_vals))
        elif method == "BINARY":
            scores.append(float(sum(1 for p in j_vals if p > 0.5)))
        elif method == "MIN":
            scores.append(min(j_vals))
        elif method == "MAX":
            scores.append(max(j_vals))
        else:
            raise ValueError(f"Unknown aggregation method: {method}")
    return scores


def main() -> None:
    # 1. Verify multi-stage inference count formula (Section 3.3 & Figure 4):
    k0 = 1000
    k1 = 50
    total_inferences = k0 + k1 * (k1 - 1)
    assert total_inferences == 3450  # Matches Figure 4 right-most axis point (3,450)!

    # 2. Verify monoBERT + duoBERT stage transition and aggregation operators (k1 = 4 candidates):
    # Candidate 0: distractor ("elevated liver enzymes", ranked #1 by monoBERT, Table 3)
    # Candidate 1: true relevant ("low / reduced liver enzymes", ranked #2 by monoBERT)
    # Candidates 2, 3: weak non-relevant candidates
    mono_probs = [0.82, 0.78, 0.20, 0.10]
    pos_set = {1}
    neg_set = {0, 2, 3}
    l_mono = mono_bert_loss(mono_probs, pos_set, neg_set)
    assert l_mono > 0.0

    # Pairwise probabilities p_{i,j} = P(d_i > d_j | q) from duoBERT:
    # Candidate 1 beats every candidate (0, 2, 3) consistently (p_{1,j} in [0.85, 0.94]).
    # Candidate 0 loses to Candidate 1 (p_{0,1} = 0.12), beats 2 (0.80), and has one extreme score against 3 (0.98).
    p_mat: dict[tuple[int, int], float] = {
        (1, 0): 0.88, (0, 1): 0.12,
        (1, 2): 0.92, (2, 1): 0.08,
        (1, 3): 0.94, (3, 1): 0.06,
        (0, 2): 0.80, (2, 0): 0.20,
        (0, 3): 0.98, (3, 0): 0.02,
        (2, 3): 0.60, (3, 2): 0.40,
    }
    assert len(p_mat) == 4 * 3

    l_duo = duo_bert_loss(p_mat, pos_set, neg_set)
    assert 0.0 < l_duo < 0.6

    sum_scores = aggregate_duobert_scores(4, p_mat, "SUM")
    bin_scores = aggregate_duobert_scores(4, p_mat, "BINARY")
    min_scores = aggregate_duobert_scores(4, p_mat, "MIN")
    max_scores = aggregate_duobert_scores(4, p_mat, "MAX")

    # SUM, BINARY, and MIN all rank Candidate 1 (#1) above Candidate 0:
    assert sum_scores[1] > sum_scores[0]
    assert bin_scores[1] == 3.0 > bin_scores[0] == 2.0
    assert min_scores[1] == 0.88 > min_scores[0] == 0.12
    # In contrast, MAX is fooled by Candidate 0's single high score against weak Candidate 3 (0.98 > 0.94),
    # matching Section 5 (Tables 1-2) where duoBERT_MAX degrades ranking accuracy!
    assert max_scores[0] > max_scores[1]

    print(
        f"[PASS] DuoBERT boundaries verified: sum_1={sum_scores[1]:.2f} > sum_0={sum_scores[0]:.2f}, "
        f"bin_1={bin_scores[1]:.0f} > bin_0={bin_scores[0]:.0f}, max_0={max_scores[0]:.2f} > max_1={max_scores[1]:.2f}, "
        f"L_duo={l_duo:.4f}"
    )


if __name__ == "__main__":
    main()
