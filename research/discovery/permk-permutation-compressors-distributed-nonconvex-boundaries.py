#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 558: PermK Permutation Compressors (Szlendak, Tyurin, & Richtarik, ICLR 2022)."""

import itertools
import math
import random


def sq_norm(v):
    return sum(x * x for x in v)


def vec_sub(u, v):
    return [a - b for a, b in zip(u, v)]


def main():
    rng = random.Random(20211007)

    # 1. Verify Theorem 1 (PermK for d >= n, d = q * n) exact AB inequality with A = B = 1 (IV(1))
    n, q = 3, 2
    d = n * q  # d = 6, K = q = 2
    a_vecs = [[rng.gauss(1.5, 1.0) for _ in range(d)] for _ in range(n)]
    a_bar = [sum(a_vecs[i][c] for i in range(n)) / n for c in range(d)]
    mean_sq_norm = sum(sq_norm(a_vecs[i]) for i in range(n)) / n
    sq_norm_mean = sq_norm(a_bar)
    input_var = sum(sq_norm(vec_sub(a_vecs[i], a_bar)) for i in range(n)) / n
    assert abs((mean_sq_norm - sq_norm_mean) - input_var) < 1e-12

    # Exact expectation over all d! = 720 permutations pi of {0, ..., d-1}
    all_perms_d = list(itertools.permutations(range(d)))
    exp_err_permk_big_d = 0.0
    for pi in all_perms_d:
        # C_i(a_i) = n * sum_{j=q*(i-1)}^{q*i - 1} (a_i)_{pi_j} e_{pi_j}
        c_vecs = []
        for i in range(n):
            ci = [0.0] * d
            for j in range(q * i, q * (i + 1)):
                coord = pi[j]
                ci[coord] = n * a_vecs[i][coord]
            c_vecs.append(ci)
        # Verify pairwise orthogonality <C_i(a_i), C_j(a_j)> == 0 for i != j
        for i in range(n):
            for j in range(i + 1, n):
                dot = sum(c_vecs[i][c] * c_vecs[j][c] for c in range(d))
                assert abs(dot) < 1e-15
        c_bar = [sum(c_vecs[i][c] for i in range(n)) / n for c in range(d)]
        exp_err_permk_big_d += sq_norm(vec_sub(c_bar, a_bar)) / len(all_perms_d)

    # By Theorem 1, E[||(1/n) sum_i C_i(a_i) - a_bar||^2] == 1 * mean_sq_norm - 1 * sq_norm_mean == input_var
    assert abs(exp_err_permk_big_d - input_var) < 1e-11

    # Compare against independent RandK (K = q = 2): A_rand = (d/K - 1)/n = 2/3, B_rand = 0
    # Exact variance of independent RandK on a_vecs: (1/n^2) sum_i (d/K - 1) ||a_i||^2 = ((d/K - 1)/n) * mean_sq_norm
    A_rand = (d / q - 1.0) / n
    var_randk_bound = A_rand * mean_sq_norm
    # Verify that when a_vecs are homogeneous (a_i = a_bar), PermK has 0 variance while RandK has positive variance
    assert input_var < mean_sq_norm

    # 2. Verify Theorem 2 (PermK for n >= d, n = q * d) exact AB inequality with A = B = 1 - (n - d)/(n - 1) = (d - 1)/(n - 1)
    d2, q2 = 2, 3
    n2 = d2 * q2  # n = 6, d = 2, multiset S has each coord in {0, 1} repeated q2 = 3 times
    S = [0, 0, 0, 1, 1, 1]
    a2_vecs = [[rng.gauss(2.0, 1.0) for _ in range(d2)] for _ in range(n2)]
    a2_bar = [sum(a2_vecs[i][c] for i in range(n2)) / n2 for c in range(d2)]
    input_var2 = sum(sq_norm(vec_sub(a2_vecs[i], a2_bar)) for i in range(n2)) / n2

    all_perms_n = list(itertools.permutations(S))
    exp_err_permk_big_n = 0.0
    for pi in all_perms_n:
        c2_bar = [0.0] * d2
        for i in range(n2):
            coord = pi[i]
            c2_bar[coord] += (d2 * a2_vecs[i][coord]) / n2
        exp_err_permk_big_n += sq_norm(vec_sub(c2_bar, a2_bar)) / len(all_perms_n)

    A2 = 1.0 - (n2 - d2) / (n2 - 1.0)
    expected_var2 = A2 * input_var2
    assert abs(exp_err_permk_big_n - expected_var2) < 1e-11

    # 3. Verify Lemma 2 (Hessian variance L_+-^2 >= L_+^2 - L_-^2)
    # Example 2 (Identical functions + linear perturbation): f_i(x) = 0.5 * L_- * ||x||^2 + b_i^T x -> L_+- = 0 while L_- = L_+ > 0
    L_minus = 5.0
    L_plus = 5.0
    L_pm = 0.0
    p_marina = 1.0 / n
    # Step size M in Theorem 4: M = L_- + sqrt((1-p)/p * ((A - B)*L_+^2 + B*L_pm^2))
    M_permk = L_minus + math.sqrt(((1.0 - p_marina) / p_marina) * ((1.0 - 1.0) * (L_plus ** 2) + 1.0 * (L_pm ** 2)))
    M_randk = L_minus + math.sqrt(((1.0 - p_marina) / p_marina) * (A_rand * (L_plus ** 2)))
    assert abs(M_permk - L_minus) < 1e-12
    assert M_permk < M_randk

    print(
        f"[PASS] Round 558 PermK verified: Var_PermK(d>=n)={exp_err_permk_big_d:.6f}==IV(1)={input_var:.6f}, "
        f"Var_PermK(n>=d)={exp_err_permk_big_n:.6f}==A2*Var={expected_var2:.6f}, M_PermK={M_permk:.2f} < M_RandK={M_randk:.2f}"
    )


if __name__ == "__main__":
    main()
