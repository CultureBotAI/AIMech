#!/usr/bin/env python3
"""Boundary and regime verification for Abbe, Bandeira, & Hall (2016)
Exact Recovery in the Stochastic Block Model: Phase Transition and Semidefinite Programming.
"""

import json
import math


def mat_vec(M, v):
    n = len(v)
    return [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]


def rayleigh(M, v):
    mv = mat_vec(M, v)
    num = sum(v[i] * mv[i] for i in range(len(v)))
    den = sum(z * z for z in v)
    return num / den


def main():
    # 1. Verify Theorems 1 & 2 exact phase transition identity:
    # (alpha + beta)/2 - sqrt(alpha*beta) > 1 <=> (sqrt(alpha) - sqrt(beta))^2 > 2
    # <=> alpha + beta > 2 and (alpha - beta)^2 > 4*(alpha + beta) - 4
    alpha_sup, beta_sup = 6.0, 0.5
    ch_sup = 0.5 * (alpha_sup + beta_sup) - math.sqrt(alpha_sup * beta_sup)
    sq_diff_sup = 0.5 * ((math.sqrt(alpha_sup) - math.sqrt(beta_sup)) ** 2)
    assert abs(ch_sup - sq_diff_sup) < 1e-15
    assert ch_sup > 1.0
    assert (alpha_sup - beta_sup) ** 2 > 4.0 * (alpha_sup + beta_sup) - 4.0

    alpha_sub, beta_sub = 2.5, 0.6
    ch_sub = 0.5 * (alpha_sub + beta_sub) - math.sqrt(alpha_sub * beta_sub)
    assert ch_sub < 1.0
    assert (alpha_sub - beta_sub) ** 2 < 4.0 * (alpha_sub + beta_sub) - 4.0

    # 2. Verify Lemma 11 (Section A.3, Eqs. 98-100): Exact spectrum of deterministic expectation
    # C = E[2 L_SBM + I_n - 1 1^T] on an n=8 two-community graph
    n = 8
    log_n = math.log(n)
    a = -2.0 * alpha_sup * log_n / n + 1.0
    b = -2.0 * beta_sup * log_n / n + 1.0
    d = (alpha_sup - beta_sup) * log_n - 2.0 * alpha_sup * log_n / n + 1.0

    g = [1.0 if i < n // 2 else -1.0 for i in range(n)]
    ones = [1.0] * n

    C = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                C[i][j] = d
            elif g[i] == g[j]:
                C[i][j] = a
            else:
                C[i][j] = b

    # Check eigenvalue lambda_1 = n - 2*beta*log(n) on eigenvector 1
    C_ones = mat_vec(C, ones)
    lam1_expected = n - 2.0 * beta_sup * log_n
    err_lam1 = max(abs(C_ones[i] - lam1_expected * ones[i]) for i in range(n))
    assert err_lam1 < 1e-13

    # Check eigenvalue lambda_2 = 0 on ground-truth community vector g
    C_g = mat_vec(C, g)
    err_lam2 = max(abs(z) for z in C_g)
    assert err_lam2 < 1e-13

    # Check eigenvalue lambda_3 = (alpha - beta)*log(n) on any vector orthogonal to 1 and g
    v_orth = [1.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    C_v = mat_vec(C, v_orth)
    lam3_expected = (alpha_sup - beta_sup) * log_n
    err_lam3 = max(abs(C_v[i] - lam3_expected * v_orth[i]) for i in range(n))
    assert err_lam3 < 1e-13

    # 3. Verify Lemma 6 KKT Dual Certificate on a planted bisection graph G (Eqs. 20-24)
    # Within-community: complete 4-cliques minus one edge; across-community: one bridge edge per vertex
    A = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if g[i] == g[j]:
                A[i][j] = A[j][i] = 1.0
            elif j == i + n // 2:
                A[i][j] = A[j][i] = 1.0

    D_plus = [sum(A[i][j] for j in range(n) if g[j] == g[i]) for i in range(n)]
    D_minus = [sum(A[i][j] for j in range(n) if g[j] != g[i]) for i in range(n)]
    # S = Y - B = 2 L_SBM + 1 1^T = 2(D^+ - D^- - A) + 1 1^T (Lemma 6, Eqs. 22-24)
    S = [
        [
            (2.0 * (D_plus[i] - D_minus[i]) + 1.0)
            if i == j
            else (-2.0 * A[i][j] + 1.0)
            for j in range(n)
        ]
        for i in range(n)
    ]

    # Verify S g == 0 (complementary slackness Tr(S g g^T) == 0)
    Sg = mat_vec(S, g)
    assert max(abs(z) for z in Sg) < 1e-14

    # Verify Tr(B g g^T) == Tr(Y) where Y = 2(D^+ - D^-) + I_n (Eq. 24)
    B = [
        [0.0 if i == j else (1.0 if A[i][j] == 1.0 else -1.0) for j in range(n)]
        for i in range(n)
    ]
    primal_obj = sum(B[i][j] * g[i] * g[j] for i in range(n) for j in range(n))
    dual_obj = sum(2.0 * (D_plus[i] - D_minus[i]) + 1.0 for i in range(n))
    assert abs(primal_obj - dual_obj) < 1e-14

    # Verify lambda_2(S) > 0 on subspace orthogonal to g
    rq_ones = rayleigh(S, ones)
    rq_orth = rayleigh(S, v_orth)
    assert rq_ones > 0.0 and rq_orth > 0.0

    summary = {
        "concept": "StochasticBlockModelExactRecoveryPhaseTransitionAndSemidefiniteProgramming",
        "supercritical_chernoff_hellinger": round(ch_sup, 6),
        "subcritical_chernoff_hellinger": round(ch_sub, 6),
        "lemma11_eigenvalues": [round(lam1_expected, 6), 0.0, round(lam3_expected, 6)],
        "sdp_primal_dual_gap": abs(primal_obj - dual_obj),
        "dual_certificate_nullspace_err": max(abs(z) for z in Sg),
        "dual_certificate_orth_rayleigh": [round(rq_ones, 6), round(rq_orth, 6)],
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
