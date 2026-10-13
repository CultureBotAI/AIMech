"""Constructed GF-RNN gate/transition checks; no author code or training."""
import json
import math

sigmoid = lambda x: 1 / (1 + math.exp(-x))


def scalar_feedback(h):
    return math.tanh(sigmoid(h) * 4 * h)


eps = 1e-6
derivative_at_zero = (scalar_feedback(eps) - scalar_feedback(-eps)) / (2 * eps)
assert math.isclose(derivative_at_zero, 2.0, rel_tol=1e-8)
pair_gates = [sigmoid(0.0)] * 3
assert sum(pair_gates) == 1.5
previous = [0.2, 0.4]
recurrent = sum(0.5 * 0.1 * h for h in previous)
lower_now = math.tanh(0.8 * 0.3 + recurrent)
upper_now = math.tanh(0.8 * lower_now + recurrent)
upper_using_old_lower = math.tanh(0.8 * previous[0] + recurrent)
assert not math.isclose(upper_now, upper_using_old_lower)
print(json.dumps(dict(pair_gate_sum=sum(pair_gates), scalar_transition_derivative_at_zero=derivative_at_zero,
                     current_lower_state=lower_now, current_upper_state=upper_now,
                     upper_using_old_lower=upper_using_old_lower,
                     interpretation='Independent sigmoid pair gates need not sum to one or guarantee contraction; current bottom-up input differs from previous recurrent inputs.')))
