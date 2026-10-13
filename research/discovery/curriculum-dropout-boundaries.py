"""Constructed schedule, mask-probability and source-proof boundaries."""
import itertools,json,math


def entropy(p):
    return -sum(v*math.log(v) for v in p if v)


def result():
    terminal=.5;updates=10000;gamma=10/updates
    def theta(t):return (1-terminal)*math.exp(-gamma*t)+terminal
    trajectory=[theta(t) for t in [0,1000,5000,10000]]
    assert trajectory[0]==1 and all(a>b for a,b in zip(trajectory,trajectory[1:]))
    residual=trajectory[-1]-terminal
    assert 0<residual<1e-4
    retention=.8;masks=list(itertools.product([0,1],repeat=2))
    probs=[retention**sum(m)*(1-retention)**(2-sum(m)) for m in masks]
    assert math.isclose(sum(probs),1)
    inflated=[p*math.comb(2,2-sum(m)) for p,m in zip(probs,masks)]
    count_probs=[math.comb(2,i)*(1-retention)**i*retention**(2-i) for i in range(3)]
    assert math.isclose(sum(count_probs),1) and sum(inflated)>1
    all_kept_ratio=retention**2/(theta(updates)**2)
    assert all_kept_ratio>1
    image_probs=[.5,.5]
    joint=[p*q for p in image_probs for q in count_probs]
    h_joint=entropy(joint);h_sum=entropy(image_probs)+entropy(count_probs)
    h_product=entropy(image_probs)*entropy(count_probs)
    assert math.isclose(h_joint,h_sum) and not math.isclose(h_joint,h_product)
    # All masks applied to an all-zero image produce the identical observed image.
    assert len({tuple(a*b for a,b in zip((0.,0.),m)) for m in masks})==1
    x=[[1.,2.],[-1.,3.]];w=[.3,-.4];y=[.2,.7]
    expected=sum(p*sum((yi-sum(v*wi*mi for v,wi,mi in zip(row,w,m)))**2 for row,yi in zip(x,y)) for m,p in zip(masks,probs))
    mean_loss=sum((yi-retention*sum(v*wi for v,wi in zip(row,w)))**2 for row,yi in zip(x,y))
    penalty=retention*(1-retention)*sum(v*v*wi*wi for row in x for v,wi in zip(row,w))
    assert math.isclose(expected,mean_loss+penalty)
    return dict(retention_trajectory=trajectory,finite_endpoint_residual=residual,mask_probabilities=probs,
                count_probabilities=count_probs,incorrect_count_factor_per_mask_total=sum(inflated),
                all_kept_density_ratio_to_terminal=all_kept_ratio,independent_joint_entropy=h_joint,
                entropy_sum=h_sum,incorrect_entropy_product=h_product,zero_image_output_entropy=0.,
                squared_loss_expectation=expected,squared_loss_of_mean=mean_loss,linear_variance_penalty=penalty)


if __name__=='__main__':print(json.dumps(result(),indent=2,sort_keys=True))
