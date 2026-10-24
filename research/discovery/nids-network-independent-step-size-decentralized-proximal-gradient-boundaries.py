#!/usr/bin/env python3
"""Boundary verification for Round 440: NIDS (Li, Shi, & Yan 2019, IEEE TSP 67(17):4494-4506, arXiv:1704.07807)."""
import math

def soft_threshold(v, thresh):
    return [math.copysign(max(abs(x) - thresh, 0.0), x) for x in v]

def main():
    # 3-node ring/chain graph with doubly stochastic mixing matrix W
    # W has eigenvalues: lambda_1 = 1, lambda_2 = 0.2, lambda_3 = -0.6
    # Construct symmetric doubly stochastic W with eigenvalues (1, 0.2, -0.6):
    # v1 = [1,1,1]/sqrt(3), v2 = [1,0,-1]/sqrt(2), v3 = [1,-2,1]/sqrt(6)
    v1 = [1.0 / math.sqrt(3.0)] * 3
    v2 = [1.0 / math.sqrt(2.0), 0.0, -1.0 / math.sqrt(2.0)]
    v3 = [1.0 / math.sqrt(6.0), -2.0 / math.sqrt(6.0), 1.0 / math.sqrt(6.0)]
    lams = [1.0, 0.2, -0.6]
    vecs = [v1, v2, v3]
    W = [[0.0] * 3 for _ in range(3)]
    for r in range(3):
        for c in range(3):
            W[r][c] = sum(lams[k] * vecs[k][r] * vecs[k][c] for k in range(3))

    # Verify W is symmetric and doubly stochastic
    for r in range(3):
        assert abs(sum(W[r]) - 1.0) < 1e-12
    # Local heterogeneous smooth quadratic objectives s_i(x) = 0.5 * L_i * (x - b_i)^2
    # plus shared nonsmooth L1 regularizer r(x) = gamma_l1 * |x|
    L_list = [4.0, 4.0, 4.0]
    L_max = max(L_list)
    mu_min = min(L_list)
    b_list = [3.0, -1.0, 4.0]
    gamma_l1 = 0.5

    # Exact global composite minimizer of (1/3)*sum_i 0.5*L_i*(x - b_i)^2 + gamma_l1*|x|
    # Mean of b_i is 2.0, average curvature is 4.0 -> unconstrained mean = 2.0, soft-threshold by gamma_l1/4.0 = 0.125
    x_star = 2.0 - gamma_l1 / L_max  # 1.875

    # Network-independent step-size alpha = 1 / L_max = 0.25
    # Note: PG-EXTRA upper bound is (1 + lambda_3(W)) / L_max = (1 - 0.6) / 4.0 = 0.10 < 0.25!
    alpha = 1.0 / L_max
    pg_extra_max_alpha = (1.0 + lams[2]) / L_max
    assert alpha > pg_extra_max_alpha

    # Remark 4 optimal coupling parameter c = 1 / ((1 - lambda_n(W)) * alpha)
    c_coup = 1.0 / ((1.0 - lams[2]) * alpha)
    # W_tilde = I - c * alpha * (I - W)
    W_tilde = [[(1.0 if r == c else 0.0) - c_coup * alpha * ((1.0 if r == c else 0.0) - W[r][c]) for c in range(3)] for r in range(3)]

    # Run NIDS (Eq. 8a-8b) vs PG-EXTRA at network-independent step size alpha = 1/L_max
    x_nids = [0.0, 0.0, 0.0]
    z_nids = [0.0, 0.0, 0.0]
    # k=0 initialization: z^1 = x^0 - alpha * grad s(x^0), x^1 = prox(z^1)
    grad0 = [L_list[i] * (x_nids[i] - b_list[i]) for i in range(3)]
    z_nids = [x_nids[i] - alpha * grad0[i] for i in range(3)]
    x_prev = x_nids[:]
    grad_prev = grad0[:]
    x_nids = soft_threshold(z_nids, alpha * gamma_l1)

    # PG-EXTRA at same alpha = 1/L_max (exceeding (1+lambda_n)/L)
    x_pge = [0.0, 0.0, 0.0]
    W_half = [[0.5 * ((1.0 if r == c else 0.0) + W[r][c]) for c in range(3)] for r in range(3)]
    z_pge = [sum(W[i][j] * x_pge[j] for j in range(3)) - alpha * grad0[i] for i in range(3)]
    x_pge_prev = x_pge[:]
    grad_pge_prev = grad0[:]
    x_pge = soft_threshold(z_pge, alpha * gamma_l1)

    for _ in range(120):
        grad_cur = [L_list[i] * (x_nids[i] - b_list[i]) for i in range(3)]
        vec_in = [2.0 * x_nids[i] - x_prev[i] - alpha * grad_cur[i] + alpha * grad_prev[i] for i in range(3)]
        wt_vec = [sum(W_tilde[i][j] * vec_in[j] for j in range(3)) for i in range(3)]
        z_next = [z_nids[i] - x_nids[i] + wt_vec[i] for i in range(3)]
        x_prev = x_nids[:]
        grad_prev = grad_cur[:]
        z_nids = z_next
        x_nids = soft_threshold(z_nids, alpha * gamma_l1)

        # PG-EXTRA step: z^{k+1} = z^k + W x^k - W_half x^{k-1} - alpha*(grad(x^k) - grad(x^{k-1}))
        grad_pge_cur = [L_list[i] * (x_pge[i] - b_list[i]) for i in range(3)]
        wx = [sum(W[i][j] * x_pge[j] for j in range(3)) for i in range(3)]
        whx = [sum(W_half[i][j] * x_pge_prev[j] for j in range(3)) for i in range(3)]
        z_pge_next = [z_pge[i] + wx[i] - whx[i] - alpha * (grad_pge_cur[i] - grad_pge_prev[i]) for i in range(3)]
        x_pge_prev = x_pge[:]
        grad_pge_prev = grad_pge_cur[:]
        z_pge = z_pge_next
        x_pge = soft_threshold(z_pge, alpha * gamma_l1)

    nids_err = max(abs(x - x_star) for x in x_nids)
    pge_err = max(abs(x - x_star) for x in x_pge)
    # Theorem 2 / Remark 4 decoupled linear convergence factor:
    rho_decoupled = max(1.0 - mu_min / L_max, (lams[1] - lams[2]) / (1.0 - lams[2]))
    assert nids_err < 1e-12, f"Expected NIDS exact convergence, got {nids_err}"
    assert pge_err > 1e5, f"Expected PG-EXTRA divergence above (1+lambda_n)/L, got {pge_err}"
    assert abs(rho_decoupled - 0.5) < 1e-12
    print(f"[PASS] Round 440 NIDS (Li, Shi, & Yan 2019): nids_err={nids_err:.2e} << pge_err={pge_err:.2e}, alpha={alpha:.2f} > pge_max={pg_extra_max_alpha:.2f}, rho_decoupled={rho_decoupled:.4f}")

if __name__ == "__main__":
    main()
