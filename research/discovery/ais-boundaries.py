"""Exact finite curator checks of AIS weights; no author-code execution."""
from fractions import Fraction as F
from itertools import product
from math import log
import json


def normalize(f):
    return [F(v, sum(f)) for v in f]


def invariant(p, t):
    return all(sum(row) == 1 and all(v >= 0 for v in row) for row in t) and all(sum(p[i] * t[i][j] for i in range(len(p))) == p[j] for j in range(len(p)))


def paths(functions, transitions, check=True):
    """functions are f0,...,fn; Tj maps xj to x(j-1)."""
    n = len(functions) - 1
    k = len(functions[0])
    assert n >= 1 and len(transitions) == n-1
    assert all(len(f) == k and all(v > 0 for v in f) for f in functions)
    if check:
        for j, t in enumerate(transitions, 1):
            assert invariant(normalize(functions[j]), t)
    out = []
    for states in product(range(k), repeat=n):
        probability = normalize(functions[n])[states[n-1]]
        for j, t in enumerate(transitions, 1):
            probability *= t[states[j]][states[j-1]]
        weight = F(1)
        for j in range(1, n+1):
            weight *= F(functions[j-1][states[j-1]], functions[j][states[j-1]])
        if probability:
            out.append((probability, states[0], weight))
    assert sum(p for p, _, _ in out) == 1
    return out


def weighted_mass(out, k):
    return [sum(p*w for p, end, w in out if end == j) for j in range(k)]


def guarded_path_weight(functions, states):
    """Evaluate chronological factors, stopping before later 0/0 ratios."""
    weight = F(1)
    evaluations = 0
    for j in range(len(functions)-1, 0, -1):
        numerator = functions[j-1][states[j-1]]
        denominator = functions[j][states[j-1]]
        assert denominator > 0
        evaluations += 1
        if numerator == 0:
            return F(0), evaluations
        weight *= F(numerator, denominator)
    return weight, evaluations


def main():
    target = [1, 2, 7]
    bridge = [1, 1, 1]
    base = [3, 2, 1]
    cycle = [[F(j == (i+1)%3) for j in range(3)] for i in range(3)]
    identity = [[F(i == j) for j in range(3)] for i in range(3)]
    uniform = normalize(bridge)
    assert invariant(uniform, cycle)
    assert uniform[0]*cycle[0][1] != uniform[1]*cycle[1][0]
    out = paths([target, bridge, base], [cycle])
    expected_mass = [F(v, sum(base)) for v in target]
    assert weighted_mass(out, 3) == expected_mass
    z = sum(p*w for p, _, w in out)
    assert z == F(5, 3)
    endpoint = [sum(p for p, end, _ in out if end == j) for j in range(3)]
    assert endpoint == [F(1,6),F(1,2),F(1,3)]
    assert endpoint != normalize(target)
    one_run_expectation = endpoint[2]
    two_run_expectation = sum(p*q*(w*(i==2)+v*(j==2))/(w+v) for p,i,w in out for q,j,v in out)
    assert one_run_expectation != F(7,10) and two_run_expectation != F(7,10)
    log_estimate_mean = sum(float(p)*log(float(w)) for p,_,w in out)
    assert log_estimate_mean < log(float(z))
    plain = paths([target,base], [])
    idle = paths([target,bridge,base], [identity])
    assert plain == idle
    reset = [[F(j==0) for j in range(3)] for _ in range(3)]
    assert not invariant(uniform,reset)
    wrong = paths([target,bridge,base],[reset],check=False)
    assert sum(p*w for p,_,w in wrong) == F(1,2) != z
    # Exhaust an explicit finite family of invariant refresh/identity mixtures.
    count = 0
    for f0 in product([1,2],repeat=3):
        for f1 in product([1,2],repeat=3):
            p1 = normalize(f1)
            for alpha in [F(0),F(1,2),F(1)]:
                t = [[(1-alpha)*F(i==j)+alpha*p1[j] for j in range(3)] for i in range(3)]
                case = paths([f0,f1,base],[t])
                assert weighted_mass(case,3) == [F(v,sum(base)) for v in f0]
                count += 1
    assert count == 192
    # A truncated-support base cannot recover target mass outside its support.
    unsupported_target=[1,1,2]
    unsupported_base=[1,1,0]
    invalid_mean=sum(F(unsupported_base[i],sum(unsupported_base))*F(unsupported_target[i],unsupported_base[i]) for i in [0,1])
    assert invalid_mean == 1 and F(sum(unsupported_target),sum(unsupported_base)) == 2
    # Valid nested supports can produce a zero-weight path. Never evaluate its
    # later 0/0 ratio or an observable at an unnecessary endpoint.
    nested = [[1,0], [1,0], [1,1]]
    assert invariant(normalize(nested[1]), [[F(1),F(0)],[F(0),F(1)]])
    assert all(not nested[j-1][i] or nested[j][i] for j in [1,2] for i in [0,1])
    try:
        F(nested[0][1], nested[1][1])
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError('The unguarded second ratio must be undefined')
    guarded = [guarded_path_weight(nested,[i,i]) for i in [0,1]]
    assert guarded == [(F(1),2),(F(0),1)]
    guarded_mean = sum(F(1,2)*w for w,_ in guarded)
    assert guarded_mean == F(sum(nested[0]),sum(nested[2])) == F(1,2)
    return dict(nonreversible_example=dict(target=target,bridge=bridge,base=base,weighted_endpoint_mass=[str(x) for x in expected_mass],expected_weight=str(z),unweighted_endpoint_probability=[str(x) for x in endpoint],target_probability=[str(x) for x in normalize(target)],self_normalized_indicator_expected_value=dict(one_run=str(one_run_expectation),two_runs=str(two_run_expectation),target='7/10'),expected_log_weight=log_estimate_mean,log_expected_weight=log(float(z))),identity_kernel_reduces_to_plain_importance_sampling=True,noninvariant_reset_expected_weight='1/2',invariant_family_cases=count,violated_support_example=dict(expected_weight=str(invalid_mean),actual_normalizing_ratio='2'),nested_support_zero_path=dict(functions=nested,guarded_weights=[str(w) for w,_ in guarded],ratio_evaluations=[n for _,n in guarded],expected_weight=str(guarded_mean),actual_normalizing_ratio='1/2',zero_path_stops_before_undefined_ratio=True),scope='Finite exact laws and counterexamples only. No continuous-state theorem certification, variance bound, benchmark replication, author implementation, paid provider or training.')


if __name__=='__main__':
    print(json.dumps(main(),indent=2))
