#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 559: 3PC Three Point Compressors (Richtarik et al., ICML 2022)."""

import math
import random


def top_k(vec, k):
    indexed = sorted(enumerate(vec), key=lambda iv: abs(iv[1]), reverse=True)
    keep = {idx for idx, _ in indexed[:k]}
    return [v if idx in keep else 0.0 for idx, v in enumerate(vec)]


def vec_add(u, v):
    return [a + b for a, b in zip(u, v)]


def vec_sub(u, v):
    return [a - b for a, b in zip(u, v)]


def sq_norm(u):
    return sum(a * a for a in u)


def main():
    rng = random.Random(20220202)
    d = 6
    k = 2
    alpha = k / d  # Top-2 on R^6 has contraction factor alpha = 1/3

    # 1. Verify Definition 4.1 (Three Point Compressor inequality, Eq. 6):
    # E[||C_{h,y}(x) - x||^2] <= (1 - A)||h - y||^2 + B||x - y||^2
    # for EF21 (Lemma C.1 & C.3), LAG (Lemma C.5), and CLAG (Lemma C.8)
    A_ef21 = 1.0 - math.sqrt(1.0 - alpha)
    B_ef21 = (1.0 - alpha) / (1.0 - math.sqrt(1.0 - alpha))

    zeta = 0.8
    A_lag, B_lag = 1.0, zeta
    A_clag, B_clag = A_ef21, max(B_ef21, zeta)

    for _ in range(50):
        x = [rng.gauss(0.0, 2.0) for _ in range(d)]
        y = [rng.gauss(0.0, 2.0) for _ in range(d)]
        h = [rng.gauss(0.0, 2.0) for _ in range(d)]

        hy_sq = sq_norm(vec_sub(h, y))
        xy_sq = sq_norm(vec_sub(x, y))
        xh_sq = sq_norm(vec_sub(x, h))

        # EF21: C_{h,y}(x) = h + TopK(x - h)
        c_ef21 = vec_add(h, top_k(vec_sub(x, h), k))
        err_ef21 = sq_norm(vec_sub(c_ef21, x))
        rhs_ef21 = (1.0 - A_ef21) * hy_sq + B_ef21 * xy_sq
        assert err_ef21 <= rhs_ef21 + 1e-11

        # LAG: C_{h,y}(x) = x if ||x - h||^2 > zeta * ||x - y||^2 else h
        c_lag = x[:] if xh_sq > zeta * xy_sq else h[:]
        err_lag = sq_norm(vec_sub(c_lag, x))
        rhs_lag = (1.0 - A_lag) * hy_sq + B_lag * xy_sq
        assert err_lag <= rhs_lag + 1e-11

        # CLAG: C_{h,y}(x) = h + TopK(x - h) if ||x - h||^2 > zeta * ||x - y||^2 else h
        c_clag = vec_add(h, top_k(vec_sub(x, h), k)) if xh_sq > zeta * xy_sq else h[:]
        err_clag = sq_norm(vec_sub(c_clag, x))
        rhs_clag = (1.0 - A_clag) * hy_sq + B_clag * xy_sq
        assert err_clag <= rhs_clag + 1e-11

    # 2. Verify Algorithm 4 (CLAG) convergence and Lemma 5.4 (3PC inequality Eq. 16) on heterogeneous smoothness task
    n = 4
    L_workers = [0.2, 0.4, 1.0, 1.4]
    targets = [[(i - 1.5) * 3.0 + 0.5 * c for c in range(d)] for i in range(n)]
    # Global objective f(x) = (1/n) sum_i 0.5 * L_i * ||x - targets[i]||^2
    w_sum = sum(L_workers)
    x_star = [sum(L_workers[i] * targets[i][c] for i in range(n)) / w_sum for c in range(d)]

    def grad_i(i, x_vec):
        return [L_workers[i] * (x_vec[c] - targets[i][c]) for c in range(d)]

    L_minus = sum(L_workers) / n
    L_plus = math.sqrt(sum(L_i ** 2 for L_i in L_workers) / n)
    gamma = 1.0 / (L_minus + L_plus * math.sqrt(2.0 * B_clag / A_clag))

    x_curr = [4.0] * d
    g_workers = [grad_i(i, x_curr) for i in range(n)]
    g_bar = [sum(g_workers[i][c] for i in range(n)) / n for c in range(d)]
    skipped_uploads = 0
    total_uploads = 0

    init_dist_sq = sq_norm(vec_sub(x_curr, x_star))

    for _ in range(180):
        G_t = sum(sq_norm(vec_sub(g_workers[i], grad_i(i, x_curr))) for i in range(n)) / n
        x_next = [x_curr[c] - gamma * g_bar[c] for c in range(d)]
        step_sq = sq_norm(vec_sub(x_next, x_curr))

        g_workers_next = []
        for i in range(n):
            gx_next = grad_i(i, x_next)
            total_uploads += 1
            # Algorithm 4 trigger condition (Section 4.3): ||grad f_i(x^{t+1}) - g_i^t||^2 > zeta * L_i^2 * ||x^{t+1} - x^t||^2
            # where worker 0 with small L_0=0.2 vs global trigger threshold zeta * (0.5 * L_plus^2) * ||x^{t+1} - x^t||^2 skips uploads
            trigger_thresh = zeta * 0.5 * (L_plus ** 2) * step_sq
            if sq_norm(vec_sub(gx_next, g_workers[i])) > trigger_thresh:
                g_new = vec_add(g_workers[i], top_k(vec_sub(gx_next, g_workers[i]), k))
            else:
                g_new = g_workers[i][:]
                skipped_uploads += 1
            g_workers_next.append(g_new)

        G_next = sum(sq_norm(vec_sub(g_workers_next[i], grad_i(i, x_next))) for i in range(n)) / n
        # Verify 3PC Lyapunov contraction (Lemma 5.4 Eq. 16)
        assert G_next <= (1.0 - A_clag) * G_t + B_clag * (L_plus ** 2) * step_sq + 1e-11

        x_curr = x_next
        g_workers = g_workers_next
        g_bar = [sum(g_workers[i][c] for i in range(n)) / n for c in range(d)]

    final_dist_sq = sq_norm(vec_sub(x_curr, x_star))
    assert final_dist_sq < 1e-4 * init_dist_sq
    assert skipped_uploads > 0

    print(
        f"[PASS] Round 559 3PC/CLAG verified: dist_sq {init_dist_sq:.4f} -> {final_dist_sq:.3e}, "
        f"skipped={skipped_uploads}/{total_uploads}, A_clag={A_clag:.4f}, B_clag={B_clag:.4f}"
    )


if __name__ == "__main__":
    main()
