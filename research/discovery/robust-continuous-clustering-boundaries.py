"""Finite exact RCC subproblem and extraction checks; no author code or training."""
from fractions import Fraction as F
from itertools import product, combinations
import json


def rho(y, mu):
    return mu * y*y / (mu + y*y)


def lifted(y, t, mu):
    # t=sqrt(l), avoiding approximate square roots.
    return t*t*y*y + mu*(t-1)**2


def objective(x, u, mu, lam):
    return sum((a-b)**2 for a,b in zip(x,u))/2 + lam*rho(u[0]-u[1],mu)/2


def components(u, edges, threshold):
    neighbors={i:set() for i in range(len(u))}
    for i,j in edges:
        if abs(u[i]-u[j]) < threshold:
            neighbors[i].add(j);neighbors[j].add(i)
    unseen=set(neighbors);groups=[]
    while unseen:
        stack=[min(unseen)];group=set()
        while stack:
            i=stack.pop()
            if i in group:continue
            group.add(i);stack.extend(neighbors[i]-group)
        unseen-=group;groups.append(sorted(group))
    return groups


def main():
    line_cases=0
    for mu,y in product(map(F,(1,4,9,16)),map(F,(0,F(1,2),1,2,4))):
        t=mu/(mu+y*y)
        assert lifted(y,t,mu)==rho(y,mu)
        # Exact square completion proves the nonnegative gap at sampled t.
        for other in (F(k,10) for k in range(21)):
            assert lifted(y,other,mu)-rho(y,mu)==(mu+y*y)*(other-t)**2
        line_cases+=1
    descent_cases=0
    for mu,lam,gap,initial in product((F(1,4),F(1),F(4)),(F(1,2),F(1),F(2)),(F(1),F(2),F(4)),('data','coincident','other')):
        x=(F(0),gap);u={'data':x,'coincident':(F(0),F(0)),'other':(F(-1),F(3))}[initial]
        t=mu/(mu+(u[0]-u[1])**2);a=lam*t*t
        v=(( (1+a)*x[0]+a*x[1])/(1+2*a),(a*x[0]+(1+a)*x[1])/(1+2*a))
        assert (1+a)*v[0]-a*v[1]==x[0]
        assert -a*v[0]+(1+a)*v[1]==x[1]
        assert 1+2*a>0
        assert objective(x,v,mu,lam)<=objective(x,u,mu,lam)
        descent_cases+=1
    influence=lambda y:2*y/(1+y*y)**2
    assert influence(F(10))<influence(F(1)) and influence(F(0))==0
    # All-pair extraction and original-edge extraction can differ.
    u=(F(0),F(1,10),F(10));edges=[(0,2),(1,2)]
    restricted=components(u,edges,F(1));all_pairs=components(u,combinations(range(3),2),F(1))
    assert restricted==[[0],[1],[2]] and all_pairs==[[0,1],[2]]
    # Literal printed loop predicate is true even after the iteration cap.
    assert (F(0)<F(1,10)) or (101<100)
    # Maximum- and median-edge initialization differ on a simple edge list.
    lengths=[F(1),F(2),F(10)]
    assert 3*lengths[-1]**2==300 and 3*lengths[1]**2==12
    print(json.dumps(dict(line_process_cases=line_cases,fixed_parameter_two_point_descent_cases=descent_cases,redescending_influence=dict(at_one=influence(F(1)),at_ten=influence(F(10))),extraction_scope=dict(representatives=u,original_edges=edges,restricted_components=restricted,all_pair_components=all_pairs,qualification='Constructed output-function distinction, not a claim that these representatives arise in an author RCC run.'),initial_mu_example=dict(maximum_based=300,median_based=12),printed_loop=dict(small_change_after_cap=True,qualification='Static predicate check only; pinned author code uses a bounded for-loop instead.'),limits='Finite rational curator checks. Fixed-parameter descent does not establish global optimality, a changing-parameter continuation guarantee, approximate-PCG convergence or author benchmark replication.'),default=str,indent=2))


if __name__=='__main__':
    main()
