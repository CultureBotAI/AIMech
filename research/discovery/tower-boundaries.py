"""Exact finite circle-shift checks, written by the AIMech author workflow.

Portable standard-library calculator; no author software, random simulation,
filesystem access or runtime metadata. Execution prints deterministic JSON only.
The maintained construction uses strictly positive weights and 0 < shift < W.
Explicit zero-mass and shift=W tests below are separate boundary extensions.
Source formulas: Suwa 2208.03935v2 pp.3-4/8; Neal 2024 pp.37/39/41;
Suwa-Todo 1007.2262v2 pp.2-3. Finite checks do not prove all-target statements.
"""
from fractions import Fraction as F
from itertools import product
from math import gcd
import json


def weights(values, allow_zero=False):
    w = tuple(F(x) for x in values)
    assert w and sum(w) > 0
    assert all(x >= 0 if allow_zero else x > 0 for x in w)
    return w


def starts(w):
    out = []
    total = F(0)
    for x in w:
        out.append(total)
        total += x
    return out


def intersect(a, b, c, d):
    return max(F(0), min(b, d) - max(a, c))


def arc_geometry(w, s, sign=1):
    """Split a translated circular interval, then intersect destination boxes."""
    W, c = sum(w), starts(w)
    out = []
    for i, wi in enumerate(w):
        a = (c[i] + sign * s) % W
        end = a + wi
        pieces = [(a, min(end, W))]
        if end > W:
            pieces.append((F(0), end - W))
        out.append([sum(intersect(a, b, c[j], c[j] + wj)
                        for a, b in pieces) for j, wj in enumerate(w)])
    return out


def suwa_flow(w, s):
    """v2 Eq.11-12 / v1 Eq.12-13, with unnormalized positive total W."""
    W, c = sum(w), starts(w)
    def entry(i, j):
        delta = c[i] + w[i] - c[j] + s
        return sum(max(F(0), min(d, w[i] + w[j] - d, w[i], w[j]))
                   for d in [delta, delta - W])
    return [[entry(i, j) for j in range(len(w))] for i in range(len(w))]


def neal_flow(w, s):
    """Neal Eq.98, generalized to total W as discussed on pp.37/40."""
    W, c = sum(w), starts(w)
    def entry(i, j):
        delta = w[i] - s + c[i] - c[j]
        return sum(max(F(0), min(d, w[i] + w[j] - d, w[i], w[j]))
                   for d in [delta, delta + W])
    return [[entry(i, j) for j in range(len(w))] for i in range(len(w))]


def pick_half_open(w, k, s, r, sign=1):
    """The mathematical interval convention, with 0 <= r < 1."""
    assert w[k] > 0 and F(0) <= r < F(1)
    W, c = sum(w), starts(w)
    x = (c[k] + r * w[k] + sign * s) % W
    return next(j for j, wj in enumerate(w) if c[j] <= x < c[j] + wj)


def printed_alg7(p, k, s, r):
    """Literal normalized exact-arithmetic traversal, including closed endpoints."""
    assert sum(p) == 1 and 0 <= r <= 1
    u = sum(p[:k]) + r * p[k] - s
    if u <= 0:
        u += 1
    i, total, chosen = 0, F(0), None
    while i < len(p) and u > total:
        if p[i] > 0:
            total += p[i]
            chosen = i
        i += 1
    return chosen


def uniform_integral(w, s, sign=1, printed=False):
    """Integrate piecewise-constant destination labels over exact uniform r.

    Breakpoints are the preimages of destination interval boundaries. This
    implementation does not use overlap or the source min/max flow formula.
    Midpoint evaluation excludes boundary points, whose uniform measure is zero.
    """
    W, c = sum(w), starts(w)
    p = [x / W for x in w]
    out, cells = [], 0
    for i, wi in enumerate(w):
        assert wi > 0
        cuts = {F(0), F(1)}
        for b in c + [W]:
            for turn in [-1, 0, 1, 2]:
                r = (b + turn * W - c[i] - sign * s) / wi
                if 0 < r < 1:
                    cuts.add(r)
        cuts = sorted(cuts)
        row = [F(0)] * len(w)
        for a, b in zip(cuts, cuts[1:]):
            r = (a + b) / 2
            j = printed_alg7(p, i, s / W, r) if printed else pick_half_open(w, i, s, r, sign)
            assert j is not None
            row[j] += (b - a) * wi
            cells += 1
        out.append(row)
    return out, cells


def kernel(w, s, sign=1):
    w = weights(w)
    assert 0 < s < sum(w)
    return rows(arc_geometry(w, F(s), sign), w)


def rows(v, w):
    return [[x / w[i] for x in row] if w[i] else None for i, row in enumerate(v)]


def transpose(a):
    return [list(x) for x in zip(*a)]


def balance(v, w):
    assert all(x >= 0 for row in v for x in row)
    assert [sum(row) for row in v] == list(w)
    assert [sum(row) for row in transpose(v)] == list(w)


def stationary(p, a):
    assert all(x >= 0 for row in a for x in row)
    assert all(sum(row) == 1 for row in a)
    result = [sum(p[i] * a[i][j] for i in range(len(p))) for j in range(len(p))]
    assert result == list(p)
    return result


def reversible(p, a):
    return all(p[i] * a[i][j] == p[j] * a[j][i]
               for i in range(len(p)) for j in range(len(p)))


def in_order(w, order, s, sign=1):
    assert sorted(order) == list(range(len(w)))
    v = arc_geometry([w[i] for i in order], s, sign)
    out = [[F(0)] * len(w) for _ in w]
    for i, label_i in enumerate(order):
        for j, label_j in enumerate(order):
            out[label_i][label_j] = v[i][j]
    return out


def suwa_todo_2010(w):
    """Printed Eq.5-8: maximum first, and S_0 is W rather than zero."""
    assert w[0] == max(w)
    W, c = sum(w), starts(w)
    def entry(i, j):
        delta = c[i] + w[i] - (c[j] if j else W) + w[0]
        return max(F(0), min(delta, w[i] + w[j] - delta, w[i], w[j]))
    return [[entry(i, j) for j in range(len(w))] for i in range(len(w))]


def alg6_row(p, k, s):
    """Printed shortcut and exact normalized nonshortcut row; positive p only."""
    if p[k] >= F(1, 2):
        return [(2 * p[k] - 1) / p[k] if i == k else min(F(1), p[i] / p[k])
                for i in range(len(p))]
    flow = neal_flow(p, s)[k]
    return [x / sum(flow) for x in flow]


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def graph_classes(a):
    """Finite positive-edge SCCs, closedness and exact graph periods."""
    n = len(a)
    edges = [[j for j in range(n) if a[i][j] > 0] for i in range(n)]
    reach = []
    for i in range(n):
        seen, stack = {i}, [i]
        while stack:
            for j in edges[stack.pop()]:
                if j not in seen:
                    seen.add(j)
                    stack.append(j)
        reach.append(seen)
    left, result = set(range(n)), []
    while left:
        root = min(left)
        group = {j for j in left if j in reach[root] and root in reach[j]}
        left -= group
        dist, queue = {root: 0}, [root]
        for i in queue:
            for j in edges[i]:
                if j in group and j not in dist:
                    dist[j] = dist[i] + 1
                    queue.append(j)
        period = 0
        for i in group:
            for j in edges[i]:
                if j in group:
                    period = gcd(period, abs(dist[i] + 1 - dist[j]))
        result.append(dict(states_zero_based=sorted(group), period=period,
                           closed=all(j in group for i in group for j in edges[i])))
    return result


def main():
    counts = dict(positive_weight_vectors=0, interior_shift_cases=0,
                  formula_geometry_orientation_comparisons=0,
                  uniform_integration_rows=0, uniform_partition_cells=0,
                  printed_alg7_integrated_rows=0, printed_alg7_partition_cells=0,
                  policy_rows_checked=0, maximum_first_2010_cases=0,
                  reverse_paired_order_cases=0, scaling_cases=0,
                  zero_extension_vectors=0, zero_extension_shift_cases=0,
                  zero_current_rows_left_undefined=0)
    # Ordered vectors; normalized duplicates remain distinct. Every formula
    # breakpoint, interval midpoint, plus specified policy/example shifts is used.
    for n in range(1, 6):
        for raw in product([1, 2, 3], repeat=n):
            w = weights(raw)
            W, c = sum(w), starts(w)
            p, M = [x / W for x in w], max(w)
            points = {F(0), W, W / 2, M, W - M, W / 10, W / 3, 2 * W / 3, 9 * W / 10}
            points.update((a - b) % W for a in c for b in c)
            ordered = sorted(points)
            shifts = sorted(({x for x in points if 0 < x < W}
                             | {(a + b) / 2 for a, b in zip(ordered, ordered[1:])}))
            counts['positive_weight_vectors'] += 1
            for s in shifts:
                plus, minus = suwa_flow(w, s), neal_flow(w, s)
                assert plus == arc_geometry(w, s, 1)
                assert minus == arc_geometry(w, s, -1) == transpose(plus)
                assert minus == in_order(w, tuple(reversed(range(n))), s, 1)
                balance(plus, w); balance(minus, w)
                integrated, cells = uniform_integral(w, s)
                assert plus == integrated
                sampled, algcells = uniform_integral(w, s, -1, printed=True)
                assert minus == sampled
                self_flow = sum(plus[i][i] for i in range(n))
                assert self_flow == sum(max(F(0), x - s) + max(F(0), x + s - W) for x in w)
                bound = max(F(0), 2 * M - W)
                assert self_flow >= bound
                assert (self_flow == bound) == (min(M, W - M) <= s <= max(M, W - M))
                if M <= W / 2:
                    assert (self_flow == 0) == (M <= s <= W - M)
                if s == W / 2:
                    assert plus == minus
                scale = F(7, 3)
                assert suwa_flow([scale * x for x in w], scale * s) == [[scale * x for x in row] for row in plus]
                counts['interior_shift_cases'] += 1
                counts['formula_geometry_orientation_comparisons'] += 2
                counts['uniform_integration_rows'] += n
                counts['uniform_partition_cells'] += cells
                counts['printed_alg7_integrated_rows'] += n
                counts['printed_alg7_partition_cells'] += algcells
                counts['scaling_cases'] += 1
            for s in [W / 2, M]:
                if s == W:  # Separate maximum-shift point-mass boundary below.
                    continue
                v = neal_flow(w, s)
                assert sum(v[i][i] for i in range(n)) == max(F(0), 2 * M - W)
                for k in range(n):
                    assert alg6_row(p, k, s / W) == rows(v, w)[k]
                    counts['policy_rows_checked'] += 1
            chosen = next(i for i, x in enumerate(w) if x == M)
            rotation = tuple(range(chosen, n)) + tuple(range(chosen))
            rw = [w[i] for i in rotation]
            assert suwa_todo_2010(rw) == arc_geometry(rw, M)
            counts['maximum_first_2010_cases'] += 1
            tail = sorted((i for i in range(n) if i != chosen), key=lambda i: (w[i], i))
            up, down = (chosen, *tail), (chosen, *reversed(tail))
            uv, dv = in_order(w, up, M), in_order(w, down, M)
            assert uv == transpose(dv)
            mix = [[(uv[i][j] + dv[i][j]) / 2 for j in range(n)] for i in range(n)]
            balance(mix, w)
            assert mix == transpose(mix)
            assert sum(mix[i][i] for i in range(n)) == max(F(0), 2 * M - W)
            counts['reverse_paired_order_cases'] += 1

    # Nonnegative flows are a separate audit extension. Unsupported rows stay
    # undefined; no preferred completion is inferred from these equations.
    for n in range(1, 5):
        for raw in product([0, 1, 2, 3], repeat=n):
            if not sum(raw):
                continue
            w = weights(raw, allow_zero=True)
            W = sum(w)
            counts['zero_extension_vectors'] += 1
            for s in [W / 10, W / 3, W / 2, 2 * W / 3, 9 * W / 10, max(w)]:
                plus, minus = suwa_flow(w, s), neal_flow(w, s)
                assert plus == arc_geometry(w, s) and minus == arc_geometry(w, s, -1)
                assert plus == transpose(minus)
                balance(plus, w); balance(minus, w)
                supported = [i for i, x in enumerate(w) if x]
                compact = arc_geometry([w[i] for i in supported], s)
                assert [[plus[i][j] for j in supported] for i in supported] == compact
                counts['zero_current_rows_left_undefined'] += sum(x == 0 for x in w)
                counts['zero_extension_shift_cases'] += 1

    p = weights([F(2, 5), F(3, 10), F(1, 10), F(1, 5)])
    orientation = dict(pi=p, shift=max(p), positive=kernel(p, max(p)),
                       negative=kernel(p, max(p), -1), half=kernel(p, F(1, 2)))
    assert orientation['positive'][0] == [0, F(3, 4), F(1, 4), 0]
    assert orientation['negative'][0] == [0, F(1, 4), F(1, 4), F(1, 2)]
    p = weights([F(3, 5), F(2, 5)])
    nonhalf = kernel(p, F(1, 10))
    assert reversible(p, nonhalf)
    shortcut = dict(pi=p, shift=F(1, 10), current_zero_based=0,
                    geometry_row=nonhalf[0], printed_alg6=alg6_row(p, 0, F(1, 10)))
    assert shortcut['geometry_row'] == [F(5, 6), F(1, 6)]
    assert shortcut['printed_alg6'] == [F(1, 3), F(2, 3)]
    p = weights([F(1, 5), F(3, 10), F(1, 2)])
    ret = printed_alg7(p, 0, F(1, 2), F(0))
    exact = kernel(p, F(1, 2), -1)
    assert ret == 1 and exact[0] == [0, 0, 1] and exact[0][ret] == 0
    endpoint = dict(pi=p, shift=F(1, 2), current_zero_based=0, r=F(0),
                    printed_return_zero_based=ret, transition_probability=exact[0][ret],
                    exact_row=exact[0], half_open_return_zero_based=pick_half_open(p, 0, F(1, 2), F(0), -1))

    periodicity = []
    for n in range(1, 10):
        w = weights([1] * n)
        h = kernel(w, F(n, 2))
        st = rows(arc_geometry(w, F(1)), w)  # n=1 is explicit endpoint extension.
        hc, sc = graph_classes(h), graph_classes(st)
        assert len(sc) == 1 and sc[0]['period'] == n
        if n % 2 == 0:
            assert len(hc) == n // 2 and all(x['period'] == 2 and x['closed'] for x in hc)
        else:
            assert len(hc) == 1 and hc[0]['period'] == 1
        periodicity.append(dict(states=n, maximum_shift=st, half_shift=h,
                                maximum_classes=sc, half_classes=hc))

    # Two individually irreducible local three-cycles give a reducible full scan.
    states = list(product(range(3), repeat=2))
    scan = [[F((c, d) == ((a + 1) % 3, (b + 1) % 3)) for c, d in states] for a, b in states]
    uniform = [F(1, 9)] * 9
    stationary(uniform, scan)
    classes = graph_classes(scan)
    assert len(classes) == 3 and all(x['period'] == 3 and x['closed'] for x in classes)

    # Positive correlated binary target: each half-shift coordinate update is
    # reversible, while their fixed ordered composition need not be reversible.
    joint_weights = [F(1), F(2), F(3), F(4)]
    binary = list(product(range(2), repeat=2))
    target = [x / sum(joint_weights) for x in joint_weights]
    updates = []
    for coordinate in [0, 1]:
        a = [[F(0)] * 4 for _ in range(4)]
        for i, state in enumerate(binary):
            labels = [j for j, other in enumerate(binary) if other[1 - coordinate] == state[1 - coordinate]]
            local = [joint_weights[j] for j in labels]
            local_k = kernel(local, sum(local) / 2)
            for j in labels:
                a[i][j] = local_k[labels.index(i)][labels.index(j)]
        stationary(target, a)
        assert reversible(target, a)
        updates.append(a)
    composition = matmul(*updates)
    mixture = [[(updates[0][i][j] + updates[1][i][j]) / 2 for j in range(4)] for i in range(4)]
    stationary(target, composition); stationary(target, mixture)
    assert not reversible(target, composition) and reversible(target, mixture)

    # Invalid row-dependent order: these three rows do not share one kernel.
    uniform3 = weights([F(1, 3)] * 3)
    orders = [(0, 1, 2), (1, 0, 2), (2, 0, 1)]
    bad = [rows(in_order(uniform3, order, F(1, 3)), uniform3)[i] for i, order in enumerate(orders)]
    bad_after = [sum(uniform3[i] * bad[i][j] for i in range(3)) for j in range(3)]
    assert bad_after == [F(2, 3), F(1, 3), F(0)]

    # Two unsupported-row completions have identical invariant supported mass.
    w = weights([0, 1, 2], allow_zero=True)
    partial = rows(arc_geometry(w, sum(w) / 2), w)
    completions = [[list(row) if row is not None else zero for row in partial]
                   for zero in [[F(1), F(0), F(0)], [F(0), F(1), F(0)]]]
    for a in completions:
        stationary([F(0), F(1, 3), F(2, 3)], a)
    point = dict(interior=kernel([F(5)], F(7, 3)), maximum_endpoint_extension=rows(arc_geometry([F(5)], F(5)), [F(5)]))
    assert point['interior'] == point['maximum_endpoint_extension'] == [[1]]

    output = dict(
        scope='Exact finite original curator calculations. Positive ordered integer vectors of lengths 1..5 with entries 1..3; duplicates after normalization retained. Shift sets include all cumulative-boundary differences, adjacent midpoints and policy/example shifts. Nonnegative extension and endpoint policies are counted separately. No floating implementation, author-code or benchmark execution.',
        counts=counts,
        orientation_example=orientation,
        reversible_nonhalf=dict(pi=[F(3, 5), F(2, 5)], shift=F(1, 10), matrix=nonhalf),
        arbitrary_shift_shortcut=shortcut,
        closed_endpoint=endpoint,
        periodicity=periodicity,
        systematic_scan_counterexample=dict(states=states, target=uniform, matrix=scan, classes=classes),
        reversible_local_nonreversible_composition=dict(states=binary, target=target, local_updates=updates,
                                                       ordered_composition=composition, equal_mixture=mixture),
        current_dependent_order_counterexample=dict(pi=uniform3, orders_zero_based=orders, matrix=bad, after=bad_after),
        zero_row_nonuniqueness=dict(weights=w, partial_rows=partial, completions=completions),
        point_mass=point,
        qualifications=['The printed-source negative controls are retained; no source erratum or universal defect in either orientation is inferred.',
                        'Only exactly reverse-paired UST/DST orders, including tied labels, justify transpose/equal-mixture checks.',
                        'Zero current rows and maximum-shift point-mass endpoints are outside the maintained positive/interior specification.',
                        'The direct lower bound follows because total incoming flow from other states is at most W-w_max; finite checks do not establish efficiency or convergence.'])
    print(json.dumps(output, default=str, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
