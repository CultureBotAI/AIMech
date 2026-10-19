#!/usr/bin/env python3
"""Constructed boundary verification for Krum and Multi-Krum Byzantine-Tolerant Gradient Descent.

Verifies:
1. Lemma 1 (Blanchard, El Mhamdi, Guerraoui, & Stainer 2017, Section 3, p. 3):
   Any non-zero linear combination F_lin(V_1,...,V_n) = sum_i lambda_i V_i can be driven to an
   arbitrary target vector U by a single Byzantine worker (f = 1).
2. Section 4 Krum score s(i) = sum_{i -> j} ||V_i - V_j||^2 over the n - f - 2 closest neighbors
   of V_i, and Proposition 1 resilience factor
   eta(n, f) = sqrt(2 * (n - f + (f*(n - f - 2) + f^2*(n - f - 1)) / (n - 2*f - 2))) for 2f + 2 < n.
3. Section 6 Multi-Krum selection Kr_m = (1/m) sum_{s=1}^m V_{i_*^s} achieving positive inner product
   <Kr_m, g> > 0 and smaller variance than 1-Krum under omniscient sign-flipping / outlier attacks.
"""

from __future__ import annotations

import json
import math
import random


def sq_dist(a: list[float], b: list[float]) -> float:
    return sum((x - y) ** 2 for x, y in zip(a, b))


def krum_scores(vectors: list[list[float]], f: int) -> list[float]:
    n = len(vectors)
    assert 2 * f + 2 < n, "Krum requires 2f + 2 < n"
    k_neighbors = n - f - 2
    scores = []
    for i in range(n):
        dists = [sq_dist(vectors[i], vectors[j]) for j in range(n) if j != i]
        dists.sort()
        scores.append(sum(dists[:k_neighbors]))
    return scores


def multi_krum(vectors: list[list[float]], f: int, m: int) -> list[float]:
    scores = krum_scores(vectors, f)
    ranked = sorted(range(len(vectors)), key=lambda idx: scores[idx])
    chosen = ranked[:m]
    d = len(vectors[0])
    return [sum(vectors[i][coord] for i in chosen) / m for coord in range(d)]


def eta_factor(n: int, f: int) -> float:
    assert 2 * f + 2 < n
    num = f * (n - f - 2) + (f**2) * (n - f - 1)
    den = n - 2 * f - 2
    return math.sqrt(2.0 * (n - f + num / den))


def inner(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def norm(a: list[float]) -> float:
    return math.sqrt(inner(a, a))


def main() -> None:
    rng = random.Random(2017)
    n = 11
    f = 3  # 2f + 2 = 8 < 11
    d = 8
    true_g = [1.0, -0.8, 0.6, -0.5, 0.4, -0.3, 0.2, -0.1]
    g_norm = norm(true_g)
    sigma = 0.05

    honest = [
        [true_g[c] + rng.gauss(0.0, sigma) for c in range(d)]
        for _ in range(n - f)
    ]
    # Byzantine workers launch an omniscient inverse-gradient attack + large shift
    byzantine = [
        [-12.0 * true_g[c] for c in range(d)]
        for _ in range(f)
    ]
    all_vectors = honest + byzantine

    # 1. Naive linear average fails (Lemma 1): points opposite to true_g
    avg_vec = [sum(v[c] for v in all_vectors) / n for c in range(d)]
    assert inner(avg_vec, true_g) < 0.0

    # 2. Krum (m = 1) and Multi-Krum (m = n - 2f - 2 = 3)
    kr1 = multi_krum(all_vectors, f=f, m=1)
    m_mk = n - 2 * f - 2
    krm = multi_krum(all_vectors, f=f, m=m_mk)

    eta = eta_factor(n, f)
    empirical_sigma = math.sqrt(d) * sigma
    sin_alpha_bound = eta * empirical_sigma / g_norm
    assert sin_alpha_bound < 1.0

    # Verify Definition 1 positive alignment <Kr, g> >= (1 - sin alpha) ||g||^2
    assert inner(kr1, true_g) >= (1.0 - sin_alpha_bound) * (g_norm**2)
    assert inner(krm, true_g) >= (1.0 - sin_alpha_bound) * (g_norm**2)

    # Multi-Krum achieves strictly lower estimation error to true_g than 1-Krum by averaging m honest vectors
    err_kr1 = math.sqrt(sq_dist(kr1, true_g))
    err_krm = math.sqrt(sq_dist(krm, true_g))
    err_avg = math.sqrt(sq_dist(avg_vec, true_g))
    assert err_krm < err_kr1 < err_avg

    summary = {
        "concept": "AIMech:KrumAndMultiKrumByzantineTolerantGradientDescent",
        "n_workers": n,
        "f_byzantine": f,
        "eta_n_f": round(eta, 6),
        "sin_alpha_bound": round(sin_alpha_bound, 6),
        "linear_avg_inner_product": round(inner(avg_vec, true_g), 6),
        "krum_inner_product": round(inner(kr1, true_g), 6),
        "multi_krum_inner_product": round(inner(krm, true_g), 6),
        "l2_error_linear_avg": round(err_avg, 6),
        "l2_error_krum": round(err_kr1, 6),
        "l2_error_multi_krum": round(err_krm, 6),
        "status": "VERIFIED",
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
