#!/usr/bin/env python3
"""Constructed boundary and negation-test verification for
AIMech:StepUpDownLeastFavorableConfigurationFDRBounds
(Blanchard, Dickhaus, Roquain, & Villers 2014, Statistica Sinica 24(1):1-23,
arXiv:1108.5262v1, DOI:10.5705/ss.2011.205).
"""

from __future__ import annotations

import json
import math
from typing import Callable


def steck_one_pop(t_seq: list[float]) -> float:
    """Standard one-population Steck's recursion (Equation (16)):
    Psi_k(t_1, ..., t_k) = P(U_(1) <= t_1, ..., U_(k) <= t_k)
    for i.i.d. Uniform(0,1) variables.
    """
    k = len(t_seq)
    if k == 0:
        return 1.0
    psi = [0.0] * (k + 1)
    psi[0] = 1.0
    for m in range(1, k + 1):
        tm = max(0.0, min(1.0, t_seq[m - 1]))
        if tm <= 0.0:
            psi[m] = 0.0
            continue
        val = tm ** m
        for j in range(0, m - 1):
            tj1 = max(0.0, min(1.0, t_seq[j]))
            diff = tm - tj1
            if diff > 0.0 and psi[j] != 0.0:
                val -= math.comb(m, j) * (diff ** (m - j)) * psi[j]
        psi[m] = max(0.0, val)
    return psi[k]


def steck_two_pop_table(
    t_seq: list[float],
    k0_max: int,
    cdf_f: Callable[[float], float],
) -> list[list[float]]:
    """Proposition 5.1 (Equation (18)): Two-population generalized Steck's recursion.
    Returns table `psi[j][j0] = Psi_{j, j0, F}(t_1, ..., t_j)` for 0 <= j <= len(t_seq)
    and 0 <= j0 <= min(j, k0_max).
    """
    k_total = len(t_seq)
    psi = [[0.0] * (k0_max + 1) for _ in range(k_total + 1)]
    psi[0][0] = 1.0
    for j in range(1, k_total + 1):
        tj = max(0.0, min(1.0, t_seq[j - 1]))
        ftj = max(0.0, min(1.0, cdf_f(tj)))
        for j0 in range(0, min(j, k0_max) + 1):
            j1 = j - j0
            term1 = (1.0 if j0 == 0 else (tj ** j0)) * (1.0 if j1 == 0 else (ftj ** j1))
            sub_sum = 0.0
            for r in range(0, j - 1):
                tr1 = max(0.0, min(1.0, t_seq[r]))
                ftr1 = max(0.0, min(1.0, cdf_f(tr1)))
                dt = max(0.0, tj - tr1)
                dft = max(0.0, ftj - ftr1)
                for r0 in range(max(0, r - j1), min(r, j0) + 1):
                    r1 = r - r0
                    if psi[r][r0] == 0.0:
                        continue
                    pow0 = 1.0 if (j0 - r0) == 0 else (dt ** (j0 - r0))
                    pow1 = 1.0 if (j1 - r1) == 0 else (dft ** (j1 - r1))
                    sub_sum += (
                        math.comb(j0, r0)
                        * math.comb(j1, r1)
                        * pow0
                        * pow1
                        * psi[r][r0]
                    )
            psi[j][j0] = max(0.0, term1 - sub_sum)
    return psi


def q_su_fm(
    t_seq: list[float],
    m: int,
    m0: int,
    cdf_f: Callable[[float], float],
    k: int,
    j: int,
) -> float:
    """Equation (21): Q_{m, m0, F}(t, k, j) = P(|SU(t) cap H0| = j, |SU(t)| = k)."""
    if j < max(0, k - m + m0) or j > min(m0, k):
        return 0.0
    tk = 0.0 if k == 0 else t_seq[k - 1]
    ftk = 0.0 if k == 0 else cdf_f(tk)
    p0 = 1.0 if j == 0 else (tk ** j)
    p1 = 1.0 if (k - j) == 0 else (ftk ** (k - j))
    if p0 == 0.0 or p1 == 0.0:
        return 0.0
    rev_t = [1.0 - t_seq[idx] for idx in range(m - 1, k - 1, -1)]
    cdf_bar = lambda u: 1.0 - cdf_f(1.0 - u)
    psi_tab = steck_two_pop_table(rev_t, m0 - j, cdf_bar)
    return (
        math.comb(m0, j)
        * math.comb(m - m0, k - j)
        * p0
        * p1
        * psi_tab[m - k][m0 - j]
    )


def q_tilde_sd_fm(
    t_seq: list[float],
    m: int,
    m0: int,
    cdf_f: Callable[[float], float],
    k: int,
    j: int,
) -> float:
    """Equation (22): tilde{Q}_{m, m0, F}(t, k, j) = P(|SD(t) cap H0| = j, |SD(t)| = k)."""
    if j < max(0, k - m + m0) or j > min(m0, k):
        return 0.0
    tk1 = 1.0 if k == m else t_seq[k]
    ftk1 = 1.0 if k == m else cdf_f(tk1)
    p0 = 1.0 if (m0 - j) == 0 else ((1.0 - tk1) ** (m0 - j))
    p1 = 1.0 if (m - m0 - k + j) == 0 else ((1.0 - ftk1) ** (m - m0 - k + j))
    if p0 == 0.0 or p1 == 0.0:
        return 0.0
    psi_tab = steck_two_pop_table(t_seq[:k], j, cdf_f)
    return (
        math.comb(m0, j)
        * math.comb(m - m0, k - j)
        * p0
        * p1
        * psi_tab[k][j]
    )


def exact_fdr_sud_fm(
    t_seq: list[float],
    lam: int,
    m: int,
    m0: int,
    cdf_f: Callable[[float], float],
) -> float:
    """Corollary 5.3(ii) (Equation (27)): Exact FDR(SUD_lambda(t)) in FM(m, m0, F)."""
    t_lam = t_seq[lam - 1]
    t_min = [min(t_lam, tj) for tj in t_seq]
    t_max = [max(t_lam, tj) for tj in t_seq]
    fdr = 0.0
    for k in range(1, lam):
        for j in range(max(0, k - m + m0), min(m0, k) + 1):
            if j > 0:
                fdr += (j / k) * q_su_fm(t_min, m, m0, cdf_f, k, j)
    for k in range(lam, m + 1):
        for j in range(max(0, k - m + m0), min(m0, k) + 1):
            if j > 0:
                fdr += (j / k) * q_tilde_sd_fm(t_max, m, m0, cdf_f, k, j)
    return fdr


def exact_fdr_sud_rm(
    t_seq: list[float],
    lam: int,
    m: int,
    pi0: float,
    cdf_f: Callable[[float], float],
) -> float:
    """Exact FDR(SUD_lambda(t)) in RM(m, pi0, F) via binomial conditioning over m0 ~ Bin(m, pi0)
    and cross-checked against Corollary 5.3(i) (Equation (26)).
    """
    total = 0.0
    for m0 in range(1, m + 1):
        prob_m0 = math.comb(m, m0) * (pi0 ** m0) * ((1.0 - pi0) ** (m - m0))
        total += prob_m0 * exact_fdr_sud_fm(t_seq, lam, m, m0, cdf_f)
    return total


def exact_fdr_sud_rm_eq26(
    t_seq: list[float],
    lam: int,
    m: int,
    pi0: float,
    cdf_f: Callable[[float], float],
) -> float:
    """Direct evaluation of Equation (26) using P_{m, pi0, F} (Eq. 19) and tilde{P}_{m, pi0, F} (Eq. 20)."""
    pi1 = 1.0 - pi0
    cdf_g = lambda u: pi0 * u + pi1 * cdf_f(u)
    t_lam = t_seq[lam - 1]
    t_min = [min(t_lam, tj) for tj in t_seq]
    t_max = [max(t_lam, tj) for tj in t_seq]

    fdr = 0.0
    for k in range(1, lam):
        tk = t_min[k - 1]
        ftk = cdf_f(tk)
        rev_g = [1.0 - cdf_g(t_min[idx]) for idx in range(m - 1, k - 1, -1)]
        psi_mk = steck_one_pop(rev_g)
        for j in range(1, k + 1):
            p0 = (pi0 * tk) ** j
            p1 = 1.0 if (k - j) == 0 else ((pi1 * ftk) ** (k - j))
            p_val = math.comb(m, j) * math.comb(m - j, k - j) * p0 * p1 * psi_mk
            fdr += (j / k) * p_val

    for k in range(lam, m + 1):
        tk1 = 1.0 if k == m else t_max[k]
        gtk1 = 1.0 if k == m else cdf_g(tk1)
        tail_factor = 1.0 if k == m else ((1.0 - gtk1) ** (m - k))
        psi_tab = steck_two_pop_table(t_max[:k], k, cdf_f)
        for j in range(1, k + 1):
            p0 = pi0 ** j
            p1 = 1.0 if (k - j) == 0 else (pi1 ** (k - j))
            p_tilde = (
                math.comb(m, j)
                * math.comb(m - j, k - j)
                * p0
                * p1
                * tail_factor
                * psi_tab[k][j]
            )
            fdr += (j / k) * p_tilde
    return fdr


def continuous_u_functional(
    ell: float,
    g_func: Callable[[float], float],
    rho_func: Callable[[float], float],
    grid_n: int = 10000,
) -> float:
    """Definition 4.2 (Equation (9)): Continuous SUD fixed-point functional U(ell, G)."""
    if g_func(rho_func(ell)) >= ell - 1e-12:
        for i in range(int(round(ell * grid_n)), grid_n + 1):
            u = i / grid_n
            if g_func(rho_func(u)) <= u + 1e-12:
                return u
        return 1.0
    else:
        for i in range(int(round(ell * grid_n)), -1, -1):
            u = i / grid_n
            if g_func(rho_func(u)) >= u - 1e-12:
                return u
        return 0.0


def main() -> None:
    # 1. Verify Proposition 5.1 & Theorem 5.2 / Corollary 5.3 consistency
    t_test = [0.05 * k / 6 for k in range(1, 7)]
    psi_1 = steck_one_pop(t_test)
    psi_2_same = steck_two_pop_table(t_test, 6, lambda u: u)[6][6]
    assert abs(psi_1 - psi_2_same) < 1e-15

    # Verify LSU (lambda = m) under Dirac-Uniform F == 1 equals alpha * m0 / m exactly
    m = 10
    m0 = 7
    alpha = 0.5
    t_linear = [alpha * k / m for k in range(1, m + 1)]
    cdf_du = lambda u: 1.0  # F(x) == 1 for x in [0, 1]
    cdf_unif = lambda u: u  # F(x) = x

    fdr_lsu_du_fm = exact_fdr_sud_fm(t_linear, m, m, m0, cdf_du)
    assert abs(fdr_lsu_du_fm - alpha * m0 / m) < 1e-12

    # 2. Verify Proposition 4.1 (Disproving Conjecture 3.2 for lambda in {4, 5, 6, 7})
    fm_fdr_unif = {}
    fm_fdr_du = {}
    rm_fdr_unif = {}
    rm_fdr_du = {}
    for lam in range(1, m + 1):
        fu = exact_fdr_sud_fm(t_linear, lam, m, m0, cdf_unif)
        fd = exact_fdr_sud_fm(t_linear, lam, m, m0, cdf_du)
        ru = exact_fdr_sud_rm(t_linear, lam, m, 0.7, cdf_unif)
        rd = exact_fdr_sud_rm(t_linear, lam, m, 0.7, cdf_du)
        ru_eq26 = exact_fdr_sud_rm_eq26(t_linear, lam, m, 0.7, cdf_unif)
        rd_eq26 = exact_fdr_sud_rm_eq26(t_linear, lam, m, 0.7, cdf_du)
        assert abs(ru - ru_eq26) < 1e-12
        assert abs(rd - rd_eq26) < 1e-12
        fm_fdr_unif[lam] = round(fu, 6)
        fm_fdr_du[lam] = round(fd, 6)
        rm_fdr_unif[lam] = round(ru, 6)
        rm_fdr_du[lam] = round(rd, 6)

    counterexample_lambdas_fm = [
        lam for lam in range(1, m + 1) if fm_fdr_unif[lam] > fm_fdr_du[lam] + 1e-9
    ]
    counterexample_lambdas_rm = [
        lam for lam in range(1, m + 1) if rm_fdr_unif[lam] > rm_fdr_du[lam] + 1e-9
    ]
    for lam in [4, 5, 6, 7]:
        assert lam in counterexample_lambdas_fm
        assert lam in counterexample_lambdas_rm
    assert counterexample_lambdas_fm == [3, 4, 5, 6, 7, 8, 9]
    assert counterexample_lambdas_rm == [3, 4, 5, 6, 7, 8, 9]
    # In FM(10, 7, F == 1), m - m0 = 3 alternatives are identically 0, so lambda=1,2,3,4 have identical FDR
    assert fm_fdr_du[1] == fm_fdr_du[2] == fm_fdr_du[3] == fm_fdr_du[4]

    # Verify monotonicity of FDR(SUD_lambda(t)) in lambda for concave F (Section 3)
    for lam in range(1, m):
        assert fm_fdr_unif[lam] <= fm_fdr_unif[lam + 1] + 1e-12
        assert fm_fdr_du[lam] <= fm_fdr_du[lam + 1] + 1e-12

    # 3. Verify Lemma 4.3 bracketing on Figure 6 example (m = 10, rho(x) = 0.5 x)
    # Construct p-values matching Figure 6 where hat_k/m = 0.7 for both lambda = 8 (SU) and lambda = 4 (SD),
    # while U(0.4, hat_G_m) = 0.4 < 0.7 = hat_k/m = U(0.4, (hat_G_m + 1/m) ^ 1) - 1/m.
    p_fig6 = [0.01, 0.03, 0.08, 0.18, 0.22, 0.27, 0.33, 0.45, 0.48, 0.49]
    # Check p_(k) vs t_k = 0.05 * k:
    # k=1: 0.01 <= 0.05; k=2: 0.03 <= 0.10; k=3: 0.08 <= 0.15; k=4: 0.18 <= 0.20 (with equality if p_4 = 0.20)
    p_fig6[3] = 0.20  # so hat_G_10(0.20) = 0.4 = 4/10, a fixed point at u = 0.4!
    # k=5: 0.22 <= 0.25; k=6: 0.27 <= 0.30; k=7: 0.33 <= 0.35; k=8: 0.45 > 0.40
    hat_g = lambda x: sum(1 for p in p_fig6 if p <= x) / m
    hat_g_plus = lambda x: min(1.0, hat_g(x) + 1.0 / m)
    rho_lin = lambda u: 0.5 * u

    # Discrete hat_k from Definition 2.1 (Equation (2))
    def discrete_sud_k_hat(p_ord: list[float], t_seq_in: list[float], lam_in: int) -> int:
        if p_ord[lam_in - 1] <= t_seq_in[lam_in - 1]:
            k_hat = lam_in
            for k_cand in range(lam_in + 1, len(p_ord) + 1):
                if p_ord[k_cand - 1] <= t_seq_in[k_cand - 1]:
                    k_hat = k_cand
                else:
                    break
            return k_hat
        else:
            k_hat = 0
            for k_cand in range(1, lam_in + 1):
                if p_ord[k_cand - 1] <= t_seq_in[k_cand - 1]:
                    k_hat = k_cand
            return k_hat

    k_hat_lam8 = discrete_sud_k_hat(p_fig6, t_linear, 8)
    k_hat_lam4 = discrete_sud_k_hat(p_fig6, t_linear, 4)
    u_lam8_lo = continuous_u_functional(0.8, hat_g, rho_lin, grid_n=1000)
    u_lam4_lo = continuous_u_functional(0.4, hat_g, rho_lin, grid_n=1000)
    u_lam4_hi = continuous_u_functional(0.4, hat_g_plus, rho_lin, grid_n=1000)

    assert k_hat_lam8 == 7 and abs(u_lam8_lo - 0.7) < 1e-9
    assert k_hat_lam4 == 7 and abs(u_lam4_lo - 0.4) < 1e-9 and abs(u_lam4_hi - 0.8) < 1e-9
    assert u_lam4_lo <= k_hat_lam4 / m <= u_lam4_hi

    # 4. Verify Theorem 4.4 & Corollary 4.5 non-asymptotic bound and O(sqrt((log m)/m)) rate
    zeta = 0.7
    alpha_bound = 0.2
    rate_table = {}
    for m_val in [100, 1000, 10000, 100000]:
        m0_val = int(zeta * m_val)
        nu_val = max(abs(m0_val / m_val - zeta), abs((m0_val - 1) / m_val - zeta))
        # Equation (37): 2 * (1 - nu/zeta) * (delta_m - nu - 1/m)^2 = (log m)/m
        factor = 2.0 * max(1e-12, 1.0 - nu_val / zeta)
        delta_m = nu_val + (1.0 / m_val) + math.sqrt(math.log(m_val) / (m_val * factor))
        # Linear critical value bound from Example 1 (Section 4.2):
        lin_term1 = (2.0 * alpha_bound * delta_m) / (1.0 - zeta + delta_m)
        tail_term = (4.0 / (1.0 - zeta)) * (1.0 / m_val)
        eps_lin = (m0_val / m_val) * (lin_term1 + tail_term)
        scaled_ratio = eps_lin / math.sqrt(math.log(m_val) / m_val)
        rate_table[str(m_val)] = {
            "delta_m": round(delta_m, 6),
            "fdr_excess_upper_bound_linear": round(eps_lin, 6),
            "scaled_by_sqrt_log_m_over_m": round(scaled_ratio, 6),
        }
    # Confirm the upper bound decreases to 0 and the scaled ratio stabilizes to a finite constant
    assert rate_table["100000"]["fdr_excess_upper_bound_linear"] < rate_table["100"]["fdr_excess_upper_bound_linear"]
    assert 0.5 < rate_table["100000"]["scaled_by_sqrt_log_m_over_m"] < 2.0

    # 5. Verify Lemma B.1 (FDR(SD) > FDR(SU) in extreme alternative F(x) = 1{x >= 1})
    t0_extreme = 0.20
    thresh_crit = 1.0 - ((1.0 - m0 / m) ** (1.0 / m0))
    fdr_sd_extreme = 1.0 - ((1.0 - t0_extreme) ** m0)
    fdr_su_extreme = m0 / m
    assert t0_extreme > thresh_crit
    assert fdr_sd_extreme > fdr_su_extreme

    summary = {
        "concept_id": "AIMech:StepUpDownLeastFavorableConfigurationFDRBounds",
        "primary_source": "Blanchard, Dickhaus, Roquain, & Villers (2014), Statistica Sinica 24(1):1-23 (arXiv:1108.5262v1, DOI:10.5705/ss.2011.205)",
        "proposition_4_1_counterexample": {
            "m": m,
            "m0": m0,
            "alpha": alpha,
            "fm_fdr_uniform_alt": fm_fdr_unif,
            "fm_fdr_dirac_uniform": fm_fdr_du,
            "rm_fdr_uniform_alt": rm_fdr_unif,
            "rm_fdr_dirac_uniform": rm_fdr_du,
            "counterexample_lambdas_fm": counterexample_lambdas_fm,
            "counterexample_lambdas_rm": counterexample_lambdas_rm,
        },
        "lemma_4_3_figure_6_bracketing": {
            "k_hat_over_m_lam8": k_hat_lam8 / m,
            "u_lam8_lower": u_lam8_lo,
            "k_hat_over_m_lam4": k_hat_lam4 / m,
            "u_lam4_lower": u_lam4_lo,
            "u_lam4_upper": u_lam4_hi,
        },
        "theorem_4_4_and_corollary_4_5_rates": rate_table,
        "lemma_b_1_extreme_sd_exceeds_su": {
            "t0": t0_extreme,
            "critical_t0": round(thresh_crit, 6),
            "fdr_sd": round(fdr_sd_extreme, 6),
            "fdr_su": round(fdr_su_extreme, 6),
        },
        "all_assertions_passed": True,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
