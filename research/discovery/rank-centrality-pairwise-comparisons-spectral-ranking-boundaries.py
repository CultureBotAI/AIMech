#!/usr/bin/env python3
"""Constructed boundary & verification script for RankCentralityIterativeRandomWalkSpectralRankingFromPairwiseComparisons.

Verifies the core mathematical properties of Negahban, Oh, & Shah (2017),
'Rank Centrality: Ranking from Pairwise Comparisons', Operations Research,
65(1), 266-287 (DOI:10.1287/opre.2016.1534, arXiv:1209.1688v4):

1. Exact Detailed Balance & Reversibility of the Ideal Rank Centrality Walk P_tilde
   (Section 2.2, Eq. 1):
     P_{ij} = (1 / d_max) A_{ij}                   if (i, j) in E, i != j,
     P_{ii} = 1 - (1 / d_max) sum_{l != i} A_{il}  if i = j,
   where A_{ij} = a_{ij} / (a_{ij} + a_{ji}) converges as k -> infty to
   w_j / (w_i + w_j) under the Bradley-Terry-Luce (BTL) / Multinomial Logit (MNL)
   model. Because pi_tilde(i) P_tilde_{ij} = pi_tilde(j) P_tilde_{ji} with
   pi_tilde(i) = w_i / sum_l w_l, P_tilde is self-adjoint in L^2(pi_tilde) and has
   unique stationary distribution pi_tilde on any connected comparison graph G,
   whereas naive Borda Count and Dwork et al.'s MC1/MC2/MC3/MC4 chains suffer non-vanishing
   asymptotic bias on irregular comparison graphs even as k -> infty (Section 3.3, Fig. 1).
2. Dirichlet Form Spectral Gap Comparison (Lemma 6, Eq. 27 & Eq. 26):
   Comparing the reversible BTL chain (P_tilde, pi_tilde) with the simple random
   walk Laplacian L = D^{-1} B (with stationary distribution mu(i) = d_i / sum_l d_l
   and spectral gap xi = 1 - max{lambda_2(L), -lambda_n(L)}) proves
     1 - lambda_max(P_tilde) >= (d_min / (b^2 d_max)) * xi,
   where b = max_{i,j} w_i / w_j is the dynamic range.
3. Finite-Sample L^2(pi_tilde) Convergence & Weighted Pairwise Ranking Error Bound
   (Lemma 2 Eq. 11, Theorem 1, and Lemma 1):
   Power iteration p_t^T = p_{t-1}^T P contracts geometrically to pi with
     ||pi - pi_tilde|| / ||pi_tilde|| = O((b^{5/2} kappa / xi) sqrt(log n / (k d_max))),
   and Lemma 1 bounds the BTL-weighted pairwise ranking error D_w(sigma) <= ||w - pi|| / ||w||.
"""

from __future__ import annotations

import json
import math
import random
from typing import List


def stationary_distribution(P: List[List[float]], steps: int = 4000, tol: float = 1e-13) -> List[float]:
    n = len(P)
    pi = [1.0 / n] * n
    for _ in range(steps):
        nxt = [0.0] * n
        for i in range(n):
            pi_i = pi[i]
            row = P[i]
            for j in range(n):
                nxt[j] += pi_i * row[j]
        s = sum(nxt)
        nxt = [x / s for x in nxt]
        if max(abs(nxt[j] - pi[j]) for j in range(n)) < tol:
            pi = nxt
            break
        pi = nxt
    return pi


def norm2(u: List[float]) -> float:
    return math.sqrt(sum(x * x for x in u))


def jacobi_sym_eigenvalues(A: List[List[float]], max_sweeps: int = 80) -> List[float]:
    n = len(A)
    M = [row[:] for row in A]
    for _ in range(max_sweeps):
        max_off = max(abs(M[i][j]) for i in range(n) for j in range(i + 1, n))
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


def weighted_ranking_error_dw(w_norm: List[float], scores: List[float]) -> float:
    n = len(w_norm)
    order = sorted(range(n), key=lambda i: scores[i], reverse=True)
    rank_pos = [0] * n
    for pos, idx in enumerate(order):
        rank_pos[idx] = pos
    w_l2_sq = sum(x * x for x in w_norm)
    err_sum = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            # In Negahban et al. (2017) Section 3.3, sigma_i < sigma_j means i is ranked higher than j
            if (w_norm[i] - w_norm[j]) * (rank_pos[i] - rank_pos[j]) > 0:
                err_sum += (w_norm[i] - w_norm[j]) ** 2
    return math.sqrt(err_sum / (2.0 * n * w_l2_sq))


def main() -> None:
    rng = random.Random(20261019)
    n = 16
    b = 4.0
    # True BTL weights with dynamic range b = max w_i / w_j = 4.0
    w_raw = [b ** ((2.0 * i - (n - 1)) / (2.0 * (n - 1))) for i in range(n)]
    sum_w = sum(w_raw)
    pi_tilde = [w / sum_w for w in w_raw]

    # Construct a connected non-regular comparison graph G = ([n], E)
    # so that degree heterogeneity exposes the asymptotic inconsistency of Borda Count and MC3
    B_adj = [[0] * n for _ in range(n)]
    for i in range(n):
        for step in (1, 2, 3):
            j = (i + step) % n
            B_adj[i][j] = 1
            B_adj[j][i] = 1
    # Add extra edges incident to middle-tier nodes to create degree irregularity
    for i in range(0, 6):
        for j in range(6, n):
            if (i + j) % 2 == 0:
                B_adj[i][j] = 1
                B_adj[j][i] = 1

    degrees = [sum(B_adj[i]) for i in range(n)]
    d_max = float(max(degrees))
    d_min = float(min(degrees))

    # 1. Population transition matrix P_tilde (k -> infty)
    A_pop = [[0.0] * n for _ in range(n)]
    P_tilde = [[0.0] * n for _ in range(n)]
    for i in range(n):
        row_sum = 0.0
        for j in range(n):
            if i != j and B_adj[i][j] == 1:
                A_pop[i][j] = pi_tilde[j] / (pi_tilde[i] + pi_tilde[j])
                P_tilde[i][j] = A_pop[i][j] / d_max
                row_sum += P_tilde[i][j]
        P_tilde[i][i] = 1.0 - row_sum

    # Verify Rank Centrality exactness as k -> infty vs Borda Count and MC3 asymptotic bias on irregular G
    pi_rc_inf = stationary_distribution(P_tilde)
    rc_inf_rel_err = norm2([pi_rc_inf[i] - pi_tilde[i] for i in range(n)]) / norm2(pi_tilde)
    assert rc_inf_rel_err < 1e-11, f"Population Rank Centrality failed to recover pi_tilde: {rc_inf_rel_err}"

    # MC3 transition matrix (Dwork et al. 2001a, Section 3.3): P^{(MC3)}_{ij} = A_{ij} / deg(i)
    P_mc3_inf = [[0.0] * n for _ in range(n)]
    for i in range(n):
        row_s = 0.0
        for j in range(n):
            if i != j and B_adj[i][j] == 1:
                P_mc3_inf[i][j] = A_pop[i][j] / degrees[i]
                row_s += P_mc3_inf[i][j]
        P_mc3_inf[i][i] = 1.0 - row_s
    pi_mc3_inf = stationary_distribution(P_mc3_inf)
    mc3_inf_rel_err = norm2([pi_mc3_inf[i] - pi_tilde[i] for i in range(n)]) / norm2(pi_tilde)
    assert mc3_inf_rel_err > 0.05, f"Expected MC3 to have non-vanishing bias on irregular graph: {mc3_inf_rel_err}"

    # 2. Verify Lemma 6 Dirichlet Form Spectral Gap Inequality (Eq. 26 & Eq. 27)
    # Symmetrized Laplacian L_sym = D^{-1/2} B D^{-1/2} has same eigenvalues as L = D^{-1} B
    L_sym = [
        [B_adj[i][j] / math.sqrt(degrees[i] * degrees[j]) if B_adj[i][j] == 1 else 0.0 for j in range(n)]
        for i in range(n)
    ]
    eigs_L = jacobi_sym_eigenvalues(L_sym)
    lam_max_L = max(eigs_L[1], -eigs_L[-1])
    xi_laplacian = 1.0 - lam_max_L

    # Symmetrized P_tilde: S = Pi_tilde^{1/2} P_tilde Pi_tilde^{-1/2}
    S_ptilde = [
        [math.sqrt(pi_tilde[i]) * P_tilde[i][j] / math.sqrt(pi_tilde[j]) for j in range(n)]
        for i in range(n)
    ]
    eigs_P_tilde = jacobi_sym_eigenvalues(S_ptilde)
    lam_max_P_tilde = max(eigs_P_tilde[1], -eigs_P_tilde[-1])
    gap_P_tilde = 1.0 - lam_max_P_tilde
    lemma4_lower_bound = (d_min / (b * b * d_max)) * xi_laplacian
    assert gap_P_tilde >= lemma4_lower_bound - 1e-12, (
        f"Lemma 4 / Eq. 26 spectral gap bound violated: {gap_P_tilde} < {lemma4_lower_bound}"
    )

    # 3. Finite-sample 1/sqrt(k) error scaling and Lemma 1 weighted ranking distance bound
    k_small = 25
    k_large = 400
    errs_small = []
    errs_large = []
    lemma1_checked = True

    for k_val, err_list in ((k_small, errs_small), (k_large, errs_large)):
        for _ in range(25):
            A_emp = [[0.0] * n for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    if B_adj[i][j] == 1:
                        wins_j = sum(1 for _ in range(k_val) if rng.random() < A_pop[i][j])
                        # Regularized Rank Centrality Beta(1, 1) Laplace smoothing (Eq. 5) or unregularized
                        A_emp[i][j] = wins_j / k_val
                        A_emp[j][i] = 1.0 - A_emp[i][j]
            P_emp = [[0.0] * n for _ in range(n)]
            for i in range(n):
                rs = 0.0
                for j in range(n):
                    if i != j and B_adj[i][j] == 1:
                        P_emp[i][j] = A_emp[i][j] / d_max
                        rs += P_emp[i][j]
                P_emp[i][i] = 1.0 - rs
            pi_hat = stationary_distribution(P_emp)
            rel_l2 = norm2([pi_hat[i] - pi_tilde[i] for i in range(n)]) / norm2(pi_tilde)
            dw_val = weighted_ranking_error_dw(pi_tilde, pi_hat)
            if dw_val > rel_l2 + 1e-12:
                lemma1_checked = False
            err_list.append(rel_l2)

    mean_err_small = sum(errs_small) / len(errs_small)
    mean_err_large = sum(errs_large) / len(errs_large)
    assert lemma1_checked, "Lemma 1 inequality D_w(sigma) <= ||w - pi|| / ||w|| violated"
    assert mean_err_large < 0.35 * mean_err_small, (
        f"Rank Centrality error failed to scale as 1/sqrt(k): {mean_err_large} vs {mean_err_small}"
    )

    summary = {
        "n_items": n,
        "dynamic_range_b": b,
        "d_min": d_min,
        "d_max": d_max,
        "population_rc_rel_l2_err": rc_inf_rel_err,
        "population_mc3_irregular_graph_bias": round(mc3_inf_rel_err, 6),
        "laplacian_spectral_gap_xi": round(xi_laplacian, 6),
        "p_tilde_spectral_gap": round(gap_P_tilde, 6),
        "eq26_dirichlet_comparison_lower_bound": round(lemma4_lower_bound, 6),
        "mean_rel_err_k25": round(mean_err_small, 6),
        "mean_rel_err_k400": round(mean_err_large, 6),
        "lemma1_dw_bound_verified": lemma1_checked,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
