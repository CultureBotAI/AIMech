#!/usr/bin/env python3
"""Constructed boundary verification for AltMinPhase and SparseAltMinPhase Phase Retrieval (Netrapalli, Jain, & Sanghavi 2015)."""

import json
import math
import random


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def norm2(u):
    return math.sqrt(dot(u, u))


def normalize(u):
    n = norm2(u)
    return [x / n for x in u]


def phase_dist(x, x_star):
    # dist(w1, w2) = sqrt(1 - (<w1, w2> / (||w1||_2 ||w2||_2))^2) (Section 2, p. 5)
    c = dot(x, x_star) / (norm2(x) * norm2(x_star))
    c = max(-1.0, min(1.0, c))
    return math.sqrt(max(0.0, 1.0 - c * c))


def solve_spd(G, b):
    # Gaussian elimination with partial pivoting for small SPD linear system G x = b
    n = len(b)
    M = [G[i][:] + [b[i]] for i in range(n)]
    for i in range(n):
        piv = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[piv] = M[piv], M[i]
        diag = M[i][i]
        for j in range(i, n + 1):
            M[i][j] /= diag
        for r in range(n):
            if r != i:
                fac = M[r][i]
                for j in range(i, n + 1):
                    M[r][j] -= fac * M[i][j]
    return [M[i][n] for i in range(n)]


def power_top_eigvec(S, iters=30):
    n = len(S)
    v = normalize([1.0 / (i + 1.0) for i in range(n)])
    for _ in range(iters):
        v = normalize([sum(S[i][j] * v[j] for j in range(n)) for i in range(n)])
    return v


def main():
    rng = random.Random(20261019)

    # Scenario A: Spectral Initialization S = (1/m) sum y_i^2 a_i a_i^T and AltMinPhase Geometric Contraction (Algorithms 1 & 2, Theorems 4.1 & 4.2)
    n = 5
    m = 350
    x_star = normalize([0.6, -0.5, 0.4, -0.3, 0.25])
    A = [[rng.gauss(0.0, 1.0) for _ in range(n)] for _ in range(m)]
    y = [abs(dot(a, x_star)) for a in A]

    # Build weighted covariance S = (1/m) sum_i y_i^2 a_i a_i^T (Algorithm 1, Step 1)
    S_mat = [[0.0] * n for _ in range(n)]
    G_mat = [[0.0] * n for _ in range(n)]
    for a, yi in zip(A, y):
        w = yi * yi / m
        for r in range(n):
            for c in range(n):
                S_mat[r][c] += w * a[r] * a[c]
                G_mat[r][c] += a[r] * a[c] / m

    x0 = power_top_eigvec(S_mat, iters=35)
    init_dist = phase_dist(x0, x_star)
    assert init_dist < 0.35

    x_cur = x0[:]
    dists = [init_dist]
    for _ in range(18):
        # Step 3: C^{t+1} = Diag(Ph(A^T x^t))
        rhs = [0.0] * n
        for a, yi in zip(A, y):
            ph = 1.0 if dot(a, x_cur) >= 0.0 else -1.0
            for j in range(n):
                rhs[j] += a[j] * (ph * yi) / m
        # Step 4: x^{t+1} = argmin_x ||A^T x - C^{t+1} y||_2 = (A A^T)^{-1} A C^{t+1} y (Eq. 3)
        x_cur = solve_spd(G_mat, rhs)
        dists.append(phase_dist(x_cur, x_star))

    assert dists[-1] < 1e-14

    # Scenario B: SparseAltMinPhase Marginal Correlation Support Recovery (Algorithm 3, Lemma 5.1, Corollary 5.2)
    n_sp = 24
    k_sp = 3
    true_supp = [2, 9, 17]
    x_sp = [0.0] * n_sp
    val = 1.0 / math.sqrt(k_sp)
    x_sp[2] = val
    x_sp[9] = -val
    x_sp[17] = val

    # Verify theoretical expectation separation from Proof of Lemma 5.1 (p. 26):
    # For j in S: E[|a_{ij} y_i|] = (2/pi) * (sqrt(1 - x_j^{*2}) + |x_j^*| arcsin(|x_j^*|)) >= 2/pi + (1/6) x_min^{*2}
    # For j not in S: E[|a_{ij} y_i|] = 2/pi
    null_mean_theory = 2.0 / math.pi
    active_mean_theory = (2.0 / math.pi) * (math.sqrt(1.0 - val * val) + val * math.asin(val))
    lower_bound_theory = 2.0 / math.pi + (val * val) / 6.0
    assert active_mean_theory >= lower_bound_theory > null_mean_theory

    m_sp = 450
    A_sp = [[rng.gauss(0.0, 1.0) for _ in range(n_sp)] for _ in range(m_sp)]
    y_sp = [abs(sum(a[j] * x_sp[j] for j in true_supp)) for a in A_sp]

    scores = []
    for j in range(n_sp):
        sc = sum(abs(A_sp[i][j]) * y_sp[i] for i in range(m_sp)) / m_sp
        scores.append((sc, j))

    scores_sorted = sorted(scores, key=lambda pair: pair[0], reverse=True)
    recovered_supp = sorted(pair[1] for pair in scores_sorted[:k_sp])
    assert recovered_supp == true_supp

    min_active_score = min(sc for sc, j in scores if j in true_supp)
    max_inactive_score = max(sc for sc, j in scores if j not in true_supp)
    assert min_active_score > max_inactive_score

    summary = {
        "altminphase_spectral_init_dist": round(init_dist, 5),
        "altminphase_final_dist": dists[-1],
        "sparse_theory_null_mean": round(null_mean_theory, 5),
        "sparse_theory_active_lower_bound": round(lower_bound_theory, 5),
        "sparse_theory_active_exact_mean": round(active_mean_theory, 5),
        "sparse_empirical_min_active_score": round(min_active_score, 5),
        "sparse_empirical_max_inactive_score": round(max_inactive_score, 5),
        "exact_support_recovered": recovered_supp == true_supp,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
