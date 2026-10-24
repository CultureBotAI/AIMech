#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 408:
FedMA: Federated Matched Averaging via Layer-Wise Bayesian Nonparametric Matching
(Wang, Yurochkin, Sun, Papailiopoulos, & Khazaeni, ICLR 2020, arXiv:2002.06440).
"""

import itertools
import math
import random


def relu(z):
    return z if z > 0.0 else 0.0


def forward_2layer(x, W1, W2):
    """Two-layer ReLU network f(x; W1, W2) = W2^T sigma(W1^T x), where W1 is D x L and W2 is L x K."""
    D = len(W1)
    L = len(W1[0])
    K = len(W2[0])
    h = [relu(sum(x[d] * W1[d][l] for d in range(D))) for l in range(L)]
    return [sum(h[l] * W2[l][k] for l in range(L)) for k in range(K)]


def mat_mul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)] for i in range(m)]


def mat_T(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def exact_bipartite_min_assignment(cost_matrix):
    """Exact minimum-weight bipartite assignment over L! permutations."""
    L = len(cost_matrix)
    best_cost = float("inf")
    best_perm = None
    for perm in itertools.permutations(range(L)):
        c = sum(cost_matrix[l][perm[l]] for l in range(L))
        if c < best_cost:
            best_cost = c
            best_perm = perm
    Pi = [[1.0 if best_perm[l] == i else 0.0 for i in range(L)] for l in range(L)]
    return Pi, best_cost


def main():
    rng = random.Random(408)
    D, L, K = 4, 4, 2

    # 1. Verify Eq. (2) permutation invariance: f(x; W1 * Pi, Pi^T * W2) == f(x; W1, W2)
    W1_true = [
        [2.5, -2.0, 0.4, 0.2],
        [0.5, 2.2, -1.8, 0.3],
        [-0.3, 0.4, 2.6, -2.1],
        [0.1, -0.2, 0.5, 2.7],
    ]
    W2_true = [
        [2.0, -1.2],
        [-1.8, 2.1],
        [1.5, 1.7],
        [-1.4, -1.9],
    ]
    perm = (2, 0, 3, 1)
    Pi_true = [[1.0 if perm[l] == i else 0.0 for i in range(L)] for l in range(L)]
    W1_perm = mat_mul(W1_true, Pi_true)
    W2_perm = mat_mul(mat_T(Pi_true), W2_true)

    test_X = [[rng.gauss(0.0, 1.0) for _ in range(D)] for _ in range(50)]
    max_inv_err = 0.0
    for x in test_X:
        y1 = forward_2layer(x, W1_true, W2_true)
        y2 = forward_2layer(x, W1_perm, W2_perm)
        err = math.sqrt(sum((y1[k] - y2[k]) ** 2 for k in range(K)))
        if err > max_inv_err:
            max_inv_err = err
    assert max_inv_err < 1e-14

    # 2. Verify Algorithm 1 (FedMA layer-wise matching vs naive coordinate FedAvg):
    W1_c1 = [[W1_true[d][l] + 0.02 * rng.gauss(0.0, 1.0) for l in range(L)] for d in range(D)]
    W2_c1 = [[W2_true[l][k] + 0.02 * rng.gauss(0.0, 1.0) for k in range(K)] for l in range(L)]
    W1_c2 = [[W1_perm[d][l] + 0.02 * rng.gauss(0.0, 1.0) for l in range(L)] for d in range(D)]
    W2_c2 = [[W2_perm[l][k] + 0.02 * rng.gauss(0.0, 1.0) for k in range(K)] for l in range(L)]

    # Naive coordinate-wise FedAvg
    W1_fedavg = [[0.5 * (W1_c1[d][l] + W1_c2[d][l]) for l in range(L)] for d in range(D)]
    W2_fedavg = [[0.5 * (W2_c1[l][k] + W2_c2[l][k]) for k in range(K)] for l in range(L)]

    # FedMA Layer 1 matching: match columns of W1_c2 to W1_c1 via squared Euclidean cost c(w_{2,l}, theta_i)
    cost_mat = [
        [sum((W1_c2[d][l] - W1_c1[d][i]) ** 2 for d in range(D)) for i in range(L)]
        for l in range(L)
    ]
    Pi_2, _ = exact_bipartite_min_assignment(cost_mat)
    # Verify that Pi_2 is the exact inverse transpose of Pi_true (Pi_true * Pi_2 == I_L)
    prod_Pi = mat_mul(Pi_true, Pi_2)
    for r in range(L):
        for c in range(L):
            assert abs(prod_Pi[r][c] - (1.0 if r == c else 0.0)) < 1e-12

    W1_c2_aligned = mat_mul(W1_c2, Pi_2)
    W1_fedma = [[0.5 * (W1_c1[d][l] + W1_c2_aligned[d][l]) for l in range(L)] for d in range(D)]
    W2_c2_aligned = mat_mul(mat_T(Pi_2), W2_c2)
    W2_fedma = [[0.5 * (W2_c1[l][k] + W2_c2_aligned[l][k]) for k in range(K)] for l in range(L)]

    mse_fedavg = 0.0
    mse_fedma = 0.0
    for x in test_X:
        y_true = forward_2layer(x, W1_true, W2_true)
        y_avg = forward_2layer(x, W1_fedavg, W2_fedavg)
        y_ma = forward_2layer(x, W1_fedma, W2_fedma)
        mse_fedavg += sum((y_avg[k] - y_true[k]) ** 2 for k in range(K)) / len(test_X)
        mse_fedma += sum((y_ma[k] - y_true[k]) ** 2 for k in range(K)) / len(test_X)

    assert mse_fedma < 0.01 and mse_fedavg > 5.0 and mse_fedma < 1e-3 * mse_fedavg, (
        f"Expected mse_fedma << mse_fedavg, got mse_fedma={mse_fedma}, mse_fedavg={mse_fedavg}"
    )

    # 3. Verify BBP-MAP adaptive global hidden size expansion (Eq. 6):
    epsilon_thresh = 1.0
    novel_neuron = [5.0, 5.0, -5.0, -5.0]
    min_dist_sq = min(
        sum((novel_neuron[d] - W1_c1[d][i]) ** 2 for d in range(D))
        for i in range(L)
    )
    spawn_new_neuron = min_dist_sq > epsilon_thresh
    assert spawn_new_neuron is True

    print(
        f"[PASS] Round 408 FedMA (Wang et al. 2020): "
        f"perm_inv_err={max_inv_err:.2e}, mse_fedma={mse_fedma:.5f}<<mse_fedavg={mse_fedavg:.4f}, "
        f"bbp_min_dist_sq={min_dist_sq:.2f}>eps={epsilon_thresh:.2f}"
    )


if __name__ == "__main__":
    main()
