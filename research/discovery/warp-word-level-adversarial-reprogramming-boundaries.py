#!/usr/bin/env python3
"""Constructed boundary verification for WARP: Word-level Adversarial ReProgramming (Hambardzumyan et al., ACL 2021, arXiv:2101.00121)."""

import math


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def softmax(logits: list[float]) -> list[float]:
    m = max(logits)
    exps = [math.exp(z - m) for z in logits]
    s = sum(exps)
    return [e / s for e in exps]


def verify_warp_boundaries() -> None:
    # 1. Parameter storage formulas (Section 4.2, Table 2 & Section 6.3, Table 4):
    # Trainable parameters per task: E * (C + K)
    E_roberta = 1024
    # Table 2: WARP_0 (K=0, C<=3) -> <= 3072; WARP_1 (K=1, C<=3) -> <= 4096; WARP_2 (K=2, C<=3) -> <= 5120;
    # WARP_4 (K=4, C<=3) -> <= 7168; WARP_8 (K=8, C<=2) -> 10240 < 11K; WARP_20 (K=20, C<=3) -> 23552 < 25K
    assert E_roberta * (3 + 0) == 3072
    assert E_roberta * (3 + 1) == 4096
    assert E_roberta * (3 + 2) == 5120
    assert E_roberta * (3 + 4) == 7168
    assert E_roberta * (2 + 8) == 10240 < 11000
    assert E_roberta * (3 + 20) == 23552 < 25000

    # ALBERT-xxlarge-v2 few-shot setup (Section 5.1 & 5.4): E = 128, K + C = 8 -> 1024 trainable parameters
    E_albert = 128
    assert E_albert * 8 == 1024

    # Table 4: Serving N tasks with frozen backbone M=355e6, E=1024, C=3, K=8
    M_backbone = 355_000_000
    N_tasks = 100
    C_max = 3
    K_prompts = 8
    storage_warp = M_backbone + N_tasks * E_roberta * (C_max + K_prompts)
    storage_full_ft = M_backbone * N_tasks
    assert storage_warp == 356_126_400
    assert storage_full_ft / storage_warp > 99.6  # >99.6x storage reduction for 100 tasks!

    # 2. Continuous Prompt + Verbalizer Softmax & Gradient Update (Section 3):
    E = 4
    K = 3
    C = 3

    # Frozen input token embeddings x_1, x_2 in R^E
    x_tokens = [[0.5, -0.2, 0.4, 0.1], [-0.3, 0.6, 0.2, -0.4]]
    x_orig_copy = [list(row) for row in x_tokens]

    # Trainable prompt embeddings Theta^P in R^{K x E} and verbalizer embeddings Theta^V in R^{C x E}
    Theta_P = [[0.1 * (k + 1) - 0.05 * d for d in range(E)] for k in range(K)]
    Theta_V = [[0.2 * (c + 1) * ((-1) ** d) for d in range(E)] for c in range(C)]

    # Toy frozen MLM encoder f(T_{Theta^P}(x)) that maps template [P_1, x_1, P_2, [MASK], x_2, P_3] to R^E
    W_enc = [[0.3 * ((r + 1) - 0.2 * (c + 1)) for c in range(E)] for r in range(E)]

    def forward_mlm(prompts: list[list[float]], tokens: list[list[float]]) -> list[float]:
        # Average pool over template tokens followed by frozen linear projection W_enc
        seq = [prompts[0], tokens[0], prompts[1], tokens[1], prompts[2]]
        avg_emb = [sum(s[d] for s in seq) / len(seq) for d in range(E)]
        return [sum(W_enc[r][c] * avg_emb[c] for c in range(E)) for r in range(E)]

    f_out = forward_mlm(Theta_P, x_tokens)
    logits = [dot(Theta_V[c], f_out) for c in range(C)]
    probs = softmax(logits)
    assert abs(sum(probs) - 1.0) < 1e-12

    target_y = 1
    loss_before = -math.log(probs[target_y])

    # Analytical gradient step on Theta^V and Theta^P (while keeping x_tokens strictly untouched!)
    lr = 0.5
    grad_logits = [probs[c] - (1.0 if c == target_y else 0.0) for c in range(C)]
    # dL / d f_out = sum_c grad_logits[c] * Theta_V[c]
    grad_f = [sum(grad_logits[c] * Theta_V[c][d] for c in range(C)) for d in range(E)]
    # dL / d avg_emb = W_enc^T grad_f
    grad_avg = [sum(W_enc[r][c] * grad_f[r] for r in range(E)) for c in range(E)]
    grad_prompt = [g / 5.0 for g in grad_avg]

    for c in range(C):
        for d in range(E):
            Theta_V[c][d] -= lr * grad_logits[c] * f_out[d]
    for k in range(K):
        for d in range(E):
            Theta_P[k][d] -= lr * grad_prompt[d]

    f_out_after = forward_mlm(Theta_P, x_tokens)
    probs_after = softmax([dot(Theta_V[c], f_out_after) for c in range(C)])
    loss_after = -math.log(probs_after[target_y])
    assert loss_after < loss_before
    # Original input token embeddings are completely untouched (Section 3.1):
    assert x_tokens == x_orig_copy

    # 3. Batched multi-task verbalizer concatenation equivalence (Section 6.3, p. 9):
    Theta_V_task2 = [[-0.15 * (c + 1) + 0.1 * d for d in range(E)] for c in range(C)]
    concat_V = [*Theta_V, *Theta_V_task2]  # shape (2*C) x E
    f_batch = [f_out_after, forward_mlm(Theta_P, x_tokens)]
    joint_logits_0 = [dot(concat_V[idx], f_batch[0]) for idx in range(2 * C)]
    assert all(abs(joint_logits_0[c] - dot(Theta_V[c], f_batch[0])) < 1e-15 for c in range(C))

    print(
        f"[PASS] WARP boundaries verified: loss {loss_before:.4f} -> {loss_after:.4f}, "
        f"storage_ratio_100tasks={storage_full_ft / storage_warp:.1f}x, input_untouched=True"
    )


if __name__ == "__main__":
    verify_warp_boundaries()
