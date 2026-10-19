#!/usr/bin/env python3
"""Constructed boundary verification for Round 358:
A Stochastic PCA and SVD Algorithm with an Exponential Convergence Rate (VR-PCA, Shamir 2015).

Verifies:
1. Appendix A Sparse Representation Identity (pp. 17-18): Maintaining w_t = alpha * g + beta * u_tilde
   with scalar invariants gamma = ||alpha * g||^2, delta = <alpha * g, u_tilde>, zeta = ||u_tilde||^2
   produces the exact same unit vector sequence w_t as dense Algorithm 1 updates while requiring O(d_s)
   operations per inner step.
2. Lemma 1 & Theorem 1 (Variance Decay and Geometric Epoch Convergence): Variance of the VR-PCA
   stochastic update ||(x_i x_i^T - A)(w_{t-1} - w_tilde_{s-1})||_2^2 decays to 0 as b_s = 1 - <w_tilde_s, v_1>^2
   contracts geometrically across epochs, outperforming standard Oja's algorithm by orders of magnitude.
"""

import math
import random


def main() -> None:
    rng = random.Random(358)
    n = 40
    d = 6
    # Construct n data points x_i in R^d with dominant first coordinate (eigengap lambda > 0)
    X: list[list[float]] = []
    for i in range(n):
        sign = 1.0 if i % 2 == 0 else -1.0
        row = [
            0.85 * sign + 0.05 * math.sin(i + 1),
            0.35 * math.cos(2 * i + 1),
            0.20 * math.sin(3 * i + 2),
            0.12 * math.cos(5 * i + 3),
            0.08 * math.sin(7 * i + 1),
            0.05 * math.cos(11 * i + 2),
        ]
        norm = math.sqrt(sum(v * v for v in row))
        X.append([v / norm for v in row])

    # Empirical covariance A = (1/n) sum_i x_i x_i^T
    A = [[sum(X[k][i] * X[k][j] for k in range(n)) / n for j in range(d)] for i in range(d)]

    # Compute exact top eigenvector v1 of A via 200 power iterations
    v1 = [1.0 / math.sqrt(d) for _ in range(d)]
    for _ in range(200):
        Av = [sum(A[i][j] * v1[j] for j in range(d)) for i in range(d)]
        nv = math.sqrt(sum(x * x for x in Av))
        v1 = [x / nv for x in Av]
    s1 = sum(v1[i] * sum(A[i][j] * v1[j] for j in range(d)) for i in range(d))

    # 1. Verify Appendix A fast scalar-vector representation vs dense Algorithm 1
    w_tilde = [0.6 * v1[i] + (0.8 if i == 1 else 0.0) for i in range(d)]
    wnorm = math.sqrt(sum(x * x for x in w_tilde))
    w_tilde = [x / wnorm for x in w_tilde]

    eta = 0.15
    m = n
    # Dense epoch
    u_tilde = [sum(A[i][j] * w_tilde[j] for j in range(d)) for i in range(d)]
    w_dense = list(w_tilde)
    # Appendix A fast representation: w_t = alpha * g + beta * u_tilde
    g = list(w_tilde)
    alpha = 1.0
    beta = 0.0
    gamma = sum(x * x for x in g)
    delta = sum(g[i] * u_tilde[i] for i in range(d))
    zeta = sum(x * x for x in u_tilde)

    for _ in range(m):
        it = rng.randrange(n)
        x_it = X[it]
        # Dense update (Algorithm 1 line 8-9)
        dot_wt = sum(x_it[i] * w_dense[i] for i in range(d))
        dot_wtilde = sum(x_it[i] * w_tilde[i] for i in range(d))
        w_prime = [w_dense[i] + eta * (x_it[i] * (dot_wt - dot_wtilde) + u_tilde[i]) for i in range(d)]
        wp_norm = math.sqrt(sum(x * x for x in w_prime))
        w_dense = [x / wp_norm for x in w_prime]

        # Appendix A update
        dot_wt_fast = alpha * sum(x_it[i] * g[i] for i in range(d)) + beta * sum(x_it[i] * u_tilde[i] for i in range(d))
        coeff = eta * (dot_wt_fast - dot_wtilde)
        delta_g = [coeff * x_it[i] for i in range(d)]
        g_dot_dg = sum(g[i] * delta_g[i] for i in range(d))
        dg_sq = sum(x * x for x in delta_g)
        dg_dot_u = sum(delta_g[i] * u_tilde[i] for i in range(d))
        for i in range(d):
            g[i] += delta_g[i] / alpha
        beta += eta
        gamma = gamma + 2.0 * alpha * g_dot_dg + dg_sq
        delta = delta + dg_dot_u
        norm_sq_fast = gamma + 2.0 * beta * delta + (beta * beta) * zeta
        inv_norm = 1.0 / math.sqrt(norm_sq_fast)
        alpha *= inv_norm
        beta *= inv_norm
        gamma *= inv_norm * inv_norm
        delta *= inv_norm

    w_fast = [alpha * g[i] + beta * u_tilde[i] for i in range(d)]
    fast_diff = max(abs(w_dense[i] - w_fast[i]) for i in range(d))
    assert fast_diff < 1e-13, f"Appendix A representation mismatch: {fast_diff}"

    # 2. Verify geometric epoch convergence of b_s = 1 - <w_tilde_s, v_1>^2 and variance decay
    w_vr = list(w_tilde)
    w_oja = list(w_tilde)
    b0 = 1.0 - (sum(w_vr[i] * v1[i] for i in range(d)) ** 2)
    var_epoch_first = 0.0
    var_epoch_last = 0.0
    n_epochs = 12
    step_count = 1
    for s in range(1, n_epochs + 1):
        u_ep = [sum(A[i][j] * w_vr[j] for j in range(d)) for i in range(d)]
        w_curr = list(w_vr)
        ep_var_sum = 0.0
        for _ in range(m):
            it = rng.randrange(n)
            x_it = X[it]
            dot_c = sum(x_it[i] * w_curr[i] for i in range(d))
            dot_s = sum(x_it[i] * w_vr[i] for i in range(d))
            diff_w = [w_curr[i] - w_vr[i] for i in range(d)]
            Adiff = [sum(A[i][j] * diff_w[j] for j in range(d)) for i in range(d)]
            stoch_xi = [eta * (x_it[i] * (dot_c - dot_s) - Adiff[i]) for i in range(d)]
            ep_var_sum += sum(x * x for x in stoch_xi)
            w_p = [w_curr[i] + eta * (x_it[i] * (dot_c - dot_s) + u_ep[i]) for i in range(d)]
            np_val = math.sqrt(sum(x * x for x in w_p))
            w_curr = [x / np_val for x in w_p]

            # Standard Oja update with decaying step size
            eta_oja = 0.5 / (10.0 + step_count)
            step_count += 1
            dot_oja = sum(x_it[i] * w_oja[i] for i in range(d))
            w_oja_p = [w_oja[i] + eta_oja * x_it[i] * dot_oja for i in range(d)]
            noja = math.sqrt(sum(x * x for x in w_oja_p))
            w_oja = [x / noja for x in w_oja_p]
        w_vr = w_curr
        if s == 1:
            var_epoch_first = ep_var_sum / m
        if s == n_epochs:
            var_epoch_last = ep_var_sum / m

    b_vr = 1.0 - (sum(w_vr[i] * v1[i] for i in range(d)) ** 2)
    b_oja = 1.0 - (sum(w_oja[i] * v1[i] for i in range(d)) ** 2)
    assert b_vr < 1e-10 and b_vr < 1e-5 * b_oja
    assert var_epoch_last < 1e-8 * var_epoch_first

    print(
        f"[PASS] Round 358 VR-PCA (Shamir 2015): "
        f"fast_diff={fast_diff:.2e}, b0={b0:.4f}->b_vr={b_vr:.2e}<<b_oja={b_oja:.4e}, "
        f"var_first={var_epoch_first:.3e}->var_last={var_epoch_last:.3e} (s1={s1:.4f})"
    )


if __name__ == "__main__":
    main()
