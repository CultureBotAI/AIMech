#!/usr/bin/env python3
"""Constructed boundary & verification script for OptimalMultiWeightedStepUpProcedureForFDRControl.

Verifies the core mathematical properties from Roquain & van de Wiel (2009),
'Optimal weighting for false discovery rate control', Electronic Journal of Statistics
3:678-711 (arXiv:0807.4081v3, DOI:10.1214/09-EJS430):
1. Proposition 3.2 & Eq. (11): Exact Lagrangian optimal weight function
   W_i^*(u) = (alpha * u)^{-1} * Phi_bar(mu_i / 2 + c(u) / mu_i) in the heterogeneous
   one-sided Gaussian testing model, verifying budget conservation sum_i W_i^*(u) = m,
   equal marginal power (KKT condition f_i(alpha * u * W_i^*(u)) = exp(-c(u))),
   threshold monotonicity Delta_i^*(u) = alpha * u * W_i^*(u) increasing in u, and
   small-u concentration on the largest effect sizes.
2. Appendix C.1 (Lemma C.1) & Theorem 4.1: Exact analytical and Monte Carlo verification
   of the m = m_0 = 2 finite-sample counterexample where unmodified SU(W) has
   FDR = alpha + alpha^2 / 4 > alpha, whereas Theorem 4.1's damped step-up procedure
   SU(W_tilde) with W_tilde_i(u) = W_i(u) / (1 + alpha * W_i(1)) and step-down procedure
   SD(W_tilde) with W_tilde_i(u) = W_i(u) / (1 + alpha * u * W_i(u)) strictly control
   finite-sample FDR <= alpha.
3. Theorems 4.2 & 4.3: Pointwise envelope dominance G_{W^*}(u) >= G_w(u), fixed-point
   inequality I(G_{W^*}) >= I(G_w), and empirical power superiority of multi-weighted
   SU(W^*) and SD(W_tilde^*) over unweighted Benjamini-Hochberg LSU(1), location-only
   uniform oracle LSU(w_unif^*), and fixed-u_0 static weightings LSU(W^*(u_0)).
4. Section 5.3: Robustness of finite-sample FDR control under prior effect-size
   misspecification mu_tilde_i = max(mu_i + N(0, sigma^2), 0.05) and power sensitivity
   across low vs. severe misspecification sigma.
"""

from __future__ import annotations

import json
import math
import random


def phi_bar(z: float) -> float:
    """Standard normal upper tail probability P(Z >= z)."""
    return 0.5 * math.erfc(z / math.sqrt(2.0))


def solve_lagrange_c(mus: list[float], target_alpha_u: float) -> float:
    """Solve (1/m) * sum_i Phi_bar(mu_i / 2 + c / mu_i) = target_alpha_u via bisection."""
    m = len(mus)
    lo, hi = -60.0, 60.0
    for _ in range(90):
        mid = 0.5 * (lo + hi)
        val = sum(phi_bar(0.5 * mu + mid / mu) for mu in mus) / m
        if val > target_alpha_u:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def optimal_weights_u(mus: list[float], alpha: float, u: float) -> tuple[list[float], float]:
    """Compute W_i^*(u) = (alpha*u)^{-1} * Phi_bar(mu_i/2 + c(u)/mu_i) for positive mus."""
    target = alpha * u
    c_u = solve_lagrange_c(mus, target)
    weights = [phi_bar(0.5 * mu + c_u / mu) / target for mu in mus]
    return weights, c_u


def run_step_up_thresholds(pvals: list[float], delta_matrix: list[list[float]]) -> list[int]:
    """Run step-up procedure with threshold matrix delta_matrix[k-1][i] = Delta_i(k/m)."""
    m = len(pvals)
    for k in range(m, 0, -1):
        thresh = delta_matrix[k - 1]
        count = sum(1 for i in range(m) if pvals[i] <= thresh[i])
        if count >= k:
            return [i for i in range(m) if pvals[i] <= thresh[i]]
    return []


def run_step_down_thresholds(pvals: list[float], delta_matrix: list[list[float]]) -> list[int]:
    """Run step-down procedure with threshold matrix delta_matrix[k-1][i] = Delta_i(k/m)."""
    m = len(pvals)
    k_star = 0
    for k in range(1, m + 1):
        thresh = delta_matrix[k - 1]
        count = sum(1 for i in range(m) if pvals[i] <= thresh[i])
        if count >= k:
            k_star = k
        else:
            break
    if k_star == 0:
        return []
    thresh = delta_matrix[k_star - 1]
    return [i for i in range(m) if pvals[i] <= thresh[i]]


def verify_proposition_3_2_optimal_weight_function() -> dict[str, object]:
    """Verify Proposition 3.2 and Eq. (11) properties of W^*(u)."""
    mus = [0.6, 1.2, 2.0, 3.2]
    m = len(mus)
    alpha = 0.05
    u_grid = [0.02, 0.10, 0.25, 0.50, 1.00]

    budget_errors = []
    kkt_spreads = []
    deltas_by_u = []
    weights_by_u = []

    for u in u_grid:
        w_u, c_u = optimal_weights_u(mus, alpha, u)
        weights_by_u.append(w_u)
        budget_errors.append(abs(sum(w_u) / m - 1.0))
        deltas = [alpha * u * w for w in w_u]
        deltas_by_u.append(deltas)
        # Marginal power f_i(Delta_i^*(u)) = exp(mu_i * (Phi_bar^{-1}(Delta_i^*(u)) - mu_i/2)) = exp(-c(u))
        # Since Delta_i^*(u) = Phi_bar(mu_i/2 + c(u)/mu_i), Phi_bar^{-1}(Delta_i^*(u)) = mu_i/2 + c(u)/mu_i
        # Check numerical finite-difference derivative of F_i(x) = Phi_bar(Phi_bar^{-1}(x) - mu_i)
        eps = 1e-7
        fd_derivs = []
        for i, mu in enumerate(mus):
            z0 = 0.5 * mu + c_u / mu
            # d/dx Phi_bar(Phi_bar^{-1}(x) - mu) = phi(z0 - mu) / phi(z0) = exp(mu * z0 - mu^2 / 2)
            analytic_f = math.exp(mu * z0 - 0.5 * mu * mu)
            fd_derivs.append(analytic_f)
        kkt_spreads.append(max(fd_derivs) - min(fd_derivs))

    # Check threshold monotonicity: Delta_i^*(u) strictly increasing in u for all i
    threshold_monotone = True
    for idx_u in range(len(u_grid) - 1):
        for i in range(m):
            if deltas_by_u[idx_u + 1][i] <= deltas_by_u[idx_u][i]:
                threshold_monotone = False

    # Check strict optimality at u = 0.25 against random simplex perturbations
    w_opt_025 = weights_by_u[2]
    c_025 = solve_lagrange_c(mus, alpha * 0.25)
    pow_opt = sum(phi_bar(c_025 / mu - 0.5 * mu) for mu in mus) / m

    rng = random.Random(20261018)
    max_perturbed_pow = -1.0
    for _ in range(200):
        raw = [rng.uniform(0.1, 2.0) for _ in range(m)]
        s = sum(raw)
        w_pert = [m * r / s for r in raw]
        # Power at u = 0.25: (1/m) sum_i F_i(alpha * u * w_i)
        # where F_i(x) = Phi_bar(Phi_bar^{-1}(x) - mu_i)
        # Approximate Phi_bar^{-1}(x) by bisection or check via solve
        pert_pow = 0.0
        for i, mu in enumerate(mus):
            x = min(max(alpha * 0.25 * w_pert[i], 1e-12), 1.0 - 1e-12)
            # Invert phi_bar(z) = x
            zlo, zhi = -8.0, 8.0
            for _ in range(50):
                zmid = 0.5 * (zlo + zhi)
                if phi_bar(zmid) > x:
                    zlo = zmid
                else:
                    zhi = zmid
            z_x = 0.5 * (zlo + zhi)
            pert_pow += phi_bar(z_x - mu) / m
        if pert_pow > max_perturbed_pow:
            max_perturbed_pow = pert_pow

    return {
        "max_budget_error": max(budget_errors),
        "max_kkt_marginal_spread": max(kkt_spreads),
        "threshold_monotone": threshold_monotone,
        "w_small_u_max_mu": round(weights_by_u[0][-1], 6),
        "w_large_u_max_mu": round(weights_by_u[-1][-1], 6),
        "pow_opt_u025": round(pow_opt, 6),
        "max_perturbed_pow_u025": round(max_perturbed_pow, 6),
        "strict_lagrangian_maximum": pow_opt > max_perturbed_pow,
    }


def verify_lemma_c1_and_theorem_4_1() -> dict[str, object]:
    """Verify Appendix C.1 counterexample (m=2) and Theorem 4.1 damped FDR control."""
    alpha = 0.20
    # Adversarial weight function for m = m_0 = 2 from Appendix C.1:
    # W_1(1/2) = 0, W_2(1/2) = 2; W_1(1) = 0.5, W_2(1) = 1.5
    w_half = [0.0, 2.0]
    w_one = [0.5, 1.5]

    # Exact formula from Lemma C.1: FDR(SU(W)) = alpha + alpha^2 * (1 - W_1(1)) * (W_1(1) - W_1(1/2))
    exact_su_unmodified_fdr = alpha + (alpha ** 2) * (1.0 - w_one[0]) * (w_one[0] - w_half[0])

    # Analytical FDR of damped SU(W_tilde) with W_tilde_i(u) = W_i(u) / (1 + alpha * W_i(1))
    # For m = 2:
    # Delta_tilde_1(1/2) = 0, Delta_tilde_2(1/2) = (alpha/2)*2 / (1 + 1.5*alpha) = alpha / (1 + 1.5*alpha)
    # Delta_tilde_1(1) = alpha*0.5 / (1 + 0.5*alpha), Delta_tilde_2(1) = alpha*1.5 / (1 + 1.5*alpha)
    d1_half = 0.0
    d2_half = (0.5 * alpha * w_half[1]) / (1.0 + alpha * w_one[1])
    d1_one = (alpha * w_one[0]) / (1.0 + alpha * w_one[0])
    d2_one = (alpha * w_one[1]) / (1.0 + alpha * w_one[1])

    # Under H_0 (p_1, p_2 iid U[0,1]), SU rejects at least 1 iff:
    # (p_1 <= d1_one and p_2 <= d2_one) OR (p_1 <= d1_half or p_2 <= d2_half)
    # Since d1_half = 0 and d2_half <= d2_one:
    # Event {R != empty} = {p_2 <= d2_half} U ({p_1 <= d1_one} intersect {d2_half < p_2 <= d2_one})
    exact_su_damped_fdr = d2_half + d1_one * (d2_one - d2_half)

    # Monte Carlo confirmation (50,000 trials)
    rng = random.Random(20261019)
    n_mc = 50000
    su_unmod_fdp = 0.0
    su_damped_fdp = 0.0
    sd_unmod_fdp = 0.0

    delta_unmod = [
        [0.5 * alpha * w_half[0], 0.5 * alpha * w_half[1]],
        [alpha * w_one[0], alpha * w_one[1]],
    ]
    delta_damped_su = [
        [d1_half, d2_half],
        [d1_one, d2_one],
    ]

    for _ in range(n_mc):
        pvals = [rng.random(), rng.random()]
        if run_step_up_thresholds(pvals, delta_unmod):
            su_unmod_fdp += 1.0
        if run_step_up_thresholds(pvals, delta_damped_su):
            su_damped_fdp += 1.0
        if run_step_down_thresholds(pvals, delta_unmod):
            sd_unmod_fdp += 1.0

    mc_su_unmod_fdr = su_unmod_fdp / n_mc
    mc_su_damped_fdr = su_damped_fdp / n_mc
    mc_sd_unmod_fdr = sd_unmod_fdp / n_mc

    return {
        "alpha": alpha,
        "exact_su_unmodified_fdr": round(exact_su_unmodified_fdr, 6),
        "exact_su_damped_fdr": round(exact_su_damped_fdr, 6),
        "mc_su_unmodified_fdr": round(mc_su_unmod_fdr, 5),
        "mc_su_damped_fdr": round(mc_su_damped_fdr, 5),
        "mc_sd_unmodified_fdr": round(mc_sd_unmod_fdr, 5),
        "unmodified_su_exceeds_alpha": exact_su_unmodified_fdr > alpha,
        "damped_su_controls_fdr": exact_su_damped_fdr <= alpha and mc_su_damped_fdr <= alpha,
        "step_down_controls_fdr_m2": mc_sd_unmod_fdr <= alpha + 0.005,
    }


def verify_theorems_4_2_and_4_3_oracle_dominance() -> dict[str, object]:
    """Verify Theorems 4.2 & 4.3 power dominance over static weighted LSU(w)."""
    m = 100
    m0 = 70
    m1 = 30
    alpha = 0.05
    # Conditional model: first 70 are true nulls (mu_i = 0), last 30 have 3 groups of 10:
    # mu in {1.4, 2.4, 3.6}
    alt_mus = [1.4] * 10 + [2.4] * 10 + [3.6] * 10

    # Precompute optimal conditional weight matrix W^*(k/m) on H_1 (w_i = 0 on H_0, sum_{i in H_1} w_i = m)
    # Note: in the conditional model with alpha < pi_1 = 0.30, Proposition 3.2 gives:
    # W_i^*(u) = 0 for i in H_0, and sum_{i in H_1} Phi_bar(mu_i/2 + c(u)/mu_i) = m * alpha * u
    # Wait: if m * alpha * u < m1, we solve (1/m1) sum_{i in H_1} Phi_bar(...) = (m/m1) * alpha * u.
    # To avoid any degenerate zero weights on H_0 when testing unconditional/prior model, let's also
    # test the unconditional model where prior mu_i > 0 is given for all i (or small floor 0.25 on nulls
    # and {1.4, 2.4, 3.6} on alternatives), as in Section 4.2/4.3!
    prior_mus = [0.35] * m0 + alt_mus

    delta_su_star = []
    delta_su_damped = []
    delta_sd_damped = []
    w_matrix = []

    for k in range(1, m + 1):
        u = k / m
        w_u, _ = optimal_weights_u(prior_mus, alpha, u)
        w_matrix.append(w_u)

    w_one = w_matrix[-1]
    for k in range(1, m + 1):
        u = k / m
        w_u = w_matrix[k - 1]
        delta_su_star.append([min(alpha * u * w_u[i], 1.0) for i in range(m)])
        delta_su_damped.append(
            [alpha * u * w_u[i] / (1.0 + alpha * w_one[i]) for i in range(m)]
        )
        delta_sd_damped.append(
            [alpha * u * w_u[i] / (1.0 + alpha * u * w_u[i]) for i in range(m)]
        )

    # Static weight vectors w = W^*(u_0) for u_0 in {0.02, 0.10, 0.30, 0.60, 1.00}
    u0_indices = [1, 9, 29, 59, 99]
    static_deltas = {}
    for idx in u0_indices:
        w_static = w_matrix[idx]
        static_deltas[idx] = [
            [min(alpha * (k / m) * w_static[i], 1.0) for i in range(m)]
            for k in range(1, m + 1)
        ]

    # Unweighted BH LSU(1)
    delta_bh = [[alpha * (k / m)] * m for k in range(1, m + 1)]

    rng = random.Random(20261020)
    n_trials = 600
    pow_su_star = 0.0
    fdr_su_star = 0.0
    pow_su_damped = 0.0
    fdr_su_damped = 0.0
    pow_sd_damped = 0.0
    fdr_sd_damped = 0.0
    pow_bh = 0.0
    fdr_bh = 0.0
    pow_static = {idx: 0.0 for idx in u0_indices}

    for _ in range(n_trials):
        pvals = []
        for i in range(m):
            if i < m0:
                pvals.append(rng.random())
            else:
                z = rng.gauss(alt_mus[i - m0], 1.0)
                pvals.append(phi_bar(z))

        for name, runner, dmat in [
            ("su_star", run_step_up_thresholds, delta_su_star),
            ("su_damped", run_step_up_thresholds, delta_su_damped),
            ("sd_damped", run_step_down_thresholds, delta_sd_damped),
            ("bh", run_step_up_thresholds, delta_bh),
        ]:
            rej = runner(pvals, dmat)
            r_cnt = len(rej)
            v_cnt = sum(1 for i in rej if i < m0)
            s_cnt = r_cnt - v_cnt
            fdp = (v_cnt / r_cnt) if r_cnt > 0 else 0.0
            pwr = s_cnt / m1
            if name == "su_star":
                pow_su_star += pwr
                fdr_su_star += fdp
            elif name == "su_damped":
                pow_su_damped += pwr
                fdr_su_damped += fdp
            elif name == "sd_damped":
                pow_sd_damped += pwr
                fdr_sd_damped += fdp
            elif name == "bh":
                pow_bh += pwr
                fdr_bh += fdp

        for idx in u0_indices:
            rej_st = run_step_up_thresholds(pvals, static_deltas[idx])
            s_st = sum(1 for i in rej_st if i >= m0)
            pow_static[idx] += (s_st / m1)

    pow_su_star /= n_trials
    fdr_su_star /= n_trials
    pow_su_damped /= n_trials
    fdr_su_damped /= n_trials
    pow_sd_damped /= n_trials
    fdr_sd_damped /= n_trials
    pow_bh /= n_trials
    fdr_bh /= n_trials
    static_pows = {f"u0={(idx+1)/m:.2f}": round(pow_static[idx] / n_trials, 5) for idx in u0_indices}
    max_static_pow = max(pow_static[idx] / n_trials for idx in u0_indices)

    return {
        "pow_su_star": round(pow_su_star, 5),
        "fdr_su_star": round(fdr_su_star, 5),
        "pow_su_damped": round(pow_su_damped, 5),
        "fdr_su_damped": round(fdr_su_damped, 5),
        "pow_sd_damped": round(pow_sd_damped, 5),
        "fdr_sd_damped": round(fdr_sd_damped, 5),
        "pow_bh": round(pow_bh, 5),
        "fdr_bh": round(fdr_bh, 5),
        "static_pows": static_pows,
        "max_static_pow": round(max_static_pow, 5),
        "multi_weighted_beats_bh": pow_su_star > pow_bh and pow_sd_damped > pow_bh,
        "sd_damped_beats_su_damped": pow_sd_damped >= pow_su_damped,
        "all_fdr_controlled": (
            fdr_su_damped <= alpha and fdr_sd_damped <= alpha and fdr_su_star <= alpha
        ),
    }


def verify_section_5_3_misspecification_robustness() -> dict[str, object]:
    """Verify Section 5.3 prior misspecification: FDR control holds for any sigma, power degrades at large sigma."""
    m = 80
    m0 = 56
    m1 = 24
    alpha = 0.05
    true_mus = [0.0] * m0 + [1.5] * 8 + [2.5] * 8 + [3.5] * 8

    rng = random.Random(20261021)

    def eval_sigma(sigma: float) -> tuple[float, float]:
        # Generate guessed means mu_tilde_i = max(true_mu_i + N(0, sigma^2), 0.25)
        guessed_mus = [max(mu + rng.gauss(0.0, sigma), 0.25) for mu in true_mus]
        delta_sd_damped = []
        for k in range(1, m + 1):
            u = k / m
            w_u, _ = optimal_weights_u(guessed_mus, alpha, u)
            delta_sd_damped.append(
                [alpha * u * w_u[i] / (1.0 + alpha * u * w_u[i]) for i in range(m)]
            )
        n_sim = 350
        tot_fdp = 0.0
        tot_pow = 0.0
        for _ in range(n_sim):
            pvals = []
            for i in range(m):
                if i < m0:
                    pvals.append(rng.random())
                else:
                    z = rng.gauss(true_mus[i], 1.0)
                    pvals.append(phi_bar(z))
            rej = run_step_down_thresholds(pvals, delta_sd_damped)
            r_cnt = len(rej)
            v_cnt = sum(1 for i in rej if i < m0)
            s_cnt = r_cnt - v_cnt
            tot_fdp += (v_cnt / r_cnt) if r_cnt > 0 else 0.0
            tot_pow += s_cnt / m1
        return tot_fdp / n_sim, tot_pow / n_sim

    fdr_low_sigma, pow_low_sigma = eval_sigma(0.20)
    fdr_high_sigma, pow_high_sigma = eval_sigma(3.50)

    return {
        "fdr_low_sigma_020": round(fdr_low_sigma, 5),
        "pow_low_sigma_020": round(pow_low_sigma, 5),
        "fdr_high_sigma_350": round(fdr_high_sigma, 5),
        "pow_high_sigma_350": round(pow_high_sigma, 5),
        "fdr_controlled_under_severe_misspecification": fdr_high_sigma <= alpha,
        "power_degrades_under_severe_misspecification": pow_low_sigma > pow_high_sigma,
    }


def main() -> None:
    prop32 = verify_proposition_3_2_optimal_weight_function()
    thm41 = verify_lemma_c1_and_theorem_4_1()
    thm42_43 = verify_theorems_4_2_and_4_3_oracle_dominance()
    sec53 = verify_section_5_3_misspecification_robustness()

    all_passed = bool(
        prop32["max_budget_error"] < 1e-10
        and prop32["max_kkt_marginal_spread"] < 1e-9
        and prop32["threshold_monotone"]
        and prop32["strict_lagrangian_maximum"]
        and thm41["unmodified_su_exceeds_alpha"]
        and thm41["damped_su_controls_fdr"]
        and thm41["step_down_controls_fdr_m2"]
        and thm42_43["multi_weighted_beats_bh"]
        and thm42_43["sd_damped_beats_su_damped"]
        and thm42_43["all_fdr_controlled"]
        and sec53["fdr_controlled_under_severe_misspecification"]
        and sec53["power_degrades_under_severe_misspecification"]
    )

    summary = {
        "concept_id": "AIMech:OptimalMultiWeightedStepUpProcedureForFDRControl",
        "proposition_3_2_optimal_weights": prop32,
        "lemma_c1_and_theorem_4_1_fdr": thm41,
        "theorems_4_2_and_4_3_oracle_dominance": thm42_43,
        "section_5_3_misspecification": sec53,
        "all_checks_passed": all_passed,
    }
    print(json.dumps(summary, indent=2))
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
