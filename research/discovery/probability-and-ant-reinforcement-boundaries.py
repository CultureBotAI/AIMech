"""Finite curator examples of method boundaries; not full algorithms or benchmarks."""
import json
from math import isclose


def calculate():
    alpha, gamma, old = .2, .9, 1.
    next_values = {'a': 2., 'b': 5.}
    local = lambda eligible: (1-alpha)*old + alpha*gamma*max(next_values[z] for z in eligible)
    aq_a, aq_ab = local(['a']), local(['a', 'b'])
    acs_constant = (1-alpha)*old + alpha*.1
    delayed = (1-alpha)*old + alpha*(100/10)
    assert isclose(aq_a, 1.16) and isclose(aq_ab, 1.7)
    assert aq_a != aq_ab and aq_a != acs_constant
    assert isclose(delayed, 2.8)

    p, lr, current, archived = [.5, .5], .2, [1, 0], [0, 1]
    attraction = [(1-lr)*v+lr*x for v,x in zip(p,current)]
    mistaken_archive = [(1-lr)*v+lr*x for v,x in zip(p,archived)]
    mutated = [.9*attraction[0]+.1*0, attraction[1]]
    concentrating = .9*attraction[0]+.1*1
    assert all(isclose(a,b) for a,b in zip(attraction,[.6,.4]))
    assert isclose(mutated[0],.54) and concentrating > attraction[0]
    assert attraction != mistaken_archive
    # Both empirical populations have marginals (.5,.5), but disjoint support.
    pop_a, pop_b = [(0,0),(1,1)], [(0,1),(1,0)]
    marginals = lambda pop: [sum(x[i] for x in pop)/len(pop) for i in range(2)]
    assert marginals(pop_a) == marginals(pop_b) == p
    independent_off_support_mass = .5 # The product model assigns .25 to each vector.
    single_elite_smoothed_ce = [(1-lr)*v+lr*x for v,x in zip(p,current)]
    assert single_elite_smoothed_ce == attraction

    lengths, best, sigma, q, rho, trail = [10.,20.,30.], 8., 3, 1., .5, 1.
    # A shared edge is used by every current tour and by the archived best.
    rank_terms = [(sigma-mu)*q/lengths[mu-1] for mu in range(1,sigma)]
    archive_term = sigma*q/best
    rank_deposit = sum(rank_terms)+archive_term
    all_ant = sum(q/c for c in lengths)
    elitist_deposit = all_ant+archive_term
    rank_after_shift = sum((sigma-mu)*q/(lengths[mu-1]+10) for mu in range(1,sigma))+sigma*q/(best+10)
    assert isclose(rank_deposit,.625)
    assert isclose(elitist_deposit,67/120)
    assert rank_deposit != rank_after_shift
    assert elitist_deposit != rank_deposit
    zero_elite = all_ant + 0*q/best
    assert zero_elite == all_ant
    # If the current rank-1 tour is also the archive (best=10), both terms remain.
    same_tour_contribution = (sigma-1)*q/lengths[0] + sigma*q/lengths[0]
    assert isclose(same_tour_contribution,.5)
    return {
        'ant_q': {'same_city_different_eligible_sets': [aq_a,aq_ab], 'acs_constant_target': acs_constant, '1995_zero_next_value_delayed_update': delayed, 'qualification': 'Per-edge arithmetic only; does not resolve source-specific update domains, terminal cases or schedules.'},
        'pbil': {'current_winner_attraction': attraction, 'archive_substitution_changes_result': mistaken_archive, 'probability_mutation_toward_zero': mutated, 'mutation_toward_one_concentrates': concentrating, 'shared_marginals': p, 'product_mass_outside_either_empirical_support': independent_off_support_mass, 'single_elite_smoothed_bernoulli_ce_step_coincides': True},
        'ant_variants': {'rank_current_terms': rank_terms, 'separate_archive_term': archive_term, 'rank_deposit': rank_deposit, 'rank_updated_trail': rho*trail+rank_deposit, 'all_ant_deposit': all_ant, 'elitist_deposit': elitist_deposit, 'elitist_updated_trail': rho*trail+elitist_deposit, 'zero_elite_recovers_base': True, 'rank_deposit_after_order_preserving_cost_shift': rank_after_shift, 'same_current_and_archived_tour_additive_contribution': same_tour_contribution},
        'limits': 'Exact illustrative states and ordinary floating-point arithmetic; no author code, stochastic search run, empirical result or convergence proof.'}


if __name__ == '__main__':
    print(json.dumps(calculate(),indent=2))
