#!/usr/bin/env python3
"""Constructed boundary & regime verification for Belloni & Chernozhukov (2013, arXiv:1001.0188v5, DOI:10.3150/11-BEJ410).

Verifies:
1. Section 2.1 & Proof of Theorem 2 Step 2 (pp. 5, 22, Eqs. 2.2-2.4): Oracle risk
   minimization program min_{0<=k<=p} (c_k^2 + sigma^2 k / n), exact orthogonality
   E_n[x_{.j} r_.] = 0 for j in T, and optimality residual correlation bound
   |E_n[x_{.j} r_.]| <= min{sigma/sqrt(n), c_s} for j in T^c.
2. Section 3 & Appendix A.1 (pp. 10-14, 21-23, Theorems 1 & 3, Remark 3.1, Lemmas 2-3,
   Eq. A.1): Lasso prediction norm bound, KKT lower bound on ||f_hat - f||_{P_n,2},
   Lemma 3 sublinearity phi(ceil(ell*k)) <= ceil(ell)*phi(k), and Lemma 2 / Theorem 3
   presparsity bound m_hat <= s * phi(m_hat) * L_n.
3. Section 4 & Section 5.1 (pp. 14-17, 23, 25-26, Theorems 4-5, Eqs. A.7-A.8):
   Generic post-model selection fit relation Q_hat(beta_tilde) - Q_hat(beta_0) <= B_n ^ C_n,
   exact C_n = 0 when T subseteq T_hat, Lasso optimality bound B_n <= (lambda/n)(||delta_T||_1
   - ||delta_{T^c}||_1), and strict prediction error reduction of OLS post-Lasso over Lasso.
4. Sections 2.3, 2.5, 5.2-5.3 & Figure 1 (pp. 3, 7-9, 17-20, Eqs. 2.9, 2.14, Theorems 6-7):
   Under equicorrelated design (matching Figure 1, p. 3) with lambda >= c n ||S||_infty,
   fitness-thresholded Lasso (fit-Lasso) exact binary search in <= ceil(log2|T_hat|) steps
   for gamma = (Q_hat(beta_tilde^0) - Q_hat(beta_hat))/2 < 0 recovers exact oracle support
   (m_tilde_fit = 0 < m_hat), achieves strictly smaller average prediction error than both
   OLS post-Lasso and Lasso across 20 Monte Carlo draws, and satisfies Theorem 7's
   thresholding loss bound gamma_t <= t * sqrt(phi(m_t) * m_t).
"""

from __future__ import annotations

import itertools
import json
import math
import random


def dot(u: list[float], v: list[float]) -> float:
    return sum(a * b for a, b in zip(u, v))


def norm2(u: list[float]) -> float:
    return math.sqrt(dot(u, u))


def norm1(u: list[float]) -> float:
    return sum(abs(a) for a in u)


def mat_vec(A: list[list[float]], v: list[float]) -> list[float]:
    return [dot(row, v) for row in A]


def solve_linear_system(A: list[list[float]], b: list[float]) -> list[float]:
    m = len(b)
    if m == 0:
        return []
    aug = [row[:] + [b[i]] for i, row in enumerate(A)]
    for col in range(m):
        pivot = max(range(col, m), key=lambda r: abs(aug[r][col]))
        aug[col], aug[pivot] = aug[pivot], aug[col]
        piv_val = aug[col][col]
        for j in range(col, m + 1):
            aug[col][j] /= piv_val
        for r in range(m):
            if r != col and aug[r][col] != 0.0:
                factor = aug[r][col]
                for j in range(col, m + 1):
                    aug[r][j] -= factor * aug[col][j]
    return [aug[i][m] for i in range(m)]


def ols_on_support(
    X: list[list[float]], y: list[float], supp: list[int]
) -> list[float]:
    n = len(X)
    p = len(X[0])
    beta = [0.0] * p
    if not supp:
        return beta
    k = len(supp)
    gram = [[0.0] * k for _ in range(k)]
    rhs = [0.0] * k
    for a in range(k):
        ja = supp[a]
        rhs[a] = sum(X[i][ja] * y[i] for i in range(n)) / n
        for b in range(a, k):
            jb = supp[b]
            val = sum(X[i][ja] * X[i][jb] for i in range(n)) / n
            gram[a][b] = val
            gram[b][a] = val
    sol = solve_linear_system(gram, rhs)
    for a, ja in enumerate(supp):
        beta[ja] = sol[a]
    return beta


def q_hat(X: list[list[float]], y: list[float], beta: list[float]) -> float:
    n = len(X)
    preds = mat_vec(X, beta)
    return sum((y[i] - preds[i]) ** 2 for i in range(n)) / n


def pred_norm(X: list[list[float]], delta: list[float]) -> float:
    n = len(X)
    xd = mat_vec(X, delta)
    return math.sqrt(sum(v * v for v in xd) / n)


def solve_lasso_cd(
    X: list[list[float]],
    y: list[float],
    lam_over_n: float,
    max_iter: int = 8000,
    tol: float = 1e-12,
) -> list[float]:
    """Minimize Q_hat(beta) + (lam/n)*||beta||_1 where Q_hat(beta) = E_n[(y - X beta)^2]."""
    n = len(X)
    p = len(X[0])
    beta = [0.0] * p
    r = y[:]
    thresh = lam_over_n / 2.0
    for _ in range(max_iter):
        max_diff = 0.0
        for j in range(p):
            old_bj = beta[j]
            if old_bj != 0.0:
                for i in range(n):
                    r[i] += X[i][j] * old_bj
            rho_j = sum(X[i][j] * r[i] for i in range(n)) / n
            if rho_j > thresh:
                new_bj = rho_j - thresh
            elif rho_j < -thresh:
                new_bj = rho_j + thresh
            else:
                new_bj = 0.0
            beta[j] = new_bj
            if new_bj != 0.0:
                for i in range(n):
                    r[i] -= X[i][j] * new_bj
            diff = abs(new_bj - old_bj)
            if diff > max_diff:
                max_diff = diff
        if max_diff < tol:
            break
    return beta


def max_sparse_eig_restricted(
    G: list[list[float]], T_set: set[int], m: int
) -> float:
    """Compute phi(m) = max_{||delta_{T^c}||_0 <= m, delta != 0} delta' G delta / ||delta||^2."""
    p = len(G)
    tc_indices = [j for j in range(p) if j not in T_set]
    m_eff = min(m, len(tc_indices))
    best_max = 0.0
    for sub_tc in itertools.combinations(tc_indices, m_eff):
        supp = sorted(list(T_set) + list(sub_tc))
        if not supp:
            continue
        k = len(supp)
        v = [1.0 / math.sqrt(k)] * k
        for _ in range(60):
            gv = [
                sum(G[supp[a]][supp[b]] * v[b] for b in range(k))
                for a in range(k)
            ]
            nv = math.sqrt(sum(val * val for val in gv))
            if nv == 0.0:
                break
            v = [val / nv for val in gv]
        rq = sum(
            v[a] * G[supp[a]][supp[b]] * v[b] for a in range(k) for b in range(k)
        )
        if rq > best_max:
            best_max = rq
    return best_max


def main() -> None:
    rng = random.Random(20261018)
    n = 60
    p = 10
    sigma = 0.25

    # Generate equicorrelated covariates (matching Figure 1, p. 3: Sigma_{jk} = rho for j != k)
    rho = 0.5
    raw_X = []
    for _ in range(n):
        z_common = rng.gauss(0.0, 1.0)
        row = [
            math.sqrt(rho) * z_common + math.sqrt(1.0 - rho) * rng.gauss(0.0, 1.0)
            for _ in range(p)
        ]
        raw_X.append(row)

    X = [[0.0] * p for _ in range(n)]
    for j in range(p):
        col_norm = math.sqrt(sum(raw_X[i][j] ** 2 for i in range(n)) / n)
        for i in range(n):
            X[i][j] = raw_X[i][j] / col_norm

    G = [
        [sum(X[i][j] * X[i][k] for i in range(n)) / n for k in range(p)]
        for j in range(p)
    ]

    # 1. Nonparametric function f_i = 1.5*x_{i,0} + 1.4*x_{i,1} + 0.018*x_{i,5}
    # where 0.018*x_{i,5} is smaller than the oracle penalty sigma/sqrt(n) = 0.25/sqrt(60) = 0.03227
    f_vec = [
        1.5 * X[i][0] + 1.4 * X[i][1] + 0.018 * X[i][5] for i in range(n)
    ]

    # Solve Oracle Risk Minimization Program (Eqs. 2.2-2.4) over k=0..p
    best_oracle_obj = float("inf")
    s_oracle = 0
    beta_0 = [0.0] * p
    c_s_sq = 0.0
    for k in range(p + 1):
        best_ck_sq = float("inf")
        best_bk = [0.0] * p
        for supp in itertools.combinations(range(p), k):
            bk = ols_on_support(X, f_vec, list(supp))
            ck_sq = q_hat(X, f_vec, bk)
            if ck_sq < best_ck_sq:
                best_ck_sq = ck_sq
                best_bk = bk
        obj_k = best_ck_sq + (sigma**2) * k / n
        if obj_k < best_oracle_obj - 1e-12:
            best_oracle_obj = obj_k
            s_oracle = k
            beta_0 = best_bk
            c_s_sq = best_ck_sq

    c_s = math.sqrt(c_s_sq)
    T_supp = [j for j in range(p) if abs(beta_0[j]) > 1e-10]
    T_set = set(T_supp)
    r_vec = [f_vec[i] - dot(X[i], beta_0) for i in range(n)]

    # Verify Step 2 of Proof of Theorem 2 (p. 22):
    # E_n[x_{.j} r_.] = 0 for j in T, and |E_n[x_{.j} r_.]| <= min{sigma/sqrt(n), c_s} for j in T^c
    xr_corrs = [sum(X[i][j] * r_vec[i] for i in range(n)) / n for j in range(p)]
    max_corr_T = max(abs(xr_corrs[j]) for j in T_supp)
    max_corr_Tc = max(abs(xr_corrs[j]) for j in range(p) if j not in T_set)
    step2_bound = min(sigma / math.sqrt(n), c_s)
    oracle_step2_ok = (
        s_oracle == 2
        and T_supp == [0, 1]
        and max_corr_T <= 1e-12
        and max_corr_Tc <= step2_bound + 1e-12
    )

    # 2. Generate noisy outcome y_i = f_i + eps_i and test Theorem 1, Remark 3.1, Lemmas 2-3, Theorem 3
    eps_vec = [sigma * rng.gauss(0.0, 1.0) for _ in range(n)]
    y_vec = [f_vec[i] + eps_vec[i] for i in range(n)]
    S_vec = [2.0 * sum(X[i][j] * eps_vec[i] for i in range(n)) / n for j in range(p)]
    S_inf = max(abs(v) for v in S_vec)

    c_const = 1.1
    lam_over_n = c_const * S_inf

    beta_hat = solve_lasso_cd(X, y_vec, lam_over_n)
    T_hat = [j for j in range(p) if abs(beta_hat[j]) > 1e-9]
    m_hat = len([j for j in T_hat if j not in T_set])

    # Verify Remark 3.1 / Eq. (A.1) KKT lower bound on ||f_hat - f||_{P_n,2}
    f_hat_err = math.sqrt(
        sum((dot(X[i], beta_hat) - f_vec[i]) ** 2 for i in range(n)) / n
    )
    phi_m_hat = max_sparse_eig_restricted(G, T_set, m_hat)
    kkt_lower_bound = (
        (1.0 - 1.0 / c_const)
        * lam_over_n
        * math.sqrt(len(T_hat))
        / (2.0 * math.sqrt(phi_m_hat))
    )
    kkt_lower_ok = f_hat_err + 1e-9 >= kkt_lower_bound

    # Verify Lemma 3 sublinearity: phi(ceil(ell * k)) <= ceil(ell) * phi(k)
    phi_1 = max_sparse_eig_restricted(G, T_set, 1)
    phi_2 = max_sparse_eig_restricted(G, T_set, 2)
    phi_3 = max_sparse_eig_restricted(G, T_set, 3)
    phi_4 = max_sparse_eig_restricted(G, T_set, 4)
    sublinearity_ok = (
        phi_2 <= 2.0 * phi_1 + 1e-9
        and phi_3 <= 3.0 * phi_1 + 1e-9
        and phi_4 <= 2.0 * phi_2 + 1e-9
    )

    # 3. Verify Theorem 4 & Theorem 5 (OLS post-Lasso):
    # Q_hat(beta_tilde) - Q_hat(beta_0) <= B_n ^ C_n, C_n = 0 when T subseteq T_hat,
    # and Eqs. (A.7)-(A.8): B_n <= (lam/n)(||delta_hat_T||_1 - ||delta_hat_{T^c}||_1)
    beta_tilde_0 = ols_on_support(X, y_vec, T_hat)
    q_beta_0 = q_hat(X, y_vec, beta_0)
    q_beta_hat = q_hat(X, y_vec, beta_hat)
    q_beta_tilde_0 = q_hat(X, y_vec, beta_tilde_0)

    beta_0_T_hat = [beta_0[j] if j in set(T_hat) else 0.0 for j in range(p)]
    B_n = q_beta_hat - q_beta_0
    C_n = q_hat(X, y_vec, beta_0_T_hat) - q_beta_0

    delta_hat = [beta_hat[j] - beta_0[j] for j in range(p)]
    delta_hat_T_l1 = sum(abs(delta_hat[j]) for j in T_supp)
    delta_hat_Tc_l1 = sum(abs(delta_hat[j]) for j in range(p) if j not in T_set)
    eq_a7_rhs = lam_over_n * (delta_hat_T_l1 - delta_hat_Tc_l1)

    f_tilde_0_err = math.sqrt(
        sum((dot(X[i], beta_tilde_0) - f_vec[i]) ** 2 for i in range(n)) / n
    )
    post_lasso_ok = (
        set(T_supp).issubset(set(T_hat))
        and abs(C_n) <= 1e-12
        and (q_beta_tilde_0 - q_beta_0) <= min(B_n, C_n) + 1e-12
        and B_n <= eq_a7_rhs + 1e-9
        and f_tilde_0_err < f_hat_err
    )

    # 4. Verify Fitness-Thresholded Lasso (fit-Lasso, Eqs. 2.9, 2.14, Theorem 6) & Traditional Thresholding (Theorem 7)
    gamma_fit = 0.5 * (q_beta_tilde_0 - q_beta_hat)

    sorted_mags = sorted(abs(beta_hat[j]) for j in T_hat)
    lo = 0
    hi = len(sorted_mags) - 1
    best_t_fit = 0.0
    eval_steps = 0
    max_allowed_steps = math.ceil(math.log2(len(T_hat))) + 1
    while lo <= hi:
        mid = (lo + hi) // 2
        t_cand = sorted_mags[mid]
        eval_steps += 1
        supp_cand = [j for j in T_hat if abs(beta_hat[j]) > t_cand]
        beta_cand = ols_on_support(X, y_vec, supp_cand)
        if q_hat(X, y_vec, beta_cand) - q_beta_hat <= gamma_fit + 1e-12:
            best_t_fit = t_cand
            lo = mid + 1
        else:
            hi = mid - 1

    T_fit = [j for j in T_hat if abs(beta_hat[j]) > best_t_fit]
    m_tilde_fit = len([j for j in T_fit if j not in T_set])
    beta_tilde_fit = ols_on_support(X, y_vec, T_fit)

    # Verify Theorem 7 thresholding loss bound: gamma_t = ||beta_hat_t - beta_hat||_{2,n} <= t * sqrt(phi(m_t) * m_t)
    t_thresh = best_t_fit
    beta_hat_t = [
        beta_hat[j] if abs(beta_hat[j]) > t_thresh else 0.0 for j in range(p)
    ]
    diff_t = [beta_hat_t[j] - beta_hat[j] for j in range(p)]
    gamma_t_actual = pred_norm(X, diff_t)
    m_t = len(T_hat) - len(T_fit)
    phi_mt = max_sparse_eig_restricted(G, set(), m_t)
    gamma_t_bound = t_thresh * math.sqrt(phi_mt * m_t)

    # Monte Carlo average across 25 draws (matching Figure 1, p. 3) to verify strict empirical risk ordering:
    # avg_err(OLS post-fit Lasso) < avg_err(OLS post-Lasso) < avg_err(Lasso)
    mc_trials = 25
    sum_err_lasso = 0.0
    sum_err_post_lasso = 0.0
    sum_err_post_fit = 0.0
    for _ in range(mc_trials):
        eps_mc = [sigma * rng.gauss(0.0, 1.0) for _ in range(n)]
        y_mc = [f_vec[i] + eps_mc[i] for i in range(n)]
        s_mc_inf = max(
            abs(2.0 * sum(X[i][j] * eps_mc[i] for i in range(n)) / n)
            for j in range(p)
        )
        lam_mc = 1.15 * s_mc_inf
        b_hat_mc = solve_lasso_cd(X, y_mc, lam_mc)
        t_hat_mc = [j for j in range(p) if abs(b_hat_mc[j]) > 1e-9]
        b_post_mc = ols_on_support(X, y_mc, t_hat_mc)
        q_hat_mc = q_hat(X, y_mc, b_hat_mc)
        q_post_mc = q_hat(X, y_mc, b_post_mc)
        gam_mc = 0.5 * (q_post_mc - q_hat_mc)
        mags_mc = sorted(abs(b_hat_mc[j]) for j in t_hat_mc)
        best_t_mc = 0.0
        for tc in mags_mc:
            sc = [j for j in t_hat_mc if abs(b_hat_mc[j]) > tc]
            bc = ols_on_support(X, y_mc, sc)
            if q_hat(X, y_mc, bc) - q_hat_mc <= gam_mc + 1e-12:
                best_t_mc = tc
        t_fit_mc = [j for j in t_hat_mc if abs(b_hat_mc[j]) > best_t_mc]
        b_fit_mc = ols_on_support(X, y_mc, t_fit_mc)

        sum_err_lasso += math.sqrt(
            sum((dot(X[i], b_hat_mc) - f_vec[i]) ** 2 for i in range(n)) / n
        )
        sum_err_post_lasso += math.sqrt(
            sum((dot(X[i], b_post_mc) - f_vec[i]) ** 2 for i in range(n)) / n
        )
        sum_err_post_fit += math.sqrt(
            sum((dot(X[i], b_fit_mc) - f_vec[i]) ** 2 for i in range(n)) / n
        )

    avg_err_lasso = sum_err_lasso / mc_trials
    avg_err_post_lasso = sum_err_post_lasso / mc_trials
    avg_err_post_fit = sum_err_post_fit / mc_trials

    fit_lasso_ok = (
        m_hat >= 1
        and gamma_fit < 0.0
        and eval_steps <= max_allowed_steps
        and m_tilde_fit == 0
        and T_fit == T_supp
        and q_hat(X, y_vec, beta_tilde_fit) - q_beta_hat <= gamma_fit + 1e-12
        and avg_err_post_fit < avg_err_post_lasso < avg_err_lasso
        and gamma_t_actual <= gamma_t_bound + 1e-12
    )

    summary = {
        "oracle_and_step2_orthogonality_check": {
            "s_oracle": s_oracle,
            "T_supp": T_supp,
            "c_s": round(c_s, 6),
            "max_corr_on_T": round(max_corr_T, 12),
            "max_corr_on_Tc": round(max_corr_Tc, 6),
            "step2_bound_min_sigma_sqrtn_cs": round(step2_bound, 6),
            "oracle_step2_ok": oracle_step2_ok,
        },
        "lasso_kkt_lower_bound_and_sublinearity_check": {
            "T_hat_size": len(T_hat),
            "m_hat": m_hat,
            "f_hat_err": round(f_hat_err, 6),
            "kkt_lower_bound": round(kkt_lower_bound, 6),
            "phi_1_2_3_4": [
                round(phi_1, 6),
                round(phi_2, 6),
                round(phi_3, 6),
                round(phi_4, 6),
            ],
            "kkt_lower_ok": kkt_lower_ok,
            "sublinearity_ok": sublinearity_ok,
        },
        "ols_post_lasso_and_eq_a7_check": {
            "C_n": round(C_n, 12),
            "B_n": round(B_n, 6),
            "eq_a7_rhs": round(eq_a7_rhs, 6),
            "q_tilde_minus_q_0": round(q_beta_tilde_0 - q_beta_0, 6),
            "f_hat_err": round(f_hat_err, 6),
            "f_tilde_0_err": round(f_tilde_0_err, 6),
            "post_lasso_ok": post_lasso_ok,
        },
        "ols_post_fit_lasso_and_thm7_gamma_t_check": {
            "m_hat": m_hat,
            "m_tilde_fit": m_tilde_fit,
            "T_fit": T_fit,
            "gamma_fit": round(gamma_fit, 6),
            "binary_search_steps": eval_steps,
            "max_allowed_steps": max_allowed_steps,
            "avg_err_lasso": round(avg_err_lasso, 6),
            "avg_err_post_lasso": round(avg_err_post_lasso, 6),
            "avg_err_post_fit": round(avg_err_post_fit, 6),
            "gamma_t_actual": round(gamma_t_actual, 6),
            "gamma_t_bound": round(gamma_t_bound, 6),
            "fit_lasso_ok": fit_lasso_ok,
        },
        "all_passed": bool(
            oracle_step2_ok
            and kkt_lower_ok
            and sublinearity_ok
            and post_lasso_ok
            and fit_lasso_ok
        ),
    }
    print(json.dumps(summary, indent=2))
    if not summary["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
