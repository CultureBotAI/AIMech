"""Exact curator certificates for Smola, Friess and Scholkopf (NIPS 1998).

These finite rational examples check objective scaling and scope boundaries.
No optimization solver, model training, or historical benchmark is executed.
"""
from fractions import Fraction as F
import json


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def svr(x, y, lam, epsilon, w, beta, alpha, alpha_star, fixed_beta=False):
    """Linear kernel and constant supplied basis; normalized Eq. 6 dual."""
    x, y, alpha, alpha_star = [list(map(F, v)) for v in (x, y, alpha, alpha_star)]
    lam, epsilon, w, beta = map(F, (lam, epsilon, w, beta))
    assert lam > 0 and epsilon >= 0
    a = [u - v for u, v in zip(alpha, alpha_star)]
    cap = 1 / lam
    assert all(0 <= z <= cap for z in alpha + alpha_star)
    assert fixed_beta or sum(a) == 0
    assert w == dot(a, x)
    residual = [yi - (w * xi + beta) for xi, yi in zip(x, y)]
    lower_slack = [max(F(0), r - epsilon) for r in residual]
    upper_slack = [max(F(0), -r - epsilon) for r in residual]
    for r, lo, up, ap, am in zip(residual, lower_slack, upper_slack, alpha, alpha_star):
        assert r <= epsilon + lo and -r <= epsilon + up
        assert ap * (epsilon + lo - r) == 0
        assert am * (epsilon + up + r) == 0
        assert (cap - ap) * lo == 0 and (cap - am) * up == 0
    raw_primal = lam * w * w / 2 + sum(lower_slack + upper_slack)
    adjusted_y = [yi - beta for yi in y] if fixed_beta else y
    normalized_dual = dot(adjusted_y, a) - w * w / 2 - epsilon * sum(alpha + alpha_star)
    assert raw_primal == lam * normalized_dual
    return dict(w=str(w), beta=str(beta), raw_primal=str(raw_primal),
                normalized_dual=str(normalized_dual), all_kkt_products_zero=True)


def lp(x, y, lam, epsilon, coefficients, beta, dual):
    """Eq. 9 finite dictionary: raw dual |K^T t|<=lambda, sum(t)=0."""
    x, y, coefficients, dual = [list(map(F, v)) for v in (x, y, coefficients, dual)]
    lam, epsilon, beta = map(F, (lam, epsilon, beta))
    assert lam > 0 and epsilon >= 0 and sum(dual) == 0
    assert all(abs(t) <= 1 for t in dual)
    gram = [[u * v for v in x] for u in x]
    correlations = [sum(gram[i][j] * dual[i] for i in range(len(x))) for j in range(len(x))]
    assert all(abs(v) <= lam for v in correlations)
    prediction = [dot(row, coefficients) + beta for row in gram]
    residual = [yi - fi for yi, fi in zip(y, prediction)]
    loss = sum(max(F(0), abs(r) - epsilon) for r in residual)
    raw_primal = loss + lam * sum(map(abs, coefficients))
    raw_dual = dot(y, dual) - epsilon * sum(map(abs, dual))
    assert raw_primal == raw_dual
    return dict(coefficients=list(map(str, coefficients)), predictions=list(map(str, prediction)),
                raw_primal=str(raw_primal), raw_dual=str(raw_dual), primal_dual_equality=True)


def certificates():
    joint = svr([1, 3], [1, 3], F(1, 2), 0, 1, 0, [0, F(1, 2)], [F(1, 2), 0])
    # beta=2 minimizes the initial constant-only absolute loss (median interval [1,3]).
    assert abs(F(1)-2) + abs(F(3)-2) == 2
    sequential = svr([1, 3], [1, 3], F(1, 2), 0, F(1, 3), 2,
                     [0, F(7, 9)], [2, 0], fixed_beta=True)
    assert F(joint['raw_primal']) == F(1, 4)
    assert F(sequential['raw_primal']) == F(49, 36) > F(joint['raw_primal'])
    # Equal lambda does not identify the two regularizers or their fitted functions.
    quadratic = svr([-1, 1], [-1, 1], 3, 0, F(2, 3), 0, [0, F(1, 3)], [F(1, 3), 0])
    linear = lp([-1, 1], [-1, 1], 3, 0, [0, 0], 0, [-1, 1])
    assert F(quadratic['raw_primal']) == F(4, 3)
    assert F(linear['raw_primal']) == 2
    # Two different coefficient vectors represent f(x)=x and have equal L1 cost.
    sparse_left = lp([-1, 1], [-1, 1], F(1, 2), 0, [-1, 0], 0, [F(-1, 4), F(1, 4)])
    sparse_right = lp([-1, 1], [-1, 1], F(1, 2), 0, [0, 1], 0, [F(-1, 4), F(1, 4)])
    assert sparse_left['predictions'] == sparse_right['predictions']
    # Their average is another optimum with two nonzero coefficients.
    dense = lp([-1, 1], [-1, 1], F(1, 2), 0, [F(-1, 2), F(1, 2)], 0, [F(-1, 4), F(1, 4)])
    assert dense['raw_primal'] == sparse_left['raw_primal'] == '1/2'
    return dict(joint_fit=joint, one_pass_fit=sequential, quadratic_regularizer=quadratic,
                coefficient_l1_regularizer=linear, alternative_lp_optima=[sparse_left, sparse_right, dense],
                limits='Finite curator-derived certificates, not performance evidence, a general convergence theorem, or an audit of all backfitting algorithms.')


if __name__ == '__main__':
    print(json.dumps(certificates(), indent=2))
