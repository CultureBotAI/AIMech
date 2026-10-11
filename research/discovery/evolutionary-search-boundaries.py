"""Original arithmetic examples for source interpretation, not author code."""
import json


def calculate():
    # Different tie conventions in DE prose and displayed pseudocode.
    old_cost = trial_cost = 3
    assert not (trial_cost < old_cost) and trial_cost <= old_cost
    # Mutation is not confined to the initial range.
    mutant = 0.9 + 0.5 * (1.0 - 0.0)
    assert mutant > 1.0
    # Distinct indices need not denote distinct coordinate values.
    collapsed = 0.7 + 0.5 * (0.7 - 0.7)
    assert collapsed == 0.7
    # A 2001 CMA rank-one blend, C=I and p=(2,0), c_cov=1/4.
    old_covariance, path, rate = [[1.0, 0.0], [0.0, 1.0]], [2.0, 0.0], 0.25
    covariance = [[(1-rate)*old_covariance[i][j]+rate*path[i]*path[j]
                   for j in range(2)] for i in range(2)]
    assert covariance == [[1.75, 0.0], [0.0, 0.75]]
    assert covariance[0][0] * covariance[1][1] > 0
    sigma = 2.0
    sampling_covariance = [[sigma**2 * x for x in row] for row in covariance]
    assert sampling_covariance == [[7.0, 0.0], [0.0, 3.0]]
    # For N(mu,sigma^2) at mu=0,sigma=1,z=1, the score is (1,0).
    # Its single-sample Fisher is singular, while exact Fisher is diag(1,2).
    z, mu, scale = 1.0, 0.0, 1.0
    score = [(z-mu)/scale**2, ((z-mu)**2-scale**2)/scale**3]
    empirical_fisher = [[a*b for b in score] for a in score]
    assert empirical_fisher == [[1.0, 0.0], [0.0, 0.0]]
    assert empirical_fisher[0][0]*empirical_fisher[1][1] == 0
    # A monotone fitness transform preserves ranks but changes raw score weighting.
    scores = [-1.0, 1.0]
    raw = sum(s*f for s,f in zip(scores,[1.0,2.0]))/2
    transformed = sum(s*f for s,f in zip(scores,[1.0,8.0]))/2
    rank_weighted = sum(s*u for s,u in zip(scores,[-0.5,0.5]))
    assert raw == 0.5 and transformed == 3.5 and rank_weighted == 1
    return {
        'de_equal_cost': {'prose_strict_accepts': trial_cost < old_cost, 'figure3_nonstrict_accepts': trial_cost <= old_cost},
        'de_initial_range_escape': mutant,
        'de_collapsed_population_mutant': collapsed,
        'cma_rank_one_covariance': covariance,
        'cma_sampling_covariance_with_sigma2': sampling_covariance,
        'nes_gaussian_score': score,
        'nes_single_sample_fisher': empirical_fisher,
        'nes_exact_fisher_at_mu0_sigma1': [[1.0,0.0],[0.0,2.0]],
        'fitness_weighting': {'raw':raw, 'cubed_fitness':transformed, 'same_rank_utility':rank_weighted},
        'scope':'Finite arithmetic only; no optimizer, author implementation, training or benchmark was executed.'
    }


if __name__ == '__main__':
    print(json.dumps(calculate(),indent=2))
