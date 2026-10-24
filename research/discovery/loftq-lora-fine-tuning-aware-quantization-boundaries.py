#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 658: LoftQ (Li et al., ICLR 2024)."""

import math
import random


def uniform_quantize_matrix(mat: list[list[float]], n_bits: int = 2) -> list[list[float]]:
    """Uniform symmetric/min-max N-bit simulated quantization q_N(W) (Section 2.2, Equations 1-3)."""
    flat = [v for row in mat for v in row]
    x_min = min(flat)
    x_max = max(flat)
    if x_max - x_min < 1e-12:
        return [list(row) for row in mat]
    levels = (1 << n_bits) - 1
    out = []
    for row in mat:
        q_row = []
        for v in row:
            norm = (v - x_min) / (x_max - x_min)
            q_int = round(levels * norm)
            q_val = x_min + (q_int / levels) * (x_max - x_min)
            q_row.append(q_val)
        out.append(q_row)
    return out


def power_iteration_svd_rank_r(mat: list[list[float]], r: int, iters: int = 80) -> tuple[list[list[float]], list[list[float]]]:
    """Compute rank-r approximation A_t B_t^T of residual R_t = W - Q_t via deflated power iteration."""
    d1 = len(mat)
    d2 = len(mat[0])
    res = [list(row) for row in mat]
    a_cols: list[list[float]] = []
    b_cols: list[list[float]] = []

    for k in range(r):
        v = [math.sin((j + 1) * (k + 2)) for j in range(d2)]
        v_norm = math.sqrt(sum(vj * vj for vj in v))
        v = [vj / v_norm for vj in v]
        for _ in range(iters):
            # u = res * v
            u = [sum(res[i][j] * v[j] for j in range(d2)) for i in range(d1)]
            u_norm = math.sqrt(sum(ui * ui for ui in u))
            if u_norm < 1e-12:
                break
            u = [ui / u_norm for ui in u]
            # v = res^T * u
            v = [sum(res[i][j] * u[i] for i in range(d1)) for j in range(d2)]
            v_norm = math.sqrt(sum(vj * vj for vj in v))
            if v_norm < 1e-12:
                break
            v = [vj / v_norm for vj in v]

        u_raw = [sum(res[i][j] * v[j] for j in range(d2)) for i in range(d1)]
        sigma = math.sqrt(sum(ui * ui for ui in u_raw))
        u_unit = [ui / sigma for ui in u_raw]
        sqrt_sigma = math.sqrt(sigma)
        a_cols.append([sqrt_sigma * ui for ui in u_unit])
        b_cols.append([sqrt_sigma * vj for vj in v])
        for i in range(d1):
            for j in range(d2):
                res[i][j] -= sigma * u_unit[i] * v[j]

    # A in R^{d1 x r}, B in R^{d2 x r}
    a_mat = [[a_cols[c][i] for c in range(r)] for i in range(d1)]
    b_mat = [[b_cols[c][j] for c in range(r)] for j in range(d2)]
    return a_mat, b_mat


def frobenius_error(w: list[list[float]], q: list[list[float]], a: list[list[float]], b: list[list[float]]) -> float:
    d1 = len(w)
    d2 = len(w[0])
    r = len(a[0])
    sq = 0.0
    for i in range(d1):
        for j in range(d2):
            ab_ij = sum(a[i][c] * b[j][c] for c in range(r))
            diff = w[i][j] - q[i][j] - ab_ij
            sq += diff * diff
    return math.sqrt(sq)


def verify_loftq_alternating_optimization() -> None:
    """Verify Algorithm 1 (Section 3.2): LoftQ strictly reduces ||W - Q_t - A_t B_t^T||_F over QLoRA (T=0)."""
    rng = random.Random(20231008)
    d1, d2, r = 12, 10, 2
    # Construct a heavy-tailed / outlier weight matrix W
    w = [[rng.gauss(0.0, 0.5) for _ in range(d2)] for _ in range(d1)]
    w[0][0] = 4.5
    w[3][4] = -3.8

    # T = 0 (QLoRA initialization): Q_0 = q_2(W), A_0 = 0, B_0 = 0
    q0 = uniform_quantize_matrix(w, n_bits=2)
    a0 = [[0.0 for _ in range(r)] for _ in range(d1)]
    b0 = [[0.0 for _ in range(r)] for _ in range(d2)]
    err_qlora = frobenius_error(w, q0, a0, b0)

    # Run LoftQ Algorithm 1 for T = 5 steps
    a_t, b_t = a0, b0
    errors = [err_qlora]
    for _ in range(5):
        # Step 1: Q_t = q_N(W - A_{t-1} B_{t-1}^T)
        w_minus_ab = [
            [w[i][j] - sum(a_t[i][c] * b_t[j][c] for c in range(r)) for j in range(d2)]
            for i in range(d1)
        ]
        q_t = uniform_quantize_matrix(w_minus_ab, n_bits=2)
        # Step 2: A_t, B_t = SVD_r(W - Q_t)
        residual = [[w[i][j] - q_t[i][j] for j in range(d2)] for i in range(d1)]
        a_t, b_t = power_iteration_svd_rank_r(residual, r=r)
        errors.append(frobenius_error(w, q_t, a_t, b_t))

    # Verify T=1 significantly reduces discrepancy vs QLoRA (T=0), and T=5 further reduces discrepancy!
    assert errors[1] < errors[0] * 0.65, f"LoftQ T=1 ({errors[1]:.4f}) must beat QLoRA ({errors[0]:.4f})"
    assert errors[-1] < errors[1], f"Alternating steps T=5 ({errors[-1]:.4f}) must improve over T=1 ({errors[1]:.4f})"


if __name__ == "__main__":
    verify_loftq_alternating_optimization()
    print("[PASS] Round 658 LoftQ boundary and mathematical verification succeeded.")
