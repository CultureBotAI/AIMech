"""Original finite diagnostics; no author code or neural model is executed."""
import itertools
import json
import math


def calculate():
    # A masked affine sum with two independent p=.5 Bernoulli weights.
    sums = [2 * a - b for a, b in itertools.product([0, 1], repeat=2)]
    mean = sum(sums) / 4
    variance = sum((x - mean) ** 2 for x in sums) / 4
    assert mean == 0.5 and variance == 1.25
    mean_relu = sum(max(0, x) for x in sums) / 4
    relu_mean = max(0, mean)
    assert mean_relu == 0.75 and relu_mean == 0.5
    # One residual block: shared input1, residual-2, survival.5.
    stochastic_outputs = [max(0, 1 + active * -2) for active in [0, 1]]
    ensemble = sum(stochastic_outputs) / 2
    scaled = max(0, 1 + 0.5 * -2)
    assert ensemble == 0.5 and scaled == 0
    # Linear survival schedule for four blocks ending at.5.
    probabilities = [1 - (index / 4) * 0.5 for index in range(1, 5)]
    assert sum(probabilities) == (3 * 4 - 1) / 4
    # Generic Zoneout: h0=1, transition h->h^2+1, preserve probability.5.
    first_states = [1, 2]
    second_states = [previous if preserve else previous**2 + 1
                     for previous in first_states for preserve in [True, False]]
    exact_second_mean = sum(second_states) / 4
    deterministic_first = 1.5
    deterministic_second = 0.5 * deterministic_first + 0.5 * (
        deterministic_first**2 + 1)
    assert exact_second_mean == 2.5 and deterministic_second == 2.375
    # Feasible LSTM gates: c_prev=1, f=.25, i=.5, g=-.5, o=.5.
    # Preserve the cell but update the hidden state: raw cell proposal is0.
    return {
        "dropconnect": {
            "masked_sums": sums, "mean": mean, "variance": variance,
            "mean_relu": mean_relu, "relu_mean": relu_mean,
            "equally_likely_masks": 4, "each_mask_probability": 0.25,
            "interpretation": "Moment identities hold; nonlinearity prevents interchanging activation and expectation.",
        },
        "stochastic_depth": {
            "mean_stochastic_block_output": ensemble,
            "survival_scaled_block_output": scaled,
            "survival_probabilities": probabilities,
            "expected_active_blocks": sum(probabilities),
            "negative_skip_after_relu": max(0, -1),
            "interpretation": "Scaled inference need not equal the stochastic prediction mean; ReLU is identity only on nonnegative values.",
        },
        "zoneout": {
            "exact_two_step_state_mean": exact_second_mean,
            "local_expectation_two_step_state": deterministic_second,
            "printed_lstm_hidden_from_unzoned_cell": 0.5 * math.tanh(0),
            "alternative_hidden_from_preserved_cell": 0.5 * math.tanh(1),
            "interpretation": "Averaging masks locally differs from full trajectory expectation; choosing the cell used for the hidden proposal matters.",
        },
    }


if __name__ == "__main__":
    print(json.dumps(calculate(), indent=2))
