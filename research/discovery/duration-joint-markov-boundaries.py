"""Original finite probability witnesses; no fitted data or author implementation.

Check explicit-duration endpoints and joint-versus-marginal Markov structure.
The exact sums validate these examples, not arbitrary model implementations.
"""
from itertools import product
from math import prod, isclose
import json


def close(a, b):
    assert isclose(a, b, rel_tol=1e-11, abs_tol=1e-12), (a, b)


def chain_paths(states, initial, kernel, length):
    return [(path, initial(path[0]) * prod(kernel(a, b) for a, b in zip(path, path[1:])))
            for path in product(states, repeat=length)]


def messages(states, initial, kernel, observed):
    """Finite joint chain state=(latent tuple, observation)."""
    allowed = [[s for s in states if s[-1] == y] for y in observed]
    alpha = [{s: initial(s) for s in allowed[0]}]
    for current in allowed[1:]:
        alpha.append({s: sum(v * kernel(p, s) for p, v in alpha[-1].items()) for s in current})
    beta = [{s: 1.0 for s in allowed[-1]}]
    for current in reversed(allowed[:-1]):
        beta.append({s: sum(kernel(s, n) * v for n, v in beta[-1].items()) for s in current})
    beta.reverse()
    evidence = sum(alpha[-1].values())
    return evidence, [{s: alpha[t][s] * beta[t][s] / evidence for s in allowed[t]} for t in range(len(observed))]


def hsmm():
    states = list(product(range(2), range(1, 4)))
    pi = (0.6, 0.4)
    duration = ((0.2, 0.5, 0.3), (0.6, 0.1, 0.3))
    emit = ((0.8, 0.2), (0.3, 0.7))
    initial = lambda s: pi[s[0]] * duration[s[0]][s[1] - 1]

    def kernel(a, b):
        m, d = a
        n, e = b
        return float(n == m and e == d - 1) if d > 1 else (duration[n][e - 1] if n != m else 0.0)

    for s in states:
        close(sum(kernel(s, n) for n in states), 1)
    paths = chain_paths(states, initial, kernel, 4)
    close(sum(p for _, p in paths), 1)
    obs = (0, 1, 1, 0)
    weight = lambda path, p: p * prod(emit[s[0]][y] for s, y in zip(path, obs))
    exact = sum(weight(path, p) for path, p in paths)
    ending = sum(weight(path, p) for path, p in paths if path[-1][1] == 1)
    alpha = {s: initial(s) * emit[s[0]][obs[0]] for s in states}
    for y in obs[1:]:
        entry = [sum(alpha[(n, 1)] for n in range(2) if n != m) for m in range(2)]
        alpha = {(m, d): (alpha.get((m, d + 1), 0) + entry[m] * duration[m][d - 1]) * emit[m][y]
                 for m, d in states}
    close(exact, sum(alpha.values()))
    close(ending, sum(alpha[(m, 1)] for m in range(2)))
    assert 0 < ending < exact
    # Independent segment recursion integrates durations extending beyond the window.
    def segments(t, m):
        value = 0.0
        for d in range(1, 4):
            k = min(d, len(obs) - t)
            likelihood = prod(emit[m][obs[i]] for i in range(t, t + k))
            value += duration[m][d - 1] * likelihood * (1 if t + d >= len(obs) else segments(t + d, 1 - m))
        return value
    close(exact, sum(pi[m] * segments(0, m) for m in range(2)))
    close(sum(sum(p * prod(emit[s[0]][y] for s, y in zip(path, observations)) for path, p in paths)
              for observations in product(range(2), repeat=4)), 1)
    first_duration_posterior = [sum(weight(path, p) for path, p in paths if path[0][1] == d) / exact for d in range(1, 4)]
    close(sum(first_duration_posterior), 1)
    hazards = [duration[0][i] / sum(duration[0][i:]) for i in range(3)]
    assert hazards == [0.2, 0.625, 1.0]
    return dict(right_censored_evidence=exact, evidence_and_sojourn_end_at_T=ending,
                segment_recursion_agrees=True, first_sojourn_duration_posterior=first_duration_posterior,
                duration_hazards=hazards, augmented_rows_normalized=True)


def joint_models():
    stay = lambda a, b: 0.9 if a == b else 0.1
    emission = lambda x, u: 0.8 if x == u else 0.2
    # PMC: Y is persistent; X is noisy given Y. Z=(X,Y) is Markov.
    states = list(product(range(2), repeat=2))
    initial = lambda z: 0.5 * emission(z[0], z[1])
    kernel = lambda a, b: stay(a[1], b[1]) * emission(b[0], b[1])
    paths = chain_paths(states, initial, kernel, 3)
    close(sum(p for _, p in paths), 1)
    def x_next(x0):
        selected = [(path, p) for path, p in paths if path[0][0] == x0 and path[1][0] == 1]
        return sum(p for path, p in selected if path[2][0] == 1) / sum(p for _, p in selected)
    assert abs(x_next(1) - x_next(0)) > 0.05
    evidence, posterior = messages(states, initial, kernel, (0, 1, 1))
    selected = [(path, p) for path, p in paths if tuple(s[-1] for s in path) == (0, 1, 1)]
    close(sum(p for _, p in selected), evidence)
    for t, marginal in enumerate(posterior):
        for s, p in marginal.items():
            close(p, sum(w for path, w in selected if path[t] == s) / evidence)
    pmc = dict(hidden_p_X3_1_given_X2_1_X1_1=x_next(1), hidden_p_X3_1_given_X2_1_X1_0=x_next(0),
               joint_mass=sum(p for _, p in paths), observed_evidence=evidence, posterior_messages_match_enumeration=True)
    # TMC: U is persistent, X noisy given U, and Y depends on both X and U.
    states = list(product(range(2), repeat=3))
    def sensor(x, u, y):
        p = 0.15 + 0.45 * x + 0.15 * u
        return p if y else 1 - p
    initial = lambda t: 0.5 * emission(t[0], t[1]) * sensor(*t)
    kernel = lambda a, b: stay(a[1], b[1]) * emission(b[0], b[1]) * sensor(*b)
    for s in states:
        close(sum(kernel(s, n) for n in states), 1)
    paths = chain_paths(states, initial, kernel, 3)
    close(sum(p for _, p in paths), 1)
    def projected_next(x0):
        selected = [(path, p) for path, p in paths
                    if (path[0][0], path[0][2]) == (x0, 0) and (path[1][0], path[1][2]) == (1, 1)]
        return sum(p for path, p in selected if (path[2][0], path[2][2]) == (1, 1)) / sum(p for _, p in selected)
    assert abs(projected_next(1) - projected_next(0)) > 0.01
    evidence, posterior = messages(states, initial, kernel, (0, 1, 1))
    selected = [(path, p) for path, p in paths if tuple(s[-1] for s in path) == (0, 1, 1)]
    close(evidence, sum(p for _, p in selected))
    x_posteriors = []
    for t, marginal in enumerate(posterior):
        by_x = [sum(p for s, p in marginal.items() if s[0] == x) for x in range(2)]
        for x, p in enumerate(by_x):
            close(p, sum(w for path, w in selected if path[t][0] == x) / evidence)
        close(sum(by_x), 1)
        x_posteriors.append(by_x)
    # A one-time TMC posterior witnesses max-over-U versus marginalizing U.
    table = ((0.26, 0.25), (0.48, 0.01))
    assert sum(table[0]) > sum(table[1]) and max(table[0]) < max(table[1])
    tmc = dict(projected_p_Z3_11_given_Z2_11_Z1_10=projected_next(1),
               projected_p_Z3_11_given_Z2_11_Z1_00=projected_next(0), joint_mass=sum(p for _, p in paths),
               observed_evidence=evidence, x_posterior_after_summing_U=x_posteriors,
               posterior_messages_match_enumeration=True, marginal_mode_example=[sum(row) for row in table],
               max_over_U_example=[max(row) for row in table])
    return dict(pairwise=pmc, triplet=tmc)


if __name__ == '__main__':
    print(json.dumps(dict(hidden_semi_markov=hsmm(), **joint_models()), indent=2))
