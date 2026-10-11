"""Original finite examples of reading boundaries; no author code or benchmark."""
import json
from fractions import Fraction

def calculate():
    # A two-variable inequality CSP: simultaneous best replies can oscillate.
    reply = lambda other: 1 - other
    state = (0, 0)
    synchronous = (reply(state[1]), reply(state[0]))
    next_sync = (reply(synchronous[1]), reply(synchronous[0]))
    first = reply(state[1])
    sequential = (first, reply(first))
    assert synchronous == (1, 1) and next_sync == state
    assert sequential == (1, 0)
    # At the atmost bound, all participating values in an already counted
    # variable share the max-over-that-variable output term in Equation9.
    active_values = [1, 0]
    per_variable_output = 1 - max(active_values)
    assert per_variable_output == 0 and 1 - active_values[1] == 1
    # Literal EGLS aspiration does not decide equal augmented costs.
    aspiration = lambda new_g, best_g, new_h, old_h: new_g < best_g and new_h > old_h
    assert aspiration(8, 9, 13, 12)
    assert not aspiration(8, 9, 12, 12)
    # GGA weights sum shared counters only for exhibited features involving
    # a gene, so different chromosomes can receive different templates.
    penalties = [2, 1]
    feature_positions = [{0, 1}, {1}]
    def template(present):
        return [sum(penalties[i] for i in present if q in feature_positions[i]) for q in range(2)]
    a, b = template([0]), template([1])
    assert a == [2, 2] and b == [0, 1]
    p_parent_a_gene1 = Fraction(b[1], a[1] + b[1])
    assert p_parent_a_gene1 == Fraction(1, 3)
    # The published rule has no normalizable distribution at zero total.
    zero_total = sum([0, 0])
    assert zero_total == 0 and not list(range(zero_total))
    return dict(genet=dict(synchronous_cycle=[state, synchronous, next_sync],sequential_solution=sequential,atmost_variable_output=per_variable_output),egls=dict(strict_aspiration=True,equality_decided_by_aspiration=False),gga=dict(templates=[a,b],lighter_parent_b_probability_gene1=str(1-p_parent_a_gene1),zero_total_rule='undefined in displayed rule; no fallback inferred'))

if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
