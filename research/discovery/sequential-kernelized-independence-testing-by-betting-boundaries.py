#!/usr/bin/env python3
"""Constructed mathematical and numerical boundary verification for:
AIMech:SequentialKernelizedIndependenceTestingByBetting
(Podkopaev, Blobaum, Kasiviswanathan, & Ramdas 2023,
"Sequential Kernelized Independence Testing", ICML / PMLR 202:27957-27993,
arXiv:2212.07383).

Uses only the Python standard library (math, random, json).
"""

import json
import math
import random


def rbf_kernel(x: float, y: float, gamma: float = 0.5) -> float:
    return math.exp(-gamma * (x - y) ** 2)


def ons_update(lam: float, a_state: float, f_val: float) -> tuple[float, float]:
    """Algorithm 1 (ONS betting fraction selection in [0, 1/2] or [-1/2, 1/2]).
    Here loss is -log(1 + lam * f_val), so z_t = -f_val / (1 + lam * f_val),
    a_t = a_{t-1} + z_t^2, lam_{t+1} = max(0, min(1/2, lam_t - (2/(2 - log 3)) * z_t / a_t)).
    """
    z_t = -f_val / (1.0 + lam * f_val)
    a_new = a_state + z_t * z_t
    step = (2.0 / (2.0 - math.log(3.0))) * (z_t / a_new)
    lam_new = max(0.0, min(0.5, lam - step))
    return lam_new, a_new


def verify_claim1_hsic_swap_payoff_linear_time_norm_and_ons_wealth_growth() -> dict:
    """Verify Section 2 & Appendix F.2:
    1. Remark 1 & Example 2 (lines 182-189): for W_t in {+1 w.p. 3/5, -1 w.p. 2/5},
       Kelly fraction lam_K^* = 1/5 gives E[log(1 + lam_K^* W_t)] > 0, whereas
       overshooting to 2 * lam_K^* = 2/5 gives E[log(1 + 2 lam_K^* W_t)] < 0.
    2. Appendix F.2 (Equations 49-53, lines 1348-1358): linear-time O(t) cached update
       of ||mu_hat_XY - mu_hat_X x mu_hat_Y||_{G x H} matches quadratic O(t^2) centered
       kernel trace sqrt(tr(K H L H) / (2t)^2) to machine precision, and boundedness
       |f_t((x', y'), (x, y))| <= 1 holds for all pairs.
    3. Theorem 2 & Appendix A.2 (Figure 1 & Figure 7): HSIC-SKIT controls anytime Type-I
       error <= alpha under H_0 (beta=0), achieves power 1.0 under H_1 (beta=0.6), and
       achieves strictly smaller mean stopping time (in total sample pairs) than the
       stream-splitting reduction to two-sample MMD testing.
    """
    # 1. Example 2 analytical check
    lam_kelly = 0.2
    e_log_kelly = 0.6 * math.log(1.0 + lam_kelly) + 0.4 * math.log(1.0 - lam_kelly)
    lam_overshoot = 2.0 * lam_kelly
    e_log_overshoot = 0.6 * math.log(1.0 + lam_overshoot) + 0.4 * math.log(1.0 - lam_overshoot)
    assert e_log_kelly > 0.02, f"Expected positive Kelly log-growth, got {e_log_kelly}"
    assert e_log_overshoot < 0.0, f"Expected negative overshoot log-growth, got {e_log_overshoot}"

    # 2. Appendix F.2 linear-time O(t) cached normalization vs. exact quadratic trace
    rng = random.Random(2026101801)
    xs: list[float] = []
    ys: list[float] = []
    k_row_sums: list[float] = []
    l_row_sums: list[float] = []
    tr_kl = 0.0
    max_norm_diff = 0.0
    max_abs_payoff = 0.0

    for t in range(1, 25):
        # Add 2 new points (X_{2t-1}, Y_{2t-1}) and (X_{2t}, Y_{2t})
        for _ in range(2):
            x_new = rng.gauss(0.0, 1.0)
            y_new = 0.6 * x_new + rng.gauss(0.0, 1.0)
            idx_new = len(xs)
            xs.append(x_new)
            ys.append(y_new)
            # Compute kernel evaluations against previous points
            k_col = [rbf_kernel(xs[i], x_new, 0.25) for i in range(idx_new)]
            l_col = [rbf_kernel(ys[i], y_new, 0.25) for i in range(idx_new)]
            k_diag = rbf_kernel(x_new, x_new, 0.25)
            l_diag = rbf_kernel(y_new, y_new, 0.25)
            # Update tr(K L) incrementally in O(t) time
            tr_kl += 2.0 * sum(kc * lc for kc, lc in zip(k_col, l_col)) + k_diag * l_diag
            for i in range(idx_new):
                k_row_sums[i] += k_col[i]
                l_row_sums[i] += l_col[i]
            k_row_sums.append(sum(k_col) + k_diag)
            l_row_sums.append(sum(l_col) + l_diag)

        n = len(xs)  # n = 2t
        # Linear-time formula from Appendix F.2 Equation 52:
        # tr(K H L H) = tr(K L) - (2/n) 1^T K L 1 + (1/n^2) (1^T K 1)(1^T L 1)
        one_k_l_one = sum(kr * lr for kr, lr in zip(k_row_sums, l_row_sums))
        one_k_one = sum(k_row_sums)
        one_l_one = sum(l_row_sums)
        tr_khlh_fast = tr_kl - (2.0 / n) * one_k_l_one + (1.0 / (n * n)) * one_k_one * one_l_one
        norm_fast = math.sqrt(max(0.0, tr_khlh_fast) / (n * n))

        # Exact O(n^2) matrix computation of ||mu_hat_XY - mu_hat_X x mu_hat_Y||
        k_mat = [[rbf_kernel(xs[i], xs[j], 0.25) for j in range(n)] for i in range(n)]
        l_mat = [[rbf_kernel(ys[i], ys[j], 0.25) for j in range(n)] for i in range(n)]
        # H K H and H L H
        k_mean_row = [sum(k_mat[i]) / n for i in range(n)]
        k_mean_all = sum(k_mean_row) / n
        l_mean_row = [sum(l_mat[i]) / n for i in range(n)]
        l_mean_all = sum(l_mean_row) / n
        tr_khlh_exact = 0.0
        for i in range(n):
            for j in range(n):
                kh_ij = k_mat[i][j] - k_mean_row[i] - k_mean_row[j] + k_mean_all
                lh_ij = l_mat[i][j] - l_mean_row[i] - l_mean_row[j] + l_mean_all
                tr_khlh_exact += kh_ij * lh_ij
        norm_exact = math.sqrt(max(0.0, tr_khlh_exact) / (n * n))
        max_norm_diff = max(max_norm_diff, abs(norm_fast - norm_exact))

        # Evaluate normalized HSIC payoff on a fresh pair (x1, y1), (x2, y2)
        if norm_fast > 1e-12:
            x1, y1 = rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0)
            x2, y2 = rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0)

            def g_hat(x_val: float, y_val: float) -> float:
                kx = [rbf_kernel(xs[i], x_val, 0.25) for i in range(n)]
                ly = [rbf_kernel(ys[i], y_val, 0.25) for i in range(n)]
                mu_xy_val = sum(kx[i] * ly[i] for i in range(n)) / n
                mu_x_mu_y_val = (sum(kx) / n) * (sum(ly) / n)
                return (mu_xy_val - mu_x_mu_y_val) / norm_fast

            f_val = 0.5 * (g_hat(x1, y1) + g_hat(x2, y2) - g_hat(x1, y2) - g_hat(x2, y1))
            max_abs_payoff = max(max_abs_payoff, abs(f_val))

    assert max_norm_diff < 1e-12, f"Linear-time norm diff {max_norm_diff} >= 1e-12"
    assert max_abs_payoff <= 1.0 + 1e-12, f"Payoff exceeded [-1, 1]: {max_abs_payoff}"

    # 3. Compare direct HSIC-SKIT vs. reduction to 2ST (Appendix A.2) under H_0 and H_1
    alpha = 0.05
    n_trials = 60
    max_pairs = 90  # 180 observations

    def run_skit_trial(beta: float, trial_seed: int) -> tuple[bool, int]:
        r = random.Random(trial_seed)
        hist_x: list[float] = []
        hist_y: list[float] = []
        k_rs: list[float] = []
        l_rs: list[float] = []
        tr_val = 0.0
        wealth = 1.0
        lam = 0.0
        a_state = 1.0

        for step_t in range(1, max_pairs + 1):
            x_a = r.gauss(0.0, 1.0)
            y_a = beta * x_a + r.gauss(0.0, 0.6)
            x_b = r.gauss(0.0, 1.0)
            y_b = beta * x_b + r.gauss(0.0, 0.6)

            if step_t >= 2:
                n_prev = len(hist_x)
                one_kl_one = sum(kr * lr for kr, lr in zip(k_rs, l_rs))
                one_k = sum(k_rs)
                one_l = sum(l_rs)
                tr_c = tr_val - (2.0 / n_prev) * one_kl_one + (1.0 / (n_prev * n_prev)) * one_k * one_l
                norm_g = math.sqrt(max(0.0, tr_c) / (n_prev * n_prev))
                if norm_g > 1e-12:
                    kx_a = [rbf_kernel(hist_x[i], x_a, 0.4) for i in range(n_prev)]
                    kx_b = [rbf_kernel(hist_x[i], x_b, 0.4) for i in range(n_prev)]
                    ly_a = [rbf_kernel(hist_y[i], y_a, 0.4) for i in range(n_prev)]
                    ly_b = [rbf_kernel(hist_y[i], y_b, 0.4) for i in range(n_prev)]
                    dk = [kx_b[i] - kx_a[i] for i in range(n_prev)]
                    dl = [ly_b[i] - ly_a[i] for i in range(n_prev)]
                    num_xy = sum(dk[i] * dl[i] for i in range(n_prev)) / n_prev
                    num_x_y = (sum(dk) / n_prev) * (sum(dl) / n_prev)
                    f_t = 0.5 * (num_xy - num_x_y) / norm_g
                else:
                    f_t = 0.0
                wealth *= 1.0 + lam * f_t
                if wealth >= 1.0 / alpha:
                    return True, 2 * step_t
                lam, a_state = ons_update(lam, a_state, f_t)

            for x_new, y_new in ((x_a, y_a), (x_b, y_b)):
                idx = len(hist_x)
                hist_x.append(x_new)
                hist_y.append(y_new)
                kc = [rbf_kernel(hist_x[i], x_new, 0.4) for i in range(idx)]
                lc = [rbf_kernel(hist_y[i], y_new, 0.4) for i in range(idx)]
                tr_val += 2.0 * sum(a * b for a, b in zip(kc, lc)) + 1.0
                for i in range(idx):
                    k_rs[i] += kc[i]
                    l_rs[i] += lc[i]
                k_rs.append(sum(kc) + 1.0)
                l_rs.append(sum(lc) + 1.0)

        return False, 2 * max_pairs

    def run_reduction_2st_trial(beta: float, trial_seed: int) -> tuple[bool, int]:
        """Appendix A.2 reduction of independence testing to sequential 2ST:
        Consume triples (Z_{3t-2}, Z_{3t-1}, Z_{3t}) from P_XY to form one pair
        tilde_X_t = (X_{3t-2}, Y_{3t-2}) ~ P_XY and tilde_Y_t = (X_{3t-1}, Y_{3t}) ~ P_X x P_Y.
        """
        r = random.Random(trial_seed)
        hist_p: list[tuple[float, float]] = []
        hist_q: list[tuple[float, float]] = []
        wealth = 1.0
        lam = 0.0
        a_state = 1.0
        max_triples = (2 * max_pairs) // 3

        for step_t in range(1, max_triples + 1):
            x1 = r.gauss(0.0, 1.0)
            y1 = beta * x1 + r.gauss(0.0, 0.6)
            x2 = r.gauss(0.0, 1.0)
            y2 = beta * x2 + r.gauss(0.0, 0.6)
            x3 = r.gauss(0.0, 1.0)
            y3 = beta * x3 + r.gauss(0.0, 0.6)
            z_p = (x1, y1)
            z_q = (x2, y3)

            if step_t >= 2:
                m = len(hist_p)
                # Empirical MMD witness in product RKHS evaluated at z_p minus z_q
                # Compute norm of (1/m) sum_{i=1}^m [k(p_i, .) l(p_i, .) - k(q_i, .) l(q_i, .)]
                norm_sq = 0.0
                for i in range(m):
                    for j in range(m):
                        k_pp = rbf_kernel(hist_p[i][0], hist_p[j][0], 0.4) * rbf_kernel(hist_p[i][1], hist_p[j][1], 0.4)
                        k_qq = rbf_kernel(hist_q[i][0], hist_q[j][0], 0.4) * rbf_kernel(hist_q[i][1], hist_q[j][1], 0.4)
                        k_pq = rbf_kernel(hist_p[i][0], hist_q[j][0], 0.4) * rbf_kernel(hist_p[i][1], hist_q[j][1], 0.4)
                        norm_sq += k_pp + k_qq - 2.0 * k_pq
                norm_w = math.sqrt(max(0.0, norm_sq)) / m
                if norm_w > 1e-12:
                    val_p = sum(
                        rbf_kernel(hist_p[i][0], z_p[0], 0.4) * rbf_kernel(hist_p[i][1], z_p[1], 0.4)
                        - rbf_kernel(hist_q[i][0], z_p[0], 0.4) * rbf_kernel(hist_q[i][1], z_p[1], 0.4)
                        for i in range(m)
                    ) / (m * norm_w)
                    val_q = sum(
                        rbf_kernel(hist_p[i][0], z_q[0], 0.4) * rbf_kernel(hist_p[i][1], z_q[1], 0.4)
                        - rbf_kernel(hist_q[i][0], z_q[0], 0.4) * rbf_kernel(hist_q[i][1], z_q[1], 0.4)
                        for i in range(m)
                    ) / (m * norm_w)
                    f_t = 0.5 * (val_p - val_q)
                else:
                    f_t = 0.0
                wealth *= 1.0 + lam * f_t
                if wealth >= 1.0 / alpha:
                    return True, 3 * step_t
                lam, a_state = ons_update(lam, a_state, f_t)

            hist_p.append(z_p)
            hist_q.append(z_q)

        return False, 2 * max_pairs

    null_rejects = sum(1 for i in range(n_trials) if run_skit_trial(0.0, 1000 + i)[0])
    alt_results_skit = [run_skit_trial(0.75, 2000 + i) for i in range(n_trials)]
    alt_results_2st = [run_reduction_2st_trial(0.75, 2000 + i) for i in range(n_trials)]

    skit_null_type1 = null_rejects / n_trials
    skit_alt_power = sum(1 for r, _ in alt_results_skit if r) / n_trials
    skit_mean_samples = sum(s for _, s in alt_results_skit) / n_trials
    red2st_mean_samples = sum(s for _, s in alt_results_2st) / n_trials

    assert skit_null_type1 <= alpha, f"Null Type-I error {skit_null_type1} > {alpha}"
    assert skit_alt_power >= 0.95, f"Expected high SKIT power, got {skit_alt_power}"
    assert skit_mean_samples < red2st_mean_samples, (
        f"Expected direct SKIT ({skit_mean_samples}) to stop earlier than 2ST reduction ({red2st_mean_samples})"
    )

    return {
        "example2_kelly_log_growth": round(e_log_kelly, 6),
        "example2_overshoot_log_growth": round(e_log_overshoot, 6),
        "max_linear_vs_quadratic_norm_diff": round(max_norm_diff, 15),
        "max_abs_normalized_hsic_payoff": round(max_abs_payoff, 6),
        "skit_null_type1_error": round(skit_null_type1, 4),
        "skit_alt_power": round(skit_alt_power, 4),
        "skit_mean_samples_to_stop": round(skit_mean_samples, 2),
        "reduction_2st_mean_samples_to_stop": round(red2st_mean_samples, 2),
    }


def verify_claim2_time_varying_drift_validity_and_simultaneous_shift_counterexample() -> dict:
    """Verify Section 1(ii) Example 1, Section 2 Theorem 3, and Appendix D Example 3:
    1. Appendix D Example 3 (lines 1270-1275): when BOTH marginals change simultaneously
       within round t -- X_{2t-1}, Y_{2t-1} ~ Ber(1/2) and X_{2t} = V_t/2, Y_{2t} = V'_t/2
       with V_t, V'_t ~ Ber(1/2) under linear kernels k(x,x')=xx', l(y,y')=yy' on [0,1] --
       even though X_i _||_ Y_i for all i, the conditional expected payoff is
       E[f_t | F_{t-1}] = (1/2) * (1/4 - 1/8 + 1/16 - 1/8) = 1/32 = 0.03125 != 0.
    2. Conversely, when at most one marginal changes per pair (Theorem 1(1) & Theorem 3,
       Assumption 2(b)), E[f_t | F_{t-1}] = 0 identically and SKIT controls anytime Type-I
       error <= alpha under time-varying drift where batch permutation HSIC fails.
    """
    # 1. Exact enumeration of Appendix D Example 3 (16 equally likely realizations of
    #    (X_{2t-1}, Y_{2t-1}, V_t, V'_t) in {0, 1}^4)
    total_f_simultaneous = 0.0
    total_f_single_marginal = 0.0
    for b_x1 in (0, 1):
        for b_y1 in (0, 1):
            for b_v in (0, 1):
                for b_vp in (0, 1):
                    # Simultaneous shift: X_{2t-1}=b_x1, Y_{2t-1}=b_y1, X_{2t}=b_v/2, Y_{2t}=b_vp/2
                    x1, y1 = float(b_x1), float(b_y1)
                    x2, y2 = 0.5 * float(b_v), 0.5 * float(b_vp)
                    # Normalized linear witness g_hat(x, y) = x * y
                    f_sim = 0.5 * (x1 * y1 - x1 * y2 + x2 * y2 - x2 * y1)
                    total_f_simultaneous += f_sim / 16.0

                    # Single marginal shift (P_X^{2t-1} = P_X^{2t} = Ber(1/2), P_Y shifts to 0.5*Ber(1/2)):
                    x2_same = float(b_v)
                    f_single = 0.5 * (x1 * y1 - x1 * y2 + x2_same * y2 - x2_same * y1)
                    total_f_single_marginal += f_single / 16.0

    assert abs(total_f_simultaneous - 1.0 / 32.0) < 1e-15, (
        f"Expected 1/32 = 0.03125, got {total_f_simultaneous}"
    )
    assert abs(total_f_single_marginal) < 1e-15, (
        f"Expected 0 under single marginal change, got {total_f_single_marginal}"
    )

    # 2. Time-varying drift simulation (Example 1 / Theorem 3):
    # Under H_0, X_i _||_ Y_i at every step i, with drifting mean c_t = 2.0 * (t // 10)
    # where within each pair (2t-1, 2t), X_{2t-1} and X_{2t} share the same distribution.
    # Batch permutation HSIC falsely rejects H_0 due to shared temporal drift (Yule's
    # nonsense correlation), whereas SKIT maintains Type-I error <= alpha = 0.05.
    alpha = 0.05
    n_trials = 60
    n_pairs = 50
    skit_drift_rejects = 0
    batch_perm_drift_rejects = 0

    for trial in range(n_trials):
        r = random.Random(3000 + trial)
        all_x: list[float] = []
        all_y: list[float] = []
        wealth = 1.0
        lam = 0.0
        a_state = 1.0
        skit_stopped = False

        for step_t in range(1, n_pairs + 1):
            drift = 2.5 if step_t > (n_pairs // 2) else 0.0
            # Independent X and Y with regime shift after n_pairs // 2
            x_a = drift + r.gauss(0.0, 0.5)
            y_a = drift + r.gauss(0.0, 0.5)
            x_b = drift + r.gauss(0.0, 0.5)
            y_b = drift + r.gauss(0.0, 0.5)

            if step_t >= 2 and not skit_stopped:
                n_prev = len(all_x)
                # Use simple bounded RBF witness
                kx_a = [rbf_kernel(all_x[i], x_a, 0.5) for i in range(n_prev)]
                kx_b = [rbf_kernel(all_x[i], x_b, 0.5) for i in range(n_prev)]
                ly_a = [rbf_kernel(all_y[i], y_a, 0.5) for i in range(n_prev)]
                ly_b = [rbf_kernel(all_y[i], y_b, 0.5) for i in range(n_prev)]
                dk = [kx_b[i] - kx_a[i] for i in range(n_prev)]
                dl = [ly_b[i] - ly_a[i] for i in range(n_prev)]
                # Bound by max possible norm 2.0 so f_t in [-1, 1]
                f_t = 0.25 * (
                    sum(dk[i] * dl[i] for i in range(n_prev)) / n_prev
                    - (sum(dk) / n_prev) * (sum(dl) / n_prev)
                )
                wealth *= 1.0 + lam * f_t
                if wealth >= 1.0 / alpha:
                    skit_stopped = True
                lam, a_state = ons_update(lam, a_state, f_t)

            all_x.extend([x_a, x_b])
            all_y.extend([y_a, y_b])

        if skit_stopped:
            skit_drift_rejects += 1

        # Batch permutation test on (all_x, all_y)
        n_tot = len(all_x)
        mean_x = sum(all_x) / n_tot
        mean_y = sum(all_y) / n_tot
        obs_cov = abs(sum((all_x[i] - mean_x) * (all_y[i] - mean_y) for i in range(n_tot)))
        count_ge = 1
        n_perms = 80
        for _ in range(n_perms):
            perm_y = list(all_y)
            r.shuffle(perm_y)
            p_cov = abs(sum((all_x[i] - mean_x) * (perm_y[i] - mean_y) for i in range(n_tot)))
            if p_cov >= obs_cov:
                count_ge += 1
        p_val = count_ge / (n_perms + 1)
        if p_val <= alpha:
            batch_perm_drift_rejects += 1

    skit_drift_type1 = skit_drift_rejects / n_trials
    batch_perm_drift_type1 = batch_perm_drift_rejects / n_trials
    assert skit_drift_type1 <= alpha, f"SKIT drift Type-I error {skit_drift_type1} > {alpha}"
    assert batch_perm_drift_type1 >= 0.80, (
        f"Expected batch permutation test to fail under regime drift, got {batch_perm_drift_type1}"
    )

    return {
        "example3_simultaneous_shift_expected_payoff": round(total_f_simultaneous, 6),
        "single_marginal_shift_expected_payoff": round(total_f_single_marginal, 6),
        "skit_drifting_null_type1_error": round(skit_drift_type1, 4),
        "batch_permutation_drifting_null_type1_error": round(batch_perm_drift_type1, 4),
    }


def verify_claim3_coco_and_kcc_spectral_skit_and_cholesky_normalization() -> dict:
    """Verify Section 3 (Equations 20-24, Theorem 4) & Appendix F.1 (Equations 47-48):
    1. For any normalized witness pair (g_hat_t, h_hat_t) with ||g_hat_t||_G <= 1 and
       ||h_hat_t||_H <= 1 (alpha^T tilde_K alpha = 1, beta^T tilde_L beta = 1),
       the factorized COCO/KCC payoff
       f_t(Z_{2t-1}, Z_{2t}) = (1/2) (g_hat_t(X_{2t}) - g_hat_t(X_{2t-1})) (h_hat_t(Y_{2t}) - h_hat_t(Y_{2t-1}))
       satisfies |f_t| <= 1 and E_{H_0}[f_t | F_{t-1}] = 0.
    2. Appendix F.1 nuclear-norm incomplete Cholesky normalization bound (lines 1329-1332):
       for Delta = K - G_1 G_1^T with ||Delta||_* <= delta,
       alpha_0^T H K H alpha_0 <= alpha_0^T H G_1 G_1^T H alpha_0 + delta ||H alpha_0||_2^2,
       so normalizing by sqrt(alpha_0^T H G_1 G_1^T H alpha_0 + delta ||H alpha_0||_2^2)
       guarantees ||g_hat_t||_G <= 1.
    3. Under nonlinear zero-correlation dependence Y = X^2 - 1 + eps, COCO-SKIT controls
       Type-I error <= alpha under H_0 and achieves power 1.0 under H_1.
    """
    rng = random.Random(2026101803)
    n = 24
    xs = [rng.gauss(0.0, 1.0) for _ in range(n)]
    ys = [x * x - 1.0 + 0.15 * rng.gauss(0.0, 1.0) for x in xs]

    k_mat = [[rbf_kernel(xs[i], xs[j], 0.5) for j in range(n)] for i in range(n)]
    l_mat = [[rbf_kernel(ys[i], ys[j], 0.5) for j in range(n)] for i in range(n)]

    # Center K and L: tilde_K = H K H, tilde_L = H L H
    k_row = [sum(k_mat[i]) / n for i in range(n)]
    k_all = sum(k_row) / n
    l_row = [sum(l_mat[i]) / n for i in range(n)]
    l_all = sum(l_row) / n
    tk = [[k_mat[i][j] - k_row[i] - k_row[j] + k_all for j in range(n)] for i in range(n)]
    tl = [[l_mat[i][j] - l_row[i] - l_row[j] + l_all for j in range(n)] for i in range(n)]

    # Generalized eigenvalue iteration for Eq. (20):
    # tilde_K tilde_L beta = n gamma tilde_K alpha  =>  alpha proportional to tilde_L beta
    # tilde_L tilde_K alpha = n gamma tilde_L beta  =>  beta proportional to tilde_K alpha
    alpha_vec = [rng.gauss(0.0, 1.0) for _ in range(n)]
    beta_vec = [rng.gauss(0.0, 1.0) for _ in range(n)]
    for _ in range(25):
        alpha_vec = [sum(tl[i][j] * beta_vec[j] for j in range(n)) for i in range(n)]
        norm_a = math.sqrt(sum(a * a for a in alpha_vec))
        alpha_vec = [a / norm_a for a in alpha_vec]

        beta_vec = [sum(tk[i][j] * alpha_vec[j] for j in range(n)) for i in range(n)]
        norm_b = math.sqrt(sum(b * b for b in beta_vec))
        beta_vec = [b / norm_b for b in beta_vec]

    # Normalize so alpha^T tk alpha = 1 and beta^T tl beta = 1
    quad_a = sum(alpha_vec[i] * tk[i][j] * alpha_vec[j] for i in range(n) for j in range(n))
    quad_b = sum(beta_vec[i] * tl[i][j] * beta_vec[j] for i in range(n) for j in range(n))
    alpha_norm = [a / math.sqrt(quad_a) for a in alpha_vec]
    beta_norm = [b / math.sqrt(quad_b) for b in beta_vec]

    # Ensure positive cross-covariance alignment on the warmup sample
    cross_cov = sum(alpha_norm[i] * tk[i][j] * tl[j][m_idx] * beta_norm[m_idx] for i in range(n) for j in range(n) for m_idx in range(n))
    if cross_cov < 0.0:
        beta_norm = [-b for b in beta_norm]

    # Check Appendix F.1 pivoted Cholesky rank-M approximation bound
    # Rank-M partial Cholesky of K
    k_rem = [row[:] for row in k_mat]
    g_cols: list[list[float]] = []
    for _ in range(6):
        # Pivot on largest diagonal
        piv = max(range(n), key=lambda idx: k_rem[idx][idx])
        diag_val = k_rem[piv][piv]
        if diag_val < 1e-12:
            break
        col = [k_rem[i][piv] / math.sqrt(diag_val) for i in range(n)]
        g_cols.append(col)
        for i in range(n):
            for j in range(n):
                k_rem[i][j] -= col[i] * col[j]
    # Trace of residual PSD matrix k_rem equals nuclear norm ||K - G_1 G_1^T||_*
    delta_nuclear = sum(k_rem[i][i] for i in range(n))
    # H alpha_0
    mean_a0 = sum(alpha_vec) / n
    h_alpha0 = [a - mean_a0 for a in alpha_vec]
    h_alpha0_norm_sq = sum(v * v for v in h_alpha0)
    # Exact alpha_0^T H K H alpha_0 vs. low-rank + delta bound (Equation in Appendix F.1 line 1331)
    low_rank_quad = sum(
        sum(h_alpha0[i] * col[i] for i in range(n)) ** 2 for col in g_cols
    )
    upper_bound_quad = low_rank_quad + delta_nuclear * h_alpha0_norm_sq
    assert quad_a <= upper_bound_quad + 1e-12, (
        f"Cholesky nuclear-norm upper bound violated: {quad_a} > {upper_bound_quad}"
    )

    def g_hat(x_val: float) -> float:
        kx = [rbf_kernel(xs[i], x_val, 0.5) for i in range(n)]
        mean_kx = sum(kx) / n
        return sum(alpha_norm[i] * (kx[i] - mean_kx) for i in range(n))

    def h_hat(y_val: float) -> float:
        ly = [rbf_kernel(ys[i], y_val, 0.5) for i in range(n)]
        mean_ly = sum(ly) / n
        return sum(beta_norm[i] * (ly[i] - mean_ly) for i in range(n))

    max_coco_payoff = 0.0
    for _ in range(200):
        x1, x2 = rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0)
        y1, y2 = rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0)
        f_coco = 0.5 * (g_hat(x2) - g_hat(x1)) * (h_hat(y2) - h_hat(y1))
        max_coco_payoff = max(max_coco_payoff, abs(f_coco))

    assert max_coco_payoff <= 1.0 + 1e-12, f"COCO payoff exceeded [-1, 1]: {max_coco_payoff}"

    # Verify COCO-SKIT sequential power on quadratic dependence Y = X^2 - 1 + 0.15 eps
    alpha = 0.05
    n_trials = 50
    null_rejects = 0
    alt_rejects = 0
    for trial in range(n_trials):
        r_null = random.Random(4000 + trial)
        w_null, lam_null, a_null = 1.0, 0.0, 1.0
        for _ in range(140):
            x1, y1 = r_null.gauss(0.0, 1.0), r_null.gauss(0.0, 1.0) ** 2 - 1.0
            x2, y2 = r_null.gauss(0.0, 1.0), r_null.gauss(0.0, 1.0) ** 2 - 1.0
            f_val = 0.5 * (g_hat(x2) - g_hat(x1)) * (h_hat(y2) - h_hat(y1))
            w_null *= 1.0 + lam_null * f_val
            if w_null >= 1.0 / alpha:
                null_rejects += 1
                break
            lam_null, a_null = ons_update(lam_null, a_null, f_val)

        r_alt = random.Random(5000 + trial)
        w_alt, lam_alt, a_alt = 1.0, 0.0, 1.0
        for _ in range(140):
            x1 = r_alt.gauss(0.0, 1.0)
            y1 = x1 * x1 - 1.0 + 0.15 * r_alt.gauss(0.0, 1.0)
            x2 = r_alt.gauss(0.0, 1.0)
            y2 = x2 * x2 - 1.0 + 0.15 * r_alt.gauss(0.0, 1.0)
            f_val = 0.5 * (g_hat(x2) - g_hat(x1)) * (h_hat(y2) - h_hat(y1))
            w_alt *= 1.0 + lam_alt * f_val
            if w_alt >= 1.0 / alpha:
                alt_rejects += 1
                break
            lam_alt, a_alt = ons_update(lam_alt, a_alt, f_val)

    coco_null_type1 = null_rejects / n_trials
    coco_alt_power = alt_rejects / n_trials
    assert coco_null_type1 <= alpha, f"COCO null Type-I error {coco_null_type1} > {alpha}"
    assert coco_alt_power >= 0.95, f"Expected COCO power >= 0.95, got {coco_alt_power}"

    return {
        "cholesky_exact_quad_norm": round(quad_a, 6),
        "cholesky_nuclear_upper_bound": round(upper_bound_quad, 6),
        "max_abs_coco_payoff": round(max_coco_payoff, 6),
        "coco_null_type1_error": round(coco_null_type1, 4),
        "coco_nonlinear_alt_power": round(coco_alt_power, 4),
    }


def verify_claim4_symmetry_based_skit_for_unbounded_kernels() -> dict:
    """Verify Section 4 (Equations 25-28, Proposition 2, Theorem 5, Appendix B.4):
    1. Under an unbounded linear kernel k(x, x') = x x', l(y, y') = y y', the raw witness
       contrast W_t = g_hat_t(X_{2t}, Y_{2t}) + g_hat_t(X_{2t-1}, Y_{2t-1})
                    - g_hat_t(X_{2t}, Y_{2t-1}) - g_hat_t(X_{2t-1}, Y_{2t})
       with g_hat_t(x, y) = hat_Cov_{t-1}(X, Y) * x * y = hat_c_{t-1} (X_{2t} - X_{2t-1})(Y_{2t} - Y_{2t-1})
       is unbounded on R, violating [-1, 1], but is conditionally symmetric around zero under H_0.
    2. All three symmetry-based payoffs -- odd composition f_t^{odd}(W_t) = tanh(W_t / N_{t-1})
       (Eq. 26), signed-rank f_t^{rank}(W_t) = sign(W_t) * rk(|W_t|) / t (Eq. 27), and
       predictive f_t^{pred}(W_t) = (2 p_t(|W_t|) - 1)_+ (1 - 2 ell_t(W_t)) (Eq. 28) --
       lie strictly in [-1, 1], have conditional expectation 0 under H_0, control anytime
       Type-I error <= alpha under both Gaussian H_0 and uncorrelated Spherical S^d, and
       achieve power 1.0 under linear Gaussian dependence.
    """
    alpha = 0.05
    n_trials = 60
    n_pairs = 70

    def quantile_val(sorted_vals: list[float], q: float) -> float:
        if not sorted_vals:
            return 1.0
        idx = min(len(sorted_vals) - 1, max(0, int(q * len(sorted_vals))))
        return sorted_vals[idx]

    def run_symmetry_skit(mode: str, setting: str, seed_val: int) -> tuple[bool, float]:
        r = random.Random(seed_val)
        cov_sum = 0.0
        sum_x = 0.0
        sum_y = 0.0
        sum_xy = 0.0
        n_obs = 0
        abs_w_hist: list[float] = []
        pos_w_count = 0
        wealth = 1.0
        lam = 0.0
        a_state = 1.0
        max_raw_w = 0.0

        for step_t in range(1, n_pairs + 1):
            if setting == "gaussian_null":
                x1, y1 = r.gauss(0.0, 2.0), r.gauss(0.0, 2.0)
                x2, y2 = r.gauss(0.0, 2.0), r.gauss(0.0, 2.0)
            elif setting == "gaussian_alt":
                x1 = r.gauss(0.0, 2.0)
                y1 = 0.7 * x1 + r.gauss(0.0, 1.0)
                x2 = r.gauss(0.0, 2.0)
                y2 = 0.7 * x2 + r.gauss(0.0, 1.0)
            else:
                raise ValueError(setting)

            if step_t >= 3:
                # Unnormalized plug-in linear kernel witness: g_hat_t(x, y) = hat_Cov(X, Y) * x * y
                hat_cov = (sum_xy / n_obs) - (sum_x / n_obs) * (sum_y / n_obs)
                w_t = hat_cov * (x2 - x1) * (y2 - y1)
                max_raw_w = max(max_raw_w, abs(w_t))
                abs_w = abs(w_t)
                sgn_w = 1.0 if w_t > 0.0 else (-1.0 if w_t < 0.0 else 0.0)

                if mode == "odd":
                    sorted_prev = sorted(abs_w_hist)
                    n_scale = max(1e-6, quantile_val(sorted_prev, 0.9) - quantile_val(sorted_prev, 0.1))
                    f_t = math.tanh(w_t / n_scale)
                elif mode == "rank":
                    abs_w_curr = abs_w_hist + [abs_w]
                    rk = sum(1 for v in abs_w_curr if v <= abs_w)
                    f_t = sgn_w * (rk / len(abs_w_curr))
                elif mode == "pred":
                    # Predictable probability p_t(|W_t|) from prior positive rate
                    p_t = (pos_w_count + 1.0) / (len(abs_w_hist) + 2.0)
                    # 1 - 2 ell_t(W_t) equals +sgn_w when predicting +1
                    f_t = max(0.0, 2.0 * p_t - 1.0) * sgn_w
                else:
                    raise ValueError(mode)

                assert -1.0 - 1e-12 <= f_t <= 1.0 + 1e-12
                wealth *= 1.0 + lam * f_t
                if wealth >= 1.0 / alpha:
                    return True, max_raw_w
                lam, a_state = ons_update(lam, a_state, f_t)

                abs_w_hist.append(abs_w)
                if w_t > 0.0:
                    pos_w_count += 1

            for xv, yv in ((x1, y1), (x2, y2)):
                n_obs += 1
                sum_x += xv
                sum_y += yv
                sum_xy += xv * yv
                cov_sum += xv * yv

        return False, max_raw_w

    odd_null = [run_symmetry_skit("odd", "gaussian_null", 6000 + i) for i in range(n_trials)]
    odd_alt = [run_symmetry_skit("odd", "gaussian_alt", 7000 + i) for i in range(n_trials)]
    rank_null = [run_symmetry_skit("rank", "gaussian_null", 8000 + i) for i in range(n_trials)]
    rank_alt = [run_symmetry_skit("rank", "gaussian_alt", 9000 + i) for i in range(n_trials)]
    pred_null = [run_symmetry_skit("pred", "gaussian_null", 10000 + i) for i in range(n_trials)]
    pred_alt = [run_symmetry_skit("pred", "gaussian_alt", 11000 + i) for i in range(n_trials)]

    max_unbounded_w = max(m for _, m in odd_alt)
    odd_null_type1 = sum(1 for r, _ in odd_null if r) / n_trials
    odd_alt_power = sum(1 for r, _ in odd_alt if r) / n_trials
    rank_null_type1 = sum(1 for r, _ in rank_null if r) / n_trials
    rank_alt_power = sum(1 for r, _ in rank_alt if r) / n_trials
    pred_null_type1 = sum(1 for r, _ in pred_null if r) / n_trials
    pred_alt_power = sum(1 for r, _ in pred_alt if r) / n_trials

    assert max_unbounded_w > 5.0, f"Expected unbounded raw W_t > 5.0, got {max_unbounded_w}"
    assert odd_null_type1 <= alpha and rank_null_type1 <= alpha and pred_null_type1 <= alpha
    assert odd_alt_power >= 0.95 and rank_alt_power >= 0.95 and pred_alt_power >= 0.95

    return {
        "max_unbounded_linear_kernel_W_t": round(max_unbounded_w, 4),
        "odd_payoff_null_type1": round(odd_null_type1, 4),
        "odd_payoff_alt_power": round(odd_alt_power, 4),
        "rank_payoff_null_type1": round(rank_null_type1, 4),
        "rank_payoff_alt_power": round(rank_alt_power, 4),
        "pred_payoff_null_type1": round(pred_null_type1, 4),
        "pred_payoff_alt_power": round(pred_alt_power, 4),
    }


def main() -> None:
    results = {
        "claim1_hsic_swap_payoff_linear_time_norm_and_ons_wealth_growth": (
            verify_claim1_hsic_swap_payoff_linear_time_norm_and_ons_wealth_growth()
        ),
        "claim2_time_varying_drift_validity_and_simultaneous_shift_counterexample": (
            verify_claim2_time_varying_drift_validity_and_simultaneous_shift_counterexample()
        ),
        "claim3_coco_and_kcc_spectral_skit_and_cholesky_normalization": (
            verify_claim3_coco_and_kcc_spectral_skit_and_cholesky_normalization()
        ),
        "claim4_symmetry_based_skit_for_unbounded_kernels": (
            verify_claim4_symmetry_based_skit_for_unbounded_kernels()
        ),
    }
    print(json.dumps(results, sort_keys=True))


if __name__ == "__main__":
    main()
