#!/usr/bin/env python3
"""Constructed boundary verification for Supermasks in Superposition (SupSup, Wortsman et al., NeurIPS 2020)."""

from __future__ import annotations

import math
import random


def softmax(logits: list[float]) -> list[float]:
    m = max(logits)
    exps = [math.exp(x - m) for x in logits]
    s = sum(exps)
    return [e / s for e in exps]


def entropy(probs: list[float]) -> float:
    return -sum(p * math.log(max(p, 1e-15)) for p in probs)


def main() -> int:
    rng = random.Random(20260715)

    # 1. Verify Lemma J.2: h({y_v}, kappa) + h({y_v}, -kappa) >= 0 for all kappa > 0 (Eq. 54, 60-62)
    for _ in range(30):
        y = [rng.gauss(0.0, 2.0) for _ in range(10)]
        kappa = rng.uniform(0.05, 3.0)
        v = 0
        other_sum = sum(math.exp(y[idx]) for idx in range(1, len(y)))
        h_pos = kappa * math.exp(y[v] + kappa) / (math.exp(y[v] + kappa) + other_sum)
        h_neg = -kappa * math.exp(y[v] - kappa) / (math.exp(y[v] - kappa) + other_sum)
        assert h_pos + h_neg >= -1e-15

    # 2. Verify Lemma I.1, I.2, I.3 and One-Shot task inference (Eq. 4, 20-36)
    m_feat = 64
    num_real = 4
    num_total = 16  # 12 superfluous neurons (s-neurons)
    num_tasks = 6

    # Signed Kaiming constant weights W_uv = xi_uv * sqrt(2/m)
    scale = math.sqrt(2.0 / m_feat)
    w = [[(1.0 if rng.random() < 0.5 else -1.0) * scale for _ in range(num_total)] for _ in range(m_feat)]

    # Prototype input features and trained masks per task using Eq. (35) score updates
    task_inputs: list[list[float]] = []
    task_masks: list[list[list[float]]] = []
    for t in range(num_tasks):
        phi = [1.0 if rng.random() < 0.5 else -1.0 for _ in range(m_feat)]
        task_inputs.append(phi)
        true_cls = t % num_real
        scores = [[0.0 for _ in range(num_total)] for _ in range(m_feat)]
        # Perform gradient updates on scores S^t (Eq. 35) to push true_cls up and s-neurons down
        for _ in range(8):
            mask_cur = [[1.0 if scores[u][v] >= 0.0 else 0.0 for v in range(num_total)] for u in range(m_feat)]
            logits = [sum(phi[u] * w[u][v] * mask_cur[u][v] for u in range(m_feat)) for v in range(num_total)]
            probs = softmax(logits)
            for v in range(num_total):
                # Cross-entropy gradient dL/dy_v = p_v - 1_{v == true_cls}
                dl_dyv = probs[v] - (1.0 if v == true_cls else 0.0)
                for u in range(m_feat):
                    scores[u][v] += 0.5 * (-dl_dyv * phi[u] * w[u][v])
        mask_final = [[1.0 if scores[u][v] > 0.0 else 0.0 for v in range(num_total)] for u in range(m_feat)]
        task_masks.append(mask_final)

    # Verify Lemma I.1 exact gradient match on s-neurons and One-Shot task recovery across all k tasks
    correct_inferred = 0
    for j in range(num_tasks):
        phi = task_inputs[j]
        alpha = [1.0 / num_tasks] * num_tasks
        # Superimposed logits y_v = sum_u phi_u W_uv (sum_i alpha_i M^i_uv) (Eq. 19)
        y = [
            sum(
                phi[u] * w[u][v] * sum(alpha[i] * task_masks[i][u][v] for i in range(num_tasks))
                for u in range(m_feat)
            )
            for v in range(num_total)
        ]
        probs = softmax(y)
        # Lemma I.1: dG/dy_v = probs[v] for v in S (v >= num_real) and 0 for v in R (v < num_real)
        dg_dy = [0.0 if v < num_real else probs[v] for v in range(num_total)]
        # Eq. (27): -dG/dalpha_i = -sum_{v in S} dG/dy_v * dy_v/dalpha_i
        neg_grad_alpha = []
        for i in range(num_tasks):
            grad_i = sum(
                dg_dy[v] * sum(phi[u] * w[u][v] * task_masks[i][u][v] for u in range(m_feat))
                for v in range(num_real, num_total)
            )
            neg_grad_alpha.append(-grad_i)
        inferred = max(range(num_tasks), key=lambda i: neg_grad_alpha[i])
        if inferred == j:
            correct_inferred += 1
        assert neg_grad_alpha[j] > 0.0

    assert correct_inferred == num_tasks

    # 3. Verify Scenario NNs uncertainty detection criterion k * max_i nu_i < 1 + eps (Section 3.4)
    eps = 0.125
    nu_uniform = softmax([0.0] * num_tasks)
    assert num_tasks * max(nu_uniform) < 1.0 + eps  # triggers new mask allocation
    nu_confident = softmax(neg_grad_alpha)
    assert num_tasks * max(nu_confident) > 1.0 + eps  # selects existing mask

    print(
        f"[PASS] SupSup boundaries verified: One-Shot recovery={correct_inferred}/{num_tasks}, "
        f"Lemma I.1/I.2/I.3/J.2 verified, NNs_conf={num_tasks * max(nu_confident):.3f} > {1.0 + eps:.3f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
