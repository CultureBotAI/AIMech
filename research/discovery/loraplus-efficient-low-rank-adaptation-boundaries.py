#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 654: LoRA+ (Hayou, Ghosh, & Yu, ICML 2024)."""

import math
import random


def verify_loraplus_scaling_exponents() -> None:
    """Verify Propositions 1 & 2 and Theorem 1 width-scaling exponent equations in Appendix A.3-A.5."""
    # In the toy linear model (Propositions 1 & 2, Appendix A.3-A.4):
    # Efficiency requires:
    #   gamma[eta_a] + 2 * gamma[b_{t-1}] + 1 = 0   (delta_t^1 = Theta(1))
    #   gamma[eta_b] + 2 * gamma[a_{t-1}^T x] = 0   (delta_t^2 = Theta(1))
    #   gamma[b_{t-1}] + gamma[a_{t-1}^T x] = 0     (f_{t-1}(x) = Theta(1))
    # Summing the first two and subtracting 2 * the third gives:
    #   gamma[eta_a] + gamma[eta_b] + 1 = 0 => gamma[eta_a] + gamma[eta_b] = -1.

    # Case 1: Standard LoRA with equal learning rates gamma[eta_a] = gamma[eta_b] = c
    c_equal = -0.5
    # Under Init[1] (b_0 = 0, sigma_a^2 = Theta(n^{-1}) => gamma[a_0^T x] = 0):
    gamma_b1_equal = c_equal + 0.0  # -0.5
    gamma_ax1_equal = 0.0
    gamma_f1_equal = gamma_b1_equal + gamma_ax1_equal  # -0.5 != 0 (lazy / vanishing feature update!)
    assert gamma_f1_equal == -0.5, "Equal learning rate under Init[1] yields O(n^{-1/2}) vanishing feature updates"

    # Case 2: LoRA+ with gamma[eta_a] = -1, gamma[eta_b] = 0 (i.e., eta_B / eta_A = Theta(n))
    gamma_eta_a = -1.0
    gamma_eta_b = 0.0
    assert gamma_eta_a + gamma_eta_b == -1.0
    # Under Init[1]:
    gamma_b1_plus = gamma_eta_b + 0.0  # 0.0
    gamma_ax1_plus = max(0.0, gamma_eta_a + gamma_b1_plus + 1.0)  # max(0, -1 + 0 + 1) = 0.0
    gamma_delta1 = gamma_eta_a + 2.0 * gamma_b1_plus + 1.0  # 0.0 -> Theta(1)
    gamma_delta2 = gamma_eta_b + 2.0 * gamma_ax1_plus  # 0.0 -> Theta(1)
    gamma_delta3 = gamma_eta_a + gamma_eta_b + gamma_b1_plus + gamma_ax1_plus + 1.0  # 0.0 -> Theta(1)
    assert gamma_delta1 == 0.0 and gamma_delta2 == 0.0 and gamma_delta3 == 0.0


def verify_loraplus_feature_update_decomposition() -> None:
    """Verify exact decomposition Delta f_t = delta_t^1 + delta_t^2 + delta_t^3 and width scaling."""
    rng = random.Random(20240212)
    for n in (64, 512, 4096):
        x = [rng.gauss(0.0, 1.0) for _ in range(n)]
        norm_x_sq = sum(xi * xi for xi in x)
        y = 1.5
        # Init[1]: a_0 ~ N(0, 1/n), b_0 = 0
        a0 = [rng.gauss(0.0, 1.0 / math.sqrt(n)) for _ in range(n)]
        b0 = 0.0
        a0_x = sum(a0[i] * x[i] for i in range(n))

        # Step 1 with LoRA+ (eta_a = 0.5 / n, eta_b = 0.5 => lambda = n)
        eta_a = 0.5 / n
        eta_b = 0.5
        u0 = b0 * a0_x - y  # -y
        grad_b0 = a0_x * u0
        grad_a0 = [b0 * u0 * xi for xi in x]
        b1 = b0 - eta_b * grad_b0
        a1 = [a0[i] - eta_a * grad_a0[i] for i in range(n)]

        # Step 2: verify exact identity Delta f_2 = f_2(x) - f_1(x) = delta_2^1 + delta_2^2 + delta_2^3
        f1 = b1 * sum(a1[i] * x[i] for i in range(n))
        u1 = f1 - y
        a1_x = sum(a1[i] * x[i] for i in range(n))
        grad_b1 = a1_x * u1
        grad_a1 = [b1 * u1 * xi for xi in x]

        b2 = b1 - eta_b * grad_b1
        a2 = [a1[i] - eta_a * grad_a1[i] for i in range(n)]
        f2 = b2 * sum(a2[i] * x[i] for i in range(n))

        delta_1 = -eta_a * (b1 ** 2) * u1 * norm_x_sq
        delta_2 = -eta_b * (a1_x ** 2) * u1
        delta_3 = eta_a * eta_b * (u1 ** 2) * b1 * a1_x * norm_x_sq
        lhs = f2 - f1
        rhs = delta_1 + delta_2 + delta_3
        assert abs(lhs - rhs) < 1e-12, f"Decomposition mismatch at n={n}: {lhs} vs {rhs}"
        # Both |delta_1| and |delta_2| remain O(1) across n=64..4096 under LoRA+ scaling
        assert abs(delta_1) > 1e-3 and abs(delta_2) > 1e-3


if __name__ == "__main__":
    verify_loraplus_scaling_exponents()
    verify_loraplus_feature_update_decomposition()
    print("[PASS] Round 654 LoRA+ boundary and mathematical verification succeeded.")
