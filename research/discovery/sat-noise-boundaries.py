"""Original exact arithmetic examples; no source solver or benchmark execution."""
from fractions import Fraction
import json

def satisfied(clause, assignment):
    return any(assignment[abs(lit)] == (lit > 0) for lit in clause)

def counts(clauses, assignment, variable):
    after = dict(assignment); after[variable] = not after[variable]
    before = [satisfied(c, assignment) for c in clauses]
    later = [satisfied(c, after) for c in clauses]
    make = sum(not a and b for a, b in zip(before, later))
    brk = sum(a and not b for a, b in zip(before, later))
    return {'make': make, 'break': brk, 'gain': make - brk}

def calculate():
    # At all-false, only (a,b) and (a,c) are unsatisfied; d occurs in (-d).
    clauses = [(1, 2), (1, 3), (-4,)]
    assignment = dict.fromkeys(range(1, 5), False)
    unsat = [c for c in clauses if not satisfied(c, assignment)]
    eligible = sorted({abs(lit) for c in unsat for lit in c})
    focused = {v: Fraction(1, len(eligible)) for v in eligible}
    clause_first = {v: sum((Fraction(1, len(unsat) * len(c)) for c in unsat if v in c), Fraction()) for v in eligible}
    assert focused == {1: Fraction(1, 3), 2: Fraction(1, 3), 3: Fraction(1, 3)}
    assert clause_first == {1: Fraction(1, 2), 2: Fraction(1, 4), 3: Fraction(1, 4)}
    assert counts(clauses, assignment, 4)['gain'] == -1
    # Break-only and net-gain rankings can differ within selected clause (a,b).
    other = [(1, 2), (2, 3), (2, 4), (2, 5), (-1,), (-2,), (-2, 6)]
    zero = dict.fromkeys(range(1, 7), False)
    scores = {v: counts(other, zero, v) for v in (1, 2)}
    assert scores == {1: {'make': 1, 'break': 1, 'gain': 0}, 2: {'make': 4, 'break': 2, 'gain': 2}}
    # A freebie is chosen before the noise coin, including p=1.
    freebie = [(1, 2), (-2,)]
    freebie_scores = {v: counts(freebie, {1: False, 2: False}, v) for v in (1, 2)}
    assert freebie_scores[1]['break'] == 0 < freebie_scores[2]['break']
    return dict(focused_probabilities={str(v): str(p) for v, p in focused.items()},
                pure_clause_first_probabilities={str(v): str(p) for v, p in clause_first.items()},
                unrestricted_noise_probability_for_d='1/4',
                break_vs_gain=scores, freebie_scores=freebie_scores,
                interpretation='These finite CNF substitutions distinguish variable-union sampling, clause-first sampling, unrestricted noise, break-only ranking and zero-break priority. Pure clause-first sampling is not asserted to be SKC at p=1 because freebies override its coin.')

if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
