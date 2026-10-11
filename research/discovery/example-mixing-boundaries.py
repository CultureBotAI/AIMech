"""Finite curation checks; no downloaded code or model is executed."""
import json
from math import log, isclose

def calculate():
    probabilities=(0.8,0.2)
    anchor_losses=[-log(p) for p in probabilities]
    symmetric_hard_mean=sum(anchor_losses)/2
    soft_half_loss=-sum(0.5*log(p) for p in probabilities)
    assert isclose(symmetric_hard_mean,soft_half_loss)
    assert not isclose(anchor_losses[0],soft_half_loss)
    # Illustrative ordered pairs with replacement; averages can collide.
    points=(0,2,4)
    averages={(a+b)/2 for a in points for b in points}
    assert len(averages)==5 and len(points)**2==9
    # Nominal 4x4 patch on an 8x8 image, centered at the corner.
    nominal_lambda=0.75
    clipped_width=2;clipped_height=2
    actual_area=clipped_width*clipped_height
    actual_lambda=1-actual_area/64
    assert actual_lambda==0.9375
    nominal_ce=sum(w*l for w,l in zip((nominal_lambda,1-nominal_lambda),anchor_losses))
    actual_ce=sum(w*l for w,l in zip((actual_lambda,1-actual_lambda),anchor_losses))
    # A squared reference loss alone need not retain the reference support.
    reference=(-1,1)
    mse=lambda x:sum((x-y)**2 for y in reference)/2
    assert mse(0)==1 and mse(1)==2 and 0 not in reference
    return dict(pairing=dict(ordered_anchor_losses=anchor_losses,symmetric_hard_loss=symmetric_hard_mean,soft_half_loss=soft_half_loss,ordered_pair_choices=9,distinct_scalar_averages=len(averages)),cutmix=dict(nominal_lambda=nominal_lambda,actual_pasted_area=actual_area,actual_lambda=actual_lambda,nominal_target_ce=nominal_ce,actual_target_ce=actual_ce),reference_mse=dict(reference_support=list(reference),midpoint_mse=mse(0),endpoint_mse=mse(1)),scope='Finite illustrative inputs. Expected-loss equivalence requires exchangeable ordering and a loss linear in targets. MSE example does not assert collapse of a joint classifier/generator. No performance or author-code reproduction.')

if __name__=='__main__':
    print(json.dumps(calculate(),indent=2))
