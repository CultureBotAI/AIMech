"""Chosen graph/GRU algebra; not author code or a trained graph model."""
from fractions import Fraction as F
from itertools import permutations
from math import exp, isclose, tanh
import json


def sigmoid(x):
    return 1 / (1 + exp(-x))


def step(hidden, edges):
    incoming = [0.0] * len(hidden)
    outgoing = [0.0] * len(hidden)
    for sender, receiver, edge_type in edges:
        incoming[receiver] += [0.2, -0.3][edge_type] * hidden[sender]
        outgoing[sender] += [0.4, 0.1][edge_type] * hidden[receiver]
    result = []
    for h, a, b in zip(hidden, incoming, outgoing):
        z = sigmoid(a + b + 0.1 * h)
        r = sigmoid(0.2 * a - b)
        candidate = tanh(a + b + 0.5 * r * h)
        result.append((1 - z) * h + z * candidate)
    return result


hidden = [0.2, -0.4, 0.7]
edges = [(0, 1, 0), (1, 2, 1)]
output = step(hidden, edges)
for order in permutations(range(3)):
    inverse = {old: new for new, old in enumerate(order)}
    relabeled_edges = [(inverse[s], inverse[r], t) for s, r, t in edges]
    got = step([hidden[i] for i in order], relabeled_edges)
    assert all(isclose(a, output[i], abs_tol=1e-12) for a, i in zip(got, order))
assert step(hidden, list(reversed(edges))) == output
assert step(hidden, [(r, s, t) for s, r, t in edges]) != output
assert step(output, edges) != output  # One finite update need not be a fixed point.

# Reset-before and reset-after projection do not commute in general.
u = [[F(1), F(2)], [F(3), F(4)]]
h = [F(2), F(5)]
r = [F(1, 4), F(3, 4)]
before = [sum(w * gate * x for w, gate, x in zip(row, r, h)) for row in u]
after = [gate * sum(w * x for w, x in zip(row, h)) for gate, row in zip(r, u)]
assert before == [F(8), F(33, 2)] and after == [F(3), F(39, 2)]
assert before != after
old, candidate, z = F(2), F(-1), F(1, 4)
assert (1-z)*old+z*candidate == F(5, 4)
assert z*old+(1-z)*candidate == F(-1, 4)

# Locality: changing node2 cannot affect node0 until two adjacency steps here.
changed = [hidden[0], hidden[1], 0.9]
one = step(changed, edges)
assert one[0] == output[0]
assert not isclose(step(one, edges)[0], step(output, edges)[0], abs_tol=1e-12)
assert sum([1, 3]) == sum([2, 2])
gates = [sigmoid(0)] * 3
assert sum(gates) == 1.5
global_output = tanh(sum(g * tanh(x) for g, x in zip(gates, output)))
for order in permutations(range(3)):
    value = tanh(sum(gates[i] * tanh(output[i]) for i in order))
    assert isclose(value, global_output, abs_tol=1e-12)
print(json.dumps(dict(node_output=output, node_relabelings=6, edge_order_invariance=True,
                     reversed_edges_change_result=True, reset_before=list(map(str, before)),
                     reset_after=list(map(str, after)), finite_step_not_fixed_point=True,
                     one_step_distant_change_absent=True, two_step_change_present=True,
                     independent_gate_sum=sum(gates), global_readout=global_output,
                     scope='Chosen tiny algebra only; no training, author-code audit, universal graph expressivity, convergence or benchmark claim.')))
