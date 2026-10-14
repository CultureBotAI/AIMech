#!/usr/bin/env python3
"""Deterministic rational illustrations for Neal's 2004 and 2020 mechanisms.

Prints JSON to stdout; no files, network, timestamps, randomness, or third-party
packages. This is original finite checking code, not author-code replication,
a benchmark, or a proof of the general asymptotic-variance theorem.
"""
from fractions import Fraction as F
from itertools import product
import json


def canonical(segments):
    """Sum piecewise-constant joint densities (state, left, right, density)."""
    out = []
    for x in sorted({s[0] for s in segments}):
        subset = [s for s in segments if s[0] == x and s[1] < s[2] and s[3]]
        edges = sorted({v for s in subset for v in s[1:3]})
        for left, right in zip(edges, edges[1:]):
            mid = (left + right) / 2
            density = sum((d for _, a, b, d in subset if a < mid < b), F(0))
            if not density:
                continue
            if out and out[-1][0] == x and out[-1][2] == left and out[-1][3] == density:
                out[-1] = (x, out[-1][1], right, density)
            else:
                out.append((x, left, right, density))
    return out


def joint(pi):
    assert all(p > 0 for p in pi) and sum(pi) == 1
    return [(x, F(-1), F(1), p / 2) for x, p in enumerate(pi)]


def mass(segments, state=None, left=F(-1), right=F(1)):
    return sum((max(F(0), min(b, right) - max(a, left)) * d
                for x, a, b, d in segments if state is None or x == state), F(0))


def translate(segments, shifts):
    """Independent finite shift mixture, wrapped modulo 2 into [-1,1)."""
    assert sum(w for _, w in shifts) == 1 and all(w >= 0 for _, w in shifts)
    out = []
    for x, a, b, d in segments:
        for shift, weight in shifts:
            a1, b1 = a + shift, b + shift
            first, last = (a1 + 1) // 2, (b1 + 1) // 2
            for k in range(first, last + 1):
                lo, hi = max(a1, 2 * k - 1), min(b1, 2 * k + 1)
                if lo < hi:
                    out.append((x, lo - 2 * k, hi - 2 * k, d * weight))
    result = canonical(out)
    assert mass(result) == mass(segments)
    return result


def refresh(segments, n):
    """Fully regenerate signed v independently, preserving the x marginal."""
    return canonical([(x, F(-1), F(1), mass(segments, x) / 2) for x in range(n)])


def accept_rescale(segments, pi, proposal, rescale=True):
    """Push forward the density-ratio accept/rescale rule exactly.

    A symmetric stochastic proposal is required for the invariance claims.
    Asymmetric proposals are allowed here solely to calculate a negative control.
    Boundaries have measure zero and do not affect these continuous densities.
    """
    assert all(sum(row) == 1 and all(q >= 0 for q in row) for row in proposal)
    out = []
    for x, left, right, density in segments:
        for y, q in enumerate(proposal[x]):
            if not q:
                continue
            cutoff = min(F(1), pi[y] / pi[x])
            cuts = sorted({left, right} | {v for v in (-cutoff, cutoff) if left < v < right})
            for a, b in zip(cuts, cuts[1:]):
                accepted = abs((a + b) / 2) < cutoff
                scale = pi[x] / pi[y] if accepted and rescale else F(1)
                out.append((y if accepted else x, a * scale, b * scale, density * q / scale))
    result = canonical(out)
    assert mass(result) == mass(segments)
    return result


def uniform_checks():
    pi = [F(1, 3), F(2, 3)]
    flip = [[F(0), F(1)], [F(1), F(0)]]
    initial = joint(pi)
    good = accept_rescale(initial, pi, flip)
    assert good == initial
    wrong_first = accept_rescale(initial, pi, flip, False)
    wrong_second = accept_rescale(wrong_first, pi, flip, False)
    assert [mass(wrong_first, x) for x in range(2)] == pi
    assert wrong_first != initial
    assert mass(wrong_second, 0) == F(1, 6)

    # A reversible threshold translation does not imply reversible composition.
    a = [(0, F(0), F(1, 4), pi[0] / 2)]
    b = [(1, F(-1, 2), F(-3, 8), pi[1] / 2)]
    half_forward = mass(accept_rescale(translate(a, [(F(1), F(1))]), pi, flip), 1, F(-1, 2), F(-3, 8))
    half_reverse = mass(accept_rescale(translate(b, [(F(1), F(1))]), pi, flip), 0, F(0), F(1, 4))
    assert half_forward == F(1, 24) and half_reverse == 0
    assert translate(translate(initial, [(F(1), F(1))]), [(F(1), F(1))]) == initial
    # Stronger direct check of the involution on a restricted, nonuniform set.
    assert translate(translate(a, [(F(1), F(1))]), [(F(1), F(1))]) == a

    # Refresh-then-accept has an ordinary Metropolis x process, but the full
    # output state includes the rescaled v and need not be reversible.
    b_refresh = [(1, F(0), F(1, 8), pi[1] / 2)]
    refresh_forward = mass(accept_rescale(refresh(a, 2), pi, flip), 1, F(0), F(1, 8))
    refresh_reverse = mass(accept_rescale(refresh(b_refresh, 2), pi, flip), 0, F(0), F(1, 4))
    assert refresh_forward == F(1, 192) and refresh_reverse == F(1, 384)

    asymmetric = [[F(1, 2), F(1, 2)], [F(1), F(0)]]
    asym_output = accept_rescale(initial, pi, asymmetric)
    assert mass(asym_output, 0) == F(1, 2)

    family_count = 0
    for n in (2, 3):
        proposals = [[[F(1, n) for _ in range(n)] for _ in range(n)]]
        if n == 2:
            proposals.append(flip)
        else:
            proposals.append([[F(1, 2), F(1, 2), F(0)],
                              [F(1, 2), F(0), F(1, 2)],
                              [F(0), F(1, 2), F(1, 2)]])
        for weights in product(range(1, 4), repeat=n):
            target = [F(w, sum(weights)) for w in weights]
            for proposal in proposals:
                assert all(proposal[x][y] == proposal[y][x] for x in range(n) for y in range(n))
                for shift in (F(0), F(1), F(1, 3), F(7, 3)):
                    for noise in ([(F(0), F(1))], [(F(-1, 5), F(1, 3)), (F(2, 5), F(2, 3))]):
                        shifts = [(shift + value, probability) for value, probability in noise]
                        output = accept_rescale(translate(joint(target), shifts), target, proposal)
                        assert output == joint(target)
                        family_count += 1

    return {
        'assumptions': 'Positive finite target, symmetric stochastic proposal independent of signed v; exact continuous piecewise densities; shift/noise independent of v. Endpoint choices have measure zero.',
        'target': pi, 'proposal': flip,
        'derived_correct_joint_density': good,
        'derived_omitted_rescale_first_density': wrong_first,
        'derived_omitted_rescale_second_density': wrong_second,
        'omitted_rescale_second_state0_mass': mass(wrong_second, 0),
        'half_period_composition_flux': {'A': a, 'B': b, 'A_to_B': half_forward, 'B_to_A': half_reverse},
        'full_refresh_composition_flux': {'A': a, 'B': b_refresh, 'A_to_B': refresh_forward, 'B_to_A': refresh_reverse},
        'asymmetric_proposal_negative_control': {'proposal': asymmetric, 'output_density': asym_output, 'state0_mass': mass(asym_output, 0)},
        'joint_invariance_family_cases': family_count,
        'boundary': 'A half-period wrapped translation is reversible by itself, yet translation-then-accept can be nonreversible. Full uniform refresh recovers ordinary Metropolis for x, but does not ensure augmented-chain detailed balance. Zero shift/no noise leaves the under-density height fixed and supplies no ergodicity guarantee.'}


def liu_conditional(q):
    """Equation (16) on the positive support, with point-mass guard."""
    support = [i for i, p in enumerate(q) if p]
    result = {}
    for a in support:
        if q[a] == 1:
            result[a] = [F(int(c == a)) for c in range(len(q))]
            continue
        row = [F(0)] * len(q)
        for c in support:
            if c != a:
                row[c] = min(q[c] / (1 - q[a]), q[c] / (1 - q[c]))
                # Derive the same transition via conditional proposal × MH acceptance.
                proposal_then_accept = q[c] / (1 - q[a]) * min(F(1), (1 - q[a]) / (1 - q[c]))
                assert row[c] == proposal_then_accept
        row[a] = 1 - sum(row)
        assert all(p >= 0 for p in row) and sum(row) == 1
        result[a] = row
    for a, c in product(support, repeat=2):
        assert q[a] * result[a][c] == q[c] * result[c][a]
        if a != c:
            assert result[a][c] >= q[c]
        else:
            assert result[a][a] <= q[a]
    return result


def reachable(matrix, start):
    seen, todo = {start}, [start]
    while todo:
        for j, p in enumerate(matrix[todo.pop()]):
            if p and j not in seen:
                seen.add(j)
                todo.append(j)
    return seen


def irreducible(matrix):
    return all(len(reachable(matrix, i)) == len(matrix) for i in range(len(matrix)))


def lift(base, pi):
    n = len(base)
    assert all(sum(row) == 1 and all(p >= 0 for p in row) for row in base)
    assert sum(pi) == 1 and all(p > 0 for p in pi)
    assert all(pi[a] * base[a][b] == pi[b] * base[b][a] for a, b in product(range(n), repeat=2))
    states = [(a, b) for a, b in product(range(n), repeat=2) if base[a][b]]
    conditionals = [liu_conditional(row) for row in base]
    matrix = [[conditionals[b][a][c] if d == b else F(0) for d, c in states] for a, b in states]
    mu = [pi[a] * base[a][b] for a, b in states]
    assert all(sum(row) == 1 for row in matrix)
    assert all(sum(mu[i] * matrix[i][j] for i in range(len(states))) == mu[j] for j in range(len(states)))
    return states, matrix, mu


def solve(matrix, vector):
    """Exact Gaussian elimination; raises if the requested system is singular."""
    a = [row[:] + [value] for row, value in zip(matrix, vector)]
    n = len(a)
    for col in range(n):
        pivot = next(i for i in range(col, n) if a[i][col])
        a[col], a[pivot] = a[pivot], a[col]
        scale = a[col][col]
        a[col] = [v / scale for v in a[col]]
        for row in range(n):
            if row != col and a[row][col]:
                scale = a[row][col]
                a[row] = [x - scale * y for x, y in zip(a[row], a[col])]
    return [row[-1] for row in a]


def asymptotic_variance(matrix, pi, values):
    """Finite irreducible-chain Poisson-equation variance, with exact arithmetic."""
    assert irreducible(matrix)
    n = len(pi)
    mean = sum(p * x for p, x in zip(pi, values))
    g = [x - mean for x in values]
    h = solve([[F(int(i == j)) - matrix[i][j] + pi[j] for j in range(n)] for i in range(n)], g)
    assert all(h[i] - sum(matrix[i][j] * h[j] for j in range(n)) == g[i] for i in range(n))
    assert sum(pi[i] * h[i] for i in range(n)) == 0
    result = 2 * sum(pi[i] * g[i] * h[i] for i in range(n)) - sum(pi[i] * g[i] ** 2 for i in range(n))
    assert result >= 0
    return result


def backtracking_checks():
    triangle = [[F(0) if i == j else F(1, 2) for j in range(3)] for i in range(3)]
    pi = [F(1, 3)] * 3
    states, matrix, mu = lift(triangle, pi)
    classes = sorted({tuple(sorted(reachable(matrix, i))) for i in range(len(matrix))})
    assert irreducible(triangle) and not irreducible(matrix)
    assert sum(triangle[0][i] * triangle[i][0] for i in range(3)) > 0
    assert sum(triangle[0][i] * triangle[i][j] * triangle[j][0]
               for i, j in product(range(3), repeat=2)) > 0  # Coprime return lengths.
    assert len(classes) == 2 and all(len(c) == 3 for c in classes)
    assert all(all(matrix[i][j] == 0 for i in c for j in range(len(matrix)) if j not in c) for c in classes)
    assert all(all(sum(mu[i] for i in c if states[i][1] == x) / sum(mu[i] for i in c) == pi[x] for x in range(3)) for c in classes)
    # A two-state alternating baseline has point-mass conditionals: never divide by zero.
    point_states, point_matrix, point_mu = lift([[F(0), F(1)], [F(1), F(0)]], [F(1, 2)] * 2)
    assert point_matrix == [[F(0), F(1)], [F(1), F(0)]]

    q = [F(3, 5), F(3, 10), F(1, 10)]
    valid = liu_conditional(q)[0]
    printed_acceptance = 1 / (1 - q[1])
    clipped_transition = q[1] * min(F(1), printed_acceptance)
    assert printed_acceptance == F(10, 7) and valid[1] == F(3, 7)
    assert clipped_transition == F(3, 10) and clipped_transition != valid[1]
    assert valid[0] == F(29, 63) > 0  # Suppression need not eliminate returns.

    families, comparisons, strict = 0, 0, 0
    example = None
    for edge_weights in product(range(1, 4), repeat=3):
        for self_weight in (1, 2):
            a, b, c = edge_weights
            weights = [[self_weight, a, b], [a, self_weight, c], [b, c, self_weight]]
            row_sums = [sum(row) for row in weights]
            target = [F(w, sum(row_sums)) for w in row_sums]
            base = [[F(w, row_sums[i]) for w in row] for i, row in enumerate(weights)]
            expanded_states, expanded, invariant = lift(base, target)
            assert irreducible(base) and irreducible(expanded)
            values = []
            for label in range(3):
                old = asymptotic_variance(base, target, [F(int(i == label)) for i in range(3)])
                new = asymptotic_variance(expanded, invariant, [F(int(y == label)) for _, y in expanded_states])
                assert new <= old
                comparisons += 1
                strict += int(new < old)
                values.append({'coordinate_indicator': label, 'baseline_asymptotic_variance': old, 'expanded_asymptotic_variance': new})
            if example is None:
                example = {'base': base, 'pi': target, 'indicator_comparisons': values}
            families += 1
    return {
        'assumptions': 'Finite reversible baseline, positive invariant mass, positive-support pair states; Liu conditional point-mass boundary handled explicitly. The variance calculation is applied only after verifying expanded irreducibility.',
        'triangle': {'base': triangle, 'pi': pi, 'expanded_states': states, 'expanded_invariant': mu, 'expanded_transition': matrix, 'closed_classes': [[states[i] for i in group] for group in classes], 'boundary': 'Base is irreducible (also aperiodic); the lift has two closed orientation cycles. Each class in this example still has the correct projected marginal; this refutes automatic expanded irreducibility, not projected correctness for this particular example.'},
        'point_mass_conditional': {'expanded_states': point_states, 'expanded_transition': point_matrix, 'expanded_invariant': point_mu},
        'printed_fast_simulator': {'conditional': q, 'current_index': 0, 'proposal_index': 1, 'printed_acceptance': printed_acceptance, 'equation16_conditional_row': valid, 'clipped_transition': clipped_transition, 'equation16_transition': valid[1], 'boundary': 'Neal2004 p.9 probability exceeds one as printed; clipping fails to implement p.8 Eq.(16). The conditional-proposal construction implements Eq.(16), but can be costly if the excluded mass is near one.'},
        'positive_conductance_family_cases': families,
        'single_coordinate_variance_comparisons': comparisons,
        'strict_variance_improvements': strict,
        'first_family_example': example,
        'boundary': 'The finite checks illustrate invariance, local balance, suppression, and the corrected variance boundary; they are not a general theorem or a speed claim.'}


def main():
    print(json.dumps({'scope': 'Exact deterministic original calculations, not author implementation, empirical reproduction, general proof, or independent scientific approval.', 'neal2020': uniform_checks(), 'neal2004': backtracking_checks()}, indent=2, default=str))


if __name__ == '__main__':
    main()
