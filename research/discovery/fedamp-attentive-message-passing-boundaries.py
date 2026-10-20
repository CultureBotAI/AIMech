#!/usr/bin/env python3
"""Constructed boundary verification for FedAMP and HeurFedAMP (Huang et al., AAAI 2021, arXiv:2007.03797)."""

import math

def sq_dist(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))

def cosine_sim(a, b):
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return sum(x * y for x, y in zip(a, b)) / (na * nb)

def main():
    # 4 clients in 2 groups: Group 1 = {0, 1} around [2.0, 2.0], Group 2 = {2, 3} around [-2.0, -2.0]
    m = 4
    targets = [
        [2.0, 1.8],
        [1.8, 2.0],
        [-2.0, -1.8],
        [-1.8, -2.0],
    ]
    W = [[t[0] + (0.4 if i % 2 == 0 else -0.4), t[1] - (0.3 if i % 2 == 0 else -0.3)] for i, t in enumerate(targets)]
    sigma = 2.0
    alpha_k = 0.25
    lam = 1.0

    # 1. Verify Definition 1 & Eq. (5)-(7): A(t) = 1 - exp(-t/sigma), A'(t) = (1/sigma) exp(-t/sigma)
    def A_func(t):
        return 1.0 - math.exp(-t / sigma)

    def A_deriv(t):
        return (1.0 / sigma) * math.exp(-t / sigma)

    def G_obj(W_mat):
        f_term = sum(0.5 * sq_dist(W_mat[i], targets[i]) for i in range(m))
        a_term = sum(A_func(sq_dist(W_mat[i], W_mat[j])) for i in range(m) for j in range(i + 1, m))
        return f_term + lam * a_term

    g_init = G_obj(W)
    for _ in range(40):
        # Server step (Eq. 5 & 7): compute personalized cloud models u_i^k = sum_j xi_{i,j} w_j^{k-1}
        U = []
        xi_mat = []
        for i in range(m):
            xi_row = [0.0 for _ in range(m)]
            for j in range(m):
                if j != i:
                    xi_row[j] = alpha_k * A_deriv(sq_dist(W[i], W[j]))
                    assert xi_row[j] > 0.0
            xi_row[i] = 1.0 - sum(xi_row[j] for j in range(m) if j != i)
            assert xi_row[i] > 0.0, f"Self-weight xi_{{i,i}} must be positive, got {xi_row[i]}"
            assert abs(sum(xi_row) - 1.0) < 1e-14
            xi_mat.append(xi_row)
            u_i = [sum(xi_row[j] * W[j][d] for j in range(m)) for d in range(2)]
            U.append(u_i)

        # Client proximal step (Eq. 6): w_i^k = argmin_w 0.5 ||w - target_i||^2 + (lam / (2 * alpha_k)) ||w - u_i^k||^2
        gamma = lam / alpha_k
        W = [[(targets[i][d] + gamma * U[i][d]) / (1.0 + gamma) for d in range(2)] for i in range(m)]

    g_final = G_obj(W)
    assert g_final < g_init
    # Within-group collaboration weight xi_{0,1} must strictly exceed cross-group weight xi_{0,2}
    assert xi_mat[0][1] > 10.0 * xi_mat[0][2], f"Expected block-diagonal collaboration: {xi_mat[0]}"

    # 2. Verify HeurFedAMP cosine-similarity weights (Section 6, Eq. 8)
    xi_self = 0.5
    sigma_cos = 3.0
    heur_xi = []
    for i in range(m):
        exps = [math.exp(sigma_cos * cosine_sim(W[i], W[h])) if h != i else 0.0 for h in range(m)]
        denom = sum(exps)
        row = [(1.0 - xi_self) * exps[j] / denom if j != i else xi_self for j in range(m)]
        assert abs(sum(row) - 1.0) < 1e-14
        assert all(w >= 0.0 for w in row)
        heur_xi.append(row)
    assert heur_xi[0][1] > 20.0 * heur_xi[0][2]

    print(
        f"[PASS] Round 465 FedAMP verified: G(W)={g_init:.4f}->{g_final:.4f}, "
        f"xi_01={xi_mat[0][1]:.4f}>>xi_02={xi_mat[0][2]:.5f}, heur_xi_01={heur_xi[0][1]:.4f}"
    )

if __name__ == "__main__":
    main()
