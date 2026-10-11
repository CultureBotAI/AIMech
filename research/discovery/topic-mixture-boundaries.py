"""Original finite probability identities; no fitting or author code execution."""
from itertools import product
from math import exp, factorial, isclose, lgamma, log, pi
import json

def close(a,b):
    assert isclose(a,b,rel_tol=1e-9,abs_tol=1e-10),(a,b)

topics=((.9,.1),(.2,.8)); weights=(.5,.5)
def lda(seq):
    total=0.
    for zs in product(range(2),repeat=len(seq)):
        counts=[zs.count(i) for i in range(2)]
        moment=factorial(counts[0])*factorial(counts[1])/factorial(len(seq)+1)
        total+=moment*__import__('math').prod(topics[z][w] for z,w in zip(zs,seq))
    return total
def fixed(seq):
    return __import__('math').prod(sum(weights[k]*topics[k][w] for k in range(2)) for w in seq)
def whole_document_mixture(seq):
    return sum(weights[k]*__import__('math').prod(topics[k][w] for w in seq) for k in range(2))

for n in range(6):
    seqs=list(product(range(2),repeat=n))
    close(sum(lda(s) for s in seqs),1)
    close(sum(fixed(s) for s in seqs),1)
    close(sum(whole_document_mixture(s) for s in seqs),1)
    for s in seqs:close(lda(s),lda(tuple(reversed(s))))
close(lda((0,0)),(.9**2+.9*.2+.2**2)/3)
assert lda((0,0))!=fixed((0,0))!=whole_document_mixture((0,0))
count_mass=[factorial(3)/(factorial(j)*factorial(3-j))*lda((0,)*j+(1,)*(3-j)) for j in range(4)]
close(sum(count_mass),1)

# Exact marginal posterior after one observed word is a mixture of Dirichlets,
# not generally Dir(alpha + expected latent count).
r=.9/(.9+.2)
exact_mean=r*2/3+(1-r)/3
exact_second=r/2+(1-r)/6
expected_count_dir_second=(1+r)*(2+r)/(3*4)
close(exact_mean,(1+r)/3)
assert abs(exact_second-expected_count_dir_second)>.01

# PLSA symmetric/asymmetric parameterizations and a single exact EM update.
priors=(.4,.6); doc=((.8,.2),(.3,.7)); word=topics
joint={(d,w):sum(priors[k]*doc[k][d]*word[k][w] for k in range(2)) for d,w in product(range(2),repeat=2)}
close(sum(joint.values()),1)
for d,w in joint:
    pd=sum(priors[k]*doc[k][d] for k in range(2))
    close(joint[d,w],pd*sum(priors[k]*doc[k][d]/pd*word[k][w] for k in range(2)))
counts={(0,0):4,(0,1):1,(1,0):2,(1,1):5}
resp={(d,w):[priors[k]*doc[k][d]*word[k][w]/joint[d,w] for k in range(2)] for d,w in joint}
nk=[sum(counts[d,w]*resp[d,w][k] for d,w in joint) for k in range(2)]
new_prior=[n/sum(nk) for n in nk]
new_doc=[[sum(counts[d,w]*resp[d,w][k] for w in range(2))/nk[k] for d in range(2)] for k in range(2)]
new_word=[[sum(counts[d,w]*resp[d,w][k] for d in range(2))/nk[k] for w in range(2)] for k in range(2)]
new_joint={(d,w):sum(new_prior[k]*new_doc[k][d]*new_word[k][w] for k in range(2)) for d,w in joint}
old_ll=sum(counts[x]*log(joint[x]) for x in joint);new_ll=sum(counts[x]*log(new_joint[x]) for x in joint)
assert new_ll>=old_ll

# TEM minimizes an entropy-regularized objective at fixed positive inverse temperature.
scores=(.36,.06)
def tempered(beta):
    vals=[s**beta for s in scores];return [v/sum(vals) for v in vals]
def free(q,beta):return sum(v*log(v)-beta*v*log(s) for v,s in zip(q,scores))
q1=tempered(1);qhalf=tempered(.5)
close(q1[0],scores[0]/sum(scores));assert .5<qhalf[0]<q1[0]
assert free(qhalf,.5)<free(q1,.5)
qnear=tempered(1e-8);assert abs(qnear[0]-.5)<1e-7
# Same fixed-temperature optimum has an exact KL gap on positive support.
q=(.6,.4);gap=free(q,.5)-free(qhalf,.5)
close(gap,sum(v*log(v/u) for v,u in zip(q,qhalf)))

# The empirical mixture over document labels must weight a whole document once.
doc_priors=(.3,.7);n=3
correct=sum(doc_priors);printed=sum(p**n for p in doc_priors)
close(correct,1);assert printed<1

# LDA appendix alpha objective has Hessian M*(trigamma(sum alpha)-delta*trigamma(alpha_i)).
def tri_integer(n):return pi*pi/6-sum(1/(i*i) for i in range(1,n))
m=4;alpha=(2.,3.)
analytic=m*(tri_integer(5)-tri_integer(2))
def alpha_obj(a):return m*(lgamma(a+alpha[1])-lgamma(a)-lgamma(alpha[1]))
h=1e-3;numeric=(alpha_obj(alpha[0]+h)-2*alpha_obj(alpha[0])+alpha_obj(alpha[0]-h))/(h*h)
assert abs(analytic-numeric)<1e-6
printed_hessian=m*tri_integer(2)-tri_integer(5)
assert analytic<0<printed_hessian
print(json.dumps(dict(status='passed',lda_normalization_lengths=list(range(6)),two_word_same_symbol=dict(lda=lda((0,0)),fixed_weights=fixed((0,0)),document_mixture=whole_document_mixture((0,0))),count_mass=count_mass,posterior_second_moments=dict(exact_mixture=exact_second,expected_count_dirichlet=expected_count_dir_second),plsa_em_loglikelihood=[old_ll,new_ll],tempered_responsibilities=dict(beta1=q1,beta_half=qhalf),tempered_kl_gap=gap,empirical_mixture_total=dict(correct=correct,literal_inside_product=printed),alpha_hessian=dict(derived=analytic,finite_difference=numeric,printed=printed_hessian)),indent=2))
