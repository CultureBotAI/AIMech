"""Constructed boundary verification for Round 543: Short-Dot Codes (Dutta, Cadambe, & Grover, NeurIPS 2016 / IEEE TIT 2019)."""

from __future__ import annotations

import itertools
import math


def invert_matrix(mat: list[list[float]]) -> list[list[float]]:
    n = len(mat)
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(mat)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(aug[r][col]))
        aug[col], aug[piv] = aug[piv], aug[col]
        div = aug[col][col]
        for j in range(col, 2 * n):
            aug[col][j] /= div
        for r in range(n):
            if r != col and aug[r][col] != 0.0:
                factor = aug[r][col]
                for j in range(col, 2 * n):
                    aug[r][j] -= factor * aug[col][j]
    return [row[n:] for row in aug]


def mat_vec(mat: list[list[float]], vec: list[float]) -> list[float]:
    return [sum(r[j] * vec[j] for j in range(len(vec))) for r in mat]


def main() -> None:
    # Algorithm 1 (p. 7): Compute A x where A is M x N across P processors with recovery threshold K
    N = 12
    P = 6
    M = 2
    K = 4
    expected_s = (N // P) * (P - K + M)  # (12/6)*(6 - 4 + 2) = 8 < 12
    assert expected_s == 8

    # Construct M x N matrix A and input vector x in R^N
    A = [
        [0.5 * (j + 1) if j % 2 == 0 else -0.3 * (j + 1) for j in range(N)],
        [1.2 - 0.1 * j for j in range(N)],
    ]
    x = [0.25 * (j + 1) - 1.0 for j in range(N)]
    true_Ax = mat_vec(A, x)

    # Vandermonde matrix B of size P x K (Eq. 18, p. 12): B[i][c] = h_i^(K - 1 - c)
    hs = [1.0 + 0.5 * i for i in range(P)]
    B = [[hs[i] ** (K - 1 - c) for c in range(K)] for i in range(P)]

    # Pre-processing: Encode F (P x N) column by column (Algorithm 1, Step [A], p. 7)
    F_cols: list[list[float]] = []
    for j in range(N):
        # 0-based cyclic set U of size K - M = 2
        U = [(j + offset) % P for offset in range(K - M)]
        B_U_first = [[B[u][c] for c in range(M)] for u in U]
        B_U_last = [[B[u][c] for c in range(M, K)] for u in U]
        A_j = [A[r][j] for r in range(M)]
        rhs = [-val for val in mat_vec(B_U_first, A_j)]
        z_j = mat_vec(invert_matrix(B_U_last), rhs)
        a_tilde_j = A_j + z_j
        f_j = mat_vec(B, a_tilde_j)
        # Enforce exact numerical zeros at U
        for u in U:
            assert abs(f_j[u]) < 1e-10
            f_j[u] = 0.0
        F_cols.append(f_j)

    # Transpose F_cols to row representation F (P x N)
    F = [[F_cols[j][i] for j in range(N)] for i in range(P)]

    # Verify Theorem 1 (p. 5): every row of F has sparsity at most s = N(P - K + M)/P = 8
    row_sparsities = [sum(1 for val in row if abs(val) > 1e-12) for row in F]
    assert all(sp <= expected_s for sp in row_sparsities), f"Row sparsities: {row_sparsities}"
    assert max(row_sparsities) == expected_s

    # Verify converse lower bound (Theorem 2, Eq. 5, p. 8): s_bar >= (N/P)*(P - K + 1)
    s_converse = (N / P) * (P - K + 1)
    assert sum(row_sparsities) / P >= s_converse

    # Online computation: each processor i computes short dot product <f_i^{S_i}, x^{S_i}>
    proc_outputs = []
    for i in range(P):
        support = [j for j in range(N) if abs(F[i][j]) > 1e-12]
        assert len(support) == expected_s
        short_dot = sum(F[i][j] * x[j] for j in support)
        proc_outputs.append(short_dot)

    # Fusion node decoding: verify exact recovery of Ax from ALL (P choose K) = 15 subsets of K processors
    max_err = 0.0
    for V in itertools.combinations(range(P), K):
        B_V = [B[i] for i in V]
        v_V = [proc_outputs[i] for i in V]
        w = mat_vec(invert_matrix(B_V), v_V)
        recovered_Ax = w[:M]
        err = max(abs(recovered_Ax[r] - true_Ax[r]) for r in range(M))
        if err > max_err:
            max_err = err
    assert max_err < 1e-9, f"Short-Dot decoding failed with max_err={max_err}"

    # Verify expected time reduction in sub-linear regime M = P / ln(P) (Theorem 4, Eq. 13-17, p. 10-12)
    P_large = 1000
    M_large = int(P_large / math.log(P_large))
    K_large = P_large - M_large // 2
    mu = 2.0
    t_sd_scaled = ((P_large - K_large + M_large) / P_large) * (
        1.0 + math.log(P_large / (P_large - K_large)) / mu
    )
    t_mds_scaled = 1.0 + math.log(P_large / (P_large - M_large)) / mu
    assert t_sd_scaled < 0.5 * t_mds_scaled

    print(
        f"[PASS] Round 543 Short-Dot verified: row_sparsity={expected_s}/{N}, "
        f"max_err={max_err:.2e} across all 15 K-subsets, "
        f"E[T_SD]/N={t_sd_scaled:.3f} < E[T_MDS]/N={t_mds_scaled:.3f}"
    )


if __name__ == "__main__":
    main()
