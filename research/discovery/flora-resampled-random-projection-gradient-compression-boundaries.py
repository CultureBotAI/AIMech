#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 684: Flora (Hao, Cao, & Mou, ICML 2024 / arXiv:2402.03293)."""

from __future__ import annotations

import math
import random


def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    m, k, n = len(A), len(A[0]), len(B[0])
    out = [[0.0] * n for _ in range(m)]
    for i in range(m):
        for r in range(k):
            air = A[i][r]
            for j in range(n):
                out[i][j] += air * B[r][j]
    return out


def transpose(M: list[list[float]]) -> list[list[float]]:
    return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]


def mat_add(A: list[list[float]], B: list[list[float]], scale_b: float = 1.0) -> list[list[float]]:
    return [[A[i][j] + scale_b * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def frob_norm(M: list[list[float]]) -> float:
    return math.sqrt(sum(val * val for row in M for val in row))


def numerical_rank(M: list[list[float]], tol: float = 1e-4) -> int:
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


def sample_proj(seed: int, r: int, m: int) -> list[list[float]]:
    """Sample A_W ~ N_{seed}(0, 1/r) in R^{r x m} on the fly from seed."""
    gen = random.Random(seed)
    std = 1.0 / math.sqrt(r)
    return [[gen.gauss(0.0, std) for _ in range(m)] for _ in range(r)]


def main() -> None:
    rng = random.Random(684)
    n, m, r = 8, 8, 2

    # 1. Verify Theorem 2.1 & Lemma A.1 exact LoRA SGD dynamics:
    # A_T = A_0 + eta * A_0 * f_A(T), B_T = eta * f_B(T) * A_0^T
    # and ||f_A(t)||_F <= eta * L^2 * (1 - (eta^2 L^2)^t) / (1 - eta^2 L^2)
    eta = 0.02
    T_steps = 6
    A0 = sample_proj(1001, r, m)
    B0 = [[0.0] * r for _ in range(n)]
    grads = [[[rng.gauss(0.0, 0.15) for _ in range(m)] for _ in range(n)] for _ in range(T_steps)]

    sum_grads = [[0.0] * m for _ in range(n)]
    L_bound = 0.0
    for g in grads:
        sum_grads = mat_add(sum_grads, g, 1.0)
        L_bound = max(L_bound, frob_norm(g) * T_steps)

    # Simulate exact SGD on (A_t, B_t) (Eq. 5-6)
    A_t = [row[:] for row in A0]
    B_t = [row[:] for row in B0]
    # Simulate Lemma A.1 recurrence (Eq. 25-26)
    f_A = [[0.0] * m for _ in range(m)]
    f_B = [[0.0] * m for _ in range(n)]
    I_m = [[1.0 if i == j else 0.0 for j in range(m)] for i in range(m)]

    for t in range(T_steps):
        G_t = grads[t]
        A_next = mat_add(A_t, matmul(transpose(B_t), G_t), -eta)
        B_next = mat_add(B_t, matmul(G_t, transpose(A_t)), -eta)
        A_t, B_t = A_next, B_next

        # Lemma A.1 update:
        # f_A(t+1) = f_A(t) - eta * f_B(t)^T * G_t
        # f_B(t+1) = f_B(t) - G_t * (eta * f_A(t)^T + I)
        f_A_next = mat_add(f_A, matmul(transpose(f_B), G_t), -eta)
        eta_fA_T_plus_I = mat_add(I_m, transpose(f_A), eta)
        f_B_next = mat_add(f_B, matmul(G_t, eta_fA_T_plus_I), -1.0)
        f_A, f_B = f_A_next, f_B_next

        # Verify Theorem 2.1 bound
        num = eta * (L_bound ** 2) * (1.0 - ((eta * L_bound) ** 2) ** (t + 1))
        den = 1.0 - (eta * L_bound) ** 2
        assert frob_norm(f_A) <= (num / den) + 1e-12

    A_thm = mat_add(A0, matmul(A0, f_A), eta)
    B_thm = [[eta * val for val in row] for row in matmul(f_B, transpose(A0))]
    thm21_err_A = frob_norm(mat_add(A_t, A_thm, -1.0))
    thm21_err_B = frob_norm(mat_add(B_t, B_thm, -1.0))
    assert thm21_err_A < 1e-14 and thm21_err_B < 1e-14

    # 2. Verify Algorithm 2 (Momentum with Flora):
    # Sublinear state M_{t,W} in R^{n x r}, resampled projection A'_W every kappa steps,
    # momentum subspace transfer M' <- M_{t,W} A_{t,W} (A'_W)^T, and full-rank weight update
    W_star = [[rng.gauss(0.0, 1.0) + (1.5 if i == j else 0.0) for j in range(m)] for i in range(n)]
    W_flora = [[0.0] * m for _ in range(n)]
    M_state = [[0.0] * r for _ in range(n)]  # Sublinear O(nr) instead of O(nm)
    seed_t = 5000
    beta = 0.8
    kappa = 10
    lr_flora = 0.08

    for t in range(180):
        G_t = mat_add(W_flora, W_star, -1.0)
        A_t_proj = sample_proj(seed_t, r, m)
        if t > 0 and t % kappa == 0:
            seed_next = seed_t + 1
            A_prime = sample_proj(seed_next, r, m)
            # Algorithm 2 Line 13: Transfer compressed momentum M' <- M_{t,W} A_{t,W} (A'_W)^T
            M_prime = matmul(matmul(M_state, A_t_proj), transpose(A_prime))
            seed_t = seed_next
        else:
            A_prime = A_t_proj
            M_prime = M_state

        # Algorithm 2 Line 18: M_{t+1,W} <- beta M' + (1 - beta) G_{t,W} (A'_W)^T
        compressed_grad = matmul(G_t, transpose(A_prime))
        M_state = [
            [beta * M_prime[i][k] + (1.0 - beta) * compressed_grad[i][k] for k in range(r)]
            for i in range(n)
        ]
        # Algorithm 2 Line 20: Decompress update M_{t+1,W} A'_W
        decompressed_step = matmul(M_state, A_prime)
        W_flora = mat_add(W_flora, decompressed_step, -lr_flora)

    rank_flora = numerical_rank(W_flora)
    err_flora = frob_norm(mat_add(W_flora, W_star, -1.0))

    # Compare against fixed-projection RP (kappa = infinity, never resampling A)
    W_fixed = [[0.0] * m for _ in range(n)]
    M_fixed = [[0.0] * r for _ in range(n)]
    A_fixed = sample_proj(5000, r, m)
    for _t in range(180):
        G_t = mat_add(W_fixed, W_star, -1.0)
        c_grad = matmul(G_t, transpose(A_fixed))
        M_fixed = [[beta * M_fixed[i][k] + (1.0 - beta) * c_grad[i][k] for k in range(r)] for i in range(n)]
        W_fixed = mat_add(W_fixed, matmul(M_fixed, A_fixed), -lr_flora)

    rank_fixed = numerical_rank(W_fixed)
    err_fixed = frob_norm(mat_add(W_fixed, W_star, -1.0))

    assert rank_fixed <= r
    assert rank_flora == n > rank_fixed
    assert err_flora < 0.25 * err_fixed

    print(
        f"[PASS] Round 684 Flora (Hao et al., ICML 2024): "
        f"thm21_err=({thm21_err_A:.2e},{thm21_err_B:.2e}), "
        f"rank_fixed={rank_fixed}->rank_flora={rank_flora}, "
        f"err_fixed={err_fixed:.4f}->err_flora={err_flora:.4f}"
    )


if __name__ == "__main__":
    main()
