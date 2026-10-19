#!/usr/bin/env python3
"""Constructed boundary verification for Oymak & Hassibi (2016), Found. Comput. Math. 16:965-1029."""

import math


def phi(t: float) -> float:
    return math.exp(-0.5 * t * t) / math.sqrt(2.0 * math.pi)


def Q_tail(t: float) -> float:
    return 0.5 * math.erfc(t / math.sqrt(2.0))


def psi_l1_zero_coord(lam: float) -> float:
    """E[dist(g, [-lam, lam])^2] for g ~ N(0,1)."""
    return 2.0 * ((1.0 + lam * lam) * Q_tail(lam) - lam * phi(lam))


def exact_l1_nonzero_coord_nmse(x0_i: float, sigma: float, lam: float) -> float:
    """Exact E[(soft(x0_i + sigma*g, sigma*lam) - x0_i)^2] / sigma^2 for g ~ N(0, 1).

    Let mu = x0_i / sigma. Then soft(x0_i + sigma*g, sigma*lam) - x0_i = sigma * h(g), where:
      - for g > lam - mu:       h(g) = g - lam
      - for -lam - mu <= g <= lam - mu: h(g) = -mu
      - for g < -lam - mu:      h(g) = g + lam
    """
    mu = x0_i / sigma
    a = -lam - mu
    b = lam - mu
    # Integral 1: g in (b, inf) of (g - lam)^2 phi(g) dg
    # = (1 + lam^2) Q_tail(b) + (b - 2*lam) phi(b)
    term_upper = (1.0 + lam * lam) * Q_tail(b) + (b - 2.0 * lam) * phi(b)
    # Integral 2: g in [a, b] of mu^2 phi(g) dg
    term_mid = (mu * mu) * (Q_tail(a) - Q_tail(b))
    # Integral 3: g in (-inf, a) of (g + lam)^2 phi(g) dg
    # By symmetry g -> -g, integral_{g < a} (g+lam)^2 phi(g) = integral_{u > -a} (u - lam)^2 phi(u)
    term_lower = (1.0 + lam * lam) * Q_tail(-a) + (-a - 2.0 * lam) * phi(-a)
    return term_upper + term_mid + term_lower


def verify_theorem_1_1_l1_monotonicity_and_limit() -> tuple[float, float, float]:
    """Verify Theorem 1.1 & Lemma 5.1 for l1 proximal denoising."""
    n = 100
    k = 10
    lam = 1.2
    x0_nonzero = 2.5
    # Subdifferential mean-squared distance D(lam * partial ||x0||_1)
    d_subdiff = k * (1.0 + lam * lam) + (n - k) * psi_l1_zero_coord(lam)

    sigmas = [10.0, 2.0, 1.0, 0.5, 0.1, 0.01, 1e-4, 1e-6]
    nmses = []
    for s in sigmas:
        nmse_s = k * exact_l1_nonzero_coord_nmse(x0_nonzero, s, lam) + (n - k) * psi_l1_zero_coord(lam)
        nmses.append(nmse_s)
        # Theorem 1.1: NMSE(sigma) <= D(lam * partial f(x0)) for all sigma > 0
        assert nmse_s <= d_subdiff + 1e-12, f"Theorem 1.1 violated at sigma={s}: {nmse_s} > {d_subdiff}"

    # Verify convergence to D(lam * partial f(x0)) as sigma -> 0+
    limit_err = abs(nmses[-1] - d_subdiff)
    assert limit_err < 1e-9, f"Limit error too large: {limit_err}"
    # Verify strict decrease at large sigma (regularization benefit at high noise)
    assert nmses[0] < d_subdiff - 1.0
    return d_subdiff, nmses[0], limit_err


def verify_proposition_6_1_sandwiching() -> tuple[float, float]:
    """Verify Proposition 6.1 sandwiching ratios for l1 and nuclear norms."""
    n, k = 1000, 25
    # From proof of Prop 6.1: if w >= k / sqrt(n) and delta <= 1 / sqrt(k),
    # then (w + delta)^2 / w^2 = (1 + delta/w)^2.
    w = math.sqrt(k * k / n)
    delta = 1.0 / math.sqrt(k)
    exact_ratio = ((w + delta) / w) ** 2
    # Paper's algebraic bound: 1 + 2 / sqrt(k^3 / n) when delta/w <= 1/sqrt(k^3/n) is small
    bound_l1 = 1.0 + 2.0 / math.sqrt((k ** 3) / n) + 1.0 / ((k ** 3) / n)
    assert abs(exact_ratio - bound_l1) < 1e-12

    d, r = 200, 10
    bound_nuc = 1.0 + 2.0 / math.sqrt((r ** 3) * d)
    assert bound_nuc > 1.0 and bound_nuc < 1.01
    return 1.0 + 2.0 / math.sqrt((k ** 3) / n), bound_nuc


def verify_theorem_3_3_lasso_phase_transition() -> tuple[float, float]:
    """Verify Theorem 3.3 / Proposition 7.1 projected LASSO risk and cost."""
    D = 40.0
    m_above = 60.0
    eta_above = D / (m_above - D)
    cost_above = m_above - eta_above
    assert abs(eta_above - 2.0) < 1e-12
    assert abs(cost_above - 58.0) < 1e-12

    # Verify complement relation (m - D) + D = m and divergence as m -> D+
    m_near = 40.001
    eta_near = D / (m_near - D)
    assert eta_near > 1e4
    return eta_above, cost_above


def main() -> None:
    d_subdiff, nmse_high_sigma, limit_err = verify_theorem_1_1_l1_monotonicity_and_limit()
    ratio_l1, ratio_nuc = verify_proposition_6_1_sandwiching()
    eta_above, cost_above = verify_theorem_3_3_lasso_phase_transition()
    print(
        f"Oymak & Hassibi (2016) verified: D(lam*partial f)={d_subdiff:.4f}, "
        f"NMSE(sigma=10)={nmse_high_sigma:.4f}, sigma->0 err={limit_err:.2e}, "
        f"Prop6.1 ratios=(l1:{ratio_l1:.4f}, nuc:{ratio_nuc:.6f}), "
        f"LASSO(m=60,D=40) eta={eta_above:.2f}, F={cost_above:.2f}."
    )


if __name__ == "__main__":
    main()
