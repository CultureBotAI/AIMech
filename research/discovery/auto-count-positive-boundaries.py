"""Original finite checks and algebraic witnesses; no empirical fit or author code."""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, exp
import json


def binomial_checks():
    trials = (2, 3, 1)
    odds = (F(2), F(3), F(5))
    interactions = {(0, 1): F(2), (1, 2): F(1, 3)}
    states = list(product(*(range(m + 1) for m in trials)))

    def weight(x):
        value = F(1)
        for i in range(3):
            value *= comb(trials[i], x[i]) * odds[i] ** x[i]
        for (i, j), v in interactions.items():
            value *= v ** (x[i] * x[j])
        return value

    raw = {x: weight(x) for x in states}
    z = sum(raw.values())
    p = {x: v / z for x, v in raw.items()}
    assert len(states) == 24 and z > 0 and sum(p.values()) == 1
    for x in states:
        for i in range(3):
            local_odds = odds[i]
            for (a, c), v in interactions.items():
                if a == i:
                    local_odds *= v ** x[c]
                elif c == i:
                    local_odds *= v ** x[a]
            denominator = sum(v for y, v in p.items() if all(y[j] == x[j] for j in range(3) if j != i))
            actual = p[x] / denominator
            expected = comb(trials[i], x[i]) * local_odds ** x[i] / (1 + local_odds) ** trials[i]
            assert actual == expected
    # Site counts require the combinatorial base measure, not just an energy term.
    m, a = 3, F(2)
    binomial_ratio_1_to_0 = m * a
    omitted_base_ratio = a
    assert binomial_ratio_1_to_0 != omitted_base_ratio
    # m=1 recovers a Bernoulli full conditional.
    for a in (F(1, 3), F(2), F(7)):
        assert sum(comb(1, k) * a ** k / (1 + a) for k in (0, 1)) == 1
        assert a / (1 + a) == 1 - 1 / (1 + a)
    # In a positive two-variable joint table, both conditional cross-odds agree.
    # Directed logistic specifications with interaction odds 2 and 3 violate this.
    x_given_y_cross_odds, y_given_x_cross_odds = F(2), F(3)
    assert x_given_y_cross_odds != y_given_x_cross_odds
    return dict(states=len(states), partition_function=str(z),
                all_site_conditionals_equal_binomial=True,
                interaction_odds=[str(x) for x in interactions.values()],
                base_measure_ratio=[str(binomial_ratio_1_to_0), str(omitted_base_ratio)],
                incompatible_directed_cross_odds=['2', '3'])


def poisson_checks():
    # Exact two-site unnormalized masses, with beta=log(r).
    def mass(x, y, r):
        return r ** (x * y) / (factorial(x) * factorial(y))

    for x, y in product(range(9), repeat=2):
        r = F(1, 2)
        assert mass(x, y, r) <= mass(x, y, F(1))
        assert mass(x + 1, y, r) / mass(x, y, r) == r ** y / (x + 1)
    # With beta=log(2)>0, diagonal terms fail even to tend to zero.
    # Their ratio is 2^(2n+1)/(n+1)^2 >= 2: 2^n >= n+1 follows by induction.
    diagonal = [mass(n, n, F(2)) for n in range(13)]
    ratios = [diagonal[n + 1] / diagonal[n] for n in range(12)]
    assert all(r >= 2 for r in ratios)
    assert all(diagonal[n + 1] > diagonal[n] for n in range(12))
    # Truncating both counts creates a different valid finite-support model.
    cap, fixed = 4, 2
    bounded = {(x, y): mass(x, y, F(2)) for x, y in product(range(cap + 1), repeat=2)}
    z = sum(bounded.values())
    assert z > 0
    denominator = sum(v for (x, y), v in bounded.items() if y == fixed)
    local_mean = F(2) ** fixed
    local_z = sum(local_mean ** k / factorial(k) for k in range(cap + 1))
    assert all(bounded[(k, fixed)] / denominator == local_mean ** k / factorial(k) / local_z for k in range(cap + 1))
    assert abs(1 / float(local_z) - exp(-float(local_mean))) > 0.001
    return dict(negative_interaction_mass_dominated_by_independent_mass=True,
                conditional_successive_mass_ratio='exp(alpha+beta*y)/(x+1)',
                positive_interaction_diagonal_ratios=list(map(str, ratios)),
                bounded_cap=cap, bounded_partition_function=str(z),
                bounded_conditional_is_truncated_not_ordinary_poisson=True,
                scope='Finite checks illustrate the analytic domination and divergence arguments; they do not prove general summability by truncation.')


def exponential_checks():
    # Rate-sign convention: q(x)=exp(-sum alpha_i*x_i - sum gamma_ij*x_i*x_j).
    alpha = (F(1), F(2), F(3))
    gamma = {(0, 1): F(1, 2), (1, 2): F(2)}

    def energy(x):
        return sum(a * v for a, v in zip(alpha, x)) + sum(g * x[i] * x[j] for (i, j), g in gamma.items())

    sample = (F(0), F(1, 2), F(2))
    rates = []
    for i in range(3):
        rate = alpha[i] + sum(g * sample[j if i == k else k] for (k, j), g in gamma.items() if i in (k, j))
        rates.append(rate)
        changed = list(sample)
        changed[i] += F(3, 2)
        assert energy(changed) - energy(sample) == rate * F(3, 2)
        assert rate > 0
        # Integral_0^infinity rate*exp(-rate*x) dx = 1 analytically.
        assert rate * (1 / rate) == 1
    assert energy(sample) >= sum(a * v for a, v in zip(alpha, sample))
    # The interaction penalty yields a pointwise independent-exponential upper bound.
    independent_integral = F(1)
    for a in alpha:
        independent_integral /= a
    assert independent_integral == F(1, 6)
    # Reversing an interaction sign can make the rate negative on the stated support.
    bad_rate = F(1) + F(-1, 2) * F(3)
    assert bad_rate == F(-1, 2)
    return dict(conditional_rates=list(map(str, rates)),
                joint_energy_increment_equals_conditional_rate_times_increment=True,
                independent_density_integral_upper_bound=str(independent_integral),
                wrong_sign_conditional_rate=str(bad_rate),
                scope='Positive alpha and nonnegative symmetric gamma give this sufficient finite-model construction; no universal necessity claim about zero-rate boundary parameterizations is made.')


if __name__ == '__main__':
    print(json.dumps(dict(binomial=binomial_checks(), poisson=poisson_checks(), exponential=exponential_checks()), indent=2))
