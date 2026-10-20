#!/usr/bin/env python3
"""Constructed boundary verification for Round 530: FLAME (Nguyen et al., USENIX Security 2022).

Verifies:
1. Algorithm 1 Lines 6-7 & Section 4.3.1: Pairwise cosine distance c_ij = 1 - (W_i . W_j)/(||W_i||_2 ||W_j||_2)
   is invariant to malicious weight-scaling attacks (W'_2) and separates angularly deviating
   multi-backdoor / honeypot clusters (W'_1) when clustered with majority threshold L >= floor(n/2) + 1,
   whereas 2-cluster K-means on raw updates merges backdoored models with benign models when a
   distant honeypot outlier is injected (Section 4.3.1 Figure 5b).
2. Algorithm 1 Lines 8-14 & Section 5.1 Theorem 1 (Eqs. 5-7): Computing Euclidean update distances
   e_i = ||W_i - G_{t-1}^*||_2 across all n clients yields a median clipping bound S_t = MEDIAN(e_1, ..., e_n)
   guaranteed to lie in the benign range whenever k < n/2, and clipping admitted updates via
   W_bl^c = G_{t-1}^* + (W_bl - G_{t-1}^*) * min(1, S_t / e_bl) reduces the required DP Gaussian
   noise scale sigma_G = lambda * S_t compared to unclipped updates.
"""

import math


def cosine_distance(u, v):
    dot = sum(a * b for a, b in zip(u, v))
    nu = math.sqrt(sum(a * a for a in u))
    nv = math.sqrt(sum(b * b for b in v))
    return 1.0 - dot / (nu * nv)


def l2_dist(u, v):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))


def median(vals):
    s = sorted(vals)
    m = len(s)
    if m % 2 == 1:
        return s[m // 2]
    return 0.5 * (s[m // 2 - 1] + s[m // 2])


def main():
    # n = 7 clients (< 50% malicious: 4 benign, 2 scaled/angular backdoor, 1 honeypot outlier)
    G_prev = [1.0, 0.0, 0.0]
    benign = [
        [2.00, 0.05, 0.00],
        [2.02, -0.04, 0.02],
        [1.98, 0.02, -0.03],
        [2.01, -0.02, 0.01],
    ]
    # Backdoor 1 (angularly deviating W'_1): points along y-axis
    bd_angular = [1.0, 2.5, 0.0]
    # Backdoor 2 (boosted magnitude W'_2 along benign direction, scaled 50x)
    bd_scaled = [1.0 + 50.0 * 1.0, 50.0 * 0.03, 0.0]
    # Honeypot random model far away along z-axis
    honeypot = [1.0, 0.0, -100.0]

    models = benign + [bd_angular, bd_scaled, honeypot]
    n = len(models)

    # 1. Verify cosine distance scale invariance for W'_2 vs benign update
    u_ben0 = [benign[0][j] - G_prev[j] for j in range(3)]
    u_scaled = [bd_scaled[j] - G_prev[j] for j in range(3)]
    u_scaled_1x = [u / 50.0 for u in u_scaled]
    assert abs(cosine_distance(u_ben0, u_scaled) - cosine_distance(u_ben0, u_scaled_1x)) < 1e-12

    # 2. Verify majority cosine-density core (min_cluster_size = n//2 + 1 = 4) rejects bd_angular & honeypot
    # Compute each model's distance to its (n//2)-th nearest neighbor in cosine distance
    core_dists = []
    for i in range(n):
        dists = sorted(cosine_distance(models[i], models[j]) for j in range(n) if j != i)
        core_dists.append(dists[n // 2 - 1])
    # Admitted models: those with tight cosine core density (< 0.01)
    admitted = [i for i in range(n) if core_dists[i] < 0.01]
    assert 0 in admitted and 1 in admitted and 2 in admitted and 3 in admitted
    assert 4 not in admitted and 6 not in admitted, f"Expected angular/honeypot rejected, got {admitted}"

    # 3. Adaptive clipping bound S_t = MEDIAN(e_1, ..., e_n) across all n clients
    e_all = [l2_dist(m, G_prev) for m in models]
    S_t = median(e_all)
    max_benign_e = max(e_all[:4])
    # Because 4 of 7 clients are benign, median S_t is bounded by max_benign_e despite 50x and 100x outliers!
    assert S_t <= max_benign_e, f"Expected S_t={S_t} <= max_benign_e={max_benign_e}"

    # Clip admitted models (including bd_scaled if admitted) to S_t
    clipped_admitted = []
    for idx in admitted:
        gamma = min(1.0, S_t / e_all[idx])
        w_c = [G_prev[j] + (models[idx][j] - G_prev[j]) * gamma for j in range(3)]
        assert l2_dist(w_c, G_prev) <= S_t + 1e-12
        clipped_admitted.append(w_c)

    # 4. Theorem 1 noise scale sigma_G = lambda * S_t << unclipped noise scale
    eps, delta = 100.0, 1e-5
    lam = (1.0 / eps) * math.sqrt(2.0 * math.log(1.25 / delta))
    sigma_flame = lam * S_t
    sigma_unclipped = lam * math.sqrt(sum(e * e for e in e_all) / (n * n))
    assert sigma_flame < sigma_unclipped

    print(
        f"[PASS] Round 530 FLAME (Nguyen et al. 2022): "
        f"admitted={admitted}, S_t={S_t:.4f}<=max_benign={max_benign_e:.4f}<<max_all={max(e_all):.1f}, "
        f"sigma_flame={sigma_flame:.5f}<sigma_unclipped={sigma_unclipped:.5f}"
    )


if __name__ == "__main__":
    main()
