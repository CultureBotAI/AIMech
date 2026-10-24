"""Constructed fixed-parameter filter and derivative checks, without fitting."""
from fractions import Fraction as Q
from math import comb
import json
inputs=[Q(1),Q(-1,2),Q(1,4),Q(2)];targets=[Q(0),Q(1),Q(-1),Q(1,2)]
w=[Q(1,5),Q(-3,10),Q(2,5)];mu=Q(3,5)
def trajectory(m,weights):
 old=[Q(0)]*3;alpha=[Q(0)]*3;loss=Q(0);gradw=[Q(0)]*3;gradmu=Q(0);states=[];sens=[]
 for u,d in zip(inputs,targets):
  x=[u]+[(1-m)*old[k]+m*old[k-1] for k in [1,2]]
  a=[Q(0)]+[(1-m)*alpha[k]+m*alpha[k-1]+old[k-1]-old[k] for k in [1,2]]
  y=sum(v*z for v,z in zip(weights,x));error=y-d;loss+=error*error/2
  gradw=[g+error*z for g,z in zip(gradw,x)];gradmu+=error*sum(v*z for v,z in zip(weights,a))
  old=x;alpha=a;states.append(x);sens.append(a)
 return loss,gradw,gradmu,states,sens
loss,gw,gm,xs,alphas=trajectory(mu,w);step=Q(1,10**6)
fdmu=(trajectory(mu+step,w)[0]-trajectory(mu-step,w)[0])/(2*step)
errors=[float(abs(fdmu-gm))]
for i in range(3):
 up=w.copy();down=w.copy();up[i]+=step;down[i]-=step
 fd=(trajectory(mu,up)[0]-trajectory(mu,down)[0])/(2*step);errors.append(float(abs(fd-gw[i])))
assert max(errors)<1e-9
# Direct differentiation of the finite second-moment matrix needs both terms.
one=[[sum(x[i]*a[j] for x,a in zip(xs,alphas)) for j in range(3)] for i in range(3)]
total=[[one[i][j]+one[j][i] for j in range(3)] for i in range(3)]
assert any(total[i][j]!=one[i][j] for i in range(3) for j in range(3))
quad=lambda a:sum(w[i]*a[i][j]*w[j] for i in range(3) for j in range(3))
assert quad(total)==2*quad(one)
old=[Q(0)]*3;impulse=[]
for n in range(8):
 x=[Q(int(n==0))]+[old[k]/2+old[k-1]/2 for k in [1,2]];impulse.append(x[2]);old=x
expected=[Q(0) if n<2 else Q(comb(n-1,1),2**n) for n in range(8)];assert impulse==expected
print(json.dumps(dict(weight_gradient=list(map(str,gw)),memory_parameter_gradient=str(gm),maximum_finite_difference_error=max(errors),two_stage_impulse=list(map(str,impulse)),second_moment_derivative_quadratic=str(quad(total)),one_sided_crossmoment_quadratic=str(quad(one)),parameter_count_for_K2=4,scope='Fixed-parameter rational recurrence with independent zero initialization; direct input tap retained. Correct derivative of a second moment includes both transpose terms. No fitting, adaptive convergence test, author implementation or empirical performance claim.'),indent=2))
