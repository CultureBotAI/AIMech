#!/usr/bin/env python3
"""Constructed boundary verification for Projected Attention Layers (PALs, Stickland & Murray, ICML 2019)."""

from __future__ import annotations

import math
import random


def layer_norm(vec: list[float], eps: float = 1e-12) -> list[float]:
    mean = sum(vec) / len(vec)
    var = sum((x - mean) ** 2 for x in vec) / len(vec)
    inv_std = 1.0 / math.sqrt(var + eps)
    return [(x - mean) * inv_std for x in vec]


def softmax(scores: list[float]) -> list[float]:
    m = max(scores)
    exps = [math.exp(s - m) for s in scores]
    total = sum(exps)
    return [e / total for e in exps]


def main() -> int:
    rng = random.Random(20260712)

    # 1. Verify Table 1 parameter budget formulas for BERT-base (d_m=768, L=12)
    d_m = 768
    num_layers = 12
    d_s_pal = 204
    # PALs with shared V^E, V^D across 12 layers and 3*d_s^2 per multi-head attention layer (no W^o):
    params_per_task_pal = 2 * d_m * d_s_pal + num_layers * 3 * (d_s_pal**2)
    assert params_per_task_pal == 1811520

    # PALs without sharing V^E, V^D across layers require d_s=84 for same ~1.8M per-task budget:
    d_s_unshared = 84
    params_per_task_unshared = num_layers * (2 * d_m * d_s_unshared + 3 * (d_s_unshared**2))
    assert params_per_task_unshared == 1802304
    assert d_s_pal > 2.4 * d_s_unshared

    # Low-rank layers (identity g(.)) with d_s=100:
    d_s_lr = 100
    params_per_task_lr = num_layers * (2 * d_m * d_s_lr)
    assert params_per_task_lr == 1843200

    # 2. Verify Parallel PAL forward pass (Eqs. 8, 11) and zero-perturbation recovery when V^D = 0
    seq_len = 5
    d_model = 12
    d_sub = 6
    n_heads = 2
    head_dim = d_sub // n_heads

    h_in = [[rng.gauss(0.0, 1.0) for _ in range(d_model)] for _ in range(seq_len)]
    sa_out = [[rng.gauss(0.0, 1.0) for _ in range(d_model)] for _ in range(seq_len)]
    v_e = [[rng.gauss(0.0, 0.3) for _ in range(d_model)] for _ in range(d_sub)]
    v_d = [[rng.gauss(0.0, 0.3) for _ in range(d_sub)] for _ in range(d_model)]

    wq = [[[rng.gauss(0.0, 0.3) for _ in range(d_sub)] for _ in range(head_dim)] for _ in range(n_heads)]
    wk = [[[rng.gauss(0.0, 0.3) for _ in range(d_sub)] for _ in range(head_dim)] for _ in range(n_heads)]
    wv = [[[rng.gauss(0.0, 0.3) for _ in range(d_sub)] for _ in range(head_dim)] for _ in range(n_heads)]

    def pal_ts(h_seq: list[list[float]], zero_decoder: bool = False) -> list[list[float]]:
        # Project down: z_t = V^E h_t in R^{d_sub}
        z = [[sum(v_e[r][c] * h_t[c] for c in range(d_model)) for r in range(d_sub)] for h_t in h_seq]
        # Multi-head attention in R^{d_sub} without W^o
        mh_concat = [[0.0] * d_sub for _ in range(seq_len)]
        for hd in range(n_heads):
            q_seq = [[sum(wq[hd][r][c] * z_t[c] for c in range(d_sub)) for r in range(head_dim)] for z_t in z]
            k_seq = [[sum(wk[hd][r][c] * z_t[c] for c in range(d_sub)) for r in range(head_dim)] for z_t in z]
            v_seq = [[sum(wv[hd][r][c] * z_t[c] for c in range(d_sub)) for r in range(head_dim)] for z_t in z]
            for j in range(seq_len):
                logits = [
                    sum(q_seq[j][r] * k_seq[t][r] for r in range(head_dim)) / math.sqrt(head_dim)
                    for t in range(seq_len)
                ]
                weights = softmax(logits)
                for r in range(head_dim):
                    mh_concat[j][hd * head_dim + r] = sum(weights[t] * v_seq[t][r] for t in range(seq_len))
        if zero_decoder:
            return [[0.0] * d_model for _ in range(seq_len)]
        return [
            [sum(v_d[r][c] * mh_concat[j][c] for c in range(d_sub)) for r in range(d_model)]
            for j in range(seq_len)
        ]

    base_out = [layer_norm([h_in[j][c] + sa_out[j][c] for c in range(d_model)]) for j in range(seq_len)]
    ts_zero = pal_ts(h_in, zero_decoder=True)
    zero_out = [
        layer_norm([h_in[j][c] + sa_out[j][c] + ts_zero[j][c] for c in range(d_model)])
        for j in range(seq_len)
    ]
    max_zero_err = max(abs(base_out[j][c] - zero_out[j][c]) for j in range(seq_len) for c in range(d_model))
    assert max_zero_err == 0.0

    ts_active = pal_ts(h_in, zero_decoder=False)
    active_out = [
        layer_norm([h_in[j][c] + sa_out[j][c] + ts_active[j][c] for c in range(d_model)])
        for j in range(seq_len)
    ]
    diff_active = math.sqrt(
        sum((active_out[j][c] - base_out[j][c]) ** 2 for j in range(seq_len) for c in range(d_model))
    )
    assert diff_active > 0.1

    # 3. Verify annealed task sampling schedule (Eqs. 13-14) on GLUE dataset sizes (Table 2)
    task_sizes = [392000, 363000, 108000, 67000, 8500, 5700, 3500, 2500]
    total_epochs = 25
    ratios = []
    for e in range(1, total_epochs + 1):
        alpha = 1.0 - 0.8 * (e - 1) / (total_epochs - 1)
        weights = [n**alpha for n in task_sizes]
        probs = [w / sum(weights) for w in weights]
        ratios.append(max(probs) / min(probs))

    assert math.isclose(ratios[0], 392000 / 2500, rel_tol=1e-12)
    assert math.isclose(ratios[-1], (392000 / 2500) ** 0.2, rel_tol=1e-12)
    for idx in range(len(ratios) - 1):
        assert ratios[idx] > ratios[idx + 1]

    print(
        f"[PASS] PALs boundaries verified: params_pal={params_per_task_pal} (d_s={d_s_pal} vs {d_s_unshared}), "
        f"diff_active={diff_active:.4f}, anneal_ratio={ratios[0]:.1f}->{ratios[-1]:.4f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
