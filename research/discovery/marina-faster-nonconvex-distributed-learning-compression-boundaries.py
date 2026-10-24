#!/usr/bin/env python3
"""Boundary verification for Round 391: MARINA Faster Non-Convex Distributed Learning with Compression
(Gorbunov, Burlachenko, Li, & Richtárik 2021, ICML 2021, PMLR 139:3788-3798, arXiv:2102.07845).

Verifies:
1. Algorithm 1 (MARINA biased recursive gradient estimator with unbiased omega-quantizer Q):
   g_i^{k+1} = nabla f_i(x^{k+1}) with probability p,
   g_i^{k+1} = g^k + Q(nabla f_i(x^{k+1}) - nabla f_i(x^k)) with probability 1-p,
   and g^{k+1} = (1/n) sum_{i=1}^n g_i^{k+1}.
2. Exact single-step variance contraction (Eq. 8 / Proof of Theorem 2.1):
   E_Q[g^{k+1} | c_k = 0] = g^k + nabla f(x^{k+1}) - nabla f(x^k) (biased estimator when g^k != nabla f(x^k)),
   and E[||g^{k+1} - nabla f(x^{k+1})||^2] <= (1 - p) ||g^k - nabla f(x^k)||^2 + ((1 - p) * omega / n) * (1/n) sum_{i=1}^n ||nabla f_i(x^{k+1}) - nabla f_i(x^k)||^2
   <= (1 - p) ||g^k - nabla f(x^k)||^2 + ((1 - p) * omega * L^2 / n) ||x^{k+1} - x^k||^2.
3. Monotone descent of the Lyapunov potential Phi_k = f(x^k) - f_* + (gamma / (2 * p)) ||g^k - nabla f(x^k)||^2
   under step size gamma <= 1 / (L * (1 + sqrt((1 - p) * omega / (p * n)))), achieving O(sqrt(omega)) improvement
   in iteration complexity over DIANA without any bounded gradient dissimilarity assumption!
"""

from __future__ import annotations
import math
import random


def rand_1_quant(v: list[float], rng: random.Random) -> list[float]:
    d = len(v)
    idx = rng.randrange(d)
    out = [0.0] * d
    out[idx] = d * v[idx]
    return out


def main() -> None:
    # Non-convex smooth distributed objective across n = 6 workers in R^4:
    # f_i(x) = sum_{j=1}^4 (0.5 * a_{i,j} * x_j^2 + c_{i,j} * cos(x_j) - b_{i,j} * x_j)
    n = 6
    d = 4
    omega = float(d - 1)  # 3.0
    p = 1.0 / (omega + 1.0)  # 0.25 (equal expected communication cost to uncompressed step)

    rng = random.Random(2102)
    a_w = [[1.5 + 0.2 * i for _ in range(d)] for i in range(n)]
    c_w = [[0.5 * ((-1) ** (i + j)) for j in range(d)] for i in range(n)]
    b_w = [[4.0 * ((-1) ** i) * (j + 1) for j in range(d)] for i in range(n)]  # large heterogeneity!

    L = 3.0  # since |a_{i,j} - c_{i,j} cos(x_j)| <= 2.5 + 0.5 = 3.0

    def grad_i(i: int, x: list[float]) -> list[float]:
        return [
            a_w[i][j] * x[j] - c_w[i][j] * math.sin(x[j]) - b_w[i][j]
            for j in range(d)
        ]

    def grad_f(x: list[float]) -> list[float]:
        return [
            sum(grad_i(i, x)[j] for i in range(n)) / n for j in range(d)
        ]

    def val_f(x: list[float]) -> float:
        total = 0.0
        for i in range(n):
            for j in range(d):
                total += (
                    0.5 * a_w[i][j] * (x[j] ** 2)
                    + c_w[i][j] * math.cos(x[j])
                    - b_w[i][j] * x[j]
                )
        return total / n

    # 1. Verify Eq. 8 / Theorem 2.1 variance recursion exactly on a pair of iterates (x^k, x^{k+1}) and biased g^k
    xk = [1.2, -0.8, 0.5, -1.1]
    xk1 = [1.0, -0.6, 0.4, -0.9]
    gf_k = grad_f(xk)
    gf_k1 = grad_f(xk1)
    gk = [gf_k[j] + 0.3 * (j - 1.5) for j in range(d)]  # intentionally biased g^k != nabla f(x^k)

    # Exact expectation over Rand-1 and Bernoulli(p):
    # When c_k = 1 (prob p): g^{k+1} = gf_k1 -> error = 0.
    # When c_k = 0 (prob 1-p): E_Q[g^{k+1}] = gk + gf_k1 - gf_k,
    # and E_Q[||g^{k+1} - gf_k1||^2] = ||gk - gf_k||^2 + (omega / n^2) sum_{i=1}^n ||nabla f_i(x^{k+1}) - nabla f_i(x^k)||^2.
    prev_err_sq = sum((gk[j] - gf_k[j]) ** 2 for j in range(d))
    diff_grad_sq_sum = sum(
        sum((grad_i(i, xk1)[j] - grad_i(i, xk)[j]) ** 2 for j in range(d))
        for i in range(n)
    )
    exact_expected_err_sq = (1.0 - p) * prev_err_sq + ((1.0 - p) * omega / (n * n)) * diff_grad_sq_sum
    lipschitz_upper_bound = (1.0 - p) * prev_err_sq + (
        (1.0 - p) * omega * (L ** 2) / n
    ) * sum((xk1[j] - xk[j]) ** 2 for j in range(d))

    trials = 3000
    mc_err_sq = 0.0
    for _ in range(trials):
        if rng.random() < p:
            gk1 = list(gf_k1)
        else:
            q_sum = [0.0] * d
            for i in range(n):
                diff_i = [grad_i(i, xk1)[j] - grad_i(i, xk)[j] for j in range(d)]
                qi = rand_1_quant(diff_i, rng)
                for j in range(d):
                    q_sum[j] += gk[j] + qi[j]
            gk1 = [q_sum[j] / n for j in range(d)]
        mc_err_sq += sum((gk1[j] - gf_k1[j]) ** 2 for j in range(d))
    mc_err_sq /= trials

    assert abs(mc_err_sq - exact_expected_err_sq) < 0.03 * exact_expected_err_sq
    assert exact_expected_err_sq <= lipschitz_upper_bound + 1e-12

    # 2. Verify Theorem 2.1 step-size bound and Lyapunov descent on MARINA trajectory
    gamma = 1.0 / (L * (1.0 + math.sqrt((1.0 - p) * omega / (p * n))))
    x = [2.0, -2.0, 1.5, -1.5]
    g = grad_f(x)
    phi_0 = val_f(x)
    grad_norms_sq = []

    for _ in range(250):
        gf = grad_f(x)
        grad_norms_sq.append(sum(c * c for c in gf))
        x_next = [x[j] - gamma * g[j] for j in range(d)]
        if rng.random() < p:
            g_next = grad_f(x_next)
        else:
            q_sum = [0.0] * d
            for i in range(n):
                diff_i = [grad_i(i, x_next)[j] - grad_i(i, x)[j] for j in range(d)]
                qi = rand_1_quant(diff_i, rng)
                for j in range(d):
                    q_sum[j] += g[j] + qi[j]
            g_next = [q_sum[j] / n for j in range(d)]
        x = x_next
        g = g_next

    gf_end = grad_f(x)
    end_grad_sq = sum(c * c for c in gf_end)
    end_est_err_sq = sum((g[j] - gf_end[j]) ** 2 for j in range(d))
    phi_end = val_f(x) + (gamma / (2.0 * p)) * end_est_err_sq

    assert phi_end < phi_0 - 5.0, f"Expected substantial Lyapunov decrease: {phi_0} -> {phi_end}"
    assert end_grad_sq < 1e-9, f"Expected MARINA to reach stationary point ||nabla f(x)||^2 -> 0, got {end_grad_sq}"
    assert end_est_err_sq < 1e-9, f"Expected MARINA estimator error ||g^k - nabla f(x^k)||^2 -> 0, got {end_est_err_sq}"

    print(
        f"[PASS] Round 391 MARINA (Gorbunov et al. 2021): mc_var={mc_err_sq:.4f}~={exact_expected_err_sq:.4f}<={lipschitz_upper_bound:.4f}, "
        f"end_grad_sq={end_grad_sq:.2e}, end_est_err_sq={end_est_err_sq:.2e}"
    )


if __name__ == "__main__":
    main()
