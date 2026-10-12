"""Finite matrix identities for SSGPR; no hyperparameter optimization or benchmark."""
import math
import json

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def transpose(a):return [list(row) for row in zip(*a)]
def multiply(a,b):return [[dot(row,col) for col in transpose(b)] for row in a]
def solve(a,b):
    n=len(a);work=[list(row)+[b[i]] for i,row in enumerate(a)]
    for i in range(n):
        pivot=max(range(i,n),key=lambda j:abs(work[j][i]))
        assert abs(work[pivot][i])>1e-14
        work[i],work[pivot]=work[pivot],work[i]
        scale=work[i][i];work[i]=[v/scale for v in work[i]]
        for j in range(n):
            if j!=i:
                scale=work[j][i];work[j]=[x-scale*y for x,y in zip(work[j],work[i])]
    return [row[-1] for row in work]
def logdet(a):
    n=len(a);lower=[[0.]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            value=a[i][j]-sum(lower[i][k]*lower[j][k] for k in range(j))
            if i==j:
                assert value>0;lower[i][j]=math.sqrt(value)
            else:lower[i][j]=value/lower[j][j]
    return 2*sum(math.log(lower[i][i]) for i in range(n))
def calculate():
    frequencies=[.37,1.12];m=len(frequencies);prior_variance=1.7;noise=.2
    x=[-.8,.3,1.6];y=[.5,-.4,1.1];test=.9;n=len(x)
    def phi(x):return [value for s in frequencies for value in (math.cos(2*math.pi*s*x),math.sin(2*math.pi*s*x))]
    def kernel(x,z):return prior_variance/m*sum(math.cos(2*math.pi*s*(x-z)) for s in frequencies)
    features=transpose([phi(v) for v in x]);phistar=phi(test)
    a=multiply(features,transpose(features));regularizer=m*noise/prior_variance
    a=[[v+(regularizer if i==j else 0) for j,v in enumerate(row)] for i,row in enumerate(a)]
    phiy=[dot(row,y) for row in features]
    mean_feature=dot(phistar,solve(a,phiy));variance_feature=noise+noise*dot(phistar,solve(a,phistar))
    covariance=[[kernel(v,z)+(noise if i==j else 0) for j,z in enumerate(x)] for i,v in enumerate(x)]
    cross=[kernel(test,v) for v in x]
    mean_kernel=dot(cross,solve(covariance,y))
    variance_kernel=noise+kernel(test,test)-dot(cross,solve(covariance,cross))
    evidence_kernel=-.5*(dot(y,solve(covariance,y))+logdet(covariance)+n*math.log(2*math.pi))
    evidence_feature=-(dot(y,y)-dot(phiy,solve(a,phiy)))/(2*noise)-.5*logdet(a)+m*math.log(regularizer)-n/2*math.log(2*math.pi*noise)
    assert math.isclose(mean_feature,mean_kernel,rel_tol=1e-12,abs_tol=1e-12)
    assert math.isclose(variance_feature,variance_kernel,rel_tol=1e-12,abs_tol=1e-12)
    assert math.isclose(evidence_feature,evidence_kernel,rel_tol=1e-12,abs_tol=1e-12)
    # Pan2017 absorbs the coefficient prior variance into its feature map.
    scale=math.sqrt(prior_variance/m)
    scaled=[[scale*v for v in row] for row in features]
    ap=multiply(scaled,transpose(scaled))
    ap=[[v+(noise if i==j else 0) for j,v in enumerate(row)] for i,row in enumerate(ap)]
    star=[scale*v for v in phistar];rhs=[dot(row,y) for row in scaled]
    mean_scaled=dot(star,solve(ap,rhs));variance_scaled=noise+noise*dot(star,solve(ap,star))
    assert math.isclose(mean_scaled,mean_feature,abs_tol=1e-12)
    assert math.isclose(variance_scaled,variance_feature,abs_tol=1e-12)
    for u,z in [(-.8,.3),(.3,1.6),(1.6,1.6)]:
        assert math.isclose(kernel(u,z),prior_variance/m*dot(phi(u),phi(z)),abs_tol=1e-12)
        assert math.isclose(kernel(u+2.4,z+2.4),kernel(u,z),abs_tol=1e-12)
        assert math.isclose(kernel(u,u),prior_variance,abs_tol=1e-12)
    atom_mass=prior_variance/(2*m);assert math.isclose(2*m*atom_mass,prior_variance)
    return dict(scope='Fixed finite scalar matrix calculation; no frequency learning, model training pipeline, simulation or source benchmark.',
                parameters=dict(frequencies_cycles=frequencies,prior_variance=prior_variance,noise_variance=noise,inputs=x,response_vector=y,test_input=test),
                feature_space=dict(mean=mean_feature,noisy_variance=variance_feature,log_marginal_likelihood=evidence_feature),
                kernel_space=dict(mean=mean_kernel,noisy_variance=variance_kernel,log_marginal_likelihood=evidence_kernel),
                scaled_features=dict(mean=mean_scaled,noisy_variance=variance_scaled),
                spectral_measure=dict(mass_per_positive_or_negative_atom=atom_mass,total_mass=prior_variance),
                interpretation=['Paired features reproduce the cosine kernel and constant prior diagonal; tested translations preserve covariance.',
                                'Feature-space and kernel-space conditioning and log evidence agree for the specified finite case.',
                                'Absorbing the coefficient prior scale into features reproduces the later unit-prior convention.',
                                'These finite checks do not prove frequency-optimization convergence, uncertainty calibration or empirical superiority.'])

if __name__=='__main__':print(json.dumps(calculate(),indent=2))
