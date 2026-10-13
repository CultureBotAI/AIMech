"""Constructed posterior-score examples, not source fitting or calibration."""
import json
import math


def simpson(fn, a, b, n):
    step=(b-a)/n
    return step/3*(fn(a)+fn(b)+sum((4 if i%2 else 2)*fn(a+i*step) for i in range(1,n)))


def experiment():
    # Independent standard Laplace coordinates have covariance 2I. Shift by
    # m=(1,0), so the null is one Euclidean unit from the posterior center.
    # Density contours are diamonds; Mahalanobis contours are circles.
    density_tail=2/math.e  # sum of two independent absolute Laplace values
    def inside_circle(theta):
        a=math.cos(theta)+math.sin(theta)
        return (1-(1+a)*math.exp(-a))/a**2
    radial_tail=1-simpson(inside_circle,0,math.pi/2,4096)
    radial_fine=1-simpson(inside_circle,0,math.pi/2,8192)
    assert abs(radial_fine-radial_tail)<1e-12
    assert radial_tail<density_tail
    a=(1.,0.);d=(1/math.sqrt(2),1/math.sqrt(2))
    assert abs(sum(v*v for v in a)-sum(v*v for v in d))<1e-14
    assert math.exp(-sum(map(abs,a)))>math.exp(-sum(map(abs,d)))

    # Scalar illustrative separator copies: theta_a~Exp(1), theta_b fixed at
    # log(2). Both differences below are continuous. Applying the same log
    # to both copies preserves their order, but changes density ordering.
    b=math.log(2)
    ordinary_density_tail=math.exp(-b)
    log_density_tail=(1-math.exp(-b))+math.exp(-2*b)
    assert abs(b*math.exp(-b)-2*b*math.exp(-2*b))<1e-15
    assert abs(ordinary_density_tail-.5)<1e-15
    assert abs(log_density_tail-.75)<1e-15
    equal_tail=2*min(1-math.exp(-b),math.exp(-b))
    assert equal_tail==1

    # Identical diffuse discrete posteriors need not have high equality mass.
    discrete_uniform_agreement=sum(.1*.1 for _ in range(10))
    assert abs(discrete_uniform_agreement-.1)<1e-15
    return dict(
        limits='Constructed score distributions only; no author code, MCMC, source model fit, empirical calibration or multiplicity guarantee.',
        nonelliptical_symmetric_unimodal=dict(distribution='Independent Laplace(0,1) coordinates shifted by (1,0)',covariance_diagonal=[2,2],null_mahalanobis=.5,density_level_tail=density_tail,empirical_radial_population_tail=radial_tail,quadrature_refinement_difference=abs(radial_tail-radial_fine),same_radius_points=[a,d],density_ratio=math.exp(math.sqrt(2)-1)),
        nonlinear_separator_scale=dict(a_distribution='Exp(1)',b_fixed=b,original_density_tail=ordinary_density_tail,log_scale_density_tail=log_density_tail,original_and_log_scale_equal_tail=equal_tail,assumption='The second copy is a point mass; this is an analytic illustration of score dependence on the common separator scale, not an empirical evidence split.'),
        discrete_agreement=dict(states=10,identical_uniform_mass=discrete_uniform_agreement,identical_point_mass=1),
    )


if __name__=='__main__':
    print(json.dumps(experiment(),indent=2,sort_keys=True))
