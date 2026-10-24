#!/usr/bin/env python3
"""Constructed boundary verification for HAQ: Hardware-Aware Automated Quantization (Wang et al., CVPR 2019)."""

import math


def map_continuous_action_to_bits(action_a, b_min=2, b_max=8):
    """Map continuous action a_k in [0, 1] to discrete bitwidth b_k (Eq. 3)."""
    return int(round(b_min - 0.5 + action_a * (b_max - b_min + 1)))


def linear_quantize_weight(w, bitwidth_b, clip_c):
    """Linearly quantize weight w into b bits on [-c, c] with s = c / (2^{b-1} - 1) (Eq. 4)."""
    s = clip_c / ((2 ** (bitwidth_b - 1)) - 1)
    clamped = max(-clip_c, min(clip_c, w))
    return round(clamped / s) * s


def enforce_resource_budget(bitwidths, layer_costs_per_bit, budget, b_min=2):
    """Sequentially decrease bitwidth of each layer until hardware resource constraint is satisfied (Section 3.2)."""
    adjusted = list(bitwidths)
    total_cost = lambda bw: sum(b * c for b, c in zip(bw, layer_costs_per_bit))
    while total_cost(adjusted) > budget and any(b > b_min for b in adjusted):
        for idx in range(len(adjusted)):
            if total_cost(adjusted) <= budget:
                break
            if adjusted[idx] > b_min:
                adjusted[idx] -= 1
    return adjusted, total_cost(adjusted)


def ddpg_target_q(reward_r, baseline_b, next_q, gamma=1.0):
    """Compute variance-reduced Bellman target Q_hat_k = R_k - B + gamma * Q(O_{k+1}, w(O_{k+1})) (Eq. 7)."""
    return reward_r - baseline_b + gamma * next_q


def main():
    # 1. Verify Eq. 3 continuous-to-discrete bitwidth mapping preserves monotonic order across [2, 8]
    b_low = map_continuous_action_to_bits(0.0, 2, 8)
    b_mid = map_continuous_action_to_bits(0.5, 2, 8)
    b_high = map_continuous_action_to_bits(1.0, 2, 8)
    assert b_low == 2 and b_mid == 5 and b_high == 8

    # 2. Verify Eq. 4 linear quantization error decreases monotonically with higher bitwidth
    weights = [-0.83, -0.41, -0.12, 0.19, 0.57, 0.94]
    err_2bit = sum((w - linear_quantize_weight(w, 2, 1.0)) ** 2 for w in weights)
    err_4bit = sum((w - linear_quantize_weight(w, 4, 1.0)) ** 2 for w in weights)
    err_8bit = sum((w - linear_quantize_weight(w, 8, 1.0)) ** 2 for w in weights)
    assert err_8bit < err_4bit < err_2bit

    # 3. Verify Section 3.2 sequential bitwidth reduction satisfies hardware latency/energy budget
    init_bits = [8, 8, 8, 8]
    costs = [2.5, 4.0, 3.0, 1.5]
    budget = 55.0
    final_bits, final_cost = enforce_resource_budget(init_bits, costs, budget, b_min=2)
    assert final_cost <= budget and all(2 <= b <= 8 for b in final_bits)

    # 4. Verify Roofline operation intensity (OPs/Byte) distinction between depthwise (memory-bound) and pointwise (compute-bound)
    # Depthwise 3x3 on C=128, H=W=28 (batch=1): MACs = 9*128*784, Bytes ~ (2*784 + 9)*128
    dw_oi = (9.0 * 128 * 784) / ((2 * 784 + 9) * 128)
    # Pointwise 1x1 on C_in=128, C_out=128, H=W=28: MACs = 128*128*784, Bytes ~ (2*784*128 + 128*128)
    pw_oi = (128.0 * 128 * 784) / (2 * 784 * 128 + 128 * 128)
    assert dw_oi < pw_oi * 0.15

    # 5. Verify Eq. 6 reward and Eq. 7 Bellman target
    r_val = 0.1 * (71.20 - 70.82)
    q_hat = ddpg_target_q(r_val, baseline_b=0.01, next_q=0.25, gamma=1.0)
    assert abs(q_hat - (r_val - 0.01 + 0.25)) < 1e-12

    print(
        f"HAQ verification passed: bits=({b_low},{b_mid},{b_high}), "
        f"err_8bit={err_8bit:.6f} < err_2bit={err_2bit:.4f}, final_cost={final_cost:.1f}<={budget}, "
        f"dw_oi={dw_oi:.2f} << pw_oi={pw_oi:.2f}"
    )


if __name__ == "__main__":
    main()
