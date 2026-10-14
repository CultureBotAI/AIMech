"""Finite fixed-sample ABRA boundaries; curator arithmetic, not author software."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import importlib.util
import json

spec = importlib.util.spec_from_file_location('abra_pair', Path(__file__).with_name('abra-pair-boundaries.py'))
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def main():
    p = F(1, 3)
    outcomes = []
    for count in [1, 2, 4]:
        mean = second = F(0)
        zero_probability = F(0)
        for bits in product([0, 1], repeat=count):
            ones = sum(bits)
            probability = p ** ones * (1-p) ** (count-ones)
            estimate = F(ones, count)
            mean += probability * estimate
            second += probability * estimate * estimate
            if not ones:
                zero_probability += probability
        variance = second-mean*mean
        assert mean == p and variance == p*(1-p)/count
        assert zero_probability == (1-p)**count
        outcomes.append(dict(count=count,mean=str(mean),variance=str(variance),
                             zero_estimate_probability=str(zero_probability),
                             error_when_estimate_zero='1/3'))
    delta = .05
    zero_bounds = [dict(count=count,xi_delta=base.deviation(0,count,delta),
                       xi_stage_one=base.deviation(0,count,delta/2))
                   for count in [1,16,64]]
    assert zero_bounds[1]['xi_stage_one'] > .5
    assert zero_bounds[2]['xi_stage_one'] < .5
    assert all(x['xi_stage_one'] >= x['xi_delta'] for x in zero_bounds)
    return dict(path3_fixed_draws=outcomes,all_zero_vectors=zero_bounds,
                interpretation='With S=16 the fixed algorithm still returns its bound even though it exceeds epsilon=.5; epsilon is not its input. Using eta=delta/2 preserves the literal first-stage allocation and is more conservative than a one-shot eta=delta bound. Zero sampled centrality is not proof of zero true centrality.',
                scope='Exhaustive finite Bernoulli arithmetic and explicit floating confidence expressions. No author implementation or empirical guarantee.')


if __name__ == '__main__':
    print(json.dumps(main(),indent=2))
