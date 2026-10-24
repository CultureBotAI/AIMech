"""Finite shortest-path edge-betweenness examples; not author software."""
from collections import deque
from fractions import Fraction as F
from itertools import combinations
import json

def betweenness(vertices,edges):
    adj={v:set() for v in vertices}
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    result={e:F(0) for e in edges}
    for source,target in combinations(sorted(vertices),2):
        distances={source:0};queue=deque([source])
        while queue:
            u=queue.popleft()
            for v in sorted(adj[u]):
                if v not in distances:distances[v]=distances[u]+1;queue.append(v)
        if target not in distances:continue
        def walks(u):
            if u==target:return [[u]]
            return [[u]+suffix for v in sorted(adj[u]) if distances.get(v)==distances[u]+1 and distances[v]<=distances[target] for suffix in walks(v)]
        paths=walks(source)
        for path in paths:
            for u,v in zip(path,path[1:]):result[tuple(sorted((u,v)))]+=F(1,len(paths))
    return result

def components(vertices,edges):
    unseen=set(vertices);groups=[]
    while unseen:
        q=[min(unseen)];seen=set(q)
        for u in q:
            for a,b in edges:
                v=b if a==u else a if b==u else None
                if v is not None and v not in seen:seen.add(v);q.append(v)
        unseen-=seen;groups.append(sorted(seen))
    return sorted(groups)

vertices=set(range(4));cycle={(0,1),(1,2),(2,3),(0,3)}
initial=betweenness(vertices,cycle);assert set(initial.values())=={F(2)}
first=min(initial,key=lambda e:(-initial[e],e));assert first==(0,1)
after=cycle-{first};updated=betweenness(vertices,after)
assert updated=={(0,3):F(3),(1,2):F(3),(2,3):F(4)}
second=min(updated,key=lambda e:(-updated[e],e));static_second=min(after,key=lambda e:(-initial[e],e))
assert second==(2,3) and static_second==(0,3)
recomputed_groups=components(vertices,after-{second});static_groups=components(vertices,after-{static_second})
assert recomputed_groups==[[0,3],[1,2]] and static_groups==[[0],[1,2,3]]
with_isolate=betweenness(vertices|{4},cycle);assert with_isolate==initial
assert components(vertices|{4},set())==[[0],[1],[2],[3],[4]]
print(json.dumps(dict(initial_cycle_scores={str(k):str(v) for k,v in sorted(initial.items())},removed_first=first,recomputed_scores={str(k):str(v) for k,v in sorted(updated.items())},removed_second_recomputed=second,removed_second_static=static_second,recomputed_first_split=recomputed_groups,static_first_split=static_groups,unreachable_isolate_adds_no_path_contributions=True,edgeless_result='No deletion steps; every retained vertex is a singleton component.',scope='Unnormalized sum over unordered reachable pairs, equal fractional weighting of multiple shortest paths, fixed lexicographic ties. Finite reference example only; no author implementation, benchmark or universal community-recovery guarantee.'),indent=2))
