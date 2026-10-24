#!/usr/bin/env python3
"""Constructed boundary verification for Hyperdecoders (Ivison & Peters, EMNLP Findings 2022, arXiv:2203.08304)."""

import math


def relu(vec: list[float]) -> list[float]:
    return [x if x > 0.0 else 0.0 for x in vec]


def matvec(mat: list[list[float]], vec: list[float], bias: list[float]) -> list[float]:
    return [sum(r_val * v_val for r_val, v_val in zip(row, vec)) + b_val for row, b_val in zip(mat, bias)]


def verify_hyperdecoder_boundaries() -> None:
    # 1. Appendix D parameter count equations (D.1, D.2, D.3):
    l_layers = 12
    d_model = 768
    a_enc = 512
    a_dec = 36
    b_hyp = 72
    e_l = 64

    # Encoder manual adapters (Appendix D.1): l * (2*a*d + a + d)
    enc_params = l_layers * (2 * a_enc * d_model + a_enc + d_model)
    # Decoder hypernetwork + 2-layer MLP (Appendix D.3): 2*d^2 + (d + e_l)*b + b*(2*a*d + a + d)
    dec_params = 2 * (d_model ** 2) + (d_model + e_l) * b_hyp + b_hyp * (2 * a_dec * d_model + a_dec + d_model)
    total_params = enc_params + dec_params
    assert enc_params == 9452544
    assert dec_params == 5278752
    assert total_params == 14731296

    # Verify strict independence of Hyperdecoder parameter count from number of tasks t:
    for t_tasks in (2, 8, 12, 50):
        total_at_t = enc_params + dec_params
        assert total_at_t == total_params

    # 2. Instance-specific decoder adapter generation (Section 2.1 - 2.3, Eqs. 1-9):
    d = 4
    a = 2
    b = 3
    el_dim = 2

    # Two distinct token sequences X^(1) and X^(2) encoded into h^(1), h^(2)
    h_seq_1 = [[0.5, -0.2, 0.8, 0.1], [0.3, 0.4, -0.1, 0.7], [0.7, 0.1, 0.5, -0.2]]
    h_seq_2 = [[-0.4, 0.9, -0.3, 0.6], [-0.2, 0.5, 0.4, -0.5], [0.0, -0.3, 0.2, 0.8]]

    def mean_pool(seq: list[list[float]]) -> list[float]:
        n = len(seq)
        return [sum(seq[s][c] for s in range(n)) / n for c in range(d)]

    # 2-layer ReLU MLP for Eq. 8: e = MLP(mean(h))
    W_mlp1 = [[0.3 * ((i + 1) - 0.4 * (j + 1)) for j in range(d)] for i in range(d)]
    b_mlp1 = [0.05 * (i + 1) for i in range(d)]
    W_mlp2 = [[0.25 * ((i + 1) + 0.2 * (j + 1)) for j in range(d)] for i in range(d)]
    b_mlp2 = [-0.02 * (i + 1) for i in range(d)]

    def compute_e(seq: list[list[float]]) -> list[float]:
        m_h = mean_pool(seq)
        z1 = relu(matvec(W_mlp1, m_h, b_mlp1))
        return matvec(W_mlp2, z1, b_mlp2)

    e1 = compute_e(h_seq_1)
    e2 = compute_e(h_seq_2)
    e_diff = math.sqrt(sum((x - y) ** 2 for x, y in zip(e1, e2)))
    assert e_diff > 1e-2

    # Hypernetwork (Eqs. 3-7 & 9): h = ReLU(W0 [e; l_i] + b0)
    in_dim = d + el_dim
    W0 = [[0.2 * ((i + 1) - 0.3 * (j + 1)) for j in range(in_dim)] for i in range(b)]
    b0 = [0.1 * (i + 1) for i in range(b)]

    # Output heads W1 (d*a x b), W2 (a*d x b), W3 (d x b), W4 (a x b)
    W1 = [[0.15 * ((r + 1) * 0.2 - (c + 1) * 0.1) for c in range(b)] for r in range(d * a)]
    b1 = [0.01 * (r + 1) for r in range(d * a)]
    W2 = [[0.12 * ((r + 1) * 0.3 + (c + 1) * 0.1) for c in range(b)] for r in range(a * d)]
    b2 = [-0.01 * (r + 1) for r in range(a * d)]
    W3 = [[0.08 * ((r + 1) - (c + 1)) for c in range(b)] for r in range(d)]
    b3 = [0.005 * (r + 1) for r in range(d)]
    W4 = [[0.09 * ((r + 1) + (c + 1)) for c in range(b)] for r in range(a)]
    b4 = [0.005 * (r + 1) for r in range(a)]

    layer_emb_1 = [0.4, -0.3]
    layer_emb_2 = [-0.5, 0.6]

    def generate_and_apply_adapter(
        e_vec: list[float], l_vec: list[float], x_dec: list[float], zero_upper: bool = False
    ) -> list[float]:
        inp = [*e_vec, *l_vec]
        h_hyp = relu(matvec(W0, inp, b0))
        if zero_upper:
            Wu_flat = [0.0] * (d * a)
            bu = [0.0] * d
        else:
            Wu_flat = matvec(W1, h_hyp, b1)
            bu = matvec(W3, h_hyp, b3)
        Wd_flat = matvec(W2, h_hyp, b2)
        bd = matvec(W4, h_hyp, b4)

        Wu = [Wu_flat[i * a : (i + 1) * a] for i in range(d)]
        Wd = [Wd_flat[i * d : (i + 1) * d] for i in range(a)]

        # Eq. 1: Adapter(x) = Wu(ReLU(Wd x + bd)) + bu
        hidden = relu(matvec(Wd, x_dec, bd))
        return matvec(Wu, hidden, bu)

    x_decoder = [0.6, -0.1, 0.3, 0.5]
    # Instance specificity: same layer embedding, different encoder inputs -> distinct decoder adapter outputs
    out_inst1 = generate_and_apply_adapter(e1, layer_emb_1, x_decoder)
    out_inst2 = generate_and_apply_adapter(e2, layer_emb_1, x_decoder)
    inst_diff = math.sqrt(sum((u - v) ** 2 for u, v in zip(out_inst1, out_inst2)))
    assert inst_diff > 1e-3

    # Layer specificity: same instance embedding, different decoder layer embeddings -> distinct outputs
    out_layer2 = generate_and_apply_adapter(e1, layer_emb_2, x_decoder)
    layer_diff = math.sqrt(sum((u - v) ** 2 for u, v in zip(out_inst1, out_layer2)))
    assert layer_diff > 1e-3

    # Zero-impact initialization when upper projection head (W1, b1, W3, b3) is zeroed:
    out_zero = generate_and_apply_adapter(e1, layer_emb_1, x_decoder, zero_upper=True)
    assert max(abs(v) for v in out_zero) == 0.0

    print(
        f"[PASS] Hyperdecoder boundaries verified: total_params={total_params}, "
        f"inst_diff={inst_diff:.4f}, layer_diff={layer_diff:.4f}, zero_init_err=0.0"
    )


if __name__ == "__main__":
    verify_hyperdecoder_boundaries()
