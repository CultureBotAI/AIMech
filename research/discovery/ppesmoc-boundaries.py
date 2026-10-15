"""Original bounded PPESMOC boundary arithmetic; not an implementation of PPESMOC.

Derivation: Gaussian entropy, finite mutual information, and explicit inspection of
the 2023 author manuscript and official supplement. Fraction handles rational
probabilities and determinants exactly. Logarithms/erf use binary64 with explicit
rel_tol=0, abs_tol=2e-14 comparisons. No third-party code or data is imported.
This supports an author workflow; it is not independent scientific approval.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import json
import math


def close(x, y):
    assert math.isclose(x, y, rel_tol=0, abs_tol=2e-14), (x, y)


def det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def swap(a):
    return [[a[1][1], a[1][0]], [a[0][1], a[0][0]]]


def entropy(rows, positions):
    d = defaultdict(F)
    for p, values in rows:
        d[tuple(values[i] for i in positions)] += p
    assert sum(d.values()) == 1
    return -sum(float(p) * math.log2(float(p)) for p in d.values() if p)


def mi(rows, a, b):
    return entropy(rows, a) + entropy(rows, b) - entropy(rows, a + b)


def dominates(a, b):
    return all(x <= y for x, y in zip(a, b)) and any(x < y for x, y in zip(a, b))


def pareto(values, feasible):
    return tuple(i for i, x in enumerate(values) if feasible[i] and not any(
        feasible[j] and dominates(y, x) for j, y in enumerate(values)))


def calculate():
    total = different = 0
    for a, b, r, v, noise in product([F(1), F(2), F(3)], [F(1), F(2), F(3)],
                                    [F(-1, 2), F(0), F(1, 2)],
                                    [(1, 1), (1, -1), (1, 0)], [F(0), F(1, 4), F(1)]):
        conditional = [[a + noise, r], [r, b + noise]]
        ordinary = [[conditional[i][j] + v[i] * v[j] for j in range(2)] for i in range(2)]
        dc, du = det(conditional), det(ordinary)
        assert dc > 0 and du >= dc
        assert det(swap(ordinary)) == du and det(swap(conditional)) == dc
        joint = .5 * math.log(float(du / dc))
        marginal = .5 * sum(math.log(float(ordinary[i][i] / conditional[i][i])) for i in range(2))
        different += not math.isclose(joint, marginal, rel_tol=0, abs_tol=2e-14)
        total += 1
    joint = .5 * math.log(3)
    marginal = math.log(2)
    assert joint < marginal
    singular = [[F(1), F(1)], [F(1), F(1)]]
    assert det(singular) == 0
    ordinary_noisy = [[F(5, 4), F(1)], [F(1), F(5, 4)]]
    conditional_noisy = [[F(3, 4), F(1, 2)], [F(1, 2), F(3, 4)]]
    assert det(ordinary_noisy) == F(9, 16) and det(conditional_noisy) == F(5, 16)
    one_dimensional = []
    for old, new, noise in product([F(1), F(2), F(3)], [F(1, 4), F(1, 2)], [F(0), F(1)]):
        score = .5 * math.log(float((old + noise) / (new + noise)))
        close(score, .5 * (math.log(float(old + noise)) - math.log(float(new + noise))))
        one_dimensional.append(score)

    # Four finite states encode feasible Pareto sets using three mutually
    # nondominated objective vectors, fixed a feasible, and b/c feasibility U/V.
    # Query channels U,U,V illustrate acquisition dependence, not fitted GPs.
    finite = []
    for u, v in product([0, 1], repeat=2):
        target = pareto([(0, 2), (1, 1), (2, 0)], [True, bool(u), bool(v)])
        finite.append((F(1, 4), (target, u, u, v)))
    singles = [mi(finite, [0], [i]) for i in [1, 2, 3]]
    repeated, complementary = mi(finite, [0], [1, 2]), mi(finite, [0], [1, 3])
    assert singles == [1., 1., 1.] and repeated == 1 and complementary == 2
    close(mi(finite, [0], [3, 1]), complementary)

    # Two independently noisy measurements of one binary target (an abstract
    # two-valued feasible Pareto identity) can add information at the same point.
    noisy = []
    for z, n1, n2 in product([0, 1], repeat=3):
        pn = lambda n: F(1, 4) if n else F(3, 4)
        noisy.append((F(1, 2) * pn(n1) * pn(n2), (z, z ^ n1, z ^ n2)))
    first, both = mi(noisy, [0], [1]), mi(noisy, [0], [1, 2])
    assert both > first > 0
    close(both, 1 + entropy(noisy, [1, 2]) - entropy(noisy, [0, 1, 2]))

    # Conditioning can couple previously independent task outputs. Feasible
    # Pareto membership is itself enough: a fixed a=(0,0) versus b=(u,v),
    # independent u,v in {-1,1}, both points feasible.
    tasks = []
    for u, v in product([-1, 1], repeat=2):
        target = pareto([(0, 0), (u, v)], [True, True])
        tasks.append((F(1, 4), (target, u, v)))
    task_joint = mi(tasks, [0], [1, 2])
    task_sum = mi(tasks, [0], [1]) + mi(tasks, [0], [2])
    assert task_joint == 1.5 and task_sum == 1

    # Literal pair factor from main Eq14, using Theta(0)=1.
    theta = lambda x: int(x >= 0)
    omega = lambda competitor, star, feasible: 1 - int(feasible) * math.prod(
        theta(s - c) for s, c in zip(star, competitor))
    pairs = ties = 0
    for competitor, star, feasible in product(list(product([-1, 0, 1], repeat=2)),
                                             list(product([-1, 0, 1], repeat=2)), [False, True]):
        value = omega(competitor, star, feasible)
        intended = int(not feasible or not dominates(competitor, star))
        mismatch = value != intended
        assert mismatch == (feasible and competitor == star)
        ties += mismatch
        pairs += 1
    assert omega((0, 0), (0, 0), True) == 0
    assert omega((1, 0), (0, 1), True) == 1
    assert not dominates((0, 1), (1, 0))
    # Excluding self and handling ties still gives membership, not completeness:
    assert pareto([(0, 1), (1, 0)], [True, True]) == (0, 1)
    assert omega((1, 0), (0, 1), True) == 1  # singleton candidate passes membership
    # A proper conditional distribution must divide by its event probability.
    unnormalized_event_mass = F(1, 2)
    assert unnormalized_event_mass != 1

    # Source supplement arithmetic diagnostics, not a full corrected EP engine.
    phi = lambda x: math.exp(-x*x/2) / math.sqrt(2*math.pi)
    Phi = lambda x: .5 * (1 + math.erf(x/math.sqrt(2)))
    ratio = phi(0) / Phi(0)
    curvature = -ratio * (0 + ratio)
    printed_curvature = -ratio * 0 * ratio
    close(curvature, -2/math.pi)
    assert printed_curvature == 0
    # In the supplement's declared [observation,star] order, the minimizing
    # rejection probability requires star-observation, not observation-star.
    correct_z = 1 - Phi(-1) * F(1, 2)
    printed_z = 1 - Phi(1) * F(1, 2)
    assert correct_z > printed_z
    hessian = [[F(-1, 8), F(1, 8)], [F(1, 8), F(-1, 8)]]
    assert det(hessian) == 0
    regular = [[int(i == j) + hessian[i][j] for j in range(2)] for i in range(2)]
    assert det(regular) == F(3, 4)
    log_error = .5 * (6 - math.log(6))
    negative_approx = .5 * math.log(F(1, 2))
    assert negative_approx < 0  # arbitrary EP covariance expansion is not exact MI

    return {
        'scope': 'Original finite channels, Gaussian covariance arithmetic and source-formula diagnostics only; no GP fitting, EP implementation, author code, optimization, benchmarks or independent approval.',
        'arithmetic': {'rational_operations': 'fractions.Fraction exact', 'transcendentals': 'binary64 log/log2/erf', 'comparison_rel_tol': 0, 'comparison_abs_tol': 2e-14},
        'batch_logdet': {'positive_definite_cases': total, 'different_from_marginal_sum_cases': different, 'batch_permutation_checks': total, 'scalar_reduction_cases': len(one_dimensional), 'example_ordinary': [[2,1],[1,2]], 'example_conditional': [[1,0],[0,1]], 'joint_nats': joint, 'marginal_sum_nats': marginal, 'printed_eq16_scale_nats': 2*joint, 'noise_both_sides_nats': .5*math.log(2), 'latent_duplicate_determinant': '0', 'noisy_duplicate_determinants': ['9/16','5/16'], 'noisy_duplicate_score_nats': .5*math.log(9/5), 'eq11_missing_log_error_nats_for_constraint_det6': log_error},
        'joint_batch_channel': {'states': len(finite), 'feasible_pareto_outcomes': 4, 'single_query_bits': singles, 'repeated_information_pair_bits': repeated, 'complementary_pair_bits': complementary, 'independent_single_score_sum_bits': 2., 'interpretation': 'Same singleton scores need not imply equal joint batch information; not an implementation or universal GP ranking theorem.'},
        'noisy_repetition': {'states': len(noisy), 'noise_flip_probability': '1/4', 'one_observation_bits': first, 'two_observations_bits': both, 'positive_increment_bits': both-first, 'interpretation': 'No universal claim that repeat evaluations contain no information.'},
        'task_factorization_boundary': {'states': len(tasks), 'joint_information_bits': task_joint, 'sum_individual_information_bits': task_sum, 'interpretation': 'Independent preconditioning outputs need not remain independent after Pareto conditioning.'},
        'pareto_product_boundaries': {'pair_cases': pairs, 'feasible_tie_mismatches': ties, 'self_factor': 0, 'nondominating_tradeoff_factor': 1, 'membership_does_not_enforce_completeness': True, 'empty_product': 1, 'unnormalized_conditional_event_mass': str(unnormalized_event_mass)},
        'supplement_diagnostics': {'phi_curvature_at_zero': curvature, 'printed_eq7_at_zero': printed_curvature, 'correct_minimizing_omega_normalizer': correct_z, 'printed_order_normalizer': printed_z, 'rank1_hessian_determinant': str(det(hessian)), 'identity_plus_hessian_determinant': str(det(regular)), 'interpretation': 'Source issues retained; these diagnostics are not a complete corrected implementation.'},
        'approximation_limit': {'arbitrary_covariance_expansion_score_nats': negative_approx, 'interpretation': 'Exact MI is nonnegative; Monte Carlo, finite representations and EP surrogates are not certified by Gaussian entropy algebra.'}
    }


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2, sort_keys=True))
