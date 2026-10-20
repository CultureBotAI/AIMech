#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 526:
FoolsGold (Cosine-Similarity Sybil Defense for Federated Learning)
Fung, Yoon, & Beschastnikh, RAID 2020 (pp. 301-316, arXiv:1808.04866).

Verifies:
1. Algorithm 1 (FoolsGold):
   - Cumulative historical gradient aggregation H_i = sum_{t=1}^T Delta_{i,t} (Line 3)
   - Pairwise indicative-feature weighted cosine similarity cs_{ij} and v_i = max_{j != i} cs_{ij} (Lines 4-8)
   - Pardoning mechanism: if v_j > v_i, cs_{ij} *= v_i / v_j so honest clients partially
     correlated with sybils are not penalized (Lines 10-15)
   - Row-wise maximum inversion alpha_i = 1 - max_{j != i} cs_{ij}, normalization
     alpha_i = alpha_i / max_k(alpha_k), and centered logit rescaling clipped to [0, 1]:
     alpha_i = clip_{[0,1]}(kappa * (ln(alpha_i / (1 - alpha_i)) + 0.5)) (Lines 16-19).
2. Appendix A convergence thresholds:
   - Sybil threshold beta_m >= 1 - exp(-0.5*kappa) / (1 + exp(-0.5*kappa)) maps to alpha_i = 0.
   - Honest threshold beta_g <= 1 - exp(0.5*kappa) / (1 + exp(0.5*kappa)) maps to alpha_i = 1.
3. Resilience when sybils outnumber honest clients (e.g., 5 sybils vs 5 honest non-i.i.d.
   clients), where Multi-Krum and FedAvg fail.
"""

import math
import random


def weighted_cosine_similarity(h_i, h_j, s_weights):
    num = sum(s * a * b for s, a, b in zip(s_weights, h_i, h_j))
    norm_i = math.sqrt(sum(s * a * a for s, a in zip(s_weights, h_i)))
    norm_j = math.sqrt(sum(s * b * b for s, b in zip(s_weights, h_j)))
    if norm_i < 1e-12 or norm_j < 1e-12:
        return 0.0
    return max(-1.0, min(1.0, num / (norm_i * norm_j)))


def foolsgold_weights(histories, s_weights, kappa=1.0):
    """Algorithm 1: Compute per-client FoolsGold learning rate weights alpha_i in [0, 1]."""
    n = len(histories)
    cs = [[0.0 for _ in range(n)] for _ in range(n)]
    v = [0.0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                cs[i][j] = weighted_cosine_similarity(histories[i], histories[j], s_weights)
        v[i] = max(cs[i][j] for j in range(n) if j != i)

    # Pardoning (Lines 10-15)
    cs_pardoned = [list(row) for row in cs]
    for i in range(n):
        for j in range(n):
            if i != j and v[j] > v[i] and v[j] > 1e-12:
                cs_pardoned[i][j] *= v[i] / v[j]

    # Row-wise maximum inversion (Line 16)
    alpha = [1.0 - max(cs_pardoned[i][j] for j in range(n) if j != i) for i in range(n)]
    max_alpha = max(alpha)
    if max_alpha > 1e-12:
        alpha = [a / max_alpha for a in alpha]

    # Centered logit function clipped to [0, 1] (Line 19)
    out_alpha = []
    for a in alpha:
        if a <= 1e-9:
            out_alpha.append(0.0)
        elif a >= 1.0 - 1e-9:
            out_alpha.append(1.0)
        else:
            logit_val = kappa * (math.log(a / (1.0 - a)) + 0.5)
            out_alpha.append(max(0.0, min(1.0, logit_val)))
    return out_alpha, cs_pardoned


def main():
    rng = random.Random(2020)
    kappa = 1.0

    # 1. Verify Appendix A exact logit cutoff thresholds beta_m and beta_g
    beta_m = 1.0 - math.exp(-0.5 * kappa) / (1.0 + math.exp(-0.5 * kappa))
    beta_g = 1.0 - math.exp(0.5 * kappa) / (1.0 + math.exp(0.5 * kappa))
    # At normalized alpha = 1 - beta_m, kappa*(ln(alpha/(1-alpha)) + 0.5) == 0
    alpha_at_beta_m = 1.0 - beta_m
    logit_at_beta_m = kappa * (math.log(alpha_at_beta_m / (1.0 - alpha_at_beta_m)) + 0.5)
    # At normalized alpha = 1 - beta_g, kappa*(ln(alpha/(1-alpha)) + 0.5) == 1 (for kappa=1)
    alpha_at_beta_g = 1.0 - beta_g
    logit_at_beta_g = kappa * (math.log(alpha_at_beta_g / (1.0 - alpha_at_beta_g)) + 0.5)
    assert abs(logit_at_beta_m - 0.0) < 1e-12
    assert abs(logit_at_beta_g - 1.0) < 1e-12

    # 2. Simulate non-i.i.d. Federated Learning with 5 honest clients (orthogonal indicative
    # class directions) and 6 colluding sybils (> 50% sybil majority!) mounting a targeted
    # label-flipping attack plus orthogonal noise on non-indicative features (Section 6.4)
    n_honest = 5
    n_sybils = 6
    n_total = n_honest + n_sybils
    d_indicative = 6
    d_irrelevant = 6
    d = d_indicative + d_irrelevant

    # Indicative feature mask S_t: 1.0 on indicative output-layer features, 0.05 on irrelevant
    s_weights = [1.0] * d_indicative + [0.05] * d_irrelevant

    histories = [[0.0 for _ in range(d)] for _ in range(n_total)]
    sybil_target_dir = [0.0, 1.0, -1.0, 0.0, 0.0, 0.0]

    for _ in range(25):
        for i in range(n_honest):
            # Honest client i updates its own class direction i (plus small stochastic noise)
            delta = [
                (1.0 if c == i else 0.0) + rng.gauss(0.0, 0.08)
                for c in range(d_indicative)
            ] + [rng.gauss(0.0, 0.05) for _ in range(d_irrelevant)]
            histories[i] = [h + u for h, u in zip(histories[i], delta)]

        for s_idx in range(n_sybils):
            client_id = n_honest + s_idx
            # Colluding sybil pushes sybil_target_dir on indicative features, while adding
            # opposite noise on irrelevant features to try to evade unfiltered cosine similarity
            sign_noise = 1.0 if s_idx % 2 == 0 else -1.0
            delta = [
                sybil_target_dir[c] + rng.gauss(0.0, 0.04)
                for c in range(d_indicative)
            ] + [sign_noise * 0.8 + rng.gauss(0.0, 0.02) for _ in range(d_irrelevant)]
            histories[client_id] = [h + u for h, u in zip(histories[client_id], delta)]

    # Verify pardoning protects honest client 1 (whose feature overlaps with sybil_target_dir[1])
    alphas, _ = foolsgold_weights(histories, s_weights, kappa=kappa)
    honest_alphas = alphas[:n_honest]
    sybil_alphas = alphas[n_honest:]

    min_honest_alpha = min(honest_alphas)
    max_sybil_alpha = max(sybil_alphas)
    assert min_honest_alpha > 0.70, f"Expected honest clients preserved (>0.70), got {honest_alphas}"
    assert max_sybil_alpha < 0.02, f"Expected sybils suppressed (<0.02), got {sybil_alphas}"

    print(
        f"[PASS] Round 526 FoolsGold (Fung et al. 2020): "
        f"beta_m={beta_m:.4f}, beta_g={beta_g:.4f}, "
        f"min_honest_alpha={min_honest_alpha:.4f} >> max_sybil_alpha={max_sybil_alpha:.4f}"
    )


if __name__ == "__main__":
    main()
