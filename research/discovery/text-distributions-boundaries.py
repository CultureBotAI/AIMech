"""Finite curator calculations; no author implementation or empirical benchmark."""
from fractions import Fraction as F
from itertools import product
from math import exp, log, isclose
import json


def close(a, b, tol=1e-7):
    assert isclose(a, b, rel_tol=tol, abs_tol=tol), (a, b)


def softmax(x):
    e = [exp(v - max(x)) for v in x]
    return [v / sum(e) for v in e]


def main():
    # Two categorical words and one binary hidden unit: W_A=log 2, W_B=0.
    seqs = list(product((0, 1), repeat=2))  # 1 denotes word A.
    unnormalized = {s: F(1 + 2 ** sum(s)) for s in seqs}
    z = sum(unnormalized.values())
    assert z == 13
    seq_prob = {s: v / z for s, v in unnormalized.items()}
    count_prob = {n: sum(v for s, v in seq_prob.items() if sum(s) == n) for n in range(3)}
    assert count_prob == {0: F(2, 13), 1: F(6, 13), 2: F(5, 13)}
    assert seq_prob[(1, 0)] == seq_prob[(0, 1)] == F(3, 13)
    base_z = sum(F(1) for _s in seqs for _h in (0, 1))
    assert base_z == 8 and base_z != 2  # K**D * 2**H, not just 2**H.
    scaled_hidden = F(4, 5)  # D=2, a=log 2, zero interaction.
    unscaled_hidden = F(2, 3)
    assert scaled_hidden != unscaled_hidden
    # One Gibbs reconstruction from AA: exact finite transition, not training.
    cd1 = {}
    for s in seqs:
        n = sum(s)
        cd1[s] = F(4, 5) * F(2, 3) ** n * F(1, 3) ** (2 - n) + F(1, 5) * F(1, 2) ** 2
    assert sum(cd1.values()) == 1 and cd1[(1, 1)] == F(73, 180)
    assert cd1[(1, 1)] != seq_prob[(1, 1)]

    # SAGE: sparse log deviations are not sparse categorical probabilities.
    m = [log(.5), log(.3), log(.2)]
    eta = [log(2), 0., 0.]
    p = softmax([x + y for x, y in zip(m, eta)])
    for actual, expected in zip(p, [2/3, 1/5, 2/15]):
        close(actual, expected)
    assert all(v > 0 for v in p) and p[1] != .3
    close(p[1] / p[2], .3 / .2)
    shifted = softmax([x + y + 7 for x, y in zip(m, eta)])
    for a, b in zip(p, shifted):
        close(a, b)
    facet = [0., log(3), 0.]
    additive = softmax([x + y + t for x, y, t in zip(m, eta, facet)])
    other = softmax([x + y for x, y in zip(m, facet)])
    mixture = [(x + y) / 2 for x, y in zip(p, other)]
    assert any(abs(x - y) > .01 for x, y in zip(additive, mixture))
    counts, precision = [10., 6., 4.], [2., 3., 4.]
    def objective(e):
        logits = [x + y for x, y in zip(m, e)]
        return sum(c*x for c,x in zip(counts,e)) - sum(counts)*log(sum(exp(x) for x in logits)) - sum(t*x*x for t,x in zip(precision,e))/2
    def gradient(e):
        b = softmax([x+y for x,y in zip(m,e)])
        return [c-sum(counts)*v-t*x for c,v,t,x in zip(counts,b,precision,e)]
    grad = gradient(eta)
    hessian = [[20*p[i]*p[j] - (20*p[i]+precision[i] if i==j else 0) for j in range(3)] for i in range(3)]
    eps = 1e-5
    for j in range(3):
        plus, minus = eta.copy(), eta.copy()
        plus[j] += eps; minus[j] -= eps
        close((objective(plus)-objective(minus))/(2*eps), grad[j])
        gp, gm = gradient(plus), gradient(minus)
        for i in range(3):
            close((gp[i]-gm[i])/(2*eps), hessian[i][j])
    a, deviation = 2., 2.
    b = deviation**2/(a-1)
    inverse_variance = 1/((a-1)*b)
    close(inverse_variance, 1/deviation**2)
    assert inverse_variance != deviation**2

    # Hierarchical softmax: probabilities of leaves, not a flat softmax of nodes.
    qroot, qleft, qright = .6, .8, .3
    leaves = [qroot*qleft, qroot*(1-qleft), (1-qroot)*qright, (1-qroot)*(1-qright)]
    close(sum(leaves), 1)
    def nll(logits):
        return -sum(log(1/(1+exp(-x))) for x in logits)
    logits = [log(qroot/(1-qroot)), log(qleft/(1-qleft))]
    for j, expected in enumerate([qroot-1, qleft-1]):
        plus, minus = logits.copy(), logits.copy()
        plus[j] += eps; minus[j] -= eps
        close((nll(plus)-nll(minus))/(2*eps), expected)
    # Distinct leaves can map to one word only by summing their disjoint masses.
    word_masses = [leaves[0]+leaves[2], leaves[1], leaves[3]]
    close(sum(word_masses), 1)
    # Three equally frequent symbols: an optimal binary prefix tree has depths 1,2,2.
    expected_depth = F(5, 3)
    assert float(expected_depth) > log(3, 2)
    # A full binary comb with eight leaves is not logarithmic in worst-case depth.
    assert 7 > log(8, 2)
    print(json.dumps({
        'scope': 'Original finite curator calculations, not author code or empirical results',
        'replicated_softmax': {'Z': int(z), 'sequence_AA': str(seq_prob[(1,1)]), 'sequence_AB': str(seq_prob[(1,0)]), 'count_one_A': str(count_prob[1]), 'zero_parameter_Z': int(base_z), 'D_scaled_hidden_probability': str(scaled_hidden), 'unscaled_hidden_probability': str(unscaled_hidden), 'one_step_AA': str(cd1[(1,1)])},
        'sage': {'probabilities': p, 'additive_facets': additive, 'probability_mixture': mixture, 'gradient': grad, 'hessian': hessian, 'gamma_inverse_variance': inverse_variance, 'printed_eta_squared': deviation**2},
        'hierarchical_softmax': {'leaf_probabilities': leaves, 'merged_word_probabilities': word_masses, 'three_symbol_mean_depth': float(expected_depth), 'log2_three': log(3,2), 'eight_leaf_comb_depth': 7},
        'result': 'PASS'
    }, indent=2))


if __name__ == '__main__':
    main()
