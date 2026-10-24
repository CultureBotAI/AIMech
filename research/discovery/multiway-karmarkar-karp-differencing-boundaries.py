"""Indexed subpartition arithmetic on small fixtures, not author-code replication."""
import itertools
import json


def all_loads(values, k):
    states = {(0,)*k}
    for value in values:
        states = {tuple(sorted(s[i]+(value if i == j else 0) for i in range(k)))
                  for s in states for j in range(k)}
    return states


def multiway_kk(values, k):
    # Each item is (normalized load, tuple of original input indices).
    states = [[(v,(i,))]+[(0,()) for _ in range(k-1)] for i,v in enumerate(values)]
    trace = []
    while len(states) > 1:
        states.sort(key=lambda s:max(x[0] for x in s),reverse=True)
        left = sorted(states.pop(0),key=lambda x:x[0],reverse=True)
        right = sorted(states.pop(0),key=lambda x:x[0])
        merged = [(a+b,ia+ib) for (a,ia),(b,ib) in zip(left,right)]
        offset = min(x[0] for x in merged)
        merged = sorted([(v-offset,idx) for v,idx in merged],key=lambda x:x[0],reverse=True)
        trace.append([v for v,_ in merged])
        states.append(merged)
    final = states[0]
    bins = [idx for _,idx in final]
    assert sorted(i for idx in bins for i in idx) == list(range(len(values)))
    loads = [sum(values[i] for i in idx) for idx in bins]
    normalized = [v for v,_ in final]
    assert [v-min(loads) for v in loads] == normalized
    return dict(loads=loads,indices=bins,normalized=normalized,range=max(loads)-min(loads),trace=trace)


fixtures = [((8,7,6,5,4),3),((4,4,4,6,6,9),3),((5,5,5,5),3),
            ((0,0,0),3),((9,),3),((8,7,6,5,4),4),((2,2,2,3,3,5),3)]
results = []
for values,k in fixtures:
    result = multiway_kk(values,k)
    optimum = min(s[-1]-s[0] for s in all_loads(values,k))
    assert result['range'] >= optimum
    results.append(dict(values=values,k=k,optimum_range=optimum,**result))
assert sorted(results[0]['loads']) == [8,11,11]
assert results[0]['trace'] == [[8,7,0],[2,1,0],[5,4,0],[3,3,0]]
# A normalized zero can represent a nonempty subset, not an unused bin.
assert results[0]['normalized'][-1] == 0 and results[0]['indices'][-1]
assert results[-1]['range'] == 2 and results[-1]['optimum_range'] == 1
objective_loads = all_loads((4,4,4,6,6,9),3)
assert min(x[-1]-x[0] for x in objective_loads) == 3
assert (10,10,13) in objective_loads and (9,12,12) in objective_loads
assert min(x[-1] for x in objective_loads) == 12
print(json.dumps(dict(scope='Seven constructed indexed fixtures, exact arithmetic and exhaustive range comparison; no statistical experiment.',results=results),indent=2))
