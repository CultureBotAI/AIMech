#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 716: Child-Tuning (Xu et al., EMNLP 2021)."""

import math


def verify_child_tuning() -> None:
    # 1. Task-Free Child-Tuning_F (Eq. 4, 5, 11, 12):
    # M_t ~ Bernoulli(p_F), reserved gradients scaled by 1/p_F:
    # E[g_hat] = (p_F / p_F) * dL/dw = dL/dw (unbiased gradient expectation).
    # Covariance of update Delta_w = -eta * g_hat for batch size |B|:
    # Sigma[Delta_w] = (eta^2 * sigma_g^2 / (p_F * |B|)) * I_k + ((1 - p_F) * eta^2 / p_F) * diag(dL/dw)^2
    eta = 0.01
    sigma_g = 0.5
    batch_size = 16
    grad = [0.2, -0.4, 0.1, 0.3]

    def update_var(p_f: float, g_i: float) -> float:
        return (eta**2 * sigma_g**2) / (p_f * batch_size) + ((1.0 - p_f) * eta**2 * (g_i**2)) / p_f

    # At p_F = 1.0, degenerates to vanilla SGD variance eta^2 * sigma_g^2 / |B|
    v_vanilla = (eta**2 * sigma_g**2) / batch_size
    for g_i in grad:
        assert math.isclose(update_var(1.0, g_i), v_vanilla, rel_tol=1e-12)
        # Strictly decreasing function of p_F in (0, 1]
        assert update_var(0.2, g_i) > update_var(0.4, g_i) > update_var(1.0, g_i)

    # 2. Task-Driven Child-Tuning_D (Eq. 10):
    # Empirical diagonal Fisher Information F^(i)(w) = (1/|D|) * sum_{j=1}^{|D|} (d log p(y_j | x_j; w) / dw^(i))^2
    log_prob_grads = [
        [0.5, 0.02, 0.8, 0.01, 0.6, 0.05],
        [0.4, 0.01, 0.7, 0.02, 0.5, 0.04],
        [0.6, 0.03, 0.9, 0.01, 0.7, 0.03],
    ]
    k_params = len(log_prob_grads[0])
    n_data = len(log_prob_grads)
    fisher_diag = [
        sum(log_prob_grads[j][i] ** 2 for j in range(n_data)) / n_data
        for i in range(k_params)
    ]
    # Top p_D = 0.5 parameters by Fisher information form child network C_0 = ... = C_T
    p_d = 0.5
    n_child = int(round(p_d * k_params))
    ranked_indices = sorted(range(k_params), key=lambda i: fisher_diag[i], reverse=True)
    child_set = set(ranked_indices[:n_child])
    assert child_set == {0, 2, 4}
    mask_d = [1.0 if i in child_set else 0.0 for i in range(k_params)]
    assert sum(mask_d) / k_params == p_d

    # Non-child parameters remain frozen at pretrained weights w_0 while still participating in forward pass
    w_0 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    step_grad = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
    w_1 = [w_0[i] - eta * step_grad[i] * mask_d[i] for i in range(k_params)]
    for i in range(k_params):
        if i not in child_set:
            assert w_1[i] == w_0[i]
        else:
            assert w_1[i] != w_0[i]

    print("Child-Tuning verification passed.")


if __name__ == "__main__":
    verify_child_tuning()
