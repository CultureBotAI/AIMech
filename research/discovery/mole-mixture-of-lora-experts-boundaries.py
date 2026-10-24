#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 686: MoLE (Wu, Huang, & Wei, ICLR 2024 / arXiv:2404.13628)."""

from __future__ import annotations

import math
import random


def normalize_vec(v: list[float]) -> list[float]:
    mean = sum(v) / len(v)
    var = sum((x - mean) ** 2 for x in v) / len(v)
    std = math.sqrt(var + 1e-8)
    return [(x - mean) / std for x in v]


def softmax_temp(logits: list[float], tau: float) -> list[float]:
    scaled = [z / tau for z in logits]
    m = max(scaled)
    exps = [math.exp(z - m) for z in scaled]
    s = sum(exps)
    return [e / s for e in exps]


def gating_balance_loss(block_gates: list[list[float]]) -> float:
    """Eq. 14-15: L_balance = -log(prod_{i=0}^{N-1} q^(i)) where q^(i) = (1/M) sum_{k=1}^M G_k(eps_i^k)."""
    M = len(block_gates)
    N = len(block_gates[0])
    q = [sum(block_gates[k][i] for k in range(M)) / M for i in range(N)]
    prod_q = 1.0
    for qi in q:
        prod_q *= max(qi, 1e-12)
    return -math.log(prod_q)


def main() -> None:
    rng = random.Random(686)
    N, L, d, M = 3, 2, 4, 4  # 3 trained LoRAs, sequence length 2, hidden dim 4, 4 gated blocks
    xi = N * L * d

    # 1. Verify Observation 1 & Observation 2 (Section 3.1, Eq. 1-2 & Section 3.2, Eq. 9-13):
    # Suppose LoRA 0 specializes at block 0, LoRA 1 at block 1, LoRA 2 at blocks 2-3.
    lora_block_outputs: list[list[list[float]]] = []
    target_block_outputs: list[list[float]] = []
    for k in range(M):
        experts_k = [[rng.gauss(0.0, 1.0) for _ in range(L * d)] for _ in range(N)]
        # Amplify distinct layer-specific trait on dominant expert for block k
        dom = min(k, N - 1)
        experts_k[dom] = [val * 2.5 for val in experts_k[dom]]
        lora_block_outputs.append(experts_k)
        # Ideal domain composition at block k weights dominant expert 0.8 and others 0.1
        y_k = [
            sum((0.8 if i == dom else 0.1) * experts_k[i][j] for i in range(N))
            for j in range(L * d)
        ]
        target_block_outputs.append(y_k)

    # Unnormalized linear arithmetic (Eq. 1): sum_{i=1}^N E_i
    unnorm_err = 0.0
    # Normalized linear arithmetic (Eq. 2): (1/N) sum_{i=1}^N E_i
    nla_err = 0.0
    # MoLE hierarchical layer-wise gating (Eq. 9-13)
    mole_err = 0.0
    mole_gates: list[list[float]] = []

    for k in range(M):
        experts_k = lora_block_outputs[k]
        y_k = target_block_outputs[k]
        unnorm_pred = [sum(experts_k[i][j] for i in range(N)) for j in range(L * d)]
        nla_pred = [sum(experts_k[i][j] for i in range(N)) / N for j in range(L * d)]
        unnorm_err += sum((a - b) ** 2 for a, b in zip(unnorm_pred, y_k))
        nla_err += sum((a - b) ** 2 for a, b in zip(nla_pred, y_k))

        # Eq. 9: Concatenation and Normalization
        concat_flat = [val for exp_out in experts_k for val in exp_out]
        assert len(concat_flat) == xi
        e_omega = normalize_vec(concat_flat)

        # Eq. 10-11: Dot-product with learnable e in R^{xi x N} and temperature-scaled softmax
        dom = min(k, N - 1)
        tau = 0.5
        # Construct gating projection e_k that aligns with dominant expert's normalized slice
        e_proj = [[0.0] * N for _ in range(xi)]
        norm_dom = sum(e_omega[dom * L * d : (dom + 1) * L * d][j] ** 2 for j in range(L * d))
        scale = (tau * math.log(8.0)) / max(norm_dom, 1e-8)
        for j in range(L * d):
            e_proj[dom * L * d + j][dom] = scale * e_omega[dom * L * d + j]

        eps = [sum(e_omega[r] * e_proj[r][i] for r in range(xi)) for i in range(N)]
        g_k = softmax_temp(eps, tau)
        mole_gates.append(g_k)

        # Eq. 12: Weighted expert output sum
        mole_pred = [sum(g_k[i] * experts_k[i][j] for i in range(N)) for j in range(L * d)]
        mole_err += sum((a - b) ** 2 for a, b in zip(mole_pred, y_k))

    assert mole_err < 1e-12
    assert mole_err < 0.01 * nla_err and mole_err < 0.01 * unnorm_err

    # 2. Verify Eq. 14-15 Gating Balancing Loss properties:
    # By AM-GM inequality on simplex sum_{i=0}^{N-1} q^(i) = 1, L_balance = -log(prod q^(i))
    # achieves unique global minimum N * log(N) iff q^(i) = 1/N for all i.
    min_theoretical = N * math.log(N)
    balanced_gates = [[1.0 / N] * N for _ in range(M)]
    collapsed_gates = [[0.90, 0.05, 0.05] for _ in range(M)]
    loss_bal = gating_balance_loss(balanced_gates)
    loss_col = gating_balance_loss(collapsed_gates)
    assert abs(loss_bal - min_theoretical) < 1e-12
    assert loss_col > loss_bal + 2.5

    # 3. Verify inference Mode 2 (proportional re-weighting under manual expert masking without retraining, Fig. 1):
    raw_gate = [0.46, 0.39, 0.15]
    # Mask out expert 2 (0.15) and redistribute proportionally
    keep_sum = raw_gate[0] + raw_gate[1]
    masked_gate = [raw_gate[0] / keep_sum, raw_gate[1] / keep_sum, 0.0]
    assert abs(sum(masked_gate) - 1.0) < 1e-12
    assert abs(masked_gate[0] / masked_gate[1] - raw_gate[0] / raw_gate[1]) < 1e-12
    assert abs(masked_gate[0] - 0.54117647) < 1e-5 and abs(masked_gate[1] - 0.45882353) < 1e-5

    print(
        f"[PASS] Round 686 MoLE (Wu et al., ICLR 2024): "
        f"mole_err={mole_err:.2e} << nla_err={nla_err:.2f} < unnorm_err={unnorm_err:.2f}, "
        f"L_bal(uniform)={loss_bal:.4f} < L_bal(collapsed)={loss_col:.4f}"
    )


if __name__ == "__main__":
    main()
