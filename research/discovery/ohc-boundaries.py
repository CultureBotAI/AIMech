"""Finite OHC predicate boundaries; not an author implementation or runtime test."""
from fractions import Fraction
from itertools import combinations
import json

def density(vertices, edges):
    if len(vertices) == 1:
        return Fraction(1)
    count = sum(frozenset(p) in edges for p in combinations(vertices, 2))
    return Fraction(2 * count, len(vertices) * (len(vertices) - 1))

edges = {frozenset(p) for p in [(0,1),(0,2),(1,2),(0,3),(1,3)]}
base = frozenset([0,1])
separate = [base | {2}, base | {3}]
joint = base | {2,3}
assert density(base, edges) == density(separate[0], edges) == density(separate[1], edges) == 1
assert density(joint, edges) == Fraction(5,6)
# Both outside vertices have the same maximal number (two) of links to base.
assert [sum(frozenset([p,q]) in edges for q in base) for p in [2,3]] == [2,2]
assert abs(density(joint, edges)-density(base, edges)) > 0
# A two-vertex connected graph has three nonempty connected induced subsets.
all_connected_subsets = [{0},{1},{0,1}]
new_cluster = {0,1}
retained = [s for s in all_connected_subsets if not s < new_cluster]
assert retained == [new_cluster]
# At distance equal to a threshold, <= admits the edge while < rejects it.
assert (1 <= 1) and not (1 < 1)
print(json.dumps(dict(singleton_density='1',base_density='1',separate_extension_density=['1','1'],joint_tied_extension_density=str(density(joint,edges)),joint_extension_allowed_at_lambda_zero=False,connected_subsets=3,retained_after_subset_removal=1,scope='Static exact predicate examples only. No claim that the tied state is reached by a complete OHC run, no complete implementation or theorem certification.'),indent=2))
