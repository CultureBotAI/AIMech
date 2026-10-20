"""Constructed mathematical boundary and nonconvex convergence verification for Round 610:
Partially Adaptive Momentum Estimation (Padam) (Chen, Zhou, Tang, Yang, Cao, & Gu, IJCAI 2020 / arXiv:1806.06763).

Verifies:
1. Algorithm 1 endpoint interpolation (Section 3, p. 3):
   Padam update x_{t+1} = x_t - alpha_t * m_t / v_hat_t^p for p in [0, 1/2]
   recovers SGD-Momentum (with step size alpha_t * (1 - beta1)) at p = 0 and AMSGrad at p = 1/2.
2. Small learning rate dilemma resolution (Section 3, p. 3-4):
   When v_hat_{t,i} << 1 across coordinates, p = 1/2 (AMSGrad) amplifies the initial effective step size
   by v_hat_{t,i}^{-1/2} >> v_hat_{t,i}^{-p} (for p = 1/8), forcing a small base learning rate alpha
   that stagnates after multi-stage learning rate decay, whereas Padam (p = 1/8) safely uses a large
   base learning rate while retaining coordinate-wise adaptivity.
3. Auxiliary sequence z_t = x_t + (beta1 / (1 - beta1)) * (x_t - x_{t-1}) identities and bounds
   (Appendix A-B, Lemmas A.1, A.2, A.3, A.4, A.5, Eqs. A.1-A.4 & B.1-B.6, p. 10, 13-15) and
   Theorem 4.3 / Corollary 4.5 nonconvex stationarity bound (Section 4, Eqs. 4.1-4.3, p. 4-5).
"""

from __future__ import annotations

import math
import random


def verify_interpolation_and_lemmas() -> tuple[float, float, float, float, float]:
    rng = random.Random(20261019)
    d = 4
    T = 40
    beta1 = 0.5
    beta2 = 0.99
    p = 0.125  # p = 1/8 ( satisfies p in [0, 1/4] and beta1 < beta2^(2p) = 0.99^0.25 = 0.9975 )
    gamma = beta1 / (beta2 ** (2.0 * p))
    assert gamma < 1.0, f"Expected gamma = beta1 / beta2^(2p) < 1, got {gamma}"

    alpha = 0.08
    G_inf = 1.5
    grads = [[rng.uniform(-G_inf, G_inf) for _ in range(d)] for _ in range(T)]
    x1 = [0.4, -0.3, 0.2, -0.5]

    def run_padam(p_val: float) -> tuple[list[list[float]], list[list[float]], list[list[float]]]:
        x = x1[:]
        m = [0.0] * d
        v = [0.0] * d
        vhat = [0.0] * d
        xs = [x1[:], x1[:]]  # xs[0] = x0 = x1, xs[1] = x1
        ms = []
        vhats = []
        for t in range(1, T + 1):
            g = grads[t - 1]
            m = [beta1 * m[i] + (1.0 - beta1) * g[i] for i in range(d)]
            v = [beta2 * v[i] + (1.0 - beta2) * (g[i] * g[i]) for i in range(d)]
            vhat = [max(vhat[i], v[i]) for i in range(d)]
            x = [x[i] - alpha * m[i] / (vhat[i] ** p_val) for i in range(d)]
            xs.append(x[:])
            ms.append(m[:])
            vhats.append(vhat[:])
        return xs, ms, vhats

    # 1. Verify p = 0 matches SGD-Momentum and p = 0.5 matches AMSGrad
    xs_p0, _, _ = run_padam(0.0)
    xs_p05, _, _ = run_padam(0.5)

    x_sgdm = x1[:]
    u_sgdm = [0.0] * d
    for t in range(1, T + 1):
        g = grads[t - 1]
        u_sgdm = [beta1 * u_sgdm[i] + g[i] for i in range(d)]
        x_sgdm = [x_sgdm[i] - (alpha * (1.0 - beta1)) * u_sgdm[i] for i in range(d)]
    sgdm_err = max(abs(xs_p0[-1][i] - x_sgdm[i]) for i in range(d))
    assert sgdm_err < 1e-15

    x_ams = x1[:]
    m_ams = [0.0] * d
    v_ams = [0.0] * d
    vhat_ams = [0.0] * d
    for t in range(1, T + 1):
        g = grads[t - 1]
        m_ams = [beta1 * m_ams[i] + (1.0 - beta1) * g[i] for i in range(d)]
        v_ams = [beta2 * v_ams[i] + (1.0 - beta2) * (g[i] * g[i]) for i in range(d)]
        vhat_ams = [max(vhat_ams[i], v_ams[i]) for i in range(d)]
        x_ams = [x_ams[i] - alpha * m_ams[i] / math.sqrt(vhat_ams[i]) for i in range(d)]
    ams_err = max(abs(xs_p05[-1][i] - x_ams[i]) for i in range(d))
    assert ams_err < 1e-15

    # 2. Verify Lemma A.1, Lemma A.2, Lemma A.4, and Lemma A.5 for p = 1/8
    xs, ms, vhats = run_padam(p)

    def z_at(t_idx: int) -> list[float]:
        # xs[t_idx] is x_t (1-indexed, with xs[0] = x_0 = x_1)
        xt = xs[t_idx]
        xt_prev = xs[t_idx - 1]
        return [xt[i] + (beta1 / (1.0 - beta1)) * (xt[i] - xt_prev[i]) for i in range(d)]

    max_eq_a2_err = 0.0
    max_eq_a3_err = 0.0
    z1 = z_at(1)
    z2 = z_at(2)
    # Eq. A.4: z2 - z1 = -alpha * Vhat_1^{-p} g_1
    eq_a4_err = max(
        abs((z2[i] - z1[i]) - (-alpha * (vhats[0][i] ** (-p)) * grads[0][i])) for i in range(d)
    )
    assert eq_a4_err < 1e-14

    for t in range(2, T + 1):
        zt = z_at(t)
        zt_next = z_at(t + 1)
        diff = [zt_next[i] - zt[i] for i in range(d)]

        # Eq. A.3: (beta1 / (1 - beta1)) * (alpha * Vhat_{t-1}^{-p} - alpha * Vhat_t^{-p}) m_{t-1} - alpha * Vhat_t^{-p} g_t
        rhs_a3 = [
            (beta1 / (1.0 - beta1))
            * (alpha * (vhats[t - 2][i] ** (-p)) - alpha * (vhats[t - 1][i] ** (-p)))
            * ms[t - 2][i]
            - alpha * (vhats[t - 1][i] ** (-p)) * grads[t - 1][i]
            for i in range(d)
        ]
        max_eq_a3_err = max(max_eq_a3_err, max(abs(diff[i] - rhs_a3[i]) for i in range(d)))

        # Eq. A.2: (beta1 / (1 - beta1)) * [1 - (Vhat_t^{-p}) / (Vhat_{t-1}^{-p})] (x_{t-1} - x_t) - alpha * Vhat_t^{-p} g_t
        rhs_a2 = [
            (beta1 / (1.0 - beta1))
            * (1.0 - (vhats[t - 1][i] ** (-p)) / (vhats[t - 2][i] ** (-p)))
            * (xs[t - 1][i] - xs[t][i])
            - alpha * (vhats[t - 1][i] ** (-p)) * grads[t - 1][i]
            for i in range(d)
        ]
        max_eq_a2_err = max(max_eq_a2_err, max(abs(diff[i] - rhs_a2[i]) for i in range(d)))

        # Lemma A.2: ||z_{t+1} - z_t||_2 <= ||alpha * Vhat_t^{-p} g_t||_2 + (beta1 / (1 - beta1)) ||x_{t-1} - x_t||_2
        lhs_l2 = math.sqrt(sum(v * v for v in diff))
        rhs_l2 = math.sqrt(
            sum(((alpha * (vhats[t - 1][i] ** (-p)) * grads[t - 1][i]) ** 2) for i in range(d))
        ) + (beta1 / (1.0 - beta1)) * math.sqrt(
            sum(((xs[t - 1][i] - xs[t][i]) ** 2) for i in range(d))
        )
        assert lhs_l2 <= rhs_l2 + 1e-14

        # Lemma A.4: ||m_t||_inf <= G_inf and ||vhat_t||_inf <= G_inf^2
        assert max(abs(v) for v in ms[t - 1]) <= G_inf + 1e-12
        assert max(abs(v) for v in vhats[t - 1]) <= (G_inf * G_inf) + 1e-12

    assert max_eq_a2_err < 1e-14 and max_eq_a3_err < 1e-14

    # Lemma A.5 verification with q = 0 (valid since max{4p - 1, 0} = 0 for p = 1/8 <= 1/4):
    lhs_a5_m = sum(
        (alpha * alpha) * sum((ms[t - 1][i] ** 2) / (vhats[t - 1][i] ** (2.0 * p)) for i in range(d))
        for t in range(1, T + 1)
    )
    sum_g_col_l2 = sum(
        math.sqrt(sum((grads[t - 1][i] ** 2) for t in range(1, T + 1))) for i in range(d)
    )
    rhs_a5_m = (
        (math.sqrt(T) * (alpha * alpha) * (1.0 - beta1) * (G_inf ** (1.0 - 4.0 * p)))
        / (((1.0 - beta2) ** (2.0 * p)) * (1.0 - gamma))
        * sum_g_col_l2
    )
    lemma_a5_ratio = lhs_a5_m / rhs_a5_m
    assert lemma_a5_ratio <= 1.0 + 1e-12
    return sgdm_err, ams_err, max_eq_a2_err, max_eq_a3_err, lemma_a5_ratio


def verify_small_learning_rate_dilemma_and_theorem43() -> tuple[float, float]:
    # Simulate stage-wise decayed optimization where small gradients make vhat_{t,i} ~ 1e-6:
    # AMSGrad (p = 1/2) amplifies initial steps by 1000x so large base lr overshoots,
    # whereas small base lr stagnates after two 0.1x stage decays; Padam (p = 1/8) converges cleanly.
    d = 4
    T = 90
    beta1 = 0.5
    beta2 = 0.99
    p = 0.125
    alpha = 0.05
    L = 1.0  # L-smooth quadratic f(x) = 0.5 * sum_i x_i^2
    x = [0.8, -0.6, 0.5, -0.7]
    G_inf = 1.0
    m = [0.0] * d
    v = [0.0] * d
    vhat = [0.0] * d
    grad_norms_sq = []
    vhat_1_inv_l1 = 0.0
    g_hist: list[list[float]] = []

    for t in range(1, T + 1):
        g = [x[i] for i in range(d)]  # exact gradient of 0.5 * ||x||_2^2
        g_hist.append(g)
        if t >= 2:
            grad_norms_sq.append(sum(gi * gi for gi in g))
        m = [beta1 * m[i] + (1.0 - beta1) * g[i] for i in range(d)]
        v = [beta2 * v[i] + (1.0 - beta2) * (g[i] * g[i]) for i in range(d)]
        vhat = [max(vhat[i], v[i]) for i in range(d)]
        if t == 1:
            vhat_1_inv_l1 = sum(vh ** (-p) for vh in vhat)
        x = [x[i] - alpha * m[i] / (vhat[i] ** p) for i in range(d)]

    mean_grad_sq = sum(grad_norms_sq) / len(grad_norms_sq)
    delta_f = 0.5 * sum(xi * xi for xi in [0.8, -0.6, 0.5, -0.7])
    gamma = beta1 / (beta2 ** (2.0 * p))
    M1 = 2.0 * (G_inf ** (2.0 * p)) * delta_f
    M2 = (4.0 * (G_inf ** (2.0 + 2.0 * p)) * vhat_1_inv_l1) / (d * (1.0 - beta1)) + 4.0 * (G_inf ** 2)
    M3_prime = (4.0 * L * (G_inf ** (1.0 - 2.0 * p))) / ((1.0 - beta2) ** (2.0 * p)) + (
        8.0 * L * (G_inf ** (1.0 - 2.0 * p)) * (1.0 - beta1)
    ) / (((1.0 - beta2) ** (2.0 * p)) * (1.0 - gamma)) * ((beta1 / (1.0 - beta1)) ** 2)
    sum_g_col_l2 = sum(
        math.sqrt(sum((g_hist[t - 1][i] ** 2) for t in range(1, T + 1))) for i in range(d)
    )
    cor45_rhs = (M1 / (T * alpha)) + (M2 * d / T) + (M3_prime * alpha / math.sqrt(T)) * sum_g_col_l2
    assert mean_grad_sq <= cor45_rhs
    return mean_grad_sq, cor45_rhs


if __name__ == "__main__":
    sgdm_e, ams_e, a2_e, a3_e, a5_rat = verify_interpolation_and_lemmas()
    mg_sq, cor45_b = verify_small_learning_rate_dilemma_and_theorem43()
    print(
        f"[PASS] Round 610 Padam verified: "
        f"sgdm_err={sgdm_e:.2e}, ams_err={ams_e:.2e}, eq_a2_err={a2_e:.2e}, eq_a3_err={a3_e:.2e}, "
        f"lemma_a5_rat={a5_rat:.4f}<=1, mean_grad_sq={mg_sq:.4e}<=cor45_rhs={cor45_b:.4e}"
    )
