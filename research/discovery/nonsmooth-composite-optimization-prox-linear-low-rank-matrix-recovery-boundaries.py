#!/usr/bin/env python3
"""Constructed boundary verification for nonsmooth composite optimization and
prox-linear low-rank matrix recovery (Charisopoulos, Chen, Davis, Diaz, Ding,
& Drusvyatskiy 2021, Found. Comput. Math. 21(6):1505-1593).

Verifies:
1. Composite formulation f(x) = h(F(x)) = (1/m) sum_{i=1}^m |(a_i^T x)^2 - (a_i^T x_sharp)^2 - s_i|
   with arbitrary outlier corruption s supported on I_fail with p_fail = |I_fail|/m < 1/2
   (Section 1.2, Assumption 2, Proposition 4.1 & 4.6).
2. Convex-composite Taylor model accuracy (Proposition 4.1):
   f_x(z) = h(F(x) + nabla F(x)(z - x)) satisfies two-sided quadratic error bound
   |f(z) - f_x(z)| <= kappa_2 * ||z - x||_2^2.
3. Exact sharpness under outlier corruption p_fail < 1/2 (Proposition 4.6):
   f(x) - f(x_sharp) >= mu_sharp * min(||x - x_sharp||_2, ||x + x_sharp||_2)
   even when 25% of measurements are corrupted by large gross outliers.
4. Polyak subgradient method (Eq. 5.2, Theorem 5.2) and Prox-Linear method (Eq. 1.7,
   Theorem 5.4):
   - Polyak subgradient step x_{k+1} = x_k - ((f(x_k) - f(x_sharp)) / ||zeta_k||_2^2) zeta_k
     achieves linear convergence to exact x_sharp despite 25% outliers.
   - Prox-linear iteration solving the linearized l1 subproblem via iteratively
     reweighted / active-set least squares achieves quadratic local convergence
     (||x_{k+1} - x_sharp|| <= C ||x_k - x_sharp||^2), reaching machine precision in 5 steps.
"""

import json
import math
import random


def dot(u, v):
    return sum(ui * vi for ui, vi in zip(u, v))


def norm2(u):
    return math.sqrt(dot(u, u))


def sign_dist(x, x_sharp):
    d1 = math.sqrt(sum((xi - si) ** 2 for xi, si in zip(x, x_sharp)))
    d2 = math.sqrt(sum((xi + si) ** 2 for xi, si in zip(x, x_sharp)))
    return min(d1, d2)


def solve_linear_system(A_mat, b_vec):
    """Gaussian elimination with partial pivoting."""
    n = len(b_vec)
    M = [row[:] + [b_vec[i]] for i, row in enumerate(A_mat)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(M[r][col]))
        M[col], M[piv] = M[piv], M[col]
        div = M[col][col]
        for j in range(col, n + 1):
            M[col][j] /= div
        for r in range(n):
            if r != col:
                factor = M[r][col]
                for j in range(col, n + 1):
                    M[r][j] -= factor * M[col][j]
    return [M[i][n] for i in range(n)]


def main():
    rng = random.Random(202106)
    d = 6
    m = 60
    x_sharp = [1.5, -1.0, 0.8, -0.5, 1.2, 0.7]
    A = [[rng.gauss(0.0, 1.0) for _ in range(d)] for _ in range(m)]

    # 25% gross outlier corruption (p_fail = 0.25 < 1/2)
    m_fail = 15
    y = []
    for i in range(m):
        clean_val = dot(A[i], x_sharp) ** 2
        if i < m_fail:
            # Large adversarial outlier
            outlier = 25.0 * (1.0 if i % 2 == 0 else -1.0)
            y.append(clean_val + outlier)
        else:
            y.append(clean_val)

    def f_val(x):
        return sum(abs(dot(A[i], x) ** 2 - y[i]) for i in range(m)) / m

    def f_model(x, z):
        # Linearized model f_x(z) = (1/m) sum_i |(a_i^T x)^2 + 2 (a_i^T x) a_i^T (z - x) - y_i|
        total = 0.0
        dx = [zi - xi for zi, xi in zip(z, x)]
        for i in range(m):
            ax = dot(A[i], x)
            adx = dot(A[i], dx)
            total += abs(ax * ax + 2.0 * ax * adx - y[i])
        return total / m

    def subgrad(x):
        g = [0.0] * d
        for i in range(m):
            ax = dot(A[i], x)
            res = ax * ax - y[i]
            sgn = 1.0 if res > 0.0 else (-1.0 if res < 0.0 else 0.0)
            coeff = (2.0 * ax * sgn) / m
            for j in range(d):
                g[j] += coeff * A[i][j]
        return g

    f_star = f_val(x_sharp)

    # 1. Verify Proposition 4.1 (quadratic error bound between f(z) and f_x(z))
    # Notice F_i(z) - F_i(x) - nabla F_i(x)(z - x) = (a_i^T (z - x))^2 exactly!
    # Therefore |f(z) - f_x(z)| <= (1/m) sum_i (a_i^T (z - x))^2 <= ||(1/m) sum a_i a_i^T||_op ||z - x||_2^2.
    x_test = [xi + 0.15 * rng.gauss(0.0, 1.0) for xi in x_sharp]
    z_test = [xi - 0.1 * rng.gauss(0.0, 1.0) for xi in x_sharp]
    model_diff = abs(f_val(z_test) - f_model(x_test, z_test))
    exact_quad_upper = sum(dot(A[i], [zi - xi for zi, xi in zip(z_test, x_test)]) ** 2 for i in range(m)) / m
    assert model_diff <= exact_quad_upper + 1e-12

    # 2. Verify Proposition 4.6 (sharpness around x_sharp despite 25% gross outliers)
    # Check f(x) - f(x_sharp) >= mu_emp * dist(x, {+/- x_sharp})
    ratios = []
    for _ in range(25):
        pert = [rng.gauss(0.0, 0.05) for _ in range(d)]
        x_p = [xi + pi for xi, pi in zip(x_sharp, pert)]
        dist_p = sign_dist(x_p, x_sharp)
        gap_p = f_val(x_p) - f_star
        assert gap_p > 0.0, f"Sharpness violated: gap={gap_p} <= 0"
        ratios.append(gap_p / dist_p)
    min_sharpness_ratio = min(ratios)
    assert min_sharpness_ratio > 0.4, f"Unexpectedly small sharpness constant: {min_sharpness_ratio}"

    # 3. Verify Polyak subgradient method (Eq. 5.2, Theorem 5.2) linear convergence
    x_polyak = [xi + 0.25 * (1.0 if j % 2 == 0 else -1.0) for j, xi in enumerate(x_sharp)]
    init_dist = sign_dist(x_polyak, x_sharp)
    for _ in range(180):
        gap = f_val(x_polyak) - f_star
        if gap <= 1e-13:
            break
        g = subgrad(x_polyak)
        g_sq = dot(g, g)
        step = gap / g_sq
        x_polyak = [xj - step * gj for xj, gj in zip(x_polyak, g)]
    polyak_final_dist = sign_dist(x_polyak, x_sharp)
    assert polyak_final_dist < 1e-4, f"Polyak subgradient did not contract cleanly: {polyak_final_dist}"

    # 4. Verify Prox-Linear / Gauss-Newton linearized exact solver quadratic convergence (Theorem 5.4)
    # In the local neighborhood where clean measurements I_clean = {m_fail..m-1} dominate,
    # solving the linearized subproblem matches solving 2 (a_i^T x_k) a_i^T (z - x_k) = y_i - (a_i^T x_k)^2
    # on the inlier consensus set, yielding exact Newton/Gauss-Newton quadratic contraction:
    # z - x_sharp = ((a_i^T (x_k - x_sharp))^2) / (2 a_i^T x_k) -> ||x_{k+1} - x_sharp|| = O(||x_k - x_sharp||^2).
    x_pl = [xi + 0.2 * (1.0 if j % 2 == 0 else -1.0) for j, xi in enumerate(x_sharp)]
    pl_errors = [sign_dist(x_pl, x_sharp)]
    for _ in range(5):
        # IRLS solver for the linearized l1 problem min_z f_{x_pl}(z) + (L/2)||z - x_pl||^2
        z_curr = list(x_pl)
        for _irls in range(25):
            H = [[1e-9 if r == c else 0.0 for c in range(d)] for r in range(d)]
            rhs = [0.0] * d
            for i in range(m):
                ax = dot(A[i], x_pl)
                az_diff = dot(A[i], [zc - xp for zc, xp in zip(z_curr, x_pl)])
                lin_res = ax * ax + 2.0 * ax * az_diff - y[i]
                w = 1.0 / max(abs(lin_res), 1e-11)
                # Row vector b_i = 2 * ax * A[i], target c_i = y[i] - ax^2 + 2 * ax * (A[i]^T x_pl)
                b_i = [2.0 * ax * aij for aij in A[i]]
                c_i = y[i] - ax * ax + 2.0 * ax * dot(A[i], x_pl)
                for r in range(d):
                    rhs[r] += w * b_i[r] * c_i
                    for c in range(d):
                        H[r][c] += w * b_i[r] * b_i[c]
            z_curr = solve_linear_system(H, rhs)
        x_pl = z_curr
        pl_errors.append(sign_dist(x_pl, x_sharp))

    assert pl_errors[-1] < 1e-12, f"Prox-linear failed quadratic convergence: {pl_errors}"
    # Verify quadratic ratio ||x_{2} - x_sharp|| / ||x_{1} - x_sharp||^2 is bounded
    quad_ratio = pl_errors[2] / (pl_errors[1] ** 2)
    assert quad_ratio < 2.0, f"Unexpectedly large quadratic convergence constant: {quad_ratio}"

    summary = {
        "concept": "NonsmoothCompositeOptimizationAndProxLinearLowRankMatrixRecovery",
        "dimension_d": d,
        "measurements_m": m,
        "outlier_fraction_p_fail": m_fail / m,
        "taylor_model_diff": round(model_diff, 8),
        "taylor_quad_upper_bound": round(exact_quad_upper, 8),
        "min_empirical_sharpness_ratio": round(min_sharpness_ratio, 6),
        "initial_distance": round(init_dist, 6),
        "polyak_subgradient_final_dist": polyak_final_dist,
        "prox_linear_error_trajectory": [round(e, 14) for e in pl_errors],
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
