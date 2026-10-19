#!/usr/bin/env python3
"""Constructed boundary and verification checks for Round 269:
Escape-Through-a-Mesh Quarter-Circle and Semicircle Null-Space Recovery Thresholds
for Matrix Rank Minimization (Oymak & Hassibi 2010, arXiv:1011.6326v1).

Verifies:
1. Exact closed-form evaluation of the quarter-circle singular-value density
   phi(x) = sqrt(4 - x^2)/pi on [0, 2], its CDF F(x), and incomplete moments
   gamma(beta) = int_{F^{-1}(1-beta)}^2 x phi(x) dx (Eq. 7) and
   gamma_2(beta) = int_{F^{-1}(1-beta)}^2 x^2 phi(x) dx (Eq. 8), including
   gamma(0)=0, gamma(1)=8/(3*pi), gamma_2(0)=0, gamma_2(1)=1, and the Wigner semicircle
   reductions gamma_s(beta) = gamma(2*beta)/2 and gamma_{2,s}(beta) = gamma_2(2*beta)/2 (Eqs. 104-107).
2. Exact root-finding and threshold evaluation for square n x n nuclear norm minimization:
   - Strong threshold mu_strong(beta) via Theorem 2 (Eqs. 44-45),
   - Sectional threshold mu_sec(beta) via Theorem 3 (Eqs. 76-77),
   - Weak threshold mu_weak(beta) via Theorem 4 (Eqs. 95-96),
   verifying strict ordering theta(beta) = beta*(2 - beta) < mu_weak(beta) < mu_sec(beta) < mu_strong(beta) <= 1,
   improvement over the delta = 0 baseline of Recht-Xu-Hassibi [4] / Oymak-Khajehnejad-Hassibi [12]
   (Section 6, p. 26), and constant-factor weak oversampling mu_weak(beta) / theta(beta) < 3.
3. Positive semidefinite (PSD) trace minimization thresholds:
   - PSD weak threshold mu_{PSD,weak}(beta) via Theorem 5 / Lemma 25 (Eqs. 137-138),
   - PSD strong threshold mu_{PSD,strong}(beta) via Theorem 6 (Eqs. 150-151),
   - PSD weak and strong uniqueness thresholds without trace minimization via Lemmas 29 & 31 (Eqs. 152-154):
     mu_{uniq,weak}(beta) = 1 - (1 - beta)^2 / 2 and mu_{uniq,strong}(beta) = (1 + gamma_2(2*beta)) / 2,
   verifying mu_{PSD,weak}(beta) < mu_{uniq,weak}(beta) for beta < 1 (trace minimization strictly improves
   upon PSD feasibility alone, which requires at least mu > 0.5 even as beta -> 0) and
   mu_{PSD,weak}(beta) < mu_{PSD,strong}(beta), plus deterministic null-space certification (Lemma 6, Eq. 20).
"""

from __future__ import annotations

import json
import math
from typing import Dict, List


def phi_qc(x: float) -> float:
    """Quarter-circle density phi(x) = (1/pi) * sqrt(4 - x^2) on [0, 2] (Eq. 4)."""
    if x <= 0.0 or x >= 2.0:
        return 0.0
    return math.sqrt(max(0.0, 4.0 - x * x)) / math.pi


def cdf_qc(x: float) -> float:
    """Exact CDF F(x) = int_0^x (1/pi) sqrt(4 - t^2) dt on [0, 2] (Eq. 6)."""
    if x <= 0.0:
        return 0.0
    if x >= 2.0:
        return 1.0
    return (x * math.sqrt(4.0 - x * x) + 4.0 * math.asin(x / 2.0)) / (2.0 * math.pi)


def inv_cdf_qc(prob: float) -> float:
    """Invert F(x) = prob on [0, 2] via bisection."""
    if prob <= 0.0:
        return 0.0
    if prob >= 1.0:
        return 2.0
    lo, hi = 0.0, 2.0
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if cdf_qc(mid) < prob:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def gamma_qc(beta: float) -> float:
    """Exact first tail moment gamma(beta) = int_{F^{-1}(1-beta)}^2 x * phi(x) dx (Eq. 7)
    = (1 / (3*pi)) * (4 - a^2)^{3/2} where a = F^{-1}(1 - beta)."""
    if beta <= 0.0:
        return 0.0
    if beta >= 1.0:
        return 8.0 / (3.0 * math.pi)
    a = inv_cdf_qc(1.0 - beta)
    return ((4.0 - a * a) ** 1.5) / (3.0 * math.pi)


def gamma2_qc(beta: float) -> float:
    """Exact second tail moment gamma_2(beta) = int_{F^{-1}(1-beta)}^2 x^2 * phi(x) dx (Eq. 8)."""
    if beta <= 0.0:
        return 0.0
    if beta >= 1.0:
        return 1.0
    a = inv_cdf_qc(1.0 - beta)
    s = math.sqrt(max(0.0, 4.0 - a * a))
    anti_2 = math.pi
    anti_a = -0.25 * a * (s**3) + 0.5 * a * s + 2.0 * math.asin(a / 2.0)
    return (anti_2 - anti_a) / math.pi


def mu_strong_nuclear(beta: float) -> float:
    """Theorem 2 strong threshold for square n x n nuclear norm minimization (Eqs. 44-45):
    If gamma(1) - 2*gamma(beta) <= 0, mu = 1. Otherwise solve for delta_s in (0, 1):
    (gamma(1 - delta_s) - 2*gamma(beta)) / (1 - delta_s) = F^{-1}(delta_s),
    then mu = gamma_2(1 - delta_s) - (gamma(1 - delta_s) - 2*gamma(beta))^2 / (1 - delta_s)."""
    g1 = gamma_qc(1.0)
    gb = gamma_qc(beta)
    if g1 - 2.0 * gb <= 0.0:
        return 1.0

    def diff(d: float) -> float:
        lhs = (gamma_qc(1.0 - d) - 2.0 * gb) / (1.0 - d)
        rhs = inv_cdf_qc(d)
        return lhs - rhs

    lo, hi = 1e-9, 1.0 - 1e-9
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if diff(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    ds = 0.5 * (lo + hi)
    num = gamma_qc(1.0 - ds) - 2.0 * gb
    val = gamma2_qc(1.0 - ds) - (num * num) / (1.0 - ds)
    return min(1.0, max(0.0, val))


def mu_strong_nuclear_delta0(beta: float) -> float:
    """Baseline strong threshold at delta_s = 0 corresponding to Recht-Xu-Hassibi [4] / [12]
    (Section 6, p. 26): mu_0 = 1 - (gamma(1) - 2*gamma(beta))^2 if gamma(1) > 2*gamma(beta) else 1."""
    g1 = gamma_qc(1.0)
    gb = gamma_qc(beta)
    if g1 - 2.0 * gb <= 0.0:
        return 1.0
    return 1.0 - (g1 - 2.0 * gb) ** 2


def mu_sectional_nuclear(beta: float) -> float:
    """Theorem 3 sectional threshold for square n x n nuclear norm minimization (Eqs. 76-77):
    If beta >= 0.5 or (1-beta)^{3/2} gamma(1) - beta^{3/2} gamma(1) <= 0, mu = 1.
    Otherwise solve for delta_sec in (0, 1):
    ((1-beta)^{3/2} gamma(1 - delta) - beta^{3/2} gamma(1)) / (sqrt(1-beta) * (1 - delta*(1-beta))) = F^{-1}(delta),
    then mu = 1 - (1-beta)^2 (1 - gamma_2(1 - delta_sec))
              - ((1-beta)^{3/2} gamma(1 - delta_sec) - beta^{3/2} gamma(1))^2 / (1 - delta_sec*(1-beta))."""
    if beta >= 0.5:
        return 1.0
    g1 = gamma_qc(1.0)
    c1 = (1.0 - beta) ** 1.5
    c2 = (beta**1.5) * g1
    if c1 * g1 - c2 <= 0.0:
        return 1.0

    def diff(d: float) -> float:
        lhs = (c1 * gamma_qc(1.0 - d) - c2) / (
            math.sqrt(1.0 - beta) * (1.0 - d * (1.0 - beta))
        )
        rhs = inv_cdf_qc(d)
        return lhs - rhs

    lo, hi = 1e-9, 1.0 - 1e-9
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if diff(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    dsec = 0.5 * (lo + hi)
    num = c1 * gamma_qc(1.0 - dsec) - c2
    val = (
        1.0
        - ((1.0 - beta) ** 2) * (1.0 - gamma2_qc(1.0 - dsec))
        - (num * num) / (1.0 - dsec * (1.0 - beta))
    )
    return min(1.0, max(0.0, val))


def mu_weak_nuclear(beta: float) -> float:
    """Theorem 4 weak threshold for square n x n nuclear norm minimization (Eqs. 95-96):
    Solve for delta_w in (0, 1):
    ((1-beta)^{3/2} gamma(1 - delta)) / (sqrt(1-beta) * (1 - delta*(1-beta))) = F^{-1}(delta),
    then mu = 1 - (1-beta)^2 (1 - gamma_2(1 - delta_w))
              - (1-beta)^3 gamma(1 - delta_w)^2 / (1 - delta_w*(1-beta))."""
    if beta >= 1.0:
        return 1.0

    def diff(d: float) -> float:
        lhs = ((1.0 - beta) * gamma_qc(1.0 - d)) / (1.0 - d * (1.0 - beta))
        rhs = inv_cdf_qc(d)
        return lhs - rhs

    lo, hi = 1e-9, 1.0 - 1e-9
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if diff(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    dw = 0.5 * (lo + hi)
    gw = gamma_qc(1.0 - dw)
    val = (
        1.0
        - ((1.0 - beta) ** 2) * (1.0 - gamma2_qc(1.0 - dw))
        - ((1.0 - beta) ** 3) * (gw * gw) / (1.0 - dw * (1.0 - beta))
    )
    return min(1.0, max(0.0, val))


def mu_weak_psd(beta: float) -> float:
    """Lemma 25 / Theorem 5 PSD weak threshold for trace minimization (Eqs. 137-138):
    Solve for delta_wp in (0, 1):
    ((1-beta)^{3/2} gamma(1 - delta)) / (1 + beta - (1-beta)*delta) = sqrt(1-beta) * F^{-1}(delta),
    then mu = 1 - (1-beta)^2 (1 - gamma_2(1 - delta_wp)/2)
              - (1-beta)^3 gamma(1 - delta_wp)^2 / (2*(1 + beta - (1-beta)*delta_wp))."""
    if beta >= 1.0:
        return 1.0

    def diff(d: float) -> float:
        lhs = ((1.0 - beta) * gamma_qc(1.0 - d)) / (
            1.0 + beta - (1.0 - beta) * d
        )
        rhs = inv_cdf_qc(d)
        return lhs - rhs

    lo, hi = 1e-9, 1.0 - 1e-9
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if diff(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    dwp = 0.5 * (lo + hi)
    gwp = gamma_qc(1.0 - dwp)
    val = (
        1.0
        - ((1.0 - beta) ** 2) * (1.0 - 0.5 * gamma2_qc(1.0 - dwp))
        - ((1.0 - beta) ** 3)
        * (gwp * gwp)
        / (2.0 * (1.0 + beta - (1.0 - beta) * dwp))
    )
    return min(1.0, max(0.0, val))


def mu_strong_psd(beta: float) -> float:
    """Theorem 6 PSD strong threshold for trace minimization (Eqs. 150-151):
    If beta >= 0.5 or gamma(1) - gamma(2*beta) <= 0, mu = 1.
    Otherwise solve for delta_sp in (0, 1):
    (gamma(1 - delta) - gamma(2*beta)) / (2*beta + 1 - delta) = F^{-1}(delta),
    then mu = 0.5 * [ gamma_2(1 - delta_sp) + gamma_2(2*beta)
                      - (gamma(1 - delta_sp) - gamma(2*beta))^2 / (2*beta + 1 - delta_sp) ]."""
    if beta >= 0.5:
        return 1.0
    g1 = gamma_qc(1.0)
    g2b = gamma_qc(2.0 * beta)
    if g1 - g2b <= 0.0:
        return 1.0

    def diff(d: float) -> float:
        lhs = (gamma_qc(1.0 - d) - g2b) / (2.0 * beta + 1.0 - d)
        rhs = inv_cdf_qc(d)
        return lhs - rhs

    lo, hi = 1e-9, 1.0 - 1e-9
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if diff(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    dsp = 0.5 * (lo + hi)
    num = gamma_qc(1.0 - dsp) - g2b
    val = 0.5 * (
        gamma2_qc(1.0 - dsp)
        + gamma2_qc(2.0 * beta)
        - (num * num) / (2.0 * beta + 1.0 - dsp)
    )
    return min(1.0, max(0.0, val))


def verify_thresholds_and_lemma6() -> Dict[str, object]:
    """Verify quarter-circle moments, Theorem 2/3/4 nuclear norm curves, Theorem 5/6 PSD curves,
    Lemmas 29/31 uniqueness curves, and Lemma 6 deterministic null-space condition."""
    assert abs(gamma_qc(1.0) - 8.0 / (3.0 * math.pi)) < 1e-12
    assert abs(gamma2_qc(1.0) - 1.0) < 1e-12

    betas = [0.02, 0.05, 0.10, 0.20, 0.30, 0.40]
    nuclear_curves: List[Dict[str, float]] = []
    psd_and_uniqueness_curves: List[Dict[str, float]] = []
    max_oversampling_ratio = 0.0

    for b in betas:
        dof = b * (2.0 - b)
        mw = mu_weak_nuclear(b)
        msec = mu_sectional_nuclear(b)
        mstr = mu_strong_nuclear(b)
        mstr0 = mu_strong_nuclear_delta0(b)
        ratio = mw / dof
        if ratio > max_oversampling_ratio:
            max_oversampling_ratio = ratio

        assert dof < mw < msec <= mstr <= mstr0 <= 1.0, (
            f"Ordering violated at beta={b}: dof={dof}, weak={mw}, sec={msec},"
            f" strong={mstr}, strong_delta0={mstr0}"
        )
        assert ratio < 3.0, f"Oversampling ratio {ratio} >= 3 at beta={b}"

        nuclear_curves.append(
            {
                "beta": b,
                "dof_theta": round(dof, 6),
                "mu_weak": round(mw, 6),
                "mu_sectional": round(msec, 6),
                "mu_strong": round(mstr, 6),
                "mu_strong_delta0_baseline": round(mstr0, 6),
                "weak_over_dof_ratio": round(ratio, 6),
            }
        )

        psd_w = mu_weak_psd(b)
        psd_s = mu_strong_psd(b)
        uniq_w = 1.0 - 0.5 * ((1.0 - b) ** 2)
        uniq_s = 0.5 * (1.0 + gamma2_qc(2.0 * b))
        # Trace minimization weak threshold is strictly lower than PSD uniqueness weak threshold
        assert dof < psd_w < uniq_w < 1.0
        assert psd_w < psd_s <= 1.0
        assert uniq_w < uniq_s <= 1.0
        psd_and_uniqueness_curves.append(
            {
                "beta": b,
                "mu_psd_weak": round(psd_w, 6),
                "mu_psd_strong": round(psd_s, 6),
                "mu_uniq_weak": round(uniq_w, 6),
                "mu_uniq_strong": round(uniq_s, 6),
            }
        )

    # Verify Lemma 6 (Eq. 20) deterministic null-space necessary and sufficient condition:
    # 2 ||W||_r < ||W||_* implies ||X + W||_* >= ||X||_* + ||W||_* - 2||W||_r > ||X||_*
    r = 1
    x_sing = [2.0, 0.0, 0.0, 0.0]
    w_sing = [0.26, 0.24, 0.22, 0.18]
    w_sorted = sorted(w_sing, reverse=True)
    w_kyfan_r = sum(w_sorted[:r])
    w_nuc = sum(w_sorted)
    assert 2.0 * w_kyfan_r < w_nuc
    # Construct worst-case aligned perturbation X + W where top-r singular values of W subtract from X
    nuc_x = sum(x_sing)
    nuc_x_plus_w = (
        abs(x_sing[0] - w_sorted[0])
        + w_sorted[1]
        + w_sorted[2]
        + w_sorted[3]
    )
    assert nuc_x_plus_w >= nuc_x + (w_nuc - 2.0 * w_kyfan_r) - 1e-12
    assert nuc_x_plus_w > nuc_x

    return {
        "gamma_1": round(gamma_qc(1.0), 8),
        "gamma2_1": round(gamma2_qc(1.0), 8),
        "baseline_limit_beta0": round(1.0 - (8.0 / (3.0 * math.pi)) ** 2, 8),
        "max_weak_oversampling_ratio": round(max_oversampling_ratio, 6),
        "nuclear_norm_phase_transitions": nuclear_curves,
        "psd_and_uniqueness_transitions": psd_and_uniqueness_curves,
        "lemma6_2_kyfan_r": round(2.0 * w_kyfan_r, 6),
        "lemma6_w_nuc": round(w_nuc, 6),
        "lemma6_nuc_x": round(nuc_x, 6),
        "lemma6_nuc_x_plus_w": round(nuc_x_plus_w, 6),
    }


def main() -> None:
    results = verify_thresholds_and_lemma6()
    summary = {
        "concept": "AIMech:EscapeThroughAMeshNullSpacePhaseTransitionThresholdsForNuclearNormAndPSDTraceMinimization",
        "source": "Oymak & Hassibi (2010), arXiv:1011.6326v1",
        "results": results,
        "all_assertions_passed": True,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
