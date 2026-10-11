"""Original finite objective and Gaussian compatibility checks, not empirical fitting."""
from fractions import Fraction as F
from itertools import product
import json


def binary_checks():
    states = list(product((0, 1), repeat=4))
    groups = ((0, 2), (1, 3))

    def model(lam):
        weight = {x: lam ** sum(x[i] == x[i + 1] for i in range(3)) for x in states}
        z = sum(weight.values())
        assert z == 2 * (1 + lam) ** 3
        return {x: w / z for x, w in weight.items()}

    def conditional(p, x, selected):
        complement = [i for i in range(4) if i not in selected]
        denominator = sum(v for y, v in p.items() if all(y[i] == x[i] for i in complement))
        return p[x] / denominator

    def code(p, x, selected):
        value = F(1)
        for i in selected:
            value *= conditional(p, x, (i,))
        return value

    p = model(F(2))
    assert sum(p.values()) == 1
    for x in states:
        for selected in groups:
            assert conditional(p, x, selected) == code(p, x, selected)
    for selected in groups:
        complement = [i for i in range(4) if i not in selected]
        for fixed in product((0, 1), repeat=len(complement)):
            compatible = [x for x in states if all(x[i] == v for i, v in zip(complement, fixed))]
            assert sum(code(p, x, selected) for x in compatible) == 1
    pl_mass = sum(code(p, x, range(4)) for x in states)
    assert pl_mass != 1
    independent = model(F(1))
    assert all(code(independent, x, range(4)) == independent[x] for x in states)
    assert sum(code(independent, x, range(4)) for x in states) == 1

    # A fixed synthetic observation and a finite, explicitly declared parameter set.
    # All candidate laws are proper; the comparison is not an empirical benchmark.
    observed = (1, 1, 1, 0)
    grid = (F(1), F(3, 2), F(2), F(21, 10), F(9, 4), F(3))
    scores = {}
    for lam in grid:
        p = model(lam)
        coding = [code(p, observed, selected) for selected in groups]
        pl = code(p, observed, range(4))
        assert pl == coding[0] * coding[1]
        scores[lam] = [p[observed], pl, *coding]

    def maximizer(column):
        best = max(v[column] for v in scores.values())
        result = [lam for lam, v in scores.items() if v[column] == best]
        assert len(result) == 1
        return result[0]

    mle, mple, first, second = [maximizer(i) for i in range(4)]
    assert mle == 2 and mple == F(21, 10)
    assert first == 3 and second == F(3, 2)
    averaged = (first + second) / 2
    assert averaged == F(9, 4) and averaged != mple
    return dict(pseudolikelihood_total_mass_at_lambda_2=str(pl_mass),
                observed=observed, parameter_grid=list(map(str, grid)),
                joint_likelihood_maximizer=str(mle), pseudolikelihood_maximizer=str(mple),
                coding_maximizers=[str(first), str(second)],
                arithmetic_mean_of_coding_maximizers=str(averaged),
                scores={str(k): list(map(str, v)) for k, v in scores.items()})


def transpose(a):
    return [list(row) for row in zip(*a)]


def multiply(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def inverse(a):
    n = len(a)
    m = [[F(x) for x in row] + [F(i == j) for j in range(n)] for i, row in enumerate(a)]
    for i in range(n):
        pivot = next(j for j in range(i, n) if m[j][i])
        m[i], m[pivot] = m[pivot], m[i]
        scale = m[i][i]
        m[i] = [x / scale for x in m[i]]
        for j in range(n):
            if j != i:
                scale = m[j][i]
                m[j] = [x - scale * y for x, y in zip(m[j], m[i])]
    return [row[n:] for row in m]


def determinant3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


def quadratic(x, a):
    return sum(x[i] * a[i][j] * x[j] for i in range(len(x)) for j in range(len(x)))


def gaussian_checks():
    q = [[F(x) for x in row] for row in ((2, -1, 0), (-1, 3, -1), (0, -1, 2))]
    assert q == transpose(q)
    assert q[0][0] > 0 and q[0][0] * q[1][1] - q[0][1] ** 2 > 0 and determinant3(q) == 8
    covariance = inverse(q)
    conditional_variance = [1 / q[i][i] for i in range(3)]
    lam = [[conditional_variance[i] if i == j else F(0) for j in range(3)] for i in range(3)]
    b = multiply(lam, q)
    assert multiply(inverse(b), lam) == covariance
    beta = [[F(i == j) - b[i][j] for j in range(3)] for i in range(3)]
    assert beta[0][1] != beta[1][0]
    for i, j in product(range(3), repeat=2):
        assert beta[i][j] * conditional_variance[j] == beta[j][i] * conditional_variance[i]
    # Sparse precision specifies conditional, not marginal, independence.
    conditional_covariance = covariance[0][2] - covariance[0][1] * covariance[1][2] / covariance[1][1]
    assert covariance[0][2] == F(1, 8) and conditional_covariance == 0

    sar_precision = multiply(multiply(transpose(b), inverse(lam)), b)
    sar_covariance = multiply(multiply(inverse(b), lam), transpose(inverse(b)))
    assert inverse(sar_precision) == sar_covariance and sar_covariance != covariance
    assert sar_precision[0][2] == F(1, 3) and q[0][2] == 0
    x = [F(1), F(-1), F(2)]
    joint_quadratic, pl_quadratic = quadratic(x, q), quadratic(x, sar_precision)
    assert joint_quadratic == 19 and pl_quadratic == 29
    # The product of normalized Gaussian site conditionals integrates to 1/|det B|.
    # Normalizing that product gives the SAR law with the same B and Lambda, not CAR.
    pl_mass = 1 / abs(determinant3(b))
    assert pl_mass == F(3, 2)

    bad = [[F(1), F(-4, 5), F(0)], [F(-4, 5), F(1), F(-4, 5)], [F(0), F(-4, 5), F(1)]]
    assert determinant3(bad) == F(-7, 25)
    assert quadratic([1, 2, 1], bad) == F(-2, 5)
    intrinsic = [[F(1), F(-1), F(0)], [F(-1), F(2), F(-1)], [F(0), F(-1), F(1)]]
    assert determinant3(intrinsic) == 0 and all(sum(row) == 0 for row in intrinsic)
    # Both bad and intrinsic specifications have positive one-site conditional variances;
    # the first has a negative joint direction, the second an unnormalized flat direction.
    assert all(a[i][i] > 0 for a in (bad, intrinsic) for i in range(3))

    def matrix_strings(a):
        return [list(map(str, row)) for row in a]

    return dict(precision=matrix_strings(q), covariance=matrix_strings(covariance),
                conditional_variances=list(map(str, conditional_variance)),
                conditional_coefficients=matrix_strings(beta),
                marginal_covariance_0_2=str(covariance[0][2]), conditional_covariance_0_2_given_1=str(conditional_covariance),
                same_coefficient_sar_precision=matrix_strings(sar_precision),
                joint_quadratic=str(joint_quadratic), pseudolikelihood_quadratic=str(pl_quadratic),
                gaussian_pseudolikelihood_total_mass=str(pl_mass),
                invalid_precision_determinant=str(determinant3(bad)),
                invalid_precision_quadratic_witness=str(quadratic([1, 2, 1], bad)),
                intrinsic_precision_determinant=str(determinant3(intrinsic)))


if __name__ == '__main__':
    print(json.dumps(dict(binary=binary_checks(), gaussian=gaussian_checks()), indent=2))
