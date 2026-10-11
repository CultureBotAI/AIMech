#!/usr/bin/env python3
"""Original finite checks of three source conventions, not model benchmarks.

CLARANS: Ng and Han, VLDB 1994, pp. 146-148, Eq. (5) and graph cost.
RCA: Bar-Hillel et al., JMLR 2005, pp. 940 and 948, Algorithms 1-2.
LMNN: Weinberger and Saul, JMLR 2009, pp. 209-210, Eqs. (1)-(3).
"""
from fractions import Fraction
import json


def calculate():
    points = (0, 6, 10, 11)
    old, new = (0, 10), (6, 10)

    def cost(point, medoids):
        return min(abs(point - medoid) for medoid in medoids)

    changes = {p: cost(p, new) - cost(p, old) for p in points}
    complete = sum(changes.values())
    nonmedoids_only = sum(v for p, v in changes.items() if p not in old)
    assert complete == 2 and nonmedoids_only == -4

    chunklets = [((0, 0), (1, 0), (2, 0)), ((10, 0), (11, 0), (12, 0))]
    count = sum(len(c) for c in chunklets)
    scatter = [[Fraction(0) for _ in range(2)] for _ in range(2)]
    for chunklet in chunklets:
        mean = [sum(Fraction(p[d]) for p in chunklet) / len(chunklet) for d in range(2)]
        for point in chunklet:
            centered = [Fraction(point[d]) - mean[d] for d in range(2)]
            for row in range(2):
                for col in range(2):
                    scatter[row][col] += centered[row] * centered[col] / count
    assert scatter == [[Fraction(2, 3), 0], [0, 0]]
    size_count = sum(len(c) - 1 for c in chunklets)
    determinant = scatter[0][0] * scatter[1][1] - scatter[0][1] * scatter[1][0]
    assert size_count == 4 and determinant == 0 and scatter[0][0] > 0

    squared_direct = (2 - 0) ** 2
    squared_via_one = (1 - 0) ** 2 + (2 - 1) ** 2
    assert squared_direct == 4 and squared_via_one == 2
    return {
        "clarans": {
            "observations": points, "old_medoids": old, "new_medoids": new,
            "old_cost": sum(cost(p, old) for p in points),
            "new_cost": sum(cost(p, new) for p in points),
            "per_point_changes": changes,
            "complete_change": complete,
            "change_over_only_old_nonmedoids": nonmedoids_only,
            "interpretation": "Omitting the removed medoid reverses the sign of this swap's cost change.",
        },
        "rca": {
            "chunklets": chunklets, "dimension": 2,
            "within_chunklet_covariance": [[str(v) for v in row] for row in scatter],
            "sum_chunklet_size_minus_one": size_count,
            "actual_rank": 1, "determinant": str(determinant),
            "interpretation": "The sample-size count can exceed dimension while the covariance is singular.",
        },
        "squared_distance": {
            "points": [0, 1, 2], "squared_direct": squared_direct,
            "sum_squared_segments": squared_via_one,
            "interpretation": "Squared Euclidean distance need not satisfy the metric triangle inequality.",
        },
    }


if __name__ == "__main__":
    print(json.dumps(calculate(), indent=2))
