#!/usr/bin/env python3
"""Constructed boundary & regime verification for Round 276:
Factor-Adjusted Regularized Model Selection and Decorrelated Variable Screening (FarmSelect)
Primary source: Fan, Ke, & Wang (2020), Journal of Econometrics 216(1):71-85, arXiv:1612.08490v2.
"""

from __future__ import annotations
import json
import math
import random


def solve_linear_system(A: list[list[float]], b: list[float]) -> list[float]:
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(M[r][col]))
        M[col], M[piv] = M[piv], M[col]
        div = M[col][col]
        for j in range(col, n + 1):
            M[col][j] /= div
        for r in range(n):
            if r != col:
                fac = M[r][col]
                for j in range(col, n + 1):
                    M[r][j] -= fac * M[col][j]
    return [M[i][n] for i in range(n)]


def invert_matrix(A: list[list[float]]) -> list[list[float]]:
    n = len(A)
    cols = []
    for j in range(n):
        e = [1.0 if i == j else 0.0 for i in range(n)]
        cols.append(solve_linear_system(A, e))
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def top_k_eigen_symmetric(M: list[list[float]], k_max: int) -> tuple[list[float], list[list[float]]]:
    """Power iteration with orthogonal deflation for top k_max eigenpairs of symmetric matrix M."""
    n = len(M)
    A = [row[:] for row in M]
    evals = []
    evecs = []
    for _ in range(k_max):
        v = [1.0 / math.sqrt(n) if i % 2 == 0 else -0.5 / math.sqrt(n) for i in range(n)]
        for _ in range(120):
            wv = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
            norm_wv = math.sqrt(sum(x * x for x in wv))
            v = [x / norm_wv for x in wv]
        wv = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
        lam = sum(v[i] * wv[i] for i in range(n))
        evals.append(lam)
        evecs.append(v)
        for i in range(n):
            for j in range(n):
                A[i][j] -= lam * v[i] * v[j]
    return evals, evecs


def compute_irrepresentable_gamma_inf(Design: list[list[float]], S_idx: list[int]) -> float:
    """Compute Gamma_infty = ||X_{S^c}^T X_S (X_S^T X_S)^{-1}||_infty (Section 2.2 Eq. 2.4 & Section 5.1 p. 18)."""
    n = len(Design)
    p = len(Design[0])
    s = len(S_idx)
    Sc_idx = [j for j in range(p) if j not in S_idx]
    XtX_SS = [[sum(Design[t][S_idx[a]] * Design[t][S_idx[b]] for t in range(n)) / n for b in range(s)] for a in range(s)]
    XtX_SS_inv = invert_matrix(XtX_SS)
    max_row_sum = 0.0
    for j in Sc_idx:
        xt_j_S = [sum(Design[t][j] * Design[t][S_idx[b]] for t in range(n)) / n for b in range(s)]
        row_vec = [sum(xt_j_S[b] * XtX_SS_inv[b][c] for b in range(s)) for c in range(s)]
        row_l1 = sum(abs(val) for val in row_vec)
        if row_l1 > max_row_sum:
            max_row_sum = row_l1
    return max_row_sum


def lasso_coordinate_descent(Design: list[list[float]], y: list[float], lam: float, unpenalized_cols: set[int]) -> list[float]:
    """Coordinate descent solver for (1/(2n)) ||y - Design * theta||_2^2 + lam * ||theta_pen||_1."""
    n = len(Design)
    p = len(Design[0])
    theta = [0.0] * p
    col_sq = [sum(Design[t][j] ** 2 for t in range(n)) / n for j in range(p)]
    r = y[:]  # residual y - Design * theta
    for _ in range(250):
        max_change = 0.0
        for j in range(p):
            if col_sq[j] < 1e-12:
                continue
            rho_j = sum(Design[t][j] * r[t] for t in range(n)) / n + col_sq[j] * theta[j]
            if j in unpenalized_cols:
                new_tj = rho_j / col_sq[j]
            else:
                if rho_j > lam:
                    new_tj = (rho_j - lam) / col_sq[j]
                elif rho_j < -lam:
                    new_tj = (rho_j + lam) / col_sq[j]
                else:
                    new_tj = 0.0
            diff = new_tj - theta[j]
            if abs(diff) > 0.0:
                for t in range(n):
                    r[t] -= Design[t][j] * diff
                theta[j] = new_tj
                if abs(diff) > max_change:
                    max_change = abs(diff)
        if max_change < 1e-10:
            break
    return theta


def main() -> None:
    rng = random.Random(20261019)
    n = 120
    p = 60
    K_true = 2
    S_true = [0, 1, 2, 3]
    beta_true = [3.5, -3.0, 2.8, -2.5] + [0.0] * (p - 4)

    # Generate factor loadings B (p x K_true) so that inactive variables have strong factor alignment
    # that violates the Lasso irrepresentable condition ||X_{S^c}^T X_S (X_S^T X_S)^{-1}||_infty > 1 (Figure 2, p. 18)
    B = []
    for j in range(p):
        if j in S_true:
            B.append([1.2 if j % 2 == 0 else -1.2, 0.8])
        elif j < 12:
            # Inactive covariates strongly co-moving with the active factors
            B.append([2.2, 1.8])
        else:
            B.append([rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0)])

    # Generate stationary AR(1) factors f_t and idiosyncratic components u_t (Section 5.1, p. 17)
    F_true = []
    U_true = []
    X = []
    y = []
    f_prev = [0.0] * K_true
    for t in range(n):
        f_t = [0.4 * f_prev[k] + math.sqrt(1.0 - 0.16) * rng.gauss(0.0, 1.0) for k in range(K_true)]
        f_prev = f_t
        u_t = [rng.gauss(0.0, 0.45) for _ in range(p)]
        x_t = [sum(B[j][k] * f_t[k] for k in range(K_true)) + u_t[j] for j in range(p)]
        eps_t = rng.gauss(0.0, 0.25)
        y_t = sum(x_t[j] * beta_true[j] for j in range(p)) + eps_t
        F_true.append(f_t)
        U_true.append(u_t)
        X.append(x_t)
        y.append(y_t)

    # 1. Check Irrepresentable Condition on raw X vs. true U (Section 2.2 Eq. 2.4 & Figure 2, p. 18)
    gamma_inf_raw_X = compute_irrepresentable_gamma_inf(X, S_true)
    gamma_inf_true_U = compute_irrepresentable_gamma_inf(U_true, S_true)
    assert gamma_inf_raw_X > 1.35  # Strongly violates irrepresentable condition (< 1)!
    assert gamma_inf_true_U < 0.75  # Holds with margin tau > 0!

    # 2. Step 1 of FarmSelect: PCA estimation of K_hat via eigenvalue ratio (Eq. 3.6, p. 11)
    # and extraction of F_hat, B_hat, U_hat = X - F_hat * B_hat^T (Section 3.1, pp. 8-9)
    XXt = [[sum(X[t1][j] * X[t2][j] for j in range(p)) for t2 in range(n)] for t1 in range(n)]
    evals, evecs = top_k_eigen_symmetric(XXt, k_max=6)
    ratios = [evals[k] / evals[k + 1] for k in range(5)]
    K_hat = 1 + max(range(5), key=lambda k: ratios[k])
    assert K_hat == K_true

    # Columns of F_hat / sqrt(n) are top K_hat eigenvectors of XX^T
    F_hat = [[math.sqrt(n) * evecs[k][t] for k in range(K_hat)] for t in range(n)]
    # B_hat = n^{-1} X^T F_hat
    B_hat = [[sum(X[t][j] * F_hat[t][k] for t in range(n)) / n for k in range(K_hat)] for j in range(p)]
    U_hat = [
        [X[t][j] - sum(F_hat[t][k] * B_hat[j][k] for k in range(K_hat)) for j in range(p)]
        for t in range(n)
    ]

    gamma_inf_U_hat = compute_irrepresentable_gamma_inf(U_hat, S_true)
    assert gamma_inf_U_hat < 0.85

    # 3. Verify exact algebraic equivalence of Augmented Profile M-estimation (Eq. 3.2, p. 9)
    # and Projected Lasso with (I_n - P_hat) (Eqs. 3.4-3.5, pp. 9-10)
    lam = 0.12
    W_aug = [U_hat[t] + F_hat[t] for t in range(n)]
    unpen_cols = set(range(p, p + K_hat))
    theta_aug = lasso_coordinate_descent(W_aug, y, lam=lam, unpenalized_cols=unpen_cols)
    beta_farm_aug = theta_aug[:p]

    # Projected response (I_n - P_hat)y and projected covariates (I_n - P_hat)U_hat:
    # Since F_hat^T F_hat / n = I_K and U_hat = (I_n - P_hat)X already satisfies F_hat^T U_hat = 0,
    # (I_n - P_hat)U_hat == U_hat and (I_n - P_hat)y = y - F_hat (F_hat^T y / n).
    Ft_y = [sum(F_hat[t][k] * y[t] for t in range(n)) / n for k in range(K_hat)]
    y_proj = [y[t] - sum(F_hat[t][k] * Ft_y[k] for k in range(K_hat)) for t in range(n)]
    beta_farm_proj = lasso_coordinate_descent(U_hat, y_proj, lam=lam, unpenalized_cols=set())

    max_aug_proj_diff = max(abs(a - b) for a, b in zip(beta_farm_aug, beta_farm_proj))
    assert max_aug_proj_diff < 1e-7

    # 4. Verify Sign Consistency (Theorem 4.1 & Theorem 4.2, pp. 12-15):
    # FarmSelect recovers exact signed support of beta_true, whereas standard Lasso on X fails
    # across ALL lambda values because Gamma_infty(X) > 1.35!
    def signed_support(b_vec: list[float], tol: float = 1e-4) -> list[tuple[int, int]]:
        return [(j, 1 if b_vec[j] > 0 else -1) for j in range(len(b_vec)) if abs(b_vec[j]) > tol]

    true_signed_supp = signed_support(beta_true)
    farm_signed_supp = signed_support(beta_farm_aug)
    assert farm_signed_supp == true_signed_supp

    lasso_any_sign_consistent = False
    for lam_grid in [0.05 * k for k in range(1, 60)]:
        b_lasso = lasso_coordinate_descent(X, y, lam=lam_grid, unpenalized_cols=set())
        if signed_support(b_lasso) == true_signed_supp:
            lasso_any_sign_consistent = True
    assert not lasso_any_sign_consistent

    # 5. Verify Decorrelated Variable Screening (Section 3.4, Eq. 3.7, pp. 11-12):
    # Augmented marginal regression on (U_hat_j, F_hat) vs. raw marginal correlation X_j^T y / n
    raw_marginal = [abs(sum(X[t][j] * y[t] for t in range(n)) / n) for j in range(p)]
    decorr_marginal = [
        abs(sum(U_hat[t][j] * y_proj[t] for t in range(n)) / math.sqrt(max(sum(U_hat[t][j] ** 2 for t in range(n)) * n, 1e-12)))
        for j in range(p)
    ]
    top4_raw = sorted(range(p), key=lambda j: raw_marginal[j], reverse=True)[:4]
    top4_decorr = sorted(range(p), key=lambda j: decorr_marginal[j], reverse=True)[:4]
    assert sorted(top4_decorr) == S_true
    assert sorted(top4_raw) != S_true

    payload = {
        "concept": "AIMech:FactorAdjustedRegularizedModelSelectionAndDecorrelatedVariableScreening",
        "source": "Fan, Ke, & Wang (2020), Journal of Econometrics 216(1):71-85, arXiv:1612.08490v2",
        "results": {
            "n": n,
            "p": p,
            "K_true": K_true,
            "K_hat_eigen_ratio": K_hat,
            "eigenvalue_ratios_1_to_5": [round(r, 4) for r in ratios],
            "gamma_inf_raw_X": round(gamma_inf_raw_X, 6),
            "gamma_inf_true_U": round(gamma_inf_true_U, 6),
            "gamma_inf_PCA_U_hat": round(gamma_inf_U_hat, 6),
            "augmented_vs_projected_max_diff": max_aug_proj_diff,
            "farmselect_sign_consistent": farm_signed_supp == true_signed_supp,
            "lasso_sign_consistent_anywhere_on_path": lasso_any_sign_consistent,
            "farmselect_l2_error": round(math.sqrt(sum((a - b) ** 2 for a, b in zip(beta_farm_aug, beta_true))), 6),
            "top4_raw_marginal_screening": top4_raw,
            "top4_decorrelated_screening_eq37": sorted(top4_decorr),
        },
        "all_assertions_passed": True,
    }
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
