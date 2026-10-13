"""Constructed mathematical checks, not a source-model or MCMC reproduction."""
from fractions import Fraction as F
from math import erfc, isclose, sqrt
from statistics import NormalDist
import json


def gaussian_frozen_parent():
    # mu~N(0,s2); lambda_i|mu~N(mu,t2); Ybar_i|lambda_i~N(lambda_i,v).
    # Conditional on remaining data: true mu and frozen parent draw are
    # independent N(m_rest,H); only the child is updated with Ybar_i.
    s2, t2, v, groups = 1.0, 1.0, 1.0, 3
    a = t2 + v
    h = 1 / (1 / s2 + (groups - 1) / a)
    w = t2 / a
    # Independent normal contributions: true parent, drawn parent, true child
    # residual, observation noise, conditional-child posterior draw noise.
    coefficients = [w * sqrt(h / t2), -w * sqrt(h / t2), w,
                    w * sqrt(v / t2), sqrt(v / a)]
    variance = sum(c * c for c in coefficients)
    closed_form = 1 + 2 * t2 * h / a**2
    assert isclose(variance, closed_form) and isclose(variance, 1.25)
    alpha = .05
    threshold = NormalDist().inv_cdf(1 - alpha / 2)
    rejection = erfc(threshold / sqrt(2 * variance))
    assert rejection > alpha
    return dict(parent_variance=h, standardized_score_argument_variance=variance,
                nominal_level=alpha, exact_rejection_probability=rejection,
                full_joint_posterior_identity='Not used by this frozen-parent construction')


def adaptive_rank_bound():
    # U uniform; p1=U, p2 is a measure-preserving permutation of intervals.
    alpha = F(1, 10)
    pieces = [(F(0), alpha / 2, alpha), (alpha / 2, alpha, F(0)),
              (alpha, 3 * alpha / 2, -alpha), (3 * alpha / 2, F(1), F(0))]
    images = sorted((lo + shift, hi + shift) for lo, hi, shift in pieces)
    assert images[0][0] == 0 and images[-1][1] == 1
    assert all(images[j][1] == images[j+1][0] for j in range(len(images)-1))
    mass = dict(smallest_rank=F(0),largest_rank=F(0),adaptive_minimum=F(0))
    for lo, hi, shift in pieces:
        cuts = sorted({lo, hi} | {x for x in [alpha / 2, alpha,
                      alpha / 2 - shift, alpha - shift] if lo < x < hi})
        for left, right in zip(cuts, cuts[1:]):
            u = (left + right) / 2
            psmall, plarge = sorted([u, u + shift])
            small, large = 2 * psmall <= alpha, plarge <= alpha
            for key, event in [('smallest_rank', small), ('largest_rank', large),
                               ('adaptive_minimum', small or large)]:
                if event:
                    mass[key] += right - left
    assert mass == dict(smallest_rank=F(1,10),largest_rank=F(1,20),adaptive_minimum=F(3,20))
    return dict(nominal_level=float(alpha),both_marginals_uniform=True,
                rejection_probabilities={k: float(v) for k,v in mass.items()},
                method='Exact interval lengths, not simulation')


def orientation_and_joint_identity():
    z = 3.0
    variance_score, precision_score = (z*z-1)/2, (1-z*z)/2
    variance_upper_tail = erfc(abs(z)/sqrt(2))
    precision_upper_tail = 1-variance_upper_tail
    assert variance_score == -precision_score and precision_upper_tail > .99
    # p~Beta(1,1), N|p~Binomial(2,p), observed N=1.
    # p|N=1~Beta(2,2), whereas defining p=N/2 gives a point mass.
    conditional_beta_variance = F(2*2, (2+2)**2*(2+2+1))
    assert conditional_beta_variance == F(1,20)
    return dict(z=z,variance_expansion_score=variance_score,
                precision_expansion_score=precision_score,
                variance_score_upper_tail=variance_upper_tail,
                precision_score_upper_tail=precision_upper_tail,
                beta_given_count_variance=float(conditional_beta_variance),
                count_ratio_given_count_variance=0)


if __name__ == '__main__':
    print(json.dumps(dict(frozen_parent=gaussian_frozen_parent(),
                         rank_minimum=adaptive_rank_bound(),
                         orientation=orientation_and_joint_identity()),indent=2))
