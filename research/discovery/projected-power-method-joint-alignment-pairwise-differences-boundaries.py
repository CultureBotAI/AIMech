#!/usr/bin/env python3
"""
Constructed boundary and mechanism verification for Round 292:
Projected Power Method for Joint Alignment from Pairwise Modulo Differences
(Chen & Candes 2018, Communications on Pure and Applied Mathematics 71(8):1648-1714, arXiv:1609.05820v3).

Verifies:
1. Lifted complex trigonometric embedding of discrete shifts x_i in {0, ..., m-1}:
   X_i in R^{L x m} with rows (X_i)_{l,:} = (1/sqrt(L)) * [1, exp(-j 2 pi k_l / m), ..., exp(-j 2 pi (m-1) k_l / m)]
   at shift x_i, so <X_i, X_j> approximates the cyclic delta / spike kernel around (x_i - x_j) mod m.
2. Generalized power iteration X^{t+1} = P(mu_t C X^t) with scaled anchor-simplex projection P(.)
   under corruptions of fraction 1 - p of pairwise comparisons.
3. Exact modular shift recovery up to a global cyclic shift when p > 0 and SNR is above threshold,
   outperforming unprojected spectral synchronization which collapses to continuous phase drift on
   discrete grids.
"""

import cmath
import json
import math
import random


def make_embedding_vector(shift: int, m: int, freqs: list[int]) -> list[complex]:
    """Construct frequency representation for shift x in {0, ..., m-1}."""
    L = len(freqs)
    scale = 1.0 / math.sqrt(L)
    return [scale * cmath.exp(-2j * math.pi * k * shift / m) for k in freqs]


def inner_prod(u: list[complex], v: list[complex]) -> float:
    return sum((a * b.conjugate()).real for a, b in zip(u, v))


def project_to_simplex_scaled(scores: list[float], target_sum: float = 1.0) -> list[float]:
    """Project real vector onto scaled probability simplex {w >= 0, sum(w) = target_sum}."""
    m = len(scores)
    u = sorted(scores, reverse=True)
    cssv = 0.0
    rho = -1
    for j in range(m):
        cssv += u[j]
        t = (cssv - target_sum) / (j + 1)
        if u[j] - t > 0:
            rho = j
    theta = (sum(u[: rho + 1]) - target_sum) / (rho + 1)
    return [max(s - theta, 0.0) for s in scores]


def cyclic_alignment_error(est: list[int], truth: list[int], m: int) -> tuple[int, float]:
    """Compute minimum Hamming and modular L1 error over global cyclic shifts 0..m-1."""
    n = len(truth)
    best_hamming = n
    best_l1 = float("inf")
    for offset in range(m):
        hamming = 0
        l1 = 0.0
        for e, t in zip(est, truth):
            diff = (e - (t + offset)) % m
            cyclic_dist = min(diff, m - diff)
            if cyclic_dist > 0:
                hamming += 1
            l1 += cyclic_dist
        if (hamming, l1) < (best_hamming, best_l1):
            best_hamming = hamming
            best_l1 = l1
    return best_hamming, best_l1 / n


def run_simulation(seed: int = 20261019) -> dict:
    rng = random.Random(seed)
    n = 36
    m = 12
    # Ground truth discrete labels in {0, ..., m-1}
    truth = [i % m for i in range(n)]

    # Pairwise likelihood matrix C in R^{(n*m) x (n*m)} represented blockwise:
    # For each pair (i, j), observation y_{ij} = (truth[i] - truth[j]) mod m with probability p,
    # otherwise uniform random in {0, ..., m-1}.
    p_clean = 0.42
    obs_diff = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < p_clean:
                y_ij = (truth[i] - truth[j]) % m
            else:
                y_ij = rng.randrange(m)
            obs_diff[i][j] = y_ij
            obs_diff[j][i] = (-y_ij) % m

    # Single-frequency angular synchronization baseline (uses only k=1 Fourier mode)
    # Power method on H_{ij} = exp(j 2 pi y_{ij} / m)
    phases = [rng.uniform(0, 2 * math.pi) for _ in range(n)]
    vec = [cmath.exp(1j * ph) for ph in phases]
    for _ in range(25):
        new_vec = []
        for i in range(n):
            acc = 0j
            for j in range(n):
                if i != j:
                    acc += cmath.exp(2j * math.pi * obs_diff[i][j] / m) * vec[j]
            new_vec.append(acc / abs(acc) if abs(acc) > 1e-12 else 1.0 + 0j)
        vec = new_vec
    single_freq_est = [round((cmath.phase(v) / (2 * math.pi)) * m) % m for v in vec]
    sf_hamming, sf_l1 = cyclic_alignment_error(single_freq_est, truth, m)

    # Projected Power Method (PPM) on lifted block-cyclic matrix C_{ij}(a, b) = 1{(a - b) mod m == y_{ij}}
    # Start from spectral / warm initialization perturbed with noise around a moderately correlated point,
    # or multi-frequency initialization using frequencies k=1..4.
    freqs = [1, 2, 3, 4]
    # Initialize from noisy 1-hop anchor comparisons to node 0 with small multi-frequency smoothing
    W = [[0.0] * m for _ in range(n)]
    for i in range(n):
        scores_i = [0.0] * m
        for a in range(m):
            emb_a = make_embedding_vector(a, m, freqs)
            # Noisy direct comparison to anchor 0 plus two random reference nodes
            val = 0.0
            for k_node in (0, 1, 2):
                implied = (obs_diff[i][k_node] + obs_diff[k_node][0]) % m
                emb_imp = make_embedding_vector(implied, m, freqs)
                val += inner_prod(emb_a, emb_imp)
            scores_i[a] = val / 3.0
        W[i] = project_to_simplex_scaled([2.5 * s for s in scores_i], 1.0)

    init_est = [ max(range(m), key=lambda a: W[i][a]) for i in range(n) ]
    init_hamming, init_l1 = cyclic_alignment_error(init_est, truth, m)

    # Run Projected Power Method iterations: W_i^{t+1} = Proj_simplex(mu_t * sum_{j != i} C_{ij} W_j^t)
    mu = 6.0
    history = []
    for t in range(15):
        W_next = [[0.0] * m for _ in range(n)]
        for i in range(n):
            raw = [0.0] * m
            for j in range(n):
                if i == j:
                    continue
                d_ij = obs_diff[i][j]
                # (C_{ij} W_j)[a] = W_j[(a - d_ij) mod m]
                for a in range(m):
                    raw[a] += W[j][(a - d_ij) % m] / (n - 1)
            W_next[i] = project_to_simplex_scaled([mu * r for r in raw], 1.0)
        W = W_next
        cur_est = [max(range(m), key=lambda a: W[i][a]) for i in range(n)]
        h_err, l1_err = cyclic_alignment_error(cur_est, truth, m)
        history.append({"iter": t + 1, "hamming_error": h_err, "modular_l1_error": round(l1_err, 4)})

    final_hamming = history[-1]["hamming_error"]
    final_l1 = history[-1]["modular_l1_error"]

    assert final_hamming == 0, f"Expected exact recovery (0 Hamming error), got {final_hamming}"
    assert final_hamming < init_hamming, "Expected PPM to strictly improve over initialization"
    assert final_hamming < sf_hamming, "Expected multi-frequency/lifted PPM to outperform single-frequency phase sync"

    return {
        "n_objects": n,
        "alphabet_size_m": m,
        "clean_observation_prob_p": p_clean,
        "single_frequency_sync_hamming_error": sf_hamming,
        "single_frequency_sync_l1_error": round(sf_l1, 4),
        "initial_multi_freq_hamming_error": init_hamming,
        "initial_multi_freq_l1_error": round(init_l1, 4),
        "ppm_final_hamming_error": final_hamming,
        "ppm_final_l1_error": final_l1,
        "ppm_trajectory": history[:6],
    }


if __name__ == "__main__":
    result = run_simulation()
    print(json.dumps(result, indent=2))
