#!/usr/bin/env python3
"""Constructed boundary verification for Expando-Mono-Duo T5 (Pradeep, Nogueira, & Lin, 2021, arXiv:2101.05667)."""

import math


def duot5_sum(p: list[list[float]]) -> list[float]:
    """Eq. (5): SUM aggregation s_i = sum_{j != i} p_{i,j}."""
    k1 = len(p)
    return [sum(p[i][j] for j in range(k1) if j != i) for i in range(k1)]


def duot5_sum_log(p: list[list[float]]) -> list[float]:
    """Eq. (6): SUM-LOG aggregation s_i = sum_{j != i} log(p_{i,j})."""
    k1 = len(p)
    return [sum(math.log(p[i][j]) for j in range(k1) if j != i) for i in range(k1)]


def duot5_sym_sum(p: list[list[float]]) -> list[float]:
    """Eq. (7): SYM-SUM aggregation s_i = sum_{j != i} (p_{i,j} + (1 - p_{j,i}))."""
    k1 = len(p)
    return [sum(p[i][j] + (1.0 - p[j][i]) for j in range(k1) if j != i) for i in range(k1)]


def duot5_sym_sum_log(p: list[list[float]]) -> list[float]:
    """Eq. (8): SYM-SUM-LOG aggregation s_i = sum_{j != i} (log(p_{i,j}) + log(1 - p_{j,i}))."""
    k1 = len(p)
    return [
        sum(math.log(p[i][j]) + math.log(1.0 - p[j][i]) for j in range(k1) if j != i)
        for i in range(k1)
    ]


def main() -> None:
    # 1. Stage cardinality invariant: k_N <= ... <= k_1 <= k_0, and duoT5 executes k_1 * (k_1 - 1) inferences
    k0, k1, k2 = 1000, 50, 10
    assert k2 <= k1 <= k0
    duo_inferences = k1 * (k1 - 1)
    assert duo_inferences == 2450, f"Expected 2450 pairwise inferences for k1=50, got {duo_inferences}"

    # 2. Pairwise prompt order sensitivity:
    # Candidate 0 and Candidate 1 have similar forward probabilities p_{i,j} due to position bias toward Document0,
    # but when placed in Document1 position (p_{j,i}), Candidate 0 resists losing (p_{j,0} is small = 0.08)
    # whereas Candidate 1 loses when placed second (p_{j,1} is high = 0.75).
    p_matrix = [
        [0.0, 0.55, 0.80],  # Candidate 0 as Document0: p_{0,1}=0.55, p_{0,2}=0.80 (forward sum = 1.35)
        [0.75, 0.0, 0.65],  # Candidate 1 as Document0: p_{1,0}=0.75, p_{1,2}=0.65 (forward sum = 1.40)
        [0.08, 0.70, 0.0],  # Candidate 2 as Document0: p_{2,0}=0.08, p_{2,1}=0.70
    ]
    # Note: p_{1,0}=0.75 and p_{2,0}=0.08 (average loss against 0 is low when 2 vs 0),
    # whereas p_{0,1}=0.55 and p_{2,1}=0.70 (Candidate 1 loses to both 0 and 2 when in Document1 slot).
    # Adjust p_{1,0}=0.48, p_{1,2}=0.90 so forward SUM favors Candidate 1 (1.38 > 1.35),
    # while SYM-SUM and SYM-SUM-LOG account for (1 - p_{j,i}) and favor Candidate 0!
    p_matrix[1][0] = 0.48
    p_matrix[1][2] = 0.90

    s_sum = duot5_sum(p_matrix)
    s_sum_log = duot5_sum_log(p_matrix)
    s_sym_sum = duot5_sym_sum(p_matrix)
    s_sym_sum_log = duot5_sym_sum_log(p_matrix)

    assert s_sum[1] > s_sum[0], "Asymmetric SUM is fooled by Document0 position bias on (1, 2)"
    assert s_sym_sum[0] > s_sym_sum[1] > s_sym_sum[2], "SYM-SUM corrects position bias via (1 - p_{j,i})"
    assert s_sym_sum_log[0] > s_sym_sum_log[1] > s_sym_sum_log[2], "SYM-SUM-LOG penalizes small probabilities symmetrically"
    assert s_sum_log[0] > s_sum_log[2]

    print("Expando-Mono-Duo T5 boundary verification passed:")
    print(f"  DuoT5 inferences for k1={k1}: {duo_inferences}")
    print(f"  SUM scores:         {[round(x, 4) for x in s_sum]}")
    print(f"  SYM-SUM scores:     {[round(x, 4) for x in s_sym_sum]}")
    print(f"  SYM-SUM-LOG scores: {[round(x, 4) for x in s_sym_sum_log]}")


if __name__ == "__main__":
    main()
