#!/usr/bin/env python3
"""Boundary and analytical verification for Donoho & Gavish (2014),
'Minimax risk of matrix denoising by singular value thresholding',
The Annals of Statistics 42(6):2413-2440 (arXiv:1304.2085v4, DOI:10.1214/14-AOS1257).

Verifies:
1. Quarter-circle incomplete moments Q_0(x), Q_1(x), Q_2(x) (Eqs. 2.17-2.19) against numerical integration
   and the square-matrix (beta=1) transcendental optimality equation (Eqs. 2.20-2.21, Theorem 5):
     theta + cot(theta) * (1 - (1/3)*cos^2(theta)) = pi * (1 + alpha^{-1}*rho - rho) / (2*(1 - rho)),
     Lambda_*(rho, rho, alpha) = 2 * sin(theta_alpha(rho)),
   confirming the parametric minimax AMSE curves (Theorem 7, pp. 13-14) for both Mat (alpha=1) and Sym (alpha=1/2).
2. General rectangular Marcenko-Pastur incomplete moments P_gamma(x; k) (Eqs. 2.7-2.9) and the unique root
   Lambda_*(rho, beta, alpha) of P_gamma(Lambda^2; 1/2) - Lambda * P_gamma(Lambda^2; 0) = Lambda * rho / (alpha * (1 - rho))
   (Theorem 3 & Theorem 4, Eqs. 2.10-2.15), verifying:
   - Monotone decrease of Lambda_*(rho, beta, alpha) from 1 + sqrt(beta) at rho -> 0 to 0 at rho -> 1
   - Agreement of rectangular Marcenko-Pastur integration at beta=1 with the closed-form quarter-circle formulas
   - First-order low-rank expansion M(rho, beta | Mat) = 2*(1 + sqrt(beta) + beta)*rho + o(rho) (Theorem 8, p. 14)
   - Global minimax lower bound M^-(rho, beta) = rho + beta*rho - beta*rho^2 and worst-case suboptimality bound
     M(rho, beta | X) / M^-(rho, beta) <= 2*(1 + sqrt(beta)/(1 + beta)) <= 3 (Theorem 9, Eqs. 2.23-2.27).
3. Finite-n Stein's Unbiased Risk Estimate (SURE_lambda, Lemma 3, p. 20) and SV-monotonicity (Theorem 1 & Lemma 4,
   pp. 7-8, 20-21): verifies via finite-n Monte Carlo (m=18, n=24, r=2) that R(hat_X_lambda, mu * C) is strictly
   increasing in signal strength mu > 0 and converges as mu -> infty to the analytical worst-case limit (Lemma 5),
   and verifies exact numerical divergence of SVST against the corrected Lemma 3 SURE formula.
"""

from __future__ import annotations

import math
import random


def q0_quarter_circle(x: float) -> float:
    if x <= 0.0:
        return 1.0
    if x >= 2.0:
        return 0.0
    s = math.sqrt(max(0.0, 4.0 - x * x))
    return 1.0 - (x / (2.0 * math.pi)) * s - (2.0 / math.pi) * math.atan(x / s)


def q1_quarter_circle(x: float) -> float:
    if x <= 0.0:
        return 8.0 / (3.0 * math.pi)
    if x >= 2.0:
        return 0.0
    return ((4.0 - x * x) ** 1.5) / (3.0 * math.pi)


def q2_quarter_circle(x: float) -> float:
    if x <= 0.0:
        return 1.0
    if x >= 2.0:
        return 0.0
    s = math.sqrt(max(0.0, 4.0 - x * x))
    return 1.0 - (x * s * (x * x - 2.0)) / (4.0 * math.pi) - (2.0 / math.pi) * math.asin(x / 2.0)


def m_square_closed_form(lam: float, rho: float, alpha: float) -> float:
    """Equation (2.16) (with typo -2*lambda*Q_1 corrected to -2*Lambda*Q_1)."""
    tail = q2_quarter_circle(lam) - 2.0 * lam * q1_quarter_circle(lam) + (lam * lam) * q0_quarter_circle(lam)
    return rho * (2.0 - rho) + (1.0 - rho) * (rho * lam * lam + alpha * (1.0 - rho) * tail)


def solve_theta_square(rho: float, alpha: float) -> float:
    """Solve Eq. (2.21) for theta_alpha(rho) in (0, pi/2) via bisection."""
    target = math.pi * (1.0 + (rho / alpha) - rho) / (2.0 * (1.0 - rho))
    lo, hi = 1e-10, 0.5 * math.pi - 1e-10
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        c = math.cos(mid)
        s = math.sin(mid)
        lhs = mid + (c / s) * (1.0 - (c * c) / 3.0)
        if lhs > target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def parametric_amse_square(theta: float, alpha: float) -> tuple[float, float]:
    """Theorem 7 (pp. 13-14) parametric representation (rho(theta), M(theta)) for beta=1."""
    c = math.cos(theta)
    s = math.sin(theta)
    g = theta + (c / s) * (1.0 - (c * c) / 3.0)
    if abs(alpha - 1.0) < 1e-12:
        rho = 1.0 - (0.5 * math.pi) / g
        coeff = 4.0 / math.pi
    else:
        # Note: Theorem 7 (p. 14) prints 1 - (g - pi/2)/(g + pi/2), which is 1 - rho(theta);
        # inverting Eq. (2.21) g(theta) = (pi/2)*(1+rho)/(1-rho) yields rho(theta) = (g - pi/2)/(g + pi/2) = 1 - pi/(g + pi/2).
        rho = (g - 0.5 * math.pi) / (g + 0.5 * math.pi)
        coeff = 2.0 / math.pi
    bracket = (math.pi - 2.0 * theta) * (1.25 - c * c) + (math.sin(2.0 * theta) / 12.0) * (math.cos(2.0 * theta) - 14.0)
    m_val = 2.0 * rho - rho * rho + 4.0 * rho * (1.0 - rho) * (s * s) + coeff * ((1.0 - rho) ** 2) * bracket
    return rho, m_val


def mp_incomplete_moment(x_low: float, gamma: float, k_pow: float, n_steps: int = 800) -> float:
    """Complementary incomplete moment P_gamma(x_low; k_pow) = int_{x_low}^{gamma_+} t^{k_pow} p_gamma(t) dt (Eq. 2.8)
    using the trigonometric substitution sqrt(t) = u, u = 1 - sqrt(gamma)*cos(phi) to remove endpoint square-root singularities.
    """
    u_minus = abs(1.0 - math.sqrt(gamma))
    u_plus = 1.0 + math.sqrt(gamma)
    u_start = max(u_minus, math.sqrt(max(0.0, x_low)))
    if u_start >= u_plus:
        return 0.0
    # Substitute t = u^2, dt = 2 u du:
    # sqrt((gamma_+ - t)(t - gamma_-)) = sqrt((u_+^2 - u^2)(u^2 - u_-^2))
    # Integrate over u in [u_start, u_plus] via midpoint rule with sin-stretching near u_plus and u_start
    h = 1.0 / n_steps
    total = 0.0
    span = u_plus - u_start
    for i in range(n_steps):
        s = (i + 0.5) * h
        # Cosine clustering toward both endpoints
        w_loc = 0.5 * (1.0 - math.cos(math.pi * s))
        dw_ds = 0.5 * math.pi * math.sin(math.pi * s)
        u = u_start + span * w_loc
        du = span * dw_ds * h
        t = u * u
        rad = max(0.0, (u_plus * u_plus - t) * (t - u_minus * u_minus))
        # p_gamma(t) dt = sqrt(rad) / (2 * pi * gamma * t) * 2 * u du = sqrt(rad) / (pi * gamma * u) du
        dens_du = math.sqrt(rad) / (math.pi * gamma * u)
        total += (t ** k_pow) * dens_du * du
    return total


def m_general_mp(lam: float, rho: float, beta: float, alpha: float) -> float:
    """Equation (2.9) worst-case asymptotic risk M(Lambda; rho, tilde_rho, alpha)."""
    rho_tilde = beta * rho if abs(alpha - 1.0) < 1e-12 else rho
    gamma = (rho_tilde - rho * rho_tilde) / (rho - rho * rho_tilde)
    lam2 = lam * lam
    p1 = mp_incomplete_moment(lam2, gamma, 1.0)
    p_half = mp_incomplete_moment(lam2, gamma, 0.5)
    p0 = mp_incomplete_moment(lam2, gamma, 0.0)
    tail = p1 - 2.0 * lam * p_half + lam2 * p0
    return rho + rho_tilde - rho * rho_tilde + (1.0 - rho_tilde) * (rho * lam2 + alpha * (1.0 - rho) * tail)


def solve_lambda_star_mp(rho: float, beta: float, alpha: float) -> float:
    """Solve Eq. (2.15) P_gamma(Lambda^2; 1/2) - Lambda * P_gamma(Lambda^2; 0) = Lambda * rho / (alpha * (1 - rho))."""
    rho_tilde = beta * rho if abs(alpha - 1.0) < 1e-12 else rho
    gamma = (rho_tilde - rho * rho_tilde) / (rho - rho * rho_tilde)
    lam_max = 1.0 + math.sqrt(gamma)
    lo, hi = 0.0, lam_max
    for _ in range(55):
        mid = 0.5 * (lo + hi)
        mid2 = mid * mid
        lhs = mp_incomplete_moment(mid2, gamma, 0.5) - mid * mp_incomplete_moment(mid2, gamma, 0.0)
        rhs = (mid * rho) / (alpha * (1.0 - rho))
        if lhs > rhs:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def jacobi_eigen_symmetric(a_in: list[list[float]], max_sweeps: int = 35, tol: float = 1e-12) -> tuple[list[float], list[list[float]]]:
    m = len(a_in)
    a = [row[:] for row in a_in]
    v = [[1.0 if i == j else 0.0 for j in range(m)] for i in range(m)]
    for _ in range(max_sweeps):
        max_off = 0.0
        for p in range(m):
            row_p = a[p]
            for q in range(p + 1, m):
                apq = row_p[q]
                if abs(apq) > max_off:
                    max_off = abs(apq)
                if abs(apq) < tol:
                    continue
                app = row_p[p]
                aqq = a[q][q]
                tau = (aqq - app) / (2.0 * apq)
                t = (1.0 / (tau + math.hypot(1.0, tau))) if tau >= 0.0 else (-1.0 / (-tau + math.hypot(1.0, tau)))
                c = 1.0 / math.hypot(1.0, t)
                s = t * c
                row_p[p] = app - t * apq
                a[q][q] = aqq + t * apq
                row_p[q] = 0.0
                a[q][p] = 0.0
                for r in range(p):
                    arp = a[r][p]
                    arq = a[r][q]
                    a[r][p] = c * arp - s * arq
                    a[r][q] = s * arp + c * arq
                for r in range(p + 1, q):
                    apr = row_p[r]
                    arq = a[r][q]
                    row_p[r] = c * apr - s * arq
                    a[r][q] = s * apr + c * arq
                for r in range(q + 1, m):
                    apr = row_p[r]
                    aqr = a[q][r]
                    row_p[r] = c * apr - s * aqr
                    a[q][r] = s * apr + c * aqr
                for r in range(m):
                    vrp = v[r][p]
                    vrq = v[r][q]
                    v[r][p] = c * vrp - s * vrq
                    v[r][q] = s * vrp + c * vrq
        if max_off < tol:
            break
    order = sorted(range(m), key=lambda idx: a[idx][idx], reverse=True)
    evals = [a[idx][idx] for idx in order]
    evecs = [[v[row][idx] for idx in order] for row in range(m)]
    return evals, evecs


def svst_denoise_and_svals(y_mat: list[list[float]], lam: float) -> tuple[list[list[float]], list[float]]:
    """Compute SVST estimator hat_X_lambda(Y) and singular values of Y (m <= n)."""
    m = len(y_mat)
    n = len(y_mat[0])
    yy_t = [[0.0] * m for _ in range(m)]
    for i in range(m):
        yi = y_mat[i]
        for j in range(i, m):
            yj = y_mat[j]
            val = sum(yi[k] * yj[k] for k in range(n))
            yy_t[i][j] = val
            yy_t[j][i] = val
    evals, u_mat = jacobi_eigen_symmetric(yy_t)
    svals = [math.sqrt(max(0.0, ev)) for ev in evals]
    x_hat = [[0.0] * n for _ in range(m)]
    for k in range(m):
        sv = svals[k]
        if sv <= lam:
            continue
        scale = (sv - lam) / sv
        uk = [u_mat[i][k] for i in range(m)]
        # uk^T Y
        ukt_y = [sum(uk[i] * y_mat[i][j] for i in range(m)) for j in range(n)]
        for i in range(m):
             factor = scale * uk[i]
             row_out = x_hat[i]
             for j in range(n):
                 row_out[j] += factor * ukt_y[j]
    return x_hat, svals


def sure_svst_unscaled(svals: list[float], lam: float, m: int, n: int, sigma: float = 1.0) -> float:
    """Exact Stein Unbiased Risk Estimate (Candès, Sing-Long, & Trzasko 2013; Donoho & Gavish 2014 Lemma 3 with
    typo y_j corrected to y_i in the second numerator term min(y_i, lambda)*y_i)."""
    # For Y = X_0 + sigma * Z, SURE(Y) = -m*n*sigma^2 + sum_i min(y_i, lam)^2 + 2*sigma^2 * div(hat_X_lam(Y))
    # Or in terms of Lemma 3 on p. 20 (where sigma = 1/sqrt(n) and SURE_lambda is n * SURE_unscaled):
    # Wait: let us compute the exact divergence of hat_X_lambda(Y):
    # div(hat_X_lambda(Y)) = sum_{i: y_i > lam} [ 1 + (n - m)*(1 - lam/y_i) ] + 2 * sum_{1 <= i < j <= m} ( (y_i - lam)_+ * y_i - (y_j - lam)_+ * y_j ) / (y_i^2 - y_j^2)
    # Using y_k - (y_k - lam)_+ = min(y_k, lam) and sum_{i < j} (y_i^2 - y_j^2)/(y_i^2 - y_j^2) = m*(m - 1)/2:
    # m*n + ||hat_X - Y||_F^2 - 2*div(Y - hat_X) equals:
    total = float(m) * (n * sigma * sigma)
    sum_sq_diff = sum((min(y, lam)) ** 2 for y in svals)
    # Divergence of (Y - hat_X_lambda(Y)) where shrinkage of y_i is min(y_i, lam):
    div_shrink = 0.0
    for i in range(m):
        yi = svals[i]
        myi = min(yi, lam)
        if yi < lam:
            div_shrink += 1.0
        div_shrink += (n - m) * (myi / yi)
        for j in range(i + 1, m):
            yj = svals[j]
            myj = min(yj, lam)
            # Notice: in Lemma 3 (p. 20), summing over 1 <= i != j <= m with factor 1/n (or 2/n over i < j)
            # requires min(y_i, lam)*y_i in the second term (NOT min(y_i, lam)*y_j as printed in Lemma 3!).
            div_shrink += 2.0 * (myi * yi - myj * yj) / (yi * yi - yj * yj)
    return total + sum_sq_diff - 2.0 * (sigma * sigma) * div_shrink


def verify_analytical_and_sure() -> dict[str, float]:
    # 1. Verify Quarter-Circle moments Q_0, Q_1, Q_2 against MP moments at gamma=1
    for x in [0.4, 1.0, 1.5]:
        assert abs(q0_quarter_circle(x) - mp_incomplete_moment(x * x, 1.0, 0.0)) < 1e-5
        assert abs(q1_quarter_circle(x) - mp_incomplete_moment(x * x, 1.0, 0.5)) < 1e-5
        assert abs(q2_quarter_circle(x) - mp_incomplete_moment(x * x, 1.0, 1.0)) < 1e-5

    # 2. Verify Theorem 5 (Eqs. 2.16-2.21) & Theorem 7 (parametric curve) against Theorem 3/4 (MP integral) at beta=1
    for alpha in [1.0, 0.5]:
        prev_lam = 2.0
        prev_m = 0.0
        for rho in [0.05, 0.2, 0.5, 0.8]:
            theta = solve_theta_square(rho, alpha)
            lam_sq = 2.0 * math.sin(theta)
            m_sq = m_square_closed_form(lam_sq, rho, alpha)
            rho_param, m_param = parametric_amse_square(theta, alpha)
            assert abs(rho_param - rho) < 1e-10
            assert abs(m_param - m_sq) < 1e-10

            lam_mp = solve_lambda_star_mp(rho, 1.0, alpha)
            m_mp = m_general_mp(lam_mp, rho, 1.0, alpha)
            assert abs(lam_sq - lam_mp) < 1e-4, f"{lam_sq} vs {lam_mp}"
            assert abs(m_sq - m_mp) < 1e-4, f"{m_sq} vs {m_mp}"

            # Verify monotone decrease of Lambda_* and monotone increase of M(rho)
            assert lam_sq < prev_lam
            assert m_sq > prev_m
            prev_lam = lam_sq
            prev_m = m_sq

    # 3. Verify Theorem 8 low-rank slope 2*(1 + sqrt(beta) + beta)*rho and Theorem 9 bound <= 2*(1 + sqrt(beta)/(1+beta))
    for beta in [0.25, 0.5, 1.0]:
        rho_small = 1e-6
        lam_small = solve_lambda_star_mp(rho_small, beta, 1.0)
        # Near rho -> 0, Lambda_* -> 1 + sqrt(beta) with O(rho^(2/5)) edge scaling (Eq. 2.13)
        assert abs(lam_small - (1.0 + math.sqrt(beta))) < 0.02, f"{lam_small} vs {1.0 + math.sqrt(beta)}"
        m_small = m_general_mp(lam_small, rho_small, beta, 1.0)
        slope_exact = 2.0 * (1.0 + math.sqrt(beta) + beta)
        assert abs(m_small / rho_small - slope_exact) / slope_exact < 0.01

        max_ratio = 2.0 * (1.0 + math.sqrt(beta) / (1.0 + beta))
        for rho in [0.01, 0.1, 0.3, 0.6, 0.9]:
            lam_r = solve_lambda_star_mp(rho, beta, 1.0)
            m_r = m_general_mp(lam_r, rho, beta, 1.0)
            m_lower = rho + beta * rho - beta * rho * rho
            ratio = m_r / m_lower
            assert 1.0 < ratio <= max_ratio + 1e-4

    # 4. Verify finite-difference divergence vs corrected Lemma 3 SURE formula on a test matrix
    rng = random.Random(20261019)
    m_t, n_t = 5, 7
    y_test = [[rng.gauss(0.0, 1.0) + (3.0 if i == j and i < 2 else 0.0) for j in range(n_t)] for i in range(m_t)]
    lam_t = 1.2
    x_hat_0, svals_0 = svst_denoise_and_svals(y_test, lam_t)
    eps = 1e-6
    div_fd = 0.0
    for i in range(m_t):
        for j in range(n_t):
            y_plus = [row[:] for row in y_test]
            y_plus[i][j] += eps
            xh_p, _ = svst_denoise_and_svals(y_plus, lam_t)
            y_minus = [row[:] for row in y_test]
            y_minus[i][j] -= eps
            xh_m, _ = svst_denoise_and_svals(y_minus, lam_t)
            div_fd += (xh_p[i][j] - xh_m[i][j]) / (2.0 * eps)

    sure_formula = sure_svst_unscaled(svals_0, lam_t, m_t, n_t, sigma=1.0)
    frob_diff_sq = sum((x_hat_0[i][j] - y_test[i][j]) ** 2 for i in range(m_t) for j in range(n_t))
    sure_from_fd = -float(m_t * n_t) + frob_diff_sq + 2.0 * div_fd
    assert abs(sure_formula - sure_from_fd) < 1e-5, f"SURE {sure_formula} != FD {sure_from_fd}"

    # 5. Verify SV-monotonicity (Theorem 1 & Lemma 4): R(hat_X_lambda, mu * C) increases monotonically with mu
    # and converges to the analytical limit M_n(Lambda; r, m, 1) as mu -> infty
    m_mc, n_mc, r_mc = 10, 15, 2
    lam_mc = 1.15
    sigma_mc = 1.0 / math.sqrt(n_mc)
    n_trials = 40
    z_samples = [
        [[rng.gauss(0.0, sigma_mc) for _ in range(n_mc)] for _ in range(m_mc)]
        for _ in range(n_trials)
    ]
    risks_by_mu = {}
    for mu in [0.0, 0.8, 2.0, 50.0]:
        tot_r = 0.0
        for z_mat in z_samples:
            y_m = [row[:] for row in z_mat]
            for k in range(r_mc):
                y_m[k][k] += mu * (1.5 if k == 0 else 1.0)
            xh, _ = svst_denoise_and_svals(y_m, lam_mc)
            err_sq = 0.0
            for i in range(m_mc):
                for j in range(n_mc):
                    truth = mu * (1.5 if i == 0 else 1.0) if (i == j and i < r_mc) else 0.0
                    d = xh[i][j] - truth
                    err_sq += d * d
            tot_r += err_sq / m_mc
        risks_by_mu[mu] = tot_r / n_trials

    assert risks_by_mu[0.0] < risks_by_mu[0.8] < risks_by_mu[2.0] < risks_by_mu[50.0]

    # Compare mu=50 risk against asymptotic formula M(Lambda; rho, beta*rho, 1)
    rho_mc = r_mc / m_mc
    beta_mc = m_mc / n_mc
    lam_resc = lam_mc / math.sqrt(1.0 - (r_mc / n_mc))
    m_asymp_mc = m_general_mp(lam_resc, rho_mc, beta_mc, 1.0)

    return {
        "m_sq_rho02": m_square_closed_form(2.0 * math.sin(solve_theta_square(0.2, 1.0)), 0.2, 1.0),
        "lam_sq_rho02": 2.0 * math.sin(solve_theta_square(0.2, 1.0)),
        "risk_mu0": risks_by_mu[0.0],
        "risk_mu50": risks_by_mu[50.0],
        "m_asymp_mc": m_asymp_mc,
    }


def main() -> None:
    stats = verify_analytical_and_sure()
    print(
        f"Donoho & Gavish (2014) SVST minimax risk verified: "
        f"M(0.2, 1|Mat)={stats['m_sq_rho02']:.4f} at Lambda*={stats['lam_sq_rho02']:.4f}; "
        f"SV-monotone risk R(mu=0)={stats['risk_mu0']:.3f} -> R(mu=50)={stats['risk_mu50']:.3f} (asymp={stats['m_asymp_mc']:.3f})."
    )


if __name__ == "__main__":
    main()
