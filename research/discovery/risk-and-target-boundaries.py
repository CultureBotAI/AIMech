"""Original finite arithmetic for source conventions; no model or author code."""
from math import exp, isclose, log
import json


def calculate():
    q = (0.8, 0.2)
    target = (1, 0)
    binary_ce = -sum(y * log(p) + (1-y) * log(1-p) for y, p in zip(target, q))
    printed_entropy = -sum(p * log(p) for p in q)
    categorical_hard_ce = -log(q[0])
    assert not isclose(binary_ce, printed_entropy)
    assert not isclose(categorical_hard_ce, printed_entropy)
    prediction = (0.6, 0.4)
    cross_entropy = -sum(p * log(r) for p, r in zip(q, prediction))
    kl = sum(p * log(p/r) for p, r in zip(q, prediction))
    assert isclose(cross_entropy-kl, printed_entropy)
    # With detached q and mask, both objectives have softmax-logit gradient r-q.
    fixed_target_logit_gradient = [r-p for p, r in zip(q, prediction)]
    eta = 0.6
    label_confidences = (0.6, 0.8)
    kept = [p <= eta for p in label_confidences]
    masked_sum = sum(-log(p) for p, retain in zip(label_confidences, kept) if retain)
    retained_mean = masked_sum/max(sum(kept), 1)
    full_batch_mean = masked_sum/len(kept)
    assert kept == [True, False]
    assert isclose(retained_mean, 2*full_batch_mean)
    classes = 10
    start = 1/classes
    exp_start = start+(1-start)*exp(-5)
    log_end = start+(1-start)*(1-exp(-5))
    assert exp_start > start and log_end < 1
    return {'scope':'Curator arithmetic; not model training, author-code execution or an author-issued correction.',
            'pseudo_label':{'probabilities':q,'hard_target_binary_ce':binary_ce,
                            'hard_target_categorical_ce':categorical_hard_ce,
                            'printed_entropy_expression':printed_entropy,
                            'conclusion':'These loss values are not equal; shared confidence-sharpening motivation does not establish objective identity.'},
            'uda':{'soft_target_cross_entropy':cross_entropy,'kl':kl,
                   'difference_target_entropy':cross_entropy-kl,
                   'same_fixed_target_logit_gradient':fixed_target_logit_gradient},
            'tsa':{'threshold':eta,'label_confidences':label_confidences,
                   'retained':kept,'retained_mean':retained_mean,'full_batch_mean':full_batch_mean,
                   'ten_class_exp_schedule_start':exp_start,'ten_class_log_schedule_end':log_end}}


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
