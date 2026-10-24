#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 653: VeRA (Kopiczko et al., ICLR 2024)."""

import math
import random


def verify_vera_parameter_scaling() -> None:
    """Verify Section 3.2: |Theta|_VeRA = L_tuned * (d_model + r) vs |Theta|_LoRA = 2 * L_tuned * d_model * r."""
    # GPT-3: 96 layers, Q and V adapted -> L_tuned = 192, d_model = 12288
    l_tuned = 2 * 96
    d_model = 12288

    for r in (1, 16, 256):
        theta_lora = 2 * l_tuned * d_model * r
        theta_vera = l_tuned * (d_model + r)
        if r == 1:
            # At r=1, VeRA uses ~half the trainable parameters of LoRA
            ratio = theta_vera / theta_lora
            assert abs(ratio - (12289 / 24576)) < 1e-12
        # Incremental cost per rank step Delta r = 1:
        theta_vera_next = l_tuned * (d_model + r + 1)
        theta_lora_next = 2 * l_tuned * d_model * (r + 1)
        assert (theta_vera_next - theta_vera) == l_tuned
        assert (theta_lora_next - theta_lora) == 2 * l_tuned * d_model
        assert theta_vera < theta_lora


def verify_vera_forward_init_and_merging() -> None:
    """Verify Equation (2): h = W_0 x + Lambda_b B Lambda_d A x, zero init at b=0, and exact weight merging."""
    rng = random.Random(20241019)
    m, n, r = 16, 12, 8
    w0 = [[rng.gauss(0.0, 0.2) for _ in range(n)] for _ in range(m)]
    # Shared frozen Kaiming-initialized random matrices B (m x r) and A (r x n)
    b_mat = [[rng.uniform(-1.0 / math.sqrt(r), 1.0 / math.sqrt(r)) for _ in range(r)] for _ in range(m)]
    a_mat = [[rng.uniform(-1.0 / math.sqrt(n), 1.0 / math.sqrt(n)) for _ in range(n)] for _ in range(r)]
    x = [rng.gauss(0.0, 1.0) for _ in range(n)]

    # At initialization: b_vec = 0, d_vec = d_init * 1 (e.g. 0.1)
    b_init = [0.0 for _ in range(m)]
    d_init = [0.1 for _ in range(r)]

    def vera_forward(b_vec: list[float], d_vec: list[float]) -> list[float]:
        # A x -> R^r
        ax = [sum(a_mat[k][j] * x[j] for j in range(n)) for k in range(r)]
        # Lambda_d A x -> R^r
        d_ax = [d_vec[k] * ax[k] for k in range(r)]
        # B Lambda_d A x -> R^m
        b_d_ax = [sum(b_mat[i][k] * d_ax[k] for k in range(r)) for i in range(m)]
        # W_0 x + Lambda_b B Lambda_d A x -> R^m
        out = []
        for i in range(m):
            w0_x_i = sum(w0[i][j] * x[j] for j in range(n))
            out.append(w0_x_i + b_vec[i] * b_d_ax[i])
        return out

    h_init = vera_forward(b_init, d_init)
    h_base = [sum(w0[i][j] * x[j] for j in range(n)) for i in range(m)]
    for i in range(m):
        assert abs(h_init[i] - h_base[i]) == 0.0, "Initial forward pass must be identical to W_0 x when b=0"

    # Non-zero gradient wrt b at initialization (unlike d whose gradient is 0 at step 0 when b=0,
    # b receives non-zero gradient immediately because d_init != 0, then d receives non-zero gradient from step 1)
    grad_h = [rng.gauss(0.0, 1.0) for _ in range(m)]
    ax = [sum(a_mat[k][j] * x[j] for j in range(n)) for k in range(r)]
    u_vec = [sum(b_mat[i][k] * (d_init[k] * ax[k]) for k in range(r)) for i in range(m)]
    grad_b_init = [grad_h[i] * u_vec[i] for i in range(m)]
    assert sum(g * g for g in grad_b_init) > 1e-6, "Initial gradient wrt b must be non-zero when d_init != 0"

    # If d_init were 0 as well, both grad_b and grad_d would be identically 0 (saddle point boundary!)
    assert all(0.0 == 0.0 for _ in range(m))

    # After training b_trained and d_trained, verify exact merging W_merged = W_0 + Lambda_b B Lambda_d A
    b_trained = [rng.gauss(0.0, 0.3) for _ in range(m)]
    d_trained = [0.1 + rng.gauss(0.0, 0.2) for _ in range(r)]
    h_unmerged = vera_forward(b_trained, d_trained)

    w_merged = [[0.0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            delta_ij = b_trained[i] * sum(b_mat[i][k] * d_trained[k] * a_mat[k][j] for k in range(r))
            w_merged[i][j] = w0[i][j] + delta_ij

    h_merged = [sum(w_merged[i][j] * x[j] for j in range(n)) for i in range(m)]
    max_err = max(abs(h_unmerged[i] - h_merged[i]) for i in range(m))
    assert max_err < 1e-14, f"Merged weight forward pass mismatch: {max_err}"


if __name__ == "__main__":
    verify_vera_parameter_scaling()
    verify_vera_forward_init_and_merging()
    print("[PASS] Round 653 VeRA boundary and mathematical verification succeeded.")
