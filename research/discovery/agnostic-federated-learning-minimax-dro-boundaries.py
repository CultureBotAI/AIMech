#!/usr/bin/env python3
"""Constructed boundary verification for Agnostic Federated Learning (AFL).

Verifies:
1. Proposition 1 (Mohri, Sivek, & Suresh 2019, Section 3.1, p. 3):
   For two client distributions D_1(x, 1) = 1, D_1(x, 0) = 0 and D_2(x, 1) = 1/2, D_2(x, 0) = 1/2
   with equal sample sizes m_1 = m_2, the uniform-mixture minimizer assigns p_1 = 3/4 (h_U(x) = 3/4)
   and incurs agnostic cross-entropy loss max_k L_{D_k}(h_U) = L_{D_2}(3/4) = -(1/2) log(3/16)
   = log(2) + (1/2) log(4/3), whereas the Agnostic Federated Learning minimax predictor assigns
   p_1^* = 1/2 (h_{D_Lambda}(x) = 1/2), equalizing domain losses L_{D_1}(1/2) = L_{D_2}(1/2) = log(2)
   and yielding an exact constant excess agnostic risk of (1/2) log(4/3) > 0 even as m_k -> infinity.
2. Section 4 Weighted Rademacher skewness (Eq. 4, p. 4):
   s(Lambda || m_bar) = 1 + max_{lambda in Lambda} chi^2(lambda || m_bar) = max_{lambda in Lambda} sum_{k=1}^p lambda_k^2 / m_bar_k.
3. Section 5 Stochastic-AFL minimax projection step (Figure 3, p. 5) onto the probability simplex Delta_p.
"""

from __future__ import annotations

import json
import math


def cross_entropy_d1(p1: float) -> float:
    return -math.log(p1)


def cross_entropy_d2(p1: float) -> float:
    return -0.5 * math.log(p1) - 0.5 * math.log(1.0 - p1)


def project_simplex(v: list[float]) -> list[float]:
    u = sorted(v, reverse=True)
    cssv = 0.0
    rho = 0
    for i, val in enumerate(u):
        cssv += val
        if val + (1.0 - cssv) / (i + 1) > 0.0:
            rho = i + 1
    theta = (sum(u[:rho]) - 1.0) / rho
    return [max(x - theta, 0.0) for x in v]


def main() -> None:
    # 1. Proposition 1 exact analytical verification (Section 3.1, p. 3)
    h_u = 0.75
    h_afl = 0.50

    loss_u_d1 = cross_entropy_d1(h_u)
    loss_u_d2 = cross_entropy_d2(h_u)
    agnostic_loss_u = max(loss_u_d1, loss_u_d2)

    loss_afl_d1 = cross_entropy_d1(h_afl)
    loss_afl_d2 = cross_entropy_d2(h_afl)
    agnostic_loss_afl = max(loss_afl_d1, loss_afl_d2)

    theoretical_gap = 0.5 * math.log(4.0 / 3.0)
    empirical_gap = agnostic_loss_u - agnostic_loss_afl

    assert abs(loss_afl_d1 - math.log(2.0)) < 1e-12
    assert abs(loss_afl_d2 - math.log(2.0)) < 1e-12
    assert abs(loss_afl_d1 - loss_afl_d2) < 1e-12
    assert abs(empirical_gap - theoretical_gap) < 1e-12

    # 2. Skewness s(Delta_2 || m_bar) for m_bar = (0.5, 0.5)
    m_bar = [0.5, 0.5]
    skewness_full_simplex = max(1.0 / m_bar[0], 1.0 / m_bar[1])
    assert abs(skewness_full_simplex - 2.0) < 1e-12

    # 3. Deterministic AFL minimax gradient descent-ascent on L(w, lambda) = lambda_1 L_1(w) + lambda_2 L_2(w)
    # Parameterize p_1 = sigmoid(w) so L_1(w) = log(1 + exp(-w)), L_2(w) = 0.5*log(1 + exp(-w)) + 0.5*log(1 + exp(w))
    # Since L_2(w) >= L_1(w) for all w >= 0 and L_2'(0) = 0, the saddle point is w^* = 0 (p_1^* = 0.5), lambda^* = (0, 1)
    w = 1.0  # start at uniform-mixture logit log(3) > 0
    lam = [0.5, 0.5]
    w_sum = 0.0
    lam_sum = [0.0, 0.0]
    steps = 3000
    gamma_w = 0.08
    gamma_lam = 0.08
    for _ in range(steps):
        p = 1.0 / (1.0 + math.exp(-w))
        l1 = -math.log(p)
        l2 = -0.5 * math.log(p) - 0.5 * math.log(1.0 - p)
        grad_w = lam[0] * (p - 1.0) + lam[1] * (p - 0.5)
        w = w - gamma_w * grad_w
        lam = project_simplex([lam[0] + gamma_lam * l1, lam[1] + gamma_lam * l2])
        w_sum += w
        lam_sum[0] += lam[0]
        lam_sum[1] += lam[1]

    w_bar = w_sum / steps
    p_bar = 1.0 / (1.0 + math.exp(-w_bar))
    lam_bar = [lam_sum[0] / steps, lam_sum[1] / steps]

    assert abs(p_bar - h_afl) < 1e-2
    assert lam_bar[1] > 0.98

    summary = {
        "concept": "AIMech:AgnosticFederatedLearningMinimaxDistributionallyRobustOptimization",
        "h_uniform": h_u,
        "h_afl_closed_form": h_afl,
        "h_afl_minimax_sgd": round(p_bar, 6),
        "saddle_lambda_sgd": [round(lam_bar[0], 6), round(lam_bar[1], 6)],
        "agnostic_loss_uniform": round(agnostic_loss_u, 6),
        "agnostic_loss_afl": round(agnostic_loss_afl, 6),
        "proposition1_gap_half_log_4_3": round(empirical_gap, 6),
        "skewness_full_simplex": skewness_full_simplex,
        "status": "VERIFIED",
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
