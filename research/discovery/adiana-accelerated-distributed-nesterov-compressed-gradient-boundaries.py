#!/usr/bin/env python3
"""Boundary verification for Round 390: ADIANA Accelerated Distributed Nesterov Gradient Descent with Compression
(Li, Kovalev, Qian, & Richtárik 2020, ICML 2020, PMLR 119:5895-5904, arXiv:2002.11364).

Verifies:
1. Algorithm 2 (ADIANA three-sequence Nesterov coupling + loopless probabilistic reference w^k + dual
   compressed gradient differences):
   - Linear coupling: x^k = theta_1 z^k + theta_2 w^k + (1 - theta_1 - theta_2) y^k
   - Dual compression: workers compress BOTH C_i^k(nabla f_i(x^k) - h_i^k) to form g^k
     AND C_tilde_i^k(nabla f_i(w^k) - h_i^k) to update shift memory h_i^{k+1} = h_i^k + alpha C_tilde_i^k(nabla f_i(w^k) - h_i^k)
   - Loopless reference update: w^{k+1} = y^k with probability p, else w^k.
2. Lemmas 2 & 3 variance bounds:
   E_k[||g^k - nabla f(x^k)||^2] <= (2*omega/n) (2*L * D_f(x^k, w^k) + H^k),
   and contraction of shift error H^{k+1} = (1/n) sum_i ||h_i^{k+1} - nabla f_i(w^k)||^2:
   E_k[H^{k+1}] <= (1 - alpha) H^k.
3. Theorem 4 accelerated O(sqrt(L/mu)) rate vs non-accelerated DIANA O(L/mu) rate on ill-conditioned
   distributed strongly convex optimization (kappa = L/mu = 100).
"""

from __future__ import annotations
import math
import random


def rand_k_compress(v: list[float], rng: random.Random) -> list[float]:
    """Unbiased Rand-1 coordinate compressor in R^d with omega = d - 1."""
    d = len(v)
    idx = rng.randrange(d)
    out = [0.0] * d
    out[idx] = d * v[idx]
    return out


def main() -> None:
    # Ill-conditioned distributed quadratic problem in R^4 across n = 8 workers:
    # f_i(x) = 0.5 * sum_{j=1}^4 lam_j * (x_j - b_{i,j})^2, where lam = [100.0, 20.0, 5.0, 1.0] (L=100, mu=1, kappa=100)
    n = 8
    d = 4
    lam = [100.0, 20.0, 5.0, 1.0]
    L = 100.0
    mu = 1.0
    omega = float(d - 1)  # 3.0 for Rand-1 in R^4

    rng = random.Random(2020)
    b_workers = [
        [rng.uniform(-3.0, 3.0) for _ in range(d)] for _ in range(n)
    ]
    x_star = [sum(b_workers[i][j] for i in range(n)) / n for j in range(d)]

    def grad_i(i: int, x: list[float]) -> list[float]:
        return [lam[j] * (x[j] - b_workers[i][j]) for j in range(d)]

    def grad_f(x: list[float]) -> list[float]:
        return [lam[j] * (x[j] - x_star[j]) for j in range(d)]

    def bregman_f(x: list[float], w: list[float]) -> float:
        return sum(0.5 * lam[j] * ((x[j] - w[j]) ** 2) for j in range(d))

    # 1. Verify Lemma 2 & Lemma 3 exactly via Monte Carlo at a test state (x^k, w^k, h_i^k)
    xk = [1.5, -1.0, 2.0, -0.5]
    wk = [0.8, -0.4, 1.2, -0.1]
    hk = [[0.2 * (i - 3.5) for _ in range(d)] for i in range(n)]
    alpha = 1.0 / (omega + 1.0)  # 0.25

    Hk = sum(
        sum((hk[i][j] - grad_i(i, wk)[j]) ** 2 for j in range(d))
        for i in range(n)
    ) / n
    df_xw = bregman_f(xk, wk)
    lemma2_rhs = (2.0 * omega / n) * (2.0 * L * df_xw + Hk)
    lemma3_rhs = (1.0 - alpha) * Hk

    trials = 2000
    emp_g_var = 0.0
    emp_h_next = 0.0
    gf_xk = grad_f(xk)
    for _ in range(trials):
        c_sum = [0.0] * d
        h_next_err = 0.0
        for i in range(n):
            gi_x = grad_i(i, xk)
            gi_w = grad_i(i, wk)
            ci = rand_k_compress([gi_x[j] - hk[i][j] for j in range(d)], rng)
            cti = rand_k_compress([gi_w[j] - hk[i][j] for j in range(d)], rng)
            for j in range(d):
                c_sum[j] += hk[i][j] + ci[j]
                hi_new_j = hk[i][j] + alpha * cti[j]
                h_next_err += (hi_new_j - gi_w[j]) ** 2
        gk = [c_sum[j] / n for j in range(d)]
        emp_g_var += sum((gk[j] - gf_xk[j]) ** 2 for j in range(d))
        emp_h_next += h_next_err / n

    emp_g_var /= trials
    emp_h_next /= trials
    assert emp_g_var <= lemma2_rhs * 1.02, f"Lemma 2 violated: {emp_g_var} > {lemma2_rhs}"
    assert abs(emp_h_next - lemma3_rhs) < 0.05 * Hk, f"Lemma 3 mismatch: {emp_h_next} vs {lemma3_rhs}"

    # 2. Compare ADIANA (Algorithm 2) vs non-accelerated DIANA over K=300 iterations
    # With omega/n = 3/8 < 1, effective smoothness is close to L = 100, kappa = 100
    eta = 1.0 / (L * (1.0 + 6.0 * math.sqrt(omega / n)))
    theta1 = 1.0 / (2.0 * math.sqrt(L / mu))
    theta2 = 0.25
    p_ref = alpha
    gamma = eta / (2.0 * theta1 + eta * mu)
    beta = 1.0 - gamma * mu

    y_ad = [0.0] * d
    z_ad = [0.0] * d
    w_ad = [0.0] * d
    h_ad = [[0.0] * d for _ in range(n)]
    hbar_ad = [0.0] * d

    x_di = [0.0] * d
    h_di = [[0.0] * d for _ in range(n)]
    hbar_di = [0.0] * d
    gamma_di = 1.0 / (L * (1.0 + 6.0 * omega / n))

    for _ in range(350):
        # ADIANA step (Algorithm 2):
        x_ad = [
            theta1 * z_ad[j] + theta2 * w_ad[j] + (1.0 - theta1 - theta2) * y_ad[j]
            for j in range(d)
        ]
        c_sum = [0.0] * d
        ct_sum = [0.0] * d
        for i in range(n):
            gi_x = grad_i(i, x_ad)
            gi_w = grad_i(i, w_ad)
            ci = rand_k_compress([gi_x[j] - h_ad[i][j] for j in range(d)], rng)
            cti = rand_k_compress([gi_w[j] - h_ad[i][j] for j in range(d)], rng)
            for j in range(d):
                c_sum[j] += ci[j]
                ct_sum[j] += cti[j]
                h_ad[i][j] += alpha * cti[j]
        gk = [hbar_ad[j] + c_sum[j] / n for j in range(d)]
        y_next = [x_ad[j] - eta * gk[j] for j in range(d)]
        z_ad = [
            beta * z_ad[j] + (1.0 - beta) * x_ad[j] - (gamma / eta) * (x_ad[j] - y_next[j])
            for j in range(d)
        ]
        if rng.random() < p_ref:
            w_ad = list(y_ad)
        y_ad = y_next
        hbar_ad = [hbar_ad[j] + alpha * (ct_sum[j] / n) for j in range(d)]

        # DIANA step:
        c_di_sum = [0.0] * d
        for i in range(n):
            gi = grad_i(i, x_di)
            ci = rand_k_compress([gi[j] - h_di[i][j] for j in range(d)], rng)
            for j in range(d):
                c_di_sum[j] += ci[j]
                h_di[i][j] += alpha * ci[j]
        g_di = [hbar_di[j] + c_di_sum[j] / n for j in range(d)]
        x_di = [x_di[j] - gamma_di * g_di[j] for j in range(d)]
        hbar_di = [hbar_di[j] + alpha * (c_di_sum[j] / n) for j in range(d)]

    err_adiana = sum((y_ad[j] - x_star[j]) ** 2 for j in range(d))
    err_diana = sum((x_di[j] - x_star[j]) ** 2 for j in range(d))
    assert err_adiana < err_diana * 0.05, f"Expected ADIANA acceleration over DIANA: {err_adiana} vs {err_diana}"
    assert err_adiana < 1e-5, f"ADIANA error too large: {err_adiana}"

    print(
        f"[PASS] Round 390 ADIANA (Li et al. 2020): Lemma2_var={emp_g_var:.2f}<={lemma2_rhs:.2f}, "
        f"Lemma3_H={emp_h_next:.2f}~={lemma3_rhs:.2f}, err_adiana={err_adiana:.2e} << err_diana={err_diana:.2e}"
    )


if __name__ == "__main__":
    main()
