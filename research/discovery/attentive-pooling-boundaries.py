"""Finite attentive-pooling examples on fixed encoded columns, not word sequences."""
import json,math
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def softmax(xs):
 ws=[math.exp(x-max(xs)) for x in xs];return [w/sum(ws) for w in ws]
def pool(q,a,u):
 g=[[math.tanh(dot(x,[dot(row,y) for row in u])) for y in a] for x in q]
 wq=softmax([max(row) for row in g]);wa=softmax([max(row[j] for row in g) for j in range(len(a))])
 rq=[sum(w*x[k] for w,x in zip(wq,q)) for k in range(len(q[0]))]
 ra=[sum(w*x[k] for w,x in zip(wa,a)) for k in range(len(a[0]))]
 score=dot(rq,ra)/(math.sqrt(dot(rq,rq))*math.sqrt(dot(ra,ra)))
 assert max(wq)/min(wq)<=math.exp(2) and max(wa)/min(wa)<=math.exp(2)
 return dict(question=rq,answer=ra,score=score,question_weights=wq,answer_weights=wa)
q=[[1.,0.],[0.,2.]];a=[[1.,1.],[2.,0.],[0.,1.]];u=[[1.,2.],[-.5,1.]]
base=pool(q,a,u);permuted=pool(q[::-1],a[::-1],u)
assert all(math.isclose(x,y) for k in ['question','answer'] for x,y in zip(base[k],permuted[k]))
swapped=pool(a,q,u);assert not math.isclose(base['score'],swapped['score'])
duplicate=pool(q+[q[0]],a,u);assert any(not math.isclose(x,y) for x,y in zip(base['question'],duplicate['question']))
changed_answer=pool(q,[[0.,1.],[0.,2.]],u);assert any(not math.isclose(x,y) for x,y in zip(base['question'],changed_answer['question']))
print(json.dumps(dict(base=base,paired_column_permutation_equal=True,swapped_pair_score=swapped['score'],duplicate_question_read=duplicate['question'],question_read_for_changed_answer=changed_answer['question'],unscaled_tanh_weight_ratio_bound=math.exp(2),limits='Nonempty chosen vectors with nonzero cosine norms; no encoder, training, max-tie gradient convention or empirical evaluation.'),indent=2))
