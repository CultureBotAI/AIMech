"""Finite curator counterexamples; no author implementation or model execution."""
import json
import math


def calculate():
    x, y = 0.25, 0.6
    weights = [(1-x)*(1-y), x*(1-y), (1-x)*y, x*y]
    pixels = [1.0, 2.0, 3.0, 5.0]
    output = sum(w*v for w, v in zip(weights, pixels))
    eps = 1e-6
    perturbed = pixels.copy()
    perturbed[0] += eps
    derivative = (sum(w*v for w, v in zip(weights, perturbed))-output)/eps
    assert math.isclose(derivative, weights[0], abs_tol=1e-8)
    assert not math.isclose(derivative, sum(weights))
    ramp_at_offset = [p + 0.5 for p in [0.0, 1.0]]
    nearest_before = math.floor(x + 0.5)
    nearest_after = math.floor(x + eps + 0.5)
    assert nearest_before == nearest_after
    # A spatial permutation cannot exchange two channels: total channel activity
    # differs even when the spatial arrangement can be rotated arbitrarily.
    original_channels = [[1, 0], [0, 0]]
    transformed_channels = [[0, 0], [0, 1]]
    assert list(map(sum, original_channels)) != list(map(sum, transformed_channels))
    input_value, trunk, mask = 1.0, 3.0, 0.2
    residual_attention = (1+mask)*trunk
    input_skip_variant = input_value+mask*trunk
    assert not math.isclose(residual_attention, input_skip_variant)
    values = [2.0, -1.0]
    scores = [2*v for v in values]
    raw_weights = [s/len(values) for s in scores]
    softmax_weights = [math.exp(s-max(scores)) for s in scores]
    total = sum(softmax_weights)
    softmax_weights = [w/total for w in softmax_weights]
    raw_output = sum(w*v for w, v in zip(raw_weights, values))
    softmax_output = sum(w*v for w, v in zip(softmax_weights, values))
    assert raw_output > max(values)
    assert min(values) <= softmax_output <= max(values)
    return {
        'spatial_sampler': {'bilinear_weights': weights, 'output': output,
                            'input_element_derivative': derivative,
                            'sum_of_all_weights': sum(weights),
                            'source_ramp_samples_at_positive_half_pixel_offset': ramp_at_offset,
                            'nearest_neighbor_local_difference': nearest_after-nearest_before,
                            'interpretation': 'A fixed input element has its own coefficient; target coordinates select source samples; nearest sampling can have zero local coordinate response.'},
        'channel_alignment': {'original_channel_sums': list(map(sum, original_channels)),
                              'transformed_channel_sums': list(map(sum, transformed_channels)),
                              'interpretation': 'A shared spatial permutation cannot restore changed channel identities; this is a finite example, not the full general invariance theorem.'},
        'residual_attention': {'one_plus_mask_times_trunk': residual_attention,
                               'input_plus_mask_times_trunk': input_skip_variant,
                               'zero_mask_output': trunk,
                               'fixed_mask_trunk_derivative': 1+mask,
                               'interpretation': 'The skip preserves trunk features and does not suppress a fixed-mask trunk gradient below one.'},
        'nonlocal': {'raw_dot_weights': raw_weights, 'softmax_weights': softmax_weights,
                     'raw_dot_aggregate': raw_output, 'softmax_aggregate': softmax_output,
                     'zero_scale_nonzero_offset_branch': 0.5,
                     'interpretation': 'Count-normalized raw dot products need not be probabilities or convex averages; zero normalization scale alone does not cancel a nonzero offset.'}}


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
