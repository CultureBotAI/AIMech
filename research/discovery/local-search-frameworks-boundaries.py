"""Finite curator examples of search conventions; not optimizer benchmarks."""
import json

def calculate():
    neighbors = {'A':['B','C'], 'B':['A','C'], 'C':['A','B']}
    costs = {'A':0, 'B':1, 'C':2}
    current, tabu_reverse = 'A', None
    path = [current]
    for _ in range(3):
        available = [n for n in neighbors[current] if (current,n) != tabu_reverse]
        following = min(available, key=costs.get)
        tabu_reverse = (following,current)
        current = following
        path.append(current)
    assert path == ['A','B','C','A']
    # A declared illustrative aspiration rule admits a new best-so-far cost.
    archive_cost, candidates = 3, [('tabu',2,True),('available',7,False)]
    without = min((c for c in candidates if not c[2]),key=lambda c:c[1])[1]
    with_aspiration = min((c for c in candidates if not c[2] or c[1] < archive_cost),key=lambda c:c[1])[1]
    assert without == 7 and with_aspiration == 2
    feature_cost = [4,2,7]
    indicators, penalties = [1,1,0], [1,0,0]
    utilities = [i*c/(1+p) for i,c,p in zip(indicators,feature_cost,penalties)]
    maximizers = [i for i,u in enumerate(utilities) if u == max(utilities)]
    assert utilities == [2,2,0] and maximizers == [0,1]
    for i in maximizers:penalties[i] += 1
    assert penalties == [2,1,0]
    original, scale = 10, 2
    augmented = original+scale*sum(p*i for p,i in zip(penalties,indicators))
    assert augmented == 16
    # Same penalty on every feature is constant only on equal-cardinality sets.
    original_pair = [10,9]
    counts = [1,2]
    common_penalty = 3
    unequal = [g+scale*common_penalty*n for g,n in zip(original_pair,counts)]
    equal = [g+scale*common_penalty for g in original_pair]
    assert unequal == [16,21] and equal == [16,15]
    assert (original_pair[0]-original_pair[1]) == (equal[0]-equal[1])
    assert (original_pair[0]-original_pair[1]) != (unequal[0]-unequal[1])
    zero_utilities = [1*0/(1+0),0*3/(1+0)]
    assert zero_utilities == [0,0]
    all_feature_ties = [i for i,u in enumerate(zero_utilities) if u == max(zero_utilities)]
    present_feature_ties = [i for i in all_feature_ties if [1,0][i]]
    assert all_feature_ties == [0,1] and present_feature_ties == [0]
    # ILS acceptance evaluates the embedded optimizer's output, not its input.
    ils_costs = {'A':2, 'perturbed':100, 'B':1, 'C':3}
    optimized_candidate = {'perturbed':'B'}['perturbed']
    assert ils_costs[optimized_candidate] < ils_costs['A'] < ils_costs['perturbed']
    better_accepts_worse = ils_costs['C'] < ils_costs['A']
    always_accepts_worse = True
    assert not better_accepts_worse and always_accepts_worse
    return dict(tabu_tenure_one_cycle=path,tabu_path_costs=[costs[x] for x in path],
                best_admissible_without_aspiration=without,with_declared_aspiration=with_aspiration,
                gls_utilities=utilities,gls_tied_penalty_updates=penalties,gls_augmented_cost=augmented,
                equal_penalties_variable_cardinality=unequal,equal_penalties_fixed_cardinality=equal,
                all_zero_utility_all_feature_ties=all_feature_ties,present_only_ties=present_feature_ties,
                ils_optimized_candidate=optimized_candidate,ils_intermediate_cost=100,
                better_accepts_worse=better_accepts_worse,always_accepts_worse=always_accepts_worse,
                interpretation='One-step reversal memory permits a longer cycle; a specified aspiration rule changes admissibility. GLS updates all positive-utility ties and must declare the all-zero case. Common penalties cancel only at fixed feature count. ILS tests the optimized candidate and supports different acceptance rules. These are finite boundary examples, not convergence proofs or performance tests.')

if __name__ == '__main__':
    print(json.dumps(calculate(),indent=2))
