"""Finite curator calculations; no author implementation or benchmark is run."""
import json
import math


def calculate():
    # Two stochastic pulls are not replaced by a deterministic midpoint pull.
    x, v, personal, shared = 0.0, 0.0, -1.0, 1.0
    next_v = v + 2 * 0.25 * (personal - x) + 2 * 0.75 * (shared - x)
    midpoint = (personal + shared) / 2
    assert next_v == 1 and midpoint - x == 0
    # A collapsed swarm can remain fixed away from the quadratic's optimum.
    stuck = 2.0
    fixed_v = 0 + 2 * 0.2 * (stuck - stuck) + 2 * 0.7 * (stuck - stuck)
    assert fixed_v == 0 and stuck**2 > 0
    # Remembered bests do not constrain each subsequent particle's cost.
    next_x = 1 + (2 + 2 * 0.5 * (1 - 1) + 2 * 0.25 * (0 - 1))
    assert next_x == 2.5 and next_x**2 > 1**2 > 0**2
    hot, cold = math.exp(-2 / 2), math.exp(-2 / 1)
    assert 0 < cold < hot < 1
    # Equal energy, asymmetric proposal: accepting everything is not uniform.
    q01, q10 = 0.9, 0.1
    uncorrected_stationary = [q10 / (q01 + q10), q01 / (q01 + q10)]
    corrected01, corrected10 = q01 * min(1, q10 / q01), q10 * min(1, q01 / q10)
    assert math.isclose(corrected01, corrected10)
    assert uncorrected_stationary != [0.5, 0.5]
    # Source Eq20 is one-indexed ceil((1-rho)*N), followed by inclusive selection.
    scores, rho = [0, 1, 2, 3], 0.25
    threshold = sorted(scores)[math.ceil((1 - rho) * len(scores)) - 1]
    elite_indices = [i for i, value in enumerate(scores) if value >= threshold]
    assert threshold == 2 and elite_indices == [2, 3]
    bits = [[1, 0], [1, 1]]
    fitted = [sum(row[j] for row in bits) / len(bits) for j in range(2)]
    smoothed = [0.5 * value + 0.5 * 0.5 for value in fitted]
    assert fitted == [1, 0.5] and smoothed == [0.75, 0.5]
    # Bernoulli fit to all-zero elites loses support for the better state one.
    collapsed_probability_one = sum([0, 0]) / 2
    assert collapsed_probability_one == 0
    return {
        "pso_two_pull_velocity": next_v,
        "pso_midpoint_displacement": midpoint - x,
        "pso_fixed_nonoptimal_position": stuck,
        "pso_overshoot_position": next_x,
        "annealing_uphill_probability_T2": hot,
        "annealing_uphill_probability_T1": cold,
        "equal_energy_uncorrected_stationary": uncorrected_stationary,
        "corrected_offdiagonal_probabilities": [corrected01, corrected10],
        "ce_threshold": threshold,
        "ce_elite_indices": elite_indices,
        "ce_bernoulli_fit": fitted,
        "ce_smoothed_fit": smoothed,
        "ce_collapsed_probability_one": collapsed_probability_one,
    }


if __name__ == "__main__":
    print(json.dumps(calculate(), indent=2))
