"""Constructed Gaussian contrast checks, not source fitting or calibration."""
import json
import math


def matvec(a,x):
    return [sum(v*w for v,w in zip(row,x)) for row in a]


def dot(x,y):
    return sum(v*w for v,w in zip(x,y))


def simpson(fn,a,b,n):
    h=(b-a)/n
    return h/3*(fn(a)+fn(b)+sum((4 if i%2 else 2)*fn(a+i*h) for i in range(1,n)))


def experiment():
    k=[[1,-1,0],[1,0,-1],[0,1,-1]]
    s=[[dot(a,b) for b in k] for a in k]
    m=matvec(k,[2,0,-1]);null=[1,-1,1]
    assert m==[2,3,1] and matvec(s,null)==[0,0,0] and dot(m,null)==0
    pinv=[[v/9 for v in row] for row in s]
    wald=dot(m,matvec(pinv,m));assert abs(wald-14/3)<1e-14
    outside=[v+w for v,w in zip(m,null)]
    assert dot(outside,null)==3
    assert abs(dot(outside,matvec(pinv,outside))-wald)<1e-14
    # Three pairwise standardized differences of independent N(0,1) copies.
    # Their maximum absolute value is the range divided by sqrt(2).
    phi=lambda x:math.exp(-x*x/2)/math.sqrt(2*math.pi)
    cdf=lambda x:.5*math.erfc(-x/math.sqrt(2))
    def box(c,n):
        width=c*math.sqrt(2)
        return 3*simpson(lambda x:phi(x)*(cdf(x+width)-cdf(x))**2,-10,10,n)
    t=[v/math.sqrt(2) for v in m]
    coarse=[1-box(abs(v),8192) for v in t]
    fine=[1-box(abs(v),16384) for v in t]
    raw=[math.erfc(abs(v)/math.sqrt(2)) for v in t]
    assert max(abs(a-b) for a,b in zip(coarse,fine))<1e-11
    assert all(a>=p for a,p in zip(fine,raw))
    # Normal tails outside the integration interval contribute < 3e-22
    # since the omitted integrand is at most 3*phi(x).
    omitted_bound=3*math.erfc(10/math.sqrt(2))
    p=.05
    return dict(limits='Known constructed Gaussian law only; no author software, original model fitting, empirical repeated-data calibration or general Bayesian familywise-control guarantee.',
        redundant_contrasts=dict(matrix=k,mean=m,covariance=s,rank=2,null_constraint=null,pseudoinverse=pinv,wald=wald,chi_square_rank_tail=math.exp(-wald/2),outside_support_mean=outside,outside_support_wald_unchanged=True,interpretation='A pseudoinverse discards nullspace displacement. Verify that the null belongs to the posterior affine support before treating its Wald value as an equality assessment.'),
        max_absolute=dict(standardized_means=t,raw_normal_two_sided=raw,single_step_adjusted=fine,global_max_tail=min(fine),refinement_error=max(abs(a-b) for a,b in zip(coarse,fine)),omitted_integral_bound=omitted_bound,reference='Maximum absolute pairwise standardized differences equals the range of three independent standard normal variables divided by sqrt(2).'),
        correlation_effect=dict(raw_marginal_tail=p,two_independent_adjusted=1-(1-p)**2,two_identical_adjusted=p),
        density_double_tail_error=dict(centered_normal_density_level_score=1,incorrect_second_two_tail_transform=0))


if __name__=='__main__':
    print(json.dumps(experiment(),indent=2,sort_keys=True))
