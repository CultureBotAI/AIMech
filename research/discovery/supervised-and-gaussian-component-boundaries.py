"""Finite checks for supervised components and Gaussian latent models.

Curator arithmetic, not historical software, training or empirical reproduction.
"""

import json
import math


def dot(a, b):
    return sum(x * y for x, y in zip(a, b, strict=True))


def close(a, b):
    assert math.isclose(a, b, rel_tol=1e-10, abs_tol=1e-10), (a, b)


def matvec(a, x):
    return [dot(row, x) for row in a]


def det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def inverse(a):
    d = det(a)
    assert d > 0
    return [[a[1][1] / d, -a[0][1] / d],
            [-a[1][0] / d, a[0][0] / d]]


def covariance(w, psi):
    return [[w[i] * w[j] + (psi[i] if i == j else 0)
             for j in range(2)] for i in range(2)]


def score(s, c):
    """Minus twice per-observation Gaussian log likelihood, up to constants."""
    inv = inverse(c)
    return math.log(det(c)) + sum(s[i][j] * inv[j][i]
                                  for i in range(2) for j in range(2))


u = [0.5, 0.5, -0.5, -0.5]
v = [0.5, -0.5, 0.5, -0.5]
columns = [[3 * z for z in u], v, [2 * z for z in v]]
y = [2 * z for z in v]
scores = [dot(x, y) / math.sqrt(dot(x, x)) for x in columns]
assert scores == [0.0, 2.0, 2.0]
selected = [j for j, s in enumerate(scores) if abs(s) > 1]
assert selected == [1, 2]
# XX^T has eigenvalues 9 along u and 5 along v; screened XX^T retains v.
close(sum(dot(x, u) ** 2 for x in columns), 9)
close(sum(dot(x, v) ** 2 for x in columns), 5)
close(dot(u, y), 0)
close(dot(v, y), 2)
loading = [1 / math.sqrt(5), 2 / math.sqrt(5)]
projection_weights = [z / math.sqrt(5) for z in loading]
new_score = dot([3, 6], projection_weights)
close(new_score, 3)
close(2 * new_score, 6)
# With response 2u, only the nuisance column survives and its fitted value is 2u.
# With response 2u+2v, all survive; the leading retained component is u, not v.
sum_response = [2 * a + 2 * b for a, b in zip(u, v, strict=True)]
assert all(abs(dot(x, sum_response) / math.sqrt(dot(x, x))) > 1
           for x in columns)
assert [2 * a for a in u] != sum_response
# Independent unit-variance Z1,Z2: X1=Z1+Z2, X2=Z1, Y=Z1-Z2.
x1, x2, target = [1, 1], [1, 0], [1, -1]
close(dot(x1, target), 0)
close(dot(x2, target), 1)
assert [2 * b - a for a, b in zip(x1, x2, strict=True)] == target
spca = dict(marginal_scores=scores, selected=selected,
            full_component_variances=[9, 5], new_sample_prediction=6,
            jointly_informative_zero_marginal_covariance=dot(x1, target))

# Factor analysis: unequal diagonal residuals change the leading covariance axis.
w, psi = [1, 2], [1, 3]
c = covariance(w, psi)
assert c == [[2, 2], [2, 7]]
cw = matvec(c, w)
assert cw[1] * w[0] != cw[0] * w[1]
posterior_variance = 1 / (1 + sum(wi * wi / pi for wi, pi in zip(w, psi)))
posterior_mean = posterior_variance * sum(wi * xi / pi
    for wi, xi, pi in zip(w, [2, 3], psi, strict=True))
close(posterior_variance, 0.3)
close(posterior_mean, 1.2)
close(posterior_mean ** 2 + posterior_variance, 1.74)
assert covariance([-z for z in w], psi) == c
scaled_c = covariance([2 * w[0], 3 * w[1]], [4 * psi[0], 9 * psi[1]])
assert scaled_c == [[4 * c[0][0], 6 * c[0][1]],
                    [6 * c[1][0], 9 * c[1][1]]]
assert det(covariance([1, 0], [0, 1])) == 1
assert det(covariance([1, 0], [0, 0])) == 0
# Complete-data EM with one latent factor and fixed latent variance one.
s = [[2, 0.5], [0.5, 3]]
old_w, old_psi = [1, 1], [1, 2]
old_c = covariance(old_w, old_psi)
gamma = matvec(inverse(old_c), old_w)
latent_variance = 1 - dot(old_w, gamma)
cross = matvec(s, gamma)
second = latent_variance + dot(gamma, cross)
new_w = [z / second for z in cross]
new_psi = [s[j][j] - cross[j] ** 2 / second for j in range(2)]
assert all(z > 0 for z in new_psi)
close(second, 0.92)
assert score(s, covariance(new_w, new_psi)) < score(s, old_c)
fa = dict(posterior_mean=posterior_mean, posterior_variance=posterior_variance,
          latent_second_moment=1.74, em_loading=new_w, em_uniqueness=new_psi,
          old_score=score(s, old_c), new_score=score(s, covariance(new_w, new_psi)))


def gaussian(x, mean, diag):
    return math.exp(-0.5 * sum((a - b) ** 2 / z
        for a, b, z in zip(x, mean, diag, strict=True))) / (2 * math.pi * math.sqrt(math.prod(diag)))


def likelihood(data, components):
    return sum(math.log(sum(pi * gaussian(x, mu, diag)
        for pi, mu, diag in components)) for x in data)


data = [[-3, -1], [-3, 1], [-1, 0], [1, 0], [3, -1], [3, 1]]
old = [(0.5, [-1, 0], [2, 1]), (0.5, [1, 0], [2, 1])]
responsibilities = []
for x in data:
    weights = [pi * gaussian(x, mu, diag) for pi, mu, diag in old]
    responsibilities.append([z / sum(weights) for z in weights])
eigen_update, gem_update = [], []
for i in range(2):
    weights = [r[i] for r in responsibilities]
    mass = sum(weights)
    mu = [sum(r * x[j] for r, x in zip(weights, data)) / mass for j in range(2)]
    scatter = [[sum(r * (x[j] - mu[j]) * (x[k] - mu[k])
        for r, x in zip(weights, data)) / mass for k in range(2)] for j in range(2)]
    close(scatter[0][1], 0)
    sx, sy = scatter[0][0], scatter[1][1]
    assert sx > sy > 0
    eigen_update.append((mass / len(data), mu, [sx, sy]))
    # One inner PPCA EM step: old W=(1,0), noise=1 and M=2.
    loading_new = sx / (1 + sx / 2)
    noise_new = (sx + sy - sx * loading_new / 2) / 2
    assert noise_new > 0
    gem_update.append((mass / len(data), mu, [loading_new ** 2 + noise_new, noise_new]))
before, after_eigen, after_gem = [likelihood(data, m) for m in [old, eigen_update, gem_update]]
assert after_eigen > before and after_gem > before
close(likelihood(data, list(reversed(old))), before)
# Density can favor a component with larger orthogonal reconstruction error.
pa = gaussian([10, 0], [0, 0], [5, 1])
pb = gaussian([10, 0], [10, 2], [5, 1])
assert pb > pa
close(pb / pa, math.exp(8))
# A shrinking component at one observation makes unconstrained mixture likelihood diverge.
collapse_data = [[0, 0], [1, 0]]
collapse_scores = [likelihood(collapse_data,
    [(0.5, [0, 0], [eps, eps]), (0.5, [0, 0], [1, 1])])
    for eps in [1e-2, 1e-4, 1e-6]]
assert collapse_scores[0] < collapse_scores[1] < collapse_scores[2]
mppca = dict(old_log_likelihood=before, eigen_log_likelihood=after_eigen,
             gem_log_likelihood=after_gem, density_ratio=pb / pa,
             reconstruction_errors=[0, 4], collapse_log_likelihoods=collapse_scores)
print(json.dumps(dict(supervised_components=spca, factor_analysis=fa, ppca_mixture=mppca,
    scope="Finite arithmetic and analytic moments; no source code, training or empirical reproduction."), indent=2))
