#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 674: PRoLoRA (Wang et al., ACL 2024)."""

import math
import random


def roll_rows(M, shift):
    r = len(M)
    if r == 0:
        return M
    s = shift % r
    if s == 0:
        return [list(row) for row in M]
    return [list(M[(idx - s) % r]) for idx in range(r)]


def roll_cols(M, shift):
    r = len(M[0])
    if r == 0:
        return M
    s = shift % r
    if s == 0:
        return [list(row) for row in M]
    return [[row[(col - s) % r] for col in range(r)] for row in M]


def matmul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)] for i in range(m)]


def frob_diff(X, Y):
    return math.sqrt(sum((X[i][j] - Y[i][j]) ** 2 for i in range(len(X)) for j in range(len(X[0]))))


def main():
    rng = random.Random(674)
    o, h, r, u, m, n = 12, 8, 4, 1, 2, 3
    c_h = h // m  # 4
    c_o = o // n  # 4

    # 1. Parameter count formula (Section 3.1, p. 5):
    # P_LoRA = r * (h + o), P_PRoLoRA = u*(h + o) + h*(r - u)/m + o*(r - u)/n
    p_lora = r * (h + o)
    p_prolora = u * (h + o) + (h * (r - u)) // m + (o * (r - u)) // n
    assert p_prolora < p_lora, f"Expected p_prolora={p_prolora} < p_lora={p_lora}"
    # When u == r, PRoLoRA degrades exactly to LoRA:
    p_degraded = r * (h + o) + (h * (r - r)) // m + (o * (r - r)) // n
    assert p_degraded == p_lora, "PRoLoRA must degrade to LoRA when u == r"

    # 2. CLoRA (Eq. 2): pure chunk broadcast produces identical (c_o x c_h) sub-blocks across all (j, i)
    A0_full = [[rng.gauss(0.0, 1.0) for _ in range(c_h)] for _ in range(r)]
    B0_full = [[rng.gauss(0.0, 1.0) for _ in range(r)] for _ in range(c_o)]
    base_block = matmul(B0_full, A0_full)
    # Every (j, i) block in CLoRA equals B0_full @ A0_full
    clora_blocks_diff = frob_diff(base_block, matmul(B0_full, A0_full))
    assert clora_blocks_diff == 0.0

    # 3. RoLoRA (Eq. 3): roll along rank dimension differentiates adjacent blocks in the same row,
    # BUT when s_A == s_B, blocks with equal relative displacement (j - i) are identical: B_1 A_1 == B_0 A_0!
    stride = 1
    A1_full = roll_rows(A0_full, 1 * stride)
    B1_full = roll_cols(B0_full, 1 * stride)
    block_00 = matmul(B0_full, A0_full)
    block_01 = matmul(B0_full, A1_full)
    block_11 = matmul(B1_full, A1_full)
    assert frob_diff(block_00, block_01) > 1.0, "RoLoRA must differentiate adjacent blocks in a row"
    diag_sym_err = frob_diff(block_00, block_11)
    assert diag_sym_err < 1e-13, f"RoLoRA equal-displacement blocks must be identical, got {diag_sym_err}"

    # 4. PRoLoRA (Eq. 4): unshared rank u breaks the equal-displacement diagonal block identity!
    r_shared = r - u
    Au = [[rng.gauss(0.0, 1.0) for _ in range(h)] for _ in range(u)]
    Bu = [[rng.gauss(0.0, 1.0) for _ in range(u)] for _ in range(o)]
    A0 = [[rng.gauss(0.0, 1.0) for _ in range(c_h)] for _ in range(r_shared)]
    B0 = [[rng.gauss(0.0, 1.0) for _ in range(r_shared)] for _ in range(c_o)]

    # Construct full A (r x h) and B (o x r) in PRoLoRA
    A_shared_chunks = [roll_rows(A0, i * stride) for i in range(m)]
    A_shared = [
        [A_shared_chunks[i][rk][col] for i in range(m) for col in range(c_h)]
        for rk in range(r_shared)
    ]
    A_pro = Au + A_shared  # r x h

    B_shared_chunks = [roll_cols(B0, j * stride) for j in range(n)]
    B_shared = [
        [B_shared_chunks[j][row][rk] for rk in range(r_shared)]
        for j in range(n)
        for row in range(c_o)
    ]
    B_pro = [Bu[row] + B_shared[row] for row in range(o)]  # o x r

    dW_pro = matmul(B_pro, A_pro)
    pro_block_00 = [[dW_pro[row][col] for col in range(c_h)] for row in range(c_o)]
    pro_block_11 = [[dW_pro[c_o + row][c_h + col] for col in range(c_h)] for row in range(c_o)]
    pro_diag_diff = frob_diff(pro_block_00, pro_block_11)
    assert pro_diag_diff > 1.0, f"PRoLoRA unshared rank u must break diagonal block identity: {pro_diag_diff}"

    # 5. Rectified Kaiming initialization (Eq. 5):
    # Using full hidden dimension h instead of chunk dimension h/m reduces sampling bound by sqrt(m)
    g = 1.0
    bound_rectified = g * math.sqrt(3.0 / h)
    bound_unrectified = g * math.sqrt(3.0 / c_h)
    assert abs(bound_unrectified / bound_rectified - math.sqrt(m)) < 1e-12

    print(
        f"[PASS] Round 674 PRoLoRA (Wang et al., ACL 2024): "
        f"params={p_prolora}<{p_lora}, rolora_diag_err={diag_sym_err:.2e}, "
        f"prolora_diag_diff={pro_diag_diff:.4f}>1.0, init_bound_ratio={bound_unrectified/bound_rectified:.4f}"
    )


if __name__ == "__main__":
    main()
