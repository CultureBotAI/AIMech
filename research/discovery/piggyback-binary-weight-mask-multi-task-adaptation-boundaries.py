#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 720: Piggyback (Mallya, Davis, & Lazebnik, ECCV 2018)."""

import math


def verify_piggyback() -> None:
    # 1. Hard binary thresholding of real-valued mask weights m^r (Eq. 4):
    # m_{ji} = 1 if m^r_{ji} >= tau else 0, with default initialization m^r = 1e-2 and tau = 5e-3
    tau = 5e-3
    W = [[0.4, -0.6, 0.2], [-0.3, 0.8, -0.5]]
    m_r = [[1e-2, 2e-3, 8e-3], [1e-3, 1.2e-2, 4e-3]]
    m = [[1.0 if val >= tau else 0.0 for val in row] for row in m_r]
    assert m == [[1.0, 0.0, 1.0], [0.0, 1.0, 0.0]]

    # 2. Forward pass with fixed backbone W and elementwise binary mask m: y = (W odot m) x
    x = [1.5, -2.0, 0.5]
    y = [
        sum(W[j][i] * m[j][i] * x[i] for i in range(len(x)))
        for j in range(len(W))
    ]
    assert math.isclose(y[0], 0.4 * 1.5 + 0.2 * 0.5, rel_tol=1e-12)
    assert math.isclose(y[1], 0.8 * (-2.0), rel_tol=1e-12)

    # 3. Straight-through gradient estimator for real-valued mask weights m^r (Eq. 5-7):
    # delta_m = (delta_y * x^T) odot W, proportional to |W|
    delta_y = [0.2, -0.1]
    delta_m = [
        [delta_y[j] * x[i] * W[j][i] for i in range(len(x))]
        for j in range(len(W))
    ]
    lr = 0.05
    m_r_updated = [
        [m_r[j][i] - lr * delta_m[j][i] for i in range(len(x))]
        for j in range(len(W))
    ]
    assert m_r_updated != m_r

    # 4. Storage overhead: 1 bit per 32-bit float parameter per new task (~3.125% per task)
    # Across 10 Visual Decathlon tasks (1 base + 9 binary masks): (32n + 9n) / 32n = 41 / 32 = 1.28125
    assert math.isclose(1.0 / 32.0, 0.03125, rel_tol=1e-12)
    assert math.isclose((32.0 + 9.0) / 32.0, 1.28125, rel_tol=1e-12)
    print("Piggyback verification passed.")


if __name__ == "__main__":
    verify_piggyback()
