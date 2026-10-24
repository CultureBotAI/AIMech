"""Independent small CKK-style arithmetic check; not the author's implementation."""
import itertools
import json


def kk(values):
    values = sorted(values, reverse=True)
    while len(values) > 1:
        values = sorted([values[0]-values[1], *values[2:]], reverse=True)
    return values[0]


def ckk(values, node_budget=None):
    initial = kk(values)
    best = initial
    history = [initial]
    nodes = 0
    cut_short = False
    parity_bound = sum(values) % 2

    def visit(state):
        nonlocal best, nodes, cut_short
        if best == parity_bound:
            return
        if node_budget is not None and nodes >= node_budget:
            cut_short = True
            return
        nodes += 1
        state = sorted(state, reverse=True)
        largest, rest = state[0], sum(state[1:])
        # Largest-minus-rest is a lower bound; when nonnegative it is attainable.
        if largest >= rest:
            candidate = largest-rest
            if candidate < best:
                best = candidate
                history.append(best)
            return
        a, b, *tail = state
        visit([a-b, *tail])
        visit([a+b, *tail])

    visit(list(values))
    assert all(a > b for a, b in zip(history, history[1:]))
    return dict(initial_kk=initial, residue=best, incumbent_history=history,
                nodes=nodes, certified=(best == parity_bound or not cut_short))


def optimum(values):
    return min(abs(values[0] + sum(s*v for s, v in zip(signs, values[1:])))
               for signs in itertools.product((-1, 1), repeat=len(values)-1))


fixtures = [(8, 7, 6, 5, 4), (73, 40, 30, 20, 13, 6, 3), (5, 5, 5, 5),
            (0, 0, 0), (9,), (10, 3, 2), (3, 2, 2), (4, 3, 3, 2),
            (13, 11, 9, 7, 5), (12, 9, 8, 7, 5, 4)]
results = []
for values in fixtures:
    result = ckk(values)
    assert result['certified'] and result['residue'] == optimum(values)
    results.append(dict(values=values, **result))
limited = ckk(fixtures[0], node_budget=1)
assert limited['residue'] == 2 and not limited['certified']
assert results[0]['incumbent_history'] == [2, 0]
# The lower bound and its attainment in a dominant state are checked separately.
assert optimum((15, 6, 5, 4)) == 15-(6+5+4) == 0
assert optimum((10, 3, 2)) == 10-(3+2) == 5
print(json.dumps(dict(scope='Ten constructed fixtures, exhaustive sign enumeration, and one one-node-budget boundary; no timing or empirical replication.', results=results, interrupted=limited), indent=2))
