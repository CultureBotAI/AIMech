#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 647:
ACProp (Asynchronous-Centering-Prop Adaptive Gradient Optimization)
Primary source: Zhuang, Ding, Tang, Dvornek, Tatikonda, & Duncan (NeurIPS 2021, arXiv:2110.05454).
"""

import math


def verify_unbiased_async_centering_expectation():
    """Verify Eq. (Algorithm 2, p. 3): E[g_t / sqrt(s_{t-1} + eps) | g_{0:t-1}] = E[g_t] / sqrt(s_{t-1} + eps)
    whereas synchronous denominator sqrt(s_t + eps) correlates with g_t and biases the step direction."""
    s_prev = 0.25
    eps = 1e-8
    beta1 = 0.9
    beta2 = 0.99
    m_prev = 0.0
    # Two equiprobable gradient realizations at step t with positive expected gradient +0.5:
    # g_t = +3.0 (prob 0.25) and g_t = -1/3 (prob 0.75) -> E[g_t] = 0.75 - 0.25 = +0.5 > 0
    outcomes = [(0.25, 3.0), (0.75, -1.0 / 3.0)]
    exp_g = sum(p * g for p, g in outcomes)
    assert abs(exp_g - 0.5) < 1e-12

    # Async-Center (ACProp) expected update direction uses s_{t-1}
    async_step = sum(p * (g / math.sqrt(s_prev + eps)) for p, g in outcomes)
    expected_unbiased = exp_g / math.sqrt(s_prev + eps)
    assert abs(async_step - expected_unbiased) < 1e-12
    assert async_step > 0.0

    # Sync-Center (AdaBelief) uses s_t = beta2 * s_{t-1} + (1 - beta2) * (g_t - m_t)^2
    sync_step = 0.0
    for p, g in outcomes:
        m_t = beta1 * m_prev + (1.0 - beta1) * g
        s_t = beta2 * s_prev + (1.0 - beta2) * ((g - m_t) ** 2)
        sync_step += p * (g / math.sqrt(s_t + eps))
    # Because large positive gradient g=3.0 inflates s_t in the denominator, sync_step is strictly smaller
    assert sync_step < async_step


def verify_reddi_periodic_counterexample_lemma_3_3():
    """Verify Lemma 3.3 / Lemma A.3 (Eqs. 12, 34, 41):
    On Reddi et al.'s periodic problem f_t(x) = P*x if t%P==1 else -x on [-1, 1] with P >= 3,
    ACProp's asymptotic periodic centered second moment S_{kP} is the minimum within each period,
    yielding strictly negative net parameter drift toward x* = -1 for any beta1, beta2 in (0, 1)."""
    P = 5
    beta1 = 0.9
    beta2 = 0.9
    # Analytical limit lim_{k->inf} m_{kP} from Eq. (12)
    m_lim_analytic = ((P + 1) * (beta1 ** (P - 1)) - P * (beta1 ** P) - 1.0) / (1.0 - (beta1 ** P))

    # Simulate recurrence for 400 periods to verify exact convergence to Eqs. (12) and (34)
    m = 0.0
    s = 0.0
    for step in range(1, 400 * P + 1):
        g = float(P) if (step % P == 1) else -1.0
        m = beta1 * m + (1.0 - beta1) * g
        s = beta2 * s + (1.0 - beta2) * ((g - m) ** 2)

    assert abs(m - m_lim_analytic) < 1e-10

    # Now trace one full period from kP+1 to kP+P and check S_i >= S_{kP} (Eq. 35)
    s_kP = s
    s_period = [s_kP]
    net_neg_update = 0.0
    for j in range(1, P + 1):
        g = float(P) if j == 1 else -1.0
        denom = math.sqrt(s + 1e-12)
        net_neg_update += g / denom
        m = beta1 * m + (1.0 - beta1) * g
        s = beta2 * s + (1.0 - beta2) * ((g - m) ** 2)
        if j < P:
            s_period.append(s)

    for s_val in s_period:
        assert s_val >= s_kP - 1e-12
    # Net negative update over period is strictly positive (>= 1 / sqrt(S_{kP} + eps)), so x moves toward -1
    assert net_neg_update >= 1.0 / math.sqrt(s_kP + 1e-12) - 1e-9
    assert net_neg_update > 0.0


def verify_sparse_gradient_centering_advantage_lemma_3_4():
    """Verify Section 3.2 / Lemma 3.4 / Lemma A.6 (Eqs. 50-75):
    On the sparse-gradient periodic problem f_t(x) = (P/2)x if t%P==1, -x if t%P==P-2, 0 otherwise,
    centered second moment keeps s^+ / s^- < v^+ / v^- because zero gradients still produce non-zero
    (0 - m_t)^2 in ACProp while v_t decays exponentially by beta2 in AdaShift."""
    P = 20
    beta1 = 0.9
    beta2 = 0.5
    m = 0.0
    v = 0.0
    s = 0.0
    for step in range(1, 400 * P + 1):
        rem = step % P
        if rem == 1:
            g = P / 2.0
            s_plus = s
            v_plus = v
        elif rem == P - 2:
            g = -1.0
            s_minus = s
            v_minus = v
        else:
            g = 0.0
        m = beta1 * m + (1.0 - beta1) * g
        v = beta2 * v + (1.0 - beta2) * (g ** 2)
        s = beta2 * s + (1.0 - beta2) * ((g - m) ** 2)

    ratio_acprop = s_plus / s_minus
    ratio_adashift = v_plus / v_minus
    assert ratio_acprop < (P ** 2) / 4.0 < ratio_adashift
    # Check early-phase regret constant advantage (Eqs. 6-7): 1/C_l^s < 1/C_l^v when |mu| > 0
    mu, sigma, eps = 2.0, 0.5, 1e-8
    inv_cl_uncentered = math.sqrt(mu ** 2 + sigma ** 2 + eps)
    inv_cl_centered = math.sqrt(sigma ** 2 + eps)
    assert inv_cl_centered < inv_cl_uncentered


if __name__ == "__main__":
    verify_unbiased_async_centering_expectation()
    verify_reddi_periodic_counterexample_lemma_3_3()
    verify_sparse_gradient_centering_advantage_lemma_3_4()
    print("[PASS] Round 647 ACProp boundary and mathematical verification succeeded.")
