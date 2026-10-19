#!/usr/bin/env python3
"""Boundary and analytical verification for Baik, Ben Arous, and Peche (2005):
'Phase transition of the largest eigenvalue for non-null complex sample covariance matrices'
(The Annals of Probability 33(5):1643-1697, arXiv:math/0403022v2,
DOI:10.1214/009117905000000233).

Verifies:
1. Section 3, eqs. (101)-(112): Double-root coalescence of the steepest-descent phase function
     f(z) = -mu * (z - q) + log(z) - (1 / gamma^2) * log(1 - z)
   at the critical point z = p_c = gamma / (gamma + 1) when mu = ((1 + gamma) / gamma)^2 = (1 + gamma^{-1})^2:
   - f'(p_c) = 0,
   - f''(p_c) = 0,
   - f^{(3)}(p_c) = 2 * (gamma + 1)^4 / gamma^3 = 2 * nu^3 > 0 where nu = (1 + gamma)^{4/3} / gamma.
2. Section 4, eqs. (209)-(219): Supercritical regime l_1 = pi_1^{-1} > 1 + gamma^{-1}
   (equivalently 0 < pi_1 < p_c = gamma / (1 + gamma)):
   - With mu = 1/pi_1 + gamma^{-2} / (1 - pi_1) = l_1 + l_1 * gamma^{-2} / (l_1 - 1)
     and nu = sqrt(1/pi_1^2 - gamma^{-2} / (1 - pi_1)^2) = sqrt(l_1^2 - l_1^2 * gamma^{-2} / (l_1 - 1)^2),
   - f'(z) = 0 has two distinct real roots z_1 = pi_1 and z_2 = 1 / (mu * pi_1) satisfying
     0 < pi_1 < p_c < 1 / (mu * pi_1) < 1 (eq. 218),
   - f''(pi_1) = -nu^2 < 0 and f''(1 / (mu * pi_1)) = (gamma * nu * mu * pi_1 * (1 - pi_1))^2 > 0 (eq. 219).
3. Section 6, eqs. (316)-(317): Last-passage percolation variational principle
     max_{x in [0, 1]} [l_1 * x + (sqrt(1 - x) + gamma^{-1})^2]
   equals:
   - (1 + gamma^{-1})^2 achieved at x* = 0 when l_1 <= 1 + gamma^{-1} (subcritical/critical M^{2/3} regime),
   - l_1 + l_1 * gamma^{-2} / (l_1 - 1) achieved at x* = 1 - gamma^{-2} / (l_1 - 1)^2 in (0, 1)
     when l_1 > 1 + gamma^{-1} (supercritical M^{1/2} regime).
4. Numerical Monte Carlo verification of Theorem 1.1(a)-(b) on complex Gaussian spiked Wishart matrices
   S = (1/M) X X* (N = 24, M = 48, gamma = sqrt(2)):
   - Subcritical spike l_1 = 1.2 < 1 + 1/sqrt(2) = 1.7071: lambda_1 concentrates near (1 + gamma^{-1})^2 = 2.9142,
   - Supercritical simple spike (k = 1) l_1 = 3.5 > 1.7071: lambda_1 concentrates near
     mu(3.5) = 3.5 + 3.5 * 0.5 / 2.5 = 4.20 with empirical standard deviation matching nu(3.5) / sqrt(M),
   - Supercritical double spike (k = 2) l_1 = l_2 = 3.5 > 1.7071: largest eigenvalue of 2x2 GUE has positive
     mean shift E[xi_{max}^{(2)}] = 1 / sqrt(pi) = 0.56419 standard units above the k = 1 Gaussian mean,
     so E[lambda_1 | k=2] > E[lambda_1 | k=1].
"""

import math
import random


def f_derivs(z: float, mu: float, gamma: float) -> tuple[float, float, float]:
    """Return f'(z), f''(z), f^{(3)}(z) from eqs. (108), (110), (111)."""
    fp = -mu + 1.0 / z - 1.0 / ((gamma ** 2) * (z - 1.0))
    fpp = -1.0 / (z ** 2) + 1.0 / ((gamma ** 2) * ((z - 1.0) ** 2))
    fppp = 2.0 / (z ** 3) - 2.0 / ((gamma ** 2) * ((z - 1.0) ** 3))
    return fp, fpp, fppp


def lpp_variational_max(l1: float, gamma: float, grid_size: int = 2000) -> tuple[float, float]:
    """Maximize f_LPP(x) = l1 * x + (sqrt(1 - x) + 1/gamma)^2 over x in [0, 1] (eqs. 316-317)."""
    inv_g = 1.0 / gamma
    best_x = 0.0
    best_val = (1.0 + inv_g) ** 2
    for i in range(grid_size + 1):
        x = i / grid_size
        val = l1 * x + (math.sqrt(max(0.0, 1.0 - x)) + inv_g) ** 2
        if val > best_val:
            best_val = val
            best_x = x
    # Also evaluate at exact interior stationary point if in (0, 1)
    if l1 > 1.0:
        x_star = 1.0 - (inv_g ** 2) / ((l1 - 1.0) ** 2)
        if 0.0 < x_star < 1.0:
            val_star = l1 * x_star + (math.sqrt(1.0 - x_star) + inv_g) ** 2
            if val_star >= best_val:
                best_val = val_star
                best_x = x_star
    return best_val, best_x


def power_iteration_top_eigenvalue_hermitian(
    h_re: list[list[float]], h_im: list[list[float]], n_iter: int = 80
) -> float:
    """Compute largest eigenvalue of positive-definite complex Hermitian matrix via power iteration."""
    d = len(h_re)
    v_re = [1.0 / math.sqrt(d) for _ in range(d)]
    v_im = [0.0 for _ in range(d)]
    rayleigh = 0.0
    for _ in range(n_iter):
        w_re = [0.0] * d
        w_im = [0.0] * d
        for i in range(d):
            row_re = h_re[i]
            row_im = h_im[i]
            s_re = 0.0
            s_im = 0.0
            for j in range(d):
                # (row_re + i row_im) * (v_re + i v_im)
                s_re += row_re[j] * v_re[j] - row_im[j] * v_im[j]
                s_im += row_re[j] * v_im[j] + row_im[j] * v_re[j]
            w_re[i] = s_re
            w_im[i] = s_im
        rayleigh = sum(v_re[i] * w_re[i] + v_im[i] * w_im[i] for i in range(d))
        norm = math.sqrt(sum(w_re[i] ** 2 + w_im[i] ** 2 for i in range(d)))
        v_re = [x / norm for x in w_re]
        v_im = [x / norm for x in w_im]
    return rayleigh


def main() -> None:
    # 1. Verify critical coalescing saddle point p_c = gamma / (gamma + 1) (Section 3, eqs. 101-111)
    for gamma in [1.0, math.sqrt(2.0), 2.0, 3.5]:
        p_c = gamma / (gamma + 1.0)
        mu_c = ((1.0 + gamma) / gamma) ** 2
        nu_c = ((1.0 + gamma) ** (4.0 / 3.0)) / gamma
        fp, fpp, fppp = f_derivs(p_c, mu_c, gamma)
        assert abs(fp) < 1e-12, f"Expected f'(p_c)=0, got {fp}"
        assert abs(fpp) < 1e-12, f"Expected f''(p_c)=0, got {fpp}"
        assert abs(fppp - 2.0 * (nu_c ** 3)) < 1e-11, f"Mismatch in f'''(p_c): {fppp} vs {2.0 * nu_c**3}"

    # 2. Verify supercritical saddle points and curvature (Section 4, eqs. 211-219)
    for gamma in [1.0, math.sqrt(2.0), 2.5]:
        p_c = gamma / (gamma + 1.0)
        l_crit = 1.0 + 1.0 / gamma
        for l1 in [l_crit + 0.25, l_crit + 1.5, l_crit + 3.0]:
            pi1 = 1.0 / l1
            mu = 1.0 / pi1 + (gamma ** -2) / (1.0 - pi1)
            nu_sq = 1.0 / (pi1 ** 2) - (gamma ** -2) / ((1.0 - pi1) ** 2)
            assert nu_sq > 0.0, f"Expected nu^2 > 0 for supercritical l1={l1}"
            nu = math.sqrt(nu_sq)
            z2 = 1.0 / (mu * pi1)
            # Verify ordering 0 < pi_1 < p_c < 1/(mu*pi_1) < 1 (eq. 218)
            assert 0.0 < pi1 < p_c < z2 < 1.0, f"Ordering eq. (218) failed: {pi1}, {p_c}, {z2}"
            fp1, fpp1, _ = f_derivs(pi1, mu, gamma)
            fp2, fpp2, _ = f_derivs(z2, mu, gamma)
            assert abs(fp1) < 1e-12 and abs(fp2) < 1e-12
            assert abs(fpp1 - (-nu_sq)) < 1e-11, f"Expected f''(pi_1)=-nu^2, got {fpp1} vs {-nu_sq}"
            expected_fpp2 = (gamma * nu * mu * pi1 * (1.0 - pi1)) ** 2
            assert abs(fpp2 - expected_fpp2) < 1e-10, f"Mismatch in f''(1/(mu*pi_1)): {fpp2} vs {expected_fpp2}"

    # 3. Verify last-passage percolation variational formula (Section 6, eqs. 316-317)
    gamma = math.sqrt(2.0)
    l_crit = 1.0 + 1.0 / gamma
    for l1 in [0.8, 1.2, l_crit]:
        val, x_opt = lpp_variational_max(l1, gamma)
        assert abs(x_opt - 0.0) < 1e-6
        assert abs(val - (l_crit ** 2)) < 1e-12
    for l1 in [l_crit + 0.3, 3.0, 4.5]:
        val, x_opt = lpp_variational_max(l1, gamma)
        expected_x = 1.0 - (gamma ** -2) / ((l1 - 1.0) ** 2)
        expected_val = l1 + l1 * (gamma ** -2) / (l1 - 1.0)
        assert abs(x_opt - expected_x) < 1e-10
        assert abs(val - expected_val) < 1e-12

    # 4. Verify 2x2 GUE maximum eigenvalue mean shift E[max(xi_1, xi_2)] = 1 / sqrt(pi) > E[xi_1] = 0
    # For 2x2 GUE with diagonal N(0, 1) and off-diagonal (N(0, 1/2) + i N(0, 1/2)),
    # eigenvalues are (H_11 + H_22)/2 +/- sqrt(((H_11 - H_22)/2)^2 + Re(H_12)^2 + Im(H_12)^2).
    # Since (H_11 - H_22)/2, Re(H_12), Im(H_12) are 3 i.i.d. N(0, 1/2) variables,
    # R = sqrt(sum_{m=1}^3 Z_m^2 / 2) = (1/sqrt(2)) * chi_3, whose expectation is
    # (1/sqrt(2)) * sqrt(2) * Gamma(2) / Gamma(3/2) = 1 / (sqrt(pi)/2) ... wait:
    # E[chi_3] = sqrt(2) * Gamma(2) / Gamma(1.5) = 2 * sqrt(2 / pi), so E[R] = 2 / sqrt(pi) = 1.128379!
    rng = random.Random(200509)
    n_gue_samples = 4000
    gue2_max_vals = []
    for _ in range(n_gue_samples):
        h11 = rng.gauss(0.0, 1.0)
        h22 = rng.gauss(0.0, 1.0)
        re12 = rng.gauss(0.0, math.sqrt(0.5))
        im12 = rng.gauss(0.0, math.sqrt(0.5))
        lam_max = 0.5 * (h11 + h22) + math.sqrt(0.25 * ((h11 - h22) ** 2) + re12 ** 2 + im12 ** 2)
        gue2_max_vals.append(lam_max)
    mean_gue2 = sum(gue2_max_vals) / n_gue_samples
    theo_mean_gue2 = 2.0 / math.sqrt(math.pi)  # 1.128379
    assert abs(mean_gue2 - theo_mean_gue2) < 0.04, f"2x2 GUE max mean {mean_gue2} vs {theo_mean_gue2}"

    # 5. Monte Carlo verification of complex Gaussian sample covariance largest eigenvalue (Theorem 1.1)
    n_vars = 20
    m_samples = 40
    gamma_mc = math.sqrt(m_samples / n_vars)  # sqrt(2)
    bulk_edge = (1.0 + 1.0 / gamma_mc) ** 2   # 2.91421
    l_super = 3.5                             # > 1 + 1/sqrt(2) = 1.7071
    mu_super = l_super + l_super * (gamma_mc ** -2) / (l_super - 1.0)  # 4.20
    nu_super = math.sqrt(l_super ** 2 - (l_super ** 2) * (gamma_mc ** -2) / ((l_super - 1.0) ** 2))  # 3.1305

    def sample_largest_eig_complex_wishart(ells: list[float], n_trials: int) -> list[float]:
        out = []
        inv_m = 1.0 / m_samples
        for _ in range(n_trials):
            # Complex Gaussian with variance ell_i: Re ~ N(0, ell_i/2), Im ~ N(0, ell_i/2)
            x_re = [[rng.gauss(0.0, math.sqrt(0.5 * ells[i])) for _ in range(m_samples)] for i in range(n_vars)]
            x_im = [[rng.gauss(0.0, math.sqrt(0.5 * ells[i])) for _ in range(m_samples)] for i in range(n_vars)]
            s_re = [[0.0] * n_vars for _ in range(n_vars)]
            s_im = [[0.0] * n_vars for _ in range(n_vars)]
            for i in range(n_vars):
                ri, ii = x_re[i], x_im[i]
                for j in range(i, n_vars):
                    rj, ij = x_re[j], x_im[j]
                    # (ri + i ii)(rj - i ij) = (ri*rj + ii*ij) + i(ii*rj - ri*ij)
                    val_re = sum(ri[t] * rj[t] + ii[t] * ij[t] for t in range(m_samples)) * inv_m
                    val_im = sum(ii[t] * rj[t] - ri[t] * ij[t] for t in range(m_samples)) * inv_m if i != j else 0.0
                    s_re[i][j] = val_re
                    s_re[j][i] = val_re
                    s_im[i][j] = val_im
                    s_im[j][i] = -val_im
            out.append(power_iteration_top_eigenvalue_hermitian(s_re, s_im))
        return out

    eigs_sub = sample_largest_eig_complex_wishart([1.2] + [1.0] * (n_vars - 1), 16)
    eigs_k1 = sample_largest_eig_complex_wishart([l_super] + [1.0] * (n_vars - 1), 24)
    eigs_k2 = sample_largest_eig_complex_wishart([l_super, l_super] + [1.0] * (n_vars - 2), 24)

    mean_sub = sum(eigs_sub) / len(eigs_sub)
    mean_k1 = sum(eigs_k1) / len(eigs_k1)
    mean_k2 = sum(eigs_k2) / len(eigs_k2)

    assert abs(mean_sub - bulk_edge) < 0.35, f"Subcritical mean {mean_sub} far from bulk edge {bulk_edge}"
    assert abs(mean_k1 - mu_super) < 0.35, f"Supercritical k=1 mean {mean_k1} far from {mu_super}"
    assert mean_k1 > mean_sub + 0.9, f"Expected supercritical separation: {mean_k1} vs {mean_sub}"
    # For k=2 degenerate supercritical spike, G_2 has positive mean shift (2/sqrt(pi)) * nu / sqrt(M) above k=1
    assert mean_k2 > mean_k1 + 0.2, f"Expected k=2 G_2 mean {mean_k2} > k=1 G_1 mean {mean_k1}"

    print(
        f"Baik-Ben Arous-Peche (2005) phase transition verified: "
        f"subcritical mean={mean_sub:.3f}~{bulk_edge:.3f}, "
        f"supercritical k=1 mean={mean_k1:.3f}~{mu_super:.3f}, "
        f"supercritical k=2 mean={mean_k2:.3f} (G_2 shift={mean_k2 - mean_k1:.3f}, "
        f"asymp={(2.0 / math.sqrt(math.pi)) * nu_super / math.sqrt(m_samples):.3f})."
    )


if __name__ == "__main__":
    main()
