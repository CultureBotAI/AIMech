#!/usr/bin/env python3
"""Check the self-neighbor convention against ROCK (ICDE 1999), Figure 1/§3.2.

Original finite set arithmetic only: the two reported counts are reproduced
when a point is excluded from its own neighborhood. This does not execute the
ROCK clustering algorithm or validate its accuracy.
"""
from fractions import Fraction
from itertools import combinations
import json


def calculate():
    points = [frozenset(p) for p in combinations([1, 2, 3, 4, 5], 3)]
    points += [frozenset(p) for p in combinations([1, 2, 6, 7], 3)]
    a, b, c = (frozenset(p) for p in ([1, 2, 6], [1, 2, 7], [1, 2, 3]))

    def neighbors(point, include_self):
        return {
            other for other in points
            if (include_self or other != point)
            and Fraction(len(point & other), len(point | other)) >= Fraction(1, 2)
        }

    results = {}
    for include in (False, True):
        shared = neighbors(a, include) & neighbors(b, include)
        results[str(include)] = {
            "first_pair_count": len(shared),
            "first_pair_common_neighbors": sorted(sorted(p) for p in shared),
            "second_pair_count": len(neighbors(a, include) & neighbors(c, include)),
        }
    assert (results["False"]["first_pair_count"], results["False"]["second_pair_count"]) == (5, 3)
    assert (results["True"]["first_pair_count"], results["True"]["second_pair_count"]) == (7, 5)
    return {
        "sample_size": len(points),
        "jaccard_threshold": "1/2",
        "include_self_results": results,
        "interpretation": "The published counts 5 and 3 match self-excluding neighborhoods.",
    }


if __name__ == "__main__":
    print(json.dumps(calculate(), indent=2))
