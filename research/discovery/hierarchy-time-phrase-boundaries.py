"""Finite curator calculations for PAM, TOT and TNG; no historical implementation."""
from collections import Counter, defaultdict
from itertools import product
from math import exp, lgamma, sqrt
import json


def dm(counts, alpha):
    return exp(lgamma(sum(alpha))-lgamma(sum(alpha)+sum(counts)) +
               sum(lgamma(a+n)-lgamma(a) for a, n in zip(alpha, counts)))


def normalize(xs):
    total = sum(xs)
    assert total > 0
    return [x/total for x in xs]


# Four-level PAM: three tokens in two documents, two supertopics and subtopics.
documents = [0, 0, 1]
words = [0, 1, 0]
root_prior = [0.6, 0.9]
super_priors = [[0.3, 1.2], [1.1, 0.7]]
word_prior = [0.4, 0.8]
choices = list(product(range(2), repeat=2))


def pam_counts(state, omit=None):
    root, middle, leaf = defaultdict(Counter), defaultdict(Counter), defaultdict(Counter)
    for i, (s, t) in enumerate(state):
        if i != omit:
            root[documents[i]][s] += 1
            middle[documents[i], s][t] += 1
            leaf[t][words[i]] += 1
    return root, middle, leaf


def pam_joint(state):
    root, middle, leaf = pam_counts(state)
    p = 1.0
    for d in range(2):
        p *= dm([root[d][s] for s in range(2)], root_prior)
        for s in range(2):
            p *= dm([middle[d, s][t] for t in range(2)], super_priors[s])
    for t in range(2):
        p *= dm([leaf[t][w] for w in range(2)], word_prior)
    return p


def pam_weight(state, i, candidate):
    root, middle, leaf = pam_counts(state, i)
    s, t = candidate
    d, w = documents[i], words[i]
    return ((root[d][s]+root_prior[s])/(sum(root[d].values())+sum(root_prior)) *
            (middle[d, s][t]+super_priors[s][t])/(sum(middle[d, s].values())+sum(super_priors[s])) *
            (leaf[t][w]+word_prior[w])/(sum(leaf[t].values())+sum(word_prior)))


errors = []
for state in product(choices, repeat=3):
    for i in range(3):
        exact = []
        for c in choices:
            changed = list(state)
            changed[i] = c
            exact.append(pam_joint(changed))
        expected = normalize([pam_weight(state, i, c) for c in choices])
        errors.append(max(abs(a-b) for a, b in zip(normalize(exact), expected)))
assert max(errors) < 1e-12
# Shared parent mass r~Beta(1,1), child split u~Beta(10,10):
# Cov(r*u,r*(1-u)) can be positive although one Dirichlet has negative covariances.
path_covariance = dm([2, 0], [1, 1])*dm([1, 1], [10, 10]) - 0.25**2
assert path_covariance > 0

# TOT: deterministic topic/word correspondence, two words from different topics,
# theta=(1/2,1/2), f0(t)=2t and f1(t)=2(1-t).
# A single timestamp mixture is uniform; repeated token factors are not.
t = 0.2
single_time_joint = 0.25 * (0.5*2*t + 0.5*2*(1-t))
repeated_time_joint = 0.25 * (2*t)*(2*(1-t))
tempered_time_joint = 0.25 * sqrt((2*t)*(2*(1-t)))
assert len({round(x, 12) for x in [single_time_joint, repeated_time_joint, tempered_time_joint]}) == 3
# Integrating the repeated-density diagonal over one t gives 1/6, not word mass 1/4.
repeated_single_time_integral = 1/6
single_time_word_mass = 1/4
mean, variance = 0.2, 16/1100
concentration = mean*(1-mean)/variance - 1
a, b = mean*concentration, (1-mean)*concentration
assert abs(a-2) < 1e-12 and abs(b-8) < 1e-12
consistent_mean = a/(a+b)
reversed_display_mean = b/(a+b)
assert abs(reversed_display_mean-0.8) < 1e-12
# For theta~Dir(1,1) and one time with f0=1.6,f1=.4, distinguish token P(z|t)
# from E(theta_0|t) under the single-time mixture construction.
f0, f1 = 1.6, 0.4
p_topic_given_time = f0/(f0+f1)
expected_theta_given_time = (f0/3 + f1/6)/(0.5*(f0+f1))
assert abs(p_topic_given_time-0.8) < 1e-12
assert abs(expected_theta_given_time-0.6) < 1e-12

# TNG three-token sequence: w=(0,0,0), gates x=(0,1,0), z_2=1,z_3=0.
# All categorical/Beta priors are (1,1). The initial gate is fixed unigram.
# Changing z_1 moves x_2's gate factor; omitting it changes the conditional.
def tng_joint(z):
    theta = Counter(z)
    unigram, bigram, gates = defaultdict(Counter), defaultdict(Counter), defaultdict(Counter)
    x = [0, 1, 0]
    w = [0, 0, 0]
    for i in range(3):
        if i:
            gates[z[i-1], w[i-1]][x[i]] += 1
        if x[i]:
            bigram[z[i], w[i-1]][w[i]] += 1
        else:
            unigram[z[i]][w[i]] += 1
    p = dm([theta[k] for k in range(2)], [1, 1])
    for rows in [unigram, bigram, gates]:
        for count in rows.values():
            p *= dm([count[k] for k in range(2)], [1, 1])
    return p


with_next_gate = normalize([tng_joint([0, 1, 0]), tng_joint([1, 1, 0])])
# Same document-topic factors cancel; word posterior predicts 2/3 vs 1/2.
without_next_gate = normalize([2/3, 1/2])
assert abs(with_next_gate[0]-2/3) < 1e-12
assert abs(without_next_gate[0]-4/7) < 1e-12
print(json.dumps(dict(
    pam_assignment_states=64, pam_conditional_checks=len(errors),
    pam_maximum_conditional_error=max(errors), positive_shared_parent_covariance=path_covariance,
    tot_single_timestamp_joint=single_time_joint, tot_repeated_timestamp_joint=repeated_time_joint,
    tot_inverse_length_tempered_joint=tempered_time_joint,
    tot_repeated_diagonal_integral=repeated_single_time_integral,
    tot_single_time_word_mass=single_time_word_mass,
    beta_consistent_mean=consistent_mean, beta_reversed_display_mean=reversed_display_mean,
    token_topic_given_time=p_topic_given_time, document_mixture_posterior_mean=expected_theta_given_time,
    tng_correct_topic_conditional=with_next_gate, tng_without_next_gate=without_next_gate,
    scope='Finite synthetic checks and counterexamples, not author-code execution or benchmark reproduction.'
), indent=2))
