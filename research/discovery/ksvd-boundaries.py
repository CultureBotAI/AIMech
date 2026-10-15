#!/usr/bin/env python3
"""Exact curator algebra for K-SVD boundaries, not a numerical SVD implementation.

Derived from Aharon, Elad and Bruckstein (2006), Section IV, Eqs. 20–24
and Figure 2. Source PDF SHA256:
4ac09163f067f8a4afbb812598145451f4bc9be6b367052f4fdffb240298c3dd.

All matrices are tiny constructed examples and all arithmetic uses Fraction.
No author code, trained model, empirical data or iterative fitting is executed.
Each general grid matrix has an explicitly supplied exact orthogonal SVD.
The script checks its spectral certificate and candidate rank-one error.
It is deliberately not a general-purpose SVD or sparse-coding solver.
Runtime and script hashes belong in an external execution receipt.
"""
from fractions import Fraction as F
from itertools import product
import json


def matrix(rows):
    return [[F(x) for x in row] for row in rows]


def transpose(a):
    return [list(row) for row in zip(*a)]


def multiply(a, b):
    return [[sum((x*y for x, y in zip(row, col)), F(0))
             for col in zip(*b)] for row in a]


def subtract(a, b):
    return [[x-y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def outer(u, v):
    return [[x*y for y in v] for x in u]


def norm_squared(a):
    return sum((x*x for row in a for x in row), F(0))


def error(e, u, a):
    return norm_squared(subtract(e, outer(u, a)))


def rotation(u):
    c, s = u
    assert c*c+s*s == 1
    return [[c, -s], [s, c]]


def serialize(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {k: serialize(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [serialize(v) for v in value]
    return value


def main():
    units = [tuple(map(F, row)) for row in
             [(1, 0), (0, 1), ('3/5', '4/5'), ('5/13', '12/13'),
              ('-3/5', '4/5')]]
    old_units = units + [(-F(1), F(0)), (F(0), -F(1))]
    old_rows = [list(map(F, row)) for row in
                [(1, 1), (1, -1), (2, 1), (-1, 2), (3, 4)]]
    identity = matrix([[1, 0], [0, 1]])
    count = comparisons = zero_spectrum = repeated_top = 0
    for u, v, s, t in product(units, units, range(4), range(4)):
        if t > s:
            continue
        U, V = rotation(u), rotation(v)
        sigma = matrix([[s, 0], [0, t]])
        e = multiply(multiply(U, sigma), transpose(V))
        assert multiply(transpose(U), U) == identity
        assert multiply(transpose(V), V) == identity
        gram = multiply(e, transpose(e))
        assert multiply(transpose(U), multiply(gram, U)) == matrix([[s*s, 0], [0, t*t]])
        row = [F(s)*x for x in v]
        residual = error(e, u, row)
        assert residual == t*t
        assert norm_squared(e) - residual == s*s
        for old_u, old_row in product(old_units, old_rows):
            assert residual <= error(e, old_u, old_row)
            comparisons += 1
        count += 1
        zero_spectrum += s == 0
        repeated_top += s == t and s > 0
    assert (count, comparisons, zero_spectrum, repeated_top) == (250, 8750, 25, 75)

    # Restricting columns preserves every inactive coefficient at zero.
    # The second sample already uses atom 2, so an unrestricted update would
    # violate its one-atom budget. These are explicit algebraic assignments.
    e = matrix([[3, 100], [0, 0]])
    d = matrix([[0, 1], [1, 0]])
    x = matrix([[1, 0], [0, 1]])
    y = matrix([[3, 101], [0, 0]])
    assert subtract(y, outer([F(1), F(0)], x[1])) == e
    restricted_x = matrix([[3, 0], [0, 1]])
    unrestricted_x = matrix([[3, 100], [0, 1]])
    new_d = matrix([[1, 1], [0, 0]])
    old_loss = norm_squared(subtract(y, multiply(d, x)))
    restricted_loss = norm_squared(subtract(y, multiply(new_d, restricted_x)))
    assert (old_loss, restricted_loss) == (10010, 10000)
    assert sum(a != 0 for a in transpose(restricted_x)[1]) == 1
    assert sum(a != 0 for a in transpose(unrestricted_x)[1]) == 2

    # A repeated top singular value has distinct equally optimal updates.
    alternatives = []
    for u in units:
        fitted = outer(u, u)
        assert error(identity, u, u) == 1
        alternatives.append({'atom': u, 'row': u, 'reconstruction': fitted})
    assert alternatives[0]['reconstruction'] != alternatives[1]['reconstruction']

    # Recompute residuals using the newest coefficients, as Figure 2 specifies.
    y1 = matrix([[3], [5]])
    initial_d = identity
    initial_x = matrix([[3], [1]])
    atom1 = [F(3, 5), F(4, 5)]
    updated_d = transpose([atom1, [F(0), F(1)]])
    sequential_x = matrix([[5], [1]])
    parallel_x = matrix([[5], [5]])
    assert subtract(y1, outer([F(0), F(1)], initial_x[1])) == matrix([[3], [4]])
    assert subtract(y1, outer(atom1, [F(5)])) == matrix([[0], [1]])
    assert subtract(y1, outer([F(1), F(0)], initial_x[0])) == matrix([[0], [5]])
    losses = [norm_squared(subtract(y1, multiply(a, b))) for a, b in
              [(initial_d, initial_x), (updated_d, sequential_x), (updated_d, parallel_x)]]
    assert losses == [16, 0, 16]

    # Arbitrary feasible recoding is not an objective-descent guarantee.
    # Both active sets before the sweep are nonempty. Repeated-singular-value
    # choices below are exact global minimizers of the two restricted blocks.
    y2 = matrix([[1, 0, 1, 0], [0, 1, 0, 1]])
    old_x2 = y2
    bad_x2 = matrix([[1, 1, 0, 0], [0, 0, 1, 1]])
    final_d2 = matrix([[1, 1], [0, 0]])
    # Correctly scatter the first rank-one fit to samples 1–2, the second to 3–4.
    final_x2 = matrix([[1, 0, 0, 0], [0, 0, 1, 0]])
    recoding_losses = [norm_squared(subtract(y2, multiply(a, b))) for a, b in
                       [(identity, old_x2), (identity, bad_x2), (final_d2, final_x2)]]
    assert recoding_losses == [0, 4, 2]
    assert all(sum(z != 0 for z in col) <= 1 for col in transpose(final_x2))

    # With fixed coefficient 1, unconstrained centroids and unit-norm atoms
    # solve different subproblems. No k-means identity is inferred from T0=1.
    ys = matrix([[2], [0]])
    centroid_loss = norm_squared(subtract(ys, matrix([[2], [0]])))
    fixed_one_unit_loss = norm_squared(subtract(ys, matrix([[1], [0]])))
    free_gain_loss = error(ys, [F(1), F(0)], [F(2)])
    assert (centroid_loss, fixed_one_unit_loss, free_gain_loss) == (0, 1, 0)

    # The corrected support range is over N samples, as in Figure 2.
    row = [F(0), F(0), F(1)]
    correct_support = [i+1 for i, a in enumerate(row) if a]
    printed_K_support = [i+1 for i, a in enumerate(row[:2]) if a]
    assert correct_support == [3] and printed_K_support == []

    empty_losses = [norm_squared([[], []]) for _ in units]
    zero_matrix = matrix([[0, 0], [0, 0]])
    zero_losses = [error(zero_matrix, u, [F(0), F(0)]) for u in units]
    assert empty_losses == [0]*5 and zero_losses == [0]*5
    sign_u, sign_a = units[2], [F(2), -F(3)]
    assert outer(sign_u, sign_a) == outer([-z for z in sign_u], [-z for z in sign_a])

    result = {
        'role': 'Curator exact algebra; not independent scientific approval or model training.',
        'domain': 'Constructed finite real matrices; exact Fraction arithmetic; no numerical SVD or author implementation.',
        'grid': {'certified_two_by_two_spectra': count, 'old_feasible_comparisons': comparisons,
                 'zero_spectrum_cases': zero_spectrum, 'positive_repeated_top_cases': repeated_top,
                 'coverage': 'Five rational rotations on each side; integer 0<=t<=s<=3; 35 old feasible rank-one choices per case.'},
        'support_restriction': {'E': e, 'Y': y, 'old_loss': old_loss, 'restricted_loss': restricted_loss,
                                'restricted_X': restricted_x, 'unrestricted_X': unrestricted_x,
                                'sample_2_budget': 1},
        'repeated_singular_value': {'E': identity, 'optimal_error': 1, 'alternatives': alternatives},
        'sequential_vs_parallel': {'Y': y1, 'initial_D': initial_d, 'initial_X': initial_x,
                                  'updated_D': updated_d, 'sequential_X': sequential_x,
                                  'parallel_X': parallel_x, 'losses_initial_sequential_parallel': losses},
        'arbitrary_recoding_negative_control': {'Y': y2, 'old_D': identity, 'old_X': old_x2,
                                              'feasible_recoding_X': bad_x2, 'post_sweep_D': final_d2,
                                              'post_sweep_X': final_x2, 'losses_old_recoded_swept': recoding_losses,
                                              'scope': 'Deliberately poor feasible coder, not a counterexample to a specified OMP implementation.'},
        'centroid_vs_unit_atom': {'Y': ys, 'unconstrained_centroid': [F(2), F(0)],
                                 'unit_atom': [F(1), F(0)], 'free_coefficient': 2,
                                 'losses_centroid_fixed_one_unit_free_gain': [centroid_loss, fixed_one_unit_loss, free_gain_loss]},
        'source_equation_22_range': {'N': 3, 'K': 2, 'coefficient_row': row,
                                   'Figure_2_support': correct_support, 'literal_Equation_22_support': printed_K_support},
        'empty_active_set': {'unit_atom_choices_tested': len(units), 'block_losses': empty_losses,
                             'meaning': 'No active column determines an atom; retaining or replacing it requires a policy.'},
        'zero_residual_block': {'E': zero_matrix, 'unit_atom_choices_tested': len(units), 'losses': zero_losses,
                                'meaning': 'Zero coefficients are optimal and the unit atom is not identified.'},
        'simultaneous_atom_row_sign_flip': {'verified': True},
        'limits': ['No universal algorithm convergence or local-minimum theorem follows from these finite checks.',
                   'Grid certificates supplement algebra; they do not validate an arbitrary floating-point SVD routine.',
                   'No empirical recovery, uniqueness of a learned dictionary, runtime or benchmark assertion.']}
    print(json.dumps(serialize(result), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
