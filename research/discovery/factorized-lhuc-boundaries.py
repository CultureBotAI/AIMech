"""Constructed factorized-LHUC amplitude checks; not acoustic evaluation."""
import json,math


def result():
    speaker,environment=0.,math.log(4)
    alpha=.5
    amplitude=alpha*math.exp(speaker)+(1-alpha)*math.exp(environment)
    latent=math.exp(alpha*speaker+(1-alpha)*environment)
    assert amplitude==2.5 and latent==2 and amplitude!=latent
    recovered=math.exp(math.log(amplitude));assert math.isclose(recovered,amplitude)
    def combine(a):return a*math.exp(speaker)+(1-a)*math.exp(environment)
    assert combine(0)==4 and combine(1)==1
    eps=1e-5;finite=(combine(alpha+eps)-combine(alpha-eps))/(2*eps)
    derivative=math.exp(speaker)-math.exp(environment)
    assert math.isclose(finite,derivative,abs_tol=1e-10)
    return dict(amplitude_interpolation=amplitude,latent_interpolation_then_exp=latent,
                inverse_representation_recovers_amplitude=recovered,endpoints=[combine(0),combine(1)],
                alpha_derivative=derivative,finite_difference=finite)


if __name__=='__main__':print(json.dumps(result(),indent=2,sort_keys=True))
