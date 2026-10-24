#!/usr/bin/env python3
"""Constructed boundary verification for HyperGrid Transformers (Tay et al., ICLR 2021, arXiv:2007.05891)."""

import math


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def matvec(mat: list[list[float]], vec: list[float]) -> list[float]:
    return [sum(r_val * v_val for r_val, v_val in zip(row, vec)) for row in mat]


def outer_sigmoid(u: list[float], v: list[float]) -> list[list[float]]:
    return [[sigmoid(x * y) for y in v] for x in u]


def repeat_grid(grid: list[list[float]], dm: int, df: int) -> list[list[float]]:
    dr = len(grid)
    dc = len(grid[0])
    assert dm % dr == 0 and df % dc == 0
    rep_r = dm // dr
    rep_c = df // dc
    out = []
    for r in range(dr):
        expanded_row = []
        for c in range(dc):
            expanded_row.extend([grid[r][c]] * rep_c)
        for _ in range(rep_r):
            out.append(list(expanded_row))
    assert len(out) == dm and len(out[0]) == df
    return out


def verify_hypergrid_boundaries() -> None:
    # 1. Parameter Cost Formulas (Section 3.2, p. 5):
    dm = 768
    df = 3072
    dr = 32
    dc = 128

    cost_lg = dm * dr + dc
    cost_gl = dr + df * dc
    cost_l2 = dm * dr + df * dc
    assert cost_lg == 24704
    assert cost_gl == 393248
    assert cost_l2 == 417792
    assert cost_lg < cost_gl < cost_l2
    # Relative to single FFN matrix W in R^{dm x df} (2,359,296 params), LG adds only 1.05%!
    assert cost_lg / (dm * df) < 0.011

    # 2. Decomposable Gridwise Projections: L^2 (Eq. 3), LG (Eq. 4), GL (Eq. 5), and Residual FFN (Eq. 6):
    dm_s = 6
    df_s = 8
    dr_s = 2
    dc_s = 4

    X = [0.4, -0.3, 0.7, 0.2, -0.5, 0.6]
    W = [[0.1 * ((i + 1) - 0.3 * (j + 1)) for j in range(df_s)] for i in range(dm_s)]

    Lr = [[0.25 * ((r + 1) + 0.2 * (c + 1)) for c in range(dm_s)] for r in range(dr_s)]
    Lc = [[-0.2 * ((r + 1) - 0.3 * (c + 1)) for c in range(dm_s)] for r in range(dc_s)]
    Gr = [0.5, -0.4]
    Gc = [0.3, -0.2, 0.6, 0.1]

    lr_x = matvec(Lr, X)
    lc_x = matvec(Lc, X)

    # Eq. 3 (L^2), Eq. 4 (LG), Eq. 5 (GL)
    gate_l2 = repeat_grid(outer_sigmoid(lr_x, lc_x), dm_s, df_s)
    gate_lg = repeat_grid(outer_sigmoid(lr_x, Gc), dm_s, df_s)
    gate_gl = repeat_grid(outer_sigmoid(Gr, lc_x), dm_s, df_s)

    for gate in (gate_l2, gate_lg, gate_gl):
        assert len(gate) == dm_s and len(gate[0]) == df_s
        assert all(0.0 < val < 1.0 for row in gate for val in row)
        # Verify blockwise constancy within each (dm_s // dr_s) x (df_s // dc_s) = 3 x 2 block
        for br in range(dr_s):
            for bc in range(dc_s):
                v0 = gate[br * 3][bc * 2]
                for r_off in range(3):
                    for c_off in range(2):
                        assert abs(gate[br * 3 + r_off][bc * 2 + c_off] - v0) < 1e-15

    # Eq. 6: Residual HyperGrid transformation Y_i = H_i(X, W) + W(X)
    H_lg_W = [[gate_lg[i][j] * W[i][j] for j in range(df_s)] for i in range(dm_s)]
    Y_res = [
        sum(H_lg_W[i][j] * X[i] for i in range(dm_s)) + sum(W[i][j] * X[i] for i in range(dm_s))
        for j in range(df_s)
    ]
    Y_combined = [
        sum((1.0 + gate_lg[i][j]) * W[i][j] * X[i] for i in range(dm_s))
        for j in range(df_s)
    ]
    max_res_err = max(abs(a - b) for a, b in zip(Y_res, Y_combined))
    assert max_res_err < 1e-15

    # 3. Distinction between Pre-ReLU Weight Gating and Post-ReLU Output Gating (Section 7.3, Eq. 7):
    # With bias b != 0, ReLU((G odot W)^T X + b) != ReLU(W^T X + b) odot g_out
    bias = [-0.15, 0.2, -0.05, 0.1, -0.25, 0.3, -0.1, 0.05]
    pre_relu_gated = [
        max(sum(H_lg_W[i][j] * X[i] for i in range(dm_s)) + bias[j], 0.0)
        for j in range(df_s)
    ]
    post_relu_gated = [
        max(sum(W[i][j] * X[i] for i in range(dm_s)) + bias[j], 0.0) * gate_lg[0][j]
        for j in range(df_s)
    ]
    gating_diff = max(abs(a - b) for a, b in zip(pre_relu_gated, post_relu_gated))
    assert gating_diff > 1e-3

    print(
        f"[PASS] HyperGrid boundaries verified: cost_lg={cost_lg} < cost_gl={cost_gl} < cost_l2={cost_l2}, "
        f"max_res_err={max_res_err:.2e}, gating_diff={gating_diff:.4f}"
    )


if __name__ == "__main__":
    verify_hypergrid_boundaries()
