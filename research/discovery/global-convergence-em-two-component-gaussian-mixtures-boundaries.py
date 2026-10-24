#!/usr/bin/env python3
"""Constructed boundary verification for Global Analysis of EM for Mixtures of Two Gaussians (Xu, Hsu, & Maleki 2016)."""

import json
import math
import random


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def norm2(u):
    return math.sqrt(dot(u, u))


def sub(u, v):
    return [x - y for x, y in zip(u, v)]


def add(u, v):
    return [x + y for x, y in zip(u, v)]


def scale(c, u):
    return [c * x for x in u]


def w_d(y, b):
    # w_d(y, b) = 1 / (1 + exp(-2 <y, b>)) (Section A.9, p. 40)
    z = 2.0 * dot(y, b)
    if z >= 0:
        return 1.0 / (1.0 + math.exp(-z))
    ez = math.exp(z)
    return ez / (1.0 + ez)


def build_2d_mixture_quadrature(theta_star_2d):
    # Exact symmetric 2D numerical quadrature for Y ~ 0.5 N(-theta^*, I_2) + 0.5 N(+theta^*, I_2)
    # By Lemma 7 (p. 13), all population EM iterates lie in the 2D subspace span(b^{<0>}, theta^*).
    half_pts = 25
    L = 6.0
    dx = L / half_pts
    pos_xs = [(i + 0.5) * dx for i in range(half_pts)]
    inv_sqrt2pi = 1.0 / math.sqrt(2.0 * math.pi)

    quad_points = []
    for y1 in pos_xs:
        # Marginal density of Y_1 is phi^+(y1, theta^*_1) = 0.5 (phi(y1 - theta^*_1) + phi(y1 + theta^*_1))
        wy1 = 0.5 * inv_sqrt2pi * (
            math.exp(-0.5 * ((y1 - theta_star_2d[0]) ** 2))
            + math.exp(-0.5 * ((y1 + theta_star_2d[0]) ** 2))
        ) * dx
        for y2 in pos_xs:
            wy2 = inv_sqrt2pi * math.exp(-0.5 * y2 * y2) * dx
            w = wy1 * wy2
            for s2 in (1.0, -1.0):
                # Pair (+y1, s2*y2) and (-y1, s2*y2) consecutively so reflection symmetry in y1 is exact
                quad_points.append(([y1, s2 * y2], w))
                quad_points.append(([-y1, s2 * y2], w))
    return quad_points


def pop_model1_step(quad_pts, theta):
    # Eq. (6): theta^{<t+1>} = E[(2 w_d(Y, theta^{<t>}) - 1) Y]
    out = [0.0, 0.0]
    for i in range(0, len(quad_pts), 2):
        y_pos, w = quad_pts[i]
        y_neg, _ = quad_pts[i + 1]
        c_pos = 2.0 * w_d(y_pos, theta) - 1.0
        c_neg = 2.0 * w_d(y_neg, theta) - 1.0
        out[0] += w * (c_pos * y_pos[0] + c_neg * y_neg[0])
        out[1] += w * (c_pos * y_pos[1] + c_neg * y_neg[1])
    return out


def pop_model2_reparam_step(quad_pts, a, b):
    # Eqs. (12)-(15): a^{<t+1>}, b^{<t+1>} via gamma^{<t+1>} and p^{<t+1>}
    gamma = [0.0, 0.0]
    p_val = 0.0
    for y, w in quad_pts:
        wt = w_d([y[0] - a[0], y[1] - a[1]], b)
        p_val += w * wt
        gamma[0] += w * wt * y[0]
        gamma[1] += w * wt * y[1]
    denom = 2.0 * p_val * (1.0 - p_val)
    a_next = [gamma[0] * (1.0 - 2.0 * p_val) / denom, gamma[1] * (1.0 - 2.0 * p_val) / denom]
    b_next = [gamma[0] / denom, gamma[1] / denom]
    return a_next, b_next


def main():
    theta_star = [1.5, 0.0]
    quad_pts = build_2d_mixture_quadrature(theta_star)

    # Scenario A: Model 1 Population EM global convergence vs. orthogonal hyperplane trap (Theorems 1 & 2, Corollary 1)
    # 1. Distant initialization with <theta^{<0>}, theta^*> < 0 and large orthogonal component
    theta_init_neg = [-0.20, 2.50]
    sgn0 = -1.0 if dot(theta_init_neg, theta_star) < 0 else 1.0
    target_m1 = scale(sgn0, theta_star)
    th = theta_init_neg[:]
    cos_angles = []
    for _ in range(35):
        cos_angles.append(dot(th, target_m1) / (norm2(th) * norm2(target_m1)))
        th = pop_model1_step(quad_pts, th)
    err_global_m1 = norm2(sub(th, target_m1))
    assert cos_angles[-1] > 0.9999999
    assert all(cos_angles[i + 1] >= cos_angles[i] - 1e-12 for i in range(len(cos_angles) - 1))
    assert err_global_m1 < 1e-4

    # 2. Orthogonal hyperplane initialization <theta^{<0>}, theta^*> = 0 => converges to saddle point 0 (Theorem 2, Corollary 3)
    theta_ortho = [0.0, 2.0]
    assert abs(dot(theta_ortho, theta_star)) == 0.0
    th_sad = theta_ortho[:]
    for _ in range(45):
        th_sad = pop_model1_step(quad_pts, th_sad)
        assert abs(dot(th_sad, theta_star)) == 0.0
    assert norm2(th_sad) < 0.25 * norm2(theta_ortho)

    # Scenario B: Model 2 re-parameterized Population EM (a^{<t>}, b^{<t>}) global convergence & Sample-based EM consistency (Theorems 3, 4, 5, 7)
    a_cur = [1.2, -0.9]
    b_cur = [0.25, 1.8]
    assert dot(b_cur, theta_star) > 0
    sin_betas = []
    a_norms = []
    for _ in range(65):
        cos_b = max(-1.0, min(1.0, dot(b_cur, theta_star) / (norm2(b_cur) * norm2(theta_star))))
        sin_betas.append(math.sqrt(max(0.0, 1.0 - cos_b * cos_b)))
        a_norms.append(norm2(a_cur))
        a_cur, b_cur = pop_model2_reparam_step(quad_pts, a_cur, b_cur)

    assert sin_betas[-1] < 1e-5
    assert a_norms[-1] < 1e-4
    assert norm2(sub(b_cur, theta_star)) < 1e-4

    # Verify Sample-based EM consistency from same distant initialization (Theorem 7)
    rng = random.Random(20261019)
    n_samp = 1200
    samp_pts = []
    for _ in range(n_samp):
        s_comp = 1.0 if rng.random() < 0.5 else -1.0
        samp_pts.append(([s_comp * theta_star[0] + rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0)], 1.0 / n_samp))

    a_samp = [1.2, -0.9]
    b_samp = [0.25, 1.8]
    for _ in range(45):
        a_samp, b_samp = pop_model2_reparam_step(samp_pts, a_samp, b_samp)
    samp_err_a = norm2(a_samp)
    samp_err_b = norm2(sub(b_samp, theta_star))
    assert samp_err_a < 0.12 and samp_err_b < 0.12

    summary = {
        "model1_initial_cosine_with_target": round(cos_angles[0], 5),
        "model1_final_cosine_with_target": round(cos_angles[-1], 7),
        "model1_final_param_error": round(err_global_m1, 6),
        "model1_orthogonal_init_norm": round(norm2(theta_ortho), 4),
        "model1_orthogonal_after_45_steps_norm": round(norm2(th_sad), 5),
        "model2_initial_sin_beta": round(sin_betas[0], 5),
        "model2_final_sin_beta": round(sin_betas[-1], 8),
        "model2_initial_a_norm": round(a_norms[0], 5),
        "model2_final_a_norm": round(a_norms[-1], 8),
        "sample_em_a_error": round(samp_err_a, 5),
        "sample_em_b_error": round(samp_err_b, 5),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
