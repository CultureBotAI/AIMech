"""Finite curator calculations, not author software or a historical crawl."""
from fractions import Fraction as F
import json

priors=[F(1,4),F(3,4)];likelihoods=[F(1,2),F(1,2)]
literal=[p*l/sum(likelihoods) for p,l in zip(priors,likelihoods)]
bayes=[p*l/sum(x*y for x,y in zip(priors,likelihoods)) for p,l in zip(priors,likelihoods)]
assert literal==[F(1,8),F(3,8)] and sum(literal)==F(1,2)
assert bayes==priors and sum(bayes)==1
# A good internal taxonomy topic has two leaves, neither the maximum leaf.
leaf={'good-a':F(3,10),'good-b':F(3,10),'other':F(2,5)}
hard=max(leaf,key=leaf.get).startswith('good');soft=sum(v for k,v in leaf.items() if k.startswith('good'))
assert not hard and soft==F(3,5)
frontier=[('tried-high',1,F(9,10)),('new-low',0,F(1,10))]
ordered=sorted(frontier,key=lambda x:(x[1],-x[2]));assert ordered[0][0]=='new-low'
assert max(F(1,4),F(3,4))==F(3,4)
# Explicit eligibility mask and inter-site edges; no claim to simulate the paper's quantile selection.
r={'low-hub':F(1,5),'high-hub':F(4,5),'same-site':F(1),'good-authority':F(9,10),'bad-authority':F(1,10)}
site={'low-hub':'L','high-hub':'H','same-site':'A','good-authority':'A','bad-authority':'B'}
edges=[(u,v) for u in ['low-hub','high-hub','same-site'] for v in ['good-authority','bad-authority']]
allowed=[(u,v) for u,v in edges if site[u]!=site[v] and v=='good-authority']
a={v:sum(r[v] for u,w in allowed if w==v) for v in ['good-authority','bad-authority']}
h={u:sum(r[u]*a[v] for w,v in allowed if w==u) for u in ['low-hub','high-hub','same-site']}
assert a=={'good-authority':F(9,5),'bad-authority':0}
assert h=={'low-hub':F(9,25),'high-hub':F(36,25),'same-site':0}
assert h['high-hub']/h['low-hub']==4
out=dict(probability_equation=dict(literal=list(map(str,literal)),literal_sum=str(sum(literal)),normalized_bayes=list(map(str,bayes))),hard_versus_soft=dict(hard_expands=hard,soft_relevance=str(soft)),frontier_order=[x[0] for x in ordered],parent_priority_max='3/4',weighted_link_step=dict(allowed_edges=allowed,raw_authorities={k:str(v) for k,v in a.items()},raw_hubs={k:str(v) for k,v in h.items()},hub_ratio='4'),limits='Exact finite arithmetic on constructed inputs. Common positive norm scaling preserves the displayed ratios; this is not a convergence proof, classifier training, author-code conformance test or historical benchmark.')
print(json.dumps(out,indent=2))
