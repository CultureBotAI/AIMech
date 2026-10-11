"""Finite curator examples. No author implementation or performance benchmark."""
import itertools
import json

def calculate():
    # Binary constraints x=y and x!=z, with y=z=0: both x values tie.
    conflicts = {x: int(x != 0) + int(x == 0) for x in [0, 1]}
    assert conflicts == {0: 1, 1: 1}
    # Morris's counterexample: one all-positive clause and all directed
    # implications between four Boolean variables. Only all-true satisfies.
    pairs = list(itertools.permutations(range(4), 2))
    def violated(state):
        return [not any(state)] + [bool(state[i] and not state[j]) for i, j in pairs]
    states = list(itertools.product([0, 1], repeat=4))
    solutions = [s for s in states if not any(violated(s))]
    assert solutions == [(1, 1, 1, 1)]
    weights = [1] * 13
    current = (0, 0, 0, 0)
    visited = {current}
    boosts = 0
    def cost(s):
        return sum(w for w, v in zip(weights, violated(s)) if v)
    for _ in range(1000):
        if not any(violated(current)):
            break
        improving = []
        for i in range(4):
            n = list(current)
            n[i] = 1 - n[i]
            n = tuple(n)
            if cost(n) < cost(current):
                improving.append(n)
        if improving:
            current = improving[0]
            visited.add(current)
        else:
            weights = [w + int(v) for w, v in zip(weights, violated(current))]
            boosts += 1
    assert all(sum(s) <= 1 for s in visited)
    assert not any(s in solutions for s in visited)
    # This finite prefix does not itself prove the author's infinite-cycle claim.
    # GSAT Figure1 checks before each flip. One unit clause x, initially false,
    # with one try and one flip reaches true after the last check.
    t = False
    returned = None
    for _ in range(1):
        if t:
            returned = t
            break
        t = not t
    assert returned is None and t is True
    return dict(min_conflicts=dict(value_conflicts=conflicts,current_value_is_eligible=True),breakout=dict(unique_solution=solutions[0],iterations=1000,boosts=boosts,visited_states=sorted(visited),scope='Finite first-improvement prefix of the published counterexample, not an independent infinite-run proof.'),gsat=dict(literal_pre_flip_check_return=returned,final_assignment_satisfies=t,meaning='A post-final-flip solution check is an implementation convention absent from Figure1. Failure does not certify UNSAT.'))

if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
