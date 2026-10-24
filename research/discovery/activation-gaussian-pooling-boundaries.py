"""Constructed input-value Gaussian pooling examples; no author implementation."""
import math,json


def pool(z,mu,beta):
    scores=[-.5*beta*(x-mu)**2 for x in z]
    m=max(scores)
    weights=[math.exp(s-m) for s in scores]
    weights=[w/sum(weights) for w in weights]
    return sum(w*x for w,x in zip(weights,z)),weights


def result():
    z,mu,beta=[0.0,1.0],0.0,10.0
    f,u=pool(z,mu,beta)
    dz=[w*(1-beta*(x-mu)*(x-f)) for w,x in zip(u,z)]
    dmu=beta*sum(w*(x-f)**2 for w,x in zip(u,z))
    sqmean=sum(w*(x-mu)**2 for w,x in zip(u,z))
    dbeta=-.5*sum(w*(x-f)*((x-mu)**2-sqmean) for w,x in zip(u,z))
    eps=1e-5
    fd=[]
    for j in range(2):
        plus,minus=z[:],z[:]
        plus[j]+=eps;minus[j]-=eps
        fd.append((pool(plus,mu,beta)[0]-pool(minus,mu,beta)[0])/(2*eps))
    fdmu=(pool(z,mu+eps,beta)[0]-pool(z,mu-eps,beta)[0])/(2*eps)
    fdbeta=(pool(z,mu,beta+eps)[0]-pool(z,mu,beta-eps)[0])/(2*eps)
    assert all(math.isclose(a,b,abs_tol=1e-9) for a,b in zip(dz+[dmu,dbeta],fd+[fdmu,fdbeta]))
    assert dz[1]<0 and min(z)<=f<=max(z)
    sharp,_=pool([0,2],.1,100)
    assert sharp<1e-20 and sharp!=2
    zero,_=pool([1,3,8],0,0)
    assert zero==4
    base,_=pool([0,1],0,1);doubled,_=pool([0,2],0,1)
    assert not math.isclose(doubled,2*base)
    a=[.2,.8];original,_=pool(a,.5,10);scaled,_=pool([2*x for x in a],.5,10)
    assert not math.isclose(scaled,2*original)
    # The normalized power mean includes log(S/K) in its order derivative.
    values,p=[1.,3.],2.
    def lp(order,normalized):return (sum(x**order for x in values)/(len(values) if normalized else 1))**(1/order)
    total=sum(x**p for x in values);logsum=sum(x**p*math.log(x) for x in values)
    actual=lp(p,True)*(logsum/(p*total)-math.log(total/len(values))/p**2)
    printed_with_normalized_forward=lp(p,True)*(logsum/(p*total)-math.log(total)/p**2)
    numeric=(lp(p+eps,True)-lp(p-eps,True))/(2*eps)
    assert math.isclose(actual,numeric,abs_tol=1e-9) and not math.isclose(actual,printed_with_normalized_forward)
    return dict(input_gradient=dz,input_finite_difference=fd,mean_gradient=dmu,mean_finite_difference=fdmu,
                precision_gradient=dbeta,precision_finite_difference=fdbeta,
                sharp_nearest_value=sharp,maximum_value=2,zero_precision_average=zero,
                nonlinear_without_tanh=[base,doubled,2*base],inside_vs_after_pool_scaling=[scaled,2*original],
                normalized_power_order_derivative=actual,finite_difference_power_order=numeric,
                printed_order_derivative_with_normalized_forward=printed_with_normalized_forward)


if __name__=='__main__':print(json.dumps(result(),indent=2,sort_keys=True))
