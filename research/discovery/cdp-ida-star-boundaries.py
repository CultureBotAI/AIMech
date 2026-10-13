"""Finite CDP scope examples; no author software or benchmark replication."""
import json
from math import isclose


def one_step_counts(root_h, threshold, branching, transitions):
    current={root_h:1.0};levels=[]
    for depth in range(threshold+1):
        expanded={h:n for h,n in current.items() if h<=threshold-depth}
        levels.append(sum(expanded.values()))
        nxt={}
        for hp,n in expanded.items():
            for hc,p in transitions[hp].items():
                nxt[hc]=nxt.get(hc,0.)+n*branching[hp]*p
        current=nxt
    return levels


def result():
    homogeneous=one_step_counts(0,2,{0:2},{0:{0:1.}})
    assert homogeneous==[1.,2.,4.] and sum(homogeneous)==7
    visited=0;expanded_before_goal=0
    for is_goal in [False,True]:
        visited+=1
        if is_goal:break
        expanded_before_goal+=1
    assert visited==2 and expanded_before_goal==1
    # A potential descendant cannot be generated through a pruned ancestor.
    path_h=[0,3,0];potential=sum(depth+h<=2 for depth,h in enumerate(path_h))
    reachable=0
    for depth,h in enumerate(path_h):
        if depth+h>2:break
        reachable+=1
    assert potential==2 and reachable==1
    # Two same-h start contexts, one always creates h=2, the other h=0.
    pooled=sum(one_step_counts(0,1,{0:1,2:1},{0:{0:.5,2:.5},2:{2:1.}}))
    assert pooled==1.5 and pooled==(1+2)/2
    # A stationary anti-correlated two-type transition has the same .5/.5
    # marginal as independent transitions but fewer expansions from h=0.
    independent=sum(one_step_counts(0,1,{0:1,2:1},{0:{0:.5,2:.5},2:{0:.5,2:.5}}))
    anticorrelated=sum(one_step_counts(0,1,{0:1,2:1},{0:{2:1.},2:{0:1.}}))
    assert independent==1.5 and anticorrelated==1.
    # Both earlier siblings survive together or both fail, each with prob .5.
    marginal_survival=.5;independent_third=marginal_survival**2;joint_third=.5
    assert joint_third!=independent_third
    actual_generated=1+.5+joint_third;independent_generated=1+.5+independent_third
    # Mixing unequal-degree parents: average fraction differs from pooled children.
    mean_branching=(1+3)/2;mean_parent_fraction=(1+0)/2;pooled_child_fraction=1/4
    actual_low_children=(1+0)/2
    assert mean_branching*mean_parent_fraction==1!=actual_low_children
    assert isclose(mean_branching*pooled_child_fraction,actual_low_children)
    return dict(homogeneous_context=dict(expanded_by_depth=homogeneous,total=7,early_stop_nodes_visited=visited,early_stop_expansions_with_goal_test_before_expansion=expanded_before_goal),
                ancestor_pruning=dict(potential_nodes=potential,actually_expanded=reachable),
                heterogeneous_start_context=dict(actual_counts=[1,2],pooled_prediction=pooled),
                independence_is_not_a_universal_lower_bound=dict(independent_prediction=independent,anticorrelated_count=anticorrelated),
                correlated_bpmx_sibling_survival=dict(third_child_joint_survival=joint_third,power_approximation=independent_third,expected_generated=actual_generated,power_based_expected_generated=independent_generated),
                variable_branching_weighting=dict(mean_branching=mean_branching,mean_parent_fraction=mean_parent_fraction,pooled_child_fraction=pooled_child_fraction,actual_mean_low_children=actual_low_children),
                interpretation='Exactness requires matched context and counting conventions; sampled or independence-based predictions are not certified bounds.')


if __name__=='__main__':print(json.dumps(result(),indent=2,sort_keys=True))
