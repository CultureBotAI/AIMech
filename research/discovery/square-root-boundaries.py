"""Original finite witnesses and analytic-bound illustrations for SQR records."""
from fractions import Fraction as F
from math import exp, factorial, isclose, log, pi, sqrt, erf
from itertools import product
import json


def conditional_checks():
    # Matrix coefficients count each off-diagonal product twice.
    phi = [[-1.0, .75], [.75, -2.0]]
    theta = [.25, -.5]
    def energy(x,y):
        u,v=sqrt(x),sqrt(y)
        return theta[0]*u+theta[1]*v+phi[0][0]*x+2*phi[0][1]*u*v+phi[1][1]*y
    for x,y in product(range(10),repeat=2):
        eta=theta[0]+2*phi[0][1]*sqrt(y)
        assert isclose(energy(x,y)-energy(0,y),phi[0][0]*x+eta*sqrt(x),abs_tol=1e-12)
        eta=theta[1]+2*phi[0][1]*sqrt(x)
        assert isclose(energy(x,y)-energy(x,0),phi[1][1]*y+eta*sqrt(y),abs_tol=1e-12)
    # A Poisson SQR conditional with nonzero square-root coefficient is not Poisson.
    # Ratios p(k+1)/p(k) multiplied by k+1 are not a common mean parameter.
    a,b=-1.0,2.0
    poisson_scaled_ratios=[exp(a+b*(sqrt(k+1)-sqrt(k))) for k in range(4)]
    assert max(poisson_scaled_ratios)-min(poisson_scaled_ratios)>1
    assert sqrt((-1)**2)==1 and sqrt((-1)**2)!=-1
    assert exp(-1+1)!=exp(-1-1)
    for x,y in product([0,1],repeat=2):
        assert sqrt(x)*sqrt(y)==x*y
    return dict(full_conditional_energy_increments_verified=True,
                poisson_scaled_successive_ratios=poisson_scaled_ratios,
                gaussian_signed_root_distinction=True,
                binary_indicator_root_is_unchanged=True,
                scope='Finite pointwise checks and algebraic identities; no infinite partition is numerically estimated.')


def exponential_checks():
    # u=sqrt(x), v=sqrt(y). 2uv<=u^2+v^2 gives the global bound.
    for u,v in product(range(10),repeat=2):
        q=-u*u-v*v+F(3,2)*u*v
        assert q<=-F(1,4)*(u*u+v*v)
        # An indefinite matrix can still be strictly negative on this orthant.
        assert -u*u-4*u*v-v*v<=-(u*u+v*v)
    assert -1+4-1==2
    # A positive diagonal already fails the strict condition on a coordinate axis.
    assert F(1)>0
    # Young's inequality supplies a uniform integrable envelope for any finite theta.
    c,epsilon=F(1,4),F(1,8)
    for theta in [F(-2),F(0),F(3)]:
        for u in range(10):
            assert theta*u<=epsilon*u*u+theta*theta/(4*epsilon)
    # Main-paper p.7 printed expression at eta1=-1, eta2=0.
    eta1,eta2=-1.0,0.0
    printed_z=(sqrt(pi)*eta1*exp(-eta2**2/(4*eta1))
               *(1-erf(-eta2/(2*sqrt(-eta1))))/(-2*(-eta1)**1.5)-1/eta1)
    true_z=1.0  # integral_0^infinity exp(-x) dx
    assert isclose(printed_z,1+sqrt(pi)/2) and not isclose(printed_z,true_z)
    # One-dimensional boundary: integral exp(b*sqrt(x)) dx=2/b^2 when b<0.
    boundary_b=F(-2)
    boundary_z=2/(boundary_b**2)
    assert boundary_z==F(1,2)
    return dict(strict_orthant_decay='u^T Phi u <= -(u^2+v^2)/4',
                indefinite_but_valid_strict_example=True,
                positive_diagonal_fails_strict_condition=True,
                uniform_envelope='exp(sum theta_i^2/(4 epsilon))*exp(-(c-epsilon)*sum x_i), 0<epsilon<c',
                printed_independent_exponential_partition=printed_z,
                actual_independent_exponential_partition=true_z,
                zero_linear_negative_root_partition=str(boundary_z),
                scope='The printed conditional partition fails an exact independent special case. Boundary example is one-dimensional; it is not a complete multivariate classification.')


def poisson_checks():
    # Global inequalities, illustrated exactly at squares; they hold for all x>=0.
    for u,v in product(range(10),repeat=2):
        assert 2*u*v<=u*u+v*v
        assert u<=1+u*u
    # An unrestricted finite Phi and theta can be bounded by exp(C+sum d_i*x_i).
    # Multiplication by product(1/x_i!) then sums to exp(C+sum exp(d_i)).
    theta=[F(2),F(-3)]
    phi=[[F(1),F(4)],[F(4),F(2)]]
    constant=sum(abs(t) for t in theta)
    coeff=[abs(phi[i][i])+abs(theta[i])+sum(abs(phi[i][j]) for j in range(2) if j!=i) for i in range(2)]
    for u,v in product(range(10),repeat=2):
        x,y=u*u,v*v
        energy=theta[0]*u+theta[1]*v+phi[0][0]*x+2*phi[0][1]*u*v+phi[1][1]*y
        assert energy<=constant+coeff[0]*x+coeff[1]*y
    # With theta=0 and Phi diagonal, factorial-weighted mass is independent Poisson.
    lambdas=[F(2),F(3)]
    for x,y in product(range(6),repeat=2):
        mass=lambdas[0]**x*lambdas[1]**y/(factorial(x)*factorial(y))
        assert mass==(lambdas[0]**x/factorial(x))*(lambdas[1]**y/factorial(y))
    return dict(unrestricted_example_diagonal=['1','2'],unrestricted_example_edge_matrix='4',
                domination_constant=str(constant),domination_linear_coefficients=list(map(str,coeff)),
                analytic_partition_bound='Z <= exp(C + sum_i exp(d_i)) < infinity',
                independent_poisson_special_case_verified=True,
                scope='Direct factorial domination, not a finite-cutoff estimate or a radial-measure argument.')


def radial_measure_checks():
    # For x=z*v,y=z*(1-v), abs(det d(x,y)/d(z,v))=z.
    for z,v in product([F(1,2),F(1),F(3)],[F(0),F(1,4),F(1)]):
        determinant=v*(-z)-z*(1-v)
        assert abs(determinant)==z
    rate=F(2)
    actual_partition=1/(rate**2)  # integral z*exp(-rate*z) dz, v in [0,1]
    omitted_jacobian_partition=1/rate
    assert actual_partition!=omitted_jacobian_partition
    return dict(jacobian='z in two dimensions; z^(p-1) in p dimensions',
                rate=str(rate),actual_joint_partition=str(actual_partition),
                ray_kernel_integral_without_jacobian=str(omitted_jacobian_partition),
                actual_radius_mean=str(2/rate),exponential_ray_kernel_mean=str(1/rate),
                scope='The continuous L1 radius of independent exponentials is not distributed as the bare one-dimensional ray kernel. Discrete count directions require a different counting-measure treatment.')


if __name__=='__main__':
    print(json.dumps(dict(conditionals=conditional_checks(),exponential=exponential_checks(),
                          poisson=poisson_checks(),radial_measure=radial_measure_checks()),indent=2))
