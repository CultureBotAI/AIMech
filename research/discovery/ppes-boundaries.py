#!/usr/bin/env python3
"""Original bounded PPES algebra checks; no author code or full EP implementation.

Source: Shah and Ghahramani, NIPS 2015, main pp3-5, supplement pp1-2.
Exact rational finite channels/matrix algebra use Fraction. Gaussian CDF, logs,
trigonometric and moment values are deterministic floating calculations using
stdlib math; assertions specify rel_tol=0 and absolute tolerances. The script
checks identities and counterexamples, not Bayesian optimization performance,
posterior sampling accuracy, EP convergence, or the complete published algorithm.
Run metadata and hashes belong in external receipts, not deterministic output.
"""
from fractions import Fraction as F
from itertools import product
import json
import math


def close(a, b, tol=2e-13):
    assert math.isclose(a, b, rel_tol=0.0, abs_tol=tol), (a, b, tol)


def phi(x):
    return math.exp(-x*x/2)/math.sqrt(2*math.pi)


def Phi(x):
    return (1+math.erf(x/math.sqrt(2)))/2


def det(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def inv(a):
    d=det(a)
    assert d>0
    return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]


def mv(a, x):
    return [sum(a[i][j]*x[j] for j in range(2)) for i in range(2)]


def dot(x,y):
    return sum(a*b for a,b in zip(x,y))


def entropy(masses):
    return -sum(float(p)*math.log2(float(p)) for p in masses if p)


def mi(rows):
    # Entries are (target, observation, exact probability); categories hashable.
    t={}; y={}; joint={}
    for a,b,p in rows:
        t[a]=t.get(a,F(0))+p; y[b]=y.get(b,F(0))+p
        joint[a,b]=joint.get((a,b),F(0))+p
    assert sum(joint.values())==1
    return entropy(t.values())+entropy(y.values())-entropy(joint.values())


def soft_moments(mu,v,noise,b):
    assert v>0 and noise>=0
    s=math.sqrt(v+noise); beta=(mu-b)/s; z=Phi(beta); r=phi(beta)/z
    return z,mu+v/s*r,v-v*v/(v+noise)*r*(r+beta)


def run():
    # For positive definite K and Sigma=K/2, noise makes a joint logdet score.
    matrix_rows=[]; different=0
    for a,b,c in product(map(F,[1,2,3]),map(F,[1,2,3]),[F(0),F(1,4),F(1,2)]):
        noise=F(1,3)
        k=[[a+noise,c],[c,b+noise]]
        s=[[a/2+noise,c/2],[c/2,b/2+noise]]
        assert det(k)>0 and det(s)>0
        joint=.5*math.log(float(det(k)/det(s)))
        singles=.5*math.log(float(k[0][0]*k[1][1]/(s[0][0]*s[1][1])))
        swapped_k=[[k[1][1],k[1][0]],[k[0][1],k[0][0]]]
        swapped_s=[[s[1][1],s[1][0]],[s[0][1],s[0][0]]]
        assert det(k)==det(swapped_k) and det(s)==det(swapped_s)
        if c==0: close(joint,singles)
        else:
            assert abs(joint-singles)>1e-5
            different+=1
        matrix_rows.append({'a':str(a),'b':str(b),'c':str(c),'joint_nats':joint,'sum_scalar_nats':singles})
    scalar=[.5*math.log(float((v+F(1,3))/(v/2+F(1,3)))) for v in map(F,[1,2,3])]
    # Repeated noiseless observations are redundant; independent noisy repeats
    # retain conditional information. These finite channels illustrate MI only.
    repeated=[(t,(t,t),F(1,2)) for t in (0,1)]
    single=mi([(t,t,F(1,2)) for t in (0,1)])
    noisy=[]
    for t,e1,e2 in product((0,1),repeat=3):
        prob=F(1,2)*(F(1,4) if e1 else F(3,4))*(F(1,4) if e2 else F(3,4))
        noisy.append((t,(t^e1,t^e2),prob))
    noisy_joint=mi(noisy); noisy_single=mi([(t,y[0],p) for t,y,p in noisy])
    close(mi(repeated),1); close(single+single,2)
    assert noisy_single<noisy_joint<2*noisy_single
    # Hyperparameter-conditional information can differ in either direction.
    xor=[(t,t^h,F(1,4)) for t,h in product((0,1),repeat=2)]
    same=[(h,h,F(1,2)) for h in (0,1)]
    close(mi(xor),0); close(mi(same),1)
    # Correct Gaussian precision/natural-mean addition; not printed Eq5 mean.
    k_inv=[[F(1,2),F(0)],[F(0),F(1,3)]]; c=[F(-1),F(1)]
    precision=[[k_inv[i][j]+c[i]*c[j]/5 for j in range(2)] for i in range(2)]
    cov=inv(precision); prior_h=mv(k_inv,[F(1),F(2)])
    mean=mv(cov,[prior_h[i]+F(4,5)*c[i] for i in range(2)])
    assert mean==[F(2,5),F(29,10)]
    # Valid full covariance diag(2,3), site variance10: projected cavity is10.
    sig=[[F(2),F(0)],[F(0),F(3)]]
    projected=dot(c,mv(sig,c)); correct_cavity=1/(1/projected-F(1,10))
    printed_cavity=1/(1/dot(c,mv(inv(sig),c))-F(1,10))
    prior_precision=[[inv(sig)[i][j]-c[i]*c[j]/10 for j in range(2)] for i in range(2)]
    assert prior_precision[0][0]>0 and det(prior_precision)>0
    assert correct_cavity==10 and printed_cavity==F(10,11)
    # A Gaussian ratio needs natural-mean subtraction, not its reciprocal.
    cavity_mu,cavity_v,tilt_mu,tilt_v=F(1),F(2),F(2),F(1)
    site_v=1/(1/tilt_v-1/cavity_v)
    site_mu=site_v*(tilt_mu/tilt_v-cavity_mu/cavity_v)
    printed_site_mu=site_v/(tilt_mu/tilt_v-cavity_mu/cavity_v)
    assert site_mu==3 and printed_site_mu==F(4,3)
    # Integrating N(z;mu,v) Phi((z-b)/sigma) is conditioning the joint
    # normal pair on z-epsilon>=b, epsilon independent N(0,sigma^2).
    soft=[]
    for mu,v,noise in product([-1.,0.,1.],[.5,1.,2.],[.25,1.,2.]):
        z,m,variance=soft_moments(mu,v,noise,0.)
        assert 0<z<1 and m>mu and 0<variance<v
        soft.append({'mu':mu,'variance':v,'noise_variance':noise,'normalizer':z,'tilted_mean':m,'tilted_variance':variance})
    z,m,v=soft_moments(0.,1.,1.,0.)
    close(z,.5); close(m,1/math.sqrt(math.pi)); close(v,1-1/math.pi)
    hard_z,hard_m,hard_v=soft_moments(0.,1.,0.,0.)
    close(hard_m,math.sqrt(2/math.pi)); close(hard_v,1-2/math.pi)
    assert abs(Phi(Phi(0))-.5)>.19
    # For one exact hard-threshold EP site at zero, Sigma=c*v. Its precision
    # is (1/c-1)/v, hence varies with the prior variance. The frozen-site
    # derivative Sigma^2/v^2=c^2 misses this dependence; exact is c.
    trunc_c=1-2/math.pi; gradients=[]
    for prior_v in [.5,1.,2.]:
        site_precision=(1/trunc_c-1)/prior_v
        exact_cov_derivative=trunc_c; frozen_cov_derivative=trunc_c**2
        assert abs(exact_cov_derivative-frozen_cov_derivative)>.2
        gradients.append({'prior_variance':prior_v,'site_precision':site_precision,'site_precision_derivative':-(1/trunc_c-1)/prior_v**2,'exact_covariance_derivative':exact_cov_derivative,'frozen_covariance_derivative':frozen_cov_derivative,'exact_gaussian_entropy_derivative':1/(2*prior_v),'frozen_gaussian_entropy_derivative':trunc_c/(2*prior_v)})
    # Posterior mean maximizer is not the optimizer-distribution MAP.
    # Degenerate exact example A=1; B,C iid N(0,100), unique maximum a.s.
    p_a=Phi(.1)**2; p_b=(1-p_a)/2
    assert p_a<p_b
    # Full-rank example: A~N(1,.01), B,C~N(0,100) independent.
    # P(A wins)<=P(B,C<=1.3)+P(A>1.3) <1/3. Symmetry then makes each
    # of B,C more likely than A. This is an analytic upper bound, not integration.
    positive_bound=Phi(.13)**2+1-Phi(3.)
    assert positive_bound<1/3
    # Can be realized on finite compact domain {0,1,2}, smooth polynomial
    # kernel 100*sum L_i(x)L_i(x'), prior mean0, observation at0 with the
    # following positive noise and observed value. It yields A's stated posterior.
    training_noise=F(100,9999); observed_y=F(10000,9999)
    post_v=F(100)*training_noise/(100+training_noise)
    post_mu=F(100)*observed_y/(100+training_noise)
    assert post_v==F(1,100) and post_mu==1
    # Local relaxed maximum constraints admit an unqueried larger value.
    relaxed={'candidate_f':0,'chosen_star_f':1,'unseen_f':2,'ymax':0,'noise_sd':1,'soft_factor':Phi(1),'candidate_indicator':True,'is_global_maximum':False}
    assert relaxed['soft_factor']>0
    # Duplicate latent points make the noiseless determinant singular; independent
    # observation noise makes it positive without asserting zero repeat utility.
    duplicate=[[F(1),F(1)],[F(1),F(1)]]
    with_noise=[[F(5,4),F(1)],[F(1),F(5,4)]]
    assert det(duplicate)==0 and det(with_noise)==F(9,16)
    # Four exactly spaced phases integrate the trigonometric second moment;
    # spectral amplitude alpha is necessary even in this bounded feature check.
    features=[]
    for alpha,d in product([.5,1.,3.],[0.,.2,1.]):
        val=sum(2*alpha*math.cos(b)*math.cos(d+b) for b in [0,math.pi/2,math.pi,3*math.pi/2])/4
        expected=alpha*math.cos(d); close(val,expected)
        features.append({'amplitude':alpha,'phase_difference':d,'phase_average':val,'expected':expected})
    return {'scope':'Original supporting bounded algebra audit; not independent scientific approval, full EP, author code execution, or benchmark.',
        'arithmetic':{'exact':'Fraction for finite probabilities, 2x2 determinants and Gaussian natural parameters','floating':'stdlib math CDF/entropy/moments/features; rel_tol=0, abs_tol=2e-13 where equality asserted','analytic_bound':'Full-rank optimizer MAP witness uses an upper bound, not numerical Gaussian integration'},
        'joint_covariance':{'cases':len(matrix_rows),'differ_from_scalar_sum':different,'permutation_checks':len(matrix_rows),'scalar_reductions':scalar,'rows':matrix_rows},
        'finite_information':{'redundant_joint_bits':mi(repeated),'sum_single_bits':2*single,'noisy_repeat_single_bits':noisy_single,'noisy_repeat_joint_bits':noisy_joint,'hyperparameter_xor':{'unconditional_bits':mi(xor),'conditional_bits':1},'hyperparameter_same':{'unconditional_bits':mi(same),'conditional_bits':0}},
        'gaussian_algebra':{'combined_mean':[str(x) for x in mean],'combined_covariance':[[str(x)for x in row]for row in cov],'projected_cavity_variance':str(correct_cavity),'printed_cavity_variance':str(printed_cavity),'correct_site_mean':str(site_mu),'printed_site_mean':str(printed_site_mu),'source_mean_formula':'Main Eq5 and supplement Eq3 add vector and matrix then invert; not evaluated as a valid formula.'},
        'soft_threshold':{'cases':len(soft),'rows':soft,'unit_example':{'normalizer':z,'mean':m,'variance':v,'printed_nested_phi_normalizer':Phi(Phi(0)),'hard_threshold_mean':hard_m,'hard_threshold_variance':hard_v}},
        'ep_site_derivative':{'cases':len(gradients),'rows':gradients,'limitation':'One hard-factor Gaussian EP counterexample refutes site constancy; no full PPES acquisition-gradient implementation.'},
        'optimizer_map':{'degenerate_example':{'A_probability':p_a,'B_probability':p_b,'C_probability':p_b},'positive_definite_example':{'means':[1,0,0],'variances':[.01,100,100],'A_win_probability_upper_bound':positive_bound,'B_and_C_win_probability_lower_bound':(1-positive_bound)/2,'training_noise_variance':str(training_noise),'observed_value':str(observed_y),'posterior_A_mean':str(post_mu),'posterior_A_variance':str(post_v),'scope':'Finite compact three-point domain; differentiable polynomial kernel realization; no assertion that this kernel has a stationary spectral density.'}},
        'relaxed_maximum':relaxed,
        'singularity':{'duplicate_noiseless_determinant':str(det(duplicate)),'duplicate_noisy_determinant':str(det(with_noise)),'tie_requirement':'A maximizer selector must be defined; compactness alone does not ensure finite attained maxima for arbitrary sample functions.'},
        'feature_amplitude':{'cases':len(features),'rows':features}}


if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
