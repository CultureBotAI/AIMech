#!/usr/bin/env python3
"""Constructed boundary verification for Orthogonal Tensor Decompositions and Robust Tensor Power Method (Anandkumar et al. 2014)."""

import json
import math
import random


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def norm2(u):
    return math.sqrt(dot(u, u))


def normalize(u):
    n = norm2(u)
    return [x / n for x in u]


def sub(u, v):
    return [x - y for x, y in zip(u, v)]


def scale(c, u):
    return [c * x for x in u]


def tensor_eval_vec(T, u):
    # T(I, u, u)_i = sum_{j,l} T_{i,j,l} u_j u_l (Eq. 5)
    k = len(u)
    out = [0.0] * k
    for i in range(k):
        s = 0.0
        for j in range(k):
            uj = u[j]
            for l in range(k):
                s += T[i][j][l] * uj * u[l]
        out[i] = s
    return out


def tensor_eval_scalar(T, u):
    # T(u, u, u) = u^T T(I, u, u)
    return dot(u, tensor_eval_vec(T, u))


def add_rank1_tensor(T, coeff, v):
    k = len(v)
    for i in range(k):
        for j in range(k):
            for l in range(k):
                T[i][j][l] += coeff * v[i] * v[j] * v[l]


def main():
    rng = random.Random(20261019)
    k = 3
    lambdas = [3.0, 2.0, 1.5]
    # Orthonormal basis in R^3
    v1 = [1.0, 0.0, 0.0]
    v2 = [0.0, 3.0 / 5.0, 4.0 / 5.0]
    v3 = [0.0, -4.0 / 5.0, 3.0 / 5.0]
    vs = [v1, v2, v3]

    T = [[[0.0] * k for _ in range(k)] for _ in range(k)]
    for lam, v in zip(lambdas, vs):
        add_rank1_tensor(T, lam, v)

    # Scenario A: Robust eigenvectors vs. spurious eigenvectors & quadratic convergence (Theorems 4.1 & 4.2, Lemma 5.1)
    # 1. Verify v_1 is a robust eigenvector with quadratic convergence (Lemma 5.1)
    theta0 = normalize([0.75 * v1[j] + 0.55 * v2[j] + 0.35 * v3[j] for j in range(k)])
    c1 = abs(lambdas[0] * dot(v1, theta0))
    c2 = abs(lambdas[1] * dot(v2, theta0))
    ratio0 = c2 / c1
    assert ratio0 < 1.0
    prefactor = 2.0 * (lambdas[0] ** 2) * sum(1.0 / (lam ** 2) for lam in lambdas[1:])

    th = theta0[:]
    for t in range(1, 8):
        th = normalize(tensor_eval_vec(T, th))
        err_sq = norm2(sub(v1, th)) ** 2
        bound_sq = prefactor * (ratio0 ** (2 ** (t + 1)))
        assert err_sq <= bound_sq + 1e-15
    assert norm2(sub(v1, th)) < 1e-12

    # 2. Verify spurious eigenvector u_spur propto (1/lambda_1) v_1 + (1/lambda_2) v_2 (Section 4.2.1, p. 2790)
    raw_spur = [v1[j] / lambdas[0] + v2[j] / lambdas[1] for j in range(k)]
    u_spur = normalize(raw_spur)
    t_spur = tensor_eval_vec(T, u_spur)
    lam_spur = dot(u_spur, t_spur)
    # Check stationary point equation T(I, u_spur, u_spur) = lam_spur * u_spur
    eig_resid_spur = norm2(sub(t_spur, scale(lam_spur, u_spur)))
    assert eig_resid_spur < 1e-15

    # Verify u_spur is NOT a local maximizer (Theorem 4.2 Case 2, p. 2802):
    # Along tangent direction w orthogonal to u_spur in span(v1, v2), Hessian quadratic form is +3 * lam_spur > 0
    w_tan = normalize([v1[j] / lambdas[1] - v2[j] / lambdas[0] for j in range(k)])
    assert abs(dot(u_spur, w_tan)) < 1e-15
    hess_quad_spur = 3.0 * lam_spur * (2.0 * (dot(v1, w_tan) ** 2 + dot(v2, w_tan) ** 2) - 1.0)
    assert abs(hess_quad_spur - 3.0 * lam_spur) < 1e-14 and hess_quad_spur > 0.0

    # Perturbing u_spur slightly escapes to v_1 or v_2 under power iteration (Theorem 4.1)
    th_escape = normalize([u_spur[j] + 0.02 * w_tan[j] for j in range(k)])
    for _ in range(12):
        th_escape = normalize(tensor_eval_vec(T, th_escape))
    dist_to_true = min(norm2(sub(th_escape, v)) for v in vs)
    assert dist_to_true < 1e-10

    # Scenario B: Robust Tensor Power Method with Deflation under Perturbation (Algorithm 1, Theorem 5.1, Lemma B.5)
    eps_pert = 0.015
    T_pert = [[[T[i][j][l] for l in range(k)] for j in range(k)] for i in range(k)]
    for i in range(k):
        for j in range(i, k):
            for l in range(j, k):
                val = eps_pert * rng.uniform(-0.35, 0.35)
                for pi, pj, pl in {(i, j, l), (i, l, j), (j, i, l), (j, l, i), (l, i, j), (l, j, i)}:
                    T_pert[pi][pj][pl] += val

    T_work = [[[T_pert[i][j][l] for l in range(k)] for j in range(k)] for i in range(k)]
    L_restarts = 24
    N_iters = 12
    recovered = []
    for _ in range(k):
        candidates = []
        for _ in range(L_restarts):
            th_r = normalize([rng.gauss(0.0, 1.0) for _ in range(k)])
            for _ in range(N_iters):
                th_r = normalize(tensor_eval_vec(T_work, th_r))
            candidates.append((tensor_eval_scalar(T_work, th_r), th_r))
        _, best_th = max(candidates, key=lambda x: x[0])
        for _ in range(N_iters):
            best_th = normalize(tensor_eval_vec(T_work, best_th))
        lam_hat = tensor_eval_scalar(T_work, best_th)
        recovered.append((lam_hat, best_th))
        add_rank1_tensor(T_work, -lam_hat, best_th)

    max_vec_err = 0.0
    max_val_err = 0.0
    for lam_true, v_true in zip(lambdas, vs):
        best_match = min(recovered, key=lambda pair: norm2(sub(pair[1], v_true)))
        v_err = norm2(sub(best_match[1], v_true))
        l_err = abs(best_match[0] - lam_true)
        assert v_err <= 8.0 * eps_pert / lam_true
        assert l_err <= 5.0 * eps_pert
        max_vec_err = max(max_vec_err, v_err)
        max_val_err = max(max_val_err, l_err)

    summary = {
        "quadratic_convergence_step5_err": norm2(sub(v1, th)),
        "spurious_eigenvector_stationarity_resid": eig_resid_spur,
        "spurious_eigenvector_tangent_hessian": round(hess_quad_spur, 5),
        "escaped_spurious_dist_to_true_basis": dist_to_true,
        "perturbation_scale_eps": eps_pert,
        "robust_power_max_eigenvector_err": round(max_vec_err, 5),
        "robust_power_max_eigenvalue_err": round(max_val_err, 5),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
