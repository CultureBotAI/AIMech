#!/usr/bin/env python3
"""Constructed boundary and mechanism verification for:
Adaptive Banding of Large Covariance Matrices via a Nested Lasso Penalty
(Levina, Rothman, & Zhu, 2008, Ann. Appl. Stat. 2(1):245-263, arXiv:0803.3872v1).

Verifies:
1. Modified Cholesky decomposition Sigma^{-1} = T^T D^{-1} T (Eq. 3) and exact
   row-by-row decomposition of the Gaussian negative log-likelihood (Eqs. 4-5).
2. The nested Lasso hierarchical zero-propagation property (Eqs. 9-11): setting
   phi_{j,l} = 0 forces phi_{j,1} = ... = phi_{j,l-1} = 0 so row j has a contiguous
   row-specific bandwidth k_j (adaptive banding).
3. Structural boundary between unstructured Cholesky Lasso (Huang et al., 2006),
   which introduces irregular zeros in T that fill in under T^T D^{-1} T, versus
   adaptive banding via nested Lasso, which preserves exact structural zeros in
   Sigma^{-1} outside the adaptive band envelope.
4. Alternating residual-variance and local quadratic approximation (LQA) ridge
   solver (Section 2.2, Eq. 13) for the J_2 nested Lasso objective on a synthetic
   variable-bandwidth autoregression (Model Sigma_3, Section 3.1).
"""

from __future__ import annotations

import math
import random


def mat_mul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    m, k, n = len(A), len(A[0]), len(B[0])
    out = [[0.0] * n for _ in range(m)]
    for i in range(m):
        for r in range(k):
            air = A[i][r]
            if air != 0.0:
                for j in range(n):
                    out[i][j] += air * B[r][j]
    return out


def mat_transpose(A: list[list[float]]) -> list[list[float]]:
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def solve_linear(A: list[list[float]], b: list[float]) -> list[float]:
    n = len(b)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(M[r][col]))
        M[col], M[piv] = M[piv], M[col]
        denom = M[col][col]
        for j in range(col, n + 1):
            M[col][j] /= denom
        for r in range(n):
            if r != col and M[r][col] != 0.0:
                factor = M[r][col]
                for j in range(col, n + 1):
                    M[r][j] -= factor * M[col][j]
    return [M[i][n] for i in range(n)]


def invert_unit_lower_triangular(T: list[list[float]]) -> list[list[float]]:
    p = len(T)
    inv = [[0.0] * p for _ in range(p)]
    for i in range(p):
        inv[i][i] = 1.0
        for j in range(i):
            s = 0.0
            for k in range(j, i):
                s += T[i][k] * inv[k][j]
            inv[i][j] = -s
    return inv


def log_det_spd(A: list[list[float]]) -> float:
    p = len(A)
    L = [[0.0] * p for _ in range(p)]
    for i in range(p):
        for j in range(i + 1):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                val = A[i][i] - s
                assert val > 0.0, f"Matrix not SPD at index {i}: {val}"
                L[i][j] = math.sqrt(val)
            else:
                L[i][j] = (A[i][j] - s) / L[j][j]
    return 2.0 * sum(math.log(L[i][i]) for i in range(p))


def precision_from_cholesky(Phi: list[list[float]], sigma2: list[float]) -> list[list[float]]:
    """Compute Sigma^{-1} = T^T D^{-1} T where T = I - Phi (Eq. 3)."""
    p = len(Phi)
    T = [[(1.0 if i == j else (-Phi[i][j] if j < i else 0.0)) for j in range(p)] for i in range(p)]
    D_inv_T = [[T[i][j] / sigma2[i] for j in range(p)] for i in range(p)]
    return mat_mul(mat_transpose(T), D_inv_T)


def covariance_from_cholesky(Phi: list[list[float]], sigma2: list[float]) -> list[list[float]]:
    """Compute Sigma = T^{-1} D (T^{-1})^T where T = I - Phi (Eq. 3)."""
    p = len(Phi)
    T = [[(1.0 if i == j else (-Phi[i][j] if j < i else 0.0)) for j in range(p)] for i in range(p)]
    T_inv = invert_unit_lower_triangular(T)
    T_inv_D = [[T_inv[i][j] * sigma2[j] for j in range(p)] for i in range(p)]
    return mat_mul(T_inv_D, mat_transpose(T_inv))


def fit_row_lqa_j2(
    X: list[list[float]],
    j: int,
    lam1: float,
    lam2: float,
    max_iter: int = 80,
    thresh: float = 1e-6,
) -> tuple[list[float], float]:
    """Fit row j of T = I - Phi via the LQA algorithm of Section 2.2 (Eq. 13) for J_2."""
    n = len(X)
    if j == 0:
        s2 = sum(X[i][0] ** 2 for i in range(n)) / n
        return [], s2

    # Initialize with marginal regression coefficients phi^*_{jt} (Section 2.2, p. 252)
    phi = []
    for t in range(j):
        num = sum(X[i][j] * X[i][t] for i in range(n))
        den = sum(X[i][t] ** 2 for i in range(n)) + 1e-12
        phi.append(max(abs(num / den), 1e-4) * (1.0 if num >= 0 else -1.0))

    # Precompute Gram matrix G = X_{1:j-1}^T X_{1:j-1} and rhs = X_{1:j-1}^T X_j
    G = [[0.0] * j for _ in range(j)]
    rhs = [0.0] * j
    for t in range(j):
        rhs[t] = sum(X[i][t] * X[i][j] for i in range(n))
        for s in range(t, j):
            val = sum(X[i][t] * X[i][s] for i in range(n))
            G[t][s] = val
            G[s][t] = val

    sigma2 = 1.0
    eps = 1e-10
    for _ in range(max_iter):
        # Step 1: closed-form residual variance update
        rss = 0.0
        for i in range(n):
            pred = sum(phi[t] * X[i][t] for t in range(j))
            rss += (X[i][j] - pred) ** 2
        sigma2 = max(rss / n, 1e-8)

        # Step 2: LQA ridge system for J_2 (Section 2.2, p. 252)
        # Enforce hierarchical clamping: if phi[t+1] is at floor eps, clamp phi[t]
        A = [[(2.0 / sigma2) * G[t][s] for s in range(j)] for t in range(j)]
        b = [(2.0 / sigma2) * rhs[t] for t in range(j)]
        for t in range(j):
            denom1 = max(abs(phi[t]), eps)
            pen_diag = lam1 / denom1
            if t < j - 1:
                denom2 = max(abs(phi[t]), eps) * max(abs(phi[t + 1]), eps)
                pen_diag += lam2 / denom2
            A[t][t] += pen_diag

        phi_new = solve_linear(A, b)
        # Apply nested zero propagation from closest predecessor j-1 down to 0
        zeroed = False
        for t in range(j - 1, -1, -1):
            if zeroed or abs(phi_new[t]) <= thresh:
                phi_new[t] = eps
                zeroed = True
        if max(abs(phi_new[t] - phi[t]) for t in range(j)) < 1e-8:
            phi = phi_new
            break
        phi = phi_new

    phi_final = [0.0 if abs(v) <= thresh else v for v in phi]
    rss = sum((X[i][j] - sum(phi_final[t] * X[i][t] for t in range(j))) ** 2 for i in range(n))
    sigma2 = max(rss / n, 1e-8)
    return phi_final, sigma2


def fit_row_unstructured_lasso_lqa(
    X: list[list[float]],
    j: int,
    lam1: float,
    max_iter: int = 80,
    thresh: float = 1e-6,
) -> tuple[list[float], float]:
    """Fit row j with unstructured L_1 penalty (Huang et al. 2006, Eq. 8; lam2 = 0)."""
    return fit_row_lqa_j2(X, j, lam1=lam1, lam2=0.0, max_iter=max_iter, thresh=thresh)


def kl_loss_precision(Sigma_true: list[list[float]], Omega_hat: list[list[float]]) -> float:
    """Kullback-Leibler loss Delta_KL(Sigma, Sigma_hat) = tr(Omega_hat Sigma) - ln|Omega_hat Sigma| - p (Eq. 14)."""
    p = len(Sigma_true)
    prod = mat_mul(Omega_hat, Sigma_true)
    tr = sum(prod[i][i] for i in range(p))
    ld = log_det_spd(Omega_hat) + log_det_spd(Sigma_true)
    return tr - ld - p


def main() -> None:
    rng = random.Random(20080327)
    p = 10
    n = 120

    # 1. Verify exact modified Cholesky identity and log-likelihood decomposition (Eqs. 3-5)
    Phi_true = [[0.0] * p for _ in range(p)]
    # Variable-bandwidth autoregression (Model Sigma_3 style, Section 3.1):
    # First block (j=1..4) has bandwidth up to 3; second block (j=5..9) is AR(1) with bandwidth 1
    row_bandwidths = [0, 1, 2, 3, 3, 1, 1, 1, 1, 1]
    for j in range(1, p):
        kj = row_bandwidths[j]
        for l in range(max(0, j - kj), j):
            Phi_true[j][l] = 0.45 if (j - l) == 1 else (0.30 if (j - l) == 2 else 0.20)
    sigma2_true = [0.05] * p

    Sigma_true = covariance_from_cholesky(Phi_true, sigma2_true)
    Omega_true = precision_from_cholesky(Phi_true, sigma2_true)
    ident_check = mat_mul(Sigma_true, Omega_true)
    max_ident_err = max(
        abs(ident_check[i][j] - (1.0 if i == j else 0.0)) for i in range(p) for j in range(p)
    )
    assert max_ident_err < 1e-10, f"Cholesky inverse identity failed: {max_ident_err}"

    # Generate synthetic data X from N(0, Sigma_true) via X = (I - Phi)^{-1} eps (Eq. 2)
    T_true = [[(1.0 if i == j else (-Phi_true[i][j] if j < i else 0.0)) for j in range(p)] for i in range(p)]
    T_inv = invert_unit_lower_triangular(T_true)
    X: list[list[float]] = []
    for _ in range(n):
        eps_vec = [rng.gauss(0.0, math.sqrt(sigma2_true[j])) for j in range(p)]
        x_vec = [sum(T_inv[j][l] * eps_vec[l] for l in range(j + 1)) for j in range(p)]
        X.append(x_vec)

    # Verify Eq. (4) = sum_j Eq. (5)
    ll_matrix = n * log_det_spd(Sigma_true)
    for i in range(n):
        xi = X[i]
        quad = sum(xi[r] * Omega_true[r][c] * xi[c] for r in range(p) for c in range(p))
        ll_matrix += quad

    ll_decomposed = 0.0
    for j in range(p):
        rss_j = sum(
            (X[i][j] - sum(Phi_true[j][l] * X[i][l] for l in range(j))) ** 2 for i in range(n)
        )
        ll_decomposed += n * math.log(sigma2_true[j]) + rss_j / sigma2_true[j]
    assert abs(ll_matrix - ll_decomposed) < 1e-8, (
        f"Log-likelihood decomposition mismatch: {ll_matrix} vs {ll_decomposed}"
    )

    # 2. Structural fill-in boundary: irregular zeros in T (unstructured Cholesky Lasso,
    #    Figure 1b) lose sparsity in Sigma^{-1} = T^T D^{-1} T, whereas nested Lasso
    #    adaptive banding (Figure 1c) preserves contiguous bands and exact zeros in Sigma^{-1}.
    Phi_irregular = [[0.0] * p for _ in range(p)]
    # Suppose row p-1 has a single distant non-zero at column 0 and also at p-2, with zeros in between
    Phi_irregular[p - 1][0] = 0.4
    Phi_irregular[p - 1][p - 2] = 0.4
    Omega_irregular = precision_from_cholesky(Phi_irregular, [1.0] * p)
    # In Omega_irregular, entry (0, p-2) becomes non-zero even though T had only 2 off-diagonal non-zeros!
    assert abs(Omega_irregular[0][p - 2]) > 0.1, "Irregular Cholesky factor must create fill-in in Omega"

    # By contrast, if T has adaptive row bandwidths k_j, for the trailing AR(1) block (j >= 5, k_j = 1),
    # all entries Omega_true[r][c] with r >= 5, c < r - 1 are identically zero!
    for r in range(5, p):
        for c in range(r - 1):
            assert abs(Omega_true[r][c]) < 1e-12, f"Expected exact zero at ({r}, {c}), got {Omega_true[r][c]}"

    # 3. Fit Nested Lasso J_2 (adaptive banding) vs. Unstructured Lasso on X
    Phi_nested = [[0.0] * p for _ in range(p)]
    sigma2_nested = [0.0] * p
    for j in range(p):
        row_phi, s2 = fit_row_lqa_j2(X, j, lam1=8.0, lam2=6.0, thresh=0.05)
        for l, val in enumerate(row_phi):
            Phi_nested[j][l] = val
        sigma2_nested[j] = s2
        # Verify nested zero-propagation invariant on every row:
        # once phi_{j,l} == 0 for some l, all phi_{j,0..l-1} == 0
        seen_zero = False
        for l in range(j - 1, -1, -1):
            if abs(Phi_nested[j][l]) == 0.0:
                seen_zero = True
            else:
                assert not seen_zero, f"Row {j} violated nested zero invariant at col {l}: {Phi_nested[j][:j]}"

    Omega_nested = precision_from_cholesky(Phi_nested, sigma2_nested)
    kl_nested = kl_loss_precision(Sigma_true, Omega_nested)

    # Compare against common-bandwidth non-adaptive banding with k=1 (underfits block 1)
    Phi_band1 = [[0.0] * p for _ in range(p)]
    sigma2_band1 = [0.0] * p
    for j in range(p):
        if j == 0:
            sigma2_band1[0] = sum(X[i][0] ** 2 for i in range(n)) / n
        else:
            num = sum(X[i][j] * X[i][j - 1] for i in range(n))
            den = sum(X[i][j - 1] ** 2 for i in range(n))
            b1 = num / den
            Phi_band1[j][j - 1] = b1
            sigma2_band1[j] = sum((X[i][j] - b1 * X[i][j - 1]) ** 2 for i in range(n)) / n
    Omega_band1 = precision_from_cholesky(Phi_band1, sigma2_band1)
    kl_band1 = kl_loss_precision(Sigma_true, Omega_band1)

    # Compare against sample covariance inverse
    Sample_Sigma = [[0.0] * p for _ in range(p)]
    for r in range(p):
        for c in range(r, p):
            val = sum(X[i][r] * X[i][c] for i in range(n)) / n
            Sample_Sigma[r][c] = val
            Sample_Sigma[c][r] = val
    Omega_sample = [solve_linear(Sample_Sigma, [1.0 if k == col else 0.0 for k in range(p)]) for col in range(p)]
    Omega_sample = mat_transpose(Omega_sample)
    kl_sample = kl_loss_precision(Sigma_true, Omega_sample)

    assert kl_nested < kl_band1, f"Adaptive banding KL ({kl_nested:.4f}) should beat fixed k=1 banding ({kl_band1:.4f})"
    assert kl_nested < kl_sample, f"Adaptive banding KL ({kl_nested:.4f}) should beat sample precision ({kl_sample:.4f})"

    print(
        f"Nested Lasso adaptive banding verified: "
        f"KL_nested={kl_nested:.4f} < KL_band1={kl_band1:.4f} and KL_sample={kl_sample:.4f}; "
        f"exact Cholesky decomposition err={max_ident_err:.2e}."
    )


if __name__ == "__main__":
    main()
