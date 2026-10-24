#!/usr/bin/env python3
"""Constructed boundary verification for TK Transformer-Kernel (Hofstatter et al., ECAI 2020, arXiv:2002.01854).

Verifies:
1. Hybrid contextualized representation hat{t}_i = t_i * alpha + context(t_{1:n})_i * (1 - alpha) (Eq. 1).
2. Interaction cosine match-matrix M_{i,j} = cos(hat{q}_i, hat{d}_j) (Eq. 4) and Gaussian RBF kernel
   transformation K_{i,j}^k = exp(-(M_{i,j} - mu_k)^2 / (2 * sigma^2)) summed over document positions j (Eqs. 5-6).
3. Dual normalization paths:
   - Log-normalization s_log^k = sum_i log_b(K_i^k) (Eq. 7)
   - Document-length normalization s_len^k = sum_i (K_i^k / d_len) (Eq. 8)
   and weighted linear combination s = s_log * beta + s_len * gamma (Eqs. 9-10).
"""

from __future__ import annotations

import math


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def norm(a: list[float]) -> float:
    return math.sqrt(dot(a, a))


def cosine_sim(a: list[float], b: list[float]) -> float:
    return dot(a, b) / (norm(a) * norm(b))


def hybrid_contextualize(
    static_embs: list[list[float]],
    context_embs: list[list[float]],
    alpha: float,
) -> list[list[float]]:
    """Implements Eq. (1): hat{t}_i = t_i * alpha + context(t_{1:n})_i * (1 - alpha)."""
    assert 0.0 <= alpha <= 1.0
    assert len(static_embs) == len(context_embs)
    return [
        [t_d * alpha + c_d * (1.0 - alpha) for t_d, c_d in zip(t_vec, c_vec)]
        for t_vec, c_vec in zip(static_embs, context_embs)
    ]


def tk_dual_kernel_score(
    q_vecs: list[list[float]],
    d_vecs: list[list[float]],
    mus: list[float],
    sigma: float,
    w_log: list[float],
    w_len: list[float],
    beta: float,
    gamma: float,
    log_base: float = 2.0,
) -> tuple[float, float, float]:
    """Implements Eqs. (4)-(10): returns (s_log, s_len, s_total)."""
    q_len = len(q_vecs)
    d_len = len(d_vecs)
    match_mat = [[cosine_sim(q_vecs[i], d_vecs[j]) for j in range(d_len)] for i in range(q_len)]

    s_log_kernels: list[float] = []
    s_len_kernels: list[float] = []
    for mu_k in mus:
        k_i_vals: list[float] = []
        for i in range(q_len):
            k_ij_sum = sum(
                math.exp(-((match_mat[i][j] - mu_k) ** 2) / (2.0 * (sigma ** 2)))
                for j in range(d_len)
            )
            k_i_vals.append(k_ij_sum)
        # Eq. (7): log_b normalization per query term
        s_log_k = sum(math.log(max(val, 1e-12)) / math.log(log_base) for val in k_i_vals)
        # Eq. (8): document-length normalization per query term
        s_len_k = sum(val / float(d_len) for val in k_i_vals)
        s_log_kernels.append(s_log_k)
        s_len_kernels.append(s_len_k)

    # Eqs. (9)-(10):
    s_log = dot(s_log_kernels, w_log)
    s_len = dot(s_len_kernels, w_len)
    s_total = s_log * beta + s_len * gamma
    return s_log, s_len, s_total


def main() -> None:
    alpha = 0.4
    mus = [0.9, 0.7, 0.5, 0.3]
    sigma = 0.1
    w_log = [0.6, 0.4, 0.1, -0.2]
    w_len = [0.5, 0.3, 0.1, -0.1]
    beta = 0.6
    gamma = 0.4

    # Query: ["androgen", "receptor", "define"] (Figure 3)
    q_static = [[0.9, 0.2, 0.1], [0.8, 0.3, 0.1], [0.1, 0.9, 0.2]]
    q_ctx = [[0.85, 0.25, 0.1], [0.78, 0.35, 0.1], [0.2, 0.88, 0.15]]
    q_hat = hybrid_contextualize(q_static, q_ctx, alpha=alpha)

    # Relevant passage (defines androgen receptor = NR3C4 nuclear receptor subfamily, Figure 3 left):
    d_pos_static = [
        [0.9, 0.2, 0.1],   # androgen
        [0.8, 0.3, 0.1],   # receptor
        [0.15, 0.85, 0.2], # "also known as" (contextual match to "define")
        [0.2, 0.82, 0.15], # "is a type" (contextual match to "define")
    ]
    d_pos_ctx = [
        [0.86, 0.24, 0.1],
        [0.79, 0.34, 0.1],
        [0.18, 0.87, 0.16],
        [0.22, 0.85, 0.14],
    ]
    d_pos_hat = hybrid_contextualize(d_pos_static, d_pos_ctx, alpha=alpha)

    # Non-relevant passage (mentions androgen receptor many times in passing without defining it, Figure 3 right):
    d_neg_static = [
        [0.9, 0.2, 0.1],
        [0.8, 0.3, 0.1],
        [0.1, 0.1, 0.9],
        [0.1, 0.2, 0.85],
        [0.2, 0.1, 0.9],
        [0.15, 0.1, 0.88],
    ]
    d_neg_ctx = [
        [0.82, 0.2, 0.2],
        [0.75, 0.28, 0.2],
        [0.1, 0.1, 0.92],
        [0.1, 0.15, 0.88],
        [0.18, 0.1, 0.91],
        [0.12, 0.1, 0.9],
    ]
    d_neg_hat = hybrid_contextualize(d_neg_static, d_neg_ctx, alpha=alpha)

    slog_pos, slen_pos, s_pos = tk_dual_kernel_score(
        q_hat, d_pos_hat, mus, sigma, w_log, w_len, beta, gamma
    )
    slog_neg, slen_neg, s_neg = tk_dual_kernel_score(
        q_hat, d_neg_hat, mus, sigma, w_log, w_len, beta, gamma
    )

    assert slog_pos > slog_neg
    assert slen_pos > slen_neg
    assert s_pos > s_neg

    print(
        f"[PASS] TK boundaries verified: s_pos={s_pos:.4f} (slog={slog_pos:.4f}, slen={slen_pos:.4f}) > "
        f"s_neg={s_neg:.4f} (slog={slog_neg:.4f}, slen={slen_neg:.4f})"
    )


if __name__ == "__main__":
    main()
