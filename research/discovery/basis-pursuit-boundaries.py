"""Exact finite certificates for curated basis-pursuit scope, not a solver."""
from fractions import Fraction as Q
import json


def dot(a, b):
    assert len(a) == len(b)
    return sum(x * y for x, y in zip(a, b))


def synth(columns, coefficients):
    return tuple(dot(row, coefficients) for row in zip(*columns))


def l1(x):
    return sum(abs(t) for t in x)


def certificate(columns, signal, coefficients, dual):
    assert synth(columns, coefficients) == signal
    correlations = tuple(dot(column, dual) for column in columns)
    assert max(map(abs, correlations)) <= 1
    assert l1(coefficients) == dot(signal, dual)
    return dict(objective=str(l1(coefficients)), support=sum(t != 0 for t in coefficients),
                dual_correlations=list(map(str, correlations)))


def main():
    e1, e2, e3 = (Q(1), Q(0), Q(0)), (Q(0), Q(1), Q(0)), (Q(0), Q(0), Q(1))
    b = (Q(8, 9), Q(4, 9), Q(1, 9))
    columns = (e1, e2, e3, b)
    assert all(dot(c, c) == 1 for c in columns)
    signal = (Q(1, 9), Q(-4, 9), Q(-1, 9))
    sparse = (Q(1), Q(0), Q(0), Q(-1))
    optimum = (*signal, Q(0))
    dual = (Q(1), Q(-1), Q(-1))
    assert synth(columns, sparse) == signal and l1(sparse) == 2
    # No one-column representation: each column fails a pairwise collinearity test.
    assert all(any(signal[i] * c[j] != signal[j] * c[i]
                   for i in range(3) for j in range(3)) for c in columns)
    less_sparse = certificate(columns, signal, optimum, dual)
    # Strict fourth dual constraint forces coefficient four to zero at optimum.
    # The remaining identity columns then fix all three coefficients uniquely.
    assert abs(dot(b, dual)) < 1
    duplicate = ( (Q(1),), (Q(1),) )
    tied = [certificate(duplicate, (Q(1),), a, (Q(1),))
            for a in [(Q(1), Q(0)), (Q(0), Q(1)), (Q(1, 2), Q(1, 2))]]
    rescaled = certificate(((Q(1),), (Q(2),)), (Q(1),),
                          (Q(0), Q(1, 2)), (Q(1, 2),))
    # Scalar penalized denoising: stationarity at positive coefficient 1-lambda.
    lam = Q(1, 2)
    penalized_coefficient = 1 - lam
    assert penalized_coefficient - 1 + lam == 0
    assert penalized_coefficient != 1  # Exact BP coefficient is one.
    # lambda=0 removes L1 preference altogether, unlike the positive-lambda limit.
    assert synth(duplicate, (Q(2), Q(-1))) == (Q(1),)
    assert l1((Q(2), Q(-1))) > 1
    print(json.dumps(dict(unit_column_l0_counterexample=dict(
        bp=less_sparse, bp_unique=True, minimum_l0=2, two_sparse_l1='2'),
        duplicate_column_optima=tied, scaled_column_optimum=rescaled,
        scalar_bp='1', scalar_bpdn=str(penalized_coefficient),
        zero_penalty_non_bp_interpolant=['2', '-1']), indent=2))


if __name__ == '__main__':
    main()
