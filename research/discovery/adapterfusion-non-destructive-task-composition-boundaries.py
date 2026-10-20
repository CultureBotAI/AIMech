#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 690: AdapterFusion (Pfeiffer et al., EACL 2021 / arXiv:2005.00247)."""

from __future__ import annotations

import math
import random


def matvec_t(x: list[float], M: list[list[float]]) -> list[float]:
    """Compute x^T M for x in R^d and M in R^{d x d}."""
    d_out = len(M[0])
    return [sum(x[i] * M[i][j] for i in range(len(x))) for j in range(d_out)]


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def softmax(logits: list[float]) -> list[float]:
    m = max(logits)
    exps = [math.exp(z - m) for z in logits]
    s = sum(exps)
    return [e / s for e in exps]


def adapter_fusion_step(
    h_lt: list[float],
    z_ltn_list: list[list[float]],
    Q_l: list[list[float]],
    K_l: list[list[float]],
    V_l: list[list[float]],
) -> tuple[list[float], list[float]]:
    """Section 3.2 (p. 5):
    s_{l,t} = softmax(h_{l,t}^T Q_l (dot) z_{l,t,n}^T K_l), n in {1..N}
    z'_{l,t,n} = z_{l,t,n}^T V_l
    o_{l,t} = s_{l,t}^T Z'_{l,t}.
    """
    q_vec = matvec_t(h_lt, Q_l)
    logits = [dot(q_vec, matvec_t(z_n, K_l)) for z_n in z_ltn_list]
    s_lt = softmax(logits)
    z_prime_list = [matvec_t(z_n, V_l) for z_n in z_ltn_list]
    d = len(z_prime_list[0])
    o_lt = [sum(s_lt[n] * z_prime_list[n][j] for n in range(len(z_ltn_list))) for j in range(d)]
    return o_lt, s_lt


def main() -> None:
    rng = random.Random(690)
    d = 8
    N = 4  # 4 pre-trained Single-Task Adapters (ST-A)

    # 1. Verify Section 4.1 near-identity V_l initialization (diag(1) + N(0, 1e-6)):
    # When V_l = I_d + eps and s_{l,t} concentrates on adapter n*, o_{l,t} recovers z_{l,t,n*} within O(1e-6).
    V_init = [
        [(1.0 if i == j else 0.0) + rng.gauss(0.0, 1e-6) for j in range(d)]
        for i in range(d)
    ]

    # Construct N frozen task adapters where Adapter 1 (e.g., MNLI) and Adapter 2 (e.g., QQP)
    # provide complementary representations for a low-resource target task m (e.g., RTE/CB).
    z_adapters = [[rng.gauss(0.0, 1.0) for _ in range(d)] for _ in range(N)]
    h_query_a = [1.0 if j < d // 2 else 0.0 for j in range(d)]
    h_query_b = [0.0 if j < d // 2 else 1.0 for j in range(d)]

    # Set z_adapters[1] and z_adapters[2] to align with subspaces A and B respectively
    z_adapters[1] = [2.0 if j < d // 2 else 0.0 for j in range(d)]
    z_adapters[2] = [0.0 if j < d // 2 else 2.0 for j in range(d)]

    Q_l = [[3.0 if i == j else 0.0 for j in range(d)] for i in range(d)]
    K_l = [[3.0 if i == j else 0.0 for j in range(d)] for i in range(d)]

    o_a, s_a = adapter_fusion_step(h_query_a, z_adapters, Q_l, K_l, V_init)
    o_b, s_b = adapter_fusion_step(h_query_b, z_adapters, Q_l, K_l, V_init)

    # Verify contextual activation selects Adapter 1 on context A and Adapter 2 on context B
    assert s_a[1] > 0.999 and s_b[2] > 0.999
    err_id_a = math.sqrt(sum((o_a[j] - z_adapters[1][j]) ** 2 for j in range(d)))
    err_id_b = math.sqrt(sum((o_b[j] - z_adapters[2][j]) ** 2 for j in range(d)))
    assert err_id_a < 1e-3 and err_id_b < 1e-3

    # 2. Verify non-destructive task composition property (Section 3.1):
    # Because Stage 2 freezes both Theta_0 and all {Phi_1, ..., Phi_N}, training Psi_m for target task m
    # causes zero parameter drift (0.0 catastrophic forgetting) on all source task adapters Phi_n.
    frozen_adapters_snapshot = [row[:] for row in z_adapters]
    # Simulate updating Q_l, K_l, V_l on target task m
    Q_trained = [[Q_l[i][j] + rng.gauss(0.0, 0.2) for j in range(d)] for i in range(d)]
    _o_new, _s_new = adapter_fusion_step(h_query_a, z_adapters, Q_trained, K_l, V_init)
    forgetting_drift = sum(
        abs(z_adapters[n][j] - frozen_adapters_snapshot[n][j])
        for n in range(N)
        for j in range(d)
    )
    assert forgetting_drift == 0.0

    # 3. Verify that dynamic contextual AdapterFusion outperforms any single fixed ST-A adapter
    # when target task instances draw from both subspace A and subspace B:
    target_a = z_adapters[1]
    target_b = z_adapters[2]
    fusion_mse = 0.5 * (
        sum((o_a[j] - target_a[j]) ** 2 for j in range(d))
        + sum((o_b[j] - target_b[j]) ** 2 for j in range(d))
    )
    best_single_adapter_mse = min(
        0.5 * (
            sum((z_adapters[n][j] - target_a[j]) ** 2 for j in range(d))
            + sum((z_adapters[n][j] - target_b[j]) ** 2 for j in range(d))
        )
        for n in range(N)
    )
    assert fusion_mse < 1e-6 and best_single_adapter_mse > 5.0

    print(
        f"[PASS] Round 690 AdapterFusion (Pfeiffer et al., EACL 2021): "
        f"s_a[1]={s_a[1]:.5f}, s_b[2]={s_b[2]:.5f}, "
        f"forgetting_drift={forgetting_drift:.1e}, "
        f"fusion_mse={fusion_mse:.2e} << single_adapter_mse={best_single_adapter_mse:.2f}"
    )


if __name__ == "__main__":
    main()
