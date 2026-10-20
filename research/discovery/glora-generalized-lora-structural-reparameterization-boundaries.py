#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 683: GLoRA (Chavan et al., arXiv:2306.07967)."""

from __future__ import annotations

import math
import random


def matvec(M: list[list[float]], x: list[float]) -> list[float]:
    return [sum(row[j] * x[j] for j in range(len(x))) for row in M]


def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    m, k, n = len(A), len(A[0]), len(B[0])
    out = [[0.0] * n for _ in range(m)]
    for i in range(m):
        for r in range(k):
            air = A[i][r]
            for j in range(n):
                out[i][j] += air * B[r][j]
    return out


def hadamard_scale(W: list[list[float]], A_tensor: list[list[float]]) -> list[list[float]]:
    """Broadcasted scaling of W0 in R^{d2 x d1} by support tensor A in R^{d2 x d1}, R^{d2 x 1}, or R^{1 x 1}."""
    d2, d1 = len(W), len(W[0])
    a_rows, a_cols = len(A_tensor), len(A_tensor[0])
    out = [[0.0] * d1 for _ in range(d2)]
    for i in range(d2):
        ri = i if a_rows == d2 else 0
        for j in range(d1):
            cj = j if a_cols == d1 else 0
            out[i][j] = W[i][j] * A_tensor[ri][cj]
    return out


def vec_hadamard(v: list[float], d_tensor: list[float]) -> list[float]:
    n = len(v)
    if len(d_tensor) == n:
        return [v[i] * d_tensor[i] for i in range(n)]
    assert len(d_tensor) == 1
    return [v[i] * d_tensor[0] for i in range(n)]


def main() -> None:
    rng = random.Random(683)
    d1, d2, r_max = 12, 10, 4

    # 1. Verify search space cardinality (Section 2.2 Eq. 11 & Appendix E):
    # |A|=4, |B|=4, |C|=3, |D|=3, |E|=3 -> 4 * 4 * 3 * 3 * 3 = 432 configurations per linear layer
    space_A = ["LoRA", "vector", "scalar", "none"]
    space_B = ["LoRA", "vector", "scalar", "none"]
    space_C = ["LoRA", "vector", "none"]
    space_D = ["vector", "scalar", "none"]
    space_E = ["vector", "scalar", "none"]
    configs_per_layer = len(space_A) * len(space_B) * len(space_C) * len(space_D) * len(space_E)
    assert configs_per_layer == 432

    # 2. Verify Structural Re-parameterization Identity (Eq. 10, 12-14):
    # Training pass: f(x) = (W0 + W0 * A + B) x + C W0 + D b0 + E + b0
    # Re-parameterized inference pass: f_uni(x) = W_uni x + b_uni
    W0 = [[rng.gauss(0.0, 0.5) for _ in range(d1)] for _ in range(d2)]
    b0 = [rng.gauss(0.0, 0.3) for _ in range(d2)]

    # Supernet weight-entangled master tensors (Section 2.2)
    Ad = [[rng.gauss(0.0, 0.2) for _ in range(r_max)] for _ in range(d2)]
    Au = [[rng.gauss(0.0, 0.2) for _ in range(d1)] for _ in range(r_max)]
    Bd = [[rng.gauss(0.0, 0.2) for _ in range(r_max)] for _ in range(d2)]
    Bu = [[rng.gauss(0.0, 0.2) for _ in range(d1)] for _ in range(r_max)]
    Cd = [[rng.gauss(0.0, 0.2) for _ in range(r_max)] for _ in range(d1)]
    Cu = [[rng.gauss(0.0, 0.2)] for _ in range(r_max)]
    D_vec = [rng.gauss(0.0, 0.2) for _ in range(d2)]
    E_vec = [rng.gauss(0.0, 0.2) for _ in range(d2)]

    # Test subnet indexing with sub-rank r1 = 2 < r_max = 4
    r1 = 2
    Ad_r1 = [row[:r1] for row in Ad]
    Au_r1 = Au[:r1]
    A_lora = matmul(Ad_r1, Au_r1)  # d2 x d1
    B_lora = matmul([row[:r1] for row in Bd], Bu[:r1])  # d2 x d1
    c_prompt = [row[0] for row in matmul([row[:r1] for row in Cd], Cu[:r1])]  # d1 x 1 prompt vector

    # Evaluate unmerged training equation Eq. 10 vs merged Eq. 12-14 across 25 random inputs x
    W0_A = hadamard_scale(W0, A_lora)
    W_uni = [[W0[i][j] + W0_A[i][j] + B_lora[i][j] for j in range(d1)] for i in range(d2)]
    CW0 = matvec(W0, c_prompt)
    Db0 = vec_hadamard(b0, D_vec)
    b_uni = [CW0[i] + Db0[i] + E_vec[i] + b0[i] for i in range(d2)]

    max_reparam_err = 0.0
    for _ in range(25):
        x = [rng.gauss(0.0, 1.0) for _ in range(d1)]
        # Unmerged forward pass
        w0x = matvec(W0, x)
        w0ax = matvec(W0_A, x)
        bx = matvec(B_lora, x)
        y_train = [w0x[i] + w0ax[i] + bx[i] + CW0[i] + Db0[i] + E_vec[i] + b0[i] for i in range(d2)]
        # Re-parameterized single-matrix forward pass (0 extra inference FLOPs)
        w_uni_x = matvec(W_uni, x)
        y_infer = [w_uni_x[i] + b_uni[i] for i in range(d2)]
        err = max(abs(y_train[i] - y_infer[i]) for i in range(d2))
        max_reparam_err = max(max_reparam_err, err)

    assert max_reparam_err < 1e-14, f"Re-parameterization mismatch: {max_reparam_err}"

    # 3. Verify special-case degradation (Section 2.2: setting A=C=D=E=none and B=LoRA recovers standard LoRA)
    W_uni_lora_only = [[W0[i][j] + B_lora[i][j] for j in range(d1)] for i in range(d2)]
    b_uni_lora_only = b0[:]
    x_test = [rng.gauss(0.0, 1.0) for _ in range(d1)]
    y_lora = [matvec(W0, x_test)[i] + matvec(B_lora, x_test)[i] + b0[i] for i in range(d2)]
    y_glora_deg = [matvec(W_uni_lora_only, x_test)[i] + b_uni_lora_only[i] for i in range(d2)]
    deg_err = max(abs(y_lora[i] - y_glora_deg[i]) for i in range(d2))
    assert deg_err < 1e-15

    print(
        f"[PASS] Round 683 GLoRA (Chavan et al., 2023): "
        f"configs_per_layer={configs_per_layer}, max_reparam_err={max_reparam_err:.2e}, deg_err={deg_err:.2e}"
    )


if __name__ == "__main__":
    main()
