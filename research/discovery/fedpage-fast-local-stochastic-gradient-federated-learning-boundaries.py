#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 563: FedPAGE (Zhao, Li, & Richtarik, 2021)."""

import math
import random


def vec_add(u, v):
    return [a + b for a, b in zip(u, v)]


def vec_sub(u, v):
    return [a - b for a, b in zip(u, v)]


def vec_scale(u, c):
    return [c * a for a in u]


def sq_norm(u):
    return sum(a * a for a in u)


def main():
    rng = random.Random(20210810)
    N, S, M, K, d = 16, 4, 6, 4, 5
    L = 2.0
    p = S / N  # p = 0.25

    # 1. Verify expected communication cost per round and Theorem 4.2 / Theorem 5.2 step sizes
    expected_comm_clients = p * N + (1.0 - p) * S
    assert expected_comm_clients < 2.0 * S
    eta_g_ncvx = 1.0 / (L * (1.0 + math.sqrt(3.0 * (1.0 - p / 3.0) / (2.0 * p * S))))
    eta_l_ncvx = math.sqrt(2.0 * p) / (24.0 * math.sqrt(S) * K * L)
    assert eta_g_ncvx > 0.0 and eta_l_ncvx > 0.0

    # Verify geometric series bound used in Lemma D.1 proof (Page 25):
    # sum_{k=0}^{K-1} (1 + 1/(K-1) + 4 K L^2 eta_l^2)^k <= 3 K for K >= 2
    geom_base = 1.0 + 1.0 / (K - 1) + 4.0 * K * (L ** 2) * (eta_l_ncvx ** 2)
    geom_sum = sum(geom_base ** k for k in range(K))
    assert geom_sum <= 3.0 * K

    # 2. Construct heterogeneous finite-sum problem across N clients, each with M local samples
    client_opt = [[[0.8 * (i - 7.5) + 0.3 * (j - 2.5) + 0.2 * c for c in range(d)] for j in range(M)] for i in range(N)]
    x_star = [
        sum(client_opt[i][j][c] for i in range(N) for j in range(M)) / (N * M)
        for c in range(d)
    ]

    def grad_ij(i, j, x):
        return [L * (x[c] - client_opt[i][j][c]) for c in range(d)]

    def grad_i_full(i, x):
        return [sum(grad_ij(i, j, x)[c] for j in range(M)) / M for c in range(d)]

    def grad_global(x):
        return [L * (x[c] - x_star[c]) for c in range(d)]

    # Verify Lemma E.1 (Page 30): when K=1 and b1=b2=M, E_r[g^r - grad f(x^r)] = (1 - p)(g^{r-1} - grad f(x^{r-1}))
    x_prev = [1.5 - 0.2 * c for c in range(d)]
    x_curr = [1.1 + 0.1 * c for c in range(d)]
    g_prev = [0.5 * c for c in range(d)]
    # Exact expectation over q ~ Bernoulli(p) and uniform subset S^r of size S:
    # For q=1 (prob p): g^r = grad_global(x_curr)
    # For q=0 (prob 1-p): E_{S^r}[g^r] = grad_global(x_curr) - grad_global(x_prev) + g_prev
    expected_err = vec_scale(vec_sub(g_prev, grad_global(x_prev)), 1.0 - p)
    mc_trials = 4000
    acc_err = [0.0] * d
    for _ in range(mc_trials):
        if rng.random() < p:
            g_r = grad_global(x_curr)
        else:
            subset = rng.sample(range(N), S)
            g_r = [0.0] * d
            for i in subset:
                gi0 = vec_add(vec_sub(grad_i_full(i, x_curr), grad_i_full(i, x_prev)), g_prev)
                g_r = vec_add(g_r, vec_scale(gi0, 1.0 / S))
        err_r = vec_sub(g_r, grad_global(x_curr))
        acc_err = vec_add(acc_err, vec_scale(err_r, 1.0 / mc_trials))
    assert math.sqrt(sq_norm(vec_sub(acc_err, expected_err))) < 0.08

    # 3. Execute Algorithm 1 (FedPAGE with K=4, b1=b2=M, b3=1) vs FedAvg with local SGD
    x_fp = [3.0] * d
    x_fp_prev = x_fp[:]
    g_fp = grad_global(x_fp)
    eta_g_run = 0.25
    eta_l_run = 0.04

    for r in range(120):
        q = 1 if (r == 0 or rng.random() < p) else 0
        if q == 1:
            g_fp = grad_global(x_fp)
        else:
            subset = rng.sample(range(N), S)
            delta_sum = [0.0] * d
            for i in subset:
                y_prev = x_fp[:]
                gi_k = vec_add(vec_sub(grad_i_full(i, x_fp), grad_i_full(i, x_fp_prev)), g_fp)
                y_curr = vec_sub(y_prev, vec_scale(gi_k, eta_l_run))
                for _ in range(1, K):
                    j_idx = rng.randrange(M)
                    diff_ij = vec_sub(grad_ij(i, j_idx, y_curr), grad_ij(i, j_idx, y_prev))
                    gi_k = vec_add(diff_ij, gi_k)
                    y_prev = y_curr
                    y_curr = vec_sub(y_curr, vec_scale(gi_k, eta_l_run))
                delta_y_i = vec_sub(x_fp, y_curr)
                delta_sum = vec_add(delta_sum, delta_y_i)
            g_fp = vec_scale(delta_sum, 1.0 / (K * eta_l_run * S))
        x_fp_prev = x_fp[:]
        x_fp = vec_sub(x_fp, vec_scale(g_fp, eta_g_run))

    # Compare against FedAvg with same effective step size and minibatch sampling
    x_fa = [3.0] * d
    for _ in range(120):
        subset = rng.sample(range(N), S)
        delta_sum = [0.0] * d
        for i in subset:
            y_curr = x_fa[:]
            for _ in range(K):
                j_idx = rng.randrange(M)
                y_curr = vec_sub(y_curr, vec_scale(grad_ij(i, j_idx, y_curr), eta_l_run))
            delta_sum = vec_add(delta_sum, vec_sub(x_fa, y_curr))
        g_fa = vec_scale(delta_sum, 1.0 / (K * eta_l_run * S))
        x_fa = vec_sub(x_fa, vec_scale(g_fa, eta_g_run))

    grad_norm_fp = math.sqrt(sq_norm(grad_global(x_fp)))
    grad_norm_fa = math.sqrt(sq_norm(grad_global(x_fa)))
    assert grad_norm_fp < 1e-6
    assert grad_norm_fp < 0.01 * grad_norm_fa

    print(
        f"[PASS] Round 563 FedPAGE verified: geom_sum={geom_sum:.3f}<=3K={3*K}, "
        f"grad_fp={grad_norm_fp:.3e} << grad_fa={grad_norm_fa:.3e}"
    )


if __name__ == "__main__":
    main()
