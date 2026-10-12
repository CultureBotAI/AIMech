"""Finite curator calculations, not author software or empirical reproduction."""
from collections import Counter
from itertools import product
from math import exp, lgamma
import json


def dm(counts, alpha):
    """Integrated probability of a particular categorical assignment sequence."""
    return exp(lgamma(sum(alpha)) - lgamma(sum(alpha) + sum(counts))
               + sum(lgamma(a+n)-lgamma(a) for a, n in zip(alpha, counts)))


def normalize(values):
    total = sum(values)
    return [x/total for x in values]


# ART: the third token chooses between recipients of sender 0.
words = [0, 1, 0]
senders = [0, 1, 0]
alpha, beta = 0.4, 0.3
choices = list(product([1, 2], [0, 1]))


def art_joint(recipient, topic):
    assignments = [(1, 0), (0, 1), (recipient, topic)]
    pair = Counter((senders[i], r, z) for i, (r, z) in enumerate(assignments))
    word = Counter((z, words[i]) for i, (_, z) in enumerate(assignments))
    pairs = set((senders[i], r) for i, (r, _) in enumerate(assignments))
    p = 0.5  # Third token's uniform recipient probability; other factors are one.
    for a, r in pairs:
        p *= dm([pair[a, r, z] for z in range(2)], [alpha]*2)
    for z in range(2):
        p *= dm([word[z, w] for w in range(2)], [beta]*2)
    return p


exact_art = normalize([art_joint(r, z) for r, z in choices])
conditional_art = []
for r, z in choices:
    pair_n = int(r == 1)
    pair_z = int(r == 1 and z == 0)
    word_z = int(z == 0)
    conditional_art.append((pair_z+alpha)/(pair_n+2*alpha)
                           * (word_z+beta)/(1+2*beta))
art_error = max(abs(a-b) for a, b in zip(exact_art, normalize(conditional_art)))
assert art_error < 1e-12

# Composite HMM/topic model: 0/1 are semantic topics, 2 is a function class.
# Two HMM classes, three tokens, fixed function-class states at both boundaries.
observed = [0, 1, 0]
states = list(product(range(3), repeat=3))
gamma, a, b, delta = 0.7, 0.4, 0.3, 0.6


def cls(s):
    return int(s == 2)


def composite_joint(state):
    path = [1] + [cls(s) for s in state] + [1]
    transitions = Counter(zip(path, path[1:]))
    topic = Counter(s for s in state if s != 2)
    emissions = Counter((s, w) for s, w in zip(state, observed))
    p = dm([topic[z] for z in range(2)], [a]*2)
    for c in range(2):
        p *= dm([transitions[c, v] for v in range(2)], [gamma]*2)
    for s in range(3):
        prior = delta if s == 2 else b
        p *= dm([emissions[s, w] for w in range(2)], [prior]*2)
    return p


posterior = normalize([composite_joint(s) for s in states])
max_transition_error = 0.0


def local_kernel(state, i):
    global max_transition_error
    others = [j for j in range(3) if j != i]
    nt = Counter(state[j] for j in others if state[j] != 2)
    theta = normalize([nt[z]+a for z in range(2)])
    emission = []
    for s in range(3):
        prior = delta if s == 2 else b
        denominator = sum(state[j] == s for j in others) + 2*prior
        numerator = sum(state[j] == s and observed[j] == observed[i] for j in others)+prior
        emission.append(numerator/denominator)
    path = [1] + [cls(s) for s in state] + [1]
    counts = Counter((path[j], path[j+1]) for j in range(4) if j not in [i, i+1])
    prev, nxt = path[i], path[i+2]
    transition = []
    direct = []
    for c in range(2):
        transition.append((counts[prev, c]+gamma)
                          * (counts[c, nxt]+gamma+int(prev == c == nxt))
                          / (sum(counts[c, v] for v in range(2))+2*gamma+int(prev == c)))
        modified = counts.copy()
        modified[prev, c] += 1
        modified[c, nxt] += 1
        direct.append(dm([modified[0, v] for v in range(2)], [gamma]*2)
                      * dm([modified[1, v] for v in range(2)], [gamma]*2))
    max_transition_error = max(max_transition_error,
                              max(abs(x-y) for x, y in zip(normalize(transition), normalize(direct))))
    # Draw the actual semantic topic, or a temporary topic for an inactive token.
    zprob = normalize([theta[z] * (emission[z] if state[i] != 2 else 1)
                       for z in range(2)])
    out = [0.0]*3
    for z in range(2):
        cprob = normalize([transition[0]*emission[z], transition[1]*emission[2]])
        out[z] += zprob[z]*cprob[0]
        out[2] += zprob[z]*cprob[1]
    return out


invariance_errors = []
index = {s: i for i, s in enumerate(states)}
for i in range(3):
    after = [0.0]*len(states)
    for old, prob in zip(states, posterior):
        for new, weight in enumerate(local_kernel(old, i)):
            target = list(old)
            target[i] = new
            after[index[tuple(target)]] += prob*weight
    invariance_errors.append(max(abs(x-y) for x, y in zip(posterior, after)))
assert max(invariance_errors) < 1e-12
assert max_transition_error < 1e-12

# Same word and reference aspect laws, theta ~ Beta(1,1), each P(value 0)=theta.
# Joint word/reference probability integrates theta^2, not two separate means.
joint_channels = dm([2, 0], [1, 1])
separate_channels = dm([1, 0], [1, 1])**2
assert abs(joint_channels - 1/3) < 1e-12
assert abs(separate_channels - 1/4) < 1e-12
# The same witness applies to two documents sharing a random emission parameter.
multinomial_duplicate_probability = 0.5**2 + 0.5**2
equal_document_loading = (0.9+0.1)/2
pooled_token_loading = (10*0.9+90*0.1)/100
assert equal_document_loading != pooled_token_loading

print(json.dumps({
    'art_joint_conditional_max_error': art_error,
    'art_conditional_probabilities': exact_art,
    'composite_state_count': len(states),
    'composite_auxiliary_update_invariance_errors': invariance_errors,
    'collapsed_transition_factor_max_error': max_transition_error,
    'shared_parameter_joint_probability': joint_channels,
    'product_of_separate_marginals': separate_channels,
    'shared_channel_covariance': joint_channels-separate_channels,
    'two_draw_multinomial_reference_duplicate_probability': multinomial_duplicate_probability,
    'equal_document_average': equal_document_loading,
    'length_weighted_token_average': pooled_token_loading,
    'scope': 'Small positive-prior synthetic cases; no author implementation, convergence proof or benchmark reproduction.'
}, indent=2))
