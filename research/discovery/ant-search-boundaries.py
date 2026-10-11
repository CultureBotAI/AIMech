"""Finite curator calculations, not an author implementation or benchmark."""
from math import isclose
import json

def calculate():
    # Ant-cycle: rho denotes retention; deposits come from all completed tours.
    old, rho, q = 2.0, 0.8, 1.0
    deposits = q / 4 + q / 8
    ant_cycle = rho * old + deposits
    wrong_convention = (1 - rho) * old + deposits
    assert isclose(ant_cycle, 1.975) and not isclose(ant_cycle, wrong_convention)
    # Equal trails, unequal inverse-distance weights: still not uniform or greedy.
    weights = [1.0, 0.5]
    probabilities = [w / sum(weights) for w in weights]
    assert all(0 < p < 1 for p in probabilities) and probabilities[0] != probabilities[1]
    # ACS's local rule can increase a below-baseline trail.
    trail, baseline, local_rate = 0.1, 0.5, 0.2
    local = (1 - local_rate) * trail + local_rate * baseline
    assert isclose(local, 0.18) and local > trail
    # Repeated visits imply repeated updates, not one update per distinct edge.
    twice = (1 - local_rate) * local + local_rate * baseline
    assert isclose(twice, 0.244) and not isclose(twice, local)
    outside_best, global_rate = 0.8, 0.2
    outside_after_global = outside_best
    all_edge_alternative = (1 - global_rate) * outside_best
    assert not isclose(outside_after_global, all_edge_alternative)
    # A positive trail does not rescue an excluded candidate or zero heuristic.
    positive_trails = [1.0, 1.0]
    eligible = [True, False]
    support = [t if allowed else 0.0 for t, allowed in zip(positive_trails, eligible)]
    assert support[1] == 0
    zero_heuristic_weights = [positive_trails[0] * 1.0, positive_trails[1] * 0.0]
    assert zero_heuristic_weights[1] == 0
    # MMAS lower-limit heuristic: fixed average branching ignores actual weights.
    n, p_best, upper = 10, 0.05, 2.0
    p_dec, avg = p_best ** (1 / n), n / 2
    lower = upper * (1 - p_dec) / ((avg - 1) * p_dec)
    simplified_decision = upper / (upper + (avg - 1) * lower)
    assert isclose(simplified_decision ** n, p_best)
    exponent_two_decision = upper**2 / (upper**2 + (avg - 1) * lower**2)
    assert not isclose(exponent_two_decision ** n, p_best)
    altered_decision = upper / (upper + (avg - 1) * lower * 2)
    assert not isclose(altered_decision ** n, p_best)
    assert upper * (1 - 1.0) / ((avg - 1) * 1.0) == 0
    # Bounded changing recurrence does not by itself imply convergence.
    # Fixed bounds [.1, 2] do not clip this two-cycle with rho=.5 and deposits 1,0.
    low, high = 2 / 3, 4 / 3
    assert isclose(0.5 * low + 1, high)
    assert isclose(0.5 * high + 0, low)
    assert 0.1 < low < high < 2
    return dict(ant_cycle=ant_cycle, mistaken_evaporation_convention=wrong_convention,
                unequal_initial_probabilities=probabilities,
                acs_local_increase=local, acs_two_local_updates=twice,
                acs_off_best_unchanged=outside_after_global,
                all_edge_evaporation_alternative=all_edge_alternative,
                excluded_candidate_weight=support[1], zero_heuristic_weight=zero_heuristic_weights[1],
                mmas_heuristic_lower=lower, simplified_tour_probability=simplified_decision ** n,
                exponent_two_probability=exponent_two_decision ** n,
                changed_heuristic_probability=altered_decision ** n,
                bounded_recurrence_two_cycle=[low, high])

if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
