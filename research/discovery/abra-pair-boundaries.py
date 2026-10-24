"""Finite curator arithmetic for ABRA pair estimators; no author code or benchmarks."""
from fractions import Fraction as F
from itertools import permutations, product
from math import exp, log, sqrt
import json


def shortest_paths(n, edges, source, target, directed=False):
    adjacency = [[] for _ in range(n)]
    for u, v, length in edges:
        assert length > 0
        adjacency[u].append((v, F(length)))
        if not directed:
            adjacency[v].append((u, F(length)))
    found = []
    def visit(path, length):
        if path[-1] == target:
            found.append((length, path))
            return
        for v, weight in adjacency[path[-1]]:
            if v not in path:
                visit(path + (v,), length + weight)
    visit((source,), F(0))
    if not found:
        return []
    distance = min(length for length, _ in found)
    return [path for length, path in found if length == distance]


def pair_rows(n, edges, directed=False):
    rows = []
    for source, target in permutations(range(n), 2):
        paths = shortest_paths(n, edges, source, target, directed)
        row = tuple(F(sum(w in p[1:-1] for p in paths), len(paths)) if paths else F(0)
                    for w in range(n))
        assert row[source] == row[target] == 0
        assert all(0 <= value <= 1 for value in row)
        rows.append(((source, target), row, paths))
    return rows


def mean(rows):
    return tuple(sum(row[w] for row in rows) / len(rows) for w in range(len(rows[0])))


def exact_rademacher(vectors):
    width = len(vectors[0])
    values = [max(sum(F(sign) * value for sign, value in zip(signs, vector))
                  for vector in vectors) / width
              for signs in product((-1, 1), repeat=width)]
    return sum(values) / len(values)


def norm_bound(vectors, r):
    width = len(vectors[0])
    terms = [r * r * float(sum(v * v for v in vector)) / (2 * width * width)
             for vector in set(vectors)]
    largest = max(terms)
    return (largest + log(sum(exp(x - largest) for x in terms))) / r


def deviation(omega, count, failure):
    ell = log(3 / failure)
    return 2 * omega + (ell + sqrt(ell * (ell + 4 * count * omega))) / count + sqrt(ell / (2 * count))


def main():
    cases = {
        'path3': (3, [(0, 1, 1), (1, 2, 1)], False),
        'diamond4': (4, [(0, 1, 1), (0, 2, 1), (1, 3, 1), (2, 3, 1)], False),
        'directed_chain3': (3, [(0, 1, 1), (1, 2, 1)], True),
        'weighted_triangle': (3, [(0, 1, 1), (1, 2, 1), (0, 2, 2)], False),
    }
    results = {}
    for label, (n, edges, directed) in cases.items():
        pairs = pair_rows(n, edges, directed)
        rows = [row for _, row, _ in pairs]
        truth = mean(rows)
        estimates = [tuple((a[w] + b[w]) / 2 for w in range(n)) for a, b in product(rows, repeat=2)]
        assert mean(estimates) == truth
        samples = rows[:4]
        vectors = list(set(tuple(row[w] for row in samples) for w in range(n)))
        rad = exact_rademacher(vectors)
        for r in (F(1, 2), F(1), F(4), F(10)):
            assert float(rad) <= norm_bound(vectors, float(r)) + 1e-12
        results[label] = dict(ordered_pairs=len(pairs), reachable_pairs=sum(bool(p) for _, _, p in pairs),
                             exact_ordered_pair_mean=[str(x) for x in truth],
                             one_and_two_draw_expectations_equal=True,
                             selected_sample_rademacher=str(rad))
    assert results['path3']['exact_ordered_pair_mean'] == ['0', '1/3', '0']
    assert results['directed_chain3']['exact_ordered_pair_mean'] == ['0', '1/6', '0']
    directed_rows = pair_rows(*cases['directed_chain3'][:2], directed=True)
    conditioned = mean([row for _, row, paths in directed_rows if paths])
    assert conditioned == (F(0), F(1, 3), F(0))
    serial = pair_rows(5, [(0,1,1),(0,2,1),(1,3,1),(2,3,1),(3,4,1)], directed=True)
    _, row, paths = next(x for x in serial if x[0] == (0,4))
    assert len(paths) == 2 and row == (0,F(1,2),F(1,2),1,0)
    vectors = [(F(0),F(0)), (F(1),F(0)), (F(0),F(1))]
    assert exact_rademacher(vectors) == F(3,8)
    assert exact_rademacher(vectors[:-1]) == F(1,4)
    assert sum(x*x for x in vectors[1]) == sum(x*x for x in vectors[2])
    p = F(1,3)
    stopped_mean = p + (1-p)*p/2
    assert stopped_mean == F(4,9)
    delta = F(1,20)
    budget = sum(delta / (2**i) for i in range(1,11))
    assert budget == delta*(1-F(1,1024))
    geometric = []
    for i in range(1,12):
        count = 16*2**(i-1)
        xi = deviation(0, count, float(delta/2**i))
        geometric.append(dict(stage=i, count=count, xi=xi))
        if xi <= .5:
            break
    assert geometric[-1]['xi'] <= .5
    lower_limit = sqrt(log(2)/2)
    assert lower_limit > .5
    return dict(cases=results,
                unreachable_pair_conditioning=dict(full_mean='1/6',conditioned_mean=str(conditioned[1])),
                multiple_shortest_paths=dict(paths=paths,fractions=[str(x) for x in row],
                                             shared_internal_raw_count=2,shared_internal_fraction='1'),
                vector_identity=dict(full_rademacher='3/8',after_invalid_equal_norm_merge='1/4',
                                     note='Equal norms do not identify sample vectors. This is not a claim that author software merges them.'),
                hypothetical_stopping=dict(fixed_mean='1/3',stop_on_first_one_else_take_two_mean=str(stopped_mean),
                                            note='Illustrates why unbiasedness at fixed size is not inherited by arbitrary stopping; not an ABRA failure example.'),
                stage_budget=dict(delta=str(delta),first_ten_stages=str(budget)),
                zero_score_complete_graph=dict(geometric_schedule=geometric,
                                               linear_schedule_lower_bound_limit=lower_limit,
                                               note='For S_i=i, the square-root term alone stays above sqrt(ln2/2), so epsilon=.5 cannot be met. Geometric example terminates.'),
                scope='Finite exact paths, pair expectations and Rademacher signs, with floating evaluation of explicit bounds; no author code, benchmark or empirical guarantee.')


if __name__ == '__main__':
    print(json.dumps(main(), indent=2))
