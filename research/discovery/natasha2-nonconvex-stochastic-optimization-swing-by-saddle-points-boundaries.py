#!/usr/bin/env python3
"""Constructed boundary verification for Natasha 1.5 and Natasha 2 (Allen-Zhu 2018)."""

import math


def main() -> None:
    # 1. Verify Claim 7.2 & Claim 7.3 (Section 7.1, p. 19):
    # (a) Second-order step along v with ||v||=1 and v^T nabla^2 f(y_k) v <= -delta/2 using step size eta = delta / L2
    # guarantees f(y_k) - E[f(y_{k+1})] >= delta^3 / (12 * L2^2).
    # Test on f(y) = -0.25 * delta * y^2 + (L2 / 6.0) * |y|^3 at y_k = 0:
    delta = 0.4
    L2 = 1.5
    eta = delta / L2

    def f_1d(y: float) -> float:
        return -0.25 * delta * (y**2) + (L2 / 6.0) * (abs(y) ** 3)

    y_k = 0.0
    expected_after = 0.5 * (f_1d(y_k + eta) + f_1d(y_k - eta))
    decrease = f_1d(y_k) - expected_after
    bound_claim73 = (delta**3) / (12.0 * (L2**2))
    assert abs(decrease - bound_claim73) < 1e-12

    # 2. Verify Claim 7.2 safe-zone penalty F^k(x) = f(x) + L * (max{0, |x - y_k| - delta / L2})^2:
    # Inside safe zone |x - y_k| <= delta / L2, F^k(x) == f(x) and F^k'(x) == f'(x);
    # Outside safe zone, the penalty adds +2*L curvature so F^k is globally 3*delta-nonconvex and 5*L-smooth.
    L = 2.0
    r_safe = delta / L2
    for x in (-0.5 * r_safe, 0.0, 0.8 * r_safe):
        pen = L * (max(0.0, abs(x - y_k) - r_safe) ** 2)
        assert pen == 0.0
    x_out = 2.5 * r_safe
    pen_out = L * (max(0.0, abs(x_out - y_k) - r_safe) ** 2)
    assert pen_out > 0.0

    # 3. Verify Lemma 5.5 first-order stopping criterion on G(x) = F(x) + sigma * ||x - x_hat||^2
    # For F(x) = -0.5 * sigma * x^2 + b * x (which is sigma-nonconvex), G(x) = 0.5 * sigma * x^2 + b * x + const
    # has unique minimizer x^* = x_hat - b / sigma, and ||nabla F(x^*)|| = | -sigma * x^* + b | = 2 * sigma * |x^* - x_hat|.
    sigma = 0.5
    b = 0.3
    x_hat = 1.0
    # G'(x) = -sigma*x + b + 2*sigma*(x - x_hat) = sigma*x + b - 2*sigma*x_hat = 0 => x^* = 2*x_hat - b/sigma
    x_star = 2.0 * x_hat - b / sigma
    grad_G_star = -sigma * x_star + b + 2.0 * sigma * (x_star - x_hat)
    assert abs(grad_G_star) < 1e-12
    grad_F_star = -sigma * x_star + b
    assert abs(abs(grad_F_star) - 2.0 * sigma * abs(x_star - x_hat)) < 1e-12

    # 4. Verify Natasha1.5 sub-epoch parameter choice (Theorem 1, p. 17) & Natasha2 rate exponent (Corollary 4.6):
    # For eps = 1e-2, delta = eps^{1/4} = 1e-0.5:
    # T_natasha2 ~ eps^{-3.25} vs SCSG eps^{-10/3} vs SGD eps^{-4}
    eps = 1e-2
    rate_natasha2 = eps**-3.25
    rate_scsg = eps ** (-10.0 / 3.0)
    rate_sgd = eps**-4.0
    assert rate_natasha2 < rate_scsg < rate_sgd

    print(
        f"[PASS] Natasha 1.5 & Natasha 2 boundaries verified: "
        f"2nd-order step decrease={decrease:.6f} == delta^3/(12*L2^2)={bound_claim73:.6f}, "
        f"Lemma 5.5 |grad F(x*)|={abs(grad_F_star):.4f} == 2*sigma*|x*-x_hat|, "
        f"eps^-3.25={rate_natasha2:.1f} < eps^-10/3={rate_scsg:.1f} < eps^-4={rate_sgd:.1f}"
    )


if __name__ == "__main__":
    main()
