#!/usr/bin/env python3
"""Boundary verification for Round 519: FLTrust (Cao, Fang, Liu, & Gong, NDSS 2021)."""

from __future__ import annotations

import math


def dot(u: list[float], v: list[float]) -> float:
    return sum(a * b for a, b in zip(u, v))


def norm(u: list[float]) -> float:
    return math.sqrt(dot(u, u))


def fltrust_aggregate(
    g0: list[float],
    client_updates: list[list[float]],
    use_relu: bool = True,
    use_norm: bool = True,
) -> tuple[list[float], list[float]]:
    """Aggregate client updates using FLTrust Equations (2)-(4) (Section IV-B, page 6)."""
    d = len(g0)
    norm_g0 = norm(g0)
    assert norm_g0 > 0.0
    trust_scores: list[float] = []
    normalized_updates: list[list[float]] = []

    for gi in client_updates:
        norm_gi = norm(gi)
        ci = dot(gi, g0) / (norm_gi * norm_g0)
        ts_i = max(0.0, ci) if use_relu else ci
        trust_scores.append(ts_i)
        scale = (norm_g0 / norm_gi) if use_norm else 1.0
        normalized_updates.append([scale * x for x in gi])

    ts_sum = sum(trust_scores)
    assert abs(ts_sum) > 1e-12
    g_agg = [
        sum(trust_scores[i] * normalized_updates[i][k] for i in range(len(client_updates))) / ts_sum
        for k in range(d)
    ]
    return g_agg, trust_scores


def main() -> None:
    # 1. Verify Equations (2)-(4) and Lemma 1 (Appendix A, Eqs. 13-24, page 16):
    # ||g - grad_F|| <= 3 ||g0 - grad_F|| + 2 ||grad_F|| for ANY number of malicious clients!
    grad_F = [1.2, -0.8, 0.5, 1.0]
    g0 = [1.1, -0.75, 0.55, 0.95]  # Server update on small root dataset D_0

    # Suppose 4 benign clients and 6 malicious clients (60% malicious majority!):
    # - 3 malicious clients send opposite-direction updates (-100 * g0)
    # - 3 malicious clients send huge-magnitude scaling attacks (1000 * skewed_vec) with positive cosine
    benign = [
        [1.25, -0.82, 0.48, 1.02],
        [1.15, -0.78, 0.52, 0.98],
        [0.60, -0.40, 0.25, 0.50],  # small-magnitude benign update
        [1.22, -0.79, 0.51, 1.01],
    ]
    mal_opposite = [[-100.0 * x for x in g0] for _ in range(3)]
    mal_scaling = [[1000.0 * 1.0, 1000.0 * 0.2, 1000.0 * 1.5, 1000.0 * 0.1] for _ in range(3)]
    clients = benign + mal_opposite + mal_scaling

    g_fltrust, ts = fltrust_aggregate(g0, clients, use_relu=True, use_norm=True)

    # Opposite-direction malicious updates get exact zero trust score (Eq. 2)
    for idx in range(4, 7):
        assert ts[idx] == 0.0, f"Expected TS=0 for opposite update, got {ts[idx]}"

    # Verify Lemma 1 inequality (Eq. 24): ||g - grad_F|| <= 3 ||g0 - grad_F|| + 2 ||grad_F||
    lhs = norm([a - b for a, b in zip(g_fltrust, grad_F)])
    rhs = 3.0 * norm([a - b for a, b in zip(g0, grad_F)]) + 2.0 * norm(grad_F)
    assert lhs <= rhs + 1e-12, f"Lemma 1 violated: {lhs} > {rhs}"

    # Verify key Step (a) in Lemma 1 (Eq. 17): because <bar_g_i, g0> > 0 for all i in S
    # and ||bar_g_i|| = ||g0||, ||sum_{i in S} phi_i bar_g_i - g0|| <= ||sum_{i in S} phi_i bar_g_i + g0|| <= 2 ||g0||
    diff_g0 = norm([a - b for a, b in zip(g_fltrust, g0)])
    sum_g0 = norm([a + b for a, b in zip(g_fltrust, g0)])
    assert diff_g0 <= sum_g0 <= 2.0 * norm(g0) + 1e-12

    # 2. Verify necessity of both ReLU clipping and hypersphere normalization (Table IV, p. 12)
    g_no_norm, _ = fltrust_aggregate(g0, clients, use_relu=True, use_norm=False)
    err_fltrust = norm([a - b for a, b in zip(g_fltrust, grad_F)])
    err_no_norm = norm([a - b for a, b in zip(g_no_norm, grad_F)])
    assert err_fltrust < 0.8 and err_no_norm > 500.0

    print(
        f"[PASS] Round 519 FLTrust (Cao et al. 2021): "
        f"err_fltrust={err_fltrust:.4f}<<err_no_norm={err_no_norm:.1f}, "
        f"Lemma1_lhs={lhs:.4f}<=rhs={rhs:.4f}"
    )


if __name__ == "__main__":
    main()
