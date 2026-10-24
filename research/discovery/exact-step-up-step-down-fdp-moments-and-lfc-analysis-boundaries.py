#!/usr/bin/env python3
"""Constructed boundary and numerical verification for Round 204:
AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis
Primary source: Etienne Roquain & Fanny Villers (2011),
"Exact calculations for false discovery proportion with application to least
favorable configurations", Annals of Statistics 39(1):584-612
(arXiv:1002.2845v2, DOI:10.1214/10-AOS847).

Verifies:
1. Theorem 3.1 (Eq. 11-14): Conditional binomial distribution of false rejections
   |H_0 cap SU(t)| given |SU(t)| = k ~ Binom(k, pi_0 * t_k / G(t_k)) under the
   independent mixture model P_bar^I_{(pi_0, F_1)}, and the exact s-th moment formula
   E[FDP(SU(t))^s] using Stirling numbers of the second kind {s \\atop ell} (Eq. 13),
   demonstrating that omitting {3 \\atop 2} = 3 (Ferreira & Zwinderman 2006) produces
   an erroneous third moment for s = 3.
2. Theorem 3.2 & Eq. (16)-(21): Non-binomial conditional law of |H_0 cap SD(t)|
   given |SD(t)| = k under nonlinear concave F_1(u) = sqrt(u), and the exact step-down
   FDR formula (Eq. 20) and Dirac-uniform linear step-down formula (Eq. 21) via
   Finner-Roters Lemma 2.1 (Eq. 7).
3. Proposition 3.6 & Section 4.1.2 (Eq. 25-26): Two-hypothesis (m = 2, m_0 = 1)
   negatively correlated Gaussian counterexample (rho -> -1^-, mu = z_1 + z_2)
   where FDR(LSU) = 3*alpha/4 = alpha*(m_0/m)*(1 + 1/2), attaining the full
   Benjamini-Yekutieli bound and exceeding the Dirac-uniform value alpha/2.
4. Theorem 4.1 & Section 4.1.1 (Eq. 24, 34): Condition (A) nondecreasing sequence
   k -> Q_k(t) and exact recursion S_{m,k} = a_{m,k} + b_{m,k}*S_{m-1,k} for linear
   step-down (LSD), plus the concave threshold counterexample t_k = 0.9*(k/m)^{9/10}
   where the LFC over concave F_1 is F_1 == 1 for SD(t) but F_1(x) = x for SU(t).
5. Theorem 4.3 & Section 6.5 (Eq. 28-30, 35): Exact closed-form minimum and maximum
   of Var[FDP(LSU)] over F_1 in F, verifying both exact agreement with Theorem 3.1
   at small m and the sparse regime benchmark (m = 10000, alpha = 0.05, 1 - pi_0 = 0.01)
   where min SD(FDP(LSU)) ~= 0.0217.
"""

from __future__ import annotations

import json
import math


def psi_steck(b_vec: list[float]) -> float:
    """Computes Psi_k(b_1, ..., b_k) = P(U_(1) <= b_1, ..., U_(k) <= b_k)
    via Steck's recursion (Eq. 6).
    """
    k = len(b_vec)
    psi = [0.0] * (k + 1)
    psi[0] = 1.0
    for r in range(1, k + 1):
        br = b_vec[r - 1]
        if br <= 0.0:
            psi[r] = 0.0
            continue
        val = br ** r
        for j in range(0, r - 1):
            diff = br - b_vec[j]
            if diff > 0.0:
                val -= math.comb(r, j) * (diff ** (r - j)) * psi[j]
        psi[r] = max(0.0, min(1.0, val))
    return psi[k]


def d_su_dist(b_vec: list[float]) -> list[float]:
    """Computes D_m(b, k) = P(|SU(b)| = k) for k = 0, ..., m using Eq. (8):
    D_m(b, k) = comb(m, k) * (b_k)^k * Psi_{m-k}(1 - b_m, ..., 1 - b_{k+1}).
    """
    m = len(b_vec)
    out = [0.0] * (m + 1)
    for k in range(0, m + 1):
        bk_pow = 1.0 if k == 0 else (b_vec[k - 1] ** k)
        rem_args = [1.0 - b_vec[m - 1 - j] for j in range(m - k)]
        psi_rem = psi_steck(rem_args)
        out[k] = math.comb(m, k) * bk_pow * psi_rem
    return out


def d_tilde_sd_dist(b_vec: list[float]) -> list[float]:
    """Computes D_tilde_m(b, k) = P(|SD(b)| = k) for k = 0, ..., m using Eq. (9) & (19):
    D_tilde_m(b, k) = comb(m, k) * Psi_k(b_1, ..., b_k) * (1 - b_{k+1})^{m-k}
    with Psi_0(.) = 1 and b_{m+1} = 1.
    """
    m = len(b_vec)
    out = [0.0] * (m + 1)
    for k in range(0, m + 1):
        psi_k = psi_steck(b_vec[:k])
        rem_pow = 1.0 if k == m else ((1.0 - b_vec[k]) ** (m - k))
        out[k] = math.comb(m, k) * psi_k * rem_pow
    return out


def stirling2(n: int, k: int) -> int:
    """Stirling numbers of the second kind {n \\atop k}."""
    if n == 0 and k == 0:
        return 1
    if n == 0 or k <= 0 or k > n:
        return 0
    return k * stirling2(n - 1, k) + stirling2(n - 1, k - 1)


def su_fdp_moment_thm31(t_vec: list[float], pi0: float, f1_vals: list[float], s: int) -> float:
    """Computes E[FDP(SU(t), H)^s] via Theorem 3.1 Eq. (13)."""
    m = len(t_vec)
    g_vec = [pi0 * t_vec[j] + (1.0 - pi0) * f1_vals[j] for j in range(m)]
    total = 0.0
    for ell in range(1, min(s, m) + 1):
        falling = math.factorial(m) // math.factorial(m - ell)
        st = stirling2(s, ell)
        sub_g = g_vec[ell:]
        d_sub = d_su_dist(sub_g)
        inner = 0.0
        for k in range(ell, m + 1):
            inner += ((t_vec[k - 1] ** ell) / (k ** s)) * d_sub[k - ell]
        total += falling * st * (pi0 ** ell) * inner
    return total


def su_fdp_moment_direct_from_cond_binomial(
    t_vec: list[float], pi0: float, f1_vals: list[float], s: int
) -> float:
    """Computes E[FDP(SU(t), H)^s] directly from the conditional binomial law
    V | (|SU(t)| = k) ~ Binom(k, pi_0 * t_k / G(t_k)) of Theorem 3.1 Eq. (11).
    """
    m = len(t_vec)
    g_vec = [pi0 * t_vec[j] + (1.0 - pi0) * f1_vals[j] for j in range(m)]
    d_full = d_su_dist(g_vec)
    total = 0.0
    for k in range(1, m + 1):
        pk = d_full[k]
        if pk <= 0.0:
            continue
        p_bin = (pi0 * t_vec[k - 1]) / g_vec[k - 1]
        ev_s = 0.0
        for v in range(1, k + 1):
            prob_v = math.comb(k, v) * (p_bin ** v) * ((1.0 - p_bin) ** (k - v))
            ev_s += ((v / k) ** s) * prob_v
        total += pk * ev_s
    return total


def sd_fdr_thm32_eq20(t_vec: list[float], pi0: float, f1_vals: list[float]) -> float:
    """Computes FDR(SD(t)) for any alternative cdf values f1_vals = [F_1(t_1), ..., F_1(t_m)]
    via Theorem 3.2 Eq. (20):
    FDR(SD(t)) = pi_0 * m * sum_{k=1}^m (t_k / k) * D_tilde_{m-1}([G(t_j)]_{1<=j<=m-1}, k-1)
                 * sum_{i=0}^{m-k} (k / (k + i)) * D_tilde_{m-k}([(G(t_{j+k}) - G(t_k))/(1 - G(t_k))]_{1<=j<=m-k}, i).
    """
    m = len(t_vec)
    g_vec = [pi0 * t_vec[j] + (1.0 - pi0) * f1_vals[j] for j in range(m)]
    d_tilde_m1 = d_tilde_sd_dist(g_vec[: m - 1])
    total = 0.0
    for k in range(1, m + 1):
        gk = g_vec[k - 1]
        if gk >= 1.0:
            inner = 1.0 if k == m else 0.0
        else:
            cond_g = [(g_vec[j + k - 1] - gk) / (1.0 - gk) for j in range(1, m - k + 1)]
            d_tilde_mk = d_tilde_sd_dist(cond_g)
            inner = sum((k / (k + i)) * d_tilde_mk[i] for i in range(m - k + 1))
        total += (t_vec[k - 1] / k) * d_tilde_m1[k - 1] * inner
    return pi0 * m * total


def lsd_fdr_dirac_uniform_finner_roters_eq21(m: int, pi0: float, alpha: float) -> float:
    """Computes FDR(LSD) in the Dirac-uniform model F_1 == 1 using the closed-form
    Finner-Roters expansion in Eq. (21).
    """
    pi1 = 1.0 - pi0
    total = 0.0
    for k in range(1, m + 1):
        # First factor: D_tilde_{m-1}([G(t_j)]_{1<=j<=m-1}, k-1) via Lemma 2.1
        # G(t_j) = pi1 + pi0 * alpha * j / m
        if k == 1:
            psi_k1 = 1.0
        else:
            psi_k1 = (pi1 + pi0 * alpha / m) * ((pi1 + pi0 * alpha * k / m) ** (k - 2))
        d_m1_k1 = math.comb(m - 1, k - 1) * psi_k1 * ((pi0 * (1.0 - alpha * k / m)) ** (m - k))

        # Second factor: sum_{i=0}^{m-k} (k/(k+i)) * D_tilde_{m-k}([(alpha*j/m)/(1 - alpha*k/m)]_{1<=j<=m-k}, i)
        # By Lemma 2.1 with nu_1 = 0, nu_2 = (alpha/m)/(1 - alpha*k/m),
        # Psi_i(nu_2, ..., i*nu_2) = nu_2 * ((i+1)*nu_2)^{i-1} = (i+1)^{i-1} * nu_2^i!
        inner = 0.0
        denom_k = 1.0 - alpha * k / m
        nu2 = (alpha / m) / denom_k
        for i in range(0, m - k + 1):
            psi_i = 1.0 if i == 0 else ((i + 1) ** (i - 1)) * (nu2 ** i)
            rem_i = 1.0 if i == m - k else ((1.0 - (i + 1) * nu2) ** (m - k - i))
            d_mk_i = math.comb(m - k, i) * psi_i * rem_i
            inner += (k / (k + i)) * d_mk_i

        total += d_m1_k1 * inner
    return alpha * pi0 * total


def condition_a_q_sequence(t_vec: list[float]) -> list[float]:
    """Computes the Condition (A) sequence Q_k(t) for k = 1, ..., m:
    Q_k(t) = (t_k / k) * sum_{i=0}^{m-k} (k / (k + i)) * D_tilde_{m-k}([(t_{j+k} - t_k)/(1 - t_k)]_{1<=j<=m-k}, i).
    Condition (A) holds iff k -> Q_k(t) is nondecreasing on {1, ..., m}.
    """
    m = len(t_vec)
    q_seq: list[float] = []
    for k in range(1, m + 1):
        tk = t_vec[k - 1]
        cond_t = [(t_vec[j + k - 1] - tk) / (1.0 - tk) for j in range(1, m - k + 1)]
        d_mk = d_tilde_sd_dist(cond_t)
        s_mk = sum((k / (k + i)) * d_mk[i] for i in range(m - k + 1))
        q_seq.append((tk / k) * s_mk)
    return q_seq


def lsd_s_mk_recursion_eq34(m: int, alpha: float) -> list[float]:
    """Computes S_{m,k} for k = 1, ..., m via the exact recursion in Section 6.4 Eq. (34):
    S_{r, r} = 1, and for 1 <= k <= r - 1:
    S_{r, k} = a_{r, k} + b_{r, k} * S_{r-1, k}
    where a_{r, k} = (k / r) * (1 - alpha * (r - k) / (r - alpha * k))
    and b_{r, k} = ((r - alpha) / r) * ((r - k) / (r - alpha * k)).
    """
    # Build table s_tab[r][k] for r = 1..m, k = 1..r
    s_tab: dict[tuple[int, int], float] = {}
    for r in range(1, m + 1):
        s_tab[(r, r)] = 1.0
        for k in range(1, r):
            denom = r - alpha * k
            a_rk = (k / r) * (1.0 - alpha * (r - k) / denom)
            b_rk = ((r - alpha) / r) * ((r - k) / denom)
            s_tab[(r, k)] = a_rk + b_rk * s_tab[(r - 1, k)]
    return [s_tab[(m, k)] for k in range(1, m + 1)]


def lsu_fdp_variance_bounds_thm43(m: int, pi0: float, alpha: float) -> dict[str, float]:
    """Computes the exact minimum and maximum of Var[FDP(LSU)] over F_1 in F
    from Theorem 4.3 & Section 6.5 (Eq. 28-30, 35):
    By Eq. (28), E[FDP(LSU)^2] = pi_0 * alpha * (1 - pi_0 * alpha)
      + pi_0 * alpha * (1 - pi_0 * alpha * (1 - 1/m)) * u_0 - pi_0 * alpha * (1 - pi_0 * alpha),
    wait: let's read Section 6.5 lines 266-270:
    u_0(beta, gamma) = E_0[(|SU((beta + (j-1)*gamma)_{1<=j<=m-1})| + 1)^{-1}]
                     = sum_{j=0}^{m-1} ((1 - (m - 1 - j)*gamma) / (j + 1)) * comb(m - 1, j) * (beta - gamma)^j!
    Wait: look at that remarkable identity in line 269 (for n = m - 1 hypotheses):
    When beta = gamma (which happens both for F_1(x) = 0 where beta = gamma = pi_0 * alpha / m
    and for F_1(x) = x where beta = gamma = alpha / m), (beta - gamma)^j = 0 for all j >= 1,
    so ONLY the j = 0 term survives:
    u_0(gamma, gamma) = 1 - (m - 1) * gamma!
    And when F_1(x) = eps (in particular eps = 1 for Dirac at 0),
    beta = pi_0 * alpha / m + (1 - pi_0) * eps and gamma = pi_0 * alpha / m,
    so beta - gamma = (1 - pi_0) * eps!
    Wait: what is E[FDP(LSU)^2] in terms of u_0?
    By Theorem 3.1 Eq. (13) for s = 2 (where {2 \atop 1} = 1, {2 \atop 2} = 1) and t_k = alpha * k / m:
    - The ell = 1 term is:
      m * pi_0 * sum_{k=1}^m (t_k / k^2) * D_{m-1}([G(t_{j+1})]_{1<=j<=m-1}, k-1)
      = pi_0 * alpha * sum_{r=0}^{m-1} (1 / (r + 1)) * D_{m-1}([G(t_{j+1})]_{1<=j<=m-1}, r)
      = pi_0 * alpha * u_0!
    - The ell = 2 term is:
      m * (m - 1) * pi_0^2 * sum_{k=2}^m (t_k^2 / k^2) * D_{m-2}([G(t_{j+2})]_{1<=j<=m-2}, k-2)
      = m * (m - 1) * pi_0^2 * (alpha / m)^2 * sum_{r=0}^{m-2} D_{m-2}(..., r)
      = (1 - 1 / m) * (pi_0 * alpha)^2 (since sum_{r=0}^{m-2} D_{m-2}(..., r) = 1)!
    Therefore, for ANY F_1 in F:
    E[FDP(LSU)^2] = pi_0 * alpha * u_0 + (1 - 1 / m) * (pi_0 * alpha)^2,
    and since FDR(LSU) = pi_0 * alpha, the variance is:
    Var[FDP(LSU)] = E[FDP(LSU)^2] - (pi_0 * alpha)^2
                  = pi_0 * alpha * u_0 - (pi_0 * alpha)^2 / m!
    """
    gamma = pi0 * alpha / m
    # For F_1 == 0 (supremum of Var[FDP]): beta = gamma = pi0 * alpha / m -> u_0 = 1 - (m - 1) * gamma
    u0_max = 1.0 - (m - 1) * gamma
    var_max_eq30 = (pi0 * alpha) * u0_max - ((pi0 * alpha) ** 2) / m

    # For F_1(x) = x (infimum over concave F_1 in F'): beta = gamma = alpha / m -> u_0 = 1 - (m - 1) * (alpha / m)
    u0_concave_min = 1.0 - (m - 1) * (alpha / m)
    var_min_concave = (pi0 * alpha) * u0_concave_min - ((pi0 * alpha) ** 2) / m

    # For F_1 == 1 (Dirac at 0, global minimum over F): beta - gamma = 1 - pi0, gamma = pi0 * alpha / m
    # By Eq. (29) / line 269 with n = m - 1:
    # u_0 = sum_{j=0}^{m-1} ((1 - (m - 1 - j)*gamma) / (j + 1)) * comb(m - 1, j) * (1 - pi0)^j * pi0^{m - 1 - j}?
    # Wait: in line 269, is it (beta - gamma)^j or binomial expansion?
    # Let's check: when G(t_{j+1}) = beta + j * gamma for j = 1..n (where n = m - 1),
    # D_n(G, r) = comb(n, r) * (beta + r*gamma)^r * Psi_{n-r}(1 - beta - n*gamma, ..., 1 - beta - (r+1)*gamma).
    # By Finner-Roters Lemma 2.1, Psi_{n-r} = (1 - beta - (r+1)*gamma) * (1 - beta - n*gamma)^{n-r-1},
    # and when beta = 1 - pi0 + 2*gamma (since G(t_2) = 1 - pi0 + 2*pi0*alpha/m = (1 - pi0 + gamma) + 1*gamma),
    # 1 - beta - n*gamma = 1 - (1 - pi0 + gamma) - (m - 1)*gamma = pi0 * (1 - alpha)!
    # Let's compute u_0 for F_1 == 1 directly via log-space Finner-Roters sum over k = 1..m (r = k - 1):
    # D_{m-1}([G(t_{j+1})]_{1<=j<=m-1}, k-1):
    # Here b_r = G(t_{r+1}) = (1 - pi0) + pi0 * alpha * (r + 1) / m for r = 1..m-1.
    # For k = 1..m (so r = k - 1 in 0..m-1):
    # b_r^r = (1 - pi0 + pi0 * alpha * k / m)^{k - 1},
    # and Psi_{m-k}(1 - b_{m-1}, ..., 1 - b_k) by Lemma 2.1 with nu_1 = pi0*(1 - alpha) - pi0*alpha/m, nu_2 = pi0*alpha/m:
    # nu_1 + nu_2 = 1 - b_{m-1} = pi0 * (1 - alpha),
    # nu_1 + (m - k + 1)*nu_2 = 1 - b_{k-1} = pi0 * (1 - alpha * k / m)!
    # So Psi_{m-k} = pi0 * (1 - alpha) * (pi0 * (1 - alpha * k / m))^{m - k - 1} for k <= m - 1, and 1 for k = m!
    u0_min = 0.0
    for k in range(1, m + 1):
        pk = 1.0 - pi0 + pi0 * alpha * (k / m)
        if k == m:
            prob_k = pk ** (m - 1)
        else:
            qk = pi0 * (1.0 - alpha * (k / m))
            log_prob = (
                math.lgamma(m)
                - math.lgamma(k)
                - math.lgamma(m - k + 1)
                + (k - 1) * math.log(pk)
                + math.log(pi0 * (1.0 - alpha))
                + (m - k - 1) * math.log(qk)
            )
            prob_k = math.exp(log_prob)
        u0_min += prob_k / k

    var_min_eq29 = (pi0 * alpha) * u0_min - ((pi0 * alpha) ** 2) / m
    return {
        "var_min_eq29": var_min_eq29,
        "sd_min": math.sqrt(max(0.0, var_min_eq29)),
        "var_min_concave": var_min_concave,
        "sd_min_concave": math.sqrt(max(0.0, var_min_concave)),
        "var_max_eq30": var_max_eq30,
        "sd_max": math.sqrt(max(0.0, var_max_eq30)),
    }


def main() -> None:
    # 1. Verify Theorem 3.1 Eq. (11)-(14) for s = 1, 2, 3, 4 and show Ferreira-Zwinderman discrepancy at s = 3
    m_small = 5
    pi0_small = 0.6
    alpha_small = 0.25
    t_small = [alpha_small * (k / m_small) for k in range(1, m_small + 1)]
    f1_small = [math.sqrt(t) for t in t_small]

    moments_check: dict[str, dict[str, float]] = {}
    for s in [1, 2, 3, 4]:
        m_thm31 = su_fdp_moment_thm31(t_small, pi0_small, f1_small, s)
        m_direct = su_fdp_moment_direct_from_cond_binomial(t_small, pi0_small, f1_small, s)
        assert abs(m_thm31 - m_direct) < 1e-12, f"Mismatch at s={s}: {m_thm31} vs {m_direct}"
        moments_check[str(s)] = {
            "stirling_formula_eq13": round(m_thm31, 10),
            "conditional_binomial_eq11": round(m_direct, 10),
        }

    assert abs(moments_check["1"]["stirling_formula_eq13"] - alpha_small * pi0_small) < 1e-12

    g_small = [pi0_small * t_small[j] + (1.0 - pi0_small) * f1_small[j] for j in range(m_small)]
    wrong_s3 = 0.0
    for ell in range(1, 4):
        falling = math.factorial(m_small) // math.factorial(m_small - ell)
        d_sub = d_su_dist(g_small[ell:])
        inner = sum(((t_small[k - 1] ** ell) / (k ** 3)) * d_sub[k - ell] for k in range(ell, m_small + 1))
        wrong_s3 += falling * 1 * (pi0_small ** ell) * inner
    stirling_s3_diff = moments_check["3"]["stirling_formula_eq13"] - wrong_s3
    assert stirling_s3_diff > 1e-4

    # 2. Verify Theorem 3.2 & Eq. (20)-(21):
    # (a) Non-binomial conditional distribution of V | |SD(t)| = 2 for m = 2, t_1 < t_2, F_1(u) = sqrt(u)
    t1, t2 = 0.1, 0.4
    pi0_sd = 0.5
    p_sd2_v2 = (pi0_sd ** 2) * (2.0 * t1 * t2 - t1 * t1)
    p_sd2_v1 = 2.0 * pi0_sd * (1.0 - pi0_sd) * (
        t2 * math.sqrt(t2) - (t2 - t1) * (math.sqrt(t2) - math.sqrt(t1))
    )
    p_sd2_v0 = ((1.0 - pi0_sd) ** 2) * (2.0 * math.sqrt(t1 * t2) - t1)
    p_sd2_total = p_sd2_v0 + p_sd2_v1 + p_sd2_v2
    cond_sd_probs = [p_sd2_v0 / p_sd2_total, p_sd2_v1 / p_sd2_total, p_sd2_v2 / p_sd2_total]
    g_t2 = pi0_sd * t2 + (1.0 - pi0_sd) * math.sqrt(t2)
    p_bin_sd = (pi0_sd * t2) / g_t2
    binom_probs = [(1.0 - p_bin_sd) ** 2, 2.0 * p_bin_sd * (1.0 - p_bin_sd), p_bin_sd ** 2]
    sd_non_binomial_l1_gap = sum(abs(a - b) for a, b in zip(cond_sd_probs, binom_probs))
    assert sd_non_binomial_l1_gap > 0.01

    # (b) Verify Finner-Roters Lemma 2.1 (Eq. 7) and closed-form Dirac-uniform LSD FDR (Eq. 21) vs Eq. (20)
    m_lsd, pi0_lsd, alpha_lsd = 6, 0.7, 0.2
    t_lsd_vec = [alpha_lsd * (k / m_lsd) for k in range(1, m_lsd + 1)]
    fdr_lsd_eq20_dirac = sd_fdr_thm32_eq20(t_lsd_vec, pi0_lsd, [1.0] * m_lsd)
    fdr_lsd_eq21_fr = lsd_fdr_dirac_uniform_finner_roters_eq21(m_lsd, pi0_lsd, alpha_lsd)
    fdr_lsd_sqrt = sd_fdr_thm32_eq20(t_lsd_vec, pi0_lsd, [math.sqrt(t) for t in t_lsd_vec])
    fdr_lsd_uniform = sd_fdr_thm32_eq20(t_lsd_vec, pi0_lsd, t_lsd_vec)
    assert abs(fdr_lsd_eq20_dirac - fdr_lsd_eq21_fr) < 1e-12
    # Verify Theorem 4.1 LFC property for LSD over concave F_1:
    # max(FDR(LSD, F_1(x)=x), FDR(LSD, F_1(x)=sqrt(x))) < FDR(LSD, F_1==1) < FDR(LSU) = alpha * pi0
    assert 0.0 < max(fdr_lsd_uniform, fdr_lsd_sqrt) < fdr_lsd_eq20_dirac < alpha_lsd * pi0_lsd

    # 3. Verify Proposition 3.6 & Eq. (25)-(26): m = 2, m_0 = 1, rho -> -1^-, mu = z_1 + z_2
    alpha_neg = 0.05
    fdr_neg_corr_exact = (alpha_neg / 2.0) * 1.0 + (alpha_neg - alpha_neg / 2.0) * 0.5
    by_bound_m2_m0_1 = alpha_neg * (1.0 / 2.0) * (1.0 + 0.5)
    dirac_uniform_m2_m0_1 = alpha_neg * (1.0 / 2.0)
    assert abs(fdr_neg_corr_exact - by_bound_m2_m0_1) < 1e-15
    assert fdr_neg_corr_exact > dirac_uniform_m2_m0_1

    # 4. Verify Theorem 4.1 Condition (A) monotonicity for LSD, quantify the Section 6.4 Eq. (34)
    # recurrence discrepancy, and verify the SU vs SD LFC split on t_k = 0.9*(k/m)^{9/10}
    s_lsd_rec = lsd_s_mk_recursion_eq34(m_lsd, alpha_lsd)
    q_lsd_direct = condition_a_q_sequence(t_lsd_vec)
    s_lsd_true = [q_lsd_direct[k] / (alpha_lsd / m_lsd) for k in range(m_lsd)]
    # Check true nondecreasing property S_{m, 1} < S_{m, 2} < ... < S_{m, m} = 1 (Condition A for LSD)
    for k in range(m_lsd - 1):
        assert s_lsd_true[k] < s_lsd_true[k + 1]
        assert q_lsd_direct[k] < q_lsd_direct[k + 1]
    assert abs(s_lsd_true[-1] - 1.0) < 1e-12
    # Quantify the Section 6.4 Eq. (34) recurrence discrepancy for k < m (caused by replacing
    # exponent m-k-i with m-1-k-i on p. 608 when applying ((m-k-i)/(m-k))*comb(m-k, i) = comb(m-k-1, i))
    eq34_max_discrepancy = max(abs(s_lsd_true[k] - s_lsd_rec[k]) for k in range(m_lsd - 1))
    assert eq34_max_discrepancy > 1e-4

    # Counterexample t_k = 0.9 * (k/m)^{9/10} (m = 5, pi0 = 0.5) from Section 4.1.1 (p. 598):
    # k -> t_k / k is decreasing (so SU LFC over concave F_1 is F_1(x) = x),
    # whereas k -> Q_k(t) is nondecreasing (so Condition (A) holds and SD LFC over concave F_1 is F_1 == 1)!
    m_ce = 5
    pi0_ce = 0.5
    t_ce = [0.9 * ((k / m_ce) ** 0.9) for k in range(1, m_ce + 1)]
    q_ce = condition_a_q_sequence(t_ce)
    for k in range(m_ce - 1):
        assert q_ce[k] <= q_ce[k + 1] + 1e-12, f"Expected nondecreasing Q_k for t_ce, got {q_ce}"
    fdr_su_ce_uniform = su_fdp_moment_direct_from_cond_binomial(t_ce, pi0_ce, t_ce, 1)
    fdr_su_ce_dirac = su_fdp_moment_direct_from_cond_binomial(t_ce, pi0_ce, [1.0] * m_ce, 1)
    fdr_sd_ce_uniform = sd_fdr_thm32_eq20(t_ce, pi0_ce, t_ce)
    fdr_sd_ce_dirac = sd_fdr_thm32_eq20(t_ce, pi0_ce, [1.0] * m_ce)
    assert fdr_su_ce_uniform > fdr_su_ce_dirac
    assert fdr_sd_ce_dirac > fdr_sd_ce_uniform

    # 5. Verify Theorem 4.3 (Eq. 28-30) FDP variance bounds:
    vb_small = lsu_fdp_variance_bounds_thm43(m_lsd, pi0_lsd, alpha_lsd)
    var_min_direct = (
        su_fdp_moment_direct_from_cond_binomial(t_lsd_vec, pi0_lsd, [1.0] * m_lsd, 2)
        - (alpha_lsd * pi0_lsd) ** 2
    )
    var_concave_direct = (
        su_fdp_moment_direct_from_cond_binomial(t_lsd_vec, pi0_lsd, t_lsd_vec, 2)
        - (alpha_lsd * pi0_lsd) ** 2
    )
    var_max_direct = (
        su_fdp_moment_direct_from_cond_binomial(t_lsd_vec, pi0_lsd, [0.0] * m_lsd, 2)
        - (alpha_lsd * pi0_lsd) ** 2
    )
    assert abs(vb_small["var_min_eq29"] - var_min_direct) < 1e-12
    assert abs(vb_small["var_min_concave"] - var_concave_direct) < 1e-12
    assert abs(vb_small["var_max_eq30"] - var_max_direct) < 1e-12
    assert 0.0 < vb_small["var_min_eq29"] < vb_small["var_min_concave"] < vb_small["var_max_eq30"]

    # Sparse genomic benchmark from Section 4.2 (p. 601): m = 10000, alpha = 0.05, 1 - pi0 = 0.01 (pi0 = 0.99)
    vb_sparse = lsu_fdp_variance_bounds_thm43(10000, 0.99, 0.05)
    assert abs(vb_sparse["sd_min"] - 0.0217) < 0.0005

    result = {
        "concept_id": "AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis",
        "primary_source": "Roquain & Villers (2011), Annals of Statistics 39(1):584-612 (arXiv:1002.2845v2, DOI:10.1214/10-AOS847)",
        "theorem_3_1_moments_verification": {
            "m": m_small,
            "pi0": pi0_small,
            "alpha": alpha_small,
            "moments_1_to_4": moments_check,
            "s3_omitting_stirling_factor_3": round(wrong_s3, 10),
            "s3_stirling_correction_magnitude": round(stirling_s3_diff, 10),
        },
        "theorem_3_2_step_down_verification": {
            "non_binomial_conditional_l1_gap": round(sd_non_binomial_l1_gap, 8),
            "lsd_fdr_m6_pi07_alpha02_uniform": round(fdr_lsd_uniform, 10),
            "lsd_fdr_m6_pi07_alpha02_sqrt": round(fdr_lsd_sqrt, 10),
            "lsd_fdr_m6_pi07_alpha02_dirac_eq20": round(fdr_lsd_eq20_dirac, 10),
            "lsd_fdr_m6_pi07_alpha02_dirac_eq21": round(fdr_lsd_eq21_fr, 10),
        },
        "proposition_3_6_negative_correlation_counterexample": {
            "m": 2,
            "m0": 1,
            "alpha": alpha_neg,
            "fdr_lsu_at_rho_minus_1": round(fdr_neg_corr_exact, 8),
            "benjamini_yekutieli_upper_bound": round(by_bound_m2_m0_1, 8),
            "dirac_uniform_fdr": round(dirac_uniform_m2_m0_1, 8),
        },
        "theorem_4_1_condition_a_and_su_vs_sd_lfc_split": {
            "s_lsd_m6_alpha02_true": [round(x, 8) for x in s_lsd_true],
            "s_lsd_m6_alpha02_recursion_eq34": [round(x, 8) for x in s_lsd_rec],
            "eq34_max_discrepancy": round(eq34_max_discrepancy, 8),
            "q_concave_t_m5": [round(x, 8) for x in q_ce],
            "fdr_su_concave_t_uniform_f1": round(fdr_su_ce_uniform, 8),
            "fdr_su_concave_t_dirac_f1": round(fdr_su_ce_dirac, 8),
            "fdr_sd_concave_t_uniform_f1": round(fdr_sd_ce_uniform, 8),
            "fdr_sd_concave_t_dirac_f1": round(fdr_sd_ce_dirac, 8),
        },
        "theorem_4_3_fdp_variance_extrema": {
            "small_m6_pi07_alpha02": {k: round(v, 10) for k, v in vb_small.items()},
            "sparse_m10000_pi099_alpha005": {
                "sd_min": round(vb_sparse["sd_min"], 6),
                "sd_min_concave": round(vb_sparse["sd_min_concave"], 6),
                "sd_max": round(vb_sparse["sd_max"], 6),
                "var_min": round(vb_sparse["var_min_eq29"], 8),
                "var_max": round(vb_sparse["var_max_eq30"], 8),
            },
        },
        "all_assertions_passed": True,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
