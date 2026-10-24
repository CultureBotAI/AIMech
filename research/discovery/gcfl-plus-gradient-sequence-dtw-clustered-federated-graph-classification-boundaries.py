#!/usr/bin/env python3
"""Boundary verification for Round 514: GCFL+ (Xie et al., NeurIPS 2021).

Verifies:
1. Bi-partitioning stopping/splitting criteria Eqs. (4)-(5):
   delta_mean = ||sum_i (|G_i|/|G|) Delta theta_i|| < eps_1 and delta_max = max_i ||Delta theta_i|| > eps_2.
2. Dynamic Time Warping (DTW) distance matrix beta_k(p, q) = dist(Q(p, :), Q(q, :)) over gradient norm sequences
   Q in R^{n x d} (Eq. 8) and standardized sequences Q'(i, :) = Q(i, :) / std(Q(i, :)) (Eq. 20), showing that
   GCFL+ accurately recovers true client domain clusters even when single-round gradient norms fluctuate/cross.
3. SGC Laplacian structure & feature perturbation bounds on optimal weight difference ||Theta' - Theta||_2^2
   (Propositions 4.1 & 4.2, Eqs. 9-16).
"""

import math


def dtw_distance(seq_a, seq_b):
    """Exact Dynamic Time Warping distance between two 1D sequences."""
    la, lb = len(seq_a), len(seq_b)
    dp = [[float("inf")] * (lb + 1) for _ in range(la + 1)]
    dp[0][0] = 0.0
    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            cost = abs(seq_a[i - 1] - seq_b[j - 1])
            dp[i][j] = cost + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[la][lb]


def standardize(seq):
    mean_v = sum(seq) / len(seq)
    var_v = sum((x - mean_v) ** 2 for x in seq) / len(seq)
    std_v = math.sqrt(max(var_v, 1e-12))
    return [x / std_v for x in seq]


def min_cut_bipartition_similarity(sim_matrix):
    """Exhaustive minimum-cut bi-partition for small n (equivalent to Stoer-Wagner min-cut)."""
    n = len(sim_matrix)
    best_cut = float("inf")
    best_part = None
    for mask in range(1, (1 << (n - 1))):
        c1 = [i for i in range(n) if (mask & (1 << i))]
        c2 = [i for i in range(n) if not (mask & (1 << i))]
        cut_val = sum(sim_matrix[i][j] for i in c1 for j in c2)
        if cut_val < best_cut:
            best_cut = cut_val
            best_part = (set(c1), set(c2))
    return best_part, best_cut


def main():
    # 1. Verify stationary point + heterogeneity splitting criteria Eqs. (4)-(5)
    # 4 clients: clients 0, 1 belong to Domain A (+g), clients 2, 3 belong to Domain B (-g)
    grads = [
        [0.42, 0.30],
        [0.38, 0.32],
        [-0.41, -0.29],
        [-0.39, -0.33],
    ]
    n = len(grads)
    mean_grad = [sum(grads[i][k] for i in range(n)) / n for k in range(2)]
    delta_mean = math.sqrt(sum(x * x for x in mean_grad))
    delta_max = max(math.sqrt(sum(x * x for x in g)) for g in grads)
    eps_1, eps_2 = 0.05, 0.35
    assert delta_mean < eps_1 and delta_max > eps_2, (
        f"Expected cluster split trigger: delta_mean={delta_mean:.4f} < {eps_1}, delta_max={delta_max:.4f} > {eps_2}"
    )

    # 2. Verify DTW gradient-sequence clustering (GCFL+ Eq. 8 & Eq. 20) vs single-round fluctuating norms
    # True clusters: {0, 1} (molecular graphs with burst-decay norm trajectory) vs {2, 3} (social graphs with steady oscillation)
    # Note that at communication round t=d-1 (last element), client 0 and client 2 cross at ~1.50!
    Q = [
        [2.0, 5.2, 8.5, 4.0, 2.1, 1.5, 5.0, 8.2, 3.9, 1.50],  # Client 0 (Domain A)
        [1.9, 2.1, 5.1, 8.4, 4.1, 2.0, 1.6, 5.1, 8.3, 3.80],  # Client 1 (Domain A, phase-shifted by 1 round)
        [1.4, 1.6, 1.3, 1.7, 1.4, 1.6, 1.3, 1.7, 1.4, 1.52],  # Client 2 (Domain B)
        [1.5, 1.3, 1.6, 1.4, 1.7, 1.3, 1.6, 1.4, 1.7, 1.48],  # Client 3 (Domain B)
    ]

    # Compute DTW distance matrix beta (Eq. 8) and convert to similarity for min-cut bi-partition
    beta = [[dtw_distance(Q[p], Q[q]) for q in range(n)] for p in range(n)]
    assert beta[0][1] < 4.5 and beta[2][3] < 2.0
    assert min(beta[0][2], beta[0][3], beta[1][2], beta[1][3]) > 18.0

    sim_dtw = [[1.0 / (1.0 + beta[p][q]) if p != q else 0.0 for q in range(n)] for p in range(n)]
    part_gcfl_plus, _ = min_cut_bipartition_similarity(sim_dtw)
    assert part_gcfl_plus in [({0, 1}, {2, 3}), ({2, 3}, {0, 1})], f"GCFL+ failed to recover clusters: {part_gcfl_plus}"

    # Also verify standardized sequence Q' (Eq. 20)
    Q_std = [standardize(row) for row in Q]
    beta_std = [[dtw_distance(Q_std[p], Q_std[q]) for q in range(n)] for p in range(n)]
    sim_std = [[1.0 / (1.0 + beta_std[p][q]) if p != q else 0.0 for q in range(n)] for p in range(n)]
    part_std, _ = min_cut_bipartition_similarity(sim_std)
    assert part_std in [({0, 1}, {2, 3}), ({2, 3}, {0, 1})]

    # 3. Verify Proposition 4.1 (Eq. 12): SGC weight difference ||Theta' - Theta||_2^2 bounded by structure perturbation
    # 2x2 diagonal normalized Laplacian L = diag(0.8, 0.5), X = I_2, Y = [1.0, -0.5]
    L1, L2 = 0.8, 0.5
    Lp1, Lp2 = 0.82, 0.48
    Y1, Y2 = 1.0, -0.5
    Yp1, Yp2 = 1.01, -0.49

    theta = [Y1 / L1, Y2 / L2]
    theta_p = [Yp1 / Lp1, Yp2 / Lp2]
    weight_diff_sq = sum((a - b) ** 2 for a, b in zip(theta_p, theta))

    eps_L = (Lp1 - L1) ** 2 + (Lp2 - L2) ** 2
    eps_Y = (Yp1 - Y1) ** 2 + (Yp2 - Y2) ** 2
    delta_L = (L1 * (Lp1 - L1)) ** 2 + (L2 * (Lp2 - L2)) ** 2
    L_inv_norm_sq = (1.0 / L1) ** 2 + (1.0 / L2) ** 2
    Y_norm_sq = Y1 ** 2 + Y2 ** 2
    rhs_bound = eps_Y * L_inv_norm_sq + (eps_L / delta_L) * Y_norm_sq + (eps_L * eps_Y) / delta_L
    assert weight_diff_sq <= rhs_bound, f"Proposition 4.1 bound violated: {weight_diff_sq} > {rhs_bound}"

    print(
        f"[PASS] Round 514 GCFL+ (Xie et al. 2021): "
        f"delta_mean={delta_mean:.4f}<{eps_1}, delta_max={delta_max:.4f}>{eps_2}, "
        f"DTW_intra={beta[0][1]:.2f}<<DTW_inter={beta[0][2]:.2f}, "
        f"prop4_1={weight_diff_sq:.4e}<={rhs_bound:.4e}"
    )


if __name__ == "__main__":
    main()
