#!/usr/bin/env python3
"""Constructed boundary verification for Model-Free Regression Functionals,
Regressor-Reweighting Well-Specification Diagnostic, and M-of-N XY-Bootstrap
Limit (Buja, Brown, Kuchibhotla, Berk, George, & Zhao 2019, Statistical
Science 34(4):545-565, arXiv:1612.03257v2, DOI:10.1214/18-STS694).

Verifies using pure Python standard library:
1. Proper Scoring & Basu-Harris-Hjort-Jones (BHHJ) Density Power Divergence
   Fisher Consistency (Section 2.2, Equation 4, Appendix A.2):
   Under a Gaussian working conditional model q(y|x; theta) = N(y; beta'x, sigma^2),
   the BHHJ scoring rule S_alpha(y, Q) = -q(y)^alpha / alpha + int q(y)^(1+alpha) dy / (1+alpha)
   has closed-form integral (2*pi*sigma^2)^(-alpha/2) * (1+alpha)^(-3/2) / (1+alpha)
   and achieves its exact conditional expectation minimum at the true parameter
   (beta_0, sigma_0^2) when P_{Y|X} = Q_{Y|X; theta_0} for any alpha > 0, while
   possessing a redescending influence function psi(y) propto (y - mu) * exp(-alpha*(y-mu)^2/(2*sigma^2))
   that vanishes as |y - mu| -> infinity.
2. Well-Specification Characterization & Regressor-Only Reweighting Invariance
   (Section 3, Definition 3.1, Proposition 3.3.3, Section 4.1, Lemma 4.1, Proposition 4.1):
   - Reweighting P^w(dy, dx) = w(x) P(dy, dx) with E_P[w(X)] = 1 preserves P^w_{Y|X} = P_{Y|X}
     (Lemma 4.1).
   - When the functional is well-specified (E_P[psi(theta_0; Y, X) | X = x] = 0 for all x,
     Proposition 3.3.3), theta(P^w) = theta_0 is strictly invariant across all Gaussian
     reweighting centers xi in the diagnostic trace xi |-> theta(w_xi P) (Proposition 4.1),
     so the two-point tilt statistic d = theta_{xi_(K)} - theta_{xi_(1)} = 0.
   - When the conditional model is misspecified (e.g., quadratic nonlinearity E[Y|X=x] = beta_0 + beta_1 x + gamma x^2
     fitted by linear OLS), the partial influence function IF(x) = E[IF(Y, X) | X = x] is
     non-zero, the Gaussian reweighting trace xi |-> theta_1(w_xi P) varies systematically
     with xi (slope ~ 2*gamma), and the tilt statistic d != 0 detects misspecification.
3. Canonical Estimation Offset Decomposition & Pythagorean CLT Variance Split
   (Sections 6-7, Propositions 6.4-6.6, Corollary 7.1):
   - Total Estimation Offset: theta_hat - theta(P) = [theta_hat - theta(X)] + [theta(X) - theta(P)],
     where theta(X) = theta(P_{Y|X} (x) P_hat_X).
   - In the noiseless deterministic case Y = f(X), Noise EO = theta_hat - theta(X) = 0
     identically while Approximation EO = theta(X) - theta(P) != 0 under misspecification
     (Proposition 6.5).
   - For any EE functional with full influence function IF(Y, X) = -Lambda(theta)^(-1) psi(theta; Y, X)
     and partial influence function IF(X) = E_P[IF(Y, X) | X] (Lemma 6.6), the noise component
     IF(Y, X) - IF(X) and the approximation component IF(X) are strictly orthogonal in L^2(P),
     giving the exact Pythagorean asymptotic variance split:
     Var_P[IF(Y, X)] = E_P[Var_P[IF(Y, X) | X]] + Var_P[IF(X)] (Section 7.1, Corollary 7.1).
4. Exact M-of-N XY-Bootstrap Limit for Fixed Sample P_hat_N (Section 8, Proposition 8.1, Corollary 8.1):
   For a fixed sample (Y_i, X_i)_{i=1}^N defining the empirical distribution P_hat_N,
   drawing M bootstrap observations (Y_j*, X_j*)_{j=1}^M i.i.d. from P_hat_N yields
   M^(1/2) (theta_M* - theta_hat_N) ->_d N(0, AV[P_hat_N; theta(.)]) as M -> infinity,
   where AV[P_hat_N; theta(.)] is the empirical Huber sandwich covariance matrix
   Lambda_hat^(-1) V_hat[psi(theta_hat_N; Y, X)] (Lambda_hat')^(-1).
"""

import math
import random


def verify_bhhj_proper_scoring_and_redescending_if() -> None:
    """Verify BHHJ scoring rule Fisher consistency and redescending influence function."""
    sigma0 = 1.25
    mu0 = 2.0
    alpha = 0.5

    def bhhj_expected_score_gaussian(mu: float, sigma: float) -> float:
        """Exact analytical E_{N(mu0, sigma0^2)}[S_alpha(Y, N(mu, sigma^2))]."""
        # Term 1: -(1/alpha) * E_{N(mu0, sigma0^2)}[ q(Y; mu, sigma)^alpha ]
        # q(y)^alpha = (2*pi*sigma^2)^(-alpha/2) * exp(-alpha*(y-mu)^2 / (2*sigma^2))
        # Integrating against N(mu0, sigma0^2):
        eff_var = (sigma * sigma) / alpha + (sigma0 * sigma0)
        integral_p_q_alpha = (
            ((2.0 * math.pi * sigma * sigma) ** (-alpha / 2.0))
            * math.sqrt((sigma * sigma / alpha) / eff_var)
            * math.exp(-((mu - mu0) ** 2) / (2.0 * eff_var))
        )
        term1 = -integral_p_q_alpha / alpha

        # Term 2: (1/(1+alpha)) * int q(y)^(1+alpha) dy
        integral_q_1_plus_alpha = (
            ((2.0 * math.pi * sigma * sigma) ** (-alpha / 2.0))
            / math.sqrt(1.0 + alpha)
        )
        term2 = integral_q_1_plus_alpha / (1.0 + alpha)
        return term1 + term2

    opt_score = bhhj_expected_score_gaussian(mu0, sigma0)
    for d_mu in (-0.6, -0.2, 0.2, 0.6):
        for d_sig in (-0.3, 0.0, 0.4):
            if d_mu == 0.0 and d_sig == 0.0:
                continue
            perturbed = bhhj_expected_score_gaussian(mu0 + d_mu, sigma0 + d_sig)
            assert perturbed > opt_score + 1e-6, (
                f"Expected strict minimum at true (mu0, sigma0), got {perturbed} <= {opt_score}"
            )

    # Verify redescending location score psi_alpha(y; mu) = d/dmu S_alpha(y, N(mu, sigma^2))
    # = -((y - mu)/sigma^2) * q(y; mu, sigma)^alpha
    def location_score(y: float) -> float:
        q_y = (1.0 / math.sqrt(2.0 * math.pi * sigma0 * sigma0)) * math.exp(
            -((y - mu0) ** 2) / (2.0 * sigma0 * sigma0)
        )
        return -((y - mu0) / (sigma0 * sigma0)) * (q_y ** alpha)

    score_moderate = abs(location_score(mu0 + 1.5 * sigma0))
    score_extreme = abs(location_score(mu0 + 10.0 * sigma0))
    assert score_moderate > 0.05
    assert score_extreme < 1e-8, f"Expected redescending score at extreme outlier, got {score_extreme}"


def verify_reweighting_invariance_and_tilt_diagnostic() -> None:
    """Verify Lemma 4.1, Proposition 4.1, and the Gaussian reweighting diagnostic trace."""
    # Construct a discrete regressor distribution on a fine grid X in [-3, 3]
    grid = [-3.0 + 6.0 * i / 600.0 for i in range(601)]
    raw_px = [math.exp(-0.5 * x * x) for x in grid]
    sum_px = sum(raw_px)
    px = [p / sum_px for p in raw_px]

    # Case A: Well-specified conditional mean mu_well(x) = 1.5 + 2.0 * x
    # Case B: Misspecified conditional mean mu_mis(x) = 1.5 + 2.0 * x + 0.4 * (x^2 - 1)
    def solve_weighted_ols(mu_vals: list[float], weights: list[float]) -> tuple[float, float]:
        # Normalize weights so E_P[w(X)] = 1 (Lemma 4.1)
        mean_w = sum(p * w for p, w in zip(px, weights))
        pw = [p * (w / mean_w) for p, w in zip(px, weights)]
        assert abs(sum(pw) - 1.0) < 1e-12

        ex = sum(q * x for q, x in zip(pw, grid))
        ey = sum(q * m for q, m in zip(pw, mu_vals))
        exx = sum(q * (x - ex) ** 2 for q, x in zip(pw, grid))
        exy = sum(q * (x - ex) * (m - ey) for q, x, m in zip(pw, grid, mu_vals))
        b1 = exy / exx
        b0 = ey - b1 * ex
        return b0, b1

    mu_well = [1.5 + 2.0 * x for x in grid]
    mu_mis = [1.5 + 2.0 * x + 0.4 * (x * x - 1.0) for x in grid]

    # Interior deciles xi_(1) < ... < xi_(9) of Z = X
    xis = [-1.28, -0.84, -0.52, -0.25, 0.0, 0.25, 0.52, 0.84, 1.28]
    gamma_bw = 0.7

    well_slopes = []
    mis_slopes = []
    for xi in xis:
        w_xi = [math.exp(-((x - xi) ** 2) / (2.0 * gamma_bw * gamma_bw)) for x in grid]
        _, b1_well = solve_weighted_ols(mu_well, w_xi)
        _, b1_mis = solve_weighted_ols(mu_mis, w_xi)
        well_slopes.append(b1_well)
        mis_slopes.append(b1_mis)

    # Under well-specification, Proposition 4.1 guarantees invariance across all xi:
    max_dev_well = max(abs(s - 2.0) for s in well_slopes)
    tilt_well = well_slopes[-1] - well_slopes[0]
    assert max_dev_well < 1e-12, f"Expected zero deviation under well-specification, got {max_dev_well}"
    assert abs(tilt_well) < 1e-12

    # Under quadratic misspecification, slope increases strictly with xi and tilt d != 0:
    for k in range(len(mis_slopes) - 1):
        assert mis_slopes[k + 1] > mis_slopes[k] + 0.05
    tilt_mis = mis_slopes[-1] - mis_slopes[0]
    assert tilt_mis > 0.8, f"Expected large positive tilt statistic under quadratic nonlinearity, got {tilt_mis}"


def verify_canonical_eo_and_pythagorean_if_split() -> None:
    """Verify Propositions 6.4-6.6 and Corollary 7.1 (Pythagorean IF variance split)."""
    rng = random.Random(20261018)
    # Construct a finite population P of (X, Y) pairs to check exact population expectations
    # and a sample X_sample to verify the canonical EO split and noiseless Proposition 6.5.
    x_support = [-2.0, -1.0, 0.0, 1.0, 2.0]
    # True nonlinear conditional mean mu(x) = 0.5 * x + 0.3 * (x^3 - 3*x)
    # and heteroskedastic noise Y = mu(x) + eps with eps in {-sigma(x), +sigma(x)} equally likely
    pop_atoms = []  # (prob, x, y, mu_x)
    for x in x_support:
        mu_x = 0.5 * x + 0.3 * (x ** 3 - 3.0 * x)
        sig_x = 0.4 + 0.2 * abs(x)
        for sign in (-1.0, 1.0):
            pop_atoms.append((0.1, x, mu_x + sign * sig_x, mu_x))

    # Population OLS slope (centered x since E_P[X] = 0):
    ex2_pop = sum(prob * x * x for prob, x, _, _ in pop_atoms)
    exy_pop = sum(prob * x * y for prob, x, y, _ in pop_atoms)
    beta_pop = exy_pop / ex2_pop

    # Full influence function for slope through origin: IF(y, x) = x * (y - beta_pop * x) / E_P[X^2]
    # Partial influence function (Equation 11, Lemma 6.6): IF(x) = E_P[IF(Y, X) | X = x] = x * (mu(x) - beta_pop * x) / E_P[X^2]
    mean_if_full = sum(prob * (x * (y - beta_pop * x) / ex2_pop) for prob, x, y, _ in pop_atoms)
    mean_if_part = sum(prob * (x * (mu_x - beta_pop * x) / ex2_pop) for prob, x, _, mu_x in pop_atoms)
    assert abs(mean_if_full) < 1e-12
    assert abs(mean_if_part) < 1e-12

    # Check exact L^2(P) orthogonality between Noise IF = IF(Y, X) - IF(X) and Approximation IF = IF(X)
    cross_cov = 0.0
    var_total = 0.0
    var_noise = 0.0
    var_approx = 0.0
    for prob, x, y, mu_x in pop_atoms:
        if_full = x * (y - beta_pop * x) / ex2_pop
        if_part = x * (mu_x - beta_pop * x) / ex2_pop
        if_noise = if_full - if_part
        var_total += prob * (if_full ** 2)
        var_noise += prob * (if_noise ** 2)
        var_approx += prob * (if_part ** 2)
        cross_cov += prob * if_noise * if_part

    assert abs(cross_cov) < 1e-12, f"Expected orthogonal noise and approximation IFs, got {cross_cov}"
    assert abs(var_total - (var_noise + var_approx)) < 1e-12
    assert var_noise > 0.01 and var_approx > 0.01

    # Verify Canonical EO decomposition on a sample and Proposition 6.5 (noiseless case):
    sample_x = [rng.choice(x_support) for _ in range(40)]
    sample_mu = [0.5 * x + 0.3 * (x ** 3 - 3.0 * x) for x in sample_x]
    sample_y_noisy = [m + rng.gauss(0.0, 0.5) for m in sample_mu]

    denom_hat = sum(x * x for x in sample_x)
    # Conditional parameter beta(X) = beta(P_{Y|X} (x) P_hat_X) uses exact conditional mean mu(X_i)
    beta_cond_x = sum(x * m for x, m in zip(sample_x, sample_mu)) / denom_hat
    beta_hat_noisy = sum(x * y for x, y in zip(sample_x, sample_y_noisy)) / denom_hat
    beta_hat_noiseless = sum(x * m for x, m in zip(sample_x, sample_mu)) / denom_hat

    # Total EO = Noise EO + Approximation EO
    total_eo = beta_hat_noisy - beta_pop
    noise_eo = beta_hat_noisy - beta_cond_x
    approx_eo = beta_cond_x - beta_pop
    assert abs(total_eo - (noise_eo + approx_eo)) < 1e-12

    # In the noiseless deterministic case Y = mu(X), Noise EO = 0 identically while Approx EO != 0 (Prop 6.5)
    assert abs(beta_hat_noiseless - beta_cond_x) < 1e-12
    assert abs(approx_eo) > 1e-4


def verify_m_of_n_xy_bootstrap_sandwich_limit() -> None:
    """Verify Proposition 8.1 / Corollary 8.1: M^(1/2)(theta_M* - theta_hat_N) -> N(0, AV[P_hat_N])."""
    rng = random.Random(20261019)
    n_obs = 50
    xs = [-2.0 + 4.0 * i / (n_obs - 1) for i in range(n_obs)]
    ys = [0.8 * x + 0.25 * (x * x - 1.3) + rng.gauss(0.0, 0.4 + 0.15 * abs(x)) for x in xs]

    # Empirical estimator theta_hat_N on P_hat_N (slope through origin for simplicity)
    s_xx = sum(x * x for x in xs) / n_obs
    s_xy = sum(x * y for x, y in zip(xs, ys)) / n_obs
    theta_hat_n = s_xy / s_xx

    # Empirical influence function values on P_hat_N: if_hat_i = x_i * (y_i - theta_hat_n * x_i) / s_xx
    if_hat = [x * (y - theta_hat_n * x) / s_xx for x, y in zip(xs, ys)]
    assert abs(sum(if_hat) / n_obs) < 1e-12

    # Exact empirical sandwich functional AV[P_hat_N; theta(.)] = (1/N) sum_{i=1}^N if_hat_i^2
    av_p_hat_n = sum(v * v for v in if_hat) / n_obs

    # Run Monte Carlo M-of-N XY-bootstrap with large M = 800 for fixed P_hat_N
    m_boot = 800
    n_rep = 1200
    scaled_diffs = []
    for _ in range(n_rep):
        sum_xx_star = 0.0
        sum_xy_star = 0.0
        for _ in range(m_boot):
            idx = rng.randrange(n_obs)
            x_star = xs[idx]
            y_star = ys[idx]
            sum_xx_star += x_star * x_star
            sum_xy_star += x_star * y_star
        theta_m_star = sum_xy_star / sum_xx_star
        scaled_diffs.append(math.sqrt(m_boot) * (theta_m_star - theta_hat_n))

    boot_mean = sum(scaled_diffs) / n_rep
    boot_var = sum((d - boot_mean) ** 2 for d in scaled_diffs) / n_rep
    rel_err = abs(boot_var - av_p_hat_n) / av_p_hat_n
    assert abs(boot_mean) < 0.06, f"Expected near-zero M-of-N bootstrap mean, got {boot_mean}"
    assert rel_err < 0.08, (
        f"Expected M-of-N bootstrap variance {boot_var:.4f} to match AV[P_hat_N] = {av_p_hat_n:.4f} "
        f"(rel_err = {rel_err:.4f})"
    )


if __name__ == "__main__":
    verify_bhhj_proper_scoring_and_redescending_if()
    verify_reweighting_invariance_and_tilt_diagnostic()
    verify_canonical_eo_and_pythagorean_if_split()
    verify_m_of_n_xy_bootstrap_sandwich_limit()
    print("All model-free regression functionals & reweighting diagnostic boundary checks passed.")
