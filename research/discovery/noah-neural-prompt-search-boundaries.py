#!/usr/bin/env python3
"""Constructed boundary and algebraic verification for Round 700:
Neural Prompt Search (NOAH) (Zhang, Zhou, & Liu, 2022, arXiv:2206.04673).
"""

import math
import random


def relu(x):
    return x if x > 0.0 else 0.0


def matmul(A, B):
    """Multiply (R x K) by (K x C) -> (R x C)."""
    R = len(A)
    K = len(A[0])
    C = len(B[0])
    assert len(B) == K
    return [
        [sum(A[r][k] * B[k][c] for k in range(K)) for c in range(C)]
        for r in range(R)
    ]


def vpt_prepend(cls_token, prompt_supernet, patch_tokens, m_tokens):
    """Section 2.1 Eq. 4 & Section 2.2: VPT-Deep prepends m_tokens sliced via weight entanglement
    from prompt_supernet: x = [CLS, P[:m_tokens], E].
    """
    assert 0 <= m_tokens <= len(prompt_supernet)
    P_sliced = [list(tok) for tok in prompt_supernet[:m_tokens]]
    return [list(cls_token)] + P_sliced + [list(tok) for tok in patch_tokens]


def lora_q_k(x, W_q, W_k, W_q_down, W_q_up, W_k_down, W_k_up, r_lora, scale_s=1.0):
    """Section 2.1 Eq. 3 & Section 2.2: LoRA updates Q and K with rank-r_lora entangled slices:
    Q = x W_q + s * x W_q_down[:, :r] W_q_up[:r, :]
    K = x W_k + s * x W_k_down[:, :r] W_k_up[:r, :].
    """
    Q_base = matmul(x, W_q)
    K_base = matmul(x, W_k)
    if r_lora == 0:
        return Q_base, K_base
    Wq_d = [row[:r_lora] for row in W_q_down]
    Wq_u = W_q_up[:r_lora]
    Wk_d = [row[:r_lora] for row in W_k_down]
    Wk_u = W_k_up[:r_lora]
    dQ = matmul(matmul(x, Wq_d), Wq_u)
    dK = matmul(matmul(x, Wk_d), Wk_u)
    N = len(x)
    d = len(Q_base[0])
    Q = [[Q_base[i][j] + scale_s * dQ[i][j] for j in range(d)] for i in range(N)]
    K = [[K_base[i][j] + scale_s * dK[i][j] for j in range(d)] for i in range(N)]
    return Q, K


def adapter_forward(h, W_down, W_up, r_adapter):
    """Section 2.1 Eq. 2 & Section 2.2: Adapter bottleneck h' = phi(h W_down[:, :r]) W_up[:r, :]
    with residual connection h + h'.
    """
    if r_adapter == 0:
        return [list(row) for row in h]
    Wd = [row[:r_adapter] for row in W_down]
    Wu = W_up[:r_adapter]
    down_proj = matmul(h, Wd)
    act = [[relu(val) for val in row] for row in down_proj]
    h_prime = matmul(act, Wu)
    N = len(h)
    d = len(h[0])
    return [[h[i][j] + h_prime[i][j] for j in range(d)] for i in range(N)]


def apply_depth_mask(dims_per_layer, active_depth):
    """Section 2.2: A depth in {0, 3, 6, 9, 12} means layers 0..active_depth-1 have the module
    installed while layers active_depth..L-1 are set to 0.
    """
    return [dims_per_layer[l] if l < active_depth else 0 for l in range(len(dims_per_layer))]


def count_subnet_params(subnet_arch, D=768, d=768):
    """Count total trainable parameters in a 12-layer NOAH subnet architecture:
    subnet_arch = {'vpt': [m_0..m_11], 'adapter': [r_0..r_11], 'lora': [r_0..r_11]}.
    - VPT layer l: m_l * D
    - Adapter layer l: 2 * d * r_l (W_down in R^{d x r_l}, W_up in R^{r_l x d})
    - LoRA layer l: 2 * (D * r_l + r_l * d) (for Q and K projections)
    """
    vpt_params = sum(m_l * D for m_l in subnet_arch["vpt"])
    adapter_params = sum(2 * d * r_l for r_l in subnet_arch["adapter"])
    lora_params = sum(2 * (D * r_l + r_l * d) for r_l in subnet_arch["lora"])
    return vpt_params + adapter_params + lora_params


def crossover_subnets(parent_a, parent_b, rng):
    """Section 2.2 Fig. 2 (Crossover): Randomly select each prompt module trajectory from parent A or B."""
    return {
        mod: list(parent_a[mod] if rng.random() < 0.5 else parent_b[mod])
        for mod in ("vpt", "adapter", "lora")
    }


def mutate_subnet(arch, search_dims, search_depths, mut_prob, rng):
    """Section 2.2 Fig. 2 (Mutation): Mutate active depth in {0, 3, 6, 9, 12} and layer dimensions."""
    L = len(arch["vpt"])
    mutated = {}
    for mod in ("vpt", "adapter", "lora"):
        seq = list(arch[mod])
        if rng.random() < mut_prob:
            new_depth = rng.choice(search_depths)
            for l in range(L):
                if l >= new_depth:
                    seq[l] = 0
                elif seq[l] == 0 or rng.random() < mut_prob:
                    seq[l] = rng.choice(search_dims)
        mutated[mod] = seq
    return mutated


def main():
    rng = random.Random(2022)
    D, d, N_patches = 8, 8, 5
    max_dim = 10

    # 1. Verify VPT-Deep sequence length and weight entanglement prefix sharing:
    cls_tok = [0.5] * D
    patches = [[rng.gauss(0.0, 1.0) for _ in range(D)] for _ in range(N_patches)]
    vpt_supernet = [[rng.gauss(0.0, 1.0) for _ in range(D)] for _ in range(max_dim)]

    x_m3 = vpt_prepend(cls_tok, vpt_supernet, patches, m_tokens=3)
    x_m6 = vpt_prepend(cls_tok, vpt_supernet, patches, m_tokens=6)
    assert len(x_m3) == 1 + 3 + N_patches
    assert len(x_m6) == 1 + 6 + N_patches
    # First 3 prompt tokens (indices 1, 2, 3) are identically shared between m=3 and m=6 subnets:
    assert x_m3[1:4] == x_m6[1:4]

    # 2. Verify LoRA Q/K update and Adapter bottleneck forward pass:
    W_q = [[rng.gauss(0.0, 0.2) for _ in range(d)] for _ in range(D)]
    W_k = [[rng.gauss(0.0, 0.2) for _ in range(d)] for _ in range(D)]
    W_q_down = [[rng.gauss(0.0, 0.1) for _ in range(max_dim)] for _ in range(D)]
    W_q_up = [[rng.gauss(0.0, 0.1) for _ in range(d)] for _ in range(max_dim)]
    W_k_down = [[rng.gauss(0.0, 0.1) for _ in range(max_dim)] for _ in range(D)]
    W_k_up = [[rng.gauss(0.0, 0.1) for _ in range(d)] for _ in range(max_dim)]

    Q_r0, K_r0 = lora_q_k(x_m3, W_q, W_k, W_q_down, W_q_up, W_k_down, W_k_up, r_lora=0)
    Q_r5, K_r5 = lora_q_k(x_m3, W_q, W_k, W_q_down, W_q_up, W_k_down, W_k_up, r_lora=5)
    assert Q_r0 == matmul(x_m3, W_q) and K_r0 == matmul(x_m3, W_k)
    assert Q_r5 != Q_r0 and K_r5 != K_r0

    W_ad_down = [[rng.gauss(0.0, 0.1) for _ in range(max_dim)] for _ in range(d)]
    W_ad_up = [[rng.gauss(0.0, 0.1) for _ in range(d)] for _ in range(max_dim)]
    h_r0 = adapter_forward(Q_r5, W_ad_down, W_ad_up, r_adapter=0)
    h_r5 = adapter_forward(Q_r5, W_ad_down, W_ad_up, r_adapter=5)
    assert h_r0 == Q_r5 and h_r5 != h_r0

    # 3. Verify Fig. 2 depth mutation example from paper:
    # Input A: VPT depth=6 -> {10, 5, 5, 5, 10, 50, 0,...,0}; new depth=3 sets layers 3..5 to 0:
    vpt_A = [10, 5, 5, 5, 10, 50, 0, 0, 0, 0, 0, 0]
    vpt_A_depth3 = apply_depth_mask(vpt_A, active_depth=3)
    assert vpt_A_depth3 == [10, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # 4. Verify evolutionary search crossover/mutation under 0.64M parameter cap (Section 3, p. 5):
    param_cap = 640_000
    search_dims = [1, 5, 10]
    search_depths = [0, 3, 6, 9, 12]
    parent_1 = {
        "vpt": apply_depth_mask([rng.choice(search_dims) for _ in range(12)], 6),
        "adapter": apply_depth_mask([rng.choice(search_dims) for _ in range(12)], 6),
        "lora": apply_depth_mask([rng.choice(search_dims) for _ in range(12)], 6),
    }
    parent_2 = {
        "vpt": apply_depth_mask([rng.choice(search_dims) for _ in range(12)], 9),
        "adapter": apply_depth_mask([rng.choice(search_dims) for _ in range(12)], 3),
        "lora": apply_depth_mask([rng.choice(search_dims) for _ in range(12)], 9),
    }
    valid_children = []
    for _ in range(50):
        child = crossover_subnets(parent_1, parent_2, rng)
        child = mutate_subnet(child, search_dims, search_depths, mut_prob=0.2, rng=rng)
        p_count = count_subnet_params(child, D=768, d=768)
        if p_count <= param_cap:
            valid_children.append((p_count, child))
    assert len(valid_children) > 0
    best_params = valid_children[0][0]
    assert 0 < best_params <= param_cap

    print(
        f"[PASS] NOAH boundary verification passed: "
        f"len(x_m3)={len(x_m3)}, len(x_m6)={len(x_m6)}, "
        f"vpt_depth3={vpt_A_depth3[:6]}, "
        f"valid_subnets={len(valid_children)}/50 (sample_params={best_params:,} <= {param_cap:,})"
    )


if __name__ == "__main__":
    main()
