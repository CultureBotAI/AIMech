#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 567: TAMUNA."""

import math
import random


def main() -> None:
    random.seed(567)
    # 1. Verify correlated active-client binary mask properties (Section 4.1 & Eq. 7-8):
    # n total clients, cohort size c in {2,...,n}, sparsity parameter s in {2,...,c}.
    # Each row j in {1,...,d} of q^{(r)} in {0,1}^{d x c} has exactly s ones.
    n = 6
    c = 4
    s = 2
    d = 5

    # Verify Eq. (8) variance/correlation bound for the correlated mask compressor:
    # E[ || (1/s) sum_{i in Omega} C_i(v_i) - (1/c) sum_{i in Omega} v_i ||^2 ]
    # = (c - s) / (s * (c - 1)) * ( (1/c) sum_{i in Omega} ||v_i||^2 - || (1/c) sum_{i in Omega} v_i ||^2 )
    vecs = [[random.uniform(-2.0, 2.0) for _ in range(d)] for _ in range(c)]
    mean_vec = [sum(vecs[idx][j] for idx in range(c)) / c for j in range(d)]
    emp_var = (
        sum(sum(v[j] ** 2 for j in range(d)) for v in vecs) / c
        - sum(mv ** 2 for mv in mean_vec)
    )
    exact_factor = (c - s) / (s * (c - 1))
    theoretical_mse = exact_factor * emp_var

    # Enumerate all C(c, s) binary row masks of length c with s ones (since coordinates are independent/marginalized identically)
    from itertools import combinations
    all_masks = list(combinations(range(c), s))
    avg_sq_err = 0.0
    for j in range(d):
        coord_err = 0.0
        for ones_idx in all_masks:
            est = sum(vecs[idx][j] for idx in ones_idx) / s
            coord_err += (est - mean_vec[j]) ** 2
        avg_sq_err += coord_err / len(all_masks)

    assert abs(avg_sq_err - theoretical_mse) < 1e-12, (
        f"Expected MSE {theoretical_mse}, got {avg_sq_err}"
    )

    # 2. Verify Theorem 1 parameter conditions and Lyapunov contraction:
    # chi <= n*(s-1)/(s*(n-1)), eta = p * chi, tau = max((1 - gamma*mu)^2, (gamma*L - 1)^2, 1 - p^2 * chi * (s-1)/(n-1))
    chi = (n * (s - 1)) / (s * (n - 1))
    assert abs(chi - 6.0 / 10.0) < 1e-12
    mu = 0.5
    L = 2.0
    gamma = 2.0 / (L + mu)
    p = 0.25
    eta = p * chi
    tau = max(
        (1.0 - gamma * mu) ** 2,
        (gamma * L - 1.0) ** 2,
        1.0 - (p ** 2) * chi * (s - 1) / (n - 1),
    )
    assert 0.0 < tau < 1.0, f"Expected contraction tau in (0,1), got {tau}"

    # 3. Simulate TAMUNA (Algorithm 1) on heterogeneous strongly convex quadratics
    # f_i(x) = (mu/2) ||x||^2 + <b_i, x>, where sum_i b_i = 0 so x* = 0, nabla f_i(x*) = b_i != 0
    raw_b = [[random.uniform(-1.5, 1.5) for _ in range(d)] for _ in range(n)]
    b_mean = [sum(raw_b[i][j] for i in range(n)) / n for j in range(d)]
    B = [[raw_b[i][j] - b_mean[j] for j in range(d)] for i in range(n)]
    A_diag = [[mu + (L - mu) * (j / (d - 1)) for j in range(d)] for _ in range(n)]

    def grad_i(i: int, x: list[float]) -> list[float]:
        return [A_diag[i][j] * x[j] + B[i][j] for j in range(d)]

    x_bar = [2.0, -1.5, 1.0, -0.5, 1.2]
    h = [[0.0] * d for _ in range(n)]  # initialized so sum_i h_i = 0

    for r in range(1200):
        # Sample geometric local steps L^{(r)} ~ Geom(p)
        u = random.random()
        L_r = max(1, int(math.ceil(math.log(max(u, 1e-12)) / math.log(1.0 - p))))
        # Sample cohort Omega^{(r)} of size c
        omega = random.sample(range(n), c)
        x_local = {}
        for i in omega:
            xi = list(x_bar)
            for _ in range(L_r):
                gi = grad_i(i, xi)
                xi = [xi[j] - gamma * gi[j] + gamma * h[i][j] for j in range(d)]
            x_local[i] = xi

        # Correlated mask generation across active clients omega:
        # For each coordinate j, pick s active clients in omega to send their coordinate
        active_masks = {i: [0] * d for i in omega}
        for j in range(d):
            chosen = random.sample(omega, s)
            for i in chosen:
                active_masks[i][j] = 1

        # Server aggregation: x_bar^{(r+1)} = (1/s) sum_{i in omega} C_i(x_i^{(r, L_r)})
        x_bar_next = [0.0] * d
        for j in range(d):
            x_bar_next[j] = sum(
                x_local[i][j] * active_masks[i][j] for i in omega
            ) / s

        # Control variate update on active clients; idle clients keep h_i^{(r+1)} = h_i^{(r)}
        for i in omega:
            for j in range(d):
                if active_masks[i][j] == 1:
                    h[i][j] = h[i][j] + (eta / gamma) * (x_bar_next[j] - x_local[i][j])

        # Verify invariant: sum_{i=1}^n h_i^{(r+1)} == 0
        for j in range(d):
            sum_hj = sum(h[i][j] for i in range(n))
            assert abs(sum_hj) < 1e-10, f"Control variate zero-sum violated: {sum_hj}"

        x_bar = x_bar_next

    err_tamuna = sum(v * v for v in x_bar)
    drift_err = sum(
        sum((h[i][j] - B[i][j]) ** 2 for j in range(d)) for i in range(n)
    ) / n
    assert err_tamuna < 1e-10 and drift_err < 1e-8, (
        f"TAMUNA failed to converge to exact optimum: err={err_tamuna}, drift_err={drift_err}"
    )
    print(
        f"[PASS] Round 567 TAMUNA verified: mse_factor={exact_factor:.4f}, tau={tau:.4f}, "
        f"err_tamuna={err_tamuna:.3e}, drift_err={drift_err:.3e}"
    )


if __name__ == "__main__":
    main()
