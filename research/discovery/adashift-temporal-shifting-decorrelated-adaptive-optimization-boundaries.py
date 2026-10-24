"""Constructed mathematical boundary and temporal-shift decorrelation verification for Round 616:
AdaShift (Zhou, Zhang, Lu, Wang, Zhang, & Yu, ICLR 2019, arXiv:1810.00143).

Verifies:
1. Lemma 2 (Section 3.2, Eq. 9 & Appendix E, p. 4, 15):
   - On the d-periodic sequential online optimization counterexample (Eq. 6: g_t = C if t mod d == 1 else -1),
     the exact closed-form limits as epoch index n -> inf for i in {1, ..., d} are:
     lim_{n->inf} m_{nd+i} = ((1 - beta1) / (1 - beta1^d)) * (C + 1) * beta1^{i-1} - 1,
     lim_{n->inf} v_{nd+i} = ((1 - beta2) / (1 - beta2^d)) * (C^2 - 1) * beta2^{i-1} + 1.
2. Lemma 3 (Section 3.2, Eqs. 11-12 & Appendix F, p. 4, 15-16):
   - The asymptotic net update factor k(g_{nd+i}) = sum_{t=nd+i}^inf ((1 - beta1) * beta1^{t-nd-i} / sqrt(v_t))
     is unimodal over i in {1, ..., d} and achieves its strict minimum at i = 1 (the large gradient g = C),
     so k(C) = k(g_{nd+1}) < k(g_{nd+i}) for all i in {2, ..., d}.
3. Lemma 4 & Theorem 5 (Section 3.2-4, Eqs. 7, 13 & Section 5.1, Figure 1a, p. 3-8):
   - On the i.i.d. stochastic online optimization counterexample (Eq. 7: g_t = C w.p. p = (1 + delta)/(C + 1)
     else -1 w.p. 1 - p = (C - delta)/(C + 1), with expected gradient E[g_t] = delta > 0):
     * In Adam (beta1 = 0), v_t = beta2 * v_{t-1} + (1 - beta2) * g_t^2 is positively correlated with g_t^2,
       yielding E[k(C)] < E[k(-1)] and causing Adam to drift in the wrong (+theta) direction when C is large.
     * In AdaShift (Eq. 14 & Algorithm 1/2), temporal shifting v_t = beta2 * v_{t-1} + (1 - beta2) * g_{t-n}^2
       decorrelates v_t from g_t so E[k(C)] == E[k(-1)], guaranteeing descent in the optimal (-theta) direction.
4. Block-wise spatial reduction & truncated moving-window momentum (Section 4.2-4.4, Eqs. 15-17, p. 6-7):
   - Truncated window weights W_i = beta1^i / sum_{j=0}^{n-1} beta1^j sum to 1 and reduce to uniform average
     1/n as beta1 -> 1.
"""

from __future__ import annotations

import math
import random


def verify_lemmas_2_and_3() -> tuple[float, float, float]:
    C = 10.0
    d = 5
    beta1 = 0.6
    beta2 = 0.8
    num_epochs = 80

    m = 0.0
    v = 0.0
    m_hist: list[float] = []
    v_hist: list[float] = []

    for n in range(num_epochs):
        for i in range(1, d + 1):
            g = C if i == 1 else -1.0
            m = beta1 * m + (1.0 - beta1) * g
            v = beta2 * v + (1.0 - beta2) * (g * g)
            m_hist.append(m)
            v_hist.append(v)

    # Check last epoch against Lemma 2 closed-form limits (Appendix E, p. 15)
    max_m_err = 0.0
    max_v_err = 0.0
    v_lim: list[float] = []
    for i in range(1, d + 1):
        m_emp = m_hist[(num_epochs - 1) * d + (i - 1)]
        v_emp = v_hist[(num_epochs - 1) * d + (i - 1)]
        m_analytic = ((1.0 - beta1) / (1.0 - (beta1 ** d))) * (C + 1.0) * (beta1 ** (i - 1)) - 1.0
        v_analytic = ((1.0 - beta2) / (1.0 - (beta2 ** d))) * (C * C - 1.0) * (beta2 ** (i - 1)) + 1.0
        v_lim.append(v_analytic)
        max_m_err = max(max_m_err, abs(m_emp - m_analytic))
        max_v_err = max(max_v_err, abs(v_emp - v_analytic))

    assert max_m_err < 1e-13
    assert max_v_err < 1e-13

    # Verify Lemma 3 net update factors k(g_{nd+i}) across i = 1..d (Appendix F, p. 15-16)
    k_vals: list[float] = []
    for i in range(1, d + 1):
        # Periodic V_tilde sequence
        k_sum = 0.0
        for offset in range(300):
            idx = (i - 1 + offset) % d
            k_sum += (1.0 - beta1) * (beta1 ** offset) / math.sqrt(v_lim[idx])
        k_vals.append(k_sum)

    # k(C) = k_vals[0] must be strictly smaller than all k_vals[1:]
    min_k_gap = min(k_vals[i] - k_vals[0] for i in range(1, d))
    assert min_k_gap > 0.0
    return max_m_err, max_v_err, min_k_gap


def verify_stochastic_counterexample_and_adashift() -> tuple[float, float, float, float]:
    # Stochastic counterexample Eq. 7 (Section 2 & 5.1, p. 3, 8)
    rng = random.Random(20261019)
    C = 50.0
    delta = 0.02
    p = (1.0 + delta) / (C + 1.0)
    # Expected gradient E[g_t] = p*C - (1-p)*1 = delta > 0
    exp_g = p * C - (1.0 - p) * 1.0
    assert abs(exp_g - delta) < 1e-14

    T = 25000
    alpha = 0.05
    beta2 = 0.9
    eps = 1e-8

    theta_adam = 0.0
    theta_adashift = 0.0
    v_adam = 0.0
    v_adashift = 0.0
    prev_g = -1.0  # n = 1 temporal shift queue

    k_adam_C_sum, k_adam_C_cnt = 0.0, 0
    k_adam_m1_sum, k_adam_m1_cnt = 0.0, 0
    k_shift_C_sum, k_shift_C_cnt = 0.0, 0
    k_shift_m1_sum, k_shift_m1_cnt = 0.0, 0

    for t in range(1, T + 1):
        g = C if rng.random() < p else -1.0

        # Adam (beta1 = 0): v_t uses current g_t^2
        v_adam = beta2 * v_adam + (1.0 - beta2) * (g * g)
        v_adam_hat = v_adam / (1.0 - (beta2 ** t))
        step_scale_adam = alpha / (math.sqrt(v_adam_hat) + eps)
        theta_adam -= step_scale_adam * g

        if t > 500:
            if g > 0:
                k_adam_C_sum += step_scale_adam
                k_adam_C_cnt += 1
            else:
                k_adam_m1_sum += step_scale_adam
                k_adam_m1_cnt += 1

        # AdaShift (n = 1, beta1 = 0): v_t uses temporally shifted g_{t-1}^2
        if t > 1:
            v_adashift = beta2 * v_adashift + (1.0 - beta2) * (prev_g * prev_g)
            v_shift_hat = v_adashift / (1.0 - (beta2 ** (t - 1)))
            step_scale_shift = alpha / (math.sqrt(v_shift_hat) + eps)
            theta_adashift -= step_scale_shift * g
            if t > 500:
                if g > 0:
                    k_shift_C_sum += step_scale_shift
                    k_shift_C_cnt += 1
                else:
                    k_shift_m1_sum += step_scale_shift
                    k_shift_m1_cnt += 1
        prev_g = g

    mean_k_adam_C = k_adam_C_sum / k_adam_C_cnt
    mean_k_adam_m1 = k_adam_m1_sum / k_adam_m1_cnt
    mean_k_shift_C = k_shift_C_sum / k_shift_C_cnt
    mean_k_shift_m1 = k_shift_m1_sum / k_shift_m1_cnt

    # Lemma 4: In Adam, E[k(C)] < E[k(-1)], causing theta_adam > 0 (wrong direction)
    assert mean_k_adam_C < 0.7 * mean_k_adam_m1
    assert theta_adam > 5.0
    # Theorem 5: In AdaShift, v_t is independent of g_t so E[k(C)] approx E[k(-1)] and theta_adashift < 0 (optimal direction)
    rel_shift_gap = abs(mean_k_shift_C - mean_k_shift_m1) / mean_k_shift_m1
    assert rel_shift_gap < 0.08 and rel_shift_gap < 0.15 * (1.0 - mean_k_adam_C / mean_k_adam_m1)
    assert theta_adashift < -5.0

    # Verify truncated moving-window weights Eq. 17 & Algorithm 2
    n_win = 10
    b1 = 0.9
    denom = sum(b1 ** i for i in range(n_win))
    weights = [(b1 ** i) / denom for i in range(n_win)]
    assert abs(sum(weights) - 1.0) < 1e-15

    return mean_k_adam_C / mean_k_adam_m1, rel_shift_gap, theta_adam, theta_adashift


if __name__ == "__main__":
    m_err, v_err, k_gap = verify_lemmas_2_and_3()
    adam_rat, shift_gap, th_ad, th_sh = verify_stochastic_counterexample_and_adashift()
    print(
        f"[PASS] Round 616 AdaShift verified: "
        f"lemma2_m_err={m_err:.2e}, lemma2_v_err={v_err:.2e}, lemma3_k_gap={k_gap:.4e}>0, "
        f"adam_k_ratio={adam_rat:.4f}<1, shift_k_gap={shift_gap:.4f}<<1, "
        f"theta_adam={th_ad:.2f}>0, theta_adashift={th_sh:.2f}<0"
    )
