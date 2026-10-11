"""Original finite bookkeeping and transition examples, not author solver runs."""
from fractions import Fraction
from itertools import product
import json

def sat(clause, assignment):
    return any(assignment[abs(lit) - 1] == (lit > 0) for lit in clause)

def calculate():
    # Current assignment controls weighting; a retained older assignment differs.
    clauses = [(1,), (-1,), (2,), (-2,)]
    current, retained = (False, False), (True, False)
    current_weights = [1 + (not sat(c, current)) for c in clauses]
    retained_weights = [1 + (not sat(c, retained)) for c in clauses]
    assert current_weights == [2, 1, 2, 1]
    assert retained_weights == [1, 2, 2, 1]
    # Averaging preserves agreement; discrepant positions are randomized.
    left, right = (0, 1, 0), (0, 0, 1)
    agreements = {i: a for i, (a, b) in enumerate(zip(left, right)) if a == b}
    disagreements = [i for i, (a, b) in enumerate(zip(left, right)) if a != b]
    assert agreements == {0: 0} and disagreements == [1, 2]
    # A two-variable satisfiable 2-CNF with a positive finite-budget miss chance.
    formula = [(1, 2), (-1, 2), (1, -2)]
    states = list(product([False, True], repeat=2))
    solutions = [s for s in states if all(sat(c, s) for c in formula)]
    assert solutions == [(True, True)]
    distribution = {(False, False): Fraction(1)}
    misses = []
    for step in range(1, 9):
        nxt = {}
        for state, probability in distribution.items():
            unsat = [c for c in formula if not sat(c, state)]
            if not unsat:
                nxt[state] = nxt.get(state, Fraction()) + probability
                continue
            clause = unsat[0]  # Declared first-unsatisfied clause selection.
            for literal in clause:
                changed = list(state); changed[abs(literal) - 1] = not changed[abs(literal) - 1]
                changed = tuple(changed)
                nxt[changed] = nxt.get(changed, Fraction()) + probability / len(clause)
        distribution = nxt
        if step % 2 == 0:
            miss = 1 - distribution.get((True, True), 0)
            assert miss == Fraction(1, 2**(step // 2))
            misses.append(dict(flips=step, miss_probability=str(miss)))
    return dict(current_assignment_weights=current_weights, retained_assignment_weights=retained_weights,
                averaging_agreements=agreements, averaging_disagreements=disagreements,
                finite_2sat_misses=misses,
                interpretation='The finite 2-CNF starts at a fixed assignment, chooses the first unsatisfied clause and samples its two literals uniformly. This exact small transition calculation is not a general runtime proof. Clause weights distinguish the current assignment from a hypothetical retained assignment; averaging does not require arithmetic real-valued variables.')

if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
