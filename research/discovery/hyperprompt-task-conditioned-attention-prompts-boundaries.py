#!/usr/bin/env python3
"""Constructed boundary verification for HyperPrompt (He et al., ICML 2022, arXiv:2203.00759)."""

import math


def relu_mat(mat: list[list[float]]) -> list[list[float]]:
    return [[x if x > 0.0 else 0.0 for x in row] for row in mat]


def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    n_rows = len(A)
    n_inner = len(B)
    n_cols = len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(n_inner)) for j in range(n_cols)] for i in range(n_rows)]


def verify_hyperprompt_boundaries() -> None:
    # 1. Exact parameter count formula (Section 3.4 & Appendix A.1):
    # N = d*l*T + 4*(b*d*t) + T*t' + M*t' + (2*t' + t)*e
    d = 768
    l_prompt = 16
    T_tasks = 8
    b_bottleneck = 24
    t_final = 64
    t_raw = 64
    M_layers = 12
    e_hidden = 128

    params_global = (
        d * l_prompt * T_tasks
        + 4 * (b_bottleneck * d * t_final)
        + T_tasks * t_raw
        + M_layers * t_raw
        + (2 * t_raw + t_final) * e_hidden
    )
    # Compare against HyperPrompt-Sep: d*l*T + 2*M*T*(2*d*b) = d*l*T + 4*M*T*b*d
    params_sep = d * l_prompt * T_tasks + 4 * M_layers * T_tasks * b_bottleneck * d
    assert params_global == 4842752
    assert params_sep == 7176192
    assert params_global < params_sep

    # Sub-linear scaling in T: doubling T from 8 to 16 increases params_global by < 3%
    T2 = 16
    params_global_t2 = (
        d * l_prompt * T2
        + 4 * (b_bottleneck * d * t_final)
        + T2 * t_raw
        + M_layers * t_raw
        + (2 * t_raw + t_final) * e_hidden
    )
    rel_increase = (params_global_t2 - params_global) / params_global
    assert rel_increase < 0.025

    # 2. Global HyperNetwork -> Local HyperNetwork -> Key/Value Hyper-Prompts (Eqs. 1-8):
    d_small = 4
    l_small = 2
    L_seq = 3
    b_small = 2
    t_dim = 3

    # Layer-aware task embedding I^m_tau in R^{t_dim}
    I_m_tau = [0.5, -0.3, 0.8]

    # Global hypernetwork weights WDk, WUk in R^{(d*b) x t_dim} and WDv, WUv in R^{(d*b) x t_dim}
    def make_local_mat(seed: float, rows: int, cols: int) -> list[list[float]]:
        flat = [
            sum((seed * (idx + 1) + 0.1 * (c + 1)) * I_m_tau[c] for c in range(t_dim))
            for idx in range(rows * cols)
        ]
        return [flat[r * cols : (r + 1) * cols] for r in range(rows)]

    D_k = make_local_mat(0.12, d_small, b_small)
    U_k = make_local_mat(0.15, b_small, d_small)
    D_v = make_local_mat(-0.10, d_small, b_small)
    U_v = make_local_mat(0.18, b_small, d_small)

    # Global prompt P_tau in R^{l_small x d_small}
    P_tau = [[0.4, -0.2, 0.6, 0.1], [-0.3, 0.7, 0.2, -0.5]]

    # Eqs. 5-6: P^m_{tau,k} = U_k(ReLU(D_k(P_tau))), P^m_{tau,v} = U_v(ReLU(D_v(P_tau)))
    P_tau_k = matmul(relu_mat(matmul(P_tau, D_k)), U_k)
    P_tau_v = matmul(relu_mat(matmul(P_tau, D_v)), U_v)
    assert len(P_tau_k) == l_small and len(P_tau_k[0]) == d_small
    assert len(P_tau_v) == l_small and len(P_tau_v[0]) == d_small

    # 3. Prepending hyper-prompts to K and V in self-attention (Eqs. 1-2) & Entropy renormalization (Sec. 4.6):
    Q_tau = [[0.2 * (i + 1) - 0.1 * j for j in range(d_small)] for i in range(L_seq)]
    K_tau = [[0.15 * (i + 1) + 0.05 * j for j in range(d_small)] for i in range(L_seq)]
    V_tau = [[-0.1 * (i + 1) + 0.2 * j for j in range(d_small)] for i in range(L_seq)]

    K_prime = [*P_tau_k, *K_tau]  # shape (l_small + L_seq) x d_small
    V_prime = [*P_tau_v, *V_tau]  # shape (l_small + L_seq) x d_small
    assert len(K_prime) == l_small + L_seq and len(V_prime) == l_small + L_seq

    scale = math.sqrt(d_small)
    O_tau = []
    for q_row in Q_tau:
        scores = [sum(q_row[c] * k_row[c] for c in range(d_small)) / scale for k_row in K_prime]
        m_sc = max(scores)
        exps = [math.exp(s - m_sc) for s in scores]
        Z = sum(exps)
        attn = [e / Z for e in exps]

        prompt_mass = sum(attn[:l_small])
        token_mass = sum(attn[l_small:])
        assert abs((prompt_mass + token_mass) - 1.0) < 1e-12
        assert 0.0 < prompt_mass < 1.0

        # Renormalized token attention distribution (Appendix A.3)
        renorm_tok_attn = [a / token_mass for a in attn[l_small:]]
        assert abs(sum(renorm_tok_attn) - 1.0) < 1e-12
        entropy = -sum(p * math.log(p) for p in renorm_tok_attn)
        assert entropy > 0.0

        out_row = [sum(attn[idx] * V_prime[idx][c] for idx in range(l_small + L_seq)) for c in range(d_small)]
        O_tau.append(out_row)

    # Output sequence length remains L_seq (prompts do not pass through FFN layers!)
    assert len(O_tau) == L_seq and len(O_tau[0]) == d_small

    print(
        f"[PASS] HyperPrompt boundaries verified: params_global={params_global} < params_sep={params_sep}, "
        f"rel_increase_2xT={rel_increase:.4f}, out_shape=({len(O_tau)}, {len(O_tau[0])})"
    )


if __name__ == "__main__":
    verify_hyperprompt_boundaries()
