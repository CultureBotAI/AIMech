"""Small exact-integer multiway search examples, not author-code replication."""
import itertools
import json
from fractions import Fraction


def normalize(state):
    offset = min(x[0] for x in state)
    return sorted([(v-offset, indices) for v, indices in state], key=lambda x:x[0], reverse=True)


def combine(left, right, perm):
    return normalize([(a+right[j][0], ia+right[j][1]) for (a,ia),j in zip(left,perm)])


def initial(values,k):
    return [[(v,(i,))]+[(0,()) for _ in range(k-1)] for i,v in enumerate(values)]


def choose(states):
    states = sorted(states,key=lambda s:s[0][0],reverse=True)
    return states[0],states[1],states[2:]


def unpack(state,values):
    bins = [indices for _,indices in state]
    assert sorted(i for ids in bins for i in ids) == list(range(len(values)))
    loads = [sum(values[i] for i in ids) for ids in bins]
    assert [v-min(loads) for v in loads] == [v for v,_ in state]
    return dict(loads=loads,indices=bins,range=max(loads)-min(loads))


def greedy(values,k):
    states = initial(values,k)
    while len(states)>1:
        left,right,rest = choose(states)
        states = rest+[combine(left,right,list(reversed(range(k))))]
    return states[0]


def ckk(values,k,budget=None):
    solution = greedy(values,k)
    best = solution[0][0]
    first = best
    history = [best]
    nodes = 0
    cut_short = False
    theoretical = int(sum(values)%k != 0)

    def visit(states):
        nonlocal best,solution,nodes,cut_short
        if best == theoretical:
            return
        if budget is not None and nodes>=budget:
            cut_short = True
            return
        nodes += 1
        total = sum(v for state in states for v,_ in state)
        maximum = max(state[0][0] for state in states)
        bound = max(Fraction(0),maximum-Fraction(total-maximum,k-1))
        if bound>=best:
            return
        if len(states)==1:
            candidate = states[0][0][0]
            if candidate < best:
                best = candidate
                solution = states[0]
                history.append(best)
            return
        left,right,rest = choose(states)
        permutations = [tuple(reversed(range(k)))]+list(itertools.permutations(range(k)))
        unique = {}
        for perm in permutations:
            child = combine(left,right,perm)
            # Equal sorted load vectors have equal objective-search futures here;
            # preserve one representative, not every membership partition.
            unique.setdefault(tuple(v for v,_ in child),child)
        children = sorted(unique.values(),key=lambda s:s[0][0])
        for child in children:
            visit(rest+[child])

    visit(initial(values,k))
    assert all(a>b for a,b in zip(history,history[1:]))
    result = unpack(solution,values)
    assert result['range']==best
    return dict(**result,initial_range=first,incumbent_history=history,nodes=nodes,
                certified=(best==theoretical or not cut_short))


def exhaustive(values,k):
    states = {(0,)*k}
    for v in values:
        states = {tuple(sorted(s[i]+(v if i==j else 0) for i in range(k)))
                  for s in states for j in range(k)}
    return states


fixtures = [((8,7,6,5,4),3),((2,2,2,3,3,5),3),((4,4,4,6,6,9),3),
            ((5,5,5,5),3),((0,0,0),3),((9,),3),((8,7,6,5,4),4)]
results = []
for values,k in fixtures:
    result = ckk(values,k)
    optimum = min(s[-1]-s[0] for s in exhaustive(values,k))
    assert result['certified'] and result['range']==optimum
    results.append(dict(values=values,k=k,optimum_range=optimum,**result))
limited = ckk((2,2,2,3,3,5),3,budget=1)
assert limited['initial_range']==limited['range']==2 and not limited['certified']
assert results[1]['range']==1
objective_states = exhaustive((4,4,4,6,6,9),3)
assert (10,10,13) in objective_states and (9,12,12) in objective_states
assert min(s[-1]-s[0] for s in objective_states)==3
assert min(s[-1] for s in objective_states)==12
print(json.dumps(dict(scope='Seven exact-integer fixtures and one-node interruption; constructed algorithm and no runtime benchmark.',results=results,interrupted=limited,objective_boundary=dict(range_optimal_loads=[10,10,13],minimum_range=3,minimum_makespan=12)),indent=2))
