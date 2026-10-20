#!/usr/bin/env python3
"""Constructed boundary verification for Round 581: 5GCS (Grudzien, Malinovsky, Richtarik, AISTATS 2023)."""

from __future__ import annotations

import itertools
import math
import random


def main() -> None:
    # 1. Verify Definition 1, Equation (11): Exact Client Sampling Operator variance identity
    # E[||H^T (P(v) - v)||^2] = (M/C)((M-C)/(M-1)) sum_{m=1}^M ||v_m||^2 - ((M-C)/(C(M-1))) ||sum_{m=1}^M v_m||^2
    m_clients, c_cohort, d = 6, 2, 3
    v_vecs = [
        [1.0, -0.5, 0.2],
        [-0.3, 1.2, -0.4],
        [0.7, 0.1, -0.8],
        [-1.1, 0.4, 0.9],
        [0.5, -0.9, 0.3],
        [0.2, 0.6, -0.5],
    ]
    v_sum = [sum(v_vecs[m][j] for m in range(m_clients)) for j in range(d)]

    subsets = list(itertools.combinations(range(m_clients), c_cohort))
    emp_lhs = 0.0
    for s in subsets:
        ht_pv = [
            sum((m_clients / c_cohort) * v_vecs[m][j] for m in s)
            for j in range(d)
        ]
        emp_lhs += sum((ht_pv[j] - v_sum[j]) ** 2 for j in range(d))
    emp_lhs /= len(subsets)

    sum_norms_sq = sum(sum(x * x for x in vm) for vm in v_vecs)
    norm_sum_sq = sum(x * x for x in v_sum)
    rhs_eq11 = (
        (m_clients / c_cohort) * ((m_clients - c_cohort) / (m_clients - 1)) * sum_norms_sq
        - ((m_clients - c_cohort) / (c_cohort * (m_clients - 1))) * norm_sum_sq
    )
    assert abs(emp_lhs - rhs_eq11) < 1e-14, f"Eq. (11) mismatch: {emp_lhs} vs {rhs_eq11}"

    # 2. Verify Algorithm 1 (5GCS) under Client Sampling (C = 2 < M = 6) with heterogeneous quadratics
    # f_m(x) = 0.5 x^T A_m x - b_m^T x where each f_m is L-smooth and mu-strongly convex
    mu = 0.5
    L = 8.0
    lf = (L - mu) / m_clients
    a_diags = []
    b_vecs = []
    rng = random.Random(581)
    for m in range(m_clients):
        diag = [
            mu + (L - mu) * ((m + j) % d) / (d - 1)
            for j in range(d)
        ]
        a_diags.append(diag)
        b_vecs.append([rng.gauss(0.0, 2.5) for _ in range(d)])

    avg_diag = [sum(a_diags[m][j] for m in range(m_clients)) / m_clients for j in range(d)]
    avg_b = [sum(b_vecs[m][j] for m in range(m_clients)) / m_clients for j in range(d)]
    x_star = [avg_b[j] / avg_diag[j] for j in range(d)]

    # F_m(x) = (1/M)(f_m(x) - (mu/2)||x||^2), so nabla F_m(x) = (1/M)((A_m - mu I)x - b_m)
    def grad_fm_lifted(m: int, x: list[float]) -> list[float]:
        return [
            ((a_diags[m][j] - mu) * x[j] - b_vecs[m][j]) / m_clients
            for j in range(d)
        ]

    u_star = [grad_fm_lifted(m, x_star) for m in range(m_clients)]
    # Verify saddle-point optimality condition Eq. (14): 0 = mu x^* + sum_{m=1}^M u_m^*
    for j in range(d):
        assert abs(mu * x_star[j] + sum(u_star[m][j] for m in range(m_clients))) < 1e-14

    # Theorem 3.3 parameters
    gamma = (3.0 / 16.0) * math.sqrt(c_cohort / (L * mu * m_clients))
    tau = 1.0 / (2.0 * gamma * m_clients)
    k_local = math.ceil((0.75 * math.sqrt((c_cohort / m_clients) * (L / mu)) + 2.0) * math.log(4.0 * L / mu))
    step_local = 1.0 / (lf + tau)

    x_t = [0.0] * d
    u_t = [[0.0] * d for _ in range(m_clients)]
    v_t = [0.0] * d

    def lyapunov(x: list[float], u: list[list[float]]) -> float:
        tx = sum((x[j] - x_star[j]) ** 2 for j in range(d)) / gamma
        tu = (
            (m_clients / c_cohort)
            * (1.0 / tau + 1.0 / lf)
            * sum(
                sum((u[m][j] - u_star[m][j]) ** 2 for j in range(d))
                for m in range(m_clients)
            )
        )
        return tx + tu

    psi_0 = lyapunov(x_t, u_t)
    rounds = 900
    for _ in range(rounds):
        x_hat = [(x_t[j] - gamma * v_t[j]) / (1.0 + gamma * mu) for j in range(d)]
        cohort = rng.sample(range(m_clients), c_cohort)
        delta_v = [0.0] * d
        for m in cohort:
            # Local solver: K steps of GD on psi_m^t(y) = F_m(y) + (tau/2)||y - (x_hat + (1/tau)u_m^t)||^2
            y = list(x_hat)
            target = [x_hat[j] + u_t[m][j] / tau for j in range(d)]
            for _ in range(k_local):
                gf = grad_fm_lifted(m, y)
                g_psi = [gf[j] + tau * (y[j] - target[j]) for j in range(d)]
                y = [y[j] - step_local * g_psi[j] for j in range(d)]
            u_new = grad_fm_lifted(m, y)
            for j in range(d):
                delta_v[j] += u_new[j] - u_t[m][j]
            u_t[m] = u_new
        x_t = [x_hat[j] - gamma * (m_clients / c_cohort) * delta_v[j] for j in range(d)]
        v_t = [v_t[j] + delta_v[j] for j in range(d)]

    psi_T = lyapunov(x_t, u_t)
    rho = min(
        (gamma * mu) / (1.0 + gamma * mu),
        (c_cohort / m_clients) * (tau / (lf + tau)),
    )
    assert psi_T < 1e-12 * psi_0 and psi_T <= ((1.0 - rho) ** rounds) * psi_0

    print(
        f"[PASS] Round 581 5GCS verified: eq11_lhs={emp_lhs:.4f}=={rhs_eq11:.4f}, "
        f"K_local={k_local}, psi_0={psi_0:.3e} -> psi_T={psi_T:.3e}"
    )


if __name__ == "__main__":
    main()
