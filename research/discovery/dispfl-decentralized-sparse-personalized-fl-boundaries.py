#!/usr/bin/env python3
"""Constructed boundary verification for DisPFL (Dai et al., ICML 2022, PMLR 162:4587-4604, arXiv:2206.00187).

Verifies:
1. Erdos-Renyi Kernel (ERK) layer-wise sparsity allocation where layer active density scales
   with (n_{l-1} + n_l + w_l + h_l) / (n_{l-1} * n_l * w_l * h_l) while maintaining target
   overall active parameter budget s_small = (1 - s) * d.
2. Intersection-weighted decentralized sparse averaging (Algorithm 1 line 7, p. 4):
   w_{k, t+1/2} = ((w_{k,t} + sum_{j in S_{k,t}} w_{j,t}) / (m_{k,t} + sum_{j in S_{k,t}} m_{j,t})) odot m_{k,t},
   ensuring coordinates active on a subset of neighbors are averaged strictly over the active count
   and masked to client k's support m_{k,t}.
3. Dynamic mask update via weight-magnitude pruning and gradient-magnitude regrowth (Algorithm 2, p. 13):
   pruning alpha_t fraction of active weights with smallest |w| and regrowing the exact same number
   of inactive weights with largest |g(w)|, preserving ||m_{k,t+1}||_0 == ||m_{k,t}||_0.
4. Cosine annealing schedule alpha_t = (alpha / 2) * (1 + cos(t * pi / (N * T_end))) (Section 3.2, p. 4).
"""

import math


def erk_layer_active_counts(layer_dims: list[tuple[int, int]], target_density: float) -> list[int]:
    """Compute ERK active parameter counts per linear layer (in_dim, out_dim)."""
    raw_scores = [(n_in + n_out) / (n_in * n_out) for (n_in, n_out) in layer_dims]
    caps = [n_in * n_out for (n_in, n_out) in layer_dims]
    total_params = sum(caps)
    target_active = int(round(target_density * total_params))
    raw_weighted = [raw_scores[i] * caps[i] for i in range(len(layer_dims))]
    scale = target_active / sum(raw_weighted)
    counts = [min(caps[i], int(round(scale * raw_weighted[i]))) for i in range(len(layer_dims))]
    diff = target_active - sum(counts)
    counts[-1] += diff
    return counts


def decentralized_sparse_average(
    w_k: list[float],
    m_k: list[int],
    neighbor_weights: list[list[float]],
    neighbor_masks: list[list[int]],
) -> list[float]:
    """Algorithm 1 line 7 (p. 4): coordinate-wise active-count normalization masked by m_k."""
    d = len(w_k)
    w_half = [0.0] * d
    for idx in range(d):
        if m_k[idx] == 0:
            w_half[idx] = 0.0
            continue
        num = w_k[idx] + sum(nw[idx] for nw in neighbor_weights)
        den = m_k[idx] + sum(nm[idx] for nm in neighbor_masks)
        assert den >= 1
        w_half[idx] = num / float(den)
    return w_half


def prune_and_regrow_mask(w: list[float], m: list[int], grad: list[float], prune_count: int) -> list[int]:
    """Algorithm 2 lines 14-16 (p. 13): magnitude pruning + gradient-magnitude regrowth."""
    active_indices = [i for i, bit in enumerate(m) if bit == 1]
    inactive_indices = [i for i, bit in enumerate(m) if bit == 0]
    assert 0 <= prune_count <= min(len(active_indices), len(inactive_indices))

    # Sort active indices by |w_i| ascending; prune the smallest prune_count
    active_sorted = sorted(active_indices, key=lambda i: (abs(w[i]), i))
    pruned_set = set(active_sorted[:prune_count])

    # Sort inactive indices by |grad_i| descending; regrow the largest prune_count
    inactive_sorted = sorted(inactive_indices, key=lambda i: (-abs(grad[i]), i))
    grown_set = set(inactive_sorted[:prune_count])

    new_m = [0] * len(m)
    for i in active_indices:
        if i not in pruned_set:
            new_m[i] = 1
    for i in grown_set:
        new_m[i] = 1
    return new_m


def main() -> None:
    # 1. Verify ERK sparsity allocation gives higher density to smaller layers while preserving total budget
    layers = [(16, 64), (64, 128), (128, 10)]
    counts = erk_layer_active_counts(layers, target_density=0.25)
    total_d = sum(a * b for a, b in layers)
    assert sum(counts) == int(round(0.25 * total_d))
    densities = [counts[i] / (layers[i][0] * layers[i][1]) for i in range(len(layers))]
    # Middle large layer (64x128) has strictly lower density than first (16x64) and output (128x10) layers
    assert densities[1] < densities[0] and densities[1] < densities[2]

    # 2. Verify Algorithm 1 line 7 decentralized sparse averaging vs naive uniform averaging
    w_k = [2.0, 4.0, 0.0, -3.0]
    m_k = [1, 1, 0, 1]
    # Two neighbors: neighbor 1 shares coords 0, 2; neighbor 2 shares coords 0, 1
    w_n1 = [4.0, 0.0, 5.0, 0.0]
    m_n1 = [1, 0, 1, 0]
    w_n2 = [6.0, 8.0, 0.0, 0.0]
    m_n2 = [1, 1, 0, 0]

    w_half = decentralized_sparse_average(w_k, m_k, [w_n1, w_n2], [m_n1, m_n2])
    # Coord 0: active on k, n1, n2 (den=3) -> (2+4+6)/3 = 4.0
    # Coord 1: active on k, n2 (den=2) -> (4+0+8)/2 = 6.0 (not diluted by n1's zero!)
    # Coord 2: inactive on k -> masked to 0.0
    # Coord 3: active only on k (den=1) -> -3.0 / 1 = -3.0
    assert w_half == [4.0, 6.0, 0.0, -3.0], f"Unexpected w_half: {w_half}"

    # 3. Verify Algorithm 2 prune-and-regrow preserves exact L0 support size and swaps low-|w| for high-|g|
    w_after_sgd = [3.5, 0.02, 0.0, -2.8, 0.05, 0.0, 0.0, 1.9]
    m_curr = [1, 1, 0, 1, 1, 0, 0, 1]  # 5 active, 3 inactive
    grad_curr = [0.1, 0.1, 4.2, 0.2, 0.1, 0.3, 2.7, 0.05]
    m_next = prune_and_regrow_mask(w_after_sgd, m_curr, grad_curr, prune_count=2)
    assert sum(m_next) == sum(m_curr) == 5
    # Coords 1 (|w|=0.02) and 4 (|w|=0.05) should be pruned; inactive coords 2 (|g|=4.2) and 6 (|g|=2.7) regrown
    assert m_next == [1, 0, 1, 1, 0, 0, 1, 1], f"Unexpected regrown mask: {m_next}"

    # 4. Verify cosine annealing schedule (Section 3.2, p. 4)
    alpha0 = 0.5
    t_total = 100
    a_start = 0.5 * alpha0 * (1.0 + math.cos(0.0 * math.pi / t_total))
    a_mid = 0.5 * alpha0 * (1.0 + math.cos(50.0 * math.pi / t_total))
    a_end = 0.5 * alpha0 * (1.0 + math.cos(100.0 * math.pi / t_total))
    assert abs(a_start - alpha0) < 1e-12
    assert abs(a_mid - 0.5 * alpha0) < 1e-12
    assert abs(a_end - 0.0) < 1e-12

    print("DisPFL boundary verification passed:", {
        "erk_densities": [round(d_i, 4) for d_i in densities],
        "w_half": w_half,
        "m_next": m_next,
    })


if __name__ == "__main__":
    main()
