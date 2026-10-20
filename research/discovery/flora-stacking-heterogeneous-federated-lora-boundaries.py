#!/usr/bin/env python3
"""Constructed boundary verification for FLoRA (Wang et al., NeurIPS 2024, arXiv:2409.05976).

Verifies:
1. Exact noise-free block-stacking aggregation identity across heterogeneous client ranks {r_k}
   (Eqs. 9-12, pp. 4-6):
   For A = p_0 A_0 (+) p_1 A_1 (+) ... (+) p_K A_K in R^{(sum r_k) x n} (vertical stacking) and
   B = B_0 (+) B_1 (+) ... (+) B_K in R^{m x (sum r_k)} (horizontal stacking),
   B * A == sum_{k=0}^K p_k B_k A_k holds to machine precision (~1e-16) for arbitrary heterogeneous ranks!
2. Non-zero cross-term aggregation noise in homogeneous FedIT (Eq. 6, p. 3) and zero-padded
   heterogeneous FedIT (Section 4.1-4.2, pp. 6-7):
   (sum_k p_k B_k)(sum_k p_k A_k) != sum_k p_k B_k A_k due to cross-client products p_i p_j B_i A_j (i != j)
   and squared weights p_k^2 on diagonal terms.
3. Rank-1 sub-module random permutation invariance (Section 5, p. 9):
   Decomposing B and A into R_tot = sum_k r_k rank-1 outer products and permuting columns of B and rows of A
   by any permutation pi in S_{R_tot} preserves B_pi * A_pi == B * A exactly while hiding client blocks.
"""

import math
import random


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    m = len(a)
    r = len(a[0])
    n = len(b[0])
    assert len(b) == r
    return [[sum(a[i][t] * b[t][j] for t in range(r)) for j in range(n)] for i in range(m)]


def matadd(a: list[list[float]], b: list[list[float]], scale_a: float = 1.0, scale_b: float = 1.0) -> list[list[float]]:
    return [[scale_a * a[i][j] + scale_b * b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def frob_norm(a: list[list[float]]) -> float:
    return math.sqrt(sum(v * v for row in a for v in row))


def flora_stack_aggregate(
    b_list: list[list[list[float]]],
    a_list: list[list[list[float]]],
    p_weights: list[float],
) -> tuple[list[list[float]], list[list[float]]]:
    """Eq. 11 (p. 6): Vertically stack p_k * A_k and horizontally stack B_k."""
    m = len(b_list[0])
    n = len(a_list[0][0])
    # Vertically stack p_k * A_k
    a_stacked: list[list[float]] = []
    for a_k, p_k in zip(a_list, p_weights):
        assert len(a_k[0]) == n
        for row in a_k:
            a_stacked.append([p_k * val for val in row])

    # Horizontally stack B_k
    b_stacked: list[list[float]] = [[] for _ in range(m)]
    for b_k in b_list:
        assert len(b_k) == m
        for i in range(m):
            b_stacked[i].extend(b_k[i])

    return b_stacked, a_stacked


def main() -> None:
    rng = random.Random(20240909)
    m, n = 5, 4
    # Three clients with heterogeneous LoRA ranks r_0 = 1, r_1 = 2, r_2 = 3 (total stacked rank = 6)
    ranks = [1, 2, 3]
    p_weights = [0.2, 0.3, 0.5]

    b_list = []
    a_list = []
    for r_k in ranks:
        b_k = [[rng.uniform(-1.0, 1.0) for _ in range(r_k)] for _ in range(m)]
        a_k = [[rng.uniform(-1.0, 1.0) for _ in range(n)] for _ in range(r_k)]
        b_list.append(b_k)
        a_list.append(a_k)

    # Exact target global update: Delta W* = sum_{k=0}^K p_k * B_k * A_k (Eq. 5, p. 3)
    delta_w_true = [[0.0] * n for _ in range(m)]
    for b_k, a_k, p_k in zip(b_list, a_list, p_weights):
        delta_w_true = matadd(delta_w_true, matmul(b_k, a_k), 1.0, p_k)

    # 1. Verify FLoRA stacking aggregation (Eq. 11, p. 6) achieves exact zero aggregation error
    b_stack, a_stack = flora_stack_aggregate(b_list, a_list, p_weights)
    assert len(b_stack) == m and len(b_stack[0]) == sum(ranks)
    assert len(a_stack) == sum(ranks) and len(a_stack[0]) == n
    delta_w_flora = matmul(b_stack, a_stack)
    flora_err = frob_norm(matadd(delta_w_flora, delta_w_true, 1.0, -1.0))
    assert flora_err < 1e-15, f"Expected machine-zero FLoRA stacking error, got {flora_err}"

    # 2. Verify zero-padded FedIT aggregation (Eq. 3 & Eq. 6, pp. 3, 6) introduces substantial error
    r_max = max(ranks)
    b_fedit = [[0.0] * r_max for _ in range(m)]
    a_fedit = [[0.0] * n for _ in range(r_max)]
    for b_k, a_k, p_k, r_k in zip(b_list, a_list, p_weights, ranks):
        for i in range(m):
            for c in range(r_k):
                b_fedit[i][c] += p_k * b_k[i][c]
        for r_idx in range(r_k):
            for j in range(n):
                a_fedit[r_idx][j] += p_k * a_k[r_idx][j]

    delta_w_fedit = matmul(b_fedit, a_fedit)
    fedit_err = frob_norm(matadd(delta_w_fedit, delta_w_true, 1.0, -1.0))
    assert fedit_err > 0.5, f"Expected large FedIT zero-padding aggregation noise, got {fedit_err}"

    # 3. Verify rank-1 sub-module random permutation privacy defense (Section 5, p. 9)
    r_tot = sum(ranks)
    perm = list(range(r_tot))
    rng.shuffle(perm)
    b_perm = [[b_stack[i][perm[c]] for c in range(r_tot)] for i in range(m)]
    a_perm = [[a_stack[perm[c]][j] for j in range(n)] for c in range(r_tot)]
    delta_w_perm = matmul(b_perm, a_perm)
    perm_err = frob_norm(matadd(delta_w_perm, delta_w_true, 1.0, -1.0))
    assert perm_err < 1e-15

    print("FLoRA boundary verification passed:", {
        "stacked_rank": r_tot,
        "flora_err": flora_err,
        "fedit_zeropad_err": round(fedit_err, 6),
        "perm_err": perm_err,
    })


if __name__ == "__main__":
    main()
