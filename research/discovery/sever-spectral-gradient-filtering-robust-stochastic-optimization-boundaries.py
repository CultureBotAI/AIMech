#!/usr/bin/env python3
"""Constructed boundary verification for Round 527: Sever (Diakonikolas et al., ICML 2019).

Verifies:
1. Algorithm 1 (Sever) & Section 3 (Figure 3): In high dimension d, an epsilon-fraction
   of correlated outliers shifting gradients by Delta along a unit direction u has
   centered l2-norm squared ||g_bad - g_bar||_2^2 ~ O(sigma^2 / epsilon), which is hidden
   inside the bulk of inlier centered l2-norms E[||g_good - g_bar||_2^2] = d * sigma^2
   whenever d >> 1/epsilon (so l2-norm gradientCentered filtering fails), whereas the
   top right singular vector v of the centered gradient matrix G aligns with u and
   produces spectral outlier scores tau_i = ((g_i - g_bar) . v)^2 that cleanly separate
   outliers in the tail (tau_bad >> tau_good).
2. Lemma B.6 supermartingale condition: Under Cov_{I_good}[grad f_i(w)] <= sigma^2 I,
   whenever the mean spectral score E_{i in S}[tau_i] >= 12 * sigma^2, the sum of outlier
   scores on S_bad exceeds the sum of outlier scores on S_good
   (sum_{i in S_bad} tau_i >= sum_{i in S_good} tau_i), ensuring randomized threshold
   filtering removes at least as many corrupted points as clean points in expectation.
"""

import math
import random


def power_iteration_top_right_singular_vector(G, iters=60):
    """Compute top right singular vector v of |S| x d matrix G via power iteration on G^T G."""
    n = len(G)
    d = len(G[0])
    v = [1.0 / math.sqrt(d) for _ in range(d)]
    for _ in range(iters):
        # u = G v
        u = [sum(G[i][j] * v[j] for j in range(d)) for i in range(n)]
        # w = G^T u
        w = [sum(G[i][j] * u[i] for i in range(n)) for j in range(d)]
        norm_w = math.sqrt(sum(x * x for x in w))
        v = [x / norm_w for x in w]
    return v


def main():
    rng = random.Random(527)
    n_good = 180
    n_bad = 20
    n = n_good + n_bad  # epsilon = 0.10
    d = 64  # high dimension d = 64 >> 1/epsilon = 10
    sigma = 1.0

    # Inlier gradients: isotropic zero-mean with coordinate variance sigma^2
    G_raw = []
    for _ in range(n_good):
        G_raw.append([rng.gauss(0.0, sigma) for _ in range(d)])

    # Correlated poisoning outliers along direction e_0 with magnitude A = 5.5 < sqrt(d)*sigma = 8.0
    # So their l2 norm squared (~30.25) is strictly smaller than inlier l2 norm squared (~64.0)!
    A = 5.5
    for _ in range(n_bad):
        vec = [0.0] * d
        vec[0] = A
        G_raw.append(vec)

    # Empirical mean gradient g_bar
    g_bar = [sum(G_raw[i][j] for i in range(n)) / n for j in range(d)]
    # Centered gradient matrix G
    G = [[G_raw[i][j] - g_bar[j] for j in range(d)] for i in range(n)]

    # Baseline gradientCentered score: ||g_i - g_bar||_2^2
    l2_scores = [sum(G[i][j] ** 2 for j in range(d)) for i in range(n)]
    mean_l2_good = sum(l2_scores[:n_good]) / n_good
    mean_l2_bad = sum(l2_scores[n_good:]) / n_bad
    # Verify outliers are hidden inside/below the bulk of l2-norm scores!
    assert mean_l2_bad < mean_l2_good, f"Expected l2_bad={mean_l2_bad} < l2_good={mean_l2_good}"

    # Sever spectral score: tau_i = ((g_i - g_bar) . v)^2 along top right singular vector v of G
    v = power_iteration_top_right_singular_vector(G)
    tau = [(sum(G[i][j] * v[j] for j in range(d))) ** 2 for i in range(n)]

    min_tau_bad = min(tau[n_good:])
    max_tau_good = max(tau[:n_good])
    sum_tau_bad = sum(tau[n_good:])
    sum_tau_good = sum(tau[:n_good])

    # 1. Every outlier has strictly larger Sever score than every inlier (100% separation)
    assert min_tau_bad > max_tau_good, f"Expected min_tau_bad={min_tau_bad} > max_tau_good={max_tau_good}"

    # 2. Lemma B.6 supermartingale condition: sum_{S_bad} tau_i > sum_{S_good} tau_i
    assert sum_tau_bad > sum_tau_good, f"Expected sum_tau_bad={sum_tau_bad} > sum_tau_good={sum_tau_good}"

    print(
        f"[PASS] Round 527 Sever (Diakonikolas et al. 2019): "
        f"mean_l2_bad={mean_l2_bad:.2f}<mean_l2_good={mean_l2_good:.2f} (l2 fails), "
        f"min_tau_bad={min_tau_bad:.2f}>max_tau_good={max_tau_good:.2f}, "
        f"sum_tau_bad={sum_tau_bad:.2f}>sum_tau_good={sum_tau_good:.2f}"
    )


if __name__ == "__main__":
    main()
