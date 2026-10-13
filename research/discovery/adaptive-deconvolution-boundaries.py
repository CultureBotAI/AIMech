"""Small algebraic examples, not a trained implementation of either paper."""
import json
import math


def project_absolute_max(values):
    index = max(range(len(values)), key=lambda i: abs(values[i]))
    return [v if i == index else 0.0 for i, v in enumerate(values)]


def matvec(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def result():
    signed = project_absolute_max([-3.0, 2.0])
    assert signed == [-3.0, 0.0] and max([-3.0, 2.0]) == 2.0
    assert signed != [-3.0, 2.0]
    separately = [a + b for a, b in zip(project_absolute_max([3.0, 0.0]),
                                       project_absolute_max([0.0, 2.0]))]
    jointly = project_absolute_max([3.0, 2.0])
    assert separately != jointly
    # F1=[[1,2],[0,1]], U=[[0],[1]], F2=[[1,-1]].
    reconstruction = [[2.0, -2.0], [1.0, -1.0]]
    transpose = [list(row) for row in zip(*reconstruction)]
    z, v = [0.3, -0.2], [1.5, -0.7]
    lhs, rhs = dot(matvec(reconstruction, z), v), dot(z, matvec(transpose, v))
    assert math.isclose(lhs, rhs, abs_tol=1e-12)
    assert matvec(transpose, matvec(reconstruction, z)) != z
    residual = [a - b for a, b in zip(matvec(reconstruction, z), v)]
    analytic = matvec(transpose, residual)
    def loss(x):
        return 0.5 * sum((a - b) ** 2 for a, b in zip(matvec(reconstruction, x), v))
    numerical = []
    for j in range(2):
        plus, minus = list(z), list(z)
        plus[j] += 1e-5
        minus[j] -= 1e-5
        numerical.append((loss(plus) - loss(minus)) / 2e-5)
    assert all(math.isclose(a, b, abs_tol=1e-9) for a, b in zip(analytic, numerical))
    # For F=[1,1], y=2 and lambda=1, every nonnegative split with sum1 is optimal:
    # ||z||1>=|sum(z)|, and min_s .5*(s-2)^2+|s|=1.5 at s=1.
    splits = [[1.0, 0.0], [0.5, 0.5], [0.0, 1.0]]
    objectives = [0.5 * (sum(x) - 2) ** 2 + sum(abs(t) for t in x) for x in splits]
    assert objectives == [1.5, 1.5, 1.5]
    return dict(signed_absolute_max_projection=signed, projection_of_sum=jointly,
                sum_of_projections=separately, fixed_switch_adjoint_pair=[lhs, rhs],
                reconstruction_gradient=analytic, finite_difference=numerical,
                duplicate_atom_minimizers=splits, equal_optimal_objectives=objectives)


if __name__ == '__main__':
    print(json.dumps(result(), indent=2, sort_keys=True))
