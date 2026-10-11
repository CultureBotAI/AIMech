"""Exact curator examples; no author software or model training."""
from fractions import Fraction as F
from itertools import product
from math import log
import json

# Binary directed model: prior p(h=1)=1/2, p(x=1|h)=(1/4,3/4).
# Observed data are x=1; recognition q(h=1|x)=1/4.
joint = {0:F(1,8), 1:F(3,8)}
proposal = {0:F(3,4), 1:F(1,4)}
px = sum(joint.values())
posterior = {h:joint[h]/px for h in joint}
weights = {h:joint[h]/proposal[h] for h in joint}
p_score = {h:F(h)-F(1,2) for h in joint}  # prior-logit derivative
q_score = {h:F(h)-F(1,4) for h in joint}  # recognition-logit derivative
exact_p_gradient = sum(posterior[h]*p_score[h] for h in joint)
exact_wake_q_gradient = sum(posterior[h]*q_score[h] for h in joint)
assert px == F(1,2) and posterior[1] == F(3,4)
assert exact_p_gradient == F(1,4) and exact_wake_q_gradient == F(1,2)

results = {}
for count in (1,2,3):
    mean_likelihood, mean_p, mean_q = F(0),F(0),F(0)
    expected_log_likelihood = 0.0
    for samples in product((0,1), repeat=count):
        mass = F(1)
        for h in samples:
            mass *= proposal[h]
        total = sum(weights[h] for h in samples)
        likelihood = total/count
        mean_likelihood += mass*likelihood
        mean_p += mass*sum(weights[h]*p_score[h] for h in samples)/total
        mean_q += mass*sum(weights[h]*q_score[h] for h in samples)/total
        expected_log_likelihood += float(mass)*log(float(likelihood))
    assert mean_likelihood == px
    assert expected_log_likelihood < log(float(px))
    results[count] = dict(mean_likelihood=str(mean_likelihood),
        mean_model_update=str(mean_p), mean_wake_recognition_update=str(mean_q),
        expected_log_likelihood=expected_log_likelihood)
assert results[1]['mean_model_update'] == '-1/4'
assert results[2]['mean_model_update'] == '-1/10'
assert results[1]['mean_wake_recognition_update'] == '0'
assert results[2]['mean_wake_recognition_update'] == '3/20'

# If recognition ignores x, sleep fits the model's prior marginal h, whereas
# a wake recognition target on data x=1 fits the conditional posterior.
sleep_q_gradient = sum(F(1,2)*q_score[h] for h in joint)
assert sleep_q_gradient == F(1,4) != exact_wake_q_gradient

# The exact free-energy identity is separate from either practical sleep update.
free_energy = sum(float(proposal[h])*log(float(proposal[h]/joint[h])) for h in joint)
kl_q_posterior = sum(float(proposal[h])*log(float(proposal[h]/posterior[h])) for h in joint)
assert abs(free_energy - (-log(float(px))+kl_q_posterior)) < 1e-12
assert kl_q_posterior > 0
print(json.dumps(dict(status='PASS',posterior_h1=str(posterior[1]),
    exact_model_gradient=str(exact_p_gradient), exact_data_wake_q_gradient=str(exact_wake_q_gradient),
    model_sleep_q_gradient=str(sleep_q_gradient), finite_sample_counts=results,
    exact_log_likelihood=log(float(px)), free_energy=free_energy,
    kl_recognition_to_posterior=kl_q_posterior,
    interpretation='Finite examples distinguish objectives, unbiased likelihood estimates and biased normalized gradients. No universal monotonic bias or variance claim and no author-code behavior is inferred.'),indent=2))
