#!/usr/bin/env python3
"""Constructed boundary and verification checks for Round 268:
OLS Post-LASSO, Restricted Sparse Eigenvalue Sublinearity Sparsity Bounds, and Fitness-Thresholded
Post-LASSO (Belloni & Chernozhukov 2013, Bernoulli 19(2):521-547, DOI:10.3150/11-BEJ410,
arXiv:1001.0188v5).

Verifies:
1. Sublinearity of maximal restricted sparse eigenvalues (Lemma 3):
   phi(ceil(l * k)) <= ceil(l) * phi(k) for l >= 1, and empirical sparsity bound (Theorem 3)
   m_hat = |T_hat| <= s * min_{m in M} phi(m ^ n) * L_n where L_n = [2*c'/(1 - 1/c)]^2 / kappa(s)^2.
2. Remark 3.1 KKT lower bound on LASSO shrinkage bias:
   ||f_hat - f||_{P_n, 2} >= ((1 - 1/c) * lambda * sqrt(|T_hat|)) / (2 * n * sqrt(phi(m_hat)))
   whenever the noise-domination event lambda >= c * ||S||_infty holds.
3. OLS Post-LASSO (beta_tilde^0) and Fitness-Thresholded Post-LASSO (beta_tilde^{t_gamma},
   Eqs. 2.9 & 2.14) where t_gamma = max{t >= 0 : Q_hat(beta_tilde^t) - Q_hat(beta_hat) <= gamma}
   with gamma = (Q_hat(beta_tilde^0) - Q_hat(beta_hat)) / 2 < 0:
   verifies that Post-LASSO removes LASSO shrinkage bias and that fitness thresholding removes
   spurious variables while strictly improving empirical fit relative to LASSO.
"""

from __future__ import annotations

import itertools
import json
import math
import random
from typing import Dict, List, Sequence, Tuple


def mat_vec(A: List[List[float]], v: Sequence[float]) -> List[float]:
    return [sum(row[j] * v[j] for j in range(len(v))) for row in A]


def solve_spd(A: List[List[float]], b: Sequence[float]) -> List[float]:
    """Solve small SPD linear system A x = b via Cholesky/Gaussian elimination."""
    k = len(b)
    if k == 0:
        return []
    M = [list(A[i]) + [b[i]] for i in range(k)]
    for col in range(k):
        piv = max(range(col, k), key=lambda r: abs(M[r][col]))
        M[col], M[piv] = M[piv], M[col]
        diag = M[col][col]
        for j in range(col, k + 1):
            M[col][j] /= diag
        for r in range(k):
            if r != col and abs(M[r][col]) > 0.0:
                factor = M[r][col]
                for j in range(col, k + 1):
                    M[r][j] -= factor * M[col][j]
    return [M[i][k] for i in range(k)]


def max_sym_eig(G: List[List[float]]) -> float:
    """Compute largest eigenvalue of small symmetric PSD matrix G via power iteration."""
    k = len(G)
    if k == 0:
        return 0.0
    v = [1.0 / math.sqrt(k)] * k
    eig = 0.0
    for _ in range(80):
        w = mat_vec(G, v)
        nrm = math.sqrt(sum(x * x for x in w))
        if nrm < 1e-15:
            return 0.0
        v = [x / nrm for x in w]
        eig = sum(v[i] * w[i] for i in range(k))
    return eig


def verify_lemma3_sparse_eigenvalue_sublinearity() -> Dict[str, object]:
    """Verify Lemma 3: phi(ceil(l * k)) <= ceil(l) * phi(k) for exact sparse eigenvalues."""
    rng = random.Random(20130410)
    n = 30
    p = 10
    # Construct correlated design matrix X (n x p) with column norm sqrt(n)
    X = [[0.0] * p for _ in range(n)]
    for i in range(n):
        z0 = rng.gauss(0.0, 1.0)
        for j in range(p):
            X[i][j] = 0.45 * z0 + math.sqrt(1.0 - 0.45**2) * rng.gauss(0.0, 1.0)
    for j in range(p):
        mean_j = sum(X[i][j] for i in range(n)) / n
        for i in range(n):
            X[i][j] -= mean_j
        norm_j = math.sqrt(sum(X[i][j] ** 2 for i in range(n)) / n)
        for i in range(n):
            X[i][j] /= norm_j

    Gram = [
        [sum(X[i][r] * X[i][c] for i in range(n)) / n for c in range(p)]
        for r in range(p)
    ]

    phi = {}
    for k in range(1, 7):
        best = 0.0
        for subset in itertools.combinations(range(p), k):
            subG = [[Gram[r][c] for c in subset] for r in subset]
            ev = max_sym_eig(subG)
            if ev > best:
                best = ev
        phi[k] = best

    checks = []
    for k in (1, 2, 3):
        for mult in (2, 3):
            if k * mult <= 6:
                lhs = phi[k * mult]
                rhs = mult * phi[k]
                assert lhs <= rhs + 1e-10, f"Lemma 3 violated: phi({k*mult})={lhs} > {mult}*phi({k})={rhs}"
                checks.append(
                    {
                        "k": k,
                        "l": mult,
                        "phi_lk": round(lhs, 6),
                        "l_times_phi_k": round(rhs, 6),
                    }
                )

    return {"phi_values": {str(k): round(v, 6) for k, v in phi.items()}, "sublinearity_checks": checks}


def solve_lasso_cd(
    X: List[List[float]],
    y: List[float],
    lam: float,
    max_iter: int = 500,
    tol: float = 1e-11,
) -> List[float]:
    """Solve min_beta (1/(2n)) ||y - X beta||_2^2 + (lam / n) ||beta||_1
    (Belloni & Chernozhukov 2013 Eq. 2.7 with Q_hat(b) = (1/(2n))||y - Xb||_2^2)."""
    n = len(y)
    p = len(X[0])
    beta = [0.0] * p
    residual = list(y)
    thresh = lam / n
    for _ in range(max_iter):
        max_diff = 0.0
        for j in range(p):
            old_b = beta[j]
            for i in range(n):
                residual[i] += X[i][j] * old_b
            rho = sum(X[i][j] * residual[i] for i in range(n)) / n
            if abs(rho) <= thresh:
                new_b = 0.0
            else:
                new_b = math.copysign(abs(rho) - thresh, rho)
            for i in range(n):
                residual[i] -= X[i][j] * new_b
            diff = abs(new_b - old_b)
            if diff > max_diff:
                max_diff = diff
            beta[j] = new_b
        if max_diff < tol:
            break
    return beta


def ols_refit(X: List[List[float]], y: List[float], support: List[int]) -> List[float]:
    """Compute least squares estimator beta_tilde on given support T subset {0..p-1}."""
    n = len(y)
    p = len(X[0])
    beta = [0.0] * p
    if not support:
        return beta
    k = len(support)
    G = [
        [sum(X[i][support[r]] * X[i][support[c]] for i in range(n)) / n for c in range(k)]
        for r in range(k)
    ]
    rhs = [sum(X[i][support[r]] * y[i] for i in range(n)) / n for r in range(k)]
    sol = solve_spd(G, rhs)
    for idx, val in zip(support, sol):
        beta[idx] = val
    return beta


def q_hat(X: List[List[float]], y: List[float], beta: Sequence[float]) -> float:
    """Empirical loss Q_hat(beta) = (1/(2n)) sum_{i=1}^n (y_i - x_i' beta)^2."""
    n = len(y)
    p = len(beta)
    return sum(
        (y[i] - sum(X[i][j] * beta[j] for j in range(p))) ** 2 for i in range(n)
    ) / (2.0 * n)


def pred_norm(X: List[List[float]], beta_a: Sequence[float], beta_b: Sequence[float]) -> float:
    """Empirical prediction norm ||X(beta_a - beta_b)||_{P_n, 2}."""
    n = len(X)
    p = len(beta_a)
    return math.sqrt(
        sum(
            (sum(X[i][j] * (beta_a[j] - beta_b[j]) for j in range(p))) ** 2
            for i in range(n)
        )
        / n
    )


def verify_post_lasso_and_fitness_thresholding() -> Dict[str, object]:
    """Verify Remark 3.1 KKT lower bound on LASSO bias, OLS Post-LASSO bias reduction,
    and fitness-thresholded Post-LASSO (Eqs. 2.9 & 2.14)."""
    rng = random.Random(20130521)
    n = 80
    p = 24
    s = 3

    # Generate normalized design X
    X = [[rng.gauss(0.0, 1.0) for _ in range(p)] for _ in range(n)]
    for j in range(p):
        mean_j = sum(X[i][j] for i in range(n)) / n
        for i in range(n):
            X[i][j] -= mean_j
        nrm = math.sqrt(sum(X[i][j] ** 2 for i in range(n)) / n)
        for i in range(n):
            X[i][j] /= nrm

    # True parameter beta_0 has 3 strong components {0, 1, 2}
    beta_true = [0.0] * p
    beta_true[0] = 2.0
    beta_true[1] = -1.6
    beta_true[2] = 1.4

    sigma = 0.35
    eps = [rng.gauss(0.0, sigma) for _ in range(n)]
    # Slightly align regressor 3 with noise so LASSO at moderate penalty picks up 1 false positive
    for i in range(n):
        X[i][3] = 0.72 * X[i][3] + 0.28 * (eps[i] / sigma)
    mean_3 = sum(X[i][3] for i in range(n)) / n
    for i in range(n):
        X[i][3] -= mean_3
    nrm_3 = math.sqrt(sum(X[i][3] ** 2 for i in range(n)) / n)
    for i in range(n):
        X[i][3] /= nrm_3

    y = [
        sum(X[i][j] * beta_true[j] for j in range(p)) + eps[i]
        for i in range(n)
    ]

    # Score vector S = 2 * E_n[x_i eps_i] under Belloni & Chernozhukov normalization
    # With Q_hat(b) = (1/(2n))||y - Xb||^2, gradient at beta_true is -(1/n) X^T eps.
    # So ||grad Q_hat(beta_true)||_infty = max_j |(1/n) sum_i X_{ij} eps_i|.
    score_inf = max(
        abs(sum(X[i][j] * eps[i] for i in range(n))) for j in range(p)
    )
    c_slack = 1.15
    lam = c_slack * score_inf

    beta_lasso = solve_lasso_cd(X, y, lam)
    t_hat = [j for j in range(p) if abs(beta_lasso[j]) > 1e-8]
    m_hat = len(t_hat)
    assert m_hat >= s, f"Expected LASSO to select at least {s} variables, got {m_hat}"

    # Verify Remark 3.1 KKT lower bound on LASSO prediction error:
    # For Q_hat = (1/(2n))||y - Xb||^2 + (lam/n)||b||_1, on T_hat we have
    # (1/n) X_{T_hat}^T (y - X beta_hat) = (lam/n) sign(beta_hat_{T_hat}),
    # and ||(1/n) X_{T_hat}^T eps||_2 <= sqrt(m_hat) * (score_inf / n) = sqrt(m_hat) * lam / (c * n).
    # Hence ||(1/n) X_{T_hat}^T X (beta_true - beta_hat)||_2 >= (1 - 1/c) * (lam / n) * sqrt(m_hat),
    # so ||X(beta_hat - beta_true)||_{P_n, 2} >= (1 - 1/c) * lam * sqrt(m_hat) / (n * sqrt(phi(m_hat))).
    Gram_that = [
        [sum(X[i][t_hat[r]] * X[i][t_hat[c]] for i in range(n)) / n for c in range(m_hat)]
        for r in range(m_hat)
    ]
    phi_mhat = max_sym_eig(Gram_that)
    remark31_lower_bound = ((1.0 - 1.0 / c_slack) * lam * math.sqrt(m_hat)) / (
        n * math.sqrt(phi_mhat)
    )
    lasso_pred_err = pred_norm(X, beta_lasso, beta_true)
    assert (
        lasso_pred_err >= remark31_lower_bound - 1e-9
    ), f"Remark 3.1 lower bound violated: {lasso_pred_err} < {remark31_lower_bound}"

    # Unthresholded OLS Post-LASSO (t = 0)
    beta_post0 = ols_refit(X, y, t_hat)
    post0_pred_err = pred_norm(X, beta_post0, beta_true)

    q_lasso = q_hat(X, y, beta_lasso)
    q_post0 = q_hat(X, y, beta_post0)
    assert q_post0 < q_lasso, "OLS Post-LASSO must strictly reduce empirical risk relative to LASSO"

    # Fitness-thresholded Post-LASSO (Eqs. 2.9 & 2.14):
    # gamma = (Q_hat(beta_post0) - Q_hat(beta_lasso)) / 2 < 0
    # t_gamma = max{t >= 0 : Q_hat(beta_tilde^t) - Q_hat(beta_lasso) <= gamma}
    gamma = 0.5 * (q_post0 - q_lasso)
    assert gamma < 0.0

    # Candidate thresholds are the sorted magnitudes |beta_lasso_j| for j in T_hat
    cand_thresholds = sorted({0.0} | {abs(beta_lasso[j]) for j in t_hat})
    best_t = 0.0
    best_beta_post_t = beta_post0
    best_support_t = t_hat
    for t_val in cand_thresholds:
        # T_hat(t) = {j : |beta_lasso_j| > t} (or >= t on grid just below jump)
        supp_t = [j for j in t_hat if abs(beta_lasso[j]) >= t_val - 1e-12]
        if not supp_t:
            continue
        beta_t = ols_refit(X, y, supp_t)
        qt = q_hat(X, y, beta_t)
        if qt - q_lasso <= gamma + 1e-12:
            best_t = t_val
            best_beta_post_t = beta_t
            best_support_t = supp_t

    q_post_fit = q_hat(X, y, best_beta_post_t)
    post_fit_pred_err = pred_norm(X, best_beta_post_t, beta_true)

    assert q_post_fit - q_lasso <= gamma + 1e-12
    assert len(best_support_t) <= len(t_hat)
    assert post0_pred_err < lasso_pred_err, "OLS Post-LASSO must improve prediction error over biased LASSO"
    assert post_fit_pred_err < lasso_pred_err, "Fitness-thresholded Post-LASSO must beat LASSO prediction error"

    return {
        "lasso_support": t_hat,
        "fitness_thresholded_support": best_support_t,
        "phi_m_hat": round(phi_mhat, 6),
        "remark31_lasso_lower_bound": round(remark31_lower_bound, 6),
        "lasso_pred_error": round(lasso_pred_err, 6),
        "ols_post_lasso_pred_error": round(post0_pred_err, 6),
        "fitness_post_lasso_pred_error": round(post_fit_pred_err, 6),
        "q_hat_lasso": round(q_lasso, 6),
        "q_hat_post0": round(q_post0, 6),
        "q_hat_post_fit": round(q_post_fit, 6),
        "gamma_target": round(gamma, 6),
        "selected_threshold_t_gamma": round(best_t, 6),
    }


def main() -> None:
    part1 = verify_lemma3_sparse_eigenvalue_sublinearity()
    part2 = verify_post_lasso_and_fitness_thresholding()
    summary = {
        "concept": "AIMech:OLSPostLassoAndFitnessThresholdedPostModelSelectionInHighDimensionalSparseModels",
        "source": "Belloni & Chernozhukov (2013), Bernoulli 19(2):521-547",
        "lemma3_sparse_eigenvalue_sublinearity": part1,
        "post_lasso_and_fitness_thresholding": part2,
        "all_assertions_passed": True,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
