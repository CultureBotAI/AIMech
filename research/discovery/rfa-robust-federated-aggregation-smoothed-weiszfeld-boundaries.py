#!/usr/bin/env python3
"""Constructed boundary verification for RFA Robust Federated Aggregation via Smoothed Weiszfeld
Geometric Median (Pillutla, Kakade, & Harchaoui 2022, IEEE TSP 70:1142-1154, arXiv:1912.13445).

Verifies:
1. Algorithm 2 (Smoothed Weiszfeld iteration, Section IV, p. 1145) & Proposition 2:
   Alternating minimization of the jointly convex surrogate
   G(v, eta) = (1/2) sum_{i=1}^m alpha_i (||v - w_i||_2^2 / eta_i + eta_i) over eta_i >= nu
   yields beta_i^{(r)} = alpha_i / max(nu, ||v^{(r)} - w_i||_2) and
   v^{(r+1)} = (sum_i beta_i^{(r)} w_i) / (sum_i beta_i^{(r)}), monotonically decreasing the
   smoothed geometric median objective g_nu(v) = min_{eta >= nu} G(v, eta).
2. Proposition 3 (Effective weight privacy bound, Section IV, p. 1145):
   When ||v^{(r)} - w_j||_2 <= B and alpha_i = 1/m, the normalized weight of any client i is
   bounded by beta_i^{(r)} / sum_j beta_j^{(r)} <= (1 + (m - 1) * nu / B)^{-1}.
3. Robustness up to corruption fraction rho < 1/2 where standard weighted mean fails.
"""

from __future__ import annotations

import json
import math
import random


def l2_dist(a: list[float], b: list[float]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def g_nu(v: list[float], points: list[list[float]], alphas: list[float], nu: float) -> float:
    total = 0.0
    for w_i, a_i in zip(points, alphas):
        dist = l2_dist(v, w_i)
        eta_i = max(nu, dist)
        total += 0.5 * a_i * ((dist**2) / eta_i + eta_i)
    return total


def smoothed_weiszfeld(
    points: list[list[float]],
    alphas: list[float],
    nu: float,
    rounds: int,
) -> tuple[list[float], list[float], float]:
    m = len(points)
    d = len(points[0])
    v = [0.0] * d
    obj_trace = [g_nu(v, points, alphas, nu)]
    max_norm_weight = 0.0
    max_radius = 0.0

    for _ in range(rounds):
        dists = [l2_dist(v, w_i) for w_i in points]
        max_radius = max(max_radius, max(dists))
        betas = [a_i / max(nu, dist) for a_i, dist in zip(alphas, dists)]
        beta_sum = sum(betas)
        norm_weights = [b / beta_sum for b in betas]
        max_norm_weight = max(max_norm_weight, max(norm_weights))
        v = [sum(norm_weights[i] * points[i][k] for i in range(m)) for k in range(d)]
        obj_trace.append(g_nu(v, points, alphas, nu))

    return v, obj_trace, max_norm_weight


def main() -> None:
    rng = random.Random(2022)
    m = 15
    f = 6  # rho = 6/15 = 0.40 < 0.50
    d = 5
    nu = 0.05
    alphas = [1.0 / m] * m
    true_center = [1.0, -0.5, 0.25, -0.75, 0.5]

    honest = [
        [true_center[k] + rng.gauss(0.0, 0.04) for k in range(d)]
        for _ in range(m - f)
    ]
    corrupted = [
        [-40.0 * true_center[k] + 25.0 for k in range(d)]
        for _ in range(f)
    ]
    points = honest + corrupted

    # 1. Run R = 8 smoothed Weiszfeld rounds
    v_rfa, obj_trace, max_w = smoothed_weiszfeld(points, alphas, nu=nu, rounds=8)

    # Verify monotonic decrease of smoothed geometric median surrogate objective g_nu(v)
    for r in range(len(obj_trace) - 1):
        assert obj_trace[r + 1] <= obj_trace[r] + 1e-12

    # 2. Verify Proposition 3 privacy bound on round 0 around v^{(0)} = 0
    b_bound = max(l2_dist([0.0] * d, w_i) for w_i in points)
    betas_0 = [(1.0 / m) / max(nu, l2_dist([0.0] * d, w_i)) for w_i in points]
    norm_w0 = max(betas_0) / sum(betas_0)
    prop3_upper = 1.0 / (1.0 + (m - 1) * (nu / m) / (b_bound / m))
    assert norm_w0 <= prop3_upper + 1e-12

    # 3. Compare estimation error vs FedAvg linear average
    v_avg = [sum(p[k] for p in points) / m for k in range(d)]
    err_rfa = l2_dist(v_rfa, true_center)
    err_avg = l2_dist(v_avg, true_center)
    assert err_rfa < 0.20
    assert err_avg > 20.0

    summary = {
        "concept": "AIMech:RfaRobustFederatedAggregationSmoothedWeiszfeldGeometricMedian",
        "m_clients": m,
        "rho_corruption": round(f / m, 4),
        "nu_smoothing": nu,
        "g_nu_initial": round(obj_trace[0], 6),
        "g_nu_final": round(obj_trace[-1], 6),
        "round0_max_normalized_weight": round(norm_w0, 6),
        "proposition3_upper_bound": round(prop3_upper, 6),
        "l2_error_rfa": round(err_rfa, 6),
        "l2_error_fedavg": round(err_avg, 6),
        "status": "VERIFIED",
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
