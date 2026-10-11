#!/usr/bin/env python3
"""Curator counterexample to the bound after Theorem 2 in Zhao/Tang (NIPS 2008).

Evaluate their Equations (3)--(4) and diagonal-resolvent formula on a two-vertex
mutual-edge graph. This is original finite arithmetic, not an implementation
or benchmark of Zell, and not an author-issued erratum.
"""
from fractions import Fraction
import json
import math


def calculate():
    # P = [[0, 1], [1, 0]]; its induced matrix 1-norm and spectral radius are 1.
    z = Fraction(1, 4)
    norm_one = Fraction(1)
    assert 0 < z < 1 / (2 * norm_one)
    determinant = 1 - z * z
    diagonal_inverse = 1 / determinant
    epsilon = -math.log(float(determinant))
    # Deleting either vertex leaves a zero one-by-one adjacency: epsilon = 0.
    epsilon_deleted = -math.log(1.0)
    chi_leave_one_out = sum(epsilon - epsilon_deleted for _ in range(2)) / 2
    chi_resolvent = sum(math.log(float(diagonal_inverse)) for _ in range(2)) / 2
    assert math.isclose(chi_leave_one_out, chi_resolvent, rel_tol=1e-14)
    assert chi_resolvent > epsilon / 2 > 0
    return {
        "P": [[0, 1], [1, 0]],
        "z": str(z),
        "det_I_minus_zP": str(determinant),
        "inverse_diagonal": [str(diagonal_inverse)] * 2,
        "epsilon": epsilon,
        "chi_leave_one_out": chi_leave_one_out,
        "chi_resolvent": chi_resolvent,
        "printed_upper_bound_epsilon_over_n": epsilon / 2,
        "printed_upper_bound_satisfied": chi_resolvent <= epsilon / 2,
        "algorithm_1_sufficient_z_bound_satisfied": True,
        "scope": "One counterexample to the printed inequality; no general replacement bound asserted.",
    }


if __name__ == "__main__":
    print(json.dumps(calculate(), indent=2))
