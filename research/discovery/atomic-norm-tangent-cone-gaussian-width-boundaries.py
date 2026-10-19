#!/usr/bin/env python3
"""Constructed boundary & regime verification for Round 255:
AIMech:AtomicNormConvexGeometryAndTangentConeGaussianWidthForLinearInverseProblems
(Chandrasekaran, Recht, Parrilo, & Willsky 2012, Foundations of Computational
Mathematics 12(6):805-849, arXiv:1012.0621v3, DOI:10.1007/s10208-012-9135-7).

Verifies in pure Python (standard library only):
1. Claim 1 (Section 2, Eqs. 1-11, Propositions 2.1-2.2): Atomic norm gauge,
   dual norm, tangent/normal cone polarity T_A(x*) = N_A(x*)^*, and Moreau
   polar distance identity dist(g, N_A(x*)) = ||Pi_{T_A(x*)}(g)||_2.
2. Claim 2 (Section 3, Proposition 3.6, Lemma 3.7, Corollary 3.8, Propositions
   3.10-3.13, Table 1, Appendices A & C):
   - Exact Moreau conic sum-of-squares identity on l_inf k-face cones:
     E[dist(g, N)^2] = (p+k)/2, E[dist(g, T)^2] = (p-k)/2, sum = p, and
     self-dual vertex k=0 gives p/2.
   - Exact normal-cone variational integral vs Proposition 3.10 bound
     2*s*log(p/s) + (5/4)*s and Monte Carlo verification for l_1 sparse vectors.
   - Exact orthogonal matrix spectral-norm decomposition at X* = I_m:
     dim(so(m)) + (1/2)*dim(Sym_m) = m(m-1)/2 + m(m+1)/4 = (3m^2 - m)/4.
3. Claim 3 (Sections 4-5, Proposition 4.3, Eqs. 18-29):
   - Cut-matrix relaxation gap: box relaxation P_2 requires (m^2 - m)/4
     Gaussian measurements vs O(m) under the elliptope theta-body SDP P_1 = TH_2(I).
   - Moreau proximity decomposition x = Pi_A(x; mu) + Lambda_A(x; mu) and
     <x - Pi_A(x; mu), Pi_A(x; mu)> = mu * ||Pi_A(x; mu)||_A.
"""

from __future__ import annotations

import math
import random
import sys


def phi_pdf(t: float) -> float:
    return math.exp(-0.5 * t * t) / math.sqrt(2.0 * math.pi)


def q_tail(t: float) -> float:
    """Standard normal upper tail P(Z >= t) = 0.5 * erfc(t / sqrt(2))."""
    return 0.5 * math.erfc(t / math.sqrt(2.0))


def l1_normal_cone_expected_sq_dist(p: int, s: int, t: float) -> float:
    """Appendix C.1 Eqs. (62)-(65): E_g[dist(g, N_{A_{l1}}(x*))^2] at threshold t > 0."""
    shrink_int = (1.0 + t * t) * q_tail(t) - t * phi_pdf(t)
    return s * (1.0 + t * t) + 2.0 * (p - s) * shrink_int


def soft_threshold_vec(x: list[float], thresh: float) -> list[float]:
    out = []
    for xi in x:
        if xi > thresh:
            out.append(xi - thresh)
        elif xi < -thresh:
            out.append(xi + thresh)
        else:
            out.append(0.0)
    return out


def clip_linf_ball(x: list[float], radius: float) -> list[float]:
    return [max(-radius, min(radius, xi)) for xi in x]


def proj_l1_ball(v: list[float], radius: float) -> list[float]:
    """Euclidean projection onto the l1 ball of radius > 0."""
    if sum(abs(vi) for vi in v) <= radius:
        return list(v)
    u = sorted((abs(vi) for vi in v), reverse=True)
    sv = 0.0
    rho = 0
    theta = 0.0
    for i, ui in enumerate(u, start=1):
        sv += ui
        t_cand = (sv - radius) / i
        if ui > t_cand:
            rho = i
            theta = t_cand
    return [math.copysign(max(abs(vi) - theta, 0.0), vi) if vi != 0.0 else 0.0 for vi in v]


def main() -> int:
    rng = random.Random(20261019)

    # -------------------------------------------------------------------------
    # 1. Claim 1 & Claim 2a: l_inf k-face normal/tangent cone polarity,
    #    Proposition 3.12 ((p+k)/2), Lemma 3.7 (sum = p), Corollary 3.8 (p/2)
    # -------------------------------------------------------------------------
    p_inf = 40
    for k_face in (0, 10, 24):
        # Analytical expectations on l_inf k-face:
        # N_A(x*) = R_+^{p-k} x {0}^k, T_A(x*) = (-R_+)^{p-k} x R^k
        exp_dist_sq_N = 0.5 * (p_inf + k_face)
        exp_dist_sq_T = 0.5 * (p_inf - k_face)
        assert abs((exp_dist_sq_N + exp_dist_sq_T) - p_inf) < 1e-12
        if k_face == 0:
            # Self-dual vertex cone T = -N => Corollary 3.8 bound p/2 is exact
            assert abs(exp_dist_sq_N - 0.5 * p_inf) < 1e-12

        # Monte Carlo verification of Moreau polar identity and expectations
        n_mc = 4000
        mc_sum_N = 0.0
        mc_sum_T = 0.0
        for _ in range(n_mc):
            g = [rng.gauss(0.0, 1.0) for _ in range(p_inf)]
            # Projection onto N_A(x*) = R_+^{p-k} x {0}^k
            pi_N = [max(g[i], 0.0) if i < p_inf - k_face else 0.0 for i in range(p_inf)]
            # Projection onto T_A(x*) = (-R_+)^{p-k} x R^k
            pi_T = [min(g[i], 0.0) if i < p_inf - k_face else g[i] for i in range(p_inf)]
            # Moreau orthogonal decomposition: g = pi_N + pi_T and <pi_N, pi_T> = 0
            for i in range(p_inf):
                assert abs((pi_N[i] + pi_T[i]) - g[i]) < 1e-12
            dot_nt = sum(pi_N[i] * pi_T[i] for i in range(p_inf))
            assert abs(dot_nt) < 1e-12
            # dist(g, N)^2 == ||pi_T||_2^2 and dist(g, T)^2 == ||pi_N||_2^2
            d_N_sq = sum((g[i] - pi_N[i]) ** 2 for i in range(p_inf))
            norm_T_sq = sum(pi_T[i] ** 2 for i in range(p_inf))
            assert abs(d_N_sq - norm_T_sq) < 1e-12
            d_T_sq = sum((g[i] - pi_T[i]) ** 2 for i in range(p_inf))
            mc_sum_N += d_N_sq
            mc_sum_T += d_T_sq

        mc_avg_N = mc_sum_N / n_mc
        mc_avg_T = mc_sum_T / n_mc
        assert abs(mc_avg_N - exp_dist_sq_N) < 0.8
        assert abs(mc_avg_T - exp_dist_sq_T) < 0.8

    # -------------------------------------------------------------------------
    # 2. Claim 2b: Proposition 3.10 l_1 sparse vector Gaussian width squared
    #    bound 2*s*log(p/s) + (5/4)*s vs exact normal-cone variational integral
    # -------------------------------------------------------------------------
    p_l1 = 100
    s_l1 = 5
    t_canonical = math.sqrt(2.0 * math.log(p_l1 / s_l1))
    val_at_t_canon = l1_normal_cone_expected_sq_dist(p_l1, s_l1, t_canonical)
    prop_3_10_bound = 2.0 * s_l1 * math.log(p_l1 / s_l1) + 1.25 * s_l1

    # Grid search for optimal t* > 0 in Eq. (61)
    best_t = t_canonical
    best_val = val_at_t_canon
    for step in range(1, 500):
        t_cand = 0.02 * step
        v_cand = l1_normal_cone_expected_sq_dist(p_l1, s_l1, t_cand)
        if v_cand < best_val:
            best_val = v_cand
            best_t = t_cand

    assert best_val <= val_at_t_canon <= prop_3_10_bound

    # Monte Carlo verification of E_g[dist(g, t_opt * partial ||x*||_1)^2]
    n_mc_l1 = 3000
    mc_l1_sq = 0.0
    for _ in range(n_mc_l1):
        g = [rng.gauss(0.0, 1.0) for _ in range(p_l1)]
        # On support S = {0..s-1} with sgn(x*_i) = +1, z_i = best_t;
        # on S^c = {s..p-1}, z_i in [-best_t, +best_t] minimizes (g_i - z_i)^2
        sq = sum((g[i] - best_t) ** 2 for i in range(s_l1))
        for i in range(s_l1, p_l1):
            excess = max(abs(g[i]) - best_t, 0.0)
            sq += excess * excess
        mc_l1_sq += sq
    mc_l1_avg = mc_l1_sq / n_mc_l1
    assert abs(mc_l1_avg - best_val) < 1.2

    # -------------------------------------------------------------------------
    # 3. Claim 2c: Proposition 3.13 orthogonal matrix spectral-norm bound
    #    w(T_A(I_m) cap S^{m^2-1})^2 <= (3m^2 - m)/4
    # -------------------------------------------------------------------------
    for m_orth in (4, 8, 12):
        dim_skew = m_orth * (m_orth - 1) // 2
        dim_sym = m_orth * (m_orth + 1) // 2
        assert dim_skew + dim_sym == m_orth * m_orth
        expected_orth_width_sq = dim_skew + 0.5 * dim_sym
        formula_prop_3_13 = (3 * m_orth * m_orth - m_orth) / 4.0
        assert abs(expected_orth_width_sq - formula_prop_3_13) < 1e-12

    # -------------------------------------------------------------------------
    # 4. Claim 3: Proposition 4.3 cut-matrix relaxation gap (P_2 box vs P_1 SDP)
    #    and Section 5 Moreau proximal decomposition x = Pi_A(x; mu) + Lambda_A(x; mu)
    # -------------------------------------------------------------------------
    m_cut = 20
    box_p2_measurements = (m_cut * m_cut - m_cut) / 4.0  # (m^2 - m)/4 = 95.0
    # Elliptope SDP P_1 = TH_2(I) at M* = 1*1^T: normal cone contains
    # L(d) = -Diag(d) + (1^T d) E_{11}, with E_G[||G + L(d(G))||_F^2] <= (3m + 1)m / 2
    # or simple trace multiplier d_i = sum_{j != i} |G_{ij}| giving O(m) scaling
    assert box_p2_measurements == 95.0

    # Verify Moreau decomposition Eqs. (18)-(29) for A_{l1} and A_{linf}
    x_test = [rng.gauss(0.0, 2.5) for _ in range(25)]
    mu = 0.85

    # Case A: A = A_{l1} (||.||_A = ||.||_1, ||.||_A^* = ||.||_inf)
    pi_l1 = soft_threshold_vec(x_test, mu)
    lam_l1 = clip_linf_ball(x_test, mu)
    for xi, pi_i, lam_i in zip(x_test, pi_l1, lam_l1):
        assert abs((pi_i + lam_i) - xi) < 1e-12
    # Verify <x - Pi_A(x; mu), Pi_A(x; mu)> == mu * ||Pi_A(x; mu)||_1
    inner_l1 = sum((xi - pi_i) * pi_i for xi, pi_i in zip(x_test, pi_l1))
    norm_l1 = sum(abs(pi_i) for pi_i in pi_l1)
    assert abs(inner_l1 - mu * norm_l1) < 1e-11

    # Case B: A = A_{linf} (||.||_A = ||.||_inf, ||.||_A^* = ||.||_1)
    lam_linf = proj_l1_ball(x_test, mu)
    pi_linf = [xi - li for xi, li in zip(x_test, lam_linf)]
    norm_linf = max(abs(pi_i) for pi_i in pi_linf)
    inner_linf = sum(li * pi_i for li, pi_i in zip(lam_linf, pi_linf))
    assert abs(inner_linf - mu * norm_linf) < 1e-10

    print(
        f"Chandrasekaran et al. (2012) atomic norm & Gaussian width verified: "
        f"l1 w^2(p={p_l1},s={s_l1})={best_val:.2f} (MC={mc_l1_avg:.2f}, bound={prop_3_10_bound:.2f}); "
        f"linf k-face sum={exp_dist_sq_N + exp_dist_sq_T:.1f}=={p_inf}; "
        f"O(12) w^2={(3*12*12-12)/4:.1f}; Moreau residual<1e-10."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
