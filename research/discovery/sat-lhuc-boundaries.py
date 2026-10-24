"""Constructed SAT-LHUC routing boundaries; no author implementation or model fitting."""
import json,math


def loss(amplitude):return math.log1p(math.exp(-amplitude))


def result():
    gamma=.6;amplitudes=[.5,2.,3.]
    expected=gamma*loss(amplitudes[0])+(1-gamma)*loss(amplitudes[1])
    mixed_amplitude=gamma*amplitudes[0]+(1-gamma)*amplitudes[1]
    loss_of_mixture=loss(mixed_amplitude)
    assert not math.isclose(expected,loss_of_mixture,abs_tol=1e-6)
    selected=[0,1,1];incoming=[.3,-.2,.4]
    routed=[sum(g for k,g in zip(selected,incoming) if k==j) for j in range(3)]
    assert routed==[.3,.2,0]
    # A finite-difference gradient of the expected two-path objective is zero for unrelated speaker2.
    def objective(a):return gamma*loss(a[0])+(1-gamma)*loss(a[1])
    analytic=[-gamma/(1+math.exp(amplitudes[0])),-(1-gamma)/(1+math.exp(amplitudes[1])),0.]
    finite=[];eps=1e-5
    for j in range(3):
        a,b=amplitudes[:],amplitudes[:];a[j]+=eps;b[j]-=eps
        finite.append((objective(a)-objective(b))/(2*eps))
    assert all(math.isclose(a,b,abs_tol=1e-10) for a,b in zip(analytic,finite))
    return dict(si_probability=gamma,expected_path_loss=expected,loss_of_interpolated_amplitude=loss_of_mixture,
                selected_transform_gradient_sums=routed,expected_objective_gradient=analytic,finite_difference=finite)


if __name__=='__main__':print(json.dumps(result(),indent=2,sort_keys=True))
