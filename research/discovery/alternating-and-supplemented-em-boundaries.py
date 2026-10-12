"""Finite curator examples for alternating and supplemented EM; no fit benchmark."""
from fractions import Fraction as F
import json
import math


def mat(rows):
    return [[F(x) for x in row] for row in rows]


def eye(n):
    return mat([[int(i == j) for j in range(n)] for i in range(n)])


def add(a, b, sign=1):
    return [[x+sign*y for x, y in zip(r, s)] for r, s in zip(a, b)]


def mul(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def inv(a):
    n = len(a)
    v = [r[:] + e for r, e in zip(a, eye(n))]
    for i in range(n):
        j = next(j for j in range(i, n) if v[j][i])
        v[i], v[j] = v[j], v[i]
        pivot = v[i][i]
        v[i] = [x/pivot for x in v[i]]
        for k in range(n):
            if k != i:
                factor = v[k][i]
                v[k] = [x-factor*y for x, y in zip(v[k], v[i])]
    return [r[n:] for r in v]


def transpose(a):
    return list(map(list, zip(*a)))


def symmetric(a):
    return a == transpose(a)


def close(a, b):
    assert math.isclose(a, b, rel_tol=1e-11, abs_tol=1e-11), (a, b)


# A legitimate Gaussian augmentation: observed precision Io; independent latent
# Z|theta ~ N(B theta,I), with B=[[1,1],[0,1]], missing information B'B.
# Work at observed y=0, so the MLE is theta*=0.
Io, Im = mat([[2, 0], [0, 1]]), mat([[1, 1], [1, 2]])
Ic = add(Io, Im)
I = eye(2)
Vcom = inv(Ic)
D_em = mul(Im, Vcom)  # ROW Jacobian: input i, output j.


def ecm(theta, refresh=True):
    a, b = theta
    v = [a+b, a+2*b] if refresh else [F(0), F(0)]
    anew = (v[0]-b)/3
    bnew = (v[1]-anew)/3
    return [anew, bnew]


# Coordinate-perturbation map derivatives, exactly finite for these linear maps.
D_ecm = [ecm(e) for e in I]
D_cm = [ecm(e, False) for e in I]
for i in range(2):
    h = F(1, 10000)
    perturb = [h*x for x in I[i]]
    assert [x/h for x in ecm(perturb)] == D_ecm[i]
    assert [x/h for x in ecm(perturb, False)] == D_cm[i]
assert add(I, D_ecm, -1) == mul(add(I, D_em, -1), add(I, D_cm, -1))
V_sem = mul(Vcom, inv(add(I, D_em, -1)))
V_secm = mul(mul(Vcom, add(I, D_cm, -1)), inv(add(I, D_ecm, -1)))
increment = mul(mul(Vcom, add(D_ecm, D_cm, -1)), inv(add(I, D_ecm, -1)))
assert V_sem == V_secm == inv(Io) == add(Vcom, increment)
assert symmetric(increment)
wrong_sem_on_ecm = mul(Vcom, inv(add(I, D_ecm, -1)))
wrong_order = mul(mul(Vcom, inv(add(I, D_ecm, -1))), add(I, D_cm, -1))
assert wrong_sem_on_ecm != V_secm and wrong_order != V_secm
# Symmetry is necessary but not sufficient: wrong curvature scaling stays symmetric.
scaled_wrong = [[x/2 for x in r] for r in V_secm]
assert symmetric(scaled_wrong) and scaled_wrong != V_secm

# AECM cycles can change augmentation. Same observed y=(0,0), unit precision;
# cycle1 latent mean a+10b; cycle2 latent mean 10a+b. Both integrate to 1.
ll = lambda a, b: -(a*a+b*b)/2
old, first = (1., 1.), (.5, 1.)
fresh_second = (.5, .5)
fixed_q_second = (.5, 105/101)
assert ll(*old) < ll(*first) < ll(*fresh_second)
assert ll(*old) < ll(*fixed_q_second) < ll(*first)
# Q1 stays fixed within its CM sweep; intermediate LL can fall.
q1 = lambda a, b: ll(a, b)-(a+10*b-11)**2/2
assert q1(*old) < q1(*first) < q1(*fixed_q_second)

# Correct the Gaussian residual update sign in SAGE1994 author PDF p.8.
y, theta, residual = 2., 0., 2.
theta_new = theta+residual
correct_residual = residual-(theta_new-theta)
printed_residual = residual+(theta_new-theta)
assert correct_residual == y-theta_new == 0
wrong_next = theta_new+printed_residual
assert -(y-wrong_next)**2/2 < -(y-theta_new)**2/2

# Positive definite H can yield non-real Gauss-Seidel eigenvalues. The two
# nonzero roots have trace5/8, determinant1/8 and discriminant -7/64.
H = mat([[1, F(1, 2), F(1, 2)], [F(1, 2), 1, F(1, 2)], [F(1, 2), F(1, 2), 1]])
L = [[H[i][j] if j <= i else F(0) for j in range(3)] for i in range(3)]
U = [[-H[i][j] if j > i else F(0) for j in range(3)] for i in range(3)]
T = mul(inv(L), U)
trace = T[1][1]+T[2][2]
determinant = T[1][1]*T[2][2]-T[1][2]*T[2][1]
assert trace == F(5, 8) and determinant == F(1, 8)
assert trace*trace-4*determinant == -F(7, 64)
# H has eigenvalues1/2,1/2,2. This exhibits a proof gap, not a counterexample
# to the published speed comparison itself.

# Small Poisson SAGE2/SAGE3 examples; update projections at every coordinate.
A, counts = [[1., 2.], [2., 1.]], [8., 5.]


def poisson_ll(lam, background):
    means = [sum(a*x for a, x in zip(row, lam))+r for row, r in zip(A, background)]
    return sum(y*math.log(m)-m for y, m in zip(counts, means))


def sage_sweep(initial, background, pseudobackground):
    lam = initial[:]
    means = [sum(a*x for a, x in zip(row, lam))+r for row, r in zip(A, background)]
    values = [poisson_ll(lam, background)]
    zs = []
    for k in range(2):
        z = min((m/row[k]-lam[k] if pseudobackground else r/row[k])
                for row, r, m in zip(A, background, means) if row[k] > 0)
        e = sum(row[k]*y/m for row, y, m in zip(A, counts, means))
        adot = sum(row[k] for row in A)
        old_k = lam[k]
        lam[k] = max((old_k+z)*e/adot-z, 0.)
        means = [m+row[k]*(lam[k]-old_k) for row, m in zip(A, means)]
        for row, r, m in zip(A, background, means):
            close(m, sum(a*x for a, x in zip(row, lam))+r)
        values.append(poisson_ll(lam, background))
        assert values[-1] >= values[-2]-1e-12
        zs.append(z)
    assert lam[0] > 0  # Starts at zero, revived by positive background shift.
    return dict(final=lam, likelihoods=values, shifts=zs)


p2 = sage_sweep([0., 1.], [1., 1.], False)
p3 = sage_sweep([0., 1.], [0., 0.], True)
# Penalized one-coordinate surrogate root, beta*w>0; derivative and curvature.
adot, e, oldk, z, beta, w, neighbor = 3., 4., .5, .25, 2., 1., 1.
B = (adot-beta*w*(neighbor+z))/(2*beta*w)
root = max(-B+math.sqrt(B*B+e*(oldk+z)/(beta*w))-z, 0.)
derivative = -adot+e*(oldk+z)/(root+z)-beta*w*(root-neighbor)
assert root > 0
close(derivative, 0)
assert -e*(oldk+z)/(root+z)**2-beta*w < 0

print(json.dumps(dict(
    supplemented=dict(complete_information=Ic, observed_information=Io,
        row_jacobian_em=D_em, row_jacobian_ecm=D_ecm, row_jacobian_frozen_cm=D_cm,
        covariance=V_secm, missing_increment=increment,
        wrong_sem_on_ecm=wrong_sem_on_ecm, wrong_factor_order=wrong_order,
        symmetric_but_wrong=scaled_wrong),
    aecm=dict(old_ll=ll(*old), first_cycle_ll=ll(*first),
        fresh_augmentation_cycle_ll=ll(*fresh_second), frozen_q_second_cm_ll=ll(*fixed_q_second)),
    sage=dict(correct_residual=correct_residual, printed_residual=printed_residual,
        gauss_seidel=T, nonzero_eigenvalue_discriminant=trace*trace-4*determinant,
        poisson_sage2=p2, poisson_sage3=p3, penalized_coordinate_root=root),
    scope='Finite mathematical curator checks; not an original-software run, '
          'empirical replication, general convergence proof or uncertainty calibration.'),
    default=str, indent=2))
