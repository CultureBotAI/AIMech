"""Curator Taylor-GP boundary examples; no training or empirical replication."""
import json
import math


def evaluate(mu, s, y=1.):
    """Unit squared-exponential GP conditioned on one exact f(0)=y."""
    k=math.exp(-mu*mu/2)
    mean=y*k
    mean_gradient=-mu*y*k
    latent_variance=1-k*k
    variance_hessian=(2-4*mu*mu)*k*k
    taylor_variance=latent_variance+.5*s*variance_hessian+s*mean_gradient**2
    q=math.exp(-mu*mu/(2*(1+s)))/math.sqrt(1+s)
    Q=math.exp(-mu*mu/(1+2*s))/math.sqrt(1+2*s)
    return dict(input_mean=mu,input_variance=s,exact_observation=y,
        taylor_mean=mean,exact_mean=y*q,
        taylor_variance=taylor_variance,exact_variance=1-Q+y*y*(Q-q*q),
        taylor_input_output_covariance=s*mean_gradient,
        exact_input_output_covariance=-y*mu*s*q/(1+s))


def calculate():
    zero=evaluate(.7,0.)
    assert math.isclose(zero['taylor_mean'],zero['exact_mean'])
    assert math.isclose(zero['taylor_variance'],zero['exact_variance'])
    local=[evaluate(0.,s) for s in [.1,.01,.001]]
    for r in local:
        s=r['input_variance']
        assert math.isclose(r['taylor_mean'],1.)
        assert math.isclose(r['taylor_variance'],s)
        assert math.isclose(r['exact_variance'],s/(1+s))
        r['mean_error_over_input_variance']=(r['taylor_mean']-r['exact_mean'])/s
    assert abs(local[-1]['mean_error_over_input_variance']-.5)<.001
    negative=evaluate(1.,2.,0.)
    assert negative['taylor_variance']<0<negative['exact_variance']
    covariance=evaluate(1.,.5,1.)
    assert not math.isclose(covariance['taylor_input_output_covariance'],covariance['exact_input_output_covariance'])
    return dict(scope='Fixed-parameter one-observation unit-kernel analytic checks, not source benchmark reproduction.',zero_input_variance=zero,local_curvature_examples=local,negative_variance_example=negative,cross_covariance_example=covariance,
        interpretation=['The first-order mean approximation omits an input-variance-order curvature correction, even when the input mean is at a stationary posterior mean.',
                        'Second-order expansion of conditional variance is not a claim of second-order accuracy for every predictive moment.',
                        'The variance can be negative for a deliberately nonlocal input law; do not silently treat an invalid covariance as a probability distribution.',
                        'Approximate input-output covariance is a local derivative formula, not an exact squared-exponential integral.',
                        'Zero input variance reproduces fixed-input moments.'])


if __name__=='__main__':
    print(json.dumps(calculate(),indent=2))
