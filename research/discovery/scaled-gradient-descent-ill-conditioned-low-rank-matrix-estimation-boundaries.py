#!/usr/bin/env python3
"""Constructed boundary verification for Scaled Gradient Descent (ScaledGD) for
ill-conditioned low-rank matrix estimation (Tong, Ma, & Chi 2021, JMLR 22(150):1-63).

Verifies:
1. ScaledGD iteration (Eq. 3):
   L_{t+1} = L_t - eta * grad_L f(L_t R_t^T) (R_t^T R_t)^{-1},
   R_{t+1} = R_t - eta * grad_R f(L_t R_t^T) (L_t^T L_t)^{-1}.
2. Equivariance with respect to invertible factor reparameterization (Section 2.1):
   Replacing (L_t, R_t) by (L_t Q, R_t Q^{-T}) produces iterates
   (L_{t+1} Q, R_{t+1} Q^{-T}) and identical product matrix X_{t+1} = L_{t+1} R_{t+1}^T.
3. Condition-number-independent linear convergence rate (Theorem 1):
   On low-rank matrix factorization X_star = U_star Sigma_star V_star^T with
   condition number kappa = sigma_1 / sigma_r = 25, ScaledGD with step size
   eta = 0.5 contracts at a rate independent of kappa (reaching < 1e-12 in 45
   steps), whereas vanilla factored GD with optimal step size eta / sigma_1
   slows down by factor kappa (remaining > 1e-2 after 45 steps).
"""

import json
import math


def mat_mul(A, B):
    m = len(A)
    k = len(B)
    n = len(B[0])
    return [
        [sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)]
        for i in range(m)
    ]


def mat_transpose(A):
    m = len(A)
    n = len(A[0])
    return [[A[i][j] for i in range(m)] for j in range(n)]


def mat_sub(A, B):
    return [[a - b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(A, B)]


def mat_scale(A, c):
    return [[c * x for x in row] for row in A]


def frob_norm(A):
    return math.sqrt(sum(x * x for row in A for x in row))


def inv_2x2(M):
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    return [
        [M[1][1] / det, -M[0][1] / det],
        [-M[1][0] / det, M[0][0] / det],
    ]


def scaled_gd_step(L, R, X_star, eta):
    # f(L, R) = 0.5 * ||L R^T - X_star||_F^2
    # grad_L = (L R^T - X_star) R, grad_R = (L R^T - X_star)^T L
    X = mat_mul(L, mat_transpose(R))
    Diff = mat_sub(X, X_star)
    grad_L = mat_mul(Diff, R)
    grad_R = mat_mul(mat_transpose(Diff), L)
    RtR_inv = inv_2x2(mat_mul(mat_transpose(R), R))
    LtL_inv = inv_2x2(mat_mul(mat_transpose(L), L))
    step_L = mat_scale(mat_mul(grad_L, RtR_inv), eta)
    step_R = mat_scale(mat_mul(grad_R, LtL_inv), eta)
    return mat_sub(L, step_L), mat_sub(R, step_R)


def vanilla_gd_step(L, R, X_star, eta_gd):
    X = mat_mul(L, mat_transpose(R))
    Diff = mat_sub(X, X_star)
    grad_L = mat_mul(Diff, R)
    grad_R = mat_mul(mat_transpose(Diff), L)
    return (
        mat_sub(L, mat_scale(grad_L, eta_gd)),
        mat_sub(R, mat_scale(grad_R, eta_gd)),
    )


def main():
    # Ground-truth rank-2 matrix of size 4x4 with singular values sigma_1 = 25.0, sigma_2 = 1.0 (kappa = 25)
    sigma1 = 25.0
    sigma2 = 1.0
    kappa = sigma1 / sigma2
    L_star = [
        [math.sqrt(sigma1), 0.0],
        [0.0, math.sqrt(sigma2)],
        [0.0, 0.0],
        [0.0, 0.0],
    ]
    R_star = [
        [math.sqrt(sigma1), 0.0],
        [0.0, math.sqrt(sigma2)],
        [0.0, 0.0],
        [0.0, 0.0],
    ]
    X_star = mat_mul(L_star, mat_transpose(R_star))
    x_star_norm = frob_norm(X_star)

    # Perturbed initialization within the local basin
    L0 = [
        [math.sqrt(sigma1) * 0.96, 0.05],
        [-0.04, math.sqrt(sigma2) * 0.92],
        [0.03, -0.02],
        [-0.02, 0.04],
    ]
    R0 = [
        [math.sqrt(sigma1) * 0.95, -0.04],
        [0.03, math.sqrt(sigma2) * 0.94],
        [-0.02, 0.03],
        [0.04, -0.03],
    ]

    # 1. Verify exact equivariance under invertible 2x2 transformation Q
    Q = [[1.7, 0.4], [-0.3, 0.9]]
    Q_inv = inv_2x2(Q)
    Q_inv_T = mat_transpose(Q_inv)
    L0_tilde = mat_mul(L0, Q)
    R0_tilde = mat_mul(R0, Q_inv_T)

    L1, R1 = scaled_gd_step(L0, R0, X_star, eta=0.5)
    L1_tilde, R1_tilde = scaled_gd_step(L0_tilde, R0_tilde, X_star, eta=0.5)
    X1 = mat_mul(L1, mat_transpose(R1))
    X1_tilde = mat_mul(L1_tilde, mat_transpose(R1_tilde))
    equivariance_diff = frob_norm(mat_sub(X1, X1_tilde))
    assert equivariance_diff < 1e-13, f"Equivariance violated: {equivariance_diff}"

    # 2. Verify kappa-independent linear convergence of ScaledGD vs. kappa-dependent vanilla GD
    eta_scaled = 0.5
    eta_vanilla = 0.5 / sigma1
    L_sc, R_sc = [row[:] for row in L0], [row[:] for row in R0]
    L_gd, R_gd = [row[:] for row in L0], [row[:] for row in R0]

    n_iters = 45
    for _ in range(n_iters):
        L_sc, R_sc = scaled_gd_step(L_sc, R_sc, X_star, eta_scaled)
        L_gd, R_gd = vanilla_gd_step(L_gd, R_gd, X_star, eta_vanilla)

    err_scaled = frob_norm(mat_sub(mat_mul(L_sc, mat_transpose(R_sc)), X_star)) / x_star_norm
    err_vanilla = frob_norm(mat_sub(mat_mul(L_gd, mat_transpose(R_gd)), X_star)) / x_star_norm

    assert err_scaled < 1e-12, f"ScaledGD failed fast contraction: {err_scaled}"
    assert err_vanilla > 1e-3, f"Vanilla GD unexpectedly fast on kappa=25: {err_vanilla}"

    # 3. Also test kappa = 100 to verify ScaledGD iteration error is invariant to kappa
    sigma1_hi = 100.0
    L_star_hi = [
        [math.sqrt(sigma1_hi), 0.0],
        [0.0, math.sqrt(sigma2)],
        [0.0, 0.0],
        [0.0, 0.0],
    ]
    X_star_hi = mat_mul(L_star_hi, mat_transpose(L_star_hi))
    L_sc_hi = [
        [math.sqrt(sigma1_hi) * 0.96, 0.05],
        [-0.04, math.sqrt(sigma2) * 0.92],
        [0.03, -0.02],
        [-0.02, 0.04],
    ]
    R_sc_hi = [
        [math.sqrt(sigma1_hi) * 0.95, -0.04],
        [0.03, math.sqrt(sigma2) * 0.94],
        [-0.02, 0.03],
        [0.04, -0.03],
    ]
    for _ in range(n_iters):
        L_sc_hi, R_sc_hi = scaled_gd_step(L_sc_hi, R_sc_hi, X_star_hi, eta_scaled)
    err_scaled_hi = frob_norm(mat_sub(mat_mul(L_sc_hi, mat_transpose(R_sc_hi)), X_star_hi)) / frob_norm(X_star_hi)
    assert err_scaled_hi < 1e-12, f"ScaledGD failed kappa=100 contraction: {err_scaled_hi}"

    summary = {
        "concept": "ScaledGradientDescentForIllConditionedLowRankMatrixEstimation",
        "condition_number_kappa": kappa,
        "equivariance_product_diff": equivariance_diff,
        "iterations": n_iters,
        "scaled_gd_rel_err_kappa_25": err_scaled,
        "scaled_gd_rel_err_kappa_100": err_scaled_hi,
        "vanilla_gd_rel_err_kappa_25": round(err_vanilla, 6),
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
