"""Exact small certificates for original nu-SVR/nu-SVC boundary claims.

Uses the C/n convention of Scholkopf et al. (2000). No optimizer or model
training is run. Feasibility, KKT products and primal/dual equality certify
the displayed finite optima for the linear PSD kernel k(x,z)=x*z.
"""
from fractions import Fraction as F
import json


def svr(x, y, nu, c, b, epsilon, alpha, astar):
    n = len(x)
    cap = c / n
    beta = [s - a for a, s in zip(alpha, astar)]
    mass = sum(alpha) + sum(astar)
    assert sum(beta) == 0 and mass <= c * nu
    assert all(0 <= a <= cap for a in alpha + astar)
    assert epsilon >= 0 and epsilon * (c * nu - mass) == 0
    w = sum(z * v for z, v in zip(x, beta))
    residuals = [w * z + b - v for z, v in zip(x, y)]
    upper = [max(F(0), r - epsilon) for r in residuals]
    lower = [max(F(0), -r - epsilon) for r in residuals]
    for r, u, l, a, s in zip(residuals, upper, lower, alpha, astar):
        assert a * (epsilon + u - r) == 0
        assert s * (epsilon + l + r) == 0
        assert (cap - a) * u == (cap - s) * l == 0
    primal = w * w / 2 + c * (nu * epsilon + sum(upper + lower) / n)
    dual = sum(v * z for v, z in zip(beta, y)) - w * w / 2
    assert primal == dual
    return dict(primal=primal, dual=dual, w=w, b=b, epsilon=epsilon,
                error_fraction=F(sum(abs(r) > epsilon for r in residuals), n),
                support_fraction=F(sum(v != 0 for v in beta), n),
                free_coefficients=sum(0 < a < cap for a in alpha + astar))


def svc(x, y, nu, b, rho, alpha):
    n = len(x)
    cap = F(1, n)
    mass = sum(alpha)
    assert rho >= 0 and mass >= nu and rho * (mass - nu) == 0
    assert sum(a * v for a, v in zip(alpha, y)) == 0
    assert all(0 <= a <= cap for a in alpha)
    w = sum(a * v * z for a, v, z in zip(alpha, y, x))
    scores = [w * z + b for z in x]
    margins = [v * s for v, s in zip(y, scores)]
    slack = [max(F(0), rho - m) for m in margins]
    for a, m, s in zip(alpha, margins, slack):
        assert a * (m - rho + s) == 0 and (cap - a) * s == 0
    primal = w * w / 2 - nu * rho + sum(slack) / n
    dual = -w * w / 2
    assert primal == dual
    return dict(primal=primal, dual=dual, w=w, b=b, rho=rho, scores=scores,
                margin_error_fraction=F(sum(m < rho for m in margins), n),
                support_fraction=F(sum(a > 0 for a in alpha), n),
                free_coefficients=sum(0 < a < cap for a in alpha))


zero = F(0)
one = F(1)
svr_positive = svr([zero] * 4, [-one, -one, one, one], F(1, 2), one,
                   zero, one, [F(1, 8), F(1, 8), zero, zero],
                   [zero, zero, F(1, 8), F(1, 8)])
assert svr_positive['error_fraction'] == 0 and svr_positive['support_fraction'] == 1
svr_zero = svr([zero] * 4, [zero] * 4, F(1, 2), one, zero, zero,
              [zero] * 4, [zero] * 4)
assert svr_zero['support_fraction'] == 0
svr_endpoint = [svr([zero, zero], [-one, one], one, one, b, e,
                    [F(1, 2), zero], [zero, F(1, 2)])
                for b, e in [(zero, zero), (F(1, 2), zero), (zero, one)]]
assert all(r['primal'] == 1 and r['free_coefficients'] == 0 for r in svr_endpoint)

svc_positive = svc([-one, -one, one, one], [-one, -one, one, one],
                   F(1, 2), zero, F(1, 2), [F(1, 8)] * 4)
assert svc_positive['margin_error_fraction'] == 0 and svc_positive['support_fraction'] == 1
svc_zero = svc([zero] * 4, [-one, -one, one, one], F(1, 4), zero, zero,
              [F(1, 16)] * 4)
assert all(s == 0 for s in svc_zero['scores'])
svc_endpoint = [svc([-one, one], [-one, one], one, b, rho, [F(1, 2)] * 2)
                for b, rho in [(zero, one), (F(3), F(4))]]
assert all(r['primal'] == -F(1, 2) and r['free_coefficients'] == 0 for r in svc_endpoint)
assert svc_endpoint[0]['scores'][0] < 0 < svc_endpoint[1]['scores'][0]

# Three positive and one negative label: maximum balanced dual mass is 1/2.
# For nu=3/4, w=0, b=rho=t, positive slacks0 and negative slack2t are feasible.
# Primal objective is -t/4, so the primal is unbounded as t grows.
feasibility = dict(n=4, positive_count=3, negative_count=1,
                   maximum_dual_mass=F(1, 2), chosen_nu=F(3, 4),
                   primal_coefficient_of_t=-F(1, 4))
assert feasibility['chosen_nu'] > feasibility['maximum_dual_mass']

results = dict(svr_positive_width=svr_positive, svr_zero_width=svr_zero,
               svr_endpoint_ambiguity=svr_endpoint, svc_positive_margin=svc_positive,
               svc_zero_margin=svc_zero, svc_endpoint_ambiguity=svc_endpoint,
               svc_infeasible_nu=feasibility,
               parametric_source_discrepancy='For zeta=1, the positive-width SVR certificate has support fraction1 at nu1/2, contradicting the printed Proposition4(ii) upper-bound wording. This contextual variant remains pending assessment.')
print(json.dumps(results, default=str, indent=2))
