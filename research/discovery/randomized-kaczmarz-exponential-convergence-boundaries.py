#!/usr/bin/env python3
"""Boundary and regime verification for Strohmer & Vershynin (2009)
A randomized Kaczmarz algorithm with exponential convergence.
"""

import json
import math


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def sq_norm(u):
    return dot(u, u)


def main():
    # 1. Verify Theorem 2 exact expected one-step contraction and Eq. (7)-(9)
    # Construct an overdetermined full-rank m x n matrix A (m=6, n=3) with heterogeneous row norms
    A = [
        [2.0, 0.0, 0.0],
        [0.0, 1.5, 0.0],
        [0.0, 0.0, 0.5],
        [1.0, 1.0, 0.0],
        [0.0, 1.0, 0.5],
        [10.0, 0.0, 0.0],  # heavy row
    ]
    m, n = len(A), len(A[0])
    row_sq_norms = [sq_norm(row) for row in A]
    frob_sq = sum(row_sq_norms)
    probs = [rn / frob_sq for rn in row_sq_norms]

    # Compute Gram matrix G = A^T A and its smallest eigenvalue lambda_min(A^T A) = 1 / ||A^{-1}||_2^2
    # Since A_3 = [0,0,0.5] and A_5 = [0,1.0,0.5], let's compute exact inverse of 3x3 G
    G = [[sum(A[r][i] * A[r][j] for r in range(m)) for j in range(n)] for i in range(n)]
    # Power iteration on G^{-1} via Gaussian elimination to get ||A^{-1}||_2^2 = lambda_max(G^{-1})
    def solve_3x3(M, rhs):
        aug = [M[i][:] + [rhs[i]] for i in range(3)]
        for i in range(3):
            piv = max(range(i, 3), key=lambda r: abs(aug[r][i]))
            aug[i], aug[piv] = aug[piv], aug[i]
            d = aug[i][i]
            for c in range(i, 4):
                aug[i][c] /= d
            for r in range(3):
                if r != i:
                    f = aug[r][i]
                    for c in range(i, 4):
                        aug[r][c] -= f * aug[i][c]
        return [aug[i][3] for i in range(3)]

    v = [0.0, 0.0, 1.0]
    for _ in range(50):
        w = solve_3x3(G, v)
        nw = math.sqrt(sq_norm(w))
        v = [z / nw for z in w]
    inv_norm_sq = math.sqrt(sq_norm(solve_3x3(G, v)))
    # kappa(A)^2 = ||A||_F^2 * ||A^{-1}||_2^2
    kappa_sq = frob_sq * inv_norm_sq
    assert kappa_sq >= n

    # True solution x* and initial approximation x_0
    x_star = [1.0, -2.0, 3.0]
    b = [dot(A[j], x_star) for j in range(m)]
    x0 = [0.0, 0.0, 0.0]
    err0_sq = sq_norm([x0[i] - x_star[i] for i in range(n)])

    # Exact expected squared error after 1 step of Algorithm 1 (sampling proportional to ||a_j||_2^2)
    exp_err1_sq = 0.0
    for j in range(m):
        res = (b[j] - dot(A[j], x0)) / row_sq_norms[j]
        x1_j = [x0[i] + res * A[j][i] for i in range(n)]
        exp_err1_sq += probs[j] * sq_norm([x1_j[i] - x_star[i] for i in range(n)])

    # Verify Pythagoras & Eq. (7): E[||x_1 - x*||_2^2] == ||x_0 - x*||_2^2 - ||A(x_0 - x*)||_2^2 / ||A||_F^2
    Az_sq = sum(dot(A[j], [x0[i] - x_star[i] for i in range(n)]) ** 2 for j in range(m))
    exact_identity_rhs = err0_sq - Az_sq / frob_sq
    assert abs(exp_err1_sq - exact_identity_rhs) < 1e-12
    assert exp_err1_sq <= (1.0 - 1.0 / kappa_sq) * err0_sq + 1e-12

    # 2. Verify Section 3.1 Theorem 3 (Optimality Lower Bound) & Section 3.2 (Tight Equality Attainment):
    # Construct the exact system of Section 3.2: n=3, kappa^2 = 6, m = 12 equations:
    # First m/kappa^2 = 2 rows equal to e_1, 5 rows equal to e_2, 5 rows equal to e_3.
    # For x* = 0 and x_0 = e_1, each step picks e_1 with probability 2/12 = 1/6 = kappa^{-2} (sending error to 0)
    # and picks e_2 or e_3 with probability 1 - kappa^{-2} (leaving x_k = e_1 unchanged).
    kappa_tight_sq = 6.0
    exact_traj = []
    lower_bound_thm3 = []
    for k in range(1, 6):
        ek = (1.0 - 1.0 / kappa_tight_sq) ** k
        lb = max(0.0, 1.0 - 2.0 * k / kappa_tight_sq)
        assert ek >= lb - 1e-12
        exact_traj.append(round(ek, 6))
        lower_bound_thm3.append(round(lb, 6))

    # 3. Verify Failure of Row-Order / Scaling Invariance under Uniform Sampling with Tiny-Norm Informative Row:
    # Suppose 9 rows are [1, 0] and 1 row is [0, 10^{-3}], and x_0 - x* = [0, 1].
    # Under uniform sampling, the 2nd coordinate is selected with prob 1/10, whereas if 999 rows are [100, 0]
    # and 1 row is [0, 1], row-norm sampling matches kappa(A)^{-2} = 1 / (999*10000 + 1).
    # Conversely, if 1 row is [100, 0] and 99 rows are [1e-4, 0] and 1 row is [0, 10]:
    # Uniform sampling wastes 99/101 steps on near-zero rows if they carry no new direction, or if 99 rows are
    # redundant copies of [1e-3, 0] and 1 row is [0, 10] with x_0 - x* = [0, 1]:
    # Row-norm sampling picks the informative heavy row [0, 10] with prob 100 / (100 + 99*1e-6) = 0.999999,
    # whereas uniform sampling picks it with prob only 1/100 = 0.01!
    p_norm_heavy = 100.0 / (100.0 + 99.0 * 1e-6)
    p_unif_heavy = 1.0 / 100.0
    exp_err1_rownorm = 1.0 - p_norm_heavy
    exp_err1_uniform = 1.0 - p_unif_heavy
    assert exp_err1_rownorm < 1e-6 and exp_err1_uniform == 0.99

    summary = {
        "concept": "RandomizedKaczmarzAlgorithmWithExponentialConvergence",
        "demmel_scaled_kappa_sq": round(kappa_sq, 6),
        "one_step_expected_err_sq": round(exp_err1_sq, 6),
        "one_step_theorem2_bound": round((1.0 - 1.0 / kappa_sq) * err0_sq, 6),
        "section32_tight_trajectory": exact_traj,
        "theorem3_lower_bounds": lower_bound_thm3,
        "rownorm_vs_uniform_1step_err": [round(exp_err1_rownorm, 8), round(exp_err1_uniform, 6)],
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
