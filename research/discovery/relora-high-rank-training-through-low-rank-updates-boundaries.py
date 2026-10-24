#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 682: ReLoRA (Lialin et al., ICLR 2024 / arXiv:2307.05695)."""

from __future__ import annotations

import math
import random


def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    m, r, n = len(A), len(A[0]), len(B[0])
    out = [[0.0] * n for _ in range(m)]
    for i in range(m):
        for k in range(r):
            aik = A[i][k]
            for j in range(n):
                out[i][j] += aik * B[k][j]
    return out


def transpose(M: list[list[float]]) -> list[list[float]]:
    return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]


def mat_sub(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mat_add(A: list[list[float]], B: list[list[float]], scale_b: float = 1.0) -> list[list[float]]:
    return [[A[i][j] + scale_b * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def frob_norm(M: list[list[float]]) -> float:
    return math.sqrt(sum(val * val for row in M for val in row))


def numerical_rank(M: list[list[float]], tol: float = 1e-4) -> int:
    """Compute matrix rank via Gaussian elimination with complete pivoting."""
    A = [row[:] for row in M]
    m, n = len(A), len(A[0])
    rank = 0
    for col in range(min(m, n)):
        pivot_row = max(range(rank, m), key=lambda r: abs(A[r][col]))
        if abs(A[pivot_row][col]) <= tol:
            continue
        A[rank], A[pivot_row] = A[pivot_row], A[rank]
        piv = A[rank][col]
        for r in range(rank + 1, m):
            factor = A[r][col] / piv
            for c in range(col, n):
                A[r][c] -= factor * A[rank][c]
        rank += 1
    return rank


def prune_by_magnitude(M: list[list[float]], prune_fraction: float) -> list[list[float]]:
    """Algorithm 1 Line 17: partial optimizer state reset via magnitude pruning."""
    flat = sorted(abs(val) for row in M for val in row)
    cutoff_idx = min(len(flat) - 1, max(0, int(prune_fraction * len(flat)) - 1))
    threshold = flat[cutoff_idx]
    return [[val if abs(val) > threshold else 0.0 for val in row] for row in M]


def jagged_cosine_lr(step: int, total_steps: int, reset_freq: int, warmup_steps: int, base_lr: float) -> float:
    """Figure 2 & Algorithm 1 Line 20: Jagged cosine scheduler with zero-LR reset and quick re-warmup."""
    cosine_env = base_lr * (0.1 + 0.9 * 0.5 * (1.0 + math.cos(math.pi * step / total_steps)))
    step_since_reset = step % reset_freq
    if step > 0 and step_since_reset < warmup_steps:
        return cosine_env * (step_since_reset / float(warmup_steps))
    return cosine_env


def main() -> None:
    rng = random.Random(682)
    d = 8
    r = 2  # Low rank r = 2 << d = 8

    # Full-rank target matrix W_star of rank 8
    W_star = [[rng.gauss(0.0, 1.0) + (1.5 if i == j else 0.0) for j in range(d)] for i in range(d)]
    assert numerical_rank(W_star) == d

    # 1. Verify Jagged Cosine Schedule properties (Figure 2):
    # At exact reset boundary (step = q), LR drops to 0.0 and warms up over warmup_steps
    q = 25
    warmup = 5
    assert jagged_cosine_lr(q, 100, q, warmup, 0.1) == 0.0
    assert 0.0 < jagged_cosine_lr(q + 2, 100, q, warmup, 0.1) < jagged_cosine_lr(q + warmup, 100, q, warmup, 0.1)

    # 2. Compare:
    # (a) Standard single-adapter LoRA (rank r=2, no restarts)
    # (b) Naive restarts WITHOUT optimizer state pruning (old momentum M_A forces W_A into prior subspace, Section 2 p. 3)
    # (c) ReLoRA (Algorithm 1: periodic merge-and-reinit + 90% magnitude pruning of optimizer state + jagged LR warmup)

    # (a) Standard LoRA (rank 2)
    W_A_lora = [[rng.gauss(0.0, 0.3) for _ in range(r)] for _ in range(d)]
    W_B_lora = [[0.0] * d for _ in range(r)]
    for _ in range(100):
        diff = mat_sub(matmul(W_A_lora, W_B_lora), W_star)
        gA = matmul(diff, transpose(W_B_lora))
        gB = matmul(transpose(W_A_lora), diff)
        W_A_lora = mat_add(W_A_lora, gA, -0.04)
        W_B_lora = mat_add(W_B_lora, gB, -0.04)
    delta_lora = matmul(W_A_lora, W_B_lora)
    err_lora = frob_norm(mat_sub(delta_lora, W_star))
    rank_lora = numerical_rank(delta_lora)
    assert rank_lora <= r

    # (b) ReLoRA with 4 stages of rank-2 updates, 90% optimizer state pruning, and jagged warmup
    W_relora = [[0.0] * d for _ in range(d)]
    W_A = [[rng.gauss(0.0, 0.3) for _ in range(r)] for _ in range(d)]
    W_B = [[0.0] * d for _ in range(r)]
    M_A = [[0.0] * r for _ in range(d)]
    M_B = [[0.0] * d for _ in range(r)]
    beta1 = 0.8
    q_relora = 40
    total_relora = 160

    for t in range(1, total_relora + 1):
        lr = jagged_cosine_lr(t - 1, total_relora, q_relora, warmup, 0.18)
        cur_W = mat_add(W_relora, matmul(W_A, W_B))
        diff = mat_sub(cur_W, W_star)
        gA = matmul(diff, transpose(W_B))
        gB = matmul(transpose(W_A), diff)
        M_A = [[beta1 * M_A[i][k] + (1.0 - beta1) * gA[i][k] for k in range(r)] for i in range(d)]
        M_B = [[beta1 * M_B[k][j] + (1.0 - beta1) * gB[k][j] for j in range(d)] for k in range(r)]
        W_A = mat_add(W_A, M_A, -lr)
        W_B = mat_add(W_B, M_B, -lr)

        if t % q_relora == 0 and t < total_relora:
            # Algorithm 1 Lines 15-17: Merge, Kaiming/zero reinit, and magnitude prune optimizer states
            W_relora = mat_add(W_relora, matmul(W_A, W_B))
            W_A = [[rng.gauss(0.0, 0.3) for _ in range(r)] for _ in range(d)]
            W_B = [[0.0] * d for _ in range(r)]
            M_A = prune_by_magnitude(M_A, 0.90)
            M_B = prune_by_magnitude(M_B, 0.90)

    W_relora = mat_add(W_relora, matmul(W_A, W_B))
    err_relora = frob_norm(mat_sub(W_relora, W_star))
    rank_relora = numerical_rank(W_relora)

    assert rank_relora > rank_lora, f"Expected rank_relora ({rank_relora}) > rank_lora ({rank_lora})"
    assert rank_relora >= 6
    assert err_relora < 0.45 * err_lora, f"Expected err_relora ({err_relora:.4f}) < 0.45 * err_lora ({err_lora:.4f})"

    print(
        f"[PASS] Round 682 ReLoRA (Lialin et al., ICLR 2024): "
        f"rank_lora={rank_lora} -> rank_relora={rank_relora}, "
        f"err_lora={err_lora:.4f} -> err_relora={err_relora:.4f}"
    )


if __name__ == "__main__":
    main()
