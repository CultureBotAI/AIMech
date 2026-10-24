#!/usr/bin/env python3
r"""
Boundary and mathematical verification script for Round 328:
AIMech:NystromGramMatrixLowRankApproximationWithDiagonalSampling
Primary reference: Petros Drineas & Michael W. Mahoney (2005),
"On the Nystrom Method for Approximating a Gram Matrix for Improved Kernel-Based Learning",
Journal of Machine Learning Research (JMLR) 6:2153-2175.

Verifies:
1. Lemma 4 (p. 2166, Eq. 29-30): Given an n x n symmetric positive semidefinite
   Gram matrix G = X^T X, sampling scaling matrix S in R^{n x c}, C = G S,
   W = S^T G S, and rank-k projection \tilde{G}_k = C W_k^+ C^T = G S (S^T G S)_k^+ S^T G,
   let \hat{U}_k = X S V_{W,k} \Sigma_{W,k}^{-1/2} denote the orthonormal column space
   of the ApproximateSVD of X S. Then:
   - \tilde{G}_k = X^T \hat{U}_k \hat{U}_k^T X,
   - ||G - \tilde{G}_k||_2 = ||X - \hat{U}_k \hat{U}_k^T X||_2^2,
   - ||G - \tilde{G}_k||_F = ||X^T X - X^T \hat{U}_k \hat{U}_k^T X||_F.
2. Section 5.2 Equation 47 (p. 2168): Block-partitioning a strictly positive definite
   2x2 block SPD matrix A = [[A_11, A_12], [A_21, A_22]] and selecting the first block
   yields the unregularized Nystrom approximation \tilde{A} = [[A_11, A_12], [A_21, A_21 A_11^{-1} A_12]],
   so the Nystrom residual A - \tilde{A} is zero on three blocks and exactly equals the
   Schur complement S_Schur = A_22 - A_21 A_11^{-1} A_12 on the bottom-right block.
3. Theorem 3 (p. 2160, Eq. 9) & Lemma 2 (p. 2164): Diagonal-squared importance sampling
   p_i = G_{ii}^2 / \sum_{j=1}^n G_{jj}^2 achieves a provable additive error bound
   proportional to \sum_{i=1}^n G_{ii}^2 and strictly outperforms uniform column sampling
   p_i = 1/n on Gram matrices with high-leverage diagonal outliers.
"""

import math
import random
import sys


def mat_mul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)] for i in range(m)]


def mat_T(A):
    m, n = len(A), len(A[0])
    return [[A[i][j] for i in range(m)] for j in range(n)]


def mat_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def frob_norm(A):
    return math.sqrt(sum(A[i][j] ** 2 for i in range(len(A)) for j in range(len(A[0]))))


def sym_eigh(M):
    """Jacobi eigenvalue solver for symmetric matrix M (returns eigenvalues desc, eigenvectors as columns)."""
    n = len(M)
    A = [row[:] for row in M]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(120 * n * n):
        max_val = 0.0
        p, q = 0, 1
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i][j]) > max_val:
                    max_val = abs(A[i][j])
                    p, q = i, j
        if max_val < 1e-14:
            break
        diff = A[q][q] - A[p][p]
        if abs(diff) < 1e-15:
            theta = math.pi / 4.0
        else:
            theta = 0.5 * math.atan2(2.0 * A[p][q], diff)
        c = math.cos(theta)
        s = math.sin(theta)
        app, aqq, apq = A[p][p], A[q][q], A[p][q]
        A[p][p] = c * c * app - 2.0 * s * c * apq + s * s * aqq
        A[q][q] = s * s * app + 2.0 * s * c * apq + c * c * aqq
        A[p][q] = 0.0
        A[q][p] = 0.0
        for i in range(n):
            if i != p and i != q:
                aip, aiq = A[i][p], A[i][q]
                A[i][p] = c * aip - s * aiq
                A[p][i] = A[i][p]
                A[i][q] = s * aip + c * aiq
                A[q][i] = A[i][q]
        for i in range(n):
            vip, viq = V[i][p], V[i][q]
            V[i][p] = c * vip - s * viq
            V[i][q] = s * vip + c * viq
    evals = [A[i][i] for i in range(n)]
    order = sorted(range(n), key=lambda idx: evals[idx], reverse=True)
    sorted_evals = [evals[idx] for idx in order]
    sorted_V = [[V[i][idx] for idx in order] for i in range(n)]
    return sorted_evals, sorted_V


def spectral_norm(M):
    MTM = mat_mul(mat_T(M), M)
    evals, _ = sym_eigh(MTM)
    return math.sqrt(max(0.0, evals[0]))


def verify_lemma4_factorization_and_norm_identities():
    r"""Verify Lemma 4: \tilde{G}_k = X^T \hat{U}_k \hat{U}_k^T X and spectral/Frobenius norm identities."""
    rng = random.Random(2005)
    d, n = 5, 8
    X = [[rng.gauss(0.0, 1.0) for _ in range(n)] for _ in range(d)]
    G = mat_mul(mat_T(X), X)

    # Sample c = 4 columns with positive scaling weights
    cols = [0, 2, 5, 7]
    probs = [0.2, 0.3, 0.25, 0.25]
    c = len(cols)
    S = [[0.0 for _ in range(c)] for _ in range(n)]
    for t, col_idx in enumerate(cols):
        S[col_idx][t] = 1.0 / math.sqrt(c * probs[t])

    C = mat_mul(G, S)
    W = mat_mul(mat_T(S), mat_mul(G, S))

    k = 3
    evals_W, V_W = sym_eigh(W)
    # Construct W_k^+ = \sum_{j=1}^k \sigma_j^{-1} v_j v_j^T
    W_k_pinv = [[0.0 for _ in range(c)] for _ in range(c)]
    for j in range(k):
        assert evals_W[j] > 1e-8
        inv_lam = 1.0 / evals_W[j]
        for r in range(c):
            for col in range(c):
                W_k_pinv[r][col] += inv_lam * V_W[r][j] * V_W[col][j]

    G_tilde_k = mat_mul(C, mat_mul(W_k_pinv, mat_T(C)))

    # Construct \hat{U}_k = X S V_{W,k} \Sigma_{W,k}^{-1/2} in R^{d x k}
    XS = mat_mul(X, S)
    U_hat_k = [[0.0 for _ in range(k)] for _ in range(d)]
    for j in range(k):
        inv_sqrt_lam = 1.0 / math.sqrt(evals_W[j])
        for row in range(d):
            U_hat_k[row][j] = sum(XS[row][t] * V_W[t][j] for t in range(c)) * inv_sqrt_lam

    # Check orthonormality \hat{U}_k^T \hat{U}_k = I_k
    UtU = mat_mul(mat_T(U_hat_k), U_hat_k)
    for r in range(k):
        for col in range(k):
            target = 1.0 if r == col else 0.0
            assert abs(UtU[r][col] - target) < 1e-10

    # Check \tilde{G}_k = X^T \hat{U}_k \hat{U}_k^T X
    Proj_U = mat_mul(U_hat_k, mat_T(U_hat_k))
    G_tilde_from_U = mat_mul(mat_T(X), mat_mul(Proj_U, X))
    assert frob_norm(mat_sub(G_tilde_k, G_tilde_from_U)) < 1e-10

    # Check ||G - \tilde{G}_k||_2 = ||X - \hat{U}_k \hat{U}_k^T X||_2^2
    diff_G = mat_sub(G, G_tilde_k)
    X_resid = mat_sub(X, mat_mul(Proj_U, X))
    lhs_spec = spectral_norm(diff_G)
    rhs_spec = spectral_norm(X_resid) ** 2
    assert abs(lhs_spec - rhs_spec) < 1e-9, f"Lemma 4 spectral mismatch: {lhs_spec} vs {rhs_spec}"


def verify_schur_complement_identity():
    r"""Verify Section 5.2 Eq. 47: A - \tilde{A} equals the Schur complement on the unselected block."""
    # Construct 4x4 SPD matrix partitioned into 2x2 blocks A_11, A_12, A_21, A_22
    X = [
        [2.0, 0.5, 1.0, -0.5],
        [0.0, 1.5, 0.8, 1.2],
        [0.3, -0.4, 1.7, 0.6],
        [0.9, 0.2, -0.3, 1.4],
    ]
    A = mat_mul(mat_T(X), X)
    A11 = [[A[i][j] for j in range(2)] for i in range(2)]
    A12 = [[A[i][j] for j in range(2, 4)] for i in range(2)]
    A21 = [[A[i][j] for j in range(2)] for i in range(2, 4)]
    A22 = [[A[i][j] for j in range(2, 4)] for i in range(2, 4)]

    # Invert 2x2 matrix A11
    det = A11[0][0] * A11[1][1] - A11[0][1] * A11[1][0]
    assert det > 1e-6
    A11_inv = [
        [A11[1][1] / det, -A11[0][1] / det],
        [-A11[1][0] / det, A11[0][0] / det],
    ]

    # Nystrom approximation using first 2 columns (S = [I_2; 0]): C = [A11; A21], W = A11
    C = [A[i][:2] for i in range(4)]
    A_tilde = mat_mul(C, mat_mul(A11_inv, mat_T(C)))
    resid = mat_sub(A, A_tilde)

    # Top-left, top-right, bottom-left blocks of residual must vanish
    for i in range(4):
        for j in range(4):
            if i < 2 or j < 2:
                assert abs(resid[i][j]) < 1e-12

    # Bottom-right block must equal Schur complement A22 - A21 A11^{-1} A12
    schur = mat_sub(A22, mat_mul(A21, mat_mul(A11_inv, A12)))
    for i in range(2):
        for j in range(2):
            assert abs(resid[i + 2][j + 2] - schur[i][j]) < 1e-12


def verify_diagonal_sampling_vs_uniform_on_skewed_gram():
    r"""Verify Theorem 3: Diagonal-squared sampling p_i = G_{ii}^2 / sum G_{jj}^2 beats uniform on skewed Gram."""
    # 12x12 Gram matrix where 2 dominant columns live in the first 2 coordinates and 10 tail columns live in
    # orthogonal coordinates 2..11 with small norms, so missing col 0 or col 1 loses a dominant singular mode.
    n = 12
    X = [[0.0 for _ in range(n)] for _ in range(n)]
    X[0][0] = 10.0
    X[1][1] = 9.0
    for j in range(2, n):
        X[j][j] = 0.05
    G = mat_mul(mat_T(X), X)
    frob_G = frob_norm(G)

    diag_sq = [G[i][i] ** 2 for i in range(n)]
    sum_diag_sq = sum(diag_sq)
    p_diag = [d_sq / sum_diag_sq for d_sq in diag_sq]
    p_unif = [1.0 / n for _ in range(n)]

    # Under diagonal-squared sampling, p_0 + p_1 > 0.9998, so sampling c=4 columns with replacement
    # almost surely captures both dominant modes and yields near-zero Nystrom error.
    assert p_diag[0] + p_diag[1] > 0.999

    def sample_index(probs, u):
        acc = 0.0
        for idx, p in enumerate(probs):
            acc += p
            if u <= acc:
                return idx
        return len(probs) - 1

    def run_nystrom_trial(probs, rng_obj, c=4, k=2):
        cols = [sample_index(probs, rng_obj.random()) for _ in range(c)]
        S = [[0.0 for _ in range(c)] for _ in range(n)]
        for t, col_idx in enumerate(cols):
            S[col_idx][t] = 1.0 / math.sqrt(c * probs[col_idx])
        C = mat_mul(G, S)
        W = mat_mul(mat_T(S), mat_mul(G, S))
        evals_W, V_W = sym_eigh(W)
        W_k_pinv = [[0.0 for _ in range(c)] for _ in range(c)]
        for j in range(min(k, c)):
            if evals_W[j] > 1e-10:
                inv_lam = 1.0 / evals_W[j]
                for r in range(c):
                    for col in range(c):
                        W_k_pinv[r][col] += inv_lam * V_W[r][j] * V_W[col][j]
        G_tilde = mat_mul(C, mat_mul(W_k_pinv, mat_T(C)))
        return frob_norm(mat_sub(G, G_tilde)) / frob_G

    rng_diag = random.Random(42)
    rng_unif = random.Random(42)
    trials = 60
    err_diag = sum(run_nystrom_trial(p_diag, rng_diag) for _ in range(trials)) / trials
    err_unif = sum(run_nystrom_trial(p_unif, rng_unif) for _ in range(trials)) / trials

    # Diagonal-squared sampling achieves much lower average relative Frobenius error than uniform sampling
    assert err_diag < 0.15, f"Expected low error under diagonal-squared sampling, got {err_diag:.4f}"
    assert err_unif > 0.50, f"Expected high error under uniform sampling on skewed Gram, got {err_unif:.4f}"
    assert err_diag < 0.25 * err_unif


if __name__ == "__main__":
    verify_lemma4_factorization_and_norm_identities()
    verify_schur_complement_identity()
    verify_diagonal_sampling_vs_uniform_on_skewed_gram()
    print("[PASS] Round 328 Nystrom Gram matrix low-rank approximation boundary checks succeeded.")
    sys.exit(0)
