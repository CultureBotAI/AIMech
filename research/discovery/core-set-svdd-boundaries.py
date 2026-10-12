"""Exact curator illustrations for Chu--Tsang--Kwok CSVDD (2004).

These are rational arithmetic checks of displayed formulas and an allowed
initialization; no historical implementation, numerical optimizer or benchmark
is executed. Locators: original author PDF, Sections II and III, pp.2-3.
"""
from fractions import Fraction as F
import json


def main():
    # The initial fixed-size sample is the entire three-point dataset.
    points = [F(0), F(1, 10), F(1)]
    n = len(points)
    nu, epsilon, k = F(1, 5), F(1, 5), F(5, 4)
    cap = 1 / (nu * n)
    sample_center, sample_radius = F(1, 2), F(1, 2)
    alpha = [F(1, 2), F(0), F(1, 2)]
    assert sum(alpha) == 1 and all(0 <= a <= cap for a in alpha)
    assert sum(a * x for a, x in zip(alpha, points)) == sample_center
    sample_primal = sample_radius**2
    sample_dual = sum(a * x**2 for a, x in zip(alpha, points)) - sample_center**2
    assert sample_primal == sample_dual == F(1, 4)
    assert all(abs(x - sample_center) <= sample_radius for x in points)
    # Unique closest sampled point; the allowed random x=0 has farthest y=1.
    z = min(points, key=lambda x: abs(x - sample_center))
    assert z == F(1, 10)
    distance = max(abs(x - points[0]) for x in points)
    radius = distance / k
    expanded_radius = (1 + epsilon) * radius
    expanded_outside = sum(abs(x - z) > expanded_radius for x in points)
    original_outside = sum(abs(x - z) > radius for x in points)
    assert expanded_outside == 0 and expanded_outside < nu * n
    assert original_outside == 1 and F(original_outside, n) > nu
    slacks = [max(F(0), (x - z)**2 - radius**2) for x in points]
    stopped_primal = radius**2 + cap * sum(slacks)
    ratio = stopped_primal / sample_primal
    assert stopped_primal == F(277, 300) and ratio == F(277, 75)
    assert ratio > (1 + epsilon)**2
    # Reusing the full-data simplex cap on a two-point subproblem can fail.
    full_n, core_n, subset_nu = 100, 2, F(1, 10)
    full_cap = 1 / (subset_nu * full_n)
    subset_cap = 1 / (subset_nu * core_n)
    assert core_n * full_cap < 1 <= core_n * subset_cap
    # An optimal enclosing radius is not an enclosure at every current center.
    pair, optimal_center, meb_radius, current_center = [F(0), F(2)], F(1), F(1), F(0)
    assert max(abs(x - optimal_center) for x in pair) == meb_radius
    assert max(abs(x - current_center) for x in pair) == 2 * meb_radius
    print(json.dumps({
        'scope': 'Exact displayed-formula illustrations; no model training or historical code execution.',
        'permitted_initialization': dict(points=list(map(str, points)), nu=str(nu), epsilon=str(epsilon), k=str(k), n0=n, z=str(z), radius=str(radius), expanded_radius=str(expanded_radius), expanded_outside=expanded_outside, original_outside=original_outside, original_outside_fraction=str(F(original_outside, n)), optimum_objective=str(sample_primal), stopped_objective=str(stopped_primal), objective_ratio=str(ratio)),
        'subset_cap': dict(full_n=full_n, core_n=core_n, nu=str(subset_nu), sum_full_caps=str(core_n * full_cap), sum_rescaled_caps=str(core_n * subset_cap), interpretation='This warns against retaining the full-data denominator; it does not identify the unpublished historical implementation.'),
        'center_dependence': dict(optimal_radius=str(meb_radius), farthest_from_current=str(2 * meb_radius)),
        'complexity_substitution': 'Source M=O(1/(delta*epsilon)); fixed delta gives O(N/epsilon^2+epsilon^-4), whereas experimental delta=0.01*epsilon gives O(N/epsilon^4+epsilon^-8) under the same model and fixed k.'
    }, indent=2))


if __name__ == '__main__':
    main()
