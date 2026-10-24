#!/usr/bin/env python3
"""Constructed boundary verification for Conformer-Kernel with QTI (Mitra et al., 2020, arXiv:2007.10434)."""

import math


def softmax_vec(vec: list[float]) -> list[float]:
    m = max(vec)
    exps = [math.exp(x - m) for x in vec]
    z = sum(exps)
    return [e / z for e in exps]


def separable_self_attention(
    q_mat: list[list[float]],
    k_mat: list[list[float]],
    v_mat: list[list[float]],
) -> tuple[list[list[float]], list[list[float]]]:
    """Eqs. (5)-(6): A = Phi(K^T) * V in R^{d_key x d_val}, Out = Phi(Q) * A in R^{n x d_val}."""
    n = len(q_mat)
    d_key = len(q_mat[0])
    d_val = len(v_mat[0])

    # Phi(K^T): softmax along sequence dimension n for each key dimension c in 0..d_key-1
    phi_kt = [softmax_vec([k_mat[r][c] for r in range(n)]) for c in range(d_key)]

    # A = Phi(K^T) * V of shape (d_key, d_val)
    a_mat = [
        [sum(phi_kt[c][r] * v_mat[r][v_col] for r in range(n)) for v_col in range(d_val)]
        for c in range(d_key)
    ]

    # Phi(Q): softmax along d_key dimension for each token r in 0..n-1
    phi_q = [softmax_vec(q_mat[r]) for r in range(n)]

    # Out = Phi(Q) * A of shape (n, d_val)
    out = [
        [sum(phi_q[r][c] * a_mat[c][v_col] for c in range(d_key)) for v_col in range(d_val)]
        for r in range(n)
    ]
    return out, a_mat


def batch_scale(xs: list[float], eps: float = 1e-8) -> list[float]:
    """Eq. (10): BS(x) = x / (E[x] + eps)."""
    mean_x = sum(xs) / len(xs)
    return [x / (mean_x + eps) for x in xs]


def explicit_bm25_submodel(
    idf: float,
    tf_batch: list[float],
    dlen_batch: list[float],
    w_dlen: float,
    b_dlen: float,
    eps: float = 1e-8,
) -> list[float]:
    """Eq. (9): s_{t,d}^{(explicit)} = IDF_t * BS(TF_{t,d}) / (BS(TF_{t,d}) + ReLU(w_dlen * BS(|d|) + b_dlen) + eps)."""
    bs_tf = batch_scale(tf_batch, eps)
    bs_len = batch_scale(dlen_batch, eps)
    scores = []
    for tf_val, len_val in zip(bs_tf, bs_len):
        denom_pen = max(0.0, w_dlen * len_val + b_dlen)
        scores.append(idf * tf_val / (tf_val + denom_pen + eps))
    return scores


def main() -> None:
    # 1. Separable self-attention avoids n x n intermediate matrix and forms (d_key x d_val) context A:
    n, d_key, d_val = 200, 8, 6
    q_mat = [[((r + c) % 5) * 0.2 for c in range(d_key)] for r in range(n)]
    k_mat = [[((r * 2 + c) % 7) * 0.15 for c in range(d_key)] for r in range(n)]
    v_mat = [[(r % 3) * 0.5 + v_col * 0.1 for v_col in range(d_val)] for r in range(n)]

    out, a_mat = separable_self_attention(q_mat, k_mat, v_mat)
    assert len(a_mat) == d_key and len(a_mat[0]) == d_val
    assert len(out) == n and len(out[0]) == d_val
    assert d_key * d_val + n * d_key < n * n, "O(n * d_key) intermediate memory is much smaller than O(n^2)"

    # 2. Explicit term matching Eq. (9)-(10) satisfies TF monotonicity and document length normalization:
    # Doc 0 and Doc 1 have identical length (500), but Doc 1 has higher TF (4 vs 1).
    # Doc 2 has same TF as Doc 1 (4), but is much longer (2000 vs 500).
    explicit_scores = explicit_bm25_submodel(
        idf=3.2,
        tf_batch=[1.0, 4.0, 4.0],
        dlen_batch=[500.0, 500.0, 2000.0],
        w_dlen=0.75,
        b_dlen=0.25,
    )
    assert explicit_scores[1] > explicit_scores[0], "Higher TF at equal length increases explicit score"
    assert explicit_scores[1] > explicit_scores[2], "Shorter document at equal TF achieves higher explicit score"

    print("Conformer-Kernel with QTI boundary verification passed:")
    print(f"  Intermediate A shape: ({len(a_mat)}, {len(a_mat[0])}) vs full ({n}, {n})")
    print(f"  Explicit BM25 scores: {[round(s, 4) for s in explicit_scores]}")


if __name__ == "__main__":
    main()
