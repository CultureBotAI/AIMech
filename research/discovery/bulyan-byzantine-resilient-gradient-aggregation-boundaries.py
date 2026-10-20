#!/usr/bin/env python3
"""Boundary verification for Round 518: Bulyan (El Mhamdi, Guerraoui, & Rouault, ICML 2018)."""

from __future__ import annotations

import math
import random


def l2_sq(u: list[float], v: list[float]) -> float:
    return sum((a - b) ** 2 for a, b in zip(u, v))


def krum_index(vectors: list[list[float]], f: int) -> int:
    """Return index of Krum winner among current candidate vectors."""
    m = len(vectors)
    k_neighbors = m - f - 2
    assert k_neighbors >= 1, f"Need m >= f + 3, got m={m}, f={f}"
    best_i = 0
    best_score = float("inf")
    for i in range(m):
        dists = sorted(l2_sq(vectors[i], vectors[j]) for j in range(m) if j != i)
        score = sum(dists[:k_neighbors])
        if score < best_score:
            best_score = score
            best_i = i
    return best_i


def bulyan_krum(vectors: list[list[float]], f: int) -> tuple[list[float], list[list[float]]]:
    """Run Bulyan(Krum) on n >= 4f + 3 vectors in R^d (Section 4, page 5)."""
    n = len(vectors)
    assert n >= 4 * f + 3, f"Bulyan requires n >= 4f + 3, got n={n}, f={f}"
    theta = n - 2 * f
    beta = theta - 2 * f
    assert theta >= 2 * f + 3 and beta >= 3

    remaining = [list(v) for v in vectors]
    selected: list[list[float]] = []
    while len(selected) < theta:
        idx = krum_index(remaining, f)
        selected.append(remaining.pop(idx))

    d = len(vectors[0])
    g_out = [0.0] * d
    for coord in range(d):
        vals = [x[coord] for x in selected]
        # Median defined in Section 4: argmin_{m = Y[i], Y in S} sum_{Z in S} |Z[i] - m|
        med = min(vals, key=lambda m: sum(abs(z - m) for z in vals))
        closest_beta = sorted(vals, key=lambda x: abs(x - med))[:beta]
        g_out[coord] = sum(closest_beta) / beta
    return g_out, selected


def main() -> None:
    rng = random.Random(518)
    # 1. Verify high-dimensional single-coordinate leeway attack on Krum (Section 3.2)
    # Minimal Bulyan quorum for f=2 is n = 4f + 3 = 11 workers (9 honest, 2 Byzantine)
    f = 2
    n = 4 * f + 3
    n_honest = n - f
    d = 200
    true_grad = [1.0] * d
    sigma = 0.25

    honest = [
        [true_grad[j] + rng.gauss(0.0, sigma) for j in range(d)]
        for _ in range(n_honest)
    ]
    mean_honest = [
        sum(honest[i][j] for i in range(n_honest)) / n_honest for j in range(d)
    ]

    # Omniscient single-coordinate attack B(gamma) = mean_honest + gamma * E_0 (Section 3.2)
    # Because B(gamma) has 0 variance on coordinates 1..d-1 and f identical copies,
    # Krum selects B(gamma) even when gamma = O(sigma * sqrt(d)) >> sigma!
    gamma_attack = 2.8  # > 11x single-coordinate honest std sigma=0.25
    byz = [[mean_honest[0] + gamma_attack] + mean_honest[1:] for _ in range(f)]
    all_proposals = honest + byz

    krum_winner_idx = krum_index(all_proposals, f)
    krum_winner = all_proposals[krum_winner_idx]
    # Krum selects the poisoned Byzantine vector!
    assert krum_winner_idx >= n_honest, "Expected Krum to select the single-coordinate poisoned vector"
    krum_coord0_err = abs(krum_winner[0] - true_grad[0])
    assert krum_coord0_err > 2.5

    # 2. Verify Bulyan(Krum) Proposition 2: each coordinate of Bulyan is bracketed by
    # honest workers and suppresses the single-coordinate leeway to O(sigma)
    bulyan_grad, selected_set = bulyan_krum(all_proposals, f)
    bulyan_coord0_err = abs(bulyan_grad[0] - true_grad[0])
    assert bulyan_coord0_err < 0.25, f"Expected Bulyan coord-0 error < 0.25, got {bulyan_coord0_err}"
    assert bulyan_coord0_err < krum_coord0_err / 15.0

    # Verify Proposition 2 bracketing property: for every coordinate i, Bulyan's output
    # lies strictly between the minimum and maximum of honest workers' i-th coordinates
    for coord in range(d):
        h_min = min(h[coord] for h in honest)
        h_max = max(h[coord] for h in honest)
        assert h_min - 1e-12 <= bulyan_grad[coord] <= h_max + 1e-12

    print(
        f"[PASS] Round 518 Bulyan (El Mhamdi et al. 2018): "
        f"krum_coord0_err={krum_coord0_err:.3f}>>bulyan_coord0_err={bulyan_coord0_err:.4f}, "
        f"bracketed_all_d={d}"
    )


if __name__ == "__main__":
    main()
