"""Annotation feedback and normalized-product examples, not a trained GGS-NN."""
from fractions import Fraction as F
from math import exp, log, isclose
import json


def softmax(xs):
    es = [exp(x-max(xs)) for x in xs]
    return [x/sum(es) for x in es]


# Different chosen output and annotation maps illustrate their distinct roles.
# This fixed state transition is not claimed to reproduce a learned sigmoid head.
annotations = [F(1, 5), F(4, 5), F(2, 5)]
initial = list(annotations)
outputs = []
states = []
for _ in range(3):
    states.append(list(map(str, annotations)))
    outputs.append(max(range(3), key=lambda i: annotations[i]))
    annotations = [annotations[2], annotations[0], annotations[1]]
assert outputs == [1, 2, 0]
frozen_outputs = [max(range(3), key=lambda i: initial[i])] * 3
assert frozen_outputs == [1, 1, 1]
assert annotations == initial

# Two per-graph distributions: summing logits requires final normalization.
p = [F(4, 5), F(1, 5)]
q = [F(3, 5), F(2, 5)]
raw = [x*y for x, y in zip(p, q)]
normalized = [x/sum(raw) for x in raw]
assert raw == [F(12, 25), F(2, 25)] and sum(raw) == F(14, 25)
assert normalized == [F(6, 7), F(1, 7)]
summed_logits = [log(float(x))+log(float(y)) for x, y in zip(p, q)]
got = softmax(summed_logits)
assert all(isclose(a, float(b), abs_tol=1e-12) for a, b in zip(got, normalized))
# Common offsets per graph cancel in the final softmax.
shifted = softmax([x+13-7 for x in summed_logits])
assert all(isclose(a,b,abs_tol=1e-12) for a,b in zip(got,shifted))
print(json.dumps(dict(annotation_states=states, outputs_with_annotation_updates=outputs,
                     outputs_with_frozen_annotations=frozen_outputs, prior_output_not_used=True,
                     raw_probability_product=list(map(str,raw)), raw_sum=str(sum(raw)),
                     normalized_product=list(map(str,normalized)), summed_logit_softmax=got,
                     scope='Constructed feedback and normalization boundaries only; not a learned GGS-NN, general graph algorithm, verifier or empirical reproduction.')))
