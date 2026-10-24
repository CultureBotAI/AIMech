#!/usr/bin/env python3
"""Constructed boundary verification for Lottery Ticket Sparse Fine-Tuning (LT-SFT, Ansell et al., ACL 2022)."""

from __future__ import annotations

import math
import random


def ltsft_two_phase(
    theta0: list[float],
    grad_phase1: list[float],
    grad_phase2: list[float],
    k: int,
    lr: float = 0.1,
) -> tuple[list[int], list[float], list[float]]:
    """Run two-phase LT-SFT (Algorithm 1) and return (mask, theta2, phi)."""
    d = len(theta0)
    assert 0 < k <= d
    # Phase 1: full fine-tuning from theta0
    theta1 = [theta0[i] - lr * grad_phase1[i] for i in range(d)]
    # Rank parameters by absolute magnitude change |theta1_i - theta0_i|
    ranked = sorted(range(d), key=lambda i: abs(theta1[i] - theta0[i]), reverse=True)
    top_k = set(ranked[:k])
    mask = [1 if i in top_k else 0 for i in range(d)]

    # Phase 2: rewind to original theta0 (NOT zeroed) and apply masked gradient
    theta2 = list(theta0)
    for i in range(d):
        theta2[i] = theta2[i] - mask[i] * lr * grad_phase2[i]

    phi = [theta2[i] - theta0[i] for i in range(d)]
    return mask, theta2, phi


def main() -> int:
    rng = random.Random(20260710)
    d = 200
    k = 20  # 10% sparsity
    theta0 = [rng.gauss(0.0, 1.0) for _ in range(d)]

    # 1. Language SFT (source language s and target language l) and Task SFT (task t)
    g_src1 = [rng.gauss(0.0, 1.0) for _ in range(d)]
    g_src2 = [rng.gauss(0.0, 1.0) for _ in range(d)]
    mask_src, theta_src, phi_src = ltsft_two_phase(theta0, g_src1, g_src2, k)

    # Verify exact support and rewinding preservation
    assert sum(mask_src) == k
    for i in range(d):
        if mask_src[i] == 0:
            assert phi_src[i] == 0.0
            assert theta_src[i] == theta0[i]

    # Task SFT trained on top of theta0 + phi_src, then phi_src is removed (Section 3.2, Alg. 1)
    theta_base_task = [theta0[i] + phi_src[i] for i in range(d)]
    g_task1 = [rng.gauss(0.0, 1.0) for _ in range(d)]
    g_task2 = [rng.gauss(0.0, 1.0) for _ in range(d)]
    mask_task, theta_prime, phi_task = ltsft_two_phase(theta_base_task, g_task1, g_task2, k)

    # Verify phi_task == theta_prime - (theta0 + phi_src)
    for i in range(d):
        assert math.isclose(
            phi_task[i], theta_prime[i] - (theta0[i] + phi_src[i]), abs_tol=1e-15
        )
        if mask_task[i] == 0:
            assert phi_task[i] == 0.0

    # Target language SFT trained on theta0
    g_tar1 = [rng.gauss(0.0, 1.0) for _ in range(d)]
    g_tar2 = [rng.gauss(0.0, 1.0) for _ in range(d)]
    mask_tar, _, phi_tar = ltsft_two_phase(theta0, g_tar1, g_tar2, k)

    # 2. Functional composition commutativity: S_L(S_T(theta0)) == S_T(S_L(theta0)) == theta0 + phi_task + phi_tar
    comp_lt = [(theta0[i] + phi_task[i]) + phi_tar[i] for i in range(d)]
    comp_tl = [(theta0[i] + phi_tar[i]) + phi_task[i] for i in range(d)]
    max_comm_err = max(abs(comp_lt[i] - comp_tl[i]) for i in range(d))
    assert max_comm_err < 1e-15

    # 3. Sparsity prevents parameter overlap / interference compared to dense adaptation
    overlap_sparse = sum(1 for i in range(d) if mask_task[i] == 1 and mask_tar[i] == 1) / d
    _, _, phi_task_dense = ltsft_two_phase(theta_base_task, g_task1, g_task2, d)
    _, _, phi_tar_dense = ltsft_two_phase(theta0, g_tar1, g_tar2, d)
    overlap_dense = sum(
        1 for i in range(d) if abs(phi_task_dense[i]) > 0 and abs(phi_tar_dense[i]) > 0
    ) / d
    assert overlap_sparse < 0.05 < overlap_dense == 1.0

    print(
        f"[PASS] LT-SFT boundaries verified: k={sum(mask_src)}/{d}, "
        f"max_comm_err={max_comm_err:.2e}, overlap_sparse={overlap_sparse:.3f} < overlap_dense={overlap_dense:.3f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
