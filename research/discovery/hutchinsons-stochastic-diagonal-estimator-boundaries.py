#!/usr/bin/env python3
"""Constructed boundary verification for Hutchinson's Stochastic Diagonal Estimator (Dharangutte & Musco 2022)."""

import itertools


def matvec(A, g):
    return [sum(A[i][j] * g[j] for j in range(len(g))) for i in range(len(A))]


def hadamard(a, b):
    return [x * y for x, y in zip(a, b)]


def main():
    # 1. Exact expectation and Lemma 3 & Lemma 4 squared-error identity over the hypercube {-1, +1}^n
    A = [
        [10.0, 2.0, -1.0],
        [2.0, 20.0, 3.0],
        [-1.0, 3.0, 30.0],
    ]
    n = 3
    diag_A = [A[i][i] for i in range(n)]
    off_diag_frob_sq = sum(A[i][j] ** 2 for i in range(n) for j in range(n) if i != j)
    diag_norm_sq = sum(d * d for d in diag_A)

    # Enumerate all 2^3 = 8 Rademacher vectors g in {-1, +1}^3
    rademacher_vecs = list(itertools.product([-1.0, 1.0], repeat=n))
    est_sum = [0.0] * n
    sq_err_sum = 0.0
    for g in rademacher_vecs:
        Ag = matvec(A, g)
        r_single = hadamard(g, Ag)
        for i in range(n):
            est_sum[i] += r_single[i]
        sq_err_sum += sum((r_single[i] - diag_A[i]) ** 2 for i in range(n))

    mean_est = [x / len(rademacher_vecs) for x in est_sum]
    expected_sq_err_rademacher = sq_err_sum / len(rademacher_vecs)

    # Unbiasedness: E[g (x) Ag] == diag(A)
    for i in range(n):
        assert abs(mean_est[i] - diag_A[i]) < 1e-12
    # Lemma 3: E[||r^1(A) - diag(A)||_2^2] == ||A_bar||_F^2 (independent of diag(A) because c_4 = E[g_i^4] = 1)
    assert abs(expected_sq_err_rademacher - off_diag_frob_sq) < 1e-12

    # 2. Lemma 4 boundary: Non-Rademacher mean-0 unit-variance probe with 4th moment c_4 > 1
    # Discrete symmetric distribution taking values {-sqrt(3), 0, +sqrt(3)} with probs {1/6, 2/3, 1/6}:
    # E[g] = 0, E[g^2] = 2*(1/6)*3 = 1, E[g^4] = 2*(1/6)*9 = 3 = c_4
    import math
    s3 = math.sqrt(3.0)
    vals = [(-s3, 1.0 / 6.0), (0.0, 2.0 / 3.0), (s3, 1.0 / 6.0)]
    non_rad_sq_err = 0.0
    for p0, p1, p2 in itertools.product(vals, repeat=n):
        g = [p0[0], p1[0], p2[0]]
        prob = p0[1] * p1[1] * p2[1]
        Ag = matvec(A, g)
        d_single = hadamard(g, Ag)
        err_sq = sum((d_single[i] - diag_A[i]) ** 2 for i in range(n))
        non_rad_sq_err += prob * err_sq

    c4 = 3.0
    lemma4_theoretical = off_diag_frob_sq + (c4 - 1.0) * diag_norm_sq
    assert abs(non_rad_sq_err - lemma4_theoretical) < 1e-9
    assert non_rad_sq_err > expected_sq_err_rademacher * 50.0

    print(
        f"[PASS] Round 827 Hutchinson Diagonal Estimator verified: "
        f"E_err_Rademacher={expected_sq_err_rademacher:.4f}==||A_bar||_F^2={off_diag_frob_sq:.4f}, "
        f"E_err_c4_3={non_rad_sq_err:.4f}=={lemma4_theoretical:.4f}"
    )


if __name__ == "__main__":
    main()
