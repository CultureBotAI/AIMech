#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 727: Black-Box Tuning (Sun et al., ICML 2022)."""

import math


def verify_black_box_tuning() -> None:
    # 1. Intrinsic subspace projection (Section 3.2, Eq. 1):
    # Continuous prompt p in R^D (D = L * d_model = 50 * 1024 = 51,200) is parameterized via
    # p = A z + p_0 where z in [-5, 5]^d (d = 500 << D) and A in R^{D x d}:
    l_prompt = 50
    d_model = 1024
    big_d = l_prompt * d_model
    small_d = 500
    assert big_d == 51_200
    assert big_d / small_d == 102.4

    # Toy projection: D = 6, d = 2
    p_0 = [0.1, -0.2, 0.3, 0.0, -0.1, 0.2]
    A = [
        [0.5, -0.2],
        [0.1, 0.4],
        [-0.3, 0.6],
        [0.2, 0.2],
        [-0.4, 0.1],
        [0.3, -0.5],
    ]
    z = [1.2, -0.8]
    p = [p_0[r] + sum(A[r][c] * z[c] for c in range(2)) for r in range(6)]
    assert len(p) == 6 and p != p_0

    # 2. Multi-class Hinge Loss (Eq. 3) and Cross-Entropy Loss (Eq. 2):
    # L_Hinge(y_hat, y_tilde) = sum_{i != y_tilde} max(0, gamma + y_hat_i - y_hat_{y_tilde}) with gamma = 2
    gamma = 2.0
    y_hat = [3.2, 1.8, 0.5]  # gold index y_tilde = 0
    l_hinge = sum(max(0.0, gamma + y_hat[i] - y_hat[0]) for i in (1, 2))
    assert math.isclose(l_hinge, max(0.0, 2.0 + 1.8 - 3.2) + max(0.0, 2.0 + 0.5 - 3.2), rel_tol=1e-12)
    assert math.isclose(l_hinge, 0.6, rel_tol=1e-12)

    # 3. Population size formula (Section 4.3): lambda = 4 + floor(3 * ln(d)) -> ~20 for d = 500
    pop_size = int(4 + round(3 * math.log(small_d)))
    assert 18 <= pop_size <= 23
    print("Black-Box Tuning verification passed.")


if __name__ == "__main__":
    verify_black_box_tuning()
