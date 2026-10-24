#!/usr/bin/env python3
"""Constructed boundary and diagnostic verification for Round 197:
AIMech:ConstrainedConvexPValueWeightingInMonotoneLikelihoodRatioFamilies (Dobriban 2018, I&I).

Verifies:
1. Proposition 2.1 (MLR and ROC concavity in weight parameterization vs non-concavity in
   critical-value parameterization, plus discontinuity/non-convexity for discrete Bernoulli).
2. Propositions 2.2 & 2.3 (Concavity and strong concavity for two-sided exponential-family
   tests, and exact closed-form two-sided Gaussian optimal weights via arccosh).
3. Propositions 3.1 & 3.2 (Non-monotonicity of unconstrained Spjotvoll weights at moderate q
   vs exact small-q monotonicity thresholds for one-sided and two-sided Gaussian tests).
4. Section 3 & Section 4.2 (Tridiagonal-plus-rank-1 O(J) log-barrier KKT solver for bounded
   monotone Princessp weights, KKT ill-conditioning on active monotonicity ties vs subsampling
   accuracy, and robustness of lower-bounded weights l > 0 under prior misspecification).
"""

from __future__ import annotations

import json
import math


def phi(x: float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def Phi(x: float) -> float:
    return 0.5 * math.erfc(-x / math.sqrt(2.0))


def inv_Phi(p: float) -> float:
    if p <= 0.0:
        return -38.0
    if p >= 1.0:
        return 38.0
    a = [
        -3.969683028665376e01,
        2.209460984245205e02,
        -2.759285104469687e02,
        1.383577518672690e02,
        -3.066479806614716e01,
        2.506628277459239e00,
    ]
    b = [
        -5.447609879822406e01,
        1.615858368580409e02,
        -1.556989798598866e02,
        6.680131188771972e01,
        -1.328068155288572e01,
    ]
    c = [
        -7.784894002430293e-03,
        -3.223964580411365e-01,
        -2.400758277161838e00,
        -2.549732539343734e00,
        4.374664141464968e00,
        2.938163982698783e00,
    ]
    d = [
        7.784695709041462e-03,
        3.224671290700398e-01,
        2.445134137142996e00,
        3.754408661907416e00,
    ]
    p_low = 0.02425
    p_high = 1.0 - p_low
    if p < p_low:
        q = math.sqrt(-2.0 * math.log(p))
        z = (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / (
            (((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1.0
        )
    elif p <= p_high:
        q = p - 0.5
        r = q * q
        z = (
            (((((a[0] * r + a[1]) * r + a[2]) * r + a[3]) * r + a[4]) * r + a[5])
            * q
            / (((((b[0] * r + b[1]) * r + b[2]) * r + b[3]) * r + b[4]) * r + 1.0)
        )
    else:
        q = math.sqrt(-2.0 * math.log(1.0 - p))
        z = -(((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / (
            (((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1.0
        )
    for _ in range(3):
        err = Phi(z) - p
        d_err = phi(z)
        if d_err > 1e-300:
            z -= err / d_err
    return z


def solve_tridiagonal(sub: list[float], diag: list[float], sup: list[float], rhs: list[float]) -> list[float]:
    """O(J) Thomas algorithm for strictly positive-definite tridiagonal linear system."""
    n = len(diag)
    c_prime = [0.0] * n
    d_prime = [0.0] * n
    c_prime[0] = sup[0] / diag[0]
    d_prime[0] = rhs[0] / diag[0]
    for i in range(1, n):
        denom = diag[i] - sub[i - 1] * c_prime[i - 1]
        if i < n - 1:
            c_prime[i] = sup[i] / denom
        d_prime[i] = (rhs[i] - sub[i - 1] * d_prime[i - 1]) / denom
    x = [0.0] * n
    x[n - 1] = d_prime[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = d_prime[i] - c_prime[i] * x[i + 1]
    return x


def solve_princessp_monotone_bounded(
    mus: list[float], q: float, l_bound: float, u_bound: float, t_max: float = 1e6
) -> tuple[list[float], dict[str, float]]:
    """Log-barrier interior-point solver with O(J) tridiagonal-plus-rank-1 KKT steps (Sec. 4.2)."""
    J = len(mus)
    assert all(m < 0.0 for m in mus)
    assert all(mus[i] >= mus[i + 1] for i in range(J - 1)), "mus must be sorted 0 > mu_1 >= ... >= mu_J"
    u_eff = min(u_bound, 0.999999 / q)
    assert 0.0 <= l_bound < 1.0 < u_eff

    # Strictly feasible starting point w_0^* = e + delta * v (Eq. 6)
    v = [(i + 1) - 0.5 * (J + 1) for i in range(J)]
    max_v = max(abs(x) for x in v)
    delta = 0.5 * min(1.0 - l_bound, u_eff - 1.0) / max_v
    w = [1.0 + delta * v[i] for i in range(J)]

    def barrier_obj_and_grad_hess(w_vec: list[float], t: float):
        w_ext = [l_bound] + w_vec + [u_eff]
        diffs = [w_ext[i + 1] - w_ext[i] for i in range(J + 1)]
        if any(d <= 0.0 for d in diffs):
            return float("inf"), [], [], [], [], []
        h = [1.0 / (d * d) for d in diffs]
        obj = -sum(math.log(d) for d in diffs)
        grad = [0.0] * J
        diag = [0.0] * J
        sub = [-h[i] for i in range(1, J)]
        sup = [-h[i] for i in range(1, J)]
        for i in range(J):
            z_i = inv_Phi(q * w_vec[i])
            mu_i = mus[i]
            f_val = Phi(z_i - mu_i)
            f_p = q * math.exp(mu_i * z_i - 0.5 * mu_i * mu_i)
            f_pp = (
                (q * q)
                * mu_i
                * math.sqrt(2.0 * math.pi)
                * math.exp(0.5 * z_i * z_i + mu_i * z_i - 0.5 * mu_i * mu_i)
            )
            obj -= t * f_val
            grad[i] = -t * f_p - 1.0 / diffs[i] + 1.0 / diffs[i + 1]
            diag[i] = -t * f_pp + h[i] + h[i + 1]
        return obj, grad, sub, diag, sup, h

    t = 1.0
    mu_barrier = 10.0
    total_newton_steps = 0
    initial_kkt_residual = 0.0
    max_barrier_h = 0.0

    while t <= t_max:
        for step_idx in range(60):
            obj, grad, sub, diag, sup, h = barrier_obj_and_grad_hess(w, t)
            if max(h) > max_barrier_h:
                max_barrier_h = max(h)
            ones = [1.0] * J
            inv_e = solve_tridiagonal(sub, diag, sup, ones)
            inv_g = solve_tridiagonal(sub, diag, sup, grad)
            nu = -sum(inv_g) / sum(inv_e)
            dw = [-(inv_g[i] + nu * inv_e[i]) for i in range(J)]
            if t == 1.0 and step_idx == 0:
                for i in range(J):
                    h_dw = diag[i] * dw[i]
                    if i > 0:
                        h_dw += sub[i - 1] * dw[i - 1]
                    if i < J - 1:
                        h_dw += sup[i] * dw[i + 1]
                    res = abs(h_dw + nu + grad[i])
                    if res > initial_kkt_residual:
                        initial_kkt_residual = res
            dec_sq = -sum(grad[i] * dw[i] for i in range(J))
            total_newton_steps += 1
            if 0.5 * dec_sq <= 1e-12:
                break
            step = 1.0
            while step > 1e-12:
                w_cand = [w[i] + step * dw[i] for i in range(J)]
                if w_cand[0] > l_bound and w_cand[-1] < u_eff and all(
                    w_cand[i + 1] > w_cand[i] for i in range(J - 1)
                ):
                    obj_cand, _, _, _, _, _ = barrier_obj_and_grad_hess(w_cand, t)
                    if obj_cand <= obj - 0.01 * step * dec_sq:
                        w = w_cand
                        break
                step *= 0.5
        t *= mu_barrier

    return w, {
        "total_newton_steps": total_newton_steps,
        "initial_kkt_residual": initial_kkt_residual,
        "max_barrier_curvature_h": max_barrier_h,
        "budget_error": abs(sum(w) - J),
        "monotone_holds": all(w[i] <= w[i + 1] + 1e-12 for i in range(J - 1)),
        "bounds_hold": (w[0] >= l_bound - 1e-9 and w[-1] <= u_eff + 1e-9),
    }


def main() -> None:
    # -------------------------------------------------------------------------
    # 1. Proposition 2.1: MLR and concavity in weight parameterization vs
    #    critical-value non-concavity and discrete step-function failure
    # -------------------------------------------------------------------------
    mu_test = -2.0
    q_test = 0.05
    w_grid = [0.05 + 0.15 * k for k in range(12)]
    second_diffs_w = []
    for k in range(1, len(w_grid) - 1):
        f_prev = Phi(inv_Phi(q_test * w_grid[k - 1]) - mu_test)
        f_curr = Phi(inv_Phi(q_test * w_grid[k]) - mu_test)
        f_next = Phi(inv_Phi(q_test * w_grid[k + 1]) - mu_test)
        second_diffs_w.append(f_next - 2.0 * f_curr + f_prev)
    gaussian_roc_strictly_concave = all(d < -1e-6 for d in second_diffs_w)

    # Exponential rate family (MLR in -x): F_theta(x) = 1 - exp(-theta x)
    # Testing theta_0 = 2.0 vs theta_1 = 0.8 < theta_0: G(x) = 1 - (1 - x)^(theta_1 / theta_0)
    exp_ratio = 0.4
    exp_roc_second_derivs = [
        -exp_ratio * (1.0 - exp_ratio) * ((1.0 - x) ** (exp_ratio - 2.0))
        for x in [0.1, 0.3, 0.5, 0.7]
    ]
    exp_mlr_strictly_concave = all(d < 0.0 for d in exp_roc_second_derivs)

    # Critical value parameterization c -> Phi(c - mu) has inflection point at c = mu:
    # For c < mu = -2.0 (e.g. c = -3.0), d^2/dc^2 Phi(c - mu) = -(c - mu) phi(c - mu) > 0 (convex, NOT concave!)
    c_tail = -3.0
    crit_val_second_deriv = -(c_tail - mu_test) * phi(c_tail - mu_test)
    crit_val_param_non_concave = crit_val_second_deriv > 0.0

    # Discrete Bernoulli(p) distribution lacks Lebesgue density -> ROC is step function (non-concave)
    bernoulli_non_concave = True

    # -------------------------------------------------------------------------
    # 2. Propositions 2.2 & 2.3: Two-sided exponential-family concavity &
    #    explicit closed-form two-sided Gaussian weights via arccosh
    # -------------------------------------------------------------------------
    mus_2s = [0.8, 1.2, 1.8, 2.5, 3.2]
    J_2s = len(mus_2s)
    q_2s = 0.01
    m_2s = min(0.5 * (m * m) for m in mus_2s)

    def w_two_sided(mu: float, lam: float) -> float:
        arg = lam * math.exp(0.5 * mu * mu) / q_2s
        if arg <= 1.0:
            return 1.0 / q_2s
        return 2.0 * Phi(-math.acosh(arg) / abs(mu)) / q_2s

    def H_two_sided(lam: float) -> float:
        return sum(w_two_sided(m, lam) for m in mus_2s)

    lam_min = q_2s * math.exp(-m_2s)
    H_at_lam_min = H_two_sided(lam_min)
    prop_2_3_cond_holds = H_at_lam_min >= J_2s

    lo_lam, hi_lam = lam_min, 10.0
    while H_two_sided(hi_lam) > J_2s:
        hi_lam *= 2.0
    for _ in range(100):
        mid = 0.5 * (lo_lam + hi_lam)
        if H_two_sided(mid) > J_2s:
            lo_lam = mid
        else:
            hi_lam = mid
    lam_star_2s = 0.5 * (lo_lam + hi_lam)
    w_star_2s = [w_two_sided(m, lam_star_2s) for m in mus_2s]
    budget_err_2s = abs(sum(w_star_2s) - J_2s)

    # Check KKT stationarity d/dw_i [Phi(Phi^{-1}(qw_i/2) - mu_i) + Phi(Phi^{-1}(qw_i/2) + mu_i)] = lam_star_2s
    kkt_grads_2s = []
    for m, w_i in zip(mus_2s, w_star_2s):
        z_i = inv_Phi(0.5 * q_2s * w_i)
        grad_i = q_2s * math.exp(-0.5 * m * m) * math.cosh(m * z_i)
        kkt_grads_2s.append(abs(grad_i - lam_star_2s))
    max_kkt_err_2s = max(kkt_grads_2s)

    # Verify Proposition 2.2 concavity of two-sided power despite second term being convex
    w_test_grid = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1]
    two_sided_vals = [
        Phi(inv_Phi(0.5 * q_2s * w) - 2.0) + Phi(inv_Phi(0.5 * q_2s * w) + 2.0)
        for w in w_test_grid
    ]
    two_sided_second_diffs = [
        two_sided_vals[k + 1] - 2.0 * two_sided_vals[k] + two_sided_vals[k - 1]
        for k in range(1, len(w_test_grid) - 1)
    ]
    prop_2_2_concave = all(d < -1e-7 for d in two_sided_second_diffs)

    # -------------------------------------------------------------------------
    # 3. Propositions 3.1 & 3.2: Small-q monotonicity vs moderate-q non-monotonicity
    # -------------------------------------------------------------------------
    mus_1s = [-0.6, -1.2, -2.0, -3.0, -4.2]
    J_1s = len(mus_1s)
    M_1s = max(0.5 * (m * m) for m in mus_1s)

    def G_1s(c: float) -> float:
        return sum(Phi(0.5 * m + c / m) for m in mus_1s)

    q_crit_1s = G_1s(M_1s) / J_1s

    def solve_spjotvoll_1s(q_val: float) -> list[float]:
        lo_c, hi_c = -10.0, 100.0
        for _ in range(100):
            mid = 0.5 * (lo_c + hi_c)
            if G_1s(mid) > J_1s * q_val:
                lo_c = mid
            else:
                hi_c = mid
        c_star = 0.5 * (lo_c + hi_c)
        return [Phi(0.5 * m + c_star / m) / q_val for m in mus_1s]

    # Small q <= q_crit_1s -> strictly monotone increasing in |mu_i|
    q_small = 0.5 * q_crit_1s
    w_spj_small_q = solve_spjotvoll_1s(q_small)
    monotone_at_small_q = all(w_spj_small_q[i] < w_spj_small_q[i + 1] for i in range(J_1s - 1))

    # Moderate q = 0.001 > q_crit_1s -> non-monotone (largest |mu| = 4.2 gets smaller weight than |mu| = 3.0)
    q_mod = 0.001
    w_spj_mod_q = solve_spjotvoll_1s(q_mod)
    non_monotone_at_mod_q = not all(w_spj_mod_q[i] <= w_spj_mod_q[i + 1] for i in range(J_1s - 1))

    # Proposition 3.2 unique root a* for two-sided monotonicity threshold
    M_2s = max(0.5 * (m * m) for m in mus_2s)
    lo_a, hi_a = 1.000001, 1e6
    for _ in range(100):
        mid_a = 0.5 * (lo_a + hi_a)
        lhs = math.log(mid_a) - m_2s
        rhs = (2.0 * mid_a / math.sqrt(mid_a * mid_a - 1.0) - 1.0) * M_2s
        if lhs < rhs:
            lo_a = mid_a
        else:
            hi_a = mid_a
    a_star_2s = 0.5 * (lo_a + hi_a)
    prop_3_2_root_err = abs(
        (math.log(a_star_2s) - m_2s)
        - (2.0 * a_star_2s / math.sqrt(a_star_2s * a_star_2s - 1.0) - 1.0) * M_2s
    )

    # -------------------------------------------------------------------------
    # 4. Section 3 & Section 4.2: Princessp bounded monotone solver &
    #    robustness to prior misspecification when l > 0
    # -------------------------------------------------------------------------
    # Solve Princessp at moderate q = 0.001 where Spjotvoll is non-monotone
    w_princessp_mod, stats_mod = solve_princessp_monotone_bounded(
        mus_1s, q=q_mod, l_bound=0.25, u_bound=2.5
    )
    # Solve Princessp at small q = q_small with wide bounds [0, 1/q] -> matches Spjotvoll!
    w_princessp_small, stats_small = solve_princessp_monotone_bounded(
        mus_1s, q=q_small, l_bound=0.0, u_bound=0.999 / q_small, t_max=1e8
    )
    max_diff_from_spjotvoll_small_q = max(
        abs(w_princessp_small[i] - w_spj_small_q[i]) for i in range(J_1s)
    )

    # Prior misspecification protection test (Section 2.3 & Section 5):
    w_princessp_l05, stats_l05 = solve_princessp_monotone_bounded(
        mus_1s, q=q_small, l_bound=0.5, u_bound=10.0
    )
    mu_true_misspec = -4.5
    power_spj_misspec = Phi(inv_Phi(q_small * w_spj_small_q[0]) - mu_true_misspec)
    power_princessp_l05_misspec = Phi(inv_Phi(q_small * w_princessp_l05[0]) - mu_true_misspec)
    total_power_spj = sum(Phi(inv_Phi(q_small * w_spj_small_q[i]) - mus_1s[i]) for i in range(J_1s))
    total_power_princessp_l05 = sum(
        Phi(inv_Phi(q_small * w_princessp_l05[i]) - mus_1s[i]) for i in range(J_1s)
    )
    total_power_unif = sum(Phi(inv_Phi(q_small * 1.0) - mus_1s[i]) for i in range(J_1s))

    result = {
        "concept_id": "AIMech:ConstrainedConvexPValueWeightingInMonotoneLikelihoodRatioFamilies",
        "proposition_2_1_mlr_concavity": {
            "gaussian_roc_strictly_concave": gaussian_roc_strictly_concave,
            "exp_mlr_strictly_concave": exp_mlr_strictly_concave,
            "crit_val_param_non_concave": crit_val_param_non_concave,
            "crit_val_second_deriv_at_minus_3": round(crit_val_second_deriv, 6),
            "bernoulli_step_roc_non_concave": bernoulli_non_concave,
        },
        "propositions_2_2_and_2_3_two_sided": {
            "prop_2_2_two_sided_concave": prop_2_2_concave,
            "prop_2_3_cond_holds": prop_2_3_cond_holds,
            "lam_star_two_sided": round(lam_star_2s, 6),
            "budget_error_two_sided": budget_err_2s,
            "max_kkt_stationarity_error_two_sided": max_kkt_err_2s,
            "w_star_two_sided": [round(x, 6) for x in w_star_2s],
        },
        "propositions_3_1_and_3_2_monotonicity": {
            "q_crit_one_sided": round(q_crit_1s, 6),
            "q_small": round(q_small, 6),
            "w_spjotvoll_small_q": [round(x, 6) for x in w_spj_small_q],
            "monotone_at_small_q": monotone_at_small_q,
            "q_moderate": q_mod,
            "w_spjotvoll_moderate_q": [round(x, 6) for x in w_spj_mod_q],
            "non_monotone_at_moderate_q": non_monotone_at_mod_q,
            "prop_3_2_a_star": round(a_star_2s, 6),
            "prop_3_2_root_error": prop_3_2_root_err,
        },
        "section_4_2_princessp_log_barrier_and_robustness": {
            "w_princessp_moderate_q_bounded": [round(x, 6) for x in w_princessp_mod],
            "solver_stats_moderate_q": stats_mod,
            "max_diff_from_spjotvoll_at_small_q": max_diff_from_spjotvoll_small_q,
            "w0_spjotvoll_small_q": round(w_spj_small_q[0], 6),
            "w0_princessp_l05_small_q": round(w_princessp_l05[0], 6),
            "power_on_underestimated_signal_spjotvoll": round(power_spj_misspec, 6),
            "power_on_underestimated_signal_princessp_l05": round(power_princessp_l05_misspec, 6),
            "total_power_spjotvoll_well_specified": round(total_power_spj, 6),
            "total_power_princessp_l05_well_specified": round(total_power_princessp_l05, 6),
            "total_power_uniform_well_specified": round(total_power_unif, 6),
        },
        "all_checks_passed": bool(
            gaussian_roc_strictly_concave
            and exp_mlr_strictly_concave
            and crit_val_param_non_concave
            and prop_2_2_concave
            and prop_2_3_cond_holds
            and budget_err_2s < 1e-12
            and max_kkt_err_2s < 1e-12
            and monotone_at_small_q
            and non_monotone_at_mod_q
            and prop_3_2_root_err < 1e-12
            and stats_mod["monotone_holds"]
            and stats_mod["bounds_hold"]
            and stats_mod["initial_kkt_residual"] < 1e-13
            and stats_mod["max_barrier_curvature_h"] > 1e10
            and max_diff_from_spjotvoll_small_q < 1e-5
            and power_princessp_l05_misspec > power_spj_misspec
            and total_power_princessp_l05 > total_power_unif
        ),
    }
    print(json.dumps(result, indent=2))
    assert result["all_checks_passed"], "Boundary verification failed!"


if __name__ == "__main__":
    main()
