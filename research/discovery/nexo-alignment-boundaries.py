"""Finite first-pass alignment example; not complete AlignOntology execution."""
from fractions import Fraction as F
import json

# Two sibling terms per ontology below a common, already matched root U.
# Direct gene annotations can fill root U={0,1,2,3,4}; no sibling is an ancestor.
x=[{0},{1,2}];y=[{0,1},{0,3,4}]
m=[[F(len(a&b),len(a|b)) for b in y] for a in x]
assert m==[[F(1,2),F(1,3)],[F(1,3),F(0)]]
# Unique top pair fixes (0,0); the remaining zero pair is below threshold .01.
greedy=m[0][0];alternative=m[0][1]+m[1][0]
assert greedy==F(1,2) and alternative==F(2,3)>greedy
# The alternative remains one-to-one, with no reversed ancestor relationship.
assert all(not(a<=b or b<=a) for a,b in (x,y))
# First pass uses intrinsic similarity only; later passes mix in relational scores.
assert F(3,4)*F(1,2)+F(1,4)*F(1)==F(5,8)
# A recurrence test accepting any old mapping need not imply adjacent equality.
sequence=['A','B','A'];assert sequence[-1] in sequence[:-1] and sequence[-1]!=sequence[-2]
print(json.dumps(dict(jaccard_matrix=[[str(v) for v in row] for row in m],greedy_first_pass_score=str(greedy),admissible_alternative_score=str(alternative),mixed_score_example='5/8',nonadjacent_mapping_recurrence_example=sequence,scope='The Jaccard sibling example assesses a single greedy k=0 pass. It does not show an actual later-iteration cycle or the behavior of uninspected author code. Empty-neighborhood conventions remain unspecified.'),indent=2))
