"""Original finite probability checks; no source implementation or benchmark."""
from itertools import product
from math import exp, sqrt, pi, isclose
import json

bits = list(product(range(2), repeat=4))
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]


def normalize(d):
    z = sum(d.values())
    assert z > 0
    return {k: v / z for k, v in d.items()}


def prob(d, event, given=lambda _: True):
    den = sum(w for k, w in d.items() if given(k))
    assert den > 0
    return sum(w for k, w in d.items() if given(k) and event(k)) / den


def close(a, b):
    assert isclose(a, b, rel_tol=1e-10, abs_tol=1e-12), (a, b)


# A positive Gibbs distribution on a four-cycle of paired variables.
pair = normalize({(x, y): exp(sum(.3 * (x[i] == x[j]) + .7 * (y[i] == y[j])
                                 for i, j in edges)
                             + .9 * sum(x[i] == y[i] for i in range(4)))
                  for x in bits for y in bits})
close(sum(pair.values()), 1)
hidden_cond = [prob(pair, lambda z: z[0][0] == 1,
                   lambda z: z[0][1] == z[0][3] == 1 and z[0][2] == c)
               for c in (0, 1)]
assert abs(hidden_cond[0] - hidden_cond[1]) > 1e-4
observed = (0, 1, 1, 0)
post_cond = [prob(pair, lambda z: z[0][0] == 1,
                 lambda z: z[1] == observed and z[0][1] == z[0][3] == 1 and z[0][2] == c)
             for c in (0, 1)]
close(*post_cond)
# Check local paired conditional: changing the opposite site cannot affect it.
joint_cond = [prob(pair, lambda z: z[0][0] == z[1][0] == 1,
                  lambda z: all(z[k][i] == 1 for k in (0, 1) for i in (1, 3))
                  and z[0][2] == z[1][2] == c) for c in (0, 1)]
close(*joint_cond)

# A triplet field: auxiliary spatial interactions and local X-U / Y-U coupling.
triplet = normalize({(x, u, y): exp(.9 * sum(u[i] == u[j] for i, j in edges)
                                    + 1.1 * sum(x[i] == u[i] for i in range(4))
                                    + .7 * sum(y[i] == u[i] for i in range(4)))
                     for x in bits for u in bits for y in bits})
close(sum(triplet.values()), 1)
projected_cond = [prob(triplet, lambda z: z[0][0] == z[2][0] == 1,
                      lambda z: all(z[k][i] == 1 for k in (0, 2) for i in (1, 3))
                      and z[0][2] == z[2][2] == c) for c in (0, 1)]
assert abs(projected_cond[0] - projected_cond[1]) > 1e-4
hidden_post_cond = [prob(triplet, lambda z: z[0][0] == 1,
                        lambda z: z[2] == observed and z[0][1] == z[0][3] == 1
                        and z[0][2] == c) for c in (0, 1)]
assert abs(hidden_post_cond[0] - hidden_post_cond[1]) > 1e-4
augmented_post_cond = [prob(triplet, lambda z: z[0][0] == z[1][0] == 1,
                           lambda z: z[2] == observed
                           and all(z[k][i] == 1 for k in (0, 1) for i in (1, 3))
                           and z[0][2] == z[1][2] == c) for c in (0, 1)]
close(*augmented_post_cond)

# A rooted branching tree of pairs, with one grandchild.
parent = {1: 0, 2: 0, 3: 1}
children = {i: [j for j, p in parent.items() if p == i] for i in range(4)}
states = list(product(range(2), repeat=2))


def initial(z):
    return .5 * (.8 if z[0] == z[1] else .2)


def kernel(child, par):
    py = .85 if child[1] == par[1] else .15
    px1 = .1 + .55 * child[1] + .2 * par[0]
    return py * (px1 if child[0] else 1 - px1)


for p in states:
    close(sum(kernel(c, p) for c in states), 1)
tree = {}
for z in product(states, repeat=4):
    w = initial(z[0])
    for i, p in parent.items():
        w *= kernel(z[i], z[p])
    tree[z] = w
close(sum(tree.values()), 1)
# Hidden siblings are dependent given only their hidden parent.
siblings = [prob(tree, lambda z: z[2][0] == 1,
                 lambda z: z[0][0] == 1 and z[1][0] == c) for c in (0, 1)]
assert abs(siblings[0] - siblings[1]) > 1e-4
y = (0, 1, 0, 1)
beta = {}
for i in (3, 2, 1, 0):
    for x in (0, 1):
        b = 1.
        for j in children[i]:
            b *= sum(kernel((v, y[j]), (x, y[i])) * beta[j, v] for v in (0, 1))
        beta[i, x] = b
root_weights = [initial((x, y[0])) * beta[0, x] for x in (0, 1)]
evidence = sum(root_weights)
marg = {0: [v / evidence for v in root_weights]}
for i in (1, 2, 3):
    p = parent[i]
    marg[i] = [0., 0.]
    for xp in (0, 1):
        row = [kernel((x, y[i]), (xp, y[p])) * beta[i, x] for x in (0, 1)]
        den = sum(row)
        for x in (0, 1):
            marg[i][x] += marg[p][xp] * row[x] / den
close(evidence, sum(w for z, w in tree.items() if tuple(v[1] for v in z) == y))
for i in range(4):
    for x in (0, 1):
        close(marg[i][x], prob(tree, lambda z: z[i][0] == x,
                              lambda z: tuple(v[1] for v in z) == y))

# The one-dimensional completed square checks sign, factor and normalizer.
alpha, beta_g, delta = .4, 1.2, .8
analytic = sqrt(pi / delta) * exp(-alpha + beta_g ** 2 / (4 * delta))
n, left, right = 4000, -12., 12.
h = (right - left) / n
values = [exp(-alpha - beta_g * (left + i * h) - delta * (left + i * h) ** 2)
          for i in range(n + 1)]
quadrature = h / 3 * (values[0] + values[-1]
                       + 4 * sum(values[1:-1:2]) + 2 * sum(values[2:-1:2]))
close(analytic, quadrature)
# Unit diagonal and -0.2 precision on each unordered eight-neighbor edge.
grid = list(product(range(4), repeat=2))
grid_edges = [(a, b) for i, a in enumerate(grid) for b in grid[i + 1:]
              if max(abs(a[0] - b[0]), abs(a[1] - b[1])) == 1]
quadratic_ones = len(grid) - .4 * len(grid_edges)
assert len(grid_edges) == 42 and quadratic_ones < 0
# With off-diagonal precision, inverse diagonal is not marginal variance.
det = 1 * 2 - .4 ** 2
conditional_variances, marginal_variances = [1., .5], [2 / det, 1 / det]
assert all(abs(a - b) > .01 for a, b in zip(conditional_variances, marginal_variances))

print(json.dumps(dict(
    pair_field=dict(hidden_nonlocal=hidden_cond, posterior_local=post_cond, joint_local=joint_cond),
    triplet_field=dict(pair_projection_nonlocal=projected_cond,
                       target_posterior_nonlocal=hidden_post_cond,
                       augmented_posterior_local=augmented_post_cond),
    pair_tree=dict(hidden_sibling_dependence=siblings, evidence=evidence, posterior=marg),
    gaussian=dict(integral_analytic=analytic, integral_quadrature=quadrature,
                  conditional_variances=conditional_variances, marginal_variances=marginal_variances,
                  grid_edges=len(grid_edges), constant_vector_quadratic_form=quadratic_ones),
    scope='Original finite witnesses and one-dimensional quadrature; not author-code reproduction, inference convergence, fitting or empirical evaluation.'
), indent=2))
