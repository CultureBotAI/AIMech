"""Finite rule substitutions and a recomputation of Hoos1999's F2 counterexample.

No author solver or benchmark is executed. The finite enumeration supports the
stated boundaries; the general incompleteness result remains the paper's theorem.
"""
from fractions import Fraction
from itertools import product
import json


def satisfied(clause, assignment):
    return any(assignment[abs(v) - 1] == (v > 0) for v in clause)


def calculate():
    gains = {'a': 3, 'b': 3, 'c': 1}
    last_flip = {'a': 5, 'b': 2, 'c': 0}
    best = [v for v in gains if gains[v] == max(gains.values())]
    hsat_choice = min(best, key=last_flip.get)
    assert hsat_choice == 'b' and min(last_flip, key=last_flip.get) == 'c'
    # Fixed-order tie between never-flipped variables, not a random tie.
    never_flipped_order = ['b', 'a']
    assert min(['a', 'b'], key=never_flipped_order.index) == 'b'
    # Novelty orders clause candidates by post-flip cost, then oldest age.
    costs = {'a': 2, 'b': 2, 'c': 5}
    ages = {'a': 10, 'b': 2, 'c': 8}
    ordered = sorted(costs, key=lambda v: (costs[v], ages[v]))
    assert ordered == ['b', 'a', 'c']
    assert ordered[0] != max(ages, key=ages.get)
    # Thus the best b is chosen for every p in this example.
    def second_probability(p, gap):
        assert 0 <= p <= 1 and gap >= 1
        if p < Fraction(1, 2):
            return 2 * p if gap == 1 else Fraction(0)
        return Fraction(1) if gap == 1 else 2 * (p - Fraction(1, 2))
    rows = []
    for p in [Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]:
        for gap in [1, 2]:
            rows.append(dict(p=str(p), gap=gap, second_probability=str(second_probability(p, gap))))
    assert [r['second_probability'] for r in rows] == ['1/2', '0', '1', '0', '1', '1/2']
    # Hoos1999 F2: variables x1,x2,y,z1,z2 in that order.
    formula = [(-1, 2), (-2, 1), (-1, -2, -3), (1, 2), (-4, 3), (-5, 3)]
    models = [s for s in product([False, True], repeat=5) if all(satisfied(c, s) for c in formula)]
    assert models == [(True, True, False, False, False)]
    trap_rows = []
    for x1, x2 in product([False, True], repeat=2):
        state = (x1, x2, True, True, True)
        unsatisfied = [i for i, c in enumerate(formula) if not satisfied(c, state)]
        assert len(unsatisfied) == 1
        candidates = {abs(v) for v in formula[unsatisfied[0]]}
        scores = {}
        for v in candidates:
            changed = list(state); changed[v - 1] = not changed[v - 1]
            scores[v] = 1 - sum(not satisfied(c, changed) for c in formula)
        assert scores[1] == scores[2] == 0
        if 3 in scores:
            assert scores[3] == -1 and x1 and x2
        trap_rows.append(dict(x1=x1, x2=x2, unsatisfied_clause=unsatisfied[0]+1, gains=scores))
    # Starting at x1=x2=True before step1, every ordinary move flips x1 or x2.
    # Before each even-numbered step, their parity is odd; c3 cannot be selected.
    # A periodic override on step100 therefore also sees only x1/x2 candidates.
    assert 100 % 2 == 0
    return dict(hsat_choice=hsat_choice, novelty_tie_order=ordered,
                rnovelty_recent_best_cases=rows, hoos_f2_model=models[0],
                hoos_f2_trap_scores=trap_rows,
                periodic_step_observation='Every100th step is even. From the declared phase, x1/x2 parity prevents the three-literal c3 from being the unsatisfied clause on those steps. Periodic random choice therefore need not expose y; a positive per-step random-walk probability changes that premise.')


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
