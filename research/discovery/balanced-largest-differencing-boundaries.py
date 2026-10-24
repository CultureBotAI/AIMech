"""Fixed indexed balanced-largest differencing examples; no empirical benchmark."""
import itertools
import json


def difference(a,b):
    if a[0]<b[0]:
        a,b = b,a
    return (a[0]-b[0],a[1]+b[2],a[2]+b[1])


def paired_round(states):
    states = sorted(states,key=lambda x:x[0],reverse=True)
    out = [difference(states[i],states[i+1]) for i in range(0,len(states)-1,2)]
    return out+([states[-1]] if len(states)%2 else [])


def solve(values,mode='balanced-largest'):
    states = [(v,(i,),()) for i,v in enumerate(values)]
    states = paired_round(states)
    first = [x[0] for x in states]
    trace = [first]
    while len(states)>1:
        if mode=='paired':
            states = paired_round(states)
        else:
            states.sort(key=lambda x:x[0],reverse=True)
            states = states[2:]+[difference(states[0],states[1])]
        trace.append([x[0] for x in states])
    residual,positive,negative = states[0]
    assert sorted(positive+negative)==list(range(len(values)))
    loads = [sum(values[i] for i in ids) for ids in [positive,negative]]
    assert loads[0]-loads[1]==residual
    assert abs(len(positive)-len(negative))==len(values)%2
    return dict(residue=residual,indices=[positive,negative],loads=loads,
                cardinality_difference=abs(len(positive)-len(negative)),first_round=first,trace=trace)


def optimum(values):
    total = sum(values)
    return min(abs(total-2*sum(values[i] for i in ids))
               for ids in itertools.combinations(range(len(values)),len(values)//2))


fixtures = [(8,7,6,5,4),(200,100,90,80,70,61,50,42),(100,10,9,8),
            (9,8,7,6,5,4,3),(5,5,5,5),(0,0,0),(9,),(7,7)]
results = []
for values in fixtures:
    result = solve(values)
    best = optimum(values)
    assert result['residue']>=best
    assert solve(tuple(7*v for v in values))['residue']==7*result['residue']
    results.append(dict(values=values,balanced_optimum=best,**result))
assert results[0]['residue']==2 and results[0]['balanced_optimum']==0
paired = solve(fixtures[1],'paired')
assert results[1]['first_round']==[100,10,9,8]
assert results[1]['residue']==73 and paired['residue']==89
print(json.dumps(dict(scope='Eight fixed integer fixtures and positive scaling; no probabilistic or hardware replication.',results=results,paired_comparison=paired),indent=2))
