#!/usr/bin/env python3
"""Constructed boundary verification for Iterative Product Quantization / And the Bit Goes Down (Stock et al., ICLR 2020)."""


def frobenius_weight_error_sq(w_vec, c_vec):
    """Standard PQ weight objective ||w - c||_2^2 (Eq. 1)."""
    return sum((w_vec[i] - c_vec[i]) ** 2 for i in range(len(w_vec)))


def activation_recon_error_sq(x_mat, w_vec, c_vec):
    """In-domain output activation objective ||x (w - c)||_2^2 (Eqs. 2-3)."""
    err = 0.0
    for row in x_mat:
        diff_dot = sum(row[d] * (w_vec[d] - c_vec[d]) for d in range(len(w_vec)))
        err += diff_dot * diff_dot
    return err


def codeword_distillation_step(codeword, subvector_grads, lr):
    """Update codeword by averaging gradients of assigned subvectors c <- c - eta * (1/|I_c|) sum_{p in I_c} dL/db_p (Eq. 5)."""
    n_assigned = len(subvector_grads)
    assert n_assigned > 0
    dim = len(codeword)
    return [
        codeword[d] - lr * (sum(g[d] for g in subvector_grads) / n_assigned)
        for d in range(dim)
    ]


def layer_storage_bytes(c_in, c_out, k_spatial, block_size_d, num_centroids_k):
    """Compute byte-aligned index storage + float16 codebook overhead (Section 4.1 Metrics)."""
    import math
    total_weights = c_in * c_out * k_spatial * k_spatial
    num_blocks = total_weights // block_size_d
    bits_per_index = int(round(math.log2(num_centroids_k)))
    index_bytes = (num_blocks * bits_per_index) // 8
    codebook_fp16_bytes = num_centroids_k * block_size_d * 2
    return index_bytes, codebook_fp16_bytes


def main():
    # Construct anisotropic in-domain activations x where dim 0 has 100x higher variance than dim 1
    x_mat = [
        [10.0, 0.1],
        [-10.0, 0.2],
        [8.0, -0.1],
        [-8.0, -0.2],
    ]
    w_target = [1.0, 1.0]
    # Codeword A is closer in Euclidean weight norm (||w - c_A||^2 = 0.04 + 0.01 = 0.05)
    # Codeword B matches the high-energy activation direction (||w - c_B||^2 = 0.0001 + 0.25 = 0.2501)
    c_standard_pq = [0.80, 0.90]
    c_activation_pq = [0.99, 0.50]

    w_err_std = frobenius_weight_error_sq(w_target, c_standard_pq)
    w_err_act = frobenius_weight_error_sq(w_target, c_activation_pq)
    assert w_err_std < w_err_act  # Standard PQ prefers c_standard_pq

    act_err_std = activation_recon_error_sq(x_mat, w_target, c_standard_pq)
    act_err_act = activation_recon_error_sq(x_mat, w_target, c_activation_pq)
    assert act_err_act < act_err_std * 0.05  # Activation-weighted PQ drastically reduces output error

    # Boundary case: isotropic activations x^T x = I -> activation error equals Frobenius weight error
    x_iso = [[1.0, 0.0], [0.0, 1.0]]
    assert abs(activation_recon_error_sq(x_iso, w_target, c_standard_pq) - w_err_std) < 1e-12

    # Verify Eq. 5 distillation codeword gradient averaging reduces KL loss on assigned subvectors
    c_init = [0.5, -0.5]
    assigned_grads = [[0.2, -0.4], [0.4, -0.2], [0.3, -0.3]]
    c_updated = codeword_distillation_step(c_init, assigned_grads, lr=0.1)
    assert abs(c_updated[0] - (0.5 - 0.1 * 0.3)) < 1e-12
    assert abs(c_updated[1] - (-0.5 - 0.1 * (-0.3))) < 1e-12

    # Verify Section 4.1 Metrics example: 128 x 128 x 3 x 3 conv with k=256, d=9 -> 16,384B index + 4,608B (4.5 KB) centroids
    idx_bytes, cb_bytes = layer_storage_bytes(128, 128, 3, 9, 256)
    assert idx_bytes == 16384 and cb_bytes == 4608

    print(
        f"iPQ verification passed: act_err_act={act_err_act:.4f} << act_err_std={act_err_std:.4f}, "
        f"idx_bytes={idx_bytes}, cb_bytes={cb_bytes}"
    )


if __name__ == "__main__":
    main()
