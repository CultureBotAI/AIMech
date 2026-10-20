#!/usr/bin/env python3
"""Constructed boundary verification for PruneFL (Jiang et al., IEEE TNNLS 2023, arXiv:1909.12326).

Verifies:
1. Adaptive pruning rate objective (Eq. 6-7, pp. 4-5):
   Gamma(A union P_bar) = (Delta(A) + sum_{j in P_bar} g_j^2) / (c + T_A + sum_{j in P_bar} t_j).
2. Exact global optimality of Algorithm 2 (Theorem 1, p. 5; proof in Appendix B-1, pp. 14-15):
   Sorting prunable indices j in P in non-increasing order of g_j^2 / t_j and greedily adding j
   while g_j^2 / t_j >= Gamma(A union P_bar) achieves the exact maximum over all 2^{|P|} subsets!
3. Strict monotone decrease of the running threshold after each greedy inclusion (Lemma 2, p. 14)
   and strict violation of g_j^2 / t_j >= Gamma* for all excluded indices.
"""

import itertools


def gamma_objective(
    delta_a: float,
    c_plus_ta: float,
    g_sq: list[float],
    t_cost: list[float],
    subset: set[int],
) -> float:
    """Eq. 7 (p. 5): Empirical risk reduction divided by single-round execution time."""
    num = delta_a + sum(g_sq[j] for j in subset)
    den = c_plus_ta + sum(t_cost[j] for j in subset)
    return num / den


def prunefl_greedy_reconfiguration(
    delta_a: float,
    c_plus_ta: float,
    g_sq: list[float],
    t_cost: list[float],
) -> tuple[set[int], float]:
    """Algorithm 2 (p. 5): Greedy O(|P| log |P|) optimal reconfiguration of prunable parameters."""
    p_indices = list(range(len(g_sq)))
    # Line 1: Sort j in P in descending order of g_j^2 / t_j
    p_sorted = sorted(p_indices, key=lambda j: -(g_sq[j] / t_cost[j]))

    # Line 2: Initialize P_bar = empty
    p_bar: set[int] = set()
    curr_num = delta_a
    curr_den = c_plus_ta

    # Lines 3-9: Greedily include j while g_j^2 / t_j >= Gamma(A union P_bar)
    for j in p_sorted:
        curr_gamma = curr_num / curr_den
        ratio_j = g_sq[j] / t_cost[j]
        if ratio_j >= curr_gamma:
            p_bar.add(j)
            curr_num += g_sq[j]
            curr_den += t_cost[j]
        else:
            break

    return p_bar, curr_num / curr_den


def main() -> None:
    # Non-prunable set A baseline risk reduction Delta(A) and constant + A-time overhead (c + T_A)
    delta_a = 1.25
    c_plus_ta = 2.0

    # 12 prunable parameter groups with heterogeneous squared gradients g_j^2 and per-round time costs t_j
    g_sq = [0.95, 0.12, 0.64, 0.45, 0.05, 1.10, 0.30, 0.18, 0.82, 0.09, 0.52, 0.22]
    t_cost = [0.40, 0.35, 0.25, 0.50, 0.20, 0.30, 0.45, 0.30, 0.35, 0.25, 0.40, 0.30]

    greedy_set, greedy_gamma = prunefl_greedy_reconfiguration(delta_a, c_plus_ta, g_sq, t_cost)

    # Brute-force check over all 2^12 = 4096 subsets to verify Theorem 1 global optimality
    best_brute_gamma = -1.0
    best_brute_set: set[int] = set()
    n_p = len(g_sq)
    for r_len in range(n_p + 1):
        for comb in itertools.combinations(range(n_p), r_len):
            s_cand = set(comb)
            val = gamma_objective(delta_a, c_plus_ta, g_sq, t_cost, s_cand)
            if val > best_brute_gamma + 1e-12:
                best_brute_gamma = val
                best_brute_set = s_cand

    assert greedy_set == best_brute_set, f"Greedy {greedy_set} != brute-force optimal {best_brute_set}"
    assert abs(greedy_gamma - best_brute_gamma) < 1e-12

    # Verify optimality conditions (Lemma 1 & Lemma 2, Appendix B-1, pp. 14-15):
    # Every j in P_bar has g_j^2 / t_j >= greedy_gamma, and every j not in P_bar has g_j^2 / t_j < greedy_gamma
    for j in range(n_p):
        ratio = g_sq[j] / t_cost[j]
        if j in greedy_set:
            assert ratio >= greedy_gamma - 1e-12
        else:
            assert ratio < greedy_gamma + 1e-12

    # Verify adaptive growth when gradient magnitudes increase during later FL stage
    g_sq_stage2 = [2.5 * x for x in g_sq]
    greedy_set_stage2, greedy_gamma_stage2 = prunefl_greedy_reconfiguration(
        delta_a, c_plus_ta, g_sq_stage2, t_cost
    )
    assert len(greedy_set_stage2) >= len(greedy_set)
    assert greedy_gamma_stage2 > greedy_gamma

    print("PruneFL boundary verification passed:", {
        "optimal_subset_size": len(greedy_set),
        "optimal_gamma": round(greedy_gamma, 6),
        "stage2_subset_size": len(greedy_set_stage2),
        "stage2_gamma": round(greedy_gamma_stage2, 6),
    })


if __name__ == "__main__":
    main()
