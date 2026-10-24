#!/usr/bin/env python3
"""Boundary verification for Round 520: KD3A (Feng et al., ICML 2021)."""

from __future__ import annotations

import math


def argmax(probs: list[float]) -> int:
    return max(range(len(probs)), key=lambda i: probs[i])


def knowledge_vote(
    teacher_preds: list[list[float]], gate: float
) -> tuple[list[float], int]:
    """Compute Knowledge Vote consensus (p_i, n_{p_i}) on one target sample (Section 3.2, page 4)."""
    k_num = len(teacher_preds)
    c_num = len(teacher_preds[0])
    # Step 1: Confidence gate filter
    confident = [q for q in teacher_preds if max(q) >= gate]
    if not confident:
        mean_p = [sum(q[c] for q in teacher_preds) / k_num for c in range(c_num)]
        return mean_p, 0  # represented by low weight 0.001 in loss, 0 support count in Q(S')

    # Step 2: Consensus class vote by summing confident teacher distributions
    summed = [sum(q[c] for q in confident) for c in range(c_num)]
    consensus_cls = argmax(summed)

    # Drop teachers whose individual argmax disagrees with consensus_cls
    supporters = [q for q in confident if argmax(q) == consensus_cls]
    if not supporters:
        supporters = confident

    # Step 3: Mean ensemble over supporting models
    n_p = len(supporters)
    p_i = [sum(q[c] for q in supporters) / n_p for c in range(c_num)]
    return p_i, n_p


def coalition_quality(
    target_preds_by_domain: list[list[list[float]]],
    domain_indices: list[int],
    gate: float,
) -> float:
    """Compute total consensus quality Q(S') (Equation 7, page 4)."""
    n_target = len(target_preds_by_domain[0])
    total_q = 0.0
    for t_idx in range(n_target):
        preds = [target_preds_by_domain[k][t_idx] for k in domain_indices]
        p_i, n_p = knowledge_vote(preds, gate)
        total_q += n_p * max(p_i)
    return total_q


def main() -> None:
    # 1. Verify Knowledge Vote (Section 3.2, Figure 1b, page 3-4)
    # Reproduce the exact 4-teacher 2-class example in Figure 1(b) (page 3):
    # q_S^1 = [0.90, 0.10], q_S^2 = [0.92, 0.08], q_S^3 = [0.02, 0.98], q_S^4 = [0.40, 0.60], gate = 0.9
    fig1b_teachers = [
        [0.90, 0.10],
        [0.92, 0.08],
        [0.02, 0.98],
        [0.40, 0.60],
    ]
    p_vote, n_support = knowledge_vote(fig1b_teachers, gate=0.90)
    # Step 1 drops q_S^4 (max 0.60 < 0.90); Step 2 sums [1.84, 1.16] -> class 0 ('stairs') wins
    # and drops q_S^3; Step 3 averages q_S^1 and q_S^2 -> [0.91, 0.09] with n_p = 2!
    assert n_support == 2
    assert abs(p_vote[0] - 0.91) < 1e-12 and abs(p_vote[1] - 0.09) < 1e-12

    # 2. Verify Consensus Focus (Equations 7-9, pages 4-5) penalizes malicious/irrelevant domains
    # Suppose 3 source domains (0: relevant, 1: relevant, 2: malicious/irrelevant) over 3 target samples
    domain_preds = [
        [[0.92, 0.08], [0.10, 0.90], [0.94, 0.06]],  # Domain 0 (high-quality consensus)
        [[0.90, 0.10], [0.06, 0.94], [0.91, 0.09]],  # Domain 1 (high-quality consensus)
        [[0.03, 0.97], [0.95, 0.05], [0.45, 0.55]],  # Domain 2 (malicious/irrelevant)
    ]
    all_doms = [0, 1, 2]
    q_all = coalition_quality(domain_preds, all_doms, gate=0.90)
    cf_vals = [
        max(0.0, q_all - coalition_quality(domain_preds, [j for j in all_doms if j != k], gate=0.90))
        for k in all_doms
    ]
    # Removing malicious Domain 2 does not reduce consensus quality Q(S), so CF(D_S^2) == 0!
    assert cf_vals[0] > 2.5 and cf_vals[1] > 2.5 and abs(cf_vals[2]) < 1e-12

    n_k = [1000, 1000, 1000]
    n_t = 1000
    alpha_k_plus_1 = n_t / (sum(n_k) + n_t)
    denom = sum(n_k[k] * cf_vals[k] for k in range(3))
    alpha_cf = [(1.0 - alpha_k_plus_1) * (n_k[k] * cf_vals[k]) / denom for k in range(3)]
    assert abs(sum(alpha_cf) + alpha_k_plus_1 - 1.0) < 1e-12
    assert alpha_cf[2] == 0.0 and alpha_cf[0] > 0.35

    # 3. Verify BatchNorm MMD closed-form solution (Equations 11-12 and Appendix E Eq. 18, pages 5, 12)
    # E[pi^2] = Var(pi) + (E[pi])^2
    weights = alpha_cf + [alpha_k_plus_1]
    bn_means = [1.0, 1.2, -5.0, 1.1]
    bn_vars = [0.5, 0.6, 9.0, 0.55]
    bn_second_moments = [bn_vars[k] + bn_means[k] ** 2 for k in range(4)]

    mu_op = sum(weights[k] * bn_means[k] for k in range(4))
    mu2_op = sum(weights[k] * bn_second_moments[k] for k in range(4))

    def bn_mmd_loss(mu_t: float, mu2_t: float) -> float:
        return sum(
            weights[k] * ((mu_t - bn_means[k]) ** 2 + (mu2_t - bn_second_moments[k]) ** 2)
            for k in range(4)
        )

    loss_opt = bn_mmd_loss(mu_op, mu2_op)
    loss_perturbed = bn_mmd_loss(mu_op + 0.2, mu2_op - 0.2)
    assert loss_opt < loss_perturbed

    print(
        f"[PASS] Round 520 KD3A (Feng et al. 2021): "
        f"fig1b_vote=({p_vote[0]:.2f},{p_vote[1]:.2f},n={n_support}), "
        f"CF={[round(v, 2) for v in cf_vals]}, alpha_CF2={alpha_cf[2]:.3f}, "
        f"bn_mmd_opt={loss_opt:.4f}<{loss_perturbed:.4f}"
    )


if __name__ == "__main__":
    main()
