"""Exact broadcast-mean examples; not a trained CommNet."""
from fractions import Fraction as F
from itertools import permutations
import json


def means(values):
    if len(values) < 2:
        raise ValueError('The paper denominator J-1 is zero for one agent.')
    return [(sum(values) - x) / (len(values) - 1) for x in values]


values = list(map(F, [2, 5, 11]))
communication = means(values)
assert communication == [F(8), F(13, 2), F(7, 2)]
# One chosen linear step after a communication vector is available.
step = [2 * h + 3 * c for h, c in zip(values, communication)]
assert step == [F(28), F(59, 2), F(65, 2)]
for order in permutations(range(3)):
    permuted = [values[i] for i in order]
    assert means(permuted) == [communication[i] for i in order]
    assert [2 * h + 3 * c for h, c in zip(permuted, means(permuted))] == [step[i] for i in order]
naive = [sum(v for k, v in enumerate(values) if k != j) / 2 for j in range(3)]
assert naive == communication
inclusive_mean = sum(values) / 3
assert any(x != inclusive_mean for x in communication)
assert means([F(2), F(5)]) == [F(5), F(2)]
assert sum([F(2), F(4)]) / 2 == sum([F(1), F(5)]) / 2
try:
    means([F(2)])
except ValueError:
    singleton_undefined = True
else:
    singleton_undefined = False
assert singleton_undefined
# Local neighborhood {1} for receiver 0 is different from the global broadcast.
local_receiver_zero = values[1]
assert local_receiver_zero != communication[0]
counts = [dict(agents=n, naive_other_agent_terms=n * (n - 1), shared_total_additions=n - 1,
               per_agent_subtractions=n, per_agent_divisions=n) for n in [2, 4, 8]]
print(json.dumps(dict(hidden_states=list(map(str, values)), exclude_self_means=list(map(str, communication)),
                     chosen_step=list(map(str, step)), inclusive_mean=str(inclusive_mean),
                     local_receiver_zero=str(local_receiver_zero), permutations_checked=6,
                     singleton_formula_undefined=singleton_undefined, mean_collision=[[2, 4], [1, 5]],
                     arithmetic_counts=counts,
                     scope='Exact tiny pooling examples; not training, physical communication cost, author-code behavior, independent actions, or empirical generalization evidence.')))
