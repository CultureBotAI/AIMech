"""Constructed dropout-gradient counterexample, not model or benchmark replication."""
import itertools
import json
import math


def result():
    # A dataset of identical x=(1,1), y=0 examples, w=(1,2), squared loss.
    # No batch-sampling variance exists. Independent inverted masks have p=1/2.
    weights=(1.0,2.0)
    full_gradient=[3.0,3.0]
    gradients=[]
    losses=[]
    for mask in itertools.product((0.0,2.0),repeat=2):
        pred=sum(w*m for w,m in zip(weights,mask))
        gradients.append([pred*m for m in mask])
        losses.append(0.5*pred*pred)
    mean=[sum(g[i] for g in gradients)/4 for i in range(2)]
    variance=[sum((g[i]-mean[i])**2 for g in gradients)/4 for i in range(2)]
    assert mean==[4.0,5.0] and variance==[24.0,27.0]
    assert mean!=full_gradient
    nonzero=[g for g in gradients if any(g)]
    def cosine_distance(g,h):
        ng=math.sqrt(sum(v*v for v in g));nh=math.sqrt(sum(v*v for v in h))
        assert ng>0 and nh>0
        return 0.5*(1-sum(x*y for x,y in zip(g,h))/(ng*nh))
    direction_error=sum(cosine_distance(g,full_gradient) for g in nonzero)/len(nonzero)
    assert direction_error>0
    assert sum(losses)/4==7.0
    return dict(full_gradient=full_gradient,no_dropout_batch_variance=[0.0,0.0],
                masked_gradients=gradients,expected_dropout_gradient=mean,
                dropout_gradient_variance=variance,dropout_expected_loss=sum(losses)/4,
                full_loss=4.5,nonzero_mask_direction_error=direction_error,
                zero_gradient_mask_probability=0.25,
                interpretation='An identical-example dataset gives a counterexample to universal gradient-variance reduction. Dropout can change the expected objective and gradient. Cosine-based errors require nonzero vectors; the conditional nonzero-mask value is not an estimate of the paper experiments.')


if __name__=='__main__':print(json.dumps(result(),indent=2,sort_keys=True))
