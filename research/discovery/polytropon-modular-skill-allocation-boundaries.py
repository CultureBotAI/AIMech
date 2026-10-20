#!/usr/bin/env python3
"""Constructed boundary verification for Polytropon / Skilled Modular Multitask Learning (Ponti et al., ICLR 2023, arXiv:2202.13914)."""

import math


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def gumbel_sigmoid(z_logit: float, u: float, tau: float) -> float:
    p = sigmoid(z_logit)
    logit_relaxed = math.log((p * u) / ((1.0 - p) * (1.0 - u))) / tau
    return sigmoid(logit_relaxed)


def binary_entropy(p: float) -> float:
    if p <= 1e-12 or p >= 1.0 - 1e-12:
        return 0.0
    return -(p * math.log(p) + (1.0 - p) * math.log(1.0 - p))


def verify_polytropon_boundaries() -> None:
    # 1. Gumbel-sigmoid relaxation (Section 2.1, Eq. 2) & Row-normalized superposition (Section 2.2, Eq. 3):
    T_tasks = 4
    S_skills = 3
    d_param = 4

    theta_0 = [1.0, -0.5, 0.25, 0.75]
    Phi = [
        [0.4, 0.2, -0.1, 0.3],
        [-0.2, 0.5, 0.4, -0.3],
        [0.1, -0.3, 0.6, 0.2],
    ]
    Z_logits = [
        [4.0, -4.0, 3.5],
        [-3.5, 4.2, -4.0],
        [3.8, 3.9, -4.2],
        [-4.1, 3.7, 4.1],
    ]
    u_fixed = 0.6
    tau = 0.5

    Z_hat = [[gumbel_sigmoid(Z_logits[i][j], u_fixed, tau) for j in range(S_skills)] for i in range(T_tasks)]
    for i in range(T_tasks):
        row_sum = sum(Z_hat[i])
        assert row_sum > 0.0
        norm_weights = [Z_hat[i][j] / row_sum for j in range(S_skills)]
        assert abs(sum(norm_weights) - 1.0) < 1e-12
        theta_i = [
            theta_0[c] + sum(Phi[j][c] * norm_weights[j] for j in range(S_skills))
            for c in range(d_param)
        ]
        # Verify convex hull norm bound: ||theta_i - theta_0||_2 <= max_j ||Phi_j||_2
        diff_norm = math.sqrt(sum((theta_i[c] - theta_0[c]) ** 2 for c in range(d_param)))
        max_phi_norm = max(math.sqrt(sum(Phi[j][c] ** 2 for c in range(d_param))) for j in range(S_skills))
        assert diff_norm <= max_phi_norm + 1e-12

    # 2. Special cases (Section 2.5): PRIVATE (Z = I) and SHARED (Z = 1_{T x 1})
    Z_private = [[1.0 if i == j else 0.0 for j in range(S_skills)] for i in range(S_skills)]
    for i in range(S_skills):
        theta_priv = [
            theta_0[c] + sum(Phi[j][c] * Z_private[i][j] for j in range(S_skills))
            for c in range(d_param)
        ]
        assert all(abs(theta_priv[c] - (theta_0[c] + Phi[i][c])) < 1e-15 for c in range(d_param))

    # 3. LoRA Skill Inventory parameter count (Section 4.2, Eq. 6):
    # 4 * l * (2 * h * r + |T|) * |S|
    l_bart = 24
    h_bart = 1024
    r_lora = 16
    T_crossfit = 120
    S_inv = 4
    params_per_skill = 4 * l_bart * (2 * h_bart * r_lora + T_crossfit)
    total_skilled_params = params_per_skill * S_inv
    assert params_per_skill == 3157248  # ~3.16M per skill (~0.78% of 400M BART-Large)
    assert total_skilled_params == 12628992

    # 4. Discreteness (Eq. 8), Sparsity (Eq. 9), and Usage (Eq. 10) metrics (Section 4.3):
    Z_probs = [[sigmoid(Z_logits[i][j]) for j in range(S_skills)] for i in range(T_tasks)]
    discreteness = (
        sum(binary_entropy(Z_probs[i][j]) / math.log(2.0) for i in range(T_tasks) for j in range(S_skills))
        / (T_tasks * S_skills)
    )
    sparsity = (
        sum(1 if round(Z_probs[i][j]) == 1 else 0 for i in range(T_tasks) for j in range(S_skills))
        / (T_tasks * S_skills)
    )
    col_sums = [sum(Z_probs[i][j] for i in range(T_tasks)) for j in range(S_skills)]
    total_col = sum(col_sums)
    col_dist = [c / total_col for c in col_sums]
    usage = -sum(p * math.log(p) for p in col_dist if p > 0.0) / math.log(S_skills)

    assert 0.0 < discreteness < 0.20  # near-binary logits have low normalized entropy
    assert abs(sparsity - (7.0 / 12.0)) < 1e-12
    assert 0.95 < usage <= 1.0  # balanced skill usage across tasks

    print(
        f"[PASS] Polytropon boundaries verified: params_per_skill={params_per_skill}, "
        f"discreteness={discreteness:.4f}, sparsity={sparsity:.4f}, usage={usage:.4f}"
    )


if __name__ == "__main__":
    verify_polytropon_boundaries()
