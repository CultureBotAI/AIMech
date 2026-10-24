#!/usr/bin/env python3
"""Constructed boundary verification for Round 577: EF21 Extensions (EF21-PAGE, EF21-BC, EF21-PP, EF21-HB, EF21-Prox) (Fatkhullin et al., JMLR 2025)."""

from __future__ import annotations

import math
import random


def top_k(v: list[float], k_keep: int) -> list[float]:
    d = len(v)
    idx = sorted(range(d), key=lambda j: abs(v[j]), reverse=True)[:k_keep]
    keep = set(idx)
    return [v[j] if j in keep else 0.0 for j in range(d)]


def soft_threshold(v: list[float], thresh: float) -> list[float]:
    out = []
    for val in v:
        if val > thresh:
            out.append(val - thresh)
        elif val < -thresh:
            out.append(val + thresh)
        else:
            out.append(0.0)
    return out


def main() -> None:
    rng = random.Random(577)
    n, m, d = 6, 8, 8
    k_w, k_m = 2, 2
    alpha_w = k_w / d
    alpha_m = k_m / d

    # Verify Lemma 35 optimal Young's inequality parameter s^* = 1/sqrt(1-alpha) - 1
    s_star = 1.0 / math.sqrt(1.0 - alpha_w) - 1.0
    theta_star = 1.0 - (1.0 - alpha_w) * (1.0 + s_star)
    beta_star = (1.0 - alpha_w) * (1.0 + 1.0 / s_star)
    assert abs(theta_star - (1.0 - math.sqrt(1.0 - alpha_w))) < 1e-12
    assert math.sqrt(beta_star / theta_star) <= (2.0 / alpha_w - 1.0) + 1e-12

    # Construct heterogeneous finite-sum components f_{ij}(x) = 0.5 x^T A_{ij} x - b_{ij}^T x
    a_ij = []
    b_ij = []
    for i in range(n):
        wa = []
        wb = []
        for j in range(m):
            diag = [0.5 + 2.5 * ((c + j + i) % d) / (d - 1) for c in range(d)]
            wa.append(diag)
            wb.append([rng.gauss(0.0, 1.2) for _ in range(d)])
        a_ij.append(wa)
        b_ij.append(wb)

    def grad_ij(i: int, j: int, x: list[float]) -> list[float]:
        return [a_ij[i][j][c] * x[c] - b_ij[i][j][c] for c in range(d)]

    def grad_i(i: int, x: list[float]) -> list[float]:
        return [
            sum(grad_ij(i, j, x)[c] for j in range(m)) / m
            for c in range(d)
        ]

    def full_grad(x: list[float]) -> list[float]:
        return [
            sum(grad_i(i, x)[c] for i in range(n)) / n
            for c in range(d)
        ]

    # 1. Compare EF21-PAGE (Algorithm 2) vs EF21-SGD (Algorithm 1) with Top-k (k=2) and minibatch tau=1
    gamma = 0.04
    p_page = 1.0 / (m + 1.0)
    steps = 800

    x_page = [0.0] * d
    v_page = [grad_i(i, x_page) for i in range(n)]
    g_page = [list(v_page[i]) for i in range(n)]
    g_bar_page = list(full_grad(x_page))

    x_sgd = [0.0] * d
    g_sgd = [grad_i(i, x_sgd) for i in range(n)]
    g_bar_sgd = list(full_grad(x_sgd))

    for _ in range(steps):
        # EF21-PAGE step
        x_next_page = [x_page[c] - gamma * g_bar_page[c] for c in range(d)]
        c_sum_page = [0.0] * d
        for i in range(n):
            if rng.random() < p_page:
                v_page[i] = grad_i(i, x_next_page)
            else:
                j_idx = rng.randrange(m)
                g_new = grad_ij(i, j_idx, x_next_page)
                g_old = grad_ij(i, j_idx, x_page)
                v_page[i] = [
                    v_page[i][c] + g_new[c] - g_old[c] for c in range(d)
                ]
            ci = top_k([v_page[i][c] - g_page[i][c] for c in range(d)], k_w)
            g_page[i] = [g_page[i][c] + ci[c] for c in range(d)]
            for c in range(d):
                c_sum_page[c] += ci[c] / n
        g_bar_page = [g_bar_page[c] + c_sum_page[c] for c in range(d)]
        x_page = x_next_page

        # EF21-SGD step
        x_next_sgd = [x_sgd[c] - gamma * g_bar_sgd[c] for c in range(d)]
        c_sum_sgd = [0.0] * d
        for i in range(n):
            j_idx = rng.randrange(m)
            g_hat = grad_ij(i, j_idx, x_next_sgd)
            ci = top_k([g_hat[c] - g_sgd[i][c] for c in range(d)], k_w)
            g_sgd[i] = [g_sgd[i][c] + ci[c] for c in range(d)]
            for c in range(d):
                c_sum_sgd[c] += ci[c] / n
        g_bar_sgd = [g_bar_sgd[c] + c_sum_sgd[c] for c in range(d)]
        x_sgd = x_next_sgd

    gn_page = sum(v * v for v in full_grad(x_page))
    gn_sgd = sum(v * v for v in full_grad(x_sgd))
    assert gn_page < 1e-12 and gn_page < 1e-6 * gn_sgd, (
        f"EF21-PAGE failed to eliminate stochastic variance: gn_page={gn_page}, gn_sgd={gn_sgd}"
    )

    # 2. Verify EF21-BC (Algorithm 4: bidirectional biased Top-k compression)
    x_bc = [0.0] * d
    g_tilde_i = [grad_i(i, x_bc) for i in range(n)]
    g_tilde = list(full_grad(x_bc))
    g_bc = list(g_tilde)
    for _ in range(500):
        x_bc = [x_bc[c] - gamma * g_bc[c] for c in range(d)]
        c_sum = [0.0] * d
        for i in range(n):
            gi_full = grad_i(i, x_bc)
            ci = top_k([gi_full[c] - g_tilde_i[i][c] for c in range(d)], k_w)
            g_tilde_i[i] = [g_tilde_i[i][c] + ci[c] for c in range(d)]
            for c in range(d):
                c_sum[c] += ci[c] / n
        g_tilde = [g_tilde[c] + c_sum[c] for c in range(d)]
        b_next = top_k([g_tilde[c] - g_bc[c] for c in range(d)], k_m)
        g_bc = [g_bc[c] + b_next[c] for c in range(d)]
    gn_bc = sum(v * v for v in full_grad(x_bc))
    assert gn_bc < 1e-10, f"EF21-BC failed to converge: {gn_bc}"

    # 3. Verify EF21-Prox (Algorithm 6: L1 composite regularization r(x) = lam_1 ||x||_1)
    lam_1 = 0.1
    x_prox = [0.0] * d
    g_prox_i = [grad_i(i, x_prox) for i in range(n)]
    g_prox = list(full_grad(x_prox))
    for _ in range(500):
        x_prox = soft_threshold(
            [x_prox[c] - gamma * g_prox[c] for c in range(d)], gamma * lam_1
        )
        c_sum = [0.0] * d
        for i in range(n):
            gi_full = grad_i(i, x_prox)
            ci = top_k([gi_full[c] - g_prox_i[i][c] for c in range(d)], k_w)
            g_prox_i[i] = [g_prox_i[i][c] + ci[c] for c in range(d)]
            for c in range(d):
                c_sum[c] += ci[c] / n
        g_prox = [g_prox[c] + c_sum[c] for c in range(d)]

    fg_prox = full_grad(x_prox)
    prox_step = soft_threshold(
        [x_prox[c] - gamma * fg_prox[c] for c in range(d)], gamma * lam_1
    )
    grad_mapping_sq = sum(
        ((x_prox[c] - prox_step[c]) / gamma) ** 2 for c in range(d)
    )
    assert grad_mapping_sq < 1e-12, f"EF21-Prox failed on composite L1 problem: {grad_mapping_sq}"

    print(
        f"[PASS] Round 577 EF21-Bells-Whistles verified: "
        f"gn_page={gn_page:.3e} << gn_sgd={gn_sgd:.3e}, "
        f"gn_bc={gn_bc:.3e}, grad_map_prox={grad_mapping_sq:.3e}"
    )


if __name__ == "__main__":
    main()
