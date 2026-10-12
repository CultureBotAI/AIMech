"""Exact elementary OCSVM boundary examples; no fitted model or solver execution."""
from fractions import Fraction as F
import json

# Two positive real observations with a linear kernel and C=1/(nu*n)=2.
# Writing alpha=(1-t,t), the OCSVM dual is (1+t)^2/2 and is minimized at t=0.
# The sphere dual is (1+t)^2-(1+3*t)=t^2-t, minimized at t=1/2.
x = [F(1), F(2)]
nu = F(1, 4)
C = 1 / (nu * len(x))
oc_alpha = [F(1), F(0)]
svdd_alpha = [F(1, 2), F(1, 2)]
assert C == 2 and sum(oc_alpha) == sum(svdd_alpha) == 1
assert all(0 <= a <= C for a in oc_alpha + svdd_alpha)
w = sum(a * z for a, z in zip(oc_alpha, x))
rho = w * x[0]  # alpha[0] is strictly inside its box, fixing rho.
center = sum(a * z for a, z in zip(svdd_alpha, x))
radius_sq = (x[0] - center) ** 2
assert w == rho == 1 and center == F(3, 2) and radius_sq == F(1, 4)
assert w * 3 >= rho and (3 - center) ** 2 > radius_sq

# nu=1 fixes all alpha=1/n but can leave an unbounded interval of optimal rho.
alpha = [F(1, 2), F(1, 2)]
w_one = sum(a * z for a, z in zip(alpha, x))
scores = [w_one * z for z in x]
objectives = []
acceptances = []
for threshold in [F(3), F(4)]:
    slacks = [max(F(0), threshold - score) for score in scores]
    objectives.append(w_one ** 2 / 2 + sum(slacks) / 2 - threshold)
    acceptances.append([score >= threshold for score in scores])
assert objectives == [F(-9, 8)] * 2
assert acceptances == [[False, True], [False, False]]

# A finite analytic nonconstant PSD kernel can still have a constant fitted score.
balanced = [F(-3, 4), F(-1, 4), F(1, 4), F(3, 4)]
balanced_alpha = [F(1, 4)] * 4
def kernel(a, b):
    return 1 + a * b
balanced_scores = [sum(a * kernel(z, query) for a, z in zip(balanced_alpha, balanced))
                   for query in balanced]
assert balanced_scores == [F(1)] * 4
assert sum(a * z for a, z in zip(balanced_alpha, balanced)) == 0
# The feature map (1,x) has convex-hull minimum norm 1; these weights achieve it.
# All coefficients are interior to C=1/2, hence rho=1 and every point is accepted.
assert all(0 < a < F(1, 2) for a in balanced_alpha)

print(json.dumps({
    "scope": "Exact rational mathematical examples; no historical solver or benchmark was run.",
    "nonconstant_diagonal": {
        "kernel": "k(x,y)=xy", "points": [1, 2], "nu": str(nu), "C": str(C),
        "ocsvm": {"alpha": list(map(str, oc_alpha)), "w": str(w), "rho": str(rho),
                  "acceptance": "x>=1"},
        "svdd": {"alpha": list(map(str, svdd_alpha)), "center": str(center),
                 "radius_squared": str(radius_sq), "acceptance": "1<=x<=2"},
        "interpretation": "Equal sample and penalty do not make the methods identical for arbitrary kernels."
    },
    "nu_one": {"scores": list(map(str, scores)), "thresholds": [3, 4],
               "objectives": list(map(str, objectives)), "accepted_training_points": acceptances,
               "interpretation": "Uniform expansion weights do not uniquely determine the acceptance threshold."},
    "finite_boundary_mass": {"kernel": "k(x,y)=1+xy, feature map (1,x)",
                             "points": list(map(str, balanced)), "nu": "1/2", "rho": "1",
                             "strict_training_outlier_fraction": "0", "support_vector_fraction": "1",
                             "interpretation": "Finite nu bounds need not be equalities, and analyticity alone does not force a nonconstant fitted score. This finite example is not an iid asymptotic counterexample."}
}, indent=2))
