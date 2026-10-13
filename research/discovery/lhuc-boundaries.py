"""Constructed LHUC and SAT-LHUC boundary checks, not author software."""
import json,math


def sigmoid(x):return 1/(1+math.exp(-x))


def result():
    basis=[.2,.8];out=[1.3,-.7];r=[.1,-.2];target=1
    def loss(theta):
        logit=sum(v*h*math.exp(t) for v,h,t in zip(out,basis,theta))+.3
        return math.log1p(math.exp(logit))-target*logit
    z=sum(v*h*math.exp(t) for v,h,t in zip(out,basis,r))+.3
    delta=sigmoid(z)-target
    grad=[delta*v*h*math.exp(t) for v,h,t in zip(out,basis,r)]
    eps=1e-5;fd=[]
    for j in range(2):
        a,b=r[:],r[:];a[j]+=eps;b[j]-=eps
        fd.append((loss(a)-loss(b))/(2*eps))
    assert all(math.isclose(a,b,abs_tol=1e-10) for a,b in zip(grad,fd))
    # A fixed constant basis cannot approximate both target values, regardless of scaling.
    constant_basis=[1.,1.]
    predictions=[sum(a*h for a,h in zip([2.,3.],constant_basis))]*2
    assert predictions[0]==predictions[1] and [0.,1.][0]!=[0.,1.][1]
    # Fixed downstream weights do not make a deep hidden output input-independent of lower scaling.
    downstream_before=sigmoid(.4*.2+.7*.8)
    downstream_after=sigmoid(.4*(2*.2)+.7*.8)
    assert downstream_before!=downstream_after
    # Gamma selects SI (index0) or the current speaker (index1), not another speaker(index2).
    gamma=.6;si_loss,sd_loss=2.,1.
    expected=gamma*si_loss+(1-gamma)*sd_loss
    assert math.isclose(expected,1.6)
    selected=[0,1,1];per_example=[.3,-.2,.4];by_transform=[sum(g for k,g in zip(selected,per_example) if k==j) for j in range(3)]
    assert by_transform==[.3,.2,0]
    # Eq10 interpolates transformed amplitudes, not latent log amplitudes.
    alpha=.5;a,b=0.,math.log(4)
    amplitude_mix=alpha*math.exp(a)+(1-alpha)*math.exp(b)
    latent_mix=math.exp(alpha*a+(1-alpha)*b)
    assert amplitude_mix==2.5 and latent_mix==2 and amplitude_mix!=latent_mix
    return dict(lhuc_gradient=grad,finite_difference=fd,constant_basis_predictions=predictions,
                lower_scaling_changes_deep_activation=[downstream_before,downstream_after],
                si_probability=gamma,expected_selected_objective=expected,routed_transform_gradients=by_transform,
                interpolated_amplitudes=amplitude_mix,exponentiated_interpolated_latents=latent_mix)


if __name__=='__main__':print(json.dumps(result(),indent=2,sort_keys=True))
