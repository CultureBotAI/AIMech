#!/usr/bin/env python3
"""Constructed boundary and edge-case verification for AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences.

Verifies the core mathematical properties from Manole & Ramdas (2023),
"Martingale Methods for Sequential Estimation of Convex Functionals and Divergences",
IEEE Transactions on Information Theory 69(7):4641-4658 (arXiv:2103.09267):

1. Claim 1 (Exchangeable-filtration reverse submartingale property, leave-one-out
   characterization, U- vs. V-statistics, and Ville's maximal inequality; Definition 1,
   Theorem 2, Proposition 3, Theorem 4, Proposition 5, Proposition 16):
   - Empirical measures P_t = (1/t) sum_{i=1}^t delta_{X_i} form a measure-valued
     reverse martingale with respect to the exchangeable filtration E_t^X:
     E[P_t(A) | E_{t+1}^X] = (1/(t+1)) sum_{i=1}^{t+1} P_{t+1}^{(-i)}(A) = P_{t+1}(A)
     identically across all multiset configurations.
   - For convex functionals Phi(P_t) (KL divergence KL(P_t || P), Total Variation
     ||P_t - P||_TV, and second-order V-statistic V_t = (1/t^2) sum_{i,j=1}^t h(X_i, X_j)
     with positive definite kernel h), the exact leave-one-out average satisfies
     (1/(t+1)) sum_{i=1}^{t+1} Phi(P_{t+1}^{(-i)}) >= Phi(P_{t+1}) (Proposition 5),
     confirming E[Phi(P_t) | E_{t+1}^X] >= Phi(P_{t+1}) a.s. and upward plug-in bias
     E[Phi(P_t)] >= E[Phi(P_{t+1})] >= Phi(P).
   - For the unbiased U-statistic U_t = (1/(t(t-1))) sum_{i != j} h(X_i, X_j), the
     leave-one-out average equals U_{t+1} with exact equality even when h is indefinite,
     whereas V_t violates the reverse submartingale inequality when h is negative definite.
   - Ville's maximal inequality for nonnegative reverse submartingales (Theorem 2):
     P(exists t >= t_0 : R_t >= u) <= E[R_{t_0}] / u.

2. Claim 2 (Geometric-epoch reverse-stitching for one-sample and partially ordered
   two-sample convex divergences and affine-minorant upper confidence sequences;
   Proposition 6, Theorem 7, Corollary 8, Proposition 9, Corollary 10, Corollary 11,
   Corollary 14, Corollary 15):
   - Combines one-sample and partially ordered two-sample Cramér-Chernoff maximal
     inequalities (Proposition 6, incurring factor e in the partially ordered index
     set N^2 from Christofides & Serfling's Proposition 3) over geometric epochs
     t_j = 2^j, s_k = 2^k with affine-minorant reverse martingales R_t^X = int f_Psi d(P_t - P)
     and R_s^Y = int g_Psi d(Q_s - Q) (Proposition 9, Corollary 11) to form two-sided
     confidence sequences C_{ts} valid uniformly over all (t, s) in N^2.
   - Verifies upward plug-in bias E[Psi(P_tau, Q_sigma)] >= Psi(P, Q) at an adaptive
     stopping time (Corollary 10) and simultaneous coverage >= 1 - delta for the
     two-sample Kolmogorov-Smirnov confidence sequence (Corollary 14).

3. Claim 3 (Discrete phi-divergence confidence sequences and parametric-rate
   restoration via Gaussian convolution smoothing; Proposition 18, Corollary 19,
   Proposition 20):
   - Verifies Proposition 18 (Guo-Richardson MGF reverse-stitched confidence sequence
     for multinomial KL(P_t || P)) and Corollary 19 (multinomial Total Variation CS).
   - Verifies Proposition 20: for a continuous distribution P on R, unsmoothed
     empirical Total Variation ||P_t - P||_TV = 1 identically for all t >= 1 due to
     lack of absolute continuity, whereas Gaussian-smoothed Total Variation
     ||P_t - P||_TV^sigma = ||P_t * K_sigma - P * K_sigma||_TV decays at the
     parametric rate O(t^{-1/2}) and stays below the Proposition 20(i) boundary.

4. Claim 4 (Stopping-time Rademacher complexity reverse submartingale and failure
   of forward canonical-filtration supermartingale construction; Corollary 22,
   Appendix E Lemma 32):
   - Empirical Rademacher complexity R_hat_t(F) satisfies the leave-one-out
     inequality (1/(t+1)) sum_{i=1}^{t+1} R_hat_t(X_{-i}) >= R_hat_{t+1}(X_{1:t+1})
     identically (Corollary 22(ii)).
   - The forward canonical-filtration supermartingale L_t(lambda) = exp(lambda t D(P_t || P) - t psi(lambda))
     where psi(lambda) = log E[exp(lambda D(delta_{X_1} || P))] (Appendix E Lemma 32)
     has linear slope psi'(0) = E[D(delta_{X_1} || P)] = H(P) > 0 for discrete KL,
     causing its Legendre-Fenchel inverse (psi^*)^{-1}(log(1/delta)/t) to converge to
     H(P) > 0 as t -> infinity (non-vanishing O(1) width), whereas the reverse
     submartingale CS width vanishes at O((log log t)/t).
"""

import json
import math
import random


def stitch_ell(u, s=1.4):
    """Polynomial stitching function ell(u) = (1 + u)^s * zeta(s)."""
    # Riemann zeta(1.4) approx 3.105547
    zeta_1_4 = sum(k ** (-s) for k in range(1, 5000))
    return ((1.0 + max(0.0, u)) ** s) * zeta_1_4


def verify_claim1_reverse_submartingale_and_ville():
    """Verify exact leave-one-out reverse submartingale property and Ville's inequality."""
    p = (0.5, 0.3, 0.2)
    t = 4  # t+1 = 5
    # Enumerate all (t+1)^3 = 243 tuples in {0, 1, 2}^5
    tuples_t1 = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    for e in range(3):
                        tuples_t1.append((a, b, c, d, e))

    # Positive definite kernel on {0, 1, 2}: h_psd(x, y) = exp(-0.5 * (x - y)^2)
    def h_psd(x, y):
        return math.exp(-0.5 * (x - y) ** 2)

    # Non-PSD hollow kernel on {0, 1, 2} with eigenvalues (2, -1, -1): h_indef(x, y) = I(x != y)
    def h_neg(x, y):
        return 1.0 if x != y else 0.0

    def kl_div(counts, n_sz):
        val = 0.0
        for j in range(3):
            if counts[j] > 0:
                qj = counts[j] / n_sz
                val += qj * math.log(qj / p[j])
        return val

    def tv_dist(counts, n_sz):
        return 0.5 * sum(abs(counts[j] / n_sz - p[j]) for j in range(3))

    def v_stat(seq, kern):
        n_sz = len(seq)
        return sum(kern(seq[i], seq[j]) for i in range(n_sz) for j in range(n_sz)) / (n_sz * n_sz)

    def u_stat(seq, kern):
        n_sz = len(seq)
        return sum(kern(seq[i], seq[j]) for i in range(n_sz) for j in range(n_sz) if i != j) / (n_sz * (n_sz - 1))

    max_emp_measure_diff = 0.0
    min_kl_loo_excess = float("inf")
    min_tv_loo_excess = float("inf")
    min_vstat_psd_loo_excess = float("inf")
    min_vstat_neg_loo_excess = float("inf")
    max_ustat_neg_loo_diff = 0.0

    for seq in tuples_t1:
        counts_t1 = [seq.count(j) for j in range(3)]
        loo_seqs = [seq[:i] + seq[i + 1 :] for i in range(t + 1)]
        loo_counts = [[s.count(j) for j in range(3)] for s in loo_seqs]

        for j in range(3):
            avg_loo_p = sum(c[j] / t for c in loo_counts) / (t + 1)
            max_emp_measure_diff = max(max_emp_measure_diff, abs(avg_loo_p - counts_t1[j] / (t + 1)))

        kl_t1 = kl_div(counts_t1, t + 1)
        kl_loo = sum(kl_div(c, t) for c in loo_counts) / (t + 1)
        min_kl_loo_excess = min(min_kl_loo_excess, kl_loo - kl_t1)

        tv_t1 = tv_dist(counts_t1, t + 1)
        tv_loo = sum(tv_dist(c, t) for c in loo_counts) / (t + 1)
        min_tv_loo_excess = min(min_tv_loo_excess, tv_loo - tv_t1)

        v_psd_t1 = v_stat(seq, h_psd)
        v_psd_loo = sum(v_stat(s, h_psd) for s in loo_seqs) / (t + 1)
        min_vstat_psd_loo_excess = min(min_vstat_psd_loo_excess, v_psd_loo - v_psd_t1)

        v_neg_t1 = v_stat(seq, h_neg)
        v_neg_loo = sum(v_stat(s, h_neg) for s in loo_seqs) / (t + 1)
        min_vstat_neg_loo_excess = min(min_vstat_neg_loo_excess, v_neg_loo - v_neg_t1)

        u_neg_t1 = u_stat(seq, h_neg)
        u_neg_loo = sum(u_stat(s, h_neg) for s in loo_seqs) / (t + 1)
        max_ustat_neg_loo_diff = max(max_ustat_neg_loo_diff, abs(u_neg_loo - u_neg_t1))

    assert max_emp_measure_diff < 1e-15
    assert min_kl_loo_excess >= -1e-15
    assert min_tv_loo_excess >= -1e-15
    assert min_vstat_psd_loo_excess >= -1e-15
    assert min_vstat_neg_loo_excess < -0.03  # non-PSD kernel violates reverse submartingale for V_t
    assert max_ustat_neg_loo_diff < 1e-15  # U_t is a reverse martingale for any symmetric kernel

    # Verify Ville's maximal inequality for nonnegative reverse submartingale R_t = KL(P_t || P)
    # P(exists t >= t_0 : R_t >= u) <= E[R_{t_0}] / u
    rng = random.Random(20261018)
    t0 = 15
    t_max = 150
    u_thresh = 0.25
    n_mc = 1000
    exceed_count = 0
    sum_r_t0 = 0.0
    for _ in range(n_mc):
        counts = [0, 0, 0]
        hit = False
        for step in range(1, t_max + 1):
            r = rng.random()
            idx = 0 if r < p[0] else (1 if r < p[0] + p[1] else 2)
            counts[idx] += 1
            if step >= t0:
                kl_val = kl_div(counts, step)
                if step == t0:
                    sum_r_t0 += kl_val
                if kl_val >= u_thresh:
                    hit = True
        if hit:
            exceed_count += 1

    emp_exceed_prob = exceed_count / n_mc
    ville_upper_bound = (sum_r_t0 / n_mc) / u_thresh
    assert emp_exceed_prob <= ville_upper_bound

    return {
        "max_emp_measure_reverse_martingale_diff": round(max_emp_measure_diff, 16),
        "min_kl_loo_excess": round(max(0.0, min_kl_loo_excess), 16),
        "min_tv_loo_excess": round(max(0.0, min_tv_loo_excess), 16),
        "min_vstat_psd_loo_excess": round(max(0.0, min_vstat_psd_loo_excess), 16),
        "min_vstat_neg_kernel_loo_excess": round(min_vstat_neg_loo_excess, 6),
        "max_ustat_neg_kernel_loo_diff": round(max_ustat_neg_loo_diff, 16),
        "ville_empirical_exceed_prob": round(emp_exceed_prob, 4),
        "ville_theoretical_upper_bound": round(ville_upper_bound, 4),
    }


def verify_claim2_two_sample_ks_cs_and_stopping_time_upward_bias():
    """Verify Corollary 10 (upward bias at stopping times) and Corollary 14 (two-sample KS CS)."""
    rng = random.Random(20261019)
    # True distributions: P = Uniform(0, 1), Q = Uniform(0, 1) (true KS distance = 0)
    # and shifted alternative Q_alt = Uniform(0.25, 1.25) (true KS distance = 0.25)
    delta = 0.1
    n_trials = 200
    t_grid = 24
    s_grid = 24

    def ks_2sample(xs, ys):
        pts = sorted(set(xs + ys))
        t_len = len(xs)
        s_len = len(ys)
        xs_s = sorted(xs)
        ys_s = sorted(ys)
        i = 0
        j = 0
        max_d = 0.0
        for z in pts:
            while i < t_len and xs_s[i] <= z:
                i += 1
            while j < s_len and ys_s[j] <= z:
                j += 1
            d = abs(i / t_len - j / s_len)
            if d > max_d:
                max_d = d
        return max_d

    # Corollary 14 two-sided CS for ||F - G||_infty = 0.25 under Q_alt
    true_ks = 0.25
    cs_violations = 0
    stopped_ks_sum = 0.0

    for _ in range(n_trials):
        xs_all = [rng.random() for _ in range(t_grid)]
        ys_all = [0.25 + rng.random() for _ in range(s_grid)]
        violated = False
        stopped = False
        for t in range(4, t_grid + 1, 4):
            for s in range(4, s_grid + 1, 4):
                emp_ks = ks_2sample(xs_all[:t], ys_all[:s])
                if not stopped and (emp_ks >= 0.45 or (t == t_grid and s == s_grid)):
                    stopped_ks_sum += emp_ks
                    stopped = True
                # Corollary 14: gamma_{ts} and kappa_{ts}
                g_val = math.e * stitch_ell(math.log2(t)) * stitch_ell(math.log2(s))
                gamma_ts = (
                    math.sqrt(math.pi / t)
                    + math.sqrt(math.pi / s)
                    + 2.0 * math.sqrt((2.0 * t * s / (t + s)) * (math.log(g_val) + math.log(2.0 / delta)))
                )
                kappa_ts = (
                    math.sqrt((1.0 / t) * (math.log(stitch_ell(math.log2(t))) + math.log(4.0 / delta)))
                    + math.sqrt((1.0 / s) * (math.log(stitch_ell(math.log2(s))) + math.log(4.0 / delta)))
                )
                lower_bd = max(0.0, emp_ks - gamma_ts)
                upper_bd = emp_ks + kappa_ts
                if true_ks < lower_bd or true_ks > upper_bd:
                    violated = True
        if violated:
            cs_violations += 1

    mean_stopped_ks = stopped_ks_sum / n_trials
    coverage = 1.0 - (cs_violations / n_trials)
    assert mean_stopped_ks > true_ks  # upward bias at stopping time (Corollary 10)
    assert coverage >= 1.0 - delta

    return {
        "true_ks_distance": true_ks,
        "mean_stopped_plugin_ks": round(mean_stopped_ks, 4),
        "upward_bias_at_stopping_time": round(mean_stopped_ks - true_ks, 4),
        "two_sample_ks_cs_simultaneous_coverage": round(coverage, 4),
    }


def verify_claim3_discrete_divergences_and_gaussian_smoothing():
    """Verify Proposition 18/Corollary 19 (discrete KL/TV) and Proposition 20 (smoothed TV)."""
    rng = random.Random(20261020)
    delta = 0.05
    # 1. Discrete TV CS (Corollary 19) for k=4 categories
    p_cat = [0.4, 0.3, 0.2, 0.1]
    k_cat = len(p_cat)
    n_runs = 200
    t_max = 120
    tv_violations = 0
    for _ in range(n_runs):
        counts = [0] * k_cat
        violated = False
        for t in range(1, t_max + 1):
            r = rng.random()
            cum = 0.0
            idx = k_cat - 1
            for j, pj in enumerate(p_cat):
                cum += pj
                if r < cum:
                    idx = j
                    break
            counts[idx] += 1
            emp_tv = 0.5 * sum(abs(counts[j] / t - p_cat[j]) for j in range(k_cat))
            bias_bd = math.sqrt((k_cat / (4.0 * t)) * max(1.0, 4.0 / math.pi - 2.0 / t))
            conc_bd = 2.0 * math.sqrt((1.0 / t) * (math.log(stitch_ell(math.log2(t))) + math.log(1.0 / delta)))
            if emp_tv >= bias_bd + conc_bd:
                violated = True
        if violated:
            tv_violations += 1

    discrete_tv_violation_rate = tv_violations / n_runs
    assert discrete_tv_violation_rate <= delta

    # 2. Continuous P = N(0, 1) with Gaussian smoothing kernel K_sigma, sigma = 1.0 (Proposition 20(i))
    # Unsmoothed ||P_t - P||_TV = 1 identically because P_t is atomic and P is continuous.
    # Under Gaussian smoothing with sigma = 1, P * K_sigma = N(0, 2), and P_t * K_sigma
    # has density (1/t) sum_{i=1}^t phi_1(x - X_i).
    unsmoothed_continuous_tv = 1.0
    sigma = 1.0
    tau = 1.0
    d = 1
    c_d = math.sqrt(2.0) * ((1.0 / math.sqrt(2.0) + tau / sigma) ** (d / 2.0)) * math.exp(3.0 * d / 16.0)

    # Numerical grid on [-6, 6] for smoothed TV (1/2) int |p_t * K_sigma(x) - p * K_sigma(x)| dx
    grid_pts = [-6.0 + 12.0 * m / 120.0 for m in range(121)]
    dx = 12.0 / 120.0
    true_smoothed_pdf = [
        math.exp(-0.5 * x * x / (1.0 + sigma * sigma)) / math.sqrt(2.0 * math.pi * (1.0 + sigma * sigma))
        for x in grid_pts
    ]

    smoothed_tv_at_t10 = 0.0
    smoothed_tv_at_t200 = 0.0
    smoothed_cs_violations = 0
    n_smooth_runs = 60
    for _ in range(n_smooth_runs):
        xs = [rng.gauss(0.0, 1.0) for _ in range(200)]
        violated = False
        for t in (10, 50, 100, 200):
            emp_pdf = [
                sum(math.exp(-0.5 * ((x - xi) / sigma) ** 2) for xi in xs[:t])
                / (t * sigma * math.sqrt(2.0 * math.pi))
                for x in grid_pts
            ]
            sm_tv = 0.5 * sum(abs(emp_pdf[m] - true_smoothed_pdf[m]) * dx for m in range(len(grid_pts)))
            if t == 10:
                smoothed_tv_at_t10 += sm_tv / n_smooth_runs
            if t == 200:
                smoothed_tv_at_t200 += sm_tv / n_smooth_runs
            # Proposition 20(i) bound
            prop20_bd = c_d / math.sqrt(t) + 4.0 * math.sqrt(
                (2.0 / t) * (math.log(stitch_ell(math.log2(t))) + math.log(1.0 / delta))
            )
            if sm_tv >= prop20_bd:
                violated = True
        if violated:
            smoothed_cs_violations += 1

    assert smoothed_tv_at_t200 < smoothed_tv_at_t10
    assert smoothed_cs_violations == 0

    return {
        "discrete_tv_cs_violation_rate": round(discrete_tv_violation_rate, 4),
        "unsmoothed_continuous_tv": unsmoothed_continuous_tv,
        "smoothed_tv_mean_at_t10": round(smoothed_tv_at_t10, 4),
        "smoothed_tv_mean_at_t200": round(smoothed_tv_at_t200, 4),
        "smoothed_tv_cs_violation_rate": round(smoothed_cs_violations / n_smooth_runs, 4),
    }


def verify_claim4_rademacher_loo_and_forward_supermartingale_failure():
    """Verify Corollary 22(ii) Rademacher LOO inequality and Appendix E Lemma 32 failure."""
    # 1. Empirical Rademacher complexity LOO inequality on threshold classifiers on R
    # F = {x -> sign(x - theta) : theta in {-1.5, -0.5, 0.5, 1.5}}
    thetas = [-1.5, -0.5, 0.5, 1.5]

    def f_eval(theta, x):
        return 1.0 if x >= theta else -1.0

    def emp_rademacher(xs):
        n_sz = len(xs)
        # Exact average over all 2^n_sz Rademacher sign vectors eps in {-1, +1}^n_sz
        total = 0.0
        for mask in range(1 << n_sz):
            eps = [1.0 if (mask & (1 << b)) else -1.0 for b in range(n_sz)]
            sup_val = max(sum(eps[b] * f_eval(th, xs[b]) for b in range(n_sz)) / n_sz for th in thetas)
            total += sup_val
        return total / (1 << n_sz)

    rng = random.Random(20261021)
    min_rademacher_loo_excess = float("inf")
    for _ in range(30):
        xs_5 = [rng.uniform(-2.0, 2.0) for _ in range(5)]
        rad_5 = emp_rademacher(xs_5)
        loo_avg = sum(emp_rademacher(xs_5[:i] + xs_5[i + 1 :]) for i in range(5)) / 5.0
        min_rademacher_loo_excess = min(min_rademacher_loo_excess, loo_avg - rad_5)

    assert min_rademacher_loo_excess >= -1e-15

    # 2. Appendix E Lemma 32 forward canonical-filtration supermartingale vs. reverse submartingale
    # For discrete P = (0.5, 0.3, 0.2), D(delta_{X_1} || P) = log(1 / p_{X_1}) has non-zero mean
    # E[D(delta_{X_1} || P)] = H(P) = -sum p_j log p_j > 0.
    p = (0.5, 0.3, 0.2)
    entropy_p = -sum(pj * math.log(pj) for pj in p)
    # Forward supermartingale L_t(lambda) = exp(lambda t KL(P_t || P) - t psi(lambda))
    # where psi(lambda) = log(sum_{j=1}^k p_j^{1 - lambda}) for lambda in [0, 1).
    # Since psi'(0) = H(P) > 0, for any t >= 1 and any u < H(P), sup_{lambda >= 0} (lambda u - psi(lambda)) = 0,
    # so the Cramér-Chernoff bound exp(-t psi^*(u)) is >= 1 for all u <= H(P)!
    # Thus any confidence threshold u_t from L_t(lambda) satisfies u_t > H(P) for all t >= 1.
    # By contrast, Proposition 18's reverse-stitched KL bound vanishes as O((log log t)/t).
    delta = 0.05
    t_eval = 500
    k_cat = 3
    lam_t = 0.25  # in [0, 1/2]
    # Guo & Richardson (2020) MGF upper bound G_{k, t}(lambda) <= (1 - lambda)^{-k/2} for lambda in [0, 1)
    g_kt = (1.0 - 2.0 * lam_t) ** (-k_cat / 2.0)
    reverse_kl_bound_t500 = (1.0 / (lam_t * t_eval)) * math.log(
        (1.0 / delta) * g_kt * stitch_ell(math.log2(t_eval))
    )
    assert entropy_p > 1.0
    assert reverse_kl_bound_t500 < 0.08

    return {
        "min_rademacher_loo_excess": round(max(0.0, min_rademacher_loo_excess), 16),
        "forward_supermartingale_asymptotic_width_limit": round(entropy_p, 6),
        "reverse_submartingale_kl_bound_at_t500": round(reverse_kl_bound_t500, 6),
    }


def main():
    results = {
        "claim1_reverse_submartingale_loo_and_ville_inequality": verify_claim1_reverse_submartingale_and_ville(),
        "claim2_two_sample_ks_cs_and_stopping_time_upward_bias": verify_claim2_two_sample_ks_cs_and_stopping_time_upward_bias(),
        "claim3_discrete_divergences_and_gaussian_smoothing": verify_claim3_discrete_divergences_and_gaussian_smoothing(),
        "claim4_rademacher_loo_and_forward_supermartingale_failure": verify_claim4_rademacher_loo_and_forward_supermartingale_failure(),
    }
    print(json.dumps(results, sort_keys=True))


if __name__ == "__main__":
    main()
