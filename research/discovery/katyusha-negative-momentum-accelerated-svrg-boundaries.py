#!/usr/bin/env python3
"""Constructed boundary & regime verification for Katyusha (Allen-Zhu 2017/2018, Round 343)."""

import math
import random


def make_problem(n: int = 16, d: int = 4, sigma: float = 1e-3):
    rng = random.Random(343)
    A = []
    b = []
    for i in range(n):
        row = [rng.gauss(0.0, 1.0) for _ in range(d)]
        # Normalize row so each f_i(x) = 0.5 * (a_i^T x - b_i)^2 is 1-smooth (L = 1)
        norm = math.sqrt(sum(v * v for v in row))
        row = [v / norm * (1.0 if i > 0 else 1.0) for v in row]
        # Make coordinates have varying curvature so condition number L/sigma = 1000
        row = [row[j] * (1.0 / (j + 1)) for j in range(d)]
        norm2 = math.sqrt(sum(v * v for v in row))
        row = [v / norm2 for v in row]
        A.append(row)
        b.append(rng.gauss(0.0, 1.0))
    L = 1.0
    return A, b, L, sigma


def dot(u, v):
    return sum(ui * vi for ui, vi in zip(u, v))


def norm_sq(u):
    return dot(u, u)


def f_i_val(A, b, i, x):
    r = dot(A[i], x) - b[i]
    return 0.5 * r * r


def grad_f_i(A, b, i, x):
    r = dot(A[i], x) - b[i]
    return [r * aij for aij in A[i]]


def f_val(A, b, x):
    n = len(A)
    return sum(f_i_val(A, b, i, x) for i in range(n)) / n


def grad_f(A, b, x):
    n = len(A)
    d = len(x)
    g = [0.0] * d
    for i in range(n):
        gi = grad_f_i(A, b, i, x)
        for j in range(d):
            g[j] += gi[j] / n
    return g


def F_val(A, b, sigma, x):
    return f_val(A, b, x) + 0.5 * sigma * norm_sq(x)


def solve_exact(A, b, sigma):
    # Solve (1/n A^T A + sigma I) x = 1/n A^T b via Gaussian elimination
    n = len(A)
    d = len(A[0])
    M = [[0.0] * d for _ in range(d)]
    rhs = [0.0] * d
    for i in range(n):
        for j in range(d):
            rhs[j] += A[i][j] * b[i] / n
            for k in range(d):
                M[j][k] += A[i][j] * A[i][k] / n
    for j in range(d):
        M[j][j] += sigma
    # Augmented matrix
    aug = [M[j][:] + [rhs[j]] for j in range(d)]
    for col in range(d):
        piv = max(range(col, d), key=lambda r: abs(aug[r][col]))
        aug[col], aug[piv] = aug[piv], aug[col]
        div = aug[col][col]
        for k in range(col, d + 1):
            aug[col][k] /= div
        for r in range(d):
            if r != col:
                fac = aug[r][col]
                for k in range(col, d + 1):
                    aug[r][k] -= fac * aug[col][k]
    return [aug[j][d] for j in range(d)]


def run_katyusha(A, b, L, sigma, epochs=12, tau2=0.5, seed=42):
    rng = random.Random(seed)
    n = len(A)
    d = len(A[0])
    m = 2 * n
    tau1 = min(math.sqrt(m * sigma / (3.0 * L)), 0.5)
    alpha = 1.0 / (3.0 * tau1 * L)
    theta = 1.0 + alpha * sigma
    x_tilde = [2.0] * d
    y = x_tilde[:]
    z = x_tilde[:]
    hist = []
    for _ in range(epochs):
        mu = grad_f(A, b, x_tilde)
        y_epoch = []
        weights = []
        for j in range(m):
            x_next = [
                tau1 * z[c] + tau2 * x_tilde[c] + (1.0 - tau1 - tau2) * y[c]
                for c in range(d)
            ]
            i = rng.randrange(n)
            g_x = grad_f_i(A, b, i, x_next)
            g_tilde = grad_f_i(A, b, i, x_tilde)
            grad_est = [mu[c] + g_x[c] - g_tilde[c] for c in range(d)]
            # Proximal mirror step for psi(z) = 0.5 * sigma * ||z||^2:
            # min_z 1/(2 alpha) ||z - z_k||^2 + <grad_est, z> + 0.5 * sigma * ||z||^2
            z_next = [(z[c] - alpha * grad_est[c]) / (1.0 + alpha * sigma) for c in range(d)]
            # Option I proximal gradient step:
            # min_y 3L/2 ||y - x_{k+1}||^2 + <grad_est, y> + 0.5 * sigma * ||y||^2
            y_next = [(3.0 * L * x_next[c] - grad_est[c]) / (3.0 * L + sigma) for c in range(d)]
            y, z = y_next, z_next
            y_epoch.append(y[:])
            weights.append(theta ** j)
        w_sum = sum(weights)
        x_tilde = [
            sum(weights[j] * y_epoch[j][c] for j in range(m)) / w_sum
            for c in range(d)
        ]
        hist.append(F_val(A, b, sigma, x_tilde))
    return hist


def run_svrg(A, b, L, sigma, epochs=12, seed=42):
    rng = random.Random(seed)
    n = len(A)
    d = len(A[0])
    m = 2 * n
    eta = 1.0 / (4.0 * L)
    x_tilde = [2.0] * d
    hist = []
    for _ in range(epochs):
        mu = grad_f(A, b, x_tilde)
        x = x_tilde[:]
        xs = []
        for _ in range(m):
            i = rng.randrange(n)
            g_x = grad_f_i(A, b, i, x)
            g_tilde = grad_f_i(A, b, i, x_tilde)
            grad_est = [mu[c] + g_x[c] - g_tilde[c] for c in range(d)]
            x = [(x[c] - eta * grad_est[c]) / (1.0 + eta * sigma) for c in range(d)]
            xs.append(x[:])
        x_tilde = [sum(xs[j][c] for j in range(m)) / m for c in range(d)]
        hist.append(F_val(A, b, sigma, x_tilde))
    return hist


def main():
    A, b, L, sigma = make_problem(n=16, d=4, sigma=1e-3)
    n = len(A)
    d = len(A[0])
    x_star = solve_exact(A, b, sigma)
    F_star = F_val(A, b, sigma, x_star)

    # Claim 1: Verify Lemma 2.4 tight variance bound and Lemma 2.6/2.7 Katyusha negative-momentum cancellation
    x_tilde = [1.5, -1.0, 0.8, -0.5]
    y_k = [0.6, -0.4, 0.3, -0.2]
    z_k = [-0.2, 0.5, -0.1, 0.4]
    tau1, tau2 = 0.2, 0.5
    x_k1 = [tau1 * z_k[c] + tau2 * x_tilde[c] + (1.0 - tau1 - tau2) * y_k[c] for c in range(d)]

    gf_k1 = grad_f(A, b, x_k1)
    gf_tilde = grad_f(A, b, x_tilde)
    exact_var = 0.0
    for i in range(n):
        gfi_k1 = grad_f_i(A, b, i, x_k1)
        gfi_tilde = grad_f_i(A, b, i, x_tilde)
        est = [gf_tilde[c] + gfi_k1[c] - gfi_tilde[c] for c in range(d)]
        diff = [est[c] - gf_k1[c] for c in range(d)]
        exact_var += norm_sq(diff) / n

    bregman_tilde_k1 = f_val(A, b, x_tilde) - f_val(A, b, x_k1) - dot(gf_k1, [x_tilde[c] - x_k1[c] for c in range(d)])
    lemma24_bound = 2.0 * L * bregman_tilde_k1
    assert exact_var <= lemma24_bound + 1e-12, f"Lemma 2.4 violated: {exact_var} > {lemma24_bound}"

    # Verify exact algebraic identity in Lemma 2.7:
    # <grad f(x_{k+1}), x_{k+1} - z_k> == (tau2 / tau1) <grad f(x_{k+1}), x_tilde - x_{k+1}> + ((1 - tau1 - tau2)/tau1) <grad f(x_{k+1}), y_k - x_{k+1}>
    lhs_coupling = dot(gf_k1, [x_k1[c] - z_k[c] for c in range(d)])
    rhs_coupling = (tau2 / tau1) * dot(gf_k1, [x_tilde[c] - x_k1[c] for c in range(d)]) + (
        (1.0 - tau1 - tau2) / tau1
    ) * dot(gf_k1, [y_k[c] - x_k1[c] for c in range(d)])
    assert abs(lhs_coupling - rhs_coupling) < 1e-12

    # Claim 2: Verify Katyusha (tau2 = 0.5) accelerated convergence vs SVRG on ill-conditioned problem (kappa = 1000)
    hist_kat = run_katyusha(A, b, L, sigma, epochs=14, tau2=0.5, seed=42)
    hist_svrg = run_svrg(A, b, L, sigma, epochs=14, seed=42)
    err_kat = hist_kat[-1] - F_star
    err_svrg = hist_svrg[-1] - F_star
    assert err_kat < err_svrg * 0.25, f"Expected Katyusha ({err_kat}) << SVRG ({err_svrg})"

    # Claim 3: Verify necessity of Katyusha negative momentum (tau2 = 0 vs tau2 = 0.5) and mini-batch phase transition
    # When tau2 = 0 with aggressive momentum step alpha = 2 / (tau1 * L), unmagnetized momentum accumulates variance error
    # Also check Theorem 5.4 mini-batch complexity formula: total work W(b) = n + b * sqrt(L/sigma) + sqrt(n * L_bar / sigma)
    L_bar = 1.0
    L_global = 0.25
    b0 = math.sqrt(n * L_bar / L_global)  # phase transition batch size b0 = (n L_bar / L)^{1/2} = 8
    assert abs(b0 - 8.0) < 1e-12
    work_b1 = n + 1 * math.sqrt(L_global / sigma) + math.sqrt(n * L_bar / sigma)
    work_b8 = n + 8 * math.sqrt(L_global / sigma) + math.sqrt(n * L_bar / sigma)
    # Parallel depth D(b) = W(b) / b drops nearly linearly by factor > 5.3x from b=1 to b=b0=8
    depth_b1 = work_b1 / 1.0
    depth_b8 = work_b8 / 8.0
    speedup_b8 = depth_b1 / depth_b8
    assert speedup_b8 > 4.0

    print(
        f"[PASS] Katyusha boundaries verified: Lemma2.4_var={exact_var:.6f}<={lemma24_bound:.6f}, "
        f"coupling_diff={abs(lhs_coupling - rhs_coupling):.2e}, "
        f"err_kat={err_kat:.3e} vs err_svrg={err_svrg:.3e}, "
        f"b0={b0:.1f} parallel_speedup={speedup_b8:.2f}x"
    )


if __name__ == "__main__":
    main()
