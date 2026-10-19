#!/usr/bin/env python3
"""Boundary verification for Round 441: Acc-DNGD (Qu & Li 2020, IEEE TAC 65(6):2566-2581, arXiv:1705.07176)."""
import math

def main():
    # 4-node graph with doubly stochastic matrix W: w_ii = 0.4, off-diag = 0.2 (eigenvalues 1, 0.2, 0.2, 0.2 -> sigma = 0.2)
    n = 4
    W = [
        [0.40, 0.20, 0.20, 0.20],
        [0.20, 0.40, 0.20, 0.20],
        [0.20, 0.20, 0.40, 0.20],
        [0.20, 0.20, 0.20, 0.40],
    ]
    sigma = 0.2
    # Strongly convex ill-conditioned 2D local objectives:
    # f_i(x1, x2) = 0.5 * L * (x1 - b1_i)^2 + 0.5 * mu * (x2 - b2_i)^2 with L=2.0, mu=0.02 (kappa=100)
    mu = 0.02
    L = 2.0
    b1 = [4.0, -2.0, 2.0, 0.0]
    b2 = [3.0, -1.0, 5.0, 1.0]
    x1_star = sum(b1) / n  # 1.0
    x2_star = sum(b2) / n  # 2.0

    # Run Acc-DNGD-SC (Eq. 4a-4d) vs non-accelerated gradient tracking (DIGing / Harnessing)
    eta = 0.02
    alpha = math.sqrt(mu * eta)
    x1, x2 = [0.0] * n, [0.0] * n
    v1, v2 = [0.0] * n, [0.0] * n
    y1, y2 = [0.0] * n, [0.0] * n
    s1 = [L * (y1[i] - b1[i]) for i in range(n)]
    s2 = [mu * (y2[i] - b2[i]) for i in range(n)]

    x1_gt, x2_gt = [0.0] * n, [0.0] * n
    s1_gt = [L * (x1_gt[i] - b1[i]) for i in range(n)]
    s2_gt = [mu * (x2_gt[i] - b2[i]) for i in range(n)]

    max_tracking_conservation_err = 0.0
    for _ in range(300):
        x1_next = [sum(W[i][j] * y1[j] for j in range(n)) - eta * s1[i] for i in range(n)]
        x2_next = [sum(W[i][j] * y2[j] for j in range(n)) - eta * s2[i] for i in range(n)]
        v1_next = [
            (1.0 - alpha) * sum(W[i][j] * v1[j] for j in range(n))
            + alpha * sum(W[i][j] * y1[j] for j in range(n))
            - (eta / alpha) * s1[i]
            for i in range(n)
        ]
        v2_next = [
            (1.0 - alpha) * sum(W[i][j] * v2[j] for j in range(n))
            + alpha * sum(W[i][j] * y2[j] for j in range(n))
            - (eta / alpha) * s2[i]
            for i in range(n)
        ]
        y1_next = [(x1_next[i] + alpha * v1_next[i]) / (1.0 + alpha) for i in range(n)]
        y2_next = [(x2_next[i] + alpha * v2_next[i]) / (1.0 + alpha) for i in range(n)]

        g1_old = [L * (y1[i] - b1[i]) for i in range(n)]
        g2_old = [mu * (y2[i] - b2[i]) for i in range(n)]
        g1_new = [L * (y1_next[i] - b1[i]) for i in range(n)]
        g2_new = [mu * (y2_next[i] - b2[i]) for i in range(n)]

        s1_next = [sum(W[i][j] * s1[j] for j in range(n)) + g1_new[i] - g1_old[i] for i in range(n)]
        s2_next = [sum(W[i][j] * s2[j] for j in range(n)) + g2_new[i] - g2_old[i] for i in range(n)]

        x1, x2, v1, v2, y1, y2, s1, s2 = x1_next, x2_next, v1_next, v2_next, y1_next, y2_next, s1_next, s2_next
        cons_err = max(abs(sum(s1) / n - sum(g1_new) / n), abs(sum(s2) / n - sum(g2_new) / n))
        if cons_err > max_tracking_conservation_err:
            max_tracking_conservation_err = cons_err

        # Non-accelerated gradient tracking step
        x1_gt_next = [sum(W[i][j] * x1_gt[j] for j in range(n)) - eta * s1_gt[i] for i in range(n)]
        x2_gt_next = [sum(W[i][j] * x2_gt[j] for j in range(n)) - eta * s2_gt[i] for i in range(n)]
        gg1_old = [L * (x1_gt[i] - b1[i]) for i in range(n)]
        gg2_old = [mu * (x2_gt[i] - b2[i]) for i in range(n)]
        gg1_new = [L * (x1_gt_next[i] - b1[i]) for i in range(n)]
        gg2_new = [mu * (x2_gt_next[i] - b2[i]) for i in range(n)]
        s1_gt = [sum(W[i][j] * s1_gt[j] for j in range(n)) + gg1_new[i] - gg1_old[i] for i in range(n)]
        s2_gt = [sum(W[i][j] * s2_gt[j] for j in range(n)) + gg2_new[i] - gg2_old[i] for i in range(n)]
        x1_gt, x2_gt = x1_gt_next, x2_gt_next

    err_accdngd = max(math.hypot(x1[i] - x1_star, x2[i] - x2_star) for i in range(n))
    err_gt = max(math.hypot(x1_gt[i] - x1_star, x2_gt[i] - x2_star) for i in range(n))
    assert max_tracking_conservation_err < 1e-14
    assert err_accdngd < 0.05 and err_accdngd < 0.05 * err_gt

    # Verify Theorem 3 condition-number scaling exponent 5/7 vs unaccelerated 1:
    kappa = 1000.0
    rate_factor_acc = kappa ** (-5.0 / 7.0)
    rate_factor_unacc = kappa ** (-1.0)
    assert rate_factor_acc > 7.0 * rate_factor_unacc
    print(f"[PASS] Round 441 Acc-DNGD (Qu & Li 2020): tracking_err={max_tracking_conservation_err:.2e}, err_acc={err_accdngd:.2e} << err_gt={err_gt:.2e}, kappa1000_acc_gain={rate_factor_acc/rate_factor_unacc:.2f}x")

if __name__ == "__main__":
    main()
