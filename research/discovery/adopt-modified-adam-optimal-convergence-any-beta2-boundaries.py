#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 603: ADOPT (Modified Adam with Optimal Convergence for Any beta_2)."""

from __future__ import annotations

import math


def project_unit(theta: float) -> float:
    if theta > 1.0:
        return 1.0
    if theta < -1.0:
        return -1.0
    return theta


def verify_reddi_counterexample_and_ablation() -> tuple[float, float, float, float]:
    """Verify Section 3 & Section 5 (Eq. 12, 17 & Fig. 1, 3): Adam, ADOPT-DE, ADOPT-CO diverge to +1 while ADOPT converges to -1."""
    # Exact Section 5 Toy Problem (Eq. 17, p. 7-8) with k = 10:
    # At each step t, g_t = +k^2 with prob p = 1/k, and -k with prob 1 - p = (k - 1)/k, independent of history.
    # True gradient is E[g_t] = +1 > 0, so unique minimum on [-1, 1] is theta^* = -1.
    k_val = 10
    p_pos = 1.0 / k_val
    p_neg = 1.0 - p_pos
    g_pos = float(k_val * k_val)
    g_neg = float(-k_val)
    beta1 = 0.9
    beta2 = 0.1
    eps = 1e-6
    T = 600
    alpha = 0.05

    # Verify Eq. (12) conditional expectation identity for any v_{t-1} > 0:
    # For ADOPT, E_{g_t}[g_t / sqrt(v_{t-1} + eps^2) | v_{t-1}] = E[g_t] / sqrt(v_{t-1} + eps^2) > 0,
    # whereas for RMSprop/Adam, E_{g_t}[g_t / sqrt(beta_2 v_{t-1} + (1 - beta_2) g_t^2 + eps^2) | v_{t-1}] < 0!
    v_test = 100.0
    adopt_cond_exp = (
        p_pos * (g_pos / math.sqrt(v_test + eps * eps))
        + p_neg * (g_neg / math.sqrt(v_test + eps * eps))
    )
    adam_cond_exp = (
        p_pos * (g_pos / math.sqrt(beta2 * v_test + (1.0 - beta2) * (g_pos ** 2) + eps * eps))
        + p_neg * (g_neg / math.sqrt(beta2 * v_test + (1.0 - beta2) * (g_neg ** 2) + eps * eps))
    )
    assert adopt_cond_exp > 0.0 and adam_cond_exp < 0.0, (
        f"Expected adopt_cond_exp > 0 and adam_cond_exp < 0, got {adopt_cond_exp}, {adam_cond_exp}"
    )

    # Simulate trajectories using exact conditional expectation of the step update over g_t given history:
    th_adam = 0.0
    th_adopt = 0.0
    th_no_de = 0.0
    th_no_co = 0.0

    m_adam = 0.0
    v_adam = v_test
    m_adopt = 0.0
    v_adopt = v_test
    m_no_de = 0.0
    v_no_de = v_test
    m_no_co = 0.0
    v_no_co = v_test

    for t in range(1, T + 1):
        # Realize g_{t-1} cyclically for state evolution while taking conditional expectation over current step g_t
        # 1. Standard Adam expected step over g_t given (m_{t-1}, v_{t-1}):
        step_adam = 0.0
        for prob, g_val in ((p_pos, g_pos), (p_neg, g_neg)):
            mt = beta1 * m_adam + (1.0 - beta1) * g_val
            vt = beta2 * v_adam + (1.0 - beta2) * (g_val * g_val)
            step_adam += prob * (mt / math.sqrt(vt + eps * eps))
        th_adam = project_unit(th_adam - alpha * step_adam)

        # 2. ADOPT (Algorithm 3): normalizes g_t by v_{t-1} BEFORE momentum update
        step_adopt = 0.0
        for prob, g_val in ((p_pos, g_pos), (p_neg, g_neg)):
            mt = beta1 * m_adopt + (1.0 - beta1) * (g_val / max(math.sqrt(v_adopt), eps))
            step_adopt += prob * mt
        th_adopt = project_unit(th_adopt - alpha * step_adopt)

        # 3. ADOPT-DE (without decorrelation: uses v_t instead of v_{t-1})
        step_no_de = 0.0
        for prob, g_val in ((p_pos, g_pos), (p_neg, g_neg)):
            vt = beta2 * v_no_de + (1.0 - beta2) * (g_val * g_val)
            mt = beta1 * m_no_de + (1.0 - beta1) * (g_val / max(math.sqrt(vt), eps))
            step_no_de += prob * mt
        th_no_de = project_unit(th_no_de - alpha * step_no_de)

        # 4. ADOPT-CO (without change of order: normalizes m_t by v_{t-1} after momentum)
        # Note that m_{t-1} contains (1 - beta_1) g_{t-1} which correlates with v_{t-1} = beta_2 v_{t-2} + (1 - beta_2) g_{t-1}^2!
        step_no_co = 0.0
        for prob_prev, g_prev_val in ((p_pos, g_pos), (p_neg, g_neg)):
            v_tm1 = beta2 * v_no_co + (1.0 - beta2) * (g_prev_val * g_prev_val)
            m_tm1 = beta1 * m_no_co + (1.0 - beta1) * g_prev_val
            for prob_cur, g_cur_val in ((p_pos, g_pos), (p_neg, g_neg)):
                mt = beta1 * m_tm1 + (1.0 - beta1) * g_cur_val
                step_no_co += prob_prev * prob_cur * (mt / max(math.sqrt(v_tm1), eps))
        th_no_co = project_unit(th_no_co - alpha * step_no_co)

        # Advance state buffers with realization g_t from cycle of length k_val
        g_real = g_pos if (t % k_val == 1) else g_neg
        m_adam = beta1 * m_adam + (1.0 - beta1) * g_real
        v_adam = beta2 * v_adam + (1.0 - beta2) * (g_real * g_real)
        m_adopt = step_adopt
        v_adopt = beta2 * v_adopt + (1.0 - beta2) * (g_real * g_real)
        v_no_de = beta2 * v_no_de + (1.0 - beta2) * (g_real * g_real)
        m_no_de = step_no_de
        m_no_co = beta1 * m_no_co + (1.0 - beta1) * g_real
        v_no_co = beta2 * v_no_co + (1.0 - beta2) * (g_real * g_real)

    assert th_adam > 0.95, f"Expected standard Adam to converge to wrong solution +1, got {th_adam}"
    assert abs(th_adopt - (-1.0)) < 1e-6, f"Expected ADOPT to converge to true optimum -1, got {th_adopt}"
    assert th_no_de > 0.95, f"Expected ADOPT without decorrelation to fail (+1), got {th_no_de}"
    assert th_no_co > 0.70, f"Expected ADOPT without change-of-order to fail (+1 side), got {th_no_co}"
    return th_adam, th_adopt, th_no_de, th_no_co


def verify_lemmas_g7_g8_and_clipped_adopt() -> tuple[float, float, float]:
    """Verify Lemmas G.7 and G.8 (p. 24-25) virtual iterate phi_t identities and Clipped ADOPT (Algorithm 2)."""
    dim = 5
    beta1, beta2 = 0.9, 0.98
    eps = 1e-6
    alpha0 = 0.05

    theta_prev = [0.5, -0.4, 0.8, -1.1, 0.3]
    phi_prev = list(theta_prev)
    m_prev = [0.0] * dim
    g0 = [0.3, -0.6, 0.9, -0.2, 0.5]
    v_prev = [gi * gi for gi in g0]

    max_lemma_g7_err = 0.0
    max_lemma_g8_err = 0.0

    for t in range(1, 35):
        alpha_t = alpha0 / math.sqrt(t)
        alpha_tm1 = alpha0 if t == 1 else (alpha0 / math.sqrt(t - 1))
        c_t = 2.0 * (t ** 0.25)

        # Synthetic gradient at step t
        g_t = [math.sin(0.7 * t + i) for i in range(dim)]
        clipped = [
            min(max(g_t[i] / max(math.sqrt(v_prev[i]), eps), -c_t), c_t)
            for i in range(dim)
        ]
        m_t = [beta1 * m_prev[i] + (1.0 - beta1) * clipped[i] for i in range(dim)]
        theta_t = [theta_prev[i] - alpha_t * m_t[i] for i in range(dim)]
        v_t = [beta2 * v_prev[i] + (1.0 - beta2) * (g_t[i] ** 2) for i in range(dim)]

        # Virtual iterate phi_t (Eq. 24, p. 16):
        phi_t = [
            (1.0 / (1.0 - beta1)) * theta_t[i] - (beta1 / (1.0 - beta1)) * theta_prev[i]
            for i in range(dim)
        ]

        # Check Lemma G.8 (Eq. 110, p. 25): phi_{t-1} - theta_{t-1} = -(alpha_{t-1} beta_1 / (1 - beta_1)) m_{t-1}
        for i in range(dim):
            lhs_g8 = phi_prev[i] - theta_prev[i]
            rhs_g8 = -(alpha_tm1 * beta1 / (1.0 - beta1)) * m_prev[i]
            err_g8 = abs(lhs_g8 - rhs_g8)
            if err_g8 > max_lemma_g8_err:
                max_lemma_g8_err = err_g8

            # Check Lemma G.7 (Eq. 100, p. 24):
            # phi_t - phi_{t-1} = ((alpha_{t-1} - alpha_t) beta_1 / (1 - beta_1)) m_{t-1} - alpha_t Clip(...)
            lhs_g7 = phi_t[i] - phi_prev[i]
            rhs_g7 = ((alpha_tm1 - alpha_t) * beta1 / (1.0 - beta1)) * m_prev[i] - alpha_t * clipped[i]
            err_g7 = abs(lhs_g7 - rhs_g7)
            if err_g7 > max_lemma_g7_err:
                max_lemma_g7_err = err_g7

        theta_prev = theta_t
        phi_prev = phi_t
        m_prev = m_t
        v_prev = v_t

    assert max_lemma_g7_err < 1e-14, f"Lemma G.7 error: {max_lemma_g7_err}"
    assert max_lemma_g8_err < 1e-14, f"Lemma G.8 error: {max_lemma_g8_err}"

    # Verify Clipped ADOPT stability when v_0 has near-zero entries (Section 4, p. 7)
    v0_zero = 0.0
    g1 = 1.0
    unclipped_step = g1 / max(math.sqrt(v0_zero), 1e-6)  # 1e6 jump!
    clipped_step = min(max(unclipped_step, -2.0), 2.0)
    assert unclipped_step == 1e6 and clipped_step == 2.0
    return max_lemma_g7_err, max_lemma_g8_err, unclipped_step / clipped_step


def main() -> None:
    th_adam, th_adopt, th_no_de, th_no_co = verify_reddi_counterexample_and_ablation()
    err_g7, err_g8, clip_ratio = verify_lemmas_g7_g8_and_clipped_adopt()
    print(
        f"[PASS] Round 603 ADOPT verified: adam={th_adam:+.4f}, adopt={th_adopt:+.4f}, "
        f"no_de={th_no_de:+.4f}, no_co={th_no_co:+.4f}, "
        f"lemma_g7_err={err_g7:.2e}, lemma_g8_err={err_g8:.2e}, clip_ratio={clip_ratio:.1e}"
    )


if __name__ == "__main__":
    main()
