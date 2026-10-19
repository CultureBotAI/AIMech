"""Constructed boundary and numerical verification for Round 439:
FedPara and pFedPara: Low-Rank Hadamard Product Parameterization
(Nam Hyeon-Woo, Moon Ye-Bin, & Tae-Hyun Oh 2022, ICLR 2022, arXiv:2108.06098).
"""

from __future__ import annotations

import math
import random


def mat_mul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    m = len(A)
    k_dim = len(A[0])
    n = len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(k_dim)) for j in range(n)] for i in range(m)]


def hadamard(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    return [[A[i][j] * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matrix_rank(M: list[list[float]], tol: float = 1e-9) -> int:
    A = [row[:] for row in M]
    m, n = len(A), len(A[0])
    rank = 0
    for col in range(n):
        pivot = None
        for row in range(rank, m):
            if abs(A[row][col]) > tol:
                pivot = row
                break
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        piv_val = A[rank][col]
        for j in range(col, n):
            A[rank][j] /= piv_val
        for row in range(m):
            if row != rank and abs(A[row][col]) > tol:
                factor = A[row][col]
                for j in range(col, n):
                    A[row][j] -= factor * A[rank][j]
        rank += 1
    return rank


def main() -> None:
    rng = random.Random(439)
    m, n = 16, 16
    r1, r2 = 4, 4  # R = 4 -> R^2 = 16 = min(m, n)

    X1 = [[rng.gauss(0.0, 1.0) for _ in range(r1)] for _ in range(m)]
    Y1_T = [[rng.gauss(0.0, 1.0) for _ in range(n)] for _ in range(r1)]
    X2 = [[rng.gauss(0.0, 1.0) for _ in range(r2)] for _ in range(m)]
    Y2_T = [[rng.gauss(0.0, 1.0) for _ in range(n)] for _ in range(r2)]

    W1 = mat_mul(X1, Y1_T)
    W2 = mat_mul(X2, Y2_T)
    W_fedpara = hadamard(W1, W2)

    rank_W1 = matrix_rank(W1)
    rank_W2 = matrix_rank(W2)
    rank_fedpara = matrix_rank(W_fedpara)

    # Proposition 1: rank(W1) <= r1, rank(W2) <= r2, but rank(W1 o W2) = r1 * r2 = 16 (full rank!)
    assert rank_W1 == r1 and rank_W2 == r2
    assert rank_fedpara == r1 * r2 == 16

    # Parameter efficiency comparison with standard low-rank factorization W_lr = X Y^T
    # Under equal parameter budget 2*R*(m+n) = 256, standard factorization has rank r_lr = 2*R = 8 < 16
    params_fedpara = (r1 + r2) * (m + n)
    r_lr_same_budget = r1 + r2
    X_lr = [[rng.gauss(0.0, 1.0) for _ in range(r_lr_same_budget)] for _ in range(m)]
    Y_lr_T = [[rng.gauss(0.0, 1.0) for _ in range(n)] for _ in range(r_lr_same_budget)]
    W_lr = mat_mul(X_lr, Y_lr_T)
    rank_lr = matrix_rank(W_lr)
    assert rank_lr == r_lr_same_budget == 8 < rank_fedpara

    # Proposition 2: For fixed rank product r1 * r2 = R^2 = 16, r1 = r2 = R = 4 uniquely minimizes (r1 + r2)(m + n)
    for pair in [(1, 16), (2, 8), (4, 4), (8, 2), (16, 1)]:
        assert (pair[0] + pair[1]) * (m + n) >= params_fedpara

    # pFedPara decomposition (Section 2.3, Eq. 4): W = W1 o (W2 + 1) = W1 o W2 + W1
    W_pfedpara = [[W1[i][j] * (W2[i][j] + 1.0) for j in range(n)] for i in range(m)]
    decomp_err = math.sqrt(
        sum((W_pfedpara[i][j] - (W_fedpara[i][j] + W1[i][j])) ** 2 for i in range(m) for j in range(n))
    )
    assert decomp_err < 1e-14

    print(
        f"[PASS] Round 439 FedPara & pFedPara (Hyeon-Woo et al. 2022): "
        f"rank(W1)={rank_W1}, rank(W2)={rank_W2} -> rank(W1 o W2)={rank_fedpara} (full rank) "
        f"vs equal-budget low-rank={rank_lr}, params={params_fedpara}"
    )


if __name__ == "__main__":
    main()
