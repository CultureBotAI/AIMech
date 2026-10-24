#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 680: LoRA-drop (Zhou et al., COLING 2025 / arXiv:2402.07721)."""

from __future__ import annotations

import math
import random


def matvec(M: list[list[float]], x: list[float]) -> list[float]:
    return [sum(row[j] * x[j] for j in range(len(x))) for row in M]


def l2_sq(v: list[float]) -> float:
    return sum(val * val for val in v)


def frob_sq(M: list[list[float]]) -> float:
    return sum(val * val for row in M for val in row)


def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    m, k, n = len(A), len(A[0]), len(B[0])
    out = [[0.0] * n for _ in range(m)]
    for i in range(m):
        for r in range(k):
            air = A[i][r]
            for j in range(n):
                out[i][j] += air * B[r][j]
    return out


def main() -> None:
    rng = random.Random(680)
    L = 12  # 12 Transformer layers
    d = 16
    r = 2
    n_samples = 20

    # Construct layer-wise LoRA matrices B_i (d x r), A_i (r x d) and layer inputs x_i
    # Specifically demonstrate that Layer 0 has a moderate Frobenius norm ||Delta W_0||_F^2
    # but its row space A_0 is nearly orthogonal to task hidden states x_0,
    # whereas Layers 7..11 have concentrated task-aligned outputs ||Delta W_i x_i||_2^2.
    B_list: list[list[list[float]]] = []
    A_list: list[list[list[float]]] = []
    X_samples: list[list[list[float]]] = []

    for i in range(L):
        # Task signal lives in coordinates 0..3 for layers 7..11, and coordinates 4..7 for layers 0..6
        B_i = [[rng.gauss(0.0, 0.4) for _ in range(r)] for _ in range(d)]
        A_i = [[0.0] * d for _ in range(r)]
        if i >= 7:
            # High output impact on task hidden states (which activate dims 0..3)
            scale = 1.2 + 0.3 * (i - 7)
            for row in range(r):
                for col in range(4):
                    A_i[row][col] = scale * rng.gauss(0.0, 1.0)
        else:
            # Weight matrix has non-trivial Frobenius norm on dims 8..15,
            # but very small projection on active task dims 0..3
            for row in range(r):
                for col in range(4):
                    A_i[row][col] = 0.08 * rng.gauss(0.0, 1.0)
                for col in range(8, d):
                    A_i[row][col] = 0.9 * rng.gauss(0.0, 1.0)
        B_list.append(B_i)
        A_list.append(A_i)

        layer_xs = []
        for _ in range(n_samples):
            x = [0.0] * d
            for col in range(4):
                x[col] = rng.gauss(0.0, 1.5)
            for col in range(4, d):
                x[col] = rng.gauss(0.0, 0.02)
            layer_xs.append(x)
        X_samples.append(layer_xs)

    # 1. Compute Eq. 2 & Eq. 3: g_i = sum_{x in D_s} ||Delta W_i x_i||_2^2 and normalized I_i
    g = []
    frob_norms = []
    for i in range(L):
        dW_i = matmul(B_list[i], A_list[i])
        frob_norms.append(frob_sq(dW_i))
        g_i = sum(l2_sq(matvec(dW_i, x)) for x in X_samples[i])
        g.append(g_i)

    sum_g = sum(g)
    assert sum_g > 0.0
    I_scores = [g_i / sum_g for g_i in g]

    # Verify Eq. 3 properties: 0 <= I_i <= 1 and sum_i I_i == 1
    assert all(0.0 <= score <= 1.0 for score in I_scores)
    assert math.isclose(sum(I_scores), 1.0, rel_tol=1e-12, abs_tol=1e-12)

    # 2. Verify threshold selection (Section 3.2, T = 0.9)
    T = 0.9
    sorted_layers = sorted(range(L), key=lambda idx: I_scores[idx], reverse=True)
    cum_importance = 0.0
    retained_layers: list[int] = []
    for idx in sorted_layers:
        retained_layers.append(idx)
        cum_importance += I_scores[idx]
        if cum_importance >= T:
            break

    k = len(retained_layers)
    # The high-impact layers (from 7..11) capture >=90% of output importance
    assert set(retained_layers).issubset({7, 8, 9, 10, 11}), f"Unexpected retained layers: {retained_layers}"
    assert 1 <= k <= 5

    # 3. Verify parameter reduction with shared LoRA for remaining L - k layers
    # Standard LoRA: L * (2 * d * r); LoRA-drop: (k + 1) * (2 * d * r)
    params_lora = L * 2 * d * r
    params_loradrop = (k + 1) * 2 * d * r
    param_ratio = params_loradrop / params_lora
    assert math.isclose(param_ratio, (k + 1) / L, rel_tol=1e-12)
    assert param_ratio <= 0.5

    # 4. Verify that retaining top-I layers preserves >>90% of total LoRA output energy
    # compared to retaining bottom-I layers (Table 3 / Table 5 Delta W x inv ablation)
    bottom_layers = sorted_layers[-k:]
    retained_energy_top = sum(g[idx] for idx in retained_layers) / sum_g
    retained_energy_bottom = sum(g[idx] for idx in bottom_layers) / sum_g
    assert retained_energy_top >= T
    assert retained_energy_top > 10.0 * retained_energy_bottom

    print(
        f"[PASS] Round 680 LoRA-drop (Zhou et al., COLING 2025): "
        f"sum_I={sum(I_scores):.6f}, k={k}/{L} (param_ratio={param_ratio:.2%}), "
        f"top_energy={retained_energy_top:.4f} vs bottom_energy={retained_energy_bottom:.4f}"
    )


if __name__ == "__main__":
    main()
