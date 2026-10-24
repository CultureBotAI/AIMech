"""Constructed boundary and numerical verification for Round 434:
EXTRA: An Exact First-Order Algorithm for Decentralized Consensus Optimization
(Wei Shi, Qing Ling, Gang Wu, & Wotao Yin 2015, SIAM J. Optim. 25(2):944-966, arXiv:1404.6264).
"""

from __future__ import annotations

import math


def mat_vec(M: list[list[float]], v: list[float]) -> list[float]:
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


def vec_norm(v: list[float]) -> float:
    return math.sqrt(sum(x * x for x in v))


def main() -> None:
    # 4-node ring graph with symmetric doubly stochastic mixing matrix W
    n = 4
    W = [
        [0.50, 0.25, 0.00, 0.25],
        [0.25, 0.50, 0.25, 0.00],
        [0.00, 0.25, 0.50, 0.25],
        [0.25, 0.00, 0.25, 0.50],
    ]
    # W_tilde = (I + W) / 2 satisfies Assumption 1: (I+W)/2 >= W_tilde >= W and W_tilde > 0
    W_tilde = [[(1.0 if i == j else 0.0) * 0.5 + 0.5 * W[i][j] for j in range(n)] for i in range(n)]
    # Eigenvalues of W on 4-cycle: 1, 0.5, 0.5, 0 -> lambda_min(W_tilde) = 0.5
    lambda_min_W_tilde = 0.5

    # Heterogeneous strongly convex local quadratics f_i(x) = 0.5 * a_i * (x - b_i)^2
    a = [1.5, 2.0, 2.5, 3.0]
    b = [-3.0, 1.0, 4.0, -2.0]
    L_f = max(a)
    x_star = sum(a[i] * b[i] for i in range(n)) / sum(a)

    def grad_f(x: list[float]) -> list[float]:
        return [a[i] * (x[i] - b[i]) for i in range(n)]

    # Theorem 5 step size bound: 0 < alpha < 2 * lambda_min(W_tilde) / L_f = 1.0 / 3.0
    alpha = 0.25
    assert alpha < 2.0 * lambda_min_W_tilde / L_f

    # Verify equivalence of:
    # (A) Two-step recursion Eq. (6)-(7): x^{k+2} = (I + W) x^{k+1} - W_tilde x^k - alpha (grad f(x^{k+1}) - grad f(x^k))
    # (B) Cumulative integral feedback Eq. (11): x^{k+1} = W_tilde x^k - alpha grad f(x^k) + sum_{t=0}^k (W - W_tilde) x^t
    x0 = [2.0, -1.0, 0.5, -2.5]
    g0 = grad_f(x0)
    Wx0 = mat_vec(W, x0)
    x1 = [Wx0[i] - alpha * g0[i] for i in range(n)]

    x_prev, x_curr = x0[:], x1[:]
    x_cum = x0[:]
    cum_diff = [0.0] * n
    max_equiv_err = 0.0

    for k in range(250):
        # Cumulative update from k to k+1
        W_tilde_xc = mat_vec(W_tilde, x_cum)
        gc = grad_f(x_cum)
        Wx_c = mat_vec(W, x_cum)
        for i in range(n):
            cum_diff[i] += Wx_c[i] - W_tilde_xc[i]
        x_cum_next = [W_tilde_xc[i] - alpha * gc[i] + cum_diff[i] for i in range(n)]

        if k == 0:
            equiv_err = vec_norm([x_cum_next[i] - x_curr[i] for i in range(n)])
            max_equiv_err = max(max_equiv_err, equiv_err)
            x_cum = x_cum_next
            continue

        # Two-step update from (x_prev, x_curr) to x_next
        Wx_curr = mat_vec(W, x_curr)
        W_tilde_prev = mat_vec(W_tilde, x_prev)
        g_prev = grad_f(x_prev)
        g_curr = grad_f(x_curr)
        x_next = [
            x_curr[i] + Wx_curr[i] - W_tilde_prev[i] - alpha * (g_curr[i] - g_prev[i])
            for i in range(n)
        ]
        equiv_err = vec_norm([x_cum_next[i] - x_next[i] for i in range(n)])
        max_equiv_err = max(max_equiv_err, equiv_err)
        x_prev, x_curr = x_curr, x_next
        x_cum = x_cum_next

    assert max_equiv_err < 1e-13, f"Equivalence error too large: {max_equiv_err}"

    # Compare EXTRA final error vs fixed-stepsize DGD x^{k+1} = W x^k - alpha grad f(x^k)
    x_dgd = x0[:]
    for _ in range(250):
        Wx = mat_vec(W, x_dgd)
        gd = grad_f(x_dgd)
        x_dgd = [Wx[i] - alpha * gd[i] for i in range(n)]

    extra_err = vec_norm([x_curr[i] - x_star for i in range(n)])
    dgd_err = vec_norm([x_dgd[i] - x_star for i in range(n)])
    assert extra_err < 1e-12, f"EXTRA did not converge to exact optimum: {extra_err}"
    assert dgd_err > 0.5, f"DGD should stall at O(alpha) bias floor: {dgd_err}"

    print(
        f"[PASS] Round 434 EXTRA (Shi et al. 2015): equiv_err={max_equiv_err:.2e}, "
        f"extra_err={extra_err:.2e} << dgd_err={dgd_err:.4f}"
    )


if __name__ == "__main__":
    main()
