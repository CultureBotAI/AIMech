#!/usr/bin/env python3
"""Boundary verification for Round 695: FISH Mask (Sung, Nair, & Raffel, NeurIPS 2021, arXiv:2111.09839)."""

import math


def softmax(logits: list[float]) -> list[float]:
    m = max(logits)
    exps = [math.exp(z - m) for z in logits]
    s = sum(exps)
    return [e / s for e in exps]


def main() -> int:
    # 1. Verify Eq. (1)-(3) (Section 2.1-2.2, pp. 3-4):
    # Diagonal Fisher information F_hat_theta = (1/N) sum_{i=1}^N E_{y ~ p_theta(y|x_i)} [(grad_theta log p_theta(y|x_i))^2]
    # and second-order KL divergence E_x[D_KL(p_theta || p_{theta + delta})] = (1/2) delta^T F_theta delta + O(delta^3).
    # Consider a binary logistic model p_theta(y=1|x) = sigma(theta^T x) over d=8 parameters.
    d = 8
    theta0 = [0.2, -0.1, 0.05, 0.3, -0.2, 0.1, -0.05, 0.15]
    # Active features on coordinates 0, 3, 6 have strong signal magnitude; others have near-zero sensitivity
    samples_x = [
        [2.5, 0.02, -0.01, -2.2, 0.03, 0.01, 1.9, -0.02],
        [-2.1, -0.01, 0.02, 2.4, -0.02, 0.02, -2.3, 0.01],
        [1.8, 0.03, 0.01, 2.0, -0.01, -0.02, 2.1, 0.02],
        [-2.4, 0.01, -0.02, -1.9, 0.02, 0.01, -1.8, -0.01],
    ]
    labels_y = [1, 0, 1, 0]

    def prob1(th: list[float], x: list[float]) -> float:
        z = sum(th[j] * x[j] for j in range(d))
        return 1.0 / (1.0 + math.exp(-z))

    # Compute exact diagonal Fisher F_hat and empirical Fisher F_emp (Eq. 3):
    f_hat = [0.0] * d
    f_emp = [0.0] * d
    for x, y_true in zip(samples_x, labels_y):
        p1 = prob1(theta0, x)
        p0 = 1.0 - p1
        # grad_theta log p(y=1|x) = (1 - p1) x; grad_theta log p(y=0|x) = -p1 x
        for j in range(d):
            g1 = (1.0 - p1) * x[j]
            g0 = (-p1) * x[j]
            f_hat[j] += (p1 * (g1 ** 2) + p0 * (g0 ** 2)) / len(samples_x)
            g_true = g1 if y_true == 1 else g0
            f_emp[j] += (g_true ** 2) / len(samples_x)

    # Check second-order KL approximation along each coordinate j:
    eps = 1e-4
    for j in range(d):
        th_pert = list(theta0)
        th_pert[j] += eps
        kl_avg = 0.0
        for x in samples_x:
            p = prob1(theta0, x)
            q = prob1(th_pert, x)
            kl = p * math.log(p / q) + (1.0 - p) * math.log((1.0 - p) / (1.0 - q))
            kl_avg += kl / len(samples_x)
        # Standard second-order Taylor of KL is 0.5 * eps^2 * F_jj
        assert abs(kl_avg - 0.5 * (eps ** 2) * f_hat[j]) < 1e-10

    # Top-k=3 FISH Mask selection: {theta_i | F_hat_{theta_i} >= sort(F_hat_theta)_k}
    k = 3
    fish_mask_true = set(sorted(range(d), key=lambda j: f_hat[j], reverse=True)[:k])
    fish_mask_emp = set(sorted(range(d), key=lambda j: f_emp[j], reverse=True)[:k])
    assert fish_mask_true == {0, 3, 6}
    assert fish_mask_emp == {0, 3, 6}  # True and Empirical Fisher select the exact same mask (Section 4.4.1)

    # 2. Compare fixed sparse mask training (FISH Mask vs Random Mask vs Dense) over T=40 gradient steps:
    def run_training(mask_indices: set[int], steps: int = 40, lr: float = 0.25) -> float:
        th = list(theta0)
        for _ in range(steps):
            grad = [0.0] * d
            for x, y_true in zip(samples_x, labels_y):
                p1 = prob1(th, x)
                diff = p1 - (1.0 if y_true == 1 else 0.0)
                for j in mask_indices:
                    grad[j] += diff * x[j] / len(samples_x)
            for j in mask_indices:
                th[j] -= lr * grad[j]
        # Return final NLL loss
        loss = 0.0
        for x, y_true in zip(samples_x, labels_y):
            p1 = prob1(th, x)
            p_y = p1 if y_true == 1 else (1.0 - p1)
            loss -= math.log(p_y) / len(samples_x)
        return loss

    loss_dense = run_training(set(range(d)))
    loss_fish = run_training(fish_mask_true)
    loss_random = run_training({1, 2, 4})

    assert abs(loss_fish - loss_dense) < 1e-3
    assert loss_fish < 0.05 * loss_random

    # 3. Verify checkpoint disk & communication savings formula (Section 4.2-4.3, pp. 7-9):
    # Storing 32-bit float value + 32-bit int index for k = s * |theta| params reduces size by factor 1/(2s) for s < 0.5
    s_ckpt = 0.10
    compression_factor = 1.0 / (2.0 * s_ckpt)
    assert abs(compression_factor - 5.0) < 1e-12

    print(
        f"[PASS] Round 695 FISH Mask (Sung et al., NeurIPS 2021): fish_mask={sorted(fish_mask_true)}, "
        f"loss_fish={loss_fish:.5f} ~= loss_dense={loss_dense:.5f} << loss_random={loss_random:.5f}, "
        f"ckpt_factor(s=10%)={compression_factor:.1f}x"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
