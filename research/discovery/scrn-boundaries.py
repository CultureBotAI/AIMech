"""Elementary SCRN trace and parameterization calculations, not training."""
import json, math

def close(x,y):assert math.isclose(x,y,rel_tol=1e-10,abs_tol=1e-10),(x,y)
def trace(xs,a,s=0.):
 for x in xs:s=(1-a)*x+a*s
 return s

a=.5;xs=[1.,3.];s0=2.
expanded=a**2*s0+(1-a)*sum(a**(1-j)*x for j,x in enumerate(xs))
close(trace(xs,a,s0),expanded)
ab=trace([1.,3.],a);ba=trace([3.,1.],a);assert ab!=ba
# Paper current-context fast preactivation vs lagged code and transformed parameters.
a=.8;b=2.;x=1.5;p=3.;amat=.4;r=.6;s_prev=4.;h_prev=.7
s=(1-a)*b*x+a*s_prev
paper=p*s+amat*x+r*h_prev
same_raw=p*s_prev+amat*x+r*h_prev
mapped=(a*p)*s_prev+(amat+(1-a)*p*b)*x+r*h_prev
close(paper,mapped);assert not math.isclose(paper,same_raw)
# Scalar-decay context remains in the convex hull of bounded initial/input values.
v=2.;largest=abs(v)
for u in [3.,-3.,1.,-2.]*100:
 v=.05*u+.95*v;largest=max(largest,abs(v));assert abs(v)<=3.+1e-12
print(json.dumps(dict(trace_unrolled=expanded,permutation_outputs=[ab,ba],carry_after_100_steps=.95**100,paper_preactivation=paper,unchanged_lagged_preactivation=same_raw,transformed_lagged_preactivation=mapped,largest_bounded_context=largest,scope='Constructed scalar trace and affine-substitution checks only; no Torch or training execution.'),indent=2))
