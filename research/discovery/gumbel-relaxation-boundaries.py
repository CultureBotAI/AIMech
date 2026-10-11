"""Curator arithmetic and fixed-tree accounting; no model or author implementation."""
from fractions import Fraction as F
from math import exp, log
import json


def fixed_tree_trace(parallelism):
    leaves = {'AAA': 1, 'AAC': 2, 'ACA': 9, 'ACC': 7,
              'CAA': 8, 'CAC': 3, 'CCA': 5, 'CCC': 4}
    score = lambda prefix: max(v for key, v in leaves.items() if key.startswith(prefix))
    queue, result, remaining, iterations, expansions = [''], [], 3, 0, 0
    trace = []
    while queue:
        iterations += 1
        chosen, queue = queue[:parallelism], queue[parallelism:]
        for prefix in chosen:
            if len(prefix) == 3:
                queue.append(prefix)
            else:
                queue.extend([prefix + x for x in 'AC'])
                expansions += 1
        queue = sorted(queue, key=score, reverse=True)[:remaining]
        while queue and len(queue[0]) == 3:
            result.append(queue.pop(0))
            remaining -= 1
        trace.append({'expanded_or_retained': chosen, 'frontier': queue.copy(), 'emitted': result.copy()})
    assert result == ['ACA', 'CAA', 'ACC']
    return dict(result=result,iterations=iterations,actual_expansions=expansions,
                processor_slots=iterations*parallelism,trace=trace)


def calculate():
    # n=2, equal weights, tau=1: the Concrete density is uniform on (0,1).
    densities = {}
    for x in [F(1,4), F(1,2), F(3,4)]:
        density = (x**-2 * (1-x)**-2) / (x**-1 + (1-x)**-1)**2
        assert density == 1
        densities[str(x)] = str(density)

    # Fixed perturbed log scores [log(3),0] at tau=1 give y1=3/4.
    y, jacobian = F(3,4), F(3,16)
    soft_sample_gradient = 2*y*jacobian
    straight_through_sample_gradient = 2*F(1)*jacobian
    assert soft_sample_gradient == F(9,32)
    assert straight_through_sample_gradient == F(3,8)
    # For equal logits and tau=1, y1 is uniform. With loss f(y)=y1^2,
    # ST expectation is integral from 1/2 to 1 of 2*y*(1-y) dy.
    primitive = lambda x: x*x - F(2,3)*x*x*x
    expected_st = primitive(F(1))-primitive(F(1,2))
    exact_discrete_gradient = F(1,4)  # derivative of sigmoid(theta) at theta=0
    assert expected_st == F(1,6) and expected_st != exact_discrete_gradient
    temperature_samples = {str(t): 1/(1+exp(-log(3)/t)) for t in [0.1,1,100]}
    assert temperature_samples['0.1'] > temperature_samples['1'] > temperature_samples['100'] > 0.5
    serial, parallel = fixed_tree_trace(1), fixed_tree_trace(3)
    assert (serial['iterations'],serial['actual_expansions'],serial['processor_slots']) == (5,5,5)
    assert (parallel['iterations'],parallel['actual_expansions'],parallel['processor_slots']) == (3,6,9)
    return dict(binary_concrete_density=densities,
                fixed_sample=dict(soft_gradient=str(soft_sample_gradient),straight_through_gradient=str(straight_through_sample_gradient)),
                exact_bias_example=dict(expected_st=str(expected_st),discrete_objective_gradient=str(exact_discrete_gradient)),
                temperature_samples=temperature_samples,serial_tree=serial,parallel_tree=parallel,
                scope='Original exact polynomial arithmetic and synthetic fixed leaf-score accounting. This is not a Monte Carlo experiment, a model evaluation, author code or a general algorithm proof.')


if __name__ == '__main__':
    print(json.dumps(calculate(),indent=2))
