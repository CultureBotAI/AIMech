#!/usr/bin/env python3
"""Constructed boundary & regime verification for Round 290:
AIMech:WirtingerFlowPhaseRetrievalAndSpectralInitialization
Primary source: Emmanuel J. Candes, Xiaodong Li, and Mahdi Soltanolkotabi (2015),
Phase Retrieval via Wirtinger Flow: Theory and Algorithms, IEEE Transactions on
Information Theory 61(4):1985-2007 (DOI:10.1109/TIT.2015.2399924, arXiv:1407.1065v3).
"""

import json
import math
import random


def verify_admissible_cdp_moments():
    """Verify Section 4.1 (Equations 4.2-4.4, p. 9):
    Octanary pattern d = b_1 b_2 and ternary pattern satisfy
    E[d] = 0, E[d^2] = 0, and E[|d|^4] = 2 (E[|d|^2])^2.
    """
    # Octanary pattern: b1 in {+1, -1, -i, +i} w.p. 1/4 each;
    # b2 = sqrt(2)/2 w.p. 4/5, sqrt(3) w.p. 1/5
    b1_vals = [(1.0, 0.0), (-1.0, 0.0), (0.0, -1.0), (0.0, 1.0)]
    b2_vals = [(math.sqrt(2.0) / 2.0, 0.8), (math.sqrt(3.0), 0.2)]

    e_d_re, e_d_im = 0.0, 0.0
    e_d2_re, e_d2_im = 0.0, 0.0
    e_abs2 = 0.0
    e_abs4 = 0.0
    for r1, i1 in b1_vals:
        for val2, p2 in b2_vals:
            prob = 0.25 * p2
            dr, di = r1 * val2, i1 * val2
            e_d_re += prob * dr
            e_d_im += prob * di
            # d^2 = (dr^2 - di^2) + i (2 dr di)
            e_d2_re += prob * (dr * dr - di * di)
            e_d2_im += prob * (2.0 * dr * di)
            mag2 = dr * dr + di * di
            e_abs2 += prob * mag2
            e_abs4 += prob * (mag2 * mag2)

    assert abs(e_d_re) < 1e-15 and abs(e_d_im) < 1e-15
    assert abs(e_d2_re) < 1e-15 and abs(e_d2_im) < 1e-15
    assert abs(e_abs2 - 1.0) < 1e-15
    assert abs(e_abs4 - 2.0 * (e_abs2 ** 2)) < 1e-15

    # Ternary pattern (Eq. 4.4): +1 w.p. 1/4, 0 w.p. 1/2, -1 w.p. 1/4
    tern_abs2 = 0.25 * 1.0 + 0.5 * 0.0 + 0.25 * 1.0
    tern_abs4 = 0.25 * 1.0 + 0.5 * 0.0 + 0.25 * 1.0
    assert abs(tern_abs4 - 2.0 * (tern_abs2 ** 2)) < 1e-15
    return {
        "octanary_E_abs_d2": round(e_abs2, 12),
        "octanary_E_abs_d4": round(e_abs4, 12),
        "octanary_2_E_abs_d2_sq": round(2.0 * (e_abs2 ** 2), 12),
        "ternary_E_abs_d2": round(tern_abs2, 12),
        "ternary_E_abs_d4": round(tern_abs4, 12),
    }


def verify_population_regularity_condition():
    """Verify Lemma 7.2 & Section 7.9 Equations (7.33)-(7.36) (p. 30-31):
    For ||x|| = 1 and z = x + h with Im(x^* h) = 0 and ||h|| <= 1/8,
    nabla F(z) = (I - x x^*) z + 2 (||z||^2 - 1) z satisfies
    ||nabla F(z)|| <= 5 ||h|| and Re<nabla F(z), h> >= (1/8) ||h||^2 + (1/200) ||nabla F(z)||^2.
    """
    rng = random.Random(20261019)
    n = 10
    x = [1.0] + [0.0] * (n - 1)
    min_margin = float("inf")
    max_grad_ratio = 0.0
    for _ in range(200):
        raw_h = [rng.gauss(0.0, 1.0) for _ in range(n)]
        norm_raw = math.sqrt(sum(v * v for v in raw_h))
        radius = rng.uniform(1e-4, 0.125)
        h = [v * radius / norm_raw for v in raw_h]
        z = [x[i] + h[i] for i in range(n)]
        norm_z2 = sum(v * v for v in z)
        xz = sum(x[i] * z[i] for i in range(n))
        # nabla F(z) = (I - x x^*) z + 2(||z||^2 - 1) z
        grad_F = [(z[i] - xz * x[i]) + 2.0 * (norm_z2 - 1.0) * z[i] for i in range(n)]
        norm_grad2 = sum(g * g for g in grad_F)
        norm_h2 = sum(v * v for v in h)
        inner_gh = sum(grad_F[i] * h[i] for i in range(n))

        ratio = math.sqrt(norm_grad2 / norm_h2)
        max_grad_ratio = max(max_grad_ratio, ratio)
        assert ratio <= 5.0 + 1e-12

        rhs_rc = 0.125 * norm_h2 + (1.0 / 200.0) * norm_grad2
        margin = (inner_gh - rhs_rc) / norm_h2
        min_margin = min(min_margin, margin)
        assert inner_gh >= rhs_rc - 1e-15

    return {
        "max_grad_to_h_ratio_bound_5": round(max_grad_ratio, 6),
        "min_rc_normalized_margin": round(min_margin, 6),
        "alpha_prime": 8,
        "beta_prime": 200,
    }


def simulate_wirtinger_flow_recovery():
    """Verify Algorithm 1 Spectral Initialization & Wirtinger Flow geometric convergence (Eq. 2.2, Theorem 3.3)."""
    rng = random.Random(20261019)
    n = 12
    m = 144
    raw_x = [rng.gauss(0.0, 1.0) for _ in range(n)]
    norm_x = math.sqrt(sum(v * v for v in raw_x))
    x = [v / norm_x for v in raw_x]

    A = [[rng.gauss(0.0, 1.0) for _ in range(n)] for _ in range(m)]
    y = [sum(A[r][j] * x[j] for j in range(n)) ** 2 for r in range(m)]

    # Algorithm 1: Spectral Initialization (p. 4)
    # lambda^2 = n * sum_r y_r / sum_r ||a_r||^2
    sum_y = sum(y)
    sum_a2 = sum(sum(val * val for val in row) for row in A)
    lam_init = math.sqrt(n * sum_y / sum_a2)

    # Power method (Algorithm 3, p. 42) on Y = (1/m) sum_r y_r a_r a_r^T
    v = [rng.gauss(0.0, 1.0) for _ in range(n)]
    v_norm = math.sqrt(sum(val * val for val in v))
    v = [val / v_norm for val in v]
    for _ in range(60):
         Yv = [0.0] * n
         for r in range(m):
             ar_v = sum(A[r][j] * v[j] for j in range(n))
             coeff = (y[r] * ar_v) / m
             for j in range(n):
                 Yv[j] += coeff * A[r][j]
         yv_norm = math.sqrt(sum(val * val for val in Yv))
         v = [val / yv_norm for val in Yv]

    z = [lam_init * val for val in v]
    norm_z0_sq = sum(val * val for val in z)

    def dist_to_x(vec):
        d_plus = math.sqrt(sum((vec[j] - x[j]) ** 2 for j in range(n)))
        d_minus = math.sqrt(sum((vec[j] + x[j]) ** 2 for j in range(n)))
        return min(d_plus, d_minus)

    init_dist = dist_to_x(z)

    # Wirtinger Flow updates (Eq. 2.2 & Eq. 2.5):
    # z_{tau+1} = z_tau - (mu_{tau+1} / ||z_0||^2) * (1/m) sum_r (|a_r^* z|^2 - y_r) (a_r a_r^*) z
    tau0 = 50.0
    mu_max = 0.25
    err_history = [round(init_dist, 6)]
    for tau in range(1, 201):
        mu_tau = min(1.0 - math.exp(-tau / tau0), mu_max)
        grad = [0.0] * n
        for r in range(m):
            ar_z = sum(A[r][j] * z[j] for j in range(n))
            resid = (ar_z * ar_z - y[r]) * ar_z / m
            for j in range(n):
                grad[j] += resid * A[r][j]
        step = mu_tau / norm_z0_sq
        for j in range(n):
            z[j] -= step * grad[j]
        if tau in (50, 100, 150, 200):
            err_history.append(round(dist_to_x(z), 12))

    final_dist = dist_to_x(z)
    assert init_dist < 0.50
    assert final_dist < 1e-9
    return {
        "n": n,
        "m": m,
        "lambda_init": round(lam_init, 6),
        "init_dist": round(init_dist, 6),
        "err_trajectory_0_50_100_150_200": err_history,
        "final_dist": final_dist,
    }


def main():
    cdp = verify_admissible_cdp_moments()
    rc = verify_population_regularity_condition()
    wf = simulate_wirtinger_flow_recovery()
    out = {
        "admissible_cdp_moments": cdp,
        "population_regularity_condition": rc,
        "wirtinger_flow_simulation": wf,
        "all_assertions_passed": True,
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
