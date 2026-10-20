#!/usr/bin/env python3
"""Constructed boundary verification for MiniLM (Wang et al., NeurIPS 2020, arXiv:2002.10957)."""

import math


def matmul_transpose_b(a: list[list[float]], b: list[list[float]], scale: float) -> list[list[float]]:
    """Compute (A * B^T) / scale."""
    r = len(a)
    c = len(b)
    d = len(a[0])
    return [[sum(a[i][k] * b[j][k] for k in range(d)) / scale for j in range(c)] for i in range(r)]


def softmax_rows(mat: list[list[float]]) -> list[list[float]]:
    out = []
    for row in mat:
        m = max(row)
        exps = [math.exp(x - m) for x in row]
        s = sum(exps)
        out.append([e / s for e in exps])
    return out


def kl_matrix(p_mat: list[list[float]], q_mat: list[list[float]], eps: float = 1e-12) -> float:
    """Average row-wise KL divergence D_KL(P || Q) over |x| tokens."""
    seq_len = len(p_mat)
    total = 0.0
    for t in range(seq_len):
        for j in range(seq_len):
            p = p_mat[t][j]
            q = q_mat[t][j]
            total += p * math.log((p + eps) / (q + eps))
    return total / seq_len


def value_relation_matrix(v_head: list[list[float]]) -> list[list[float]]:
    """Equations (7)-(8): VR = softmax((V * V^T) / sqrt(d_k))."""
    d_k = len(v_head[0])
    return softmax_rows(matmul_transpose_b(v_head, v_head, math.sqrt(d_k)))


def minilm_deep_self_attention_loss(
    q_t_heads: list[list[list[float]]],
    k_t_heads: list[list[list[float]]],
    v_t_heads: list[list[list[float]]],
    q_s_heads: list[list[list[float]]],
    k_s_heads: list[list[list[float]]],
    v_s_heads: list[list[list[float]]],
) -> tuple[float, float, float]:
    """Equations (6)-(10): L = L_AT + L_VR on last Transformer layer."""
    a_h = len(q_t_heads)
    l_at = 0.0
    l_vr = 0.0
    for a in range(a_h):
        dk_t = len(q_t_heads[a][0])
        dk_s = len(q_s_heads[a][0])
        a_t = softmax_rows(matmul_transpose_b(q_t_heads[a], k_t_heads[a], math.sqrt(dk_t)))
        a_s = softmax_rows(matmul_transpose_b(q_s_heads[a], k_s_heads[a], math.sqrt(dk_s)))
        l_at += kl_matrix(a_t, a_s)

        vr_t = value_relation_matrix(v_t_heads[a])
        vr_s = value_relation_matrix(v_s_heads[a])
        l_vr += kl_matrix(vr_t, vr_s)

    l_at /= a_h
    l_vr /= a_h
    return l_at, l_vr, l_at + l_vr


def main() -> None:
    # Teacher has head dimension d_k = 4 (e.g., d_h = 768 / 12 = 64 in full model),
    # while Student has smaller head dimension d'_k = 2 (e.g., d'_h = 384 / 12 = 32):
    seq_len = 3
    v_t = [[[0.8, 0.2, 0.4, 0.2], [0.1, 0.9, 0.2, 0.3], [0.7, 0.3, 0.5, 0.1]]]
    v_s_good = [[[0.6, 0.15], [0.08, 0.65], [0.52, 0.22]]]
    v_s_bad = [[[-0.5, 0.8], [0.9, -0.4], [0.1, -0.7]]]

    # 1. Verify value-relation matrices have identical shape (|x| x |x|) despite d_k != d'_k:
    vr_t = value_relation_matrix(v_t[0])
    vr_s = value_relation_matrix(v_s_good[0])
    assert len(vr_t) == len(vr_s) == seq_len
    assert len(vr_t[0]) == len(vr_s[0]) == seq_len

    # 2. Verify L = L_AT + L_VR rewards aligned student queries/keys/values:
    q_t = [[[1.0, 0.0, 0.5, 0.0], [0.0, 1.0, 0.0, 0.5], [0.5, 0.5, 0.2, 0.2]]]
    k_t = q_t
    q_s_good = [[[0.8, 0.0], [0.0, 0.8], [0.4, 0.4]]]
    q_s_bad = [[[0.0, 0.9], [0.9, 0.0], [-0.5, 0.5]]]

    l_at_g, l_vr_g, l_tot_g = minilm_deep_self_attention_loss(q_t, k_t, v_t, q_s_good, q_s_good, v_s_good)
    l_at_b, l_vr_b, l_tot_b = minilm_deep_self_attention_loss(q_t, k_t, v_t, q_s_bad, q_s_bad, v_s_bad)
    assert l_at_g < l_at_b
    assert l_vr_g < l_vr_b
    assert l_tot_g < l_tot_b

    print("MiniLM boundary verification passed:")
    print(f"  VR shape (teacher d_k=4 vs student d'_k=2): ({len(vr_s)}, {len(vr_s[0])})")
    print(f"  L_AT + L_VR (aligned vs mismatched): {l_tot_g:.5f} < {l_tot_b:.5f}")


if __name__ == "__main__":
    main()
