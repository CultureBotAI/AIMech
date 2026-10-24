"""Original bounded PESMO source/approximation checks; not a PESMO implementation.

Only Python's standard library is used. No author code is imported or executed.
Finite probabilities and Gaussian matrix arithmetic use Fraction; entropy and
Gaussian cdf evaluations use binary64 with explicit absolute-only tolerances.
The dominance convention is weak improvement in every minimization objective
and strict improvement in at least one. Corrected predicates below are audit
references, not a claim that the paper or its implementation was repaired.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, product
import json
import math


def close(a, b, tol=2e-14):
    assert math.isclose(a, b, rel_tol=0.0, abs_tol=tol), (a, b)


def dominates(challenger, target):
    return all(a <= b for a, b in zip(challenger, target)) and any(
        a < b for a, b in zip(challenger, target)
    )


def pareto(values):
    return tuple(i for i, v in enumerate(values)
                 if not any(dominates(w, v) for w in values))


def printed_factor(challenger, target):
    # Main Eq4/Eq6, supplement Eq8, with Theta(0)=1.
    return int(not all(a >= b for a, b in zip(challenger, target)))


def entropy(probabilities):
    return -sum(float(p) * math.log2(float(p)) for p in probabilities if p)


def distribution(states, select):
    out = defaultdict(F)
    for state, probability in states:
        out[select(state)] += probability
    return dict(out)


def information(states, left, right):
    pl = distribution(states, left)
    pr = distribution(states, right)
    joint = distribution(states, lambda x: (left(x), right(x)))
    return entropy(pl.values()) + entropy(pr.values()) - entropy(joint.values())


def inverse(matrix):
    n = len(matrix)
    work = [[F(x) for x in row] + [F(i == j) for j in range(n)]
            for i, row in enumerate(matrix)]
    for i in range(n):
        pivot = next(j for j in range(i, n) if work[j][i])
        work[i], work[pivot] = work[pivot], work[i]
        divisor = work[i][i]
        work[i] = [x / divisor for x in work[i]]
        for j in range(n):
            if i != j:
                scale = work[j][i]
                work[j] = [x - scale * y for x, y in zip(work[j], work[i])]
    return [row[n:] for row in work]


def rational(matrix):
    return [[str(x) for x in row] for row in matrix]


def main():
    outputs = {}
    vectors = tuple(product((-1, 0, 1), repeat=2))
    mismatch = sum(printed_factor(a, b) != int(not dominates(a, b))
                   for a in vectors for b in vectors)
    witnesses = []
    for challenger, target in [((1, 1), (0, 0)), ((-1, -1), (0, 0)),
                               ((0, 0), (0, 0)), ((-1, 1), (0, 0)),
                               ((0, 1), (0, 0))]:
        witnesses.append(dict(challenger=challenger, target=target,
                              nondominated_against_challenger=not dominates(challenger, target),
                              printed_factor=printed_factor(challenger, target)))
    assert [w['printed_factor'] for w in witnesses] == [0, 1, 0, 1, 0]
    assert pareto(((0, 0), (0, 0))) == (0, 1)
    assert printed_factor((0, 0), (0, 0)) == 0
    # Every nonempty strict-dominance Pareto set in a finite nonempty domain exists.
    tables = 0
    accepted_subsets = 0
    incomplete_accepted_subsets = 0
    full_set_size_counts = Counter()
    for values in product(vectors, repeat=3):
        target = pareto(values)
        assert target
        tables += 1
        full_set_size_counts[len(target)] += 1
        for size in range(1, 4):
            for subset in combinations(range(3), size):
                membership_only = all(not dominates(v, values[i])
                                      for i in subset for v in values)
                assert membership_only == set(subset).issubset(target)
                if membership_only:
                    accepted_subsets += 1
                    incomplete_accepted_subsets += subset != target
    assert tables == 729
    # A corrected membership product still accepts a proper subset of a tradeoff set.
    values = ((0, 1), (1, 0))
    assert pareto(values) == (0, 1)
    assert all(not dominates(v, values[0]) for v in values)
    outputs['dominance_and_set_membership'] = dict(
        pair_cases=len(vectors)**2, printed_mismatches=mismatch,
        witnesses=witnesses, finite_three_point_tables=tables,
        full_pareto_set_size_counts=dict(sorted(full_set_size_counts.items())),
        nonempty_membership_accepted_subsets=accepted_subsets,
        incomplete_accepted_subsets=incomplete_accepted_subsets,
        subset_witness=dict(values=values, full_set=[0, 1], accepted_subset=[0]),
        limit='Membership-only predicates are not a normalized law or equality characterization of a complete Pareto set; self/tie policies matter.')

    states = [(b, F(1, 4)) for b in product((-1, 1), repeat=2)]
    target = lambda b: pareto(((0, 0), b))
    joint_mi = information(states, target, lambda b: b)
    individual_mi = [information(states, target, lambda b, k=k: b[k]) for k in (0, 1)]
    close(joint_mi, 1.5)
    close(sum(individual_mi), 1.0)
    conditional = [(b, F(1, 2)) for b, p in states if target(b) == (0, 1)]
    mean = [sum(p*b[k] for b, p in conditional) for k in (0, 1)]
    covariance = sum(p*b[0]*b[1] for b, p in conditional) - mean[0]*mean[1]
    assert covariance == -1
    target_dist = distribution(states, target)
    outputs['pareto_information_nonadditivity'] = dict(
        states=[dict(objective_values_at_B=b, probability=str(p),
                     pareto_set=target(b)) for b, p in states],
        objective_values_at_A=[0, 0], independent_objectives=True,
        target_probabilities={str(k): str(v) for k, v in target_dist.items()},
        joint_information_bits=joint_mi, individual_information_bits=individual_mi,
        gap_bits=joint_mi-sum(individual_mi),
        covariance_given_both_points_nondominated=str(covariance),
        scope='Finite noiseless four-state diagnostic, not a fitted GP or accuracy benchmark.')

    # A continuous independent-Gaussian diagnostic for cross-objective coupling.
    # X,Y ~ iid N(0,1); condition on NOT(X<0 and Y<0), the event that B=(X,Y)
    # does not dominate A=(0,0). Integrate using quadrant symmetry and standard
    # normal half-line first/second moments: P=3/4, E[X]=sqrt(2/pi)/3.
    mu = math.sqrt(2/math.pi)/3
    var = 1-2/(9*math.pi)
    cov = -8/(9*math.pi)
    assert cov < 0 and var > abs(cov)
    Phi = lambda z: (1+math.erf(z/math.sqrt(2)))/2
    printed_Z = 1-Phi(1/math.sqrt(2))**2
    minimization_Z = 1-Phi(-1/math.sqrt(2))**2
    assert printed_Z < minimization_Z
    outputs['gaussian_conditioning'] = dict(
        event='Independent standard Gaussian B coordinates do not both lie below fixed A=(0,0).',
        probability='3/4', mean_each=mu, variance_each=var,
        cross_objective_covariance=cov, covariance_formula='-8/(9*pi)',
        printed_reversed_event_mean_each=-mu,
        factorized_projection_cross_covariance=0,
        nonzero_mean_normalizer=dict(difference_mean_each=1,
            difference_variance_each=2, printed_supplement_Eq10=printed_Z,
            minimization_sign_context=minimization_Z),
        scope='Analytic one-factor moments with binary64 pi/erf; not a complete EP run.')

    # Gaussian normalization requires precision, not covariance, as natural parameter.
    prior = [[F(1), F(0)], [F(0), F(4)]]
    printed_precision = [[F(1), F(0)], [F(0), F(4)]]
    printed_var = inverse(printed_precision)[1][1]
    assert printed_var == F(1, 4) and prior[1][1] == 4
    # Marginalizing the middle variable is not taking a principal precision block.
    full_cov = [[F(2), F(1), F(0)], [F(1), F(2), F(1)], [F(0), F(1), F(2)]]
    full_precision = inverse(full_cov)
    principal = [[full_precision[i][j] for j in (0, 2)] for i in (0, 2)]
    marginal_cov = [[full_cov[i][j] for j in (0, 2)] for i in (0, 2)]
    marginal_precision = inverse(marginal_cov)
    assert principal != marginal_precision
    # Eq2 prints one c*u*v inside -1/2, while Eq4 puts c in both symmetric entries.
    u = v = F(1)
    c = F(2)
    literal_exponent = -F(1, 2)*(4*u*u+4*v*v+c*u*v)
    reconstructed_exponent = -F(1, 2)*(4*u*u+4*v*v+2*c*u*v)
    assert (literal_exponent, reconstructed_exponent) == (-5, -6)
    outputs['printed_gaussian_parameter_checks'] = dict(
        zero_site_candidate_variance=str(prior[1][1]),
        printed_Eq7_candidate_variance=str(printed_var),
        full_covariance=rational(full_cov), full_precision=rational(full_precision),
        principal_precision_block=rational(principal),
        correct_marginal_precision=rational(marginal_precision),
        source_Eq2_cross_exponent=str(literal_exponent),
        source_Eq4_reconstruction_exponent=str(reconstructed_exponent),
        source_Eq4_index_example=dict(M=1,N=2,printed_j_range=[2],required_j_range=[2,3]),
        scope='Counterexamples to literal supplement formulas, not a full implementation or proposed erratum.')

    prior_variances = (4, 9)
    noise = (1, 4)
    conditional_variances = ((1, 4), (2, 3))
    scores = [0.5*(math.log(prior_variances[k]+noise[k])-
              sum(math.log(v[k]+noise[k]) for v in conditional_variances)/2)
              for k in (0, 1)]
    joint_gaussian = 0.5*math.log(math.prod(prior_variances[k]+noise[k] for k in (0,1))) - sum(
        0.5*math.log(math.prod(v[k]+noise[k] for k in (0,1)))
        for v in conditional_variances)/2
    close(sum(scores), joint_gaussian)
    scores_noise = [0.5*math.log((4+n)/(1+n)) for n in (0,1,10,100)]
    assert all(a>b for a,b in zip(scores_noise,scores_noise[1:]))
    # Conditioning reduces entropy in expectation, not at every target realization.
    p = [F(9,10),F(1,20),F(1,20)]
    prior_H = entropy(p)
    rare_H = 1.0
    assert rare_H > prior_H
    expected_reduction = prior_H-F(1,10)*rare_H
    clipped_reduction = F(9,10)*prior_H
    assert clipped_reduction > expected_reduction
    outputs['entropy_approximation_boundaries'] = dict(
        latent_prior_variances=prior_variances, observation_noise_variances=noise,
        two_latent_conditional_samples=conditional_variances,
        factorized_gaussian_component_scores_nats=scores,
        aggregate_score_nats=joint_gaussian,
        noise_variances=[0,1,10,100], single_component_scores_nats=scores_noise,
        per_realization_clipping_witness=dict(probabilities=[str(x) for x in p],
            target='whether observation is nonzero',
            prior_entropy_bits=prior_H, rare_event_entropy_bits=rare_H,
            exact_expected_reduction_bits=expected_reduction,
            clipped_per_realization_reduction_bits=clipped_reduction),
        scope='Variance formula identity is within a stipulated factorized Gaussian approximation; clipping witness is a separate finite channel.')
    print(json.dumps(dict(scope='Five bounded source and approximation diagnostics; no external code execution.',
                          arithmetic='Fraction for exact finite/matrix checks; binary64 logs/erf with rel_tol=0 and abs_tol=2e-14.',
                          checks=outputs), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
