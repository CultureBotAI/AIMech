"""Indexed complete balanced/constrained differencing on fixed small integers."""
import itertools
import json


def initial(values):
    return sorted([(v,1,(i,),()) for i,v in enumerate(values)],key=lambda x:x[0],reverse=True)


def combine(a,b,subtract):
    assert a[0]>=b[0]
    if subtract:
        return (a[0]-b[0],a[1]-b[1],a[2]+b[3],a[3]+b[2])
    return (a[0]+b[0],a[1]+b[1],a[2]+b[2],a[3]+b[3])


def first_round(values):
    s = initial(values)
    return [combine(s[i],s[i+1],True) for i in range(0,len(s)-1,2)]+([s[-1]] if len(s)%2 else [])


def bldm(values):
    s = first_round(values)
    while len(s)>1:
        s.sort(key=lambda x:x[0],reverse=True)
        s = s[2:]+[combine(s[0],s[1],True)]
    return s[0]


def unpack(state,values):
    v,m,positive,negative = state
    assert sorted(positive+negative)==list(range(len(values)))
    loads = [sum(values[i] for i in ids) for ids in [positive,negative]]
    assert loads[0]-loads[1]==v and len(positive)-len(negative)==m
    return dict(residue=v,cardinality_difference=abs(m),signed_cardinality=m,
                indices=[positive,negative],loads=loads)


def complete(values,target=None,budget=None,restrict_first_round=False):
    n = len(values)
    target = n%2 if target is None else target
    assert n>0 and all(isinstance(v,int) and v>=0 for v in values)
    assert 0<=target<=n and target%2==n%2
    solution = bldm(values) if target==n%2 else None
    best = solution[0] if solution is not None else float('inf')
    history = [best] if solution is not None else []
    nodes = 0
    cut_short = False
    first_phase_limit = (n+1)//2

    def visit(states):
        nonlocal best,solution,nodes,cut_short
        if best==sum(values)%2:
            return
        if budget is not None and nodes>=budget:
            cut_short = True
            return
        nodes += 1
        for v,m,pos,neg in states:
            assert v==sum(values[i] for i in pos)-sum(values[i] for i in neg)
            assert m==len(pos)-len(neg)
        if len(states)==1:
            v,m,_,_ = states[0]
            if abs(m)==target and v<best:
                best = v
                solution = states[0]
                history.append(v)
            return
        total = sum(x[0] for x in states)
        maximum = max(x[0] for x in states)
        if max(0,2*maximum-total)>=best:
            return
        magnitudes = [abs(x[1]) for x in states]
        count_total = sum(magnitudes)
        if max(0,2*max(magnitudes)-count_total)>target or count_total<target:
            return
        if len(states)<=first_phase_limit:
            states = sorted(states,key=lambda x:x[0],reverse=True)
        a,b = states[:2]
        for subtract in [True,False]:
            visit(states[2:]+[combine(a,b,subtract)])

    visit(first_round(values) if restrict_first_round else initial(values))
    assert solution is not None
    assert all(a>b for a,b in zip(history,history[1:]))
    result = unpack(solution,values)
    assert result['cardinality_difference']==target
    return dict(**result,target=target,nodes=nodes,incumbent_history=history,
                certified_for_searched_tree=(best==sum(values)%2 or not cut_short))


def exact(values,target):
    count = (len(values)-target)//2
    return min(abs(sum(values)-2*sum(values[i] for i in ids))
               for ids in itertools.combinations(range(len(values)),count))


fixtures = [(8,7,6,5,4),(200,100,90,80,70,61,50,42),(100,10,9,8),
            (9,8,7,6,5,4,3),(5,5,5,5),(0,0,0),(9,),(7,7)]
results = []
for values in fixtures:
    for target in range(len(values)%2,len(values)+1,2):
        result = complete(values,target)
        assert result['certified_for_searched_tree'] and result['residue']==exact(values,target)
        results.append(dict(values=values,**result))
limited = complete(fixtures[0],budget=1)
assert limited['residue']==2 and not limited['certified_for_searched_tree']
restricted = complete(fixtures[0],restrict_first_round=True)
assert restricted['residue']==2 and exact(fixtures[0],1)==0
# Necessary magnitude bounds do not imply feasibility, even with matching parity.
magnitudes = [2,2,2]
assert max(0,2*max(magnitudes)-sum(magnitudes))==0
attainable = sorted({abs(sum(a*s for a,s in zip(magnitudes,signs)))
                     for signs in itertools.product([-1,1],repeat=3)})
assert attainable==[2,6] and 0 not in attainable
print(json.dumps(dict(scope='Eight fixed integer instances, all valid absolute cardinality targets, one-node interruption and two incompleteness boundaries; not author-code or performance replication.',tested_targets=len(results),results=results,interrupted=limited,restricted_initial_pairs=dict(best_residue=restricted['residue'],global_balanced_optimum=0),necessary_only_cardinality_bound=dict(magnitudes=magnitudes,target=0,lower=0,upper=6,attainable=attainable)),indent=2))
