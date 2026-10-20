#!/usr/bin/env python3
"""Constructed boundary verification for DeTAG (Lu & De Sa, ICML 2021 / arXiv:2006.08085).

Verifies:
1. R-step Accelerated Gossip (Algorithm 3):
   eta = (1 - sqrt(1 - lambda^2)) / (1 + sqrt(1 - lambda^2)),
   z_{r+1} = (1 + eta)*W*z_r - eta*z_{r-1},
   contracting consensus error at geometric rate rho = O((1 - sqrt(1 - lambda^2))^R),
   strictly faster than standard unaccelerated R-step gossip W^R (rate lambda^R).
2. DeTAG by-phase gradient tracking (Algorithm 2):
   y_0 = G_0, x_{k+1} = AG_R(x_k) - alpha * y_k, y_{k+1} = AG_R(y_k) + g_(k+1) - g_(k),
   preserving the exact global average (1/n)*sum_i y_{k,i} == (1/n)*sum_i g_{(k),i} across phases
   and converging to the exact global optimum on heterogeneous quadratics where D-PSGD drifts.
"""

import math


def make_ring_gossip_matrix(n):
    W = [[0.0] * n for _ in range(n)]
    for i in range(n):
        W[i][i] = 0.5
        W[i][(i - 1) % n] = 0.25
        W[i][(i + 1) % n] = 0.25
    # Second largest eigenvalue magnitude on n-ring with weights (1/4, 1/2, 1/4)
    lam = max(abs(0.5 + 0.5 * math.cos(2.0 * math.pi * k / n)) for k in range(1, n))
    return W, lam


def mat_vec(W, z):
    n = len(W)
    return [sum(W[i][j] * z[j] for j in range(n)) for i in range(n)]


def accelerated_gossip(z0, W, lam, R):
    n = len(z0)
    eta = (1.0 - math.sqrt(1.0 - lam * lam)) / (1.0 + math.sqrt(1.0 - lam * lam))
    z_prev = list(z0)
    z_curr = list(z0)
    for _ in range(R):
        Wz = mat_vec(W, z_curr)
        z_next = [(1.0 + eta) * Wz[i] - eta * z_prev[i] for i in range(n)]
        z_prev = z_curr
        z_curr = z_next
    return z_curr


def standard_gossip(z0, W, R):
    z = list(z0)
    for _ in range(R):
        z = mat_vec(W, z)
    return z


def consensus_err(z):
    mean = sum(z) / len(z)
    return math.sqrt(sum((v - mean) ** 2 for v in z))


def verify_detag_boundaries():
    n = 12
    W, lam = make_ring_gossip_matrix(n)
    R = 8
    z0 = [
        10.0 * math.cos(2.0 * math.pi * i / n) + 4.0 * math.sin(4.0 * math.pi * i / n) + 3.0
        for i in range(n)
    ]

    # 1. Verify Accelerated Gossip achieves strictly smaller consensus error than standard R-step gossip
    z_ag = accelerated_gossip(z0, W, lam, R)
    z_std = standard_gossip(z0, W, R)
    err_ag = consensus_err(z_ag)
    err_std = consensus_err(z_std)
    assert err_ag < 0.4 * err_std, f"Expected AG error << standard gossip error: {err_ag} vs {err_std}"
    # Verify exact mean preservation: (1/n)*sum(AG(z0)) == (1/n)*sum(z0)
    assert abs(sum(z_ag) / n - sum(z0) / n) < 1e-12

    # 2. Verify DeTAG Algorithm 2 phase updates and exact gradient tracker mean invariant (Equation 60)
    # Heterogeneous local objectives f_i(x) = 0.5 * (x - b_i)^2 with sum(b_i) == 0 => x* = 0
    b = [15.0 * (i - (n - 1) / 2.0) for i in range(n)]
    assert abs(sum(b)) < 1e-12

    x = [4.0 for _ in range(n)]
    g_prev = [x[i] - b[i] for i in range(n)]
    y = list(g_prev)  # initialized tracker y_0 = g_0
    alpha = 0.15

    for _ in range(60):
        x_tilde = accelerated_gossip(x, W, lam, R)
        y_ag = accelerated_gossip(y, W, lam, R)
        x_next = [x_tilde[i] - alpha * y[i] for i in range(n)]
        g_curr = [x_next[i] - b[i] for i in range(n)]
        y_next = [y_ag[i] + g_curr[i] - g_prev[i] for i in range(n)]

        # Equation (60) invariant: mean(y_next) == mean(g_curr)
        assert abs(sum(y_next) / n - sum(g_curr) / n) < 1e-10, "Tracker mean invariant violated!"
        x = x_next
        y = y_next
        g_prev = g_curr

    detag_err = max(abs(xi) for xi in x)
    assert detag_err < 1e-3, f"DeTAG failed to converge to x*=0: {detag_err}"

    print(
        f"[PASS] DeTAG boundaries verified: err_ag={err_ag:.4f} < err_std={err_std:.4f}, "
        f"detag_max_err={detag_err:.2e}"
    )


if __name__ == "__main__":
    verify_detag_boundaries()
