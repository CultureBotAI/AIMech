#!/usr/bin/env python3
"""Boundary and verification script for Round 338:
Gradient Descent Converges to Minimizers (Stable Manifold Theorem Avoidance of Strict Saddles)
(Lee, Simchowitz, Jordan, & Recht, COLT 2016, PMLR 49:1246-1257, arXiv:1602.04915).
"""

import math
import random
import sys


def f_quartic(x, y):
    """Section 3 Example (p. 4): f(x, y) = 0.5 x^2 + 0.25 y^4 - 0.5 y^2."""
    return 0.5 * x * x + 0.25 * (y ** 4) - 0.5 * y * y


def grad_quartic(x, y):
    return (x, (y ** 3) - y)


def g_map(x, y, alpha):
    """Gradient map g(x, y) = [(1 - alpha) x, (1 + alpha) y - alpha y^3] (Section 3, p. 4)."""
    gx, gy = grad_quartic(x, y)
    return (x - alpha * gx, y - alpha * gy)


def inv_g_proximal(yx, yy, alpha):
    """Proposition 4.5 (Section 4.1, p. 6):
    For alpha < 1/L, g is a diffeomorphism whose inverse x_y = g^{-1}(y) is the unique minimizer of
    the strongly convex proximal-point objective on -f:
      min_x  0.5 ||x - y||_2^2 - alpha f(x)  <=>  x - alpha grad f(x) = y.
    Solve via Newton's method on the strongly convex proximal objective.
    """
    x = yx / (1.0 - alpha)
    y = yy
    for _ in range(40):
        # Residual of y_var + alpha (y_var - y_var^3) - yy = 0
        res = (1.0 + alpha) * y - alpha * (y ** 3) - yy
        jac = (1.0 + alpha) - 3.0 * alpha * (y ** 2)
        y -= res / jac
    return (x, y)


def main():
    # On [-1.2, 1.2]^2, max eigenvalue of Hessian diag(1, 3 y^2 - 1) is L = 3*(1.2)^2 - 1 = 3.32 < 4.0
    alpha = 0.2  # 0 < alpha < 1/L

    # 1. Verify Proposition 4.5 (Section 4.1, p. 6):
    # g is a bijection and diffeomorphism for alpha < 1/L, and proximal point on -f inverts g exactly.
    x0, y0 = 0.75, -0.45
    gx, gy = g_map(x0, y0, alpha)
    rx, ry = inv_g_proximal(gx, gy, alpha)
    prox_inv_err = math.hypot(rx - x0, ry - y0)

    # Verify Jacobian determinant det(Dg) = (1 - alpha) * (1 + alpha - 3 alpha y^2) > 0 everywhere on [-1.2, 1.2]^2
    min_det_dg = min(
        (1.0 - alpha) * (1.0 + alpha - 3.0 * alpha * (yv ** 2))
        for yv in [-1.2 + 0.1 * k for k in range(25)]
    )

    # 2. Verify Section 3 & Theorem 4.1 (pp. 4-5):
    # The global stable set W^s(z_1) of the strict saddle z_1 = (0, 0) (where Hess f(0,0) = diag(1, -1))
    # is the 1D subspace {(x, 0) : x in R} (Lebesgue measure zero in R^2).
    # (a) Any point on W^s(z_1) = {(x, 0)} converges to the saddle point (0, 0) at rate (1 - alpha)^k:
    xs, ys = 0.9, 0.0
    for _ in range(60):
        xs, ys = g_map(xs, ys, alpha)
    saddle_manifold_dist = math.hypot(xs - 0.0, ys - 0.0)
    exact_rate_err = abs(xs - 0.9 * ((1.0 - alpha) ** 60))

    # (b) Any random initialization outside the measure-zero x-axis escapes the strict saddle (0, 0)
    # and converges to one of the isolated local minima z_2 = (0, -1) or z_3 = (0, 1):
    rng = random.Random(20261019)
    escaped_count = 0
    n_trials = 40
    for _ in range(n_trials):
        xt = rng.uniform(-1.0, 1.0)
        yt = rng.uniform(-1.0, 1.0)
        if abs(yt) < 1e-3:
            yt = 0.01
        for _ in range(120):
            xt, yt = g_map(xt, yt, alpha)
        dist_min = min(math.hypot(xt, yt - 1.0), math.hypot(xt, yt + 1.0))
        if dist_min < 1e-6:
            escaped_count += 1

    # 3. Verify Proposition 4.11 (Section 4.2, pp. 7-8):
    # Lojasiewicz exponent a = 1/2 (strong convexity near z_3 = (0, 1)) gives geometric convergence C b^k,
    # whereas a degenerate non-strict critical point f_deg(x, y) = 0.5 x^2 + 0.25 y^4 (Hess = diag(1, 0),
    # Lojasiewicz exponent a = 3/4 > 1/2 since |grad f| = y^3 = 4^{3/4} (f)^{3/4}) converges only
    # sublinearly at rate O(k^{-(1-a)/(2a-1)}) = O(k^{-1/2})!
    yd = 0.5
    for _ in range(200):
        yd = yd - alpha * (yd ** 3)
    # Compare yd (sublinear ~ 1/sqrt(k)) vs non-degenerate y near z_3 (geometric):
    yn = 0.5
    for _ in range(200):
        _, yn = g_map(0.0, yn, alpha)
    nondeg_err = abs(yn - 1.0)

    # 4. Verify failure boundary when step size alpha >= 1/L (Section 4.1 & Section 5):
    # At alpha_bad = 1.0, Dg(0, 1) = diag(0, 1 - 2*1) = diag(0, -1) has det(Dg) = 0 (not a diffeomorphism!),
    # and g maps (x, 1) and (x', 1) to the same point (0, 1) (non-injective!).
    g1 = g_map(0.5, 1.0, 1.0)
    g2 = g_map(-0.7, 1.0, 1.0)
    non_injective_diff = math.hypot(g1[0] - g2[0], g1[1] - g2[1])

    ok = (
        prox_inv_err < 1e-14
        and min_det_dg > 0.0
        and exact_rate_err < 1e-15
        and saddle_manifold_dist < 2e-6
        and escaped_count == n_trials
        and nondeg_err < 1e-14
        and yd > 0.09
        and non_injective_diff == 0.0
    )
    if not ok:
        print("Verification failed!", file=sys.stderr)
        sys.exit(1)

    print(
        f"[PASS] Round 338 Stable Manifold GD (Lee et al. 2016): "
        f"prox_inv_err={prox_inv_err:.2e}, min_det_dg={min_det_dg:.4f}, "
        f"escaped={escaped_count}/{n_trials}, nondeg_err={nondeg_err:.2e}, deg_sublinear_err={yd:.4f}"
    )


if __name__ == "__main__":
    main()
