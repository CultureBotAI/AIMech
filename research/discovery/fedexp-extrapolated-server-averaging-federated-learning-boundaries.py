#!/usr/bin/env python3
"""Constructed boundary verification for Round 446:
FedExP: Speeding Up Federated Averaging via Extrapolation
(Divyansh Jhunjhunwala, Shiqiang Wang, & Gauri Joshi, ICLR 2023, arXiv:2301.09604).

Verifies:
1. Lemma 1 (Section 3, p. 4): In the overparameterized convex setting where client functions
   F_i(w) = 0.5 * ||A_i (w - w*)||^2 share a common global minimizer w*, multi-step local
   gradient descent with step size eta_l <= 1/L produces pseudo-gradients
   Delta_i^(t) = w^(t) - w_i^(t, tau) that satisfy the quasi-projection property
   <Delta_i^(t), w^(t) - w*> >= 0.5 * ||Delta_i^(t)||^2.
2. Adaptive POCS extrapolation step size (Eqs. 5-6, Algorithm 1):
   eta_g^(t) = max(1, sum_i ||Delta_i^(t)||^2 / (2 * M * (||bar_Delta^(t)||^2 + eps))) > 1
   strictly contracts ||w^(t+1) - w*||^2 by at least (sum_i ||Delta_i^(t)||^2)^2 / (4 M^2 ||bar_Delta^(t)||^2)
   when eps = 0, converging orders of magnitude faster than standard FedAvg (eta_g = 1).
"""

from __future__ import annotations
import math
import random


def dot(u: list[float], v: list[float]) -> float:
    return sum(x * y for x, y in zip(u, v))


def sqnorm(u: list[float]) -> float:
    return dot(u, u)


def sub(u: list[float], v: list[float]) -> list[float]:
    return [x - y for x, y in zip(u, v)]


def add_scaled(u: list[float], v: list[float], alpha: float) -> list[float]:
    return [x + alpha * y for x, y in zip(u, v)]


def matvec(h_mat: list[list[float]], v: list[float]) -> list[float]:
    return [dot(row, v) for row in h_mat]


def main() -> None:
    rng = random.Random(20230109)
    d = 12
    m_clients = 10
    rank_per_client = 3
    w_star = [rng.uniform(-2.0, 2.0) for _ in range(d)]

    # Each client i has rank-3 positive semidefinite Hessian H_i with max eigenvalue <= L = 2.0
    l_smooth = 2.0
    hessians: list[list[list[float]]] = []
    for _ in range(m_clients):
        h_i = [[0.0] * d for _ in range(d)]
        for _ in range(rank_per_client):
            u = [rng.gauss(0.0, 1.0) for _ in range(d)]
            nrm = math.sqrt(sqnorm(u))
            u = [x / nrm for x in u]
            eig = rng.uniform(0.3, l_smooth / rank_per_client)
            for r in range(d):
                for c in range(d):
                    h_i[r][c] += eig * u[r] * u[c]
        hessians.append(h_i)

    eta_l = 0.45 / l_smooth  # strictly <= 1/L
    tau = 5
    rounds = 45

    w_fedexp = [0.0] * d
    w_fedavg = [0.0] * d

    min_quasi_proj_margin = float("inf")
    max_pocs_bound_violation = 0.0
    eta_g_values: list[float] = []

    for _ in range(rounds):
        deltas_exp: list[list[float]] = []
        for i in range(m_clients):
            w_loc = list(w_fedexp)
            for _ in range(tau):
                grad = matvec(hessians[i], sub(w_loc, w_star))
                w_loc = add_scaled(w_loc, grad, -eta_l)
            delta_i = sub(w_fedexp, w_loc)
            deltas_exp.append(delta_i)
            # Check Lemma 1: <delta_i, w_fedexp - w_star> >= 0.5 * ||delta_i||^2
            lhs = dot(delta_i, sub(w_fedexp, w_star))
            rhs = 0.5 * sqnorm(delta_i)
            min_quasi_proj_margin = min(min_quasi_proj_margin, lhs - rhs)

        bar_delta = [sum(deltas_exp[i][j] for i in range(m_clients)) / m_clients for j in range(d)]
        mean_sq_norms = sum(sqnorm(deltas_exp[i]) for i in range(m_clients)) / m_clients
        bar_sq = sqnorm(bar_delta)
        eta_g = max(1.0, mean_sq_norms / (2.0 * (bar_sq + 1e-15)))
        eta_g_values.append(eta_g)

        dist_before = sqnorm(sub(w_fedexp, w_star))
        w_fedexp = add_scaled(w_fedexp, bar_delta, -eta_g)
        dist_after = sqnorm(sub(w_fedexp, w_star))
        # Exact POCS distance reduction bound: dist_after <= dist_before - mean_sq_norms^2 / (4 * bar_sq)
        if eta_g > 1.0:
            rhs_bound = dist_before - (mean_sq_norms ** 2) / (4.0 * bar_sq)
            max_pocs_bound_violation = max(max_pocs_bound_violation, dist_after - rhs_bound)

        # Standard FedAvg (eta_g = 1.0)
        deltas_avg: list[list[float]] = []
        for i in range(m_clients):
            w_loc = list(w_fedavg)
            for _ in range(tau):
                grad = matvec(hessians[i], sub(w_loc, w_star))
                w_loc = add_scaled(w_loc, grad, -eta_l)
            deltas_avg.append(sub(w_fedavg, w_loc))
        bar_delta_avg = [sum(deltas_avg[i][j] for i in range(m_clients)) / m_clients for j in range(d)]
        w_fedavg = add_scaled(w_fedavg, bar_delta_avg, -1.0)

    err_fedexp = math.sqrt(sqnorm(sub(w_fedexp, w_star)))
    err_fedavg = math.sqrt(sqnorm(sub(w_fedavg, w_star)))
    mean_eta_g = sum(eta_g_values) / len(eta_g_values)

    assert min_quasi_proj_margin >= -1e-12, f"Lemma 1 violated: {min_quasi_proj_margin}"
    assert max_pocs_bound_violation <= 1e-10, f"POCS contraction violated: {max_pocs_bound_violation}"
    assert mean_eta_g > 1.8, f"Expected extrapolated eta_g > 1.8, got {mean_eta_g}"
    assert err_fedexp < 0.05 * err_fedavg, f"Expected FedExP << FedAvg error, got {err_fedexp} vs {err_fedavg}"

    print(
        f"[PASS] Round 446 FedExP (Jhunjhunwala et al. 2023): "
        f"Lemma1_margin={min_quasi_proj_margin:.2e}>=0, mean_eta_g={mean_eta_g:.3f}, "
        f"err_fedexp={err_fedexp:.4e} << err_fedavg={err_fedavg:.4e}"
    )


if __name__ == "__main__":
    main()
