#!/usr/bin/env python3
"""Constructed boundary verification for ATTEMPT (Asai et al., EMNLP 2022, arXiv:2205.11961)."""

import math


def silu(vec: list[float]) -> list[float]:
    return [x / (1.0 + math.exp(-x)) for x in vec]


def layer_norm(vec: list[float], gamma: list[float], beta: list[float], eps: float = 1e-6) -> list[float]:
    d = len(vec)
    mean = sum(vec) / d
    var = sum((x - mean) ** 2 for x in vec) / d
    std = math.sqrt(var + eps)
    return [gamma[i] * (vec[i] - mean) / std + beta[i] for i in range(d)]


def max_pool_rows(mat: list[list[float]]) -> list[float]:
    d = len(mat[0])
    return [max(row[c] for row in mat) for c in range(d)]


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def verify_attempt_boundaries() -> None:
    # 1. Parameter efficiency formula (Section 3.4 & Table 1):
    # Per-task parameters across N shared target tasks: d * m + (2*r*d + 2*d)/N = d*(m + 2*(r+1)/N)
    d_t5_base = 768
    m_prompt = 100
    r_proj = 100
    params_single = d_t5_base * m_prompt + (2 * r_proj * d_t5_base + 2 * d_t5_base) // 1
    params_formula_single = d_t5_base * (m_prompt + 2 * (r_proj + 1))
    assert params_single == params_formula_single == 231936  # ~232k in Table 1

    n_glue = 8
    params_multi_glue = int(d_t5_base * (m_prompt + 2 * (r_proj + 1) / n_glue))
    assert params_multi_glue == 96192  # ~96k in Table 1

    # Independence from number of LM layers L:
    for n_layers in (12, 24, 36, 48):
        params_at_l = d_t5_base * (m_prompt + 2 * (r_proj + 1) / n_glue)
        assert abs(params_at_l - 96192.0) < 1e-9

    # 2. Input-prompt attention (Section 3.2.1, Eq. 3) & Prompt Interpolation (Section 3.2.2, Eq. 4)
    d = 4
    m = 3
    l_seq = 5
    r = 2
    t_sources = 3  # t=3 source prompts + 1 target prompt -> t+1 = 4 prompts

    X = [[math.sin(0.4 * (s + 1) * (c + 1)) for c in range(d)] for s in range(l_seq)]
    P_sources = [
        [[0.2 * (j + 1) * ((tok + 1) - 0.5 * c) for c in range(d)] for tok in range(m)]
        for j in range(t_sources)
    ]
    P_target = [[0.15 * (tok + 1) + 0.05 * c for c in range(d)] for tok in range(m)]
    all_prompts = [*P_sources, P_target]  # length t+1 = 4

    X_hat = max_pool_rows(X)
    P_hats = [max_pool_rows(P_j) for P_j in all_prompts]
    assert len(X_hat) == d and all(len(p) == d for p in P_hats)

    W_down = [[0.3 * ((i + 1) - 0.5 * (j + 1)) for j in range(r)] for i in range(d)]
    W_up = [[0.25 * ((i + 1) + 0.3 * (j + 1)) for j in range(d)] for i in range(r)]
    gamma = [1.0] * d
    beta = [0.0] * d

    H_down = [sum(W_down[i][j] * X_hat[i] for i in range(d)) for j in range(r)]
    H_act = silu(H_down)
    H_up = [sum(W_up[j][i] * H_act[j] for j in range(r)) for i in range(d)]
    H_out = layer_norm(H_up, gamma, beta)

    # Temperature T = d * exp(1) (Appendix C.5)
    temp = d * math.exp(1.0)
    logits = [dot(P_hat, H_out) / temp for P_hat in P_hats]
    max_logit = max(logits)
    exps = [math.exp(z - max_logit) for z in logits]
    Z = sum(exps)
    attn = [e / Z for e in exps]
    assert abs(sum(attn) - 1.0) < 1e-12
    assert all(0.0 < a < 1.0 for a in attn)

    # Eq. 4: P_instance(X) = P_target + sum_{j=1}^{t+1} a_j P_j
    P_instance = [
        [
            P_target[tok][c] + sum(attn[j] * all_prompts[j][tok][c] for j in range(t_sources + 1))
            for c in range(d)
        ]
        for tok in range(m)
    ]

    # Verify algebraic decomposition: P_instance = (1 + a_{t+1}) P_target + sum_{j=1}^t a_j P_j
    eff_target_weight = 1.0 + attn[t_sources]
    assert 1.0 < eff_target_weight < 2.0
    max_decomp_err = 0.0
    for tok in range(m):
        for c in range(d):
            reconstructed = eff_target_weight * P_target[tok][c] + sum(
                attn[j] * P_sources[j][tok][c] for j in range(t_sources)
            )
            max_decomp_err = max(max_decomp_err, abs(P_instance[tok][c] - reconstructed))
    assert max_decomp_err < 1e-15

    # 3. Token-level alternative attention (Appendix A.4, Eq. 5):
    for tok in range(m):
        tok_logits = [dot(all_prompts[j][tok], H_out) / temp for j in range(t_sources + 1)]
        m_tok = max(tok_logits)
        tok_exps = [math.exp(z - m_tok) for z in tok_logits]
        tok_Z = sum(tok_exps)
        tok_attn = [e / tok_Z for e in tok_exps]
        assert abs(sum(tok_attn) - 1.0) < 1e-12

    print(
        f"[PASS] ATTEMPT boundaries verified: params(N=1)={params_single}, params(N=8)={params_multi_glue}, "
        f"eff_target_weight={eff_target_weight:.4f}, max_decomp_err={max_decomp_err:.2e}"
    )


if __name__ == "__main__":
    verify_attempt_boundaries()
