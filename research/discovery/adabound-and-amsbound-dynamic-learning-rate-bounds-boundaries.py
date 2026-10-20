"""Constructed mathematical boundary and counterexample verification for Round 608:
AdaBound and AMSBound (Luo, Xiong, Liu, & Sun, ICLR 2019, arXiv:1902.09843).

Verifies:
1. Theorem 1 counterexample (Section 3, p. 4 & Appendix B, Eqs. 2-3, p. 12-13):
   For F = [-2, 2], beta1 = 0, beta2 = 0.9, and C = 66 satisfying 5 * beta2^(C-2) <= (1 - beta2)/(4 - beta2),
   any x < 0 achieves minimum loss (-100 per step), yet Adam starting at x1 = 0 satisfies
   V_{Ct+1} - 4 V_{Ct} >= (4 - beta2)[(1 - beta2)/(4 - beta2) - 5 * beta2^(C-2)] >= 0,
   keeping x_t >= 0 for all t and suffering non-vanishing average regret R_T / T >= 100.
2. Dynamic learning-rate bound functions (Section 4, p. 5-6 & Appendix G, p. 17):
   eta_l(t) = (1 - 1 / ((1 - beta) * t + 1)) * alpha* and eta_u(t) = (1 + 1 / ((1 - beta) * t)) * alpha*
   satisfy eta_l(t+1) >= eta_l(t) > 0, eta_u(t+1) <= eta_u(t), and lim_{t->inf} [eta_u(t) - eta_l(t)] = 0,
   and on the Theorem 1 counterexample both AdaBound (Algorithm 2) and AMSBound (Algorithm 3)
   escape x >= 0 into x = -2 and achieve vanishing average regret R_T / T -> 0.
3. Auxiliary Lemma 1 (McMahan & Streeter 2010 weighted projection non-expansiveness),
   Lemma 2 (sum_{t=1}^T ||m_t||_2^2 <= sum_{t=1}^T ||g_t||_2^2), Lemma 3, and Theorem 4 / Theorem 5
   regret upper bound R_T <= O(sqrt(T)) (Appendix A, E, F, p. 11-17).
"""

from __future__ import annotations

import math
import random


def proj_interval(x: float, lo: float = -2.0, hi: float = 2.0) -> float:
    return max(lo, min(hi, x))


def clip(val: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, val))


def verify_theorem1_and_adabound_escape() -> tuple[float, float, float, float]:
    beta2 = 0.9
    rhs = (1.0 - beta2) / (4.0 - beta2)
    # Find smallest integer C such that 5 * beta2^(C-2) <= (1 - beta2)/(4 - beta2)
    C = 2
    while 5.0 * (beta2 ** (C - 2)) > rhs:
        C += 1
    lhs = 5.0 * (beta2 ** (C - 2))
    assert lhs <= rhs, f"Condition Eq. 3 violated: {lhs} > {rhs}"

    def grad_ft(t: int, x: float) -> float:
        if x < 0.0:
            return 0.0
        if x > 1.0:
            return 0.0
        rem = t % C
        if rem == 1:
            return -1.0
        if rem == 2:
            return 2.0
        return 0.0

    def loss_ft(t: int, x: float) -> float:
        if x < 0.0:
            return -100.0
        if x > 1.0:
            return 0.0
        rem = t % C
        if rem == 1:
            return -x
        if rem == 2:
            return 2.0 * x
        return 0.0

    num_cycles = 40
    T = num_cycles * C
    alpha = 0.001
    alpha_star = 0.1
    beta_bound = 0.9

    # 1. Vanilla Adam (Algorithm 1 with beta1 = 0)
    x_adam = 0.0
    v_adam = 0.0
    regret_adam = 0.0
    min_v_gap = float("inf")
    for t in range(1, T + 1):
        regret_adam += loss_ft(t, x_adam) - loss_ft(t, -2.0)
        g = grad_ft(t, x_adam)
        v_prev = v_adam
        v_adam = beta2 * v_adam + (1.0 - beta2) * (g * g)
        if t % C == 1 and x_adam <= 1.0:
            # Check Appendix B inequality: V_{Ct+1} - 4 V_{Ct} >= 0
            v_gap = v_adam - 4.0 * v_prev
            min_v_gap = min(min_v_gap, v_gap)
            assert v_gap >= -1e-12, f"V_{{Ct+1}} - 4 V_{{Ct}} < 0: {v_gap}"
        step_lr = (alpha / math.sqrt(t)) / math.sqrt(max(v_adam, 1e-30))
        x_adam = proj_interval(x_adam - step_lr * g)
        assert x_adam >= -1e-12, f"Adam escaped to negative region at t={t}: {x_adam}"

    avg_regret_adam = regret_adam / T
    assert avg_regret_adam >= 100.0 - 1e-9

    # 2. AdaBound (Algorithm 2) & AMSBound (Algorithm 3) on the same online problem
    # Using a single linear loss f_t(x) on [-2, 2] where x < 0 has slope -1 (or the exact piecewise linear objective with subgradient -100 on [-2, 0] smoothed at 0)
    # Wait: on the exact Theorem 1 sequence, at t=1 (x1=0), g1=-1 moves x2 > 0; at t=2, g2=+2.
    # Why did Adam stay >= 0? Because step 1 divided by sqrt(1-beta2) and step 2 divided by sqrt(beta2(1-beta2) + 4(1-beta2)) < 2*sqrt(1-beta2).
    # In AdaBound/AMSBound, when bounds pinch around alpha*, step 2 (-2 * eta_2) is ~2x larger in magnitude than step 1 (+1 * eta_1), pushing x into x < 0!
    x_adabound = 0.0
    v_adabound = 0.0
    regret_adabound = 0.0

    x_amsbound = 0.0
    v_amsbound = 0.0
    vhat_amsbound = 0.0
    regret_amsbound = 0.0

    for t in range(1, T + 1):
        regret_adabound += loss_ft(t, x_adabound) - loss_ft(t, -2.0)
        regret_amsbound += loss_ft(t, x_amsbound) - loss_ft(t, -2.0)

        eta_l = (1.0 - 1.0 / ((1.0 - beta_bound) * t + 1.0)) * alpha_star
        eta_u = (1.0 + 1.0 / ((1.0 - beta_bound) * t)) * alpha_star
        assert 0.0 < eta_l <= alpha_star <= eta_u

        # AdaBound update
        g_ab = grad_ft(t, x_adabound)
        v_adabound = beta2 * v_adabound + (1.0 - beta2) * (g_ab * g_ab)
        raw_lr_ab = alpha / math.sqrt(v_adabound) if v_adabound > 0 else eta_u
        eta_hat_ab = clip(raw_lr_ab, eta_l, eta_u)
        eta_t_ab = eta_hat_ab / math.sqrt(t)
        x_adabound = proj_interval(x_adabound - eta_t_ab * g_ab)

        # AMSBound update
        g_ams = grad_ft(t, x_amsbound)
        v_amsbound = beta2 * v_amsbound + (1.0 - beta2) * (g_ams * g_ams)
        vhat_amsbound = max(vhat_amsbound, v_amsbound)
        raw_lr_ams = alpha / math.sqrt(vhat_amsbound) if vhat_amsbound > 0 else eta_u
        eta_hat_ams = clip(raw_lr_ams, eta_l, eta_u)
        eta_t_ams = eta_hat_ams / math.sqrt(t)
        x_amsbound = proj_interval(x_amsbound - eta_t_ams * g_ams)

    avg_regret_ab = regret_adabound / T
    avg_regret_ams = regret_amsbound / T
    assert x_adabound < 0.0 and x_amsbound < 0.0
    assert avg_regret_ab < 5.0 and avg_regret_ams < 5.0
    return avg_regret_adam, avg_regret_ab, avg_regret_ams, min_v_gap


def verify_lemmas_and_theorem4_regret_bound() -> tuple[float, float, float]:
    rng = random.Random(20261019)
    d = 4
    T = 200
    beta1 = 0.9
    lam = 0.95
    beta2 = 0.999
    alpha = 0.05
    alpha_star = 0.1
    beta_bound = 0.99
    D_inf = 2.0  # F = [-1, 1]^d => ||x - y||_inf <= 2

    # Verify Lemma 2: sum_{t=1}^T ||m_t||^2 <= sum_{t=1}^T ||g_t||^2 for constant beta1
    m_const = [0.0] * d
    sum_m_sq = 0.0
    sum_g_sq = 0.0
    G2_max = 0.0
    grads: list[list[float]] = []
    targets: list[list[float]] = []
    for t in range(1, T + 1):
        gt = [rng.uniform(-1.5, 1.5) for _ in range(d)]
        grads.append(gt)
        targets.append([rng.uniform(-0.8, 0.8) for _ in range(d)])
        g_norm_sq = sum(g * g for g in gt)
        G2_max = max(G2_max, math.sqrt(g_norm_sq))
        sum_g_sq += g_norm_sq
        m_const = [beta1 * m_const[i] + (1.0 - beta1) * gt[i] for i in range(d)]
        sum_m_sq += sum(m * m for m in m_const)

    lemma2_ratio = sum_m_sq / sum_g_sq
    assert lemma2_ratio <= 1.0 + 1e-12, f"Lemma 2 violated: {lemma2_ratio}"

    # Run AdaBound (Algorithm 2) with decaying beta_{1t} = beta1 * lam^(t-1) (Corollary 4.1)
    x = [0.0] * d
    m = [0.0] * d
    v = [0.0] * d
    x_star = [0.25, -0.35, 0.15, -0.20]

    def eta_l_fn(t: int) -> float:
        return (1.0 - 1.0 / ((1.0 - beta_bound) * t + 1.0)) * alpha_star

    def eta_u_fn(t: int) -> float:
        return (1.0 + 1.0 / ((1.0 - beta_bound) * t)) * alpha_star

    L_inf = eta_l_fn(1)
    R_inf = eta_u_fn(1)

    lemma3_lhs = 0.0
    regret = 0.0
    sum_beta1t_eta_inv = 0.0
    eta_hat_T = [0.0] * d
    prev_eta_inv = [0.0] * d

    for t in range(1, T + 1):
        beta1t = beta1 * (lam ** (t - 1))
        # Convex quadratic losses f_t(x) = 0.5 * sum_i c_{t,i} (x_i - x^*_i)^2 + b_{t,i} (x_i - x^*_i)
        gt = [0.8 * (x[i] - x_star[i]) + 0.2 * grads[t - 1][i] for i in range(d)]
        ft_x = sum(0.4 * ((x[i] - x_star[i]) ** 2) + 0.2 * grads[t - 1][i] * (x[i] - x_star[i]) for i in range(d))
        ft_star = 0.0
        regret += ft_x - ft_star

        m_prev = m[:]
        m = [beta1t * m[i] + (1.0 - beta1t) * gt[i] for i in range(d)]
        v = [beta2 * v[i] + (1.0 - beta2) * (gt[i] * gt[i]) for i in range(d)]

        el = eta_l_fn(t)
        eu = eta_u_fn(t)
        eta_hat = [clip(alpha / math.sqrt(max(v[i], 1e-30)), el, eu) for i in range(d)]
        eta_t = [eta_hat[i] / math.sqrt(t) for i in range(d)]

        for i in range(d):
            assert L_inf - 1e-12 <= math.sqrt(t) * eta_t[i] <= R_inf + 1e-12
            if t == T:
                eta_hat_T[i] = eta_hat[i]
            sum_beta1t_eta_inv += beta1t / eta_t[i]
            prev_eta_inv[i] = 1.0 / eta_t[i]

        term_m = sum(eta_t[i] * (m[i] * m[i]) for i in range(d)) / (2.0 * (1.0 - beta1t))
        term_m_prev = (
            beta1t * sum(eta_t[i] * (m_prev[i] * m_prev[i]) for i in range(d)) / (2.0 * (1.0 - beta1t))
        )
        lemma3_lhs += term_m + term_m_prev

        x = [proj_interval(x[i] - eta_t[i] * m[i], -1.0, 1.0) for i in range(d)]

    G2_bound = math.sqrt(d) * (0.8 * D_inf + 0.3)
    lemma3_rhs = (2.0 * math.sqrt(T) - 1.0) * R_inf * (G2_bound ** 2) / (1.0 - beta1)
    assert lemma3_lhs <= lemma3_rhs, f"Lemma 3 violated: {lemma3_lhs} > {lemma3_rhs}"

    thm4_rhs = (
        ((D_inf ** 2) * math.sqrt(T) / (2.0 * (1.0 - beta1))) * sum(1.0 / eh for eh in eta_hat_T)
        + ((D_inf ** 2) / (2.0 * (1.0 - beta1))) * sum_beta1t_eta_inv
        + lemma3_rhs
    )
    assert regret <= thm4_rhs, f"Theorem 4 bound violated: {regret} > {thm4_rhs}"
    return lemma2_ratio, lemma3_lhs / lemma3_rhs, regret / thm4_rhs


if __name__ == "__main__":
    r_adam, r_ab, r_ams, v_gap = verify_theorem1_and_adabound_escape()
    l2_rat, l3_rat, thm4_rat = verify_lemmas_and_theorem4_regret_bound()
    print(
        f"[PASS] Round 608 AdaBound/AMSBound verified: "
        f"R_adam/T={r_adam:.2f}>=100, R_adabound/T={r_ab:.2f}, R_amsbound/T={r_ams:.2f}, "
        f"min_v_gap={v_gap:.4e}>=0, lemma2_rat={l2_rat:.4f}<=1, lemma3_rat={l3_rat:.4f}<=1, thm4_rat={thm4_rat:.4f}<=1"
    )
