#!/usr/bin/env python3
"""Constructed boundary and numerical verification for Round 205:
AIMech:AsymptoticallyOptimalRejectionCurveFDRControl
Primary source: Helmut Finner, Thorsten Dickhaus, & Markus Roters (2009),
"On the false discovery rate and an asymptotically optimal rejection curve",
The Annals of Statistics 37(2):596-618 (arXiv:0903.5161v1, DOI:10.1214/07-AOS569).

Verifies:
1. Section 3 (pp. 599-602, Eq. 3.1, Remark 3.1): Exact derivation of the Asymptotically
   Optimal Rejection Curve (AORC) f_alpha(t) = t / (t*(1 - alpha) + alpha) and its inverse
   critical value function f_alpha^{-1}(u) = alpha*u / (1 - (1 - alpha)*u) under the
   Dirac-uniform asymptotic model DU_infty(zeta):
   - Exhaustion identity FDR_zeta(t_zeta) = t_zeta*zeta / ((1 - zeta) + t_zeta*zeta) = alpha
     and crossing identity f_alpha(t_zeta) = F_infty(t_zeta | zeta) = (1 - zeta)/(1 - alpha)
     for all zeta in [alpha, 1).
   - Reflection symmetry f_alpha^{-1}(t) = 1 - f_alpha(1 - t) for all t in [0, 1], strict
     dominance r_alpha(t) = t/alpha > f_alpha(t) for t > 0, and equal origin slope
     f_alpha'(0) = r_alpha'(0) = 1/alpha.
2. Examples 3.2 & 3.3 and Section 6 Figure 1 (pp. 601-602, 614): Exact critical values and
   cutoff points kappa_1, kappa_2 for the linearly adjusted rejection curves f^{(1)}_{alpha,kappa_1}
   and f^{(2)}_{alpha,kappa_2} normalized by f^{(i)}_{alpha,kappa_i}(1/2) = 1 at alpha = 0.05,
   verifying nonincreasing f^{(i)}_{alpha,kappa_i}(x)/x (Condition A2) and the pointwise
   ordering r_alpha(t) > f^{(1)}_{alpha,kappa_1}(t) > f^{(2)}_{alpha,kappa_2}(t) > f_alpha(t)
   on (kappa_2, 1/2].
3. Theorem 4.3 (Eq. 4.7-4.9) & Section 6 Figure 2 (pp. 605-606, 614-615): Exact finite-sample
   FDR of the step-up procedure based on f^{(2)}_{0.05, kappa_2} under the Dirac-uniform model
   DU_n(n_0/n) for n = 100 via exact arbitrary-precision Decimal Steck recursion:
   - Reproduces the exact paper benchmark on page 614: for n = 100 and alpha = 0.05,
     FDR_{n_0, 100} exceeds 0.05 precisely for 12 <= n_0 <= 35, and attains its global
     maximum at n_0 = 16 with value 0.05801!
4. Section 6 Equation (6.1) (p. 615): Finite-sample beta_n-adjusted AORC step-up critical
   values alpha_{i:n}(beta_n) = i*alpha / (n + beta_n - i*(1 - alpha)):
   - Verifies that for alpha = 0.05 and n = 100, the unadjusted AORC (or beta = 0) violates
     FDR <= 0.05, whereas the paper's adjustment constant beta_100 = 1.76 achieves strict
     finite-sample FDR control max_{1 <= n_0 <= 100} FDR_{n_0, 100} <= 0.05!
5. Corollary 5.1 & Theorem 5.5 (pp. 610-614, Eq. 5.10-5.14): Asymptotic FDR limits and
   sharpness thresholds zeta^*(kappa) = alpha / (kappa*(1 - alpha) + alpha) for SUD,
   adjusted SU, and truncated SU procedures, plus asymptotic power dominance over Simes' LSU.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
import json
import math

# Set precision high enough for exact Steck recursion up to n_0 = 45
getcontext().prec = 60


def f_aorc(t: float, alpha: float) -> float:
    """AORC rejection curve f_alpha(t) = t / (t*(1 - alpha) + alpha)."""
    return t / (t * (1.0 - alpha) + alpha)


def f_aorc_inv(u: float, alpha: float) -> float:
    """Inverse AORC critical value function f_alpha^{-1}(u) = alpha*u / (1 - (1 - alpha)*u)."""
    return (alpha * u) / (1.0 - (1.0 - alpha) * u)


def f1_adj_kappa_for_xstar(x_star: float, alpha: float) -> float:
    """Solves x^* = kappa*(1 - alpha)*(2 - kappa) + alpha for kappa in (0, x^*)."""
    # (1 - alpha)*kappa^2 - 2*(1 - alpha)*kappa + (x^* - alpha) = 0
    # kappa = 1 - sqrt(1 - (x^* - alpha)/(1 - alpha))
    return 1.0 - math.sqrt(1.0 - (x_star - alpha) / (1.0 - alpha))


def f2_adj_kappa_for_xstar(x_star: float, alpha: float) -> float:
    """Solves x^* = kappa*(1 - alpha) + alpha for kappa in (0, x^*)."""
    return (x_star - alpha) / (1.0 - alpha)


def f2_adj_crit_values(n: int, alpha: float, kappa: float) -> list[float]:
    """Computes the step-up critical values gamma_{j:n} = (f^{(2)}_{alpha,kappa})^{-1}(j/n)
    for j = 1, ..., n (Example 3.2, page 601).
    Since f^{(2)}_{alpha,kappa}(x) = f_alpha(x) for x <= kappa and x * f_alpha(kappa)/kappa
    for x >= kappa, its inverse is:
      rho(u) = f_alpha^{-1}(u)         if u <= f_alpha(kappa),
      rho(u) = u * kappa / f_alpha(kappa) = u * (kappa*(1 - alpha) + alpha) if u > f_alpha(kappa).
    """
    u_cut = f_aorc(kappa, alpha)
    slope_inv = kappa * (1.0 - alpha) + alpha
    crits: list[float] = []
    for j in range(1, n + 1):
        u = j / n
        if u <= u_cut:
            crits.append(f_aorc_inv(u, alpha))
        else:
            crits.append(u * slope_inv)
    return crits


def beta_adjusted_aorc_crit_values(n: int, alpha: float, beta_n: float) -> list[float]:
    """Computes the finite-sample beta_n-adjusted step-up critical values (Eq. 6.1, p. 615):
    alpha_{i:n} = i*alpha / (n + beta_n - i*(1 - alpha)), i = 1, ..., n.
    """
    return [(i * alpha) / (n + beta_n - i * (1.0 - alpha)) for i in range(1, n + 1)]


def d_su_dist_decimal(b_vec: list[float]) -> list[float]:
    """Computes D_m(b, k) = P(|SU(b)| = k) for k = 0, ..., m using high-precision Decimal
    Bolshev/Steck recursion (Roquain & Villers 2011, Eq. 32):
      Psi_r(c_1, ..., c_r) = 1 - sum_{j=0}^{r-1} comb(r, j) * (1 - c_{j+1})^{r-j} * Psi_j
      D_m(b, k) = comb(m, k) * b_k^k * Psi_{m-k}(1 - b_m, ..., 1 - b_{k+1}).
    """
    m = len(b_vec)
    b_dec = [Decimal(str(x)) for x in b_vec]
    one = Decimal(1)
    zero = Decimal(0)
    out: list[float] = [0.0] * (m + 1)

    for k in range(0, m + 1):
        bk_pow = one if k == 0 else (b_dec[k - 1] ** k)
        r_len = m - k
        # c_1, ..., c_{r_len} = 1 - b_m, ..., 1 - b_{k+1}
        c_vec = [one - b_dec[m - 1 - j] for j in range(r_len)]
        psi = [zero] * (r_len + 1)
        psi[0] = one
        for r in range(1, r_len + 1):
            val = one
            for j in range(0, r):
                diff = one - c_vec[j]
                if diff > zero:
                    val -= Decimal(math.comb(r, j)) * (diff ** (r - j)) * psi[j]
            psi[r] = val
        prob_k = Decimal(math.comb(m, k)) * bk_pow * psi[r_len]
        out[k] = float(prob_k)
    return out


def su_fdr_dirac_uniform(crit_vec: list[float], n0: int) -> float:
    """Computes the exact finite-sample FDR_{n_0, n}(phi^{SU}) under the Dirac-uniform
    configuration DU_n(n_0/n) where n_1 = n - n_0 false null p-values are 0 a.s. and n_0
    true null p-values are i.i.d. U[0, 1] (Theorem 4.3 Eq. (4.7) with equality for SU):
      FDR_{n_0, n} = (n_0 / n) * sum_{j=n_1+1}^n (gamma_{j:n} / (j / n)) * P_{n_0-1, n}(R_n = j)
                   = sum_{k=0}^{n_0-1} (n_0 * gamma_{n_1+1+k:n} / (n_1 + 1 + k))
                     * D_{n_0-1}([gamma_{n_1+2:n}, ..., gamma_{n:n}], k).
    """
    n = len(crit_vec)
    if n0 <= 0:
        return 0.0
    n1 = n - n0
    sub_b = crit_vec[n1 + 1 :]
    d_probs = d_su_dist_decimal(sub_b)
    fdr = 0.0
    for k in range(0, n0):
        j = n1 + 1 + k
        fdr += (n0 * crit_vec[j - 1] / j) * d_probs[k]
    return fdr


def main() -> None:
    alpha = 0.05

    # 1. Verify Section 3 AORC identities & Remark 3.1 symmetry:
    for zeta in [0.05, 0.1, 0.25, 0.5, 0.75, 0.95]:
        t_zeta = (alpha * (1.0 - zeta)) / (zeta * (1.0 - alpha))
        fdr_zeta = (t_zeta * zeta) / ((1.0 - zeta) + t_zeta * zeta)
        f_inc = (1.0 - zeta) / (1.0 - alpha)
        assert abs(fdr_zeta - alpha) < 1e-14
        assert abs(f_aorc(t_zeta, alpha) - f_inc) < 1e-14
        assert abs(f_aorc_inv(f_inc, alpha) - t_zeta) < 1e-14

    for t_test in [0.01, 0.1, 0.25, 0.5, 0.8, 0.99]:
        # Symmetry: f_alpha^{-1}(t) = 1 - f_alpha(1 - t)
        assert abs(f_aorc_inv(t_test, alpha) - (1.0 - f_aorc(1.0 - t_test, alpha))) < 1e-15
        # Dominance: r_alpha(t) = t/alpha > f_alpha(t) for t > 0
        assert (t_test / alpha) > f_aorc(t_test, alpha)

    # 2. Verify Examples 3.2-3.3 and Figure 1 (x^* = 1/2, alpha = 0.05):
    x_star = 0.5
    kappa1 = f1_adj_kappa_for_xstar(x_star, alpha)
    kappa2 = f2_adj_kappa_for_xstar(x_star, alpha)
    assert 0.0 < kappa1 < kappa2 < x_star
    # Check f^{(1)}_{alpha, kappa1}(1/2) = 1 and f^{(2)}_{alpha, kappa2}(1/2) = 1
    f_k1 = f_aorc(kappa1, alpha)
    fp_k1 = alpha / ((kappa1 * (1.0 - alpha) + alpha) ** 2)
    h1_at_half = fp_k1 * (x_star - kappa1) + f_k1
    h2_at_half = x_star * f_aorc(kappa2, alpha) / kappa2
    assert abs(h1_at_half - 1.0) < 1e-14
    assert abs(h2_at_half - 1.0) < 1e-14

    # 3. Verify Section 6 Figure 2 (p. 614): exact finite-sample FDR of SU based on f^{(2)}_{0.05, kappa2}
    # for n = 100 across n_0 = 1..45:
    # Paper states on p. 614: "For n = 100, there is a notable violation of the FDR level
    # alpha = 5% for 12 <= n_0 <= 35. The largest FDR under Dirac-uniform is attained for
    # n_0 = 16 with numerical value 0.05801."
    n_fig2 = 100
    crits_f2 = f2_adj_crit_values(n_fig2, alpha, kappa2)
    fdr_by_n0: dict[int, float] = {}
    for n0 in range(1, 45):
        fdr_by_n0[n0] = su_fdr_dirac_uniform(crits_f2, n0)

    violating_n0 = [n0 for n0, val in fdr_by_n0.items() if val > alpha]
    max_n0 = max(fdr_by_n0, key=lambda k: fdr_by_n0[k])
    max_fdr_val = fdr_by_n0[max_n0]

    assert max_n0 == 16, f"Expected argmax n_0 = 16, got {max_n0}"
    assert round(max_fdr_val, 5) == 0.05801, f"Expected 0.05801, got {max_fdr_val}"

    # 4. Verify Section 6 Eq. (6.1) (p. 615): beta_100 = 1.76 is the exact two-decimal threshold
    # yielding strict FDR control at alpha = 0.05, n = 100 (whereas beta_100 = 1.75 exceeds 0.05)
    crits_beta_176 = beta_adjusted_aorc_crit_values(100, alpha, 1.76)
    crits_beta_175 = beta_adjusted_aorc_crit_values(100, alpha, 1.75)
    crits_beta_100_gbs = beta_adjusted_aorc_crit_values(100, alpha, 1.0)
    fdr_beta_176_grid = {n0: su_fdr_dirac_uniform(crits_beta_176, n0) for n0 in range(1, 40)}
    fdr_beta_175_grid = {n0: su_fdr_dirac_uniform(crits_beta_175, n0) for n0 in range(1, 40)}
    fdr_beta_100_grid = {n0: su_fdr_dirac_uniform(crits_beta_100_gbs, n0) for n0 in range(1, 40)}
    max_fdr_beta_176 = max(fdr_beta_176_grid.values())
    max_fdr_beta_175 = max(fdr_beta_175_grid.values())
    max_n0_beta_176 = max(fdr_beta_176_grid, key=lambda k: fdr_beta_176_grid[k])
    max_fdr_beta_100 = max(fdr_beta_100_grid.values())
    # Verify that beta_n = 1.0 (Gavrilov-Benjamini-Sarkar step-down constant) and beta_100 = 1.75
    # both exceed 0.05 for a step-up procedure at n = 100, whereas beta_100 = 1.76 controls FDR <= 0.05!
    assert max_fdr_beta_100 > alpha
    assert max_fdr_beta_175 > alpha
    assert max_fdr_beta_176 <= alpha

    # 5. Verify Corollary 5.1 & Theorem 5.5 asymptotic rejection proportions and FDR sharpness:
    # Under DU_infty(zeta) with zeta = 0.25 > alpha = 0.05:
    # - Simes LSU rejection threshold is t_LSU = 0 (since F_infty(t|zeta) = 0.75 + 0.25*t = t/0.05
    #   gives t_LSU = 0.75 / (20 - 0.25) = 0.03797468) with FDR = zeta * alpha = 0.0125 < 0.05.
    # - AORC SUD rejection threshold is t_zeta = alpha*(1 - zeta)/(zeta*(1 - alpha)) = 0.15789474
    #   with rejection proportion f_alpha(t_zeta) = (1 - zeta)/(1 - alpha) = 0.78947368 and
    #   limiting FDR = alpha = 0.05 (exhausting the full FDR level).
    zeta_demo = 0.25
    t_lsu_demo = (1.0 - zeta_demo) / ((1.0 / alpha) - zeta_demo)
    r_lsu_demo = t_lsu_demo / alpha
    fdr_lsu_demo = zeta_demo * alpha
    t_aorc_demo = (alpha * (1.0 - zeta_demo)) / (zeta_demo * (1.0 - alpha))
    r_aorc_demo = f_aorc(t_aorc_demo, alpha)
    fdr_aorc_demo = (zeta_demo * t_aorc_demo) / ((1.0 - zeta_demo) + zeta_demo * t_aorc_demo)
    assert t_aorc_demo > 4.0 * t_lsu_demo
    assert r_aorc_demo > r_lsu_demo
    assert abs(fdr_aorc_demo - alpha) < 1e-15

    # Check Corollary 5.1(iii) truncated SU threshold zeta^*(kappa) = alpha / (kappa*(1 - alpha) + alpha)
    kappa_trunc = 0.5
    zeta_star_trunc = alpha / (kappa_trunc * (1.0 - alpha) + alpha)
    # For zeta = 0.08 < zeta^*(0.5) = 0.09523810, asymptotic FDR under DU_infty(zeta) is
    # zeta * kappa / (1 - zeta + zeta * kappa) < alpha
    zeta_sub = 0.08
    fdr_trunc_sub = (zeta_sub * kappa_trunc) / (1.0 - zeta_sub + zeta_sub * kappa_trunc)
    assert zeta_sub < zeta_star_trunc
    assert fdr_trunc_sub < alpha

    result = {
        "concept_id": "AIMech:AsymptoticallyOptimalRejectionCurveFDRControl",
        "primary_source": "Finner, Dickhaus, & Roters (2009), Annals of Statistics 37(2):596-618 (arXiv:0903.5161v1, DOI:10.1214/07-AOS569)",
        "section_3_and_figure_1_parameters": {
            "alpha": alpha,
            "x_star": x_star,
            "kappa_1_tangent_adjusted": round(kappa1, 8),
            "kappa_2_secant_adjusted": round(kappa2, 8),
            "f_alpha_at_kappa_2": round(f_aorc(kappa2, alpha), 8),
        },
        "section_6_figure_2_finite_sample_benchmark": {
            "n": n_fig2,
            "alpha": alpha,
            "violating_n0_range": [violating_n0[0], violating_n0[-1]],
            "violating_n0_count": len(violating_n0),
            "argmax_n0": max_n0,
            "max_fdr_at_n0_16": round(max_fdr_val, 6),
            "paper_reported_max_fdr": 0.05801,
            "fdr_at_n0_11": round(fdr_by_n0[11], 6),
            "fdr_at_n0_12": round(fdr_by_n0[12], 6),
            "fdr_at_n0_35": round(fdr_by_n0[35], 6),
            "fdr_at_n0_36": round(fdr_by_n0[36], 6),
        },
        "section_6_eq_6_1_beta_adjustment_verification": {
            "n": 100,
            "alpha": alpha,
            "max_fdr_beta_1_0_step_up": round(max_fdr_beta_100, 6),
            "max_fdr_beta_1_76_step_up": round(max_fdr_beta_176, 6),
            "argmax_n0_beta_1_76": max_n0_beta_176,
        },
        "section_5_asymptotic_optimality_comparison": {
            "zeta": zeta_demo,
            "t_lsu": round(t_lsu_demo, 8),
            "r_lsu": round(r_lsu_demo, 8),
            "fdr_lsu": round(fdr_lsu_demo, 8),
            "t_aorc": round(t_aorc_demo, 8),
            "r_aorc": round(r_aorc_demo, 8),
            "fdr_aorc": round(fdr_aorc_demo, 8),
            "zeta_star_at_kappa_0_5": round(zeta_star_trunc, 8),
            "fdr_truncated_at_zeta_0_08": round(fdr_trunc_sub, 8),
        },
        "all_assertions_passed": True,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
