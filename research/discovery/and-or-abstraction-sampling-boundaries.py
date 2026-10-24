"""Exact finite examples, not the authors' implementation or benchmark replication."""
from fractions import Fraction as F
from itertools import product
import json


def moments(outcomes):
    assert sum(p for p, _ in outcomes) == 1
    mean = sum(p * v for p, v in outcomes)
    variance = sum(p * (v - mean) ** 2 for p, v in outcomes)
    return mean, variance


def enumerated_probe(root_cost, left_cost, right_cost, right_bound):
    """A retained root frontier, one left representative, pruning, then one right.

    The pseudo-tree has A with independent children B,C. Factors are a(A),
    b(A,B), c(A,C). A's assignments are initially separate abstract states.
    B's four assignments share one state, crossing A contexts. After its
    selection only that A survives, and C is sampled under that A. Heuristics
    at terminal B,C are 1; C's unexpanded OR estimate is right_bound[A].
    All probabilities, inherited weights and relative backup are explicit.
    """
    masses = {(a, b): F(root_cost[a] * left_cost[a][b] * right_bound[a])
              for a, b in product(range(2), repeat=2)}
    total = sum(masses.values())
    outcomes = []
    for (a, b), mass in masses.items():
        p_b = mass / total
        w_a, w_b = F(1), 1 / p_b
        v_b = F(left_cost[a][b]) * w_b / w_a
        # r_C is the backed-up B value. g_C includes root and C costs.
        c_masses = [w_a * root_cost[a] * cost * v_b for cost in right_cost[a]]
        for c in range(2):
            p_c = c_masses[c] / sum(c_masses)
            w_c = w_a / p_c
            v_a = v_b * right_cost[a][c] * w_c / w_a
            estimate = root_cost[a] * w_a * v_a
            outcomes.append((p_b * p_c, estimate))
    return outcomes


def two_left_strata(root_cost, left_cost, right_cost, right_bound):
    """Keep one B representative per B value; C can still cross two A contexts."""
    outcomes = []
    for a_for_b0, a_for_b1 in product(range(2), repeat=2):
        branch_probability = F(1)
        left_estimates = [F(0), F(0)]
        for b, a in enumerate([a_for_b0, a_for_b1]):
            masses = [F(root_cost[x] * left_cost[x][b] * right_bound[x]) for x in range(2)]
            p_b = masses[a] / sum(masses)
            branch_probability *= p_b
            left_estimates[a] += F(left_cost[a][b]) / p_b
        survivors = [a for a in range(2) if left_estimates[a] > 0]
        masses = {(a, c): root_cost[a] * right_cost[a][c] * left_estimates[a]
                  for a in survivors for c in range(2)}
        for (a, c), mass in masses.items():
            p_c = mass / sum(masses.values())
            # C's retained representative now removes all other A contexts.
            estimate = root_cost[a] * left_estimates[a] * right_cost[a][c] / p_c
            outcomes.append((branch_probability * p_c, estimate))
    return outcomes


def main():
    ac = [1, 3]
    bc = [[2, 5], [7, 11]]
    cc = [[13, 17], [19, 23]]
    truth = sum(ac[a] * bc[a][b] * cc[a][c]
                for a, b, c in product(range(2), repeat=3))
    approximate = moments(enumerated_probe(ac, bc, cc, [50, 50]))
    oracle = moments(enumerated_probe(ac, bc, cc, list(map(sum, cc))))
    assert truth == 2478 and approximate[0] == oracle[0] == truth
    assert oracle[1] == 0 and approximate[1] > 0
    two_strata_approx = moments(two_left_strata(ac, bc, cc, [50, 50]))
    two_strata_oracle = moments(two_left_strata(ac, bc, cc, list(map(sum, cc))))
    assert two_strata_approx[0] == two_strata_oracle[0] == truth
    assert two_strata_oracle[1] == 0

    # If A itself was sampled with p=1/2, children inherit its weight 2.
    # Independent binary B,C draws with p=1/2 then have cumulative weight4.
    # Each backup must use child/parent, applying shared ancestral weight once.
    w_a, w_b, w_c = F(2), F(4), F(4)
    relative = w_a * (w_b / w_a) * (w_c / w_a)
    absolute = w_a * w_b * w_c
    assert relative == 8 and absolute == 32

    # A naive simultaneous unrestricted selection can leave no full solution.
    # This particular construction remains unbiased despite invalid probes;
    # structural invalidity by itself is not proof of bias in every variant.
    naive = []
    invalid = F(0)
    for a_b, b, a_c, c in product(range(2), repeat=4):
        prob = F(1, 16)
        if a_b != a_c:
            invalid += prob
        naive.append((prob, F(16 if a_b == a_c else 0)))
    naive_moments = moments(naive)
    pruned = moments(enumerated_probe([1, 1], [[1, 1]] * 2, [[1, 1]] * 2, [2, 2]))
    assert invalid == F(1, 2) and naive_moments == (8, 64) and pruned == (8, 0)

    # Four binary independent children can be represented by 1 parent+8 AND
    # leaves while encoding 16 configurations; OR/dummy nodes are excluded.
    compact = dict(real_and_nodes=1 + 2 * 4, configurations=2 ** 4)
    # A single-variable domain still requires generating all d candidates
    # before one representative is retained by the stated expansion rule.
    generated = [dict(domain=d, generated=d, retained=1) for d in [2, 10, 100]]

    # Literal 2018 supplement weight interpretation, deliberately separate:
    # two binary variables in a chain, cumulative weights2 then4, OR weight1.
    # Its printed internal w(s)/w(parent(s)) times leaf w(s)c(s) gives8 vs4.
    literal_2018 = dict(true_partition=4, printed_or_parent_interpretation=2 * 4,
                        alternative_local_weight_product=2 * 2)
    # The printed winning-v term substitutes old weight u for selected v.
    u, v, z_u, z_v, p = F(1), F(3), F(1), F(5), F(1, 2)
    intended = (1 - p) * u / (1 - p) * z_u + p * v / p * z_v
    printed = (1 - p) * u / (1 - p) * z_u + p * u / p * z_v
    assert intended == 16 and printed == 6

    result = dict(
        factorized_model_truth=truth,
        approximate_sibling_bound_mean_variance=list(map(str, approximate)),
        exact_sibling_bound_mean_variance=list(map(str, oracle)),
        two_left_strata_approximate_mean_variance=list(map(str, two_strata_approx)),
        two_left_strata_exact_mean_variance=list(map(str, two_strata_oracle)),
        relative_weight_estimate=str(relative), wrong_absolute_weight_estimate=str(absolute),
        naive_invalid_probe_probability=str(invalid),
        naive_mean_variance=list(map(str, naive_moments)),
        sequential_pruning_mean_variance=list(map(str, pruned)),
        compact_probe=compact, generated_vs_retained=generated,
        unsupported_root_context=dict(retained_contribution=210, omitted_contribution=2268, target=2478),
        separate_2018_notation_check=literal_2018,
        separate_2018_winning_v_expected_contribution=dict(correct=str(intended), printed=str(printed)),
        scope='Finite rational examples of the 2020 mechanism and separately labeled 2018 notation. No general proof, literal pseudocode certification, author-code execution or benchmark replication.')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
