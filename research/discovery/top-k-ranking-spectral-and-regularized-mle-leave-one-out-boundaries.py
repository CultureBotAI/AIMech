#!/usr/bin/env python3
"""Constructed boundary & verification script for TopKRankingSpectralAndRegularizedMLEByLeaveOneOutAnalysis.

Verifies the core mathematical properties of Chen, Fan, Ma, & Wang (2019),
'Spectral Method and Regularized MLE Are Both Optimal for Top-K Ranking',
The Annals of Statistics, 47(4), 2204-2235 (DOI:10.1214/18-AOS1745, arXiv:1707.09971v3):

1. Stationary distribution exactness of the Bradley-Terry-Luce (BTL) spectral
   comparison transition matrix P^*:
     P^*_{i,j} = (1 / d) * p_{i,j} * y^*_{i,j}   for i != j,
     P^*_{i,i} = 1 - sum_{j != i} P^*_{i,j},
   where y^*_{i,j} = w^*_j / (w^*_i + w^*_j) and w^*_i = exp(theta^*_i).
   Under detailed balance pi^*_i P^*_{i,j} = pi^*_j P^*_{j,i}, pi^*_i = w^*_i / sum_l w^*_l
   is the unique stationary distribution of P^* ((pi^*)^T P^* = (pi^*)^T) and
   P^* is reversible with respect to pi^*.
2. Theorem 8 (New perturbation bound for stationary distributions of reversible
   Markov chains in the pi^*-weighted norm ||x||_{pi^*} = sqrt(sum_i pi^*_i x_i^2)):
     ||pi - pi^*||_{pi^*} <= ||(pi^*)^T (P - P^*)||_{pi^*} / (1 - rho^* - ||P - P^*||_{pi^*}),
   where rho^* = max{lambda_2(P^*), -lambda_n(P^*)} is the spectral gap parameter
   of the reversible chain P^*.
3. Leave-one-out decoupling for the Spectral Method (Section 4.2, Theorem 3)
   and Regularized MLE (Section 4.3, Theorem 4):
   Replacing row/column m's random comparison outcomes by their population means
   produces a leave-one-out transition matrix P^{(m)} (with stationary vector
   pi^{(m)}) and a leave-one-out regularized loss L_lambda^{(m)}(theta) (with
   gradient descent iterate theta^{t,(m)}) that are statistically independent of
   item m's comparison realizations while remaining O((1/n) ||hat_pi - pi^*||_infty)
   close to the full estimator, yielding minimax-optimal l_infty error
   O(sqrt(log n / (n p L))) and exact top-K identification when
   n p L >= C * kappa^4 * log(n) / (Delta_K / w^*_K)^2.
"""

from __future__ import annotations

import json
import math
import random
from typing import List, Tuple


def build_btl_transition_matrix(
    w: List[float], adj: List[List[int]], y_mat: List[List[float]], d_max: float
) -> List[List[float]]:
    n = len(w)
    P = [[0.0] * n for _ in range(n)]
    for i in range(n):
        row_off = 0.0
        for j in range(n):
            if i != j and adj[i][j] == 1:
                P[i][j] = y_mat[i][j] / d_max
                row_off += P[i][j]
        P[i][i] = 1.0 - row_off
    return P


def stationary_distribution_power(P: List[List[float]], tol: float = 1e-13, max_iter: int = 20000) -> List[float]:
    n = len(P)
    pi = [1.0 / n] * n
    for _ in range(max_iter):
        nxt = [0.0] * n
        for i in range(n):
            pi_i = pi[i]
            row = P[i]
            for j in range(n):
                nxt[j] += pi_i * row[j]
        s = sum(nxt)
        nxt = [x / s for x in nxt]
        diff = max(abs(nxt[j] - pi[j]) for j in range(n))
        pi = nxt
        if diff < tol:
            break
    return pi


def pi_weighted_vec_norm(x: List[float], pi_star: List[float]) -> float:
    return math.sqrt(sum(pi_star[i] * (x[i] ** 2) for i in range(len(x))))


def jacobi_sym_eigenvalues(A: List[List[float]], max_sweeps: int = 80) -> List[float]:
    n = len(A)
    M = [row[:] for row in A]
    for _ in range(max_sweeps):
        max_off = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(M[i][j]) > max_off:
                    max_off = abs(M[i][j])
        if max_off < 1e-13:
            break
        for p in range(n):
            for q in range(p + 1, n):
                apq = M[p][q]
                if abs(apq) < 1e-14:
                    continue
                app = M[p][p]
                aqq = M[q][q]
                tau = (aqq - app) / (2.0 * apq)
                t = (1.0 / (abs(tau) + math.sqrt(1.0 + tau * tau))) * (1.0 if tau >= 0 else -1.0)
                c = 1.0 / math.sqrt(1.0 + t * t)
                s = t * c
                M[p][p] = app - t * apq
                M[q][q] = aqq + t * apq
                M[p][q] = 0.0
                M[q][p] = 0.0
                for r in range(n):
                    if r != p and r != q:
                        mrp = M[r][p]
                        mrq = M[r][q]
                        M[r][p] = c * mrp - s * mrq
                        M[p][r] = M[r][p]
                        M[r][q] = s * mrp + c * mrq
                        M[q][r] = M[r][q]
    return sorted([M[i][i] for i in range(n)], reverse=True)


def pi_weighted_matrix_op_norm(Delta: List[List[float]], pi_star: List[float]) -> float:
    """Operator norm ||Delta||_{pi^*} = || D^{1/2} Delta D^{-1/2} ||_2 where D = diag(pi^*)."""
    n = len(Delta)
    B = [[0.0] * n for _ in range(n)]
    for i in range(n):
        si = math.sqrt(pi_star[i])
        for j in range(n):
            B[i][j] = si * Delta[i][j] / math.sqrt(pi_star[j])
    # Compute largest singular value via eigenvalues of B^T B
    BTB = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            s = sum(B[k][i] * B[k][j] for k in range(n))
            BTB[i][j] = s
            BTB[j][i] = s
    eigs = jacobi_sym_eigenvalues(BTB)
    return math.sqrt(max(0.0, eigs[0]))


def regularized_mle_gd(
    adj: List[List[int]],
    y_mat: List[List[float]],
    lam: float,
    eta: float,
    steps: int = 400,
) -> List[float]:
    """Minimize L_lambda(theta) = sum_{i>j, (i,j) in E} [ -y_{j,i}(theta_i - theta_j) + log(1 + exp(theta_i - theta_j)) ] + 0.5 * lam * ||theta||_2^2."""
    n = len(adj)
    theta = [0.0] * n
    for _ in range(steps):
        grad = [lam * theta[i] for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if adj[i][j] == 1:
                    # y_{j,i} = fraction of times i beats j = 1 - y_{i,j} where y_{i,j} is P(j beats i)
                    y_ji = 1.0 - y_mat[i][j]
                    diff = theta[i] - theta[j]
                    sig = 1.0 / (1.0 + math.exp(-diff))
                    g_ij = -y_ji + sig
                    grad[i] += g_ij
                    grad[j] -= g_ij
        mean_g = sum(grad) / n
        for i in range(n):
            theta[i] -= eta * (grad[i] - mean_g)
    mean_t = sum(theta) / n
    return [theta[i] - mean_t for i in range(n)]


def top_k_set(scores: List[float], k: int) -> set[int]:
    idx = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
    return set(idx[:k])


def main() -> None:
    rng = random.Random(20261019)
    n = 18
    k_top = 5
    # Construct latent scores theta^* with clear separation Delta_K at boundary K=5
    theta_star_raw = [
        1.10, 0.98, 0.86, 0.74, 0.62,   # top-K = {0, 1, 2, 3, 4}
        -0.05, -0.12, -0.18, -0.25, -0.31, -0.38, -0.44,
        -0.50, -0.56, -0.62, -0.68, -0.74, -0.80,
    ]
    mean_theta = sum(theta_star_raw) / n
    theta_star = [t - mean_theta for t in theta_star_raw]
    w_star = [math.exp(t) for t in theta_star]
    sum_w = sum(w_star)
    pi_star = [w / sum_w for w in w_star]

    # Complete comparison graph (p = 1.0) with d_max = 2 * n
    adj = [[0 if i == j else 1 for j in range(n)] for i in range(n)]
    d_max = 2.0 * n

    # Population pairwise comparison matrix y^*_{i,j} = w^*_j / (w^*_i + w^*_j)
    y_star = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                y_star[i][j] = w_star[j] / (w_star[i] + w_star[j])

    P_star = build_btl_transition_matrix(w_star, adj, y_star, d_max)

    # 1. Verify detailed balance pi^*_i P^*_{i,j} = pi^*_j P^*_{j,i} and stationarity (pi^*)^T P^* = (pi^*)^T
    max_detailed_balance_err = 0.0
    for i in range(n):
        for j in range(n):
            err = abs(pi_star[i] * P_star[i][j] - pi_star[j] * P_star[j][i])
            if err > max_detailed_balance_err:
                max_detailed_balance_err = err

    pi_star_check = stationary_distribution_power(P_star)
    stationarity_max_err = max(abs(pi_star_check[i] - pi_star[i]) for i in range(n))
    assert max_detailed_balance_err < 1e-15, f"Detailed balance failed: {max_detailed_balance_err}"
    assert stationarity_max_err < 1e-12, f"Stationarity check failed: {stationarity_max_err}"

    # Compute spectral gap 1 - rho^* of reversible P^* via symmetrized D^{1/2} P^* D^{-1/2}
    S_star = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            S_star[i][j] = math.sqrt(pi_star[i]) * P_star[i][j] / math.sqrt(pi_star[j])
    eigs_P_star = jacobi_sym_eigenvalues(S_star)
    # Largest eigenvalue is 1.0; rho^* = max(lambda_2, -lambda_n)
    rho_star = max(eigs_P_star[1], -eigs_P_star[-1])
    spectral_gap = 1.0 - rho_star
    assert spectral_gap > 0.10, f"Unexpected spectral gap: {spectral_gap}"

    # 2. Simulate L repeated pairwise comparisons per edge (high-SNR vs low-SNR)
    L_high = 400
    y_hat = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            wins_j_over_i = sum(1 for _ in range(L_high) if rng.random() < y_star[i][j])
            y_hat[i][j] = wins_j_over_i / L_high
            y_hat[j][i] = 1.0 - y_hat[i][j]

    P_hat = build_btl_transition_matrix(w_star, adj, y_hat, d_max)
    pi_hat = stationary_distribution_power(P_hat)

    # Verify Theorem 8 perturbation bound in ||.||_{pi^*} norm
    Delta_P = [[P_hat[i][j] - P_star[i][j] for j in range(n)] for i in range(n)]
    op_norm_delta = pi_weighted_matrix_op_norm(Delta_P, pi_star)
    assert op_norm_delta < spectral_gap, f"Perturbation too large for Theorem 8: {op_norm_delta} >= {spectral_gap}"

    # Numerator ||(pi^*)^T (P_hat - P^*)||_{pi^*} where row vector v_j = sum_i pi^*_i Delta_P_{i,j}
    # Note: In Theorem 8 of Chen et al. (2019), for reversible P^* with stationary distribution pi^*,
    # the vector representation in inner product space satisfies ||pi_hat - pi^*||_{pi^*} <= ||pi^* (P_hat - P^*) / pi^*||_{pi^*} / (1 - rho^* - ||P_hat - P^*||_{pi^*})
    # where under the paper's convention ||pi||_{pi^*} = sqrt(sum_i (pi_i^2 / pi^*_i)) for row distributions!
    lhs_thm8 = math.sqrt(sum(((pi_hat[j] - pi_star[j]) ** 2) / pi_star[j] for j in range(n)))
    v_row = [sum(pi_star[i] * Delta_P[i][j] for i in range(n)) for j in range(n)]
    num_thm8 = math.sqrt(sum((v_row[j] ** 2) / pi_star[j] for j in range(n)))
    rhs_thm8 = num_thm8 / (1.0 - rho_star - op_norm_delta)
    assert lhs_thm8 <= rhs_thm8 + 1e-12, f"Theorem 8 violated: {lhs_thm8} > {rhs_thm8}"

    # 3. Verify Leave-One-Out (LOO) approximation for both Spectral and Regularized MLE (m = 0)
    m_loo = 0
    y_loo = [row[:] for row in y_hat]
    for j in range(n):
        if j != m_loo:
            y_loo[m_loo][j] = y_star[m_loo][j]
            y_loo[j][m_loo] = y_star[j][m_loo]
    P_loo = build_btl_transition_matrix(w_star, adj, y_loo, d_max)
    pi_loo = stationary_distribution_power(P_loo)

    spectral_linf_err = max(abs(pi_hat[i] - pi_star[i]) / pi_star[i] for i in range(n))
    spectral_loo_gap = max(abs(pi_hat[i] - pi_loo[i]) / pi_star[i] for i in range(n))
    assert spectral_loo_gap < spectral_linf_err, (
        f"LOO spectral trajectory should be closer to full spectral estimator than estimation error: "
        f"{spectral_loo_gap} vs {spectral_linf_err}"
    )

    lam = 0.05
    eta = 0.04
    theta_mle = regularized_mle_gd(adj, y_hat, lam=lam, eta=eta, steps=450)
    theta_mle_loo = regularized_mle_gd(adj, y_loo, lam=lam, eta=eta, steps=450)
    mle_linf_err = max(abs(theta_mle[i] - theta_star[i]) for i in range(n))
    mle_loo_gap = max(abs(theta_mle[i] - theta_mle_loo[i]) for i in range(n))
    assert mle_loo_gap < mle_linf_err, (
        f"LOO regularized MLE should be closer to full MLE than estimation error: "
        f"{mle_loo_gap} vs {mle_linf_err}"
    )

    # 4. Verify exact Top-K identification by both Spectral Method and Regularized MLE
    true_top_k = top_k_set(w_star, k_top)
    spec_top_k = top_k_set(pi_hat, k_top)
    mle_top_k = top_k_set(theta_mle, k_top)
    assert spec_top_k == true_top_k, f"Spectral top-K mismatch: {spec_top_k} != {true_top_k}"
    assert mle_top_k == true_top_k, f"Regularized MLE top-K mismatch: {mle_top_k} != {true_top_k}"

    summary = {
        "n_items": n,
        "k_top": k_top,
        "L_comparisons_per_pair": L_high,
        "detailed_balance_max_err": max_detailed_balance_err,
        "stationarity_max_err": stationarity_max_err,
        "reversible_spectral_gap": round(spectral_gap, 6),
        "thm8_lhs_pi_star_norm": round(lhs_thm8, 6),
        "thm8_rhs_bound": round(rhs_thm8, 6),
        "spectral_rel_linf_err": round(spectral_linf_err, 6),
        "spectral_loo_rel_gap": round(spectral_loo_gap, 6),
        "reg_mle_linf_err": round(mle_linf_err, 6),
        "reg_mle_loo_gap": round(mle_loo_gap, 6),
        "exact_top_k_recovered_spectral": spec_top_k == true_top_k,
        "exact_top_k_recovered_reg_mle": mle_top_k == true_top_k,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
