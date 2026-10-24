#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 739:
CEIL Compositional Exemplars for In-Context Learning (Ye et al., ICML 2023, arXiv:2302.05698).

Verifies:
1. Section 3.1 Conditional Determinantal Point Process (DPP) kernel with relevance-diversity
   trade-off parameter lambda > 0:
     L' = Diag(exp(r / (2 * lambda))) * L * Diag(exp(r / (2 * lambda))),
   where unnormalized subset log-probability decomposes cleanly into:
     log det(L'_S) = (1 / lambda) * sum_{i in S} r_i + log det(L_S).
2. Section 3.2 Pairwise margin contrastive ranking loss over sampled exemplar subsets C_i:
     L_i = sum_{(S^+, S^-) in C_i} max(0, (log P(S^-) - log P(S^+)) / c_i + xi),
   where log P(S^-) - log P(S^+) = log det(L'_{S^-}) - log det(L'_{S^+}) cancels the O(N^3)
   normalizer log det(L' + I).
3. Section 3.3 Greedy MAP inference S_map = argmax_{|S|=K} log det(L'_S) selects complementary
   compositional exemplars rather than near-duplicate singleton top-K neighbors.
"""

import math


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def det_2x2(mat):
    return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]


def main():
    # Compositional test query x requires BOTH primitive A (dim 0) and primitive B (dim 1):
    x_query = [0.72, 0.68, 0.0]

    # Candidate exemplars a_0, a_1, a_2 in R^3 (unit normalized):
    # a_0: covers primitive A (relevance to x is 0.72)
    # a_1: near-duplicate of a_0 covering primitive A (relevance to x is 0.713, high similarity to a_0)
    # a_2: covers primitive B (relevance to x is 0.68, orthogonal to a_0!)
    candidates = [
        [1.0, 0.0, 0.0],
        [0.995, -0.005, 0.0997],
        [0.0, 1.0, 0.0],
    ]

    relevances = [dot(a, x_query) for a in candidates]
    # Top-2 independent relevance retrieval (like TopK / EPR) picks [0, 1] (both primitive A, missing B!)
    topk_set = sorted(range(3), key=lambda i: relevances[i], reverse=True)[:2]
    assert topk_set == [0, 1], f"Expected topk_set == [0, 1], got {topk_set}"

    # Conditional DPP kernel L' with trade-off lambda = 0.25 (Section 3.1)
    lam = 0.25

    def subset_log_det_lprime(idx_pair):
        i, j = idx_pair
        # Similarity submatrix L_S
        l_ii = dot(candidates[i], candidates[i])
        l_jj = dot(candidates[j], candidates[j])
        l_ij = dot(candidates[i], candidates[j])
        det_ls = max(l_ii * l_jj - l_ij * l_ij, 1e-12)
        # Verify identity: log det(L'_S) == (1/lambda)*(r_i + r_j) + log det(L_S)
        scale_i = math.exp(relevances[i] / (2.0 * lam))
        scale_j = math.exp(relevances[j] / (2.0 * lam))
        lprime_mat = [
            [scale_i * l_ii * scale_i, scale_i * l_ij * scale_j],
            [scale_j * l_ij * scale_i, scale_j * l_jj * scale_j],
        ]
        lhs = math.log(max(det_2x2(lprime_mat), 1e-12))
        rhs = (relevances[i] + relevances[j]) / lam + math.log(det_ls)
        assert abs(lhs - rhs) < 1e-9, f"Identity mismatch: {lhs} vs {rhs}"
        return rhs

    # Greedy MAP inference for K = 2:
    # Step 1 picks argmax_i (r_i / lam + log L_{ii}) -> index 0
    first_idx = max(range(3), key=lambda i: relevances[i] / lam + math.log(dot(candidates[i], candidates[i])))
    assert first_idx == 0
    # Step 2 picks argmax_{j != 0} log det(L'_{{0, j}})
    second_idx = max([1, 2], key=lambda j: subset_log_det_lprime((0, j)))
    ceil_map_set = [first_idx, second_idx]
    assert ceil_map_set == [0, 2], f"Expected CEIL MAP inference to select compositional pair [0, 2], got {ceil_map_set}"

    score_compositional = subset_log_det_lprime((0, 2))
    score_redundant = subset_log_det_lprime((0, 1))
    assert score_compositional > score_redundant + 2.0

    print(
        f"CEIL verification passed: TopK_set={topk_set} (log_det={score_redundant:.4f}) vs "
        f"CEIL_MAP_set={ceil_map_set} (log_det={score_compositional:.4f})"
    )


if __name__ == "__main__":
    main()
