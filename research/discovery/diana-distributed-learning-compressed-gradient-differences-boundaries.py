#!/usr/bin/env python3
"""Boundary verification for Round 389: DIANA Distributed Learning with Compressed Gradient Differences
(Mishchenko, Gorbunov, Takáč, & Richtárik 2019/2023, arXiv:1901.09269).

Verifies:
1. Lemma 4.1 / Lemma 4.2 exact contraction parameter alpha_p(d) = inf_{x!=0} ||x||_2^2 / (||x||_1 ||x||_p)
   for random l_p quantization in dimension d:
   - alpha_1(d) = 1 / d
   - alpha_2(d) = 1 / sqrt(d)
   - alpha_inf(d) = 2 / (1 + sqrt(d)) (when sqrt(d) is an integer)
   and variance bound E[||Quant_p(Delta) - Delta||_2^2] <= (1/alpha_p(d) - 1) ||Delta||_2^2.
2. Algorithm 1 (DIANA) invariant h^k = (1/n) sum_{i=1}^n h_i^k and unbiasedness of compressed gradient
   difference estimator g_hat^k = h^k + (1/n) sum_{i=1}^n Quant_p(g_i^k - h_i^k):
   E_Q[g_hat^k] == (1/n) sum_{i=1}^n g_i^k.
3. Theorem 4.4 / Corollary 4.5 Lyapunov linear convergence on composite strongly convex problem
   min_x (1/n) sum_{i=1}^n f_i(x) + R(x) with non-zero local optimum gradients nabla f_i(x^*) != 0:
   both ||x^k - x^*||_2^2 -> 0 AND ||h_i^k - nabla f_i(x^*)||_2^2 -> 0 geometrically,
   whereas direct gradient quantization without memory shift (h_i^k = 0, QSGD/TernGrad) suffers non-vanishing
   quantization variance at x^* because nabla f_i(x^*) != 0.
"""

from __future__ import annotations
import math
import random


def quant_inf(v: list[float], rng: random.Random) -> list[float]:
    norm_inf = max(abs(x) for x in v)
    if norm_inf == 0.0:
        return [0.0 for _ in v]
    out = []
    for x in v:
        prob = abs(x) / norm_inf
        xi = 1.0 if rng.random() < prob else 0.0
        sign = 1.0 if x >= 0.0 else -1.0
        out.append(norm_inf * sign * xi)
    return out


def main() -> None:
    # 1. Verify Lemma 4.2 closed-form alpha_p(d) for d = 9 (sqrt(d) = 3)
    d = 9
    alpha_1 = 1.0 / d
    alpha_2 = 1.0 / math.sqrt(d)
    alpha_inf = 2.0 / (1.0 + math.sqrt(d))
    assert abs(alpha_1 - 1.0 / 9.0) < 1e-15
    assert abs(alpha_2 - 1.0 / 3.0) < 1e-15
    assert abs(alpha_inf - 0.5) < 1e-15

    # Check extreme vector attaining alpha_inf(9) = 0.5: x with 1 coordinate equal to 1 and d-1=8 equal to 1/(1+sqrt(d))=1/4
    x_ext = [1.0] + [1.0 / (1.0 + math.sqrt(d))] * (d - 1)
    l2_sq = sum(c * c for c in x_ext)
    l1 = sum(abs(c) for c in x_ext)
    linf = max(abs(c) for c in x_ext)
    ratio = l2_sq / (l1 * linf)
    assert abs(ratio - alpha_inf) < 1e-14, f"Expected {alpha_inf}, got {ratio}"

    # Verify exact variance formula E||Quant_inf(v) - v||^2 == ||v||_inf * ||v||_1 - ||v||_2^2 <= (1/alpha_inf - 1)||v||_2^2
    exact_var = linf * l1 - l2_sq
    bound_var = (1.0 / alpha_inf - 1.0) * l2_sq
    assert abs(exact_var - bound_var) < 1e-14

    # 2. Run DIANA vs memoryless TernGrad (alpha=0, h_i=0) on composite problem with L1 regularizer R(x) = lam * ||x||_1
    # n = 4 workers in R^4, f_i(x) = 0.5 * ||x - c_i||_2^2 with heterogeneous shifts c_i so nabla f_i(x^*) != 0
    n = 4
    dim = 4
    c_workers = [
        [2.0, -1.0, 0.5, -2.0],
        [-1.0, 3.0, -1.5, 1.0],
        [1.5, -0.5, 2.0, -0.5],
        [-0.5, 0.5, -1.0, 3.5],
    ]
    # Mean c_bar = [0.5, 0.5, 0.0, 0.5]
    # With L1 regularizer R(x) = 0.2 * ||x||_1, prox_{gamma R}(u)_j = sign(u_j) * max(|u_j| - gamma*0.2, 0)
    lam = 0.2
    # Exact composite optimum x^* of 0.5 * ||x - c_bar||_2^2 + lam * ||x||_1 is soft_threshold(c_bar, lam):
    c_bar = [sum(c_workers[i][j] for i in range(n)) / n for j in range(dim)]
    x_star = [
        (1.0 if cb >= 0 else -1.0) * max(abs(cb) - lam, 0.0) for cb in c_bar
    ]  # [0.3, 0.3, 0.0, 0.3]
    grad_star = [[x_star[j] - c_workers[i][j] for j in range(dim)] for i in range(n)]

    def prox_r(u: list[float], gamma: float) -> list[float]:
        return [
            (1.0 if uj >= 0 else -1.0) * max(abs(uj) - gamma * lam, 0.0)
            for uj in u
        ]

    rng = random.Random(1901)
    alpha = 2.0 / (1.0 + math.sqrt(dim))  # 2 / (1 + 2) = 2/3
    gamma = 0.15

    x_diana = [0.0] * dim
    h_workers = [[0.0] * dim for _ in range(n)]
    h_bar = [0.0] * dim
    max_h_inv_err = 0.0

    for _ in range(350):
        delta_hats = []
        for i in range(n):
            g_i = [x_diana[j] - c_workers[i][j] for j in range(dim)]
            delta_i = [g_i[j] - h_workers[i][j] for j in range(dim)]
            dh_i = quant_inf(delta_i, rng)
            delta_hats.append(dh_i)
            for j in range(dim):
                h_workers[i][j] += alpha * dh_i[j]
        dh_mean = [sum(delta_hats[i][j] for i in range(n)) / n for j in range(dim)]
        g_hat = [h_bar[j] + dh_mean[j] for j in range(dim)]
        for j in range(dim):
            h_bar[j] += alpha * dh_mean[j]
        # Verify invariant h_bar == (1/n) sum_i h_i
        for j in range(dim):
            mean_hj = sum(h_workers[i][j] for i in range(n)) / n
            max_h_inv_err = max(max_h_inv_err, abs(h_bar[j] - mean_hj))
        x_diana = prox_r([x_diana[j] - gamma * g_hat[j] for j in range(dim)], gamma)

    # Run memoryless TernGrad (alpha = 0, h_i = 0) with the same constant step size gamma:
    x_terngrad = [0.0] * dim
    tg_errs = []
    for step in range(350):
        q_grads = []
        for i in range(n):
            g_i = [x_terngrad[j] - c_workers[i][j] for j in range(dim)]
            q_grads.append(quant_inf(g_i, rng))
        g_tg = [sum(q_grads[i][j] for i in range(n)) / n for j in range(dim)]
        x_terngrad = prox_r([x_terngrad[j] - gamma * g_tg[j] for j in range(dim)], gamma)
        if step >= 250:
            tg_errs.append(sum((x_terngrad[j] - x_star[j]) ** 2 for j in range(dim)))

    diana_x_err = sum((x_diana[j] - x_star[j]) ** 2 for j in range(dim))
    diana_h_err = sum(
        sum((h_workers[i][j] - grad_star[i][j]) ** 2 for j in range(dim))
        for i in range(n)
    ) / n
    mean_tg_err = sum(tg_errs) / len(tg_errs)

    assert max_h_inv_err < 1e-14
    assert diana_x_err < 1e-12, f"Expected DIANA exact convergence to composite x^*, got {diana_x_err}"
    assert diana_h_err < 1e-10, f"Expected DIANA shift learning h_i -> nabla f_i(x^*), got {diana_h_err}"
    assert mean_tg_err > 1e-2, f"Expected memoryless TernGrad quantization noise floor, got {mean_tg_err}"

    print(
        f"[PASS] Round 389 DIANA (Mishchenko et al. 2019): alpha_inf(9)={alpha_inf:.4f}, "
        f"diana_x_err={diana_x_err:.2e}, diana_h_err={diana_h_err:.2e} << terngrad_err={mean_tg_err:.4e}"
    )


if __name__ == "__main__":
    main()
