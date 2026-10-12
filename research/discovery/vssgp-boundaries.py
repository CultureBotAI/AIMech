"""Fixed variational moment/bound calculations, not model fitting or a benchmark."""
import math
import json

def dot(x,y):return sum(a*b for a,b in zip(x,y))
def mv(a,x):return [dot(row,x) for row in a]
def determinant(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def inverse(a):
    d=determinant(a);assert d>0
    return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]
def trace_product(a,b):return sum(a[i][j]*b[j][i] for i in range(2) for j in range(2))
def moments(x):
    mu=[.4,1.1];variance=[.2,.3];phase=[.1,.4]
    mean=[math.exp(-.5*v*x*x)*math.cos(m*x+b) for m,v,b in zip(mu,variance,phase)]
    diagonal=[.5*(1+math.exp(-2*v*x*x)*math.cos(2*(m*x+b))) for m,v,b in zip(mu,variance,phase)]
    return mean,[[diagonal[0],mean[0]*mean[1]],[mean[0]*mean[1],diagonal[1]]]
def explicit_bound(y,features,h,m,s,tau):
    g=[sum(f[i]*v for f,v in zip(features,y)) for i in range(2)]
    expected_quadratic=trace_product(s,h)+dot(m,mv(h,m))
    ll=-len(y)/2*math.log(2*math.pi/tau)-tau/2*(dot(y,y)-2*dot(g,m)+expected_quadratic)
    kl=.5*(s[0][0]+s[1][1]+dot(m,m)-math.log(determinant(s))-2)
    return ll-kl
def quadrature(fn,intervals=20000):
    lower=-10.;upper=10.;h=(upper-lower)/intervals
    def integrand(z):return fn(z)*math.exp(-z*z/2)/math.sqrt(2*math.pi)
    total=integrand(lower)+integrand(upper)
    for i in range(1,intervals):total+=(4 if i%2 else 2)*integrand(lower+i*h)
    return total*h/3

def calculate():
    x=[-.5,.3,1.2];y=[.5,-.4,1.1];tau=2.5
    features=[moments(v)[0] for v in x]
    h=[[sum(moments(v)[1][i][j] for v in x) for j in range(2)] for i in range(2)]
    b=[[tau*h[i][j]+(1 if i==j else 0) for j in range(2)] for i in range(2)]
    s=inverse(b);g=[sum(f[i]*v for f,v in zip(features,y)) for i in range(2)]
    m=mv(s,[tau*v for v in g]);diag_s=[[1/b[0][0],0.],[0.,1/b[1][1]]]
    full=explicit_bound(y,features,h,m,s,tau);diagonal=explicit_bound(y,features,h,m,diag_s,tau)
    collapsed=-len(y)/2*math.log(2*math.pi/tau)-tau/2*dot(y,y)-.5*math.log(determinant(b))+.5*tau*dot(g,m)
    gap=.5*math.log(b[0][0]*b[1][1]/determinant(b))
    assert abs(full-collapsed)<1e-12 and abs(full-diagonal-gap)<1e-12 and gap>0
    # This omits the same fixed frequency KL from both bounds, so their difference is unaffected.
    # Enumerate every uniform two-of-three minibatch at fixed variational parameters.
    kl=.5*(diag_s[0][0]+diag_s[1][1]+dot(m,m)-math.log(determinant(diag_s))-2)
    local=[]
    for xi,yi in zip(x,y):
        ef,eh=moments(xi)
        local.append(-.5*math.log(2*math.pi/tau)-tau/2*(yi*yi-2*yi*dot(ef,m)+trace_product(diag_s,eh)+dot(m,mv(eh,m))))
    minibatch_bounds=[len(x)/2*(local[i]+local[j])-kl for i,j in [(0,1),(0,2),(1,2)]]
    mean_minibatch=sum(minibatch_bounds)/3
    assert abs(mean_minibatch-diagonal)<1e-12
    wrong_kl_scaling=[len(x)/2*(local[i]+local[j]-kl) for i,j in [(0,1),(0,2),(1,2)]]
    assert abs(sum(wrong_kl_scaling)/3-diagonal)>.01
    t=.8;f,psi=moments(t)
    predicted_mean=dot(f,m)
    predicted_variance=1/tau+trace_product(s,psi)+dot(m,mv(psi,m))-predicted_mean**2
    assert predicted_variance>0
    errors=[]
    for i,(mu,v,phase) in enumerate(zip([.4,1.1],[.2,.3],[.1,.4])):
        first=quadrature(lambda z:math.cos((mu+math.sqrt(v)*z)*t+phase))
        second=quadrature(lambda z:math.cos((mu+math.sqrt(v)*z)*t+phase)**2)
        errors.extend([abs(first-f[i]),abs(second-psi[i][i])])
    assert max(errors)<1e-10
    fixed_phase_square_of_mean=f[0]**2
    assert psi[0][0]-fixed_phase_square_of_mean>0
    # Uniform phase and fixed phase are different distributions.
    alpha=.2;beta=1.1;mu=.4;v=.2
    uniform_mean=math.exp(-.5*v*t*t)*(math.sin(mu*t+beta)-math.sin(mu*t+alpha))/(beta-alpha)
    uniform_second=.5+.5*math.exp(-2*v*t*t)*(math.sin(2*(mu*t+beta))-math.sin(2*(mu*t+alpha)))/(2*(beta-alpha))
    fixed_at_alpha=math.exp(-.5*v*t*t)*math.cos(mu*t+alpha)
    assert abs(uniform_mean-fixed_at_alpha)>.01
    far_mean,far_psi=moments(100.)
    far_variance=1/tau+trace_product(s,far_psi)+dot(m,mv(far_psi,m))-dot(far_mean,m)**2
    far_formula=1/tau+.5*(s[0][0]+s[1][1]+dot(m,m))
    assert abs(far_variance-far_formula)<1e-12
    assert abs(far_variance-(1/tau+1))>.01
    return dict(scope='Finite analytic variational arithmetic for two independent Gaussian angular frequencies and fixed phases; no optimization run, training pipeline, author-code execution or benchmark.',
      parameters=dict(inputs=x,responses=y,precision=tau,frequency_means=[.4,1.1],frequency_variances=[.2,.3],phases=[.1,.4],feature_amplitude=1),
      coefficient_variational_optimum=dict(mean=m,full_covariance=s,diagonal_restriction_covariance=diag_s),
      bounds_without_common_frequency_kl=dict(explicit_full=full,collapsed=collapsed,diagonal_restricted=diagonal,full_minus_diagonal=gap),
      prediction=dict(input=t,mean=predicted_mean,noisy_variance=predicted_variance,first_feature_mean=f[0],first_feature_second_moment=psi[0][0],first_feature_squared_mean=fixed_phase_square_of_mean,quadrature_max_abs_error=max(errors)),
      minibatch_identity=dict(full_diagonal_bound=diagonal,uniform_two_of_three_estimates=minibatch_bounds,mean=mean_minibatch,incorrect_scaled_kl_mean=sum(wrong_kl_scaling)/3),
      phase_comparison=dict(interval=[alpha,beta],uniform_mean=uniform_mean,uniform_second_moment=uniform_second,fixed_at_lower_endpoint_mean=fixed_at_alpha),
      far_field=dict(input=100.,noisy_variance=far_variance,derived_limit=far_formula,unit_coefficient_prior_noisy_variance=1/tau+1),
      caveats=['The full coefficient optimum is within a factorization between coefficients and frequencies, not exact frequency inference.',
               'The same fixed frequency KL is omitted in both displayed bound values; do not compare them directly to complete evidence.',
               'The diagonal coefficient restriction is strictly looser in this nonorthogonal finite example.',
               'Uniform phase integration differs from fixing the phase at one endpoint; zero width is not a finite-density variational distribution.',
               'The far-field variance depends on fitted variational coefficient moments and need not equal the original prior variance.'])

if __name__=='__main__':print(json.dumps(calculate(),indent=2))
