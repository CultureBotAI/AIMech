"""Original finite substitutions for IHSAT and the 1999 random-walk extensions.

Reuses the published Hoos F2 clauses to enumerate only three-step monotone
random-walk paths. This is not an implementation of a full author solver.
"""
from fractions import Fraction
import json


def satisfied(clause, state):
    return any(state[abs(v)-1] == (v > 0) for v in clause)


def calculate():
    scores = {'a': 2, 'b': 0, 'c': -1}
    last = {'a': 5, 'b': 1, 'c': 0}
    candidates = [v for v in scores if scores[v] >= 0]
    ihsat = min(candidates, key=last.get)
    hsat = max(scores, key=scores.get)
    assert ihsat == 'b' and hsat == 'a'
    negative = {'a': -1, 'b': -3}
    pool = [v for v in negative if negative[v] >= 0] or list(negative)
    downhill = min(pool, key=last.get)
    assert downhill == 'b' and negative[downhill] < max(negative.values())
    formula = [(-1, 2), (-2, 1), (-1, -2, -3), (1, 2), (-4, 3), (-5, 3)]
    target = (True, True, False, False, False)
    start = (True, True, True, True, True)
    assert all(satisfied(c, target) for c in formula)
    w = Fraction(1, 100)
    distribution = {start: Fraction(1)}
    for step in range(3):
        nxt = {}
        for state, mass in distribution.items():
            clauses = [c for c in formula if not satisfied(c, state)]
            for clause in clauses:
                for v in clause:
                    i = abs(v)-1
                    if state[i] == target[i]:
                        continue
                    changed = list(state); changed[i] = not changed[i]; changed = tuple(changed)
                    nxt[changed] = nxt.get(changed, Fraction()) + mass*w/len(clauses)/len(clause)
        distribution = nxt
    path_probability = distribution[target]
    assert path_probability == w**3/12
    one_step_y_probability = w/3
    epsilon = (w/Fraction(6*3))**5
    assert one_step_y_probability > 0 and epsilon > 0
    return dict(ihsat_nondecreasing_choice=ihsat, hsat_best_choice=hsat,
                ihsat_all_negative_choice=downhill,
                declared_walk_probability=str(w), first_step_y_probability=str(one_step_y_probability),
                three_random_step_monotone_path_probability=str(path_probability),
                conservative_five_step_success_lower_bound=str(epsilon),
                interpretation='The three-step probability counts only the two monotone all-random paths through y,z1,z2 to the known F2 model; other algorithm trajectories are omitted. The five-step value is the theorem’s conservative bound, not measured success or expected runtime. A per-step walk branch can expose y immediately, unlike the previously declared periodic phase. IHSAT can prefer a neutral or more-worsening older candidate.')


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
