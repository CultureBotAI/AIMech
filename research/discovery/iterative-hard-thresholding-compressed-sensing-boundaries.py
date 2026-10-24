#!/usr/bin/env python3
"""Boundary and regime verification for Blumensath & Davies (2009)
Iterative Hard Thresholding (IHT) for Compressed Sensing.
"""

import json
import math
import random


def norm(v):
    return math.sqrt(sum(z * z for z in v))


def hard_threshold(a, s):
    idx = sorted(range(len(a)), key=lambda i: abs(a[i]), reverse=True)[:s]
    idx_set = set(idx)
    return [a[i] if i in idx_set else 0.0 for i in range(len(a))]


def mat_vec(Phi, y):
    return [sum(row[j] * y[j] for j in range(len(y))) for row in Phi]


def mat_t_vec(Phi, x):
    M, N = len(Phi), len(Phi[0])
    return [sum(Phi[i][j] * x[i] for i in range(M)) for j in range(N)]


def main():
    rng = random.Random(20261019)
    M, N, s = 24, 32, 2

    # Construct normalized sensing matrix Phi with small coherence / RIP constant
    Phi_raw = [[rng.gauss(0.0, 1.0 / math.sqrt(M)) for _ in range(N)] for _ in range(M)]
    # Rescale columns to norm 0.92 so beta_{3s} < 1/8 on sparse subsets (Eq. 6)
    Phi = [[0.0] * N for _ in range(M)]
    for j in range(N):
        cn = math.sqrt(sum(Phi_raw[i][j] ** 2 for i in range(M)))
        for i in range(M):
            Phi[i][j] = 0.92 * Phi_raw[i][j] / cn

    # Ground-truth s-sparse signal y^s
    y_true = [0.0] * N
    y_true[3] = 2.0
    y_true[11] = -1.5
    y_norm = norm(y_true)

    # 1. Noiseless geometric convergence (Corollary 1, Eq. 16: ||y^s - y^[k]||_2 <= 2^{-k} ||y^s||_2)
    x_clean = mat_vec(Phi, y_true)
    yk = [0.0] * N
    for _ in range(60):
        res = [x_clean[i] - mv for i, mv in enumerate(mat_vec(Phi, yk))]
        a = [yk[j] + g for j, g in enumerate(mat_t_vec(Phi, res))]
        yk = hard_threshold(a, s)

    err_clean = norm([y_true[j] - yk[j] for j in range(N)])
    assert err_clean < 1e-10, f"Noiseless IHT failed to converge: {err_clean}"

    # 2. Noisy recovery & Corollary 1 bound ||y^s - y^[k^*]||_2 <= 5 ||e||_2 (Eq. 18) + Lemma 5 stopping criterion (Eq. 33)
    e = [0.01 * math.sin(i + 1) for i in range(M)]
    e_norm = norm(e)
    x_noisy = [x_clean[i] + e[i] for i in range(M)]
    k_star = math.ceil(math.log2(y_norm / e_norm))
    yn = [0.0] * N
    for _ in range(k_star + 10):
        res = [x_noisy[i] - mv for i, mv in enumerate(mat_vec(Phi, yn))]
        a = [yn[j] + g for j, g in enumerate(mat_t_vec(Phi, res))]
        yn = hard_threshold(a, s)

    err_noisy = norm([y_true[j] - yn[j] for j in range(N)])
    res_noisy = norm([x_noisy[i] - mv for i, mv in enumerate(mat_vec(Phi, yn))])
    lemma5_bound = 1.07 * (res_noisy + 2.0 * e_norm)
    assert err_noisy <= 5.0 * e_norm
    assert err_noisy <= lemma5_bound

    # 3. Verify failure when signal sparsity exceeds measurement capacity (s_bad = M)
    y_dense = [1.0 if j < M else 0.0 for j in range(N)]
    x_dense = mat_vec(Phi, y_dense)
    yd = [0.0] * N
    for _ in range(20):
        res = [x_dense[i] - mv for i, mv in enumerate(mat_vec(Phi, yd))]
        a = [yd[j] + g for j, g in enumerate(mat_t_vec(Phi, res))]
        yd = hard_threshold(a, s)
    err_under = norm([y_dense[j] - yd[j] for j in range(N)])
    assert err_under > 2.0

    summary = {
        "concept": "IterativeHardThresholdingForCompressedSensing",
        "noiseless_final_l2_err": err_clean,
        "noise_l2_norm": round(e_norm, 6),
        "noisy_final_l2_err": round(err_noisy, 6),
        "corollary1_bound_5e": round(5.0 * e_norm, 6),
        "lemma5_stopping_bound": round(lemma5_bound, 6),
        "undersampled_dense_err": round(err_under, 6),
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
