#!/usr/bin/env python3
"""Constructed boundary verification for Procrustes Flow Low-Rank Matrix Recovery (Tu et al. 2016)."""

import json
import math


def mat_mul(A, B):
    n = len(A)
    k = len(B)
    m = len(B[0])
    return [[sum(A[i][p] * B[p][j] for p in range(k)) for j in range(m)] for i in range(n)]


def mat_t(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def mat_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mat_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mat_scale(c, A):
    return [[c * x for x in row] for row in A]


def frob_sq(A):
    return sum(x * x for row in A for x in row)


def frob_norm(A):
    return math.sqrt(frob_sq(A))


def mat_inner(A, B):
    return sum(A[i][j] * B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def best_ortho_2x2(P):
    # Exact orthogonal polar factor R = A B^T of 2x2 matrix P = X^T U
    # Maximizes trace(P R^T) = (p00 + p11) cos(theta) + (p01 - p10) sin(theta) or reflection
    best_R = None
    best_tr = -1e18
    for det_sign in (1.0, -1.0):
        c_part = P[0][0] + det_sign * P[1][1]
        s_part = P[1][0] - det_sign * P[0][1]
        r_len = math.hypot(c_part, s_part)
        if r_len > 1e-15:
            co = c_part / r_len
            si = s_part / r_len
        else:
            co, si = 1.0, 0.0
        R = [[co, -det_sign * si], [si, det_sign * co]]
        tr = P[0][0] * R[0][0] + P[0][1] * R[0][1] + P[1][0] * R[1][0] + P[1][1] * R[1][1]
        if tr > best_tr:
            best_tr = tr
            best_R = R
    return best_R


def procrustes_dist_r2(U, X):
    P = mat_mul(mat_t(X), U)
    R = best_ortho_2x2(P)
    XR = mat_mul(X, R)
    return frob_norm(mat_sub(U, XR)), XR


def main():
    # Scenario A: Symmetric PSD Procrustes Flow Regularity Condition RC(alpha, beta, delta) and Geometric Convergence (Algorithm 1, Theorem 3.2, Lemmas 5.4 & 5.7)
    n = 5
    # Construct rank-2 X in R^{5x2} with orthogonal columns of singular values sigma_1(X)=2.0, sigma_2(X)=1.2
    X = [
        [2.0, 0.0],
        [0.0, 1.2],
        [0.0, 0.0],
        [0.0, 0.0],
        [0.0, 0.0],
    ]
    sigma_r_X = 1.2
    sigma_1_X = 2.0
    M_psd = mat_mul(X, mat_t(X))

    # Perturbed initial factor U0 within basin dist(U0, X) <= (1/4) sigma_r(X) = 0.30 (Eq. 3.3)
    # Apply an orthogonal rotation R0 and small perturbation
    ang = 0.6
    R0 = [[math.cos(ang), -math.sin(ang)], [math.sin(ang), math.cos(ang)]]
    Delta0 = [
        [0.08, -0.06],
        [0.05, 0.07],
        [0.06, -0.05],
        [-0.04, 0.05],
        [0.03, -0.03],
    ]
    U0 = mat_add(mat_mul(X, R0), Delta0)
    dist0, XR0 = procrustes_dist_r2(U0, X)
    assert dist0 <= 0.25 * sigma_r_X

    # Verify Lemma 5.4: dist^2(U0, X) <= ||U0 U0^T - X X^T||_F^2 / (2 (sqrt(2) - 1) sigma_r^2(X))
    diff_M0 = mat_sub(mat_mul(U0, mat_t(U0)), M_psd)
    lemma54_rhs = frob_sq(diff_M0) / (2.0 * (math.sqrt(2.0) - 1.0) * (sigma_r_X ** 2))
    assert dist0 * dist0 <= lemma54_rhs

    # Verify Lemma 5.7 regularity inequality (Eq. 5.5) at U0
    grad_F0 = mat_mul(diff_M0, U0)
    H0 = mat_sub(U0, XR0)
    lhs_57 = mat_inner(grad_F0, H0) - 0.05 * (frob_sq(diff_M0) + frob_sq(mat_mul(H0, mat_t(U0))))
    rhs_57 = 0.25 * (sigma_r_X ** 2) * frob_sq(H0) + 0.20 * frob_sq(diff_M0)
    assert lhs_57 >= rhs_57

    # Run Procrustes Flow gradient updates (Eq. 2.3)
    U = [row[:] for row in U0]
    mu_step = 0.25
    u0_norm_sq = sigma_1_X * sigma_1_X
    dists_psd = [dist0]
    for _ in range(120):
        diff = mat_sub(mat_mul(U, mat_t(U)), M_psd)
        grad = mat_mul(diff, U)
        U = mat_sub(U, mat_scale(mu_step / u0_norm_sq, grad))
        d_cur, _ = procrustes_dist_r2(U, X)
        dists_psd.append(d_cur)

    assert dists_psd[-1] < 1e-5
    assert all(dists_psd[t + 1] < dists_psd[t] for t in range(len(dists_psd) - 1))

    # Scenario B: Rectangular Procrustes Flow with Factor-Balancing Regularizer (1/16)||U^T U - V^T V||_F^2 (Algorithm 2, Theorem 3.3, Eqs. 2.4-2.6)
    X_rect = [
        [1.8, 0.0],
        [0.0, 1.2],
        [0.0, 0.0],
        [0.0, 0.0],
    ]
    Y_rect = [
        [0.0, 1.2],
        [1.8, 0.0],
        [0.0, 0.0],
        [0.0, 0.0],
    ]
    M_rect = mat_mul(X_rect, mat_t(Y_rect))

    # Start from unbalanced perturbed factors in the rank-2 subspace to test factor-balancing regularizer
    U_r = [
        [1.8 * 1.15, -0.12],
        [0.10, 1.2 * 1.10],
        [0.08, -0.05],
        [-0.06, 0.04],
    ]
    V_r = [
        [-0.08, 1.2 * 0.88],
        [1.8 * 0.85, 0.09],
        [0.0, 0.0],
        [0.0, 0.0],
    ]

    imbalance_init = frob_norm(mat_sub(mat_mul(mat_t(U_r), U_r), mat_mul(mat_t(V_r), V_r)))
    err_rect_init = frob_norm(mat_sub(mat_mul(U_r, mat_t(V_r)), M_rect))

    eta = 0.06
    for _ in range(350):
        res = mat_sub(mat_mul(U_r, mat_t(V_r)), M_rect)
        imb = mat_sub(mat_mul(mat_t(U_r), U_r), mat_mul(mat_t(V_r), V_r))
        grad_U = mat_add(mat_mul(res, V_r), mat_scale(0.25, mat_mul(U_r, imb)))
        grad_V = mat_sub(mat_mul(mat_t(res), U_r), mat_scale(0.25, mat_mul(V_r, imb)))
        U_r = mat_sub(U_r, mat_scale(eta, grad_U))
        V_r = mat_sub(V_r, mat_scale(eta, grad_V))

    imbalance_final = frob_norm(mat_sub(mat_mul(mat_t(U_r), U_r), mat_mul(mat_t(V_r), V_r)))
    err_rect_final = frob_norm(mat_sub(mat_mul(U_r, mat_t(V_r)), M_rect))
    assert err_rect_final < 1e-6
    assert imbalance_final < 1e-6

    summary = {
        "psd_init_procrustes_dist": round(dist0, 5),
        "lemma54_upper_bound_sq": round(lemma54_rhs, 5),
        "lemma57_regularity_lhs": round(lhs_57, 5),
        "lemma57_regularity_rhs": round(rhs_57, 5),
        "psd_final_procrustes_dist": dists_psd[-1],
        "rect_init_matrix_err": round(err_rect_init, 5),
        "rect_final_matrix_err": err_rect_final,
        "rect_init_factor_imbalance": round(imbalance_init, 5),
        "rect_final_factor_imbalance": imbalance_final,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
