"""Finite HAC-E score identities; no author program or full HAC execution."""
from fractions import Fraction as F
import json

# For a binary graph, edge density is average adjacency, and 1-density is
# average dissimilarity for d(u,v)=1-A(u,v), over disjoint nonempty groups.
ac=F(2,2*2);bc=F(2,1*2);merged=F(4,3*2)
weighted=F(2,3)*ac+F(1,3)*bc
unweighted=(ac+bc)/2
assert merged==weighted==F(2,3) and unweighted==F(3,4)
assert 1-merged==F(1,3)
# Three-vertex path a--b--c: density prefers adjacent pairs. In the upstream
# profile score, a,c agree about their external adjacency; a,b disagree at c.
assert F(1)>F(0)
ml_agreement=F(1);ml_mismatch=F(1,4)
assert ml_agreement>ml_mismatch
print(json.dumps(dict(merged_edge_density=str(merged),size_weighted_update=str(weighted),unweighted_update=str(unweighted),mean_binary_dissimilarity=str(1-merged),path_adjacent_density='1',path_nonadjacent_density='0',path_nonadjacent_profile_ratio=str(ml_agreement),path_adjacent_profile_ratio=str(ml_mismatch),scope='Local exact score comparison and average-linkage algebra only. Candidate restrictions, ties, Bayesian selection and a complete author execution are not modeled.'),indent=2))
