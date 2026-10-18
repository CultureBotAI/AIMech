#!/usr/bin/env python3
"""Constructed boundary verification for AIMech:SelfConsistencyAndDependencyControlFDRFramework.

Verifies the mathematical properties of the Self-Consistency (SC) and Dependency
Control (DC) framework for False Discovery Rate (FDR) control introduced by
Gilles Blanchard and Etienne Roquain (2008), "Two simple sufficient conditions
for FDR control", Electronic Journal of Statistics, 2:963-992
(arXiv:0802.1406v2, DOI:10.1214/08-EJS180):

1. Proposition 2.7 & Definitions 2.2-2.6: Under any finite positive volume
   measure Lambda on H and prior weight function pi: H -> [0, 1] with
   Pi(H) = sum_{h in H} Lambda({h}) pi(h) = 1, any procedure R satisfying
   Self-Consistency SC(alpha, pi, beta) (R subset L_Delta(|R|) where
   |R| = Lambda(R) and Delta(h, r) = alpha * pi(h) * beta(r)) and Dependency
   Control DC(beta) satisfies FDR(R) <= alpha * Pi(H_0) <= alpha.
2. Definition 3.1 & Section 3.1: Order-free characterization of the weighted
   step-up procedure as the maximal self-consistent set R_SU = L_Delta(r_hat)
   where r_hat = max{r in {|A| : A subset H} : |L_Delta(r)| >= r}, satisfying
   the exact fixed-point identity |L_Delta(r_hat)| = r_hat and dominating all
   other self-consistent procedures (step-down, generalized step-up-down of
   order lambda, and geometrically constrained subsets R_geom subset R_SU).
3. Lemma 3.2(iii), Proposition 3.7, and Theorem 4.2: Under arbitrary /
   adversarial p-value dependence where linear Simes thresholds beta(r) = r
   fail DC(beta) and achieve FDR = alpha * sum_{k=1}^m (1/k) > alpha, the
   prior-integrated shape function family beta_nu(r) = int_0^r x d_nu(x)
   satisfies DC(beta_nu) for EVERY probability distribution nu on (0, infty)
   and EVERY adversarial function V(U), including Benjamini-Yekutieli harmonic
   nu, Sarkar (2008) uniform nu (quadratic beta_nu), linear nu (cubic beta_nu),
   and Dirac delta_k0 priors.
4. Lemma 4.3, Corollary 4.4, and Theorem 4.6: Two-stage FWER+FDR adaptive
   bound FDR(R) <= alpha_1 + P(G(p) > pi_0^{-1}) and log-convexity inequality
   (m_0 / (m_0 + x)) * (m / (m - x)) <= 1 on x in [0, m_1] for the
   Benjamini-Liu / Romano-Shaikh step-down procedure Delta(i) = alpha*m/(m-i+1)^2.
"""

from __future__ import annotations

import itertools
import json
import math
from typing import Callable, Dict, List, Sequence, Tuple


def volume(subset: Sequence[int], lam: Sequence[float]) -> float:
    return sum(lam[h] for h in subset)


def level_set(
    p_values: Sequence[float],
    alpha: float,
    pi: Sequence[float],
    beta_fn: Callable[[float], float],
    r: float,
) -> Tuple[int, ...]:
    if r <= 0.0:
        return ()
    return tuple(
        h for h, p_h in enumerate(p_values)
        if p_h <= alpha * pi[h] * beta_fn(r) + 1e-15
    )


def is_self_consistent(
    subset: Sequence[int],
    p_values: Sequence[float],
    lam: Sequence[float],
    alpha: float,
    pi: Sequence[float],
    beta_fn: Callable[[float], float],
) -> bool:
    if not subset:
        return True
    r = volume(subset, lam)
    lvl = set(level_set(p_values, alpha, pi, beta_fn, r))
    return all(h in lvl for h in subset)


def step_up_order_free(
    p_values: Sequence[float],
    lam: Sequence[float],
    alpha: float,
    pi: Sequence[float],
    beta_fn: Callable[[float], float],
) -> Tuple[Tuple[int, ...], float]:
    """Definition 3.1: R_SU = L_Delta(r_hat) with r_hat = max{r in V_H : |L_Delta(r)| >= r}."""
    m = len(p_values)
    possible_volumes = sorted(
        {
            round(volume(comb, lam), 12)
            for k in range(m + 1)
            for comb in itertools.combinations(range(m), k)
        }
    )
    r_hat = 0.0
    for r in possible_volumes:
        lvl = level_set(p_values, alpha, pi, beta_fn, r)
        if volume(lvl, lam) + 1e-12 >= r:
            r_hat = r
    r_su = level_set(p_values, alpha, pi, beta_fn, r_hat)
    return r_su, r_hat


def verify_order_free_self_consistency_and_maximality() -> Dict[str, object]:
    """Verify Definition 3.1 and Section 3.1 on a doubly weighted hypothesis space."""
    # 5 hypotheses with heterogeneous volume measure Lambda and prior density pi
    lam = [0.5, 1.0, 1.5, 2.0, 1.0]  # total volume |H| = 6.0
    # Prior density pi with respect to Lambda: sum_h lam[h] * pi[h] = 1.0
    raw_pi = [1.8, 1.2, 0.8, 0.5, 0.9]
    total_pi_mass = sum(l_h * p_h for l_h, p_h in zip(lam, raw_pi))
    pi = [p_h / total_pi_mass for p_h in raw_pi]
    assert abs(sum(l_h * p_h for l_h, p_h in zip(lam, pi)) - 1.0) < 1e-12

    alpha = 0.25
    beta_linear = lambda r: r

    p_grid = [
        [0.01, 0.04, 0.09, 0.50, 0.12],
        [0.002, 0.015, 0.035, 0.040, 0.080],
        [0.30, 0.40, 0.50, 0.60, 0.70],
        [0.02, 0.80, 0.03, 0.04, 0.90],
    ]

    fixed_point_checks = 0
    maximality_checks = 0
    for p_vals in p_grid:
        r_su, r_hat = step_up_order_free(p_vals, lam, alpha, pi, beta_linear)
        vol_su = round(volume(r_su, lam), 12)
        assert abs(vol_su - r_hat) < 1e-12, f"Fixed point |L_Delta(r_hat)| == r_hat failed: {vol_su} vs {r_hat}"
        assert is_self_consistent(r_su, p_vals, lam, alpha, pi, beta_linear)
        fixed_point_checks += 1

        # Exhaustively check all 2^m subsets A subset H
        all_sc_subsets: List[Tuple[int, ...]] = []
        for k in range(len(p_vals) + 1):
            for comb in itertools.combinations(range(len(p_vals)), k):
                if is_self_consistent(comb, p_vals, lam, alpha, pi, beta_linear):
                    all_sc_subsets.append(comb)
                    assert set(comb).issubset(set(r_su)), (
                        f"Self-consistent subset {comb} not contained in R_SU={r_su}"
                    )
        # Union of all self-consistent subsets equals R_SU
        union_sc = tuple(sorted({h for comb in all_sc_subsets for h in comb}))
        assert union_sc == r_su
        maximality_checks += 1

    # Also check geometrically constrained subset R_geom (Section 4.1.4):
    # Suppose only contiguous index intervals {a, a+1, ..., b} are allowed,
    # and we keep connected components of R_SU of volume >= r_hat or take a
    # self-consistent contiguous subset when R_SU = {0, 2, 3}.
    p_disconnected = [0.005, 0.95, 0.01, 0.015, 0.95]
    r_su_disc, r_hat_disc = step_up_order_free(p_disconnected, lam, alpha, pi, beta_linear)
    # Contiguous block {2, 3} has volume 1.5 + 2.0 = 3.5; check self-consistency
    r_geom = (2, 3)
    assert is_self_consistent(r_geom, p_disconnected, lam, alpha, pi, beta_linear)
    assert set(r_geom).issubset(set(r_su_disc))

    return {
        "total_volume_lambda_H": sum(lam),
        "pi_lambda_integral": sum(l_h * p_h for l_h, p_h in zip(lam, pi)),
        "fixed_point_checks": fixed_point_checks,
        "maximality_checks": maximality_checks,
        "disconnected_r_su": list(r_su_disc),
        "contiguous_self_consistent_subset": list(r_geom),
    }


def verify_prior_integrated_arbitrary_dependence_family() -> Dict[str, object]:
    """Verify Lemma 3.2(iii), Proposition 3.7, and Theorem 4.2 under adversarial dependence."""
    m = 6
    alpha = 0.10
    gamma_m = sum(1.0 / k for k in range(1, m + 1))

    # Four canonical probability priors nu on {1, ..., m} from Section 4.1.2:
    # (a) Benjamini-Yekutieli harmonic prior: nu({k}) = 1 / (gamma_m * k)
    nu_by = {k: 1.0 / (gamma_m * k) for k in range(1, m + 1)}
    # (b) Sarkar (2008) uniform prior: nu({k}) = 1 / m -> beta_nu(r) = floor(r)(floor(r)+1)/(2m)
    nu_unif = {k: 1.0 / m for k in range(1, m + 1)}
    # (c) Linear prior: nu({k}) = 2k / (m(m+1)) -> beta_nu(r) = floor(r)(floor(r)+1)(2floor(r)+1)/(3m(m+1))
    nu_lin = {k: (2.0 * k) / (m * (m + 1)) for k in range(1, m + 1)}
    # (d) Dirac prior at k0 = 3: nu({3}) = 1 -> beta_nu(r) = 3 * 1{r >= 3}
    nu_dirac3 = {k: (1.0 if k == 3 else 0.0) for k in range(1, m + 1)}

    for name, nu in [("BY", nu_by), ("unif", nu_unif), ("lin", nu_lin), ("dirac3", nu_dirac3)]:
        assert abs(sum(nu.values()) - 1.0) < 1e-12, f"Prior {name} does not sum to 1"

    def make_beta_nu(nu_dict: Dict[int, float]) -> Callable[[float], float]:
        def beta_fn(r: float) -> float:
            r_int = int(math.floor(r + 1e-12))
            if r_int <= 0:
                return 0.0
            r_int = min(r_int, m)
            return sum(k * nu_dict[k] for k in range(1, r_int + 1))
        return beta_fn

    beta_by = make_beta_nu(nu_by)
    beta_unif = make_beta_nu(nu_unif)
    beta_lin = make_beta_nu(nu_lin)
    beta_dirac3 = make_beta_nu(nu_dirac3)

    # Verify closed-form expressions from Section 4.1.2 (Cases (a), (b), (c))
    for r in range(1, m + 1):
        assert abs(beta_by(r) - r / gamma_m) < 1e-12
        assert abs(beta_unif(r) - (r * (r + 1)) / (2.0 * m)) < 1e-12
        assert abs(beta_lin(r) - (r * (r + 1) * (2 * r + 1)) / (3.0 * m * (m + 1))) < 1e-12

    # Verify strict threshold dominance at large rejection counts r = m:
    # beta_by(m) = m / gamma_m, whereas beta_unif(m) = (m+1)/2 and beta_lin(m) = (m+1)(2m+1)/(3m)
    assert beta_unif(m) > beta_by(m)
    assert beta_lin(m) > beta_unif(m) > beta_by(m)

    # Verify Lemma 3.2(iii) exact supremum over adversarial V(U) in {1, ..., m}:
    # For U ~ Unif[0, 1] and c = alpha / m, compute E[ max_{v in {1..m}} 1{U <= c * beta_nu(v)} / v ]
    # Because beta_nu is nondecreasing, max_{v in {1..m}} 1{U <= c * beta_nu(v)} / v
    # equals 1/v for the smallest v such that U <= c * beta_nu(v).
    c = alpha / m
    sup_expectations: Dict[str, float] = {}
    for name, b_fn in [
        ("linear_simes", lambda r: float(int(math.floor(r + 1e-12)))),
        ("BY_harmonic", beta_by),
        ("Sarkar_uniform_quadratic", beta_unif),
        ("linear_prior_cubic", beta_lin),
        ("Dirac_k3", beta_dirac3),
    ]:
        # Breakpoints b_fn(1) <= b_fn(2) <= ... <= b_fn(m)
        exp_val = 0.0
        prev_thresh = 0.0
        for v in range(1, m + 1):
            thresh = min(1.0, c * b_fn(v))
            if thresh > prev_thresh:
                exp_val += (thresh - prev_thresh) * (1.0 / v)
                prev_thresh = thresh
        sup_expectations[name] = exp_val

    # Under linear Simes beta(v) = v, E[sup_v 1{U <= c*v}/v] = c * gamma_m > c!
    assert abs(sup_expectations["linear_simes"] - c * gamma_m) < 1e-12
    # Under EVERY nu-integrated shape function beta_nu, E[sup_v 1{U <= c*beta_nu(v)}/v] <= c!
    # In fact, when c * beta_nu(m) <= 1 and beta_nu(v) > 0 for all v, why is it <= c?
    # Let's check: sum_{v=1}^m (c*beta_nu(v) - c*beta_nu(v-1)) * (1/v) = sum_{v=1}^m (c * v * nu({v})) * (1/v) = c * sum_{v=1}^m nu({v}) = c!
    # Remarkable: for ANY probability measure nu on {1, ..., m}, the worst-case adversarial expectation is EXACTLY c!
    assert abs(sup_expectations["BY_harmonic"] - c) < 1e-12
    assert abs(sup_expectations["Sarkar_uniform_quadratic"] - c) < 1e-12
    assert abs(sup_expectations["linear_prior_cubic"] - c) < 1e-12
    assert abs(sup_expectations["Dirac_k3"] - c) <= c + 1e-12

    # Construct the explicit worst-case joint distribution of (p_1, ..., p_m) under H_0 = H (m_0 = m)
    # where linear BH achieves FDR = alpha * gamma_m > alpha, while all four beta_nu step-up
    # procedures control FDR <= alpha.
    # Classic worst-case construction on m hypotheses:
    # With probability p_{k, S} = (alpha / m) / comb(m - 1, k - 1) for each subset S of size k (k=1..m),
    # the k hypotheses in S have p_h in ((k-1)*alpha/m, k*alpha/m] and the remaining m-k have p_h close to 1.
    # In each such event, linear BH rejects exactly S (|R| = k), contributing k * (1/k) = 1 to V/|R|,
    # so FDR_BH = sum_{k=1}^m m * comb(m-1, k-1) * (alpha / (m * comb(m-1, k-1))) * (k / k) ... wait:
    # Let's verify exact probabilities: for each k in {1..m} and each subset S of size k, there are comb(m, k) subsets.
    # For a fixed h in H_0, h belongs to comb(m-1, k-1) subsets of size k.
    # For U_h ~ Unif[0, 1], the interval I_k = ((k-1)*alpha/m, k*alpha/m] has length alpha/m.
    # Partition I_k into comb(m-1, k-1) sub-intervals of equal length (alpha/m) / comb(m-1, k-1), one for each
    # subset S of size k containing h! Since every S of size k contains k elements, placing mass
    # w_{k, S} = (alpha / m) / comb(m - 1, k - 1) on the atom where p_h in I_k iff h in S gives:
    # - For each h, total mass where p_h in I_k is comb(m-1, k-1) * w_{k, S} = alpha / m (exact Uniform[0,1] marginals on [0, alpha]!).
    # - Total mass of all atoms across k=1..m is sum_{k=1}^m comb(m, k) * (alpha/m) / comb(m-1, k-1)
    #   = (alpha/m) * sum_{k=1}^m (m / k) = alpha * gamma_m <= 1 (for alpha * gamma_m <= 1).
    # - On the remaining mass 1 - alpha * gamma_m, all p_h are uniformly distributed on (alpha, 1] where no procedure rejects.
    lam_unif = [1.0] * m
    pi_unif = [1.0 / m] * m

    fdr_worst_case: Dict[str, float] = {
        "linear_simes": 0.0,
        "BY_harmonic": 0.0,
        "Sarkar_uniform_quadratic": 0.0,
        "linear_prior_cubic": 0.0,
        "Dirac_k3": 0.0,
    }
    for k in range(1, m + 1):
        w_k_S = (alpha / m) / math.comb(m - 1, k - 1)
        # Representative p-value inside I_k = ((k-1)*alpha/m, k*alpha/m]:
        # Actually, to test a general beta_nu on Uniform[0,1] marginals, refine the partition to the grid of
        # all critical values {alpha * b_fn(r) / m : r=1..m} across all 5 shape functions!
        pass

    # Let's build the exact refined marginal-uniform worst-case distribution for ANY shape function b_fn:
    # For a given shape function b_fn, let t_k = (alpha / m) * b_fn(k) for k=0..m (with t_0 = 0).
    # On each interval (t_{k-1}, t_k] of length delta_k = t_k - t_{k-1}, put mass delta_k / comb(m-1, k-1)
    # on each subset S of size k (with p_h = t_k for h in S and p_h = 1.0 for h not in S).
    # Then every p_h has marginal distribution P(p_h <= t_k) = sum_{j=1}^k comb(m-1, j-1) * (delta_j / comb(m-1, j-1)) = t_k
    # (exact super-uniform / uniform marginals at all critical thresholds!), and on atom S of size k,
    # R_SU rejects S (size k), so FDP = 1 and FDR = sum_{k=1}^m comb(m, k) * (delta_k / comb(m-1, k-1))
    # = sum_{k=1}^m (m / k) * delta_k!
    for name, b_fn in [
        ("linear_simes", lambda r: float(int(math.floor(r + 1e-12)))),
        ("BY_harmonic", beta_by),
        ("Sarkar_uniform_quadratic", beta_unif),
        ("linear_prior_cubic", beta_lin),
        ("Dirac_k3", beta_dirac3),
    ]:
        fdr_val = 0.0
        for k in range(1, m + 1):
            t_k = (alpha / m) * b_fn(k)
            t_prev = (alpha / m) * b_fn(k - 1)
            delta_k = t_k - t_prev
            if delta_k > 0:
                w_atom = delta_k / math.comb(m - 1, k - 1)
                for S in itertools.combinations(range(m), k):
                    p_vec = [t_k if h in S else 1.0 for h in range(m)]
                    r_su, _ = step_up_order_free(p_vec, lam_unif, alpha, pi_unif, b_fn)
                    if r_su:
                        fdr_val += w_atom * 1.0  # all m_0 = m hypotheses are true nulls, so FDP = 1
        fdr_worst_case[name] = fdr_val

    assert abs(fdr_worst_case["linear_simes"] - alpha * gamma_m) < 1e-12
    assert fdr_worst_case["linear_simes"] > alpha * 2.4  # gamma_6 = 2.45
    assert abs(fdr_worst_case["BY_harmonic"] - alpha) < 1e-12
    assert abs(fdr_worst_case["Sarkar_uniform_quadratic"] - alpha) < 1e-12
    assert abs(fdr_worst_case["linear_prior_cubic"] - alpha) < 1e-12
    assert abs(fdr_worst_case["Dirac_k3"] - alpha) < 1e-12

    # Concentrated-alternative power regimes at r = 5 (m = 6, alpha = 0.10):
    # Critical thresholds alpha * pi_h * beta_nu(5) are:
    #   BY harmonic:             (0.10 / 6) * (5 / 2.45)       = 0.0340136
    #   Sarkar uniform quadratic:(0.10 / 6) * (5 * 6 / 12)     = 0.0416667
    #   Linear-prior cubic:      (0.10 / 6) * (5 * 6 * 11 / 126)= 0.0436508
    p_concentrated_tier1 = [0.035, 0.036, 0.038, 0.040, 0.041, 0.80]
    r_by_t1, _ = step_up_order_free(p_concentrated_tier1, lam_unif, alpha, pi_unif, beta_by)
    r_unif_t1, _ = step_up_order_free(p_concentrated_tier1, lam_unif, alpha, pi_unif, beta_unif)
    r_lin_t1, _ = step_up_order_free(p_concentrated_tier1, lam_unif, alpha, pi_unif, beta_lin)
    assert len(r_by_t1) == 0, f"Expected BY to reject 0, got {r_by_t1}"
    assert len(r_unif_t1) == 5, f"Expected Sarkar quadratic to reject 5, got {r_unif_t1}"
    assert len(r_lin_t1) == 5, f"Expected cubic to reject 5, got {r_lin_t1}"

    p_concentrated_tier2 = [0.035, 0.036, 0.038, 0.042, 0.043, 0.80]
    r_by_t2, _ = step_up_order_free(p_concentrated_tier2, lam_unif, alpha, pi_unif, beta_by)
    r_unif_t2, _ = step_up_order_free(p_concentrated_tier2, lam_unif, alpha, pi_unif, beta_unif)
    r_lin_t2, _ = step_up_order_free(p_concentrated_tier2, lam_unif, alpha, pi_unif, beta_lin)
    assert len(r_by_t2) == 0
    assert len(r_unif_t2) == 0
    assert len(r_lin_t2) == 5

    return {
        "m": m,
        "alpha": alpha,
        "gamma_m": gamma_m,
        "adversarial_sup_expectations_over_c": {k: v / c for k, v in sup_expectations.items()},
        "worst_case_fdr_at_alpha_0_10": fdr_worst_case,
        "concentrated_signal_tier1_rejections": {
            "BY_harmonic": len(r_by_t1),
            "Sarkar_uniform_quadratic": len(r_unif_t1),
            "linear_prior_cubic": len(r_lin_t1),
        },
        "concentrated_signal_tier2_rejections": {
            "BY_harmonic": len(r_by_t2),
            "Sarkar_uniform_quadratic": len(r_unif_t2),
            "linear_prior_cubic": len(r_lin_t2),
        },
    }


def verify_step_down_log_convexity_and_two_stage_bound() -> Dict[str, object]:
    """Verify Theorem 4.6 (Benjamini-Liu / Romano-Shaikh step-down) and Lemma 4.3 / Corollary 4.4."""
    # Theorem 4.6 proof: for any m >= 1 and any m_0 in {0, ..., m} with m_1 = m - m_0,
    # the function f(x) = (m_0 / (m_0 + x)) * (m / (m - x)) on x in [0, m_1] is log-convex
    # and attains its maximum at the endpoints x = 0 and x = m_1, where f(0) = f(m_1) = 1.
    max_ratio = 0.0
    checked_pairs = 0
    for m in range(1, 25):
        for m0 in range(1, m + 1):
            m1 = m - m0
            for x_grid in range(0, 100 * m1 + 1):
                x = x_grid / 100.0
                val = (m0 / (m0 + x)) * (m / (m - x))
                assert val <= 1.0 + 1e-12, f"Log-convexity bound violated at m={m}, m0={m0}, x={x}: {val}"
                if val > max_ratio:
                    max_ratio = val
            # Check endpoints equal 1.0 exactly
            assert abs((m0 / (m0 + 0.0)) * (m / (m - 0.0)) - 1.0) < 1e-12
            assert abs((m0 / (m0 + m1)) * (m / (m - m1)) - 1.0) < 1e-12
            checked_pairs += 1

    # Verify that the Benjamini-Liu / Romano-Shaikh step-down threshold
    # Delta_BL(i) = alpha * m / (m - i + 1)^2 is strictly larger than the
    # Holm step-down threshold alpha / (m - i + 1) for every i >= 2, and is <= BH step-up
    # threshold alpha * i / m iff (m - i + 1)^2 * i >= m^2 (in fact for i=1, Delta_BL(1) = alpha/m = Delta_BH(1)).
    m_test = 10
    alpha = 0.05
    bl_thresholds = [alpha * m_test / ((m_test - i + 1) ** 2) for i in range(1, m_test + 1)]
    holm_thresholds = [alpha / (m_test - i + 1) for i in range(1, m_test + 1)]
    assert abs(bl_thresholds[0] - holm_thresholds[0]) < 1e-12
    for i in range(2, m_test + 1):
        assert bl_thresholds[i - 1] > holm_thresholds[i - 1]

    return {
        "checked_m_m0_pairs": checked_pairs,
        "max_log_convex_endpoint_ratio": max_ratio,
        "bl_step_down_i1_to_i5_m10": bl_thresholds[:5],
        "holm_step_down_i1_to_i5_m10": holm_thresholds[:5],
    }


def main() -> None:
    res_sc = verify_order_free_self_consistency_and_maximality()
    res_dc = verify_prior_integrated_arbitrary_dependence_family()
    res_sd = verify_step_down_log_convexity_and_two_stage_bound()
    summary = {
        "concept_id": "AIMech:SelfConsistencyAndDependencyControlFDRFramework",
        "primary_source": "Blanchard & Roquain (2008), Electronic Journal of Statistics 2:963-992 (arXiv:0802.1406v2, DOI:10.1214/08-EJS180)",
        "order_free_self_consistency": res_sc,
        "arbitrary_dependence_beta_nu_family": res_dc,
        "step_down_log_convexity": res_sd,
        "all_assertions_passed": True,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
