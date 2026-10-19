#!/usr/bin/env python3
"""Boundary and regime verification for Ge, Huang, Jin, & Yuan (2015)
Strict Saddle Property and Noisy Stochastic Gradient Descent for Orthogonal Tensor Decomposition.
"""

import json
import math
import random


def normalize(v):
    n = math.sqrt(sum(z * z for z in v))
    return [z / n for z in v]


def cross_corr_obj(U):
    """Objective (13) / (171): sum_{i != j} sum_k (U_{ik} U_{jk})^2 in standard basis a_k = e_k."""
    d = len(U)
    total = 0.0
    for i in range(d):
        for j in range(d):
            if i != j:
                total += sum((U[i][k] * U[j][k]) ** 2 for k in range(d))
    return 0.5 * total


def tangent_grad_and_hessian_quad(U):
    """Compute Riemannian tangent gradient chi(U) (Eq. 177) and verify strict-saddle negative curvature (Lemma 44)."""
    d = len(U)
    # h(u^(i), u^(j)) = sum_l U_{il}^2 U_{jl}^2
    h = [[sum((U[i][l] * U[j][l]) ** 2 for l in range(d)) for j in range(d)] for i in range(d)]
    psi = [
        [
            sum((U[j][k] ** 2) - h[j][i] for j in range(d) if j != i)
            for k in range(d)
        ]
        for i in range(d)
    ]
    chi = [[2.0 * U[i][k] * psi[i][k] for k in range(d)] for i in range(d)]
    return chi, psi


def eval_M_quadratic_form(U, psi, V):
    """Evaluate v^T M(U) v using Equation (179)."""
    d = len(U)
    total = 0.0
    for k in range(d):
        for i in range(d):
            total += 2.0 * psi[i][k] * (V[i][k] ** 2)
            for ip in range(d):
                if ip != i:
                    total += 4.0 * U[ip][k] * U[i][k] * V[i][k] * V[ip][k]
    return total


def main():
    d = 3

    # 1. Verify Lemma 44 (Strict Saddle Negative Curvature) at a symmetric saddle point U_saddle
    # where u^(0) and u^(1) share support {0, 1}
    s2 = 1.0 / math.sqrt(2.0)
    U_saddle = [
        [s2, s2, 0.0],
        [s2, -s2, 0.0],
        [0.0, 0.0, 1.0],
    ]
    chi_s, psi_s = tangent_grad_and_hessian_quad(U_saddle)
    chi_norm_s = math.sqrt(sum(chi_s[i][k] ** 2 for i in range(d) for k in range(d)))
    assert chi_norm_s < 1e-15, f"Expected stationary point at U_saddle: {chi_norm_s}"

    # Construct tangent vector v from Lemma 44 Case 1 (Eq. 182-183)
    V_dir = [[0.0] * d for _ in range(d)]
    # Here U_{00} U_{10} U_{01} U_{11} = (1/2) * (-1/2) = -1/4 < 0
    V_dir[0][0] = U_saddle[0][1] / 4.0
    V_dir[0][1] = -U_saddle[0][0] / 4.0
    V_dir[1][0] = U_saddle[1][1] / 4.0
    V_dir[1][1] = -U_saddle[1][0] / 4.0
    v_norm = math.sqrt(sum(V_dir[i][k] ** 2 for i in range(d) for k in range(d)))
    V_hat = [[V_dir[i][k] / v_norm for k in range(d)] for i in range(d)]

    # Verify V_hat is in tangent space T(U_saddle): sum_k U_{ik} V_{ik} == 0 for all i
    for i in range(d):
        assert abs(sum(U_saddle[i][k] * V_hat[i][k] for k in range(d))) < 1e-15

    saddle_curv = eval_M_quadratic_form(U_saddle, psi_s, V_hat)
    assert saddle_curv < -0.5, f"Expected strict negative curvature at saddle: {saddle_curv}"

    # 2. Verify Lemma 45: at signed permutation local minimum V = I_3, tangent Hessian M(V) >= 2 I (Eq. 194-195)
    U_min = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ]
    chi_m, psi_m = tangent_grad_and_hessian_quad(U_min)
    # Any unit tangent vector at U_min = I_3 has V_{ii} = 0
    V_tan = [
        [0.0, 0.6, 0.0],
        [0.0, 0.0, 0.8],
        [0.0, 0.0, 0.0],
    ]
    min_curv = eval_M_quadratic_form(U_min, psi_m, V_tan)
    assert abs(min_curv - 2.0) < 1e-12

    # 3. Verify Algorithm 2 (Projected Noisy SGD) escapes U_saddle and converges to a signed permutation of I_3,
    # whereas noiseless GD initialized at U_saddle remains trapped forever
    U_noiseless = [row[:] for row in U_saddle]
    for _ in range(50):
        chi_nl, _ = tangent_grad_and_hessian_quad(U_noiseless)
        U_noiseless = [
            normalize([U_noiseless[i][k] - 0.1 * chi_nl[i][k] for k in range(d)])
            for i in range(d)
        ]
    obj_noiseless = cross_corr_obj(U_noiseless)
    assert abs(obj_noiseless - 0.5) < 1e-12

    rng = random.Random(20261019)
    U_noisy = [row[:] for row in U_saddle]
    for t in range(300):
        chi_cur, _ = tangent_grad_and_hessian_quad(U_noisy)
        noise_scale = 0.03 if t < 60 else 0.0
        eta = 0.12
        U_next = []
        for i in range(d):
            row = [
                U_noisy[i][k] - eta * chi_cur[i][k] + noise_scale * rng.gauss(0.0, 1.0)
                for k in range(d)
            ]
            U_next.append(normalize(row))
        U_noisy = U_next

    obj_noisy_final = cross_corr_obj(U_noisy)
    assert obj_noisy_final < 1e-12, f"Projected Noisy SGD failed to escape saddle: {obj_noisy_final}"

    summary = {
        "concept": "StrictSaddlePropertyAndNoisyStochasticGradientSaddleEscapingForOrthogonalTensorDecomposition",
        "saddle_stationary_grad_norm": chi_norm_s,
        "saddle_tangent_quadratic_curvature": round(saddle_curv, 6),
        "local_min_tangent_quadratic_curvature": round(min_curv, 6),
        "noiseless_gd_trapped_obj": round(obj_noiseless, 6),
        "noisy_psgd_escaped_final_obj": obj_noisy_final,
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
