#!/usr/bin/env python3
"""Constructed boundary verification for Stochastic Cubic Regularization (Tripuraneni et al. 2018)."""

import math


def w_synthetic(x: float, eps: float = 0.01, L: float = 5.0) -> tuple[float, float, float]:
    """Exact W-shaped piecewise cubic function w(x), w'(x), w''(x) from Appendix C.1 (p. 26)."""
    rt = math.sqrt(eps)
    if x <= -L * rt:
        u = x + (L + 1.0) * rt
        val = rt * (u**2) - (u**3) / 3.0 - (3.0 * L + 1.0) * (eps**1.5) / 3.0
        g = 2.0 * rt * u - (u**2)
        h = 2.0 * rt - 2.0 * u
    elif x <= -rt:
        val = eps * x + (eps**1.5) / 3.0
        g = eps
        h = 0.0
    elif x <= 0.0:
        val = -rt * (x**2) - (x**3) / 3.0
        g = -2.0 * rt * x - (x**2)
        h = -2.0 * rt - 2.0 * x
    elif x <= rt:
        val = -rt * (x**2) + (x**3) / 3.0
        g = -2.0 * rt * x + (x**2)
        h = -2.0 * rt + 2.0 * x
    elif x <= L * rt:
        val = -eps * x + (eps**1.5) / 3.0
        g = -eps
        h = 0.0
    else:
        u = x - (L + 1.0) * rt
        val = rt * (u**2) + (u**3) / 3.0 - (3.0 * L + 1.0) * (eps**1.5) / 3.0
        g = 2.0 * rt * u + (u**2)
        h = 2.0 * rt + 2.0 * u
    return val, g, h


def solve_cubic_1d(g: float, b_hess: float, rho: float) -> float:
    """Exact global minimizer Delta* of 1D cubic submodel g*Delta + 0.5*b_hess*Delta^2 + (rho/6)*|Delta|^3."""
    # Stationarity (Eq. 15-16): g + b_hess*Delta + 0.5*rho*|Delta|*Delta = 0 and b_hess + 0.5*rho*|Delta| >= 0
    best_d = 0.0
    best_m = 0.0
    for sign in (-1.0, 1.0):
        # (0.5*rho)*r^2 + sign*b_hess*r + sign*g = 0 for r = |Delta| >= max(0, -2*b_hess/rho)
        a_q = 0.5 * rho
        b_q = sign * b_hess
        c_q = sign * g
        disc = b_q * b_q - 4.0 * a_q * c_q
        if disc >= 0.0:
            for s_root in (-1.0, 1.0):
                r = (-b_q + s_root * math.sqrt(disc)) / (2.0 * a_q)
                if r >= 0.0 and b_hess + 0.5 * rho * r >= -1e-12:
                    d = sign * r
                    m_val = g * d + 0.5 * b_hess * (d**2) + (rho / 6.0) * (r**3)
                    if m_val < best_m:
                        best_m = m_val
                        best_d = d
    return best_d


def main() -> None:
    # 1. Verify Appendix C.1 W-shaped synthetic function properties:
    # Saddle point at x = 0 with w(0) = 0, w'(0) = 0, w''(0) = -2*sqrt(eps) = -0.2 (for eps = 0.01),
    # and global minima at x = +-(L + 1)*sqrt(eps) = +-0.6 with value -(3L+1)*eps^{1.5}/3 = -16*0.001/3 = -2/375.
    val0, g0, h0 = w_synthetic(0.0, eps=0.01, L=5.0)
    assert abs(val0) < 1e-12 and abs(g0) < 1e-12 and abs(h0 - (-0.2)) < 1e-12
    val_min, g_min, h_min = w_synthetic(0.6, eps=0.01, L=5.0)
    assert abs(val_min - (-2.0 / 375.0)) < 1e-12
    assert abs(g_min) < 1e-12 and abs(h_min - 0.2) < 1e-12

    # 2. Verify Lemma 5 & Equations (15)-(16) on escaping the strict saddle point x = 0:
    # At x = 0, g = 0, b_hess = -0.2 < 0, rho = 1.0:
    # Global optimizer Delta^* has |Delta^*| = -2 * b_hess / rho = 0.4,
    # and cubic submodel decrease is m(Delta^*) - m(0) = -(1/12) * rho * |Delta^*|^3 <= -(1/12)*0.4^3!
    rho = 1.0
    d_star = solve_cubic_1d(g=0.0, b_hess=-0.2, rho=rho)
    assert abs(abs(d_star) - 0.4) < 1e-12
    m_star = 0.5 * (-0.2) * (d_star**2) + (rho / 6.0) * (abs(d_star) ** 3)
    bound_lemma5 = -(1.0 / 12.0) * rho * (abs(d_star) ** 3)
    assert abs(m_star - bound_lemma5) < 1e-12

    # 3. Verify Lemma 9 Cauchy step radius R_c >= (7/10)*(ell/rho) when ||g|| >= ell^2 / rho (Appendix B.1, Eq. (27))
    ell = 1.2
    g_large = (ell**2) / rho
    b_hess_bound = ell
    Rc = -(g_large * b_hess_bound) / (rho * g_large) + math.sqrt(
        (b_hess_bound / rho) ** 2 + 2.0 * g_large / rho
    )
    assert Rc >= 0.7 * (ell / rho)
    m_cauchy = -0.5 * g_large * Rc - (rho / 12.0) * (Rc**3)
    assert m_cauchy <= -(7.0 / 20.0) * ((ell**3) / (rho**2))

    print(
        f"[PASS] Stochastic Cubic Regularization boundaries verified: "
        f"w(0.6)={val_min:.6f} (-2/375), saddle |Delta*|={abs(d_star):.2f}, "
        f"m(Delta*)={m_star:.6f} == -(1/12)*rho*|Delta*|^3, Cauchy Rc={Rc:.4f} >= 0.7*ell/rho={0.7*ell/rho:.4f}"
    )


if __name__ == "__main__":
    main()
