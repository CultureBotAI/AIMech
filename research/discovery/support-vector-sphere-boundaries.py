"""Exact boundary example for the displayed support-vector sphere formulation.

This is an analytic two-observation example, not a historical solver run.
The Gaussian Gram matrix [[1,1/2],[1/2,1]] is realizable at a separation
whose squared length times the kernel scale equals log(2).
"""
from fractions import Fraction as F
import json


def check():
    kernel = [[F(1), F(1, 2)], [F(1, 2), F(1)]]
    beta = [F(1, 2), F(1, 2)]
    penalty = F(1, 2)
    assert sum(beta) == 1 and all(b == penalty for b in beta)
    center_norm = sum(beta[i] * kernel[i][j] * beta[j]
                      for i in range(2) for j in range(2))
    distances = [kernel[i][i] - 2 * sum(beta[j] * kernel[i][j]
                 for j in range(2)) + center_norm for i in range(2)]
    dual = sum(kernel[i][i] * beta[i] for i in range(2)) - center_norm
    assert distances == [F(1, 4), F(1, 4)] and dual == F(1, 4)
    examples = []
    for radius_sq in [F(0), F(1, 8), F(1, 4)]:
        slack = [d - radius_sq for d in distances]
        assert all(s >= 0 for s in slack)
        assert radius_sq + penalty * sum(slack) == dual
        assert all(beta[i] * (radius_sq + slack[i] - distances[i]) == 0
                   for i in range(2))
        examples.append(dict(radius_squared=str(radius_sq),
                             slack=[str(s) for s in slack],
                             objective=str(dual)))
    return dict(gaussian_kernel_off_diagonal='1/2', penalty='1/2',
                beta=['1/2', '1/2'], free_support_vectors=0,
                primal_dual_optimum='1/4', examples=examples,
                conclusion='No free support vector determines the radius. At squared radius1/4 both box-bound vectors lie on the boundary, not strictly outside. The displayed constraints alone give a non-strict bounded-vector count bound.')


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
