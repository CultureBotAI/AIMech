#!/usr/bin/env python3
"""Constructed boundary verification for Round 572: L-SVRG and L-Katyusha (Kovalev et al., ALT 2020)."""

from __future__ import annotations

import math
import random


def main() -> None:
    rng = random.Random(572)
    n, d = 12, 8
    # Construct n L-smooth, mu-strongly convex quadratic components f_i(x) = 0.5 x^T A_i x - b_i^T x
    # with distinct local minimizers so stochastic gradient variance at x^* is non-zero.
    mu = 0.2
    L = 4.0
    a_diags = []
    b_vecs = []
    for i in range(n):
        diag = [
            mu + (L - mu) * (j / (d - 1)) * (0.7 + 0.3 * ((i + j) % 2))
            for j in range(d)
        ]
        a_diags.append(diag)
        b_vecs.append([rng.gauss(0.0, 1.5) for _ in range(d)])

    # Exact minimizer x^* of f(x) = (1/n) sum_i f_i(x)
    avg_diag = [sum(a_diags[i][j] for i in range(n)) / n for j in range(d)]
    avg_b = [sum(b_vecs[i][j] for i in range(n)) / n for j in range(d)]
    x_star = [avg_b[j] / avg_diag[j] for j in range(d)]

    def f_i_grad(i: int, x: list[float]) -> list[float]:
        return [a_diags[i][j] * x[j] - b_vecs[i][j] for j in range(d)]

    def full_grad(x: list[float]) -> list[float]:
        return [avg_diag[j] * x[j] - avg_b[j] for j in range(d)]

    def f_val(x: list[float]) -> float:
        total = 0.0
        for i in range(n):
            for j in range(d):
                total += 0.5 * a_diags[i][j] * x[j] * x[j] - b_vecs[i][j] * x[j]
        return total / n

    f_star = f_val(x_star)
    grad_star_i = [f_i_grad(i, x_star) for i in range(n)]

    # 1. Verify Lemma 3.4 & Theorem 3.5 single-step conditional expectation inequality for L-SVRG:
    # E[Phi^{k+1} | x^k, w^k] <= (1 - eta * mu) ||x^k - x^*||^2 + (1 - p/2) D^k
    eta = 1.0 / (6.0 * L)
    p = 1.0 / n
    xk = [rng.uniform(-2.0, 2.0) for _ in range(d)]
    wk = [rng.uniform(-2.0, 2.0) for _ in range(d)]

    dist_xk_sq = sum((xk[j] - x_star[j]) ** 2 for j in range(d))
    dk_val = (4.0 * eta * eta / (p * n)) * sum(
        sum((f_i_grad(i, wk)[j] - grad_star_i[i][j]) ** 2 for j in range(d))
        for i in range(n)
    )
    fw_grad = full_grad(wk)
    exp_dist_next = 0.0
    for i in range(n):
        gi = [
            f_i_grad(i, xk)[j] - f_i_grad(i, wk)[j] + fw_grad[j]
            for j in range(d)
        ]
        x_next = [xk[j] - eta * gi[j] for j in range(d)]
        exp_dist_next += sum((x_next[j] - x_star[j]) ** 2 for j in range(d)) / n

    d_if_updated = (4.0 * eta * eta / (p * n)) * sum(
        sum((f_i_grad(i, xk)[j] - grad_star_i[i][j]) ** 2 for j in range(d))
        for i in range(n)
    )
    exp_d_next = (1.0 - p) * dk_val + p * d_if_updated
    exp_phi_next = exp_dist_next + exp_d_next
    rhs_bound = (1.0 - eta * mu) * dist_xk_sq + (1.0 - 0.5 * p) * dk_val
    assert exp_phi_next <= rhs_bound + 1e-12, (
        f"Lemma 3.4 violated: {exp_phi_next} > {rhs_bound}"
    )

    # 2. Run L-SVRG and L-Katyusha and verify linear convergence and acceleration
    # L-SVRG trajectory
    x_lsvrg = [0.0] * d
    w_lsvrg = [0.0] * d
    fw_lsvrg = full_grad(w_lsvrg)
    gw_i_lsvrg = [f_i_grad(i, w_lsvrg) for i in range(n)]
    steps = 1200
    for _ in range(steps):
        i = rng.randrange(n)
        gi = [
            f_i_grad(i, x_lsvrg)[j] - gw_i_lsvrg[i][j] + fw_lsvrg[j]
            for j in range(d)
        ]
        x_lsvrg = [x_lsvrg[j] - eta * gi[j] for j in range(d)]
        if rng.random() < p:
            w_lsvrg = list(x_lsvrg)
            fw_lsvrg = full_grad(w_lsvrg)
            gw_i_lsvrg = [f_i_grad(idx, w_lsvrg) for idx in range(n)]

    err_lsvrg = sum((x_lsvrg[j] - x_star[j]) ** 2 for j in range(d))

    # L-Katyusha trajectory (Algorithm 2, Theorem 4.6)
    sigma = mu / L
    theta1 = min(math.sqrt(2.0 * sigma * n / 3.0), 0.5)
    theta2 = 0.5
    eta_kat = theta2 / ((1.0 + theta2) * theta1)
    theta_rate = min(sigma / (6.0 * theta1), theta1 / (2.0 * n))
    assert 0.0 < theta_rate < 1.0

    yk = [0.0] * d
    zk = [0.0] * d
    wk_kat = [0.0] * d
    fw_kat = full_grad(wk_kat)
    gw_i_kat = [f_i_grad(i, wk_kat) for i in range(n)]

    def psi_kat(y_v: list[float], z_v: list[float], w_v: list[float]) -> float:
        z_term = (
            (L * (1.0 + eta_kat * sigma) / (2.0 * eta_kat))
            * sum((z_v[j] - x_star[j]) ** 2 for j in range(d))
        )
        y_term = max(0.0, f_val(y_v) - f_star) / theta1
        w_term = (theta2 * (1.0 + theta1) / (p * theta1)) * max(
            0.0, f_val(w_v) - f_star
        )
        return z_term + y_term + w_term

    psi_0 = psi_kat(yk, zk, wk_kat)
    for _ in range(steps):
        xk_kat = [
            theta1 * zk[j] + theta2 * wk_kat[j] + (1.0 - theta1 - theta2) * yk[j]
            for j in range(d)
        ]
        i = rng.randrange(n)
        gi = [
            f_i_grad(i, xk_kat)[j] - gw_i_kat[i][j] + fw_kat[j]
            for j in range(d)
        ]
        z_next = [
            (eta_kat * sigma * xk_kat[j] + zk[j] - (eta_kat / L) * gi[j])
            / (1.0 + eta_kat * sigma)
            for j in range(d)
        ]
        y_next = [xk_kat[j] + theta1 * (z_next[j] - zk[j]) for j in range(d)]
        if rng.random() < p:
            wk_kat = list(yk)
            fw_kat = full_grad(wk_kat)
            gw_i_kat = [f_i_grad(idx, wk_kat) for idx in range(n)]
        zk = z_next
        yk = y_next

    psi_final = psi_kat(yk, zk, wk_kat)
    err_lkat = sum((yk[j] - x_star[j]) ** 2 for j in range(d))
    assert err_lsvrg < 1e-6, f"L-SVRG failed to converge: {err_lsvrg}"
    assert err_lkat < err_lsvrg and psi_final < 1e-10 * psi_0, (
        f"L-Katyusha failed to accelerate: err_lkat={err_lkat}, err_lsvrg={err_lsvrg}"
    )

    print(
        f"[PASS] Round 572 L-SVRG & L-Katyusha verified: "
        f"E[Phi_1]={exp_phi_next:.4f}<=rhs={rhs_bound:.4f}, "
        f"err_lsvrg={err_lsvrg:.3e}, err_lkat={err_lkat:.3e}, psi_ratio={psi_final/psi_0:.3e}"
    )


if __name__ == "__main__":
    main()
