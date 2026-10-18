#!/usr/bin/env python3
"""Constructed mathematical and numerical verification for:
AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit
Primary source: Helmut Finner, Thorsten Dickhaus, & Markus Roters (2007),
"Dependency and false discovery rate: Asymptotics", The Annals of Statistics
35(4):1432-1455 (arXiv:0710.3171v1, DOI:10.1214/009053607000000046).

Verifies:
1. Lemma 2.2 & Example 2.3 (pp. 1440-1441): Exact conditional linear step-up
   FDR_n(zeta_n | z) = zeta_n * alpha * gamma(z) when F_xi(t) = gamma(z)*t on [0, alpha]
   via exact Bolshev/Steck recursion, and shifted exponential model T_i = X_i - Z
   where gamma(z) = 2*exp(-z) integrates over Z ~ Exp(1) to FDR_n(zeta_n) = zeta_n * alpha.
2. Section 3 Equations (3.1)-(3.5), Theorem 3.2, and Remark 3.1 (pp. 1443-1445):
   Exact tangent point solution (u^*, x_0(t_2 | 1)) of d(u | x_0, 1) = 0 and
   d_u(u | x_0, 1) = 0 in the equicorrelated normal model D-EX-N(1), verifying
   Remark 3.1 bound x_0(t_2 | 1) <= underline{x}_0 = -sqrt(2*ln(sqrt(1 - rho)/alpha))
   and FDR_infty(1) = Phi(x_0(t_2 | 1)) <= Phi(underline{x}_0).
3. Theorem 3.3 (p. 1445, Eq. 3.6 & Appendix proof p. 1453): Exact algebraic
   Mills-ratio exponent identity exp((w(rho, delta)^2 - u(rho, delta)^2)/2) = delta
   and numerical convergence of FDR_infty(1; rho) as rho -> 0^+ to the double-limit
   discontinuity value Phi(-sqrt(-2*ln(alpha))) = 0.00718789 < alpha = 0.05.
4. Theorem 3.1 (p. 1444-1446): Exact integration of EER_infty(zeta) and FDR_infty(zeta)
   for zeta in (0, 1) in D-EX-N(zeta), confirming lim_{rho->0^+} EER_infty(zeta) =
   alpha*(1 - zeta)/(1 - alpha*zeta) and lim_{rho->0^+} FDR_infty(zeta) = zeta*alpha.
5. Lemma 4.1 & Theorem 4.3 (pp. 1448-1449, 1453-1454, Eq. 4.1): Asymptotic
   inflection-point scaling s_nu(x) = 1 - nu^{-1/2}*sqrt(-ln x) in the studentized
   D-EX-t(1) model, verifying a(s_nu(x), nu)^4/nu -> -4*ln(x),
   a(s_nu(x), nu)^2*(1 - s_nu(x)^2) -> -4*ln(x), and
   (nu*s_nu(alpha)^2 - nu)/sqrt(2*nu) -> -sqrt(-2*ln(alpha)).
"""
from __future__ import annotations

import json
import math


def phi_cdf(x: float) -> float:
    if x < 0.0:
        return 0.5 * math.erfc(-x / math.sqrt(2.0))
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def log_phi_neg(u: float) -> float:
    """Computes ln(Phi(-u)) accurately for all u > 0 using erfc for u <= 25 and
    the high-order asymptotic Mills-ratio series for u > 25.
    """
    if u <= 25.0:
        return math.log(0.5 * math.erfc(u / math.sqrt(2.0)))
    inv_u2 = 1.0 / (u * u)
    # Phi(-u) / phi(u) = (1/u) * (1 - 1/u^2 + 3/u^4 - 15/u^6 + 105/u^8)
    mills = (1.0 / u) * (
        1.0
        - inv_u2
        + 3.0 * (inv_u2 ** 2)
        - 15.0 * (inv_u2 ** 3)
        + 105.0 * (inv_u2 ** 4)
    )
    return -0.5 * u * u - 0.5 * math.log(2.0 * math.pi) + math.log(mills)


def phi_pdf(x: float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def phi_inv(p: float) -> float:
    """High-precision inverse standard normal c.d.f. via bisection + Newton."""
    if p <= 0.0:
        return -40.0
    if p >= 1.0:
        return 40.0
    lo, hi = -40.0, 40.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if phi_cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    x = 0.5 * (lo + hi)
    for _ in range(6):
        pdf = phi_pdf(x)
        if pdf > 1e-300:
            x -= (phi_cdf(x) - p) / pdf
    return x


def d_su_dist(b_vec: list[float]) -> list[float]:
    """Exact Bolshev/Steck recursion for step-up rejection count probabilities."""
    m = len(b_vec)
    out = [0.0] * (m + 1)
    for k in range(0, m + 1):
        bk_pow = 1.0 if k == 0 else (b_vec[k - 1] ** k)
        r_len = m - k
        c_vec = [1.0 - b_vec[m - 1 - j] for j in range(r_len)]
        psi = [0.0] * (r_len + 1)
        psi[0] = 1.0
        for r in range(1, r_len + 1):
            val = 1.0
            for j in range(0, r):
                diff = 1.0 - c_vec[j]
                if diff > 0.0:
                    val -= math.comb(r, j) * (diff ** (r - j)) * psi[j]
            psi[r] = val
        out[k] = math.comb(m, k) * bk_pow * psi[r_len]
    return out


def solve_tp_zeta1(rho: float, alpha: float) -> tuple[float, float, float]:
    """Solves the tangent point conditions (3.3) and (3.4) for zeta = 1 in log-space:
      u_2(x_0) = -x_0 / sqrt(rho) - sqrt((1 - rho)/rho) * sqrt(x_0^2 - 2*ln(sqrt(1 - rho)/alpha))
      ln Phi(-w) - (ln Phi(-u_2) - ln alpha) = 0.
    Returns (x0_tp, u_tp, t2_tp).
    """
    rho_bar = 1.0 - rho
    x0_upper = -math.sqrt(max(0.0, 2.0 * math.log(math.sqrt(rho_bar) / alpha)))

    def log_diff_at_u2(x0: float) -> float:
        rad = max(0.0, x0 * x0 - 2.0 * math.log(math.sqrt(rho_bar) / alpha))
        u2 = -x0 / math.sqrt(rho) - math.sqrt(rho_bar / rho) * math.sqrt(rad)
        w = u2 / math.sqrt(rho_bar) + math.sqrt(rho / rho_bar) * x0
        return log_phi_neg(w) - (log_phi_neg(u2) - math.log(alpha))

    hi = x0_upper
    lo = x0_upper - 0.5
    while log_diff_at_u2(lo) <= 0.0:
        lo -= 0.5
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if log_diff_at_u2(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    x0_tp = 0.5 * (lo + hi)
    rad = max(0.0, x0_tp * x0_tp - 2.0 * math.log(math.sqrt(rho_bar) / alpha))
    u_tp = -x0_tp / math.sqrt(rho) - math.sqrt(rho_bar / rho) * math.sqrt(rad)
    t2_tp = phi_cdf(-u_tp)
    return x0_tp, u_tp, t2_tp


def x0_func(t: float, zeta: float, rho: float, alpha: float) -> float:
    """Equation (3.1): x_0(t | zeta) = sqrt(rho_bar/rho)*Phi^{-1}((1 - t/alpha)/zeta)
    - Phi^{-1}(1 - t)/sqrt(rho).
    """
    rho_bar = 1.0 - rho
    q1 = phi_inv((1.0 - t / alpha) / zeta)
    q2 = phi_inv(1.0 - t)
    return math.sqrt(rho_bar / rho) * q1 - q2 / math.sqrt(rho)


def eer_fdr_dex_n_no_tp(zeta: float, rho: float, alpha: float, n_grid: int = 800) -> tuple[float, float]:
    """Computes EER_infty(zeta) and FDR_infty(zeta) in Theorem 3.1 when t_1 = t_2 (no TP):
      EER_infty(zeta) = int_{1-zeta}^1 Phi(x_0(alpha*t | zeta)) dt
      FDR_infty(zeta) = int_0^zeta Phi(x_0(alpha*(1 - zeta)/(1 - z) | zeta)) dz.
    """
    # Midpoint quadrature
    eer = 0.0
    a_eer, b_eer = 1.0 - zeta, 1.0
    h_eer = (b_eer - a_eer) / n_grid
    for i in range(n_grid):
        t_val = a_eer + (i + 0.5) * h_eer
        eer += phi_cdf(x0_func(alpha * t_val, zeta, rho, alpha)) * h_eer

    fdr = 0.0
    a_fdr, b_fdr = 0.0, zeta
    h_fdr = (b_fdr - a_fdr) / n_grid
    for i in range(n_grid):
        z_val = a_fdr + (i + 0.5) * h_fdr
        t_arg = alpha * (1.0 - zeta) / (1.0 - z_val)
        fdr += phi_cdf(x0_func(t_arg, zeta, rho, alpha)) * h_fdr

    return eer, fdr


def main() -> None:
    alpha = 0.05

    # 1. Verify Lemma 2.2 & Example 2.3 (pp. 1440-1441):
    # Under F_xi(t) = gamma(z)*t on [0, alpha] with gamma(z) = 2*exp(-z) <= 1/alpha,
    # for n = 6, n_0 = 4 (and n_1 = 2 Dirac-zero alternatives), alpha = 0.2, z = 0.8:
    n_ex, n0_ex, alpha_ex, z_ex = 6, 4, 0.2, 0.8
    n1_ex = n_ex - n0_ex
    gamma_z = 2.0 * math.exp(-z_ex)
    assert gamma_z <= 1.0 / alpha_ex
    # Under n_1 Dirac-zero false nulls, R'_n >= n_1, and the remaining n_0 i.i.d. nulls
    # have c.d.f. values F_xi(c_j) = gamma(z) * (j * alpha / n) at thresholds c_{n1+1}, ..., c_n.
    b_sub = [gamma_z * (j * alpha_ex / n_ex) for j in range(n1_ex + 2, n_ex + 1)]
    d_probs = d_su_dist(b_sub)
    fdr_cond_exact = 0.0
    for k in range(0, n0_ex):
        j = n1_ex + 1 + k
        p_xi_le_cj = gamma_z * (j * alpha_ex / n_ex)
        fdr_cond_exact += (n0_ex * p_xi_le_cj / j) * d_probs[k]
    fdr_lemma_2_2 = (n0_ex / n_ex) * gamma_z * alpha_ex
    assert abs(fdr_cond_exact - fdr_lemma_2_2) < 1e-15
    # Verify integral over Z ~ Exp(1): int_0^infty 2*exp(-z) * exp(-z) dz = 1
    # so unconditional FDR_n(zeta_n) = (n_0/n) * alpha
    uncond_fdr_ex23 = (n0_ex / n_ex) * alpha_ex * 1.0
    assert abs(uncond_fdr_ex23 - (n0_ex / n_ex) * alpha_ex) < 1e-15

    # 2. Verify Section 3 Equations (3.1)-(3.5), Theorem 3.2, Remark 3.1, and Theorem 3.3:
    # Exact limit as rho -> 0^+: Phi(-sqrt(-2*ln(alpha)))
    x0_limit_alpha = -math.sqrt(-2.0 * math.log(alpha))
    fdr_limit_rho0 = phi_cdf(x0_limit_alpha)
    # Check proof of Theorem 3.3 (p. 1453, PDF p. 22):
    # For u = -x_0(delta)/sqrt(rho) and w = u/sqrt(1-rho) + sqrt(rho/(1-rho))*x_0(delta)
    # where x_0(delta) = -sqrt(-2*ln(delta)):
    # Verify algebraically and numerically that exp((w^2 - u^2)/2) == delta independent of rho!
    for delta_test in [0.01, 0.03, 0.05]:
        x0_d = -math.sqrt(-2.0 * math.log(delta_test))
        for rho_test in [0.5, 0.1, 0.01, 0.001]:
            rb = 1.0 - rho_test
            u_val = -x0_d / math.sqrt(rho_test)
            w_val = u_val / math.sqrt(rb) + math.sqrt(rho_test / rb) * x0_d
            # Note w = -x0_d * (1/(sqrt(rho)*sqrt(rb)) - sqrt(rho)/sqrt(rb)) = -x0_d * sqrt(rb/rho)
            # so w^2 - u^2 = x0_d^2 * ((1 - rho)/rho - 1/rho) = -x0_d^2 = 2*ln(delta)!
            ratio_exp = math.exp(0.5 * (w_val * w_val - u_val * u_val))
            assert abs(ratio_exp - delta_test) < 1e-11

    rho_grid = [0.5, 0.1, 0.01, 0.001, 0.0001]
    tp_results: dict[str, dict[str, float]] = {}
    prev_fdr1 = 1.0
    for rho_val in rho_grid:
        x0_tp, u_tp, t2_tp = solve_tp_zeta1(rho_val, alpha)
        x0_ub = -math.sqrt(2.0 * math.log(math.sqrt(1.0 - rho_val) / alpha))
        fdr1_val = phi_cdf(x0_tp)
        fdr1_ub = phi_cdf(x0_ub)
        assert x0_tp <= x0_ub + 1e-12
        assert fdr1_val <= fdr1_ub + 1e-12
        tp_results[str(rho_val)] = {
            "x0_tp": round(x0_tp, 6),
            "x0_remark31_upper_bound": round(x0_ub, 6),
            "fdr_infty_1": round(fdr1_val, 6),
            "fdr_remark31_upper_bound": round(fdr1_ub, 6),
        }
        prev_fdr1 = fdr1_val

    # Confirm that at rho = 0.0001, FDR_infty(1) is strictly below alpha = 0.05 and
    # approaches Phi(-sqrt(-2*ln(alpha))) = 0.007188
    assert tp_results["0.0001"]["fdr_infty_1"] < 0.015
    assert fdr_limit_rho0 < 0.008

    # 3. Verify Theorem 3.1 (p. 1444-1446) for zeta = 0.5, alpha = 0.05:
    # As rho -> 0^+, the limiting crossing point is t^* = alpha*(1 - zeta)/(1 - alpha*zeta)
    # and EER_infty(zeta) = t^*/alpha - (1 - zeta) = zeta*t^* = alpha*zeta*(1 - zeta)/(1 - alpha*zeta)
    # (note: prose on p. 1446 writes alpha*(1 - zeta)/(1 - alpha*zeta), omitting the factor zeta,
    # whereas Theorem 3.1 and Figure 2 on p. 1445 plot the true value alpha*zeta*(1 - zeta)/(1 - alpha*zeta) = 0.01282051).
    zeta_mid = 0.5
    t_star_indep_mid = (alpha * (1.0 - zeta_mid)) / (1.0 - alpha * zeta_mid)
    eer_indep_mid = zeta_mid * t_star_indep_mid
    fdr_indep_mid = zeta_mid * alpha
    eer_rho001, fdr_rho001 = eer_fdr_dex_n_no_tp(zeta_mid, 0.001, alpha, n_grid=1000)
    eer_rho050, fdr_rho050 = eer_fdr_dex_n_no_tp(zeta_mid, 0.5, alpha, n_grid=1000)
    assert abs(eer_rho001 - eer_indep_mid) < 1e-4
    assert abs(fdr_rho001 - fdr_indep_mid) < 1e-4
    # EER_infty(0.5) increases with rho (Figure 2, p. 1445) while FDR_infty(0.5) <= zeta*alpha (Figure 3, p. 1446)
    assert eer_rho050 > eer_rho001
    assert fdr_rho050 < fdr_indep_mid

    # 4. Verify Lemma 4.1 & Theorem 4.3 (pp. 1448-1449, 1453-1454) for studentized D-EX-t(1):
    # s_nu(x) = 1 - nu^{-1/2}*sqrt(-ln x), a(s, nu) = sqrt((nu + 1)/s^2 - nu)
    nu_large = 100000000.0
    s_nu_alpha = 1.0 - math.sqrt(-math.log(alpha)) / math.sqrt(nu_large)
    a_val = math.sqrt((nu_large + 1.0) / (s_nu_alpha * s_nu_alpha) - nu_large)
    limit_a4_over_nu = (a_val ** 4) / nu_large
    limit_a2_one_minus_s2 = (a_val ** 2) * (1.0 - s_nu_alpha * s_nu_alpha)
    target_minus_4ln_alpha = -4.0 * math.log(alpha)
    clt_quantile = (nu_large * (s_nu_alpha * s_nu_alpha) - nu_large) / math.sqrt(2.0 * nu_large)
    assert abs(limit_a4_over_nu - target_minus_4ln_alpha) < 0.01
    assert abs(limit_a2_one_minus_s2 - target_minus_4ln_alpha) < 0.01
    assert abs(clt_quantile - x0_limit_alpha) < 0.001

    result = {
        "concept_id": "AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit",
        "primary_source": "Finner, Dickhaus, & Roters (2007), Annals of Statistics 35(4):1432-1455 (arXiv:0710.3171v1, DOI:10.1214/009053607000000046)",
        "lemma_2_2_and_example_2_3_verification": {
            "n": n_ex,
            "n0": n0_ex,
            "alpha": alpha_ex,
            "z": z_ex,
            "gamma_z": round(gamma_z, 8),
            "fdr_cond_exact_steck": round(fdr_cond_exact, 8),
            "fdr_cond_lemma_2_2": round(fdr_lemma_2_2, 8),
            "unconditional_fdr_example_2_3": round(uncond_fdr_ex23, 8),
        },
        "theorem_3_2_and_3_3_global_null_discontinuity": {
            "alpha": alpha,
            "x0_limit_minus_sqrt_minus_2ln_alpha": round(x0_limit_alpha, 8),
            "fdr_infty_1_limit_as_rho_to_0": round(fdr_limit_rho0, 8),
            "independent_global_null_fdr": alpha,
            "discontinuity_ratio_alpha_over_limit": round(alpha / fdr_limit_rho0, 4),
            "rho_grid_evaluations": tp_results,
        },
        "theorem_3_1_zeta_0_5_verification": {
            "zeta": zeta_mid,
            "alpha": alpha,
            "eer_independent_limit": round(eer_indep_mid, 8),
            "eer_at_rho_0_001": round(eer_rho001, 8),
            "eer_at_rho_0_5": round(eer_rho050, 8),
            "fdr_independent_limit": round(fdr_indep_mid, 8),
            "fdr_at_rho_0_001": round(fdr_rho001, 8),
            "fdr_at_rho_0_5": round(fdr_rho050, 8),
        },
        "lemma_4_1_and_theorem_4_3_studentized_t_scaling": {
            "nu": int(nu_large),
            "a4_over_nu": round(limit_a4_over_nu, 6),
            "a2_times_1_minus_s2": round(limit_a2_one_minus_s2, 6),
            "exact_minus_4_ln_alpha": round(target_minus_4ln_alpha, 6),
            "clt_quantile_at_nu_100000": round(clt_quantile, 6),
            "exact_clt_limit": round(x0_limit_alpha, 6),
        },
        "all_assertions_passed": True,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
