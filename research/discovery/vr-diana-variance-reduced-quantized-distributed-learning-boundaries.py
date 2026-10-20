#!/usr/bin/env python3
"""Constructed boundary verification for Round 573: VR-DIANA (Horvath et al., 2019/2023)."""

from __future__ import annotations

import random


def main() -> None:
    rng = random.Random(573)
    n, m, d = 6, 8, 10
    mu = 0.4
    L = 3.2
    # Construct n workers, each with m L-smooth convex functions f_{ij}(x) = 0.5 x^T A_{ij} x - b_{ij}^T x
    a_ij = []
    b_ij = []
    for i in range(n):
        worker_a = []
        worker_b = []
        for j in range(m):
            diag = [
                mu + (L - mu) * ((k + j) % d) / (d - 1)
                for k in range(d)
            ]
            worker_a.append(diag)
            worker_b.append([rng.gauss(0.0, 1.2) for _ in range(d)])
        a_ij.append(worker_a)
        b_ij.append(worker_b)

    # Exact global minimizer x^* of f(x) = (1/(nm)) sum_{i,j} f_{ij}(x)
    avg_a = [
        sum(a_ij[i][j][k] for i in range(n) for j in range(m)) / (n * m)
        for k in range(d)
    ]
    avg_b = [
        sum(b_ij[i][j][k] for i in range(n) for j in range(m)) / (n * m)
        for k in range(d)
    ]
    x_star = [avg_b[k] / avg_a[k] for k in range(d)]

    def grad_ij(i: int, j: int, x: list[float]) -> list[float]:
        return [a_ij[i][j][k] * x[k] - b_ij[i][j][k] for k in range(d)]

    def grad_i(i: int, x: list[float]) -> list[float]:
        return [
            sum(a_ij[i][j][k] * x[k] - b_ij[i][j][k] for j in range(m)) / m
            for k in range(d)
        ]

    # Unbiased random sparsification operator Q(v) keeping r=2 out of d=10 coordinates: omega = d/r - 1 = 4.0
    r_keep = 2
    omega = (d / r_keep) - 1.0
    scale = d / r_keep

    def quantize(v: list[float]) -> list[float]:
        idx = set(rng.sample(range(d), r_keep))
        return [scale * v[k] if k in idx else 0.0 for k in range(d)]

    # Verify unbiasedness and omega-variance identity exactly over all (d choose r) subsets
    test_v = [rng.uniform(-2.0, 2.0) for _ in range(d)]
    norm_v_sq = sum(val * val for val in test_v)
    from itertools import combinations
    all_subsets = list(combinations(range(d), r_keep))
    mean_q = [0.0] * d
    var_q = 0.0
    for sub in all_subsets:
        qv = [scale * test_v[k] if k in sub else 0.0 for k in range(d)]
        for k in range(d):
            mean_q[k] += qv[k] / len(all_subsets)
        var_q += sum((qv[k] - test_v[k]) ** 2 for k in range(d)) / len(all_subsets)
    assert max(abs(mean_q[k] - test_v[k]) for k in range(d)) < 1e-12
    assert abs(var_q - omega * norm_v_sq) < 1e-10

    # Compare VR-DIANA (Algorithm 2 Variant 1: L-SVRG) vs non-variance-reduced DIANA with stochastic local gradients
    alpha = 1.0 / (omega + 1.0)
    gamma = 0.12 / L  # stable step size for comparison
    steps = 1500

    # 1. VR-DIANA (L-SVRG Variant 1)
    x_vr = [0.0] * d
    h_vr = [[0.0] * d for _ in range(n)]
    h_bar_vr = [0.0] * d
    w_vr = [0.0] * d
    mu_vr = [grad_i(i, w_vr) for i in range(n)]

    # 2. Non-VR DIANA (sampling 1 component j_i^k per worker without variance reduction)
    x_diana = [0.0] * d
    h_diana = [[0.0] * d for _ in range(n)]
    h_bar_diana = [0.0] * d

    for _ in range(steps):
        uk = 1 if rng.random() < (1.0 / m) else 0
        delta_hat_vr_sum = [0.0] * d
        delta_hat_diana_sum = [0.0] * d

        for i in range(n):
            jik = rng.randrange(m)
            # VR-DIANA local variance-reduced gradient
            g_vr_i = [
                grad_ij(i, jik, x_vr)[k] - grad_ij(i, jik, w_vr)[k] + mu_vr[i][k]
                for k in range(d)
            ]
            dh_vr = quantize([g_vr_i[k] - h_vr[i][k] for k in range(d)])
            h_vr[i] = [h_vr[i][k] + alpha * dh_vr[k] for k in range(d)]
            for k in range(d):
                delta_hat_vr_sum[k] += dh_vr[k] / n

            # Non-VR DIANA local stochastic gradient
            g_diana_i = grad_ij(i, jik, x_diana)
            dh_diana = quantize([g_diana_i[k] - h_diana[i][k] for k in range(d)])
            h_diana[i] = [h_diana[i][k] + alpha * dh_diana[k] for k in range(d)]
            for k in range(d):
                delta_hat_diana_sum[k] += dh_diana[k] / n

        if uk == 1:
            w_vr = list(x_vr)
            mu_vr = [grad_i(i, w_vr) for i in range(n)]

        gk_vr = [h_bar_vr[k] + delta_hat_vr_sum[k] for k in range(d)]
        x_vr = [x_vr[k] - gamma * gk_vr[k] for k in range(d)]
        h_bar_vr = [h_bar_vr[k] + alpha * delta_hat_vr_sum[k] for k in range(d)]

        gk_diana = [h_bar_diana[k] + delta_hat_diana_sum[k] for k in range(d)]
        x_diana = [x_diana[k] - gamma * gk_diana[k] for k in range(d)]
        h_bar_diana = [h_bar_diana[k] + alpha * delta_hat_diana_sum[k] for k in range(d)]

    err_vr = sum((x_vr[k] - x_star[k]) ** 2 for k in range(d))
    err_diana = sum((x_diana[k] - x_star[k]) ** 2 for k in range(d))
    h_err_vr = sum(
        sum((h_vr[i][k] - grad_i(i, x_star)[k]) ** 2 for k in range(d))
        for i in range(n)
    )
    assert err_vr < 1e-12 and err_vr < 1e-8 * err_diana, (
        f"VR-DIANA failed to beat DIANA neighborhood: err_vr={err_vr}, err_diana={err_diana}"
    )
    assert h_err_vr < 1e-10, f"Shift vectors H^k did not converge to grad f_i(x^*): {h_err_vr}"

    print(
        f"[PASS] Round 573 VR-DIANA verified: omega={omega:.1f}, "
        f"err_vr={err_vr:.3e} << err_diana={err_diana:.3e}, H_K={h_err_vr:.3e}"
    )


if __name__ == "__main__":
    main()
