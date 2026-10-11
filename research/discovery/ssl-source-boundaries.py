"""Finite curator checks of source conventions; no model or benchmark execution."""
from fractions import Fraction as F
import json
import math


def calculate():
    predictions = [(F(9, 10), F(1, 10)), (F(1, 10), F(9, 10))]
    prior = (F(4, 5), F(1, 5))
    running = tuple(sum(q[j] for q in predictions) / 2 for j in range(2))
    aligned = []
    for q in predictions:
        weighted = [q[j] * prior[j] / running[j] for j in range(2)]
        aligned.append(tuple(v / sum(weighted) for v in weighted))
    aligned_mean = tuple(sum(q[j] for q in aligned) / 2 for j in range(2))
    assert running == (F(1, 2), F(1, 2))
    assert aligned_mean != prior

    confidence, threshold = [F(19, 20), F(9, 10)], F(19, 20)
    inclusive = sum(q >= threshold for q in confidence)
    strict = sum(q > threshold for q in confidence)
    assert (inclusive, strict) == (1, 0)
    full_batch_loss = inclusive * math.log(2) / len(confidence)
    retained_only_loss = math.log(2)
    assert full_batch_loss == retained_only_loss / 2

    old_student, new_student, old_teacher, decay = F(0), F(2), F(0), F(1, 2)
    pre_step_teacher = decay * old_teacher + (1 - decay) * old_student
    post_step_teacher = decay * old_teacher + (1 - decay) * new_student
    assert (pre_step_teacher, post_step_teacher) == (0, 1)
    return {
        "distribution_alignment": {
            "inputs": [[str(v) for v in q] for q in predictions],
            "prior": [str(v) for v in prior],
            "running": [str(v) for v in running],
            "aligned": [[str(v) for v in q] for q in aligned],
            "aligned_mean": [str(v) for v in aligned_mean],
            "equals_prior": False,
        },
        "threshold_and_denominator": {
            "confidence": [str(v) for v in confidence], "threshold": str(threshold),
            "inclusive_count": inclusive, "strict_count": strict,
            "full_batch_masked_ce": full_batch_loss,
            "retained_only_ce": retained_only_loss,
        },
        "ema_order": {
            "old_student": str(old_student), "new_student": str(new_student),
            "old_teacher": str(old_teacher), "decay": str(decay),
            "pre_step_teacher": str(pre_step_teacher),
            "post_step_teacher": str(post_step_teacher),
        },
    }


if __name__ == "__main__":
    print(json.dumps(calculate(), indent=2))
