"""Standalone geometry checks of inspected PERCH expressions; no author execution."""
from itertools import product
from fractions import Fraction as F
import json


def ds(a,b):return sum((x-y)**2 for x,y in zip(a,b))
def corners(points):return [tuple(min(p[j] for p in points) for j in range(len(points[0]))),tuple(max(p[j] for p in points) for j in range(len(points[0])))]
def cached_min_squared(a,b):
    return max(min(min(ds(x,c) for x in a) for c in corners(b)),min(min(ds(x,c) for x in b) for c in corners(a)))
def cached_max_squared(a,b):
    return min(max(max(ds(x,c) for x in a) for c in corners(b)),max(max(ds(x,c) for x in b) for c in corners(a)))


def main():
    a=[(0,),(5,),(10,)];b=[(4,),(6,)]
    lower=cached_min_squared(a,b);true_min=min(ds(x,y) for x,y in product(a,b))
    assert lower==16 and true_min==1
    c=[(0,1),(1,0)];d=[(10,-10)]
    upper=cached_max_squared(c,d);true_max=max(ds(x,y) for x,y in product(c,d))
    assert upper==202 and true_max==221
    # The paper's unsquared diagonal-times-count is not a general SSE bound.
    pts=[F(0),F(10)];mean=sum(pts)/len(pts)
    sse=sum((x-mean)**2 for x in pts);diagonal=max(pts)-min(pts)
    assert sse==50 and diagonal*len(pts)==20
    print(json.dumps(dict(cached_min=dict(left=a,right=b,reported_squared=lower,actual_squared=true_min),cached_max=dict(left=c,right=d,reported_squared=upper,actual_squared=true_max),pruning_units=dict(points=pts,sse=sse,paper_diagonal_times_count=diagonal*len(pts),python_half_child_distance_times_count=diagonal*len(pts)/2),limits='These are standalone evaluations of inspected scalar expressions for explicit point sets. They do not execute PERCH, construct an insertion history, establish reachability, or measure dendrogram purity or runtime.'),default=str,indent=2))


if __name__=='__main__':main()
