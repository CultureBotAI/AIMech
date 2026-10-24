#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 411:
FedPD: Federated Primal-Dual Optimization with Adaptivity to Non-IID Data (Zhang et al. 2021).
"""

import math


def main() -> None:
    # 1. Claim 2.2 / Appendix D.2: FedAvg divergence on f_1(x) = 0.5*(x - 1)^2, f_2(x) = -0.5*(x - 1)^2
    # where global f(x) = 0.5*(f_1(x) + f_2(x)) = 0 (every x is globally stationary).
    # With Q = 2 local GD steps and constant step size eta = 0.25:
    # client 1 maps x -> 1 + (1 - eta)^Q (x - 1); client 2 maps x -> 1 + (1 + eta)^Q (x - 1).
    # Server average maps (x - 1) -> 0.5 * ((1 - eta)^2 + (1 + eta)^2) (x - 1) = (1 + eta^2) (x - 1).
    eta = 0.25
    Q = 2
    amp_factor = 0.5 * ((1.0 - eta) ** Q + (1.0 + eta) ** Q)
    assert abs(amp_factor - (1.0 + eta ** 2)) < 1e-12
    assert amp_factor > 1.0, "FedAvg amplification factor must exceed 1 for Q=2"

    x_fedavg = 2.0
    for _ in range(50):
        x1 = 1.0 + ((1.0 - eta) ** Q) * (x_fedavg - 1.0)
        x2 = 1.0 + ((1.0 + eta) ** Q) * (x_fedavg - 1.0)
        x_fedavg = 0.5 * (x1 + x2)
    assert abs(x_fedavg - 1.0) > 20.0, f"Expected FedAvg divergence, got x={x_fedavg}"

    # 2. Theorem 1: FedPD convergence for 0 < eta < (sqrt(5) - 1) / (4 L) on the exact same non-convex pair
    L = 1.0
    eta_max = (math.sqrt(5.0) - 1.0) / (4.0 * L)
    eta_pd = 0.25
    assert eta_pd < eta_max

    # Exact local augmented Lagrangian subproblem:
    # L_1(x_1) = 0.5*(x_1 - 1)^2 + lam_1*(x_1 - x_0) + (1/(2*eta))*(x_1 - x_0)^2
    #   => (1 + 1/eta)*x_1 = 1 - lam_1 + x_0/eta
    # L_2(x_2) = -0.5*(x_2 - 1)^2 + lam_2*(x_2 - x_0) + (1/(2*eta))*(x_2 - x_0)^2
    #   => (-1 + 1/eta)*x_2 = -1 - lam_2 + x_0/eta  (strongly convex since eta < 1)
    x0 = 2.0
    lam1, lam2 = 0.0, 0.0
    for _ in range(60):
        x1 = (1.0 - lam1 + x0 / eta_pd) / (1.0 + 1.0 / eta_pd)
        x2 = (-1.0 - lam2 + x0 / eta_pd) / (-1.0 + 1.0 / eta_pd)
        x0_next = 0.5 * ((x1 + eta_pd * lam1) + (x2 + eta_pd * lam2))
        lam1 = lam1 + (x1 - x0_next) / eta_pd
        lam2 = lam2 + (x2 - x0_next) / eta_pd
        x0 = x0_next

    consensus_gap = max(abs(x1 - x0), abs(x2 - x0))
    dual_stationarity = abs(0.5 * (lam1 + lam2))
    assert consensus_gap < 1e-12, f"Expected FedPD consensus, got {consensus_gap}"
    assert dual_stationarity < 1e-12, f"Expected dual sum zero, got {dual_stationarity}"
    assert abs(lam1 + (x0 - 1.0)) < 1e-12, "Expected lam1 = -grad f_1(x0)"
    print(
        f"[PASS] FedPD boundaries verified: FedAvg amp_factor={amp_factor:.4f} (x_50={x_fedavg:.2f}), "
        f"FedPD eta_max={eta_max:.4f}, consensus_gap={consensus_gap:.2e}, x0_final={x0:.6f}"
    )


if __name__ == "__main__":
    main()
