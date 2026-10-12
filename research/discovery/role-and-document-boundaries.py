"""Finite curator checks for role and document mixtures; no source implementation."""
from collections import Counter, defaultdict
from itertools import product
from math import exp, lgamma, log
import json


def dm(counts, alpha):
    return exp(lgamma(sum(alpha)) - lgamma(sum(alpha) + sum(counts)) +
               sum(lgamma(a + n) - lgamma(a) for a, n in zip(alpha, counts)))


def normalize(xs):
    total = sum(xs)
    assert total > 0
    return [x / total for x in xs]


# Two actors, two roles, two topics, two words. A recipient can equal sender.
senders = [0, 1]
words = [0, 1]
choices = list(product(range(2), repeat=4))  # recipient, sender role, recipient role, topic
alpha = [0.7, 1.1]
beta = [0.4, 0.9]
gamma = [0.6, 1.3]


def counts(assignments, omit=None):
    actor = defaultdict(Counter)
    pair = defaultdict(Counter)
    topic = defaultdict(Counter)
    for i, (r, g, h, z) in enumerate(assignments):
        if i == omit:
            continue
        actor[senders[i]][g] += 1
        actor[r][h] += 1
        pair[g, h][z] += 1
        topic[z][words[i]] += 1
    return actor, pair, topic


def joint(assignments):
    actor, pair, topic = counts(assignments)
    p = 0.5 ** len(assignments)
    for a in range(2):
        p *= dm([actor[a][k] for k in range(2)], gamma)
    for g, h in product(range(2), repeat=2):
        p *= dm([pair[g, h][z] for z in range(2)], alpha)
    for z in range(2):
        p *= dm([topic[z][v] for v in range(2)], beta)
    return p


def conditional(assignments, i, candidate):
    actor, pair, topic = counts(assignments, i)
    r, g, h, z = candidate
    # Sequential predictive factors correctly handle two draws from the same psi.
    p = 0.5
    for a, role in [(senders[i], g), (r, h)]:
        p *= (actor[a][role] + gamma[role]) / (sum(actor[a].values()) + sum(gamma))
        actor[a][role] += 1
    p *= (pair[g, h][z] + alpha[z]) / (sum(pair[g, h].values()) + sum(alpha))
    p *= (topic[z][words[i]] + beta[words[i]]) / (sum(topic[z].values()) + sum(beta))
    return p


errors = []
for state in product(choices, repeat=2):
    for i in range(2):
        direct = []
        for choice in choices:
            changed = list(state)
            changed[i] = choice
            direct.append(joint(changed))
        predicted = [conditional(state, i, c) for c in choices]
        errors.append(max(abs(x-y) for x, y in zip(normalize(direct), normalize(predicted))))
assert max(errors) < 1e-12
# With uniform two-role prior, the probability of equal roles is 2/3 if the
# two draws share an integrated actor vector, versus 1/2 for independent actors.
shared_equal_roles = sum(dm([2, 0] if k == 0 else [0, 2], [1, 1]) for k in range(2))
independent_equal_roles = 0.5
assert abs(shared_equal_roles - 2/3) < 1e-12

# Multilabel mode substitution: E[lambda^2] != (mode lambda)^2 for Beta(2,2).
integrated_two_words = dm([2, 0], [2, 2])
mode_two_words = 0.5 ** 2
assert abs(integrated_two_words - 0.3) < 1e-12
additive_estimate = normalize([3 + 1, 1 + 1])
flat_prior_map = normalize([3, 1])
assert additive_estimate != flat_prior_map

# Cohn-Hofmann alpha-weighted document/channel normalized criterion.
# These are finite positive categorical parameters; ordinary beta=1 EM only.
channel_counts = [[[8, 2], [1, 3]], [[1, 4], [9, 1]]]
channel_weights = [0.6, 0.4]
theta = [[0.7, 0.3], [0.4, 0.6]]
emissions = [[[0.8, 0.2], [0.3, 0.7]], [[0.6, 0.4], [0.2, 0.8]]]


def objective(theta, emissions):
    return sum(channel_weights[c] * count/sum(row) *
               log(sum(theta[d][z]*emissions[c][z][v] for z in range(2)))
               for d, channels in enumerate(channel_counts)
               for c, row in enumerate(channels) for v, count in enumerate(row))


expected_emissions = [[[0.0, 0.0] for _ in range(2)] for _ in range(2)]
new_theta = [[0.0, 0.0] for _ in range(2)]
for d, channels in enumerate(channel_counts):
    for c, row in enumerate(channels):
        for v, count in enumerate(row):
            resp = normalize([theta[d][z] * emissions[c][z][v] for z in range(2)])
            for z in range(2):
                mass = channel_weights[c] * count/sum(row) * resp[z]
                new_theta[d][z] += mass
                expected_emissions[c][z][v] += mass
raw_sums = [[sum(row) for row in channel] for channel in expected_emissions]
new_emissions = [[normalize(row) for row in channel] for channel in expected_emissions]
new_theta = [normalize(row) for row in new_theta]
before, after = objective(theta, emissions), objective(new_theta, new_emissions)
assert after >= before - 1e-12
assert any(abs(s - 1) > 1e-6 for channel in raw_sums for s in channel)
print(json.dumps(dict(
    rart_assignment_states=256, rart_conditional_checks=len(errors),
    maximum_rart_conditional_error=max(errors),
    same_actor_equal_role_probability=shared_equal_roles,
    independent_actors_equal_role_probability=independent_equal_roles,
    integrated_multilabel_two_word_probability=integrated_two_words,
    mode_substitution_two_word_probability=mode_two_words,
    additive_smoothing=additive_estimate, flat_dirichlet_map=flat_prior_map,
    joint_channel_objective_before=before, joint_channel_objective_after=after,
    unnormalized_emission_row_sums=raw_sums,
    scope='Finite synthetic probability and ordinary-EM checks, not source code or benchmarks.'
), indent=2))
