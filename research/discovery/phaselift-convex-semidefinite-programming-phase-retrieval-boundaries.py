#!/usr/bin/env python3
"""Constructed boundary verification for PhaseLift (Candes, Strohmer, & Voroninski 2013, CPAM 66(8):1241-1274)."""

import json
import math
import random


def f_real_rank2(t):
    # Equation (3.3), Lemma 3.4: E|Z_1^2 - t Z_2^2| = (2/pi) * (2*sqrt(t) + (1-t)*(pi/2 - 2*atan(sqrt(t))))
    return (2.0 / math.pi) * (
        2.0 * math.sqrt(t) + (1.0 - t) * (math.pi / 2.0 - 2.0 * math.atan(math.sqrt(t)))
    )


def f_complex_rank2(t):
    # Equation (5.2), Lemma 5.2: E||Z_1|^2 - t|Z_2|^2| = (1 + t^2) / (1 + t)
    return (1.0 + t * t) / (1.0 + t)


def sym_eigen(A, max_iter=250):
    n = len(A)
    M = [row[:] for row in A]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(max_iter):
        p, q = 0, 1
        max_val = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(M[i][j]) > max_val:
                    max_val = abs(M[i][j])
                    p, q = i, j
        if max_val < 1e-12:
            break
        diff = M[q][q] - M[p][p]
        if abs(M[p][q]) < 1e-15:
            t = 0.0
        else:
            phi = diff / (2.0 * M[p][q])
            t = 1.0 / (abs(phi) + math.sqrt(phi * phi + 1.0))
            if phi < 0.0:
                t = -t
        c = 1.0 / math.sqrt(1.0 + t * t)
        s = t * c
        tau = s / (1.0 + c)
        h = t * M[p][q]
        M[p][p] -= h
        M[q][q] += h
        M[p][q] = 0.0
        M[q][p] = 0.0
        for i in range(n):
            if i != p and i != q:
                g = M[i][p]
                e = M[i][q]
                M[i][p] = g - s * (e + g * tau)
                M[p][i] = M[i][p]
                M[i][q] = e + s * (g - e * tau)
                M[q][i] = M[i][q]
        for i in range(n):
            g = V[i][p]
            e = V[i][q]
            V[i][p] = g - s * (e + g * tau)
            V[i][q] = e + s * (g - e * tau)
    evals = [M[i][i] for i in range(n)]
    idx = sorted(range(n), key=lambda i: evals[i], reverse=True)
    return [evals[i] for i in idx], [[V[row][idx[col]] for col in range(n)] for row in range(n)]


def S_op(X):
    # Section 4.1 Eq (4.1): S(X) = 2 X + Tr(X) I_n
    n = len(X)
    tr = sum(X[i][i] for i in range(n))
    return [[2.0 * X[i][j] + (tr if i == j else 0.0) for j in range(n)] for i in range(n)]


def S_inv_op(Y):
    # Section 4.1: S^{-1}(Y) = (1/2) (Y - (1/(n+2)) Tr(Y) I_n)
    n = len(Y)
    tr = sum(Y[i][i] for i in range(n))
    return [[0.5 * (Y[i][j] - (tr / (n + 2.0) if i == j else 0.0)) for j in range(n)] for i in range(n)]


def main():
    # 1. Verify Lemma 3.4 (real rank-2 L1 isometry) & Lemma 5.2 (complex rank-2 L1 isometry)
    grid_t = [i / 200.0 for i in range(201)]
    min_f_real = min(f_real_rank2(t) for t in grid_t)
    min_f_complex = min(f_complex_rank2(t) for t in grid_t)
    exact_min_complex = 2.0 * (math.sqrt(2.0) - 1.0)
    assert abs(f_real_rank2(0.0) - 1.0) < 1e-12
    assert abs(f_real_rank2(1.0) - 4.0 / math.pi) < 1e-12
    assert min_f_real > 0.94
    assert abs(min_f_complex - exact_min_complex) < 1e-4

    # Verify Lemma 3.4 polar-coordinate integral numerically at t = 0.25
    t_test = 0.25
    n_phi = 2000
    dphi = math.pi / n_phi
    num_int = (2.0 / math.pi) * sum(
        abs(math.cos((k + 0.5) * dphi) ** 2 - t_test * (math.sin((k + 0.5) * dphi) ** 2)) * dphi
        for k in range(n_phi)
    )
    assert abs(num_int - f_real_rank2(t_test)) < 1e-6

    # 2. Verify Section 4.1 operator S and S^{-1} and Section 4.4 Eq (4.9) exact moment algebra
    n = 6
    e1e1 = [[1.0 if (i == 0 and j == 0) else 0.0 for j in range(n)] for i in range(n)]
    recovered_e1e1 = S_op(S_inv_op(e1e1))
    max_s_err = max(abs(recovered_e1e1[i][j] - e1e1[i][j]) for i in range(n) for j in range(n))
    assert max_s_err < 1e-15

    # Exact expectation of ||y||_2^2 in Equation (4.9):
    # E[||y||_2^2] = (1/4)(15n + 90) - (1/(2(n+2)))(3n^2 + 30n + 72) + (1/(4(n+2)))(n+4)(n+6) - 1
    for n_val in [6, 10, 20]:
        E_y_norm_sq = (
            0.25 * (15 * n_val + 90)
            - (3 * n_val * n_val + 30 * n_val + 72) / (2.0 * (n_val + 2))
            + ((n_val + 4) * (n_val + 6)) / (4.0 * (n_val + 2))
            - 1.0
        )
        assert E_y_norm_sq <= 4.0 * (n_val + 4)
        E_y1_sq = 101.0 / 4.0 - (27.0 * n_val * n_val + 210.0 * n_val + 288.0) / (
            4.0 * ((n_val + 2) ** 2)
        )
        assert E_y1_sq <= 22.0

    # 3. Verify PhaseLift SDP recovery (Eq 1.5 / 7.1) via PSD-projected trace-regularized solver
    rng = random.Random(20261019)
    n_sig = 5
    m_meas = 45
    x_true = [1.0, -0.5, 0.8, -0.3, 0.6]
    norm_x = math.sqrt(sum(v * v for v in x_true))
    x_true = [v / norm_x for v in x_true]
    X_true = [[x_true[i] * x_true[j] for j in range(n_sig)] for i in range(n_sig)]

    Z_vecs = [[rng.gauss(0.0, 1.0) for _ in range(n_sig)] for _ in range(m_meas)]
    b_meas = [sum(Z_vecs[k][j] * x_true[j] for j in range(n_sig)) ** 2 for k in range(m_meas)]

    # Minimize (1/(2m)) ||A(X) - b||_2^2 + lam * Tr(X) subject to X >= 0 with continuation on lam
    X_est = [[0.0] * n_sig for _ in range(n_sig)]
    step = 0.12
    for stage, lam in enumerate([0.02, 0.002, 0.0001, 0.0]):
        n_iters = 120 if stage < 3 else 200
        for _ in range(n_iters):
            grad = [[lam if i == j else 0.0 for j in range(n_sig)] for i in range(n_sig)]
            for k in range(m_meas):
                z = Z_vecs[k]
                az = sum(
                    z[i] * X_est[i][j] * z[j] for i in range(n_sig) for j in range(n_sig)
                )
                res = (az - b_meas[k]) / m_meas
                for i in range(n_sig):
                    for j in range(n_sig):
                        grad[i][j] += res * z[i] * z[j]
            X_cand = [[X_est[i][j] - step * grad[i][j] for j in range(n_sig)] for i in range(n_sig)]
            evals, evecs = sym_eigen(X_cand)
            pos_evals = [max(0.0, ev) for ev in evals]
            X_est = [
                [
                    sum(pos_evals[k] * evecs[i][k] * evecs[j][k] for k in range(n_sig))
                    for j in range(n_sig)
                ]
                for i in range(n_sig)
            ]

    evals_final, evecs_final = sym_eigen(X_est)
    x_hat = [math.sqrt(max(0.0, evals_final[0])) * evecs_final[i][0] for i in range(n_sig)]
    frob_err = math.sqrt(
        sum((X_est[i][j] - X_true[i][j]) ** 2 for i in range(n_sig) for j in range(n_sig))
    )
    vec_err = min(
        math.sqrt(sum((x_hat[i] - x_true[i]) ** 2 for i in range(n_sig))),
        math.sqrt(sum((x_hat[i] + x_true[i]) ** 2 for i in range(n_sig))),
    )
    rank1_energy_ratio = evals_final[0] / sum(max(0.0, ev) for ev in evals_final)
    assert frob_err < 1e-3
    assert vec_err < 1e-3
    assert rank1_energy_ratio > 0.999

    out = {
        "rank2_l1_isometry_lemmas": {
            "f_real_at_0": round(f_real_rank2(0.0), 8),
            "f_real_at_1": round(f_real_rank2(1.0), 8),
            "min_f_real_on_0_1": round(min_f_real, 6),
            "min_f_complex_on_0_1": round(min_f_complex, 6),
            "exact_2_sqrt2_minus_1": round(exact_min_complex, 6),
        },
        "dual_certificate_moments": {
            "S_S_inv_max_err": max_s_err,
        },
        "phaselift_sdp_recovery": {
            "n": n_sig,
            "m": m_meas,
            "matrix_frob_err": round(frob_err, 6),
            "signal_vec_err": round(vec_err, 6),
            "top_eigenvalue_ratio": round(rank1_energy_ratio, 6),
        },
        "all_assertions_passed": True,
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
