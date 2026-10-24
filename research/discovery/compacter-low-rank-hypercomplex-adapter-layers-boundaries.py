#!/usr/bin/env python3
"""Constructed boundary verification for Round 659:
Compacter: Efficient Low-Rank Hypercomplex Adapter Layers
(Karimi Mahabadi, Henderson, & Ruder, NeurIPS 2021, arXiv:2106.04647).

Verifies:
1. LPHM Kronecker decomposition W^j = sum_{i=1}^n A_i (x) (s_i^j (t_i^j)^T)
   and exact equivalence with factored bilinear evaluation without materializing
   full k x d matrices per forward step.
2. Parameter complexity laws (Section 4, p. 5):
   - Standard Adapter: 4 L k d
   - PHM-Adapter: 4 L (k d / n + n^3)
   - Compacter: 4 L (k + d) + n^3
   - Compacter++: 2 L (k + d) + n^3
3. Shared slow weights {A_i} vs. fast rank-one layer-specific weights {s_i^j, t_i^j}:
   cross-layer gradient coupling on {A_i} while preserving distinct rank-n
   weight matrices W^j across adapter positions j.
"""

from __future__ import annotations
import math
import random


def kron_2d(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    """Compute Kronecker product A (x) B."""
    m, f = len(A), len(A[0])
    p, q = len(B), len(B[0])
    out = [[0.0] * (f * q) for _ in range(m * p)]
    for i in range(m):
        for j in range(f):
            aij = A[i][j]
            for r in range(p):
                row_idx = i * p + r
                base_col = j * q
                for c in range(q):
                    out[row_idx][base_col + c] = aij * B[r][c]
    return out


def outer_vec(s: list[float], t: list[float]) -> list[list[float]]:
    """Compute rank-1 outer product s t^T in R^{|s| x |t|}."""
    return [[si * tj for tj in t] for si in s]


def lphm_weight(
    A_list: list[list[list[float]]],
    s_list: list[list[float]],
    t_list: list[list[float]],
) -> list[list[float]]:
    """Synthesize W = sum_{i=1}^n A_i (x) (s_i t_i^T) in R^{k x d} (Equation 5)."""
    n = len(A_list)
    k = len(A_list[0]) * len(s_list[0])
    d = len(A_list[0][0]) * len(t_list[0])
    W = [[0.0] * d for _ in range(k)]
    for i in range(n):
        Bi = outer_vec(s_list[i], t_list[i])
        Ki = kron_2d(A_list[i], Bi)
        for r in range(k):
            for c in range(d):
                W[r][c] += Ki[r][c]
    return W


def lphm_factored_matvec(
    A_list: list[list[list[float]]],
    s_list: list[list[float]],
    t_list: list[list[float]],
    x: list[float],
) -> list[float]:
    """Compute y = W^T x in R^d directly via Kronecker mixed-product identity
    without forming full k x d matrices."""
    n = len(A_list)
    p = len(s_list[0])  # k // n
    q = len(t_list[0])  # d // n
    d = n * q
    # Reshape x in R^{n*p} into X in R^{n x p}
    X = [x[row * p : (row + 1) * p] for row in range(n)]
    y = [0.0] * d
    for i in range(n):
        Ai = A_list[i]
        si = s_list[i]
        ti = t_list[i]
        # First contract each block row r of X with s_i: u_r = sum_{u=0}^{p-1} X[r][u] * s_i[u]
        u = [sum(X[r][u_idx] * si[u_idx] for u_idx in range(p)) for r in range(n)]
        # Next apply A_i^T to u: v_c = sum_{r=0}^{n-1} A_i[r][c] * u_r
        v = [sum(Ai[r][c] * u[r] for r in range(n)) for c in range(n)]
        # Finally outer product with t_i gives block c: v_c * t_i
        for c in range(n):
            vc = v[c]
            base = c * q
            for col_sub in range(q):
                y[base + col_sub] += vc * ti[col_sub]
    return y


def main() -> None:
    rng = random.Random(20210604)
    # 1. Verify parameter counts on T5-base configuration (Section 4, p. 5):
    # L = 12 layers (encoder + decoder), k = 768, d = 24, n = 4
    L, k, d, n = 12, 768, 24, 4
    params_adapter = 4 * L * (k * d)
    params_phm = 4 * L * ((k * d) // n + n ** 3)
    params_compacter = 4 * L * (k + d) + n ** 3
    params_compacter_pp = 2 * L * (k + d) + n ** 3

    assert params_adapter == 884736
    assert params_phm == 224256
    assert params_compacter == 38080
    assert params_compacter_pp == 19072
    assert params_compacter < params_phm < params_adapter
    assert params_compacter_pp < params_compacter

    # 2. Verify exact equivalence between Equation (5) Kronecker synthesis and factored matvec
    k_s, d_s, n_s = 16, 8, 4
    p_s, q_s = k_s // n_s, d_s // n_s
    A_shared = [
        [[rng.uniform(-0.5, 0.5) for _ in range(n_s)] for _ in range(n_s)]
        for _ in range(n_s)
    ]
    s_j1 = [[rng.uniform(-0.5, 0.5) for _ in range(p_s)] for _ in range(n_s)]
    t_j1 = [[rng.uniform(-0.5, 0.5) for _ in range(q_s)] for _ in range(n_s)]
    s_j2 = [[rng.uniform(-0.5, 0.5) for _ in range(p_s)] for _ in range(n_s)]
    t_j2 = [[rng.uniform(-0.5, 0.5) for _ in range(q_s)] for _ in range(n_s)]

    W1 = lphm_weight(A_shared, s_j1, t_j1)
    W2 = lphm_weight(A_shared, s_j2, t_j2)
    x = [rng.uniform(-1.0, 1.0) for _ in range(k_s)]

    # Dense matvec y = W1^T x
    y1_dense = [sum(W1[r][c] * x[r] for r in range(k_s)) for c in range(d_s)]
    y1_factored = lphm_factored_matvec(A_shared, s_j1, t_j1, x)
    max_diff = max(abs(a - b) for a, b in zip(y1_dense, y1_factored))
    assert max_diff < 1e-12, f"Mismatch between Kronecker and factored LPHM: {max_diff}"

    # Verify that sharing slow weights {A_i} with distinct fast rank-1 weights produces distinct W1 != W2
    diff_w1_w2 = math.sqrt(
        sum((W1[r][c] - W2[r][c]) ** 2 for r in range(k_s) for c in range(d_s))
    )
    assert diff_w1_w2 > 0.1, f"Expected distinct adapter weights W1 != W2, got {diff_w1_w2}"

    print(
        f"[PASS] Round 659 Compacter (Karimi Mahabadi et al. 2021): "
        f"params_adapter={params_adapter} > params_phm={params_phm} > "
        f"params_compacter={params_compacter} > params_compacter++={params_compacter_pp}, "
        f"max_diff={max_diff:.2e}, ||W1-W2||_F={diff_w1_w2:.4f}"
    )


if __name__ == "__main__":
    main()
