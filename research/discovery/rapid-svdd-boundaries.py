"""Exact curator illustrations for RAPID (Englhardt et al., 2022).

These calculations test mathematical and pseudocode interpretations, not the
historical Julia implementation. The kernel chosen here is 2**(-(x-y)**2).
The paper's displayed kernel and implementation conventions are distinguished
in the associated record; no SVDD optimizer or benchmark is executed.
"""
from fractions import Fraction as F
import json


def gram(points):
    return [[F(2) ** (-(x-y)**2) for y in points] for x in points]


def solve(matrix, vector):
    rows = [list(row) + [v] for row, v in zip(matrix, vector)]
    n = len(rows)
    for col in range(n):
        pivot = next(i for i in range(col, n) if rows[i][col])
        rows[col], rows[pivot] = rows[pivot], rows[col]
        divisor = rows[col][col]
        rows[col] = [v / divisor for v in rows[col]]
        for i in range(n):
            if i != col:
                factor = rows[i][col]
                rows[i] = [a-factor*b for a, b in zip(rows[i], rows[col])]
    return [row[-1] for row in rows]


def main():
    points = [0, 1, 2]
    kernel = gram(points)
    density = list(map(sum, kernel))
    assert density == [F(25, 16), F(2), F(25, 16)]
    after = [d-row[1] for d, row in zip(density, kernel)]
    old_threshold = min(after)
    candidate_threshold = min(after[0], after[2])
    assert after == [F(17, 16), F(1), F(17, 16)]
    assert all(d >= old_threshold for d in after)
    assert not all(d >= candidate_threshold for d in after)
    # Old-S minimum can permit a second removal down to one point.
    final_density = [d-row[0] for d, row in zip(after, kernel)]
    second_old_threshold = min(final_density[0], final_density[2])
    assert all(d >= second_old_threshold for d in final_density)
    assert final_density == [F(1, 16), F(1, 2), F(1)]

    # Hard-SVDD: the positive solution K alpha=q*1, sum(alpha)=1
    # is the unique minimizer of alpha^T K alpha on the simplex.
    asymmetric = [0, 1, 4]
    kernel2 = gram(asymmetric)
    z = solve(kernel2, [F(1)] * 3)
    alpha = [v / sum(z) for v in z]
    q = 1 / sum(z)
    assert sum(alpha) == 1 and all(0 < a < 1 for a in alpha)
    assert all(sum(k*a for k, a in zip(row, alpha)) == q for row in kernel2)
    # Gaussian Gram matrices on distinct points are positive definite.
    # Check leading principal minors explicitly for this instance too.
    determinant = (
        kernel2[0][0]*(kernel2[1][1]*kernel2[2][2]-kernel2[1][2]*kernel2[2][1])
        - kernel2[0][1]*(kernel2[1][0]*kernel2[2][2]-kernel2[1][2]*kernel2[2][0])
        + kernel2[0][2]*(kernel2[1][0]*kernel2[2][1]-kernel2[1][1]*kernel2[2][0])
    )
    assert kernel2[0][0] > 0 and 1-kernel2[0][1]**2 > 0 and determinant > 0
    row_density = list(map(sum, kernel2))
    derivative_factors = [
        -sum(a*(x-y)*k for a, y, k in zip(alpha, asymmetric, row))
        for x, row in zip(asymmetric, kernel2)
    ]
    assert all(v != 0 for v in derivative_factors)
    assert len(set(row_density)) == 3
    # Each training point is a crossing of weighted score=q. A single
    # unweighted KDE threshold cannot have all three distinct densities
    # as its level, so the whole continuous decision regions cannot coincide.

    # Current author code's percentage threshold clamps the zero index to 1.
    ordered = sorted(row_density)
    zero_threshold = (ordered[0]+ordered[1])/2
    zero_retained = sum(d >= zero_threshold for d in row_density)
    assert zero_retained == 2
    print(json.dumps({
        'scope': 'Exact formula and pseudocode illustrations; no historical Julia execution or benchmark.',
        'kernel': 'k(x,y)=2^(-(x-y)^2), a specified standard Gaussian example.',
        'printed_old_set_threshold': dict(points=points, initial=list(map(str, density)), after_removing_middle=list(map(str, after)), old_threshold=str(old_threshold), candidate_threshold=str(candidate_threshold), final=list(map(str, final_density)), interpretation='Printed Algorithm 2 accepts the middle removal; the candidate-set minimum would reject it. This is not the inspected public Julia code.'),
        'finite_global_boundary_nonidentity': dict(points=asymmetric, alpha=list(map(str, alpha)), weighted_boundary_score=str(q), unweighted_densities=list(map(str, row_density)), derivative_factors=list(map(str, derivative_factors)), determinant=str(determinant), interpretation='Distinct unweighted densities at three nonstationary hard-SVDD boundary crossings preclude a single common KDE level. This does not contradict an asymptotic consistency theorem or finite-set accept-all equivalence.'),
        'zero_percentage_code_convention': dict(threshold=str(zero_threshold), retained=zero_retained, total=3, interpretation='The inspected midpoint/clamped-index formula excludes one uniquely least-dense point at percentage zero. No Julia code was run.'),
        'tie_convention': 'Equal densities all pass the >= split, regardless of percentage; exact requested removal fractions are not assured.',
        'current_loop_convention': 'With m initial inliers, i=1 and while i<m-2 permit at most m-3 accepted removals for m>=3; smaller sets are unchanged.'
    }, indent=2))


if __name__ == '__main__':
    main()
