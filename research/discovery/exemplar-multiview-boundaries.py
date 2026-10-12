"""Finite curator checks for exemplar and multiview CMM boundaries.

These are formula checks, not author software or benchmark reproduction.
Natural logarithms are used; all matrices below are stated explicitly.
"""
import json
from math import exp, log, pi, sqrt

def fit_step(S, q):
    z = [sum(s * w for s, w in zip(row, q)) for row in S]
    r = [[s * w / a for s, w in zip(row, q)] for row, a in zip(S, z)]
    eta = [sum(row[j] / a for row, a in zip(S, z)) / len(S) for j in range(len(q))]
    return [w * e for w, e in zip(q, eta)], r, eta

def objective(S, q):
    return -sum(log(sum(s * w for s, w in zip(row, q))) for row in S) / len(S)

def near(a, b, tol=1e-10):
    assert abs(a - b) < tol, (a, b)

S = [[1.0, .25], [.25, 1.0]]
qn, r, eta = fit_step(S, [.6, .4])
for row in r:
    near(sum(row), 1)
    near(sum(v / 2 for v in row), .5)
near(sum(qn), 1)
assert objective(S, qn) < objective(S, [.6, .4])
locked, _, _ = fit_step(S, [1., 0.])
assert locked == [1., 0.]
assert objective(S, locked) > objective(S, [.5, .5])
zero_beta, _, inactive = fit_step([[1., 1.], [1., 1.]], [1., 0.])
assert zero_beta == [1., 0.] and inactive == [1., 1.]
qsmall, _, _ = fit_step([[1., .1], [.1, 1.]], [1 - 1e-10, 1e-10])
assert 0 < qsmall[1] < 1e-3 / 2
pruned = [1., 0.]
assert objective([[1., .1], [.1, 1.]], pruned) > objective([[1., .1], [.1, 1.]], [.5, .5])
q = [.9, .1]
for _ in range(5):
    q, _, _ = fit_step(S, q)
    assert q[0] > q[1]
ranking_gap = objective(S, q) - objective(S, [.5, .5])
assert ranking_gap > 1e-4

# Converged soft channel whose MAP-exemplar postprocessing picks just one point.
x = [0., 1., 3.]
beta = .25
S3 = [[exp(-beta * (a - b) ** 2) for b in x] for a in x]
q = [1 / 3] * 3
for iterations in range(5000):
    qn, _, _ = fit_step(S3, q)
    change = max(abs(a - b) for a, b in zip(q, qn))
    q = qn
    if change < 1e-14:
        break
_, r3, eta3 = fit_step(S3, q)
certificate = max(log(e) for e in eta3)
assert certificate < 1e-10
I = sum(v * log(v / qj) for row in r3 for v, qj in zip(row, q) if v > 0) / 3
hard_exemplars = sorted({max(range(3), key=lambda j: row[j]) for row in r3})
assert hard_exemplars == [1] and I > .03
assert I > log(len(hard_exemplars))

# Two Gaussian-shaped proximity views on points 0 and 1.
Sv = [[[1., .1], [.1, 1.]], [[1., .8], [.8, 1.]]]
q0 = [.7, .3]
pi0 = [.5, .5]
Q = [[sum(s * w for s, w in zip(row, q0)) for row in v] for v in Sv]
U = -sum(log(a) for v in Q for a in v) / 4
W = -sum(log(sum(pi0[v] * Q[v][i] for v in range(2))) for i in range(2)) / 2
assert abs(U - W) > .01
unweighted = [sum(fit_step(v, q0)[0][j] for v in Sv) / 2 for j in range(2)]
gamma = [[pi0[v] * Q[v][i] / sum(pi0[w] * Q[w][i] for w in range(2)) for v in range(2)] for i in range(2)]
pinew = [sum(row[v] for row in gamma) / 2 for v in range(2)]
qinner = q0[:]
for inner_iterations in range(10000):
    Qinner = [[sum(s * w for s, w in zip(row, qinner)) for row in v] for v in Sv]
    qnext = [qinner[j] * sum(gamma[i][v] * Sv[v][i][j] / Qinner[v][i] for i in range(2) for v in range(2)) / 2 for j in range(2)]
    change = max(abs(a - b) for a, b in zip(qinner, qnext))
    qinner = qnext
    if change < 1e-14:
        break
near(sum(qinner), 1)
near(sum(pinew), 1)
assert abs(qinner[0] - unweighted[0]) > 1e-4
Wnext = -sum(log(sum(pinew[v] * sum(Sv[v][i][j] * qinner[j] for j in range(2)) for v in range(2))) for i in range(2)) / 2
assert Wnext < W

# Density-scale dependence of the outer weights, unlike the unweighted q fit.
C = [sqrt(log(10) / pi), sqrt(log(1.25) / pi)]
a = [C[v] * sum(Sv[v][0]) / 2 for v in range(2)]
density_weight = a[0] / sum(a)
rescaled_weight = (a[0] / 10) / (a[0] / 10 + a[1])
raw_weight = .55 / (.55 + .9)
assert density_weight > .6 and rescaled_weight < .2 and raw_weight < .4
near(sqrt(1 / (2 * pi)) * sqrt(pi), 1 / sqrt(2))

# Unaugmented marginal mixture on a 2-by-3 observation product space.
P1, P2 = [.7, .3], [.2, .3, .5]
piv = .4
mass = sum(piv * a + (1 - piv) * b for a in P1 for b in P2)
near(mass, 3 * piv + 2 * (1 - piv))
assert mass != 1

print(json.dumps(dict(status='passed',conditional_row_sums=[sum(row) for row in r],printed_assignment_row_sums=[sum(v / 2 for v in row) for row in r],pruned_small_weight=qsmall[1],stable_ranking_objective_gap=ranking_gap,soft_vs_hard=dict(points=x,beta=beta,weights=q,iterations=iterations+1,mutual_information_nats=I,hard_exemplar_indices=hard_exemplars,soft_gap_certificate=certificate),multiview=dict(unweighted_objective=U,weighted_uniform_objective=W,unweighted_one_step=unweighted,weighted_outer_view_update=pinew,weighted_inner_solution=qinner,weighted_next_objective=Wnext),view_scale=dict(raw_affinity_outer_weight=raw_weight,normalized_density_outer_weight=density_weight,coordinate_rescaled_density_outer_weight=rescaled_weight),unnormalized_product_mass=mass,printed_gaussian_integral=1/sqrt(2)),indent=2))
