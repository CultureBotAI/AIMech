"""Exact constructed Gaussian examples; no fitted source model or package run."""
import json
from math import erf,erfc,exp,isclose,sqrt
from statistics import NormalDist


def result():
    normal=NormalDist();alpha=.05;t=[2.,1.]
    raw=[erfc(abs(x)/sqrt(2)) for x in t]
    # Two independent standard normals; max absolute joint rectangle mass.
    adjusted=[1-erf(abs(x)/sqrt(2))**2 for x in t]
    global_p=1-erf(max(map(abs,t))/sqrt(2))**2
    q=normal.inv_cdf((1+sqrt(1-alpha))/2)
    assert all(a>=r for a,r in zip(adjusted,raw))
    assert isclose(erf(q/sqrt(2))**2,1-alpha)
    # Duplicate or sign-reversed coordinates have rank-one correlation;
    # max(|Z|,|Z|)=|Z|, so counting two independent tests is wrong.
    duplicate_q=normal.inv_cdf(1-alpha/2)
    duplicate_p=erfc(2/sqrt(2))
    assert duplicate_q<q and duplicate_p<global_p
    # The distinct quadratic global reference is chi-square_2 at 2^2+1^2.
    wald_p=exp(-sum(x*x for x in t)/2)
    assert not isclose(global_p,wald_p)
    return dict(observed_statistics=t,marginal_two_sided_tails=raw,
                independent_two_test_adjusted_tails=adjusted,
                independent_two_test_global_tail=global_p,
                independent_two_test_critical_value=q,
                simultaneous_coverage=erf(q/sqrt(2))**2,
                unadjusted_two_test_familywise_error=1-(1-alpha)**2,
                duplicate_or_sign_reversed_global_tail=duplicate_p,
                duplicate_or_sign_reversed_critical_value=duplicate_q,
                wald_chisquare2_tail=wald_p,
                interpretation='Exact distribution calculations for constructed known-covariance Gaussian laws; not empirical calibration or source data reproduction.')


if __name__=='__main__':print(json.dumps(result(),indent=2))
