#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 533:
SignGuard: Norm-Based and Sign-Clustering Collaborative Malicious Gradient Filtering
(Xu, Huang, Song, & Lan, ICDCS 2022 / arXiv:2109.05872).
"""

import math
import random


def l2_norm(v):
    return math.sqrt(sum(x * x for x in v))


def median(vals):
    s = sorted(vals)
    m = len(s)
    if m % 2 == 1:
        return s[m // 2]
    return 0.5 * (s[m // 2 - 1] + s[m // 2])


def sign_statistics(g):
    d = len(g)
    pos = sum(1 for x in g if x > 1e-12) / d
    zero = sum(1 for x in g if abs(x) <= 1e-12) / d
    neg = sum(1 for x in g if x < -1e-12) / d
    return (pos, zero, neg)


def two_cluster_partition(features):
    """Deterministic 2-cluster K-means / Mean-Shift style partition on normalized sign stats."""
    # Normalize each feature dimension across clients
    idxs = list(range(len(features)))
    dim = len(features[0])
    norm_f = {i: list(features[i]) for i in idxs}
    for j in range(dim):
        col = [features[i][j] for i in idxs]
        mu = sum(col) / len(col)
        sd = math.sqrt(sum((x - mu) ** 2 for x in col) / len(col)) + 1e-12
        for i in idxs:
            norm_f[i][j] = (features[i][j] - mu) / sd

    # Farthest-pair initialization
    best_pair = (idxs[0], idxs[-1])
    best_dist = -1.0
    for a in idxs:
        for b in idxs:
            dist = sum((norm_f[a][j] - norm_f[b][j]) ** 2 for j in range(dim))
            if dist > best_dist:
                best_dist = dist
                best_pair = (a, b)

    c0 = list(norm_f[best_pair[0]])
    c1 = list(norm_f[best_pair[1]])
    for _ in range(15):
        g0, g1 = [], []
        for i in idxs:
            d0 = sum((norm_f[i][j] - c0[j]) ** 2 for j in range(dim))
            d1 = sum((norm_f[i][j] - c1[j]) ** 2 for j in range(dim))
            if d0 <= d1:
                g0.append(i)
            else:
                g1.append(i)
        if g0:
            c0 = [sum(norm_f[i][j] for i in g0) / len(g0) for j in range(dim)]
        if g1:
            c1 = [sum(norm_f[i][j] for i in g1) / len(g1) for j in range(dim)]
    return g0 if len(g0) >= len(g1) else g1


def signguard_aggregate(gradients, L=0.1, R=3.0):
    n = len(gradients)
    d = len(gradients[0])
    norms = [l2_norm(g) for g in gradients]
    M = median(norms)

    # Step 1: Norm-based filtering (Algorithm 2, Line 2)
    S1 = [i for i in range(n) if L <= (norms[i] / (M + 1e-12)) <= R]

    # Step 2: Sign-based clustering (Algorithm 2, Lines 3-8)
    feats = [sign_statistics(g) for g in gradients]
    S2 = two_cluster_partition(feats)

    # Step 3: Intersection and median-clipped aggregation (Algorithm 2, Lines 9-10)
    S_trusted = sorted(set(S1).intersection(set(S2)))
    if not S_trusted:
        S_trusted = S1

    agg = [0.0] * d
    for i in S_trusted:
        scale = min(1.0, M / (norms[i] + 1e-12))
        for j in range(d):
            agg[j] += gradients[i][j] * scale
    agg = [x / len(S_trusted) for x in agg]
    return agg, S1, S2, S_trusted, M


def main():
    rng = random.Random(20261019)
    d = 60
    # True gradient with 75% positive coordinates and 25% negative coordinates
    g_true = [0.4 if j < 45 else -0.35 for j in range(d)]

    # 6 honest clients with small zero-mean Gaussian noise
    honest_grads = []
    for _ in range(6):
        g_i = [g_true[j] + rng.gauss(0.0, 0.03) for j in range(d)]
        honest_grads.append(g_i)

    # 4 Byzantine clients executing a dual stealth + large-norm ByzMean attack (Eq. 8):
    # 2 stealthy sign-flipping / ALIE-style attackers with honest norm (~M) but inverted signs,
    # and 2 high-magnitude scaling attackers with honest signs but 8x norm.
    byz_stealth = [[-g_true[j] * (1.0 + rng.gauss(0.0, 0.02)) for j in range(d)] for _ in range(2)]
    byz_large = [[g_true[j] * 8.0 for j in range(d)] for _ in range(2)]
    # Make byz_large push in a corrupted direction while keeping positive sign proportions similar
    byz_large = [[(8.0 if g_true[j] > 0 else -8.0) for j in range(d)] for _ in range(2)]

    all_grads = honest_grads + byz_stealth + byz_large

    agg_sg, S1, S2, S_trusted, M = signguard_aggregate(all_grads, L=0.1, R=3.0)

    # Norm-only filter (S1 only) retains byz_stealth (indices 6, 7)
    assert 6 in S1 and 7 in S1, f"Expected stealth attackers in S1, got {S1}"
    assert 8 not in S1 and 9 not in S1, f"Expected large-norm attackers filtered by S1, got {S1}"

    # Sign-only filter (S2 only) retains byz_large (indices 8, 9) because their sign ratios match honest
    assert 8 in S2 and 9 in S2, f"Expected large-norm sign-matching attackers in S2, got {S2}"
    assert 6 not in S2 and 7 not in S2, f"Expected sign-flipped attackers filtered by S2, got {S2}"

    # Intersection S1 \cap S2 retains strictly the 6 honest clients [0, 1, 2, 3, 4, 5]
    assert S_trusted == [0, 1, 2, 3, 4, 5], f"Expected exact honest set, got {S_trusted}"

    # Compare estimation error against Norm-only and Sign-only averages
    norm_only_avg = [sum(all_grads[i][j] for i in S1) / len(S1) for j in range(d)]
    sign_only_avg = [sum(all_grads[i][j] for i in S2) / len(S2) for j in range(d)]

    err_sg = l2_norm([agg_sg[j] - g_true[j] for j in range(d)])
    err_norm_only = l2_norm([norm_only_avg[j] - g_true[j] for j in range(d)])
    err_sign_only = l2_norm([sign_only_avg[j] - g_true[j] for j in range(d)])

    assert err_sg < 0.12
    assert err_norm_only > 0.70
    assert err_sign_only > 10.0

    print(
        f"[PASS] Round 533 SignGuard verified: S1={S1}, S2={S2}, S_trusted={S_trusted}, "
        f"err_sg={err_sg:.4f} << err_norm_only={err_norm_only:.4f} << err_sign_only={err_sign_only:.4f}"
    )


if __name__ == "__main__":
    main()
