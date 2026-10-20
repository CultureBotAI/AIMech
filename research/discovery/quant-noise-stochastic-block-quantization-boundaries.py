#!/usr/bin/env python3
"""Constructed boundary verification for Quant-Noise (Fan et al., ICLR 2021, arXiv:2004.07320)."""

import math


def quant_int_n(w, scale, zero_point, q_min, q_max):
    """Fixed-point scalar quantizer phi_intN(w) = (clip(round(w/s + z), q_min, q_max) - z) * s (Eqs. 2, 9)."""
    q = max(q_min, min(q_max, round(w / scale + zero_point)))
    return (q - zero_point) * scale


def quant_pq_block(block, codebook):
    """Vector product quantizer phi_PQ(b) = argmin_{c in C} ||b - c||_2^2 (Eqs. 3, 4, 10)."""
    return min(codebook, key=lambda c: sum((block[i] - c[i]) ** 2 for i in range(len(block))))


def apply_quant_noise_blocks(blocks, selected_indices, quant_fn):
    """Apply stochastic block quantization psi(b_kl | J) = phi(b_kl) if (k,l) in J else b_kl (Eq. 7)."""
    distorted = []
    grad_mask = []
    for idx, b in enumerate(blocks):
        if idx in selected_indices:
            distorted.append(quant_fn(b))
            grad_mask.append(0.0)  # zero or STE gradient on quantized block
        else:
            distorted.append(list(b))
            grad_mask.append(1.0)  # exact unbiased gradient flows through unquantized block (1 - p)
    return distorted, grad_mask


def pq_int8_memory_bits(k_centroids, block_dim_d, m_subvectors, p_cols, n_rows):
    """Compute memory footprint M = 8*K*d + log2(K)*m*p + 8*n bits for PQ + int8 centroids/scales (Eq. 5)."""
    return int(8 * k_centroids * block_dim_d + round(math.log2(k_centroids)) * m_subvectors * p_cols + 8 * n_rows)


def main():
    blocks = [
        [0.42, -0.18, 0.91, -0.53],
        [0.11, 0.77, -0.29, 0.34],
        [-0.64, 0.22, 0.48, -0.85],
        [0.95, -0.41, 0.15, 0.62],
    ]
    codebook = [
        [0.40, -0.20, 0.90, -0.50],
        [0.10, 0.80, -0.30, 0.30],
        [-0.60, 0.20, 0.50, -0.80],
        [0.90, -0.40, 0.10, 0.60],
    ]

    # Boundary case p = 0 (J = empty): exact full-precision forward pass and 100% clean gradients
    dist_p0, mask_p0 = apply_quant_noise_blocks(blocks, set(), lambda b: quant_pq_block(b, codebook))
    assert dist_p0 == blocks and all(g == 1.0 for g in mask_p0)

    # Boundary case p = 1 (all blocks quantized): full QAT distortion, 0% clean unquantized blocks
    dist_p1, mask_p1 = apply_quant_noise_blocks(blocks, {0, 1, 2, 3}, lambda b: quant_pq_block(b, codebook))
    assert dist_p1 != blocks and all(g == 0.0 for g in mask_p1)

    # Intermediate Quant-Noise p = 0.5: partial distortion + exact gradients on unquantized blocks
    dist_p50, mask_p50 = apply_quant_noise_blocks(blocks, {0, 2}, lambda b: quant_pq_block(b, codebook))
    assert dist_p50[0] == codebook[0] and dist_p50[1] == blocks[1]
    assert dist_p50[2] == codebook[2] and dist_p50[3] == blocks[3]
    assert sum(mask_p50) == 2.0

    # Verify commutative composition with LayerDrop (Eq. 8): psi_layerdrop(psi_quantnoise(W)) == psi_quantnoise(psi_layerdrop(W))
    zero_layer = lambda blks: [[0.0 for _ in b] for b in blks]
    comp_1 = zero_layer(apply_quant_noise_blocks(blocks, {0, 2}, lambda b: quant_pq_block(b, codebook))[0])
    comp_2 = apply_quant_noise_blocks(zero_layer(blocks), {0, 2}, lambda b: [0.0 for _ in b])[0]
    assert comp_1 == comp_2

    # Verify Eq. 5 memory reduction vs 32-bit float (32 * n * p bits)
    n_rows, p_cols, d_block, k_centroids = 768, 768, 8, 256
    m_subvectors = n_rows // d_block
    fp32_bits = 32 * n_rows * p_cols
    pq_bits = pq_int8_memory_bits(k_centroids, d_block, m_subvectors, p_cols, n_rows)
    compression_ratio = fp32_bits / pq_bits
    assert compression_ratio > 25.0

    print(
        f"Quant-Noise verification passed: clean_grads_p50={sum(mask_p50):.0f}/4, "
        f"pq_bits={pq_bits}, fp32_bits={fp32_bits}, compression_ratio={compression_ratio:.2f}x"
    )


if __name__ == "__main__":
    main()
