#!/usr/bin/env python3
"""Constructed boundary verification for Round 574: FedNL (Safaryan et al., ICML 2022)."""

from __future__ import annotations

import math
import random


def solve_linear_system(mat: list[list[float]], rhs: list[float]) -> list[float]:
    """Pure-Python Gaussian elimination with partial pivoting."""
    d = len(rhs)
    a = [row[:] + [rhs[i]] for i, row in enumerate(mat)]
    for col in range(d):
        pivot = max(range(col, d), key=lambda r: abs(a[r][col]))
        a[col], a[pivot] = a[pivot], a[col]
        piv_val = a[col][col]
        for j in range(col, d + 1):
            a[col][j] /= piv_val
        for r in range(d):
            if r != col and abs(a[r][col]) > 0.0:
                factor = a[r][col]
                for j in range(col, d + 1):
                    a[r][j] -= factor * a[col][j]
    return [a[i][d] for i in range(d)]


def top_k_matrix(mat: list[list[float]], k_keep: int) -> list[list[float]]:
    """Top-K contractive matrix compressor on d x d matrices (Definition 3.3, Appendix B.3.3)."""
    d = len(mat)
    entries = [(abs(mat[r][c]), r, c) for r in range(d) for c in range(d)]
    entries.sort(reverse=True)
    out = [[0.0] * d for _ in range(d)]
    for _, r, c in entries[:k_keep]:
        out[r][c] = mat[r][c]
    return out


def frob_sq(mat: list[list[float]]) -> float:
    return sum(val * val for row in mat for val in row)


def mat_sub(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    d = len(a)
    return [[a[r][c] - b[r][c] for c in range(d)] for r in range(d)]


def mat_add_scaled(
    a: list[list[float]], b: list[list[float]], scale: float
) -> list[list[float]]:
    d = len(a)
    return [[a[r][c] + scale * b[r][c] for c in range(d)] for r in range(d)]


def main() -> None:
    rng = random.Random(574)
    n, m, d = 5, 10, 4
    lam = 0.05
    # Generate federated L2-regularized logistic regression instances across n clients (Eq. 11)
    features = []
    labels = []
    for _ in range(n):
        c_feat = []
        c_lab = []
        for _ in range(m):
            vec = [rng.gauss(0.0, 1.0) for _ in range(d)]
            c_feat.append(vec)
            c_lab.append(1.0 if sum(vec) > 0.0 else -1.0)
        features.append(c_feat)
        labels.append(c_lab)

    def local_grad(i: int, x: list[float]) -> list[float]:
        g = [lam * x[j] for j in range(d)]
        for s in range(m):
            a_s = features[i][s]
            b_s = labels[i][s]
            z = b_s * sum(a_s[j] * x[j] for j in range(d))
            sig = 1.0 / (1.0 + math.exp(z))
            coeff = -b_s * sig / m
            for j in range(d):
                g[j] += coeff * a_s[j]
        return g

    def local_hess(i: int, x: list[float]) -> list[list[float]]:
        h = [[lam if r == c else 0.0 for c in range(d)] for r in range(d)]
        for s in range(m):
            a_s = features[i][s]
            b_s = labels[i][s]
            z = b_s * sum(a_s[j] * x[j] for j in range(d))
            p_sig = 1.0 / (1.0 + math.exp(-z))
            w = p_sig * (1.0 - p_sig) / m
            for r in range(d):
                for c in range(d):
                    h[r][c] += w * a_s[r] * a_s[c]
        return h

    def global_grad(x: list[float]) -> list[float]:
        grads = [local_grad(i, x) for i in range(n)]
        return [sum(grads[i][j] for i in range(n)) / n for j in range(d)]

    def global_hess(x: list[float]) -> list[list[float]]:
        hesses = [local_hess(i, x) for i in range(n)]
        return [
            [sum(hesses[i][r][c] for i in range(n)) / n for c in range(d)]
            for r in range(d)
        ]

    # Compute exact optimum x^* via 25 steps of exact Newton's method
    x_star = [0.0] * d
    for _ in range(25):
        g = global_grad(x_star)
        h = global_hess(x_star)
        step = solve_linear_system(h, g)
        x_star = [x_star[j] - step[j] for j in range(d)]
    assert sum(v * v for v in global_grad(x_star)) < 1e-26
    h_star_i = [local_hess(i, x_star) for i in range(n)]

    # Verify Top-K matrix contraction property (Definition 3.3): ||C(M) - M||_F^2 <= (1 - K/d^2) ||M||_F^2
    k_keep = d  # O(d) communication per round out of d^2 entries
    delta = k_keep / (d * d)
    test_m = mat_sub(local_hess(0, [0.5] * d), h_star_i[0])
    comp_m = top_k_matrix(test_m, k_keep)
    err_comp = frob_sq(mat_sub(comp_m, test_m))
    assert err_comp <= (1.0 - delta) * frob_sq(test_m) + 1e-12

    # Run FedNL (Option 2: H^k + l^k I, Top-K with K=d, alpha = 1.0 under Assumption 3.4(ii))
    # vs Newton Zero (N0) from local neighborhood x^0
    x0 = [x_star[j] + 0.15 * ((-1) ** j) for j in range(d)]
    alpha = 1.0

    # Initialize H_i^0 = 0.0 to test Hessian learning H^k -> grad^2 f_i(x^*) from scratch
    h_est_i = [
        [[0.0 for _ in range(d)] for _ in range(d)]
        for _ in range(n)
    ]
    h_est_global = [[0.0] * d for _ in range(d)]

    x_fednl = list(x0)
    x_n0 = list(x0)
    h_n0 = global_hess(x0)

    r_prev = sum((x_fednl[j] - x_star[j]) ** 2 for j in range(d))
    ratios = []
    n0_ratios = []
    r_n0_prev = sum((x_n0[j] - x_star[j]) ** 2 for j in range(d))
    hess_err_init = (
        sum(frob_sq(mat_sub(h_est_i[i], h_star_i[i])) for i in range(n)) / n
    )

    for _ in range(20):
        # FedNL step (Algorithm 1 Option 2)
        g_k = global_grad(x_fednl)
        l_k = 0.0
        s_global = [[0.0] * d for _ in range(d)]
        for i in range(n):
            hi_true = local_hess(i, x_fednl)
            diff_i = mat_sub(hi_true, h_est_i[i])
            l_i = math.sqrt(frob_sq(diff_i))
            l_k += l_i / n
            s_i = top_k_matrix(diff_i, k_keep)
            h_est_i[i] = mat_add_scaled(h_est_i[i], s_i, alpha)
            for r in range(d):
                for c in range(d):
                    s_global[r][c] += s_i[r][c] / n

        # Option 2 corrected matrix H^k + l^k I
        h_corr = [
            [
                h_est_global[r][c] + (l_k if r == c else 0.0)
                for c in range(d)
            ]
            for r in range(d)
        ]
        step_fednl = solve_linear_system(h_corr, g_k)
        x_fednl = [x_fednl[j] - step_fednl[j] for j in range(d)]
        h_est_global = mat_add_scaled(h_est_global, s_global, alpha)

        r_curr = sum((x_fednl[j] - x_star[j]) ** 2 for j in range(d))
        if r_prev > 1e-22:
            ratios.append(r_curr / r_prev)
        r_prev = r_curr

        # Newton Zero (N0) step (Eq. 10)
        g_n0 = global_grad(x_n0)
        step_n0 = solve_linear_system(h_n0, g_n0)
        x_n0 = [x_n0[j] - step_n0[j] for j in range(d)]
        r_n0_curr = sum((x_n0[j] - x_star[j]) ** 2 for j in range(d))
        if r_n0_prev > 1e-22:
            n0_ratios.append(r_n0_curr / r_n0_prev)
        r_n0_prev = r_n0_curr

    hess_err_final = (
        sum(frob_sq(mat_sub(h_est_i[i], h_star_i[i])) for i in range(n)) / n
    )
    err_fednl = sum((x_fednl[j] - x_star[j]) ** 2 for j in range(d))

    # Verify Hessian learning H^k -> grad^2 f_i(x^*), universal local linear rate (<= 0.5),
    # and superlinear decay of r_{k+1}/r_k for FedNL below N0's asymptotic linear ratio
    assert hess_err_final < 1e-2 * hess_err_init, (
        f"Hessian learning failed: {hess_err_init} -> {hess_err_final}"
    )
    assert max(n0_ratios) <= 0.5 and ratios[-1] < 0.05 * ratios[0] and ratios[-1] < n0_ratios[-1], (
        f"FedNL superlinear convergence failed: ratios={ratios[0]:.4f}->{ratios[-1]:.4e}, "
        f"n0_ratio={n0_ratios[-1]:.4e}"
    )

    print(
        f"[PASS] Round 574 FedNL verified: delta={delta:.2f}, "
        f"H_err={hess_err_init:.4e}->{hess_err_final:.4e}, "
        f"fednl_ratio={ratios[0]:.4f}->{ratios[-1]:.4e} < n0_ratio={n0_ratios[-1]:.4e}, "
        f"err_fednl={err_fednl:.3e}"
    )


if __name__ == "__main__":
    main()
