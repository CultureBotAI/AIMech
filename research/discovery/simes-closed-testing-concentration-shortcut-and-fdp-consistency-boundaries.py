#!/usr/bin/env python3
"""Constructed boundary & numerical verification for Round 210:

AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
Primary source: Jelle J. Goeman, Rosa J. Meijer, Thijmen J. P. Krebs, & Aldo
Solari (2019), "Simultaneous control of all false discovery proportions in
large-scale multiple hypothesis testing", Biometrika 106(4):841-856
(arXiv:1611.06739v2, DOI:10.1093/biomet/asz041).
"""

from __future__ import annotations

import json
import math
import random


def simes_rejects(p_subset: list[float], alpha: float) -> bool:
    """Return True iff Simes local test rejects H_I at level alpha (Eq. 4)."""
    k = len(p_subset)
    if k == 0:
        return False
    sp = sorted(p_subset)
    for i, p_val in enumerate(sp, start=1):
        if k * p_val <= i * alpha + 1e-15:
            return True
    return False


def exhaustive_closed_testing(
    p_vals: list[float], alpha: float
) -> tuple[set[int], set[int]]:
    """Return bitmask sets (U_alpha, X_alpha) for m <= 12 hypotheses."""
    m = len(p_vals)
    u_alpha: set[int] = set()
    for mask in range(1, 1 << m):
        sub_p = [p_vals[j] for j in range(m) if (mask >> j) & 1]
        if simes_rejects(sub_p, alpha):
            u_alpha.add(mask)
    x_alpha: set[int] = set()
    for mask in range(1, 1 << m):
        ok = True
        for sup in range(1, 1 << m):
            if (sup & mask) == mask and sup not in u_alpha:
                ok = False
                break
        if ok:
            x_alpha.add(mask)
    return u_alpha, x_alpha


def compute_h_alpha(p_vals: list[float], alpha: float) -> int:
    """Compute Hommel's h_alpha = max{0 <= i <= m : K_i not in U_alpha} via bisection (p. 8)."""
    m = len(p_vals)
    sp = sorted(p_vals)
    lo, hi = 0, m
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if not simes_rejects(sp[m - mid :], alpha):
            lo = mid
        else:
            hi = mid - 1
    return lo


def compute_z_alpha(p_vals: list[float], alpha: float, h: int) -> int:
    """Compute concentration threshold index z_alpha (Lemma 3, p. 8)."""
    m = len(p_vals)
    if h == m:
        return 0
    sp = sorted(p_vals)
    for i in range(m - h, m + 1):
        if h * sp[i - 1] <= (i - m + h + 1) * alpha + 1e-15:
            return i
    raise RuntimeError("z_alpha not found")


def compute_b_alpha(p_vals: list[float], alpha: float) -> int:
    """Compute Benjamini-Hochberg threshold index b_alpha (Eq. 11, p. 9)."""
    m = len(p_vals)
    sp = sorted(p_vals)
    b = 0
    for i in range(1, m + 1):
        if m * sp[i - 1] <= i * alpha + 1e-15:
            b = i
    return b


def shortcut_d_alpha(
    p_vals: list[float], subset_indices: list[int], alpha: float, h: int
) -> int:
    """Theorem 1 exact shortcut for d_alpha(S) (Eq. 10, p. 8) in O(|S| log |S|) time."""
    k = len(subset_indices)
    if k == 0 or h == 0:
        return k
    # As shown on p. 8: t_alpha(S) depends on p_i only through c_i = ceil(h * p_i / alpha)
    counts = [0] * (k + 2)
    for idx in subset_indices:
        hp = h * p_vals[idx]
        if hp <= 0.0:
            c_i = 1
        else:
            c_i = max(1, int(math.ceil((hp - 1e-15) / alpha)))
        if c_i <= k:
            counts[c_i] += 1
    best = 0
    running = 0
    for u in range(1, k + 1):
        running += counts[u]
        val = 1 - u + running
        if val > best:
            best = val
    return best


def verify_section_3_figure_1() -> dict[str, object]:
    """Verify Section 3 Figure 1 non-consonant example and Goeman-Solari (2011) failure."""
    alpha = 0.05
    # alpha/2 = 0.025 < p1 <= p2 <= p3 <= 2*alpha/3 = 0.0333... and p4 > alpha
    p_vals = [0.026, 0.030, 0.032, 0.200]
    m = 4
    u_alpha, x_alpha = exhaustive_closed_testing(p_vals, alpha)

    non_rejected_local = []
    for mask in range(1, 1 << m):
        if mask not in u_alpha:
            elems = [j + 1 for j in range(m) if (mask >> j) & 1]
            non_rejected_local.append(elems)
    assert sorted(non_rejected_local) == [[1, 4], [2, 4], [3, 4], [4]]

    # Elementary rejected set R_alpha
    r_alpha = [j + 1 for j in range(m) if (1 << j) in x_alpha]
    assert r_alpha == []

    # Check non-consonant pairs {1,2}, {1,3}, {2,3} are in X_alpha
    for pair in [(0, 1), (0, 2), (1, 2)]:
        mask = (1 << pair[0]) | (1 << pair[1])
        assert mask in x_alpha

    # Exact t_alpha(S) on L3 = {1,2,3} and L2 = {1,2}
    h = compute_h_alpha(p_vals, alpha)
    assert h == 2
    d_l3 = shortcut_d_alpha(p_vals, [0, 1, 2], alpha, h)
    t_l3 = 3 - d_l3
    assert t_l3 == 1  # whereas |S \ R_alpha| = 3

    d_l2 = shortcut_d_alpha(p_vals, [0, 1], alpha, h)
    t_l2 = 2 - d_l2
    assert t_l2 == 1

    # Goeman-Solari (2011) approximate shortcut on L_j:
    # t_alpha(L_j) <= j - d if there is d <= i <= j such that (m - d + 1)*p_{(i)} <= (i - d + 1)*alpha
    def gs2011_t_bound(j: int) -> int:
        best_d = 0
        for d in range(1, j + 1):
            if any(
                (m - d + 1) * p_vals[i - 1] <= (i - d + 1) * alpha + 1e-15
                for i in range(d, j + 1)
            ):
                best_d = d
        return j - best_d

    gs2011_l3 = gs2011_t_bound(3)
    gs2011_l2 = gs2011_t_bound(2)
    assert gs2011_l3 == 1
    assert gs2011_l2 == 2  # Strictly worse than exact t_alpha(L_2) = 1!

    return {
        "h_alpha": h,
        "non_rejected_local_sets": sorted(non_rejected_local),
        "r_alpha_elementary": r_alpha,
        "t_alpha_L3_exact": t_l3,
        "trivial_fwer_bound_L3": 3,
        "t_alpha_L2_exact": t_l2,
        "gs2011_shortcut_L2": gs2011_l2,
    }


def verify_sections_4_and_5_exhaustive() -> dict[str, object]:
    """Verify Lemmas 1-5 and Theorem 1 across all 256 subsets of an 8-hypothesis problem."""
    alpha = 0.05
    # 8 sorted p-values with non-consonant discoveries, z_alpha < b_alpha
    p_vals = [0.004, 0.011, 0.014, 0.019, 0.024, 0.029, 0.180, 0.450]
    m = len(p_vals)
    u_alpha, x_alpha = exhaustive_closed_testing(p_vals, alpha)

    h = compute_h_alpha(p_vals, alpha)
    z = compute_z_alpha(p_vals, alpha, h)
    b = compute_b_alpha(p_vals, alpha)
    pi_hat = h / m

    # Lemma 1: |I| > h implies I in X_alpha, and t_alpha({1..m}) = h
    for mask in range(1, 1 << m):
        sz = mask.bit_count()
        if sz > h:
            assert mask in x_alpha

    # Lemma 2: I in X_alpha iff exists 1 <= i <= |I| s.t. h * p_{(i:I)} <= i * alpha
    for mask in range(1, 1 << m):
        sub_p = sorted(p_vals[j] for j in range(m) if (mask >> j) & 1)
        lemma2_cond = any(
            h * sub_p[i - 1] <= i * alpha + 1e-15 for i in range(1, len(sub_p) + 1)
        )
        assert (mask in x_alpha) == lemma2_cond

    # Elementary Hommel set R_alpha, concentration set Z_alpha, BH set B_alpha
    r_set = {j for j in range(m) if (1 << j) in x_alpha}
    z_set = set(range(z))
    b_set = set(range(b))
    assert (m - h) <= z <= b

    u_max_lemma3 = 0 if h == m else (z - m + h + 1)

    # Exhaustively verify Theorem 1, Lemma 3, and Lemma 4 across all 2^m = 256 subsets
    non_consonant_strict_subsets = 0
    for mask in range(0, 1 << m):
        s_indices = [j for j in range(m) if (mask >> j) & 1]
        k = len(s_indices)
        # Exact definition Eq. (2): t_alpha(S) = max{|I| : I subseteq S, I not in X_alpha}
        t_exact = 0
        for sub in range(1, 1 << m):
            if (sub & mask) == sub and sub not in x_alpha:
                sz = sub.bit_count()
                if sz > t_exact:
                    t_exact = sz
        d_exact = k - t_exact

        # Theorem 1 shortcut Eq. (10)
        d_thm1 = shortcut_d_alpha(p_vals, s_indices, alpha, h)
        assert d_thm1 == d_exact

        # Lemma 3 restricted u-range 1 <= u <= min(|S|, z - m + h + 1)
        d_lemma3 = 0
        for u in range(1, min(k, u_max_lemma3) + 1):
            cnt = sum(
                1 for idx in s_indices if h * p_vals[idx] <= u * alpha + 1e-15
            )
            val = 1 - u + cnt
            if val > d_lemma3:
                d_lemma3 = val
        assert d_lemma3 == d_exact

        # Lemma 4.1: d_alpha(S) == d_alpha(S cap Z_alpha)
        s_cap_z = [idx for idx in s_indices if idx in z_set]
        d_cap_z = shortcut_d_alpha(p_vals, s_cap_z, alpha, h)
        assert d_exact == d_cap_z

        # Sandwich inequality (p. 9): |S cap R| <= d_alpha(S) <= |S cap Z| <= |S cap B|
        s_cap_r_len = sum(1 for idx in s_indices if idx in r_set)
        s_cap_b_len = sum(1 for idx in s_indices if idx in b_set)
        assert s_cap_r_len <= d_exact <= len(s_cap_z) <= s_cap_b_len
        if d_exact > s_cap_r_len:
            non_consonant_strict_subsets += 1

    # Lemma 4.2 minimality of Z_alpha and Lemma 4.3 d_alpha(Z_alpha) = m - h
    d_z = shortcut_d_alpha(p_vals, list(z_set), alpha, h)
    assert d_z == m - h
    for drop_idx in z_set:
        smaller_y = [idx for idx in z_set if idx != drop_idx]
        assert shortcut_d_alpha(p_vals, smaller_y, alpha, h) < m - h

    # Lemma 5: For any q in [0, 1], alpha * q_alpha(B_q) <= pi_hat_alpha * q
    for q_int in range(1, 20):
        q = q_int * 0.025
        b_q = compute_b_alpha(p_vals, q)
        if b_q == 0:
            q_alpha_bq = 0.0
        else:
            d_bq = shortcut_d_alpha(p_vals, list(range(b_q)), alpha, h)
            q_alpha_bq = (b_q - d_bq) / b_q
        assert alpha * q_alpha_bq <= pi_hat * q + 1e-12

    # Median-unbiased bound Eq. (12): q_{1/2}(B_q) <= 2 * q * pi_hat_{1/2}
    h_half = compute_h_alpha(p_vals, 0.5)
    pi_hat_half = h_half / m
    b_005 = compute_b_alpha(p_vals, 0.05)
    d_half_b005 = shortcut_d_alpha(p_vals, list(range(b_005)), 0.5, h_half)
    q_half_b005 = (b_005 - d_half_b005) / b_005
    assert q_half_b005 <= 2.0 * 0.05 * pi_hat_half + 1e-12

    return {
        "m": m,
        "h_alpha": h,
        "pi_hat_alpha": pi_hat,
        "r_alpha_size": len(r_set),
        "z_alpha": z,
        "b_alpha": b,
        "d_alpha_Z": d_z,
        "q_alpha_B_alpha": round((b - (m - h)) / b, 6),
        "verified_subsets": 1 << m,
        "non_consonant_strict_subsets": non_consonant_strict_subsets,
        "q_half_B_005": round(q_half_b005, 6),
        "two_q_pi_hat_half": round(2.0 * 0.05 * pi_hat_half, 6),
    }


def norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def norm_ppf(p: float) -> float:
    """Bisection inverse normal CDF on (0, 1)."""
    lo, hi = -10.0, 10.0
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if norm_cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def verify_sections_6_and_7_asymptotics() -> dict[str, object]:
    """Verify Lemma 6, Theorem 2, and Theorem 3 double-limit consistency."""
    alpha = 0.05
    gamma = 0.70
    # Fixed sample size n = 16 with effect delta = 0.625 => signal mu = sqrt(n)*delta = 2.50
    mu_fixed = 2.50

    def mix_cdf(x: float, mu: float) -> float:
        if x <= 0.0:
            return 0.0
        if x >= 1.0:
            return 1.0
        z_x = norm_ppf(1.0 - x)
        alt_p = 1.0 - norm_cdf(z_x - mu)
        return gamma * x + (1.0 - gamma) * alt_p

    # Theoretical bar_pi_alpha from Lemma 6: inf_{0 <= x < 1} (1 - P(x*alpha)) / (1 - x)
    pi_bar_alpha = min(
        (1.0 - mix_cdf((k / 2000.0) * alpha, mu_fixed)) / (1.0 - (k / 2000.0))
        for k in range(2000)
    )
    assert gamma <= pi_bar_alpha < 1.0

    # Simulate m = 100 and m = 4000 under Efron's model at fixed mu = 2.50
    rng = random.Random(20261018)
    p_m100 = [rng.random() for _ in range(70)] + [
        max(1e-15, 1.0 - norm_cdf(rng.gauss(mu_fixed, 1.0))) for _ in range(30)
    ]
    h_m100 = compute_h_alpha(p_m100, alpha)
    r_frac_m100 = sum(1 for p in p_m100 if h_m100 * p <= alpha) / 100.0

    m_large = 4000
    n_null = int(round(gamma * m_large))
    p_sim: list[float] = []
    for _ in range(n_null):
        p_sim.append(rng.random())
    for _ in range(m_large - n_null):
        z_stat = rng.gauss(mu_fixed, 1.0)
        p_sim.append(max(1e-15, 1.0 - norm_cdf(z_stat)))

    h_sim = compute_h_alpha(p_sim, alpha)
    pi_hat_sim = h_sim / m_large
    assert abs(pi_hat_sim - pi_bar_alpha) < 0.03

    # Equation (14): Hommel FWER rejections |R_alpha| / m decays toward 0 as m grows
    r_sim_count = sum(1 for p in p_sim if h_sim * p <= alpha)
    r_sim_frac = r_sim_count / m_large
    assert r_sim_frac < r_frac_m100
    assert r_sim_frac < 0.02

    # Theorem 2: J_m = B_{tilde_alpha_m} at target q = 0.25 has non-vanishing size |J_m|/m
    q_target = 0.25
    alpha_tilde = q_target * alpha * pi_bar_alpha / pi_hat_sim
    b_jm = compute_b_alpha(p_sim, alpha_tilde)
    sp_sim = sorted(p_sim)
    d_jm = shortcut_d_alpha(sp_sim, list(range(b_jm)), alpha, h_sim)
    q_alpha_jm = (b_jm - d_jm) / b_jm if b_jm > 0 else 0.0
    assert b_jm / m_large > 0.08 > r_sim_frac
    assert q_alpha_jm <= pi_bar_alpha * q_target + 1e-9

    # Theorem 3: As both (m, n) -> infinity, q_{alpha,m,n}(S_m) -> gamma_S
    # Let S_m have relative size c = 0.50 and true null proportion gamma_S = 0.60
    c_rel = 0.50
    gamma_s = 0.60
    q_estimates: dict[str, float] = {}
    bh_fractions: dict[str, float] = {}
    for m_val, n_val in [(200, 16), (1000, 36), (4000, 81)]:
        mu_n = math.sqrt(n_val) * 0.65
        s_len = int(round(c_rel * m_val))
        s_null = int(round(gamma_s * s_len))
        s_alt = s_len - s_null

        comp_len = m_val - s_len
        # Overall null proportion gamma = 0.70 => complement has null proportion 0.80
        comp_null = int(round(0.80 * comp_len))
        comp_alt = comp_len - comp_null

        p_all: list[float] = []
        s_idx: list[int] = []
        # Deterministic stratified quantiles for zero-variance reproducible limit check
        for k_i in range(s_null):
            s_idx.append(len(p_all))
            p_all.append((k_i + 0.5) / s_null)
        for k_i in range(s_alt):
            s_idx.append(len(p_all))
            z_quant = norm_ppf((k_i + 0.5) / s_alt) + mu_n
            p_all.append(max(1e-15, 1.0 - norm_cdf(z_quant)))
        for k_i in range(comp_null):
            p_all.append((k_i + 0.5) / comp_null)
        for k_i in range(comp_alt):
            z_quant = norm_ppf((k_i + 0.5) / comp_alt) + mu_n
            p_all.append(max(1e-15, 1.0 - norm_cdf(z_quant)))

        h_mn = compute_h_alpha(p_all, alpha)
        d_sm = shortcut_d_alpha(p_all, s_idx, alpha, h_mn)
        q_sm = (s_len - d_sm) / s_len
        b_mn = compute_b_alpha(p_all, alpha)
        q_estimates[f"m={m_val},n={n_val}"] = round(q_sm, 6)
        bh_fractions[f"m={m_val},n={n_val}"] = round(b_mn / m_val, 6)

    # Check convergence to gamma_S = 0.60 and BH limit (1 - gamma)/(1 - alpha*gamma)
    bh_theoretical_limit = (1.0 - gamma) / (1.0 - alpha * gamma)
    assert abs(q_estimates["m=4000,n=81"] - gamma_s) < 0.015
    assert abs(bh_fractions["m=4000,n=81"] - bh_theoretical_limit) < 0.005

    return {
        "gamma": gamma,
        "pi_bar_alpha_n25": round(pi_bar_alpha, 6),
        "pi_hat_sim_m4000": round(pi_hat_sim, 6),
        "hommel_fwer_fraction_m4000": round(r_sim_frac, 6),
        "theorem_2_jm_fraction_m4000": round(b_jm / m_large, 6),
        "theorem_2_q_alpha_jm": round(q_alpha_jm, 6),
        "theorem_2_upper_bound": round(pi_bar_alpha * q_target, 6),
        "theorem_3_gamma_S": gamma_s,
        "theorem_3_q_alpha_S_m_trajectory": q_estimates,
        "bh_rejection_fraction_trajectory": bh_fractions,
        "bh_theoretical_limit": round(bh_theoretical_limit, 6),
    }


def main() -> int:
    s3 = verify_section_3_figure_1()
    s45 = verify_sections_4_and_5_exhaustive()
    s67 = verify_sections_6_and_7_asymptotics()

    result = {
        "concept_id": "AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency",
        "primary_source": (
            "Goeman, Meijer, Krebs, & Solari (2019), Biometrika 106(4):841-856 "
            "(arXiv:1611.06739v2, DOI:10.1093/biomet/asz041)"
        ),
        "section_3_figure_1_non_consonant_and_gs2011_gap": s3,
        "sections_4_and_5_exact_shortcut_and_concentration_set": s45,
        "sections_6_and_7_simes_detectability_and_double_limit_consistency": s67,
        "all_assertions_passed": True,
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
