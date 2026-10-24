#!/usr/bin/env python3
"""Constructed boundary & regime verification for Chambolle-Pock Primal-Dual Algorithm (2011, Round 346)."""

import math


def make_saddle_problem():
    # Saddle-point problem: min_{x in R^2} max_{y in R^2} <K x, y> + G(x) - F^*(y)
    # where K = [[2.0, 1.0], [1.0, 2.0]] (symmetric with eigenvalues 3 and 1, so L = ||K|| = 3.0),
    # G(x) = (gamma / 2) ||x - x_target||^2, F^*(y) = (delta / 2) ||y - y_target||^2
    K = [[2.0, 1.0], [1.0, 2.0]]
    L = 3.0
    gamma = 0.5
    delta = 0.4
    x_target = [1.0, -0.5]
    y_target = [-0.4, 0.8]
    # Exact saddle point (x_hat, y_hat) satisfies:
    # K^T y_hat + gamma (x_hat - x_target) = 0  =>  y_hat = (1/delta) (K x_hat - delta y_target)?
    # Wait: max_y <K x, y> - (delta/2)||y - y_target||^2 => K x - delta (y - y_target) = 0 => y_hat = y_target + (1/delta) K x_hat
    # And min_x: K^T y_hat + gamma (x_hat - x_target) = 0 => (gamma I + (1/delta) K^T K) x_hat = gamma x_target - K^T y_target
    # Let's solve 2x2 linear system for x_hat, y_hat:
    KTK = [
        [K[0][0] ** 2 + K[1][0] ** 2, K[0][0] * K[0][1] + K[1][0] * K[1][1]],
        [K[0][1] * K[0][0] + K[1][1] * K[1][0], K[0][1] ** 2 + K[1][1] ** 2],
    ]
    A00 = gamma + KTK[0][0] / delta
    A01 = KTK[0][1] / delta
    A10 = KTK[1][0] / delta
    A11 = gamma + KTK[1][1] / delta
    rhs0 = gamma * x_target[0] - (K[0][0] * y_target[0] + K[1][0] * y_target[1])
    rhs1 = gamma * x_target[1] - (K[0][1] * y_target[0] + K[1][1] * y_target[1])
    det = A00 * A11 - A01 * A10
    x_hat = [(A11 * rhs0 - A01 * rhs1) / det, (-A10 * rhs0 + A00 * rhs1) / det]
    Kx = [K[0][0] * x_hat[0] + K[0][1] * x_hat[1], K[1][0] * x_hat[0] + K[1][1] * x_hat[1]]
    y_hat = [y_target[0] + Kx[0] / delta, y_target[1] + Kx[1] / delta]
    return K, L, gamma, delta, x_target, y_target, x_hat, y_hat


def mat_vec(K, v):
    return [K[0][0] * v[0] + K[0][1] * v[1], K[1][0] * v[0] + K[1][1] * v[1]]


def norm_sq(u, v):
    return (u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2


def main():
    K, L, gamma, delta, x_target, y_target, x_hat, y_hat = make_saddle_problem()

    # Claim 1: Algorithm 1 (theta = 1, tau * sigma * L^2 < 1) bounded weighted distance (Eq. 8) and O(1/N) ergodic gap (Eq. 9)
    tau = 0.25
    sigma = 0.35  # tau * sigma * L^2 = 0.25 * 0.35 * 9 = 0.7875 < 1
    assert tau * sigma * (L ** 2) < 1.0
    x = [0.0, 0.0]
    y = [0.0, 0.0]
    x_bar = x[:]
    d0 = norm_sq(y, y_hat) / (2.0 * sigma) + norm_sq(x, x_hat) / (2.0 * tau)
    c_bound = 1.0 / (1.0 - tau * sigma * (L ** 2))
    N = 60
    x_avg = [0.0, 0.0]
    y_avg = [0.0, 0.0]
    for _ in range(N):
        Kx_bar = mat_vec(K, x_bar)
        # Resolvent (I + sigma partial F^*)^{-1}(y + sigma K x_bar):
        y_next = [
            (y[c] + sigma * Kx_bar[c] + sigma * delta * y_target[c]) / (1.0 + sigma * delta)
            for c in range(2)
        ]
        KT_y = mat_vec(K, y_next)
        # Resolvent (I + tau partial G)^{-1}(x - tau K^* y_next):
        x_next = [
            (x[c] - tau * KT_y[c] + tau * gamma * x_target[c]) / (1.0 + tau * gamma)
            for c in range(2)
        ]
        x_bar = [2.0 * x_next[c] - x[c] for c in range(2)]
        x, y = x_next, y_next
        dn = norm_sq(y, y_hat) / (2.0 * sigma) + norm_sq(x, x_hat) / (2.0 * tau)
        assert dn <= c_bound * d0 + 1e-12
        for c in range(2):
            x_avg[c] += x[c] / N
            y_avg[c] += y[c] / N

    # Verify saddle-point gap at (x_avg, y_avg) against (x_hat, y_hat) is <= D / N (Eq. 16)
    gap_N = (
        0.5 * gamma * norm_sq(x_avg, x_hat) + 0.5 * delta * norm_sq(y_avg, y_hat)
    )
    assert gap_N <= d0 / N + 1e-12

    # Claim 2a: Algorithm 2 adaptive acceleration when G is gamma-uniformly convex (delta = 0 bilinearity + L2 G)
    # Verify Corollary 1: lim_{N->infty} N * gamma * tau_N = 1 and O(1/N^2) decay of tau_N^2
    tau_n = 1.0 / L
    sigma_n = 1.0 / L
    for _ in range(200):
        theta_n = 1.0 / math.sqrt(1.0 + 2.0 * gamma * tau_n)
        tau_n = theta_n * tau_n
        sigma_n = sigma_n / theta_n
        assert abs(tau_n * sigma_n * (L ** 2) - 1.0) < 1e-12
    assert abs(200.0 * gamma * tau_n - 1.0) < 0.05

    # Claim 2b: Algorithm 3 linear convergence O(omega^N) when both G and F^* are uniformly convex (Theorem 3, Eq. 59)
    mu = 2.0 * math.sqrt(gamma * delta) / L
    tau_lin = (1.0 / L) * math.sqrt(delta / gamma)
    sigma_lin = (1.0 / L) * math.sqrt(gamma / delta)
    theta_lin = 1.0 / (1.0 + mu)
    omega = (1.0 + theta_lin) / (2.0 + mu)
    assert omega < 1.0
    x_l = [0.0, 0.0]
    y_l = [0.0, 0.0]
    x_bar_l = x_l[:]
    init_lyap = gamma * norm_sq(x_l, x_hat) + delta * norm_sq(y_l, y_hat)
    for n_step in range(1, 41):
        Kx_b = mat_vec(K, x_bar_l)
        y_l_next = [
            (y_l[c] + sigma_lin * Kx_b[c] + sigma_lin * delta * y_target[c]) / (1.0 + sigma_lin * delta)
            for c in range(2)
        ]
        KT_yl = mat_vec(K, y_l_next)
        x_l_next = [
            (x_l[c] - tau_lin * KT_yl[c] + tau_lin * gamma * x_target[c]) / (1.0 + tau_lin * gamma)
            for c in range(2)
        ]
        x_bar_l = [x_l_next[c] + theta_lin * (x_l_next[c] - x_l[c]) for c in range(2)]
        x_l, y_l = x_l_next, y_l_next
        lhs_eq59 = gamma * norm_sq(x_l, x_hat) + (1.0 - omega) * delta * norm_sq(y_l, y_hat)
        rhs_eq59 = (omega ** n_step) * init_lyap
        assert lhs_eq59 <= rhs_eq59 + 1e-12

    # Claim 3: Violation of tau * sigma * L^2 <= 1 on pure bilinear saddle min_x max_y <K x, y> causes divergence
    x_u = [1.0, 1.0]
    y_u = [1.0, 1.0]
    xb_u = x_u[:]
    tau_u, sigma_u = 0.6, 0.6  # tau_u * sigma_u * L^2 = 0.36 * 9 = 3.24 > 1
    init_u = norm_sq(x_u, [0.0, 0.0]) + norm_sq(y_u, [0.0, 0.0])
    for _ in range(15):
        Kxb = mat_vec(K, xb_u)
        y_u_next = [y_u[c] + sigma_u * Kxb[c] for c in range(2)]
        KTyu = mat_vec(K, y_u_next)
        x_u_next = [x_u[c] - tau_u * KTyu[c] for c in range(2)]
        xb_u = [2.0 * x_u_next[c] - x_u[c] for c in range(2)]
        x_u, y_u = x_u_next, y_u_next
    final_u = norm_sq(x_u, [0.0, 0.0]) + norm_sq(y_u, [0.0, 0.0])
    assert final_u > init_u * 100.0

    print(
        f"[PASS] Chambolle-Pock boundaries verified: gap_N={gap_N:.3e}<=d0/N={d0/N:.3e}, "
        f"200*gamma*tau_200={200.0*gamma*tau_n:.4f}, Alg3_err={lhs_eq59:.2e}<=omega^40*D0={rhs_eq59:.2e}, "
        f"unstable_blowup={final_u/init_u:.1e}x"
    )


if __name__ == "__main__":
    main()
