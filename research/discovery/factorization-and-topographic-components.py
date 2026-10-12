"""Curator arithmetic checks; no author implementation or empirical benchmark."""
import itertools
import json
import math


def transpose(a):
    return [list(v) for v in zip(*a)]


def multiply(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def squared(v, w, h):
    q = multiply(w, h)
    return sum((v[i][j] - q[i][j]) ** 2 for i in range(len(v)) for j in range(len(v[0])))


def divergence(v, w, h):
    q = multiply(w, h)
    return sum((x * math.log(x / y) if x else 0) - x + y
               for vr, qr in zip(v, q) for x, y in zip(vr, qr))


def h_update(v, w, h, kl=False):
    q = multiply(w, h)
    if kl:
        numerator = multiply(transpose(w), [[x / y for x, y in zip(vr, qr)] for vr, qr in zip(v, q)])
        denominator = [[sum(row)] * len(h[0]) for row in transpose(w)]
    else:
        numerator = multiply(transpose(w), v)
        denominator = multiply(transpose(w), q)
    return [[x * n / d for x, n, d in zip(hr, nr, dr)]
            for hr, nr, dr in zip(h, numerator, denominator)]


v = [[1., 2., 0.], [3., 1., 4.]]
w = [[.8, .3], [.2, .7]]
h = [[.4, .9, .2], [.6, .1, .8]]
descent = {}
for kl, objective in [(False, squared), (True, divergence)]:
    new_h = h_update(v, w, h, kl)
    new_w = transpose(h_update(transpose(v), transpose(new_h), transpose(w), kl))
    values = [objective(v, w, h), objective(v, w, new_h), objective(v, new_w, new_h)]
    assert values[2] <= values[1] <= values[0]
    descent['generalized_kl' if kl else 'squared_error'] = values
simultaneous = [(1 - .5 * .5) ** 2, (1 - 2 * 2) ** 2]
assert simultaneous[1] > simultaneous[0]
locked_w, locked_v, locked_h = [[1., 0.], [1., 1.]], [[1.], [2.]], [[1.5], [0.]]
assert h_update(locked_v, locked_w, locked_h) == locked_h
locked_gradient = multiply(transpose(locked_w), [[.5], [-.5]])
assert locked_gradient[1][0] < 0
assert squared(locked_v, locked_w, [[1.5], [.1]]) < squared(locked_v, locked_w, locked_h)


def det(w):
    return w[0][0] * w[1][1] - w[0][1] * w[1][0]


def inv_transpose(w):
    d = det(w)
    return [[w[1][1] / d, -w[1][0] / d], [-w[0][1] / d, w[0][0] / d]]


samples = [[.2, -.7], [1.1, .4], [-.5, .8]]
weight, bias = [[1.2, .3], [-.2, .9]], [.1, -.15]


def infomax(w, b):
    total = math.log(abs(det(w)))
    for x in samples:
        for row, c in zip(w, b):
            u = sum(a * z for a, z in zip(row, x)) + c
            total += (-math.log1p(math.exp(-u)) - math.log1p(math.exp(u))) / len(samples)
    return total


gradient, bias_gradient = inv_transpose(weight), [0., 0.]
for x in samples:
    for i in range(2):
        u = sum(a * z for a, z in zip(weight[i], x)) + bias[i]
        score = 1 - 2 / (1 + math.exp(-u))
        bias_gradient[i] += score / len(samples)
        for j in range(2):
            gradient[i][j] += score * x[j] / len(samples)
errors = []
eps = 1e-6
for i in range(2):
    for j in range(2):
        plus, minus = [r[:] for r in weight], [r[:] for r in weight]
        plus[i][j] += eps
        minus[i][j] -= eps
        errors.append(abs((infomax(plus, bias) - infomax(minus, bias)) / (2 * eps) - gradient[i][j]))
    plus, minus = bias[:], bias[:]
    plus[i] += eps
    minus[i] -= eps
    errors.append(abs((infomax(weight, plus) - infomax(weight, minus)) / (2 * eps) - bias_gradient[i]))
assert max(errors) < 1e-8
# Under the source generalized-sigmoid ODE, d log(g')/du = (d log(g')/dy) g'.
y, p, r = .3, 2., 3.
chain_score = (p / y - r / (1 - y)) * y ** p * (1 - y) ** r
displayed_score = p * (1 - y) - r * y
assert abs(chain_score - displayed_score * y ** (p - 1) * (1 - y) ** (r - 1)) < 1e-14
assert abs(chain_score - displayed_score) > .1

# Discrete positive latent scales are a finite analogue of the same mixture/bound algebra.
scales = [(u, v, u + .5 * v, .5 * u + v) for u, v in itertools.product([1., 4.], repeat=2)]
q_mass = sum(math.sqrt(u * v / (a * b)) for u, v, a, b in scales) / 4
assert 0 < q_mass < 1


def densities(x, y):
    exact = sum(math.sqrt(a * b) * math.exp(-.5 * (a * x * x + b * y * y))
                for u, v, a, b in scales) / (8 * math.pi)
    lower = sum(math.sqrt(u * v) * math.exp(-.5 * (a * x * x + b * y * y))
                for u, v, a, b in scales) / (8 * math.pi)
    return exact, lower


ratios = []
for x, y in itertools.product([0., .5, 1., 2.], repeat=2):
    exact, lower = densities(x, y)
    assert 0 < lower <= exact
    ratios.append((lower / q_mass) / exact)
assert max(ratios) > 1
mean_a = sum(1 / a for u, v, a, b in scales) / 4
mean_b = sum(1 / b for u, v, a, b in scales) / 4
energy_covariance = sum(1 / (a * b) for u, v, a, b in scales) / 4 - mean_a * mean_b
assert energy_covariance > 0  # E[s1 s2] = 0 by independent zero-mean conditional normals.
neighborhood = [[1., .5], [.5, 1.]]


def tica_contrast(w):
    total = 0.
    for z in samples:
        s = [sum(a * x for a, x in zip(row, z)) for row in w]
        total += sum(-math.sqrt(.01 + sum(h * a * a for h, a in zip(row, s))) for row in neighborhood)
    return total / len(samples)


tica_gradient = [[0., 0.], [0., 0.]]
for z in samples:
    s = [sum(a * x for a, x in zip(row, z)) for row in weight]
    local = [sum(h * a * a for h, a in zip(row, s)) for row in neighborhood]
    for i in range(2):
        modulation = sum(neighborhood[k][i] * (-.5 / math.sqrt(.01 + local[k])) for k in range(2))
        for j in range(2):
            tica_gradient[i][j] += 2 * z[j] * s[i] * modulation / len(samples)
tica_errors = []
for i, j in itertools.product(range(2), repeat=2):
    plus, minus = [r[:] for r in weight], [r[:] for r in weight]
    plus[i][j] += eps
    minus[i][j] -= eps
    tica_errors.append(abs((tica_contrast(plus) - tica_contrast(minus)) / (2 * eps) - tica_gradient[i][j]))
assert max(tica_errors) < 1e-8
print(json.dumps(dict(nmf_block_objectives=descent, nmf_simultaneous_scalar_errors=simultaneous,
                     zero_locked_half_squared_gradient=locked_gradient,
                     infomax_gradient_max_error=max(errors), generalized_sigmoid_scores=[chain_score, displayed_score],
                     tica_lower_bound_mass=q_mass, normalized_surrogate_max_ratio=max(ratios),
                     tica_energy_covariance=energy_covariance, tica_gradient_max_error=max(tica_errors),
                     cauchy_truncated_second_moments=[2 / math.pi * (a - math.atan(a)) for a in [10, 100, 1000]]), indent=2))
