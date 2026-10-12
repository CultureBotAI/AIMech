"""Curator fixed-parameter Gaussian-input calculations, not empirical replication."""
import json
import math


def kernel(a,b):
    return math.exp(-0.5*(a-b)**2)


def moments(mu, variance, points):
    q=[math.exp(-(mu-a)**2/(2*(1+variance)))/math.sqrt(1+variance) for a in points]
    Q=[[math.exp(-(a-b)**2/4-(mu-(a+b)/2)**2/(1+2*variance))/math.sqrt(1+2*variance)
        for b in points] for a in points]
    return q,Q


def integrate_normal(fn, mu, variance, intervals=20000):
    """Independent Simpson quadrature on [-10,10] standard deviations."""
    assert intervals%2==0 and variance>0
    h=20/intervals
    def g(z):return fn(mu+math.sqrt(variance)*z)*math.exp(-z*z/2)/math.sqrt(2*math.pi)
    total=g(-10)+g(10)
    for i in range(1,intervals):total+=(4 if i%2 else 2)*g(-10+i*h)
    return total*h/3


def calculate():
    mu=.4;s=.7;points=[-1.,1.]
    q,Q=moments(mu,s,points)
    q_num=[integrate_normal(lambda x:kernel(x,a),mu,s) for a in points]
    Q_num=[[integrate_normal(lambda x:kernel(x,a)*kernel(x,b),mu,s) for b in points] for a in points]
    error=max([abs(x-y) for x,y in zip(q,q_num)]+[abs(Q[i][j]-Q_num[i][j]) for i in range(2) for j in range(2)])
    assert error<1e-10
    q0,Q0=moments(mu,0.,points)
    assert all(math.isclose(q0[i],kernel(mu,points[i])) for i in range(2))
    assert all(math.isclose(Q0[i][j],q0[i]*q0[j]) for i in range(2) for j in range(2))
    # A unit GP conditioned on f(0)=0, evaluated at independent X~N(0,1).
    # Its mixture is zero-mean with random conditional variance 1-exp(-X^2).
    v=1-1/math.sqrt(3)
    fourth=3*(1-2/math.sqrt(3)+1/math.sqrt(5))
    gaussian_fourth=3*v*v
    assert fourth>gaussian_fourth
    # One exact observation f(2)=0; mean remains zero. Uncertain test input
    # can LOWER variance relative to evaluating only at its mean zero.
    point_v=1-math.exp(-4)
    input_v=1-math.exp(-4/3)/math.sqrt(3)
    assert input_v<point_v
    # First-order mean / second-order variance Taylor approximation for
    # f(0)=0, expansion at x=1: s2=1-exp(-x^2), s2''(1)=-2/e.
    # At Var(X)=2, approximate variance=1-3/e is negative.
    taylor_v=1-3/math.e
    exact_v=1-math.exp(-1/5)/math.sqrt(5)
    assert taylor_v<0<exact_v
    # f(x)=A*x, A~N(0,1), x0=1. A shared GP sample gives x2=A^2.
    # Fresh independent A1,A2 gives x2=A2*A1 and a different law.
    shared=dict(mean=1,variance=2)
    independent=dict(mean=0,variance=1)
    return dict(scope='Analytic and quadrature curator illustrations, not fitted source models or benchmark replication.',
        rbf_kernel_moments=dict(input_mean=mu,input_variance=s,training_locations=points,q=q,Q=Q,maximum_quadrature_error=error),
        zero_input_variance=dict(q=q0,Q=Q0),
        non_gaussian_mixture=dict(variance=v,fourth_moment=fourth,matched_gaussian_fourth_moment=gaussian_fourth),
        variance_need_not_increase=dict(value_only_at_mean=point_v,integrated_input=input_v),
        taylor_invalid_variance=dict(input_mean=1,input_variance=2,taylor_variance=taylor_v,exact_mixture_variance=exact_v),
        shared_function_dependence=dict(shared_coefficient_second_step=shared,independent_redraw_second_step=independent),
        limits=['The q/Q check uses the one-dimensional unit squared-exponential kernel and fixed Gaussian input parameters.',
                'The linear-kernel shared-function example illustrates an additional dependence assumption, not a numerical reproduction of the squared-exponential benchmark.',
                'Gaussian matching preserves the first two moments under its stated mixture law, not the entire distribution or arbitrary multistep dependence.',
                'Taylor negativity is a deliberately nonlocal example and does not refute the small-uncertainty approximation within its regime.'])


if __name__=='__main__':
    print(json.dumps(calculate(),indent=2))
