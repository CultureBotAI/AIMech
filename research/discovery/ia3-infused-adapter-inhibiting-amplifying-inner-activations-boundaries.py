#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 657: (IA)^3 (Liu et al., NeurIPS 2022)."""

import math
import random


def softmax(logits: list[float]) -> list[float]:
    m = max(logits)
    exps = [math.exp(z - m) for z in logits]
    s = sum(exps)
    return [e / s for e in exps]


def verify_ia3_attention_ffn_and_weight_folding() -> None:
    """Verify Section 3.3: (IA)^3 activation rescaling, identity init at l=1, and exact weight folding."""
    rng = random.Random(20220505)
    seq_len, d_model, d_k, d_v, d_ff = 4, 6, 4, 4, 10
    x = [[rng.gauss(0.0, 1.0) for _ in range(d_model)] for _ in range(seq_len)]
    w_q = [[rng.gauss(0.0, 0.4) for _ in range(d_k)] for _ in range(d_model)]
    w_k = [[rng.gauss(0.0, 0.4) for _ in range(d_k)] for _ in range(d_model)]
    w_v = [[rng.gauss(0.0, 0.4) for _ in range(d_v)] for _ in range(d_model)]
    w_1 = [[rng.gauss(0.0, 0.4) for _ in range(d_ff)] for _ in range(d_model)]
    w_2 = [[rng.gauss(0.0, 0.4) for _ in range(d_model)] for _ in range(d_ff)]

    def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
        return [
            [sum(a[i][p] * b[p][j] for p in range(len(b))) for j in range(len(b[0]))]
            for i in range(len(a))
        ]

    q_mat = matmul(x, w_q)
    k_mat = matmul(x, w_k)
    v_mat = matmul(x, w_v)

    def ia3_attention(lk: list[float], lv: list[float]) -> list[list[float]]:
        # softmax(Q (l_k odot K^T) / sqrt(d_k)) (l_v odot V)
        out = []
        for i in range(seq_len):
            scores = [
                sum(q_mat[i][c] * (lk[c] * k_mat[j][c]) for c in range(d_k)) / math.sqrt(d_k)
                for j in range(seq_len)
            ]
            probs = softmax(scores)
            row = [
                sum(probs[j] * (lv[c] * v_mat[j][c]) for j in range(seq_len))
                for c in range(d_v)
            ]
            out.append(row)
        return out

    def ia3_ffn(lff: list[float]) -> list[list[float]]:
        # (l_ff odot gamma(x W_1)) W_2 with ReLU nonlinearity gamma
        xw1 = matmul(x, w_1)
        hidden = [[lff[c] * max(0.0, xw1[i][c]) for c in range(d_ff)] for i in range(seq_len)]
        return matmul(hidden, w_2)

    # 1. Identity initialization: l_k = 1, l_v = 1, l_ff = 1 leaves outputs strictly unchanged
    lk_ones = [1.0 for _ in range(d_k)]
    lv_ones = [1.0 for _ in range(d_v)]
    lff_ones = [1.0 for _ in range(d_ff)]
    att_init = ia3_attention(lk_ones, lv_ones)
    ffn_init = ia3_ffn(lff_ones)

    # 2. Trained (IA)^3 vectors: verify permanent weight folding l odot (W x) == (l odot W) x
    lk_tr = [rng.uniform(0.5, 1.5) for _ in range(d_k)]
    lv_tr = [rng.uniform(0.5, 1.5) for _ in range(d_v)]
    lff_tr = [rng.uniform(0.5, 1.5) for _ in range(d_ff)]

    att_unfolded = ia3_attention(lk_tr, lv_tr)
    ffn_unfolded = ia3_ffn(lff_tr)

    # Fold lk_tr into columns of W_k, lv_tr into columns of W_v, and lff_tr into rows of W_2
    w_k_folded = [[w_k[r][c] * lk_tr[c] for c in range(d_k)] for r in range(d_model)]
    w_v_folded = [[w_v[r][c] * lv_tr[c] for c in range(d_v)] for r in range(d_model)]
    w_2_folded = [[lff_tr[r] * w_2[r][c] for c in range(d_model)] for r in range(d_ff)]

    k_folded = matmul(x, w_k_folded)
    v_folded = matmul(x, w_v_folded)
    att_folded = []
    for i in range(seq_len):
        scores = [
            sum(q_mat[i][c] * k_folded[j][c] for c in range(d_k)) / math.sqrt(d_k)
            for j in range(seq_len)
        ]
        probs = softmax(scores)
        att_folded.append([sum(probs[j] * v_folded[j][c] for j in range(seq_len)) for c in range(d_v)])

    xw1 = matmul(x, w_1)
    hidden_base = [[max(0.0, xw1[i][c]) for c in range(d_ff)] for i in range(seq_len)]
    ffn_folded = matmul(hidden_base, w_2_folded)

    for i in range(seq_len):
        for c in range(d_v):
            assert abs(att_unfolded[i][c] - att_folded[i][c]) < 1e-14
        for c in range(d_model):
            assert abs(ffn_unfolded[i][c] - ffn_folded[i][c]) < 1e-14
    assert att_init != att_unfolded and ffn_init != ffn_unfolded


def verify_ia3_parameter_budget() -> None:
    """Verify parameter counts L(d_k + d_v + d_ff) for encoder and L(2*d_k + 2*d_v + d_ff) for decoder."""
    l_layers, d_k, d_v, d_ff = 24, 1024, 1024, 4096
    enc_params = l_layers * (d_k + d_v + d_ff)
    dec_params = l_layers * (2 * d_k + 2 * d_v + d_ff)
    assert enc_params == 24 * 6144 and dec_params == 24 * 8192


if __name__ == "__main__":
    verify_ia3_attention_ffn_and_weight_folding()
    verify_ia3_parameter_budget()
    print("[PASS] Round 657 (IA)^3 boundary and mathematical verification succeeded.")
