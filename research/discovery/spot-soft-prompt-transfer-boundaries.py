#!/usr/bin/env python3
"""Constructed boundary and algebraic verification for Round 698:
SPoT: Better Frozen Model Adaptation through Soft Prompt Transfer (Vu et al., ACL 2022, arXiv:2110.07904).
"""

import math


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def norm(u):
    return math.sqrt(dot(u, u))


def cosine(u, v):
    nu = norm(u)
    nv = norm(v)
    assert nu > 0.0 and nv > 0.0
    return dot(u, v) / (nu * nv)


def avg_token_cosine_sim(e1, e2):
    """Section 3.2: Cosine Similarity of Average Tokens:
    sim(t^1, t^2) = cos( (1/L) sum_i e^1_i, (1/L) sum_j e^2_j ).
    """
    L1 = len(e1)
    L2 = len(e2)
    assert L1 == L2 and L1 > 0
    dim = len(e1[0])
    mean1 = [sum(e1[i][d] for i in range(L1)) / L1 for d in range(dim)]
    mean2 = [sum(e2[j][d] for j in range(L2)) / L2 for d in range(dim)]
    return cosine(mean1, mean2)


def per_token_avg_cosine_sim(e1, e2):
    """Section 3.2: Per-token Average Cosine Similarity:
    sim(t^1, t^2) = (1/L^2) sum_i sum_j cos(e^1_i, e^2_j).
    """
    L1 = len(e1)
    L2 = len(e2)
    assert L1 == L2 and L1 > 0
    total = 0.0
    for i in range(L1):
        for j in range(L2):
            total += cosine(e1[i], e2[j])
    return total / (L1 * L2)


def top_k_weighted_average(source_prompts, source_embs, target_emb, k, sim_fn):
    """Section 3.3: Top-k Weighted Average prompt initialization:
    alpha_r = sim(e^{s_r}, e^t) / sum_{l=1}^k sim(e^{s_l}, e^t).
    """
    scored = []
    for idx, (rho_s, e_s) in enumerate(zip(source_prompts, source_embs)):
        s = sim_fn(e_s, target_emb)
        scored.append((s, idx, rho_s, e_s))
    scored.sort(key=lambda item: item[0], reverse=True)
    top_k = scored[:k]
    denom = sum(item[0] for item in top_k)
    assert denom > 0.0
    alphas = [item[0] / denom for item in top_k]
    L = len(target_emb)
    E = len(target_emb[0])
    init_prompt = [[0.0 for _ in range(E)] for _ in range(L)]
    for alpha_r, (_, _, rho_sr, _) in zip(alphas, top_k):
        for i in range(L):
            for d in range(E):
                init_prompt[i][d] += alpha_r * rho_sr[i][d]
    return init_prompt, alphas, [item[1] for item in top_k]


def main():
    # 1. Parameter efficiency check (Section 2.1.4 & Appendix D Table 5):
    # Prompt rho in R^{L x E} with L = 100 tokens. For T5 XXL (11B params, E = 4096):
    L_prompt = 100
    E_xxl = 4096
    prompt_params = L_prompt * E_xxl  # 409,600 (~410K)
    total_xxl_params = 11_000_000_000
    reduction_ratio = total_xxl_params / prompt_params
    assert prompt_params == 409600
    assert 26800.0 <= reduction_ratio <= 27000.0

    # 2. Task embedding similarity metrics (Section 3.2):
    # Construct 4 synthetic task embeddings with L = 4 tokens, E = 3:
    # Target task t (e.g., CB - NLI), Source 0 (MNLI - NLI, high similarity),
    # Source 1 (QNLI - NLI, medium-high similarity), Source 2 (uncorrelated task).
    e_target = [
        [0.90, 0.20, 0.10],
        [0.85, 0.25, 0.15],
        [0.88, 0.18, 0.12],
        [0.92, 0.22, 0.08],
    ]
    e_src0 = [
        [0.89, 0.21, 0.11],
        [0.86, 0.24, 0.14],
        [0.87, 0.19, 0.13],
        [0.91, 0.23, 0.09],
    ]
    e_src1 = [
        [0.75, 0.45, 0.20],
        [0.70, 0.50, 0.25],
        [0.72, 0.48, 0.22],
        [0.78, 0.42, 0.18],
    ]
    e_src2 = [
        [0.10, 0.20, 0.95],
        [0.15, 0.25, 0.90],
        [0.12, 0.18, 0.92],
        [0.08, 0.22, 0.96],
    ]

    sim_avg_self = avg_token_cosine_sim(e_target, e_target)
    assert abs(sim_avg_self - 1.0) < 1e-12

    s_avg_0 = avg_token_cosine_sim(e_src0, e_target)
    s_avg_1 = avg_token_cosine_sim(e_src1, e_target)
    s_avg_2 = avg_token_cosine_sim(e_src2, e_target)
    assert s_avg_0 > s_avg_1 > s_avg_2 > 0.0

    s_tok_0 = per_token_avg_cosine_sim(e_src0, e_target)
    s_tok_1 = per_token_avg_cosine_sim(e_src1, e_target)
    s_tok_2 = per_token_avg_cosine_sim(e_src2, e_target)
    assert s_tok_0 > s_tok_1 > s_tok_2 > 0.0
    # Symmetry check
    assert abs(per_token_avg_cosine_sim(e_src0, e_target) - per_token_avg_cosine_sim(e_target, e_src0)) < 1e-12

    # 3. Top-k Weighted Average prompt initialization & transfer gain (Section 3.3):
    # Optimal target prompt rho_star is close to Source 0 and Source 1 best prompts.
    rho_star = [
        [1.00, 0.20, 0.10],
        [0.95, 0.25, 0.15],
        [0.98, 0.18, 0.12],
        [1.02, 0.22, 0.08],
    ]
    rho_src0 = [
        [0.98, 0.21, 0.11],
        [0.94, 0.24, 0.14],
        [0.96, 0.19, 0.13],
        [1.00, 0.23, 0.09],
    ]
    rho_src1 = [
        [0.82, 0.40, 0.18],
        [0.78, 0.44, 0.22],
        [0.80, 0.42, 0.20],
        [0.85, 0.38, 0.16],
    ]
    rho_src2 = [
        [0.05, 0.15, 0.90],
        [0.10, 0.20, 0.85],
        [0.08, 0.12, 0.88],
        [0.04, 0.18, 0.92],
    ]
    source_prompts = [rho_src2, rho_src0, rho_src1]
    source_embs = [e_src2, e_src0, e_src1]

    init_prompt, alphas, ranked_indices = top_k_weighted_average(
        source_prompts, source_embs, e_target, k=2, sim_fn=per_token_avg_cosine_sim
    )
    assert abs(sum(alphas) - 1.0) < 1e-12
    assert alphas[0] > alphas[1] > 0.0
    assert ranked_indices == [1, 2]  # src0 then src1

    def prompt_mse(rho_a, rho_b):
        return sum(
            (rho_a[i][d] - rho_b[i][d]) ** 2
            for i in range(len(rho_a))
            for d in range(len(rho_a[0]))
        ) / (len(rho_a) * len(rho_a[0]))

    # Compare target error after S gradient steps from scratch (zero init) vs SPoT init
    rho_scratch = [[0.0 for _ in range(3)] for _ in range(4)]
    err_scratch_init = prompt_mse(rho_scratch, rho_star)
    err_spot_init = prompt_mse(init_prompt, rho_star)
    err_best_top1 = prompt_mse(rho_src0, rho_star)
    assert err_best_top1 < err_spot_init < err_scratch_init

    print(
        f"[PASS] SPoT boundary verification passed: "
        f"reduction_ratio={reduction_ratio:.1f}x, "
        f"s_tok=({s_tok_0:.4f}>{s_tok_1:.4f}>{s_tok_2:.4f}), "
        f"alphas={[round(a, 4) for a in alphas]}, "
        f"mse_top1={err_best_top1:.5f} < mse_spot_wavg={err_spot_init:.5f} << mse_scratch={err_scratch_init:.5f}"
    )


if __name__ == "__main__":
    main()
