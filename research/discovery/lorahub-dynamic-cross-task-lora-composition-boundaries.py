#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 681: LoraHub (Huang et al., COLM 2024 / arXiv:2307.13269)."""

from __future__ import annotations

import math
import random


def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    m, r, k = len(A), len(A[0]), len(B[0])
    out = [[0.0] * k for _ in range(m)]
    for i in range(m):
        for p in range(r):
            aip = A[i][p]
            for j in range(k):
                out[i][j] += aip * B[p][j]
    return out


def mat_add(M1: list[list[float]], M2: list[list[float]], scale2: float = 1.0) -> list[list[float]]:
    return [[M1[i][j] + scale2 * M2[i][j] for j in range(len(M1[0]))] for i in range(len(M1))]


def frob_sq(M: list[list[float]]) -> float:
    return sum(val * val for row in M for val in row)


def compose_lorahub(
    A_list: list[list[list[float]]],
    B_list: list[list[list[float]]],
    w: list[float],
) -> tuple[list[list[float]], list[list[float]], list[list[float]]]:
    """LoraHub Eq. 1: m_hat = (sum_i w_i A_i)(sum_i w_i B_i)."""
    d, r = len(A_list[0]), len(A_list[0][0])
    k = len(B_list[0][0])
    A_hat = [[0.0] * r for _ in range(d)]
    B_hat = [[0.0] * k for _ in range(r)]
    for idx, wi in enumerate(w):
        for i in range(d):
            for p in range(r):
                A_hat[i][p] += wi * A_list[idx][i][p]
        for p in range(r):
            for j in range(k):
                B_hat[p][j] += wi * B_list[idx][p][j]
    return A_hat, B_hat, matmul(A_hat, B_hat)


def main() -> None:
    rng = random.Random(681)
    N = 5  # N upstream LoRA modules
    d, k, r = 10, 10, 2

    A_list = [[[rng.gauss(0.0, 0.5) for _ in range(r)] for _ in range(d)] for _ in range(N)]
    B_list = [[[rng.gauss(0.0, 0.5) for _ in range(k)] for _ in range(r)] for _ in range(N)]

    # 1. Verify Eq. 1 bilinear expansion identity:
    # (sum_i w_i A_i)(sum_j w_j B_j) == sum_i w_i^2 A_i B_i + sum_{i != j} w_i w_j A_i B_j
    w_test = [0.7, -0.4, 0.0, 0.9, -0.25]
    A_hat, B_hat, m_hat = compose_lorahub(A_list, B_list, w_test)
    assert len(A_hat) == d and len(A_hat[0]) == r
    assert len(B_hat) == r and len(B_hat[0]) == k

    expanded = [[0.0] * k for _ in range(d)]
    for i in range(N):
        for j in range(N):
            prod_ij = matmul(A_list[i], B_list[j])
            expanded = mat_add(expanded, prod_ij, w_test[i] * w_test[j])

    bilinear_err = math.sqrt(frob_sq(mat_add(m_hat, expanded, -1.0)))
    assert bilinear_err < 1e-14, f"Bilinear expansion mismatch: {bilinear_err}"

    # 2. Verify ADAPT stage (Section 3.4): gradient-free evolution strategy optimization
    # over w in [-1.5, 1.5]^N with L1 regularization L(w) + alpha * sum_i |w_i|
    # Construct an unseen target task whose ideal adapter is formed from modules 1 and 3
    w_true = [0.0, 0.85, 0.0, -0.60, 0.0]
    _, _, target_delta_W = compose_lorahub(A_list, B_list, w_true)
    alpha = 0.02

    def objective(w_cand: list[float]) -> float:
        _, _, m_cand = compose_lorahub(A_list, B_list, w_cand)
        loss_q = frob_sq(mat_add(m_cand, target_delta_W, -1.0))
        l1_pen = alpha * sum(abs(wi) for wi in w_cand)
        return loss_q + l1_pen

    # Baseline 1: Zero-shot (w = 0)
    loss_zeroshot = frob_sq(target_delta_W)
    # Baseline 2: Single-module LoRA Retrieval (Table 2 baseline: best single module i)
    single_losses = []
    for i in range(N):
        w_one = [1.0 if j == i else 0.0 for j in range(N)]
        _, _, m_one = compose_lorahub(A_list, B_list, w_one)
        single_losses.append(frob_sq(mat_add(m_one, target_delta_W, -1.0)))
    loss_retrieval = min(single_losses)

    # Gradient-free Evolutionary Search (Section 3.4 / Appendix G: K=40 steps, |w_i| <= 1.5)
    mean = [0.0] * N
    sigma = 0.5
    pop_size = 32
    elite_size = 8
    for _step in range(40):
        candidates = []
        for _ in range(pop_size):
            cand = [max(-1.5, min(1.5, mean[j] + rng.gauss(0.0, sigma))) for j in range(N)]
            candidates.append((objective(cand), cand))
        candidates.sort(key=lambda pair: pair[0])
        elites = [pair[1] for pair in candidates[:elite_size]]
        mean = [sum(el[j] for el in elites) / elite_size for j in range(N)]
        sigma *= 0.92

    _, _, m_opt = compose_lorahub(A_list, B_list, mean)
    loss_lorahub = frob_sq(mat_add(m_opt, target_delta_W, -1.0))

    assert loss_lorahub < 0.05 * loss_retrieval
    assert loss_lorahub < 0.02 * loss_zeroshot

    print(
        f"[PASS] Round 681 LoraHub (Huang et al., COLM 2024): "
        f"bilinear_err={bilinear_err:.2e}, loss_zeroshot={loss_zeroshot:.4f} -> "
        f"loss_retrieval={loss_retrieval:.4f} -> loss_lorahub={loss_lorahub:.4f}"
    )


if __name__ == "__main__":
    main()
