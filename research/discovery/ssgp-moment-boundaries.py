"""Independent scalar Gaussian integrals for fixed Fourier-feature GP moments."""
import json
import math


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def quadratic(a, matrix, b):
    return sum(a[i]*matrix[i][j]*b[j] for i in range(2) for j in range(2))


def moments(mu, variance, omega):
    decay=math.exp(-.5*omega*omega*variance)
    q=[decay*math.cos(omega*mu),decay*math.sin(omega*mu)]
    c2=math.exp(-2*omega*omega*variance)*math.cos(2*omega*mu)
    s2=math.exp(-2*omega*omega*variance)*math.sin(2*omega*mu)
    psi=[[(1+c2)/2,s2/2],[s2/2,(1-c2)/2]]
    cross=[-variance*omega*q[1],variance*omega*q[0]]
    return q,psi,cross


def calculate():
    mu=.4;variance=.7;omega=1.3;alpha=[.8,-.6]
    weight_covariance=[[.4,.1],[.1,.2]];noise=.05
    q,psi,cross=moments(mu,variance,omega)
    mean=dot(alpha,q)
    total_variance=noise+sum(weight_covariance[i][j]*psi[i][j] for i in range(2) for j in range(2))+quadratic(alpha,psi,alpha)-mean*mean
    # Direct quadrature of the conditional first/second moments over X.
    n=20000;lo=mu-10*math.sqrt(variance);hi=mu+10*math.sqrt(variance);step=(hi-lo)/n
    acc=[0.]*9
    for i in range(n+1):
        x=lo+i*step;p=math.exp(-(x-mu)**2/(2*variance))/math.sqrt(2*math.pi*variance)
        phi=[math.cos(omega*x),math.sin(omega*x)]
        m=dot(alpha,phi);v=noise+quadratic(phi,weight_covariance,phi)
        values=[phi[0],phi[1],phi[0]**2,phi[0]*phi[1],phi[1]**2,(x-mu)*phi[0],(x-mu)*phi[1],m,v+m*m]
        w=1 if i in (0,n) else (4 if i%2 else 2)
        acc=[a+w*p*x for a,x in zip(acc,values)]
    numerical=[a*step/3 for a in acc]
    analytic=[*q,psi[0][0],psi[0][1],psi[1][1],*cross,mean,total_variance+mean*mean]
    error=max(abs(a-n) for a,n in zip(analytic,numerical));assert error<1e-11
    phi=[math.cos(omega*mu),math.sin(omega*mu)];dphi=[-omega*phi[1],omega*phi[0]]
    linear_mean=dot(alpha,phi);gradient=dot(alpha,dphi)
    linear_variance=noise+quadratic(phi,weight_covariance,phi)+variance*gradient*gradient
    linear_cross=variance*gradient
    q0,p0,c0=moments(mu,0.,omega)
    assert all(math.isclose(a,b) for a,b in zip(q0,phi))
    assert all(math.isclose(p0[i][j],phi[i]*phi[j],abs_tol=1e-15) for i in range(2) for j in range(2))
    assert c0==[0.,0.]
    # Pure uncertain cosine coefficient: mean zero, covariance at the input mean.
    s=2.;exact_cosine_variance=(1+math.exp(-2*s))/2
    frozen_variance=1.;variance_hessian=-2.;second_order_variance=1+.5*s*variance_hessian
    assert exact_cosine_variance>0 and frozen_variance>0 and second_order_variance<0
    # Deterministic cosine coefficient gives a bounded, non-Gaussian output.
    cosine_mean=math.exp(-.5);cosine_variance=(1+math.exp(-2))/2-math.exp(-1)
    assert cosine_variance>0
    return dict(scope='Fixed one-frequency two-feature posterior, analytic formulas versus deterministic quadrature; no model training or empirical benchmark.',
                parameters=dict(input_mean=mu,input_variance=variance,omega=omega,weight_mean=alpha,weight_covariance=weight_covariance,observation_noise_variance=noise),
                exact=dict(feature_mean=q,feature_second_moment=psi,input_feature_covariance=cross,output_mean=mean,output_variance=total_variance,input_output_covariance=dot(cross,alpha)),
                numerical_check=dict(interval_standard_deviations=10,simpson_subintervals=n,maximum_absolute_error=error),
                linearized=dict(output_mean=linear_mean,output_variance=linear_variance,input_output_covariance=linear_cross),
                conditional_variance_order=dict(model='Y=W*cos(X), W~N(0,1) independent of X~N(0,2).',exact_variance=exact_cosine_variance,frozen_conditional_variance=frozen_variance,second_order_conditional_variance=second_order_variance),
                non_gaussian=dict(model='Y=cos(X), X~N(0,1), fixed coefficient and no observation noise.',mean=cosine_mean,variance=cosine_variance,support=[-1,1]),
                interpretation=['Exact moments are for fixed finite features and a specified independent input/weight posterior, not the original kernel or a Gaussian predictive law.',
                                'Sine/cosine cross moments and input-feature covariance signs agree with independent quadrature.',
                                'SSGP-Lin freezes the conditional variance and differs from the Girard second-order variance expansion.',
                                'A nondegenerate bounded cosine output cannot have the full law of its moment-matched Gaussian.'])


if __name__=='__main__':
    print(json.dumps(calculate(),indent=2))
