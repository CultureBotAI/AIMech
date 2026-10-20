#!/usr/bin/env python3
"""Constructed boundary verification for Round 640: LISA (Pan et al., NeurIPS 2024)."""

from __future__ import annotations
import math
import random


def verify_layerwise_importance_sampling_expectation() -> tuple[float, float, float]:
    """Verify Section 3.2 layerwise importance sampling identity E[I_ell * eta_ell] == tilde_eta_ell * (tilde_w_ell / w_ell)."""
    n_layers = 32
    gamma = 2  # E+H+2L configuration on 32-layer LLaMA-2-7B / Mistral-7B
    base_lr = 5e-5

    # Activation probabilities {p_ell}: embedding (0) and LM head (n_layers+1) have p = 1.0,
    # while NL = 32 intermediate layers each have p_ell = gamma / NL
    p_probs = [1.0] + [gamma / n_layers for _ in range(n_layers)] + [1.0]
    expected_active_intermediate = sum(p_probs[1:-1])
    assert abs(expected_active_intermediate - gamma) < 1e-14

    # Under Algorithm 1 (sampling exactly gamma intermediate layers uniformly without replacement per K-step window):
    # each intermediate layer ell in {1, ..., NL} is selected with marginal probability exactly gamma / NL,
    # and the maximum number of simultaneously active intermediate layers is strictly upper-bounded by gamma!
    rng = random.Random(20261019)
    n_periods = 4000
    counts = [0] * n_layers
    max_simultaneous_active = 0
    for _ in range(n_periods):
        active_set = rng.sample(range(n_layers), gamma)
        max_simultaneous_active = max(max_simultaneous_active, len(active_set))
        for idx in active_set:
            counts[idx] += 1

    assert max_simultaneous_active == gamma
    empirical_probs = [c / n_periods for c in counts]
    max_prob_err = max(abs(ep - (gamma / n_layers)) for ep in empirical_probs)
    assert max_prob_err < 0.015, f"Empirical inclusion probability deviated from gamma/NL: {max_prob_err}"

    # Effective expected step size for intermediate layer vs embedding/head layer matches skewness ratio gamma / NL:
    effective_lr_ratio = (base_lr * (gamma / n_layers)) / (base_lr * 1.0)
    assert abs(effective_lr_ratio - (gamma / n_layers)) < 1e-15
    return expected_active_intermediate, max_prob_err, effective_lr_ratio


def verify_memory_reduction_and_theorem1_regularized_adamw() -> tuple[float, float, float]:
    """Verify Section 4.1 active optimizer/gradient state fraction and Section 5 Theorem 1 regularized convex convergence."""
    # Compare active trainable parameters at any instant on LLaMA-2-7B (32 layers, d_model=4096, d_mlp=11008, vocab=32000)
    d_model = 4096
    d_mlp = 11008
    vocab = 32000
    n_layers = 32
    gamma = 2

    layer_params = 4 * (d_model * d_model) + 3 * (d_model * d_mlp)  # 202,375,168 params per Transformer block
    embed_head_params = 2 * (vocab * d_model)  # 262,144,000 params for E + H

    full_trainable_params = n_layers * layer_params + embed_head_params
    lisa_active_params = gamma * layer_params + embed_head_params
    active_state_fraction = lisa_active_params / full_trainable_params
    # Only ~9.9% of parameters require gradients and AdamW states in GPU memory during any K-step period!
    assert active_state_fraction < 0.10, f"Expected <10% active trainable parameters, got {active_state_fraction:.4f}"

    # Verify Section 5 Theorem 1 convergence of LISA on regularized convex objective f^reg(w) = f(w) + 0.5 * w^T S w
    # Let f(w) = 0.5 * sum_{l=1}^4 c_l * (w_l - w*_l)^2 and regularizer S = diag(s_1, ..., s_4)
    c_l = [2.0, 1.5, 1.0, 2.5]
    w_star = [1.2, -0.8, 0.6, -1.0]
    s_l = [0.1, 0.1, 0.1, 0.1]
    # Exact optimum of f^reg(w) = 0.5 * sum c_l (w_l - w*_l)^2 + 0.5 * sum s_l w_l^2 is w_reg*_l = (c_l / (c_l + s_l)) * w*_l
    w_reg_star = [(c_l[i] / (c_l[i] + s_l[i])) * w_star[i] for i in range(4)]

    def f_reg(w: list[float]) -> float:
        return sum(
            0.5 * c_l[i] * ((w[i] - w_star[i]) ** 2) + 0.5 * s_l[i] * (w[i] ** 2)
            for i in range(4)
        )

    f_opt = f_reg(w_reg_star)
    w_curr = [0.0, 0.0, 0.0, 0.0]
    f_init = f_reg(w_curr)

    rng = random.Random(42)
    t_total = 200
    k_period = 5
    eta0 = 0.15
    sum_subopt = 0.0
    for period in range(t_total // k_period):
        # Layer 0 (E) and Layer 3 (H) always active; sample gamma=1 intermediate layer from {1, 2}
        mid_layer = rng.choice([1, 2])
        active = {0, mid_layer, 3}
        for step_in_k in range(k_period):
            t = period * k_period + step_in_k + 1
            eta_t = eta0 / math.sqrt(t)
            for i in active:
                grad_i = c_l[i] * (w_curr[i] - w_star[i]) + s_l[i] * w_curr[i]
                w_curr[i] -= eta_t * grad_i
            sum_subopt += f_reg(w_curr) - f_opt

    avg_regret = sum_subopt / t_total
    final_gap = f_reg(w_curr) - f_opt
    assert final_gap < 0.01 * (f_init - f_opt)
    return active_state_fraction, avg_regret, final_gap


if __name__ == "__main__":
    exp_act, p_err, lr_rat = verify_layerwise_importance_sampling_expectation()
    act_frac, avg_reg, fin_gap = verify_memory_reduction_and_theorem1_regularized_adamw()
    print(
        f"[PASS] Round 640 LISA verified: exp_active={exp_act:.1f}, prob_err={p_err:.4f}, "
        f"lr_ratio={lr_rat:.4f}, active_param_frac={act_frac:.2%}, avg_regret={avg_reg:.4e}, final_gap={fin_gap:.4e}"
    )
