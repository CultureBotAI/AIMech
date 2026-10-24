"""Finite arithmetic checks of SCC source boundaries, not author-code execution."""
from fractions import Fraction as F
import json

# Definition 3 permits a nearest-neighbor edge in either direction. A weak
# component need not be a clique or consist solely of reciprocal pairs.
points = [F(0), F(1), F(3)]
nearest = {i: min((j for j in range(3) if j != i),
                  key=lambda j: (abs(points[i] - points[j]), j)) for i in range(3)}
eligible = [(i, j) for i, j in nearest.items() if abs(points[i] - points[j]) <= 2]
assert nearest == {0: 1, 1: 0, 2: 1}
assert eligible == [(0, 1), (1, 0), (2, 1)]
assert abs(points[0] - points[2]) > 2

# Two well-separated target groups, each containing two tight distinct clouds.
# R is exactly 1 under both the Euclidean and squared-Euclidean readings.
# delta=30 is satisfied in both, with centers 0 and 40. Appendix A.3's
# lambda=(delta-2)*R is 28. All 404 observations are distinct.
clouds = [[F(center) + sign * (F(99, 100) + F(i, 10000))
           for i in range(101)] for center in [0, 40] for sign in [-1, 1]]
groups = [clouds[0] + clouds[1], clouds[2] + clouds[3]]
all_points = sum(clouds, [])
assert len(set(all_points)) == len(all_points) == 404
assert [sum(g) / len(g) for g in groups] == [0, 40]
radius = max(abs(x - c) for g, c in zip(groups, [0, 40]) for x in g)
assert radius == 1 and F(40) >= 30 * radius and F(40)**2 >= 30 * radius**2
penalty = F(28)

def sse(group, center):
    return sum((x - center)**2 for x in group)

target_dp = sum(sse(g, sum(g) / len(g)) for g in groups) + 2 * penalty
target_facility = sum(min(sse(g, c) for c in all_points) for g in groups) + 2 * penalty
four_centers = [sorted(g)[len(g) // 2] for g in clouds]
assert all(c in all_points for c in four_centers)
four_facility = sum(sse(g, c) for g, c in zip(clouds, four_centers)) + 4 * penalty
assert four_facility < target_facility
assert target_dp > 2 * four_facility
# This disproves optimality of this target partition in Proposition 3 as
# printed. It does not rule out a better partition elsewhere in an SCC tree,
# and does not constitute a counterexample to Theorem 2's existential claim.

# Empty thresholds incur work even without a new partition. Ten doubling
# thresholds below distance 1 precede a merge of two singleton points.
threshold = F(1, 1000)
empty_rounds = 0
while threshold < 1:
    empty_rounds += 1
    threshold *= 2
assert empty_rounds == 10

print(json.dumps(dict(
    nearest_neighbor_edges=eligible,
    component=[0, 1, 2], component_is_threshold_clique=False,
    separated_points=len(all_points), radius=str(radius), delta=30,
    penalty=str(penalty), target_dp_cost=str(target_dp),
    target_facility_cost=str(target_facility), four_facility_cost=str(four_facility),
    target_dp_exceeds_twice_feasible_cost=True, empty_threshold_rounds=empty_rounds,
    limits='Exact finite arithmetic and a source-predicate check only. No author program, benchmark, or counterexample to the existential SCC-tree approximation claim.'
), indent=2))
