"""Small exact-integer range-minimization examples; no performance benchmark."""
import itertools
import json
from fractions import Fraction


def score(loads):
    return max(loads)-min(loads)


def all_loads(values, k):
    states = {(0,)*k}
    for value in values:
        states = {tuple(sorted(s[i]+(value if i == j else 0) for i in range(k)))
                  for s in states for j in range(k)}
    return states


def greedy(values, k):
    loads = [0]*k
    for value in sorted(values, reverse=True):
        j = min(range(k), key=lambda i: loads[i])
        loads[j] += value
    return tuple(sorted(loads))


def cga(values, k, budget=None):
    values = sorted(values, reverse=True)
    best = score(greedy(values, k))
    history = [best]
    nodes = 0
    cut_short = False
    theoretical = int(sum(values) % k != 0)

    def visit(i, loads):
        nonlocal best, nodes, cut_short
        if best == theoretical:
            return
        if budget is not None and nodes >= budget:
            cut_short = True
            return
        nodes += 1
        remaining = sum(values[i:])
        # Source bound on the minimum achievable range, not a makespan bound.
        bound = max(Fraction(0), max(loads)-Fraction(sum(loads)-max(loads)+remaining, k-1))
        if bound >= best:
            return
        if i == len(values):
            candidate = score(loads)
            if candidate < best:
                best = candidate
                history.append(best)
            return
        seen = set()
        for j in sorted(range(k), key=lambda j: loads[j]):
            if loads[j] in seen:
                continue
            seen.add(loads[j])
            child = list(loads)
            child[j] += values[i]
            visit(i+1, tuple(child))

    visit(0, (0,)*k)
    assert all(a > b for a, b in zip(history, history[1:]))
    return dict(best_range=best, incumbent_history=history, nodes=nodes,
                certified=(best == theoretical or not cut_short))


fixtures = [((8,7,6,5,4),2), ((8,7,6,5,4),3), ((4,4,4,6,6,9),3),
            ((5,5,5,5),3), ((0,0,0),3), ((9,),3), ((10,3,2),2), ((3,2,2),2)]
results = []
for values, k in fixtures:
    exact = min(map(score, all_loads(values,k)))
    result = cga(values,k)
    assert result['certified'] and result['best_range'] == exact
    results.append(dict(values=values,k=k,greedy_loads=greedy(values,k),**result))
limited = cga((8,7,6,5,4),2,budget=1)
assert limited['best_range'] == 4 and not limited['certified']
values = (4,4,4,6,6,9)
loads = all_loads(values,3)
assert min(map(score,loads)) == 3
assert (10,10,13) in loads and score((10,10,13)) == 3
assert (9,12,12) in loads and min(map(max,loads)) == 12
# A partial-load average bound can be strictly optimistic for indivisible weights.
assert Fraction(10)-Fraction(0+0+4,2) == 8
completions = [(10+4,0,0),(10,4,0),(10,0,4)]
assert min(map(score,completions)) == 10
print(json.dumps(dict(scope='Eight fixed integer fixtures, one interruption and two objective/bound counterexamples; not an empirical experiment.',results=results,interrupted=limited,range_vs_makespan=dict(values=values,minimum_range=3,range_optimal_loads=[10,10,13],minimum_makespan=12,makespan_optimal_loads=[9,12,12]),optimistic_bound=dict(partial_loads=[10,0,0],remaining=[4],bound=8,attainable_minimum_range=10)),indent=2))
