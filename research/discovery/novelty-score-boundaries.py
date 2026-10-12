"""Exact score examples; no classifier training or historical benchmark."""
from fractions import Fraction as F
import json

def nearest_indices(points, query):
    distances=[abs(x-query) for x in points]
    return [i for i,d in enumerate(distances) if d==min(distances)]

def ratio(points, query, chosen):
    assert chosen in nearest_indices(points,query)
    spacing=min(abs(points[chosen]-p) for i,p in enumerate(points) if i!=chosen)
    numerator=abs(query-points[chosen])
    return numerator,spacing,None if spacing==0 else numerator/spacing

points=[F(-1,10),F(0),F(2)]
tied=nearest_indices(points,F(1))
assert tied==[1,2]
tie_scores=[ratio(points,F(1),i)[2] for i in tied]
assert tie_scores==[F(10),F(1,2)]
query=F(9,10)
chosen=nearest_indices(points,query)
assert chosen==[1] and ratio(points,query,chosen[0])[2]==9
assert abs(query-points[2])<min(abs(points[2]-p) for i,p in enumerate(points) if i!=2)
assert all(ratio(points,p,i)[2]==0 for i,p in enumerate(points))
duplicate=ratio([F(0),F(0),F(2)],F(0),0)
assert duplicate==(0,0,None)
single_neighbor_error=False
try:
    ratio([F(0)],F(1),0)
except ValueError:
    single_neighbor_error=True
assert single_neighbor_error

def variance(outputs):
    mean=sum(outputs)/len(outputs)
    return sum(x*x for x in outputs)/len(outputs)-mean*mean

assert variance([F(0),F(1)])==F(1,4)
assert variance([F(1),F(1)])==0
calibration=[F(0),F(1,4)]
mean=sum(calibration)/2
score_variance=variance(calibration)
score_sd=F(1,8)
assert score_sd**2==score_variance
variance_threshold=mean+3*score_variance
sd_threshold=mean+3*score_sd
query_score=F(1,4)
assert variance_threshold==F(11,64) and sd_threshold==F(1,2)
assert query_score>variance_threshold and not query_score>sd_threshold
scaled_calibration=[4*x for x in calibration] # Doubling classifier outputs quadruples variance scores.
scaled_query=4*query_score
scaled_variance_threshold=sum(scaled_calibration)/2+3*variance(scaled_calibration)
assert scaled_variance_threshold==F(5,4)
assert not scaled_query>scaled_variance_threshold
assert variance([F(2),F(4)])==4*variance([F(0),F(1)])
print(json.dumps(dict(status='passed',nearest_tie_scores=list(map(str,tie_scores)),nearest_selection_differs_from_union_of_balls=True,duplicate_ratio='undefined 0/0',singleton_has_no_other_neighbor=True,distinct_training_ratios='all zero',bootstrap_variance=str(F(1,4)),stable_outputs_variance='0',variance_threshold=str(variance_threshold),standard_deviation_threshold=str(sd_threshold),doubled_output_variance_threshold=str(scaled_variance_threshold),interpretation='Exact score-level counterexamples expose unspecified conventions and distinguish the source threshold formulas; no source policy is invented and no trained model is evaluated.'),indent=2))
