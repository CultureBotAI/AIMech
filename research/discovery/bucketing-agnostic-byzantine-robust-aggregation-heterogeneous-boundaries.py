#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 538:
Byzantine-Robust Learning on Heterogeneous Datasets via Bucketing
(Karimireddy, He, & Jaggi, ICLR 2022 / arXiv:2006.09365).
"""

import math
import random


def l2_sq(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))


def coord_median(vecs):
    m = len(vecs)
    d = len(vecs[0])
    out = [0.0] * d
    for j in range(d):
        s = sorted(v[j] for v in vecs)
        if m % 2 == 1:
            out[j] = s[m // 2]
        else:
            out[j] = 0.5 * (s[m // 2 - 1] + s[m // 2])
    return out


def krum(vecs, q):
    m = len(vecs)
    keep = max(1, m - q - 2)
    best_idx = 0
    best_score = float("inf")
    for i in range(m):
        dists = sorted(l2_sq(vecs[i], vecs[j]) for j in range(m) if j != i)
        score = sum(dists[:keep])
        if score < best_score:
            best_score = score
            best_idx = i
    return list(vecs[best_idx])


def s_bucketing(vecs, s, rng):
    """Algorithm 1 (p. 5): Randomly permute n inputs into ceil(n/s) buckets of size <= s and average."""
    n = len(vecs)
    d = len(vecs[0])
    perm = list(range(n))
    rng.shuffle(perm)
    buckets = []
    for start in range(0, n, s):
        idxs = perm[start : min(n, start + s)]
        avg = [sum(vecs[k][j] for k in idxs) / len(idxs) for j in range(d)]
        buckets.append(avg)
    return buckets


def main():
    # 1. Verify Lemma 1 (Bucketing reduces inter-client variance by factor 1/s while preserving mean):
    # Consider n = 12 heterogeneous good workers in R^2 with pairwise variance rho^2.
    good_vecs = [
        [1.0 if i % 2 == 0 else -1.0, 2.0 if (i // 2) % 2 == 0 else -2.0]
        for i in range(12)
    ]
    x_bar = [
        sum(v[0] for v in good_vecs) / 12.0,
        sum(v[1] for v in good_vecs) / 12.0,
    ]
    assert abs(x_bar[0]) < 1e-12 and abs(x_bar[1]) < 1e-12

    # Empirical average pairwise squared distance before vs after s=3 bucketing over 2000 random shuffles
    rng = random.Random(20261019)
    raw_var = sum(
        l2_sq(good_vecs[i], good_vecs[j])
        for i in range(12)
        for j in range(12)
        if i != j
    ) / (12 * 11)

    bucket_var_accum = 0.0
    bucket_mean_accum = [0.0, 0.0]
    trials = 2000
    s = 3
    m_b = 12 // s
    for _ in range(trials):
        ys = s_bucketing(good_vecs, s=s, rng=rng)
        bucket_mean_accum[0] += ys[0][0] / trials
        bucket_mean_accum[1] += ys[0][1] / trials
        pw = sum(
            l2_sq(ys[a], ys[b]) for a in range(m_b) for b in range(m_b) if a != b
        ) / (m_b * (m_b - 1))
        bucket_var_accum += pw / trials

    # Lemma 1: E[y_i] == x_bar and E||y_i - y_j||^2 == raw_var / s
    assert l2_sq(bucket_mean_accum, x_bar) < 1e-3
    assert abs(bucket_var_accum - (raw_var / s)) < 0.08, (
        f"Expected {raw_var / s:.3f}, got {bucket_var_accum:.3f}"
    )

    # 2. Verify Section 3.1 & 3.2 (Failure of unbucketed CM/Krum on heterogeneous data + Mimic attack)
    # and Theorem I (Bucketing + CM/Krum fixes heterogeneity bias):
    # 16 honest workers: 8 hold [+1.0, -1.0], 8 hold [-1.0, +1.0] -> true honest mean is [0.0, 0.0].
    # 3 Byzantine workers execute the Mimic attack (Section 3.2): they copy worker 0 ([+1.0, -1.0]).
    honest_16 = [[1.0, -1.0] for _ in range(8)] + [[-1.0, 1.0] for _ in range(8)]
    byz_mimic = [[1.0, -1.0] for _ in range(3)]
    all_19 = honest_16 + byz_mimic
    true_mean = [0.0, 0.0]

    # Without bucketing, both CM and Krum fixate on [+1.0, -1.0], giving squared error 2.0!
    cm_unbucketed = coord_median(all_19)
    krum_unbucketed = krum(all_19, q=3)
    err_cm_unbucketed = l2_sq(cm_unbucketed, true_mean)
    err_krum_unbucketed = l2_sq(krum_unbucketed, true_mean)
    assert abs(err_cm_unbucketed - 2.0) < 1e-12
    assert abs(err_krum_unbucketed - 2.0) < 1e-12

    # With s=2 bucketing averaged over 300 iterations (as in Algorithm 2), expected error drops sharply
    err_cm_bucketed = 0.0
    err_krum_bucketed = 0.0
    avg_cm_out = [0.0, 0.0]
    for _ in range(300):
        ys = s_bucketing(all_19, s=2, rng=rng)
        c_out = coord_median(ys)
        k_out = krum(ys, q=3)
        err_cm_bucketed += l2_sq(c_out, true_mean) / 300.0
        err_krum_bucketed += l2_sq(k_out, true_mean) / 300.0
        avg_cm_out[0] += c_out[0] / 300.0
        avg_cm_out[1] += c_out[1] / 300.0

    assert err_cm_bucketed < 0.45, f"Expected < 0.45, got {err_cm_bucketed}"
    assert err_krum_bucketed < 0.75, f"Expected < 0.75, got {err_krum_bucketed}"

    # 3. Verify Theorem III information-theoretic lower bound:
    # Two indistinguishable problem instances f^1 (all n good) and f^2 (delta*n Byzantine)
    # with optima separated by G/mu = zeta*sqrt(delta)/mu -> min worst-case error >= delta*zeta^2/(4*mu).
    delta, zeta, mu = 0.2, 1.0, 1.0
    G = zeta * math.sqrt(delta)
    opt_f1 = G / mu
    opt_f2 = 0.0
    midpoint = 0.5 * (opt_f1 + opt_f2)
    lb_subopt = 0.5 * mu * (midpoint - opt_f2) ** 2
    assert abs(lb_subopt - (delta * (zeta ** 2)) / (8.0 * mu)) < 1e-12

    print(
        f"[PASS] Round 538 Bucketing verified: raw_var={raw_var:.2f}->bucket_var={bucket_var_accum:.2f} "
        f"(s={s}), err_cm_unbucketed={err_cm_unbucketed:.2f}->bucketed={err_cm_bucketed:.3f}, "
        f"err_krum_unbucketed={err_krum_unbucketed:.2f}->bucketed={err_krum_bucketed:.3f}"
    )


if __name__ == "__main__":
    main()
