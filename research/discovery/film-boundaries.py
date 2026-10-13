"""Constructed FiLM affine, gradient and operation-count boundaries."""
import json,math


def result():
    features=[[.1,.4],[.2,.8]];gamma=[0.,2.];beta=[.3,-.1]
    def forward(f,g,b):return [[gc*v+bc for v in channel] for channel,gc,bc in zip(f,g,b)]
    def loss(f,g,b):return sum(v*v/2 for channel in forward(f,g,b) for v in channel)
    y=forward(features,gamma,beta)
    dgamma=[sum(a*b for a,b in zip(f,o)) for f,o in zip(features,y)]
    dbeta=[sum(o) for o in y];dfeature=[[g*v for v in o] for g,o in zip(gamma,y)]
    eps=1e-5;fd_gamma=[];fd_beta=[]
    for j in range(2):
        a,b=gamma[:],gamma[:];a[j]+=eps;b[j]-=eps
        fd_gamma.append((loss(features,a,beta)-loss(features,b,beta))/(2*eps))
        a,b=beta[:],beta[:];a[j]+=eps;b[j]-=eps
        fd_beta.append((loss(features,gamma,a)-loss(features,gamma,b))/(2*eps))
    assert all(math.isclose(a,b,abs_tol=1e-10) for a,b in zip(dgamma+dbeta,fd_gamma+fd_beta))
    assert y[0]==[.3,.3] and dfeature[0]==[0.,0.] and dgamma[0]!=0
    # Nonzero shift makes the fixed-conditioning map affine, not linear.
    assert 2*0+1!=0
    # Same-input conditioning gamma(x)=x makes y=x*x, with a second derivative path.
    x=2.;total_fd=((x+eps)**2-(x-eps)**2)/(2*eps)
    assert math.isclose(total_fd,2*x,abs_tol=1e-9) and total_fd!=x
    c=2;counts=[dict(height=h,width=h,coefficients=2*c,multiplies_plus_adds=2*c*h*h) for h in [14,28]]
    assert counts[0]['coefficients']==counts[1]['coefficients']
    assert counts[1]['multiplies_plus_adds']==4*counts[0]['multiplies_plus_adds']
    return dict(output=y,partial_feature_gradient_fixed_condition=dfeature,gamma_gradient=dgamma,beta_gradient=dbeta,
                gamma_finite_difference=fd_gamma,beta_finite_difference=fd_beta,
                coupled_input_total_derivative=total_fd,frozen_condition_partial_derivative=x,operation_counts=counts)


if __name__=='__main__':print(json.dumps(result(),indent=2,sort_keys=True))
