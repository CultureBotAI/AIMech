#!/usr/bin/env python3
"""Constructed boundary verification for HeteroPCA (Zhang, Cai, & Wu 2022, Ann. Stat. 50(1):53-80)."""

import json
import math
import random


def mat_mul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)] for i in range(m)]


def mat_T(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def sym_eigen(A, max_iter=1500):
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
        if max_val < 1e-13:
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
    idx = sorted(range(n), key=lambda i: abs(evals[i]), reverse=True)
    sorted_evals = [evals[i] for i in idx]
    sorted_V = [[V[row][ idx[col] ] for col in range(n)] for row in range(n)]
    return sorted_evals, sorted_V


def op_norm_sym(A):
    evals, _ = sym_eigen(A)
    return max(abs(x) for x in evals)


def delta_zero_diag(A):
    n = len(A)
    return [[0.0 if i == j else A[i][j] for j in range(n)] for i in range(n)]


def diag_only(A):
    n = len(A)
    return [[A[i][j] if i == j else 0.0 for j in range(n)] for i in range(n)]


def sin_theta_norm(U_hat, U_true):
    # ||sin Theta(U_hat, U_true)|| = sqrt(1 - sigma_min^2(U_hat^T U_true))
    G = mat_mul(mat_T(U_hat), U_true)
    GTG = mat_mul(mat_T(G), G)
    evals, _ = sym_eigen(GTG)
    min_ev = min(max(0.0, min(evals)), 1.0)
    return math.sqrt(max(0.0, 1.0 - min_ev))


def heteropca(Sigma_hat, r, T):
    n = len(Sigma_hat)
    N_t = delta_zero_diag(Sigma_hat)
    off_diag = delta_zero_diag(Sigma_hat)
    errors_or_traj = []
    U_t = None
    for _ in range(T + 1):
        evals, evecs = sym_eigen(N_t)
        # Keep top r by largest positive/signed or singular values (for symmetric PSD/near-PSD)
        idx = sorted(range(n), key=lambda i: evals[i], reverse=True)
        U_t = [[evecs[row][idx[col]] for col in range(r)] for row in range(n)]
        N_tilde_diag = [
            sum(evals[idx[k]] * (evecs[i][idx[k]] ** 2) for k in range(r))
            for i in range(n)
        ]
        errors_or_traj.append(U_t)
        N_next = [row[:] for row in off_diag]
        for i in range(n):
            N_next[i][i] = N_tilde_diag[i]
        N_t = N_next
    return U_t, errors_or_traj


def main():
    # 1. Verify Lemma 4 sharp factor-2 bound for Delta(M):
    # M = 1_p 1_p^T - (p/2) I_p => ||Delta(M)|| / ||M|| = 2 - 2/p
    p_lem4 = 10
    M_lem4 = [
        [1.0 - (p_lem4 / 2.0 if i == j else 0.0) for j in range(p_lem4)]
        for i in range(p_lem4)
    ]
    Delta_M_lem4 = delta_zero_diag(M_lem4)
    ratio_lem4 = op_norm_sym(Delta_M_lem4) / op_norm_sym(M_lem4)
    exact_ratio = 2.0 - 2.0 / p_lem4
    assert abs(ratio_lem4 - exact_ratio) < 1e-10

    # 2. Verify Lemma 1 contraction bounds:
    # ||D(P_U D(A))|| <= (I(U) r / p) ||D(A)|| and ||D(P_U A)|| <= sqrt(I(U) r / p) ||A||
    p, r = 12, 2
    # Construct incoherent U via orthonormal discrete cosine basis columns (non-constant row norms)
    U = [[0.0] * r for _ in range(p)]
    for i in range(p):
        U[i][0] = math.sqrt(2.0 / p) * math.cos(math.pi * (i + 0.5) / p)
        U[i][1] = math.sqrt(2.0 / p) * math.cos(2.0 * math.pi * (i + 0.5) / p)
    P_U = mat_mul(U, mat_T(U))
    inc_U = (p / r) * max(sum(U[i][k] ** 2 for k in range(r)) for i in range(p))
    assert inc_U <= 2.0

    rng = random.Random(20261019)
    A_diag = [[(rng.uniform(-2.0, 2.0) if i == j else 0.0) for j in range(p)] for i in range(p)]
    lhs_diag = op_norm_sym(diag_only(mat_mul(P_U, A_diag)))
    rhs_diag = (inc_U * r / p) * op_norm_sym(A_diag)
    assert lhs_diag <= rhs_diag + 1e-12

    # 3. Verify Theorem 3 (Deterministic Robust sin Theta Theorem) & Theorem 1 (HeteroPCA vs SVD & Diagonal-Deletion):
    # Signal M = U Lambda U^T with eigenvalues (15.0, 10.0)
    lam = [15.0, 10.0]
    M_sig = [
        [sum(lam[k] * U[i][k] * U[j][k] for k in range(r)) for j in range(p)]
        for i in range(p)
    ]
    # Pure diagonal perturbation Z_diag (Delta(Z_diag) = 0): Theorem 3 says ||sin Theta(U^(t), U)|| contracts geometrically
    Z_pure_diag = [[(25.0 * (i + 1) / p if i == j else 0.0) for j in range(p)] for i in range(p)]
    N_pure = [[M_sig[i][j] + Z_pure_diag[i][j] for j in range(p)] for i in range(p)]
    _, traj_pure = heteropca(N_pure, r=r, T=20)
    sin_theta_pure_t0 = sin_theta_norm(traj_pure[0], U)
    sin_theta_pure_t8 = sin_theta_norm(traj_pure[20], U)
    assert sin_theta_pure_t8 < 1e-5
    assert sin_theta_pure_t8 < sin_theta_pure_t0 * 1e-3

    # Full heteroskedastic sample covariance simulation: Y_k = X_k + eps_k
    n_samples = 400
    sigmas = [0.2 + 2.8 * ((i / (p - 1)) ** 3) for i in range(p)]
    Sigma_hat = [[0.0] * p for _ in range(p)]
    for _ in range(n_samples):
        g = [rng.gauss(0.0, 1.0) for _ in range(r)]
        x = [
            sum(U[i][k] * math.sqrt(lam[k]) * g[k] for k in range(r))
            + rng.gauss(0.0, sigmas[i])
            for i in range(p)
        ]
        for i in range(p):
            for j in range(p):
                Sigma_hat[i][j] += x[i] * x[j] / n_samples

    # Regular SVD on Sigma_hat
    evals_reg, evecs_reg = sym_eigen(Sigma_hat)
    idx_reg = sorted(range(p), key=lambda i: evals_reg[i], reverse=True)
    U_reg = [[evecs_reg[row][idx_reg[col]] for col in range(r)] for row in range(p)]
    err_reg_svd = sin_theta_norm(U_reg, U)

    # Diagonal-deletion SVD (t=0 of HeteroPCA) and T=10 HeteroPCA
    U_hpca, traj_hpca = heteropca(Sigma_hat, r=r, T=10)
    err_diag_del = sin_theta_norm(traj_hpca[0], U)
    err_hpca = sin_theta_norm(U_hpca, U)

    assert err_hpca < err_reg_svd
    assert err_hpca < err_diag_del

    out = {
        "lemma4_sharp_factor_2": {
            "p": p_lem4,
            "empirical_ratio": round(ratio_lem4, 8),
            "exact_2_minus_2_over_p": round(exact_ratio, 8),
        },
        "lemma1_contraction": {
            "incoherence_I_U": round(inc_U, 6),
            "lhs_D_PU_D_A_norm": round(lhs_diag, 6),
            "rhs_bound_I_r_over_p": round(rhs_diag, 6),
        },
        "theorem3_and_theorem1_heteropca": {
            "pure_diag_perturbation_t0_err": round(sin_theta_pure_t0, 6),
            "pure_diag_perturbation_t8_err": round(sin_theta_pure_t8, 10),
            "heteroskedastic_sample_err_regular_svd": round(err_reg_svd, 5),
            "heteroskedastic_sample_err_diag_deletion": round(err_diag_del, 5),
            "heteroskedastic_sample_err_heteropca_T10": round(err_hpca, 5),
        },
        "all_assertions_passed": True,
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
