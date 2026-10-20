#!/usr/bin/env python3
"""Constructed boundary and algebraic verification for Round 703:
Parameter-efficient Multi-task Fine-tuning for Transformers via Shared Hypernetworks
(HyperFormer / HyperFormer++) (Karimi Mahabadi et al., ACL/IJCNLP 2021, arXiv:2106.04489).
"""

import math
import random


def relu(x):
    return x if x > 0.0 else 0.0


def gelu(x):
    return 0.5 * x * (1.0 + math.erf(x / math.sqrt(2.0)))


def layer_norm_vec(x, gamma, beta, eps=1e-6):
    """Section 2.2 Eq. 4: Conditional Layer Normalization LN^l_tau(x) = gamma (o) (x - mu)/sigma + beta."""
    m = sum(x) / len(x)
    var = sum((v - m) ** 2 for v in x) / len(x)
    std = math.sqrt(var + eps)
    return [gamma[i] * ((x[i] - m) / std) + beta[i] for i in range(len(x))]


def matvec(W, x):
    return [sum(row[j] * x[j] for j in range(len(x))) for row in W]


def task_projector_h_prime(z_tau, l_i, p_j, W1, W2, gamma_p, beta_p):
    """Section 2.4 Eq. 8: I_tau = LayerNorm(h'_I(concat(z_tau, l_i, p_j))),
    where h'_I is a two-layer MLP with ReLU nonlinearity (Section 2.3 Eq. 5).
    """
    concat_in = list(z_tau) + list(l_i) + list(p_j)
    hidden = [relu(val) for val in matvec(W1, concat_in)]
    raw_emb = matvec(W2, hidden)
    return layer_norm_vec(raw_emb, gamma_p, beta_p)


def hypernetwork_generate(I_tau, W_U, W_D, W_gamma, W_beta, h, d):
    """Section 2.3 Eqs. 6-7:
    (U^l_tau, D^l_tau) = (W^U, W^D) I_tau
    (gamma^l_tau, beta^l_tau) = (W^gamma, W^beta) I_tau.
    """
    u_flat = matvec(W_U, I_tau)
    d_flat = matvec(W_D, I_tau)
    U = [u_flat[r * d : (r + 1) * d] for r in range(h)]  # h x d (maps d -> h)
    D = [d_flat[r * h : (r + 1) * h] for r in range(d)]  # d x h (maps h -> d)
    gamma = matvec(W_gamma, I_tau)
    beta = matvec(W_beta, I_tau)
    return U, D, gamma, beta


def conditional_adapter_forward(x, U, D, gamma, beta):
    """Section 2.1 Eq. 3: A^l_tau(x) = LN^l_tau(U^l_tau(GeLU(D^l_tau(x)))) + x."""
    down = [gelu(val) for val in matvec(D, x)]
    up = matvec(U, down)
    normed = layer_norm_vec(up, gamma, beta)
    return [normed[i] + x[i] for i in range(len(x))]


def standard_adapters_param_count(T, L, h, d):
    """Section 4.1: Standard Adapters across T tasks and L encoder+decoder layers:
    4 * T * L * (2*h*d + 2*h).
    """
    return 4 * T * L * (2 * h * d + 2 * h)


def hyperformer_pp_param_count(T, L, h, d, t=64, e=128):
    """Section 4.1: HyperFormer++ parameter formula:
    t*(T + 4 + 2*L) [Task features] + 8*t*e + 2*t*(2*h*d + 2*h) [Hypernetworks].
    """
    task_features = t * (T + 4 + 2 * L)
    hypernetworks = 8 * t * e + 2 * t * (2 * h * d + 2 * h)
    return task_features, hypernetworks, task_features + hypernetworks


def main():
    rng = random.Random(2021)

    # 1. Verify Section 4.1 parameter complexity scaling on T5-Base (L=12, h=768, r=32 -> d=24, t=64, e=128, T=8 GLUE tasks):
    T_glue = 8
    L_t5_base = 12
    h_t5_base = 768
    d_bottleneck = 768 // 32  # d = 24
    t_dim = 64
    e_dim = 128

    p_adapters = standard_adapters_param_count(T_glue, L_t5_base, h_t5_base, d_bottleneck)
    tf_params, hn_params, p_hf_pp = hyperformer_pp_param_count(
        T_glue, L_t5_base, h_t5_base, d_bottleneck, t=t_dim, e=e_dim
    )
    # Section 4.1: Leading coefficient ratio is 2*T*L / t = 2*8*12 / 64 = 192 / 64 = 3.0:
    leading_factor_ratio = (2.0 * T_glue * L_t5_base) / float(t_dim)
    assert abs(leading_factor_ratio - 3.0) < 1e-12
    assert p_adapters / p_hf_pp > 2.90

    # At T = 16 tasks, HyperFormer++ achieves > 5.8x reduction because hypernetwork size hn_params is constant:
    p_adapters_16 = standard_adapters_param_count(16, L_t5_base, h_t5_base, d_bottleneck)
    _, hn_params_large, p_hf_pp_16 = hyperformer_pp_param_count(
        T=16, L=L_t5_base, h=h_t5_base, d=d_bottleneck, t=t_dim, e=e_dim
    )
    assert hn_params == hn_params_large
    assert p_adapters_16 / p_hf_pp_16 > 5.80

    # 2. Verify HyperFormer++ conditional adapter generation (Eqs. 3-8):
    t_small, e_small, h_small, d_small = 6, 8, 10, 3
    W1 = [[rng.gauss(0.0, 0.2) for _ in range(3 * t_small)] for _ in range(e_small)]
    W2 = [[rng.gauss(0.0, 0.2) for _ in range(e_small)] for _ in range(t_small)]
    gamma_p = [1.0] * t_small
    beta_p = [0.0] * t_small

    W_U = [[rng.gauss(0.0, 0.1) for _ in range(t_small)] for _ in range(h_small * d_small)]
    W_D = [[rng.gauss(0.0, 0.1) for _ in range(t_small)] for _ in range(d_small * h_small)]
    W_gamma = [[rng.gauss(0.0, 0.1) for _ in range(t_small)] for _ in range(h_small)]
    W_beta = [[rng.gauss(0.0, 0.1) for _ in range(t_small)] for _ in range(h_small)]

    z_task1 = [rng.gauss(0.0, 1.0) for _ in range(t_small)]
    z_task2 = [rng.gauss(0.0, 1.0) for _ in range(t_small)]
    l_layer0 = [rng.gauss(0.0, 1.0) for _ in range(t_small)]
    l_layer1 = [rng.gauss(0.0, 1.0) for _ in range(t_small)]
    p_attn = [rng.gauss(0.0, 1.0) for _ in range(t_small)]
    p_ffn = [rng.gauss(0.0, 1.0) for _ in range(t_small)]

    I_t1_l0_attn = task_projector_h_prime(z_task1, l_layer0, p_attn, W1, W2, gamma_p, beta_p)
    I_t2_l0_attn = task_projector_h_prime(z_task2, l_layer0, p_attn, W1, W2, gamma_p, beta_p)
    I_t1_l1_attn = task_projector_h_prime(z_task1, l_layer1, p_attn, W1, W2, gamma_p, beta_p)
    I_t1_l0_ffn = task_projector_h_prime(z_task1, l_layer0, p_ffn, W1, W2, gamma_p, beta_p)

    # All conditioned embeddings are distinct across tasks, layers, and adapter positions:
    assert I_t1_l0_attn != I_t2_l0_attn
    assert I_t1_l0_attn != I_t1_l1_attn
    assert I_t1_l0_attn != I_t1_l0_ffn

    U1, D1, g1, b1 = hypernetwork_generate(I_t1_l0_attn, W_U, W_D, W_gamma, W_beta, h_small, d_small)
    U2, D2, g2, b2 = hypernetwork_generate(I_t2_l0_attn, W_U, W_D, W_gamma, W_beta, h_small, d_small)
    assert U1 != U2 and D1 != D2

    x_in = [rng.gauss(0.0, 1.0) for _ in range(h_small)]
    out1 = conditional_adapter_forward(x_in, U1, D1, g1, b1)
    out2 = conditional_adapter_forward(x_in, U2, D2, g2, b2)
    assert len(out1) == h_small and out1 != out2

    # When gamma = 0 and beta = 0, residual connection preserves input x_in exactly:
    out_id = conditional_adapter_forward(x_in, U1, D1, [0.0] * h_small, [0.0] * h_small)
    assert all(abs(a - b) < 1e-15 for a, b in zip(out_id, x_in))

    print(
        f"[PASS] HyperFormer++ boundary verification passed: "
        f"p_hf_pp={p_hf_pp:,} vs p_adapters={p_adapters:,} ({p_adapters/p_hf_pp:.2f}x reduction), "
        f"const_hn_params={hn_params:,}"
    )


if __name__ == "__main__":
    main()
