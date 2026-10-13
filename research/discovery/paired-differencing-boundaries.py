"""Fixed differencing-round examples with indexed reconstruction; no benchmark."""
import itertools
import json


def difference(a,b):
    if a[0]<b[0]:
        a,b = b,a
    return (a[0]-b[0],a[1]+b[2],a[2]+b[1])


def solve(values,mode):
    states = [(v,(i,),()) for i,v in enumerate(values)]
    trace = []
    while len(states)>1:
        states.sort(key=lambda x:x[0],reverse=True)
        if mode=='paired':
            combined = [difference(states[i],states[i+1]) for i in range(0,len(states)-1,2)]
            if len(states)%2:
                combined.append(states[-1])
            states = combined
        elif mode=='largest':
            states = states[2:]+[difference(states[0],states[1])]
        else:
            raise ValueError(mode)
        trace.append([x[0] for x in states])
    value,positive,negative = states[0]
    assert sorted(positive+negative)==list(range(len(values)))
    loads = [sum(values[i] for i in ids) for ids in [positive,negative]]
    assert loads[0]-loads[1]==value
    return dict(residue=value,indices=[positive,negative],loads=loads,
                cardinality_difference=abs(len(positive)-len(negative)),trace=trace)


def balanced_optimum(values):
    n = len(values)
    total = sum(values)
    return min(abs(total-2*sum(values[i] for i in ids))
               for ids in itertools.combinations(range(n),n//2))


fixtures = [(8,7,6,5,4),(100,10,9,8),(9,8,7,6,5,4,3),(5,5,5,5),
            (0,0,0),(9,),(7,7),(1,2,3,4,5,6,7,8)]
results = []
for values in fixtures:
    paired = solve(values,'paired')
    assert paired['cardinality_difference']==len(values)%2
    optimum = balanced_optimum(values)
    assert paired['residue']>=optimum
    assert solve(tuple(7*x for x in values),'paired')['residue']==7*paired['residue']
    results.append(dict(values=values,balanced_optimum=optimum,**paired))
assert results[0]['residue']==2 and results[0]['balanced_optimum']==0
largest = solve((100,10,9,8),'largest')
assert largest['residue']==73 and largest['cardinality_difference']==2
assert results[1]['residue']==89 and results[1]['cardinality_difference']==0
print(json.dumps(dict(scope='Eight fixed integer fixtures, one largest-versus-paired comparison and positive scaling; no average-case replication.',results=results,largest_comparison=largest),indent=2))
