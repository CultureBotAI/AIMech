#!/usr/bin/env python3
"""Constructed boundary & regime verification for Round 224.

Concept: AIMech:GloballyConvergentRegularizationHomotopyAndNystromNewtonForGeneralizedSelfConcordantLosses
Primary source: Ulysse Marteau-Ferey, Francis Bach, & Alessandro Rudi (2019),
"Globally Convergent Newton Methods for Ill-conditioned Generalized
Self-concordant Losses", Advances in Neural Information Processing Systems 32
(NeurIPS 2019), arXiv:1907.01771v2.
"""

from __future__ import annotations

import json
import math


def dot(u: list[float], v: list[float]) -> float:
    return sum(ui * vi for ui, vi in zip(u, v))


def norm2(u: list[float]) -> float:
    return math.sqrt(dot(u, u))


def mat_vec(a: list[list[float]], v: list[float]) -> list[float]:
    return [dot(row, v) for row in a]


def mat_add_diag(a: list[list[float]], lam: float) -> list[list[float]]:
    d = len(a)
    return [
        [a[i][j] + (lam if i == j else 0.0) for j in range(d)]
        for i in range(d)
    ]


def solve_spd(a: list[list[float]], b: list[float]) -> list[float]:
    """Solve A x = b via Cholesky decomposition A = L L^T."""
    d = len(a)
    l_mat = [[0.0] * d for _ in range(d)]
    for i in range(d):
        for j in range(i + 1):
            s = sum(l_mat[i][k] * l_mat[j][k] for k in range(j))
            if i == j:
                l_mat[i][j] = math.sqrt(max(a[i][i] - s, 1e-18))
            else:
                l_mat[i][j] = (a[i][j] - s) / l_mat[j][j]
    # Forward substitution L y = b
    y = [0.0] * d
    for i in range(d):
        y[i] = (b[i] - sum(l_mat[i][k] * y[k] for k in range(i))) / l_mat[i][i]
    # Backward substitution L^T x = y
    x = [0.0] * d
    for i in range(d - 1, -1, -1):
        x[i] = (
            y[i] - sum(l_mat[k][i] * x[k] for k in range(i + 1, d))
        ) / l_mat[i][i]
    return x


def psi(t: float) -> float:
    if abs(t) < 1e-8:
        return 0.5 + t / 6.0 + t * t / 24.0
    return (math.exp(t) - t - 1.0) / (t * t)


def phi_under(t: float) -> float:
    if abs(t) < 1e-8:
        return 1.0 - 0.5 * t + t * t / 6.0
    return (1.0 - math.exp(-t)) / t


def phi_over(t: float) -> float:
    if abs(t) < 1e-8:
        return 1.0 + 0.5 * t + t * t / 6.0
    return (math.exp(t) - 1.0) / t


class LogisticGSCProblem:
    """Regularized logistic regression f_mu(x) = f(x) + (mu/2)||x||^2."""

    def __init__(self) -> None:
        self.w = [
            [1.2, -0.4, 0.3],
            [0.9, 0.7, -0.2],
            [-1.1, 0.5, 0.6],
            [0.8, -0.9, 0.4],
            [-0.6, -0.8, -0.5],
            [1.0, 0.3, -0.7],
        ]
        self.y = [1.0, 1.0, -1.0, 1.0, -1.0, -1.0]
        self.n = len(self.w)
        self.d = 3
        self.r_gsc = max(norm2(wi) for wi in self.w)

    def f_val(self, x: list[float], mu: float) -> float:
        acc = 0.0
        for wi, yi in zip(self.w, self.y):
            z = -yi * dot(wi, x)
            if z > 20.0:
                acc += z + math.log1p(math.exp(-z))
            else:
                acc += math.log1p(math.exp(z))
        return acc / self.n + 0.5 * mu * dot(x, x)

    def grad(self, x: list[float], mu: float) -> list[float]:
        g = [mu * xj for xj in x]
        for wi, yi in zip(self.w, self.y):
            z = yi * dot(wi, x)
            sig = 1.0 / (1.0 + math.exp(z))
            coef = -yi * sig / self.n
            for j in range(self.d):
                g[j] += coef * wi[j]
        return g

    def hess(self, x: list[float], mu: float) -> list[list[float]]:
        h = [[mu if i == j else 0.0 for j in range(self.d)] for i in range(self.d)]
        for wi, yi in zip(self.w, self.y):
            z = yi * dot(wi, x)
            ez = math.exp(-abs(z))
            sec = ez / ((1.0 + ez) ** 2) / self.n
            for i in range(self.d):
                for j in range(self.d):
                    h[i][j] += sec * wi[i] * wi[j]
        return h

    def newton_step_and_decrement(
        self, x: list[float], mu: float
    ) -> tuple[list[float], float]:
        g = self.grad(x, mu)
        h = self.hess(x, mu)
        delta = solve_spd(h, g)
        nu = math.sqrt(max(dot(g, delta), 0.0))
        return delta, nu

    def approx_newton_step(
        self, x: list[float], mu: float, rho: float
    ) -> tuple[list[float], float]:
        """Construct a deterministic rho-relative approximate Newton step."""
        delta, nu = self.newton_step_and_decrement(x, mu)
        # Scale by (1 - rho) so ||tilde_delta - delta||_{H_mu(x)} = rho * nu
        tilde_delta = [(1.0 - rho) * dj for dj in delta]
        return tilde_delta, nu

    def exact_minimizer(self, mu: float) -> list[float]:
        g0 = self.grad([0.0] * self.d, 0.0)
        cur_mu = max(mu, 7.0 * self.r_gsc * norm2(g0))
        x = [0.0] * self.d
        while cur_mu > mu:
            for _ in range(2):
                delta, _ = self.newton_step_and_decrement(x, cur_mu)
                x = [xj - dj for xj, dj in zip(x, delta)]
            q = (1.0 / 3.0 + 7.0 * self.r_gsc * norm2(x)) / (
                1.0 + 7.0 * self.r_gsc * norm2(x)
            )
            cur_mu = max(mu, q * cur_mu)
        for _ in range(20):
            delta, nu = self.newton_step_and_decrement(x, mu)
            x = [xj - dj for xj, dj in zip(x, delta)]
            if nu < 1e-15:
                break
        return x


def check_1_gsc_dikin_and_regimes() -> dict[str, object]:
    """Verify Appendix A.1 Eqs. (13)-(22), Lemma 6, Lemma 10, and Proposition 5."""
    max_phi_ratio_err = 0.0
    for t in [0.05, 0.2, 0.5, 1.0, 2.0]:
        err = abs(phi_over(t) / phi_under(t) - math.exp(t))
        max_phi_ratio_err = max(max_phi_ratio_err, err)

    prob = LogisticGSCProblem()
    lam = 0.05
    x_star = prob.exact_minimizer(lam)
    f_star = prob.f_val(x_star, lam)

    # Pick x0 inside D_lam(1/7), i.e., nu_lam(x0) <= (1/7)*sqrt(lam)/R
    x0 = [x_star[0] + 0.04, x_star[1] - 0.03, x_star[2] + 0.02]
    _, nu0 = prob.newton_step_and_decrement(x0, lam)
    renorm_nu0 = prob.r_gsc * nu0 / math.sqrt(lam)
    f0_diff = prob.f_val(x0, lam) - f_star
    lemma6_holds = (0.25 * nu0 * nu0 <= f0_diff + 1e-15) and (
        f0_diff <= nu0 * nu0 + 1e-15
    )

    # Exact Newton quadratic convergence (Lemma 10): nu_lam(x_t) <= 2^{-(2^t - 1)} nu_lam(x0)
    x_nm = list(x0)
    quad_holds = True
    for t in range(1, 4):
        delta, _ = prob.newton_step_and_decrement(x_nm, lam)
        x_nm = [xj - dj for xj, dj in zip(x_nm, delta)]
        _, nu_t = prob.newton_step_and_decrement(x_nm, lam)
        bound_t = (2.0 ** (-(2**t - 1))) * nu0
        if nu_t > bound_t + 1e-15:
            quad_holds = False

    # Relative Approximate Newton linear convergence (Proposition 5, rho = 1/7)
    rho = 1.0 / 7.0
    x_anm = list(x0)
    lin_holds = True
    for t in range(1, 6):
        tilde_delta, _ = prob.approx_newton_step(x_anm, lam, rho)
        x_anm = [xj - dj for xj, dj in zip(x_anm, tilde_delta)]
        _, nu_t = prob.newton_step_and_decrement(x_anm, lam)
        bound_t = (2.0 ** (-t)) * nu0
        if nu_t > bound_t + 1e-15:
            lin_holds = False

    passed = (
        max_phi_ratio_err < 1e-14
        and renorm_nu0 <= 1.0 / 7.0
        and lemma6_holds
        and quad_holds
        and lin_holds
    )
    return {
        "passed": passed,
        "max_phi_ratio_err": round(max_phi_ratio_err, 16),
        "initial_renorm_decrement": round(renorm_nu0, 6),
        "dikin_threshold_1_over_7": round(1.0 / 7.0, 6),
        "lemma6_function_equivalence_holds": lemma6_holds,
        "exact_newton_quadratic_convergence_holds": quad_holds,
        "relative_anm_linear_convergence_holds": lin_holds,
    }


def check_2_homotopy_globalization_scheme() -> dict[str, object]:
    """Verify Lemma 3/13, Proposition 6, and Theorem 1 two-phase globalization."""
    prob = LogisticGSCProblem()
    lam = 1e-4
    eps = 1e-8
    rho = 1.0 / 7.0

    x_star = prob.exact_minimizer(lam)
    f_star = prob.f_val(x_star, lam)

    # Direct initialization at x0 = 0 for small lam = 1e-4 violates D_lam(1/7)
    _, nu_direct0 = prob.newton_step_and_decrement([0.0, 0.0, 0.0], lam)
    direct_renorm_nu0 = prob.r_gsc * nu_direct0 / math.sqrt(lam)

    # Theorem 1 initialization: x0 = 0, mu0 = 7 * R * ||nabla f(0)||
    g0 = prob.grad([0.0, 0.0, 0.0], 0.0)
    mu0 = 7.0 * prob.r_gsc * norm2(g0)
    x_k = [0.0, 0.0, 0.0]
    mu_k = mu0

    _, nu_init = prob.newton_step_and_decrement(x_k, mu_k)
    max_renorm_decrement = prob.r_gsc * nu_init / math.sqrt(mu_k)
    dikin_inclusion_holds = max_renorm_decrement <= 1.0 / 7.0 + 1e-12

    k_stages = 0
    while True:
        # Perform t = 2 steps of rho-relative ANM on f_{mu_k}
        for _ in range(2):
            tilde_delta, _ = prob.approx_newton_step(x_k, mu_k, rho)
            x_k = [xj - dj for xj, dj in zip(x_k, tilde_delta)]
        _, nu_after_anm = prob.newton_step_and_decrement(x_k, mu_k)
        # Check contraction into D_{mu_k}((1/7)/3)
        if prob.r_gsc * nu_after_anm / math.sqrt(mu_k) > (1.0 / 21.0) + 1e-12:
            dikin_inclusion_holds = False

        q_next = (1.0 / 3.0 + 7.0 * prob.r_gsc * norm2(x_k)) / (
            1.0 + 7.0 * prob.r_gsc * norm2(x_k)
        )
        mu_next = q_next * mu_k
        if mu_next < lam:
            x_last = list(x_k)
            break
        mu_k = mu_next
        k_stages += 1
        _, nu_new_mu = prob.newton_step_and_decrement(x_k, mu_k)
        renorm_new = prob.r_gsc * nu_new_mu / math.sqrt(mu_k)
        max_renorm_decrement = max(max_renorm_decrement, renorm_new)
        if renorm_new > (1.0 / 7.0) + 1e-12:
            dikin_inclusion_holds = False

    # Verify R * nu_lam(x_last) / sqrt(lam) <= 1/7 at end of Phase I (Proposition 6.3)
    _, nu_lam_last = prob.newton_step_and_decrement(x_last, lam)
    phase1_final_renorm = prob.r_gsc * nu_lam_last / math.sqrt(lam)
    if phase1_final_renorm > (1.0 / 7.0) + 1e-12:
        dikin_inclusion_holds = False

    k_bound = math.floor(
        (3.0 + 11.0 * prob.r_gsc * norm2(x_star)) * math.log(mu0 / lam)
    )

    # Phase II: T = ceil(log2(sqrt(max(1, lam * eps^{-1} / R^2)))) steps of ANM on f_lam
    t_phase2 = math.ceil(
        math.log2(math.sqrt(max(1.0, (lam / eps) / (prob.r_gsc**2))))
    )
    x_hat = list(x_last)
    for _ in range(t_phase2):
        tilde_delta, _ = prob.approx_newton_step(x_hat, lam, rho)
        x_hat = [xj - dj for xj, dj in zip(x_hat, tilde_delta)]

    final_suboptimality = max(0.0, prob.f_val(x_hat, lam) - f_star)
    passed = (
        direct_renorm_nu0 > 5.0
        and dikin_inclusion_holds
        and k_stages <= k_bound
        and final_suboptimality <= eps
    )
    return {
        "passed": passed,
        "direct_init_renorm_decrement_at_lam": round(direct_renorm_nu0, 4),
        "max_renorm_decrement_along_homotopy": round(max_renorm_decrement, 6),
        "phase1_final_renorm_decrement_at_lam": round(phase1_final_renorm, 6),
        "dikin_threshold_1_over_7": round(1.0 / 7.0, 6),
        "phase1_stages_K": k_stages,
        "theorem1_stage_bound": k_bound,
        "phase2_steps_T": t_phase2,
        "final_suboptimality": float(f"{final_suboptimality:.3e}"),
        "target_eps": eps,
    }


def check_3_pcg_and_nystrom_projection() -> dict[str, object]:
    """Verify Appendix D.5.1 Eq. (34) PCG 3-step bound and Appendix G.2 Prop. 15."""
    # Construct diagonal SPD matrix A and preconditioner A_tilde satisfying (1/2) A_tilde <= A <= (3/2) A_tilde
    a_tilde_diag = [100.0, 10.0, 1.0, 0.01, 1e-4]
    ratios = [0.52, 0.75, 1.0, 1.25, 1.48]  # all in [1/2, 3/2]
    a_diag = [rt * at for rt, at in zip(ratios, a_tilde_diag)]
    b_vec = [1.5, -0.8, 2.1, -1.2, 0.7]

    # Exact solution z^* = A^{-1} b
    x_star = [bi / ai for bi, ai in zip(b_vec, a_diag)]

    def a_norm(v: list[float]) -> float:
        return math.sqrt(sum(ai * (vi**2) for ai, vi in zip(a_diag, v)))

    # Preconditioned CG with B = diag(sqrt(a_tilde_diag))
    b_inv = [1.0 / math.sqrt(at) for at in a_tilde_diag]
    # Preconditioned operator M = B^{-T} A B^{-1} = diag(ratios), rhs r0 = B^{-T} b
    r = [bi * bi_inv for bi, bi_inv in zip(b_vec, b_inv)]
    p = list(r)
    s0 = dot(r, r)
    z = [0.0] * len(b_vec)

    for _ in range(3):  # tau = 3 iterations
        az = [rt * pj for rt, pj in zip(ratios, p)]
        alpha = s0 / dot(p, az)
        z = [zj + alpha * pj for zj, pj in zip(z, p)]
        r = [rj - alpha * azj for rj, azj in zip(r, az)]
        s1 = dot(r, r)
        if s1 < 1e-30:
            break
        p = [rj + (s1 / s0) * pj for rj, pj in zip(r, p)]
        s0 = s1

    x_tau = [bi_inv * zj for bi_inv, zj in zip(b_inv, z)]
    diff = [xt - xs for xt, xs in zip(x_tau, x_star)]
    rel_err = a_norm(diff) / a_norm(x_star)
    theo_bound = 2.0 * (((math.sqrt(3.0) - 1.0) / (math.sqrt(3.0) + 1.0)) ** 3)

    # Verify Proposition 15 (Appendix G.2, p. 55):
    # Project 3D logistic problem onto first 2 coordinates P = diag(1, 1, 0) where 3rd coordinate has tiny weight
    prob = LogisticGSCProblem()
    for i in range(prob.n):
        prob.w[i][2] *= 0.01
    prob.r_gsc = max(norm2(wi) for wi in prob.w)
    lam = 2.0
    x_star_full = prob.exact_minimizer(lam)
    h_full = prob.hess(x_star_full, lam)
    h_unreg = prob.hess(x_star_full, 0.0)
    # Since I - P selects coordinate 2, ||H(x)^{1/2}(I - P)||^2 = H_{2,2}(x)
    c_p = h_unreg[2][2] / lam

    # Source term s_lam = ||nabla f(x_lam^*)||_{H_lam^{-1}(x_lam^*)}
    g_unreg_star = prob.grad(x_star_full, 0.0)
    s_lam_vec = solve_spd(h_full, g_unreg_star)
    s_lam = math.sqrt(dot(g_unreg_star, s_lam_vec))
    r_lam_star = math.sqrt(lam) / prob.r_gsc


    # Solve projected problem in H_P (coordinate 2 fixed to 0)
    x_proj = [x_star_full[0], x_star_full[1], 0.0]
    g_proj_full = prob.grad(x_proj, lam)
    g_p = [g_proj_full[0], g_proj_full[1], 0.0]
    h_proj_full = prob.hess(x_proj, 0.0)
    h_p_lam = [
        [h_proj_full[0][0] + lam, h_proj_full[0][1], 0.0],
        [h_proj_full[1][0], h_proj_full[1][1] + lam, 0.0],
        [0.0, 0.0, lam],
    ]
    delta_p = solve_spd(h_p_lam, g_p)
    nu_p_lam = math.sqrt(dot(g_p, delta_p))
    _, nu_full_at_proj = prob.newton_step_and_decrement(x_proj, lam)

    prop15_bound = 3.0 * (nu_p_lam + s_lam)
    prop15_holds = (
        c_p <= 1.0 / 120.0
        and (s_lam / r_lam_star) <= 0.25
        and nu_full_at_proj <= prop15_bound + 1e-15
    )

    passed = (
        rel_err <= theo_bound + 1e-15
        and theo_bound <= 1.0 / 7.0
        and prop15_holds
    )
    return {
        "passed": passed,
        "pcg_tau3_relative_error": round(rel_err, 6),
        "pcg_tau3_theoretical_bound": round(theo_bound, 6),
        "target_rho_1_over_7": round(1.0 / 7.0, 6),
        "projector_capacity_C_P": round(c_p, 6),
        "nu_full_at_projected_point": round(nu_full_at_proj, 6),
        "prop15_upper_bound_3_nuP_plus_s": round(prop15_bound, 6),
    }


def main() -> int:
    c1 = check_1_gsc_dikin_and_regimes()
    c2 = check_2_homotopy_globalization_scheme()
    c3 = check_3_pcg_and_nystrom_projection()
    all_passed = bool(c1["passed"] and c2["passed"] and c3["passed"])
    summary = {
        "concept_id": "AIMech:GloballyConvergentRegularizationHomotopyAndNystromNewtonForGeneralizedSelfConcordantLosses",
        "all_passed": all_passed,
        "check_1_gsc_dikin_and_regimes": c1,
        "check_2_homotopy_globalization_scheme": c2,
        "check_3_pcg_and_nystrom_projection": c3,
    }
    print(json.dumps(summary, indent=2))
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
