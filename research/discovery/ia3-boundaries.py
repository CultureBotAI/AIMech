"""Small constructed IA3 algebra checks; no author implementation or training."""
import json,math


def attention(q,k,v,lk,lv):
    z=[[sum(a*b*c for a,b,c in zip(qi,kj,lk))/math.sqrt(len(lk)) for kj in k] for qi in q]
    a=[]
    for row in z:
        exp=[math.exp(x-max(row)) for x in row];a.append([x/sum(exp) for x in exp])
    y=[[sum(ai[j]*v[j][c]*lv[c] for j in range(len(v))) for c in range(len(lv))] for ai in a]
    return y,a


def result():
    q=[[1.,.2],[-.4,1.]];k=[[.3,1.],[-.5,.8]];v=[[1.,-.3],[.2,.9]]
    lk=[.7,-.4];lv=[1.2,.6];y,a=attention(q,k,v,lk,lv)
    da=[[sum(y[i][c]*v[j][c]*lv[c] for c in range(2)) for j in range(2)] for i in range(2)]
    dz=[[a[i][j]*(da[i][j]-sum(a[i][t]*da[i][t] for t in range(2))) for j in range(2)] for i in range(2)]
    analytic_k=[sum(dz[i][j]*q[i][c]*k[j][c] for i in range(2) for j in range(2))/math.sqrt(2) for c in range(2)]
    analytic_v=[sum(y[i][c]*a[i][j]*v[j][c] for i in range(2) for j in range(2)) for c in range(2)]
    def loss(kk,vv):return .5*sum(x*x for row in attention(q,k,v,kk,vv)[0] for x in row)
    fd=[];eps=1e-5
    for target in [0,1]:
        current=[]
        for c in range(2):
            ka,kb,va,vb=lk[:],lk[:],lv[:],lv[:]
            if target==0:ka[c]+=eps;kb[c]-=eps
            else:va[c]+=eps;vb[c]-=eps
            current.append((loss(ka,va)-loss(kb,vb))/(2*eps))
        fd.append(current)
    assert all(math.isclose(x,z,abs_tol=1e-10) for row,other in zip([analytic_k,analytic_v],fd) for x,z in zip(row,other))
    # Key/value channel factors can be folded into their already projected arrays.
    folded_k=[[x*s for x,s in zip(row,lk)] for row in k]
    folded_v=[[x*s for x,s in zip(row,lv)] for row in v]
    folded=attention(q,folded_k,folded_v,[1.,1.],[1.,1.])[0]
    assert all(math.isclose(x,z,abs_tol=1e-12) for row,other in zip(y,folded) for x,z in zip(row,other))
    # With an affine projection, absorbing an output scale includes its bias.
    x,w,b,s=2.,3.,.5,4.
    direct=(x*w+b)*s;correct=x*(w*s)+b*s;wrong=x*(w*s)+b
    assert direct==correct and direct!=wrong
    sigmoid=lambda t:1/(1+math.exp(-t))
    after=2*sigmoid(1.);before=sigmoid(2.)
    assert not math.isclose(after,before)
    assert attention(q,k,v,[1.,1.],[1.,1.])[0]!=y
    return dict(key_scale_gradient=analytic_k,value_scale_gradient=analytic_v,finite_differences=fd,
                task_specific_fold_matches=True,affine_bias_example=dict(direct=direct,correct_fold=correct,omitted_bias_scale=wrong),
                nonlinearity_placement=dict(scale_after=after,scale_before=before),
                encoder_decoder_parameter_example=dict(L=2,dk=3,dv=3,dff=7,encoder=2*(3+3+7),decoder=2*(2*3+2*3+7)))


if __name__=='__main__':print(json.dumps(result(),indent=2,sort_keys=True))
