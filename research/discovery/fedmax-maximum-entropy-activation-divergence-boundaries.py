#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 477:
FedMAX (Mitigating Activation Divergence for Accurate and Communication-Efficient Federated Learning,
Chen, Bhardwaj, & Marculescu 2020, ECML PKDD 2020, arXiv:2004.03657).

Verifies:
1. Exact equivalence up to an additive constant between Maximum Entropy activation
   regularization (Equation 3) and KL-divergence to the uniform distribution U
   over D-dimensional softmax-normalized penultimate activations a_i^k (Equation 4):
   g_k(w_k) = F_k(w_k) - (beta / N) sum_{i=1}^N H(sigma(a_i^k))
   == F_k(w_k) + (beta / N) sum_{i=1}^N KL(sigma(a_i^k) || U) - beta * log(D),
   so their gradients w.r.t. w_k are identical:
   nabla_w [ -H(sigma(a_i^k)) ] == nabla_w [ KL(sigma(a_i^k) || U) ].
2. Reduction of cross-device activation KL divergence delta = (1/M) sum_k KL(a_bar || a_k)
   (Section 4.1, p. 7) compared to unregularized FedAvg (beta = 0) while avoiding
   the activation-collapse-to-zero pathology of L2 norm regularization (Equation 2).
"""

from __future__ import annotations
import math


def softmax(vec: list[float]) -> list[float]:
    m = max(vec)
    exps = [math.exp(v - m) for v in vec]
    s = sum(exps)
    return [e / s for e in exps]


def shannon_entropy(p: list[float]) -> float:
    return -sum(pi * math.log(max(pi, 1e-15)) for pi in p)


def kl_to_uniform(p: list[float]) -> float:
    d = len(p)
    u = 1.0 / d
    return sum(pi * math.log(max(pi, 1e-15) / u) for pi in p)


def kl_div(p: list[float], q: list[float]) -> float:
    return sum(pi * math.log(max(pi, 1e-15) / max(qi, 1e-15)) for pi, qi in zip(p, q))


def grad_neg_entropy_wrt_logits(a: list[float]) -> list[float]:
    # For p = softmax(a), -H(p) = sum_j p_j log p_j
    # d(-H(p)) / d a_m = p_m * (log p_m + H(p))
    p = softmax(a)
    h = shannon_entropy(p)
    return [pm * (math.log(max(pm, 1e-15)) + h) for pm in p]


def main() -> None:
    D = 6
    test_activations = [
        [2.5, -1.0, 0.4, -0.8, 1.2, -0.3],
        [-0.5, 3.1, -1.2, 0.7, 0.1, -0.9],
        [0.8, 0.2, -0.4, 2.2, -1.5, 0.6],
    ]

    # 1. Verify KL(p || U) == -H(p) + log(D) and exact gradient identity between Eq (3) and Eq (4)
    eps = 1e-7
    for a in test_activations:
        p = softmax(a)
        h_val = shannon_entropy(p)
        kl_val = kl_to_uniform(p)
        assert abs(kl_val - (-h_val + math.log(D))) < 1e-14

        g_analytic = grad_neg_entropy_wrt_logits(a)
        for m in range(D):
            a_plus = a[:]
            a_minus = a[:]
            a_plus[m] += eps
            a_minus[m] -= eps
            fd_h = (-shannon_entropy(softmax(a_plus)) - (-shannon_entropy(softmax(a_minus)))) / (2.0 * eps)
            fd_kl = (kl_to_uniform(softmax(a_plus)) - kl_to_uniform(softmax(a_minus))) / (2.0 * eps)
            assert abs(fd_h - fd_kl) < 1e-8
            assert abs(g_analytic[m] - fd_kl) < 1e-8

    # 2. Verify cross-device activation divergence delta = (1/M) sum_k KL(a_bar || a_k) shrinks under FedMAX steps
    device_acts = [row[:] for row in test_activations]
    M = len(device_acts)

    def compute_delta(acts: list[list[float]]) -> float:
        probs = [softmax(a) for a in acts]
        a_bar = [sum(probs[k][d] for k in range(M)) / M for d in range(D)]
        return sum(kl_div(a_bar, probs[k]) for k in range(M)) / M

    delta_fedavg = compute_delta(device_acts)
    # Apply local FedMAX gradient steps on penultimate activations
    acts_fedmax = [row[:] for row in device_acts]
    beta_lr = 0.4
    for _step in range(20):
        for k in range(M):
            g = grad_neg_entropy_wrt_logits(acts_fedmax[k])
            acts_fedmax[k] = [acts_fedmax[k][d] - beta_lr * g[d] for d in range(D)]
    delta_fedmax = compute_delta(acts_fedmax)
    assert delta_fedmax < 0.2 * delta_fedavg, f"Expected FedMAX to reduce activation divergence: {delta_fedmax} vs {delta_fedavg}"

    # Verify FedMAX preserves non-zero activation norm whereas L2 penalty (Eq 2) shrinks norm toward zero
    norm_fedmax = sum(math.sqrt(sum(v * v for v in a)) for a in acts_fedmax) / M
    acts_l2 = [[v * ((1.0 - 0.15) ** 15) for v in row] for row in device_acts]
    norm_l2 = sum(math.sqrt(sum(v * v for v in a)) for a in acts_l2) / M
    assert norm_fedmax > 3.0 * norm_l2

    print(
        f"[PASS] FedMAX boundary verification passed: delta_FedAvg={delta_fedavg:.4f} -> "
        f"delta_FedMAX={delta_fedmax:.4f}, norm_FedMAX={norm_fedmax:.3f} > norm_L2={norm_l2:.3f}"
    )


if __name__ == "__main__":
    main()
