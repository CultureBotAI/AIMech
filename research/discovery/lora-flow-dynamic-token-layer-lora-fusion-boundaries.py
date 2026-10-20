#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 685: LoRA-Flow (Wang et al., ACL 2024 / arXiv:2402.11455)."""

from __future__ import annotations

import math
import random


def matvec(M: list[list[float]], x: list[float]) -> list[float]:
    return [sum(row[j] * x[j] for j in range(len(x))) for row in M]


def softmax(logits: list[float]) -> list[float]:
    m = max(logits)
    exps = [math.exp(z - m) for z in logits]
    s = sum(exps)
    return [e / s for e in exps]


def l2_sq(v1: list[float], v2: list[float]) -> float:
    return sum((a - b) ** 2 for a, b in zip(v1, v2))


def main() -> None:
    rng = random.Random(685)
    d = 8
    # Two pre-trained LoRA modules with HETEROGENEOUS intermediate ranks (Section 3.2 & Section 4.1:
    # e.g., language LoRA with rank r1=2 and code/math task LoRA with rank r2=5)
    r1, r2 = 2, 5
    A1 = [[rng.gauss(0.0, 0.5) for _ in range(d)] for _ in range(r1)]
    B1 = [[rng.gauss(0.0, 0.5) for _ in range(r1)] for _ in range(d)]
    A2 = [[rng.gauss(0.0, 0.5) for _ in range(d)] for _ in range(r2)]
    B2 = [[rng.gauss(0.0, 0.5) for _ in range(r2)] for _ in range(d)]

    def lora1_out(x: list[float]) -> list[float]:
        return matvec(B1, matvec(A1, x))

    def lora2_out(x: list[float]) -> list[float]:
        return matvec(B2, matvec(A2, x))

    # 1. Verify Eq. 5 & Eq. 6:
    # w^l = softmax(W^l_gate x^l_t) + b^l, where b^l allows negative weights (Section 5.3),
    # and output integration h' = h + Delta h * w^l works across heterogeneous ranks r1 != r2.
    W_gate = [[2.5 if j < d // 2 else -2.5 for j in range(d)], [-2.5 if j < d // 2 else 2.5 for j in range(d)]]
    b_gate = [-0.15, 0.10]

    # Token type A (language-context token: positive on dims 0..3)
    # Token type B (math/code calculation token: positive on dims 4..7)
    x_lang = [1.2 if j < d // 2 else -1.2 for j in range(d)]
    x_math = [-1.2 if j < d // 2 else 1.2 for j in range(d)]

    w_lang = [s + b for s, b in zip(softmax(matvec(W_gate, x_lang)), b_gate)]
    w_math = [s + b for s, b in zip(softmax(matvec(W_gate, x_math)), b_gate)]

    # Verify dynamic token-level switching and negative-weight capability via b^l
    assert w_lang[0] > 0.8 and w_lang[1] > 0.0
    assert w_math[0] < 0.0 and w_math[1] > 1.0  # b_gate[0] = -0.15 produces negative weight when softmax_0 ~ 0

    # 2. Verify that dynamic token-dependent LoRA-Flow strictly outperforms any static task-level weight (w1, w2)
    # on a mixed-token sequence where language tokens require LoRA 1 and math tokens require LoRA 2
    seq_tokens = []
    target_deltas = []
    for t in range(20):
        if t % 2 == 0:
            xt = [1.0 + rng.gauss(0.0, 0.1) if j < d // 2 else -1.0 + rng.gauss(0.0, 0.1) for j in range(d)]
            # Ideal output uses LoRA 1 (0.9 * dh1 + 0.1 * dh2)
            dh1, dh2 = lora1_out(xt), lora2_out(xt)
            y_star = [0.9 * dh1[i] + 0.1 * dh2[i] for i in range(d)]
        else:
            xt = [-1.0 + rng.gauss(0.0, 0.1) if j < d // 2 else 1.0 + rng.gauss(0.0, 0.1) for j in range(d)]
            # Ideal output uses LoRA 2 (0.1 * dh1 + 0.9 * dh2)
            dh1, dh2 = lora1_out(xt), lora2_out(xt)
            y_star = [0.1 * dh1[i] + 0.9 * dh2[i] for i in range(d)]
        seq_tokens.append(xt)
        target_deltas.append(y_star)

    # Optimal static task-level weights (best constant (w1, w2) across all tokens)
    best_static_loss = float("inf")
    for i1 in range(-10, 21):
        for i2 in range(-10, 21):
            sw1, sw2 = i1 * 0.1, i2 * 0.1
            loss = 0.0
            for xt, y_star in zip(seq_tokens, target_deltas):
                dh1, dh2 = lora1_out(xt), lora2_out(xt)
                pred = [sw1 * dh1[i] + sw2 * dh2[i] for i in range(d)]
                loss += l2_sq(pred, y_star)
            best_static_loss = min(best_static_loss, loss / len(seq_tokens))

    # LoRA-Flow dynamic gate loss
    g_scale = math.log(9.0) / (2.0 * d)
    W_flow = [[g_scale if j < d // 2 else -g_scale for j in range(d)], [-g_scale if j < d // 2 else g_scale for j in range(d)]]
    b_flow = [0.0, 0.0]
    flow_loss = 0.0
    for xt, y_star in zip(seq_tokens, target_deltas):
        wt = [s + b for s, b in zip(softmax(matvec(W_flow, xt)), b_flow)]
        dh1, dh2 = lora1_out(xt), lora2_out(xt)
        pred = [wt[0] * dh1[i] + wt[1] * dh2[i] for i in range(d)]
        flow_loss += l2_sq(pred, y_star)
    flow_loss /= len(seq_tokens)

    # Verify parameter efficiency: gate has k * d + k parameters vs LoRA's 2 * d * r
    gate_params = 2 * d + 2
    lora_params = 2 * d * r1 + 2 * d * r2
    assert gate_params < 0.25 * lora_params
    assert flow_loss < 0.05 * best_static_loss

    print(
        f"[PASS] Round 685 LoRA-Flow (Wang et al., ACL 2024): "
        f"w_lang=({w_lang[0]:.3f},{w_lang[1]:.3f}), w_math=({w_math[0]:.3f},{w_math[1]:.3f}), "
        f"flow_loss={flow_loss:.5f} << static_loss={best_static_loss:.5f}"
    )


if __name__ == "__main__":
    main()
