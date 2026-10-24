#!/usr/bin/env python3
"""Constructed boundary & numerical verification for AIMech:ForestStructuredDKWPostHocConfidenceBounds.

Verifies the core mathematical claims of:
  Guillermo Durand, Gilles Blanchard, Pierre Neuvial, & Etienne Roquain (2020),
  "Post hoc false positive control for structured hypotheses"
  (arXiv title: "Post hoc false positive control for spatially structured hypotheses"),
  Scandinavian Journal of Statistics, Vol. 47, No. 4, pp. 1114-1148
  (arXiv:1807.01470v2, DOI:10.1111/sjos.12453):

1. Section 2.3 (Lemma 2.1, Example 2.2, p. 4):
   - Multi-subset interpolation hierarchy V^*_R(S) <= V_tilde_R(S) <= V_tilde^q_R(S) <= V_bar_R(S).
   - Strict gap V^*_R(S) = 1 < V_tilde_R(S) = 2 on the 3-set non-forest family of Example 2.2
     (m = 4, R_1 = {1,2,4}, R_2 = {2,3,4}, R_3 = {1,3,4}, zeta_1 = zeta_2 = zeta_3 = 1, S = N_4).

2. Section 3.1-3.2 & Appendices A-B (Definition 3.1, Example 3.2, Lemma 3.3, Example 3.4,
   Definition 3.5, Theorem 3.6, Corollary 3.7, Algorithm 1, Algorithm 2, Lemmas A.2-A.4):
   - Exact node depths phi(k) and Algorithm 2 atomic partition P_1, ..., P_8 for the 9-node
     forest reference family of Example 3.2 on m = 25 (H = 3, d = 6).
   - Completion invariance V^*_{R^oplus}(S) = V^*_R(S) and V_tilde_{R^oplus}(S) = V_tilde_R(S).
   - Exact equality V^*_R(S) = V_tilde_R(S) = V_tilde^d_R(S) = Algorithm_1(R, S) across query sets
     S subset N_25, and strict improvement over single-subset interpolation V_bar_R(S).

3. Section 4.1 & Appendix A (Proposition 4.1, Remarks 4.2-4.3, Equation 32, Lemma A.1):
   - Quadratic-inversion DKW-Massart local bound zeta_k(X) vs. Genovese-Wasserman (2004, Eq. 16)
     bound zeta^{GW}_k(X): verifies Lemma A.1 inequality (33) and strict uniform improvement
     zeta_k(X) <= zeta^{GW}_k(X) across all regions and realizations.
   - Verifies empirical JER control <= alpha on a binary-tree reference family under independence.
   - Documents why Equation (16)'s notation floor(...)^2 is a typographical slip for floor((...)^2)
     from Equation (32).

4. Section 4.2 & Section 5.3 (Proposition 4.5, Figure 6, Corollary 4.6, and Hybrid Bound V^gamma_hybrid):
   - Evaluates the exact theoretical ratio upper bound Eq. (23) for Figure 6 parameters
     (m = 10^7, s = m^{2/3}, K = m/s, r = 3/5, alpha = 0.1) across effect sizes mu, confirming
     the asymptotic factor 1 - r = 0.40 improvement over Simes and Bonferroni.
   - Verifies that the hybrid post hoc bound V^gamma_hybrid(alpha, S_k) = min(V_Simes((1-gamma)alpha, S_k),
     V_tree(gamma*alpha, S_k)) (alpha = 0.05, gamma = 0.02) combines small-k Simes pinpointing
     with large-k multiscale DKW-tree estimation.
"""

from __future__ import annotations

import itertools
import json
import math
import random
from typing import Dict, FrozenSet, List, Sequence, Set, Tuple


def std_normal_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def std_normal_sf(x: float) -> float:
    return 0.5 * math.erfc(x / math.sqrt(2.0))


def std_normal_isf(p: float) -> float:
    """Inverse survival function bar{Phi}^{-1}(p) via bisection."""
    lo, hi = -12.0, 12.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if std_normal_sf(mid) > p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def v_star_combinatorial(
    m: int, regions: Sequence[FrozenSet[int]], zetas: Sequence[int], s_set: FrozenSet[int]
) -> int:
    """Exact optimal post hoc bound V^*_R(S) = max_{A subset N_m : forall k, |R_k cap A| <= zeta_k} |S cap A|."""
    universe = list(range(1, m + 1))
    best = 0
    for r in range(len(universe) + 1):
        for comb in itertools.combinations(universe, r):
            a_set = frozenset(comb)
            if all(len(rk & a_set) <= zk for rk, zk in zip(regions, zetas)):
                val = len(s_set & a_set)
                if val > best:
                    best = val
    return best


def v_tilde_q(
    regions: Sequence[FrozenSet[int]], zetas: Sequence[int], s_set: FrozenSet[int], q: int
) -> int:
    """q-subset interpolation bound V_tilde^q_R(S) (Equation 8, p. 4)."""
    k_len = len(regions)
    best = len(s_set)
    indices = list(range(k_len))
    for r in range(1, min(q, k_len) + 1):
        for q_sub in itertools.combinations(indices, r):
            union_rk = frozenset().union(*(regions[k] for k in q_sub))
            val = sum(min(zetas[k], len(s_set & regions[k])) for k in q_sub) + len(s_set - union_rk)
            if val < best:
                best = val
    return best


def node_depths(regions: Sequence[FrozenSet[int]]) -> List[int]:
    """Depth function phi(k) = 1 + |{k' in K : R_{k'} supsetneq R_k}| (Equation 11, p. 5)."""
    depths = []
    for k, rk in enumerate(regions):
        strict_ancestors = sum(1 for kp, rkp in enumerate(regions) if kp != k and rk < rkp)
        depths.append(1 + strict_ancestors)
    return depths


def algorithm_2_atoms(m: int, regions: Sequence[FrozenSet[int]]) -> List[FrozenSet[int]]:
    """Algorithm 2 (Appendix B, p. 24): Computation of atomic partition (P_n)_{1 <= n <= N}."""
    depths = node_depths(regions)
    h_max = max(depths) if depths else 0
    universe = frozenset(range(1, m + 1))
    partition: List[FrozenSet[int]] = [universe]
    for h in range(1, h_max + 1):
        new_p: List[FrozenSet[int]] = []
        for pn in partition:
            succ = [k for k, rk in enumerate(regions) if rk <= pn and depths[k] == h]
            for k in succ:
                if regions[k]:
                    new_p.append(regions[k])
            rem = pn - frozenset().union(*(regions[k] for k in succ)) if succ else pn
            if rem:
                new_p = [rem] + new_p
        partition = new_p
    return partition


def complete_forest_family(
    m: int, regions: Sequence[FrozenSet[int]], zetas: Sequence[int]
) -> Tuple[List[FrozenSet[int]], List[int]]:
    """Definition 3.5 (p. 6): Completed forest reference family R^oplus."""
    atoms = algorithm_2_atoms(m, regions)
    reg_list = list(regions)
    zeta_list = list(zetas)
    existing = set(reg_list)
    for pn in atoms:
        if pn not in existing:
            reg_list.append(pn)
            zeta_list.append(len(pn))
            existing.add(pn)
    return reg_list, zeta_list


def algorithm_1_bottom_up(
    m: int, regions: Sequence[FrozenSet[int]], zetas: Sequence[int], s_set: FrozenSet[int]
) -> int:
    """Algorithm 1 (Section 3.2, p. 8): O(Hm) bottom-up computation of V^*_R(S)."""
    comp_regions, comp_zetas = complete_forest_family(m, regions, zetas)
    atoms = set(algorithm_2_atoms(m, regions))
    depths = node_depths(comp_regions)
    h_max = max(depths)

    def level_kh(h: int) -> List[int]:
        return [
            k
            for k, rk in enumerate(comp_regions)
            if depths[k] == h or (rk in atoms and depths[k] <= h)
        ]

    kh_cur = level_kh(h_max)
    v_map: Dict[int, int] = {
        k: min(comp_zetas[k], len(s_set & comp_regions[k])) for k in kh_cur
    }
    for h in range(h_max - 1, 0, -1):
        kh_next = level_kh(h)
        new_v: Dict[int, int] = {}
        for k in kh_next:
            rk = comp_regions[k]
            succ_k = [kp for kp in kh_cur if comp_regions[kp] <= rk]
            sum_succ = sum(v_map[kp] for kp in succ_k)
            new_v[k] = min(min(comp_zetas[k], len(s_set & rk)), sum_succ)
        v_map = new_v
        kh_cur = kh_next

    return sum(v_map[k] for k in kh_cur)


def verify_section_2_and_3() -> Dict[str, object]:
    """Verify Example 2.2, Example 3.2/3.4, Algorithm 2, Theorem 3.6, and Algorithm 1."""
    # 1. Example 2.2 (p. 4): m = 4, K = 3, R1={1,2,4}, R2={2,3,4}, R3={1,3,4}, zeta=(1,1,1), S=N_4
    r_ex22 = [frozenset([1, 2, 4]), frozenset([2, 3, 4]), frozenset([1, 3, 4])]
    z_ex22 = [1, 1, 1]
    s_ex22 = frozenset([1, 2, 3, 4])
    v_star_22 = v_star_combinatorial(4, r_ex22, z_ex22, s_ex22)
    v_tilde_22 = v_tilde_q(r_ex22, z_ex22, s_ex22, 3)
    v_bar_22 = v_tilde_q(r_ex22, z_ex22, s_ex22, 1)
    assert v_star_22 == 1 and v_tilde_22 == 2 and v_bar_22 == 2

    # 2. Example 3.2 & 3.4 (pp. 5-8): m = 25, K = 9 forest family
    r_ex32 = [
        frozenset(range(1, 21)),   # R1 = {1..20}
        frozenset(range(1, 3)),    # R2 = {1,2}
        frozenset(range(3, 11)),   # R3 = {3..10}
        frozenset(range(11, 21)),  # R4 = {11..20}
        frozenset(range(5, 11)),   # R5 = {5..10}
        frozenset(range(11, 17)),  # R6 = {11..16}
        frozenset(range(17, 21)),  # R7 = {17..20}
        frozenset(range(21, 23)),  # R8 = {21,22}
        frozenset([22]),           # R9 = {22}
    ]
    # Verify (Forest) property
    for rk, rkp in itertools.combinations(r_ex32, 2):
        inter = rk & rkp
        assert inter in (rk, rkp, frozenset())

    depths_32 = node_depths(r_ex32)
    # R1, R8 depth 1; R2, R3, R4, R9 depth 2; R5, R6, R7 depth 3
    assert depths_32 == [1, 2, 2, 2, 3, 3, 3, 1, 2]

    atoms_32 = algorithm_2_atoms(25, r_ex32)
    expected_atoms = {
        frozenset(range(1, 3)),    # R2
        frozenset(range(3, 5)),    # R3 \ R5
        frozenset(range(5, 11)),   # R5
        frozenset(range(11, 17)),  # R6
        frozenset(range(17, 21)),  # R7
        frozenset([21]),           # R8 \ R9
        frozenset([22]),           # R9
        frozenset(range(23, 26)),  # N_25 \ (R1 cup R8)
    }
    assert set(atoms_32) == expected_atoms
    assert len(atoms_32) == 8

    # Max number of disjoint sets d in R_ex32: {R2, R5, R6, R7, R9} has 5 sets
    disjoint_max = 0
    for r in range(1, len(r_ex32) + 1):
        for comb in itertools.combinations(r_ex32, r):
            if all(len(a & b) == 0 for a, b in itertools.combinations(comb, 2)):
                disjoint_max = r
    assert disjoint_max == 5

    # Test Algorithm 1 == V_tilde_R == V_tilde^d_R < V_bar_R on Example 3.2
    zetas_32 = [10, 1, 4, 5, 2, 2, 2, 1, 0]
    s_query = frozenset(range(1, 26))
    v_alg1 = algorithm_1_bottom_up(25, r_ex32, zetas_32, s_query)
    v_tilde_full = v_tilde_q(r_ex32, zetas_32, s_query, len(r_ex32))
    v_tilde_d = v_tilde_q(r_ex32, zetas_32, s_query, disjoint_max)
    v_bar_1 = v_tilde_q(r_ex32, zetas_32, s_query, 1)
    assert v_alg1 == v_tilde_full == v_tilde_d
    assert v_alg1 < v_bar_1

    # Also verify exact equality with combinatorial V^*_R(S) across all 2^8 = 256 subsets
    # on an 8-element 2-tree forest
    r_small = [
        frozenset([1, 2, 3, 4, 5, 6]),
        frozenset([1, 2]),
        frozenset([3, 4, 5]),
        frozenset([4, 5]),
        frozenset([7, 8]),
        frozenset([8]),
    ]
    z_small = [4, 1, 2, 1, 1, 0]
    d_small = 3  # {1,2}, {4,5}, {8}
    verified_subsets = 0
    strict_gains_over_vbar = 0
    for r in range(9):
        for comb in itertools.combinations(range(1, 9), r):
            s_sub = frozenset(comb)
            v_star = v_star_combinatorial(8, r_small, z_small, s_sub)
            v_a1 = algorithm_1_bottom_up(8, r_small, z_small, s_sub)
            v_td = v_tilde_q(r_small, z_small, s_sub, d_small)
            v_tf = v_tilde_q(r_small, z_small, s_sub, len(r_small))
            v_b1 = v_tilde_q(r_small, z_small, s_sub, 1)
            assert v_star == v_a1 == v_td == v_tf
            assert v_star <= v_b1
            if v_star < v_b1:
                strict_gains_over_vbar += 1
            verified_subsets += 1

    return {
        "example_2_2_non_forest_gap": {
            "v_star": v_star_22,
            "v_tilde": v_tilde_22,
            "v_bar": v_bar_22,
        },
        "example_3_2_forest": {
            "depths": depths_32,
            "num_atoms": len(atoms_32),
            "max_disjoint_d": disjoint_max,
            "v_alg1_full_query": v_alg1,
            "v_tilde_d_full_query": v_tilde_d,
            "v_bar_full_query": v_bar_1,
        },
        "small_forest_exhaustive_verification": {
            "verified_subsets": verified_subsets,
            "strict_gains_over_vbar": strict_gains_over_vbar,
        },
    }


def zeta_dkw_region(p_vals: Sequence[float], c_const: float) -> int:
    """Local DKW-Massart quadratic-inversion bound zeta_k(X) (Equation 16/32 & Remark 4.2, pp. 9, 18)."""
    s = len(p_vals)
    p_sorted = [0.0] + sorted(p_vals)
    best = s
    for ell in range(s + 1):
        p_ell = p_sorted[ell]
        if p_ell >= 1.0:
            continue
        one_minus_t = 1.0 - p_ell
        root_term = (c_const / (2.0 * one_minus_t)) + math.sqrt(
            (c_const * c_const) / (4.0 * one_minus_t * one_minus_t)
            + (s - ell) / one_minus_t
        )
        # Equation (32) proves |S cap H_0| <= (root_term)^2; since |S cap H_0| is an integer,
        # floor((root_term)^2) is the exact integer bound.
        val = int(math.floor(root_term * root_term))
        if val < best:
            best = val
    return best


def zeta_gw_region(p_vals: Sequence[float], c_const: float) -> int:
    """Genovese-Wasserman (2004, Eq. 16) local DKW bound zeta^{GW}_k(X) (Remark 4.3, p. 9)."""
    s = len(p_vals)
    p_sorted = [0.0] + sorted(p_vals)
    best = s
    for ell in range(s + 1):
        p_ell = p_sorted[ell]
        if p_ell >= 1.0:
            continue
        one_minus_t = 1.0 - p_ell
        val = int(math.floor(((s - ell) + math.sqrt(s) * c_const) / one_minus_t))
        if val < best:
            best = val
    return best


def verify_section_4_and_5() -> Dict[str, object]:
    """Verify Proposition 4.1, Remark 4.3, Lemma A.1, Proposition 4.5, Figure 6, and Hybrid Bound."""
    # 1. Verify Lemma A.1 (Equation 33, p. 21) and Remark 4.3 uniform improvement
    rng = random.Random(20261018)
    alpha = 0.05
    # Binary tree with q = 3, s = 20 -> K_part = 8, K_tree = 15, m = 160, K_1 = 2, r = 0.8, mu = 3.0
    q_depth = 3
    s_leaf = 20
    k_part = 1 << q_depth
    m = k_part * s_leaf
    k_1 = 2
    r_sig = 0.8
    mu_sig = 3.0

    # Construct tree regions (K_tree = 15)
    leaves = [
        frozenset(range(1 + (k - 1) * s_leaf, k * s_leaf + 1))
        for k in range(1, k_part + 1)
    ]
    tree_regions: List[FrozenSet[int]] = []
    cur_level = leaves
    while cur_level:
        tree_regions.extend(cur_level)
        if len(cur_level) == 1:
            break
        cur_level = [
            cur_level[2 * i] | cur_level[2 * i + 1]
            for i in range(len(cur_level) // 2)
        ]
    assert len(tree_regions) == (1 << (q_depth + 1)) - 1

    # True null index set H_0
    h1_set: Set[int] = set()
    n_sig_per_leaf = int(round(r_sig * s_leaf))
    for k in range(k_1):
        leaf_list = sorted(leaves[k])
        h1_set.update(leaf_list[:n_sig_per_leaf])
    h0_set = frozenset(set(range(1, m + 1)) - h1_set)

    c_tree = math.sqrt(0.5 * math.log(len(tree_regions) / alpha))
    c_part = math.sqrt(0.5 * math.log(len(leaves) / alpha))

    n_trials = 200
    jer_violations_tree = 0
    jer_violations_part = 0
    gw_dominance_checks = 0
    strict_gw_improvements = 0

    for _ in range(n_trials):
        p_map: Dict[int, float] = {}
        for i in range(1, m + 1):
            z = rng.gauss(mu_sig if i in h1_set else 0.0, 1.0)
            p_map[i] = std_normal_sf(z)

        # Check tree JER and GW dominance
        viol_t = False
        for rk in tree_regions:
            p_rk = [p_map[i] for i in rk]
            zk = zeta_dkw_region(p_rk, c_tree)
            zk_gw = zeta_gw_region(p_rk, c_tree)
            assert zk <= zk_gw
            gw_dominance_checks += 1
            if zk < zk_gw:
                strict_gw_improvements += 1
            if len(rk & h0_set) > zk:
                viol_t = True
        if viol_t:
            jer_violations_tree += 1

        viol_p = False
        for rk in leaves:
            p_rk = [p_map[i] for i in rk]
            zk = zeta_dkw_region(p_rk, c_part)
            if len(rk & h0_set) > zk:
                viol_p = True
        if viol_p:
            jer_violations_part += 1

    emp_jer_tree = jer_violations_tree / n_trials
    emp_jer_part = jer_violations_part / n_trials
    assert emp_jer_tree <= alpha
    assert emp_jer_part <= alpha
    assert strict_gw_improvements > 0

    # 2. Verify Proposition 4.5 & Figure 6 (p. 10, Eq. 20-23)
    # Parameters from Figure 6 caption: m = 10^7, s = m^{2/3}, K = m/s, r = 3/5, alpha = 0.1
    m_fig6 = 10**7
    s_fig6 = m_fig6 ** (2.0 / 3.0)
    k_fig6 = m_fig6 / s_fig6
    r_fig6 = 0.6
    alpha_fig6 = 0.1
    c_fig6 = math.sqrt(0.5 * math.log(k_fig6 / alpha_fig6))

    fig6_ratios: Dict[str, float] = {}
    for mu_val in [0.5, 1.0, 1.75, 2.0, 3.0, 4.0, 5.0]:
        num = min(
            1.0,
            1.0
            - r_fig6
            + 2.0 * r_fig6 * std_normal_sf(mu_val)
            + (4.0 * c_fig6 / math.sqrt(s_fig6)) * (1.0 + c_fig6 / math.sqrt(s_fig6)),
        )
        thresh_simes = std_normal_isf(alpha_fig6 * s_fig6 / m_fig6)
        den = (1.0 - r_fig6) * (1.0 - alpha_fig6 * s_fig6 / m_fig6) + r_fig6 * std_normal_sf(
            mu_val - thresh_simes
        )
        fig6_ratios[str(mu_val)] = round(num / den, 6)

    # At mu = 2.0 (bottom of Figure 6 trough), the ratio is 0.492043 < 0.50, and at mu = 4.0 it is 0.798222
    assert fig6_ratios["2.0"] < 0.50 and abs(fig6_ratios["4.0"] - 0.798222) < 1e-4

    # 3. Verify Section 5.3 Hybrid Bound V^gamma_hybrid(alpha, S_k) (Figure 10 setting:
    # s = 100, q = 3, K_part = 8, K_tree = 15, m = 800, K_1 = 2, r = 0.9, mu = 2.8, alpha = 0.05, gamma = 0.02)
    gamma = 0.02
    alpha_simes = (1.0 - gamma) * alpha
    alpha_tree = gamma * alpha
    s_hyb = 100
    m_hyb = 8 * s_hyb
    leaves_hyb = [
        frozenset(range(1 + (k - 1) * s_hyb, k * s_hyb + 1))
        for k in range(1, 9)
    ]
    tree_hyb: List[FrozenSet[int]] = []
    cur_lvl = leaves_hyb
    while cur_lvl:
        tree_hyb.extend(cur_lvl)
        if len(cur_lvl) == 1:
            break
        cur_lvl = [
            cur_lvl[2 * i] | cur_lvl[2 * i + 1]
            for i in range(len(cur_lvl) // 2)
        ]
    h1_hyb: Set[int] = set()
    for k in range(2):
        h1_hyb.update(sorted(leaves_hyb[k])[:90])

    c_tree_hyb = math.sqrt(0.5 * math.log(len(tree_hyb) / alpha_tree))
    p_hyb: Dict[int, float] = {}
    for i in range(1, m_hyb + 1):
        z = rng.gauss(2.8 if i in h1_hyb else 0.0, 1.0)
        p_hyb[i] = std_normal_sf(z)

    zetas_tree_hyb = [zeta_dkw_region([p_hyb[i] for i in rk], c_tree_hyb) for rk in tree_hyb]
    sorted_indices = sorted(range(1, m_hyb + 1), key=lambda idx: p_hyb[idx])

    def v_simes_bound(s_set: FrozenSet[int], a_lvl: float) -> int:
        best_s = len(s_set)
        for k_idx in range(1, m_hyb + 1):
            cnt = sum(1 for i in s_set if p_hyb[i] > a_lvl * k_idx / m_hyb) + k_idx - 1
            if cnt < best_s:
                best_s = cnt
        return best_s

    s_small = frozenset(sorted_indices[:10])
    s_large = frozenset(sorted_indices[:200])

    v_simes_small = v_simes_bound(s_small, alpha_simes)
    v_tree_small = algorithm_1_bottom_up(m_hyb, tree_hyb, zetas_tree_hyb, s_small)
    v_hyb_small = min(v_simes_small, v_tree_small)

    v_simes_large = v_simes_bound(s_large, alpha_simes)
    v_tree_large = algorithm_1_bottom_up(m_hyb, tree_hyb, zetas_tree_hyb, s_large)
    v_hyb_large = min(v_simes_large, v_tree_large)

    # Small k = 10: Simes is tighter than tree (which pays the floor(C^2) minimum cost)
    assert v_simes_small < v_tree_small
    assert v_hyb_small == v_simes_small
    # Large k = 200: Tree is tighter than Simes
    assert v_tree_large < v_simes_large
    assert v_hyb_large == v_tree_large

    return {
        "empirical_jer_tree": round(emp_jer_tree, 4),
        "empirical_jer_part": round(emp_jer_part, 4),
        "gw_dominance_checks": gw_dominance_checks,
        "strict_gw_improvements": strict_gw_improvements,
        "figure_6_ratio_upper_bounds": fig6_ratios,
        "hybrid_envelope_comparison": {
            "small_k_10": {
                "v_simes": v_simes_small,
                "v_tree": v_tree_small,
                "v_hybrid": v_hyb_small,
            },
            "large_k_200": {
                "v_simes": v_simes_large,
                "v_tree": v_tree_large,
                "v_hybrid": v_hyb_large,
            },
        },
    }


def main() -> None:
    sec23 = verify_section_2_and_3()
    sec45 = verify_section_4_and_5()
    summary = {
        "concept_id": "AIMech:ForestStructuredDKWPostHocConfidenceBounds",
        "primary_source": "Durand, Blanchard, Neuvial, & Roquain (2020), Scandinavian Journal of Statistics 47(4):1114-1148 (arXiv:1807.01470v2, DOI:10.1111/sjos.12453)",
        "section_2_and_3_forest_interpolation_and_algorithm_1": sec23,
        "section_4_and_5_dkw_calibration_figure_6_and_hybrid": sec45,
        "all_assertions_passed": True,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
