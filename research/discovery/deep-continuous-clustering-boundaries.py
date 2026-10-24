"""Finite checks of DCC source expressions; no author code or model is run."""
from fractions import Fraction as F
import json


def main():
    mu,r=F(2),F(3)
    rho=mu*r*r/(mu+r*r)
    derivative=2*mu*mu*r/(mu+r*r)**2
    printed_gradient=mu*mu*r/(mu+r*r)**2
    assert derivative==F(24,121)==2*printed_gradient
    n,d,lam,w=2,5,3,2
    code_pair=F(lam*w,n*d)*rho
    eq6_pair=F(lam*w,n)*rho
    assert code_pair==F(54,55) and eq6_pair==d*code_pair
    def flag_trace(changes,threshold):
        flag=1;trace=[]
        for change in changes:
            if change>threshold:flag+=1
            trace.append(flag)
            if flag==4:break
        return trace
    stable=flag_trace([0]*5,1)
    changing=flag_trace([2,0,2,0,2],1)
    assert stable==[1]*5 and changing==[2,2,3,3,4]
    print(json.dumps(dict(robust_scalar=dict(mu=mu,residual=r,penalty=rho,derivative=derivative,printed_without_factor_two=printed_gradient),pair_scaling=dict(batch_vertices=n,latent_dimension=d,lambda_value=lam,edge_weight=w,implementation_pair_term=code_pair,printed_eq6_pair_term=eq6_pair),stopping_flags=dict(threshold=1,stable_changes=[0]*5,stable_flags=stable,changing_changes=[2,0,2,0,2],changing_flags=changing),limits="Scalar derivative identity, normalization comparison and literal flag predicate only. No author imports, autodiff execution, training, numerical convergence, reachable clustering trajectory or benchmark result."),default=str,indent=2))


if __name__=='__main__':main()
