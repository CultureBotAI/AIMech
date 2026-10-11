"""Finite curator examples of gating boundaries; no model or author code execution."""
import json
import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def channel_gate(features):
    # Shared identity/relu/identity MLP on positive average and maximum descriptors.
    gates = [sigmoid(max(sum(row) / len(row), 0) + max(max(row), 0))
             for row in features]
    return [[v * gates[c] for v in row] for c, row in enumerate(features)]


def spatial_gate(features):
    # Center-only weights on average and maximum maps are a valid sparse setting
    # of a spatial convolution. This is a finite illustration, not a trained CBAM.
    columns = list(zip(*features))
    gates = [sigmoid(sum(col) / len(col) + max(col)) for col in columns]
    return [[v * gates[j] for j, v in enumerate(row)] for row in features]


def calculate():
    se_gates = [sigmoid(0)] * 3
    assert sum(se_gates) == 1.5
    features = [[1.0, 3.0], [2.0, -1.0]]
    channel_first = spatial_gate(channel_gate(features))
    spatial_first = channel_gate(spatial_gate(features))
    difference = max(abs(a - b) for ra, rb in zip(channel_first, spatial_first)
                     for a, b in zip(ra, rb))
    assert difference > 0.001
    assert all(abs(out) <= abs(original) for row, source in zip(channel_first, features)
               for out, original in zip(row, source))
    channel_logit, spatial_logit = 2.0, -1.0
    sum_gate = sigmoid(channel_logit + spatial_logit)
    product_gate = sigmoid(channel_logit * spatial_logit)
    assert not math.isclose(sum_gate, product_gate)
    assert 1 < 1 + sum_gate < 2 and 1 < 1 + product_gate < 2
    return {
        'se': {'zero_logit_channel_gates': se_gates, 'gate_sum': sum(se_gates),
               'interpretation': 'Independent sigmoid gates are not a normalized channel distribution.'},
        'cbam_order': {'channel_then_spatial': channel_first,
                       'spatial_then_channel': spatial_first,
                       'largest_absolute_difference': difference,
                       'interpretation': 'Input-dependent stages need not commute; immediate gate products attenuate magnitudes.'},
        'bam_fusion': {'channel_logit': channel_logit, 'spatial_logit': spatial_logit,
                       'paper_sum_gate': sum_gate, 'pinned_code_product_gate': product_gate,
                       'paper_residual_multiplier': 1 + sum_gate,
                       'code_residual_multiplier': 1 + product_gate,
                       'interpretation': 'SUM and product fusion differ; both residual multipliers exceed one for finite logits.'}}


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
