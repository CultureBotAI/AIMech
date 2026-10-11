"""Original finite arithmetic examples; not implementations or convergence proofs."""
from fractions import Fraction
import json

def calculate():
    # Same successor scores, different old-state backups in RTA* and LRTA*.
    scores = sorted([1 + 1, 1 + 2, 1 + 3])
    assert scores[:2] == [2, 3]
    # Admissible but inconsistent estimate: true costs n=4, neighbor=3.
    old_h, neighbor_h, edge = 3, 0, 1
    backup = edge + neighbor_h
    assert old_h <= 4 and neighbor_h <= 3 and backup == 1 < old_h
    # A single-state lift cannot increase a different state's cost.
    costs = {'current': 1, 'neighbor': 2, 'goal': 0}
    raised = dict(costs); raised['current'] += 1
    assert raised['neighbor'] == 2 and raised['goal'] == 0
    # Positive increments can sum to a bounded amount. A cost initially 0
    # lifted by 2^-k remains below its fixed neighbor cost 2 forever.
    prefix = sum((Fraction(1, 2**k) for k in range(1, 21)), Fraction())
    assert prefix == 1 - Fraction(1, 2**20) < 1 < 2
    return dict(successor_scores=scores, rta_backup=scores[1], lrta_backup=scores[0],
                admissible_inconsistent_case=dict(old=old_h, new=backup, true_cost=4),
                unit_fill_lift=raised,
                bounded_increment_prefix=str(prefix),
                bounded_increment_limit=1,
                interpretation='Finite substitutions distinguish backup rules and state-specific lifting. The geometric-series limit explains why merely positive increments do not establish unbounded lifting. No original solver or benchmark was run.')

if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
