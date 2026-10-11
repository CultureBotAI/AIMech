"""Original finite source checks, not author-code execution or training."""
from fractions import Fraction as F
import json

def calculate():
    gamma=F(1,4)
    l=(F(4,5),F(1,5));g=(F(1,5),F(4,5))
    # Joint model: good loss=0.5, bad loss=3, threshold=2.
    good_loss=F(1,2);threshold=F(2)
    marginal=[gamma*a+(1-gamma)*b for a,b in zip(l,g)]
    ranking=[1/(gamma+(1-gamma)*b/a) for a,b in zip(l,g)]
    improvement=[gamma*a*(threshold-good_loss)/p for a,p in zip(l,marginal)]
    scale=gamma*(threshold-good_loss)
    assert improvement==[scale*r for r in ranking]
    assert improvement[0]>improvement[1] and sum(marginal)==1
    # One observed positive sample change need not have positive expectation.
    mean_delta=F(1,10)*1+F(9,10)*(-1)
    assert mean_delta<0
    # Equal-prior optimal discriminator for two normalized two-point densities.
    real=(F(4,5),F(1,5));fake=(F(2,5),F(3,5))
    discriminator=[p/(p+q) for p,q in zip(real,fake)]
    assert sum(real)==sum(fake)==1 and sum(discriminator)!=1
    # Real losses (1,3), synthetic losses (4,4,4,4): separate means vs pooled mean.
    real_losses=[F(1),F(3)];fake_losses=[F(4)]*4
    separate=sum(real_losses)/len(real_losses)+sum(fake_losses)/len(fake_losses)
    pooled=sum(real_losses+fake_losses)/len(real_losses+fake_losses)
    assert separate==6 and pooled==F(10,3)
    def vals(v):return [float(x) for x in v]
    return dict(tpe=dict(marginal=vals(marginal),ratio_ranking=vals(ranking),expected_improvement=vals(improvement),proportionality_constant=float(scale)),sample_change=dict(possible_observed_delta=1,expected_delta=float(mean_delta)),discriminator=dict(real=vals(real),fake=vals(fake),real_posterior=vals(discriminator),sum_of_real_posteriors=float(sum(discriminator))),classification_normalization=dict(separate_group_means=float(separate),pooled_mean=float(pooled)),scope='Illustrative finite arithmetic; neither a complete counterexample to an EM theorem under its full assumptions nor an empirical reproduction.')

if __name__=='__main__':
    print(json.dumps(calculate(),indent=2))
