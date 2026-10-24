#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 656: BOFT (Liu et al., ICLR 2024)."""

import math
import random


def cayley_2x2(theta: float) -> list[list[float]]:
    """Construct 2x2 orthogonal matrix R = (I + Q)(I - Q)^{-1} for skew-symmetric Q = [[0, -theta], [theta, 0]]."""
    # (I - Q) = [[1, theta], [-theta, 1]], det = 1 + theta^2
    # (I - Q)^{-1} = (1 / (1 + theta^2)) * [[1, -theta], [theta, 1]]
    # (I + Q)(I - Q)^{-1} = (1 / (1 + theta^2)) * [[1 - theta^2, -2*theta], [2*theta, 1 - theta^2]]
    denom = 1.0 + theta * theta
    c = (1.0 - theta * theta) / denom
    s = (2.0 * theta) / denom
    return [[c, -s], [s, c]]


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    d = len(a)
    n = len(b[0])
    k_dim = len(b)
    return [
        [sum(a[i][k] * b[k][j] for k in range(k_dim)) for j in range(n)]
        for i in range(d)
    ]


def build_butterfly_component_d8(k_block: int, thetas: list[float]) -> list[list[float]]:
    """Build 8x8 orthogonal butterfly component B_tilde(8, k_block) with 2x2 Cayley blocks (b=2 in BOFT(m, b) notation)."""
    d = 8
    mat = [[0.0 for _ in range(d)] for _ in range(d)]
    stride = k_block // 2
    idx = 0
    for block_start in range(0, d, k_block):
        for offset in range(stride):
            i1 = block_start + offset
            i2 = block_start + offset + stride
            r2 = cayley_2x2(thetas[idx])
            idx += 1
            mat[i1][i1] = r2[0][0]
            mat[i1][i2] = r2[0][1]
            mat[i2][i1] = r2[1][0]
            mat[i2][i2] = r2[1][1]
    return mat


def verify_boft_orthogonality_density_and_angle_preservation() -> None:
    """Verify Section 4-5: BOFT(m=3, b=2) on d=8 produces a dense orthogonal matrix preserving neuron angles."""
    rng = random.Random(20241106)
    d = 8
    # m = log2(8) = 3 butterfly components: B_tilde(8, 8) * B_tilde(8, 4) * B_tilde(8, 2)
    b8 = build_butterfly_component_d8(8, [rng.uniform(-0.6, 0.6) for _ in range(4)])
    b4 = build_butterfly_component_d8(4, [rng.uniform(-0.6, 0.6) for _ in range(4)])
    b2 = build_butterfly_component_d8(2, [rng.uniform(-0.6, 0.6) for _ in range(4)])

    # Contrast boundary: m=1 (block-diagonal OFT) is b2 alone -> has only 16 non-zero entries out of 64
    nz_oft = sum(1 for i in range(d) for j in range(d) if abs(b2[i][j]) > 1e-12)
    assert nz_oft == 16, f"Block-diagonal OFT(1, 2) must have 16 non-zeros, got {nz_oft}"

    # BOFT(3, 2) product R = b8 * b4 * b2 is completely dense (all 64 entries non-zero!)
    r_boft = matmul(matmul(b8, b4), b2)
    nz_boft = sum(1 for i in range(d) for j in range(d) if abs(r_boft[i][j]) > 1e-12)
    assert nz_boft == 64, f"BOFT(3, 2) on d=8 must be dense (64 non-zeros), got {nz_boft}"

    # Effective trainable parameter count: (1/2) * (b - 1) * d * m = 0.5 * 1 * 8 * 3 = 12 parameters
    # versus full 8x8 skew-symmetric Cayley OFT: d*(d-1)/2 = 28 parameters
    params_boft = int(0.5 * (2 - 1) * d * 3)
    params_full_oft = d * (d - 1) // 2
    assert params_boft == 12 and params_boft < params_full_oft

    # Verify R^T R = I_8
    r_t = [[r_boft[j][i] for j in range(d)] for i in range(d)]
    rt_r = matmul(r_t, r_boft)
    for i in range(d):
        for j in range(d):
            target = 1.0 if i == j else 0.0
            assert abs(rt_r[i][j] - target) < 1e-12

    # Verify pairwise neuron inner-product / angle preservation on W^0 in R^{8 x 5}
    n_neurons = 5
    w0 = [[rng.gauss(0.0, 1.0) for _ in range(n_neurons)] for _ in range(d)]
    w_boft = matmul(r_boft, w0)
    for u in range(n_neurons):
        for v in range(n_neurons):
            dot_before = sum(w0[k][u] * w0[k][v] for k in range(d))
            dot_after = sum(w_boft[k][u] * w_boft[k][v] for k in range(d))
            assert abs(dot_before - dot_after) < 1e-11, "BOFT must preserve all pairwise neuron inner products"


if __name__ == "__main__":
    verify_boft_orthogonality_density_and_angle_preservation()
    print("[PASS] Round 656 BOFT boundary and mathematical verification succeeded.")
