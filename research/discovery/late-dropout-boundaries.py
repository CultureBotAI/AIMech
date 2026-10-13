"""Constructed affine gradient-map compositions; no empirical training run."""
import json


def result():
    # For squared error at x=y=1, inverted Bernoulli dropout with p=1/2
    # has expected gradient 2w-1. The no-dropout gradient is w-1.
    # At step size 1/4 these give two affine maps.
    ordinary=lambda w:0.75*w+0.25
    masked_expectation=lambda w:0.5*w+0.25
    initial=0.0
    early_then_off=ordinary(masked_expectation(initial))
    late_after_onset=masked_expectation(ordinary(initial))
    assert early_then_off==0.4375 and late_after_onset==0.375
    assert early_then_off!=late_after_onset
    return dict(initial_value=initial,early_then_off=early_then_off,
                late_after_onset=late_after_onset,
                interpretation='The same two expected-gradient maps in different order need not commute. Equal numbers of dropout and no-dropout steps do not guarantee the same optimization trajectory. This is a deterministic algebra construction, not training or a performance comparison of the source methods.')


if __name__=='__main__':print(json.dumps(result(),indent=2,sort_keys=True))
