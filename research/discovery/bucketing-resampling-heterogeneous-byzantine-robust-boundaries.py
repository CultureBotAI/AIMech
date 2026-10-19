#!/usr/bin/env python3
"""Constructed boundary verification for Bucketing Resampling for Heterogeneous Byzantine-Robust
Optimization (Karimireddy, He, & Jaggi 2022, ICLR 2022, arXiv:2006.09365).

Verifies:
1. Section 3 Mimic Attack failure mode: When honest workers have heterogeneous data (two clusters
   around -mu_het and +mu_het with true average 0) and delta-fraction Byzantine workers mimic one
   cluster, unbucketed Krum and Coordinate-wise Median consistently bias toward the mimicked cluster.
2. Section 4 Algorithm 1 (s-bucketing) and Lemma 1: Randomly partitioning n vectors into ceil(n/s)
   buckets of size s and averaging within each bucket reduces expected pairwise variance between
   honest bucket averages by a factor of 1/s: E||y_i - y_j||^2 <= rho^2 / s while keeping the
   corrupted bucket fraction <= delta * s.
3. Theorem I: Composing Krum or Coordinate-wise Median with s-bucketing drastically reduces
   expected squared error E||Aggr(Bucket_s(X)) - x_bar_good||^2 under the Mimic attack.
"""

from __future__ import annotations

import json
import math
import random


def sq_dist(a: list[float], b: list[float]) -> float:
    return sum((x - y) ** 2 for x, y in zip(a, b))


def krum_one(vectors: list[list[float]], f: int) -> list[float]:
    n = len(vectors)
    k = max(1, n - f - 2)
    best_idx = 0
    best_score = float("inf")
    for i in range(n):
        dists = sorted(sq_dist(vectors[i], vectors[j]) for j in range(n) if j != i)
        score = sum(dists[:k])
        if score < best_score:
            best_score = score
            best_idx = i
    return vectors[best_idx]


def coord_median(vectors: list[list[float]]) -> list[float]:
    n = len(vectors)
    d = len(vectors[0])
    out = []
    for k in range(d):
        col = sorted(vectors[i][k] for i in range(n))
        if n % 2 == 1:
            out.append(col[n // 2])
        else:
            out.append(0.5 * (col[n // 2 - 1] + col[n // 2]))
    return out


def bucket_vectors(
    vectors: list[list[float]], s: int, rng: random.Random
) -> list[list[float]]:
    n = len(vectors)
    d = len(vectors[0])
    perm = list(range(n))
    rng.shuffle(perm)
    buckets = []
    for start in range(0, n, s):
        idxs = perm[start : start + s]
        m_b = len(idxs)
        buckets.append([sum(vectors[i][k] for i in idxs) / m_b for k in range(d)])
    return buckets


def main() -> None:
    rng = random.Random(2022)
    n_good = 20
    n_bad = 2  # delta = 2/22 < 1/10
    n_total = n_good + n_bad
    s = 2
    d = 4

    # Honest workers split evenly into two heterogeneous groups: +2.0 and -2.0 (true good mean = 0)
    good_vectors = []
    for i in range(n_good):
        sign = 1.0 if i < (n_good // 2) else -1.0
        good_vectors.append([sign * 2.0 + rng.gauss(0.0, 0.05) for _ in range(d)])

    good_mean = [sum(v[k] for v in good_vectors) / n_good for k in range(d)]

    # Compute empirical pairwise variance among good workers before bucketing vs after s-bucketing
    raw_pairs = [
        sq_dist(good_vectors[i], good_vectors[j])
        for i in range(n_good)
        for j in range(i + 1, n_good)
    ]
    rho_sq_raw = sum(raw_pairs) / len(raw_pairs)

    trials = 200
    bucket_pair_acc = 0.0
    err_krum_raw = 0.0
    err_krum_bkt = 0.0
    err_cm_raw = 0.0
    err_cm_bkt = 0.0

    # Mimic attack: Byzantine workers copy the first worker in the +2.0 cluster
    mimic_vec = list(good_vectors[0])
    all_vectors = good_vectors + [mimic_vec for _ in range(n_bad)]

    for _ in range(trials):
        # 1. Verify Lemma 1 variance reduction on good workers
        b_good = bucket_vectors(good_vectors, s=s, rng=rng)
        m_bg = len(b_good)
        bg_pairs = [
            sq_dist(b_good[i], b_good[j])
            for i in range(m_bg)
            for j in range(i + 1, m_bg)
        ]
        bucket_pair_acc += sum(bg_pairs) / len(bg_pairs)

        # 2. Compare unbucketed vs s-bucketed Krum and Coordinate-wise Median under Mimic attack
        kr_raw = krum_one(all_vectors, f=n_bad)
        cm_raw = coord_median(all_vectors)
        err_krum_raw += sq_dist(kr_raw, good_mean)
        err_cm_raw += sq_dist(cm_raw, good_mean)

        b_all = bucket_vectors(all_vectors, s=s, rng=rng)
        kr_bkt = krum_one(b_all, f=n_bad)
        cm_bkt = coord_median(b_all)
        err_krum_bkt += sq_dist(kr_bkt, good_mean)
        err_cm_bkt += sq_dist(cm_bkt, good_mean)

    rho_sq_bkt = bucket_pair_acc / trials
    err_krum_raw /= trials
    err_krum_bkt /= trials
    err_cm_raw /= trials
    err_cm_bkt /= trials

    # Lemma 1: bucketed variance is reduced by ~1/s
    assert rho_sq_bkt < 0.6 * rho_sq_raw
    # Theorem I: bucketing significantly reduces Mimic bias for both Krum and Coordinate-wise Median
    assert err_krum_bkt < 0.55 * err_krum_raw
    assert err_cm_bkt < 0.35 * err_cm_raw

    summary = {
        "concept": "AIMech:BucketingResamplingForHeterogeneousByzantineRobustOptimization",
        "s_bucket_size": s,
        "pairwise_variance_raw": round(rho_sq_raw, 4),
        "pairwise_variance_bucketed": round(rho_sq_bkt, 4),
        "mimic_mse_krum_raw": round(err_krum_raw, 4),
        "mimic_mse_krum_bucketed": round(err_krum_bkt, 4),
        "mimic_mse_cm_raw": round(err_cm_raw, 4),
        "mimic_mse_cm_bucketed": round(err_cm_bkt, 4),
        "status": "VERIFIED",
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
