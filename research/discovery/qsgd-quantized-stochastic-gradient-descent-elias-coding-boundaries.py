#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 378:
QSGD: Communication-Efficient SGD via Gradient Quantization and Elias Coding
(Alistarh, Grubic, Li, Tomioka, & Vojnovic 2017, NeurIPS 2017, pp. 1709-1720, arXiv:1610.02132).
"""

import math
import random


def elias_gamma_len(k: int) -> int:
    """Bit length of Elias gamma code for positive integer k >= 1: 2 * floor(log2(k)) + 1."""
    assert k >= 1
    return 2 * int(math.floor(math.log2(k))) + 1


def main() -> None:
    rng = random.Random(20261019)

    # 1. Verify Lemma 3.1 (Unbiasedness, Second-Moment Variance Bound, and Expected Sparsity of Q_s(v)):
    # For any v \in R^n and quantization level s >= 1:
    # Let r_i = s * |v_i| / ||v||_2 = l_i + p_i with l_i = floor(r_i) \in {0, ..., s} and p_i = r_i - l_i \in [0, 1).
    # Then \xi_i(v, s) = (l_i + 1)/s w.p. p_i and l_i/s w.p. 1 - p_i.
    # Exact analytical expectations per coordinate:
    # E[Q_s(v)_i] = ||v||_2 * sgn(v_i) * (l_i + p_i) / s = v_i (unbiased!).
    # Var(Q_s(v)_i) = (||v||_2^2 / s^2) * p_i * (1 - p_i).
    # Total variance: E[||Q_s(v) - v||_2^2] = (||v||_2^2 / s^2) \sum_{i=1}^n p_i (1 - p_i)
    # <= \min(n / s^2, \sqrt{n} / s) * ||v||_2^2!
    n = 64
    v = [rng.gauss(0.0, 1.0) for _ in range(n)]
    norm_v = math.sqrt(sum(x * x for x in v))

    for s in [1, 4, 8, 16]:
        exact_var = 0.0
        exact_nnz = 0.0
        for x in v:
            r_i = s * abs(x) / norm_v
            l_i = int(math.floor(r_i))
            p_i = r_i - l_i
            mean_i = norm_v * (1.0 if x >= 0 else -1.0) * (l_i + p_i) / s
            assert abs(mean_i - x) < 1e-12, "Unbiasedness failed"
            exact_var += ((norm_v ** 2) / (s ** 2)) * p_i * (1.0 - p_i)
            # Coordinate is non-zero iff l_i >= 1 (prob 1) or l_i == 0 and rounded up (prob p_i = r_i)
            exact_nnz += 1.0 if l_i >= 1 else p_i

        var_bound = min(n / (s ** 2), math.sqrt(n) / s) * (norm_v ** 2)
        assert exact_var <= var_bound + 1e-12, f"Variance bound violated: {exact_var} > {var_bound}"

        # Lemma A.5 Sparsity bound: E[||Q_s(v)||_0] <= s(s + \sqrt{n})
        sparsity_bound = s * (s + math.sqrt(n))
        assert exact_nnz <= sparsity_bound + 1e-12, f"Sparsity bound violated: {exact_nnz} > {sparsity_bound}"

    # 2. Verify Theorem 3.4 / Theorem A.6 Elias Coding Communication Bound:
    # At s = \sqrt{n} (here s = 8 for n = 64), variance blowup is <= \sqrt{n}/s = 1.0 (at most 2x total second moment),
    # and expected code length (32-bit float norm + Elias-coded run lengths + signs + Elias-coded levels)
    # is bounded by (3/2 + 0.5 * log2(2(s^2+n)/s)) * s(s+\sqrt{n}) + 32 <= 2.818 * n + 32 bits, vs 32*n = 2048 bits!
    s_opt = int(math.isqrt(n))  # 8
    total_bits_trials = []
    for _ in range(200):
        # Sample Q_s(v)
        nz_indices = []
        levels = []
        for idx, x in enumerate(v):
            r_i = s_opt * abs(x) / norm_v
            l_i = int(math.floor(r_i))
            p_i = r_i - l_i
            k_i = l_i + (1 if rng.random() < p_i else 0)
            if k_i > 0:
                nz_indices.append(idx)
                levels.append(k_i)
        bits = 32  # 32-bit float for ||v||_2
        prev_idx = -1
        for idx, k_i in zip(nz_indices, levels):
            gap = idx - prev_idx  # >= 1
            bits += elias_gamma_len(gap)
            bits += 1  # sign bit
            bits += elias_gamma_len(k_i)
            prev_idx = idx
        total_bits_trials.append(bits)

    avg_bits = sum(total_bits_trials) / len(total_bits_trials)
    theo_code_bound = 2.818 * n + 32.0
    raw_32bit = 32 * n
    assert avg_bits <= theo_code_bound and avg_bits < raw_32bit * 0.15

    print(
        f"[PASS] Round 378 QSGD (Alistarh et al. 2017): s=sqrt(n)={s_opt}, "
        f"avg_bits={avg_bits:.1f} <= theo_bound={theo_code_bound:.1f} << raw_32bit={raw_32bit} ({raw_32bit/avg_bits:.1f}x compression)"
    )


if __name__ == "__main__":
    main()
