#!/usr/bin/env python3
"""Constructed boundary verification for TKL (Hofstätter et al., SIGIR 2020, arXiv:2005.04908)."""

import math


def sliding_windows_non_pad(doc_tokens: list[int], w: int, o: int) -> list[list[int]]:
    """Eq. (1): Overlapping windows of width w and overlap o, skipping pure-padding (0) windows."""
    windows = []
    n = len(doc_tokens)
    for start in range(0, n, w):
        left = max(0, start - o)
        right = min(n, start + w + o)
        chunk = doc_tokens[left:right]
        # Skip segments containing only padding (token == 0)
        if any(tok != 0 for tok in chunk):
            windows.append(chunk)
    return windows


def rbf_kernel(cos_sim: float, mu: float, sigma: float) -> float:
    """Eq. (2): K_{i,j}^k = exp(-(cos(q_i, d_j) - mu_k)^2 / (2 * sigma^2))."""
    return math.exp(-((cos_sim - mu) ** 2) / (2.0 * sigma * sigma))


def learned_saturation(k_sum: float, e_i: float, c_len: float) -> float:
    """Eqs. (4)-(5): Non-linear query-salience conditioned power saturation a_i * (K_i^{r,k})^{1/b_i} - c_i."""
    relu_e = max(0.0, e_i)
    a_i = 0.8 * relu_e + 0.01 * c_len + 1.0
    b_i = 2.0 * relu_e + 0.05 * c_len + 100.0
    c_i = 0.8 * relu_e + 0.01 * c_len + 1.0
    if k_sum <= 0.0:
        return 0.0
    return a_i * (k_sum ** (1.0 / b_i)) - c_i


def top_local_max(s_r: list[float], r_size: int, t: int, f: int) -> list[list[float]]:
    """Eq. (7): Select top-t non-overlapping local maxima (separated by >= r_size) and f neighbors."""
    remaining = set(range(len(s_r)))
    selected_regions = []
    for _ in range(t):
        if not remaining:
            break
        best_idx = max(remaining, key=lambda idx: s_r[idx])
        region_vec = []
        for offset in range(-f, f + 1):
            nbr = best_idx + offset
            region_vec.append(s_r[nbr] if 0 <= nbr < len(s_r) else 0.0)
        selected_regions.append((best_idx, region_vec))
        # Mask out local neighborhood of radius r_size so term matches are not counted twice
        for idx in list(remaining):
            if abs(idx - best_idx) < r_size:
                remaining.remove(idx)
    return selected_regions


def main() -> None:
    # 1. Windowed local self-attention skips pure-padding windows and scales linearly O(L * w):
    doc_padded = [10, 12, 14, 15, 18, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    packed = sliding_windows_non_pad(doc_padded, w=4, o=1)
    assert len(packed) == 2, f"Expected 2 non-padding windows, got {len(packed)}"

    # 2. Learned saturation is strictly concave and increases with salience e_i and match count k_sum:
    s1 = learned_saturation(1.0, e_i=2.5, c_len=30.0)
    s2 = learned_saturation(4.0, e_i=2.5, c_len=30.0)
    s3 = learned_saturation(8.0, e_i=2.5, c_len=30.0)
    assert 0.0 <= s1 < s2 < s3
    # Concavity check: marginal gain from 1->4 is larger per unit than 4->8
    assert (s2 - s1) / 3.0 > (s3 - s2) / 4.0

    # 3. Long document with relevant region at token index > 200 (missed by TK-200, detected by TKL):
    s_r = [0.05] * 20
    s_r[3] = 0.85   # Early relevant region
    s_r[4] = 0.70   # Immediate neighbor of peak 3 (within saturation radius r_size=3)
    s_r[14] = 1.25  # Late relevant region (beyond 200-token cutoff)
    s_r[13] = 0.60
    s_r[15] = 0.65

    top_regions = top_local_max(s_r, r_size=3, t=2, f=1)
    assert len(top_regions) == 2
    assert top_regions[0][0] == 14, "First local maximum is the late relevant region at index 14"
    assert top_regions[0][1] == [0.60, 1.25, 0.65]
    assert top_regions[1][0] == 3, "Second non-overlapping local maximum is at index 3 (index 4 masked)"

    print("TKL boundary verification passed:")
    print(f"  Packed non-padding windows: {len(packed)} (from 4 total chunks)")
    print(f"  Learned saturation values:  s(1)={s1:.6f}, s(4)={s2:.6f}, s(8)={s3:.6f}")
    print(f"  Top-2 local maxima indices: {[idx for idx, _ in top_regions]}")


if __name__ == "__main__":
    main()
