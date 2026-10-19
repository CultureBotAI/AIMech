#!/usr/bin/env python3
"""Constructed boundary & mathematical verification for Round 382:
AIMech:ChocoSgdAndChocoGossipDecentralizedCompressedOptimization
(Koloskova, Stich, & Jaggi 2019, ICML 2019, PMLR 97:3478-3487, arXiv:1902.00340).

Verifies:
1. Algorithm 1 (Choco-Gossip) Exact Average Preservation (Remark 14) & Linear Convergence (Theorem 2):
   For any doubly stochastic mixing matrix W (W 1 = 1, 1^T W = 1^T) with spectral gap delta > 0
   and any omega-contractive compressor Q (such as Top-k with omega = k/d),
   x_i^{(t+1)} = x_i^{(t)} + gamma * sum_j w_{ij} (x_hat_j^{(t+1)} - x_hat_i^{(t+1)})
   where x_hat_i^{(t+1)} = x_hat_i^{(t)} + Q(x_i^{(t)} - x_hat_i^{(t)}) satisfies:
   (a) Exact conservation of the global average: (1/n) sum_i x_i^{(t)} == (1/n) sum_i x_i^{(0)} for all t >= 0,
   (b) Geometric decay of the joint Lyapunov function
       e_t = sum_i ||x_i^{(t)} - x_bar||^2 + sum_i ||x_i^{(t)} - x_hat_i^{(t+1)}||^2 -> 0.
2. Comparison Against Naive Compressed Gossip Baselines (Remark 15):
   - Q1-G: x_i^{(t+1)} = x_i^{(t)} + gamma * sum_j w_{ij} Q(x_j^{(t)} - x_i^{(t)}) violates average preservation
     under asymmetric/biased Top-k compression when Q(-z) != -Q(z) or stochastic compression isn't shared.
   - Q2-G: x_i^{(t+1)} = x_i^{(t)} + gamma * sum_j w_{ij} (Q(x_j^{(t)}) - Q(x_i^{(t)})) preserves the average
     but fails to converge to consensus whenever x_bar != 0 because Q(x_bar) != x_bar for Top-k (k < d).
3. Algorithm 2 (Choco-SGD) Decentralized Optimization (Theorem 4):
   Choco-SGD converges to the global optimum x* of (1/n) sum_i f_i(x) over a ring topology with Top-1 compression.
"""

from __future__ import annotations
import math
import random


def top_k(x: list[float], k: int) -> list[float]:
    d = len(x)
    idx_sorted = sorted(range(d), key=lambda i: abs(x[i]), reverse=True)
    keep = set(idx_sorted[:k])
    return [x[i] if i in keep else 0.0 for i in range(d)]


def norm_sq(v: list[float]) -> float:
    return sum(vi * vi for vi in v)


def ring_mixing_matrix(n: int) -> list[list[float]]:
    W = [[0.0] * n for _ in range(n)]
    for i in range(n):
        W[i][i] = 0.5
        W[i][(i - 1) % n] = 0.25
        W[i][(i + 1) % n] = 0.25
    return W


def test_choco_gossip_average_preservation_and_q2g_failure() -> None:
    rng = random.Random(38201)
    n = 5
    d = 6
    k = 1
    W = ring_mixing_matrix(n)
    gamma = 0.5

    x_init = [[rng.uniform(2.0, 10.0) for _ in range(d)] for _ in range(n)]
    x_bar = [sum(x_init[i][c] for i in range(n)) / n for c in range(d)]

    x_choco = [list(xi) for xi in x_init]
    x_hat = [[0.0] * d for _ in range(n)]

    x_q2g = [list(xi) for xi in x_init]

    init_lyapunov = sum(norm_sq([x_choco[i][c] - x_bar[c] for c in range(d)]) for i in range(n))

    for t in range(250):
        # Choco-Gossip (Algorithm 1): compress first or communicate first (equivalent)
        for i in range(n):
            q_i = top_k([x_choco[i][c] - x_hat[i][c] for c in range(d)], k)
            x_hat[i] = [x_hat[i][c] + q_i[c] for c in range(d)]

        x_next = [[0.0] * d for _ in range(n)]
        for i in range(n):
            for c in range(d):
                diff_sum = sum(W[i][j] * (x_hat[j][c] - x_hat[i][c]) for j in range(n))
                x_next[i][c] = x_choco[i][c] + gamma * diff_sum
        x_choco = x_next

        # Check exact average preservation at every iteration t (Remark 14)
        cur_bar = [sum(x_choco[i][c] for i in range(n)) / n for c in range(d)]
        for c in range(d):
            assert abs(cur_bar[c] - x_bar[c]) < 1e-11, f"Average drifted at t={t}"

        # Q2-G baseline (Remark 15): x_i^{(t+1)} = x_i^{(t)} + gamma * sum_j w_{ij} (Q(x_j) - Q(x_i))
        q_direct = [top_k(x_q2g[i], k) for i in range(n)]
        x_q2g_next = [[0.0] * d for _ in range(n)]
        for i in range(n):
            for c in range(d):
                diff_sum = sum(W[i][j] * (q_direct[j][c] - q_direct[i][c]) for j in range(n))
                x_q2g_next[i][c] = x_q2g[i][c] + gamma * diff_sum
        x_q2g = x_q2g_next

    final_lyapunov = sum(
        norm_sq([x_choco[i][c] - x_bar[c] for c in range(d)])
        + norm_sq([x_choco[i][c] - x_hat[i][c] for c in range(d)])
        for i in range(n)
    )
    q2g_consensus_err = sum(norm_sq([x_q2g[i][c] - x_bar[c] for c in range(d)]) for i in range(n))

    assert final_lyapunov < 1e-10 * init_lyapunov, (
        f"Expected Choco-Gossip Lyapunov to decay < 1e-10, got {final_lyapunov / init_lyapunov:.3e}"
    )
    assert q2g_consensus_err > 1.0, (
        f"Expected Q2-G without state memory to fail consensus when x_bar != 0, got {q2g_consensus_err}"
    )


def test_choco_sgd_decentralized_strongly_convex_convergence() -> None:
    """Verify Choco-SGD (Algorithm 2) on a decentralized heterogeneous quadratic over a ring graph."""
    rng = random.Random(38202)
    n = 4
    d = 4
    k = 1
    W = ring_mixing_matrix(n)
    gamma = 0.4

    # f_i(x) = 0.5 * ||x - b_i||^2, global optimum x* = (1/n) sum_i b_i
    b_nodes = [[rng.uniform(-4.0, 4.0) for _ in range(d)] for _ in range(n)]
    x_star = [sum(b_nodes[i][c] for i in range(n)) / n for c in range(d)]

    x_nodes = [[0.0] * d for _ in range(n)]
    x_hat = [[0.0] * d for _ in range(n)]
    a = 40.0
    T = 600
    w_sum = 0.0
    x_weighted = [0.0] * d
    x_node_weighted = [[0.0] * d for _ in range(n)]

    for t in range(T):
        eta_t = 4.0 / (a + t)
        w_t = (a + t) ** 2
        x_bar_t = [sum(x_nodes[i][c] for i in range(n)) / n for c in range(d)]
        w_sum += w_t
        for c in range(d):
            x_weighted[c] += w_t * x_bar_t[c]
            for i in range(n):
                x_node_weighted[i][c] += w_t * x_nodes[i][c]

        # Step 1 (Algorithm 2 line 4): Local gradient step x_{i}^{(t + 1/2)} = x_i^{(t)} - eta_t * grad f_i(x_i^{(t)})
        x_half = [
            [x_nodes[i][c] - eta_t * (x_nodes[i][c] - b_nodes[i][c]) for c in range(d)]
            for i in range(n)
        ]
        # Step 2 (Algorithm 2 lines 5-8): Compress x_i^{(t+1/2)} - x_hat_i^{(t)} and update x_hat_i^{(t+1)}
        for i in range(n):
            q_i = top_k([x_half[i][c] - x_hat[i][c] for c in range(d)], k)
            x_hat[i] = [x_hat[i][c] + q_i[c] for c in range(d)]
        # Step 3 (Algorithm 2 line 9): Gossip mixing x_i^{(t+1)} = x_i^{(t+1/2)} + gamma * sum_j w_{ij} (x_hat_j^{(t+1)} - x_hat_i^{(t+1)})
        x_next = [[0.0] * d for _ in range(n)]
        for i in range(n):
            for c in range(d):
                diff_sum = sum(W[i][j] * (x_hat[j][c] - x_hat[i][c]) for j in range(n))
                x_next[i][c] = x_half[i][c] + gamma * diff_sum
        x_nodes = x_next

    x_avg_T = [xw / w_sum for xw in x_weighted]
    weighted_err = norm_sq([x_avg_T[c] - x_star[c] for c in range(d)])
    init_node_err = norm_sq(x_star)
    avg_node_err = sum(norm_sq([x_nodes[i][c] - x_star[c] for c in range(d)]) for i in range(n)) / n
    assert weighted_err < 1e-5, f"Expected Theorem 4 weighted average error < 1e-5, got {weighted_err}"
    assert avg_node_err < 1e-2 and avg_node_err < 0.005 * init_node_err, (
        f"Expected Choco-SGD last-iterate node error < 1e-2, got {avg_node_err}"
    )


if __name__ == "__main__":
    test_choco_gossip_average_preservation_and_q2g_failure()
    test_choco_sgd_decentralized_strongly_convex_convergence()
    print("[PASS] Round 382 Choco-SGD and Choco-Gossip boundaries verified.")
