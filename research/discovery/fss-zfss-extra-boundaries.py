"""Portable exact support, endpoint, source-figure and composition checks.
Uses only the sibling curator module. No calculation runs on import; main()
returns deterministic semantic output and the CLI prints it to stdout. No file writes.
Execution times and hashes belong in an external receipt."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util
import json
import sys
base=Path(__file__).with_name('fss-zfss-boundaries.py')
spec=importlib.util.spec_from_file_location('fss_zfss_exact_boundaries',base)
module=importlib.util.module_from_spec(spec)
previous_bytecode_setting=sys.dont_write_bytecode
try:
    sys.dont_write_bytecode=True
    spec.loader.exec_module(module)
finally:
    sys.dont_write_bytecode=previous_bytecode_setting
A=module.alg8;sample=module.sample9;check=module.properties;strings=module.strings
Z=Q(0);ONE=Q(1)
def matrix(p,z):return [A(p,k,z) for k in range(len(p))]
def multiply(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(A))) for j in range(len(B[0]))] for i in range(len(A))]
def ss_geometry(p):
    n=len(p);flow=[[Z]*n for _ in p];levels=sorted({Z,*p})
    for low,high in zip(levels,levels[1:]):
        active=[i for i,v in enumerate(p) if v>(low+high)/2]
        for j,i in enumerate(active):flow[i][active[j-1]]+=high-low
    return [[v/p[i] for v in row] for i,row in enumerate(flow)]
def main():
    out={'scope':'Supplementary curator rational calculations; uses the independently authored algorithms of the base audit, never author software.'}
    p=(Q(1,10),Q(1,5),Q(1,5),Q(1,20),Q(9,20));S=ss_geometry(p)
    expected=[[Z,Z,Z,Z,ONE],[Q(1,2),Z,Z,Z,Q(1,2)],[Z,ONE,Z,Z,Z],[Z,Z,ONE,Z,Z],[Z,Z,Q(1,3),Q(1,9),Q(5,9)]]
    assert S==expected;check(p,S)
    out['figure10_simple_slice']={'target':p,'matrix':S,'agrees_with_printed_matrix':True}
    p=(Q(1,4),Q(1,4),Q(1,2));endpoints=[]
    for zero in [False,True]:
        M=matrix(p,zero);j,_=sample(p,2,zero,ONE);assert j==2 and M[2][j]==0
        endpoints.append({'method':'ZFSS' if zero else 'FSS','target':p,'current_state_1based':3,'uniform_value':ONE,'returned_state_1based':j+1,'returned_transition_probability':M[2][j],'row':M[2]})
    out['endpoint_counterexamples']=endpoints
    p=(Q(1,2),Q(1,2),Q(0));M=matrix(p,True);alt=[r[:] for r in M];alt[2]=[ONE,Z,Z]
    assert check(p,M)==(True,Z)==check(p,alt)
    out['zero_row_nonuniqueness']={'target':p,'published_algorithm8_kernel':M,'alternative_invariant_kernel':alt,'both_reversible_and_minimal_self':True,'meaning':'Uniqueness of Eq112 is on positive support; a zero-mass row is not determined by stationarity. Algorithm8 explicitly sets that row to the target law.'}
    # Zero-height labels are part of the fixed order: compressing support is not
    # always the same FSS kernel, although both resulting kernels are stationary.
    p=(Z,Q(3,7),Q(2,7),Q(2,7));positive=p[1:]
    fullF=matrix(p,False);fullZ=matrix(p,True);shortF=matrix(positive,False);shortZ=matrix(positive,True)
    restrictF=[row[1:] for row in fullF[1:]];restrictZ=[row[1:] for row in fullZ[1:]]
    assert restrictF!=shortF and restrictZ==shortZ
    assert fullF[1][1]==Q(1,6) and shortF[0][0]==0
    out['zero_label_order_effect']={'target_with_leading_zero':p,'positive_target':positive,'FSS_positive_rows_with_zero_label':restrictF,'FSS_after_deleting_zero_label':shortF,'ZFSS_same_after_this_deletion':True,'meaning':'Do not silently delete zero-probability labels before applying FSS: the immediate predecessor excluded from mass redistribution is part of the specified order. This example distinguishes support preservation from kernel identity.'}

    # Each coordinate conditional exists here, although some individual states have zero mass.
    w=(1,0,2,3,2,1,2,3,1);joint=tuple(Q(a,sum(w)) for a in w);states=[(a,b) for a in range(3) for b in range(3)]
    out['joint_compositions']=[]
    for zero in [False,True]:
        kernels=[]
        for c in range(2):
            K=[[Z]*9 for _ in range(9)]
            for i,state in enumerate(states):
                group=[j for j,t in enumerate(states) if t[1-c]==state[1-c]]
                denominator=sum(joint[j] for j in group);assert denominator>0
                conditional=tuple(joint[j]/denominator for j in group)
                row=A(conditional,group.index(i),zero)
                for j,v in zip(group,row):K[i][j]=v
            check(joint,K);kernels.append(K)
        cycle=multiply(*kernels);mix=[[Q(1,3)*kernels[0][i][j]+Q(2,3)*kernels[1][i][j] for j in range(9)] for i in range(9)]
        cycle_prop=check(joint,cycle);mix_prop=check(joint,mix)
        out['joint_compositions'].append({'method':'ZFSS' if zero else 'FSS','joint_target_row_major_3x3':joint,'both_coordinate_kernels_stationary':True,'fixed_scan_stationary':True,'fixed_mixture_stationary':True,'fixed_scan_reversible':cycle_prop[0],'fixed_mixture_reversible':mix_prop[0],'fixed_scan_matrix':cycle,'fixed_mixture_matrix':mix})
    # Uniform independent coordinates: every coordinate deterministically cycles backwards.
    joint=tuple(Q(1,9) for _ in range(9));classes=[]
    for d in range(3):classes.append([i for i,(a,b) in enumerate(states) if (a-b)%3==d])
    for zero in [False,True]:
        for a,b in states:
            row=A((Q(1,3),)*3,a,zero);assert row[(a-1)%3]==1
            row=A((Q(1,3),)*3,b,zero);assert row[(b-1)%3]==1
    out['systematic_scan_counterexample']={'joint_target':'Uniform independent 3x3 coordinates','transition':'(a,b) -> (a-1 mod3,b-1 mod3) each full scan','three_closed_classes_0based_row_major':classes,'period_within_class':3,'meaning':'Both FSS and ZFSS preserve the target but a deterministic full scan is reducible. Zero self transitions do not guarantee convergence from every initial state.'}
    return strings(out)


if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
