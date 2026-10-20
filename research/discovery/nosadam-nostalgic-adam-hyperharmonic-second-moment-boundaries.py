"""Constructed mathematical boundary and hyperharmonic nostalgia verification for Round 617:
Nostalgic Adam / NosAdam (Huang, Wang, & Dong, IJCAI 2019, arXiv:1805.07557).

Verifies:
1. Algorithm 1 & Lemma 3.1 (Section 3, p. 3-4):
   - With beta_{2,t} = B_{t-1} / B_t where B_t = sum_{k=1}^t b_k (b_k >= 0, B_0 = 0),
     the recursive update V_t = beta_{2,t} V_{t-1} + (1 - beta_{2,t}) g_t^2 equals the exact
     weighted average V_t = (1 / B_t) * sum_{j=1}^t b_j g_j^2.
   - With alpha_t = alpha / sqrt(t), Gamma_t = V_t / alpha_t^2 - V_{t-1} / alpha_{t-1}^2 >= 0
     holds for all gradient sequences if and only if B_t / t is non-increasing (b_k non-increasing).
2. Theorem 3.2, Corollary 3.2.1, & Theorem A.1 (Section 3, p. 4 & Appendix A, p. 11-16):
   - Hyperharmonic weights b_k = k^{-gamma} (gamma >= 0, NosAdam-HH) automatically satisfy both
     convergence conditions:
     (1) B_t / t <= B_{t-1} / (t - 1), and
     (2) B_t / (t * b_t^p) >= B_{t-1} / ((t - 1) * b_{t-1}^p) for p >= 2.
   - Lemma A.5 algebraic inequality: 1 / S_j^{1/p} <= (p / (p - 1)) * (S_j^{(p-1)/p} - S_{j-1}^{(p-1)/p}) / (S_j - S_{j-1})
     for all p > 1 and 0 < S_{j-1} < S_j.
   - Corollary 3.2.1 O(sqrt(T)) regret bound holds on 1D online convex optimization.
3. Section 4 Counterexample & Outlier Spike Recovery (Eq. 4, Figures 1 & 3, p. 5-7):
   - On Reddi et al.'s 3-periodic counterexample (f_t(x) = C*x if t mod 3 == 1 else -x, C > 2, x in [-1, 1]),
     Adam diverges to +1 whereas NosAdam-HH converges to the true optimum x* = -1.
   - When a single massive outlier gradient spike occurs at step t_spike, AMSGrad's v_hat_t = max(v_hat_{t-1}, v_t)
     is permanently pinned at the spike level whereas NosAdam's V_t decays back toward the nominal gradient scale.
"""

from __future__ import annotations

import math
import random


def verify_lemma_3_1_and_hyperharmonic_conditions() -> tuple[float, float, float]:
    rng = random.Random(20261019)
    T = 60
    gamma = 0.35
    p = 2.0
    alpha = 0.1

    b = [k ** (-gamma) for k in range(1, T + 1)]
    B = []
    running_B = 0.0
    for val in b:
        running_B += val
        B.append(running_B)

    grads = [rng.uniform(-3.0, 3.0) for _ in range(T)]
    v_rec = 0.0
    max_unrolled_err = 0.0
    min_gamma_diff = float("inf")
    prev_scaled_v = 0.0

    for t in range(1, T + 1):
        beta2_t = (B[t - 2] / B[t - 1]) if t > 1 else 0.0
        v_rec = beta2_t * v_rec + (1.0 - beta2_t) * (grads[t - 1] ** 2)
        v_weighted = sum(b[j - 1] * (grads[j - 1] ** 2) for j in range(1, t + 1)) / B[t - 1]
        max_unrolled_err = max(max_unrolled_err, abs(v_rec - v_weighted))

        alpha_t = alpha / math.sqrt(t)
        scaled_v = v_rec / (alpha_t * alpha_t)
        if t > 1:
            # Verify Condition 1: B_t / t <= B_{t-1} / (t - 1)
            assert (B[t - 1] / t) <= (B[t - 2] / (t - 1)) + 1e-15
            # Verify Condition 2: B_t / (t * b_t^p) >= B_{t-1} / ((t - 1) * b_{t-1}^p)
            lhs2 = B[t - 1] / (t * (b[t - 1] ** p))
            rhs2 = B[t - 2] / ((t - 1) * (b[t - 2] ** p))
            assert lhs2 + 1e-15 >= rhs2
            # Verify Lemma 3.1: V_t / alpha_t^2 - V_{t-1} / alpha_{t-1}^2 >= 0
            min_gamma_diff = min(min_gamma_diff, scaled_v - prev_scaled_v)
        prev_scaled_v = scaled_v

    assert max_unrolled_err < 1e-13
    assert min_gamma_diff >= -1e-15

    # Verify Lemma A.5 inequality (p. 15-16) for p in {1.5, 2.0, 3.0}
    max_lemma_a5_ratio = 0.0
    for p_val in (1.5, 2.0, 3.0):
        s_prev = 0.4
        for j in range(20):
            s_curr = s_prev + rng.uniform(0.1, 2.5)
            lhs = 1.0 / (s_curr ** (1.0 / p_val))
            rhs = (p_val / (p_val - 1.0)) * (
                (s_curr ** ((p_val - 1.0) / p_val) - s_prev ** ((p_val - 1.0) / p_val)) / (s_curr - s_prev)
            )
            assert lhs <= rhs + 1e-15
            max_lemma_a5_ratio = max(max_lemma_a5_ratio, lhs / rhs)
            s_prev = s_curr

    return max_unrolled_err, min_gamma_diff, max_lemma_a5_ratio


def verify_regret_counterexample_and_spike_recovery() -> tuple[float, float, float, float]:
    # 1. Verify Corollary 3.2.1 regret bound on 1D convex functions f_t(x) = 0.5 * (x - c_t)^2 on [-1, 1]
    rng = random.Random(20261019)
    T = 300
    D_inf = 2.0
    G_inf = 2.0
    alpha = 0.2
    beta1 = 0.9
    lam = 0.8
    gamma = 0.2

    x = 0.5
    x_star = -0.25
    m = 0.0
    v = 0.0
    B_t = 0.0
    regret = 0.0

    for t in range(1, T + 1):
        c_t = x_star + (0.3 if t % 2 == 0 else -0.3)
        f_x = 0.5 * ((x - c_t) ** 2)
        f_star = 0.5 * ((x_star - c_t) ** 2)
        regret += f_x - f_star

        g = x - c_t
        b_t = t ** (-gamma)
        B_prev = B_t
        B_t += b_t
        beta2_t = B_prev / B_t if t > 1 else 0.0
        beta1_t = beta1 * (lam ** (t - 1))

        m = beta1_t * m + (1.0 - beta1_t) * g
        v = beta2_t * v + (1.0 - beta2_t) * (g * g)
        alpha_t = alpha / math.sqrt(t)
        x_hat = x - alpha_t * m / math.sqrt(max(v, 1e-16))
        x = max(-1.0, min(1.0, x_hat))

    cor_rhs = (
        ((D_inf ** 2) / (2.0 * alpha * (1.0 - beta1))) * math.sqrt(T) * math.sqrt(v)
        + ((D_inf ** 2) * G_inf * beta1) / (2.0 * (1.0 - beta1) * ((1.0 - lam) ** 2))
        + (2.0 * alpha * beta1 / ((1.0 - beta1) ** 3)) * G_inf * math.sqrt(T)
    )
    assert regret <= cor_rhs

    # 2. Verify Section 4 (Eq. 4, p. 5) 3-periodic counterexample: f_t(x) = C*x if t mod 3 == 1 else -x (C = 10.0, beta2 = 0.05)
    C = 10.0
    x_adam = 0.0
    x_nos = 0.0
    m_ad, v_ad = 0.0, 0.0
    m_ns, v_ns, B_ns = 0.0, 0.0, 0.0
    for t in range(1, 1501):
        g = C if (t % 3 == 1) else -1.0
        lr = 0.5 / math.sqrt(t)
        # Adam (beta1 = 0, beta2 = 0.05 < 1 / (1 + C^2/4))
        v_ad = 0.05 * v_ad + 0.95 * (g * g)
        x_adam = max(-1.0, min(1.0, x_adam - lr * g / (math.sqrt(v_ad) + 1e-8)))

        # NosAdam-HH (beta1 = 0, gamma = 0.1)
        b_t = t ** (-0.1)
        B_prev = B_ns
        B_ns += b_t
        b2_t = B_prev / B_ns if t > 1 else 0.0
        v_ns = b2_t * v_ns + (1.0 - b2_t) * (g * g)
        x_nos = max(-1.0, min(1.0, x_nos - lr * g / (math.sqrt(v_ns) + 1e-8)))

    assert x_adam > 0.8 and x_nos < -0.8

    # 3. Verify outlier gradient spike recovery vs AMSGrad (Section 4, Figure 3, p. 6-7)
    v_ams = 0.0
    v_hat_ams = 0.0
    v_nos_spike = 0.0
    B_sp = 0.0
    for t in range(1, 501):
        g = 100.0 if t == 10 else 1.0
        v_ams = 0.9 * v_ams + 0.1 * (g * g)
        v_hat_ams = max(v_hat_ams, v_ams)

        b_t = t ** (-0.1)
        B_prev = B_sp
        B_sp += b_t
        b2_t = B_prev / B_sp if t > 1 else 0.0
        v_nos_spike = b2_t * v_nos_spike + (1.0 - b2_t) * (g * g)

    # At t = 500, AMSGrad's v_hat_ams is still > 1000 while NosAdam's v_nos_spike has decayed below 35
    assert v_hat_ams > 1000.0 and v_nos_spike < 35.0
    return regret / cor_rhs, x_adam, x_nos, v_nos_spike / v_hat_ams


if __name__ == "__main__":
    un_err, g_diff, a5_rat = verify_lemma_3_1_and_hyperharmonic_conditions()
    reg_rat, x_ad, x_ns, sp_rat = verify_regret_counterexample_and_spike_recovery()
    print(
        f"[PASS] Round 617 NosAdam verified: "
        f"unrolled_err={un_err:.2e}, min_gamma_diff={g_diff:.2e}>=0, lemma_a5_rat={a5_rat:.4f}<=1, "
        f"regret_ratio={reg_rat:.4f}<=1, x_adam={x_ad:.2f}>0, x_nosadam={x_ns:.2f}<0, spike_v_ratio={sp_rat:.4f}<<1"
    )
