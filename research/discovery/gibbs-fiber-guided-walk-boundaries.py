"""Original deterministic boundary calculations for three narrow method drafts.

Stdlib only. No file/network/random/time side effects; JSON stdout.
Rational matrix results are exact. Half-normal values are separately labeled
floating evaluations of analytic identities, not simulation or a proof engine.
Does not execute author/library code and does not establish general convergence.
"""
from fractions import Fraction as F
from itertools import product
from math import erf,sqrt,gcd
import json

def normalize(w):
    assert w and all(x>=0 for x in w) and sum(w)>0
    return [F(x)/sum(w) for x in w]
def eye(n):return [[F(i==j)for j in range(n)]for i in range(n)]
def compose(A,B):
    n=len(A);C=[[F(0)]*n for _ in range(n)]
    for i in range(n):
        for k,a in enumerate(A[i]):
            if a:
                for j,b in enumerate(B[k]):
                    if b:C[i][j]+=a*b
    return C
def mix(weights,kernels):
    n=len(kernels[0]);return [[sum(w*K[i][j]for w,K in zip(weights,kernels))for j in range(n)]for i in range(n)]
def after(p,K):return [sum(p[i]*K[i][j]for i in range(len(p)))for j in range(len(p))]
def invariant(p,K):return after(p,K)==p
def reversible(p,K):return all(p[i]*K[i][j]==p[j]*K[j][i]for i in range(len(p))for j in range(len(p)))
def check(p,K):
    assert all(sum(r)==1 and min(r)>=0 for r in K)
    assert invariant(p,K)
def reachable(K,i):
    seen={i};todo=[i]
    while todo:
        for j,v in enumerate(K[todo.pop()]):
            if v and j not in seen:seen.add(j);todo.append(j)
    return seen
def connected(K):return all(len(reachable(K,i))==len(K)for i in range(len(K)))
def period(K):
    assert connected(K)
    distances={0:0};todo=[0]
    while todo:
        i=todo.pop(0)
        for j,v in enumerate(K[i]):
            if v and j not in distances:distances[j]=distances[i]+1;todo.append(j)
    result=0
    for i,row in enumerate(K):
        for j,v in enumerate(row):
            if v:result=gcd(result,abs(distances[i]+1-distances[j]))
    return result

def liu(weights):
    """Restrict state indices to positive support; undefined zero-mass rows omitted."""
    support=[i for i,w in enumerate(weights)if w>0];p=normalize([weights[i]for i in support]);n=len(p);K=[[F(0)]*n for _ in range(n)]
    for a in range(n):
        if p[a]==1:K[a][a]=1;continue
        for c in range(n):
            if c!=a:
                proposal=p[c]/(1-p[a]);accept=min(F(1),(1-p[a])/(1-p[c]));K[a][c]=proposal*accept
        K[a][a]=1-sum(K[a])
    check(p,K);assert reversible(p,K)
    assert all(K[a][c]>=p[c]for a in range(n)for c in range(n)if a!=c)
    return support,p,K

def coordinates(weights,modified):
    states=list(product(range(2),repeat=2));p=normalize(weights);out=[]
    for coordinate in range(2):
        K=[[F(0)]*4 for _ in states]
        for i,x in enumerate(states):
            subset=[j for j,y in enumerate(states)if y[1-coordinate]==x[1-coordinate]];local=normalize([weights[j]for j in subset])
            T=liu(local)[2]if modified else [local[:]for _ in local]
            for c,j in enumerate(subset):K[i][j]=T[subset.index(i)][c]
        check(p,K);assert reversible(p,K);out.append(K)
    return states,p,out

def solve(A,b):
    n=len(A);M=[[F(x)for x in row]+[F(bi)]for row,bi in zip(A,b)]
    for c in range(n):
        r=next(i for i in range(c,n)if M[i][c]);M[c],M[r]=M[r],M[c];pivot=M[c][c];M[c]=[x/pivot for x in M[c]]
        for i in range(n):
            if i!=c:
                k=M[i][c];M[i]=[a-k*b for a,b in zip(M[i],M[c])]
    return [row[-1]for row in M]
def asymptotic_variance(p,K,f):
    assert connected(K)and period(K)==1 and invariant(p,K)
    mean=sum(w*x for w,x in zip(p,f));g=[x-mean for x in f];n=len(p)
    A=[[F(i==j)-K[i][j]+p[j]for j in range(n)]for i in range(n)];h=solve(A,g)
    return 2*sum(p[i]*g[i]*h[i]for i in range(n))-sum(p[i]*g[i]**2 for i in range(n))

def fiber(weights,partitions,choices,thetas):
    """Construct separate involutive proposal/MH and sign matrices, then compose.
    Allows zero choice and theta endpoints only for explicit outside-proposition checks.
    """
    n=len(weights);d=len(partitions);assert n>=1 and d>=1 and all(x>0 for x in weights)
    assert len(choices)==len(thetas)==d and sum(choices)==1 and all(w>=0 for w in choices)
    assert all(0<=t<=1 for t in thetas)
    assert all(all(line for line in part)and sorted(x for line in part for x in line)==list(range(n))for part in partitions)
    signs=list(product((-1,1),repeat=d));states=[(x,z)for x in range(n)for z in signs];ix={s:i for i,s in enumerate(states)}
    mu=[F(weights[x],sum(weights)*2**d)for x,z in states];N=len(states);kernels=[]
    for a in range(d):
        M=[[F(0)]*N for _ in states];S=[[F(0)]*N for _ in states]
        for i,(x,z)in enumerate(states):
            zflip=list(z);zflip[a]*=-1;zflip=tuple(zflip);S[i][i]=thetas[a];S[i][ix[(x,zflip)]]=1-thetas[a]
            line=next(line for line in partitions[a]if x in line);step=line.index(x)+z[a]
            if not 0<=step<len(line):M[i][i]=1;continue
            y=line[step];accept=min(F(1),F(weights[y],weights[x]));j=ix[(y,zflip)]
            # Reverse deterministic proposal is the original point and sign.
            assert line[line.index(y)+zflip[a]]==x
            M[i][j]=accept;M[i][i]+=1-accept
        check(mu,M);check(mu,S);assert reversible(mu,M)and reversible(mu,S)
        K=compose(M,S);check(mu,K);kernels.append(K)
    K=mix(choices,kernels);check(mu,K)
    return states,mu,K,kernels

def main():
    zero_cases=0
    for n in range(1,5):
        for weights in product((0,1,2),repeat=n):
            if sum(weights):liu(weights);zero_cases+=1
    weights=[4,2,2,1];states,p,L=coordinates(weights,True);_,_,G=coordinates(weights,False);f=[(1 if x==0 else -2)*(1 if y==0 else -2)for x,y in states]
    LA=compose(*L);GA=compose(*G);LR=mix([F(1,2)]*2,[LA,compose(L[1],L[0])]);GR=mix([F(1,2)]*2,[GA,compose(G[1],G[0])]);LS=mix([F(1,2)]*2,L);GS=mix([F(1,2)]*2,G)
    assert LR==LA and GR==GA and reversible(p,LR)and reversible(p,GR)
    sweep_l=asymptotic_variance(p,LR,f);sweep_g=asymptotic_variance(p,GR,f);scan_l=asymptotic_variance(p,LS,f);scan_g=asymptotic_variance(p,GS,f)
    assert (sweep_l,sweep_g,scan_l,scan_g)==(F(20,3),F(4),F(4,3),F(4))
    domination_failures=[{'from':states[i],'to':states[j],'modified':LR[i][j],'gibbs':GR[i][j]}for i in range(4)for j in range(4)if i!=j and LR[i][j]<GR[i][j]];assert domination_failures
    _,q,Q=coordinates([1,2,3,4],True);sequential=compose(*Q);permuted=mix([F(1,2)]*2,[sequential,compose(Q[1],Q[0])]);assert not reversible(q,sequential)and reversible(q,permuted)
    state_dependent=mix([F(1,2)]*2,Q)
    state_dependent=[Q[i%2][i]for i in range(4)];assert not invariant(q,state_dependent)
    family_specs=[('one_state',1,[[[0]]]),('one_state_three_signs',1,[[[0]],[[0]],[[0]]]),('one_line',3,[[[0,1,2]]]),('overlapping_with_singletons',3,[[[0,1],[2]],[[0],[1,2]]]),('singleton_partition_plus_line',3,[[[0],[1],[2]],[[0,1,2]]]),('oppositely_ordered_duplicate_partition',3,[[[0,1,2]],[[2,1,0]]]),('grid',4,[[[0,1],[2,3]],[[0,2],[1,3]]])]
    tested=[]
    for name,n,parts in family_specs:
        count=0;d=len(parts)
        for w in product((1,2),repeat=n):
            for ts in product((F(1,5),F(3,5)),repeat=d):
                st,mu,K,_=fiber(w,parts,[F(1,d)]*d,ts);assert connected(K)and period(K)==1;count+=1
        tested.append({'family':name,'positive_cases':count,'states':n,'signs':2**d})
    st,mu,disconnected,_=fiber([1,2,3],[[[0,1],[2]]],[F(1)],[F(1,5)]);assert not connected(disconnected)
    st,mu,zero_choice,_=fiber([1,2,3],[[[0,1,2]],[[0,1,2]]],[F(1),F(0)],[F(1,5),F(1,5)]);assert not connected(zero_choice)
    endpoint=[]
    for n in (1,2,3):
        for t in (F(0),F(1)):
            st,mu,K,_=fiber([1]*n,[[list(range(n))]],[F(1)],[t]);endpoint.append({'n':n,'theta':t,'invariant':True,'irreducible':connected(K),'period':period(K)if connected(K)else None,'reachable_state_counts':sorted({len(reachable(K,i))for i in range(len(K))})})
    # Half-normal continuous incoming-flow identities on a uniform [0,1] target.
    # H(t)=P(|N(0,sigma^2)|<=t). At interior x, positive-sign incoming
    # accepted mass density is H(x)/2; incoming rejection from negative sign
    # contributes [1-H(x)]/2. This sums exactly to1/2 algebraically.
    # A faulty same-sign rejection rule instead gives [H(x)+1-H(1-x)]/2.
    x=.25;sigma=1.;H=lambda t:erf(t/(sqrt(2)*sigma));a=.5*H(x);reject_from_other=.5*(1-H(x));wrong=.5*(H(x)+1-H(1-x));assert abs(a+reject_from_other-.5)<1e-15 and abs(wrong-.5)>.1
    print(json.dumps({
      'scope':'Original bounded rational illustrations and explicit analytic flow identities; no author/library runtime, benchmark replication, whole-repository gate or scientific approval.',
      'liu':{'supported_subspace_cases_including_zero_mass_categories':zero_cases,'support_example':liu([0,2,0,1]),'point_mass_example':liu([0,0,1]),'uniform_binary_period':period(liu([1,1])[2]),'sweep_counterexample':{'target_weights':weights,'target':p,'states':states,'centered_observable':f,'exact_gibbs_sweep_kernel':GR,'liu_sweep_kernel':LR,'uniform_random_permutation_equals_fixed_sweep_here':True,'both_sweep_kernels_reversible_irreducible_aperiodic':True,'asymptotic_variance_per_full_sweep':{'liu':sweep_l,'gibbs':sweep_g},'asymptotic_variance_per_single_fixed_random_scan_update':{'liu':scan_l,'gibbs':scan_g},'failed_sweep_off_diagonal_domination':domination_failures,'meaning':'Local Peskun ordering does not transfer automatically to full sweeps, including reversible uniform random-permutation sweeps. No wall-clock comparison.'},'dependent_target_scan_check':{'weights':[1,2,3,4],'systematic_invariant_nonreversible':True,'uniform_random_permutation_invariant_reversible':True,'state_dependent_selection_counterexample_after':after(q,state_dependent)}},
      'dhn':{'construction':'Independent separate reversible MH-proposal and sign matrices composed then mixed; all exact, with explicit proposal involution check.','degenerate_fiber_families':tested,'total_positive_cases':sum(x['positive_cases']for x in tested),'disconnected_partition_example':{'invariant':True,'irreducible':False},'zero_direction_selection_example':{'invariant':True,'irreducible':False,'reason':'An unselected sign remains frozen.'},'theta_endpoints':endpoint,'scope':'Singleton lines, redundant/overlapping partitions and one-state spaces are allowed by the tested finite construction. Positivity/connectivity/fixed-mixture assumptions must not be silently removed.'},
      'gustafson':{'continuous_proposal_density':'r_sigma(s)=sqrt(2/pi)/sigma*exp(-s^2/(2 sigma^2)), s>0. q((x,p),(y,-p))=r_sigma(|y-x|) when p(y-x)>0; the reverse proposal has equal density.','exact_density_identity':'For A_p(x)=integral_0^infinity r_sigma(s)*min(pi(x-p*s),pi(x)) ds, incoming acceptance density at(x,p) is A_p(x)/2 and incoming rejection density from(x,-p) is[pi(x)-A_p(x)]/2; total pi(x)/2. Assumes proper measurable target density and well-defined finite positive current density, fixed sigma>0. Zero density outside support is included in the integral.','uniform_target_incoming_example':{'x':x,'sigma':sigma,'half_normal_cdf_to_left_boundary':H(x),'accepted_incoming_plus_density':a,'rejection_from_minus_density':reject_from_other,'correct_total_density':a+reject_from_other,'wrong_same_sign_rejection_density':wrong,'target_plus_density':.5,'numeric_scope':'math.erf floating evaluation only; the displayed analytic identity supplies exact cancellation.'},'negative_control_distinction':'Keeping the old sign on both acceptance and rejection breaks the augmented target in this example. Omitting the final unconditional flip from the equivalent MH-plus-flip representation instead leaves a different valid reversible MH kernel: it is not the same negative control.','nonreversibility_witness':'On a positive-density interval, accepted transitions from(x,+) to(y,+), y>x, have positive density but their direct reverse with unchanged plus sign has zero density. The complete guided-walk kernel differs from reversible ordinary MH.','support_note':'No reflection, clipping, rejection-resampling or connected-support assumption is needed for the invariance identity. The unbounded half-normal law can jump across zero-density gaps. This calculation does not certify general Harris recurrence, rates or a multivariate bookkeeping implementation.','scale_endpoint':'sigma=0 lies outside the draft definition; then y=x and acceptance1 leaves both state/sign unchanged, giving an identity kernel.'}
    },indent=2,default=str))
if __name__=='__main__':main()
