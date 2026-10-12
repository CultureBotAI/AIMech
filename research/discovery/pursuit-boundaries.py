"""Exact, curator-derived counterexamples for MP/OMP; no fitted models or benchmarks."""
from fractions import Fraction as F
import json

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(a,c): return tuple(c*x for x in a)
def solve(a,b):
    m=[list(row)+[v] for row,v in zip(a,b)]
    for j in range(len(m)):
        p=next(i for i in range(j,len(m)) if m[i][j])
        m[j],m[p]=m[p],m[j]
        q=m[j][j];m[j]=[v/q for v in m[j]]
        for i in range(len(m)):
            if i!=j:
                q=m[i][j];m[i]=[v-q*w for v,w in zip(m[i],m[j])]
    return [row[-1] for row in m]
def fit(d,y,selected):
    a=solve([[dot(d[i],d[j]) for j in selected] for i in selected],[dot(d[i],y) for i in selected])
    pred=tuple(sum(a[k]*d[j][i] for k,j in enumerate(selected)) for i in range(len(y)))
    r=sub(y,pred)
    assert all(dot(r,d[j])==0 for j in selected)
    return a,r
def omp(d,y):
    selected=[];r=y;trace=[]
    while any(dot(r,g) for g in d):
        available=[j for j in range(len(d)) if j not in selected]
        j=max(available,key=lambda j:abs(dot(r,d[j])))
        selected.append(j);a,r=fit(d,y,selected)
        trace.append(dict(selected=list(selected),coefficients=a,residual=r))
    return trace
def certificates():
    d=[(F(1),F(0)),(F(3,5),F(4,5))];y=(F(0),F(1));r=y;mp=[]
    for step in range(3):
        j=max(range(2),key=lambda j:abs(dot(r,d[j])))
        c=dot(r,d[j]);r=sub(r,scale(d[j],c));mp.append(dict(atom=j,coefficient=c,residual=r))
    assert [s['atom'] for s in mp]==[1,0,1]
    assert mp[1]['residual']==(0,F(9,25)) and dot(mp[1]['residual'],d[1])==F(36,125)
    o=omp(d,y);assert len(o)==2 and o[-1]['coefficients']==[F(5,4),F(-3,4)] and o[-1]['residual']==(0,0)
    d3=[(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1)),(F(8,9),F(4,9),F(1,9))]
    assert all(dot(g,g)==1 for g in d3)
    y3=sub(d3[0],d3[3]);o3=omp(d3,y3)
    assert o3[-1]['selected']==[1,0,2] and len(o3)==3 and o3[-1]['residual']==(0,0,0)
    assert sub(d3[0],d3[3])==y3
    assert all(any(y3[i]*g[j]!=y3[j]*g[i] for i in range(3) for j in range(i)) for g in d3)
    # No one-atom representation exists, but e1-b uses two atoms. OMP used three.
    weak_y=(F(1),F(3,4));alpha=F(1,2);delta=F(4,5)
    assert abs(weak_y[1])>=alpha*max(map(abs,weak_y)) and abs(weak_y[1])<delta<abs(weak_y[0])
    # Raw correlation and normalized projection-energy gain can rank candidates differently.
    gain_d=[(F(1),F(0),F(0)),(F(12,13),F(5,13),F(0)),(F(0),F(0),F(1))]
    gain_y=(F(10),F(4,5),F(3,5))
    gain_trace=omp(gain_d,gain_y);assert gain_trace[0]['selected']==[0] and gain_trace[1]['selected']==[0,2]
    gain_r=gain_trace[0]['residual'];correlations=[abs(dot(gain_r,gain_d[j])) for j in [1,2]]
    gains=[]
    for j in [1,2]:
        gamma=sub(gain_d[j],scale(gain_d[0],dot(gain_d[0],gain_d[j])))
        gains.append(dot(gain_r,gain_d[j])**2/dot(gamma,gamma))
    assert correlations==[F(4,13),F(3,5)] and gains==[F(16,25),F(9,25)]
    return dict(mp_three_steps=mp,omp_two_steps=o,omp_nonminimal_support=o3,minimum_possible_support=2,weak_selected_threshold_not_maximum=dict(signal=weak_y,alpha=alpha,delta=delta),raw_correlation_versus_projection_gain=dict(dictionary=gain_d,signal=gain_y,first_selected=0,remaining_correlations=correlations,remaining_gains=gains,omp_next=2,gain_maximizer=1),scope='Exact finite real unit dictionaries; deterministic lowest-index ties. Algebraic counterexamples, not empirical benchmarks.')
if __name__=='__main__':print(json.dumps(certificates(),default=str,indent=2))
