"""Constructed memory/scoring boundaries, not a trained MemNN implementation."""
import json
memory=['a','b',None];params={'scale':2};before=params.copy();H=2;encoded='c';updated=[encoded if i==H else m for i,m in enumerate(memory)]
assert updated==['a','b','c'] and params==before and memory==['a','b',None]
# One-dimensional embedding projection with different query and support columns.
query={'a':1,'b':2};support={'a':4,'b':3}
score_ab=query['a']*support['b'];score_ba=query['b']*support['a'];assert score_ab==3 and score_ba==8
scores={'a':1,'b':3,'c':2};full=max(scores,key=scores.get);restricted=max(['a','c'],key=scores.get);assert full=='b' and restricted=='c'
# Chosen cyclic pairwise preferences show a generic strict tournament limitation.
beats={('b','a'),('c','b'),('a','c')}
def winner(order):
 w=order[0]
 for c in order[1:]:
  if (c,w) in beats:w=c
 return w
w1=winner(['a','b','c']);w2=winner(['a','c','b']);assert w1!=w2
print(json.dumps(dict(single_slot_update=updated,parameters_unchanged=params==before,role_conditioned_score_ab=score_ab,role_conditioned_score_ba=score_ba,global_max=full,restricted_candidate_max=restricted,chosen_pairwise_winners=[w1,w2],limits='Constructed generic examples only. The cyclic preferences are not claimed to be a fitted paper model; author code, training and empirical evaluation are not executed.'),indent=2))
