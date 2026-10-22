#!/usr/bin/env python3
"""Constructed boundary verification for SAWB (Statistics-Aware Weight Binning, Choi et al. 2018)."""

import math


def quantize_symmetric_2bit(w_list, alpha):
    """2-bit symmetric quantization into {-alpha, -alpha/3, +alpha/3, +alpha} (Equation 4)."""
    levels = [-alpha, -alpha / 3.0, alpha / 3.0, alpha]
    q_list = []
    for w in w_list:
        c = max(-alpha, min(alpha, w))
        best_l = min(levels, key=lambda l: abs(c - l))
        q_list.append(best_l)
    return q_list


def mse(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) / len(a)


def main():
    # Construct zero-mean Gaussian-like weight tensor with outlier tails
    # Standard 2-bit SAWB formula (Section 2.2, Equation 5 & Table 2):
    # alpha_w^* = c1 * sqrt(E[w^2]) - c2 * E[|w|], with Table 2 2-bit coefficients c1=3.12, c2=2.064
    weights = []
    for i in range(1, 201):
        # Inverse-CDF-like deterministic Gaussian-shaped grid plus two sharp outliers
        u = (i - 0.5) / 200.0
        # Approximate standard normal quantile
        z = math.sqrt(2.0) * math.erfinv(2.0 * u - 1.0) if hasattr(math, "erfinv") else (
            (u ** 0.135 - (1.0 - u) ** 0.135) / 0.1975
        )
        weights.append(0.5 * z)
    # Inject two large weight outliers that distort full-range MinMax quantization
    weights.extend([-4.5, 4.5])

    e_abs = sum(abs(w) for w in weights) / len(weights)
    sqrt_e_w2 = math.sqrt(sum(w * w for w in weights) / len(weights))

    c1_2bit, c2_2bit = 3.12, 2.064
    alpha_sawb = c1_2bit * sqrt_e_w2 - c2_2bit * e_abs
    alpha_minmax = max(abs(w) for w in weights)

    q_sawb = quantize_symmetric_2bit(weights, alpha_sawb)
    q_minmax = quantize_symmetric_2bit(weights, alpha_minmax)

    mse_sawb = mse(weights, q_sawb)
    mse_minmax = mse(weights, q_minmax)

    # Exhaustive grid search for ground-truth MSE-optimal clipping threshold alpha*
    best_alpha_grid = min(
        [0.05 * k for k in range(1, 100)],
        key=lambda a: mse(weights, quantize_symmetric_2bit(weights, a)),
    )
    mse_grid = mse(weights, quantize_symmetric_2bit(weights, best_alpha_grid))

    assert 0.5 < alpha_sawb < alpha_minmax * 0.5
    assert mse_sawb < mse_minmax * 0.35
    assert abs(mse_sawb - mse_grid) < 0.02

    print(
        f"[PASS] Round 829 SAWB verified: alpha_SAWB={alpha_sawb:.4f} (grid={best_alpha_grid:.4f}) "
        f"vs alpha_MinMax={alpha_minmax:.4f}, MSE_SAWB={mse_sawb:.6f} << MSE_MinMax={mse_minmax:.6f}"
    )


if __name__ == "__main__":
    main()
