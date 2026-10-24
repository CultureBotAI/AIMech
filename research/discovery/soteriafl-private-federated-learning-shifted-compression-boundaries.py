#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 561: SoteriaFL (Li, Zhao, Li, & Chi, NeurIPS 2022)."""

import math
import random


def rand_k_compress(vec, k, rng):
    d = len(vec)
    chosen = set(rng.sample(range(d), k))
    scale = d / k
    return [scale * v if idx in chosen else 0.0 for idx, v in enumerate(vec)]


def vec_add(u, v):
    return [a + b for a, b in zip(u, v)]


def vec_sub(u, v):
    return [a - b for a, b in zip(u, v)]


def vec_scale(u, c):
    return [c * a for a in u]


def sq_norm(u):
    return sum(a * a for a in u)


def main():
    rng = random.Random(20220620)
    n, d, k = 10, 6, 2
    omega = (d / k) - 1.0  # omega = 2.0

    # 1. Verify Lemma 7 optimal shift step size gamma_t = sqrt((1 + 2*omega) / (2 * (1 + omega)^3))
    # and contraction factor 1 - 1 / (2 * (1 + omega))
    beta_t = 1.0 / (1.0 + 2.0 * omega)
    gamma_t = math.sqrt((1.0 + 2.0 * omega) / (2.0 * ((1.0 + omega) ** 3)))
    contraction_coeff = (1.0 + beta_t) * (1.0 - 2.0 * gamma_t + (gamma_t ** 2) * (1.0 + omega))
    expected_contraction = 1.0 - 1.0 / (2.0 * (1.0 + omega))
    # Verify algebraic identity in Proof of Lemma 7 (p. 28, Eq. 31-32):
    # (1 + 1/(1+2w)) * (1 - 2*gamma_t + gamma_t^2*(1+w)) <= 1 - 1/(2*(1+w))
    assert contraction_coeff <= expected_contraction + 1e-12

    # 2. Compare SoteriaFL (shifted compression of LDP gradients) vs CDP-SGD (direct compression of LDP gradients)
    # on a heterogeneous distributed quadratic objective where ||grad f_i(x*)||^2 > 0
    targets = [[(i - 4.5) * 4.0 * ((-1) ** c) for c in range(d)] for i in range(n)]
    x_star = [sum(targets[i][c] for i in range(n)) / n for c in range(d)]

    def grad_i(i, x):
        return [x[c] - targets[i][c] for c in range(d)]

    sigma_p = 0.05  # LDP Gaussian perturbation scale
    eta = 0.08
    T = 180

    # Baseline CDP-SGD (Algorithm 1): v_i^t = C_i^t(grad f_i(x^t) + xi_i^t)
    # Direct compression amplifies client heterogeneity omega * ||grad f_i(x^t)||^2 / n
    x_cdp = [3.0] * d
    for _ in range(T):
        v_sum = [0.0] * d
        for i in range(n):
            g_priv = [grad_i(i, x_cdp)[c] + rng.gauss(0.0, sigma_p) for c in range(d)]
            v_i = rand_k_compress(g_priv, k, rng)
            v_sum = vec_add(v_sum, v_i)
        v_t = vec_scale(v_sum, 1.0 / n)
        x_cdp = vec_sub(x_cdp, vec_scale(v_t, eta))

    # SoteriaFL (Algorithm 2): v_i^t = C_i^t(g_i^t - s_i^t), s_i^{t+1} = s_i^t + gamma_t * v_i^t
    x_sot = [3.0] * d
    s_clients = [[0.0] * d for _ in range(n)]
    s_bar = [0.0] * d
    for _ in range(T):
        v_sum = [0.0] * d
        for i in range(n):
            g_priv = [grad_i(i, x_sot)[c] + rng.gauss(0.0, sigma_p) for c in range(d)]
            v_i = rand_k_compress(vec_sub(g_priv, s_clients[i]), k, rng)
            s_clients[i] = vec_add(s_clients[i], vec_scale(v_i, gamma_t))
            v_sum = vec_add(v_sum, v_i)
        v_avg = vec_scale(v_sum, 1.0 / n)
        v_t = vec_add(s_bar, v_avg)
        x_sot = vec_sub(x_sot, vec_scale(v_t, eta))
        s_bar = vec_add(s_bar, vec_scale(v_avg, gamma_t))
        # Verify invariant s_bar == (1/n) sum_i s_i^t
        s_mean = [sum(s_clients[i][c] for i in range(n)) / n for c in range(d)]
        assert sq_norm(vec_sub(s_bar, s_mean)) < 1e-22

    cdp_err = sq_norm(vec_sub(x_cdp, x_star))
    sot_err = sq_norm(vec_sub(x_sot, x_star))
    # Shifted compression eliminates the O(omega * G^2) heterogeneity variance floor of direct compression
    assert sot_err < 0.05 * cdp_err

    print(
        f"[PASS] Round 561 SoteriaFL verified: gamma_t={gamma_t:.4f}, "
        f"contraction={contraction_coeff:.4f}<={expected_contraction:.4f}, "
        f"sot_err={sot_err:.4e} << cdp_err={cdp_err:.4e}"
    )


if __name__ == "__main__":
    main()
