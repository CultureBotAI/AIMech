"""Original model-boundary calculations, not author-code or empirical reproduction."""
from fractions import Fraction as F
from decimal import Decimal as D, localcontext
from itertools import product
from math import factorial, sqrt, pi, exp
import json


def truncated_checks():
    cap = 4
    states = list(product(range(cap + 1), repeat=2))
    weights = {(x, y): F(2) ** x * F(3) ** y * F(2) ** (x*y) / (factorial(x)*factorial(y)) for x, y in states}
    z = sum(weights.values())
    p = {x: w/z for x, w in weights.items()}
    assert sum(p.values()) == 1
    for x, y in states:
        mu = F(2) * F(2) ** y
        norm = sum(mu ** k / factorial(k) for k in range(cap + 1))
        assert p[(x, y)] / sum(p[(k, y)] for k in range(cap + 1)) == mu ** x / factorial(x) / norm
        mu = F(3) * F(2) ** x
        norm = sum(mu ** k / factorial(k) for k in range(cap + 1))
        assert p[(x, y)] / sum(p[(x, k)] for k in range(cap + 1)) == mu ** y / factorial(y) / norm
    lam = F(4)
    local_z = sum(lam**k/factorial(k) for k in range(cap+1))
    mean_direct = sum(k*lam**k/factorial(k) for k in range(cap+1))/local_z
    mean_formula = lam*sum(lam**k/factorial(k) for k in range(cap))/local_z
    assert mean_direct == mean_formula == F(284,103) and mean_direct != lam
    return dict(cap=cap, states=len(states), partition_function=str(z),
                all_full_conditionals_verified=True,
                underlying_poisson_parameter=str(lam), actual_truncated_conditional_mean=str(mean_direct),
                scope='Finite-support joint with positive interaction; neither an unbounded Poisson nor a Winsorized law.')


def winsorization_checks():
    with localcontext() as ctx:
        ctx.prec = 60
        cap = 4
        def winsorized(lam):
            low = [(-lam).exp() * lam**k / D(factorial(k)) for k in range(cap)]
            return low + [D(1) - sum(low)]
        a, b = winsorized(D(1)), winsorized(D(2))
        joint = {(x,y):a[x]*b[y] for x,y in product(range(cap+1),repeat=2)}
        tol = D('1e-55')
        assert abs(sum(joint.values())-1) < tol
        for x,y in joint:
            assert abs(joint[(x,y)]/sum(joint[(k,y)] for k in range(cap+1))-a[x]) < tol
            assert abs(joint[(x,y)]/sum(joint[(x,k)] for k in range(cap+1))-b[y]) < tol
        # Constant E is allowed by the literal main-paper Theorem 1 wording.
        # This independent product refutes its unqualified universal impossibility.
        # Conversely, the usual interacting specification need not be compatible.
        cond = {y:winsorized(D(2)**y) for y in range(cap+1)}
        # Any positive joint must give the same mixed odds ratio by either direction.
        first = (cond[4][1]/cond[4][0])/(cond[0][1]/cond[0][0])
        second = (cond[1][4]/cond[1][0])/(cond[0][4]/cond[0][0])
        assert abs(first-16) < tol and abs(first-second) > 1
        return dict(cap=cap, independent_product_is_valid=True,
                    incompatible_interacting_mixed_odds=[str(first),str(second)],
                    interpretation='Independent Winsorized conditionals are compatible. A symmetric log-mean interaction example is not; no claim that arbitrary interacting Winsorization is valid follows.')


def quadratic_checks():
    # The once-counted edge coefficient is twice the symmetric matrix entry.
    matrix = [[F(-1), F(3,4)], [F(3,4), F(-1)]]
    for x,y in product(range(8),repeat=2):
        energy = -x*x-y*y+F(3,2)*x*y
        matrix_form = matrix[0][0]*x*x+2*matrix[0][1]*x*y+matrix[1][1]*y*y
        assert energy == matrix_form
        assert energy <= -F(1,4)*(x*x+y*y)
    # Negative definiteness on the entire real space is sufficient, not necessary.
    # q=-x^2-4xy-y^2 <= -(x^2+y^2) on the nonnegative orthant,
    # yet q(1,-1)=2 > 0, so its symmetric matrix is indefinite.
    for x,y in product(range(8),repeat=2):
        assert -x*x-4*x*y-y*y <= -(x*x+y*y)
    assert -1+4-1 == 2
    # A discrete nonnegative-integer kernel includes its k=0 term, equal to 1.
    # The claimed full-real Gaussian integral upper bound is smaller than that term.
    discrete_lower_bound = 1.0
    continuous_integral = sqrt(pi/100)
    assert continuous_integral < discrete_lower_bound
    # Even eta>0 does not repair the universal bound: choose eta=1, theta_ss=-100.
    positive_eta_integral = sqrt(pi/100)*exp(1/400)
    assert positive_eta_integral < discrete_lower_bound
    return dict(once_counted_edge_coefficient='3/2', symmetric_off_diagonal='3/4',
                uniform_negative_quadratic_bound='-(x^2+y^2)/4',
                indefinite_but_orthant_negative_example=True,
                discrete_partition_lower_bound=discrete_lower_bound,
                claimed_gaussian_integral_bound_at_eta_0=continuous_integral,
                claimed_gaussian_integral_bound_at_eta_1=positive_eta_integral,
                interpretation='The source Gaussian sum-to-integral inequality is not a universal upper bound. These counterexamples concern the approximation, not existence of the quadratic count model.')


def sublinear_checks():
    r0, r = F(1), F(3)
    plateau = (r+r0)/2
    def b(x):
        x = F(x)
        if x <= r0:return x
        if x <= r:return -x*x/(2*(r-r0))+r*x/(r-r0)-r0*r0/(2*(r-r0))
        return plateau
    values = [b(x) for x in range(10)]
    assert values == [F(0),F(1),F(7,4)]+[F(2)]*7
    assert all(0 <= b(x) <= min(F(x),plateau) for x in range(20))
    assert b(r0)==r0 and b(r)==plateau
    # Integral powers give exact rational conditional kernels for eta=4*log(2).
    kernel = [F(2)**int(4*b(x))/factorial(x) for x in range(15)]
    assert all((4*b(x)).denominator==1 for x in range(15))
    assert all(kernel[x+1]/kernel[x] == F(1,x+1) for x in range(3,14))
    # The Poisson upper bound eta>=0 uses B(x)<=x. For eta<0 it reverses.
    positive_partial = sum(kernel)
    poisson_positive_partial = sum(F(16)**x/factorial(x) for x in range(15))
    negative_partial = sum(F(2)**(-int(4*b(x)))/factorial(x) for x in range(15))
    poisson_negative_partial = sum(F(1,16)**x/factorial(x) for x in range(15))
    assert positive_partial < poisson_positive_partial
    assert negative_partial > poisson_negative_partial
    # Zero unary terms cause no difficulty: bounded B bounds the interaction factor.
    for x,y in product(range(8),repeat=2):
        assert b(x)*b(y) <= plateau**2
    return dict(r0=str(r0), r=str(r), statistic_values=list(map(str,values)),
                high_count_kernel_ratio='1/(x+1) beyond the plateau',
                positive_eta_termwise_poisson_bound_holds=True,
                negative_eta_termwise_bound_reverses=True,
                zero_unary_parameter_bounded_interaction=True,
                interpretation='The full partition bound uses globally bounded B and the convergent product of reciprocal-factorial sums, not a finite numerical cutoff. An arbitrary unbounded sublinear statistic is not covered.')


if __name__ == '__main__':
    print(json.dumps(dict(truncated=truncated_checks(), winsorization=winsorization_checks(),
                          quadratic=quadratic_checks(), sublinear=sublinear_checks()),indent=2))
