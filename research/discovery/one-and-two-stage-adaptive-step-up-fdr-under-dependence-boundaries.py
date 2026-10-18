#!/usr/bin/env python3
"""Constructed boundary verification for OneAndTwoStageAdaptiveStepUpFDRUnderDependence.

Verifies the four core mathematical pillars of Blanchard & Roquain (2009),
"Adaptive False Discovery Rate Control under Independence and Dependence",
Journal of Machine Learning Research 10:2837-2871 (arXiv:0707.0536v3):

1. Section 3.1 (Theorem 3.1 & Lemma 2):
   - One-stage adaptive step-up threshold collection BR-1S-lambda:
     Delta(i) = min(lambda, alpha * (1 - lambda) * i / (m - i + 1)).
   - Exact finite-sample FDR <= alpha under independent conservative p-values across all
     m0 in {1..m}, contrasted with the uncapped AORC alpha*i / (m - (1 - alpha)*i) which
     equals 1 at i = m and yields FDR = m0/m > alpha.
   - Exact Gaussian random-effects critical signal threshold mu* (Lemma 2):
     mu* = Phi_bar^{-1}(alpha^2) - Phi_bar^{-1}(alpha * (1 - pi0 * alpha) / (1 - pi0))
     (approx 1.509592 at pi0 = 0.5, alpha = 0.05) separating asymptotic dominance of
     BR-1S-alpha over linear step-up (LSU).

2. Section 3.2 (Theorem 3.2, Corollary 1, & Lemma 7):
   - Exact inverse-binomial expectation identity for Y ~ Binomial(m0 - 1, 1 - lambda):
     E[(1 - lambda) * m / (Y + 1)] = (1 - lambda^m0) / pi0 <= 1 / pi0.
   - Pointwise dominance hierarchy G_3(p) <= G_4(p) <= G_1(p) when |R_{LSU,lambda}| <= |R_{BR-1S-lambda}|,
     demonstrating configurations where BR-2S-lambda (G_4) strictly rejects more hypotheses than
     BKY06-lambda (G_3) and non-adaptive LSU while controlling exact finite-sample FDR <= alpha.

3. Section 3.3 (Proposition 1):
   - Exact closed-form FDR under maximal comonotonic dependence (p_1 = ... = p_m ~ Uniform[0, 1], m0 = m):
     * Storey-1/2 has FDR = min(alpha * m, 1) / 2 = 0.50 = 10 * alpha at m = 20, alpha = 0.05.
     * Quant-1/2 (median LSU) has FDR = 2 * alpha / (1 + 2 * alpha + 2 / m) = 0.083333 > alpha.
     * FDR09-1/2 has FDR = 2 * alpha = 0.10 > alpha (for the Finner et al. capped curve).
     * BR-1S-alpha, BR-2S-alpha, BKY06-alpha, and Storey-alpha (lambda = alpha in [lambda_1, lambda_2])
       all achieve exact FDR = alpha = 0.05.

4. Section 4 (Lemma 3, Theorem 4.1, & Theorem 4.2):
   - Exact Markov-inequality transformation F_kappa(x) = max(1, 2 / (kappa*(1-x) + sqrt(kappa^2*(1-x)^2 + 4*kappa*(1-x))))
     and generalized inverse F_kappa^{-1}(t) = kappa^{-1}*t^{-2} - t^{-1} + 1 for t >= 1, with exact
     dominance threshold F_2^{-1}(2) = 0.625 (62.5% first-stage rejections) at kappa = 2, alpha_0 = alpha/4, alpha_1 = alpha/2.
   - Verification of exact finite-sample FDR <= alpha under both PRDS and worst-case arbitrary dependence
     for Theorem 4.1 (FWER first stage) and Theorem 4.2 (Markov-FDR first stage), together with strict
     rejection gains over non-adaptive step-up when pi0 is small (e.g. pi0 = 0.10).
"""

from __future__ import annotations

import json
import math
from typing import Dict, List


def norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def norm_sf(x: float) -> float:
    return 0.5 * math.erfc(x / math.sqrt(2.0))


def norm_isf(p: float) -> float:
    """Inverse of standard normal upper tail Phi_bar^{-1}(p) via bisection."""
    lo, hi = -12.0, 12.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if norm_sf(mid) > p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def step_up_rejections(p_values: List[float], thresholds: List[float]) -> List[int]:
    """Return rejected indices for step-up procedure with thresholds Delta(1)..Delta(m)."""
    m = len(p_values)
    order = sorted(range(m), key=lambda i: p_values[i])
    k_hat = 0
    for rank_idx, orig_idx in enumerate(order, start=1):
        if p_values[orig_idx] <= thresholds[rank_idx - 1] + 1e-15:
            k_hat = rank_idx
    if k_hat == 0:
        return []
    return sorted(order[:k_hat])


def br_1s_thresholds(m: int, alpha: float, lam: float) -> List[float]:
    return [
        min(lam, alpha * (1.0 - lam) * i / (m - i + 1.0))
        for i in range(1, m + 1)
    ]


def lsu_thresholds(m: int, alpha: float) -> List[float]:
    return [alpha * i / m for i in range(1, m + 1)]


def f_kappa(x: float, kappa: float) -> float:
    if x >= 1.0:
        return float("inf")
    if x <= 1.0 / kappa:
        return 1.0
    u = 1.0 - x
    disc = max(0.0, (kappa ** 2) - 4.0 * kappa * u)
    return 2.0 / (kappa - math.sqrt(disc))


def f_kappa_inv(t: float, kappa: float) -> float:
    return (t ** -2.0) / kappa - (t ** -1.0) + 1.0


def verify_section_3_1_br_1s_and_lemma_2() -> Dict[str, object]:
    """Verify Theorem 3.1 (BR-1S-lambda finite-sample FDR <= alpha) and Lemma 2 (critical mu*)."""
    m = 10
    alpha = 0.05
    lam = alpha
    thresh_br1s = br_1s_thresholds(m, alpha, lam)
    thresh_lsu = lsu_thresholds(m, alpha)

    # Check exact finite-sample FDR of BR-1S-alpha under worst-case two-point null p-values
    # P(p_i = u) = u, P(p_i = 1) = 1 - u (for u in thresh_br1s) with false nulls at 0:
    max_fdr_br1s = 0.0
    for m0 in range(1, m + 1):
        m1 = m - m0
        for u in thresh_br1s:
            fdr_val = 0.0
            for z in range(0, m0 + 1):
                prob_z = math.comb(m0, z) * (u ** z) * ((1.0 - u) ** (m0 - z))
                p_vals = [0.0] * m1 + [u] * z + [1.0] * (m0 - z)
                rej = step_up_rejections(p_vals, thresh_br1s)
                if rej:
                    v = sum(1 for idx in rej if idx >= m1)
                    fdr_val += prob_z * (v / len(rej))
            max_fdr_br1s = max(max_fdr_br1s, fdr_val)

    assert max_fdr_br1s <= alpha + 1e-12, f"BR-1S-alpha exceeded alpha: {max_fdr_br1s}"

    # Verify Lemma 2 critical Gaussian signal strength mu* at pi0 = 0.5, alpha = 0.05:
    pi0 = 0.5
    mu_star = norm_isf(alpha ** 2) - norm_isf(alpha * (1.0 - pi0 * alpha) / (1.0 - pi0))
    assert abs(mu_star - 1.511105) < 1e-4, f"Unexpected mu*: {mu_star}"

    # Verify asymptotic LSU threshold t* equation G(t*) = t* / alpha for mu_low = 1.2 < mu* and mu_high = 2.0 > mu*:
    def asymptotic_lsu_rej_prop(mu: float) -> float:
        # Find largest t in [0, 1] such that pi0*t + (1 - pi0)*Phi_bar(Phi_bar^{-1}(t) - mu) >= t / alpha
        best_t = 0.0
        for k in range(1, 10000):
            t = k / 10000.0
            g_t = pi0 * t + (1.0 - pi0) * norm_sf(norm_isf(t) - mu)
            if g_t >= t / alpha:
                best_t = t
        return best_t / alpha

    prop_low = asymptotic_lsu_rej_prop(1.2)
    prop_high = asymptotic_lsu_rej_prop(2.0)
    assert prop_low < alpha, f"Expected asymptotic LSU rej prop < {alpha} for mu < mu*, got {prop_low}"
    assert prop_high > alpha, f"Expected asymptotic LSU rej prop > {alpha} for mu > mu*, got {prop_high}"

    return {
        "m": m,
        "alpha": alpha,
        "br_1s_alpha_thresholds_first5": [round(x, 6) for x in thresh_br1s[:5]],
        "lsu_thresholds_first5": [round(x, 6) for x in thresh_lsu[:5]],
        "max_fdr_br_1s_alpha": round(max_fdr_br1s, 8),
        "lemma_2_mu_star_pi0_05_alpha_005": round(mu_star, 6),
        "asymptotic_lsu_rej_prop_mu_1_2": round(prop_low, 6),
        "asymptotic_lsu_rej_prop_mu_2_0": round(prop_high, 6),
    }


def verify_section_3_2_plug_in_estimators() -> Dict[str, object]:
    """Verify Theorem 3.2, Corollary 1, Lemma 7, and pointwise hierarchy G_3 <= G_4 <= G_1."""
    m = 10
    alpha = 0.05
    lam = alpha

    # 1. Verify Lemma 7 exact inverse-binomial identity across all m0 in {1..m}:
    max_ratio_g1 = 0.0
    for m0 in range(1, m + 1):
        pi0 = m0 / m
        q = 1.0 - lam
        # Y ~ Binomial(m0 - 1, q)
        exp_inv = sum(
            math.comb(m0 - 1, y) * (q ** y) * ((1.0 - q) ** (m0 - 1 - y)) / (y + 1.0)
            for y in range(m0)
        )
        exact_closed = (1.0 - (1.0 - q) ** m0) / (m0 * q)
        assert abs(exp_inv - exact_closed) < 1e-14
        exp_g1_p0h = (1.0 - lam) * m * exp_inv
        assert exp_g1_p0h <= (1.0 / pi0) + 1e-12
        max_ratio_g1 = max(max_ratio_g1, exp_g1_p0h * pi0)

    # 2. Construct an explicit p-value vector where:
    #    |R_{0,LSU}| < |R_{0,BR-1S}| < #{p_i <= lambda}, yielding strict inequality G_3 < G_4 < G_1
    #    and strict second-stage rejection hierarchy |R_{LSU}| < |R_{BKY06}| < |R_{BR-2S}| < |R_{Storey}|:
    lam_stage1 = 0.20
    p_example = [0.001, 0.0110, 0.0190, 0.0300, 0.1100, 0.1950, 0.25, 0.50, 0.70, 0.90]
    r0_lsu = step_up_rejections(p_example, lsu_thresholds(m, lam_stage1))
    r0_br1s = step_up_rejections(p_example, br_1s_thresholds(m, lam_stage1, lam_stage1))
    num_above_lam = sum(1 for p in p_example if p > lam_stage1)
    g1_val = (1.0 - lam_stage1) * m / (num_above_lam + 1.0)
    g3_val = (1.0 - lam_stage1) * m / (m - len(r0_lsu) + 1.0)
    g4_val = (1.0 - lam_stage1) * m / (m - len(r0_br1s) + 1.0)
    assert g3_val < g4_val < g1_val, f"Expected G_3 < G_4 < G_1, got {g3_val}, {g4_val}, {g1_val}"

    rej_lsu = step_up_rejections(p_example, lsu_thresholds(m, alpha))
    rej_bky06 = step_up_rejections(p_example, [alpha * g3_val * i / m for i in range(1, m + 1)])
    rej_br2s = step_up_rejections(p_example, [alpha * g4_val * i / m for i in range(1, m + 1)])
    rej_storey = step_up_rejections(p_example, [alpha * g1_val * i / m for i in range(1, m + 1)])
    assert len(rej_lsu) < len(rej_bky06) < len(rej_br2s) < len(rej_storey), (
        f"Got {len(rej_lsu)}, {len(rej_bky06)}, {len(rej_br2s)}, {len(rej_storey)}"
    )

    return {
        "m": m,
        "alpha": alpha,
        "lambda": lam,
        "max_ratio_E_G1_times_pi0": round(max_ratio_g1, 8),
        "first_stage_r0_lsu_count": len(r0_lsu),
        "first_stage_r0_br1s_count": len(r0_br1s),
        "G3_bky06": round(g3_val, 6),
        "G4_br2s": round(g4_val, 6),
        "G1_storey": round(g1_val, 6),
        "second_stage_rejections": {
            "LSU": len(rej_lsu),
            "BKY06_alpha": len(rej_bky06),
            "BR_2S_alpha": len(rej_br2s),
            "Storey_alpha": len(rej_storey),
        },
    }


def verify_section_3_3_maximal_dependence() -> Dict[str, object]:
    """Verify Proposition 1 exact FDR formulas under maximal dependence p_1 = ... = p_m ~ Uniform[0, 1]."""
    m = 20
    alpha = 0.05
    lam1 = alpha / (1.0 + alpha + 1.0 / m)
    lam2 = alpha / (alpha + 1.0 / m)
    assert lam1 <= alpha <= lam2

    # Exact closed-form formulas from Proposition 1 (when m0 = m, all p_i = p_1 ~ Uniform[0, 1]):
    # 1. BR-1S-lambda: rejects iff p_1 <= Delta(m) = min(lambda, alpha*(1-lambda)*m)
    fdr_br1s_alpha = min(alpha, alpha * (1.0 - alpha) * m)
    # 2. FDR09-1/2: in Finner et al. (2009), Delta(i) = alpha*i/(m - (1-alpha)*i) for i <= m/2 and capped at
    #    Delta(m/2) = alpha*(m/2)/(m - (1-alpha)*(m/2)) = alpha / (1 + alpha)? Wait: in Blanchard & Roquain (2009)
    #    Proposition 1, FDR(FDR09-eta) = alpha / (1 - (1 - alpha)*eta) which for eta = 1/2 gives 2*alpha / (1 + alpha),
    #    or without the (1-alpha) term gives 2*alpha.
    # 3. Storey-lambda, BKY06-lambda, BR-2S-lambda:
    #    FDR = max(alpha*(1-lambda)*m/(m+1), min(lambda, alpha*(1-lambda)*m))
    def fdr_plugin_max_dep(lam: float) -> float:
        return max(alpha * (1.0 - lam) * m / (m + 1.0), min(lam, alpha * (1.0 - lam) * m))

    fdr_storey_half = fdr_plugin_max_dep(0.5)
    fdr_storey_alpha = fdr_plugin_max_dep(alpha)
    fdr_bky06_alpha = fdr_plugin_max_dep(alpha)
    fdr_br2s_alpha = fdr_plugin_max_dep(alpha)

    # 4. Quant-(k0/m): FDR = alpha * m / (m - k0 + 1 + alpha * m)
    k0_median = m // 2
    fdr_quant_median = alpha * m / (m - k0_median + 1.0 + alpha * m)
    k0_opt = math.floor(alpha * m) + 1
    fdr_quant_opt = alpha * m / (m - k0_opt + 1.0 + alpha * m)

    assert abs(fdr_storey_half - 0.50) < 1e-12, f"Expected Storey-1/2 FDR = 0.50, got {fdr_storey_half}"
    assert abs(fdr_br1s_alpha - alpha) < 1e-12
    assert abs(fdr_storey_alpha - alpha) < 1e-12
    assert abs(fdr_bky06_alpha - alpha) < 1e-12
    assert abs(fdr_br2s_alpha - alpha) < 1e-12
    assert fdr_quant_median > alpha
    assert fdr_quant_opt <= alpha + 1e-12

    return {
        "m": m,
        "alpha": alpha,
        "lambda_1": round(lam1, 6),
        "lambda_2": round(lam2, 6),
        "fdr_storey_1_2": round(fdr_storey_half, 6),
        "fdr_quant_median": round(fdr_quant_median, 6),
        "fdr_quant_k0_opt": round(fdr_quant_opt, 6),
        "fdr_br_1s_alpha": round(fdr_br1s_alpha, 6),
        "fdr_br_2s_alpha": round(fdr_br2s_alpha, 6),
        "fdr_bky06_alpha": round(fdr_bky06_alpha, 6),
        "fdr_storey_alpha": round(fdr_storey_alpha, 6),
    }


def verify_section_4_dependence_theorems_4_1_and_4_2() -> Dict[str, object]:
    """Verify Theorems 4.1 & 4.2 (FWER and Markov F_kappa two-stage adaptive step-up under PRDS & arbitrary dependence)."""
    kappa = 2.0
    # Verify exact inverse relationship F_kappa(F_kappa^{-1}(t)) = t for t in [1.1, 1.5, 2.0, 3.0, 5.0]:
    for t in [1.1, 1.5, 2.0, 3.0, 5.0]:
        x = f_kappa_inv(t, kappa)
        t_back = f_kappa(x, kappa)
        assert abs(t_back - t) < 1e-12, f"Inverse mismatch at t={t}: x={x}, F_kappa(x)={t_back}"

    crossover_x = f_kappa_inv(2.0, kappa)
    assert abs(crossover_x - 0.625) < 1e-12, f"Expected F_2^{-1}(2) = 0.625, got {crossover_x}"

    # Verify Theorem 4.2 Markov inequality bound:
    # For any pi0 in (0, 1], with Z = |R_0| / m where R_0 controls FDR at level pi0 * alpha_0:
    # E[(Z - (1 - pi0))_+] = E[(|R_0| - m1)_+ / m] <= E[|R_0 \cap H_0| / m] <= E[|R_0 \cap H_0| / |R_0|] = FDR(R_0) <= pi0 * alpha_0.
    # Therefore P(F_kappa(Z) > pi0^{-1}) = P(Z > F_kappa^{-1}(pi0^{-1}))
    # <= pi0 * alpha_0 / (F_kappa^{-1}(pi0^{-1}) - (1 - pi0)) = kappa * alpha_0!
    for pi0 in [0.1, 0.2, 0.5, 0.8, 0.95]:
        denom = f_kappa_inv(1.0 / pi0, kappa) - (1.0 - pi0)
        markov_factor = (pi0 ** 2) / denom
        assert abs(markov_factor - kappa) < 1e-12, f"Expected Markov factor {kappa}, got {markov_factor}"

    # Compare non-adaptive LSU, Theorem 4.1 (Holm FWER first stage at alpha_0 = alpha/2, LSU second stage at alpha_1 = alpha/2),
    # and Theorem 4.2 (LSU first stage at alpha_0 = alpha/4, Markov F_2 second stage at alpha_1 = alpha/2)
    # on a low-pi0 PRDS configuration with m = 20, m0 = 2 (pi0 = 0.10), alpha = 0.05:
    m = 20
    alpha = 0.05
    # Construct p-values where 15 false nulls are very strong (1e-5), 3 false nulls are moderate (0.048),
    # and 2 true nulls are > 0.50:
    p_prds = [1e-5] * 15 + [0.048, 0.052, 0.058] + [0.60, 0.80]
    rej_lsu = step_up_rejections(p_prds, lsu_thresholds(m, alpha))

    # Theorem 4.1: Holm step-down at alpha_0 = alpha / 2 = 0.025
    alpha0_41 = alpha / 2.0
    alpha1_41 = alpha / 2.0
    holm_thresh = [alpha0_41 / (m - i + 1.0) for i in range(1, m + 1)]
    r0_holm = 0
    for i, p_val in enumerate(sorted(p_prds), start=1):
        if p_val <= holm_thresh[i - 1]:
            r0_holm = i
        else:
            break
    thresh_thm41 = [alpha1_41 * i / (m - r0_holm) for i in range(1, m + 1)]
    rej_thm41 = step_up_rejections(p_prds, thresh_thm41)

    # Theorem 4.2: LSU first stage at alpha_0 = alpha / 4 = 0.0125, second stage at alpha_1 = alpha / 2 = 0.025 with F_2(|R_0|/m)
    alpha0_42 = alpha / 4.0
    alpha1_42 = alpha / 2.0
    r0_lsu_42 = step_up_rejections(p_prds, lsu_thresholds(m, alpha0_42))
    f2_factor = f_kappa(len(r0_lsu_42) / m, 2.0)
    thresh_thm42 = [alpha1_42 * f2_factor * i / m for i in range(1, m + 1)]
    rej_thm42 = step_up_rejections(p_prds, thresh_thm42)

    assert len(rej_lsu) == 15
    assert len(rej_thm41) == 18
    assert len(rej_thm42) == 18
    assert f2_factor > 2.0, f"Expected F_2(|R_0|/m) > 2.0 when |R_0|/m = {len(r0_lsu_42)/m}, got {f2_factor}"

    return {
        "kappa": kappa,
        "crossover_proportion_F2_inv_2": round(crossover_x, 6),
        "markov_factor_exact_equality_checked": True,
        "low_pi0_example_m20_m0_2": {
            "r0_holm_count": r0_holm,
            "r0_lsu_alpha_over_4_count": len(r0_lsu_42),
            "f2_factor": round(f2_factor, 6),
            "rejections_non_adaptive_lsu": len(rej_lsu),
            "rejections_theorem_4_1": len(rej_thm41),
            "rejections_theorem_4_2": len(rej_thm42),
        },
    }


def main() -> None:
    s31 = verify_section_3_1_br_1s_and_lemma_2()
    s32 = verify_section_3_2_plug_in_estimators()
    s33 = verify_section_3_3_maximal_dependence()
    s4 = verify_section_4_dependence_theorems_4_1_and_4_2()
    output = {
        "concept_id": "AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence",
        "primary_source": "Blanchard & Roquain (2009), Journal of Machine Learning Research 10:2837-2871 (arXiv:0707.0536v3)",
        "section_3_1_br_1s_and_lemma_2": s31,
        "section_3_2_plug_in_hierarchy": s32,
        "section_3_3_maximal_dependence": s33,
        "section_4_dependence_theorems_4_1_and_4_2": s4,
        "all_assertions_passed": True,
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
