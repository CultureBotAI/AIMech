"""Constructed mathematical boundary and momental step-size smoothing verification for Round 613:
AdaMod (Ding, Ren, Luo, & Sun, 2019, arXiv:1910.12249).

Verifies:
1. Algorithm 2 & Eqs. 1-3 (Methods Section, p. 3):
   - Unrolled exponentially weighted moving average identity (Eq. 2):
     s_t = beta3 * s_{t-1} + (1 - beta3) * eta_t = (1 - beta3) * sum_{k=0}^{t-1} beta3^k * eta_{t-k}
     with s_0 = 0 (no bias correction), and clipped step size eta_hat_t = min(eta_t, s_t).
   - Exact reduction to vanilla Adam as beta3 -> 0 (Methods Section, p. 3).
2. Intrinsic early-stage warmup and extreme learning-rate spike suppression (Introduction & Methods,
   Figures 1 & 3, p. 1-5):
   - In early iterations when v_hat_t is tiny (e.g., 1e-14 on un-warmed-up Transformer layers),
     Adam's raw step size eta_t = alpha_t / (sqrt(v_hat_t) + eps) soars above 10^4, causing oscillation
     and divergence; AdaMod with beta3 in {0.999, 0.9999} bounds eta_hat_1 = (1 - beta3) * eta_1
     and caps any single-step spike by s_t = beta3 * s_{t-1} + (1 - beta3) * eta_t, reducing the
     effective spike by a factor of (1 - beta3) = 10^{-3} to 10^{-4}.
3. Stationary variance reduction of smoothed step size s_t:
   - For independent step-size fluctuations eta_t with variance sigma^2,
     lim_{t->inf} Var(s_t) = ((1 - beta3) / (1 + beta3)) * sigma^2.
"""

from __future__ import annotations

import math
import random


def verify_adamod_identities_and_spike_suppression() -> tuple[float, float, float, float, float]:
    rng = random.Random(20261019)
    T = 40
    beta1 = 0.9
    beta2 = 0.98
    beta3 = 0.999
    alpha = 0.001
    eps = 1e-9

    grads = [rng.uniform(-1.2, 1.2) for _ in range(T)]

    # 1. Verify Eq. 2 unrolled recursion and beta3 = 0 exact equivalence to Adam
    def run_adamod(b3: float, g_seq: list[float]) -> tuple[list[float], list[float], list[float]]:
        theta = 1.25
        m = 0.0
        v = 0.0
        s = 0.0
        thetas = []
        etas = []
        eta_hats = []
        for t, g in enumerate(g_seq, start=1):
            m = beta1 * m + (1.0 - beta1) * g
            v = beta2 * v + (1.0 - beta2) * (g * g)
            m_hat = m / (1.0 - (beta1 ** t))
            v_hat = v / (1.0 - (beta2 ** t))
            eta_t = alpha / (math.sqrt(v_hat) + eps)
            s = b3 * s + (1.0 - b3) * eta_t
            eta_hat_t = min(eta_t, s)
            theta = theta - eta_hat_t * m_hat
            thetas.append(theta)
            etas.append(eta_t)
            eta_hats.append(eta_hat_t)
        return thetas, etas, eta_hats

    thetas_b3_0, etas_0, _ = run_adamod(0.0, grads)
    # Direct Adam
    theta_adam = 1.25
    m_ad = 0.0
    v_ad = 0.0
    adam_thetas = []
    for t, g in enumerate(grads, start=1):
        m_ad = beta1 * m_ad + (1.0 - beta1) * g
        v_ad = beta2 * v_ad + (1.0 - beta2) * (g * g)
        m_hat = m_ad / (1.0 - (beta1 ** t))
        v_hat = v_ad / (1.0 - (beta2 ** t))
        eta_t = alpha / (math.sqrt(v_hat) + eps)
        theta_adam = theta_adam - eta_t * m_hat
        adam_thetas.append(theta_adam)

    adam_equiv_err = max(abs(a - b) for a, b in zip(thetas_b3_0, adam_thetas))
    assert adam_equiv_err < 1e-15

    # Verify unrolled s_t identity: s_t = (1 - beta3) * sum_{k=0}^{t-1} beta3^k * eta_{t-k}
    _, etas, eta_hats = run_adamod(beta3, grads)
    s_rec = 0.0
    max_unrolled_err = 0.0
    for t in range(1, T + 1):
        s_rec = beta3 * s_rec + (1.0 - beta3) * etas[t - 1]
        s_unrolled = (1.0 - beta3) * sum((beta3 ** k) * etas[t - 1 - k] for k in range(t))
        max_unrolled_err = max(max_unrolled_err, abs(s_rec - s_unrolled))
        assert eta_hats[t - 1] <= etas[t - 1] and eta_hats[t - 1] <= s_rec + 1e-16
    assert max_unrolled_err < 1e-15

    # 2. Early-stage extreme learning rate spike and intrinsic warmup scenario (Figure 1b & 3, p. 2, 4):
    # At t = 1, a vanishing stochastic gradient g_1 = -1e-8 (wrong sign from mini-batch noise) causes Adam's
    # raw learning rate eta_1 = alpha / (sqrt(v_hat_1) + eps) to spike above 1e5 and take a full un-warmed-up
    # step in the wrong direction, followed by large oscillatory steps under alpha_high = 0.8 on f(theta) = 0.5*(theta - 0.5)^2.
    # AdaMod (beta3 = 0.999) bounds eta_hat_1 = (1 - beta3)*eta_1 = 1e-3 * eta_1 and smoothly warms up s_t.
    theta_ad_spike = 2.0
    theta_am_spike = 2.0
    m_a, v_a = 0.0, 0.0
    m_m, v_m, s_m = 0.0, 0.0, 0.0
    alpha_high = 0.8

    eta_1_adam = 0.0
    eta_1_adamod = 0.0

    for t in range(1, 151):
        g_a = -1e-8 if t == 1 else (theta_ad_spike - 0.5)
        m_a = beta1 * m_a + (1.0 - beta1) * g_a
        v_a = beta2 * v_a + (1.0 - beta2) * (g_a * g_a)
        mh_a = m_a / (1.0 - (beta1 ** t))
        vh_a = v_a / (1.0 - (beta2 ** t))
        eta_a = alpha_high / (math.sqrt(vh_a) + eps)
        if t == 1:
            eta_1_adam = eta_a
        theta_ad_spike -= eta_a * mh_a

        g_m = -1e-8 if t == 1 else (theta_am_spike - 0.5)
        m_m = beta1 * m_m + (1.0 - beta1) * g_m
        v_m = beta2 * v_m + (1.0 - beta2) * (g_m * g_m)
        mh_m = m_m / (1.0 - (beta1 ** t))
        vh_m = v_m / (1.0 - (beta2 ** t))
        eta_m = alpha_high / (math.sqrt(vh_m) + eps)
        s_m = 0.999 * s_m + 0.001 * eta_m
        eta_hat_m = min(eta_m, s_m)
        if t == 1:
            eta_1_adamod = eta_hat_m
        theta_am_spike -= eta_hat_m * mh_m

    assert eta_1_adam > 1e6 and abs(eta_1_adamod / eta_1_adam - (1.0 - beta3)) < 1e-15
    err_adamod = abs(theta_am_spike - 0.5)
    err_adam = abs(theta_ad_spike - 0.5)
    assert err_adamod < err_adam

    # 3. Verify stationary variance factor of s_t: sum_{k=0}^inf ((1 - beta3) * beta3^k)^2 = (1 - beta3) / (1 + beta3)
    b3_test = 0.9
    var_sum = sum(((1.0 - b3_test) * (b3_test ** k)) ** 2 for k in range(500))
    var_analytic = (1.0 - b3_test) / (1.0 + b3_test)
    var_err = abs(var_sum - var_analytic)
    assert var_err < 1e-15

    return adam_equiv_err, max_unrolled_err, eta_1_adamod / eta_1_adam, err_adamod, var_err


if __name__ == "__main__":
    eq_err, un_err, sp_rat, am_err, v_err = verify_adamod_identities_and_spike_suppression()
    print(
        f"[PASS] Round 613 AdaMod verified: "
        f"adam_equiv_err={eq_err:.2e}, unrolled_err={un_err:.2e}, "
        f"spike_lr_ratio={sp_rat:.4e}<<1, err_adamod={am_err:.4e}, var_err={v_err:.2e}"
    )
