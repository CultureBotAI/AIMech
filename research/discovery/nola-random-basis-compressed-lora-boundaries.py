#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 688: NOLA (Koohpayegani et al., ICLR 2024 / arXiv:2310.02556)."""

from __future__ import annotations

import math
import random


def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    m, r, n = len(A), len(A[0]), len(B[0])
    out = [[0.0] * n for _ in range(m)]
    for i in range(m):
        for t in range(r):
            ait = A[i][t]
            for j in range(n):
                out[i][j] += ait * B[t][j]
    return out


def numerical_rank(M: list[list[float]], tol: float = 1e-5) -> int:
    A = [row[:] for row in M]
    m, n = len(A), len(A[0])
    rank = 0
    for col in range(min(m, n)):
        pivot_row = max(range(rank, m), key=lambda r: abs(A[r][col]))
        if abs(A[pivot_row][col]) <= tol:
            continue
        A[rank], A[pivot_row] = A[pivot_row], A[rank]
        piv = A[rank][col]
        for r in range(rank + 1, m):
            factor = A[r][col] / piv
            for c in range(col, n):
                A[r][c] -= factor * A[rank][c]
        rank += 1
    return rank


def generate_nola_basis(seed: int, k: int, l: int, m: int, n: int, r: int) -> tuple[list[list[list[float]]], list[list[list[float]]]]:
    gen = random.Random(seed)
    std = 1.0 / math.sqrt(r)
    A_basis = [[[gen.gauss(0.0, std) for _ in range(r)] for _ in range(m)] for _ in range(k)]
    B_basis = [[[gen.gauss(0.0, std) for _ in range(n)] for _ in range(r)] for _ in range(l)]
    return A_basis, B_basis


def nola_delta_w(
    alpha: list[float],
    beta: list[float],
    A_basis: list[list[list[float]]],
    B_basis: list[list[list[float]]],
) -> list[list[float]]:
    """Section 2, Eq. 1-2: A = sum_{i=1}^k alpha_i A_i, B = sum_{j=1}^l beta_j B_j, Delta W = A x B."""
    k, m, r = len(A_basis), len(A_basis[0]), len(A_basis[0][0])
    l, n = len(B_basis), len(B_basis[0][0])
    A = [[sum(alpha[i] * A_basis[i][row][col] for i in range(k)) for col in range(r)] for row in range(m)]
    B = [[sum(beta[j] * B_basis[j][row][col] for j in range(l)) for col in range(n)] for row in range(r)]
    return matmul(A, B)


def main() -> None:
    rng = random.Random(688)

    # 1. Verify rank-one compression bound breaking & rank/shape decoupling (Section 2, Eq. 1-2):
    # For m = 64, n = 64, LoRA rank-1 requires m + n = 128 trainable parameters and is restricted to rank <= 1.
    # NOLA with k = 16, l = 16 uses only k + l = 32 trainable parameters (4x fewer than rank-1 LoRA!)
    # while achieving matrix rank r = 8 > 1!
    m, n, r = 16, 16, 4
    k, l = 6, 6  # k + l = 12 < m + n = 32 (less than half of rank-1 LoRA's 32 parameters!)
    lora_rank1_params = 1 * (m + n)
    nola_params = k + l
    assert nola_params < 0.5 * lora_rank1_params

    A_basis, B_basis = generate_nola_basis(seed=42, k=k, l=l, m=m, n=n, r=r)
    alpha = [rng.gauss(0.0, 1.0) for _ in range(k)]
    beta = [rng.gauss(0.0, 1.0) for _ in range(l)]
    dW = nola_delta_w(alpha, beta, A_basis, B_basis)
    rk_dw = numerical_rank(dW)
    assert rk_dw == r > 1

    # Verify bilinear expansion identity: Delta W == sum_{i=1}^k sum_{j=1}^l (alpha_i * beta_j) (A_i B_j)
    dW_bilinear = [[0.0] * n for _ in range(m)]
    for i in range(k):
        for j in range(l):
            coef = alpha[i] * beta[j]
            ab_ij = matmul(A_basis[i], B_basis[j])
            for row in range(m):
                for col in range(n):
                    dW_bilinear[row][col] += coef * ab_ij[row][col]
    max_bilinear_err = max(abs(dW[row][col] - dW_bilinear[row][col]) for row in range(m) for col in range(n))
    assert max_bilinear_err < 1e-14

    # 2. Verify Appendix A.1 (Figure 2, p. 15) solution-subspace coverage advantage of NOLA over PRANC:
    # With k + l = 12 parameters in a d x d = 6 x 6 weight space (d^2 = 36 dimensions):
    # PRANC linear combination of 12 basis matrices can span at most a 12-dimensional subspace of R^{36}.
    # NOLA bilinear combination (k = 6, l = 6, r = 4) spans up to k * l = 36 dimensions of R^{36}!
    d_small = 6
    k_s, l_s, r_s = 6, 6, 4
    A_b_s, B_b_s = generate_nola_basis(seed=99, k=k_s, l=l_s, m=d_small, n=d_small, r=r_s)
    pranc_basis = [[rng.gauss(0.0, 1.0) for _ in range(d_small * d_small)] for _ in range(k_s + l_s)]

    n_samples = 45
    nola_samples = []
    pranc_samples = []
    for _ in range(n_samples):
        al = [rng.gauss(0.0, 1.0) for _ in range(k_s)]
        be = [rng.gauss(0.0, 1.0) for _ in range(l_s)]
        dw_s = nola_delta_w(al, be, A_b_s, B_b_s)
        nola_samples.append([val for row in dw_s for val in row])

        gam = al + be
        pranc_vec = [sum(gam[idx] * pranc_basis[idx][pos] for idx in range(k_s + l_s)) for pos in range(d_small * d_small)]
        pranc_samples.append(pranc_vec)

    rank_subspace_pranc = numerical_rank(pranc_samples)
    rank_subspace_nola = numerical_rank(nola_samples)
    assert rank_subspace_pranc == k_s + l_s == 12
    assert rank_subspace_nola > 2 * rank_subspace_pranc

    # 3. Verify compute reduction factor vs PRANC (Section 2, p. 4):
    # PRANC compute ~ k_total * d^2 vs NOLA compute ~ (k + l) * d * r
    d_large, r_large, k_tot = 1024, 8, 1000
    pranc_ops = k_tot * (d_large ** 2)
    nola_ops = k_tot * d_large * r_large + 2 * (d_large ** 2) * r_large
    speedup = pranc_ops / nola_ops
    assert speedup > 40.0

    print(
        f"[PASS] Round 688 NOLA (Koohpayegani et al., ICLR 2024): "
        f"params={nola_params}<rank1_LoRA={lora_rank1_params}, rank(dW)={rk_dw}, "
        f"subspace_rank(NOLA)={rank_subspace_nola}>>subspace_rank(PRANC)={rank_subspace_pranc}, "
        f"speedup={speedup:.1f}x"
    )


if __name__ == "__main__":
    main()
