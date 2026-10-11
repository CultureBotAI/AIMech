"""Curator arithmetic for three concept boundaries; no author code or benchmark."""
import json
from math import isclose


def calculate():
    table = {('x','a'): 1., ('x','unvisited'): 7., ('y','b'): 2., ('y','c'): 8.}
    before = dict(table)
    alpha, gamma, reward = .25, .9, 2.
    target = reward + gamma*max(table['y','b'],table['y','c'])
    table['x','a'] = (1-alpha)*table['x','a']+alpha*target
    behavior_action_target_update = (1-alpha)*before['x','a']+alpha*(reward+gamma*table['y','b'])
    assert isclose(table['x','a'],3.05) and isclose(behavior_action_target_update,1.7)
    assert all(table[k]==before[k] for k in before if k!=('x','a'))
    # Exact formula for the first n squared stepsizes under constant alpha=.25.
    constant_squared_sum_100 = 100*alpha**2
    constant_squared_sum_200 = 200*alpha**2
    assert constant_squared_sum_200 == 2*constant_squared_sum_100

    p,queues,mixing = [.2,.3,.5],[1.,2.,3.],.3
    heuristics = [1-q/sum(queues) for q in queues]
    weights = [x+mixing*h for x,h in zip(p,heuristics)]
    normalizer = 1+mixing*(len(p)-1)
    full = [w/normalizer for w in weights]
    assert isclose(sum(full),1.)
    eligible = full[:2]
    conditional = [v/sum(eligible) for v in eligible]
    assert not isclose(sum(eligible),1.) and isclose(sum(conditional),1.)
    def reinforce(values,index,r):
        return [(1-r)*v+(r if i==index else 0.) for i,v in enumerate(values)]
    updated = reinforce(p,0,.2)
    assert all(isclose(x,y) for x,y in zip(updated,[.36,.24,.4]))
    assert isclose(sum(updated),1.)
    weak = reinforce(p,0,.01)
    assert weak[0]>p[0]
    boundary = reinforce(p,0,1.)
    assert boundary == [1.,0.,0.]
    power_weights = [v**1.2 for v in p]
    data_policy = [v/sum(power_weights) for v in power_weights]
    assert all(v>0 for v in data_policy)
    first_then_second = reinforce(reinforce(p,0,.2),1,.3)
    second_then_first = reinforce(reinforce(p,1,.3),0,.2)
    assert first_then_second != second_then_first
    forward_time,backward_time = sum([2.,7.]),sum([1.,1.])
    assert forward_time != backward_time

    evaporate = lambda x: .5*x
    deposit = lambda x: x+1.
    evaporate_then_deposit = deposit(evaporate(2.))
    deposit_then_evaporate = evaporate(deposit(2.))
    assert evaporate_then_deposit==2. and deposit_then_evaporate==1.5
    return {
        'q_learning': {'max_target':target,'updated_observed_entry':table['x','a'],'next_behavior_action_substitution':behavior_action_target_update,'other_entries_unchanged':True,'constant_stepsize_squared_sums_at_100_and_200':[constant_squared_sum_100,constant_squared_sum_200],'qualification':'The exact constant-rate squared-sum grows linearly, violating the theorem condition; these finite values are not a convergence proof or a universal failure claim.'},
        'antnet': {'full_neighbor_probabilities':full,'mass_after_excluding_third_without_renormalizing':sum(eligible),'conditional_eligible_probabilities':conditional,'reinforced_probabilities':updated,'weakly_rewarded_selected_probability':weak[0],'r_equals_one':boundary,'power_reweighted_data_policy':data_policy,'two_update_orders':[first_then_second,second_then_first],'measured_forward_time':forward_time,'different_backward_time_not_substituted':backward_time},
        'aco_schedule': {'evaporate_then_deposit':evaporate_then_deposit,'deposit_then_evaporate':deposit_then_evaporate,'qualification':'A simple noncommuting pair illustrates why a framework must declare update scheduling; it does not assert one universal ACO update.'},
        'limits':'Illustrative finite arithmetic only; no stochastic algorithm execution, simulator, author code, benchmark or theorem-proof audit.'}


if __name__=='__main__':
    print(json.dumps(calculate(),indent=2))
