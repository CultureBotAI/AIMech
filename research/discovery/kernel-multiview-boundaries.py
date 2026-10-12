"""Finite curator calculations for Tzortzis-Likas (2012), not benchmark reproduction."""
import json, math

def weights(d, p):
    assert p > 1 and all(x > 0 for x in d)
    z = [-math.log(x)/(p-1) for x in d]
    z = [math.exp(x-max(z)) for x in z]
    return [x/sum(z) for x in z]

def coefficients(d, p):
    # Normalize in log space to avoid underflow at large p.
    z = [-p*math.log(x)/(p-1) for x in d]
    z = [math.exp(x-max(z)) for x in z]
    return [x/sum(z) for x in z]

def obj(d,w,p):return sum(x*y**p for x,y in zip(d,w))

w=weights([1.,4.],2.)
assert all(abs(a-b)<1e-12 for a,b in zip(w,[.8,.2]))
assert abs(obj([1.,4.],w,2)-.8)<1e-12
assert obj([1.,4.],w,2)<obj([1.,4.],[.5,.5],2)
# Finite positive p produces no exact zero weights when all residuals are positive.
assert all(x>0 for x in weights([1.,4.],1.2))
large_p_weights=weights([1.,4.],10001.)
large_p_coefficients=coefficients([1.,4.],10001.)
assert abs(large_p_weights[0]-.5)<1e-4
assert abs(large_p_coefficients[0]-.8)<1e-4
# p=1: an entire minimizer face, not only simplex vertices.
assert obj([1,1,4],[.3,.7,0],1)==1
# p>1 with zero residuals: mass can be split arbitrarily over zero-D views.
assert obj([0,0,4],[.3,.7,0],2)==0
# For PSD view kernels diag(1,0), diag(0,1), M=1, p=2,
# Y=(cos theta,sin theta) yields residuals (sin^2 theta,cos^2 theta).
# w=(.5,.5), theta=pi/4 is coordinatewise optimal: composite K=.25 I.
# A simultaneous nearby change of Y and its minimizing w lowers the objective.
theta=math.pi/4
start_d=[math.sin(theta)**2,math.cos(theta)**2]
start=obj(start_d,[.5,.5],2)
theta_new=theta+.01
new_d=[math.sin(theta_new)**2,math.cos(theta_new)**2]
new_w=weights(new_d,2)
new=obj(new_d,new_w,2)
assert abs(start-.25)<1e-12 and new<start
assert abs(new-(.25*math.cos(.02)**2))<1e-12
# Fixed Y perturbation with equal weights leaves the value constant;
# fixed Y at pi/4 has globally minimal weight objective at equal weights.
assert abs(obj(new_d,[.5,.5],2)-start)<1e-12
assert obj(start_d,[.51,.49],2)>start
# Per-view scalar rescaling changes weights unless normalized consistently.
assert weights([1,4],2)!=weights([4,4],2)
# For a constant all-ones kernel, every pairwise squared distance is zero.
k=[[1.,1.],[1.,1.]]
mean_distance=sum(k[i][i]-2*k[i][j]+k[j][j] for i in range(2) for j in range(2))/4
assert mean_distance==0
print(json.dumps(dict(status='passed',positive_residual_weights=w,objective=.8,large_p_weights=large_p_weights,large_p_normalized_coefficients=large_p_coefficients,spectral_fixed_point=dict(initial_objective=start,perturbed_objective=new,perturbed_weights=new_w,eigenvalue_tie=True),constant_kernel_mean_squared_distance=mean_distance),indent=2))
