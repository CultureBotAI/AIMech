#!/usr/bin/env python3
"""Finite curator checks for APT, GT and GCA; not author-code reproduction."""
import itertools
import json
import math
from collections import Counter


def dm(counts, prior):
    return math.exp(math.lgamma(sum(prior)) - math.lgamma(sum(prior) + sum(counts))
                    + sum(math.lgamma(a + n) - math.lgamma(a) for n, a in zip(counts, prior)))


def norm(weights):
    total = sum(weights)
    return [x / total for x in weights]


def discrepancy(a, b):
    return max(abs(x - y) for x, y in zip(norm(a), norm(b)))


def apt():
    authors = [0, 0, 1]
    docs = [0, 0, 1, 2]
    words = [0, 1, 0, 1]
    alpha, beta, gamma = [.7, 1.3], [.8, 1.2], [1.1, .9]
    states = list(itertools.product(range(2), repeat=7))  # 3 personas, 4 topics

    def counts(state, omit_doc=None, omit_token=None):
        person = {(a, g): 0 for a in range(2) for g in range(2)}
        topics = {(a, g): [0, 0] for a in range(2) for g in range(2)}
        emissions = [[0, 0], [0, 0]]
        for d, a in enumerate(authors):
            if d != omit_doc:
                person[a, state[d]] += 1
        for i, (d, w) in enumerate(zip(docs, words)):
            if i == omit_token or d == omit_doc:
                continue
            k = state[3 + i]
            topics[authors[d], state[d]][k] += 1
            emissions[k][w] += 1
        return person, topics, emissions

    def joint(state):
        p, t, e = counts(state)
        return (math.prod(dm([p[a, 0], p[a, 1]], gamma) for a in range(2))
                * math.prod(dm(c, alpha) for c in t.values())
                * math.prod(dm(c, beta) for c in e))

    error, checked = 0., 0
    for state in states:
        for i, (d, w) in enumerate(zip(docs, words)):
            _, t, e = counts(state, omit_token=i)
            local = t[authors[d], state[d]]
            weights = [(local[k] + alpha[k]) / (sum(local) + sum(alpha))
                       * (e[k][w] + beta[w]) / (sum(e[k]) + sum(beta)) for k in range(2)]
            brute = []
            for k in range(2):
                s = list(state)
                s[3 + i] = k
                brute.append(joint(s))
            error = max(error, discrepancy(weights, brute))
            checked += 1
        for d, a in enumerate(authors):
            p, t, _ = counts(state, omit_doc=d)
            h = Counter(state[3 + i] for i, dd in enumerate(docs) if dd == d)
            weights, brute = [], []
            for g in range(2):
                c = t[a, g]
                weights.append((p[a, g] + gamma[g])
                               * dm([c[k] + h[k] for k in range(2)], alpha) / dm(c, alpha))
                s = list(state)
                s[d] = g
                brute.append(joint(s))
            error = max(error, discrepancy(weights, brute))
            checked += 1
    assert error < 1e-12 and checked == 896
    reinforced = dm([3, 0], [1, 1]) / dm([1, 0], [1, 1])
    independent = (2 / 3) ** 2
    assert abs(reinforced - .5) < 1e-12 and abs(independent - 4 / 9) < 1e-12
    shared = .5 * .9 ** 2 + .5 * .1 ** 2
    tokenwise = (.5 * .9 + .5 * .1) ** 2
    assert abs(shared - .41) < 1e-12 and tokenwise == .25
    return dict(states=len(states), conditionals=checked, max_error=error,
                whole_document_predictive=reinforced, unchanged_token_product=independent,
                shared_persona_query=shared, independent_token_personas=tokenwise)


def gt():
    # This finite example explicitly uses all three distinct unordered pairs; no self-pairs.
    pairs = [(0, 1), (0, 2), (1, 2)]
    relations = [[1, 1, 1], [0, 0, 1]]
    words = [[0, 0], [1]]
    alpha, eta, beta = [.7, 1.3], [.8, 1.2], [1.1, .9]
    states = list(itertools.product(range(2), repeat=8))  # 2 topics x 3 entities, 2 event topics

    def blocks(s, event, topic, omit_entity=None, only_entity=None):
        out = {(0, 0): [0, 0], (0, 1): [0, 0], (1, 1): [0, 0]}
        for (u, v), r in zip(pairs, relations[event]):
            if omit_entity is not None and omit_entity in (u, v):
                continue
            if only_entity is not None and only_entity not in (u, v):
                continue
            key = tuple(sorted([s[topic * 3 + u], s[topic * 3 + v]]))
            out[key][r] += 1
        return out

    def event_likelihood(s, b, t):
        return math.prod(dm(c, beta) for c in blocks(s, b, t).values())

    def word_counts(s, t, omit_event=None):
        return [sum(w.count(k) for b, w in enumerate(words)
                    if b != omit_event and s[6 + b] == t) for k in range(2)]

    def joint(s, power):
        return (math.prod(dm([s[t * 3:t * 3 + 3].count(k) for k in range(2)], alpha)
                          * dm(word_counts(s, t), eta) ** power for t in range(2))
                * math.prod(event_likelihood(s, b, s[6 + b]) / 2 for b in range(2)))

    error, checked = 0., 0
    for power in (1, 5):
        for state in states:
            for t in range(2):
                for u in range(3):
                    weights, brute = [], []
                    for g in range(2):
                        s = list(state)
                        s[t * 3 + u] = g
                        weight = alpha[g] + sum(state[t * 3 + v] == g for v in range(3) if v != u)
                        for b in range(2):
                            if state[6 + b] != t:
                                continue
                            base = blocks(s, b, t, omit_entity=u)
                            extra = blocks(s, b, t, only_entity=u)
                            weight *= math.prod(dm([c[k] + extra[key][k] for k in range(2)], beta)
                                                / dm(c, beta) for key, c in base.items())
                        weights.append(weight)
                        brute.append(joint(s, power))
                    error = max(error, discrepancy(weights, brute))
                    checked += 1
            for b in range(2):
                weights, brute = [], []
                for t in range(2):
                    c = word_counts(state, t, omit_event=b)
                    h = [words[b].count(k) for k in range(2)]
                    weights.append((dm([c[k] + h[k] for k in range(2)], eta) / dm(c, eta)) ** power
                                   * event_likelihood(state, b, t))
                    s = list(state)
                    s[6 + b] = t
                    brute.append(joint(s, power))
                error = max(error, discrepancy(weights, brute))
                checked += 1
    assert error < 1e-12 and checked == 4096
    literal_indicator_product = math.prod(int(t == 0) for t in [0, 1])
    impossible_vote_assignments = sum(all(v[u] != v[w] for u, w in pairs)
                                     for v in itertools.product(range(2), repeat=3))
    network_probability = dm([3, 0], [1, 1])
    assert literal_indicator_product == 0 and impossible_vote_assignments == 0
    assert abs(network_probability - .25) < 1e-12
    return dict(states_per_power=len(states), powers=[1, 5], conditionals=checked, max_error=error,
                literal_unrelated_event_indicator=literal_indicator_product,
                binary_vote_assignments_for_all_different=impossible_vote_assignments,
                integrated_all_different_network_probability=network_probability)


def gca():
    # Two categorical word positions, two author positions, one timestamp: fixed size.
    matrices = [[[.7, .2], [0., 0.]], [[.3, -.4], [0., 0.]], [[.1, .6], [0., 0.]]]
    states = list(itertools.product(range(2), repeat=5))

    def projection(s, mm):
        cols = [mm[0][s[0]], mm[0][s[1]], mm[1][s[2]], mm[1][s[3]], mm[2][s[4]]]
        return [sum(c[i] for c in cols) for i in range(2)]

    def probabilities(mm):
        return norm([math.exp(.5 * sum(x * x for x in projection(s, mm))) for s in states])

    p = probabilities(matrices)
    q = 2 ** -.5
    rotated = [[[q * (x - y), q * (x + y)] for x, y in matrix] for matrix in matrices]
    rotation_error = max(abs(a - b) for a, b in zip(p, probabilities(rotated)))
    penalty = lambda mm: sum(x * x for matrix in mm for col in matrix for x in col)
    assert rotation_error < 1e-14 and abs(penalty(matrices) - penalty(rotated)) < 1e-14
    target = (0, 1, 0, 0, 0)
    idx = states.index(target)
    statistic = lambda s: s[2:4].count(0) * projection(s, matrices)[0]
    gradient = statistic(target) - sum(pp * statistic(s) for s, pp in zip(states, p))
    eps = 1e-6
    logs = []
    for delta in (-eps, eps):
        mm = [[c[:] for c in m] for m in matrices]
        mm[1][0][0] += delta
        logs.append(math.log(probabilities(mm)[idx]))
    numerical = (logs[1] - logs[0]) / (2 * eps)
    assert abs(gradient - numerical) < 1e-8
    sufficient_count = statistic(target)
    presence_indicator = projection(target, matrices)[0]
    assert abs(sufficient_count - 2 * presence_indicator) < 1e-14
    # Separate fixed-size example: one word, one unknown author, observed time.
    means = [[1.1, .4], [.8, .8]]
    weights = norm([math.exp(.5 * sum(x * x for x in s)) for s in means])
    mean = [sum(w * s[i] for w, s in zip(weights, means)) for i in range(2)]
    variance = [1 + sum(w * (s[i] - mean[i]) ** 2 for w, s in zip(weights, means)) for i in range(2)]
    assert mean != [.8, .8] and all(v > 1 for v in variance)
    return dict(visible_states=len(states), rotation_probability_error=rotation_error,
                exact_gradient=gradient, finite_difference_gradient=numerical,
                author_occurrence_statistic=sufficient_count, presence_statistic=presence_indicator,
                missing_author_weights=weights, missing_author_log_hidden_mean=mean,
                missing_author_log_hidden_variance=variance,
                all_observed_positive_hidden_mean=[math.exp(x + .5) for x in means[0]])


if __name__ == '__main__':
    print(json.dumps(dict(apt=apt(), gt=gt(), gca=gca(), status='PASS'), indent=2))
