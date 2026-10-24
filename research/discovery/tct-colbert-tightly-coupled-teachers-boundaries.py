#!/usr/bin/env python3
"""Constructed boundary verification for TCT-ColBERT (Lin et al., 2020/2021, arXiv:2010.11386).

Verifies:
1. Late-interaction ColBERT MaxSim operator (Eq. 3) vs. average-pooled dot-product
   student bi-encoder PoolDot (Eq. 2).
2. Tightly-coupled in-batch knowledge distillation loss combining hard labels and
   temperature-scaled KL divergence over all in-batch passages D_B (Eqs. 5-6).
3. Min-score-substituted hybrid dense-sparse score combination over D_sp U D_ds (Eq. 7).
"""

from __future__ import annotations

import math


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def l2_normalize(vec: list[float]) -> list[float]:
    norm = math.sqrt(sum(x * x for x in vec))
    return [x / norm for x in vec]


def colbert_maxsim(q_tokens: list[list[float]], d_tokens: list[list[float]]) -> float:
    """Implements Eq. (3): sum_{i in |E_q|} max_{j in |E_d|} <eta_q(E_{q_i}), eta_d(E_{d_j})>."""
    q_norm = [l2_normalize(tok) for tok in q_tokens]
    d_norm = [l2_normalize(tok) for tok in d_tokens]
    return sum(max(dot(qi, dj) for dj in d_norm) for qi in q_norm)


def pool_dot(q_tokens: list[list[float]], d_tokens: list[list[float]]) -> float:
    """Implements Eq. (2) with PoolAvg over token embeddings."""
    dim = len(q_tokens[0])
    q_avg = [sum(tok[c] for tok in q_tokens) / len(q_tokens) for c in range(dim)]
    d_avg = [sum(tok[c] for tok in d_tokens) / len(d_tokens) for c in range(dim)]
    return dot(q_avg, d_avg)


def softmax_temp(scores: list[float], tau: float = 1.0) -> list[float]:
    scaled = [s / tau for s in scores]
    m = max(scaled)
    exps = [math.exp(x - m) for x in scaled]
    total = sum(exps)
    return [e / total for e in exps]


def tct_distillation_loss(
    student_scores_grid: list[list[float]],
    teacher_scores_grid: list[list[float]],
    pos_indices: list[int],
    tau: float = 0.25,
    gamma: float = 0.1,
) -> float:
    """Implements Eq. (6) over batch B and in-batch passage pool D_B."""
    total_loss = 0.0
    for q_idx, pos_d_idx in enumerate(pos_indices):
        p_student = softmax_temp(student_scores_grid[q_idx], tau=1.0)
        p_teacher = softmax_temp(teacher_scores_grid[q_idx], tau=tau)
        hard_ce = -math.log(p_student[pos_d_idx])
        # KL(P_hat || P) = sum_{d' in D_B} P_hat(d'|q_i) * log(P_hat(d'|q_i) / P(d'|q_i))
        kl_div = sum(
            pt * math.log(max(pt, 1e-12) / max(ps, 1e-12))
            for pt, ps in zip(p_teacher, p_student)
        )
        total_loss += gamma * hard_ce + (1.0 - gamma) * kl_div
    return total_loss


def hybrid_dense_sparse_scores(
    d_sp: dict[str, float],
    d_ds: dict[str, float],
    alpha: float = 0.24,
) -> dict[str, float]:
    """Implements Eq. (7): min-score-substituted hybrid linear combination over D_sp U D_ds."""
    min_sp = min(d_sp.values())
    min_ds = min(d_ds.values())
    all_docs = sorted(set(d_sp.keys()) | set(d_ds.keys()))
    combined: dict[str, float] = {}
    for d in all_docs:
        if d not in d_ds:
            combined[d] = alpha * d_sp[d] + min_ds
        elif d not in d_sp:
            combined[d] = alpha * min_sp + d_ds[d]
        else:
            combined[d] = alpha * d_sp[d] + d_ds[d]
    return combined


def main() -> None:
    # 1. Verify ColBERT MaxSim vs PoolDot and in-batch distillation (Batch size B = 2, |D_B| = 4)
    q0 = [[1.0, 0.2, 0.0], [0.1, 0.9, 0.1]]
    q1 = [[0.0, 0.2, 1.0], [0.2, 0.1, 0.9]]
    passages = [
        [[0.95, 0.15, 0.0], [0.1, 0.88, 0.05], [0.2, 0.1, 0.1]],   # d0+ (positive for q0)
        [[0.5, 0.4, 0.2], [0.3, 0.3, 0.3], [0.1, 0.2, 0.4]],       # d0- (BM25 neg for q0)
        [[0.05, 0.15, 0.95], [0.15, 0.1, 0.92], [0.1, 0.2, 0.2]],  # d1+ (positive for q1)
        [[0.2, 0.3, 0.4], [0.3, 0.4, 0.3], [0.4, 0.2, 0.2]],       # d1- (BM25 neg for q1)
    ]
    queries = [q0, q1]
    pos_indices = [0, 2]

    teacher_grid = [
        [colbert_maxsim(q, d) for d in passages]
        for q in queries
    ]
    student_grid = [
        [pool_dot(q, d) for d in passages]
        for q in queries
    ]
    # Teacher MaxSim assigns highest score to each query's positive passage:
    assert teacher_grid[0][0] == max(teacher_grid[0])
    assert teacher_grid[1][2] == max(teacher_grid[1])

    loss_before = tct_distillation_loss(
        student_grid, teacher_grid, pos_indices, tau=0.25, gamma=0.1
    )
    # Simulate student aligning closer to teacher logits after distillation step:
    aligned_student_grid = [
        [0.5 * s + 2.0 * t for s, t in zip(s_row, t_row)]
        for s_row, t_row in zip(student_grid, teacher_grid)
    ]
    loss_after = tct_distillation_loss(
        aligned_student_grid, teacher_grid, pos_indices, tau=0.25, gamma=0.1
    )
    assert loss_after < loss_before

    # 2. Verify Hybrid Dense-Sparse Ranking with minimum-score substitution (Eq. 7)
    d_sp = {"doc_both": 12.0, "doc_sparse_only": 14.5}
    d_ds = {"doc_both": 70.0, "doc_dense_only": 71.2}
    hybrid = hybrid_dense_sparse_scores(d_sp, d_ds, alpha=0.24)

    # Check exact Eq. (7) branches:
    assert abs(hybrid["doc_sparse_only"] - (0.24 * 14.5 + 70.0)) < 1e-9
    assert abs(hybrid["doc_dense_only"] - (0.24 * 12.0 + 71.2)) < 1e-9
    assert abs(hybrid["doc_both"] - (0.24 * 12.0 + 70.0)) < 1e-9

    print(
        f"[PASS] TCT-ColBERT boundaries verified: loss_before={loss_before:.4f} -> "
        f"loss_after={loss_after:.4f}, hybrid_scores={hybrid}"
    )


if __name__ == "__main__":
    main()
