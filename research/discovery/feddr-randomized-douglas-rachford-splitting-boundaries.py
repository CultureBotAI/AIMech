#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 482:
FedDR & asyncFedDR (FedDR – Randomized Douglas-Rachford Splitting Algorithms for Nonconvex
Federated Composite Optimization, Tran-Dinh, Pham, Phan, & Nguyen 2021, NeurIPS 2021, arXiv:2103.03452).

Verifies:
1. Nonconvex Douglas-Rachford (DR) envelope and stationary-point equivalence (Equation 3, Lemma 1, p. 4):
   For each client i with L_i-smooth f_i and proper closed g, the triad (x_bar^k, y_i^k, x_i^k) updated by:
   - y_i^{k+1} = y_i^k + alpha (x_bar^k - x_i^k)
   - x_i^{k+1} = prox_{eta f_i}(y_i^{k+1}) = argmin_x { f_i(x) + (1 / (2 eta)) ||x - y_i^{k+1}||^2 }
   - x_hat_i^{k+1} = 2 x_i^{k+1} - y_i^{k+1}
   - x_bar^{k+1} = prox_{eta g}( (1/n) sum_{i=1}^n x_hat_i^{k+1} )
   satisfies the exact reflection identity at consensus fixed points:
   when x_bar^* = x_i^* = x^* for all i (consensus stationary point of f + g),
   0 = x_i^* - y_i^* + eta nabla f_i(x^*) => y_i^* = x^* + eta nabla f_i(x^*) and x_hat_i^* = 2 x^* - y_i^* = x^* - eta nabla f_i(x^*),
   so (1/n) sum_{i=1}^n x_hat_i^* = x^* - eta nabla f(x^*) and x^* = prox_{eta g}(x^* - eta nabla f(x^*)),
   i.e., G_eta(x^*) = (1/eta)(x^* - prox_{eta g}(x^* - eta nabla f(x^*))) = 0 (exact zero gradient mapping,
   eliminating heterogeneous non-IID client drift where FedAvg/FedProx fail to reach G_eta(x^*) = 0).
2. Exact Step-Size / Relaxation Positivity Condition (Theorem 1, Equation 7, p. 6):
   2 (2 - alpha) - alpha eta L - (1 + 2 alpha) eta^2 L^2 > 0 for 0 < alpha < 2 and 0 < eta < eta_bar.
"""

from __future__ import annotations
import math


def soft_threshold(v: float, thresh: float) -> float:
    if v > thresh:
        return v - thresh
    if v < -thresh:
        return v + thresh
    return 0.0


def main() -> None:
    # 1. Verify Theorem 1 (Eq. 7) step-size upper bound positivity
    L = 2.0
    alpha = 1.0
    eta_max = (math.sqrt((alpha ** 2) + 8.0 * (2.0 - alpha) * (1.0 + 2.0 * alpha)) - alpha) / (
        2.0 * L * (1.0 + 2.0 * alpha)
    )
    eta = 0.5 * eta_max
    lhs_thm1 = 2.0 * (2.0 - alpha) - alpha * eta * L - (1.0 + 2.0 * alpha) * (eta ** 2) * (L ** 2)
    assert lhs_thm1 > 0.0, f"Theorem 1 condition violated: {lhs_thm1}"

    # 2. Verify exact convergence of FedDR to composite stationary point G_eta(x^*) = 0 on heterogeneous
    # composite problem min_x (1/n) sum_{i=1}^n (1/2) a_i (x - b_i)^2 + lam |x|
    # Here f_i(x) = 0.5 * a_i * (x - b_i)^2, g(x) = lam * |x|.
    a_list = [1.5, 2.0, 2.5]
    b_list = [-2.0, 0.5, 3.0]
    n = len(a_list)
    lam = 0.4

    # Analytical optimum of F(x) = (1/n) sum_i 0.5 a_i (x - b_i)^2 + lam |x|
    a_bar = sum(a_list) / n
    ab_bar = sum(a * b for a, b in zip(a_list, b_list)) / n
    x_star = soft_threshold(ab_bar, lam) / a_bar

    def grad_f(x: float) -> float:
        return sum(a * (x - b) for a, b in zip(a_list, b_list)) / n

    def grad_mapping_norm(x: float, step: float = 0.2) -> float:
        prox = soft_threshold(x - step * grad_f(x), step * lam)
        return abs((x - prox) / step)

    assert grad_mapping_norm(x_star) < 1e-15

    # Run FedDR (Algorithm 1 / Equation 3 with full participation S_k = [n], exact prox_{eta f_i})
    x_bar = 0.0
    x_i = [0.0] * n
    y_i = [0.0] * n
    x_hat_i = [0.0] * n
    eta_dr = 0.35
    alpha_dr = 1.2

    for _k in range(200):
        for i in range(n):
            y_i[i] = y_i[i] + alpha_dr * (x_bar - x_i[i])
            # prox_{eta f_i}(y_i): argmin_x { 0.5 a_i (x - b_i)^2 + (1/(2 eta)) (x - y_i)^2 }
            x_i[i] = (y_i[i] + eta_dr * a_list[i] * b_list[i]) / (1.0 + eta_dr * a_list[i])
            x_hat_i[i] = 2.0 * x_i[i] - y_i[i]
        x_hat_avg = sum(x_hat_i) / n
        x_bar = soft_threshold(x_hat_avg, eta_dr * lam)

    err_feddr = abs(x_bar - x_star)
    gm_feddr = grad_mapping_norm(x_bar)
    assert err_feddr < 1e-10 and gm_feddr < 1e-10, f"FedDR failed to reach composite optimum: {err_feddr}"

    print(
        f"[PASS] FedDR boundary verification passed: lhs_thm1={lhs_thm1:.4f} > 0, "
        f"|x_bar - x^*|={err_feddr:.3e}, ||G_eta(x_bar)||={gm_feddr:.3e}"
    )


if __name__ == "__main__":
    main()
