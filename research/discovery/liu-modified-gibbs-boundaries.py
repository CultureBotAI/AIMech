"""Exact equations/negative controls; not execution or replication of author/library code.
Stdlib only, no random draws, network, file writes or timestamps. JSON stdout.
"""
from fractions import Fraction as F
from itertools import product
import json

def normalize(w):
    return [F(x,sum(w)) for x in w]

def kernel(p):
    n=len(p);K=[[F(0) for _ in p] for _ in p]
    for a in range(n):
        if p[a]==1:
            K[a][a]=F(1);continue
        for c in range(n):
            if c!=a:
                K[a][c]=min(p[c]/(1-p[a]),p[c]/(1-p[c]))
        K[a][a]=1-sum(K[a])
    return K

def invariant(p,K):
    return [sum(p[i]*K[i][j] for i in range(len(p))) for j in range(len(p))]==p

def reversible(p,K):
    return all(p[i]*K[i][j]==p[j]*K[j][i] for i in range(len(p)) for j in range(len(p)))

def verify(p,K):
    assert all(sum(row)==1 and min(row)>=0 for row in K)
    assert invariant(p,K) and reversible(p,K)
    assert all(K[i][j]>=p[j] for i in range(len(p)) for j in range(len(p)) if i!=j)
    for a in range(len(p)):
        for c in range(len(p)):
            if a==c:continue
            proposal=p[c]/(1-p[a]);ratio=(1-p[a])/(1-p[c])
            assert K[a][c]==proposal*min(F(1),ratio)
            # NumPyro 0.7.0 source algebra, evaluated as exact weights rather than logs.
            other_mass=(1-p[a])/p[a]
            selected_relative=p[c]/p[a]
            assert other_mass/(1+other_mass-selected_relative)==ratio

def compose(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def coordinate_kernel(p,coordinate):
    states=list(product(range(2),repeat=2));K=[[F(0) for _ in states] for _ in states]
    for i,s in enumerate(states):
        ids=[j for j,t in enumerate(states) if t[1-coordinate]==s[1-coordinate]]
        local=normalize([p[j] for j in ids]);local_K=kernel(local);a=ids.index(i)
        for c,j in enumerate(ids):K[i][j]=local_K[a][c]
    return K

def inferred_pymc_bad_kernel(p):
    """Exact-arithmetic interpretation of inspected v5.9.0 code, no runtime claim."""
    K=[[F(0) for _ in p] for _ in p]
    for a in range(len(p)):
        for c in range(len(p)):
            if c==a:continue
            proposal=p[c]/(1-p[a])
            # Source rejects nonfinite ratio; denominator zero maps to this branch.
            accept=F(0) if proposal==1 else min(F(1),(1-p[a])/(1-proposal))
            K[a][c]=proposal*accept
        K[a][a]=1-sum(K[a])
    return K

def main():
    count=0
    for n in range(2,6):
        for weights in product(range(1,4),repeat=n):
            p=normalize(weights);verify(p,kernel(p));count+=1
    p=normalize([6,3,1]);correct=kernel(p);bad=inferred_pymc_bad_kernel(p)
    assert correct[0][1]==F(3,7) and bad[0][1]==F(3,4)
    assert not invariant(p,bad)
    q=normalize([1,2,3,4]);A=coordinate_kernel(q,0);B=coordinate_kernel(q,1)
    fixed_scan=[[ (A[i][j]+B[i][j])/2 for j in range(4)] for i in range(4)]
    systematic=compose(A,B)
    assert invariant(q,fixed_scan) and reversible(q,fixed_scan)
    assert invariant(q,systematic) and not reversible(q,systematic)
    out={
      'scope':'Independent exact finite algebra checks, not author-code replication, scientific approval, floating-point/library execution or a general proof.',
      'positive_conditional_cases':count,
      'checks':'Rows stochastic, conditional invariance, detailed balance, off-diagonal domination of the independent conditional draw, equality of proposal/acceptance and min-form kernels, equivalence of NumPyro 0.7.0 correction algebra under positive finite conditional weights.',
      'example':{'conditional':p,'kernel':correct,'rejection_probability_current_0':correct[0][0]},
      'point_mass_guard':{'target':[1],'kernel':kernel([F(1)])},
      'uniform_binary_boundary':{'target':normalize([1,1]),'kernel':kernel(normalize([1,1])),'period':2,'interpretation':'Propose a different category does not guarantee an aperiodic chain; accepted moves can coexist with periodicity.'},
      'scan_boundary':{'states':list(product(range(2),repeat=2)),'target':q,'random_scan_invariant_reversible':True,'systematic_order_invariant':True,'systematic_order_reversible':False,'systematic_kernel':systematic,'limitation':'Does not compare asymptotic variances of systematic or random-permutation scan against Gibbs.'},
      'pymc_v5_9_0_code_negative_control':{'target':p,'equation_kernel':bad,'target_after_one_step':[sum(p[i]*bad[i][j] for i in range(3)) for j in range(3)],'preserves_target':False,'binary_case':inferred_pymc_bad_kernel(normalize([6,4])),'scope':'Exact algebraic interpretation of the inspected source overwriting probabilities before constructing its denominator. Actual PyMC/JAX runtime and floating-point behavior were not tested.'}
    }
    print(json.dumps(out,indent=2,default=str))
if __name__=='__main__':main()
