#!/usr/bin/env python3
"""Constructed boundary verification for Round 575: Unified (A,B,C,D1,D2,rho) Theory of SGD (Gorbunov et al., AISTATS 2020)."""

from __future__ import annotations

import random


def main() -> None:
    rng = random.Random(575)
    n, d = 10, 6
    mu = 0.5
    L = 3.5
    # Construct n L-smooth, mu-strongly convex quadratic functions f_i(x) = 0.5 x^T A_i x - b_i^T x
    a_diags = []
    b_vecs = []
    for i in range(n):
        diag = [
            mu + (L - mu) * ((j + i) % d) / (d - 1)
            for j in range(d)
        ]
        a_diags.append(diag)
        b_vecs.append([rng.gauss(0.0, 1.5) for _ in range(d)])

    avg_diag = [sum(a_diags[i][j] for i in range(n)) / n for j in range(d)]
    avg_b = [sum(b_vecs[i][j] for i in range(n)) / n for j in range(d)]
    x_star = [avg_b[j] / avg_diag[j] for j in range(d)]

    def grad_i(i: int, x: list[float]) -> list[float]:
        return [a_diags[i][j] * x[j] - b_vecs[i][j] for j in range(d)]

    grad_star_i = [grad_i(i, x_star) for i in range(n)]
    sigma_sq_opt = (
        sum(sum(v * v for v in grad_star_i[i]) for i in range(n)) / n
    )
    assert sigma_sq_opt > 0.5

    # Verify Theorem 4.1 & Table 2 dichotomy:
    # 1. SGD-star (Algorithm 4: A=2L, B=0, rho=1, C=0, D1=0, D2=0) -> exact linear convergence
    # 2. tau-L-SVRG interpolation (Algorithm 16, Example A.1):
    #    g^k = tau * g_SGD^k + (1 - tau) * g_{L-SVRG}^k -> oscillation radius proportional to tau^2 * sigma^2
    gamma = 1.0 / (6.0 * L)
    p = 1.0 / n
    steps = 1200

    # Run SGD-star (tau=0 limit with exact optimal shifts)
    x_star_alg = [0.0] * d
    for _ in range(steps):
        i = rng.randrange(n)
        gi = [grad_i(i, x_star_alg)[j] - grad_star_i[i][j] for j in range(d)]
        x_star_alg = [x_star_alg[j] - gamma * gi[j] for j in range(d)]
    err_sgd_star = sum((x_star_alg[j] - x_star[j]) ** 2 for j in range(d))

    # Run tau-L-SVRG (Algorithm 16) for tau in {0.0, 0.25, 1.0}
    tau_errors = {}
    for tau in (0.0, 0.25, 1.0):
        rng_tau = random.Random(5750 + int(tau * 100))
        xk = [0.0] * d
        wk = [0.0] * d
        gw_i = [grad_i(i, wk) for i in range(n)]
        fw = [
            sum(gw_i[i][j] for i in range(n)) / n for j in range(d)
        ]
        tail_errs = []
        for step in range(steps):
            i = rng_tau.randrange(n)
            j_idx = rng_tau.randrange(n)
            g_lsvrg = [
                grad_i(i, xk)[c] - gw_i[i][c] + fw[c] for c in range(d)
            ]
            g_sgd = grad_i(j_idx, xk)
            gk = [
                tau * g_sgd[c] + (1.0 - tau) * g_lsvrg[c] for c in range(d)
            ]
            xk = [xk[c] - gamma * gk[c] for c in range(d)]
            if rng_tau.random() < p:
                wk = list(xk)
                gw_i = [grad_i(idx, wk) for idx in range(n)]
                fw = [
                    sum(gw_i[idx][c] for idx in range(n)) / n
                    for c in range(d)
                ]
            if step >= steps - 200:
                tail_errs.append(
                    sum((xk[c] - x_star[c]) ** 2 for c in range(d))
                )
        tau_errors[tau] = sum(tail_errs) / len(tail_errs)

    assert err_sgd_star < 1e-12, f"SGD-star failed to converge to x^*: {err_sgd_star}"
    assert tau_errors[0.0] < 1e-7 < tau_errors[0.25] < tau_errors[1.0], (
        f"tau-L-SVRG oscillation ordering violated: {tau_errors}"
    )

    print(
        f"[PASS] Round 575 Unified SGD verified: err_sgd_star={err_sgd_star:.3e}, "
        f"tau_errs=(0.0:{tau_errors[0.0]:.3e}, 0.25:{tau_errors[0.25]:.3e}, 1.0:{tau_errors[1.0]:.3e})"
    )


if __name__ == "__main__":
    main()
