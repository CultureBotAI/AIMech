#!/usr/bin/env python3
"""Boundary and regime verification for Guedon & Vershynin (2016)
Community detection in sparse networks via Grothendieck's inequality.
"""

import itertools
import json
import math
import random


def cut_norm_inf_to_1(M):
    n = len(M)
    best = 0.0
    for s in itertools.product((-1.0, 1.0), repeat=n):
        # max_t sum_i t_i (sum_j M_ij s_j) == sum_i |sum_j M_ij s_j|
        val = sum(abs(sum(M[i][j] * s[j] for j in range(n))) for i in range(n))
        if val > best:
            best = val
    return best


def spectral_norm_sym(M):
    n = len(M)
    v = [1.0 / math.sqrt(n)] * n
    best = 0.0
    for seed in range(n):
        v = [1.0 if i == seed else 0.0 for i in range(n)]
        for _ in range(40):
            w = [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]
            nw = math.sqrt(sum(z * z for z in w))
            if nw < 1e-15:
                break
            v = [z / nw for z in w]
        w = [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]
        nw = math.sqrt(sum(z * z for z in w))
        if nw > best:
            best = nw
    return best


def frob_inner(A, B):
    n = len(A)
    return sum(A[i][j] * B[i][j] for i in range(n) for j in range(n))


def l1_dist(A, B):
    n = len(A)
    return sum(abs(A[i][j] - B[i][j]) for i in range(n) for j in range(n))


def main():
    K_G = math.pi / (2.0 * math.log(1.0 + math.sqrt(2.0)))
    assert K_G <= 1.783

    # 1. Verify Fact 3.2 (Grothendieck's inequality on M_G^+):
    # For any B in R^{n x n} and any Z in M_G^+ = {Z >= 0, diag(Z) <= I_n}, |<B, Z>| <= K_G ||B||_{inf->1}
    rng = random.Random(20261019)
    n = 6
    B = [[rng.uniform(-1.0, 1.0) for _ in range(n)] for _ in range(n)]
    B_cut = cut_norm_inf_to_1(B)

    max_ratio = 0.0
    for _ in range(50):
        # Generate random X in R^{n x n} with rows in unit Euclidean ball B_2^n, Z = X X^T in M_G^+
        X = []
        for _ in range(n):
            row = [rng.gauss(0.0, 1.0) for _ in range(n)]
            nr = math.sqrt(sum(z * z for z in row))
            scale = rng.uniform(0.5, 1.0) / max(nr, 1e-12)
            X.append([z * scale for z in row])
        Z = [[sum(X[i][k] * X[j][k] for k in range(n)) for j in range(n)] for i in range(n)]
        val = abs(frob_inner(B, Z))
        ratio = val / B_cut
        if ratio > max_ratio:
            max_ratio = ratio
        assert val <= K_G * B_cut + 1e-12

    # 2. Verify Lemma 6.1 & Lemma 6.2 (General SBM Reference Objective Curvature):
    # <A_bar, Z_bar - Z> >= ((p - q)/2) ||Z_bar - Z||_1 for all Z in M_opt
    p, q = 0.75, 0.20
    # Two communities C_1 = {0,1,2}, C_2 = {3,4,5}
    comm = [0, 0, 0, 1, 1, 1]
    Z_bar = [[1.0 if comm[i] == comm[j] else 0.0 for j in range(n)] for i in range(n)]
    lam = sum(Z_bar[i][j] for i in range(n) for j in range(n))  # 18.0
    # Heterogeneous edge probabilities p_ij >= p inside, p_ij <= q outside
    A_bar = [[0.0] * n for _ in range(n)]
    for i in range(n):
        A_bar[i][i] = 1.0
        for j in range(i + 1, n):
            if comm[i] == comm[j]:
                A_bar[i][j] = A_bar[j][i] = p + 0.05 * ((i + j) % 3)
            else:
                A_bar[i][j] = A_bar[j][i] = q - 0.03 * ((i + j) % 3)

    # Test convex combinations Z(t) = (1-t) Z_bar + t Z_alt where Z_alt is another partition of same size lam
    comm_alt = [0, 1, 0, 1, 0, 1]
    Z_alt = [[1.0 if comm_alt[i] == comm_alt[j] else 0.0 for j in range(n)] for i in range(n)]
    min_curvature_margin = float("inf")
    for t in (0.1, 0.25, 0.5, 0.75, 1.0):
        Z_t = [[(1.0 - t) * Z_bar[i][j] + t * Z_alt[i][j] for j in range(n)] for i in range(n)]
        diff_Z = [[Z_bar[i][j] - Z_t[i][j] for j in range(n)] for i in range(n)]
        lhs = frob_inner(A_bar, diff_Z)
        rhs = 0.5 * (p - q) * l1_dist(Z_bar, Z_t)
        assert lhs >= rhs - 1e-12
        min_curvature_margin = min(min_curvature_margin, lhs - rhs)

    # 3. Verify Remark 4.2 (Automatic regularization effect of l_inf -> l_1 cut norm vs spectral norm):
    # Adding a high-degree star hub on vertex 0 Perturbation E_hub
    E_hub = [[0.0] * n for _ in range(n)]
    for j in range(1, n):
        E_hub[0][j] = E_hub[j][0] = 1.0
    # Relative perturbation in spectral norm vs cut norm relative to all-ones reference n E_n
    spec_hub = spectral_norm_sym(E_hub)  # sqrt(n-1)
    cut_hub = cut_norm_inf_to_1(E_hub)  # 2*(n-1)
    # Normalized by full graph scale (n for spectral, n^2 for cut norm):
    rel_spec = spec_hub / n
    rel_cut = cut_hub / (n * n)
    assert rel_cut < rel_spec

    summary = {
        "concept": "GrothendieckInequalityAndSemidefiniteProgrammingForSparseSBM",
        "grothendieck_constant_bound": round(K_G, 6),
        "empirical_max_grothendieck_ratio": round(max_ratio, 6),
        "lemma62_min_curvature_margin": round(min_curvature_margin, 6),
        "hub_relative_spectral_perturbation": round(rel_spec, 6),
        "hub_relative_cut_norm_perturbation": round(rel_cut, 6),
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
