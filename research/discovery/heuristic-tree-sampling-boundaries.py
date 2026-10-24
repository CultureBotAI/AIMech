"""Finite exact expectation checks for tree sampling, not author implementation."""
from fractions import Fraction as F
import json
# Root has two children; one has one leaf and the other has three leaves.
# Depth-only sampling selects either parent with equal probability.
values=[F(5),F(9)];mean=sum(values)/2;var=sum((x-mean)**2 for x in values)/2
assert mean==7 and var==4
# Separating the two parents, then merging four terminal leaves, is exact.
refined=1+1+1+4
assert refined==7

# Merge an existing representative(weight1,subtree sum1) and incoming(3,5).
old_w,new_w=F(1),F(3);old_phi,new_phi=F(1),F(5);total=old_w+new_w
expected=old_w*old_phi+new_w*new_phi
hs_expectation=(old_w/total)*total*old_phi+(new_w/total)*total*new_phi
wrong_uniform=F(1,2)*total*(old_phi+new_phi)
q=F(1,2)
gs_expectation=(1-q)*(old_w/(1-q))*old_phi+q*(new_w/q)*new_phi
assert expected==hs_expectation==gs_expectation==16 and wrong_uniform==12

# A diamond DAG unfolds into five path occurrences but has four distinct nodes.
path_occurrences=1+2+2;distinct_graph_nodes=4
assert path_occurrences!=distinct_graph_nodes

# One of1000children has1000leaves; others terminate immediately.
p=F(1,1000);rare=F(1001001);common=F(1001)
rare_mean=p*rare+(1-p)*common
rare_var=p*(rare-rare_mean)**2+(1-p)*(common-rare_mean)**2
assert rare_mean==2001 and rare_var==999000000
miss_five=(1-p)**5
assert miss_five>F(99,100)

# Printed AppendixEq99 inequality points the wrong way for k>r.
k,r=4,3;left=F(k*(k-1)-r*(r-1),2);printed_right=F(r*(k-r),2)
assert left==3 and printed_right==F(3,2) and not left<=printed_right
print(json.dumps({
 'depth_only_outcomes':[str(x) for x in values],
 'depth_only_mean':str(mean),'depth_only_variance':str(var),
 'separated_parent_strata_exact_count':refined,
 'weighted_merge_expected_sum':str(hs_expectation),
 'uncorrected_uniform_merge_expected_sum':str(wrong_uniform),
 'importance_corrected_merge_expected_sum':str(gs_expectation),
 'unfolded_path_count_vs_distinct_DAG_nodes':[path_occurrences,distinct_graph_nodes],
 'rare_tree_actual_and_expected_count':str(rare_mean),
 'rare_tree_single_probe_variance':str(rare_var),
 'probability_five_probes_miss_deep_nodes':str(miss_five),
 'appendix99_left_and_right':[str(left),str(printed_right)],
 'scope':'Finite rational counterexamples and expectations; no author software, theorem-wide certification or benchmark replication.'
},indent=2))
