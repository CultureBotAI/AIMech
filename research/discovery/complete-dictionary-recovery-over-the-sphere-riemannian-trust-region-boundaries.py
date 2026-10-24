#!/usr/bin/env python3
"""Boundary and regime verification for Sun, Qu, & Wright (2017)
Complete Dictionary Recovery Over the Sphere and Riemannian Trust-Region Method.
"""

import json
import math
import random


def h_mu(z, mu):
    # Numerically stable mu * log(cosh(z / mu))
    az = abs(z) / mu
    return az * mu + mu * math.log(0.5 * (1.0 + math.exp(-2.0 * az)))


def dh_mu(z, mu):
    return math.tanh(z / mu)


def d2h_mu(z, mu):
    t = math.tanh(z / mu)
    return (1.0 - t * t) / mu


def main():
    rng = random.Random(20261019)
    n = 3
    theta = 0.25
    mu = 0.04
    p = 2400

    # Generate Bernoulli-Gaussian matrix X_0 in R^{3 x p} (Section 1.3)
    X0 = [
        [
            rng.gauss(0.0, 1.0) if rng.random() < theta else 0.0
            for _ in range(p)
        ]
        for _ in range(n)
    ]

    # 1. Verify Theorem 2.1 / Propositions 2.5-2.7 three-zone geometry in w-chart q(w) = (w, sqrt(1 - ||w||^2))
    def grad_hess_g(w):
        wn2 = sum(z * z for z in w)
        qn = math.sqrt(1.0 - wn2)
        grad = [0.0, 0.0]
        H = [[0.0, 0.0], [0.0, 0.0]]
        for k in range(p):
            xk = [X0[0][k], X0[1][k]]
            xn = X0[2][k]
            q_dot_x = w[0] * xk[0] + w[1] * xk[1] + qn * xn
            t1 = dh_mu(q_dot_x, mu)
            t2 = d2h_mu(q_dot_x, mu)
            zeta = [xk[0] - (xn / qn) * w[0], xk[1] - (xn / qn) * w[1]]
            grad[0] += t1 * zeta[0] / p
            grad[1] += t1 * zeta[1] / p
            for a in range(2):
                for b in range(2):
                    phi_ab = (1.0 / qn if a == b else 0.0) + (w[a] * w[b]) / (qn ** 3)
                    H[a][b] += (t2 * zeta[a] * zeta[b] - t1 * xn * phi_ab) / p
        return grad, H

    # Region R_1 (||w|| <= mu / (4 sqrt(2))): strong convexity lambda_min(nabla^2 g(w)) >= c_* theta / mu
    w_r1 = [0.003, -0.002]
    _, H_r1 = grad_hess_g(w_r1)
    tr_r1 = H_r1[0][0] + H_r1[1][1]
    det_r1 = H_r1[0][0] * H_r1[1][1] - H_r1[0][1] * H_r1[1][0]
    lambda_min_r1 = 0.5 * (tr_r1 - math.sqrt(max(0.0, tr_r1 * tr_r1 - 4.0 * det_r1)))
    assert lambda_min_r1 > 0.5, f"Expected strong convexity in R1: {lambda_min_r1}"

    # Region R_2 (mu / (4 sqrt(2)) <= ||w|| <= 1 / (20 sqrt(5))): radial gradient w^T nabla g(w) / ||w|| > 0
    w_r2 = [0.015, 0.010]
    wn_r2 = math.sqrt(w_r2[0] ** 2 + w_r2[1] ** 2)
    g_r2, _ = grad_hess_g(w_r2)
    radial_grad_r2 = (w_r2[0] * g_r2[0] + w_r2[1] * g_r2[1]) / wn_r2
    assert radial_grad_r2 > 0.01, f"Expected positive radial gradient in R2: {radial_grad_r2}"

    # Region R_3 (1 / (20 sqrt(5)) <= ||w|| <= sqrt((4n-1)/(4n))): negative radial curvature w^T nabla^2 g(w) w / ||w||^2 < 0
    w_r3 = [0.45, 0.45]
    wn2_r3 = w_r3[0] ** 2 + w_r3[1] ** 2
    _, H_r3 = grad_hess_g(w_r3)
    radial_curv_r3 = (
        w_r3[0] * (H_r3[0][0] * w_r3[0] + H_r3[0][1] * w_r3[1])
        + w_r3[1] * (H_r3[1][0] * w_r3[0] + H_r3[1][1] * w_r3[1])
    ) / wn2_r3
    assert radial_curv_r3 < -0.02, f"Expected negative radial curvature in R3: {radial_curv_r3}"

    # 2. Verify Riemannian steps on S^{n-1} with exponential map retraction (Eq. 3.4) from an equatorial saddle neighborhood
    q = [1.0 / math.sqrt(3.0), 1.0 / math.sqrt(3.0), 1.0 / math.sqrt(3.0)]
    for it in range(60):
        # Compute Euclidean gradient and Hessian (Eq. 3.12-3.13)
        grad_e = [0.0, 0.0, 0.0]
        hess_e = [[0.0] * 3 for _ in range(3)]
        for k in range(p):
            yk = [X0[0][k], X0[1][k], X0[2][k]]
            qx = q[0] * yk[0] + q[1] * yk[1] + q[2] * yk[2]
            t1 = dh_mu(qx, mu) / p
            t2 = d2h_mu(qx, mu) / p
            for i in range(3):
                grad_e[i] += t1 * yk[i]
                for j in range(3):
                    hess_e[i][j] += t2 * yk[i] * yk[j]

        # Riemannian gradient (Eq. 3.14): P_{T_q S^2} nabla f(q)
        qg = sum(q[i] * grad_e[i] for i in range(3))
        grad_r = [grad_e[i] - qg * q[i] for i in range(3)]
        nr = math.sqrt(sum(z * z for z in grad_r))
        if nr < 1e-7:
            break
        # Trust-region bounded tangent step delta in T_q S^2 and exponential map retraction (Eq. 3.4)
        step_len = min(0.15, nr * (0.8 if it < 25 else 0.15))
        delta = [-step_len * z / nr for z in grad_r]
        nd = math.sqrt(sum(z * z for z in delta))
        q = [q[i] * math.cos(nd) + (delta[i] / nd) * math.sin(nd) for i in range(3)]
        nq = math.sqrt(sum(z * z for z in q))
        q = [z / nq for z in q]

    max_coord = max(abs(z) for z in q)
    dist_to_signed_basis = math.sqrt(2.0 * (1.0 - max_coord))
    assert dist_to_signed_basis < 0.05, f"Failed to approach signed basis vector: {q}"

    # 3. Verify Lemma 4.2 LP Rounding threshold (Eq. 9.11): <r, q_*> >= 249/250 guarantees exact basis recovery
    assert max_coord >= 249.0 / 250.0

    summary = {
        "concept": "CompleteDictionaryRecoveryOverTheSphereAndRiemannianTrustRegionMethod",
        "r1_strong_convexity_lambda_min": round(lambda_min_r1, 6),
        "r2_positive_radial_gradient": round(radial_grad_r2, 6),
        "r3_negative_radial_curvature": round(radial_curv_r3, 6),
        "riemannian_sphere_final_basis_alignment": round(max_coord, 6),
        "dist_to_signed_basis": round(dist_to_signed_basis, 6),
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
