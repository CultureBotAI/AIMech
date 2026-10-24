#!/usr/bin/env python3
"""Constructed boundary verification for Nonconvex Matrix Completion No Spurious Local Minimum (Ge, Lee, & Ma 2016)."""

import json
import math
import random


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def norm2(u):
    return math.sqrt(dot(u, u))


def grad_full_rank1(x, z):
    # Section 3 Eq (3.4): g(x) = (1/2)||z z^T - x x^T||_F^2, grad g(x) = (||x||^2 - <x,z>*...) -> 2 (x x^T - z z^T) x
    # Using paper's normalization in Section 4 Proposition 4.1: grad f(x) = 2 (x x^T - M) x
    xz = dot(x, z)
    xx = dot(x, x)
    return [2.0 * (xx * xi - xz * zi) for xi, zi in zip(x, z)]


def hess_quad_form_full_rank1(x, z, v):
    # Proposition 4.1 Eq (4.3): v^T nabla^2 g(x) v = ||v x^T + x v^T||_F^2 - 2 v^T (z z^T - x x^T) v
    vx = dot(v, x)
    vv = dot(v, v)
    xx = dot(x, x)
    vz = dot(v, z)
    norm_vx_xv_sq = 2.0 * vv * xx + 2.0 * (vx ** 2)
    rhs = 2.0 * (vz ** 2 - vx ** 2)
    return norm_vx_xv_sq - rhs


def reg_R_and_grad(X, alpha, lam):
    # Section 5 Eq (5.1) & Proposition 5.2: R(X) = sum_i (||X_i|| - alpha)^4 I_{||X_i|| >= alpha}
    # grad R(X)_i = 4 (||X_i|| - alpha)^3 / ||X_i|| * X_i
    d, r = len(X), len(X[0])
    val = 0.0
    G = [[0.0] * r for _ in range(d)]
    for i in range(d):
        row_norm = math.sqrt(sum(X[i][k] ** 2 for k in range(r)))
        if row_norm > alpha:
            diff = row_norm - alpha
            val += lam * (diff ** 4)
            scale = 4.0 * lam * (diff ** 3) / row_norm
            for k in range(r):
                G[i][k] = scale * X[i][k]
    return val, G


def main():
    # 1. Verify Section 3 Claims 1f & 2f and Proposition 4.1:
    # At saddle point x = 0, grad g(0) = 0, but <z, nabla^2 g(0) z> = -2 ||z||^4 = -2 < 0 (strict negative curvature).
    # At any orthogonal eigenvector x perp z, grad g(x) = 2 ||x||^2 x != 0 unless x = 0.
    # At global minima x = +-z, grad g(+-z) = 0 and <v, nabla^2 g(+-z) v> = 4 <v, z>^2 >= 0.
    d = 8
    z = [1.0 / math.sqrt(d) for _ in range(d)]
    x_zero = [0.0] * d
    curv_at_zero = hess_quad_form_full_rank1(x_zero, z, z)
    assert abs(curv_at_zero - (-2.0)) < 1e-12

    curv_at_z = hess_quad_form_full_rank1(z, z, z)
    assert abs(curv_at_z - 4.0) < 1e-12

    # Claim 2f: if <z, nabla^2 g(x) z> >= 0, then 2||x||^2 + 4<x,z>^2 >= 2 => ||x||^2 >= 1/3
    for scale in [0.5, 0.57, 0.58, 0.8, 1.0]:
        x_test = [scale * zi for zi in z]
        qf = hess_quad_form_full_rank1(x_test, z, z)
        if qf >= 0.0:
            assert dot(x_test, x_test) >= 1.0 / 3.0 - 1e-12

    # 2. Verify Proposition 5.2, Lemma 5.7, and Claim C.3 for the row-norm regularizer R(X):
    # For any U with U U^T = Z Z^T (so ||U_i|| = ||Z_i|| <= mu*sqrt(r/d)) and alpha >= 2*mu*sqrt(r/d),
    # <grad R(X), X - U> >= 0.
    rng = random.Random(20261019)
    r = 2
    Z = [[1.0 / math.sqrt(d) if k == 0 else ((1.0 if i % 2 == 0 else -1.0) / math.sqrt(d)) for k in range(r)] for i in range(d)]
    # Orthonormal rotation R_rot
    theta = 0.6
    R_rot = [[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]]
    U = [[sum(Z[i][p] * R_rot[p][q] for p in range(r)) for q in range(r)] for i in range(d)]
    alpha = 2.5 * math.sqrt(r / d)
    # Create coherent X with spiked rows
    X_spiky = [[rng.uniform(-2.0, 2.0) for _ in range(r)] for _ in range(d)]
    _, grad_R = reg_R_and_grad(X_spiky, alpha=alpha, lam=1.0)
    inner_gradR_X_minus_U = sum(
        grad_R[i][k] * (X_spiky[i][k] - U[i][k]) for i in range(d) for k in range(r)
    )
    assert inner_gradR_X_minus_U > 0.0

    # 3. Verify Theorem 1.1 / Theorem 5.3: Gradient descent from multiple arbitrary/random initializations
    # on f(X) = (1/2) ||P_Omega(M - X X^T)||_F^2 + lam * R(X) converges to global minimum X X^T = M.
    M_true = [[sum(Z[i][k] * Z[j][k] for k in range(r)) for j in range(d)] for i in range(d)]
    p_obs = 0.75
    Omega = [[False] * d for _ in range(d)]
    for i in range(d):
        Omega[i][i] = True
        for j in range(i + 1, d):
            if rng.random() < p_obs:
                Omega[i][j] = True
                Omega[j][i] = True

    max_final_frob_err = 0.0
    init_frob_errs = []
    for trial in range(3):
        X = [[rng.gauss(0.0, 0.35) for _ in range(r)] for _ in range(d)]
        XXT_init = [[sum(X[i][k] * X[j][k] for k in range(r)) for j in range(d)] for i in range(d)]
        init_err = math.sqrt(sum((XXT_init[i][j] - M_true[i][j]) ** 2 for i in range(d) for j in range(d)))
        init_frob_errs.append(round(init_err, 5))

        lr = 0.06
        for _ in range(800):
            _, gR = reg_R_and_grad(X, alpha=alpha, lam=0.2)
            # Residual P_Omega(X X^T - M)
            Res = [[0.0] * d for _ in range(d)]
            for i in range(d):
                for j in range(d):
                    if Omega[i][j]:
                        Res[i][j] = (sum(X[i][k] * X[j][k] for k in range(r)) - M_true[i][j]) / p_obs
            for i in range(d):
                for k in range(r):
                    grad_ik = 2.0 * sum(Res[i][j] * X[j][k] for j in range(d)) + gR[i][k]
                    X[i][k] -= lr * grad_ik

        XXT_final = [[sum(X[i][k] * X[j][k] for k in range(r)) for j in range(d)] for i in range(d)]
        final_err = math.sqrt(sum((XXT_final[i][j] - M_true[i][j]) ** 2 for i in range(d) for j in range(d)))
        max_final_frob_err = max(max_final_frob_err, final_err)

    assert max_final_frob_err < 1e-6

    out = {
        "rank1_landscape_geometry": {
            "curvature_at_origin_saddle": round(curv_at_zero, 6),
            "curvature_at_global_min_z": round(curv_at_z, 6),
        },
        "row_norm_regularizer_claim_c3": {
            "alpha": round(alpha, 5),
            "inner_product_gradR_X_minus_U": round(inner_gradR_X_minus_U, 6),
        },
        "random_init_gd_convergence": {
            "d": d,
            "r": r,
            "p_obs": p_obs,
            "init_frob_errors": init_frob_errs,
            "max_final_frob_error": max_final_frob_err,
        },
        "all_assertions_passed": True,
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
