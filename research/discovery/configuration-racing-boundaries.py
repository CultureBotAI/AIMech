"""Original finite examples; not an implementation of any author's algorithm."""
import json
from statistics import mean


def calculate():
    # Nonnegative run costs: the partial sum / full N is a lower bound.
    n, bound, observed, cutoff = 100, 0.1, 11, 100
    lower_bound = observed / n
    assert lower_bound > bound
    remaining_allowance = n * bound - 4
    printed_max = max(cutoff, remaining_allowance)
    shortening_min = min(cutoff, remaining_allowance)
    assert printed_max == 100 and shortening_min == 6
    # A literal <= first-acceptable loop can alternate on a two-node plateau.
    costs = {'a': 1, 'b': 1}
    state, trace = 'a', ['a']
    for _ in range(4):
        neighbor = 'b' if state == 'a' else 'a'
        if costs[neighbor] <= costs[state]:
            state = neighbor
        trace.append(state)
    assert trace == ['a', 'b', 'a', 'b', 'a']
    # Common-prefix comparison reverses the misleading unequal-prefix ranking.
    longer, shorter = [10, 1], [6]
    assert mean(longer) < mean(shorter) < mean(longer[:len(shorter)])
    # Rank sums and raw means are different objectives, without simulating a test.
    a, b = [0, 0, 100], [1, 1, 2]
    a_ranks = [1 if x < y else 2 for x, y in zip(a, b)]
    b_ranks = [3 - v for v in a_ranks]
    assert sum(a_ranks) < sum(b_ranks) and mean(a) > mean(b)
    return {
        'nonnegative_cost_lower_bound': {'partial_sum': observed, 'N': n, 'lower_bound': lower_bound, 'comparison_bound': bound},
        'printed_capping_max_vs_shortening': {'cutoff': cutoff, 'remaining_allowance': remaining_allowance, 'printed_max': printed_max, 'shortening_min': shortening_min},
        'non_strict_plateau_trace': trace,
        'blocked_comparison': {'longer_all_mean': mean(longer), 'longer_common_prefix_mean': mean(longer[:len(shorter)]), 'shorter_mean': mean(shorter)},
        'ranks_vs_means': {'a_rank_sum': sum(a_ranks), 'b_rank_sum': sum(b_ranks), 'a_mean': mean(a), 'b_mean': mean(b)},
        'scope': 'Finite arithmetic and control-flow counterexamples only; no statistical significance test, author code, model or benchmark was executed.'
    }


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
