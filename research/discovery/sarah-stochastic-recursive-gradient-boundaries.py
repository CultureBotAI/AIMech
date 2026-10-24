#!/usr/bin/env python3
"""Constructed boundary & regime verification for SARAH (Nguyen et al. 2017, Round 344)."""

import math
import random


def make_strongly_convex_finite_sum():
    # Construct n = 6 quadratic component functions f_i(w) = 0.5 * w^T Q_i w - b_i^T w
    # each mu-strongly convex and L-smooth with mu = 0.2, L = 1.0 (kappa = 5)
    Q = [
        [[1.0, 0.0], [0.0, 0.2]],
        [[0.2, 0.0], [0.0, 1.0]],
        [[0.6, 0.3], [0.3, 0.6]],
        [[0.6, -0.3], [-0.3, 0.6]],
        [[0.8, 0.1], [0.1, 0.4]],
        [[0.4, -0.1], [-0.1, 0.8]],
    ]
    b = [
        [1.0, -1.0],
        [-1.0, 1.0],
        [0.5, 0.5],
        [-0.5, -0.5],
        [1.5, -0.5],
        [-1.5, 0.5],
    ]
    # Note sum(b_i) = [0, 0], so w^* = [0, 0], but individual grad f_i(w^*) = -b_i != 0!
    return Q, b, 0.2, 1.0


def grad_fi(Q, b, i, w):
    q = Q[i]
    bi = b[i]
    return [
        q[0][0] * w[0] + q[0][1] * w[1] - bi[0],
        q[1][0] * w[0] + q[1][1] * w[1] - bi[1],
    ]


def grad_P(Q, b, w):
    n = len(Q)
    g0, g1 = 0.0, 0.0
    for i in range(n):
        gi = grad_fi(Q, b, i, w)
        g0 += gi[0] / n
        g1 += gi[1] / n
    return [g0, g1]


def norm_sq(v):
    return v[0] * v[0] + v[1] * v[1]


def main():
    Q, b, mu, L = make_strongly_convex_finite_sum()
    n = len(Q)
    eta = 0.4  # satisfies eta <= 2 / (mu + L) = 2 / 1.2 = 1.667 and eta < 1/L = 1.0

    # Claim 1: Verify SARAH conditional bias (Eq. 5) and exact Lemma 2 variance identity by exact enumeration over all n^2 paths for t = 2
    w0 = [2.0, -1.5]
    v0 = grad_P(Q, b, w0)
    w1 = [w0[0] - eta * v0[0], w0[1] - eta * v0[1]]
    gp_w1 = grad_P(Q, b, w1)

    # Check Eq. (5) at t = 1: E[v_1 | F_1] == grad P(w_1) - grad P(w_0) + v_0 == grad P(w_1) (at t=1 since v_0 = grad P(w_0)),
    # and at t = 2: E[v_2 | F_2] = grad P(w_2) - grad P(w_1) + v_1 != grad P(w_2)
    i1_test = 0
    g1_w1 = grad_fi(Q, b, i1_test, w1)
    g1_w0 = grad_fi(Q, b, i1_test, w0)
    v1_test = [g1_w1[0] - g1_w0[0] + v0[0], g1_w1[1] - g1_w0[1] + v0[1]]
    w2_test = [w1[0] - eta * v1_test[0], w1[1] - eta * v1_test[1]]
    gp_w2_test = grad_P(Q, b, w2_test)
    cond_exp_v2 = [0.0, 0.0]
    for i2 in range(n):
        g2_w2 = grad_fi(Q, b, i2, w2_test)
        g2_w1 = grad_fi(Q, b, i2, w1)
        v2 = [g2_w2[0] - g2_w1[0] + v1_test[0], g2_w2[1] - g2_w1[1] + v1_test[1]]
        cond_exp_v2[0] += v2[0] / n
        cond_exp_v2[1] += v2[1] / n
    rhs_eq5 = [gp_w2_test[0] - gp_w1[0] + v1_test[0], gp_w2_test[1] - gp_w1[1] + v1_test[1]]
    assert norm_sq([cond_exp_v2[0] - rhs_eq5[0], cond_exp_v2[1] - rhs_eq5[1]]) < 1e-24
    # Conditional bias is strictly non-zero: E[v_2 | F_2] != grad P(w_2)
    bias_sq = norm_sq([cond_exp_v2[0] - gp_w2_test[0], cond_exp_v2[1] - gp_w2_test[1]])
    assert bias_sq > 1e-4

    # Exact enumeration over all n^2 paths (i1, i2) for Lemma 2 identity at t = 2:
    # E[||grad P(w_2) - v_2||^2] == sum_{j=1}^2 E[||v_j - v_{j-1}||^2] - sum_{j=1}^2 E[||grad P(w_j) - grad P(w_{j-1})||^2]
    lhs_lemma2 = 0.0
    rhs_lemma2 = 0.0
    total_v2 = [0.0, 0.0]
    total_gp2 = [0.0, 0.0]
    for i1 in range(n):
        gi1_w1 = grad_fi(Q, b, i1, w1)
        gi1_w0 = grad_fi(Q, b, i1, w0)
        v1 = [gi1_w1[0] - gi1_w0[0] + v0[0], gi1_w1[1] - gi1_w0[1] + v0[1]]
        w2 = [w1[0] - eta * v1[0], w1[1] - eta * v1[1]]
        gp_w2 = grad_P(Q, b, w2)
        dv1_sq = norm_sq([v1[0] - v0[0], v1[1] - v0[1]])
        dgp1_sq = norm_sq([gp_w1[0] - v0[0], gp_w1[1] - v0[1]])
        for i2 in range(n):
            gi2_w2 = grad_fi(Q, b, i2, w2)
            gi2_w1 = grad_fi(Q, b, i2, w1)
            v2 = [gi2_w2[0] - gi2_w1[0] + v1[0], gi2_w2[1] - gi2_w1[1] + v1[1]]
            dv2_sq = norm_sq([v2[0] - v1[0], v2[1] - v1[1]])
            dgp2_sq = norm_sq([gp_w2[0] - gp_w1[0], gp_w2[1] - gp_w1[1]])
            prob = 1.0 / (n * n)
            lhs_lemma2 += prob * norm_sq([gp_w2[0] - v2[0], gp_w2[1] - v2[1]])
            rhs_lemma2 += prob * ((dv1_sq + dv2_sq) - (dgp1_sq + dgp2_sq))
            total_v2[0] += prob * v2[0]
            total_v2[1] += prob * v2[1]
            total_gp2[0] += prob * gp_w2[0]
            total_gp2[1] += prob * gp_w2[1]

    assert abs(lhs_lemma2 - rhs_lemma2) < 1e-12, f"Lemma 2 mismatch: {lhs_lemma2} vs {rhs_lemma2}"
    # Unconditional total expectation E[v_2] == E[grad P(w_2)]
    assert norm_sq([total_v2[0] - total_gp2[0], total_v2[1] - total_gp2[1]]) < 1e-24

    # Claim 2: Single inner-loop linear convergence of SARAH E[||v_t||^2] -> 0 (Theorem 1b) vs SVRG non-vanishing step variance
    rng = random.Random(344)
    w_sarah = w0[:]
    v_sarah = v0[:]
    w_svrg = w0[:]
    eta_inner = 0.2
    for _ in range(80):
        idx = rng.randrange(n)
        w_next = [w_sarah[0] - eta_inner * v_sarah[0], w_sarah[1] - eta_inner * v_sarah[1]]
        g_next = grad_fi(Q, b, idx, w_next)
        g_curr = grad_fi(Q, b, idx, w_sarah)
        v_sarah = [g_next[0] - g_curr[0] + v_sarah[0], g_next[1] - g_curr[1] + v_sarah[1]]
        w_sarah = w_next

        g_svrg_curr = grad_fi(Q, b, idx, w_svrg)
        g_svrg_0 = grad_fi(Q, b, idx, w0)
        v_svrg = [g_svrg_curr[0] - g_svrg_0[0] + v0[0], g_svrg_curr[1] - g_svrg_0[1] + v0[1]]
        w_svrg = [w_svrg[0] - eta_inner * v_svrg[0], w_svrg[1] - eta_inner * v_svrg[1]]

    sarah_vt_norm = norm_sq(v_sarah)
    svrg_vt_norm = norm_sq(v_svrg)
    assert sarah_vt_norm < 1e-6 and svrg_vt_norm > 0.1, (
        f"Expected SARAH inner step norm -> 0 ({sarah_vt_norm}) while SVRG inner step norm stays O(1) ({svrg_vt_norm})"
    )

    # Also verify Remark 1 outer-loop contraction factor inequality: sigma_m < alpha_m for eta < 1/(4L)
    eta_comp = 0.2 / L
    m_comp = 20
    sigma_m = 1.0 / (mu * eta_comp * (m_comp + 1)) + (eta_comp * L) / (2.0 - eta_comp * L)
    alpha_m = 1.0 / (mu * eta_comp * (1.0 - 2.0 * L * eta_comp) * m_comp) + (2.0 * eta_comp * L) / (1.0 - 2.0 * eta_comp * L)
    assert sigma_m < alpha_m

    # Claim 3: SARAH+ adaptive inner loop stopping ||v_{t-1}||^2 > gamma ||v_0||^2
    # Verify gamma = 1 stops after t = 1 step (steepest descent), whereas gamma = 1/8 takes multiple inner steps and achieves much faster per-pass reduction
    def run_sarah_plus(gamma: float, outer_loops: int = 6):
        rng_p = random.Random(99)
        w_tilde = w0[:]
        grad_evals = 0
        for _ in range(outer_loops):
            v = grad_P(Q, b, w_tilde)
            grad_evals += n
            v0_sq = norm_sq(v)
            w = [w_tilde[0] - eta * v[0], w_tilde[1] - eta * v[1]]
            t = 1
            while norm_sq(v) > gamma * v0_sq and t < 30:
                idx = rng_p.randrange(n)
                g_w = grad_fi(Q, b, idx, w)
                g_prev = grad_fi(Q, b, idx, [w[0] + eta * v[0], w[1] + eta * v[1]])
                v = [g_w[0] - g_prev[0] + v[0], g_w[1] - g_prev[1] + v[1]]
                w = [w[0] - eta * v[0], w[1] - eta * v[1]]
                grad_evals += 2
                t += 1
            w_tilde = w[:]
        return norm_sq(grad_P(Q, b, w_tilde)), grad_evals

    err_g1, _ = run_sarah_plus(gamma=1.0, outer_loops=6)
    err_g8, _ = run_sarah_plus(gamma=0.125, outer_loops=6)
    assert err_g8 < err_g1 * 1e-4

    print(
        f"[PASS] SARAH boundaries verified: Lemma2_var={lhs_lemma2:.6f}=={rhs_lemma2:.6f}, "
        f"inner_v_sarah={sarah_vt_norm:.2e} vs inner_v_svrg={svrg_vt_norm:.3f}, "
        f"sigma_m={sigma_m:.3f}<alpha_m={alpha_m:.3f}, SARAH+_g8={err_g8:.2e}<<g1={err_g1:.2e}"
    )


if __name__ == "__main__":
    main()
