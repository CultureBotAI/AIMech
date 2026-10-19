#!/usr/bin/env python3
"""Constructed boundary verification for Round 447:
HeteroFL: Computation and Communication Efficient Federated Learning for Heterogeneous Clients
(Enmao Diao, Jie Ding, & Vahid Tarokh, ICLR 2021, arXiv:2010.01264).

Verifies:
1. Width-scaled nested submatrix hierarchy (Section 3.1, Eq. 1):
   For global hidden layer W_g in R^{d_g x k_g} and width shrinkage ratio r in (0, 1),
   computation complexity level p in {1, ..., P} extracts the top-left submatrix
   W_l^p = W_g[:d_l^p, :k_l^p] with d_l^p = r^{p-1} d_g, k_l^p = r^{p-1} k_g, giving exact
   parameter ratio |W_l^p| / |W_g| = r^{2(p-1)}.
2. Scaler module (Section 3.2): Scaling subnetwork activations by 1 / r^{p-1} makes the expected
   output magnitude invariant across complexity levels p in {1, ..., P}.
3. Disjoint partitioned parameter aggregation (Section 3.1, Eqs. 2-4, Algorithm 1):
   Aggregating each disjoint parameter partition W_g^{p-1} \ W_g^p using only the m - m^{(p)}
   clients with capability p_i <= p-1 yields an unbiased estimator of the true target parameter
   matrix across all blocks, whereas naive zero-padded full-matrix averaging biases outer blocks
   toward zero by factor (m - m^{(p)}) / m.
"""

from __future__ import annotations
import math
import random


def main() -> None:
    rng = random.Random(20201003)
    d_g, k_g = 16, 16
    r = 0.5
    p_levels = [1, 2, 3]
    dims = {p: (int(round((r ** (p - 1)) * d_g)), int(round((r ** (p - 1)) * k_g))) for p in p_levels}

    # Check exact parameter compression ratios r^{2(p-1)}
    for p in p_levels:
        d_p, k_p = dims[p]
        ratio = (d_p * k_p) / (d_g * k_g)
        expected = r ** (2 * (p - 1))
        assert abs(ratio - expected) < 1e-12, f"Compression ratio mismatch at p={p}: {ratio} vs {expected}"

    # Check Scaler module invariance: for isotropic unit inputs x and unit weights,
    # E[(1/r^{p-1}) * sum_{j=1}^{k_l^p} W_{i,j} x_j] has variance (1/r^{2(p-1)}) * k_l^p * Var
    # and for positive constant activation mean, mean is exactly preserved:
    x_const = [1.0] * k_g
    w_ones = [[1.0] * k_g for _ in range(d_g)]
    full_out = sum(w_ones[0][j] * x_const[j] for j in range(k_g))
    for p in p_levels:
        _, k_p = dims[p]
        scaler = 1.0 / (r ** (p - 1))
        scaled_out = scaler * sum(w_ones[0][j] * x_const[j] for j in range(k_p))
        assert abs(scaled_out - full_out) < 1e-12

    # Verify partitioned aggregation vs naive zero-padded aggregation (Eqs. 2-4)
    w_true = [[rng.uniform(-1.5, 1.5) for _ in range(k_g)] for _ in range(d_g)]
    client_tiers = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3]  # m = 10 clients across tiers 1, 2, 3
    m_total = len(client_tiers)

    client_models: list[tuple[int, list[list[float]]]] = []
    for p_i in client_tiers:
        d_p, k_p = dims[p_i]
        # Each client observes noisy local optimum of its active submatrix
        w_loc = [[w_true[row][col] + rng.gauss(0.0, 0.01) for col in range(k_p)] for row in range(d_p)]
        client_models.append((p_i, w_loc))

    # HeteroFL partitioned aggregation (Eqs. 2-4): each coordinate (row, col) is averaged over
    # exactly those clients whose submatrix covers (row, col)
    w_heterofl = [[0.0] * k_g for _ in range(d_g)]
    w_naive_zeropad = [[0.0] * k_g for _ in range(d_g)]

    for row in range(d_g):
        for col in range(k_g):
            active_vals = []
            for p_i, w_loc in client_models:
                d_p, k_p = dims[p_i]
                if row < d_p and col < k_p:
                    active_vals.append(w_loc[row][col])
            w_heterofl[row][col] = sum(active_vals) / len(active_vals)
            w_naive_zeropad[row][col] = sum(active_vals) / m_total

    err_heterofl = math.sqrt(
        sum((w_heterofl[row][col] - w_true[row][col]) ** 2 for row in range(d_g) for col in range(k_g))
        / (d_g * k_g)
    )
    err_naive = math.sqrt(
        sum((w_naive_zeropad[row][col] - w_true[row][col]) ** 2 for row in range(d_g) for col in range(k_g))
        / (d_g * k_g)
    )

    assert err_heterofl < 0.02, f"Expected small HeteroFL estimation error, got {err_heterofl}"
    assert err_naive > 20.0 * err_heterofl, f"Expected naive zero-pad error >> HeteroFL: {err_naive} vs {err_heterofl}"

    print(
        f"[PASS] Round 447 HeteroFL (Diao et al. 2021): "
        f"ratios={[ (dims[p][0]*dims[p][1])/(d_g*k_g) for p in p_levels ]}, "
        f"err_heterofl={err_heterofl:.4e} << err_naive_zeropad={err_naive:.4e}"
    )


if __name__ == "__main__":
    main()
