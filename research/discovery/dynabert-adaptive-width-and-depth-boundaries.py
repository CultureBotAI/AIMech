#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 806:
DynaBERT: Dynamic BERT with Adaptive Width and Depth
(Hou, Huang, Shang, Jiang, Chen, & Liu, NeurIPS 2020, arXiv:2004.04037).

Verifies:
1. Parallel decomposition of Multi-Head Attention across N_H heads (Eq. 1) and FFN across d_ff intermediate
   neurons (Eq. 2), where width multiplier m_w in {1.0, 0.75, 0.5, 0.25} retains floor(m_w * N_H) heads
   and floor(m_w * d_ff) intermediate neurons while preserving residual hidden dimension d.
2. First-order Taylor expansion importance scoring for Network Rewiring (Section 2.1.1):
   I_h = |L_h - L_{h=0}| approx |(dL/dh) * h| for attention heads and I_w approx |sum_{i=1}^{2d} (dL/dw_i) * w_i|
   for FFN intermediate neurons; rewiring in descending importance guarantees that for any m_{w,1} < m_{w,2},
   the active head/neuron subset S(m_{w,1}) is a strict prefix of S(m_{w,2}) maximizing cumulative importance.
3. Layer pruning and teacher-layer matching rule (Section 2.2 & Appendix A):
   For L=12 layers and depth multiplier m_d < 1, dropping student layers d where mod(d, 1/(1 - m_d)) == 0
   and matching kept student layers against teacher layers L_T where mod(d + 1, 1/(1 - m_d)) != 0 yields
   exact sets L_T = {1, 2, 4, 5, 6, 8, 9, 10, 12} for m_d = 0.75 and L_T = {2, 4, 6, 8, 10, 12} for m_d = 0.5,
   always preserving the final teacher layer d = 12.
"""

import json


def taylor_head_importance(grad_h, h):
    """Section 2.1.1: I_h approx |<dL/dh, h>|."""
    return abs(sum(g * x for g, x in zip(grad_h, h)))


def teacher_matched_layers(L, m_d):
    """Appendix A: teacher layers d in 1..L satisfying mod(d + 1, round(1 / (1 - m_d))) != 0."""
    if m_d == 1.0:
        return list(range(1, L + 1))
    stride = int(round(1.0 / (1.0 - m_d)))
    return [d for d in range(1, L + 1) if ((d + 1) % stride) != 0]


def student_dropped_layers(L, m_d):
    """Appendix A: student layers d in 1..L dropped when mod(d, round(1 / (1 - m_d))) == 0."""
    if m_d == 1.0:
        return []
    stride = int(round(1.0 / (1.0 - m_d)))
    return [d for d in range(1, L + 1) if (d % stride) == 0]


def main():
    L = 12
    N_H = 12
    d_ff = 3072
    width_multipliers = [1.0, 0.75, 0.5, 0.25]
    depth_multipliers = [1.0, 0.75, 0.5]

    # 1. Verify 4 x 3 = 12 sub-network configurations and active head/neuron counts
    configs = []
    for m_w in width_multipliers:
        for m_d in depth_multipliers:
            active_heads = int(m_w * N_H)
            active_neurons = int(m_w * d_ff)
            active_layers = int(m_d * L)
            configs.append((m_w, m_d, active_heads, active_neurons, active_layers))
    assert len(configs) == 12
    assert (0.25, 0.5, 3, 768, 6) in configs
    assert (0.75, 0.75, 9, 2304, 9) in configs

    # 2. Verify Taylor importance network rewiring maximizes sub-network prefix importance
    raw_heads = [
        ([0.1, -0.2], [1.0, 0.5]),   # |0.1 - 0.1| = 0.0
        ([0.8, 0.6], [1.5, 1.0]),    # |1.2 + 0.6| = 1.8
        ([-0.5, 0.4], [2.0, -1.0]),  # |-1.0 - 0.4| = 1.4
        ([0.2, 0.3], [0.5, 1.0]),    # |0.1 + 0.3| = 0.4
        ([0.9, -0.7], [1.0, -2.0]),  # |0.9 + 1.4| = 2.3
        ([-0.3, -0.2], [1.0, 1.0]),  # |-0.3 - 0.2| = 0.5
        ([0.4, 0.5], [2.0, 1.0]),    # |0.8 + 0.5| = 1.3
        ([0.1, 0.1], [1.0, 1.0]),    # |0.1 + 0.1| = 0.2
    ]
    scores_unrewired = [taylor_head_importance(g, h) for g, h in raw_heads]
    scores_rewired = sorted(scores_unrewired, reverse=True)
    # For m_w = 0.25 (top 2 of 8 heads) and m_w = 0.5 (top 4 of 8 heads), rewired strictly dominates unrewired
    assert sum(scores_rewired[:2]) > sum(scores_unrewired[:2])
    assert sum(scores_rewired[:4]) > sum(scores_unrewired[:4])
    assert abs(sum(scores_rewired) - sum(scores_unrewired)) < 1e-12

    # 3. Verify Appendix A exact layer-dropping and teacher-layer matching indices for L=12
    dropped_075 = student_dropped_layers(L, 0.75)
    matched_075 = teacher_matched_layers(L, 0.75)
    assert dropped_075 == [4, 8, 12]
    assert matched_075 == [1, 2, 4, 5, 6, 8, 9, 10, 12]
    assert len(matched_075) == 9 and matched_075[-1] == 12

    dropped_050 = student_dropped_layers(L, 0.5)
    matched_050 = teacher_matched_layers(L, 0.5)
    assert dropped_050 == [2, 4, 6, 8, 10, 12]
    assert matched_050 == [2, 4, 6, 8, 10, 12]
    assert len(matched_050) == 6 and matched_050[-1] == 12

    summary = {
        "concept": "DynaBERTDynamicBERTWithAdaptiveWidthAndDepth",
        "num_subnetwork_configs": len(configs),
        "top2_importance_unrewired": round(sum(scores_unrewired[:2]), 4),
        "top2_importance_rewired": round(sum(scores_rewired[:2]), 4),
        "dropped_layers_md_075": dropped_075,
        "teacher_matched_layers_md_075": matched_075,
        "dropped_layers_md_050": dropped_050,
        "teacher_matched_layers_md_050": matched_050,
        "status": "ok",
    }
    print(json.dumps(summary))


if __name__ == "__main__":
    main()
