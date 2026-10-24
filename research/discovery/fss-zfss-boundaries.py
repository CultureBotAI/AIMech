#!/usr/bin/env python3
"""Portable curator-authored exact checks; no author code imported or executed.
Prints deterministic semantic JSON to stdout; does not write files.
Execution time, output hashes and derivation provenance belong in an external receipt.
Primary source: Neal2024 author PDF SHA256 3d637d3eec046118a4c81d0d3824f387e1077d5ed8bd15d90a4db242c89d8bea.
Algorithm8 pp44–45 is the transition reference; geometry is pp41–43.
Algorithm9 pp46–47 interpretation omits the stray zero-current outer `For i`
line, retaining its displayed CDF operation. This is explicit interpretation,
not a claim of literal executable source or verified author implementation.
All arithmetic and integrated random-input laws use fractions.Fraction.
"""
from fractions import Fraction as Q
from itertools import product
from collections import Counter
import json
Z=Q(0); ONE=Q(1); HALF=Q(1,2)

def validate(p):
    assert p and all(isinstance(x,Q) and x>=0 for x in p) and sum(p)==1

def alg8(p,k,zero):
    validate(p); m=len(p)
    if p[k]==0:return list(p)
    x1=0
    for i in range(1,m):
        if p[i]>p[x1]:x1=i
    p1=p[x1]
    if p1>=HALF or m<=2:
        return [(2*p1-1)/p1 if i==k else p[i]/p1 for i in range(m)] if k==x1 else [Q(i==x1) for i in range(m)]
    p2=max(p[i] for i in range(m) if i!=x1)
    x0=x1
    for _ in range(m):
        x0=(x0-1)%m
        f=(p1-p2)/((HALF-p1)+(HALF-p[x0]))
        if not zero or p[x0]>=f*p2:break
    else:raise AssertionError('blocker search did not terminate')
    assert 0<=f<=1
    v=[f*p[i] if k==x1 and i not in [x1,x0] else Z for i in range(m)]
    lo=Z; up=p2 if k==x1 else p[k]; i=k
    steps=0
    while lo<up:
        steps+=1; assert steps<=m+1
        if i==x1:i=x0
        else:
            i=(x1-1)%m if i==x0 else (i-1)%m
            if i==x0:i=(x0-1)%m
        if lo<p[i]:
            if i not in [x1,x0]:
                t=min(up,f*p[i])
                if lo<t:v[x1]+=t-lo; lo=t
            t=min(up,p[i]); v[i]+=t-lo; lo=t
    return [x/p[k] for x in v]

def geometry(p,zero):
    """Independent bar/slice measure calculation; no alg8 helpers."""
    validate(p); n=len(p); a=max(range(n),key=lambda j:p[j]); h=p[a]
    flow=[[Z]*n for _ in p]
    if h>=HALF:
        for j in range(n):
            if j!=a:flow[a][j]=p[j]; flow[j][a]=p[j]
        flow[a][a]=2*h-1
    else:
        second=sorted(p,reverse=True)[1]
        for d in range(1,n+1):
            b=(a-d)%n
            tail=sum(p[j] for j in range(n) if j not in [a,b])
            scale=(h-second)/tail
            if not zero or p[b]>=scale*second:break
        else:raise AssertionError('geometric blocker absent')
        order=[j for j in range(n) if j!=b]
        order.insert(order.index(a),b)
        bars=[]
        for j in order:
            bars.append((j,second if j==a else p[j]))
            if j not in [a,b]:bars.append((a,scale*p[j]))
        assert [sum(t for j,t in bars if j==i) for i in range(n)]==list(p)
        levels=sorted({Z,*[h for _,h in bars]})
        for bottom,top in zip(levels,levels[1:]):
            mid=(bottom+top)/2
            active=[j for j,h in bars if h>mid]
            for q,j in enumerate(active):flow[j][active[q-1]]+=top-bottom
    return [[v/p[i] for v in row] if p[i] else list(p) for i,row in enumerate(flow)]

class UniformTrace:
    def __init__(self,value): self.value=value;self.offset=Z;self.thresholds=set()
    def ge(self,t):
        self.thresholds.add(t+self.offset)
        return self.value>=t+self.offset
    def sub(self,t):self.offset+=t

def sample9(p,k,zero,r):
    """Independent scalar sampler transcription with recorded uniform comparisons.
    For zero-current branch, interpret the repeated/stray outer For line as a
    typesetting ambiguity and use one displayed inverse-CDF traversal.
    """
    n=len(p);u=UniformTrace(r)
    if p[k]<=0:
        s=Z;i=-1;j=None
        while i<n-1 and u.ge(s):
            i+=1
            if p[i]>0:s+=p[i];j=i
        return j,u.thresholds
    a=0
    for j in range(1,n):
        if p[j]>p[a]:a=j
    maximum=p[a]
    if maximum>=HALF or n<=2:
        if k!=a:return a,u.thresholds
        s=Z;i=-1;j=None
        while i<n-1 and u.ge(s):
            i+=1
            if p[i]>0:
                s+=((2*maximum-1)/maximum if i==k else p[i]/maximum)
                j=i
        return j,u.thresholds
    second=Z;j=None
    for i in range(n):
        if i!=a and p[i]>second:second=p[i];j=i
    b=a
    for _ in range(n):
        b=(b-1)%n
        multiplier=(maximum-second)/((HALF-maximum)+(HALF-p[b]))
        if not zero or p[b]>=multiplier*second:break
    else:raise AssertionError('sampler blocker absent')
    if k==a and u.ge(second):
        u.sub(second);s=Z;i=-1
        while i<n-1 and u.ge(s):
            i+=1
            if i not in [a,b] and p[i]>0:s+=multiplier*p[i];j=i
    else:
        low=Z;upper=second if k==a else p[k];i=k;s=Z;steps=0
        while low<upper and u.ge(s):
            steps+=1;assert steps<=n+1
            if i==a:i=b
            else:
                i=(a-1)%n if i==b else (i-1)%n
                if i==b:i=(b-1)%n
            if low<p[i]:
                if i not in [a,b]:
                    t=min(upper,multiplier*p[i])
                    if low<t:s+=t-low;j=a;low=t
                if u.ge(s):
                    t=min(upper,p[i]);s+=t-low;j=i;low=t
    return j,u.thresholds

def sampler_law(p,k,zero):
    """Integrate exact piecewise-constant sampler using traced branch thresholds.
    Each midpoint run returns all scalar comparisons encountered. Splitting at
    those thresholds yields cells with constant control flow and output.
    Endpoints have zero Lebesgue measure and are tested separately.
    """
    width=ONE if p[k]==0 or max(p)>=HALF else p[k]
    queue=[(Z,width)];mass=[Z]*len(p);cells=[];runs=0
    while queue:
        lo,hi=queue.pop();j,thresholds=sample9(p,k,zero,(lo+hi)/2);runs+=1
        inner=sorted(x for x in thresholds if lo<x<hi)
        if inner:
            ends=[lo,*inner,hi];queue.extend(zip(ends,ends[1:]));continue
        assert j is not None
        mass[j]+=hi-lo;cells.append((lo,hi,j))
        assert runs<10000
    return [x/width for x in mass],cells,runs

def compositions(n,m):
    if m==1:yield (n,)
    else:
        for a in range(n+1):
            for rest in compositions(n-a,m-1):yield (a,*rest)

def properties(p,M):
    n=len(p)
    assert all(sum(row)==1 and min(row)>=0 for row in M)
    assert [sum(p[i]*M[i][j] for i in range(n)) for j in range(n)]==list(p)
    assert all(M[i][j]==0 for i in range(n) for j in range(n) if p[i]>0 and p[j]==0)
    rev=all(p[i]*M[i][j]==p[j]*M[j][i] for i in range(n) for j in range(n))
    stationary_self=sum(p[i]*M[i][i] for i in range(n))
    return rev,stationary_self

def strings(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {str(k):strings(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [strings(v) for v in x]
    return x

def main():
    results={'scope':'Three original exact finite constructions. No author code executed; no general theorem or floating-point implementation verification.','sampler_interpretation':'Algorithm9 zero-current CDF branch interpreted without its ambiguous outer For line. Ordinary continuous uniform inputs integrated exactly; closed endpoints checked separately.','case_generation':'All distinct nonnegative rational probability vectors with 1–6 states obtained from ordered weak compositions of totals1–8; plus explicit Figure10, strict half-neighbors, irregular ties and zero-mass cases.','counts':Counter(),'endpoint_zero_probability_outputs':[],'differences':[]}
    cases=set()
    for m in range(1,7):
        for denominator in range(1,9):
            for w in compositions(denominator,m):cases.add(tuple(Q(v,denominator) for v in w))
    extra=[(Q(1,10),Q(1,5),Q(1,5),Q(1,20),Q(9,20)),(Q(499,1000),Q(251,1000),Q(1,4)),(Q(501,1000),Q(249,1000),Q(1,4)),(Q(0),Q(499,1000),Q(251,1000),Q(0),Q(1,4)),(Q(9,20),Q(1,20),Q(1,5),Q(1,5),Q(1,10))]
    cases.update(extra)
    counts=results['counts'];firstdiff=None;reorder_zeros=None
    for ix,p in enumerate(sorted(cases,key=lambda p:(len(p),p))):
        counts['distributions']+=1
        for zero in [False,True]:
            name='ZFSS' if zero else 'FSS';counts['kernels']+=1
            M=[alg8(p,k,zero) for k in range(len(p))]
            assert M==geometry(p,zero),('geometry',p,zero)
            rev,stay=properties(p,M);lower=max(Z,2*max(p)-1)
            assert stay>=lower
            if zero:assert stay==lower,('minimal',p,stay,lower)
            if max(p)>=HALF:assert rev
            else:assert not rev,('nonreversibility',p,zero)
            counts[name+'_nonminimal_self']+=int(stay>lower)
            counts[name+'_reversible']+=int(rev)
            counts['zero_mass_rows']+=sum(x==0 for x in p)
            counts['tied_max_kernels']+=int(p.count(max(p))>1)
            counts['half_boundary_kernels']+=int(max(p)==HALF)
            counts['point_mass_kernels']+=int(max(p)==1)
            for k in range(len(p)):
                law,cells,runs=sampler_law(p,k,zero)
                assert M[k]==law,('sampler',p,k,zero,M[k],law)
                counts['integrated_sampler_rows']+=1;counts['integrated_uniform_cells']+=len(cells);counts['sampler_executions']+=runs
                width=ONE if p[k]==0 or max(p)>=HALF else p[k]
                for endpoint in [Z,width]:
                    j,_=sample9(p,k,zero,endpoint)
                    counts['endpoint_checks']+=1
                    if j is None or M[k][j]==0:
                        counts['endpoint_zero_probability_outputs']+=1
                        if len(results['endpoint_zero_probability_outputs'])<6:results['endpoint_zero_probability_outputs'].append({'target':p,'method':name,'current_0based':k,'uniform':endpoint,'range':[Z,width],'returned_0based':j,'row':M[k]})
            if not zero:F=M
            else:
                if F!=M:
                    counts['distributions_FSS_ZFSS_distinct']+=1
                    if firstdiff is None:firstdiff={'target':p,'FSS':F,'ZFSS':M}
    results['first_distinct_kernel']=firstdiff
    p=extra[0]
    SS=[[Q(0),Q(0),Q(0),Q(0),Q(1)],[Q(1,2),Q(0),Q(0),Q(0),Q(1,2)],[Q(0),Q(1),Q(0),Q(0),Q(0)],[Q(0),Q(0),Q(1),Q(0),Q(0)],[Q(0),Q(0),Q(1,3),Q(1,9),Q(5,9)]]
    expectedF=[[Q(0),Q(0),Q(0),Q(0),Q(1)],[Q(1,4),Q(0),Q(0),Q(0),Q(3,4)],[Q(0),Q(1,2),Q(0),Q(0),Q(1,2)],[Q(0),Q(0),Q(0),Q(0),Q(1)],[Q(1,9),Q(2,9),Q(4,9),Q(1,9),Q(1,9)]]
    expectedZ=[*expectedF[:4],[Q(10,63),Q(20,63),Q(4,9),Q(5,63),Q(0)]]
    F=[alg8(p,k,False) for k in range(5)];T=[alg8(p,k,True) for k in range(5)]
    assert F==expectedF and T!=expectedZ
    expected_correct_Z=[expectedF[0],[Q(1,7),Z,Z,Z,Q(6,7)],[Z,Q(2,7),Z,Q(1,14),Q(9,14)],expectedF[3],expectedZ[4]]
    assert T==expected_correct_Z
    printed_push=[sum(p[i]*expectedZ[i][j] for i in range(5)) for j in range(5)]
    assert printed_push==[Q(17,140),Q(17,70),Q(1,5),Q(1,28),Q(2,5)]
    results['figure10']={'target':p,'SS_printed':SS,'FSS_verified':F,'ZFSS_printed_nonstationary':expectedZ,'ZFSS_calculated_three_ways':T,'printed_ZFSS_target_after_one_step':printed_push,'printed_ZFSS_stationarity_residual':[a-b for a,b in zip(printed_push,p)],'stationary_self_correct_kernels':[sum(p[i]*M[i][i] for i in range(5)) for M in [SS,F,T]],'source_caveat':'The printed ZFSS matrix rows2 and3 retain FSS entries and fail stationarity. Its final row agrees with Algorithms8–9 and geometric calculation. This script preserves the printed matrix as a negative control, not a valid kernel.','matrix_rows_in_original_state_order':True}
    results['uniform_periodicity']={}
    for m in range(2,9):
        p=tuple(Q(1,m) for _ in range(m));M=geometry(p,True)
        assert M==[alg8(p,k,False) for k in range(m)]
        assert all(M[k][(k-1)%m]==1 for k in range(m))
        results['uniform_periodicity'][m]={'deterministic_predecessor_cycle':True,'period':m}
    invalids=[(),(Q(-1),Q(2)),(Q(0),Q(0)),(Q(1,3),Q(1,3))]
    for p in invalids:
        try:validate(p)
        except AssertionError:counts['invalid_probability_vectors_rejected']+=1
        else:raise AssertionError('invalid input accepted')
    return strings(results)


if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
