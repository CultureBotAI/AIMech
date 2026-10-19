#!/usr/bin/env python3
"""Constructed boundary & verification script for ImplicitRegularizationInNonconvexStatisticalEstimationByLeaveOneOutTrajectoryAnalysis.

Verifies the core mathematical properties of Ma, Wang, Chi, & Chen (2020),
'Implicit Regularization in Nonconvex Statistical Estimation: Gradient Descent
Converges Linearly for Phase Retrieval, Matrix Completion, and Blind Deconvolution',
Foundations of Computational Mathematics, 20(3), 451-632
(DOI:10.1007/s10208-019-09429-9, arXiv:1711.10467v3):

1. General Leave-One-Out Perturbation Recipe (Section 2, Theorem 5):
   Vanilla gradient descent x^{t+1} = x^t - eta_t grad f(x^t) on nonconvex
   statistical estimation objectives without explicit projection, clipping, or
   regularization penalties stays inside a Region of Incoherence and Contraction
   (RIC) where the restricted Hessian satisfies strong convexity and smoothness.
2. Phase Retrieval (Section 3, Theorem 1 & Lemma 1):
   Minimizing f(x) = (1/(4m)) sum_{j=1}^m ((a_j^T x)^2 - (a_j^T x^*)^2)^2 via
   vanilla Wirtinger/real gradient descent maintains:
     - Linear l_2 contraction: dist(x^t, x^*) <= (1 - rho)^t dist(x^0, x^*)
     - Leave-one-out proximity: max_{1<=l<=m} ||x^t - x^{t,(l)}||_2 << ||x^t - x^*||_2,
       where x^{t,(l)} is the gradient descent trajectory on the leave-one-out
       empirical loss f^{(l)}(x) dropping sample a_l (statistically independent of a_l).
     - Implicit incoherence preservation: max_{1<=l<=m} |a_l^T (x^t - x^*)| stays
       uniformly bounded by O(sqrt(log m) ||x^t - x^*||_2) across all iterations t >= 0
       without any explicit trimming or projection step.
3. Low-Rank Matrix Completion (Section 4, Theorem 2):
   Minimizing f(X) = (1/(4p)) ||P_Omega(X X^T - M^*)||_F^2 for rank-r PSD matrix
   M^* = X^* (X^*)^T via vanilla factored gradient descent X^{t+1} = X^t - eta grad f(X^t)
   simultaneously contracts in Frobenius error ||X^t H^t - X^*||_F and preserves
   row-wise incoherence ||X^t H^t - X^*||_{2,infty} without projection onto the
   incoherence constraint set.
"""

from __future__ import annotations

import json
import math
import random
from typing import List, Tuple


def dot(u: List[float], v: List[float]) -> float:
    return sum(a * b for a, b in zip(u, v))


def vec_sub(u: List[float], v: List[float]) -> List[float]:
    return [a - b for a, b in zip(u, v)]


def vec_add(u: List[float], v: List[float]) -> List[float]:
    return [a + b for a, b in zip(u, v)]


def norm2(u: List[float]) -> float:
    return math.sqrt(dot(u, u))


def align_sign(x: List[float], x_star: List[float]) -> List[float]:
    return x[:] if dot(x, x_star) >= 0.0 else [-v for v in x]


def phase_retrieval_gd_step(
    x: List[float], A: List[List[float]], y: List[float], eta: float, drop_idx: int = -1
) -> List[float]:
    m = len(A)
    n = len(x)
    grad = [0.0] * n
    for j in range(m):
        if j == drop_idx:
            continue
        aj = A[j]
        ax = dot(aj, x)
        coeff = (ax * ax - y[j]) * ax / m
        for i in range(n):
            grad[i] += coeff * aj[i]
    return [x[i] - eta * grad[i] for i in range(n)]


def spectral_init_phase_retrieval(A: List[List[float]], y: List[float], n: int, power_steps: int = 60) -> List[float]:
    m = len(A)
    # Y = (1/m) sum_j y_j a_j a_j^T
    v = [1.0 / math.sqrt(n)] * n
    for _ in range(power_steps):
        Yv = [0.0] * n
        for j in range(m):
            aj = A[j]
            s = y[j] * dot(aj, v) / m
            for i in range(n):
                Yv[i] += s * aj[i]
        nv = norm2(Yv)
        v = [c / nv for c in Yv]
    # Scale by sqrt(mean(y) / 3) or sqrt(mean(y))
    lam1 = sum(y) / m
    scale = math.sqrt(max(lam1, 1e-12))
    return [scale * c for c in v]


def main() -> None:
    rng = random.Random(20261019)

    # Part A: Phase Retrieval vanilla gradient descent & leave-one-out trajectory analysis
    n = 10
    m = 90
    x_star_raw = [rng.gauss(0.0, 1.0) for _ in range(n)]
    nx = norm2(x_star_raw)
    x_star = [v / nx for v in x_star_raw]

    A = [[rng.gauss(0.0, 1.0) for _ in range(n)] for _ in range(m)]
    y = [(dot(aj, x_star) ** 2) for aj in A]

    x0 = align_sign(spectral_init_phase_retrieval(A, y, n), x_star)
    init_l2_err = norm2(vec_sub(x0, x_star))

    # Track full GD trajectory and leave-one-out trajectories for l in {0, 1, 2, 3, 4}
    loo_indices = [0, 1, 2, 3, 4]
    x_curr = x0[:]
    x_loo_curr = {l: align_sign(spectral_init_phase_retrieval(A[:l] + A[l + 1 :], y[:l] + y[l + 1 :], n), x_star) for l in loo_indices}

    eta = 0.08
    T_steps = 45
    max_incoherence_ratio = 0.0
    for t in range(T_steps):
        x_curr = align_sign(phase_retrieval_gd_step(x_curr, A, y, eta, drop_idx=-1), x_star)
        err_vec = vec_sub(x_curr, x_star)
        err_l2 = norm2(err_vec)
        if err_l2 > 1e-12:
            max_proj = max(abs(dot(A[j], err_vec)) for j in range(m))
            ratio = max_proj / (math.sqrt(math.log(m)) * err_l2)
            if ratio > max_incoherence_ratio:
                max_incoherence_ratio = ratio
        for l in loo_indices:
            x_loo_curr[l] = align_sign(phase_retrieval_gd_step(x_loo_curr[l], A, y, eta, drop_idx=l), x_star)

    final_l2_err = norm2(vec_sub(x_curr, x_star))
    max_loo_gap = max(norm2(vec_sub(x_curr, x_loo_curr[l])) for l in loo_indices)

    # Verify linear contraction and leave-one-out proximity
    assert final_l2_err < 0.02 * init_l2_err, f"Phase retrieval GD failed to contract linearly: {final_l2_err} vs {init_l2_err}"
    assert max_loo_gap < 0.02, f"Leave-one-out trajectory gap too large: {max_loo_gap}"
    assert max_incoherence_ratio < 3.0, f"Incoherence ratio exceeded bound: {max_incoherence_ratio}"

    # Part B: Rank-1 PSD Matrix Completion vanilla factored GD without projection
    n_mc = 14
    p_obs = 0.65
    # Incoherent unit vector x_mc_star
    x_mc_raw = [math.sin(0.7 * (i + 1)) + 0.5 * math.cos(1.3 * (i + 1)) for i in range(n_mc)]
    norm_mc = norm2(x_mc_raw)
    x_mc_star = [v / norm_mc for v in x_mc_raw]

    Omega = [[0] * n_mc for _ in range(n_mc)]
    for i in range(n_mc):
        Omega[i][i] = 1
        for j in range(i + 1, n_mc):
            if rng.random() < p_obs:
                Omega[i][j] = 1
                Omega[j][i] = 1

    # Initialize near x_mc_star with incoherent perturbation
    x_mc = [x_mc_star[i] + 0.08 * rng.gauss(0.0, 1.0) / math.sqrt(n_mc) for i in range(n_mc)]
    x_mc = align_sign(x_mc, x_mc_star)
    mc_init_l2 = norm2(vec_sub(x_mc, x_mc_star))
    mc_init_linf = max(abs(x_mc[i] - x_mc_star[i]) for i in range(n_mc))

    eta_mc = 0.18
    for _ in range(80):
        grad_mc = [0.0] * n_mc
        for i in range(n_mc):
            for j in range(n_mc):
                if Omega[i][j] == 1:
                    resid = x_mc[i] * x_mc[j] - x_mc_star[i] * x_mc_star[j]
                    grad_mc[i] += (resid * x_mc[j]) / p_obs
        x_mc = align_sign([x_mc[i] - eta_mc * grad_mc[i] for i in range(n_mc)], x_mc_star)

    mc_final_l2 = norm2(vec_sub(x_mc, x_mc_star))
    mc_final_linf = max(abs(x_mc[i] - x_mc_star[i]) for i in range(n_mc))
    assert mc_final_l2 < 0.01 * mc_init_l2, f"Matrix completion GD failed l_2 contraction: {mc_final_l2} vs {mc_init_l2}"
    assert mc_final_linf < 0.02 * mc_init_linf, f"Matrix completion GD failed l_infty contraction: {mc_final_linf} vs {mc_init_linf}"

    summary = {
        "phase_retrieval": {
            "n": n,
            "m": m,
            "init_l2_err": round(init_l2_err, 6),
            "final_l2_err": round(final_l2_err, 8),
            "max_loo_trajectory_gap": round(max_loo_gap, 6),
            "max_incoherence_ratio": round(max_incoherence_ratio, 4),
        },
        "matrix_completion_rank1": {
            "n": n_mc,
            "p_obs": p_obs,
            "init_l2_err": round(mc_init_l2, 6),
            "final_l2_err": round(mc_final_l2, 8),
            "init_two_to_inf_err": round(mc_init_linf, 6),
            "final_two_to_inf_err": round(mc_final_linf, 8),
        },
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
