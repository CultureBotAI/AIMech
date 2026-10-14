"""Finite curator arithmetic for RAND; no author implementation or benchmark.

For iid uniform sources X_i and Z_i=n*d(X_i,u)/(n-1), E Z_i=mu(u).
Hoeffding with range R=n*Delta/(n-1) gives
P(|mean Z_i-mu| >= xi) <= 2 exp(-2*k*xi**2/R**2).
The union bound multiplies by n, irrespective of dependence across targets.
Setting xi=epsilon*Delta and requiring that bound <= failure gives the
sample count below. The finite checks illustrate, rather than prove, this.
"""
from fractions import Fraction as F
from itertools import product
import json
import math


def estimates(distances, sources):
    n = len(distances)
    assert n > 1 and sources
    means = [F(n, len(sources) * (n - 1)) * sum(distances[s][u] for s in sources)
             for u in range(n)]
    reciprocals = [None if x == 0 else 1 / x for x in means]
    return means, reciprocals


def exact_means(distances):
    n = len(distances)
    return [sum(distances[v][u] for v in range(n)) / (n - 1) for u in range(n)]


def main():
    distances = [[F(abs(v-u)) for u in range(3)] for v in range(3)]
    exact = exact_means(distances)
    samples = list(product(range(3), repeat=2))
    values = [estimates(distances, s) for s in samples]
    expected = [sum(m[u] for m, _ in values) / len(values) for u in range(3)]
    assert expected == exact == [F(3, 2), F(1), F(3, 2)]
    undefined = [sum(c[u] is None for _, c in values) for u in range(3)]
    assert undefined == [1, 1, 1]
    zero_fallback_expected = [sum(c[u] or F(0) for _, c in values) / len(values)
                              for u in range(3)]
    assert all(zero_fallback_expected[u] != 1 / exact[u] for u in range(3))
    once = estimates(distances, (0, 1, 2))
    repeated = estimates(distances, (0, 0, 0))
    assert once[0] == exact and repeated[0] != exact
    assert repeated[1][0] is None
    scaled = [[7*x for x in row] for row in distances]
    for s in samples:
        means, reciprocal = estimates(distances, s)
        changed_means, changed_reciprocal = estimates(scaled, s)
        assert changed_means == [7*x for x in means]
        assert changed_reciprocal == [None if x is None else x/7 for x in reciprocal]
    epsilon = F(1, 4)
    failure = F(1, 20)
    n = 3
    required = math.ceil(n*n / (2*(n-1)**2 * float(epsilon)**2)
                         * math.log(2*n/float(failure)))
    bound = 2*n*math.exp(-2*required*float(epsilon)**2*(n-1)**2/n**2)
    assert required == 87 and bound <= float(failure)
    xi = F(1, 2)  # epsilon * diameter = 1/4 * 2
    tail_count = sum(any(abs(m[u]-exact[u]) >= xi for u in range(3))
                     for m, _ in values)
    finite_tail = F(tail_count, len(values))
    loose_bound = 2*n*math.exp(-2*2*float(epsilon)**2*(n-1)**2/n**2)
    assert float(finite_tail) <= loose_bound
    eta = F(1, 5)
    ratios = [F(1)/(1-eta), F(1)/(1+eta)]
    assert ratios == [F(5, 4), F(5, 6)]
    # Weighted stars with one length-1 edge and other edges length 1/n^2.
    # Diameter < 2 stays bounded, while center mean/diameter can approach zero.
    stars = []
    for size in (11, 101, 1001):
        short = F(1, size*size)
        mean = (1+(size-2)*short)/(size-1)
        diameter = 1+short
        stars.append(dict(n=size, center_mean=mean, diameter=diameter,
                          mean_diameter_ratio=mean/diameter))
    assert all(x['diameter'] < 2 for x in stars)
    assert stars[2]['mean_diameter_ratio'] < F(1, 900)
    return dict(path3_exact_means=exact, all_nine_iid_pairs_expected_mean=expected,
                undefined_reciprocal_probability=[F(x, len(samples)) for x in undefined],
                exact_centrality=[1/x for x in exact],
                hypothetical_zero_fallback_expected_centrality=zero_fallback_expected,
                hypothetical_fallback_note='Not specified by the paper and not adopted in the record.',
                each_vertex_once=once, repeated_three_sources=repeated,
                weight_scaling='All nine pairs: times-7 distances give times-7 means and divided-by-7 defined reciprocals.',
                sample_count_example=dict(n=n, epsilon=epsilon, failure=failure,
                                          sufficient_k=required, union_bound=bound),
                k2_all_vertex_tail_probability=finite_tail,
                relative_error_endpoint_ratios=ratios, bounded_diameter_weighted_stars=stars,
                scope='Finite exact arithmetic and explicit algebra; not benchmark replication, author code, an empirically measured guarantee or proof by enumeration for arbitrary graphs.')


if __name__ == '__main__':
    print(json.dumps(main(), indent=2, default=str))
