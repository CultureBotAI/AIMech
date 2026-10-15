#!/usr/bin/env python3
"""Original exact rational DIRECT boundary audit, not author code or benchmark.
Jones, Perttunen, Stuckman (1993), Definitions3.1/4.1 and rectangle subdivision.
The selector handles a finite rational radius/value cloud. It is cross-checked
against independent enumeration of all positive affine breakpoints and intervals.
Full multivariate Euclidean radii need square roots; this audit instead checks
multivariate subdivision geometry exactly and uses rational radii for selection.
No floating optimization, source implementation, or general proof is executed.
"""
from fractions import Fraction as F
from itertools import product, combinations
import json
import math


def slope_interval(rows,j,epsilon):
    assert epsilon>0 and all(d>0 for d,f in rows)
    d,f=rows[j];fmin=min(v for _,v in rows)
    low=max(F(0),(f-fmin+epsilon*abs(fmin))/d);high=None
    for di,fi in rows:
        if di==d:
            if fi<f:return None
        elif di>d:
            bound=(fi-f)/(di-d)
            high=bound if high is None else min(high,bound)
        else:low=max(low,(f-fi)/(d-di))
    if high is not None and (high<low or high<=0):return None
    witness=low if low>0 else (F(1) if high is None else high/2)
    assert witness>0
    assert all(f-witness*d<=fi-witness*di for di,fi in rows)
    assert f-witness*d<=fmin-epsilon*abs(fmin)
    return low,high,witness


def select(rows,epsilon):
    return [j for j in range(len(rows))if slope_interval(rows,j,epsilon)is not None]


def breakpoint_oracle(rows,epsilon):
    # Truth of every affine inequality can change only at these exact roots.
    cuts={F(0)};fmin=min(f for d,f in rows)
    for d,f in rows:
        cuts.add((f-fmin+epsilon*abs(fmin))/d)
        for di,fi in rows:
            if di!=d:cuts.add((f-fi)/(d-di))
    cuts=sorted(x for x in cuts if x>=0)
    probes={x for x in cuts if x>0}
    probes.update((a+b)/2 for a,b in zip(cuts,cuts[1:]))
    probes.add(cuts[-1]+1)
    result=[]
    for j,(d,f)in enumerate(rows):
        if any(k>0 and f-k*d<=fmin-epsilon*abs(fmin) and all(f-k*d<=fi-k*di for di,fi in rows)for k in probes):result.append(j)
    return result


def center(box):return tuple((lo+hi)/2 for lo,hi in box)
def volume(box):return math.prod(hi-lo for lo,hi in box)
def radius2(box):return sum((hi-lo)**2/4 for lo,hi in box)


def divide(box,fun,tie_reverse=False):
    lengths=[hi-lo for lo,hi in box];long=max(lengths)
    axes=[i for i,l in enumerate(lengths)if l==long];delta=long/3;c=center(box)
    samples={c:fun(c)};w={}
    for i in axes:
        values=[]
        for sign in [-1,1]:
            x=list(c);x[i]+=sign*delta;x=tuple(x);samples[x]=fun(x);values.append(samples[x])
        w[i]=min(values)
    order=sorted(axes,key=lambda i:(w[i],-i if tie_reverse else i))
    children=[];middle=list(box)
    for i in order:
        lo,hi=middle[i];step=(hi-lo)/3
        for limits in [(lo,lo+step),(lo+2*step,hi)]:
            child=middle.copy();child[i]=limits;children.append(tuple(child))
        middle[i]=(lo+step,lo+2*step)
    children.append(tuple(middle))
    assert len(samples)==2*len(axes)+1==len(children)
    assert sum(map(volume,children))==volume(box)
    assert {center(b)for b in children}==set(samples)
    for b in children:
        assert all(lo>=p_lo and hi<=p_hi and lo<hi for (lo,hi),(p_lo,p_hi)in zip(b,box))
        assert radius2(b)<radius2(box)
    for a,b in combinations(children,2):
        assert not all(max(al,bl)<min(ah,bh)for(al,ah),(bl,bh)in zip(a,b))
    return children,samples,order


def run_1d(fun,iterations,epsilon=F(1,10000)):
    boxes=[((F(0),F(1)),)];observed={F(1,2):fun(F(1,2))};history=[]
    for t in range(iterations+1):
        ordered=sorted(boxes);last=F(0)
        for b in ordered:
            assert b[0][0]==last;last=b[0][1]
        assert last==1
        fmin=min(observed.values());max_radius=max((b[0][1]-b[0][0])/2 for b in boxes)
        history.append({'iteration':t,'rectangles':len(boxes),'evaluations':len(observed),'best':str(fmin),'maximum_radius':str(max_radius)})
        if t==iterations:break
        rows=[((b[0][1]-b[0][0])/2,observed[center(b)[0]])for b in boxes]
        chosen=select(rows,epsilon);assert chosen
        # Freeze the complete selected set at the beginning of this iteration.
        replacement=[]
        for j,b in enumerate(boxes):
            if j not in chosen:replacement.append(b);continue
            children,samples,_=divide(b,lambda x:fun(x[0]))
            replacement+=children
            for x,value in samples.items():observed[x[0]]=value
        boxes=replacement
    return history,observed


def run():
    epsilon_values=[F(1,100),F(1,10),F(1)]
    cases=checks=largest_checks=0
    for values in product(map(F,[-2,-1,0,1,2]),repeat=3):
        rows=list(zip([F(1,18),F(1,6),F(1,2)],values))
        for epsilon in epsilon_values:
            got=select(rows,epsilon);assert got==breakpoint_oracle(rows,epsilon)
            assert 2 in got # unique largest radius always potentially optimal
            cases+=1;checks+=3;largest_checks+=1
    for values in product(map(F,[-1,0,1]),repeat=4):
        rows=list(zip([F(1,18),F(1,18),F(1,6),F(1,6)],values))
        for epsilon in epsilon_values:
            got=select(rows,epsilon);assert got==breakpoint_oracle(rows,epsilon)
            best_large=min(values[2:]);assert all(i in got for i in [2,3]if values[i]==best_large)
            cases+=1;checks+=4;largest_checks+=1
    assert cases==618 and checks==2097
    zero_only=[(F(1),F(0)),(F(2),F(0))]
    assert select(zero_only,F(1,100))==[1]
    tied=[(F(1,6),F(1)),(F(1,6),F(1)),(F(1,18),F(1))]
    assert select(tied,F(1,100))==[0,1]
    # Realizable five-interval partition: side thirds, central third trisected.
    rows=[(F(1,6),F(1)),(F(1,18),F(1,10)),(F(1,18),F(0)),(F(1,18),F(1,5)),(F(1,6),F(1))]
    base=select(rows,F(1,100));shift=select([(d,f+100)for d,f in rows],F(1,100))
    assert base==[0,2,4] and shift==[0,4]
    scaled=select([(d,7*f)for d,f in rows],F(1,100));assert scaled==base
    # Second condition alone is origin-sensitive; first condition is shift invariant.
    shift_witness={'base_indices':base,'plus100_indices':shift,'positive_scale7_indices':scaled,'small_radius':'1/18','small_base_f':'0','large_radius':'1/6','large_base_f':'1','epsilon':'1/100','base_small_K_range':['0 excluded','9 included'],'shifted_small_K_required_at_least':'18'}
    geometry=0;dimension_counts={}
    for n in range(1,5):
        count=0
        for level in [0,1,2]:
            for offsets in product([0,1],repeat=n):
                # All generated boxes have the balanced side-exponent property.
                box=tuple((F(0),F(1,3**(level+v)))for v in offsets)
                for kind in ['linear','tied']:
                    fun=(lambda x:sum((i+1)*z for i,z in enumerate(x)))if kind=='linear'else(lambda x:F(0))
                    children,_,_=divide(box,fun)
                    for b in children:
                        lengths=[hi-lo for lo,hi in b];assert max(lengths)<=3*min(lengths)
                    geometry+=1;count+=1
        dimension_counts[n]=count
    # Figure7 values: vertical pair min2 precedes horizontal pair min5.
    unit=((F(0),F(1)),)*2;c=(F(1,2),F(1,2))
    values={c:F(0),(F(1,6),F(1,2)):F(5),(F(5,6),F(1,2)):F(8),(F(1,2),F(1,6)):F(2),(F(1,2),F(5,6)):F(6)}
    children,_,order=divide(unit,values.__getitem__);assert order==[1,0]
    by_value={values[center(b)]:volume(b)for b in children}
    assert by_value[2]==by_value[6]==F(1,3)and by_value[5]==by_value[8]==F(1,9)
    # A tie convention can change the labelled partition despite identical values.
    left,_,left_order=divide(unit,lambda x:F(0));right,_,right_order=divide(unit,lambda x:F(0),True)
    assert left_order==[0,1] and right_order==[1,0] and set(left)!=set(right)
    histories={};sample_sets={}
    for name,fun in [('zero',lambda x:F(0)),('negative_constant',lambda x:F(-2)),('linear_boundary',lambda x:x),('quadratic',lambda x:(x-F(1,4))**2+2),('absolute',lambda x:abs(x-F(2,7)))]:
        h,obs=run_1d(fun,5);histories[name]=h;sample_sets[name]=obs
        best=[F(row['best'])for row in h];assert all(a>=b for a,b in zip(best,best[1:]))
    for t,row in enumerate(histories['zero']):assert row['evaluations']==3**t and F(row['maximum_radius'])==F(1,2*3**t)
    assert F(histories['linear_boundary'][-1]['best'])>0
    # Finite-run hidden continuous dip: after t=2 constant observations there are
    #9 centers; choose a gap-contained rational tent around an unobserved point.
    _,observed=run_1d(lambda x:F(0),2);a=F(1,9);width=F(1,100)
    tent=lambda x:-max(F(0),1-abs(x-a)/width)
    assert all(tent(x)==0 for x in observed) and tent(a)==-1
    # Discontinuous isolated minimum at sqrt(2)/2 cannot be any rational center.
    # This is a mathematical observation, not a floating equality simulation.
    # IntroEq5 claims the V-intersection value; endpoint0, length2,K1 gives-1.
    crossing=F(1);true_v=max(-crossing,crossing-2);printed_v=F(-2)
    assert true_v==-1 and printed_v<true_v
    # Equal-radius indices make printed convergenceEq11 divide by zero; direct
    # definition still admits the best largest rectangle with positive K.
    equal=[(F(1,6),F(0)),(F(1,6),F(1))]
    assert select(equal,F(1,100))==[0]
    return {'scope':'Original supporting rational boundary audit; no external author code, canonical review, performance benchmark or infinite-run proof by testing.',
        'arithmetic':'Fraction exact arithmetic throughout; no floating comparisons or numerical optimization.',
        'selector':{'cloud_cases':cases,'candidate_checks':checks,'largest_rectangle_checks':largest_checks,'epsilon_values':list(map(str,epsilon_values)),'oracle':'Independent finite positive breakpoint/endpoints/interval enumeration of affine inequalities','K_zero_only_rejected':True,'identical_largest_ties_selected':True},
        'objective_origin':shift_witness,
        'subdivision':{'cases':geometry,'by_dimension':dimension_counts,'checked':'Volume conservation, disjoint interiors, bounds, sampled centers,2|I| new samples, strictly smaller squared radii and balanced side lengths','figure7':{'axis_order':order,'volumes_by_value':{str(k):str(v)for k,v in by_value.items()}},'tie_orders':[left_order,right_order],'tie_partitions_differ':True},
        'finite_1d_runs':histories,
        'finite_budget_counterexample':{'sample_count':len(observed),'sample_locations':list(map(str,sorted(observed))),'tent_center':str(a),'half_width':str(width),'observed_values':'all0','true_minimum':'-1','scope':'Explicit continuous narrow dip consistent with all finite samples; demonstrates absence of a finite accuracy certificate from these samples alone.'},
        'discontinuous_counterexample':{'domain':'[0,1]','function':'-1 only at sqrt(2)/2,0 elsewhere','reason':'All exact DIRECT center samples are rational; density does not imply convergence of sampled values without continuity near a global minimizer.'},
        'source_caveats':{'intro_Eq5':{'a':'0','b':'2','endpoint_values':['0','0'],'K':'1','crossing':'1','correct_V_minimum':str(true_v),'printed_value':str(printed_v),'qualification':'Printed expression is a weaker lower bound here, but not the claimed bottom-of-V value; DIRECT center-sample Eq8 and definitions are separate.'},'convergence_Eq11':{'equal_radius_rows':[[str(d),str(f)]for d,f in equal],'selected':[0],'needed_guard':'Take slope ratios only over strictly smaller radii; equal-radius rows are handled by value comparison. The printed unrestricted maximum includes zero denominators.'}},
        'limits':['Only rational radius clouds are used for potential-optimality arithmetic; general multivariate Euclidean radius selection is not implemented.','Finite geometry/1D examples do not establish asymptotic rates or convergence of every variant.','Original method requires complete selected-set processing, exact comparisons in the proof, finite objective values and an attained global minimum with continuity nearby for value convergence.','No stochastic/noisy objective handling, constraints beyond a box, author software, wall-clock comparison or high-dimensional benchmark.']}


if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
