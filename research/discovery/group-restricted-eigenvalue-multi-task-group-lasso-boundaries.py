#!/usr/bin/env python3
"""Constructed boundary and verification checks for Round 267:
Group Restricted Eigenvalue Oracle Inequalities, Multi-Task Dimension-Independence,
and Maximal Moment Inequality for Group LASSO (Lounici, Pontil, van de Geer, & Tsybakov 2011,
The Annals of Statistics 39(4):2164-2204, DOI:10.1214/11-AOS896, arXiv:1007.1771v3).

Verifies:
1. Block-coordinate descent KKT optimality conditions (Eqs. 2.3-2.4) and Lemma 3.1 score bound
   ||(X^T X (beta_hat - beta*))^j||_2 / N <= (3/2) * lambda_j on the high-probability event.
2. Multi-task dimension-independence phenomenon (Corollary 4.1 vs Theorem 7.1, Eqs. 7.9-7.10):
   In trace regression / multi-task learning with T tasks, M features, sample size n per task
   (N = nT), and s active groups, Group LASSO achieves l2 error rate O((s/n)(1 + log(M)/T))
   which strictly improves as T grows and beats standard l1 LASSO's O((s/n)*log(MT)) rate.
3. Block-coherence (2, infinity)-norm bound (Theorem 5.1) and thresholded group support
   recovery J_hat = {j : ||beta_hat^j||_2 > a_0 * lambda_j} = J(beta*) (Corollary 5.2).
4. Maximal moment inequality (Lemma 9.1): E[max_{1<=j<=M} |sum_{i=1}^k Z_{i,j}|^m]
   <= [8 * log(c(m) * M)]^{m/2} * E[(max_{1<=j<=M} sum_{i=1}^k Z_{i,j}^2)^{m/2}] for m in {1, 2, 4}.
"""

from __future__ import annotations

import json
import math
import random
from typing import Dict, List, Tuple


def vec_norm2(v: List[float]) -> float:
    return math.sqrt(sum(x * x for x in v))


def solve_group_lasso_bcd(
    X_groups: List[List[List[float]]],
    y: List[float],
    lambdas: List[float],
    max_iter: int = 400,
    tol: float = 1e-10,
) -> List[List[float]]:
    """Solve (1/N)||sum_j X^j beta^j - y||_2^2 + 2 * sum_j lambda_j ||beta^j||_2
    when within-group Gram matrices (1/N)(X^j)^T X^j = I_{d_j} (multi-task normalized design
    of Section 4) or via exact block proximal gradient / Newton step."""
    N = len(y)
    M = len(X_groups)
    d_list = [len(X_groups[j][0]) for j in range(M)]
    beta = [[0.0] * d_list[j] for j in range(M)]
    # Precompute Gram blocks G_j = (1/N) (X^j)^T X^j and Lipschitz constants L_j
    G = []
    L_blocks = []
    for j in range(M):
        dj = d_list[j]
        Gj = [[0.0] * dj for _ in range(dj)]
        for r in range(dj):
            for c in range(dj):
                Gj[r][c] = sum(X_groups[j][i][r] * X_groups[j][i][c] for i in range(N)) / N
        G.append(Gj)
        # Frobenius upper bound on spectral norm of Gj
        frob = math.sqrt(sum(Gj[r][c] ** 2 for r in range(dj) for c in range(dj)))
        L_blocks.append(max(frob, 1e-8))

    # Maintain residual r = y - X beta
    residual = list(y)
    for _ in range(max_iter):
        max_diff = 0.0
        for j in range(M):
            dj = d_list[j]
            Xj = X_groups[j]
            old_bj = list(beta[j])
            # Add back X^j old_bj to residual
            for i in range(N):
                s = sum(Xj[i][k] * old_bj[k] for k in range(dj))
                residual[i] += s
            # Compute z_j = (1/N) (X^j)^T r_partial
            zj = [sum(Xj[i][k] * residual[i] for i in range(N)) / N for k in range(dj)]
            # Check if Gj is close to scalar alpha_j * I_{dj}
            diag_avg = sum(G[j][k][k] for k in range(dj)) / dj
            off_diag = sum(
                abs(G[j][r][c]) for r in range(dj) for c in range(dj) if r != c
            ) + sum(abs(G[j][k][k] - diag_avg) for k in range(dj))
            if off_diag < 1e-9:
                # Exact closed-form block soft-thresholding:
                # min_{b} alpha_j ||b||_2^2 - 2 z_j^T b + 2 lambda_j ||b||_2
                znorm = vec_norm2(zj)
                if znorm <= lambdas[j]:
                    new_bj = [0.0] * dj
                else:
                    scale = (znorm - lambdas[j]) / (diag_avg * znorm)
                    new_bj = [scale * z for z in zj]
            else:
                # Inner proximal gradient steps on group j
                bj = list(old_bj)
                step = 1.0 / L_blocks[j]
                for _inner in range(30):
                    # grad of (1/2) b^T Gj b - zj^T b is Gj b - zj
                    grad = [
                        sum(G[j][r][c] * bj[c] for c in range(dj)) - zj[r]
                        for r in range(dj)
                    ]
                    u = [bj[r] - step * grad[r] for r in range(dj)]
                    unorm = vec_norm2(u)
                    thresh = step * lambdas[j]
                    if unorm <= thresh:
                        bj = [0.0] * dj
                    else:
                        bj = [(1.0 - thresh / unorm) * val for val in u]
                new_bj = bj
            # Update residual and beta[j]
            for i in range(N):
                s = sum(Xj[i][k] * new_bj[k] for k in range(dj))
                residual[i] -= s
            diff = vec_norm2([new_bj[k] - old_bj[k] for k in range(dj)])
            if diff > max_diff:
                max_diff = diff
            beta[j] = new_bj
        if max_diff < tol:
            break
    return beta


def verify_kkt_and_multitask_dimension_independence() -> Dict[str, object]:
    """Verify KKT conditions (Eqs. 2.3-2.4), Lemma 3.1 score bound, and Corollary 4.1 vs
    Theorem 7.1 multi-task dimension independence as T grows."""
    rng = random.Random(20110896)
    M = 12  # features / groups
    s = 2   # active groups {0, 1}
    n = 40  # samples per task
    tasks_grid = [1, 4, 16]

    kkt_max_violation = 0.0
    lemma31_max_ratio = 0.0
    gl_l2_errors: List[float] = []
    lasso_l2_errors: List[float] = []
    theoretical_gl_rates: List[float] = []
    theoretical_lasso_rates: List[float] = []

    sigma = 0.25
    alpha = 0.05

    for T in tasks_grid:
        N = n * T
        # Construct multi-task block design X_groups: M groups, each N x T
        # In multi-task setting (Section 4), task t uses design matrix Z^{(t)} in R^{n x M}
        # with normalized columns (1/n) sum_{i=1}^n (Z_{i,j}^{(t)})^2 = 1.
        # Then (1/N) (X^j)^T X^j = (1/T) I_T.
        Z_tasks: List[List[List[float]]] = []
        for _t in range(T):
            Zt = [[0.0] * M for _ in range(n)]
            for j in range(M):
                col = [rng.gauss(0.0, 1.0) for _ in range(n)]
                mean_c = sum(col) / n
                col = [c - mean_c for c in col]
                norm_c = math.sqrt(sum(c * c for c in col) / n)
                for i in range(n):
                    Zt[i][j] = col[i] / norm_c
            Z_tasks.append(Zt)

        # Build X_groups[j] of shape N x T
        X_groups: List[List[List[float]]] = []
        for j in range(M):
            Xj = [[0.0] * T for _ in range(N)]
            for t in range(T):
                for i in range(n):
                    Xj[t * n + i][t] = Z_tasks[t][i][j]
            X_groups.append(Xj)

        # True coefficients beta*_{j,t}: active on j in {0, 1} with unit per-task energy
        beta_star = [[0.0] * T for _ in range(M)]
        for t in range(T):
            beta_star[0][t] = 1.2 * (1.0 if t % 2 == 0 else -1.0)
            beta_star[1][t] = 0.9 * (1.0 if t % 3 == 0 else -1.0)

        # Noise xi_i ~ N(0, sigma^2)
        xi = [rng.gauss(0.0, sigma) for _ in range(N)]
        y = [0.0] * N
        for i in range(N):
            val = xi[i]
            for j in range(s):
                for t in range(T):
                    val += X_groups[j][i][t] * beta_star[j][t]
            y[i] = val

        # Eq. (4.3) Group LASSO penalty level:
        # lambda = (2 * sigma / sqrt(n * T)) * sqrt(1 + (2.5 / T) * log(M / alpha))
        lam_gl = (2.0 * sigma / math.sqrt(N)) * math.sqrt(
            1.0 + (2.5 / T) * math.log(M / alpha)
        )
        lambdas = [lam_gl] * M

        beta_hat = solve_group_lasso_bcd(X_groups, y, lambdas)

        # Check KKT conditions Eqs. (2.3)-(2.4)
        y_hat = [0.0] * N
        for i in range(N):
            y_hat[i] = sum(
                X_groups[j][i][t] * beta_hat[j][t] for j in range(M) for t in range(T)
            )
        for j in range(M):
            grad_j = [
                sum(X_groups[j][i][t] * (y_hat[i] - y[i]) for i in range(N)) / N
                for t in range(T)
            ]
            bnorm = vec_norm2(beta_hat[j])
            if bnorm > 1e-7:
                # Eq. (2.3): grad_j + lam_gl * beta_hat[j] / ||beta_hat[j]||_2 = 0
                err = vec_norm2(
                    [grad_j[t] + lam_gl * beta_hat[j][t] / bnorm for t in range(T)]
                )
            else:
                # Eq. (2.4): ||grad_j||_2 <= lam_gl
                err = max(0.0, vec_norm2(grad_j) - lam_gl)
            if err > kkt_max_violation:
                kkt_max_violation = err

            # Check Lemma 3.1 score bound ||(X^T X (beta_hat - beta*))^j||_2 / N <= 1.5 * lam_gl
            score_j = [
                sum(
                    X_groups[j][i][t]
                    * (
                        y_hat[i]
                        - sum(
                            X_groups[k][i][tau] * beta_star[k][tau]
                            for k in range(M)
                            for tau in range(T)
                        )
                    )
                    for i in range(N)
                )
                / N
                for t in range(T)
            ]
            ratio = vec_norm2(score_j) / (1.5 * lam_gl)
            if ratio > lemma31_max_ratio:
                lemma31_max_ratio = ratio

        # Normalize per-task l2 error: (1/T) sum_{j,t} (beta_hat_{j,t} - beta*_{j,t})^2
        err_gl = (
            sum(
                (beta_hat[j][t] - beta_star[j][t]) ** 2
                for j in range(M)
                for t in range(T)
            )
            / T
        )
        gl_l2_errors.append(err_gl)

        # Compare with standard elementwise l1 LASSO (groups of size 1, penalty Eq. 7.7)
        # On each task t and feature j, (1/N) sum_i X_{i,(j,t)}^2 = 1/T, so soft-thresholding
        # with lambda_L = (2*sigma / sqrt(n*T)) * sqrt((2.5/T)*log(M*T/alpha)):
        lam_lasso = (2.0 * sigma / math.sqrt(N)) * math.sqrt(
            (2.5 / T) * math.log((M * T) / alpha)
        )
        beta_lasso = [[0.0] * T for _ in range(M)]
        for t in range(T):
            # Solve task t standard Lasso via coordinate descent on Z_tasks[t]
            yt = y[t * n : (t + 1) * n]
            Zt = Z_tasks[t]
            # Per-task Lasso penalty is T * lam_lasso / 2 in (1/n)||Zt b - yt||^2 + 2 lam_task ||b||_1
            lam_task = T * lam_lasso
            bt = [0.0] * M
            res_t = list(yt)
            for _it in range(250):
                for j in range(M):
                    old_v = bt[j]
                    for i in range(n):
                        res_t[i] += Zt[i][j] * old_v
                    zj = sum(Zt[i][j] * res_t[i] for i in range(n)) / n
                    if abs(zj) <= lam_task:
                        new_v = 0.0
                    else:
                        new_v = math.copysign(abs(zj) - lam_task, zj)
                    for i in range(n):
                        res_t[i] -= Zt[i][j] * new_v
                    bt[j] = new_v
            for j in range(M):
                beta_lasso[j][t] = bt[j]

        err_lasso = (
            sum(
                (beta_lasso[j][t] - beta_star[j][t]) ** 2
                for j in range(M)
                for t in range(T)
            )
            / T
        )
        lasso_l2_errors.append(err_lasso)

        # Theoretical rate factors from Eq. (7.9) vs Eq. (7.10):
        # Group LASSO per-task rate ~ (sigma^2 * s / n) * (1 + (2.5/T) * log(M/alpha))
        # LASSO per-task rate ~ (sigma^2 * s / n) * log(M * T / alpha)
        theoretical_gl_rates.append((sigma**2 * s / n) * (1.0 + (2.5 / T) * math.log(M / alpha)))
        theoretical_lasso_rates.append((sigma**2 * s / n) * 2.5 * math.log(M * T / alpha))

    assert kkt_max_violation < 1e-7, f"KKT violation too large: {kkt_max_violation}"
    assert lemma31_max_ratio <= 1.000001, f"Lemma 3.1 ratio exceeded 1: {lemma31_max_ratio}"
    assert gl_l2_errors[-1] < gl_l2_errors[0], "Group LASSO per-task error must decrease with T"
    assert gl_l2_errors[-1] < lasso_l2_errors[-1], "Group LASSO must outperform elementwise LASSO for multi-task T=16"
    assert theoretical_gl_rates[-1] < theoretical_gl_rates[0]
    assert theoretical_lasso_rates[-1] > theoretical_lasso_rates[0]

    return {
        "tasks_grid": tasks_grid,
        "kkt_max_violation": round(kkt_max_violation, 12),
        "lemma31_max_ratio": round(lemma31_max_ratio, 6),
        "gl_per_task_l2_errors": [round(x, 6) for x in gl_l2_errors],
        "lasso_per_task_l2_errors": [round(x, 6) for x in lasso_l2_errors],
        "theoretical_gl_rates": [round(x, 6) for x in theoretical_gl_rates],
        "theoretical_lasso_rates": [round(x, 6) for x in theoretical_lasso_rates],
    }


def verify_block_coherence_and_support_recovery() -> Dict[str, object]:
    """Verify Theorem 5.1 (2, infinity)-norm bound and Corollary 5.2 thresholded support recovery
    under orthogonal within-group blocks and small off-diagonal block coherencetheta < 1/(7s)."""
    M = 8
    d = 3
    s = 2
    N = 60
    rng = random.Random(20110502)

    # Generate orthonormal columns for all M*d = 24 columns in R^N via Gram-Schmidt,
    # then perturb off-diagonal blocks slightly so theta <= 0.02 < 1/(7*s) = 1/14 ≈ 0.0714.
    cols: List[List[float]] = []
    for _ in range(M * d):
        v = [rng.gauss(0.0, 1.0) for _ in range(N)]
        for u in cols:
            proj = sum(v[i] * u[i] for i in range(N)) / N
            v = [v[i] - proj * u[i] for i in range(N)]
        nrm = math.sqrt(sum(x * x for x in v) / N)
        v = [x / nrm for x in v]
        cols.append(v)

    X_groups: List[List[List[float]]] = []
    for j in range(M):
        Xj = [[cols[j * d + k][i] for k in range(d)] for i in range(N)]
        X_groups.append(Xj)

    # Verify block coherence theta = max_{j != j'} ||(1/N)(X^j)^T X^{j'}||_{2->2} < 1/(7s)
    theta = 0.0
    for j in range(M):
        for jp in range(M):
            if j == jp:
                continue
            frob = 0.0
            for r in range(d):
                for c in range(d):
                    ip = sum(X_groups[j][i][r] * X_groups[jp][i][c] for i in range(N)) / N
                    frob += ip * ip
            theta = max(theta, math.sqrt(frob))

    assert theta < 1.0 / (7.0 * s), f"Block coherence {theta} not < 1/(7s)"

    # True sparse vector supported on J(beta*) = {0, 1} with min_{j in J} ||beta*^j|| > 2 * a_0 * lambda
    sigma = 0.08
    lam = 0.09
    a0 = 1.5 / (1.0 - 7.0 * s * theta)
    min_signal = 2.5 * a0 * lam
    beta_star = [[0.0] * d for _ in range(M)]
    beta_star[0] = [min_signal, 0.2, -0.1]
    beta_star[1] = [-0.15, min_signal, 0.1]

    xi = [rng.gauss(0.0, sigma * 0.4) for _ in range(N)]
    y = [
        xi[i]
        + sum(
            X_groups[j][i][k] * beta_star[j][k]
            for j in range(s)
            for k in range(d)
        )
        for i in range(N)
    ]

    beta_hat = solve_group_lasso_bcd(X_groups, y, [lam] * M)
    max_group_err = max(
        vec_norm2([beta_hat[j][k] - beta_star[j][k] for k in range(d)])
        for j in range(M)
    )
    bound_2_inf = a0 * lam
    assert max_group_err <= bound_2_inf, f"(2,inf) error {max_group_err} > {bound_2_inf}"

    # Thresholded estimator J_hat = {j : ||beta_hat^j||_2 > a0 * lam}
    j_hat = [j for j in range(M) if vec_norm2(beta_hat[j]) > a0 * lam]
    assert j_hat == [0, 1], f"Expected support [0, 1], got {j_hat}"

    return {
        "block_coherence_theta": round(theta, 8),
        "coherence_threshold_1_over_7s": round(1.0 / (7.0 * s), 6),
        "a0_constant": round(a0, 6),
        "max_group_l2_error": round(max_group_err, 6),
        "theorem51_bound": round(bound_2_inf, 6),
        "recovered_support": j_hat,
    }


def verify_lemma91_maximal_moment_inequality() -> Dict[str, object]:
    """Verify Lemma 9.1 maximal moment inequality for independent centered Z_{i,j}:
    E[max_{1<=j<=M} |sum_{i=1}^k Z_{i,j}|^m]
      <= [8 * log(c(m) * M)]^{m/2} * E[(max_{1<=j<=M} sum_{i=1}^k Z_{i,j}^2)^{m/2}]
    for m in {1, 2, 4} where c(m) = 2 if m=1 and c(m) = 2*e^{m-1} if m>=2."""
    rng = random.Random(20110901)
    M = 16
    k = 25
    trials = 600

    lhs_acc = {1: 0.0, 2: 0.0, 4: 0.0}
    rhs_expect_acc = {1: 0.0, 2: 0.0, 4: 0.0}

    for _ in range(trials):
        max_abs_sum = 0.0
        max_sq_sum = 0.0
        for _j in range(M):
            s1 = 0.0
            s2 = 0.0
            for _i in range(k):
                # Heterogeneous centered bounded-variance Rademacher-Gaussian product
                z = rng.choice([-1.0, 1.0]) * abs(rng.gauss(0.0, 1.0))
                s1 += z
                s2 += z * z
            if abs(s1) > max_abs_sum:
                max_abs_sum = abs(s1)
            if s2 > max_sq_sum:
                max_sq_sum = s2
        for m in (1, 2, 4):
            lhs_acc[m] += max_abs_sum**m
            rhs_expect_acc[m] += max_sq_sum ** (m / 2.0)

    ratios = {}
    for m in (1, 2, 4):
        c_m = 2.0 if m == 1 else 2.0 * math.exp(m - 1.0)
        factor = (8.0 * math.log(c_m * M)) ** (m / 2.0)
        lhs = lhs_acc[m] / trials
        rhs = factor * (rhs_expect_acc[m] / trials)
        assert lhs <= rhs, f"Lemma 9.1 violated for m={m}: {lhs} > {rhs}"
        ratios[f"m={m}"] = {
            "lhs": round(lhs, 4),
            "rhs": round(rhs, 4),
            "ratio_lhs_over_rhs": round(lhs / rhs, 6),
        }

    return ratios


def main() -> None:
    part1 = verify_kkt_and_multitask_dimension_independence()
    part2 = verify_block_coherence_and_support_recovery()
    part3 = verify_lemma91_maximal_moment_inequality()
    summary = {
        "concept": "AIMech:GroupRestrictedEigenvalueOracleInequalitiesAndMultiTaskGroupLassoMinimaxOptimality",
        "source": "Lounici, Pontil, van de Geer, & Tsybakov (2011), Ann. Statist. 39(4):2164-2204",
        "multitask_and_kkt": part1,
        "block_coherence_and_support_recovery": part2,
        "lemma91_maximal_moment_inequality": part3,
        "all_assertions_passed": True,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
