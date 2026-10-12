"""Finite curator calculations for kernel PCA, GTM and FastICA.

These synthetic algebra checks do not reproduce author software or benchmarks.
Run with Python's standard library only.
"""
import itertools
import json
import math


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def close(a, b, tol=1e-10):
    assert abs(a - b) < tol, (a, b)


def unit(a):
    n = math.sqrt(dot(a, a))
    assert n > 1e-14
    return [x / n for x in a]


def phi(x):
    return [x[0] ** 2, x[1] ** 2, math.sqrt(2) * x[0] * x[1]]


train = [[1., 0.], [0., 1.]]
features = [phi(x) for x in train]
mean = [sum(row[j] for row in features) / 2 for j in range(3)]
centered = [[row[j] - mean[j] for j in range(3)] for row in features]
k = [[dot(a, b) ** 2 for b in train] for a in train]
kc = [[k[i][j] - sum(k[i]) / 2 - sum(row[j] for row in k) / 2
       + sum(map(sum, k)) / 4 for j in range(2)] for i in range(2)]
for i, j in itertools.product(range(2), repeat=2):
    close(kc[i][j], dot(centered[i], centered[j]))
v = unit([1., -1.])
kappa = 1.
alpha = [a / math.sqrt(kappa) for a in v]
axis = [sum(alpha[i] * centered[i][j] for i in range(2)) for j in range(3)]
close(dot(axis, axis), 1.)
close(dot(v, [dot(row, v) for row in kc]), kappa)
cov_variance = sum(dot(axis, row) ** 2 for row in centered) / 2
close(cov_variance, kappa / 2)
test = [2., 1.]
raw = [dot(test, x) ** 2 for x in train]
kt = [raw[i] - sum(raw) / 2 - sum(k[i]) / 2 + sum(map(sum, k)) / 4
      for i in range(2)]
project_kernel = dot(alpha, kt)
project_explicit = dot(axis, [a - m for a, m in zip(phi(test), mean)])
close(project_kernel, project_explicit)
close(project_kernel, 3 / math.sqrt(2))
# Centered inputs +/-1 have constant quadratic features, which center to zero.
input_mean = (-1 + 1) / 2
feature_mean = ((-1) ** 2 + 1 ** 2) / 2
close(input_mean, 0.); close(feature_mean, 1.)
# The feature mean (.5,.5,0) has no real quadratic-map preimage.
required_cross_squared = 2 * mean[0] * mean[1]
assert required_cross_squared > mean[2] ** 2
# A tanh similarity need not be PSD, even after Gram centering.
a, b, c = math.tanh(1), math.tanh(2), math.tanh(4)
tanh_det = a * c - b * b
tanh_centered_nonzero_eigenvalue = (a + c - 2 * b) / 2
assert tanh_det < 0 and tanh_centered_nonzero_eigenvalue < 0


def gtm_responsibilities(points, centers, beta):
    rows = []
    likelihood = 0.
    d = len(points[0])
    for t in points:
        logs = [-beta * sum((x - y) ** 2 for x, y in zip(t, m)) / 2
                for m in centers]
        top = max(logs)
        weights = [math.exp(z - top) for z in logs]
        total = sum(weights)
        rows.append([w / total for w in weights])
        likelihood += d / 2 * math.log(beta / (2 * math.pi)) + top + math.log(total / len(centers))
    return rows, likelihood


nodes = [-1., 0., 1.]
basis = [[1., x] for x in nodes]
w = [[.2, .7], [-.1, .3]]
points = [[-.8, -.3], [-.4, .2], [.3, 0.], [.9, .4]]
centers = [[dot(row, f) for row in w] for f in basis]
r, ll_before = gtm_responsibilities(points, centers, 2.)
for row in r:
    close(sum(row), 1.)
g = [sum(row[i] for row in r) for i in range(3)]
normal = [[sum(g[i] * basis[i][a] * basis[i][b] for i in range(3))
           for b in range(2)] for a in range(2)]
rhs = [[sum(r[n][i] * basis[i][a] * points[n][d]
            for n in range(4) for i in range(3)) for d in range(2)] for a in range(2)]
det = normal[0][0] * normal[1][1] - normal[0][1] * normal[1][0]
assert det > 0
inv = [[normal[1][1] / det, -normal[0][1] / det],
       [-normal[1][0] / det, normal[0][0] / det]]
w_new = [[sum(inv[a][b] * rhs[b][d] for b in range(2)) for a in range(2)] for d in range(2)]
new_centers = [[dot(row, f) for row in w_new] for f in basis]
residual = sum(r[n][i] * sum((points[n][d] - new_centers[i][d]) ** 2 for d in range(2))
               for n in range(4) for i in range(3))
beta_new = 8 / residual
_, ll_after = gtm_responsibilities(points, new_centers, beta_new)
assert ll_after >= ll_before
stationarity = max(abs(sum(normal[a][b] * w_new[d][b] for b in range(2)) - rhs[a][d])
                   for a in range(2) for d in range(2))
assert stationarity < 1e-12
# A smooth map with everywhere unit derivative norm can identify distant nodes.
fold_nodes = [-math.pi, 0., math.pi]
circle = [[math.cos(x), math.sin(x)] for x in fold_nodes]
fold_r, _ = gtm_responsibilities([[-1., 0.]], circle, 10.)
posterior_mean = dot(fold_nodes, fold_r[0])
close(posterior_mean, 0.)
assert fold_r[0][1] < 1e-8 and fold_r[0][0] > .49 and fold_r[0][2] > .49


def cubic_step(distribution, vector):
    return [sum(p * s[j] * dot(vector, s) ** 3 for s, p in distribution) - 3 * vector[j]
            for j in range(2)]


# Non-Gaussian, finite-support, mean-zero, unit-variance distribution with kurtosis zero.
zero_kurt = [(-math.sqrt(3), 1 / 6), (0., 2 / 3), (math.sqrt(3), 1 / 6)]
m2 = sum(p * x ** 2 for x, p in zero_kurt)
m4 = sum(p * x ** 4 for x, p in zero_kurt)
close(m2, 1.); close(m4, 3.)
distribution = [([x, y], px * py) for x, px in zero_kurt for y, py in zero_kurt]
zero_update = cubic_step(distribution, [.8, .6])
assert max(map(abs, zero_update)) < 1e-12
# Two Rademacher sources have kurtosis -2. A symmetric tied start stays mixed up to sign.
rad = [([x, y], .25) for x in [-1., 1.] for y in [-1., 1.]]
tied = unit([1., 1.])
tied_next = unit(cubic_step(rad, tied))
close(abs(dot(tied, tied_next)), 1.)
assert min(map(abs, tied_next)) > .7
ordinary = [.8, .6]
ordinary_next = unit(cubic_step(rad, ordinary))
close(abs(ordinary_next[1] / ordinary_next[0]), (.6 / .8) ** 3)
# Iterative symmetric decorrelation cannot turn an exact zero eigenvalue into one.
def decorrelation_eigenvalue(lam):
    return 2.25 * lam - 1.5 * lam ** 2 + .25 * lam ** 3
close(decorrelation_eigenvalue(0.), 0.)
assert .25 < decorrelation_eigenvalue(.25) < 1.

print(json.dumps({
    'kernel_pca': {'gram_eigenvalue': kappa, 'covariance_eigenvalue': cov_variance,
                   'test_projection_kernel': project_kernel, 'test_projection_explicit': project_explicit,
                   'input_mean': input_mean, 'quadratic_feature_mean': feature_mean,
                   'feature_mean_required_cross_squared': required_cross_squared,
                   'tanh_gram_determinant': tanh_det,
                   'tanh_centered_nonzero_eigenvalue': tanh_centered_nonzero_eigenvalue},
    'gtm': {'log_likelihood_before': ll_before, 'log_likelihood_after_one_exact_update': ll_after,
            'new_precision': beta_new, 'normal_equation_max_error': stationarity,
            'folded_map_responsibilities': fold_r[0], 'posterior_mean': posterior_mean},
    'fastica': {'zero_kurtosis_source_second_moment': m2, 'fourth_moment': m4,
                'two_source_cubic_update': zero_update, 'tied_mixed_start_next': tied_next,
                'untied_ratio_after_update': abs(ordinary_next[1] / ordinary_next[0]),
                'zero_decorrelation_eigenvalue_after_update': decorrelation_eigenvalue(0.)},
    'scope': 'Finite synthetic arithmetic only; no author software, training or empirical benchmark reproduced.'
}, indent=2))
