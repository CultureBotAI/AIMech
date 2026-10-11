"""Synthetic mathematical witnesses; no author implementation or benchmark executed."""
import itertools
import json
import math


def softmax(x):
    e = [math.exp(v - max(x)) for v in x]
    return [v / sum(e) for v in e]


x = [0.2, -0.8, 1.1]
shift_error = max(abs(a-b) for a, b in zip(softmax(x), softmax([v+7 for v in x])))
assert shift_error < 1e-14
alpha = [1, 2, 3]
dirichlet_cov12 = -alpha[0]*alpha[1]/(sum(alpha)**2*(sum(alpha)+1))
assert dirichlet_cov12 < 0
# Three-point Gaussian quadrature is an illustration, not an exact covariance.
points = [(-math.sqrt(3), 1/6), (0, 2/3), (math.sqrt(3), 1/6)]
e1 = e2 = e12 = 0.0
for (g, wg), (a, wa), (b, wb) in itertools.product(points, repeat=3):
    th = softmax([g+0.1*a, g+0.1*b, 0])
    weight = wg*wa*wb
    e1 += weight*th[0]
    e2 += weight*th[1]
    e12 += weight*th[0]*th[1]
quadrature_cov12 = e12-e1*e2
assert quadrature_cov12 > 0
# K=1: E log exp(eta)=mu, while log E exp(eta)=mu+variance/2.
auxiliary_bound_gap = 1/2
# Two-time Gaussian joint covariance with unit marginal variances.
rho = 0.75
adjacent_difference_variance = 2-2*rho
omitting_cross_covariance = 2
joint_entropy = math.log(2*math.pi*math.e)+0.5*math.log(1-rho*rho)
summed_marginal_entropy = math.log(2*math.pi*math.e)
assert adjacent_difference_variance != omitting_cross_covariance
assert joint_entropy < summed_marginal_entropy
# Full posterior expectation versus posterior-mean plug-in for repeated words.
# For p~Beta(1,1), E[p^2]=1/3, but E[p]^2=1/4.
beta_two_word_predictive, beta_plugin = 1/3, 1/4
assert beta_two_word_predictive > beta_plugin
# Author and topic assignments for three words; compare collapsed joint ratios
# with the leave-one-out author-topic Gibbs formula for the third word.
words = [0, 1, 0]
fixed = [(0, 0), (1, 1)]
a, b, K, V, A = 0.5, 0.3, 2, 2, 2


def dm(counts, prior):
    return math.lgamma(len(counts)*prior)-math.lgamma(sum(counts)+len(counts)*prior)+sum(math.lgamma(c+prior)-math.lgamma(prior) for c in counts)


def joint(assignments):
    at = [[0]*K for _ in range(A)]
    wt = [[0]*V for _ in range(K)]
    for w, (author, topic) in zip(words, assignments):
        at[author][topic] += 1
        wt[topic][w] += 1
    return math.exp(sum(dm(row, a) for row in at)+sum(dm(row, b) for row in wt)-len(words)*math.log(A))


pairs = list(itertools.product(range(A), range(K)))
joint_weights = [joint(fixed+[p]) for p in pairs]
at, wt = [[1, 0], [0, 1]], [[1, 0], [0, 1]]
formula_weights = [(wt[t][0]+b)/(sum(wt[t])+V*b)*(at[u][t]+a)/(sum(at[u])+K*a) for u, t in pairs]
joint_probs = [v/sum(joint_weights) for v in joint_weights]
formula_probs = [v/sum(formula_weights) for v in formula_weights]
gibbs_error = max(abs(u-v) for u, v in zip(joint_probs, formula_probs))
assert gibbs_error < 1e-14
# Swapping author profiles leaves the equally weighted document mixture intact.
profiles = [[0.9, 0.1], [0.2, 0.8]]
mixture = [sum(p[k] for p in profiles)/len(profiles) for k in range(K)]
assert mixture == [sum(p[k] for p in reversed(profiles))/len(profiles) for k in range(K)]
print(json.dumps(dict(softmax_shift_error=shift_error,dirichlet_cov12=dirichlet_cov12,logistic_normal_quadrature_cov12=quadrature_cov12,one_logit_auxiliary_bound_gap=auxiliary_bound_gap,adjacent_difference_variance=adjacent_difference_variance,omitting_cross_covariance=omitting_cross_covariance,joint_entropy=joint_entropy,sum_marginal_entropy=summed_marginal_entropy,beta_two_word_predictive=beta_two_word_predictive,beta_plugin=beta_plugin,author_topic_gibbs_probs=formula_probs,gibbs_joint_comparison_error=gibbs_error,uniform_author_mixture=mixture),indent=2))
