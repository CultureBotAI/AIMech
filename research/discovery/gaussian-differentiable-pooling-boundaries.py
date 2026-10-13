"""Constructed algebra and finite differences, not the authors' implementation."""
import json
import math


def weights(a):
    assert all(x > 0 for x in a)
    return [math.sqrt(x / sum(a)) for x in a]


def result():
    a = [1.0, 4.0]
    w = weights(a)
    assert math.isclose(sum(x*x for x in w), 1.0)
    assert not math.isclose(sum(w), 1.0)
    jac = [[w[i] / 2 * ((1/a[i] if i == j else 0) - 1/sum(a))
            for j in range(2)] for i in range(2)]
    numerical = [[0.0, 0.0], [0.0, 0.0]]
    for j in range(2):
        plus, minus = list(a), list(a)
        plus[j] += 1e-5
        minus[j] -= 1e-5
        for i in range(2):
            numerical[i][j] = (weights(plus)[i] - weights(minus)[i]) / 2e-5
    assert all(math.isclose(jac[i][j], numerical[i][j], abs_tol=1e-10)
               for i in range(2) for j in range(2))
    assert jac[0][1] < 0
    printed_off_diagonal = w[0] / sum(a)
    assert printed_off_diagonal > 0 and not math.isclose(printed_off_diagonal, jac[0][1])
    printed_diagonal = (1-w[1]) / sum(a)
    assert not math.isclose(printed_diagonal,jac[1][1])
    p = 3.0
    unpooled = [x*p for x in w]
    recovered = sum(x*y for x,y in zip(w,unpooled))
    assert math.isclose(recovered,p)
    z = [1.0,0.0]
    pooled = sum(x*y for x,y in zip(w,z))
    reconstructed = [x*pooled for x in w]
    assert reconstructed != z
    uniform = weights([1.0]*4)
    assert uniform == [0.5]*4
    uniform_pool = sum(x*y for x,y in zip(uniform,[1,2,3,4]))
    assert uniform_pool == 5 and uniform_pool != 2.5
    # Gaussian mean0 selects spatial position0 as precision grows, not value9 at position1.
    sharp = weights([1.0,math.exp(-50)])
    selected = sharp[0]*1 + sharp[1]*9
    assert abs(selected-1) < 1e-8
    # If two unit columns overlap identically, U^T U is all ones, not identity.
    overlap_gram = [[sum(x*y for x,y in zip(w,w))]*2 for _ in range(2)]
    assert math.isclose(overlap_gram[0][1],1)
    return dict(unit_l2_weights=w,analytic_jacobian=jac,finite_difference=numerical,
                printed_eq19_off_diagonal=printed_off_diagonal,
                printed_eq20_diagonal=printed_diagonal,
                scalar_recovered_from_own_unpooling=recovered,
                arbitrary_region_projection=reconstructed,
                zero_precision_pool=uniform_pool,arithmetic_mean=2.5,
                sharp_spatial_mean_pool=selected,activation_max=9,
                overlapping_unit_columns_gram=overlap_gram)


if __name__ == '__main__':
    print(json.dumps(result(),indent=2,sort_keys=True))
