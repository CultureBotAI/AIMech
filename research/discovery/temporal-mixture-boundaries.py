"""Original finite witnesses for temporal graphical-model identity boundaries.

Fixed probabilities/energies only: no learned model, author code or benchmark.
Run with the Python standard library. These examples do not prove general claims.
"""
import itertools
import json
import math


def bern(x, p):
    return p if x else 1-p


def normalized(weights):
    z=sum(weights.values())
    return {k:v/z for k,v in weights.items()}


bits=list(itertools.product(range(2),repeat=3))
states=list(itertools.product(range(2),repeat=2))
paths=list(itertools.product(states,repeat=3))
u=(0,1,0)


def hmdt(path, y):
    a,b=path[0]
    p=bern(a,.3+.2*u[0])*bern(b,.15+.55*a+.1*u[0])
    p*=bern(y[0],.1+.2*a+.4*b+.1*u[0])
    for t in range(1,3):
        a,b=path[t];ap,bp=path[t-1]
        p*=bern(a,.1+.6*ap+.15*u[t])
        p*=bern(b,.05+.4*a+.35*bp+.1*u[t])
        p*=bern(y[t],.1+.2*a+.4*b+.1*u[t])
    return p


hjoint={(p,y):hmdt(p,y) for p in paths for y in bits}
assert abs(sum(hjoint.values())-1)<1e-12
# The second level's transition explicitly depends on its current ancestor.
ancestor_gap=bern(1,.05+.4*1+.35*0+.1)-bern(1,.05+.4*0+.35*0+.1)
assert abs(ancestor_gap-.4)<1e-12

# Observed mixed-memory transitions: one latent selector picks one predecessor.
psi=(.35,.65)
lag_p=((.15,.8),(.3,.6))  # P(current=1 | predecessor), two possible lags


def mm(y, history):
    return sum(psi[m]*bern(y,lag_p[m][history[m]]) for m in range(2))


prob={h:mm(1,h) for h in states}
contrast=prob[0,0]+prob[1,1]-prob[0,1]-prob[1,0]
assert abs(contrast)<1e-12
xor={h:float(h[0]!=h[1]) for h in states}
xor_contrast=xor[0,0]+xor[1,1]-xor[0,1]-xor[1,0]
assert xor_contrast==-2
h=(1,0);y=1
r=[psi[m]*bern(y,lag_p[m][h[m]])/mm(y,h) for m in range(2)]
assert abs(sum(r)-1)<1e-12
# Given a previous vector, current components factorize; mixing previous states
# can nevertheless induce marginal dependence among current components.
mix_weights=((.8,.2),(.25,.75))
cp=(((.1,.9),(.2,.65)),((.3,.8),(.15,.85)))


def vector_t(now, prev):
    return math.prod(sum(mix_weights[v][m]*bern(now[v],cp[v][m][prev[m]])
                         for m in range(2)) for v in range(2))


assert max(abs(sum(vector_t(s,p) for s in states)-1) for p in states)<1e-12
prior={(0,0):.45,(0,1):.05,(1,0):.05,(1,1):.45}
marg={s:sum(prior[p]*vector_t(s,p) for p in states) for s in states}
dep=abs(marg[1,1]-sum(v for s,v in marg.items() if s[0])*sum(v for s,v in marg.items() if s[1]))
assert dep>.01
# Exact latent-source counts are joint expectations, not products of marginal
# selector and hidden-state probabilities. A fixed correlated posterior witness.
post={(0,0):.45,(0,1):.05,(1,0):.05,(1,1):.45}
joint_count=post[1,1]
factorized_count=sum(v for (x,i),v in post.items() if x)*sum(v for (x,i),v in post.items() if i)
assert abs(joint_count-factorized_count)>.1

# Linear categorical Boltzmann chain with positive finite potentials (beta=1).
A=((.7,-.2),(.1,.5));B=((.3,-.4),(-.1,.6));P=(.15,-.25)


def weight(s,y,delta=0):
    return math.exp(P[s[0]]+sum(A[s[t]][s[t+1]]+delta*(s[t]==0 and s[t+1]==1)
                                 for t in range(2))+sum(B[s[t]][y[t]] for t in range(3)))


raw={(s,y):weight(s,y) for s in bits for y in bits};z=sum(raw.values());bc=normalized(raw)
E=[[math.exp(v) for v in row] for row in B]
T=[[math.exp(v) for v in row] for row in A]
U=[math.exp(v) for v in P];es=[sum(row) for row in E]
message=[U[i]*es[i] for i in range(2)]
for t in range(1,3):message=[es[j]*sum(message[i]*T[i][j] for i in range(2)) for j in range(2)]
assert abs(sum(message)-z)<1e-11
observed=(1,0,1)


def feature(s):return sum(s[t]==0 and s[t+1]==1 for t in range(2))


clamp=normalized({s:raw[s,observed] for s in bits})
gradient=sum(p*feature(s) for s,p in clamp.items())-sum(p*feature(s) for (s,y),p in bc.items())


def ll(delta):
    zz=sum(weight(s,y,delta) for s in bits for y in bits)
    return math.log(sum(weight(s,observed,delta) for s in bits)/zz)


fd=(ll(1e-5)-ll(-1e-5))/2e-5
assert abs(fd-gradient)<1e-8
# MacKay gauge transform: positive eigenvector of M_ij = emission_sum_i*T_ij.
M=[[es[i]*T[i][j] for j in range(2)] for i in range(2)]
a,b=M[0];c,d=M[1]
lam=(a+d+math.sqrt((a-d)**2+4*b*c))/2
v=(b,lam-a)
trans=[[M[i][j]*v[j]/(lam*v[i]) for j in range(2)] for i in range(2)]
emit=[[E[i][j]/es[i] for j in range(2)] for i in range(2)]
init=[U[i]*v[i]/sum(U[k]*v[k] for k in range(2)) for i in range(2)]
assert max(abs(sum(row)-1) for row in trans)<1e-12


def hmm(s,y):
    return init[s[0]]*math.prod(trans[s[t]][s[t+1]] for t in range(2))*math.prod(emit[s[t]][y[t]] for t in range(3))


hp={(s,y):hmm(s,y) for s in bits for y in bits}
assert abs(sum(hp.values())-1)<1e-12
bc_end=normalized({k:p for k,p in bc.items() if k[0][-1]==1})
hmm_end=normalized({k:p for k,p in hp.items() if k[0][-1]==1})
end_error=max(abs(p-hmm_end[k]) for k,p in bc_end.items())
assert end_error<1e-12
free_end_gap=max(abs(p-hp[k]) for k,p in bc.items())
terminal_reweighted=normalized({(s,y):p*es[s[-1]]/v[s[-1]] for (s,y),p in hp.items()})
terminal_error=max(abs(p-terminal_reweighted[k]) for k,p in bc.items())
assert terminal_error<1e-12 and free_end_gap>1e-4
# Naive separate local normalization is not this gauge transformation.
naive_trans=[[x/sum(row) for x in row] for row in T]
naive={(s,y):U[s[0]]/sum(U)*math.prod(naive_trans[s[t]][s[t+1]] for t in range(2))*math.prod(emit[s[t]][y[t]] for t in range(3)) for s in bits for y in bits}
naive_gap=max(abs(p-naive[k]) for k,p in bc.items())
assert naive_gap>.001
print(json.dumps(dict(scope='Original finite fixed-parameter witnesses; not training or universal proofs',hmdt_joint_mass=sum(hjoint.values()),hmdt_current_ancestor_transition_gap=ancestor_gap,mixed_memory_additive_contrast=contrast,xor_contrast=xor_contrast,selector_responsibilities=r,vector_marginal_dependence=dep,joint_count_product_of_marginals_gap=joint_count-factorized_count,boltzmann_normalizer=z,elimination_error=abs(sum(message)-z),clamped_minus_free_score=gradient,score_finite_difference_error=abs(fd-gradient),fixed_terminal_equivalence_error=end_error,unconditioned_endpoint_gap=free_end_gap,terminal_reweighting_error=terminal_error,naive_local_normalization_gap=naive_gap),indent=2))
