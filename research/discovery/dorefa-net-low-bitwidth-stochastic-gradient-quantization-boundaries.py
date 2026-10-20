#!/usr/bin/env python3
"""Constructed boundary verification for DoReFa-Net (Zhou et al., 2016, arXiv:1606.06160)."""

import json
import math
import random


def quantize_k(r, k):
    """Uniform k-bit quantizer on [0, 1] (Eq. 5)."""
    levels = (1 << k) - 1
    return round(levels * r) / levels


def dorefa_weight_quantize(weights, k):
    """Deterministic k-bit weight quantization via normalized tanh (Eq. 9) or mean scale for k=1 (Eq. 7)."""
    if k == 1:
        scale = sum(abs(w) for w in weights) / len(weights)
        return [(1.0 if w >= 0 else -1.0) * scale for w in weights]
    t = [math.tanh(w) for w in weights]
    max_t = max(abs(v) for v in t)
    return [2.0 * quantize_k(v / (2.0 * max_t) + 0.5, k) - 1.0 for v in t]


def dorefa_grad_quantize(dr, k, rng=None):
    """Stochastic k-bit gradient quantization with uniform noise N(k) (Eqs. 12-14)."""
    max_dr = max(abs(g) for g in dr)
    if max_dr == 0.0:
        return [0.0 for _ in dr]
    levels = (1 << k) - 1
    out = []
    for g in dr:
        noise = (rng.uniform(-0.5, 0.5) / levels) if rng is not None else 0.0
        val = min(1.0, max(0.0, g / (2.0 * max_dr) + 0.5 + noise))
        q = quantize_k(val, k)
        out.append(2.0 * max_dr * (q - 0.5))
    return out


def bitwise_dot_uint2(x_int, y_int):
    """Bitwise convolution kernel dot product for 2-bit unsigned integers (Eq. 3)."""
    total = 0
    for m in range(2):
        for k in range(2):
            xm_bits = [((v >> m) & 1) for v in x_int]
            yk_bits = [((v >> k) & 1) for v in y_int]
            bitcount_and = sum(a & b for a, b in zip(xm_bits, yk_bits))
            total += (1 << (m + k)) * bitcount_and
    return total


def main():
    # 1. Verify Eq. 3 bitwise dot product matches integer inner product
    x_u2 = [0, 1, 2, 3, 2, 1, 3, 3]
    y_u2 = [3, 2, 1, 3, 0, 2, 2, 1]
    exact_dot = sum(a * b for a, b in zip(x_u2, y_u2))
    bit_dot = bitwise_dot_uint2(x_u2, y_u2)
    assert exact_dot == bit_dot == 24

    # 2. Verify Eq. 9 deterministic weight quantization bounds in [-1, 1]
    w_fp = [-1.8, -0.5, -0.1, 0.2, 0.7, 2.1]
    w_q2 = dorefa_weight_quantize(w_fp, k=2)
    assert all(-1.0 - 1e-9 <= v <= 1.0 + 1e-9 for v in w_q2)
    assert min(w_q2) == -1.0 or max(w_q2) == 1.0

    # 3. Verify Eqs. 12-14 stochastic gradient quantization is unbiased whereas deterministic fails on small gradients
    rng = random.Random(42)
    dr = [0.08, -0.45, 1.0]  # max_dr = 1.0; for k=2 (levels=3), step is 2.0/3 = 0.6667
    det_g0 = dorefa_grad_quantize(dr, k=2, rng=None)[0]
    stoch_trials = [dorefa_grad_quantize(dr, k=2, rng=rng)[0] for _ in range(4000)]
    mean_stoch_g0 = sum(stoch_trials) / len(stoch_trials)

    # Deterministic rounding collapses small gradient 0.08 to -0.3333 or +0.3333 (bias > 0.25),
    # whereas stochastic dithering preserves E[f_gamma^k(dr)] == dr within Monte Carlo tolerance.
    det_err = abs(det_g0 - dr[0])
    stoch_err = abs(mean_stoch_g0 - dr[0])
    assert det_err > 0.24
    assert stoch_err < 0.015

    # 4. Verify Eq. 15 commute property quantize_k(max(a, b)) == max(quantize_k(a), quantize_k(b))
    for a in [0.12, 0.48, 0.81]:
        for b in [0.29, 0.51, 0.92]:
            assert abs(quantize_k(max(a, b), 3) - max(quantize_k(a, 3), quantize_k(b, 3))) < 1e-12

    summary = {
        "concept": "DoReFaNetTrainingLowBitwidthConvolutionalNeuralNetworksWithLowBitwidthGradients",
        "bitwise_dot_product_eq3": bit_dot,
        "deterministic_small_grad_bias": round(det_err, 5),
        "stochastic_small_grad_mean_bias": round(stoch_err, 5),
        "max_pooling_commutation_eq15_verified": True,
        "verification": "passed",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
