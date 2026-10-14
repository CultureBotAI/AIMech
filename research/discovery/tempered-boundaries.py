"""Finite path-law checks of Neal's tempered transitions."""
from fractions import Fraction as F
from itertools import product
import json


def normalize(f):return [F(v,sum(f)) for v in f]


def invariant(p,t):
    return all(sum(row)==1 for row in t) and all(sum(p[i]*t[i][j] for i in range(len(p)))==p[j] for j in range(len(p)))


def paired(p,up,down):
    return invariant(p,up) and invariant(p,down) and all(p[i]*up[i][j]==p[j]*down[j][i] for i in range(len(p)) for j in range(len(p)))


def transition(functions,up,down,check=True,acceptance='path'):
    n=len(functions)-1;k=len(functions[0]);assert n==len(up)==len(down)
    if check:
        assert all(paired(normalize(functions[j+1]),up[j],down[j]) for j in range(n))
    kernels=up+list(reversed(down))
    kernel=[[F(0) for _ in range(k)] for _ in range(k)]
    for start in range(k):
        for rest in product(range(k),repeat=2*n):
            states=(start,)+rest
            q=F(1)
            for step,t in enumerate(kernels):q*=t[states[step]][states[step+1]]
            if not q:continue
            ratio=F(1)
            for j in range(1,n+1):
                a=states[j-1];z=states[2*n-j+1]
                ratio*=F(functions[j][a],functions[j-1][a])*F(functions[j-1][z],functions[j][z])
            if acceptance=='endpoint':ratio=F(functions[0][states[-1]],functions[0][start])
            a=min(F(1),ratio)
            kernel[start][states[-1]]+=q*a
            kernel[start][start]+=q*(1-a)
    assert all(sum(row)==1 for row in kernel)
    return kernel


def detailed(p,k):return all(p[i]*k[i][j]==p[j]*k[j][i] for i in range(len(p)) for j in range(len(p)))


def rows(k):return [[str(x) for x in row] for row in k]


def main():
    f0=[1,2,7];f1=[1,2,3];f2=[1,1,1];p0=normalize(f0)
    identity=[[F(i==j) for j in range(3)] for i in range(3)]
    cycle=[[F(j==(i+1)%3) for j in range(3)] for i in range(3)]
    reverse=[list(row) for row in zip(*cycle)]
    refresh1=[normalize(f1) for _ in range(3)]
    refresh2=[normalize(f2) for _ in range(3)]
    fs=[f0,f1,f2]
    good=transition(fs,[refresh1,refresh2],[refresh1,refresh2])
    assert invariant(p0,good) and detailed(p0,good)
    scaled=[[s*x for x in f] for s,f in zip([7,11,13],fs)]
    assert transition(scaled,[refresh1,refresh2],[refresh1,refresh2])==good
    endpoint=transition(fs,[refresh1,refresh2],[refresh1,refresh2],acceptance='endpoint')
    assert not invariant(p0,endpoint)
    after_endpoint=[sum(p0[i]*endpoint[i][j] for i in range(3)) for j in range(3)]
    # Both directions can be individually invariant but fail mutual reversal.
    uniform=normalize(f2)
    assert invariant(uniform,cycle) and not paired(uniform,cycle,cycle)
    wrong=transition([f0,f2],[cycle],[cycle],check=False)
    assert not invariant(p0,wrong)
    after_wrong=[sum(p0[i]*wrong[i][j] for i in range(3)) for j in range(3)]
    # Correct reversal may cancel all movement: invariance is not ergodicity.
    no_movement=transition([f0,f2],[cycle],[reverse])
    assert no_movement==identity
    count=0
    for target in product([1,2],repeat=3):
        for a,b in product([F(0),F(1,2),F(1)],repeat=2):
            u1=[[(1-a)*identity[i][j]+a*refresh1[i][j] for j in range(3)] for i in range(3)]
            u2=[[(1-b)*identity[i][j]+b*cycle[i][j] for j in range(3)] for i in range(3)]
            d2=[list(row) for row in zip(*u2)]
            k=transition([target,f1,f2],[u1,u2],[u1,d2]);p=normalize(target)
            assert invariant(p,k) and detailed(p,k)
            count+=1
    assert count==72
    return dict(target=[str(x) for x in p0],correct_path_kernel=rows(good),independent_density_scales_cancel=True,endpoint_only_acceptance=dict(kernel=rows(endpoint),target_after_one_step=[str(x) for x in after_endpoint]),wrong_same_nonreversible_directions=dict(kernel=rows(wrong),target_after_one_step=[str(x) for x in after_wrong]),correct_cycle_reverse_is_identity=True,finite_invariant_family_cases=count,scope='Exact finite path enumeration, including rejection self-loops. No author-code or benchmark replication, universal efficiency bound, guarantee of ergodicity or numerical implementation audit.')


if __name__=='__main__':print(json.dumps(main(),indent=2))
