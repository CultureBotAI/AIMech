#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 679: KronA (Edalati et al., 2022)."""

import math
import random


def kronecker(A, B):
    a1, a2 = len(A), len(A[0])
    b1, b2 = len(B), len(B[0])
    W = [[0.0 for _ in range(a2 * b2)] for _ in range(a1 * b1)]
    for i in range(a1):
        for j in range(a2):
            aij = A[i][j]
            for p in range(b1):
                for q in range(b2):
                    W[i * b1 + p][j * b2 + q] = aij * B[p][q]
    return W


def matvec(M, x):
    return [sum(M[i][j] * x[j] for j in range(len(x))) for i in range(len(M))]


def matmul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)] for i in range(m)]


def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def reshape_col_major(x, rows, cols):
    # eta_{rows x cols}(x) in column-major order matching vec() / gamma() stacking columns
    M = [[0.0 for _ in range(cols)] for _ in range(rows)]
    for c in range(cols):
        for r in range(rows):
            M[r][c] = x[c * rows + r]
    return M


def vec_col_major(Y):
    # gamma(Y) stacks columns of Y into a vector
    rows, cols = len(Y), len(Y[0])
    out = []
    for c in range(cols):
        for r in range(rows):
            out.append(Y[r][c])
    return out


def main():
    rng = random.Random(679)
    a1, a2 = 4, 3
    b1, b2 = 3, 4
    d_h = a1 * b1  # 12 == a2 * b2

    Ak = [[rng.gauss(0.0, 1.0) for _ in range(a2)] for _ in range(a1)]
    Bk = [[rng.gauss(0.0, 1.0) for _ in range(b2)] for _ in range(b1)]
    x = [rng.gauss(0.0, 1.0) for _ in range(d_h)]

    # 1. Verify Eq. (2) fast Kronecker-vector product identity:
    # (A_k (x) B_k) x == gamma(B_k * eta_{b2 x a2}(x) * A_k^T)
    W_kron = kronecker(Ak, Bk)
    y_direct = matvec(W_kron, x)

    X_mat = reshape_col_major(x, b2, a2)
    Y_mat = matmul(matmul(Bk, X_mat), transpose(Ak))
    y_fast = vec_col_major(Y_mat)

    vec_identity_err = math.sqrt(sum((y_direct[i] - y_fast[i]) ** 2 for i in range(d_h)))
    assert vec_identity_err < 1e-13, f"Eq. (2) Kronecker-vec identity failed: {vec_identity_err}"

    # 2. Verify parameter count & FLOP reduction (Appendix A, Table 3, p. 6):
    # For T5-base d_h = 768 with A_k of shape (32, 24) and B_k of shape (24, 32):
    dh_t5 = 768
    a1_t5, a2_t5, b1_t5, b2_t5 = 32, 24, 24, 32
    assert a1_t5 * b1_t5 == dh_t5 and a2_t5 * b2_t5 == dh_t5
    params_krona = a1_t5 * a2_t5 + b1_t5 * b2_t5  # 1536
    params_lora_r1 = 2 * dh_t5 * 1  # 1536
    assert params_krona == params_lora_r1 == 1536

    # 3. Verify full-rank preservation of Kronecker product vs rank-1 LoRA:
    # For square full-rank A_sq (3x3) and B_sq (4x4), rank(A_sq (x) B_sq) = 3 * 4 = 12,
    # whereas LoRA with the same parameter count (2 * 12 * 1 = 24 vs 9 + 16 = 25) has rank 1!
    A_diag = [[float(i + 1) if i == j else 0.0 for j in range(3)] for i in range(3)]
    B_diag = [[float(i + 2) if i == j else 0.0 for j in range(4)] for i in range(4)]
    K_diag = kronecker(A_diag, B_diag)
    nonzero_diag = sum(1 for i in range(12) if abs(K_diag[i][i]) > 1e-9)
    assert nonzero_diag == 12, f"Expected full rank 12 for Kronecker product, got {nonzero_diag}"

    # 4. Verify Eq. (4) weight merging for linear KronA:
    W0 = [[rng.gauss(0.0, 0.5) for _ in range(d_h)] for _ in range(d_h)]
    s = 2.5
    W_tuned = [[W0[i][j] + s * W_kron[i][j] for j in range(d_h)] for i in range(d_h)]
    y_unmerged = [matvec(W0, x)[i] + s * y_fast[i] for i in range(d_h)]
    y_merged = matvec(W_tuned, x)
    merge_err = math.sqrt(sum((y_unmerged[i] - y_merged[i]) ** 2 for i in range(d_h)))
    assert merge_err < 1e-13, f"Eq. (4) KronA merge error failed: {merge_err}"

    print(
        f"[PASS] Round 679 KronA (Edalati et al., 2022): "
        f"vec_identity_err={vec_identity_err:.2e}, rank_kron={nonzero_diag}>rank_lora=1 "
        f"(params={params_krona}), merge_err={merge_err:.2e}"
    )


if __name__ == "__main__":
    main()
