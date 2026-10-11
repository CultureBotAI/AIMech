"""Original finite estimator examples; no author implementation or model training."""
from fractions import Fraction as F
from itertools import product
import json


def calculate():
    p = F(1, 4)
    prob = {0: 1-p, 1: p}
    score = lambda h: h-p
    exact = p*(1-p)
    baseline_checks = {}
    for baseline in [F(0), p, 1-p, F(2)]:
        values = {h: (h-baseline)*score(h) for h in [0, 1]}
        mean = sum(prob[h]*values[h] for h in [0, 1])
        variance = sum(prob[h]*(values[h]-mean)**2 for h in [0, 1])
        assert mean == exact
        baseline_checks[str(baseline)] = dict(mean=str(mean), variance=str(variance))
    assert baseline_checks['3/4']['variance'] == '0'
    assert baseline_checks['1/4']['variance'] != '0'
    dependent_mean = sum(prob[h]*(h-h)*score(h) for h in [0, 1])
    assert dependent_mean == 0 and dependent_mean != exact

    # A differentiable extension with f(0)=0, f(1)=1 but f'(0)=f'(1)=-1.
    # One Bernoulli unit thus has a positive true logit gradient while the
    # identity straight-through estimate is always negative.
    f = lambda h: -h+6*h*h-4*h*h*h
    derivative = lambda h: -1+12*h-12*h*h
    assert f(0) == 0 and f(1) == 1
    st_mean = sum(prob[h]*derivative(h) for h in [0, 1])
    assert st_mean == -1 and exact > 0
    # The printed Bengio Eq. 3 uses U>p, whereas its proof uses P(h=1)=p.
    printed_probability = 1-p
    printed_score_mean = printed_probability-p
    assert printed_probability == F(3,4) and printed_score_mean == F(1,2)

    # NVIL-style current-batch running centering, with normalization inactive.
    # q(h|x)=1/2; choose P(x,h=0)=exp(-1)/2 and P(x,h=1)=1/2.
    # This is a valid joint slice (remaining mass can lie at another x), and
    # its learning signals log(P/q) are exactly -1 and 0.
    # At equal logits the raw inference gradient is 1/4.
    alpha, n = F(4,5), 2
    raw_mean = F(0)
    centered_mean = F(0)
    traces = []
    for sample in product([0,1], repeat=n):
        signals = [F(h-1) for h in sample]
        batch_mean = sum(signals)/n
        population_var = sum((v-batch_mean)**2 for v in signals)/n
        unbiased_var = sum((v-batch_mean)**2 for v in signals)/(n-1)
        # Both conventional batch-variance denominators keep sqrt(v)<1 here.
        assert (1-alpha)*max(population_var, unbiased_var) < 1
        new_c = (1-alpha)*batch_mean  # prior c=0, updated before the gradient
        raw = sum(signals[i]*(F(sample[i])-F(1,2)) for i in range(n))/n
        centered = sum((signals[i]-new_c)*(F(sample[i])-F(1,2)) for i in range(n))/n
        raw_mean += raw/F(4)
        centered_mean += centered/F(4)
        traces.append(dict(sample=list(sample),raw=str(raw),centered=str(centered)))
    assert raw_mean == F(1,4) and centered_mean == F(9,40)
    assert centered_mean/raw_mean == 1-(1-alpha)/n
    return dict(bernoulli_baselines=baseline_checks,action_dependent_baseline_mean=str(dependent_mean),
                straight_through=dict(loss='-h+6*h^2-4*h^3',expected_surrogate=str(st_mean),exact_logit_gradient=str(exact)),
                printed_threshold=dict(p=str(p),probability_for_U_greater_than_p=str(printed_probability),expected_h_minus_p=str(printed_score_mean)),
                current_batch_centering=dict(alpha=str(alpha),batch_size=n,raw_expectation=str(raw_mean),centered_expectation=str(centered_mean),traces=traces),
                scope='Exact rational enumeration and polynomial derivatives for small constructed examples. This is not an author-code run, a numerical benchmark, or a general convergence theorem.')


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
