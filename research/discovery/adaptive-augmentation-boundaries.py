"""Original finite arithmetic for source conventions; no author code is executed."""

import json
import math


def calculate():
    view_probabilities = ((0.9, 0.2), (0.4, 0.8))
    losses = [[-math.log(p) for p in view] for view in view_probabilities]
    mean_ce = sum(map(sum, losses)) / 4
    concatenated_losses = [value for view in losses for value in view]
    batch_global_minimum = min(concatenated_losses)
    logged_minus_loss = -batch_global_minimum / 2
    best_view_ce = sum(min(v[i] for v in losses) for i in range(2)) / 2
    average_view_correctness = sum(p > 0.5 for v in view_probabilities for p in v) / 4
    any_view_correctness = sum(any(v[i] > 0.5 for v in view_probabilities) for i in range(2)) / 2
    assert -logged_minus_loss < best_view_ce < mean_ce
    assert any_view_correctness > average_view_correctness
    # Positive log minimization favors a smaller probability of the designated class.
    positive_logs = [math.log(p) for p in (0.9, 0.1)]
    negative_logs = [-x for x in positive_logs]
    assert positive_logs[1] < positive_logs[0] and negative_logs[1] > negative_logs[0]
    alpha, delta, epsilon = 0.2, 0.5, 0.6
    gamma = alpha + delta * epsilon
    previous = (0.3, 0.7)
    recursive = [gamma * x for x in previous] + [1 - gamma]
    assert min(recursive) >= 0 and math.isclose(sum(recursive), 1)
    # The PBA count is a cap: every probability test fails when all probabilities are zero.
    pba_no_application_probability = 0.2 + 0.8 * 0.9**30
    assert pba_no_application_probability > 0.2
    return {
        "faa": {"mean_view_ce": mean_ce, "best_view_ce": best_view_ce,
                "batch_global_minimum": batch_global_minimum, "logged_minus_loss_for_one_batch_of_two": logged_minus_loss,
                "mean_view_correctness": average_view_correctness, "any_view_correctness": any_view_correctness},
        "ada": {"probabilities": [0.9, 0.1], "printed_positive_log": positive_logs,
                "negative_log": negative_logs, "gamma": gamma, "recursive_weights": recursive},
        "pba": {"probability_zero_cap": 0.2,
                "probability_no_application_with_30_independent_probability_0_1_entries": pba_no_application_probability,
                "probability_no_application_with_all_probabilities_zero": 1.0},
    }


if __name__ == "__main__":
    print(json.dumps(calculate(), indent=2))
