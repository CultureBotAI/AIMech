"""Finite mathematical checks; no historical optimizer or benchmark execution."""
from fractions import Fraction as F
from itertools import product
import json

def winner_term(x):
    # n=1, two classes, mask e_1 and scores (x,0); nonzero x avoids ties.
    return max(x, F(0)) + int(x > 0)
a,b,t=F(-1,5),F(1,5),F(3,4)
x=(1-t)*a+t*b
assert winner_term(x) > (1-t)*winner_term(a)+t*winner_term(b)

cuts=[[1,1,1,-1,-1,-1],[1,1,-1,1,-1,-1],[1,-1,1,1,-1,-1]]
def mixture(rows):
    n=len(rows[0]);count=len(rows)
    assert all(sum(y)==0 for y in rows)
    return [[sum(F(y[i]*y[j],count) for y in rows) for j in range(n)] for i in range(n)]
def mv(M,v):return [sum(m*x for m,x in zip(row,v)) for row in M]
def check_constraints(M):
    n=len(M)
    # PSD follows analytically because M is a convex combination of yy^T.
    for i,j,k in product(range(n),repeat=3):
        assert M[i][i]==1 and M[i][j]==M[j][i]
        assert -1<=M[i][j]<=1
        assert M[i][k]>=M[i][j]+M[j][k]-1
        assert M[j][k]>=-M[i][j]-M[i][k]-1
    assert all(sum(row)==0 for row in M)
M=mixture(cuts);check_constraints(M)
v=[sum(y[i] for y in cuts) for i in range(6)]
lam=F(10,3)
assert mv(M,v)==[lam*x for x in v]
assert lam>F(6)-lam # PSD + trace six certify this eigenvalue is uniquely largest.
soft=[F(x,3) for x in v]
assert sum(x*x for x in soft)==lam and sum(soft)==0
signs=[1 if x>0 else -1 for x in soft]
assert sum(signs)==2 # balanced relaxed columns do not ensure balanced sign rounding.

semi_cuts=[[1,-1,1,1,-1,-1],[1,-1,-1,-1,1,1]]
S=mixture(semi_cuts);check_constraints(S)
assert S[0][1]==-1
assert all(S[0][j]+S[1][j]>=0 for j in range(2,6)) # S2 with n_labeled=2
u=[0,0,1,1,-1,-1]
assert mv(S,u)==[4*x for x in u]
assert 4>6-4 # unique largest eigenvalue; recovered soft labels equal u.
assert u[:2]==[0,0] # fixed opposite labeled relation cannot orient these zeros.

# Two zero-feature observations with opposite labels, C=1. For the displayed
# primal, hinge sum >=2 and w=0,b=0 attain cost2. The printed dual has maximum4.
C=F(1);primal=2*C;printed_dual=4*C
assert primal!=printed_dual
assert 2*primal==printed_dual

print(json.dumps(dict(winner_convexity=dict(left=float(a),right=float(b),mix=float(x),
    value_at_mix=float(winner_term(x)),convex_upper_bound=float((1-t)*winner_term(a)+t*winner_term(b))),
    balanced_relaxation=dict(cuts=cuts,matrix=[[float(x) for x in row] for row in M],
    largest_eigenvalue=float(lam),soft_labels=list(map(float,soft)),rounded_labels=signs,rounded_label_sum=sum(signs)),
    semisupervised_decoding=dict(cuts=semi_cuts,largest_eigenvalue=4,soft_labels=u,
    fixed_labeled_relation=-1,interpretation='Feasible relaxed constraints, including S1-S2, permit leading-eigenvector zeros on both observed labels. With zero kernel, every feasible M is also optimal for the relaxed dual.'),
    slack_normalization=dict(displayed_primal_C1=2,printed_dual_C1=4,
    interpretation='For norm-squared primal with slack coefficient C, alpha=2*lambda yields lambda<=C/2. The printed dual bound C corresponds to slack coefficient 2C.'),
    interpretation='Exact finite examples plus PSD Gram and trace arguments; no solver or benchmark reproduction.'),indent=2))
