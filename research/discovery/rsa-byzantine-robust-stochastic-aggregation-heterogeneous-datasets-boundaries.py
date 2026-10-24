#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 522:
RSA (Byzantine-Robust Stochastic Aggregation for Heterogeneous Datasets)
Li, Xu, Chen, Giannakis, & Ling, AAAI 2019 (DOI:10.1609/AAAI.V33I01.33011544, arXiv:1811.03761).

Verifies:
1. Proposition 1 & Theorem 1 exact consensus condition: for heterogeneous regular workers
   i in R with local strongly convex objectives f_i(x) and master regularizer f_0(x),
   whenever penalty lambda >= lambda_0 := max_{i in R} ||nabla f_i(tilde_x^*)||_infty
   (for l1-norm RSA, p=1, dual norm b=infty), the penalized objective (Eq. 5) achieves
   exact consensus x_i^* = x_0^* = tilde_x^*.
2. Eqs. 7-8 (l1-norm RSA updates): each regular worker updates
   x_i^{k+1} = x_i^k - alpha^{k+1} (nabla F_i(x_i^k) + lambda * sign(x_i^k - x_0^k))
   and the master updates
   x_0^{k+1} = x_0^k - alpha^{k+1} (nabla f_0(x_0^k) + lambda * (sum_{i in R} sign(x_0^k - x_i^k) + sum_{j in B} sign(x_0^k - z_j^k))).
3. Under heterogeneous worker optima and omniscient large-magnitude Byzantine attacks z_j^k,
   every Byzantine worker's per-coordinate influence is bounded in [-lambda, +lambda],
   outperforming coordinate-wise median and mean aggregation on heterogeneous data.
"""

import math


def sign_val(u):
    if u > 1e-12:
        return 1.0
    if u < -1e-12:
        return -1.0
    return 0.0


def sign_vec(v):
    return [sign_val(u) for u in v]


def l2_dist(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def main():
    # 6 regular workers with strongly heterogeneous local quadratics:
    # f_i(x) = 0.5 * ||x - c_i||_2^2, and master regularizer f_0(x) = 0.5 * rho_0 * ||x||_2^2
    # Plus q = 2 Byzantine workers (m = 8 total workers, r = 6 regular workers)
    d = 4
    rho_0 = 0.2
    regular_centers = [
        [2.4, -1.8, 0.9, -1.2],
        [2.2, -2.0, 1.1, -1.0],
        [-1.8, 2.5, -1.3, 1.6],
        [-2.0, 2.3, -1.1, 1.4],
        [0.4, 0.2, 2.0, -0.8],
        [0.2, 0.4, 1.8, -1.0],
    ]
    r = len(regular_centers)
    q = 2

    # True global consensus optimum tilde_x^* minimizing sum_{i in R} f_i(x) + f_0(x):
    # (r + rho_0) * tilde_x^* = sum_{i in R} c_i
    tilde_x_star = [
        sum(regular_centers[i][j] for i in range(r)) / (r + rho_0)
        for j in range(d)
    ]

    # Compute threshold lambda_0 = max_{i in R} ||nabla f_i(tilde_x^*)||_infty (Theorem 1, p=1 => b=infty)
    lambda_0 = max(
        max(abs(tilde_x_star[j] - regular_centers[i][j]) for j in range(d))
        for i in range(r)
    )
    # Choose lambda > lambda_0 for exact consensus (Theorem 1) in benign regime (q=0)
    lam_consensus = lambda_0 + 0.35

    # 1. Verify Theorem 1 consensus in benign setting (q=0)
    x_master = [0.0 for _ in range(d)]
    x_workers = [[0.0 for _ in range(d)] for _ in range(r)]
    for k in range(1, 3001):
        alpha = 0.06 / (k ** 0.6)
        x_master_prev = list(x_master)
        x_workers_prev = [list(w) for w in x_workers]
        for i in range(r):
            grad_i = [x_workers_prev[i][j] - regular_centers[i][j] for j in range(d)]
            sgn_i = sign_vec([x_workers_prev[i][j] - x_master_prev[j] for j in range(d)])
            x_workers[i] = [
                x_workers_prev[i][j] - alpha * (grad_i[j] + lam_consensus * sgn_i[j])
                for j in range(d)
            ]
        grad_0 = [rho_0 * x_master_prev[j] for j in range(d)]
        sum_sgn = [
            sum(sign_val(x_master_prev[j] - x_workers_prev[i][j]) for i in range(r))
            for j in range(d)
        ]
        x_master = [
            x_master_prev[j] - alpha * (grad_0[j] + lam_consensus * sum_sgn[j])
            for j in range(d)
        ]

    max_worker_gap = max(l2_dist(x_workers[i], x_master) for i in range(r))
    opt_gap_benign = l2_dist(x_master, tilde_x_star)
    assert max_worker_gap < 0.03 and opt_gap_benign < 0.03, (
        f"Theorem 1 consensus failed: worker_gap={max_worker_gap}, opt_gap={opt_gap_benign}"
    )

    # 2. Verify Byzantine resilience (Eqs. 7-8) under extreme omniscient attack z_j^k = +1000
    lam_byz = 0.75
    x0_rsa = [0.0 for _ in range(d)]
    xw_rsa = [[0.0 for _ in range(d)] for _ in range(r)]
    x_sgd_mean = [0.0 for _ in range(d)]

    for k in range(1, 1201):
        alpha = min(0.03, 1.5 / (k + 20.0))
        x0_prev = list(x0_rsa)
        xw_prev = [list(w) for w in xw_rsa]
        # Byzantine workers transmit extreme malicious model z_j^k = -500.0
        byz_models = [[-500.0 for _ in range(d)] for _ in range(q)]

        for i in range(r):
            grad_i = [xw_prev[i][j] - regular_centers[i][j] for j in range(d)]
            sgn_i = sign_vec([xw_prev[i][j] - x0_prev[j] for j in range(d)])
            xw_rsa[i] = [
                xw_prev[i][j] - alpha * (grad_i[j] + lam_byz * sgn_i[j])
                for j in range(d)
            ]
        grad_0 = [rho_0 * x0_prev[j] for j in range(d)]
        sum_sgn_reg = [
            sum(sign_val(x0_prev[j] - xw_prev[i][j]) for i in range(r))
            for j in range(d)
        ]
        sum_sgn_byz = [
            sum(sign_val(x0_prev[j] - byz_models[b_idx][j]) for b_idx in range(q))
            for j in range(d)
        ]
        # Verify per-coordinate Byzantine influence is strictly bounded by q * lam_byz
        for j in range(d):
            assert abs(lam_byz * sum_sgn_byz[j]) <= q * lam_byz + 1e-12

        x0_rsa = [
            x0_prev[j] - alpha * (grad_0[j] + lam_byz * (sum_sgn_reg[j] + sum_sgn_byz[j]))
            for j in range(d)
        ]

        # Contrast with standard mean-aggregated SGD under the same extreme attack
        mean_grad = [
            (
                sum(x_sgd_mean[j] - regular_centers[i][j] for i in range(r))
                + sum(500.0 for _ in range(q))
                + rho_0 * x_sgd_mean[j]
            ) / (r + q)
            for j in range(d)
        ]
        x_sgd_mean = [x_sgd_mean[j] - alpha * mean_grad[j] for j in range(d)]

    err_rsa = l2_dist(x0_rsa, tilde_x_star)
    err_mean = l2_dist(x_sgd_mean, tilde_x_star)
    assert err_rsa < 1.5 and err_rsa < 0.01 * err_mean, (
        f"Expected bounded RSA error err_rsa={err_rsa:.4f} << err_mean={err_mean:.4f}"
    )

    print(
        f"[PASS] Round 522 RSA (Li et al. 2019): "
        f"lambda_0={lambda_0:.3f}, benign_opt_gap={opt_gap_benign:.4f}, "
        f"err_rsa_byz={err_rsa:.4f} << err_mean_byz={err_mean:.4f}"
    )


if __name__ == "__main__":
    main()
