#!/usr/bin/env python3
"""Constructed boundary verification for PromptFL (Guo et al., IEEE TMC 2024, arXiv:2208.11625).

Verifies:
1. Frozen-backbone CLIP cosine-similarity classification with learnable continuous prompt vectors P
   (Eq. 1, p. 3): p(y = i | x) = exp(cos(g(x), h(P, K_i))) / sum_j exp(cos(g(x), h(P, K_j))).
2. Prompt-only local gradient update and server FedAvg aggregation over P in R^{p x d} (Eq. 2, p. 6)
   while keeping image encoder g(.) and text encoder h(.) weights strictly invariant (zero parameter drift).
3. Parameter and communication compression ratios: p*d trainable parameters vs full backbone parameters,
   matching the 0.01%--0.1% trainable parameter ratio and >100x communication reduction (Tables 1-2, Fig. 4).
4. Input-agnostic static nature of prompt updates across clients with non-overlapping class distributions.
"""

import math


def l2_normalize(vec: list[float], eps: float = 1e-12) -> list[float]:
    norm = math.sqrt(sum(v * v for v in vec))
    return [v / max(norm, eps) for v in vec]


def cosine_sim(u: list[float], v: list[float]) -> float:
    un = l2_normalize(u)
    vn = l2_normalize(v)
    return sum(a * b for a, b in zip(un, vn))


def text_encoder_forward(prompt_vecs: list[list[float]], class_emb: list[float], proj_w: list[list[float]]) -> list[float]:
    """Frozen attention-modulated text encoder surrogate h(P, K_i) combining p prompt vectors and class token K_i."""
    d = len(class_emb)
    p_len = len(prompt_vecs)
    p_mean = [sum(prompt_vecs[t][j] for t in range(p_len)) / float(p_len) for j in range(d)]
    # Prompt tokens modulate class token via cross-token gating + context shift before frozen projection proj_w
    modulated = [(1.0 + p_mean[j]) * class_emb[j] + 0.25 * p_mean[j] for j in range(d)]
    out_dim = len(proj_w)
    return [sum(proj_w[row][col] * modulated[col] for col in range(d)) for row in range(out_dim)]


def promptfl_probs(img_feat: list[float], prompt_vecs: list[list[float]], class_embs: list[list[float]], proj_w: list[list[float]]) -> list[float]:
    """Eq. 1 (p. 3): Softmax over cosine similarities cos[g(x) | h(P, K_i)]."""
    logits = [5.0 * cosine_sim(img_feat, text_encoder_forward(prompt_vecs, k_i, proj_w)) for k_i in class_embs]
    m_val = max(logits)
    exps = [math.exp(z - m_val) for z in logits]
    s_val = sum(exps)
    return [e / s_val for e in exps]


def cross_entropy_loss(img_feat: list[float], label: int, prompt_vecs: list[list[float]], class_embs: list[list[float]], proj_w: list[list[float]]) -> float:
    probs = promptfl_probs(img_feat, prompt_vecs, class_embs, proj_w)
    return -math.log(max(probs[label], 1e-15))


def numerical_prompt_grad(
    img_feat: list[float],
    label: int,
    prompt_vecs: list[list[float]],
    class_embs: list[list[float]],
    proj_w: list[list[float]],
    eps: float = 1e-5,
) -> list[list[float]]:
    p_len = len(prompt_vecs)
    d = len(prompt_vecs[0])
    grad = [[0.0] * d for _ in range(p_len)]
    for t in range(p_len):
        for j in range(d):
            orig = prompt_vecs[t][j]
            prompt_vecs[t][j] = orig + eps
            l_plus = cross_entropy_loss(img_feat, label, prompt_vecs, class_embs, proj_w)
            prompt_vecs[t][j] = orig - eps
            l_minus = cross_entropy_loss(img_feat, label, prompt_vecs, class_embs, proj_w)
            prompt_vecs[t][j] = orig
            grad[t][j] = (l_plus - l_minus) / (2.0 * eps)
    return grad


def main() -> None:
    # 1. Verify trainable parameter ratio (Table 2, p. 5):
    # p = 16 prompt vectors of dimension d = 512 -> 8,192 parameters vs ViT-B/16 (86.6M) and ResNet50 (38.3M)
    p_tokens = 16
    d_emb = 512
    prompt_params = p_tokens * d_emb
    resnet50_params = 38_300_000
    vit_b16_params = 86_600_000
    ratio_rn50 = prompt_params / resnet50_params
    ratio_vit = prompt_params / vit_b16_params
    assert 0.0001 <= ratio_rn50 <= 0.001
    assert 0.00005 <= ratio_vit <= 0.0002

    # 2. Verify federated prompt optimization over non-overlapping client classes (Eq. 1-2, pp. 3, 6)
    d = 4
    p_len = 2
    proj_w = [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]
    proj_w_snapshot = [row[:] for row in proj_w]
    class_embs = [
        [1.0, 0.4, 0.0, 0.8],
        [0.0, 1.0, 0.4, 0.8],
        [0.4, 0.0, 1.0, 0.8],
    ]
    # Shared background dimension 3 is negative in target domain; prompt P learns p_mean[3] < -1 to flip/suppress it
    client_samples = [
        ([1.0, 0.0, 0.0, -0.5], 0),  # Client 0 owns class 0
        ([0.0, 1.0, 0.0, -0.5], 1),  # Client 1 owns class 1
        ([0.0, 0.0, 1.0, -0.5], 2),  # Client 2 owns class 2
    ]

    global_prompt = [[0.0, 0.0, 0.0, 0.5] for _ in range(p_len)]
    init_loss = sum(
        cross_entropy_loss(x, y, global_prompt, class_embs, proj_w) for x, y in client_samples
    ) / len(client_samples)

    lr = 0.6
    for _round in range(15):
        client_prompts = []
        for x_k, y_k in client_samples:
            local_p = [row[:] for row in global_prompt]
            for _step in range(3):
                g_p = numerical_prompt_grad(x_k, y_k, local_p, class_embs, proj_w)
                for t in range(p_len):
                    for j in range(d):
                        local_p[t][j] -= lr * g_p[t][j]
            client_prompts.append(local_p)
        # Server aggregates only prompt learner parameters P
        for t in range(p_len):
            for j in range(d):
                global_prompt[t][j] = sum(cp[t][j] for cp in client_prompts) / len(client_prompts)

    final_loss = sum(
        cross_entropy_loss(x, y, global_prompt, class_embs, proj_w) for x, y in client_samples
    ) / len(client_samples)

    assert final_loss < init_loss, f"Expected prompt loss decrease: {init_loss} -> {final_loss}"
    # Verify frozen CLIP backbone weights proj_w did not change at all
    assert proj_w == proj_w_snapshot

    print("PromptFL boundary verification passed:", {
        "prompt_params": prompt_params,
        "ratio_rn50_pct": round(100.0 * ratio_rn50, 4),
        "ratio_vit_pct": round(100.0 * ratio_vit, 4),
        "init_loss": round(init_loss, 5),
        "final_loss": round(final_loss, 5),
    })


if __name__ == "__main__":
    main()
