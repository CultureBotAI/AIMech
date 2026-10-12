"""Exact formula checks for CVM/BVM; no optimizer or benchmark execution."""
from fractions import Fraction as F
import json


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def dist2(x, y):
    return dot([a-b for a, b in zip(x, y)], [a-b for a, b in zip(x, y)])


# L2 binary CVM: two orthogonal unit inputs, opposite labels, C=1.
# K_tilde = y_i*y_j*(K_ij+1) + delta_ij/C, not K + I/C.
x = [(F(1), F(0)), (F(0), F(1))]
y = [1, -1]
K = [[y[i]*y[j]*(dot(x[i], x[j])+1)+(i == j) for j in range(2)] for i in range(2)]
assert K == [[3, -1], [-1, 3]]
alpha = [F(1, 2), F(1, 2)]
q = sum(alpha[i]*K[i][j]*alpha[j] for i in range(2) for j in range(2))
assert q == 1
w = [sum(alpha[i]*y[i]*x[i][j] for i in range(2)) for j in range(2)]
b = sum(alpha[i]*y[i] for i in range(2))
xi = alpha[:]
rho = q
primal = dot(w, w)+b*b-2*rho+sum(v*v for v in xi)
assert primal == -q == -1
assert all(y[i]*(dot(w, x[i])+b) == rho-xi[i] for i in range(2))
radius2 = K[0][0]-q
assert radius2 == 2 and radius2 < K[0][0]
assert [K[i][i]-2*sum(alpha[j]*K[i][j] for j in range(2))+q for i in range(2)] == [2, 2]

# Dropping variable diagonal terms changes MEB optimization.
# Features 0,2 have true MEB center1, radius1; minimizing alpha^T K alpha
# alone selects center0, so constant-diagonal assumption is essential.
true_center = F(1)
assert max((z-true_center)**2 for z in [0, 2]) == 1
assert max(z*z for z in [0, 2]) == 4

# Exact fixed-radius BVM step: r=1 > R_star=4/5.
p = (F(1), F(0))
z = (F(-7, 25), F(24, 25))
assert dot(p, p) == dot(z, z) == 1
assert dist2(p, z) == F(64, 25)
beta = F(5, 8)
c = tuple(zj+beta*(pj-zj) for pj, zj in zip(p, z))
opt = tuple((pj+zj)/2 for pj, zj in zip(p, z))
assert c == (F(13, 25), F(9, 25))
assert opt == (F(9, 25), F(12, 25))
assert dist2(c, p) == F(9, 25) and dist2(c, z) == 1
assert dist2(opt, p) == dist2(opt, z) == F(16, 25)
assert dist2(c, opt) == F(1, 25)
for epsilon in [F(1, 10), F(1, 100), F(1, 1000)]:
    assert dist2(p, z) > (1+epsilon)**2
    assert all(dist2(c, a) <= (1+epsilon)**2 for a in [p, z])

# With-replacement independent draws: farthest 5% versus one rare violator.
hit_top_five_percent = 1-F(19, 20)**59
miss_one_of_thousand = F(999, 1000)**59
assert F(95, 100) < hit_top_five_percent < F(96, 100)
assert F(94, 100) < miss_one_of_thousand < F(95, 100)
print(json.dumps({
    "l2_svm_primal_and_dual": str(primal),
    "transformed_diagonal": 3,
    "optimal_meb_squared_radius": str(radius2),
    "fixed_radius_bvm_center": list(map(str, c)),
    "true_meb_center": list(map(str, opt)),
    "fixed_radius_center_error": "1/5",
    "hit_top_five_percent_59_iid_draws": float(hit_top_five_percent),
    "miss_one_violator_of_1000_59_iid_draws": float(miss_one_of_thousand),
    "scope": "Exact rational illustrations; sampling assumes independent draws with replacement. No CVM/BVM code, optimizer, trained model or benchmark executed."
}, indent=2))
