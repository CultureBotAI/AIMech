#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 557: BEER (Zhao, Li, Li, Richtarik, & Chi, NeurIPS 2022)."""

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


def vec_scale(u, c):
    return [c * a for a in u]


def sq_norm(u):
    return sum(a * a for a in u)


def main():
    rng = random.Random(20220131)
    # 4-worker ring with heterogeneous strongly convex quadratic objectives:
    # f_i(x) = 0.5 * ||x - b_i||^2, where b_i has large inter-client heterogeneity G^2
    n, d = 4, 6
    k_keep = 2  # Top-2 contractive compressor on R^6 -> alpha = k/d = 1/3
    alpha = k_keep / d

    W = [
        [0.50, 0.25, 0.00, 0.25],
        [0.25, 0.50, 0.25, 0.00],
        [0.00, 0.25, 0.50, 0.25],
        [0.25, 0.00, 0.25, 0.50],
    ]
    # Eigenvalues of W: 1, 0, 0, -0.5? Wait: for 4-ring [0.5, 0.25, 0, 0.25], eigenvalues are 1, 0.5, 0.5, 0 -> rho = 1 - 0.5 = 0.5
    b_clients = [[(i - 1.5) * 8.0 * ((-1) ** c) + rng.gauss(0.0, 0.5) for c in range(d)] for i in range(n)]
    # Global optimum x* = (1/n) sum_i b_i
    x_star = [sum(b_clients[i][c] for i in range(n)) / n for c in range(d)]

    def grad_i(i, x):
        return [x[c] - b_clients[i][c] for c in range(d)]

    def grad_global(x):
        return [x[c] - x_star[c] for c in range(d)]

    # Initialize X^0 = x_0 1^T, H^0 = 0, G^0 = 0, V^0 = grad F(X^0)
    x0 = [2.0 for _ in range(d)]
    X = [x0[:] for _ in range(n)]
    H = [[0.0] * d for _ in range(n)]
    G = [[0.0] * d for _ in range(n)]
    V = [grad_i(i, X[i]) for i in range(n)]

    gamma = 0.25
    eta = 0.05

    # Verify Definition 2.2 (alpha-contractive property of Top-k)
    for i in range(n):
        diff = vec_sub(X[i], H[i])
        comp = top_k(diff, k_keep)
        assert sq_norm(vec_sub(comp, diff)) <= (1.0 - alpha) * sq_norm(diff) + 1e-12

    init_grad_sq = sq_norm(grad_global(x0))

    # Run BEER (Algorithm 1, p. 7) for T = 250 iterations and verify Lemma B.3 at every step
    for t in range(250):
        # Verify Lemma B.3 (Eq. 11): v_bar^t == (1/n) sum_i grad f_i(x_i^t)
        v_bar = [sum(V[i][c] for i in range(n)) / n for c in range(d)]
        true_mean_grad = [sum(grad_i(i, X[i])[c] for i in range(n)) / n for c in range(d)]
        assert sq_norm(vec_sub(v_bar, true_mean_grad)) < 1e-20

        x_bar_prev = [sum(X[i][c] for i in range(n)) / n for c in range(d)]

        # Line 3: X^{t+1} = X^t + gamma * H^t (W - I) - eta * V^t
        X_next = []
        for i in range(n):
            mix_h = [sum(H[j][c] * (W[j][i] - (1.0 if j == i else 0.0)) for j in range(n)) for c in range(d)]
            x_new = [X[i][c] + gamma * mix_h[c] - eta * V[i][c] for c in range(d)]
            X_next.append(x_new)

        # Verify Lemma B.3 (Eq. 12): x_bar^{t+1} == x_bar^t - (eta/n) sum_i grad f_i(x_i^t)
        x_bar_next = [sum(X_next[i][c] for i in range(n)) / n for c in range(d)]
        expected_x_bar_next = vec_sub(x_bar_prev, vec_scale(true_mean_grad, eta))
        assert sq_norm(vec_sub(x_bar_next, expected_x_bar_next)) < 1e-20

        # Lines 4-5: Q_h^{t+1} = C(X^{t+1} - H^t), H^{t+1} = H^t + Q_h^{t+1}
        H_next = [vec_add(H[i], top_k(vec_sub(X_next[i], H[i]), k_keep)) for i in range(n)]

        # Line 6: V^{t+1} = V^t + gamma * G^t (W - I) + grad F(X^{t+1}) - grad F(X^t)
        V_next = []
        for i in range(n):
            mix_g = [sum(G[j][c] * (W[j][i] - (1.0 if j == i else 0.0)) for j in range(n)) for c in range(d)]
            g_diff = vec_sub(grad_i(i, X_next[i]), grad_i(i, X[i]))
            v_new = [V[i][c] + gamma * mix_g[c] + g_diff[c] for c in range(d)]
            V_next.append(v_new)

        # Lines 7-8: Q_g^{t+1} = C(V^{t+1} - G^t), G^{t+1} = G^t + Q_g^{t+1}
        G_next = [vec_add(G[i], top_k(vec_sub(V_next[i], G[i]), k_keep)) for i in range(n)]

        X, H, V, G = X_next, H_next, V_next, G_next

    x_bar_final = [sum(X[i][c] for i in range(n)) / n for c in range(d)]
    final_grad_sq = sq_norm(grad_global(x_bar_final))
    consensus_err = sum(sq_norm(vec_sub(X[i], x_bar_final)) for i in range(n)) / n
    assert final_grad_sq < 1e-6 * init_grad_sq
    assert consensus_err < 1e-5

    print(
        f"[PASS] Round 557 BEER verified: grad_sq {init_grad_sq:.4f} -> {final_grad_sq:.3e}, "
        f"consensus_err={consensus_err:.3e}"
    )


if __name__ == "__main__":
    main()
