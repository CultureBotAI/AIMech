"""Constructed boundary and numerical verification for Round 436:
GT-SAGA and GT-SVRG: Decentralized Variance-Reduced Gradient Tracking
(Ran Xin, Usman A. Khan, & Soummya Kar 2020, IEEE Trans. Signal Process. 68:6255-6270, arXiv:1912.04230).
"""

from __future__ import annotations

import math
import random


def mat_vec(W: list[list[float]], v: list[float]) -> list[float]:
    return [sum(W[i][j] * v[j] for j in range(len(v))) for i in range(len(W))]


def vec_norm(v: list[float]) -> float:
    return math.sqrt(sum(x * x for x in v))


def main() -> None:
    rng = random.Random(436)
    n = 4
    m = 5
    W = [
        [0.50, 0.25, 0.00, 0.25],
        [0.25, 0.50, 0.25, 0.00],
        [0.00, 0.25, 0.50, 0.25],
        [0.25, 0.00, 0.25, 0.50],
    ]

    # Component functions f_{i,j}(x) = 0.5 * a_{i,j} * (x - b_{i,j})^2
    a = [[1.5 + 0.2 * i + 0.1 * j for j in range(m)] for i in range(n)]
    b = [[(-1.0) ** i * (2.0 + i) + 0.6 * (j - 2.0) for j in range(m)] for i in range(n)]

    def grad_fij(i: int, j: int, x_val: float) -> float:
        return a[i][j] * (x_val - b[i][j])

    def grad_fi(i: int, x_val: float) -> float:
        return sum(grad_fij(i, j, x_val) for j in range(m)) / m

    x_star = sum(a[i][j] * b[i][j] for i in range(n) for j in range(m)) / sum(
        a[i][j] for i in range(n) for j in range(m)
    )

    # Inter-node heterogeneity zeta^2 and intra-node variance nu^2 at x_star
    zeta_sq = sum(grad_fi(i, x_star) ** 2 for i in range(n)) / n
    nu_sq = sum((grad_fij(i, j, x_star) - grad_fi(i, x_star)) ** 2 for i in range(n) for j in range(m)) / (n * m)
    assert zeta_sq > 1.0 and nu_sq > 0.1

    alpha = 0.08
    x0 = [1.0, -1.0, 2.0, -2.0]

    # 1. GT-SAGA (Algorithm 1)
    x_saga = x0[:]
    table = [[grad_fij(i, j, x_saga[i]) for j in range(m)] for i in range(n)]
    g_saga = [sum(table[i]) / m for i in range(n)]
    y_saga = g_saga[:]
    max_tracker_drift_saga = 0.0

    for _ in range(1200):
        Wx = mat_vec(W, x_saga)
        x_next = [Wx[i] - alpha * y_saga[i] for i in range(n)]
        g_next = [0.0] * n
        for i in range(n):
            s_i = rng.randrange(m)
            new_g = grad_fij(i, s_i, x_next[i])
            old_g = table[i][s_i]
            avg_table = sum(table[i]) / m
            g_next[i] = new_g - old_g + avg_table
            table[i][s_i] = new_g
        Wy = mat_vec(W, y_saga)
        y_next = [Wy[i] + g_next[i] - g_saga[i] for i in range(n)]
        drift = abs(sum(y_next) / n - sum(g_next) / n)
        max_tracker_drift_saga = max(max_tracker_drift_saga, drift)
        x_saga, y_saga, g_saga = x_next, y_next, g_next

    # 2. GT-SVRG (Algorithm 2) with snapshot period T = 2*m
    x_svrg = x0[:]
    v_svrg = [grad_fi(i, x_svrg[i]) for i in range(n)]
    y_svrg = v_svrg[:]
    snap_x = x_svrg[:]
    snap_full = [grad_fi(i, snap_x[i]) for i in range(n)]
    T_period = 2 * m

    for k in range(1, 1201):
        Wx = mat_vec(W, x_svrg)
        x_next = [Wx[i] - alpha * y_svrg[i] for i in range(n)]
        if k % T_period == 0:
            snap_x = x_next[:]
            snap_full = [grad_fi(i, snap_x[i]) for i in range(n)]
        v_next = [0.0] * n
        for i in range(n):
            s_i = rng.randrange(m)
            v_next[i] = grad_fij(i, s_i, x_next[i]) - grad_fij(i, s_i, snap_x[i]) + snap_full[i]
        Wy = mat_vec(W, y_svrg)
        y_next = [Wy[i] + v_next[i] - v_svrg[i] for i in range(n)]
        x_svrg, y_svrg, v_svrg = x_next, y_next, v_next

    # 3. Decentralized SAGA without gradient tracking (stalls at O(alpha * zeta^2))
    x_no_gt = x0[:]
    tab_no_gt = [[grad_fij(i, j, x_no_gt[i]) for j in range(m)] for i in range(n)]
    for _ in range(1200):
        Wx = mat_vec(W, x_no_gt)
        g_step = [0.0] * n
        for i in range(n):
            s_i = rng.randrange(m)
            new_g = grad_fij(i, s_i, x_no_gt[i])
            g_step[i] = new_g - tab_no_gt[i][s_i] + sum(tab_no_gt[i]) / m
            tab_no_gt[i][s_i] = new_g
        x_no_gt = [Wx[i] - alpha * g_step[i] for i in range(n)]

    err_gt_saga = vec_norm([x_saga[i] - x_star for i in range(n)])
    err_gt_svrg = vec_norm([x_svrg[i] - x_star for i in range(n)])
    err_no_gt = vec_norm([x_no_gt[i] - x_star for i in range(n)])

    assert max_tracker_drift_saga < 1e-13
    assert err_gt_saga < 1e-11, f"GT-SAGA did not converge to exact optimum: {err_gt_saga}"
    assert err_gt_svrg < 1e-11, f"GT-SVRG did not converge to exact optimum: {err_gt_svrg}"
    assert err_no_gt > 0.25, f"SAGA without GT should stall at heterogeneity floor: {err_no_gt}"

    print(
        f"[PASS] Round 436 GT-SAGA & GT-SVRG (Xin et al. 2020): "
        f"err_gt_saga={err_gt_saga:.2e}, err_gt_svrg={err_gt_svrg:.2e} << err_no_gt={err_no_gt:.4f}"
    )


if __name__ == "__main__":
    main()
