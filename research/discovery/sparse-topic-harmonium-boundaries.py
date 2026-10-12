#!/usr/bin/env python3
"""Finite curator checks; no reproduction of historical code or benchmarks."""
import itertools
import json
import math
from fractions import Fraction as F


def dm(c, a):
    return math.exp(math.lgamma(sum(a)) - math.lgamma(sum(a) + sum(c))
                    + sum(math.lgamma(x + n) - math.lgamma(x) for n, x in zip(c, a)))


def norm(x):
    total = sum(x)
    return [v / total for v in x]


def dcm_lda():
    pages = [0, 0, 1, 2, 3]
    book_for_page = [0, 0, 1, 1]
    words = [0, 0, 1, 0, 1]
    alpha, beta = [.7, 1.3], [[.8, 1.2], [1.1, .9]]
    states = list(itertools.product(range(2), repeat=5))

    def counts(state, omit=None):
        pt = [[0, 0] for _ in range(4)]
        btw = {(b, t): [0, 0] for b in range(2) for t in range(2)}
        for i, (p, w, t) in enumerate(zip(pages, words, state)):
            if i != omit:
                pt[p][t] += 1
                btw[book_for_page[p], t][w] += 1
        return pt, btw

    def joint(state):
        pt, btw = counts(state)
        return math.prod(dm(c, alpha) for c in pt) * math.prod(dm(c, beta[t]) for (b, t), c in btw.items())

    error, checked = 0., 0
    for state in states:
        for i, (p, w) in enumerate(zip(pages, words)):
            pt, btw = counts(state, i)
            weights, brute = [], []
            for t in range(2):
                c = btw[book_for_page[p], t]
                weights.append((pt[p][t] + alpha[t]) / (sum(pt[p]) + sum(alpha))
                               * (c[w] + beta[t][w]) / (sum(c) + sum(beta[t])))
                s = list(state)
                s[i] = t
                brute.append(joint(s))
            error = max(error, max(abs(x - y) for x, y in zip(norm(weights), norm(brute))))
            checked += 1
    assert error < 1e-12 and checked == 160
    same_book = dm([2, 0], [1, 1])
    different_books = dm([1, 0], [1, 1]) ** 2
    assert abs(same_book - 1/3) < 1e-12 and abs(different_books - 1/4) < 1e-12
    p, q = [.5, .5, 0.], [0., .25, .75]
    js = .5 * sum(x * math.log2(2 * x / (x + y)) if x else 0. for x, y in zip(p, q))
    js += .5 * sum(y * math.log2(2 * y / (x + y)) if y else 0. for x, y in zip(p, q))
    sparse = 1 + .5 * sum(x * math.log2(x) + y * math.log2(y)
                         - (x + y) * math.log2((x + y) / 2) - x - y
                         for x, y in zip(p, q) if x and y)
    assert abs(js - sparse) < 1e-14
    return dict(states=len(states), conditionals=checked, max_error=error,
                same_book_two_word_probability=same_book, separate_books_probability=different_books,
                js_base_two=js, shared_support_js=sparse, natural_log_disjoint_js=math.log(2))


def pruned_pam():
    # Proper four-level PAM special case: 2 supertopics, 1 subtopic, 1 word,
    # one 2-token document. Only root allocations are nontrivial; alpha=(1,1).
    states = list(itertools.product(range(2), repeat=2))
    pi = [F(1, 3), F(1, 6), F(1, 6), F(1, 3)]

    def sweep(start, prune):
        distribution = {start: F(1)}
        for i in range(2):
            out = {}
            for state, mass in distribution.items():
                candidates = set(state) if prune else {0, 1}  # pre-removal candidate set
                weights = {t: F(1 + int(state[1-i] == t)) for t in candidates}
                for t, w in weights.items():
                    s = list(state)
                    s[i] = t
                    s = tuple(s)
                    out[s] = out.get(s, F(0)) + mass * w / sum(weights.values())
            distribution = out
        return [distribution.get(s, F(0)) for s in states]

    exact = [sweep(s, False) for s in states]
    pruned = [sweep(s, True) for s in states]
    propagate = lambda p, matrix: [sum(p[i] * matrix[i][j] for i in range(4)) for j in range(4)]
    assert propagate(pi, exact) == pi
    biased = propagate(pi, pruned)
    assert biased == [F(13, 27), F(1, 54), F(1, 54), F(13, 27)]
    assert propagate(propagate(pi, exact), pruned) == biased != pi
    assert pruned[0][0] == pruned[3][3] == 1
    assert all(x > 0 for row in exact for x in row)
    tv = sum(abs(x-y) for x, y in zip(pi, biased)) / 2
    # A fixed retained subset with mass .98 has conditional TV .02; this alone
    # says nothing universal about accumulated/adaptive-chain stationary error.
    full = [F(1, 2), F(12, 25), F(1, 50)]
    restricted = [full[0]/F(49, 50), full[1]/F(49, 50), F(0)]
    assert sum(abs(x-y) for x, y in zip(full, restricted))/2 == F(1, 50)
    # Dirichlet coordinate moment identity versus the manuscript's divided form.
    mean, variance = [.5, .5], [1/12, 1/12]
    concentration = [m*(1-m)/v-1 for m, v in zip(mean, variance)]
    printed_denominator = math.exp(sum(math.log(c) for c in concentration)/(len(mean)-1))
    printed_alpha = [m/printed_denominator for m in mean]
    correct_alpha = [m*concentration[0] for m in mean]
    assert max(abs(x-1) for x in correct_alpha) < 1e-12
    assert max(abs(x-.125) for x in printed_alpha) < 1e-12
    return dict(states=states, target=[str(x) for x in pi], exact_sweep_invariant=True,
                target_after_full_then_pruned=[str(x) for x in biased], total_variation=str(tv),
                full_sweep_positive_support=True, pruned_all_one_topic_states_absorbing=True,
                retained_mass_example='49/50', conditional_tv_example='1/50',
                moment_consistent_alpha=correct_alpha, literal_display_alpha=printed_alpha)


def harmonium():
    # Two count-bin categorical variables with 3 categories; 2 unit-Gaussian hidden units.
    weights = [[[.2, -.3], [.8, .1], [-.4, .6]], [[.3, .2], [-.5, .4], [.1, -.7]]]
    biases = [[.1, -.2, .3], [-.1, .2, .0]]
    states = list(itertools.product(range(3), repeat=2))
    projection = lambda s, w: [sum(w[i][s[i]][j] for i in range(2)) for j in range(2)]

    def probabilities(w, a):
        return norm([math.exp(sum(a[i][s[i]] for i in range(2))
                              + .5*sum(x*x for x in projection(s, w))) for s in states])

    p = probabilities(weights, biases)
    angle = .63
    c, s = math.cos(angle), math.sin(angle)
    rotated = [[[c*x-s*y, s*x+c*y] for x, y in rows] for rows in weights]
    rotation_error = max(abs(x-y) for x, y in zip(p, probabilities(rotated, biases)))
    # Shift every category at position i by v_i; compensate unary energies.
    shifts = [[.2, -.1], [-.1, .4]]
    total = [sum(v[j] for v in shifts) for j in range(2)]
    shifted = [[[x+shifts[i][0], y+shifts[i][1]] for x, y in row] for i, row in enumerate(weights)]
    adjusted = [[biases[i][a]-sum(total[j]*weights[i][a][j] for j in range(2)) for a in range(3)] for i in range(2)]
    shift_error = max(abs(x-y) for x, y in zip(p, probabilities(shifted, adjusted)))
    assert rotation_error < 1e-14 and shift_error < 1e-14
    # Proper Gaussian conditionals h|x~N(wx,1), x|h~N(wh,1) can coexist with
    # a nonnormalizable proposed joint exp[-(x^2+h^2)/2+w*x*h] when |w|>=1.
    w_bad = 1.2
    bad_precision_eigenvalues = [1-w_bad, 1+w_bad]
    assert min(bad_precision_eigenvalues) < 0
    # Positive Poisson-Poisson interaction gives diagonal terms growing like
    # w*n^2-2*log(n!), so they fail even to tend to zero.
    w_pp = .1
    diagonal_log_terms = [w_pp*n*n - 2*math.lgamma(n+1) for n in [100, 1000, 10000]]
    assert diagonal_log_terms[2] > diagonal_log_terms[1] > diagonal_log_terms[0]
    return dict(categorical_states=len(states), rotation_error=rotation_error, compensated_shift_error=shift_error,
                improper_gaussian_joint_precision_eigenvalues=bad_precision_eigenvalues,
                positive_poisson_interaction_diagonal_log_terms=diagonal_log_terms,
                normalizability_note='Local conditional families do not alone certify a finite joint normalizer.')


if __name__ == '__main__':
    print(json.dumps(dict(dcm_lda=dcm_lda(), pruned_pam=pruned_pam(), harmonium=harmonium(), status='PASS'), indent=2))
