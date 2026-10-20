#!/usr/bin/env python3
"""Constructed boundary verification for Round 667:
MoRA: High-Rank Updating for Parameter-Efficient Fine-Tuning
(Ting Jiang, Shaohan Huang, Shengyue Luo, Zihan Zhang, Haizhen Huang, Furu Wei,
Weiwei Deng, Feng Sun, Qi Zhang, Deqing Wang, & Fuzhen Zhuang, arXiv:2405.12130).

Verifies:
1. Square-matrix rank maximization under equal parameter budget (Section 4):
   For W_0 in R^{d x k} and LoRA rank r with (d+k)r parameters, MoRA uses a
   square matrix M in R^{r_hat x r_hat} with r_hat = floor(sqrt((d+k)r)),
   increasing maximum update rank from r to r_hat (e.g., from r=8 to r_hat=256
   when d=k=4096).
2. Lossless weight-merging equivalence (Equation 3):
   f_decomp(M f_comp(x)) == Delta_W x for all four operator designs:
   (a) Truncation/Padding (Equations 4-5),
   (b) Row and Column Sharing (Equations 6-7),
   (c) Decoupling / Reshaping (Equation 8), and
   (d) RoPE-inspired Rotation + Decoupling (Equations 9-11).
3. Expressive rank and rotational block differentiation:
   Verify that rank(Delta_W) = r_hat >> r for full-rank M, and that the
   RoPE-inspired rotation operator (Equations 9-11) produces distinct effective
   sub-blocks P^i = M R_i across input chunks while preserving chunk L2 norms.
"""

from __future__ import annotations
import math
import random


def matvec(W: list[list[float]], x: list[float]) -> list[float]:
    return [sum(W[i][j] * x[j] for j in range(len(x))) for i in range(len(W))]


def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    m, k, n = len(A), len(A[0]), len(B[0])
    return [
        [sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)]
        for i in range(m)
    ]


def vec_err(u: list[float], v: list[float]) -> float:
    return max(abs(a - b) for a, b in zip(u, v))


def matrix_rank(M: list[list[float]], tol: float = 1e-8) -> int:
    A = [list(row) for row in M]
    rows, cols = len(A), len(A[0])
    rank = 0
    for c in range(cols):
        if rank >= rows:
            break
        piv = max(range(rank, rows), key=lambda r: abs(A[r][c]))
        if abs(A[piv][c]) <= tol:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        pv = A[rank][c]
        for j in range(c, cols):
            A[rank][j] /= pv
        for r in range(rows):
            if r != rank and abs(A[r][c]) > tol:
                f = A[r][c]
                for j in range(c, cols):
                    A[r][j] -= f * A[rank][j]
        rank += 1
    return rank


def rotation_block_matrix(r_hat: int, chunk_idx: int) -> list[list[float]]:
    """Construct r_hat x r_hat block-diagonal rotation matrix R_i (Equations 10-11)."""
    R = [[0.0] * r_hat for _ in range(r_hat)]
    for j in range(1, r_hat // 2 + 1):
        theta_j = 10000.0 ** (-2.0 * (j - 1) / r_hat)
        ang = chunk_idx * theta_j
        c_val, s_val = math.cos(ang), math.sin(ang)
        idx = 2 * (j - 1)
        R[idx][idx] = c_val
        R[idx][idx + 1] = -s_val
        R[idx + 1][idx] = s_val
        R[idx + 1][idx + 1] = c_val
    return R


def main() -> None:
    rng = random.Random(20240520)

    # 1. Verify rank amplification formula r_hat = floor(sqrt((d + k) * r))
    d_llm, k_llm, r_llm = 4096, 4096, 8
    r_hat_llm = int(math.isqrt((d_llm + k_llm) * r_llm))
    assert r_hat_llm == 256
    assert r_hat_llm * r_hat_llm == (d_llm + k_llm) * r_llm

    # Small synthetic verification: d = k = 8, LoRA rank r = 1 -> params = 16 -> r_hat = 4
    d, k, r = 8, 8, 1
    r_hat = int(math.isqrt((d + k) * r))
    assert r_hat == 4
    M = [[rng.gauss(0.0, 1.0) for _ in range(r_hat)] for _ in range(r_hat)]
    x = [rng.gauss(0.0, 1.0) for _ in range(k)]

    # 2(a). Equations (4)-(5): Truncation / zero-padding
    f_comp_trunc = x[:r_hat]
    y_trunc_op = matvec(M, f_comp_trunc) + [0.0] * (d - r_hat)
    DW_trunc = [
        [M[i][j] if (i < r_hat and j < r_hat) else 0.0 for j in range(k)]
        for i in range(d)
    ]
    y_trunc_merged = matvec(DW_trunc, x)
    assert vec_err(y_trunc_op, y_trunc_merged) < 1e-12

    # 2(b). Equations (6)-(7): Sharing rows and columns (grouping adjacent k/r_hat columns/rows)
    group_size = k // r_hat  # 2
    f_comp_share = [
        sum(x[i * group_size + m_idx] for m_idx in range(group_size))
        for i in range(r_hat)
    ]
    z_share = matvec(M, f_comp_share)
    y_share_op = [z_share[i // group_size] for i in range(d)]
    DW_share = [
        [M[i // group_size][j // group_size] for j in range(k)]
        for i in range(d)
    ]
    y_share_merged = matvec(DW_share, x)
    assert vec_err(y_share_op, y_share_merged) < 1e-12
    assert matrix_rank(DW_share) == r_hat

    # 2(c). Equation (8): Decoupling / reshaping x into n = k // r_hat chunks of length r_hat
    n_chunks = k // r_hat  # 2
    chunks = [x[c_idx * r_hat : (c_idx + 1) * r_hat] for c_idx in range(n_chunks)]
    y_decouple_op = []
    for ch in chunks:
        y_decouple_op.extend(matvec(M, ch))
    DW_decouple = [[0.0] * k for _ in range(d)]
    for c_idx in range(n_chunks):
        base = c_idx * r_hat
        for i in range(r_hat):
            for j in range(r_hat):
                DW_decouple[base + i][base + j] = M[i][j]
    y_decouple_merged = matvec(DW_decouple, x)
    assert vec_err(y_decouple_op, y_decouple_merged) < 1e-12
    assert matrix_rank(DW_decouple) == n_chunks * r_hat  # Full rank 8!

    # 2(d). Equations (9)-(11): Rotation + Decoupling
    y_rot_op = []
    DW_rot = [[0.0] * k for _ in range(d)]
    P_blocks = []
    for c_idx in range(n_chunks):
        R_i = rotation_block_matrix(r_hat, c_idx)
        ch = chunks[c_idx]
        a_i = matvec(R_i, ch)
        # Verify rotation preserves chunk Euclidean norm
        norm_ch = math.sqrt(sum(v * v for v in ch))
        norm_ai = math.sqrt(sum(v * v for v in a_i))
        assert abs(norm_ch - norm_ai) < 1e-12
        y_rot_op.extend(matvec(M, a_i))

        P_i = matmul(M, R_i)
        P_blocks.append(P_i)
        base = c_idx * r_hat
        for i in range(r_hat):
            for j in range(r_hat):
                DW_rot[base + i][base + j] = P_i[i][j]

    y_rot_merged = matvec(DW_rot, x)
    merge_rot_err = vec_err(y_rot_op, y_rot_merged)
    assert merge_rot_err < 1e-12
    # Verify P^0 != P^1 (rotation differentiates chunk 0 from chunk 1)
    block_diff = max(
        abs(P_blocks[0][i][j] - P_blocks[1][i][j])
        for i in range(r_hat)
        for j in range(r_hat)
    )
    assert block_diff > 0.1
    rank_mora_rot = matrix_rank(DW_rot)
    assert rank_mora_rot == d  # Rank 8 vs LoRA rank 1

    print(
        f"[PASS] Round 667 MoRA (Jiang et al. 2024): "
        f"r_hat_4096={r_hat_llm} (vs r=8), merge_rot_err={merge_rot_err:.2e}, "
        f"rank_share={matrix_rank(DW_share)}, rank_rot={rank_mora_rot}>>r={r}"
    )


if __name__ == "__main__":
    main()
