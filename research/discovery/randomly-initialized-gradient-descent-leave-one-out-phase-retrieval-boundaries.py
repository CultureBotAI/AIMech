#!/usr/bin/env python3
"""Boundary and regime verification for Chen, Chi, Fan, & Ma (2019)
Gradient Descent with Random Initialization: Fast Global Convergence for Nonconvex Phase Retrieval.
"""

import json
import math
import random


def main():
    # 1. Verify Population State Evolution (Equations 9a-9b) & Lemma 1 two-stage dynamics
    # Starting from tiny initial signal alpha_0 = 1 / sqrt(n log n) and beta_0 = 1.0 (n = 256)
    n = 256
    eta = 0.08
    alpha = 1.0 / math.sqrt(n * math.log(n))
    beta = 1.0
    init_ratio = alpha / beta

    min_ratio_growth = float("inf")
    t_enter_basin = None
    for t in range(1, 120):
        norm_sq = alpha * alpha + beta * beta
        alpha_next = (1.0 + 3.0 * eta * (1.0 - norm_sq)) * alpha
        beta_next = (1.0 + eta * (1.0 - 3.0 * norm_sq)) * beta
        if t <= 40:
            growth = (alpha_next / alpha) / (beta_next / beta)
            min_ratio_growth = min(min_ratio_growth, growth)
        alpha, beta = alpha_next, beta_next
        if t_enter_basin is None and abs(alpha - 1.0) <= 0.1 and beta <= 0.1:
            t_enter_basin = t

    assert min_ratio_growth > 1.0 + 0.5 * (eta ** 2)
    assert t_enter_basin is not None and t_enter_basin <= 65
    assert abs(alpha - 1.0) < 1e-4 and beta < 1e-4

    # 2. Verify Finite-Sample Leave-One-Out and Random-Sign Sequences (Algorithms 1-3, Equations 29-40d)
    rng = random.Random(20261019)
    d = 10
    m = 80
    # True signal x^\natural = e_1 = [1, 0, ..., 0]
    A = [[rng.gauss(0.0, 1.0) for _ in range(d)] for _ in range(m)]
    y = [A[i][0] ** 2 for i in range(m)]

    # Random sign flips xi_i^{sgn} in {-1, +1} on first coordinate (Eq. 33-34)
    xi_sgn = [1.0 if rng.random() < 0.5 else -1.0 for _ in range(m)]
    A_sgn = [[xi_sgn[i] * abs(A[i][0])] + A[i][1:] for i in range(m)]
    # Verify Eq. (37): (a_i^T x^\natural)^2 == (a_i^{sgn T} x^\natural)^2 == |a_{i,1}|^2
    max_meas_diff = max(abs((A_sgn[i][0] ** 2) - y[i]) for i in range(m))
    assert max_meas_diff < 1e-15

    # Theorem 3 data-scaled random initialization x^0 = sqrt((1/m) sum y_i) * u
    u_rand = [rng.gauss(0.0, 1.0) for _ in range(d)]
    if abs(u_rand[0]) < 0.15:
        u_rand[0] = 0.25
    u_norm = math.sqrt(sum(z * z for z in u_rand))
    u_unit = [z / u_norm for z in u_rand]
    scale0 = math.sqrt(sum(y) / m)
    x0 = [scale0 * z for z in u_unit]

    def grad_step(x, design_mat, y_vec, drop_idx=None, step_eta=0.05):
        g = [0.0] * d
        for i in range(m):
            if i == drop_idx:
                continue
            ai = design_mat[i]
            ip = sum(ai[j] * x[j] for j in range(d))
            coeff = ((ip * ip) - y_vec[i]) * ip / m
            for j in range(d):
                g[j] += coeff * ai[j]
        return [x[j] - step_eta * g[j] for j in range(d)]

    # Run 4 steps of original sequence x^t, leave-one-out x^{t,(0)}, random-sign x^{t,sgn}, and joint x^{t,sgn,(0)}
    xt = x0[:]
    xt_l = x0[:]
    xt_sgn = x0[:]
    xt_sgn_l = x0[:]
    for _ in range(4):
        xt = grad_step(xt, A, y, drop_idx=None)
        xt_l = grad_step(xt_l, A, y, drop_idx=0)
        xt_sgn = grad_step(xt_sgn, A_sgn, y, drop_idx=None)
        xt_sgn_l = grad_step(xt_sgn_l, A_sgn, y, drop_idx=0)

    diff_loo = math.sqrt(sum((xt[j] - xt_l[j]) ** 2 for j in range(d)))
    diff_sgn = math.sqrt(sum((xt[j] - xt_sgn[j]) ** 2 for j in range(d)))
    diff_double = math.sqrt(
        sum((xt[j] - xt_sgn[j] - xt_l[j] + xt_sgn_l[j]) ** 2 for j in range(d))
    )
    assert diff_loo < 0.05
    assert diff_loo < diff_sgn
    assert diff_double < diff_sgn

    # Continue original randomly initialized GD for 300 iterations and verify global convergence to +/- e_1
    for _ in range(300):
        xt = grad_step(xt, A, y, drop_idx=None, step_eta=0.10)

    dist_plus = math.sqrt((xt[0] - 1.0) ** 2 + sum(xt[j] ** 2 for j in range(1, d)))
    dist_minus = math.sqrt((xt[0] + 1.0) ** 2 + sum(xt[j] ** 2 for j in range(1, d)))
    final_dist = min(dist_plus, dist_minus)
    assert final_dist < 1e-6, f"Randomly initialized GD failed to converge: {final_dist}"

    # 3. Verify saddle trapping when initialized exactly on the orthogonal hyperplane alpha_0 = 0
    # under population / sign-symmetric expectation (Eq. 9a: alpha_0 = 0 => alpha_t = 0 for all t)
    A_sym = A + [[-row[0]] + row[1:] for row in A]
    y_sym = y + y
    x_saddle = [0.0] + [z / math.sqrt(3.0) for z in u_unit[1:]]
    for _ in range(20):
        g_sym = [0.0] * d
        for i in range(len(A_sym)):
            ai = A_sym[i]
            ip = sum(ai[j] * x_saddle[j] for j in range(d))
            coeff = ((ip * ip) - y_sym[i]) * ip / len(A_sym)
            for j in range(d):
                g_sym[j] += coeff * ai[j]
        x_saddle = [x_saddle[j] - 0.05 * g_sym[j] for j in range(d)]
    assert abs(x_saddle[0]) < 1e-15

    summary = {
        "concept": "RandomlyInitializedGradientDescentAndLeaveOneOutSignFlipPhaseRetrievalAnalysis",
        "init_snr_ratio": round(init_ratio, 6),
        "min_snr_growth_factor": round(min_ratio_growth, 6),
        "stage1_basin_entry_iter": t_enter_basin,
        "loo_single_diff_t4": round(diff_loo, 6),
        "sgn_flip_diff_t4": round(diff_sgn, 6),
        "loo_sign_double_diff_t4": round(diff_double, 6),
        "random_init_gd_final_dist": final_dist,
        "orthogonal_hyperplane_signal_coord": abs(x_saddle[0]),
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
