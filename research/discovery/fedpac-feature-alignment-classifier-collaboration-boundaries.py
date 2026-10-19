#!/usr/bin/env python3
"""Constructed boundary verification for FedPAC (Xu, Tong, & Huang, ICLR 2023, arXiv:2306.11867)."""

import math
import random

def project_simplex(v):
    n = len(v)
    u = sorted(v, reverse=True)
    cssv = 0.0
    rho = -1
    for i in range(n):
        cssv += u[i]
        t = (cssv - 1.0) / (i + 1)
        if u[i] - t > 0:
            rho = i
    theta = (sum(u[: rho + 1]) - 1.0) / (rho + 1)
    return [max(0.0, x - theta) for x in v]

def solve_fedpac_qp(V, D, n_samples, steps=400, lr=0.05):
    m = len(V)
    alpha = [1.0 / m for _ in range(m)]
    for _ in range(steps):
        grad = []
        for j in range(m):
            g_j = 2.0 * alpha[j] * V[j] / n_samples[j] + 2.0 * sum(D[j][jp] * alpha[jp] for jp in range(m))
            grad.append(g_j)
        alpha = project_simplex([alpha[j] - lr * grad[j] for j in range(m)])
    return alpha

def main():
    rng = random.Random(460)
    # 4 clients in 2 cluster groups (Clients 0,1 share distribution Group A; Clients 2,3 share distribution Group B)
    m = 4
    K = 3
    d = 4
    true_priors = [
        [0.70, 0.20, 0.10],
        [0.70, 0.20, 0.10],
        [0.10, 0.20, 0.70],
        [0.10, 0.20, 0.70],
    ]
    true_means = [
        [1.5, 0.0, -0.5, 0.2],
        [-1.0, 1.2, 0.5, -0.3],
        [0.2, -1.3, 1.0, 0.8],
    ]
    n_samples = [40, 40, 40, 40]

    # Sample empirical feature statistics for each client
    P_hat = []
    mu_hat = []
    V_stat = []
    g_hat = []
    for i in range(m):
        counts = [max(1, int(round(n_samples[i] * true_priors[i][y]))) for y in range(K)]
        n_i = sum(counts)
        n_samples[i] = n_i
        p_i = [counts[y] / n_i for y in range(K)]
        P_hat.append(p_i)
        mu_i = []
        v_i = 0.0
        g_i = []
        for y in range(K):
            feats = [[true_means[y][ dim ] + rng.gauss(0.0, 0.6) for dim in range(d)] for _ in range(counts[y])]
            mean_y = [sum(f[dim] for f in feats) / counts[y] for dim in range(d)]
            tr_lam_y = sum(sum(f[dim] ** 2 for dim in range(d)) for f in feats) / counts[y]
            mu_i.append(mean_y)
            norm_sq = sum((p_i[y] * mean_y[dim]) ** 2 for dim in range(d))
            v_i += p_i[y] * tr_lam_y - norm_sq
            # Eq. (28) with Lambda_f = I_d and P_Y(y) = 1/K: g_hat_i(y) = K * P_hat_Y^{(i)}(y) * mu_{i,y}
            g_i.append([K * p_i[y] * mean_y[dim] for dim in range(d)])
        mu_hat.append(mu_i)
        V_stat.append(v_i)
        g_hat.append(g_i)

    # Compute D_{jj'} for target client i=0 via Eq. (45)-(46)
    i_target = 0
    h = [[[P_hat[l][y] * mu_hat[l][y][dim] for dim in range(d)] for y in range(K)] for l in range(m)]
    D_mat = [[0.0 for _ in range(m)] for _ in range(m)]
    for j in range(m):
        for jp in range(m):
            val = 0.0
            for y in range(K):
                for dim in range(d):
                    val += (h[i_target][y][dim] - h[j][y][dim]) * (h[i_target][y][dim] - h[jp][y][dim])
            D_mat[j][jp] = val

    alpha_opt = solve_fedpac_qp(V_stat, D_mat, n_samples)
    # Client 0 and Client 1 belong to Group A; Clients 2 and 3 belong to Group B
    group_a_weight = alpha_opt[0] + alpha_opt[1]
    group_b_weight = alpha_opt[2] + alpha_opt[3]
    assert group_a_weight > 0.85, f"Expected same-group weight > 0.85, got {alpha_opt}"
    assert alpha_opt[1] > 0.25, f"Expected peer client 1 weight > 0.25, got {alpha_opt}"
    assert group_b_weight < 0.15, f"Expected unrelated-group weight < 0.15, got {alpha_opt}"

    # Verify QP objective R_0(alpha_opt) < R_0(local-only) and R_0(uniform)
    def qp_risk(alpha):
        var_term = sum((alpha[j] ** 2) * V_stat[j] / n_samples[j] for j in range(m))
        bias_term = sum(alpha[j] * alpha[jp] * D_mat[j][jp] for j in range(m) for jp in range(m))
        return var_term + bias_term

    r_opt = qp_risk(alpha_opt)
    r_local = qp_risk([1.0, 0.0, 0.0, 0.0])
    r_unif = qp_risk([0.25, 0.25, 0.25, 0.25])
    assert r_opt < r_local and r_opt < r_unif, f"Expected r_opt={r_opt} < min(r_local={r_local}, r_unif={r_unif})"

    print(
        f"[PASS] Round 460 FedPAC verified: alpha_opt={[round(a, 3) for a in alpha_opt]}, "
        f"R_opt={r_opt:.4f} < R_local={r_local:.4f} < R_unif={r_unif:.4f}"
    )

if __name__ == "__main__":
    main()
