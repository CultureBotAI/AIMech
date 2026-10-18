#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for
AIMech:ContinuumMeasureSpaceStepUpFDRControl
(Blanchard, Delattre, & Roquain 2014, Bernoulli 20(1):304-333,
arXiv:1110.3599v3, DOI:10.3150/12-BEJ488).

Verifies:
1. Section 3.3 & Section 4.1 (Definition 3.2, Theorem 4.1, Lemma 4.3, and Section 5.1 Lemma 5.3):
   Continuum step-up rejection volume fixed-point identity Lambda(L_Delta(r_hat)) = r_hat
   on ([0, 1], B([0, 1]), Leb) and Glivenko-Cantelli discrete grid convergence
   |r_hat_n - r_hat| <= 1/n under empirical measure approximations Lambda_n.
2. Section 4.2.1 (Proposition 4.2, Corollary 4.4, and Remark 4.6):
   Exact closed-form Lebesgue measure formula
   gamma(u) = sum_{j=0}^m min(max(t_j(u) - X_{(j)}, 0), X_{(j+1)} - X_{(j)})
   for one-sided continuous c.d.f. testing H_{0,t}: F(t) <= t on (0, 1), where t_j(u) is
   the unique root of P(Binomial(m, t) >= j) = u, and exact continuum step-up fixed-point
   identity gamma(alpha * r_hat) = r_hat.
3. Section 4.2.2 (Proposition 4.3, Corollary 4.5, and Remark 4.6):
   Exact data-dependent interval-length weighted step-up reduction
   r_hat(X) = max{sum_{l=0}^k w_l : q_{sigma(k)}(X) <= alpha sum_{l=0}^k w_l}
   with w_l = X_{(sigma(l)+1)} - X_{(sigma(l))} and left-endpoint Poisson tail p-values
   q_j(X) = P(Poisson(lambda_0 X_{(j)}) >= j | X) for testing Poisson process intensity.
"""
from __future__ import annotations

import json
import math


def binom_tail(m: int, j: int, t: float) -> float:
    """Exact binomial upper tail P(Binomial(m, t) >= j)."""
    if j <= 0:
        return 1.0
    if j > m:
        return 0.0
    if t <= 0.0:
        return 0.0
    if t >= 1.0:
        return 1.0
    total = 0.0
    for i in range(j, m + 1):
        total += math.comb(m, i) * (t ** i) * ((1.0 - t) ** (m - i))
    return min(1.0, max(0.0, total))


def inv_binom_tail(m: int, j: int, u: float) -> float:
    """Unique root t_j(u) in [0, 1] of P(Binomial(m, t) >= j) = u via bisection."""
    if j == 0:
        return 0.0 if u < 1.0 else 1.0
    if u <= 0.0:
        return 0.0
    if u >= 1.0:
        return 1.0
    lo, hi = 0.0, 1.0
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if binom_tail(m, j, mid) < u:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def gamma_cdf_test(x_ord: list[float], u: float) -> float:
    """Remark 4.6 closed-form Lebesgue measure gamma(u) = Leb{t in (0,1) : p_t(X) <= u}.
    x_ord has length m + 2 with x_ord[0] = 0.0 and x_ord[m+1] = 1.0.
    """
    m = len(x_ord) - 2
    total = 0.0
    for j in range(0, m + 1):
        tj = inv_binom_tail(m, j, u)
        diff = max(0.0, tj - x_ord[j])
        interval_len = x_ord[j + 1] - x_ord[j]
        total += min(diff, interval_len)
    return total


def poisson_tail(lam: float, j: int) -> float:
    """Exact Poisson upper tail P(Poisson(lam) >= j) = 1 - sum_{i=0}^{j-1} e^{-lam} lam^i / i!."""
    if j <= 0:
        return 1.0
    if lam <= 0.0:
        return 0.0
    cdf_below = 0.0
    term = math.exp(-lam)
    for i in range(0, j):
        if i > 0:
            term *= lam / i
        cdf_below += term
    return max(0.0, min(1.0, 1.0 - cdf_below))


def verify_section_4_1_and_5_1_continuum_and_discretization() -> dict[str, object]:
    """Verify Definition 3.2, Theorem 4.1, and Section 5.1 Lemma 5.3 continuum fixed point
    and discrete grid approximation convergence.
    """
    alpha = 0.05
    # Continuous p-value profile p_h = alpha * (0.4*h + 1.2*h^2) on h in [0, 1]
    # Sublevel set L_Delta(r) = {h in [0, 1] : 0.4*h + 1.2*h^2 <= r}
    # Positive root of 1.2*h^2 + 0.4*h - r = 0 is (-0.4 + sqrt(0.16 + 4.8*r)) / 2.4
    def leb_l_delta(r: float) -> float:
        if r <= 0.0:
            return 0.0
        root = (-0.4 + math.sqrt(0.16 + 4.8 * r)) / 2.4
        return min(1.0, max(0.0, root))

    # Fixed point r_hat > 0 solving leb_l_delta(r_hat) = r_hat:
    # 0.4*r + 1.2*r^2 = r  =>  1.2*r = 0.6  =>  r_hat = 0.5
    r_hat_exact = 0.5
    assert abs(leb_l_delta(r_hat_exact) - r_hat_exact) < 1e-15

    # Discrete grid approximations Lambda_n = (1/n) sum_{i=1}^n delta_{i/n}
    grid_Sizes = [20, 50, 100, 500, 1000]
    discrete_r_hats: dict[str, float] = {}
    max_scaled_err = 0.0
    for n in grid_Sizes:
        r_hat_n = 0.0
        for k in range(n, 0, -1):
            r_cand = k / n
            count = sum(
                1 for i in range(1, n + 1)
                if (0.4 * (i / n) + 1.2 * ((i / n) ** 2)) <= r_cand + 1e-15
            )
            if count / n >= r_cand - 1e-15:
                r_hat_n = r_cand
                break
        discrete_r_hats[str(n)] = round(r_hat_n, 6)
        err = abs(r_hat_n - r_hat_exact)
        assert err <= (1.0 / n) + 1e-12
        max_scaled_err = max(max_scaled_err, n * err)

    return {
        "alpha": alpha,
        "continuum_r_hat_exact": r_hat_exact,
        "continuum_leb_L_Delta_at_r_hat": round(leb_l_delta(r_hat_exact), 8),
        "discrete_grid_r_hats": discrete_r_hats,
        "max_n_times_abs_error": round(max_scaled_err, 6),
    }


def verify_section_4_2_1_cdf_continuum_step_up() -> dict[str, object]:
    """Verify Section 4.2.1 Corollary 4.4 and Remark 4.6 exact Lebesgue step-up formula
    gamma(u) = sum_{j=0}^m (t_j(u) - X_{(j)})_+ ^ (X_{(j+1)} - X_{(j)}) for continuous c.d.f. testing.
    """
    alpha = 0.10
    # Sample of m = 8 observations concentrated near 0 (stochastically smaller than Uniform[0,1],
    # so F(t) > t on an interval)
    sample = [0.008, 0.015, 0.024, 0.035, 0.048, 0.062, 0.250, 0.600]
    m = len(sample)
    x_ord = [0.0] + sorted(sample) + [1.0]

    # Solve for the positive continuum step-up fixed point r_hat = max{r in [0,1] : gamma(alpha*r) >= r}
    # Since gamma(alpha*r) - r is continuous and crosses 0 from above:
    lo, hi = 0.20, 0.90
    assert gamma_cdf_test(x_ord, alpha * lo) > lo
    assert gamma_cdf_test(x_ord, alpha * hi) < hi
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if gamma_cdf_test(x_ord, alpha * mid) >= mid:
            lo = mid
        else:
            hi = mid
    r_hat = 0.5 * (lo + hi)
    gamma_at_r_hat = gamma_cdf_test(x_ord, alpha * r_hat)
    assert abs(gamma_at_r_hat - r_hat) < 1e-12

    # Compare Remark 4.6 closed-form gamma(alpha*r_hat) against high-resolution midpoint Riemann sum
    n_grid = 20000
    u_crit = alpha * r_hat
    riemann_count = 0
    for k in range(n_grid):
        t = (k + 0.5) / n_grid
        # empirical cdf m * F_hat_m(t)
        j_emp = sum(1 for x in sample if x <= t)
        p_t = binom_tail(m, j_emp, t)
        if p_t <= u_crit:
            riemann_count += 1
    riemann_leb = riemann_count / n_grid
    assert abs(riemann_leb - gamma_at_r_hat) < 1e-3

    return {
        "m": m,
        "alpha": alpha,
        "r_hat_continuum": round(r_hat, 6),
        "gamma_at_alpha_r_hat": round(gamma_at_r_hat, 6),
        "riemann_quadrature_leb": round(riemann_leb, 6),
        "fixed_point_abs_residual": round(abs(gamma_at_r_hat - r_hat), 15),
    }


def verify_section_4_2_2_poisson_process_weighted_step_up() -> dict[str, object]:
    """Verify Section 4.2.2 Corollary 4.5 and Remark 4.6 exact data-dependent interval-length
    weighted step-up reduction for testing the intensity of a Poisson process on [0, 1].
    """
    alpha = 0.05
    lambda_0 = 5.0
    # Arrival times of a Poisson process with elevated intensity on [0, 0.5] and lower thereafter
    arrivals = [0.02, 0.05, 0.09, 0.14, 0.18, 0.23, 0.29, 0.35, 0.42, 0.48, 0.72, 0.88]
    n_arr = len(arrivals)
    x_grid = [0.0] + arrivals + [1.0]

    # Left-endpoint p-values q_j(X) = P(Poisson(lambda_0 * X_{(j)}) >= j) for j = 0..N
    q_vals: list[float] = []
    weights: list[float] = []
    for j in range(0, n_arr + 1):
        qj = 1.0 if j == 0 else poisson_tail(lambda_0 * x_grid[j], j)
        wj = x_grid[j + 1] - x_grid[j]
        q_vals.append(qj)
        weights.append(wj)

    assert abs(sum(weights) - 1.0) < 1e-15

    # Order indices sigma(0), ..., sigma(N) so that q_{sigma(0)} <= ... <= q_{sigma(N)}
    sigma = sorted(range(n_arr + 1), key=lambda j: q_vals[j])

    # Remark 4.6 weighted step-up formula:
    # r_hat(X) = max{sum_{l=0}^k w_l : q_{sigma(k)}(X) <= alpha * sum_{l=0}^k w_l}
    cum_weights: list[float] = []
    running = 0.0
    for idx in sigma:
        running += weights[idx]
        cum_weights.append(running)

    r_hat_weighted = 0.0
    k_hat = -1
    for k in range(n_arr, -1, -1):
        if q_vals[sigma[k]] <= alpha * cum_weights[k] + 1e-15:
            r_hat_weighted = cum_weights[k]
            k_hat = k
            break

    assert k_hat >= 0 and r_hat_weighted > 0.5

    # Verify directly that under localized threshold Delta(t, r) = alpha * r * 1{forall s in [X_{(j)}, X_{(j+1)}), p_s(X) <= alpha*r},
    # since p_s(X) is non-decreasing on [X_{(j)}, X_{(j+1)}) with supremum p_{X_{(j+1)}^-}(X) = P(Poisson(lambda_0 X_{(j+1)}) >= j),
    # wait: Remark 4.6 notes that t -> p_t(X) is non-decreasing on [X_{(j)}, X_{(j+1)}) (since lambda_0 t increases while N_t = j is constant),
    # and the left-endpoint p-value q_j(X) = p_{X_{(j)}}(X) defines the interval-wise test with volume sum_{j: q_j(X) <= alpha*r} (X_{(j+1)} - X_{(j)}).
    vol_at_r_hat = sum(
        weights[j] for j in range(n_arr + 1) if q_vals[j] <= alpha * r_hat_weighted + 1e-15
    )
    assert abs(vol_at_r_hat - r_hat_weighted) < 1e-15

    # Verify no strictly larger r in (r_hat_weighted, 1] satisfies vol(r) >= r
    for k in range(k_hat + 1, n_arr + 1):
        r_test = cum_weights[k]
        assert q_vals[sigma[k]] > alpha * r_test

    return {
        "n_arrivals": n_arr,
        "lambda_0": lambda_0,
        "alpha": alpha,
        "k_hat_index": k_hat,
        "r_hat_weighted_step_up": round(r_hat_weighted, 6),
        "volume_fixed_point_check": round(vol_at_r_hat, 6),
        "smallest_q_val": round(q_vals[sigma[0]], 6),
        "critical_q_val_at_k_hat": round(q_vals[sigma[k_hat]], 6),
    }


def main() -> None:
    s41 = verify_section_4_1_and_5_1_continuum_and_discretization()
    s421 = verify_section_4_2_1_cdf_continuum_step_up()
    s422 = verify_section_4_2_2_poisson_process_weighted_step_up()

    summary = {
        "concept_id": "AIMech:ContinuumMeasureSpaceStepUpFDRControl",
        "primary_source": "Blanchard, Delattre, & Roquain (2014), Bernoulli 20(1):304-333 (arXiv:1110.3599v3, DOI:10.3150/12-BEJ488)",
        "section_4_1_and_5_1_continuum_and_discretization": s41,
        "section_4_2_1_cdf_continuum_step_up": s421,
        "section_4_2_2_poisson_process_weighted_step_up": s422,
        "all_assertions_passed": True,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
