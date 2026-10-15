#!/usr/bin/env python3
"""Small curator probability/algebra checks for ES/PES source interpretation.

Not ES/PES, EP, random-feature GP fitting, an acquisition optimizer, or author code.
Probability masses and matrix examples are exact Fraction arithmetic. Entropy
values use standard-library floating natural logarithms and a 2e-14 tolerance.
Source lineage and actual execution timestamps belong in the external handoff.
"""
from fractions import Fraction as F
from math import log, isclose
from itertools import product
import json


def entropy(ps):
    return -sum(float(p)*log(float(p)) for p in ps if p)


def kl(ps, qs):
    return sum(float(p)*log(float(p/q)) for p,q in zip(ps,qs) if p)


def measures(joint):
    ps=[sum(row,F(0)) for row in joint]
    py=[sum((row[y] for row in joint),F(0)) for y in range(len(joint[0]))]
    qsy=[[joint[s][y]/py[y] for s in range(len(ps))] if py[y] else [] for y in range(len(py))]
    qys=[[p/ps[s] for p in row] if ps[s] else [] for s,row in enumerate(joint)]
    target=entropy(ps)-sum(float(p)*entropy(q) for p,q in zip(py,qsy))
    predictive=entropy(py)-sum(float(p)*entropy(q) for p,q in zip(ps,qys))
    mi=sum(float(p)*log(float(p/(ps[s]*py[y]))) for s,row in enumerate(joint) for y,p in enumerate(row) if p)
    assert isclose(target,predictive,rel_tol=0,abs_tol=2e-14)
    assert isclose(target,mi,rel_tol=0,abs_tol=2e-14)
    return {'target_entropy':entropy(ps),'predictive_entropy':entropy(py),'target_entropy_drop':target,'predictive_entropy_drop':predictive,'mutual_information':mi},ps,py,qsy


def main():
    count=0;worst=0
    base=[F(1,3),F(2,3)]
    for prior,a,b in product([F(1,4),F(1,2),F(3,4)],repeat=3):
        joint=[[(1-prior)*(1-a),(1-prior)*a],[prior*(1-b),prior*b]]
        m,ps,py,qsy=measures(joint)
        assert [sum((py[y]*qsy[y][s] for y in range(2)),F(0)) for s in range(2)]==ps
        change=sum(float(p)*kl(q,base) for p,q in zip(py,qsy))-kl(ps,base)
        assert isclose(change,m['mutual_information'],rel_tol=0,abs_tol=2e-14)
        worst=max(worst,abs(change-m['mutual_information']))
        count+=1
    assert count==27
    independent4=[[F(1,8)]*4 for _ in range(2)]
    informative2=[[F(1,2),F(0)],[F(0),F(1,2)]]
    a=measures(independent4)[0];b=measures(informative2)[0]
    assert a['predictive_entropy']>b['predictive_entropy']
    assert a['mutual_information']==0 and isclose(b['mutual_information'],log(2),rel_tol=0,abs_tol=2e-14)
    # Hyperparameter average is conditional MI, not in general marginal MI.
    conditional=[[[F(1,2),F(0)],[F(0),F(1,2)]],[[F(0),F(1,2)],[F(1,2),F(0)]]]
    avg=sum(measures(j)[0]['mutual_information']/2 for j in conditional)
    marginal=[[sum((j[s][y] for j in conditional),F(0))/2 for y in range(2)] for s in range(2)]
    marginal_mi=measures(marginal)[0]['mutual_information']
    assert isclose(avg,log(2),rel_tol=0,abs_tol=2e-14) and marginal_mi==0
    # Fixed off-diagonal values drawn from a negative-definite sample Hessian
    # do not make arbitrary subsequently negative diagonal values sufficient.
    sampled=[[-F(3),F(2)],[F(2),-F(3)]]
    allowed=[[-F(1),F(2)],[F(2),-F(1)]]
    sample_det=sampled[0][0]*sampled[1][1]-sampled[0][1]**2
    allowed_det=allowed[0][0]*allowed[1][1]-allowed[0][1]**2
    assert sample_det==5 and allowed_det==-3
    # Supplement B.1/B.3 says K and Kdag use [z;c]. For diagonal K with
    # z=(z1,z2), c=(c1,c2), site variances (1,1), choose f=z1.
    # The integral definition gives mean 4, variance 2/3. Using the printed
    # [c;mtilde] and W=diag(0,Vtilde) without reordering K gives 9,0.
    kvals=[F(2),F(3),F(5),F(7)]
    correct_values=[F(6),F(12),F(9),F(10)]
    printed_values=[F(9),F(10),F(6),F(12)]
    correct_noise=[F(1),F(1),F(0),F(0)]
    printed_noise=[F(0),F(0),F(1),F(1)]
    def first_posterior(values,noises):
        return [2*values[0]/(kvals[0]+noises[0]),F(2)-F(4)/(kvals[0]+noises[0])]
    correct=first_posterior(correct_values,correct_noise)
    literal=first_posterior(printed_values,printed_noise)
    assert correct==[F(4),F(2,3)] and literal==[F(9),F(0)]
    # Kernel averaging and posterior conditioning do not commute.
    conditional_variances=[v/(v+1) for v in [F(1),F(3)]]
    mean_variance=sum(conditional_variances)/2
    averaged_kernel_variance=F(2,3)
    assert mean_variance==F(5,8) and mean_variance!=averaged_kernel_variance
    # A compact-domain maximum can be at a boundary without zero gradient.
    values=[F(0),F(1,2),F(1)]
    assert max(values)==1
    result={
        'role':'Supporting curator boundary algebra, not an independent scientific review.',
        'probability_grid':{'positive_binary_channels':count,'exact_posterior_martingale':True,'entropy_and_kl_identity_tolerance':2e-14,'max_observed_kl_difference':worst},
        'predictive_entropy_is_not_information':{'uninformative_four_outcomes':a,'informative_binary_outcomes':b,'scope':'Finite probability example, not a PES surrogate run.'},
        'hyperparameter_marginalization':{'construction':'Psi and S independent fair bits, Y=S xor Psi.','mean_conditional_mi_nats':avg,'marginal_mi_nats':marginal_mi,'scope':'Demonstrates a general distinction between averaging conditional acquisitions and mutual information under a marginalized model; not a claim about a particular PES experiment.'},
        'hessian_negative_control':{'sampled_negative_definite':sampled,'permitted_after_negative_diagonal_only_constraints':allowed,'determinants':[sample_det,allowed_det],'eigenvalues_sampled':[-1,-5],'eigenvalues_permitted':[1,-3]},
        'supplement_block_order':{'declared_order':['z1','z2','c1','c2'],'K_diagonal':kvals,'prediction':'f=z1','correct_site_order_values':correct_values,'printed_order_values':printed_values,'correct_mean_variance':correct,'literal_printed_mean_variance':literal,'scope':'Generic Gaussian block calculation; K and Kdag kept in their stated [z;c] order. Reordering every object consistently resolves the notation problem.'},
        'kernel_average_boundary':{'random_scalar_kernel_values':[F(1),F(3)],'noise_variance':1,'average_conditional_posterior_variance':mean_variance,'posterior_variance_at_average_kernel':averaged_kernel_variance,'scope':'Generic covariance example. Unbiased feature inner products do not make finite-feature posterior inference exact.'},
        'boundary_optimizer':{'function':'f(x)=x on [0,1]','maximizer':1,'derivative_at_maximizer':1,'scope':'Logical domain boundary example, not a sampled stationary GP trajectory.'},
        'limits':['No universal accuracy, convergence, runtime or regret guarantee.','No author code or EP/GP implementation was executed.','No claim that the displayed ES innovation/Taylor notation has been fully repaired or numerically reproduced.']}
    def serial(v):
        if isinstance(v,F):return str(v)
        if isinstance(v,dict):return {k:serial(w) for k,w in v.items()}
        if isinstance(v,list):return [serial(w) for w in v]
        return v
    print(json.dumps(serial(result),indent=2,sort_keys=True))


if __name__=='__main__':
    main()
