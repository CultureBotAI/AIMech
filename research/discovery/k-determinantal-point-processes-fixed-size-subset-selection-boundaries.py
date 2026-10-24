#!/usr/bin/env python3
"""Boundary and verification script for Round 334:
k-DPPs: Fixed-Size Determinantal Point Processes
(Kulesza & Taskar, ICML 2011 pp. 1193-1200; Foundations and Trends in Machine Learning 2012, arXiv:1207.6083).
"""

import itertools
import math
import sys


def det_small(M):
    """Exact determinant for k x k matrix M (k <= 6)."""
    k = len(M)
    if k == 0:
        return 1.0
    if k == 1:
        return M[0][0]
    if k == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    if k == 3:
        return (
            M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
        )
    A = [row[:] for row in M]
    sign = 1.0
    for i in range(k):
        piv = i
        for r in range(i + 1, k):
            if abs(A[r][i]) > abs(A[piv][i]):
                piv = r
        if abs(A[piv][i]) < 1e-15:
            return 0.0
        if piv != i:
            A[i], A[piv] = A[piv], A[i]
            sign = -sign
        for r in range(i + 1, k):
            f = A[r][i] / A[i][i]
            for c in range(i + 1, k):
                A[r][c] -= f * A[i][c]
    prod = sign
    for i in range(k):
        prod *= A[i][i]
    return prod


def submatrix(L, subset):
    return [[L[i][j] for j in subset] for i in subset]


def elem_sym_poly_dp(lambdas, k_max):
    """Algorithm 2 (Section 3.3, Equation 12, p. 1196):
    Compute e_l^n for l = 0..k_max and n = 0..N via e_l^n = e_l^{n-1} + lambda_n * e_{l-1}^{n-1}.
    Returns (N+1) x (k_max+1) table E where E[n][l] = e_l(lambda_1, ..., lambda_n).
    """
    N = len(lambdas)
    E = [[0.0] * (k_max + 1) for _ in range(N + 1)]
    for n in range(N + 1):
        E[n][0] = 1.0
    for n in range(1, N + 1):
        lam_n = lambdas[n - 1]
        for l in range(1, k_max + 1):
            E[n][l] = E[n - 1][l] + lam_n * E[n - 1][l - 1]
    return E


def phase1_subset_prob(J_set, lambdas, E, k):
    """Exact sequential Phase 1 probability of sampling eigenvector subset J_set
    under Algorithm 1 (lines 2-10, Section 3.3, p. 1196).
    """
    N = len(lambdas)
    l = k
    prob = 1.0
    for n in range(N, 0, -1):
        if l == 0:
            break
        p_include = lambdas[n - 1] * E[n - 1][l - 1] / E[n][l]
        if (n - 1) in J_set:
            prob *= p_include
            l -= 1
        else:
            prob *= 1.0 - p_include
    return prob


def phase2_ordered_prob(V_cols, ordered_Y):
    """Exact Phase 2 sequential probability of sampling ordered tuple ordered_Y
    given orthonormal eigenvector columns V_cols (Algorithm 1 lines 12-19, Section 2.2 / 3.3).
    """
    # V_cols is list of k vectors in R^N (orthonormal)
    V = [v[:] for v in V_cols]
    prob = 1.0
    for i_item in ordered_Y:
        m = len(V)
        # Pr(i_item) = (1/m) * sum_{v in V} (v^T e_{i_item})^2
        weights = [v[i_item] ** 2 for v in V]
        sum_sq = sum(weights)
        if sum_sq < 1e-15:
            return 0.0
        prob *= sum_sq / m
        if m == 1:
            break
        # Choose pivot vector with largest |v[i_item]| and project onto subspace orthogonal to e_{i_item}
        piv = max(range(m), key=lambda idx: abs(V[idx][i_item]))
        v_piv = V[piv]
        reduced = []
        for idx in range(m):
            if idx == piv:
                continue
            ratio = V[idx][i_item] / v_piv[i_item]
            w = [V[idx][r] - ratio * v_piv[r] for r in range(len(v_piv))]
            reduced.append(w)
        # Orthonormalize reduced basis via Gram-Schmidt
        ortho = []
        for w in reduced:
            u = w[:]
            for q in ortho:
                dot = sum(u[r] * q[r] for r in range(len(u)))
                u = [u[r] - dot * q[r] for r in range(len(u))]
            nrm = math.sqrt(sum(x * x for x in u))
            ortho.append([x / nrm for x in u])
        V = ortho
    return prob


def main():
    # Construct N=6 ground set with known orthonormal eigenvectors V and spectrum lambdas
    N = 6
    k = 3
    # Build orthonormal 6x6 matrix via Householder reflections
    vecs = [
        [1.0, 0.5, -0.3, 0.2, 0.4, -0.1],
        [0.2, -1.0, 0.6, 0.3, -0.2, 0.5],
        [-0.4, 0.3, 1.0, -0.5, 0.1, 0.2],
        [0.3, 0.2, 0.1, 1.0, -0.6, -0.3],
        [-0.1, 0.4, -0.2, 0.3, 1.0, 0.7],
        [0.5, -0.2, 0.4, -0.1, -0.3, 1.0],
    ]
    V_basis = []
    for v in vecs:
        u = v[:]
        for q in V_basis:
            dot = sum(u[r] * q[r] for r in range(N))
            u = [u[r] - dot * q[r] for r in range(N)]
        nrm = math.sqrt(sum(x * x for x in u))
        V_basis.append([x / nrm for x in u])

    lambdas = [4.2, 2.7, 1.5, 0.9, 0.4, 0.15]
    # L = sum_{n=1}^N lambda_n v_n v_n^T
    L = [
        [sum(lambdas[n] * V_basis[n][i] * V_basis[n][j] for n in range(N)) for j in range(N)]
        for i in range(N)
    ]

    # 1. Verify Proposition 3.1 (Equation 10) & Algorithm 2 DP (Equation 12):
    # sum_{|Y|=k} det(L_Y) == sum_{|J|=k} prod_{n in J} lambda_n == E[N][k]
    E = elem_sym_poly_dp(lambdas, N)
    all_k_subsets = list(itertools.combinations(range(N), k))
    sum_det_LY = sum(det_small(submatrix(L, Y)) for Y in all_k_subsets)
    sum_prod_lam = sum(
        math.prod(lambdas[n] for n in J) for J in all_k_subsets
    )
    e_k_dp = E[N][k]
    prop31_det_err = abs(sum_det_LY - e_k_dp)
    prop31_lam_err = abs(sum_prod_lam - e_k_dp)

    # 2. Verify Algorithm 1 Phase 1 exact probability distribution over all (N choose k) subsets J
    max_phase1_err = 0.0
    for J in all_k_subsets:
        p_seq = phase1_subset_prob(set(J), lambdas, E, k)
        p_exact = math.prod(lambdas[n] for n in J) / e_k_dp
        max_phase1_err = max(max_phase1_err, abs(p_seq - p_exact))

    # 3. Verify Algorithm 1 Two-Phase exact marginal P_L^k(Y) = det(L_Y) / e_k(lambda)
    # and Projection DPP Lemma 2.1 (Equation 4): P^{V_J}(Y) = det(K^J_Y) = sum_{pi in S_k} P_phase2(pi(Y) | J)
    max_phase2_lemma21_err = 0.0
    alg1_marginal_Y = {Y: 0.0 for Y in all_k_subsets}
    for J in all_k_subsets:
        p_J = phase1_subset_prob(set(J), lambdas, E, k)
        V_J = [V_basis[n] for n in J]
        K_J = [
            [sum(V_J[r][i] * V_J[r][j] for r in range(k)) for j in range(N)]
            for i in range(N)
        ]
        for Y in all_k_subsets:
            det_KJ_Y = det_small(submatrix(K_J, Y))
            p_Y_given_J = sum(
                phase2_ordered_prob(V_J, perm_Y)
                for perm_Y in itertools.permutations(Y)
            )
            max_phase2_lemma21_err = max(max_phase2_lemma21_err, abs(p_Y_given_J - det_KJ_Y))
            alg1_marginal_Y[Y] += p_J * p_Y_given_J

    max_k_dpp_err = max(
        abs(alg1_marginal_Y[Y] - det_small(submatrix(L, Y)) / e_k_dp)
        for Y in all_k_subsets
    )

    # 4. Verify scale invariance P_{alpha L}^k(Y) == P_L^k(Y) vs failure of standard DPP cardinality
    alpha = 3.7
    L_scaled = [[alpha * L[i][j] for j in range(N)] for i in range(N)]
    e_k_scaled = elem_sym_poly_dp([alpha * lam for lam in lambdas], k)[N][k]
    max_scale_inv_err = max(
        abs(
            det_small(submatrix(L_scaled, Y)) / e_k_scaled
            - det_small(submatrix(L, Y)) / e_k_dp
        )
        for Y in all_k_subsets
    )

    # Standard DPP with expected size E[|Y|] = k still assigns high probability to |Y| != k
    # Solve sum_{n=1}^N (c * lam_n) / (c * lam_n + 1) = k by bisection
    lo, hi = 0.01, 100.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        exp_sz = sum((mid * lam) / (mid * lam + 1.0) for lam in lambdas)
        if exp_sz < k:
            lo = mid
        else:
            hi = mid
    c_star = 0.5 * (lo + hi)
    E_c = elem_sym_poly_dp([c_star * lam for lam in lambdas], N)[N]
    det_cL_plus_I = math.prod(c_star * lam + 1.0 for lam in lambdas)
    std_dpp_prob_size_k = E_c[k] / det_cL_plus_I
    std_dpp_prob_wrong_size = 1.0 - std_dpp_prob_size_k

    ok = (
        prop31_det_err < 1e-13
        and prop31_lam_err < 1e-14
        and max_phase1_err < 1e-15
        and max_phase2_lemma21_err < 1e-14
        and max_k_dpp_err < 1e-14
        and max_scale_inv_err < 1e-15
        and std_dpp_prob_wrong_size > 0.45
    )
    if not ok:
        print("Verification failed!", file=sys.stderr)
        sys.exit(1)

    print(
        f"[PASS] Round 334 k-DPPs (Kulesza & Taskar 2011): "
        f"prop31_det_err={prop31_det_err:.2e}, max_phase1_err={max_phase1_err:.2e}, "
        f"max_phase2_lemma21_err={max_phase2_lemma21_err:.2e}, max_k_dpp_err={max_k_dpp_err:.2e}, "
        f"std_dpp_prob_wrong_size={std_dpp_prob_wrong_size:.4f}"
    )


if __name__ == "__main__":
    main()
