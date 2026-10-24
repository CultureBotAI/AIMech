#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 414:
CFL: Clustered Federated Learning via Cosine Similarity Bipartitioning (Sattler, Müller, & Samek 2021).
"""

import math


def dot(u: list[float], v: list[float]) -> float:
    return sum(ui * vi for ui, vi in zip(u, v))


def norm(u: list[float]) -> float:
    return math.sqrt(dot(u, u))


def cosine_sim(u: list[float], v: list[float]) -> float:
    return dot(u, v) / (norm(u) * norm(v))


def minimax_bipartition(alpha: list[list[float]]) -> tuple[set[int], set[int], float]:
    """Algorithm 1 (Sattler et al. 2021): agglomerative single/minimax-linkage bipartitioning
    minimizing max_{i in c1, j in c2} alpha_{i,j}.
    """
    m = len(alpha)
    clusters: list[set[int]] = [{i} for i in range(m)]
    while len(clusters) > 2:
        best_sim = -2.0
        best_pair = (0, 1)
        for a_idx in range(len(clusters)):
            for b_idx in range(a_idx + 1, len(clusters)):
                sim = max(alpha[i][j] for i in clusters[a_idx] for j in clusters[b_idx])
                if sim > best_sim:
                    best_sim = sim
                    best_pair = (a_idx, b_idx)
        i_idx, j_idx = best_pair
        merged = clusters[i_idx] | clusters[j_idx]
        clusters = [c for k, c in enumerate(clusters) if k not in (i_idx, j_idx)] + [merged]

    c1, c2 = clusters[0], clusters[1]
    cross_max = max(alpha[i][j] for i in c1 for j in c2)
    return c1, c2, cross_max


def main() -> None:
    # 2 incongruent clusters of 3 clients each in R^3 at global stationary point theta*
    # True cluster gradients: R_1 = [1, 0, 0], R_2 = [-1, 0, 0] (sum = 0 at global stationary point)
    # Empirical client gradients r_i have relative noise gamma_i = ||R_{I(i)} - r_i|| / ||R_{I(i)}|| <= 0.15
    R1 = [1.0, 0.0, 0.0]
    R2 = [-1.0, 0.0, 0.0]
    r = [
        [1.0, 0.10, -0.05],
        [1.0, -0.08, 0.06],
        [1.0, -0.02, -0.01],
        [-1.0, 0.09, 0.04],
        [-1.0, -0.10, -0.02],
        [-1.0, 0.01, -0.02],
    ]
    m = len(r)
    true_Rs = [R1, R1, R1, R2, R2, R2]
    gammas = [norm([ri[d] - Ri[d] for d in range(3)]) / norm(Ri) for ri, Ri in zip(r, true_Rs)]
    gamma_max = max(gammas)
    assert gamma_max < 0.15

    # Check global stationarity ||(1/m) sum_i r_i|| < eps_1 and client incongruence max_i ||r_i|| > eps_2
    global_grad_norm = norm([sum(r[i][d] for i in range(m)) / m for d in range(3)])
    max_client_norm = max(norm(ri) for ri in r)
    assert global_grad_norm < 1e-12
    assert max_client_norm > 1.0

    # Compute pairwise cosine similarity matrix alpha
    alpha = [[cosine_sim(r[i], r[j]) for j in range(m)] for i in range(m)]
    c1, c2, cross_max = minimax_bipartition(alpha)
    assert {frozenset(c1), frozenset(c2)} == {frozenset({0, 1, 2}), frozenset({3, 4, 5})}

    intra_min = min(
        min(alpha[i][j] for i in c1 for j in c1 if i != j),
        min(alpha[i][j] for i in c2 for j in c2 if i != j),
    )
    sep_gap = intra_min - cross_max

    # Theorem 1 / Corollary 1 theoretical bounds for k=2 (cos(pi/(k-1)) = cos(pi) = -1):
    # alpha_intra^min >= 1 - 2 * gamma_max^2
    intra_bound = 1.0 - 2.0 * (gamma_max ** 2)
    assert intra_min >= intra_bound - 1e-12
    assert sep_gap > 1.9, f"Expected large separation gap, got {sep_gap}"

    # Section V-B: exact invariance under orthogonal encryption P
    theta_rot = 0.73
    P = [
        [math.cos(theta_rot), -math.sin(theta_rot), 0.0],
        [math.sin(theta_rot), math.cos(theta_rot), 0.0],
        [0.0, 0.0, -1.0],
    ]
    r_enc = [[sum(P[row][col] * ri[col] for col in range(3)) for row in range(3)] for ri in r]
    alpha_enc = [[cosine_sim(r_enc[i], r_enc[j]) for j in range(m)] for i in range(m)]
    enc_diff = max(abs(alpha[i][j] - alpha_enc[i][j]) for i in range(m) for j in range(m))
    assert enc_diff < 1e-15

    print(
        f"[PASS] CFL boundaries verified: global_grad={global_grad_norm:.2e}, max_client={max_client_norm:.4f}, "
        f"gamma_max={gamma_max:.4f}, intra_min={intra_min:.4f}>={intra_bound:.4f}, sep_gap={sep_gap:.4f}"
    )


if __name__ == "__main__":
    main()
