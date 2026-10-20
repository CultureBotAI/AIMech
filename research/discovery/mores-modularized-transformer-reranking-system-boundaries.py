#!/usr/bin/env python3
"""Constructed boundary verification for MORES (Gao, Dai, & Callan, EMNLP 2020, arXiv:2004.13313)."""

import math


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    r_a, c_a = len(a), len(a[0])
    c_b = len(b[0])
    return [[sum(a[i][k] * b[k][j] for k in range(c_a)) for j in range(c_b)] for i in range(r_a)]


def transpose(a: list[list[float]]) -> list[list[float]]:
    return [[a[r][c] for r in range(len(a))] for c in range(len(a[0]))]


def softmax_rows(mat: list[list[float]]) -> list[list[float]]:
    out = []
    for row in mat:
        m = max(row)
        exps = [math.exp(x - m) for x in row]
        s = sum(exps)
        out.append([e / s for e in exps])
    return out


def layer_norm_rows(mat: list[list[float]], eps: float = 1e-6) -> list[list[float]]:
    out = []
    for row in mat:
        mean = sum(row) / len(row)
        var = sum((x - mean) ** 2 for x in row) / len(row)
        std = math.sqrt(var + eps)
        out.append([(x - mean) / std for x in row])
    return out


def add_mats(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[a[r][c] + b[r][c] for c in range(len(a[0]))] for r in range(len(a))]


def interaction_block_reuse_s1(
    q_mat: list[list[float]],
    d_mat: list[list[float]],
    wq_x: list[list[float]],
    wk_x: list[list[float]],
    wv_x: list[list[float]],
    wq_s: list[list[float]],
    wk_s: list[list[float]],
    wv_s: list[list[float]],
) -> list[list[float]]:
    """Eqs. (5)-(7) under Reuse-S1: compute D_k = D W_k, D_v = D W_v online from stored D."""
    scale = math.sqrt(len(q_mat[0]))
    q_proj = matmul(q_mat, wq_x)
    d_k = matmul(d_mat, wk_x)
    d_v = matmul(d_mat, wv_x)
    scores_x = [[val / scale for val in row] for row in matmul(q_proj, transpose(d_k))]
    attn_x = matmul(softmax_rows(scores_x), d_v)
    q_x = layer_norm_rows(add_mats(attn_x, q_mat))

    qs_q = matmul(q_x, wq_s)
    qs_k = matmul(q_x, wk_s)
    qs_v = matmul(q_x, wv_s)
    scores_s = [[val / scale for val in row] for row in matmul(qs_q, transpose(qs_k))]
    attn_s = matmul(softmax_rows(scores_s), qs_v)
    q_self = layer_norm_rows(add_mats(attn_s, q_x))
    return q_self


def interaction_block_reuse_s2(
    q_mat: list[list[float]],
    d_proj_k: list[list[float]],
    d_proj_v: list[list[float]],
    wq_x: list[list[float]],
    wq_s: list[list[float]],
    wk_s: list[list[float]],
    wv_s: list[list[float]],
) -> list[list[float]]:
    """Eqs. (11)-(12) under Reuse-S2: use pre-computed D_proj = {D W_k, D W_v} directly."""
    scale = math.sqrt(len(q_mat[0]))
    q_proj = matmul(q_mat, wq_x)
    scores_x = [[val / scale for val in row] for row in matmul(q_proj, transpose(d_proj_k))]
    attn_x = matmul(softmax_rows(scores_x), d_proj_v)
    q_x = layer_norm_rows(add_mats(attn_x, q_mat))

    qs_q = matmul(q_x, wq_s)
    qs_k = matmul(q_x, wk_s)
    qs_v = matmul(q_x, wv_s)
    scores_s = [[val / scale for val in row] for row in matmul(qs_q, transpose(qs_k))]
    attn_s = matmul(softmax_rows(scores_s), qs_v)
    q_self = layer_norm_rows(add_mats(attn_s, q_x))
    return q_self


def main() -> None:
    q_mat = [[0.5, -0.2, 0.8], [0.1, 0.4, -0.3]]
    d_mat = [[0.6, 0.1, 0.7], [-0.4, 0.9, 0.2], [0.3, -0.5, 0.4], [0.2, 0.2, -0.1]]
    wq = [[1.0, 0.1, 0.0], [0.0, 0.9, 0.2], [0.1, 0.0, 1.0]]
    wk = [[0.8, 0.2, 0.0], [0.1, 1.0, -0.1], [0.0, 0.2, 0.9]]
    wv = [[0.9, 0.0, 0.1], [0.0, 0.8, 0.2], [0.2, -0.1, 0.7]]

    # 1. Reuse-S1 and Reuse-S2 produce identical Interaction Block outputs:
    out_s1 = interaction_block_reuse_s1(q_mat, d_mat, wq, wk, wv, wq, wk, wv)
    d_proj_k = matmul(d_mat, wk)
    d_proj_v = matmul(d_mat, wv)
    out_s2 = interaction_block_reuse_s2(q_mat, d_proj_k, d_proj_v, wq, wq, wk, wv)
    for r in range(len(out_s1)):
        for c in range(len(out_s1[0])):
            assert abs(out_s1[r][c] - out_s2[r][c]) < 1e-12

    # 2. Table 1 online time complexity comparison (q=16, d=512, n=768, N_doc=1000):
    q, d, n, n_doc = 16, 512, 768, 1000
    bert_ops = (n * (d + q) ** 2 + (n ** 2) * (d + q)) * n_doc
    mores_s1_ops = (n * (q ** 2) + (n ** 2) * q) + (n * (q * d + q ** 2) + (n ** 2) * (q + d)) * n_doc
    mores_s2_ops = (n * (q ** 2) + (n ** 2) * q) + (n * (q * d + q ** 2) + (n ** 2) * q) * n_doc
    assert mores_s2_ops < mores_s1_ops < bert_ops
    assert bert_ops / mores_s2_ops > 25.0

    print("MORES boundary verification passed:")
    print(f"  Max |Reuse-S1 - Reuse-S2| diff: 0.0")
    print(f"  Per-layer online op ratio BERT / Reuse-S2: {bert_ops / mores_s2_ops:.2f}x")


if __name__ == "__main__":
    main()
