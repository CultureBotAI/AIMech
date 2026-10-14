"""Finite printed-predicate checks for CliXO, not author implementation execution."""
from itertools import combinations,product
from fractions import Fraction
import json
# All maximal cliques of a complete three-partite graph with two vertices per part.
parts=((0,1),(2,3),(4,5));cliques={frozenset(t) for t in product(*parts)}
pairs={c:{frozenset(p) for p in combinations(c,2)} for c in cliques}
necessary={c for c in cliques if any(sum(pair in pairs[d] for d in cliques)==1 for pair in pairs[c])}
assert len(cliques)==8 and not necessary
# A complete k-clique minus one edge has two maximal (k-1)-cliques.
k=5;V=frozenset(range(k));missing=frozenset([0,1]);edges={frozenset(p) for p in combinations(V,2)}-{missing}
subsets=[frozenset(s) for n in range(1,k+1) for s in combinations(V,n)]
complete=[s for s in subsets if all(frozenset(p) in edges for p in combinations(s,2))]
maximal=[s for s in complete if not any(s<t for t in complete)]
assert len(maximal)==2 and all(len(s)==k-1 for s in maximal) and len(maximal[0]&maximal[1])==k-2
mindegree=min(Fraction(sum(frozenset([a,c]) in edges for c in V if c!=a),len(V)-1) for a in V)
assert mindegree==Fraction(3,4)
# The literal strict threshold test does not admit a new maximum-threshold clique.
maximum_distance=Fraction(2);threshold=maximum_distance;alpha=Fraction(0)
assert not maximum_distance < threshold-alpha
# One root with two leaves is feasible under the printed imperfect scaling.
# Its root-to-leaf edges have length2; the leaf-to-leaf path therefore has length4.
input_distance=Fraction(1);root_height=2*input_distance;pair_distance=2*root_height
assert root_height==2*input_distance and pair_distance>=input_distance
assert pair_distance==4 and pair_distance!=input_distance
# No outside terminal or second nonterminal exists: witness comparisons are vacuous.
print(json.dumps(dict(imperfect_example_input_distance=str(input_distance),imperfect_example_root_height=str(root_height),imperfect_example_pair_distance=str(pair_distance),imperfect_example_satisfies_lower_bound=True,current_maximal_cliques=8,necessary_under_simultaneous_full_pool_predicate=len(necessary),single_missing_edge_clique_sizes=[len(s) for s in maximal],intersection_size=k-2,minimum_normalized_degree=str(mindegree),new_last_threshold_clique_passes_strict_alpha_zero=False,scope='Static exact source-predicate checks. No assertion about uninspected implementation ordering, terminal flushing, or general theorem correctness.'),indent=2))
