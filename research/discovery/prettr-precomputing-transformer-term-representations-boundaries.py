#!/usr/bin/env python3
"""Constructed boundary verification for PreTTR (MacAvaney et al., SIGIR 2020, arXiv:2004.14255).

Verifies:
1. Equivalence between:
   (a) Jointly running layers 1..l with a block-diagonal cross-segment attention mask disallowing
       query tokens ([CLS]; q; [SEP]) from attending to document tokens (d; [SEP]) and vice versa, and
   (b) Independently precomputing document token representations at index time and query token
       representations at query time up to layer l, then concatenating them for layers l+1..n.
2. GELU token representation compression r = GELU(s_l W_comp + b_comp) in R^{m x e} and linear
   decompression s_hat_l = r W_decomp + b_decomp in R^{m x d} trained via attention-score MSE loss
   L = (1 / (n - l)) * sum_{i=l+1}^n MSE(a_i, a_hat_i) (Eq. 2).
"""

from __future__ import annotations

import math


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def gelu(x: float) -> float:
    """Implements Gaussian Error Linear Unit (Hendrycks & Gimpel, 2016)."""
    return 0.5 * x * (1.0 + math.erf(x / math.sqrt(2.0)))


def softmax(scores: list[float]) -> list[float]:
    m = max(scores)
    exps = [math.exp(s - m) for s in scores]
    total = sum(exps)
    return [e / total for e in exps]


def self_attention_layer(
    tokens: list[list[float]],
    w_q: list[list[float]],
    w_k: list[list[float]],
    w_v: list[list[float]],
    mask: list[list[bool]] | None = None,
) -> tuple[list[list[float]], list[list[float]]]:
    """Single-head self-attention returning (updated_tokens, attention_matrix)."""
    m = len(tokens)
    d = len(w_q)
    scale = math.sqrt(float(d))
    q_proj = [[dot(row, tok) for row in w_q] for tok in tokens]
    k_proj = [[dot(row, tok) for row in w_k] for tok in tokens]
    v_proj = [[dot(row, tok) for row in w_v] for tok in tokens]

    attn_matrix: list[list[float]] = []
    out_tokens: list[list[float]] = []
    for i in range(m):
        raw_scores: list[float] = []
        for j in range(m):
            if mask is not None and not mask[i][j]:
                raw_scores.append(-1e9)
            else:
                raw_scores.append(dot(q_proj[i], k_proj[j]) / scale)
        # Filter out masked positions exactly to avoid any floating-point leakage
        if mask is not None:
            allowed_indices = [j for j in range(m) if mask[i][j]]
            allowed_probs = softmax([raw_scores[j] for j in allowed_indices])
            probs = [0.0] * m
            for idx, p in zip(allowed_indices, allowed_probs):
                probs[idx] = p
        else:
            probs = softmax(raw_scores)
        attn_matrix.append(probs)
        out_vec = [sum(probs[j] * v_proj[j][dim] for j in range(m)) + tokens[i][dim] for dim in range(d)]
        out_tokens.append(out_vec)
    return out_tokens, attn_matrix


def compress_decompress(
    s_l: list[list[float]],
    w_comp: list[list[float]],
    b_comp: list[float],
    w_decomp: list[list[float]],
    b_decomp: list[float],
) -> tuple[list[list[float]], list[list[float]]]:
    """Implements Section 4.2: r = GELU(s_l W_comp + b_comp), s_hat_l = r W_decomp + b_decomp."""
    r_mat: list[list[float]] = []
    s_hat: list[list[float]] = []
    for tok in s_l:
        r_vec = [gelu(dot(col, tok) + b_c) for col, b_c in zip(w_comp, b_comp)]
        r_mat.append(r_vec)
        sh_vec = [dot(col, r_vec) + b_d for col, b_d in zip(w_decomp, b_decomp)]
        s_hat.append(sh_vec)
    return r_mat, s_hat


def attention_mse_loss(attn_orig: list[list[list[float]]], attn_comp: list[list[list[float]]]) -> float:
    """Implements Eq. (2): average MSE between attention matrices across layers l+1..n."""
    assert len(attn_orig) == len(attn_comp) and len(attn_orig) > 0
    layer_mses: list[float] = []
    for a_i, ah_i in zip(attn_orig, attn_comp):
        m = len(a_i)
        sq_err = sum((a_i[r][c] - ah_i[r][c]) ** 2 for r in range(m) for c in range(m))
        layer_mses.append(sq_err / float(m * m))
    return sum(layer_mses) / float(len(layer_mses))


def main() -> None:
    # 2 query tokens ([CLS], q1) and 3 document tokens (d1, d2, [SEP])
    q_tokens = [[0.5, 0.2, -0.1, 0.4], [0.8, -0.3, 0.5, 0.2]]
    d_tokens = [[0.7, -0.2, 0.6, 0.1], [-0.4, 0.9, 0.1, -0.3], [0.1, 0.1, 0.2, 0.0]]
    joint_tokens = q_tokens + d_tokens
    n_q = len(q_tokens)
    m_total = len(joint_tokens)

    # Block-diagonal cross-segment attention mask for layers 1..l:
    mask = [
        [(i < n_q and j < n_q) or (i >= n_q and j >= n_q) for j in range(m_total)]
        for i in range(m_total)
    ]

    w_q = [[1.0, 0.2, 0.0, 0.1], [0.1, 0.9, 0.2, 0.0], [0.0, 0.1, 1.0, 0.2], [0.2, 0.0, 0.1, 0.8]]
    w_k = [[0.9, 0.1, 0.1, 0.0], [0.0, 1.0, 0.1, 0.1], [0.1, 0.0, 0.9, 0.1], [0.1, 0.1, 0.0, 0.9]]
    w_v = [[0.8, 0.1, 0.0, 0.1], [0.1, 0.8, 0.1, 0.0], [0.0, 0.1, 0.8, 0.1], [0.1, 0.0, 0.1, 0.8]]

    # 1. Verify exact equivalence between masked joint encoding and decoupled index-time + query-time encoding:
    s_l_masked, _ = self_attention_layer(joint_tokens, w_q, w_k, w_v, mask=mask)
    s_l_q_only, _ = self_attention_layer(q_tokens, w_q, w_k, w_v, mask=None)
    s_l_d_only, _ = self_attention_layer(d_tokens, w_q, w_k, w_v, mask=None)
    s_l_decoupled = s_l_q_only + s_l_d_only

    max_diff = max(
        abs(s_l_masked[i][dim] - s_l_decoupled[i][dim])
        for i in range(m_total)
        for dim in range(4)
    )
    assert max_diff < 1e-12

    # 2. Upper layer l+1..n (unmasked full cross-segment attention) and token compression MSE (Eq. 2):
    _, attn_upper_orig = self_attention_layer(s_l_decoupled, w_q, w_k, w_v, mask=None)

    # Compress d=4 -> e=2 for document tokens:
    w_comp = [[0.9, 0.4, 0.1, 0.2], [0.1, 0.3, 0.8, 0.5]]
    b_comp = [0.1, -0.1]
    w_decomp = [[0.9, 0.1], [0.4, 0.3], [0.1, 0.8], [0.2, 0.5]]
    b_decomp = [0.0, 0.0, 0.0, 0.0]
    r_doc, s_hat_d = compress_decompress(s_l_d_only, w_comp, b_comp, w_decomp, b_decomp)
    assert len(r_doc[0]) == 2 < len(s_l_d_only[0]) == 4  # 50% dimension reduction

    _, attn_upper_comp = self_attention_layer(s_l_q_only + s_hat_d, w_q, w_k, w_v, mask=None)
    mse_loss = attention_mse_loss([attn_upper_orig], [attn_upper_comp])
    assert 0.0 <= mse_loss < 0.01

    print(
        f"[PASS] PreTTR boundaries verified: decoupled_diff={max_diff:.2e}, "
        f"compressed_dim={len(r_doc[0])}/{len(s_l_d_only[0])}, attn_mse_loss={mse_loss:.6f}"
    )


if __name__ == "__main__":
    main()
