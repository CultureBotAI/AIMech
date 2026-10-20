#!/usr/bin/env python3
"""Constructed boundary verification for AMC: AutoML for Model Compression (He et al., ECCV 2018)."""

import math


def amc_duty_constrained_sparsity(raw_actions, layer_weights, target_sparsity_alpha, action_max=0.8):
    """Execute Algorithm 1: bound layer-wise sparsity action_t to meet overall target reduction alpha."""
    w_all = sum(layer_weights)
    w_reduced = 0.0
    bounded_actions = []
    n_layers = len(layer_weights)
    for t in range(n_layers):
        w_t = layer_weights[t]
        w_rest = sum(layer_weights[t + 1 :])
        action_t = min(raw_actions[t], action_max)
        w_duty = target_sparsity_alpha * w_all - action_max * w_rest - w_reduced
        action_t = max(action_t, w_duty / w_t)
        # Clamp to [0.0, 1.0] for feasibility when action_max allows
        action_t = max(0.0, min(1.0, action_t))
        w_reduced += action_t * w_t
        bounded_actions.append(action_t)
    achieved_sparsity = w_reduced / w_all
    return bounded_actions, achieved_sparsity


def reward_resource_constrained(val_error):
    """Compute resource-constrained reward R_err = -Error (Eq. 4)."""
    return -val_error


def reward_accuracy_guaranteed(val_error, resource_amount):
    """Compute accuracy-guaranteed reward R_FLOPs = -Error * log(FLOPs) or R_Param = -Error * log(#Param) (Eqs. 5-6)."""
    return -val_error * math.log(max(resource_amount, 1.0))


def main():
    # 1. Verify Algorithm 1 duty bound forces later layers to prune enough when early layers prune too little
    layer_weights = [100.0, 200.0, 300.0, 400.0]  # W_all = 1000
    # Agent proposes very conservative pruning (0.1) on all layers, but target overall sparsity is alpha = 0.5
    raw_actions = [0.1, 0.1, 0.1, 0.1]
    bounded, achieved = amc_duty_constrained_sparsity(
        raw_actions, layer_weights, target_sparsity_alpha=0.5, action_max=0.8
    )
    assert abs(achieved - 0.5) < 1e-9
    assert bounded[0] == 0.1  # Early layer allowed arbitrary action since W_rest can still cover duty
    assert bounded[-1] > 0.5  # Later layers forced up by W_duty / W_t

    # 2. Verify boundary case where raw actions exceed action_max = 0.8
    high_actions = [0.95, 0.90, 0.85, 0.92]
    bounded_hi, achieved_hi = amc_duty_constrained_sparsity(
        high_actions, layer_weights, target_sparsity_alpha=0.5, action_max=0.8
    )
    assert all(a <= 0.8 + 1e-9 for a in bounded_hi)
    assert achieved_hi >= 0.5

    # 3. Verify Eqs. 5-6 accuracy-guaranteed reward prefers smaller FLOPs at equal error and lower error at equal FLOPs
    r_large_flops = reward_accuracy_guaranteed(val_error=0.10, resource_amount=500e6)
    r_small_flops = reward_accuracy_guaranteed(val_error=0.10, resource_amount=250e6)
    r_lower_err = reward_accuracy_guaranteed(val_error=0.08, resource_amount=250e6)
    assert r_large_flops < r_small_flops < r_lower_err < 0.0
    assert reward_resource_constrained(0.08) > reward_resource_constrained(0.10)

    print(
        f"AMC verification passed: bounded={[round(x, 3) for x in bounded]}, "
        f"achieved={achieved:.4f}, r_small_flops={r_small_flops:.4f} > r_large_flops={r_large_flops:.4f}"
    )


if __name__ == "__main__":
    main()
