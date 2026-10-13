"""Constructed clock schedule, topology and finite-count checks; no training."""
import json
import math

g, k = 3, 2
periods = [1, 2, 4]
parameters = k * k * g * (g + 1) // 2
per_phase = [sum(k * k * (g - i) for i, period in enumerate(periods) if t % period == 0)
             for t in range(4)]
average = sum(per_phase) / len(per_phase)
finite_sum = sum((g - i) / (2 ** i) for i in range(g))
assert parameters == 24 and per_phase == [24, 12, 20, 12]
assert average == k * k * finite_sum == 17
assert finite_sum == 2 * g - 2 + 2 ** (1 - g)
assert average > k * k * (2 * g - 2)


def step(old, x, t):
    fast = math.tanh(x + 0.5 * old[0] + 0.2 * old[1])
    slow = math.tanh(x + 0.4 * old[1]) if t % 2 == 0 else old[1]
    return [fast, slow]


a1, b1 = step([0, 0.5], 1, 1), step([0, 0.5], 3, 1)
a2, b2 = step(a1, 0, 2), step(b1, 0, 2)
assert a1[1] == b1[1] == 0.5 and a2[1] == b2[1]
assert a2[0] != b2[0]
eps = 1e-6
active_derivative = (math.tanh(4 * eps) - math.tanh(-4 * eps)) / (2 * eps)
assert math.isclose(active_derivative, 4.0, rel_tol=1e-8)
print(json.dumps(dict(recurrent_parameters=parameters, dense_recurrent_parameters=(g*k)**2,
                     operations_by_phase=per_phase, average_recurrent_operations=average,
                     appendix_intermediate_expression=k*k*(2*g-2), positive_remainder=k*k*2**(1-g),
                     distinct_input_paths=[a2, b2], active_scalar_derivative=active_derivative,
                     interpretation='Whole clock-cycle recurrence counts exclude input/output, nonlinear, copy and hardware costs; the unobserved transient affects the fast state but not this slow module.')))
