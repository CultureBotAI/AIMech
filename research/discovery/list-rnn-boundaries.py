"""Constructed checks of the paper's head-centered list update; no training."""
import json
import math


def step(old, left=0.0, right=0.0, insert=0.0, stay=0.0, value=0.9):
    assert math.isclose(left + right + insert + stay, 1.0)
    result = {}
    for i in old:
        proposal = value if i == 0 else old.get(i + 1, -1.0) if i < 0 else old[i]
        result[i] = (right * old.get(i + 1, -1.0) + left * old.get(i - 1, -1.0)
                     + insert * proposal + stay * old[i])
    return result


old = {-2: 0.1, -1: 0.2, 0: 0.3, 1: 0.4, 2: 0.5}
inserted = step(old, insert=1.0)
assert list(inserted.values()) == [0.2, 0.3, 0.9, 0.4, 0.5]
right = step(old, right=1.0)
assert right[0] == old[1]
roundtrip = step(right, left=1.0)
assert roundtrip[-2] == -1.0 and roundtrip[-1] == old[-1]
mixed = step(old, left=0.5, right=0.5)
assert math.isclose(mixed[0], 0.3)
sigmoid = lambda x: 1.0 / (1.0 + math.exp(-x))
from_mean = sigmoid(10 * mixed[0])
mean_hidden = 0.5 * sigmoid(10 * old[-1]) + 0.5 * sigmoid(10 * old[1])
assert not math.isclose(from_mean, mean_hidden)
assert step(old, stay=1.0) == old
print(json.dumps(dict(inserted=inserted, right_head=right[0], finite_window_roundtrip=roundtrip,
                     mixed_head=mixed[0], nonlinear_from_mean=from_mean,
                     mean_nonlinear=mean_hidden, caveat='Finite window and -1 boundary are curator assumptions, not a verified List RNN implementation.')))
