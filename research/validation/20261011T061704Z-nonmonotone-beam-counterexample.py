"""Curator toy counterexample, not an execution of the authors' implementation."""
import json,heapq,hashlib
from collections import Counter
from pathlib import Path
from datetime import datetime,timezone
nodes={'root':(0,0),'a':(1,-1),'b':(1,-2),'ac':(2,1),'ad':(2,0),'be':(2,10),'bf':(2,-10),'ac/EOS':(3,-5),'ad/EOS':(3,-6),'be/EOS':(3,10),'bf/EOS':(3,-10)}
succ={'root':['a','b'],'a':['ac','ad'],'b':['be','bf'],'ac':['ac/EOS'],'ad':['ad/EOS'],'be':['be/EOS'],'bf':['bf/EOS']}
k=2
def best_completion(n):
 return max((best_completion(x) for x in succ.get(n,[])),default=nodes[n][1])
def beam():
 current=['root'];trace=[]
 while any(n in succ for n in current):
  current=sorted([x for n in current for x in succ.get(n,[n])],key=lambda n:(-nodes[n][1],n))[:k];trace.append(current)
 return current[0],trace
def best_first_with_bound():
 queue=[(0,0,'root')];pops=Counter();trace=[];incumbent=None
 while queue:
  if incumbent is not None and all(nodes[incumbent][1]>=best_completion(n) for _,_,n in queue):
   trace.append({'action':'bounded-stop','incumbent':incumbent,'remaining':[n for _,_,n in queue]});break
  _,depth,n=heapq.heappop(queue)
  if pops[depth]>=k:
   trace.append({'action':'skip-per-length-budget','node':n,'score':nodes[n][1]});continue
  pops[depth]+=1;trace.append({'action':'accept','node':n,'score':nodes[n][1]})
  if n.endswith('/EOS'):
   if incumbent is None or nodes[n][1]>nodes[incumbent][1]:incumbent=n
  else:
   for x in succ[n]:heapq.heappush(queue,(-nodes[x][1],nodes[x][0],x))
 return incumbent,trace
a,at=beam();b,bt=best_first_with_bound();assert a=='be/EOS' and b=='ac/EOS'
out={'created_at':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),'source_context':'Meister et al., TACL 2020 Algorithm 2 per-length pop budget and Section 4.1 Equation 6 stop-only extension to nonmonotone scores; also present in arXiv v5 (2022).','authorship':'Curator-authored finite-tree illustration; not an audit or execution of the authors implementation.','beam_width':k,'nodes':nodes,'successors':succ,'upper_bound':'Exact best descendant completion score for every remaining hypothesis; equivalent to score+U.','layer_beam':{'result':a,'score':nodes[a][1],'trace':at},'best_first_stop_only':{'result':b,'score':nodes[b][1],'trace':bt},'interpretation':'Changing only stopping does not restore the comparison guarantee for arbitrary nonmonotone scores when a per-length budget can prune an as-yet-unexpanded superior hypothesis. This toy analysis does not challenge the monotone-score method.','limits':['This implementation specializes a finite depth-three tree and stores complete hypotheses as incumbents instead of repeated EOS padding.','The optional monotonicity-based older-layer deletion is deliberately not used; the per-length limit alone produces the discrepancy.','All complete paths have the same length, ties do not determine the result, and successor-score increments can represent an additively decomposable nonprobabilistic scoring function.','A primary correction or stronger nonmonotonic algorithm could add conditions or change pruning; that remains a separate evidence check.'],'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(out,indent=2))
