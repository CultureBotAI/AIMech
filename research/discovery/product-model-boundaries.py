"""Original finite witnesses for product models; no fitting or benchmark execution."""
from itertools import product
from math import exp, log, prod
import json


def normalize(xs):
    z = sum(xs)
    assert z > 0
    return [x / z for x in xs]


def pool(ps, weights):
    return normalize([prod(p[i] ** w for p, w in zip(ps, weights)) for i in range(len(ps[0]))])


def kl(p, q):
    return sum(a * log(a / b) for a, b in zip(p, q) if a)


p, q, truth = [.8, .2], [.6, .4], [.3, .7]
weights = [.4, .6]
opinion = pool([p, q], weights)
poe = pool([p, q], [1, 1])
z = sum(prod(r[i] ** w for r, w in zip([p, q], weights)) for i in range(2))
average_kl = sum(w * kl(truth, r) for w, r in zip(weights, [p, q]))
ambiguity = sum(w * kl(opinion, r) for w, r in zip(weights, [p, q]))
assert abs(ambiguity + log(z)) < 1e-14
assert abs(kl(truth, opinion) - (average_kl - ambiguity)) < 1e-14
trial = [.45, .55]
assert abs(sum(w * kl(trial, r) for w, r in zip(weights, [p, q])) - kl(trial, opinion) - ambiguity) < 1e-14
assert max(abs(a-b) for a,b in zip(pool([p,p], weights),p)) < 1e-14
assert pool([p,p], [1,1]) != p
likelihood = [.4, .9]
update = lambda r: normalize([a*b for a,b in zip(r,likelihood)])
assert max(abs(a-b) for a,b in zip(pool([update(p),update(q)],weights), update(opinion))) < 1e-14
unweighted_update_gap = max(abs(a-b) for a,b in zip(pool([update(p),update(q)],[1,1]),update(poe)))
assert unweighted_update_gap > .05
veto = pool([[1,0],[.2,.8]],[.5,.5])
assert veto == [1.,0.]
assert sum(a*b for a,b in zip([1,0],[0,1])) == 0  # undefined normalization

# Two two-state, binary-emission HMM experts, sequence length two.
pi = [[.7,.3],[.4,.6]]
trans = [[[.8,.2],[.3,.7]],[[.6,.4],[.1,.9]]]
emission = [[[.9,.1],[.2,.8]],[[.65,.35],[.15,.85]]]
seqs = list(product(range(2), repeat=2))
paths = seqs


def joint(m, v, s, delta=0., power=1.):
    a = [row[:] for row in trans[m]]
    if m == 0:
        odds = a[0][0] / a[0][1] * exp(delta)
        a[0] = [odds/(1+odds), 1/(1+odds)]
    return pi[m][s[0]] * a[s[0]][s[1]] * prod(emission[m][st][vt] ** power for st,vt in zip(s,v))


def marginal(m, v, delta=0., power=1.):
    return sum(joint(m,v,s,delta,power) for s in paths)


def distribution(delta=0.):
    raw = [marginal(0,v,delta)*marginal(1,v) for v in seqs]
    return normalize(raw), sum(raw)


pv, z2 = distribution()
z1 = sum(prod(sum(pi[m][s]*emission[m][s][v] for s in range(2)) for m in range(2)) for v in range(2))
assert abs(z1-z2) > .1
posterior_error = 0.
kernel = []
for v in seqs:
    latent = normalize([joint(0,v,a)*joint(1,v,b) for a in paths for b in paths])
    pa = normalize([joint(0,v,a) for a in paths])
    pb = normalize([joint(1,v,b) for b in paths])
    posterior_error = max(posterior_error, max(abs(latent[i*4+j]-pa[i]*pb[j]) for i in range(4) for j in range(4)))
    row = []
    for vp in seqs:
        value = 0.
        for ia,a in enumerate(paths):
            for ib,b in enumerate(paths):
                conditional = prod(normalize([emission[0][a[t]][c]*emission[1][b[t]][c] for c in range(2)])[vp[t]] for t in range(2))
                value += latent[ia*4+ib]*conditional
        row.append(value)
    assert abs(sum(row)-1) < 1e-14
    kernel.append(row)
invariance_error = max(abs(sum(pv[i]*kernel[i][j] for i in range(4))-pv[j]) for j in range(4))
assert posterior_error < 1e-14 and invariance_error < 1e-14
# Missing second observation: hidden chains need not remain independent.
missing = normalize([sum(joint(0,(0,last),a)*joint(1,(0,last),b) for last in range(2)) for a in paths for b in paths])
ma = [sum(missing[i*4+j] for j in range(4)) for i in range(4)]
mb = [sum(missing[i*4+j] for i in range(4)) for j in range(4)]
missing_dependence = max(abs(missing[i*4+j]-ma[i]*mb[j]) for i in range(4) for j in range(4))
assert missing_dependence > 1e-3
# Fisher score uses an expectation of a derivative, with the posterior fixed.
score = lambda v: sum(joint(0,v,s)/marginal(0,v) * ((1. if s==(0,0) else 0.)-.8*(s[0]==0)) for s in paths)
observed = (0,1)
analytic = score(observed)-sum(prob*score(v) for prob,v in zip(pv,seqs))
epsilon = 1e-5
index = seqs.index(observed)
fd = (log(distribution(epsilon)[0][index])-log(distribution(-epsilon)[0][index]))/(2*epsilon)
assert abs(analytic-fd) < 1e-9

# Normalizing each emission product before marginalizing defines a different model.
directed = []
for v in seqs:
    directed.append(sum(pi[0][a[0]]*trans[0][a[0]][a[1]]*pi[1][b[0]]*trans[1][b[0]][b[1]]*
        prod(normalize([emission[0][a[t]][c]*emission[1][b[t]][c] for c in range(2)])[v[t]] for t in range(2))
        for a in paths for b in paths))
assert abs(sum(directed)-1) < 1e-14
directed_gap = max(abs(a-b) for a,b in zip(pv,directed))
assert directed_gap > .01
# Emission-only tempering through a latent sum is not a power of its marginal.
tempered = normalize([marginal(0,v,power=.5) for v in seqs])
powered = normalize([marginal(0,v)**.5 for v in seqs])
tempering_gap = max(abs(a-b) for a,b in zip(tempered,powered))
assert tempering_gap > .001

print(json.dumps(dict(product=poe, opinion_pool=opinion, repeated_product=pool([p,p],[1,1]),
    repeated_opinion_pool=pool([p,p],weights), pool_normalizer=z, weighted_truth_kl=average_kl,
    pool_truth_kl=kl(truth,opinion), ambiguity=ambiguity, unweighted_bayes_update_gap=unweighted_update_gap,
    positive_weight_zero_veto=veto, pohmm_probabilities=pv, normalizers_by_length=[z1,z2],
    conditional_independence_error=posterior_error, gibbs_invariance_error=invariance_error,
    missing_observation_dependence=missing_dependence, likelihood_gradient=analytic,
    finite_difference_gradient=fd, gradient_error=abs(analytic-fd),
    locally_normalized_directed_model_gap=directed_gap, emission_tempering_vs_marginal_power_gap=tempering_gap),indent=2))
