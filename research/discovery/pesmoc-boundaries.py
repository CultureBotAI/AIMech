"""Original bounded PESMOC checks, standard library only, deterministic stdout.

Written from finite Pareto/feasibility definitions and Gaussian identities after
reading Garrido-Merchan/Hernandez-Lobato 2016v2 and 2019 main/supplement.
No author code is imported or executed. Exact discrete probabilities and matrix
arithmetic use Fraction; logarithms and Gaussian constants use binary64 with
rel_tol=0 and abs_tol=2e-14 for stated equality checks. These checks are not an
implementation, convergence proof, benchmark, or independent scientific review.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product, combinations
import json
import math

TOL = 2e-14

def close(a, b):
    assert math.isclose(a, b, rel_tol=0, abs_tol=TOL), (a, b)

def feasible(c):
    return all(x >= 0 for x in c)

def dominates(a, b):
    return all(x <= y for x, y in zip(a, b)) and any(x < y for x, y in zip(a, b))

def pareto(f, c):
    return tuple(i for i in range(len(f)) if feasible(c[i]) and not any(
        feasible(c[j]) and dominates(f[j], f[i]) for j in range(len(f))))

def omega(star, other, other_c):
    # Main 2019 Eq9/10, including its zero/equality convention.
    return int(not (feasible(other_c) and all(a >= b for a, b in zip(star, other))))

def factor_product(f, c, chosen, self_pairs=True, weak_dominance=False):
    if not all(feasible(c[i]) for i in chosen):
        return 0
    return int(all((not feasible(c[j]) or not dominates(f[j], f[i])) if weak_dominance
                   else omega(f[i], f[j], c[j])
                   for i in chosen for j in range(len(f)) if self_pairs or j != i))

def entropy(values):
    n=len(values)
    return -sum(float(F(v,n))*math.log2(float(F(v,n))) for v in Counter(values).values())

def mi(a, b):
    return entropy(a)+entropy(b)-entropy(list(zip(a,b)))

def check_finite_factors():
    pair_count=ties_rejected=0
    for a in product([-1,0,1],repeat=2):
        for b in product([-1,0,1],repeat=2):
            for c in product([-1,0,1],repeat=2):
                pair_count+=1
                literal=omega(a,b,c)
                membership=int(not feasible(c) or not dominates(b,a))
                if a==b and feasible(c):
                    assert literal==0 and membership==1
                    ties_rejected+=1
                else:assert literal==membership
    counts=Counter()
    for flat in product([0,1],repeat=6):
        f=[flat[2*i:2*i+2] for i in range(3)]
        for mask in product([-1,1],repeat=3):
            c=[(v,) for v in mask];actual=pareto(f,c);counts['targets']+=1
            for bits in product([0,1],repeat=3):
                chosen=tuple(i for i,b in enumerate(bits) if b);counts['candidate_sets']+=1
                lit=factor_product(f,c,chosen)
                assert lit==int(not chosen)
                if bool(lit)!=(chosen==actual):counts['literal_equality_mismatches']+=1
                member=factor_product(f,c,chosen,self_pairs=False,weak_dominance=True)
                assert bool(member)==set(chosen).issubset(actual)
                if member:
                    counts['membership_accepts']+=1
                    if chosen!=actual:counts['membership_accepts_incomplete_sets']+=1
            if actual and not factor_product(f,c,actual,self_pairs=False):
                counts['true_pareto_rejected_after_self_exclusion_due_to_ties']+=1
    assert pair_count==729 and counts['targets']==512 and counts['candidate_sets']==4096
    # Change only competitor constraint: exact factor must change; star-only site cannot encode it.
    assert omega((0,0),(-1,-1),(-1,))==1
    assert omega((0,0),(-1,-1),(1,))==0
    return dict(pair_checks=pair_count,tie_cases_rejected_by_literal_factor=ties_rejected,
                **counts,wrong_constraint_location_witness={'star_f':[0,0],'star_c':1,
                'competitor_f':[-1,-1],'competitor_c_values':[-1,1],'omega':[1,0]},
                limits='Finite exhaustive checks do not normalize a continuum random-set law; explicit self exclusion and tie handling still do not enforce set completeness.')

def check_information():
    rows=[]
    for b1,b2,g in product([-1,1],repeat=3):
        s=pareto([(0,0),(b1,b2)],[(1,),(g,)])
        rows.append((b1,b2,g,s))
    s=[r[3] for r in rows];tasks=[[r[i] for r in rows] for i in range(3)]
    joint=mi(s,[r[:3] for r in rows]);parts=[mi(s,x) for x in tasks]
    close(joint,entropy(s));assert joint>sum(parts)>0
    assert Counter(s)==Counter({(0,):5,(1,):1,(0,1):2})
    # Fixed A feasible ensures no empty-set ambiguity in this MI counterexample.
    selected=[r for r in rows if 0 in r[3]]
    means=[sum(F(r[i],len(selected)) for r in selected) for i in range(3)]
    cov_b1_g=sum(F(r[0]*r[2],len(selected)) for r in selected)-means[0]*means[2]
    assert len(selected)==7 and cov_b1_g==F(8,49)
    # Opposing objectives: constraints alter target; unconstrained Pareto remains A,B.
    assert pareto([(0,1),(1,0)],[(1,),(-1,)])==(0,)
    assert pareto([(0,1),(1,0)],[(1,),(1,)])==(0,1)
    return {'states':8,'pareto_probabilities':{'A':'5/8','B':'1/8','A,B':'1/4'},
            'joint_information_bits':joint,'individual_information_bits':parts,
            'sum_individual_information_bits':sum(parts),
            'conditional_B1_constraint_covariance_given_A_is_member':str(cov_b1_g),
            'limits':'Finite channel is an exact counterexample to universal task additivity, not a GP/PESMOC performance calculation.'}

def check_gaussian_factors():
    phi=1/math.sqrt(2*math.pi)
    # Independent standard-normal difference variables D1,D2 and constraint G.
    # E excludes the positive orthant: not(G>=0 and D1>=0 and D2>=0).
    z=F(7,8);mean=-float(F(2,7))*phi
    second_cross=-float(F(4,7))*phi**2
    covariance=second_cross-mean**2
    close(covariance,-16/(49*math.pi))
    # Main Psi uses D=f(star)-f(other). Supplement Eq30 uses opposite sign
    # for its stated observation-first pair, without the implementation's minimization sign.
    cdf=lambda t:(1+math.erf(t/math.sqrt(2)))/2
    correct_z=1-0.5*cdf(1)**2;reversed_z=1-0.5*cdf(-1)**2
    assert correct_z<reversed_z
    # Phi at N(0,1), conditioned nonnegative: curvature=-2/pi, not Eq22 zero.
    correct_h=-2/math.pi;printed_h=-phi/0.5*0*phi/0.5
    assert printed_h==0 and correct_h<0
    close(1+correct_h,1-2/math.pi)
    return {'orthant_event_probability':str(z),'conditional_mean_each':mean,
            'conditional_variance_each':1-mean**2,'conditional_cross_covariance':covariance,
            'nonzero_objective_constraint_correlation':True,
            'omega_normalizer_D_mean1_variance1_constraint_mean0_variance1':correct_z,
            'supplement_reversed_difference_normalizer':reversed_z,
            'phi_correct_log_normalizer_second_derivative_at_zero':correct_h,
            'phi_printed_Eq22_second_derivative_at_zero':printed_h,
            'phi_correct_conditioned_variance':1-2/math.pi,
            'limits':'Analytic Gaussian moments, evaluated in binary64; no EP loop or source implementation is executed.'}

def check_precision_and_entropy():
    h=[[F(-1,8),F(1,8)],[F(1,8),F(-1,8)]]
    det=lambda a:a[0][0]*a[1][1]-a[0][1]*a[1][0]
    assert det(h)==0
    ip=[[F(int(i==j))+h[i][j] for j in range(2)] for i in range(2)]
    assert det(ip)==F(3,4)
    prior=[F(4),F(9),F(1)];noise=[F(1),F(4),F(1)]
    cond=[[F(1),F(4),F(1,2)],[F(2),F(3),F(1,4)]]
    parts=[0.5*(math.log(float(prior[t]+noise[t]))-
             sum(math.log(float(v[t]+noise[t])) for v in cond)/len(cond)) for t in range(3)]
    correct=sum(parts);printed_Eq15=2*correct
    mixed_Eq7=sum(parts[:2])+2*parts[2]
    assert correct<mixed_Eq7<printed_Eq15
    # Zero-site precision construction must preserve prior variance.
    v=F(4);correct_zero=1/(1/v);printed_zero=1/v
    assert correct_zero==4 and printed_zero==F(1,4)
    # Per-constraint 95% probability is not joint 95%, even under independence.
    joint_feasible=F(19,20)**2;assert joint_feasible<F(19,20)
    return {'singular_difference_hessian_determinant':str(det(h)),
            'identity_plus_hessian_determinant':str(det(ip)),
            'zero_site_expected_variance':str(correct_zero),
            'literal_variance_as_precision_inverse':str(printed_zero),
            'gaussian_entropy_components_nats':parts,'correct_gaussian_score_nats':correct,
            'printed_Eq15_common_double_scale':printed_Eq15,
            'Eq7_mixed_coefficients_score_nats':mixed_Eq7,
            'two_independent_95_percent_constraints_joint_probability':str(joint_feasible),
            'limits':'The common missing 1/2 preserves uncosted rankings; inconsistent task weights need not. Singular inverses and covariance/precision substitutions are source caveats, not a repaired full algorithm.'}

def main():
    out={'scope':'Original bounded supporting math; no independent approval or implementation benchmark.',
         'numeric_tolerance':{'rel_tol':0,'abs_tol':TOL},
         'finite_feasibility_and_pareto_factors':check_finite_factors(),
         'feasible_pareto_information':check_information(),
         'gaussian_factor_boundaries':check_gaussian_factors(),
         'precision_and_entropy_boundaries':check_precision_and_entropy()}
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':main()
