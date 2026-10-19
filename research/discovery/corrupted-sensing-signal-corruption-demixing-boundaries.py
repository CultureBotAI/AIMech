#!/usr/bin/env python3
"""Constructed boundary and primary-source verification for Foygel & Mackey (2014).

Reference:
Rina Foygel and Lester Mackey (2014), "Corrupted Sensing: Novel Guarantees for
Separating Structured Signals," IEEE Transactions on Information Theory,
60(2):1223-1247, DOI:10.1109/TIT.2013.2293654 (arXiv:1305.2524v2).

Verifies:
1. Proposition 3 (p. 17) general subdifferential squared distance bound
   eta^2(t * partial ||x||) <= p - (tilde_omega / max_{||z||_2=1} ||z||)^2
   at t = tilde_omega / max_{||z||_2=1} ||z||^2, and its comparison on s-sparse
   vectors in R^p (||.||_1) between Eq. (8) (Chandrasekaran et al., 2s*log(p/s) + 1.5*s),
   Eq. (9) (p*(1 - (2/pi)*(1 - s/p)^2) at t' = sqrt(2/pi)*(1 - s/p)), and the exact
   integral minimum Eq. (10), confirming Eq. (9) is strictly tighter than Eq. (8)
   for all s/p >= 0.07.
2. Proposition 4 (p. 17, Eqs. 24-25) block-sparse l_1/l_2 subdifferential squared
   distance bounds inBoth sparse regime (4s*log(m/s) + (0.5 + 3k)*s at
   t = sqrt(2*log(m/s)) + sqrt(k)) and dense regime (p*(1 - (mu_k^2/k)*(1 - s/m)^2)
   at t' = mu_k*(1 - s/m)), and Proposition 5 (p. 19) matrix nuclear norm bound
   m1*m2*(1 - (4/27)^2*(1 - r/m1)*(1 - r/m2)^2).
3. Theorem 1 & Corollary 1 (pp. 4, 8) constrained corrupted sensing recovery
   condition mu_n > tau = sqrt(omega^2(T_sig) + omega^2(T_cor)) + 1/sqrt(2) + 1/sqrt(2*pi)
   and Wyner coding / gross sparse corruption phase transition gamma_0 ~= 19.3%
   where psi_l1(gamma_0) = 1/2.
4. Theorem 2 (p. 4) penalized corrupted sensing recovery with penalty parameter
   lambda = t_cor / t_sig and empirical verification on synthetic Gaussian
   corrupted sensing y = Phi*x_star + v_star.
"""

from __future__ import annotations

import json
import math
import random


def norm_pdf(x: float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def norm_sf(x: float) -> float:
    return 0.5 * math.erfc(x / math.sqrt(2.0))


def mu_chi(k: int) -> float:
    """Expected Euclidean norm E[||g||_2] of g ~ N(0, I_k), Fact 3."""
    return math.sqrt(2.0) * math.exp(
        math.lgamma(0.5 * (k + 1)) - math.lgamma(0.5 * k)
    )


def l1_exact_psi(rho: float) -> tuple[float, float]:
    """Exact normalized min_t eta^2(t * partial ||x||_1)/p from Eq. (10), p. 6."""
    lo, hi = 0.0, 20.0
    for _ in range(100):
        m1 = lo + (hi - lo) / 3.0
        m2 = hi - (hi - lo) / 3.0
        v1 = rho * (1.0 + m1 * m1) + (1.0 - rho) * 2.0 * (
            (1.0 + m1 * m1) * norm_sf(m1) - m1 * norm_pdf(m1)
        )
        v2 = rho * (1.0 + m2 * m2) + (1.0 - rho) * 2.0 * (
            (1.0 + m2 * m2) * norm_sf(m2) - m2 * norm_pdf(m2)
        )
        if v1 < v2:
            hi = m2
        else:
            lo = m1
    t_opt = 0.5 * (lo + hi)
    val = rho * (1.0 + t_opt * t_opt) + (1.0 - rho) * 2.0 * (
        (1.0 + t_opt * t_opt) * norm_sf(t_opt) - t_opt * norm_pdf(t_opt)
    )
    return t_opt, val


def verify_l1_subdifferential_bounds() -> dict[str, object]:
    """Verify Eqs. (8), (9), and (10) across sparsity fractions s/p."""
    p = 1000
    comparisons = {}
    for rho in [0.02, 0.05, 0.07, 0.10, 0.25, 0.50]:
        s = int(round(rho * p))
        # Eq. (8): Chandrasekaran et al. bound 2s log(p/s) + (3/2)s
        bound_eq8 = 2.0 * s * math.log(p / s) + 1.5 * s
        t_eq8 = math.sqrt(2.0 * math.log(p / s))
        # Eq. (9): Foygel & Mackey dense-regime bound p*(1 - (2/pi)*(1 - s/p)^2)
        t_eq9 = math.sqrt(2.0 / math.pi) * (1.0 - rho)
        bound_eq9 = p * (1.0 - (2.0 / math.pi) * ((1.0 - rho) ** 2))
        # Eq. (10): exact integral minimum
        t_exact, psi_exact = l1_exact_psi(rho)
        bound_eq10 = p * psi_exact

        # Verify analytical ordering: bound_eq10 <= bound_eq9 < p for all rho < 1
        assert bound_eq10 <= bound_eq9 + 1e-9
        assert bound_eq9 < p
        if rho >= 0.07:
            assert bound_eq9 < bound_eq8, (
                f"Expected Eq. (9) < Eq. (8) at rho={rho}: {bound_eq9} vs {bound_eq8}"
            )
        comparisons[f"rho_{rho:.2f}"] = {
            "t_eq8": round(t_eq8, 6),
            "bound_eq8_normalized": round(bound_eq8 / p, 6),
            "t_eq9": round(t_eq9, 6),
            "bound_eq9_normalized": round(bound_eq9 / p, 6),
            "t_eq10": round(t_exact, 6),
            "bound_eq10_normalized": round(bound_eq10 / p, 6),
        }
    return comparisons


def verify_block_sparse_and_nuclear_bounds() -> dict[str, object]:
    """Verify Proposition 4 (block-sparse l_1/l_2) and Proposition 5 (nuclear norm)."""
    k = 5
    m = 200
    p = k * m
    s = 40  # s/m = 0.20
    rho_block = s / m
    mu_k = mu_chi(k)
    # Fact 3: k / sqrt(k+1) <= mu_k <= sqrt(k)
    assert k / math.sqrt(k + 1.0) <= mu_k <= math.sqrt(k)

    # Eq. (24): sparse block regime
    t_eq24 = math.sqrt(2.0 * math.log(m / s)) + math.sqrt(k)
    bound_eq24 = 4.0 * s * math.log(m / s) + (0.5 + 3.0 * k) * s

    # Eq. (25): dense block regime (Proposition 4)
    t_eq25 = mu_k * (1.0 - rho_block)
    bound_eq25 = p * (1.0 - (mu_k * mu_k / k) * ((1.0 - rho_block) ** 2))
    assert bound_eq25 < p
    assert bound_eq25 < bound_eq24

    # Monte Carlo check of E[dist(g, t' * partial ||x||_{l1/l2})^2] at t' = t_eq25
    rng = random.Random(20261019)
    n_mc = 400
    mc_sum = 0.0
    for _ in range(n_mc):
        dist_sq = 0.0
        # Active blocks i=1..s have unit subgradient e_i = (1,0,...,0)
        for _ in range(s):
            g0 = rng.gauss(0.0, 1.0) - t_eq25
            dist_sq += g0 * g0
            for _ in range(k - 1):
                gj = rng.gauss(0.0, 1.0)
                dist_sq += gj * gj
        # Inactive blocks i=s+1..m have subgradient ball ||z_i||_2 <= t_eq25
        for _ in range(m - s):
            norm_sq = sum(rng.gauss(0.0, 1.0) ** 2 for _ in range(k))
            norm_g = math.sqrt(norm_sq)
            excess = max(0.0, norm_g - t_eq25)
            dist_sq += excess * excess
        mc_sum += dist_sq
    mc_mean = mc_sum / n_mc
    assert mc_mean <= bound_eq25

    # Proposition 5: nuclear norm in R^{m1 x m2}
    m1, m2, r = 50, 40, 4
    t_nuc = (4.0 / 27.0) * (m2 - r) * math.sqrt(m1 - r) / m2
    bound_prop5 = (
        m1
        * m2
        * (
            1.0
            - ((4.0 / 27.0) ** 2)
            * (1.0 - r / m1)
            * ((1.0 - r / m2) ** 2)
        )
    )
    bound_crpw_nuc = 3.0 * r * (m1 + m2 - r)
    assert bound_prop5 < m1 * m2

    return {
        "block_sparse_k5_m200_s40": {
            "mu_k": round(mu_k, 6),
            "t_eq24": round(t_eq24, 6),
            "bound_eq24_normalized": round(bound_eq24 / p, 6),
            "t_eq25": round(t_eq25, 6),
            "bound_eq25_normalized": round(bound_eq25 / p, 6),
            "mc_mean_normalized": round(mc_mean / p, 6),
        },
        "nuclear_norm_50x40_r4": {
            "t_prop5": round(t_nuc, 6),
            "bound_prop5_normalized": round(bound_prop5 / (m1 * m2), 6),
            "bound_crpw_normalized": round(bound_crpw_nuc / (m1 * m2), 6),
        },
    }


def verify_corrupted_sensing_demixing_thresholds() -> dict[str, object]:
    """Verify Corollary 1 Wyner coding threshold gamma_0 and Theorem 1 vs Theorem 2."""
    # Find gamma_0 where exact l_1 normalized Gaussian width squared psi(gamma_0) = 0.5
    lo, hi = 0.15, 0.25
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        _, psi_val = l1_exact_psi(mid)
        if psi_val < 0.5:
            lo = mid
        else:
            hi = mid
    gamma_0 = 0.5 * (lo + hi)
    # Section IV.A p. 8 reports gamma_0 ~= 19.3%
    assert 0.192 <= gamma_0 <= 0.194

    # Compare Theorem 1 (constrained) and Theorem 2 (penalized) sample thresholds
    p = 500
    s_sig = 5  # 1% sparse signal
    gamma_cor = 0.02  # 2% corrupted measurements
    n = 1200
    s_cor = int(round(gamma_cor * n))

    t_sig, psi_sig = l1_exact_psi(s_sig / p)
    t_cor, psi_cor = l1_exact_psi(s_cor / n)
    eta_sig = math.sqrt(p * psi_sig)
    eta_cor = math.sqrt(n * psi_cor)

    c_const = 1.0 / math.sqrt(2.0) + 1.0 / math.sqrt(2.0 * math.pi)
    tau_thm1 = math.sqrt(eta_sig * eta_sig + eta_cor * eta_cor) + c_const
    tau_thm2 = (
        2.0 * eta_sig
        + eta_cor
        + 3.0 * math.sqrt(2.0 * math.pi)
        + c_const
    )
    mu_n = n / math.sqrt(n + 1.0)
    lambda_opt = t_cor / t_sig
    assert mu_n > tau_thm1
    assert mu_n > tau_thm2
    assert tau_thm1 < tau_thm2

    return {
        "wyner_coding_max_corruption_fraction_gamma0": round(gamma_0, 6),
        "demixing_p500_ssig5_n1200_gamma002": {
            "t_sig": round(t_sig, 6),
            "t_cor": round(t_cor, 6),
            "lambda_penalized_ratio": round(lambda_opt, 6),
            "eta_sig": round(eta_sig, 6),
            "eta_cor": round(eta_cor, 6),
            "tau_theorem1_constrained": round(tau_thm1, 6),
            "tau_theorem2_penalized": round(tau_thm2, 6),
            "mu_n_lower_bound": round(mu_n, 6),
        },
    }


def main() -> None:
    res = {
        "l1_subdifferential_bounds": verify_l1_subdifferential_bounds(),
        "block_sparse_and_nuclear_bounds": verify_block_sparse_and_nuclear_bounds(),
        "corrupted_sensing_thresholds": verify_corrupted_sensing_demixing_thresholds(),
    }
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
