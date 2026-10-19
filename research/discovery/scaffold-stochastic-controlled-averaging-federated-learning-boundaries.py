#!/usr/bin/env python3
"""Constructed boundary & mathematical verification for Round 384:
AIMech:ScaffoldStochasticControlledAveragingForFederatedLearning
(Karimireddy, Kale, Mohri, Reddi, Stich, & Suresh 2020, ICML 2020, PMLR 119:5132-5143, arXiv:1910.06378).

Verifies:
1. Theorem II Client-Drift Fixed-Point Bias of FedAvg under Heterogeneous Clients:
   Consider N=2 deterministic heterogeneous quadratics f_1(x) = 0.5 * lambda_1 * (x - b_1)^2
   and f_2(x) = 0.5 * lambda_2 * (x - b_2)^2 with lambda_1 != lambda_2 and b_1 != b_2.
   The global minimizer of f(x) = 0.5*(f_1(x) + f_2(x)) is x* = (lambda_1*b_1 + lambda_2*b_2)/(lambda_1 + lambda_2).
   However, for any K >= 2 local steps with constant local step size eta_l > 0, FedAvg started AT x*
   drifts away from x* in a single round and converges to a strictly biased fixed point x_FedAvg != x*
   whose error scales as Omega(eta_l * (K - 1) * G).
2. Algorithm 1 (SCAFFOLD) Exact Fixed-Point Preservation & Client-Drift Elimination (Theorem III):
   With local control variates c_i and server control variate c = (1/N) sum_{i=1}^N c_i:
   (a) At (x = x*, c_i = grad f_i(x*)), the corrected local gradient g_i(y_i) - c_i + c vanishes identically
       at y_i = x* for all k = 1..K, making x* an exact fixed point for ANY K >= 1 and ANY heterogeneity G,
   (b) Both Option I (c_i^+ = grad f_i(x)) and Option II (c_i^+ = c_i - c + (1/(K*eta_l))*(x - y_i))
       maintain c == (1/N) sum_i c_i and converge linearly to x* without client drift.
"""

from __future__ import annotations
import math


def test_fedavg_client_drift_vs_scaffold_exact_convergence() -> None:
    # Two clients with different curvatures and optima:
    # f_1(x) = 0.5 * 1.0 * (x - 4.0)^2 -> grad f_1(x) = 1.0 * (x - 4.0)
    # f_2(x) = 0.5 * 3.0 * (x + 2.0)^2 -> grad f_2(x) = 3.0 * (x + 2.0)
    # Global objective f(x) = 0.5 * (f_1(x) + f_2(x)) has gradient:
    # grad f(x) = 0.5 * ((x - 4.0) + 3.0*(x + 2.0)) = 2.0 * x + 1.0 => x* = -0.5!
    lam = [1.0, 3.0]
    b = [4.0, -2.0]
    x_star = (lam[0] * b[0] + lam[1] * b[1]) / (lam[0] + lam[1])
    assert abs(x_star - (-0.5)) < 1e-12

    def grad_i(i: int, x: float) -> float:
        return lam[i] * (x - b[i])

    K = 8
    eta_l = 0.08
    eta_g = 1.0

    # 1. Verify FedAvg started AT x_star immediately drifts away when K >= 2:
    y_fed_from_star = []
    for i in range(2):
        yi = x_star
        for _ in range(K):
            yi = yi - eta_l * grad_i(i, yi)
        y_fed_from_star.append(yi)
    x_fed_after_1 = 0.5 * (y_fed_from_star[0] + y_fed_from_star[1])
    assert abs(x_fed_after_1 - x_star) > 0.15, (
        f"Expected FedAvg to drift away from x*={x_star}, got {x_fed_after_1}"
    )

    # 2. Verify SCAFFOLD at (x*, c_i = grad_i(x*)) is an exact fixed point for all K:
    c_star = [grad_i(0, x_star), grad_i(1, x_star)]
    c_server_star = 0.5 * (c_star[0] + c_star[1])
    assert abs(c_server_star) < 1e-12
    for i in range(2):
        yi = x_star
        for _ in range(K):
            yi = yi - eta_l * (grad_i(i, yi) - c_star[i] + c_server_star)
        assert abs(yi - x_star) < 1e-14

    # 3. Run FedAvg, SCAFFOLD Option I, and SCAFFOLD Option II from x_0 = 2.0 for R = 80 rounds:
    x_fed = 2.0
    x_scaf1 = 2.0
    c_scaf1 = [0.0, 0.0]
    c_srv1 = 0.0

    x_scaf2 = 2.0
    c_scaf2 = [0.0, 0.0]
    c_srv2 = 0.0

    for _ in range(80):
        # FedAvg round
        y_f = []
        for i in range(2):
            yi = x_fed
            for _ in range(K):
                yi -= eta_l * grad_i(i, yi)
            y_f.append(yi)
        x_fed = x_fed + eta_g * (0.5 * sum(yi - x_fed for yi in y_f))

        # SCAFFOLD Option I round
        y_s1 = []
        c_new1 = []
        for i in range(2):
            yi = x_scaf1
            for _ in range(K):
                yi -= eta_l * (grad_i(i, yi) - c_scaf1[i] + c_srv1)
            y_s1.append(yi)
            c_new1.append(grad_i(i, x_scaf1))
        x_scaf1 = x_scaf1 + eta_g * (0.5 * sum(yi - x_scaf1 for yi in y_s1))
        c_srv1 = c_srv1 + 0.5 * sum(c_new1[i] - c_scaf1[i] for i in range(2))
        c_scaf1 = c_new1
        assert abs(c_srv1 - 0.5 * sum(c_scaf1)) < 1e-12

        # SCAFFOLD Option II round (reuses local trajectories with zero extra gradient evaluations)
        y_s2 = []
        c_new2 = []
        for i in range(2):
            yi = x_scaf2
            for _ in range(K):
                yi -= eta_l * (grad_i(i, yi) - c_scaf2[i] + c_srv2)
            y_s2.append(yi)
            ci_plus = c_scaf2[i] - c_srv2 + (x_scaf2 - yi) / (K * eta_l)
            c_new2.append(ci_plus)
        x_scaf2 = x_scaf2 + eta_g * (0.5 * sum(yi - x_scaf2 for yi in y_s2))
        c_srv2 = c_srv2 + 0.5 * sum(c_new2[i] - c_scaf2[i] for i in range(2))
        c_scaf2 = c_new2
        assert abs(c_srv2 - 0.5 * sum(c_scaf2)) < 1e-12

    err_fed = abs(x_fed - x_star)
    err_scaf1 = abs(x_scaf1 - x_star)
    err_scaf2 = abs(x_scaf2 - x_star)

    assert err_fed > 0.35, f"Expected FedAvg asymptotic client-drift bias > 0.35, got {err_fed}"
    assert err_scaf1 < 1e-10, f"Expected SCAFFOLD Option I error < 1e-10, got {err_scaf1}"
    assert err_scaf2 < 1e-10, f"Expected SCAFFOLD Option II error < 1e-10, got {err_scaf2}"


if __name__ == "__main__":
    test_fedavg_client_drift_vs_scaffold_exact_convergence()
    print("[PASS] Round 384 SCAFFOLD Stochastic Controlled Averaging boundaries verified.")
