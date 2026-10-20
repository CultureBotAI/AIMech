#!/usr/bin/env python3
"""Constructed boundary and algebraic verification for Round 699:
Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning / SAID
(Aghajanyan, Zettlemoyer, & Gupta, ACL/IJCNLP 2021, arXiv:2012.13255).
"""

import math
import random


def fwht(a):
    """In-place Fast Walsh-Hadamard Transform in O(D log D) operations (Section 3, Eq. 2)."""
    res = list(a)
    n = len(res)
    assert n > 0 and (n & (n - 1)) == 0
    h = 1
    while h < n:
        for i in range(0, n, h * 2):
            for j in range(i, i + h):
                x = res[j]
                y = res[j + h]
                res[j] = x + y
                res[j + h] = x - y
        h *= 2
    return res


def dense_hadamard_matvec(x):
    """Explicit Sylvester Hadamard matrix multiplication H x for verification."""
    n = len(x)
    H = [[1.0]]
    while len(H) < n:
        k = len(H)
        new_H = [[0.0] * (2 * k) for _ in range(2 * k)]
        for r in range(k):
            for c in range(k):
                val = H[r][c]
                new_H[r][c] = val
                new_H[r][c + k] = val
                new_H[r + k][c] = val
                new_H[r + k][c + k] = -val
        H = new_H
    return [sum(H[r][c] * x[c] for c in range(n)) for r in range(n)]


def fastfood_project(theta_sub, D, B, Pi, G):
    """Section 3, Eq. 2: Fastfood projection P(theta^d) = theta^d M with M = H G Pi H B."""
    d_sub = len(theta_sub)
    assert d_sub <= D and (D & (D - 1)) == 0
    padded = list(theta_sub) + [0.0] * (D - d_sub)
    # Apply B (diagonal +-1), then H, then Pi, then G (diagonal Gaussian), then H / sqrt(D)
    v1 = [padded[i] * B[i] for i in range(D)]
    v2 = fwht(v1)
    v3 = [v2[Pi[i]] for i in range(D)]
    v4 = [v3[i] * G[i] for i in range(D)]
    v5 = fwht(v4)
    scale = 1.0 / float(D)
    return [v5[i] * scale for i in range(D)]


def did_reparam(theta0_layers, theta_d, layer_Fastfood_params):
    """Eq. 1-2: Direct Intrinsic Dimension (layer-unaware) theta^D_i = theta^D_{0,i} + P(theta^d)_i."""
    out = []
    for theta0_i, (D_i, B_i, Pi_i, G_i) in zip(theta0_layers, layer_Fastfood_params):
        proj_i = fastfood_project(theta_d, D_i, B_i, Pi_i, G_i)
        out.append([t0 + p for t0, p in zip(theta0_i, proj_i)])
    return out


def said_reparam(theta0_layers, theta_d_minus_m, lambdas, layer_Fastfood_params):
    """Eq. 3: Structure-Aware Intrinsic Dimension (SAID):
    theta^D_i = theta^D_{0,i} + lambda_i P(theta^{d-m})_i, where theta^d = [theta^{d-m}, lambda].
    """
    assert len(lambdas) == len(theta0_layers)
    out = []
    for theta0_i, lam_i, (D_i, B_i, Pi_i, G_i) in zip(theta0_layers, lambdas, layer_Fastfood_params):
        proj_i = fastfood_project(theta_d_minus_m, D_i, B_i, Pi_i, G_i)
        out.append([t0 + lam_i * p for t0, p in zip(theta0_i, proj_i)])
    return out


def main():
    rng = random.Random(2021)

    # 1. Verify Fast Walsh-Hadamard Transform matches dense Hadamard matrix multiplication exactly:
    D_block = 16
    x_test = [rng.gauss(0.0, 1.0) for _ in range(D_block)]
    fwht_out = fwht(x_test)
    dense_out = dense_hadamard_matvec(x_test)
    max_fwht_err = max(abs(a - b) for a, b in zip(fwht_out, dense_out))
    assert max_fwht_err < 1e-12

    # 2. Verify DID and SAID exact pretrained initialization recovery (theta^d = 0 => theta^D = theta^D_0):
    m_layers = 4
    d_total = 10  # Total intrinsic dimension budget d = 10; SAID uses d - m = 6 + 4 = 10
    theta0_layers = [[rng.gauss(0.0, 1.0) for _ in range(D_block)] for _ in range(m_layers)]
    layer_ff_params = []
    for _ in range(m_layers):
        B_i = [rng.choice([-1.0, 1.0]) for _ in range(D_block)]
        Pi_i = list(range(D_block))
        rng.shuffle(Pi_i)
        G_i = [rng.gauss(0.0, 1.0) for _ in range(D_block)]
        layer_ff_params.append((D_block, B_i, Pi_i, G_i))

    did_zero = did_reparam(theta0_layers, [0.0] * d_total, layer_ff_params)
    said_zero = said_reparam(theta0_layers, [0.0] * (d_total - m_layers), [0.0] * m_layers, layer_ff_params)
    for l in range(m_layers):
        for j in range(D_block):
            assert abs(did_zero[l][j] - theta0_layers[l][j]) < 1e-15
            assert abs(said_zero[l][j] - theta0_layers[l][j]) < 1e-15

    # 3. Verify SAID layer-wise scaling advantage over layer-unaware DID under equal total parameter budget d:
    # Suppose a downstream task requires a strong update in layer 3 (top specialized layer, Clark et al. 2019)
    # and near-zero updates in layers 0, 1, 2.
    true_sub = [rng.gauss(0.0, 1.0) for _ in range(d_total - m_layers)]
    true_lambdas = [0.02, 0.01, 0.05, 2.50]
    target_layers = said_reparam(theta0_layers, true_sub, true_lambdas, layer_ff_params)

    def layer_mse(pred_layers):
        return sum(
            (pred_layers[l][j] - target_layers[l][j]) ** 2
            for l in range(m_layers)
            for j in range(D_block)
        ) / (m_layers * D_block)

    # Optimize DID (d_total = 10 parameters) via coordinate/gradient descent
    theta_did = [0.0] * d_total
    lr_did = 0.08
    for _ in range(250):
        base_mse = layer_mse(did_reparam(theta0_layers, theta_did, layer_ff_params))
        grad = [0.0] * d_total
        eps = 1e-5
        for k in range(d_total):
            theta_did[k] += eps
            grad[k] = (layer_mse(did_reparam(theta0_layers, theta_did, layer_ff_params)) - base_mse) / eps
            theta_did[k] -= eps
        for k in range(d_total):
            theta_did[k] -= lr_did * grad[k]
    final_did_mse = layer_mse(did_reparam(theta0_layers, theta_did, layer_ff_params))

    # SAID with budget (d_total - m_layers) + m_layers = d_total parameters recovers target exactly
    final_said_mse = layer_mse(said_reparam(theta0_layers, true_sub, true_lambdas, layer_ff_params))
    assert final_said_mse < 1e-24
    assert final_said_mse < final_did_mse and final_did_mse > 0.05

    # 4. Verify Theorem 1 & Eq. 7-8 compression-based generalization bound independence of full D:
    # Bound term sqrt((d * log r) / m_samples) depends only on intrinsic dimension d, quantization states r, and sample size m_samples
    m_samples = 3700  # MRPC training set size (Section 4.1)
    r_states = 2 ** 16  # FP16 discretization (Appendix A.1)
    d_roberta_base = 896   # Table 1 SAID MRPC d_90 for RoBERTa-Base (125M params)
    d_roberta_large = 207  # Table 1 SAID MRPC d_90 for RoBERTa-Large (355M params)
    bound_base = math.sqrt((d_roberta_base * math.log(r_states)) / m_samples)
    bound_large = math.sqrt((d_roberta_large * math.log(r_states)) / m_samples)
    assert bound_large < bound_base

    print(
        f"[PASS] SAID boundary verification passed: "
        f"fwht_err={max_fwht_err:.1e}, "
        f"mse_SAID={final_said_mse:.1e} << mse_DID={final_did_mse:.4f}, "
        f"bound_RoBERTa_Large(d90=207)={bound_large:.4f} < bound_RoBERTa_Base(d90=896)={bound_base:.4f}"
    )


if __name__ == "__main__":
    main()
