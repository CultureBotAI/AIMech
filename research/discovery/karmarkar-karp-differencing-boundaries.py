"""Constructed exact-integer examples; no timing or author-code replication."""
import heapq
import itertools
import json


def kk(values):
    # Preserve input indices and a binary expression tree, including equal values.
    heap = [(-v, i, i) for i, v in enumerate(values)]
    heapq.heapify(heap)
    serial = len(values)
    trace = [sorted(values, reverse=True)]
    while len(heap) > 1:
        neg_a, _, a = heapq.heappop(heap)
        neg_b, _, b = heapq.heappop(heap)
        heapq.heappush(heap, (neg_a - neg_b, serial, (a, b)))
        serial += 1
        trace.append(sorted((-x[0] for x in heap), reverse=True))
    signs = [0] * len(values)

    def reconstruct(tree, sign):
        if isinstance(tree, int):
            signs[tree] = sign
        else:
            reconstruct(tree[0], sign)
            reconstruct(tree[1], -sign)

    reconstruct(heap[0][2], 1)
    residue = -heap[0][0]
    assert all(s in (-1, 1) for s in signs)
    assert sum(v*s for v, s in zip(values, signs)) == residue
    return dict(residue=residue, signs=signs, trace=trace)


def optimum(values):
    return min(abs(values[0] + sum(s*v for s, v in zip(signs, values[1:])))
               for signs in itertools.product((-1, 1), repeat=len(values)-1))


cases = [(8, 7, 6, 5, 4), (73, 40, 30, 20, 13, 6, 3), (5, 5, 5, 5),
         (0, 0, 0), (9,), (10, 3, 2), (3, 2, 2), (4, 3, 3, 2)]
results = []
for values in cases:
    result = kk(values)
    exact = optimum(values)
    assert result['residue'] >= exact
    results.append(dict(values=values, exhaustive_optimum=exact, **result))
assert results[0]['residue'] == 2 and results[0]['exhaustive_optimum'] == 0
assert results[1]['residue'] == 1
assert results[2]['residue'] == results[3]['residue'] == 0
assert kk(tuple(7*v for v in cases[0]))['residue'] == 14
print(json.dumps(dict(scope='Eight constructed exact-integer fixtures and one scale check; not a statistical performance experiment.', results=results), indent=2))
