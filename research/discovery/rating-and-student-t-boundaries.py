"""Finite curator checks of primary-paper equations, not author-code reproduction.

RBM-CF: omitted items change the joint family; a query softplus score is exact
for the augmented visible set, whereas plugging in hidden means is approximate.
PoT: full rank and positive exponents alone do not establish integrability.
For a scalar nonzero filter the tail is |x|^(-2*alpha), requiring alpha>1/2.
A square independent subset with each alpha>1/2 is sufficient for a product:
its integral is finite after an invertible transform and extra factors <=1.
The overcomplete pseudoinverse sampling shortcut has a different covariance.
IWF: exact tangent-majorization steps decrease the objective, but two stable
solutions for the same proper prior demonstrate dependence on initialization.
"""
import itertools
import json
import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def normalize(xs):
    z = sum(xs)
    return [x / z for x in xs]


def check():
    hidden = list(itertools.product([0, 1], repeat=2))
    w = [[[0.2, -0.5], [1.0, 0.7]], [[-0.6, 0.4], [0.8, -0.2]],
         [[-0.2, 1.3], [1.4, -0.7]]]
    bias = [[0.1, -0.3], [0.2, 0.0], [-0.4, 0.6]]
    c = [-0.2, 0.3]

    def mass(v, h):
        return math.exp(sum(c[j] * h[j] for j in range(2)) +
                        sum(bias[i][k] + sum(w[i][k][j] * h[j] for j in range(2))
                            for i, k in enumerate(v)))

    errors = []
    plugin_gaps = []
    marginal_pairs = []
    observed = list(itertools.product([0, 1], repeat=2))
    omitted = normalize([sum(mass(v, h) for h in hidden) for v in observed])
    integrated = normalize([sum(mass(v + (k,), h) for k in [0, 1] for h in hidden)
                            for v in observed])
    for v in observed:
        a = [c[j] + sum(w[i][k][j] for i, k in enumerate(v)) for j in range(2)]
        ph = [sigmoid(x) for x in a]
        exact = normalize([sum(mass(v + (k,), h) for h in hidden) for k in [0, 1]])
        score = normalize([math.exp(bias[2][k]) * math.prod(1 + math.exp(a[j] + w[2][k][j])
                                                                         for j in range(2))
                           for k in [0, 1]])
        plugin = normalize([math.exp(bias[2][k] + sum(ph[j] * w[2][k][j] for j in range(2)))
                            for k in [0, 1]])
        errors.extend(abs(x - y) for x, y in zip(exact, score))
        plugin_gaps.append(max(abs(x - y) for x, y in zip(exact, plugin)))
        actual_hidden = normalize([mass(v, h) for h in hidden])
        expected_hidden = [math.prod(ph[j] if h[j] else 1 - ph[j] for j in range(2))
                           for h in hidden]
        errors.extend(abs(x - y) for x, y in zip(actual_hidden, expected_hidden))
        marginal_pairs.append(dict(observed=list(v), exact_query=exact, plugin_query=plugin))
    assert max(errors) < 1e-12
    assert max(plugin_gaps) > 0.01
    assert max(abs(x - y) for x, y in zip(omitted, integrated)) > 0.01

    # Gamma integral: int u^(alpha-1) exp(-rate*u) du = Gamma(alpha)/rate^alpha.
    gamma_checks = []
    for alpha in [0.25, 0.75, 1.0, 2.5]:
        for z in [-3.0, 0.0, 2.0]:
            rate = 1 + z * z / 2
            integrated_factor = math.gamma(alpha) / rate**alpha
            gamma_checks.append(abs(integrated_factor / math.gamma(alpha) - rate**(-alpha)))
    assert max(gamma_checks) < 1e-12
    # J=[1,1], u=(1,4). Exact Q=5; (J^T)^+ = [1/2,1/2].
    exact_variance = 1 / 5
    pseudoinverse_variance = (1 / 2)**2 * (1 / 1 + 1 / 4)
    assert pseudoinverse_variance == 5 / 16 != exact_variance
    # Two individually nonintegrable scalar factors with alpha=.375 each
    # multiply to an integrable exponent .75; expert factors need not be densities.
    alpha_total = 0.75
    product_z = math.sqrt(2 * math.pi) * math.gamma(alpha_total - 0.5) / math.gamma(alpha_total)
    assert math.isfinite(product_z) and product_z > 0

    alpha, y = 10.0, 8.5

    def objective(x):
        return (x - y)**2 / 2 + alpha * math.log1p(x * x / 2)

    max_bound_violation = 0.0
    for anchor in [-5, 0, 2, 8.5]:
        gamma = 1 / (1 + anchor * anchor / 2)
        for trial in [-10, -1, 0, 3, 10]:
            t = 1 + trial * trial / 2
            max_bound_violation = max(max_bound_violation, math.log(t) - (gamma*t - math.log(gamma) - 1))
    assert max_bound_violation < 1e-12
    runs = []
    for initial in [0.0, y]:
        x = initial
        objectives = [objective(x)]
        for steps in range(10000):
            gamma = 1 / (1 + x*x/2)
            nxt = y / (1 + alpha*gamma)
            objectives.append(objective(nxt))
            assert objectives[-1] <= objectives[-2] + 1e-12
            if abs(nxt-x) < 1e-13:
                x = nxt
                break
            x = nxt
        else:
            raise AssertionError('No convergence in the declared finite check')
        stationary = x-y + alpha*x/(1+x*x/2)
        hessian = 1 + alpha*(1-x*x/2)/(1+x*x/2)**2
        assert abs(stationary) < 1e-11 and hessian > 0
        runs.append(dict(initial=initial, solution=x, objective=objective(x),
                         stationary_residual=stationary, hessian=hessian, iterations=steps+1))
    assert abs(runs[0]['solution']-runs[1]['solution']) > 2
    assert runs[1]['objective'] > runs[0]['objective'] + 0.05
    return dict(rbm=dict(max_exact_error=max(errors), omitted_item_distribution=omitted,
                         integrated_item_distribution=integrated, predictions=marginal_pairs,
                         max_plugin_gap=max(plugin_gaps)),
                pot=dict(gamma_factor_max_error=max(gamma_checks), exact_conditional_variance=exact_variance,
                         pseudoinverse_variance=pseudoinverse_variance,
                         scalar_integrability_threshold='sum(alpha)>1/2 for identical nonzero scalar filters',
                         scalar_product_alpha=alpha_total, scalar_product_normalizer=product_z),
                iwf=dict(max_bound_violation=max_bound_violation, runs=runs,
                         conclusion='Both runs decrease the objective to distinct strict local minima; the higher one is not global.'))


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
