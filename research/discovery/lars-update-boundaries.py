"""Constructed LARS update algebra, not a training or implementation benchmark."""
import json
from math import isclose, sqrt


def norm(v):
    return sqrt(sum(x*x for x in v))


def fresh(w, g, beta=0., eta=.1, gamma=.2):
    denominator = norm(g) + beta*norm(w)
    if denominator == 0:
        raise ZeroDivisionError('The primary formula does not define a zero denominator.')
    local = eta*norm(w)/denominator
    return [gamma*local*(x+beta*y) for x, y in zip(g, w)]


def result():
    w = [3., 4.]
    g = [.6, .8]
    a = fresh(w, g)
    scaled = fresh(w, [100*x for x in g])
    assert all(isclose(x, y) for x, y in zip(a, scaled))
    assert isclose(norm(a), .2*.1*norm(w))
    # Two consecutive steps with a constant linear-objective gradient and v0=0.
    w1 = [x-y for x, y in zip(w, a)]
    b = fresh(w1, g)
    v2 = [.9*x+y for x, y in zip(a, b)]
    assert norm(v2) > .2*.1*norm(w1)
    # Sum of norms in the primary denominator differs from norm of the sum.
    opposite = [-3., -4.]
    decay = fresh(w, opposite, beta=.5)
    combined = [x+.5*y for x, y in zip(opposite, w)]
    combined_normalized = [.2*.1*norm(w)*x/norm(combined) for x in combined]
    assert not isclose(norm(decay), norm(combined_normalized))
    assert norm(decay) <= .2*.1*norm(w)
    # With g=0 and beta>0, the fresh shrinkage coefficient cancels beta.
    zero_gradient = fresh(w, [0., 0.], beta=.5)
    assert all(isclose(x, .2*.1*y) for x, y in zip(zero_gradient, w))
    zero_weight = fresh([0., 0.], g)
    assert zero_weight == [0., 0.]
    try:
        fresh([0., 0.], [0., 0.])
    except ZeroDivisionError:
        zero_denominator = 'undefined in the primary formula'
    else:
        raise AssertionError('Unexpected zero-denominator policy')
    return dict(no_decay_increment=a, no_decay_norm=norm(a),
                positive_gradient_rescaling_same_increment=scaled,
                second_fresh_norm=norm(b), second_momentum_displacement_norm=norm(v2),
                coupled_decay_increment_norm=norm(decay),
                norm_of_combined_direction_alternative=norm(combined_normalized),
                zero_gradient_with_positive_decay=zero_gradient,
                zero_weight_nonzero_gradient=zero_weight,
                zero_denominator=zero_denominator,
                interpretation='Algebra on constructed two-dimensional states using Equation6 and a consistently indexed momentum recurrence. No source code, fitted model, training or empirical performance was executed.')


if __name__ == '__main__':
    print(json.dumps(result(), indent=2))
