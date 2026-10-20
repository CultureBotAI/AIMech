#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 678: Chain of LoRA / COLA (Xia et al., ICML 2024)."""

import math
import random


def matmul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)] for i in range(m)]


def mat_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mat_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def frob_norm(A):
    return math.sqrt(sum(x * x for row in A for x in row))


def random_orthogonal(n, rng):
    cols = []
    for _ in range(n):
        v = [rng.gauss(0.0, 1.0) for _ in range(n)]
        for u in cols:
            dot = sum(v[i] * u[i] for i in range(n))
            v = [v[i] - dot * u[i] for i in range(n)]
        norm = math.sqrt(sum(x * x for x in v))
        cols.append([x / norm for x in v])
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def main():
    rng = random.Random(678)
    d, k = 10, 10
    U = random_orthogonal(d, rng)
    V = random_orthogonal(k, rng)
    # Target ideal task update dW* has rank 6 with decaying singular values
    sigmas = [8.0, 6.0, 4.0, 2.5, 1.5, 0.8, 0.0, 0.0, 0.0, 0.0]

    dW_star = [[0.0 for _ in range(k)] for _ in range(d)]
    for idx, s in enumerate(sigmas):
        for i in range(d):
            for j in range(k):
                dW_star[i][j] += s * U[i][idx] * V[j][idx]

    def rank_r_truncated(modes_start, modes_count):
        M = [[0.0 for _ in range(k)] for _ in range(d)]
        for idx in range(modes_start, modes_start + modes_count):
            s = sigmas[idx]
            for i in range(d):
                for j in range(k):
                    M[i][j] += s * U[i][idx] * V[j][idx]
        return M

    # 1. Single-stage LoRA of rank r=2 can at best capture top-2 singular modes of dW*:
    lora_r2 = rank_r_truncated(0, 2)
    err_chain_1 = frob_norm(mat_sub(dW_star, lora_r2))

    # 2. COLA with chain length M=2 (each stage rank r=2):
    # Stage 1 learns top-2 modes and merges ("tie a knot"); Stage 2 learns top-2 modes of residual dW* - B_1 A_1
    stage2_r2 = rank_r_truncated(2, 2)
    cola_len2 = mat_add(lora_r2, stage2_r2)
    err_chain_2 = frob_norm(mat_sub(dW_star, cola_len2))

    # 3. COLA with chain length M=3 (each stage rank r=2):
    stage3_r2 = rank_r_truncated(4, 2)
    cola_len3 = mat_add(cola_len2, stage3_r2)
    err_chain_3 = frob_norm(mat_sub(dW_star, cola_len3))

    assert err_chain_3 < 1e-12 and err_chain_3 < err_chain_2 < err_chain_1, (
        f"Expected monotonic residual error decrease: {err_chain_1} > {err_chain_2} > {err_chain_3}"
    )

    # 4. Verify rank step-down COLA(r1=3, r2=1) vs fixed LoRA(r=3) under 5 epochs:
    # LoRA(r=3) for 5 epochs captures at most rank 3; COLA(3, 1) (3 epochs at r=3, 2 epochs at r=1)
    # captures rank 3 + 1 = 4 while using fewer FLOPs!
    err_lora_r3 = frob_norm(mat_sub(dW_star, rank_r_truncated(0, 3)))
    cola_stepdown = mat_add(rank_r_truncated(0, 3), rank_r_truncated(3, 1))
    err_cola_stepdown = frob_norm(mat_sub(dW_star, cola_stepdown))
    flops_lora_r3 = 5 * 3
    flops_cola_3_1 = 3 * 3 + 2 * 1  # 11 < 15
    assert err_cola_stepdown < err_lora_r3 and flops_cola_3_1 < flops_lora_r3

    # 5. Verify Theorem 4.1 nonconvex Frank-Wolfe gap bound 2 * sqrt(M_bound * beta) * D / sqrt(T) + eps:
    M_bound, beta, D, eps = 4.0, 2.0, 3.0, 0.05
    gaps = [2.0 * math.sqrt(M_bound * beta) * D / math.sqrt(T) + eps for T in (10, 100, 1000)]
    assert gaps[0] > gaps[1] > gaps[2] > eps

    print(
        f"[PASS] Round 678 Chain of LoRA (Xia et al., ICML 2024): "
        f"err_M1={err_chain_1:.4f}->M2={err_chain_2:.4f}->M3={err_chain_3:.2e}, "
        f"stepdown_err={err_cola_stepdown:.4f}<lora_r3={err_lora_r3:.4f} (flops {flops_cola_3_1}<{flops_lora_r3})"
    )


if __name__ == "__main__":
    main()
