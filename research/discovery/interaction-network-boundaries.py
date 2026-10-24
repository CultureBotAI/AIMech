"""Constructed graph aggregation examples; not a trained Interaction Network."""
from itertools import permutations
import json


def forward(objects, external, edges):
    effects = [2 * objects[receiver] + 3 * objects[sender] + attribute
               for sender, receiver, attribute in edges]
    pooled = [sum(effect for effect, edge in zip(effects, edges) if edge[1] == j)
              for j in range(len(objects))]
    return effects, pooled, [o + x + e for o, x, e in zip(objects, external, pooled)]


objects = [1, 4, 7]
external = [0, 1, 2]
edges = [(0, 1, 2), (2, 1, 5), (0, 2, 1), (0, 1, 2)]
effects, pooled, output = forward(objects, external, edges)
assert effects == [13, 34, 18, 13] and pooled == [0, 60, 18] and output == [1, 65, 27]
for order in permutations(range(len(edges))):
    assert forward(objects, external, [edges[i] for i in order])[2] == output
for order in permutations(range(3)):
    inverse = {old: new for new, old in enumerate(order)}
    relabeled = [(inverse[s], inverse[r], a) for s, r, a in edges]
    assert forward([objects[i] for i in order], [external[i] for i in order], relabeled)[2] == [output[i] for i in order]
without_duplicate = forward(objects, external, edges[:-1])[2]
reversed_output = forward(objects, external, [(r, s, a) for s, r, a in edges])[2]
shifted = forward([x + 10 for x in objects], external, edges)[2]
assert without_duplicate == [1, 52, 27] and reversed_output != output
assert shifted != output
assert sum([1, 3]) == sum([2, 2])  # Aggregation is not injective.
counts = [dict(objects=n, complete_directed_edges=n * (n - 1), bidirectional_chain_edges=2 * (n - 1)) for n in [3, 6, 12]]
print(json.dumps(dict(effects=effects, receiver_sums=pooled, object_outputs=output,
                     without_duplicate=without_duplicate, reversed_edges=reversed_output,
                     shifted_absolute_features=shifted, edge_orderings_checked=24,
                     node_permutations_checked=6, sum_collision=[[1, 3], [2, 2]],
                     relation_call_counts=counts,
                     scope='Tiny chosen linear functions verify routing and algebra only; no author code, learned physical model, runtime benchmark or universal generalization proof.')))
