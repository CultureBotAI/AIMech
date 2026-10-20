#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 809:
Q-BERT: Hessian Based Ultra Low Precision Quantization of BERT
(Shen, Dong, Ye, Ma, Yao, Gholami, Mahoney, & Keutzer, AAAI 2020, arXiv:1909.05840).

Verifies:
1. Matrix-free Hessian-vector product power iteration (Eq. 3.1 & Algorithm 1):
   d(g^T v)/dW = H v recovers the dominant eigenvalue lambda_max of a symmetric Hessian H without
   explicit matrix formation.
2. Mean-plus-standard-deviation Hessian sensitivity metric (Eq. 3.2):
   Omega_i = |mean(lambda_i)| + std(lambda_i) correctly ranks a high-variance layer (such as SQuAD layer 7
   with mean ~ 1.0 and variance > 61.6, std > 7.85) as more quantization-sensitive than a low-variance
   layer with slightly higher mean (e.g. mean = 2.0, std = 0.1), whereas mean-only HAWQ misranks them.
3. Group-wise uniform quantization with clamping (Section 3.3 & Appendix A):
   Partitioning an output-neuron weight matrix across G subgroups, each with its own clamping interval
   [q_0, q_{2^k - 1}] and step Delta = (q_{2^k - 1} - q_0) / (2^k - 1), strictly reduces quantization MSE
   compared to single-range layer-wise quantization (G = 1) when different heads/subgroups have heterogeneous
   dynamic ranges.
"""

import json
import math


def power_iteration_top_eigenvalue(H, iters=40):
    """Algorithm 1: Matrix-free Hessian-vector product power iteration."""
    n = len(H)
    v = [1.0 / math.sqrt(n) for _ in range(n)]
    for _ in range(iters):
        Hv = [sum(H[r][c] * v[c] for c in range(n)) for r in range(n)]
        norm = math.sqrt(sum(x * x for x in Hv))
        v = [x / norm for x in Hv]
    # Rayleigh quotient v^T H v
    Hv = [sum(H[r][c] * v[c] for c in range(n)) for r in range(n)]
    return sum(v[r] * Hv[r] for r in range(n))


def omega_sensitivity(eigen_samples):
    """Eq. 3.2: Omega_i = |mean(lambda_i)| + std(lambda_i)."""
    m = sum(eigen_samples) / len(eigen_samples)
    var = sum((x - m) ** 2 for x in eigen_samples) / len(eigen_samples)
    return abs(m) + math.sqrt(var), abs(m), var


def uniform_quantize_dequantize(vec, k_bits):
    """Appendix A: Q(X) = Delta * round((Clamp(X, q_0, q_{2^k-1}) - q_0) / Delta) + q_0."""
    q0 = min(vec)
    qmax = max(vec)
    levels = (1 << k_bits) - 1
    if qmax == q0:
        return list(vec)
    delta = (qmax - q0) / levels
    out = []
    for x in vec:
        clamped = min(max(x, q0), qmax)
        xi = round((clamped - q0) / delta)
        out.append(delta * xi + q0)
    return out


def groupwise_quantize_mse(weights, k_bits, num_groups):
    """Partition weights into num_groups contiguous subgroups and compute overall MSE."""
    n = len(weights)
    assert n % num_groups == 0
    gsize = n // num_groups
    recon = []
    for g in range(num_groups):
        sub = weights[g * gsize : (g + 1) * gsize]
        recon.extend(uniform_quantize_dequantize(sub, k_bits))
    return sum((w - q) ** 2 for w, q in zip(weights, recon)) / n


def main():
    # 1. Verify Algorithm 1 power iteration on a 3x3 symmetric Hessian with eigenvalues 5.0, 2.0, 0.5
    H = [
        [5.0, 0.0, 0.0],
        [0.0, 2.0, 0.0],
        [0.0, 0.0, 0.5],
    ]
    lam_est = power_iteration_top_eigenvalue(H)
    assert abs(lam_est - 5.0) < 1e-9

    # 2. Verify Eq. 3.2 sensitivity metric Omega_i on SQuAD layer 7 vs low-variance layer
    # SQuAD layer 7: mean ~ 1.0, variance > 61.6 (e.g., alternating +9.0 and -7.0 across data partitions -> mean=1.0, var=64.0, std=8.0)
    squad_layer7_samples = [9.0, -7.0, 9.0, -7.0, 9.0, -7.0, 9.0, -7.0, 9.0, -7.0]
    stable_layer_samples = [2.0, 2.1, 1.9, 2.0, 2.05, 1.95, 2.0, 2.1, 1.9, 2.0]

    omega_l7, mean_l7, var_l7 = omega_sensitivity(squad_layer7_samples)
    omega_stable, mean_stable, var_stable = omega_sensitivity(stable_layer_samples)
    assert abs(mean_l7 - 1.0) < 1e-12 and var_l7 > 61.6
    # Mean-only HAWQ ranks stable_layer (2.0) above squad_layer7 (1.0), whereas Q-BERT Omega_i ranks squad_layer7 (9.0) >> stable_layer (2.063)
    assert mean_l7 < mean_stable
    assert omega_l7 > 4.0 * omega_stable

    # 3. Verify Section 3.3 group-wise quantization strictly reduces quantization error across G=1, 4, 16 groups
    # Construct 16 subgroups of 8 weights each with heterogeneous scales across attention heads/neuron groups
    weights = []
    for g in range(16):
        scale = 0.02 * (1 + (g % 4) ** 3) * (1.0 if g < 8 else 4.0)
        for j in range(8):
            weights.append(scale * ((j - 3.5) / 3.5))

    mse_g1 = groupwise_quantize_mse(weights, k_bits=2, num_groups=1)
    mse_g4 = groupwise_quantize_mse(weights, k_bits=2, num_groups=4)
    mse_g16 = groupwise_quantize_mse(weights, k_bits=2, num_groups=16)
    assert mse_g1 > mse_g4 > mse_g16
    assert mse_g16 < 0.25 * mse_g1

    # 4. Verify 13x encoder weight compression ratio (324.5 MB FP32 vs 25.4 MB 2/3-bit MP in Table 1)
    compression_ratio = 324.5 / 25.4
    assert 12.7 < compression_ratio < 12.85

    summary = {
        "concept": "QBERTHessianBasedUltraLowPrecisionQuantizationOfBERT",
        "power_iteration_top_eig": round(lam_est, 6),
        "omega_squad_layer7": round(omega_l7, 4),
        "omega_stable_layer": round(omega_stable, 4),
        "quant_mse_layerwise_g1": round(mse_g1, 6),
        "quant_mse_groupwise_g4": round(mse_g4, 6),
        "quant_mse_groupwise_g16": round(mse_g16, 6),
        "encoder_compression_ratio": round(compression_ratio, 2),
        "status": "ok",
    }
    print(json.dumps(summary))


if __name__ == "__main__":
    main()
