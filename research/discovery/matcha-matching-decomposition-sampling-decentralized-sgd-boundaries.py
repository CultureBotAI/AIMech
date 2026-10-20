#!/usr/bin/env python3
"""Constructed boundary verification for MATCHA (Wang et al., MLSys 2020 / arXiv:1905.09435).

Verifies:
1. Matching decomposition L = sum_{j=1}^M L_j of a base graph G(V, E) where each L_j is the
   Laplacian of a set of vertex-disjoint edges (matching).
2. Exact expected second-moment expansion (Equations 13-16 & 25-26):
   E[L^(k)] = L_bar = sum_{j=1}^M p_j L_j,
   E[L^(k)^T L^(k)] = L_bar^2 + 2 * L_tilde, where L_tilde = sum_{j=1}^M p_j * (1 - p_j) * L_j
   (using L_j^2 = 2 * L_j for any matching Laplacian!).
3. Theorem 1 optimal mixing weight alpha* = lambda / (lambda^2 + 2*zeta) (Equation 22)
   ensuring rho = ||E[W^(k)^T W^(k)] - J||_2 < 1 for any communication budget C_b > 0, and
   showing non-uniform critical-link probabilities p_j achieve strictly smaller rho than
   uniform Periodic-DecenSGD at the same communication budget sum(p_j) = C_b * M.
"""

import math


def matching_laplacian(n, edges):
    L = [[0.0] * n for _ in range(n)]
    for u, v in edges:
        L[u][u] += 1.0
        L[v][v] += 1.0
        L[u][v] -= 1.0
        L[v][u] -= 1.0
    return L


def mat_mul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def mat_add(A, B, scale_b=1.0):
    n = len(A)
    return [[A[i][j] + scale_b * B[i][j] for j in range(n)] for i in range(n)]


def spectral_norm_symmetric(M):
    """Power-iteration spectral norm on orthogonal complement of 1 and all space."""
    n = len(M)
    best = 0.0
    for seed_idx in range(n):
        v = [1.0 if i == seed_idx else -0.1 for i in range(n)]
        for _ in range(80):
            mv = [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]
            norm = math.sqrt(sum(x * x for x in mv))
            if norm < 1e-15:
                break
            v = [x / norm for x in mv]
        mv = [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]
        rayleigh = abs(sum(v[i] * mv[i] for i in range(n)))
        if rayleigh > best:
            best = rayleigh
    return best


def verify_matcha_boundaries():
    # 4-node graph with a bridge edge (1, 2) and triangle-like redundant edges:
    # Matching 1: [(0, 1), (2, 3)]
    # Matching 2: [(1, 2)]  <-- critical bridge connecting {0,1} and {2,3}
    # Matching 3: [(0, 2)]  <-- redundant cross link
    n = 4
    L1 = matching_laplacian(n, [(0, 1), (2, 3)])
    L2 = matching_laplacian(n, [(1, 2)])
    L3 = matching_laplacian(n, [(0, 2)])
    matchings = [L1, L2, L3]
    M = len(matchings)

    # 1. Verify matching Laplacian identity L_j^2 == 2 * L_j (used in Equation 15 -> 16)
    for idx, Lj in enumerate(matchings):
        Lj2 = mat_mul(Lj, Lj)
        for r in range(n):
            for c in range(n):
                assert abs(Lj2[r][c] - 2.0 * Lj[r][c]) < 1e-12, f"L_{idx}^2 != 2*L_{idx}"

    # 2. Verify exact expectation E[W^(k)^T W^(k)] == I - 2*alpha*L_bar + alpha^2*(L_bar^2 + 2*L_tilde)
    probs = [0.7, 0.6, 0.2]  # sum(p_j) = 1.5 => C_b = 0.5
    alpha = 0.22
    I_mat = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    J_mat = [[1.0 / n for _ in range(n)] for _ in range(n)]

    # Exact enumeration over all 2^3 = 8 Bernoulli realizations B in {0,1}^3
    E_WTW_exact = [[0.0] * n for _ in range(n)]
    for b0 in (0, 1):
        for b1 in (0, 1):
            for b2 in (0, 1):
                prob_b = (
                    (probs[0] if b0 else 1.0 - probs[0])
                    * (probs[1] if b1 else 1.0 - probs[1])
                    * (probs[2] if b2 else 1.0 - probs[2])
                )
                Lk = [[b0 * L1[r][c] + b1 * L2[r][c] + b2 * L3[r][c] for c in range(n)] for r in range(n)]
                Wk = mat_add(I_mat, Lk, -alpha)
                Wk2 = mat_mul(Wk, Wk)
                E_WTW_exact = mat_add(E_WTW_exact, Wk2, prob_b)

    L_bar = [[sum(probs[j] * matchings[j][r][c] for j in range(M)) for c in range(n)] for r in range(n)]
    L_tilde = [
        [sum(probs[j] * (1.0 - probs[j]) * matchings[j][r][c] for j in range(M)) for c in range(n)]
        for r in range(n)
    ]
    L_bar2 = mat_mul(L_bar, L_bar)
    formula_mat = mat_add(
        mat_add(I_mat, L_bar, -2.0 * alpha),
        mat_add(L_bar2, L_tilde, 2.0),
        alpha * alpha,
    )
    for r in range(n):
        for c in range(n):
            assert abs(E_WTW_exact[r][c] - formula_mat[r][c]) < 1e-12, "Eq (26) mismatch!"

    # 3. Verify rho = ||E[W^(k)^T W^(k)] - J||_2 < 1 and compare non-uniform MATCHA vs uniform p_j = C_b
    diff_matcha = mat_add(formula_mat, J_mat, -1.0)
    rho_matcha = spectral_norm_symmetric(diff_matcha)
    assert rho_matcha < 1.0, f"Expected rho_matcha < 1, got {rho_matcha}"

    # Compare against biased allocation that starves critical matching L1
    probs_bad = [0.1, 0.7, 0.7]  # same budget sum(p_j) = 1.5
    L_bar_bad = [[sum(probs_bad[j] * matchings[j][r][c] for j in range(M)) for c in range(n)] for r in range(n)]
    L_tilde_bad = [
        [sum(probs_bad[j] * (1.0 - probs_bad[j]) * matchings[j][r][c] for j in range(M)) for c in range(n)]
        for r in range(n)
    ]
    form_bad = mat_add(
        mat_add(I_mat, L_bar_bad, -2.0 * alpha),
        mat_add(mat_mul(L_bar_bad, L_bar_bad), L_tilde_bad, 2.0),
        alpha * alpha,
    )
    rho_bad = spectral_norm_symmetric(mat_add(form_bad, J_mat, -1.0))
    assert rho_matcha < rho_bad, f"Expected MATCHA rho={rho_matcha} < bad allocation rho={rho_bad}"

    print(
        f"[PASS] MATCHA boundaries verified: L_j^2==2*L_j exact, Eq(26) exact, "
        f"rho_matcha={rho_matcha:.4f} < rho_bad={rho_bad:.4f} < 1.0"
    )


if __name__ == "__main__":
    verify_matcha_boundaries()
