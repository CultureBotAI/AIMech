#!/usr/bin/env python3
"""Boundary and regime verification for Needell & Tropp (2009)
CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples.
"""

import json
import math
import random


def norm(v):
    return math.sqrt(sum(z * z for z in v))


def top_k_indices(v, k):
    return sorted(range(len(v)), key=lambda i: (-abs(v[i]), i))[:k]


def solve_spd(A, b):
    n = len(b)
    M = [A[i][:] + [b[i]] for i in range(n)]
    for i in range(n):
        piv = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[piv] = M[piv], M[i]
        div = M[i][i]
        for c in range(i, n + 1):
            M[i][c] /= div
        for r in range(n):
            if r != i:
                fac = M[r][i]
                for c in range(i, n + 1):
                    M[r][c] -= fac * M[i][c]
    return [M[i][n] for i in range(n)]


def least_squares_on_support(Phi, u, T_list):
    m = len(Phi)
    k = len(T_list)
    G = [
        [sum(Phi[i][T_list[a]] * Phi[i][T_list[b]] for i in range(m)) for b in range(k)]
        for a in range(k)
    ]
    rhs = [sum(Phi[i][T_list[a]] * u[i] for i in range(m)) for a in range(k)]
    sol = solve_spd(G, rhs)
    b = [0.0] * len(Phi[0])
    for idx, val in zip(T_list, sol):
        b[idx] = val
    return b, G, rhs, sol


def main():
    rng = random.Random(20261019)
    m, N, s = 24, 32, 3

    Phi_raw = [[rng.gauss(0.0, 1.0 / math.sqrt(m)) for _ in range(N)] for _ in range(m)]
    Phi = [[0.0] * N for _ in range(m)]
    for j in range(N):
        cn = math.sqrt(sum(Phi_raw[i][j] ** 2 for i in range(m)))
        for i in range(m):
            Phi[i][j] = Phi_raw[i][j] / cn

    x_true = [0.0] * N
    x_true[2] = 3.0
    x_true[9] = -2.0
    x_true[19] = 1.25

    u_clean = [sum(Phi[i][j] * x_true[j] for j in range(N)) for i in range(m)]

    # 1. Run CoSaMP (Algorithm 2.1) on noiseless measurements and verify Lemmas 4.2-4.5 & Theorem 2.2
    a = [0.0] * N
    v = u_clean[:]
    iters_needed = 0
    richardson_3step_err = None

    for k in range(1, 10):
        # Identification: y = Phi^* v, Omega = supp(y_{2s})
        y = [sum(Phi[i][j] * v[i] for i in range(m)) for j in range(N)]
        Omega = set(top_k_indices(y, 2 * s))
        supp_a = {j for j, val in enumerate(a) if abs(val) > 1e-15}
        T = sorted(Omega | supp_a)

        # Estimation: b|_T = Phi_T^\dagger u
        b, G, rhs, sol_exact = least_squares_on_support(Phi, u_clean, T)

        # Verify Section 5.1 (Lemma 5.1): Richardson iteration z^{l+1} = A^* u - (A^* A - I) z^l
        # satisfies ||z^l - z*||_2 <= ||A^* A - I||^l ||z^0 - z*||_2
        if k == 1:
            dim_T = len(T)
            E_mat = [[G[r][c] - (1.0 if r == c else 0.0) for c in range(dim_T)] for r in range(dim_T)]
            # Power iteration for spectral norm of symmetric E_mat = A^* A - I
            v_pow = [1.0 / math.sqrt(dim_T)] * dim_T
            for _ in range(40):
                w_pow = [sum(E_mat[r][c] * v_pow[c] for c in range(dim_T)) for r in range(dim_T)]
                nw = norm(w_pow)
                v_pow = [w / nw for w in w_pow]
            c_T = norm([sum(E_mat[r][c] * v_pow[c] for c in range(dim_T)) for r in range(dim_T)])
            z = [a[idx] for idx in T]
            init_ls_err = norm([z[r] - sol_exact[r] for r in range(dim_T)])
            for step_l in range(1, 7):
                z = [
                    rhs[r] - sum(E_mat[r][c] * z[c] for c in range(dim_T))
                    for r in range(dim_T)
                ]
                cur_err = norm([z[r] - sol_exact[r] for r in range(dim_T)])
                assert cur_err <= (c_T ** step_l) * init_ls_err + 1e-12
                if step_l == 3:
                    richardson_3step_err = cur_err

        # Pruning: a^k = b_s (Lemma 4.5: ||x - b_s||_2 <= 2 ||x - b||_2)
        err_b = norm([x_true[j] - b[j] for j in range(N)])
        top_s = set(top_k_indices(b, s))
        a = [b[j] if j in top_s else 0.0 for j in range(N)]
        err_a = norm([x_true[j] - a[j] for j in range(N)])
        assert err_a <= 2.0 * err_b + 1e-12

        # Sample update: v = u - Phi a^k
        v = [u_clean[i] - sum(Phi[i][j] * a[j] for j in range(N)) for i in range(m)]
        if err_a < 1e-13:
            iters_needed = k
            break

    assert iters_needed > 0 and iters_needed <= 4
    assert richardson_3step_err is not None and richardson_3step_err < init_ls_err * (c_T ** 3) + 1e-12

    # 2. Verify Theorem 2.1 on compressible + noisy signal: ||x - a^k||_2 <= 2^{-k} ||x||_2 + 20 nu
    x_comp = x_true[:]
    x_comp[5] = 0.04
    x_comp[14] = -0.03
    e = [0.01 * math.cos(i) for i in range(m)]
    u_noisy = [
        sum(Phi[i][j] * x_comp[j] for j in range(N)) + e[i] for i in range(m)
    ]
    tail = [0.04, -0.03]
    nu = norm(tail) + sum(abs(z) for z in tail) / math.sqrt(s) + norm(e)

    a_n = [0.0] * N
    v_n = u_noisy[:]
    for _ in range(6):
        y = [sum(Phi[i][j] * v_n[i] for i in range(m)) for j in range(N)]
        Omega = set(top_k_indices(y, 2 * s))
        supp_a = {j for j, val in enumerate(a_n) if abs(val) > 1e-15}
        T = sorted(Omega | supp_a)
        b, _, _, _ = least_squares_on_support(Phi, u_noisy, T)
        top_s = set(top_k_indices(b, s))
        a_n = [b[j] if j in top_s else 0.0 for j in range(N)]
        v_n = [u_noisy[i] - sum(Phi[i][j] * a_n[j] for j in range(N)) for i in range(m)]

    noisy_err = norm([x_comp[j] - a_n[j] for j in range(N)])
    assert noisy_err <= 20.0 * nu

    summary = {
        "concept": "CoSaMPCompressiveSamplingMatchingPursuit",
        "exact_recovery_iterations": iters_needed,
        "noiseless_final_err": err_a,
        "richardson_3step_ls_err": round(richardson_3step_err, 6),
        "unrecoverable_energy_nu": round(nu, 6),
        "noisy_compressible_err": round(noisy_err, 6),
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
