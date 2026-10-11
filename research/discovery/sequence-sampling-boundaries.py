"""Curator finite examples; not author code, a statistical test or a decoder benchmark."""
from fractions import Fraction as F
from itertools import permutations
from math import exp, log, isclose
import json


def calculate():
    p = {'a': F(1, 2), 'b': F(1, 3), 'c': F(1, 6)}
    ordered = {(a, b): p[a] * p[b] / (1 - p[a]) for a, b in permutations(p, 2)}
    assert sum(ordered.values()) == 1
    inclusion_c = sum(q for ab, q in ordered.items() if 'c' in ab)
    assert inclusion_c == F(5, 12) and inclusion_c != 2 * p['c']
    assert ordered['a', 'b'] == F(1, 3) and ordered['b', 'a'] == F(1, 4)

    # Fixed real numbers check the conditional-maximum transform algebra only.
    raw = [-1.0, 2.0, 0.5]
    maximum, target = max(raw), 0.25
    shifted = [-log(exp(-target) - exp(-maximum) + exp(-g)) for g in raw]
    assert isclose(max(shifted), target)
    assert sorted(range(3), key=lambda i: raw[i]) == sorted(range(3), key=lambda i: shifted[i])

    # Complete finite tree with declared perturbed leaf scores; no random draws.
    leaves = {'aa': 3.0, 'ab': 2.0, 'ba': 1.0, 'bb': 0.5, 'ca': 0.0, 'cb': -1.0}
    prefixes = {x: max(v for y, v in leaves.items() if y.startswith(x)) for x in 'abc'}
    retained = sorted(prefixes, key=prefixes.get, reverse=True)[:2]
    top_leaves = sorted(leaves, key=leaves.get, reverse=True)[:2]
    pruned_top = sorted((y for y in leaves if y[0] in retained), key=leaves.get, reverse=True)[:2]
    assert top_leaves == pruned_top == ['aa', 'ab']
    assert len({x[0] for x in top_leaves}) == 1

    # One decoding step, B=2/G=2, B'=1, negative token-overlap diversity.
    scores = {'a': -0.1, 'b': -0.2, 'c': -0.3}
    first = max(scores, key=scores.get)
    second_zero = max(scores, key=scores.get)
    strength = 0.15
    second_diverse = max(scores, key=lambda t: scores[t] - strength * (t == first))
    ordinary_width_two = sorted(scores, key=scores.get, reverse=True)[:2]
    assert [first, second_zero] == ['a', 'a']
    assert [first, second_diverse] == ordinary_width_two == ['a', 'b']
    return {
        'ordered_without_replacement': {','.join(k): str(v) for k, v in ordered.items()},
        'c_inclusion_probability': str(inclusion_c),
        'incorrect_k_times_p_c': str(2 * p['c']),
        'conditional_transform': {'raw': raw, 'target': target, 'transformed': shifted},
        'prefix_maximum_example': {'retained_prefixes': retained, 'top_leaves': top_leaves},
        'dbs_one_step': {'zero_diversity_groups': [first, second_zero],
                         'positive_diversity_groups': [first, second_diverse],
                         'ordinary_width_two': ordinary_width_two},
        'scope': 'Exact small arithmetic and fixed-score boundary illustrations; no full implementation, random simulation, author code or general proof.'}


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
