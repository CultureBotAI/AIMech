"""Exact curator examples; not an empirical system-identification benchmark."""
from fractions import Fraction as Q
import json


def main():
    out = {}
    # Chen–Billings1989 Example1 requires an output-inverse branch.
    observe = lambda x: x + x*x
    x1, x2, u = Q(0), Q(-1), Q(1, 4)
    assert observe(x1) == observe(x2) == 0
    a, b = observe(x1 + u), observe(x2 + u)
    assert (a, b) == (Q(5, 16), Q(-3, 16))
    out['hidden_branch'] = {'same_current_output': '0', 'same_input': str(u),
                            'next_outputs': [str(a), str(b)]}
    # Printed pp1023–1024: the specific degree4 error bound fails.
    failures = []
    for y, root in [(Q(-1, 4), Q(0)), (Q(-6, 25), Q(1, 5))]:
        assert root*root == 1 + 4*y
        exact = y + root + 1
        polynomial = y + 1 + 2*y - 2*y*y + 4*y**3 + 1
        error = abs(exact-polynomial)
        assert error > Q(1, 25) > Q(5, 128)
        failures.append({'y': str(y), 'u': '1', 'exact': str(exact),
                         'polynomial': str(polynomial), 'error': str(error)})
    assert failures[1]['error'] == '2336/15625'
    out['published_numerical_bound_counterexamples'] = failures
    # A fixed polynomial basis is coefficient-linear, not input-linear.
    phi = lambda y, u: (Q(1), y, u, y*y, y*u, u*u)
    theta = (Q(1, 3), Q(1, 2), Q(-1), Q(2), Q(3, 5), Q(-2))
    evaluate = lambda t, y, u: sum(a*b for a, b in zip(t, phi(y, u)))
    v = evaluate(theta, Q(1, 2), Q(-1, 3))
    assert evaluate(tuple(2*t for t in theta), Q(1, 2), Q(-1, 3)) == 2*v
    assert evaluate(theta, Q(1), Q(-2, 3)) != 2*v
    out['polynomial_basis'] = {'terms': 6, 'value': str(v),
                               'coefficient_linear': True, 'input_output_linear': False}
    # Linear lagged-error dependence alone does not guarantee forgetting.
    # y_t = u_(t-1)^2 + a e_(t-1) + e_t; same observed y,u.
    results = []
    for coefficient in (Q(1, 2), Q(2)):
        r1, r2 = Q(0), Q(1)
        for t in range(1, 9):
            observed, lag_input = Q(t % 3), Q(t % 2)
            r1 = observed - lag_input**2 - coefficient*r1
            r2 = observed - lag_input**2 - coefficient*r2
            assert r2-r1 == (-coefficient)**t
        results.append({'coefficient': str(coefficient), 'initial_difference': '1',
                        'difference_after_eight_steps': str(r2-r1)})
    assert results[0]['difference_after_eight_steps'] == '1/256'
    assert results[1]['difference_after_eight_steps'] == '256'
    out['residual_initialization'] = results
    # Uniform one-step difference does not imply uniformly bounded rollout error.
    exact, approximate, delta = Q(0), Q(0), Q(1, 100)
    for t in range(1, 9):
        exact, approximate = 2*exact, 2*approximate + delta
        assert approximate-exact == delta*(2**t-1)
    out['error_propagation'] = {'one_step_function_error': str(delta),
                                'eight_step_trajectory_error': str(approximate-exact)}
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
