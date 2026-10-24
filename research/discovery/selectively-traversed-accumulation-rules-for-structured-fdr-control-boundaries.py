#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 192:
AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl
(Lei, Ramdas, & Fithian 2021, Biometrika 108(2):253-267, arXiv:1710.02776v2).
"""
from __future__ import annotations

import json
import math
import random


def norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def verify_claim1_accumulation_masking_and_prop21() -> dict[str, float]:
    """Verify Theorem 2.5 H(s(p)) = H(p), E_U[h(p)|g(p)] = 1, and Proposition 2.1 E_{P0}[h(p)|g(p)] >= 1."""
    # 1. SeqStep with p_* = 0.7: h(p) = (1/(1-p_*)) * 1{p > p_*}
    p_star = 0.7
    # H(x) = int_0^x (h(p) - 1) dp
    # On [0, p_*]: H(x) = -x
    # On [p_*, 1]: H(x) = -p_* + (x - p_*) * (p_* / (1 - p_*)) = (p_* / (1 - p_*)) * (x - 1)
    # By Theorem 2.5 / Section B.3: for p in [p_*, 1], s(p) = (p_* / (1 - p_*)) * (1 - p) in [0, p_*]
    q_grid = [0.05 * k for k in range(1, 13)]  # in (0, 0.7)
    max_H_err = 0.0
    max_cond_exp_unif_err = 0.0
    min_cond_exp_beta21 = 10.0

    for q in q_grid:
        # Preimages of g(p) = min(p, s(p)) = q are p1 = q < p_* and p2 = s^{-1}(q) = 1 - ((1 - p_*) / p_*) * q > p_*
        p1 = q
        p2 = 1.0 - ((1.0 - p_star) / p_star) * q
        H_p1 = -p1
        H_p2 = -p_star + (p2 - p_star) * (p_star / (1.0 - p_star))
        max_H_err = max(max_H_err, abs(H_p1 - H_p2))

        # Jacobian |(s^{-1})'(q)| = (1 - p_*) / p_*
        jac = (1.0 - p_star) / p_star
        h_p1 = 0.0
        h_p2 = 1.0 / (1.0 - p_star)
        cond_exp_unif = (h_p1 * 1.0 + h_p2 * jac) / (1.0 + jac)
        max_cond_exp_unif_err = max(max_cond_exp_unif_err, abs(cond_exp_unif - 1.0))

        # Under strictly increasing null density f_0(p) = 2p (Beta(2, 1), Proposition 2.1):
        w1 = 2.0 * p1
        w2 = 2.0 * p2 * jac
        cond_exp_beta21 = (h_p1 * w1 + h_p2 * w2) / (w1 + w2)
        min_cond_exp_beta21 = min(min_cond_exp_beta21, cond_exp_beta21)

    # 2. Truncated ForwardStop (Section B.3): h_raw(p) = min(-log(1-p), C), C = -log(0.01)
    C = -math.log(0.01)
    norm_const = 1.0 - math.exp(-C)  # 0.99

    def H_fs(p: float) -> float:
        # int_0^p (h_raw(u)/norm_const - 1) du
        thresh = 1.0 - math.exp(-C)
        if p <= thresh:
            integral_raw = p + (1.0 - p) * math.log(1.0 - p)
        else:
            integral_raw = thresh + (1.0 - thresh) * (-C) + C * (p - thresh)
        return integral_raw / norm_const - p

    # Solve H_fs(s(p)) = H_fs(p) via binary search for p in (p_fs_star, 1)
    # where h(p_fs_star) = 1 => -log(1 - p_fs_star) = norm_const
    p_fs_star = 1.0 - math.exp(-norm_const)
    fs_H_err = 0.0
    for p_upper in [0.70, 0.80, 0.90, 0.95]:
        target_H = H_fs(p_upper)
        lo, hi = 0.0, p_fs_star
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            if H_fs(mid) < target_H:
                hi = mid
            else:
                lo = mid
        s_p = 0.5 * (lo + hi)
        fs_H_err = max(fs_H_err, abs(H_fs(s_p) - target_H))

    assert max_H_err < 1e-12
    assert max_cond_exp_unif_err < 1e-12
    assert min_cond_exp_beta21 > 1.10  # strictly >= 1 as guaranteed by Proposition 2.1
    assert fs_H_err < 1e-12

    return {
        "seqstep_max_H_symmetry_err": round(max_H_err, 12),
        "seqstep_max_unif_cond_exp_err": round(max_cond_exp_unif_err, 12),
        "seqstep_min_beta21_cond_exp": round(min_cond_exp_beta21, 6),
        "forwardstop_max_H_inversion_err": round(fs_H_err, 12),
    }


def verify_claim2_tree_heredity_fdr_and_bottom_up_power() -> dict[str, float]:
    """Verify Theorem 2.3 finite-sample FDR control and 100% rooted-subtree heredity validity vs BH and top-down."""
    rng = random.Random(20261018)
    # Construct a balanced binary tree with 63 nodes (depth 6: nodes 0..62, parent of i is (i-1)//2)
    n = 63
    parents = [-1] + [(i - 1) // 2 for i in range(1, n)]
    children = [[] for _ in range(n)]
    for i in range(1, n):
        children[parents[i]].append(i)

    # True non-nulls form a rooted subtree of size 25 where top nodes have weak signal (mu=1.3)
    # and deeper nodes in the subtree have strong signal (mu=3.0) (Case 3, Appendix D.3).
    non_null_subtree = list(range(25))  # 0..24 is a valid rooted subtree in heap indexing
    non_null_set = set(non_null_subtree)
    alpha = 0.20
    trials = 40

    fdr_star_sum = 0.0
    power_star_sum = 0.0
    star_subtree_valid_count = 0
    bh_subtree_valid_count = 0
    power_topdown_sum = 0.0

    for _ in range(trials):
        p_vals = []
        for i in range(n):
            z = rng.gauss(0.0, 1.0)
            if i in non_null_set:
                mu = 1.3 if i < 7 else 3.0
                p = 1.0 - norm_cdf(z + mu)
            else:
                # Mix of Uniform(0,1) and conservative Beta(2,1) null p-values (Assumption 2)
                u = rng.random()
                p = math.sqrt(u) if (i % 2 == 1) else u
            p_vals.append(min(max(p, 1e-12), 1.0 - 1e-12))

        # Canonical score g(p_i) = min(p_i, 1 - p_i), accumulation h(p_i) = 2 * 1{p_i >= 0.5}
        g_vals = [min(p, 1.0 - p) for p in p_vals]
        h_vals = [2.0 if p >= 0.5 else 0.0 for p in p_vals]

        # Run STAR bottom-up leaf peeling (Algorithm 2.1 + Section D.2)
        R = set(range(n))
        while R:
            fdp_hat = (2.0 + sum(h_vals[i] for i in R)) / (1.0 + len(R))
            if fdp_hat <= alpha:
                break
            # Find leaves of current subtree R
            leaves = [i for i in R if not any(c in R for c in children[i])]
            # Peel leaf with largest canonical score g(p_i) (least favorable)
            worst_leaf = max(leaves, key=lambda idx: g_vals[idx])
            R.remove(worst_leaf)

        # Check rooted subtree constraint: every i in R (except 0) has parent in R
        is_subtree = all((parents[i] in R) for i in R if i != 0)
        if is_subtree:
            star_subtree_valid_count += 1

        v_star = sum(1 for i in R if i not in non_null_set)
        s_star = sum(1 for i in R if i in non_null_set)
        fdr_star_sum += v_star / max(1, len(R))
        power_star_sum += s_star / len(non_null_set)

        # Standard BH at level alpha (ignores tree structure)
        sorted_idx = sorted(range(n), key=lambda idx: p_vals[idx])
        k_bh = 0
        for rank, idx in enumerate(sorted_idx, start=1):
            if p_vals[idx] <= alpha * rank / n:
                k_bh = rank
        R_bh = set(sorted_idx[:k_bh])
        bh_is_subtree = all((parents[i] in R_bh) for i in R_bh if i != 0)
        if bh_is_subtree:
            bh_subtree_valid_count += 1

        # Top-down hierarchical testing (only tests children of rejected parents at level alpha/2)
        R_td = set()
        if p_vals[0] <= alpha:
            R_td.add(0)
            queue = [0]
            while queue:
                curr = queue.pop(0)
                c_list = children[curr]
                # BH on children of curr
                c_sorted = sorted(c_list, key=lambda idx: p_vals[idx])
                k_c = 0
                for rk, cid in enumerate(c_sorted, start=1):
                    if p_vals[cid] <= alpha * rk / len(c_list):
                        k_c = rk
                for cid in c_sorted[:k_c]:
                    R_td.add(cid)
                    queue.append(cid)
        power_topdown_sum += sum(1 for i in R_td if i in non_null_set) / len(non_null_set)

    fdr_star = fdr_star_sum / trials
    power_star = power_star_sum / trials
    power_topdown = power_topdown_sum / trials
    star_subtree_rate = star_subtree_valid_count / trials
    bh_subtree_rate = bh_subtree_valid_count / trials

    assert star_subtree_rate == 1.0
    assert bh_subtree_rate < 0.25
    assert fdr_star <= alpha
    assert power_star > power_topdown + 0.25

    return {
        "bh_subtree_constraint_valid_rate": round(bh_subtree_rate, 6),
        "fdr_star_tree": round(fdr_star, 6),
        "power_star_bottom_up": round(power_star, 6),
        "power_topdown_hierarchical": round(power_topdown, 6),
        "star_subtree_constraint_valid_rate": round(star_subtree_rate, 6),
    }


def verify_claim3_one_group_em_and_structured_knockoffs() -> dict[str, float]:
    """Verify Appendix B.4 Gaussian one-group EM score accuracy + Section 6 structured knockoffs."""
    rng = random.Random(20261019)
    # 1D spatial grid x_i in [-1, 1] of length n = 80; true convex interval is [-0.35, 0.35] (28 non-nulls)
    n = 80
    xs = [-1.0 + 2.0 * i / (n - 1) for i in range(n)]
    non_null = {i for i, x in enumerate(xs) if abs(x) <= 0.35}
    alpha = 0.15
    trials = 30

    fdr_em_sum = 0.0
    power_em_sum = 0.0
    power_canon_sum = 0.0
    corr_em_oracle_sum = 0.0

    # Precompute Gaussian kernel smoother weights W_ij for spatial M-step (Appendix B.4 Example 2)
    bandwidth = 0.18
    kernel_w = []
    for i in range(n):
        row = [math.exp(-0.5 * ((xs[i] - xs[j]) / bandwidth) ** 2) for j in range(n)]
        s_row = sum(row)
        kernel_w.append([w / s_row for w in row])

    def fit_em_mu(abs_z: list[float], z_full: list[float], masked_set: set[int]) -> list[float]:
        mu = [0.5] * n
        for _ in range(6):
            pseudo_z = []
            for i in range(n):
                if i not in masked_set:
                    pseudo_z.append(z_full[i])
                else:
                    # E-step Eq (17)/Example 2: w_tilde = 1 / (1 + exp(-2 * mu_i * |z_i|))
                    exponent = max(min(-2.0 * mu[i] * abs_z[i], 40.0), -40.0)
                    w_tilde = 1.0 / (1.0 + math.exp(exponent))
                    pseudo_z.append((2.0 * w_tilde - 1.0) * abs_z[i])
            # M-step: smooth pseudo-dataset with spatial kernel basis
            mu = [sum(kernel_w[i][j] * pseudo_z[j] for j in range(n)) for i in range(n)]
        return mu

    for _ in range(trials):
        z_vals = []
        p_vals = []
        for i in range(n):
            mu_true = 2.4 if i in non_null else 0.0
            z = rng.gauss(mu_true, 1.0)
            z_vals.append(z)
            p_vals.append(1.0 - norm_cdf(z))
        abs_z = [abs(z) for z in z_vals]
        h_vals = [2.0 if p >= 0.5 else 0.0 for p in p_vals]
        g_vals = [min(p, 1.0 - p) for p in p_vals]

        # Oracle smooth on full z_vals vs initial EM smooth on fully masked |z_i|
        mu_oracle = [sum(kernel_w[i][j] * z_vals[j] for j in range(n)) for i in range(n)]
        mu_init = fit_em_mu(abs_z, z_vals, set(range(n)))
        mean_o = sum(mu_oracle) / n
        mean_m = sum(mu_init) / n
        num = sum((mu_oracle[i] - mean_o) * (mu_init[i] - mean_m) for i in range(n))
        den = math.sqrt(
            sum((mu_oracle[i] - mean_o) ** 2 for i in range(n))
            * sum((mu_init[i] - mean_m) ** 2 for i in range(n))
        )
        corr_em_oracle_sum += num / max(den, 1e-12)

        # Convex interval peeling [lo, hi] using EM model-assisted scores vs canonical g(p_i)
        lo_em, hi_em = 0, n - 1
        scores_em = mu_init
        step = 0
        while lo_em <= hi_em:
            length = hi_em - lo_em + 1
            fdp_hat = (2.0 + sum(h_vals[i] for i in range(lo_em, hi_em + 1))) / (1.0 + length)
            if fdp_hat <= alpha:
                break
            if step > 0 and step % 15 == 0:
                scores_em = fit_em_mu(abs_z, z_vals, set(range(lo_em, hi_em + 1)))
            # Peel boundary endpoint (lo_em or hi_em) with smaller estimated signal score
            if scores_em[lo_em] <= scores_em[hi_em]:
                lo_em += 1
            else:
                hi_em -= 1
            step += 1

        R_em = set(range(lo_em, hi_em + 1)) if lo_em <= hi_em else set()
        fdr_em_sum += sum(1 for i in R_em if i not in non_null) / max(1, len(R_em))
        power_em_sum += sum(1 for i in R_em if i in non_null) / len(non_null)

        # Canonical score interval peeling (peels boundary endpoint with larger g(p_i))
        lo_c, hi_c = 0, n - 1
        while lo_c <= hi_c:
            length = hi_c - lo_c + 1
            fdp_hat = (2.0 + sum(h_vals[i] for i in range(lo_c, hi_c + 1))) / (1.0 + length)
            if fdp_hat <= alpha:
                break
            if g_vals[lo_c] >= g_vals[hi_c]:
                lo_c += 1
            else:
                hi_c -= 1
        R_c = set(range(lo_c, hi_c + 1)) if lo_c <= hi_c else set()
        power_canon_sum += sum(1 for i in R_c if i in non_null) / len(non_null)

    # 2. Structured Knockoffs (Section 6): p_i = (1 + 1{W_i <= 0}) / 2, h(p_i) = 2 * 1{W_i <= 0}
    fdr_knock_sum = 0.0
    power_knock_sum = 0.0
    for _ in range(trials):
        W_abs = []
        W_sign = []
        for i in range(n):
            if i in non_null:
                W_abs.append(abs(rng.gauss(2.8, 1.0)))
                W_sign.append(1 if rng.random() < 0.96 else -1)
            else:
                W_abs.append(abs(rng.gauss(0.0, 1.0)))
                W_sign.append(1 if rng.random() < 0.50 else -1)
        # h_knock_i = 2 if W_sign[i] < 0 else 0 (expectation 1 under coin-flip null)
        h_knock = [2.0 if s < 0 else 0.0 for s in W_sign]
        # F_0-measurable smoothed magnitude score across spatial grid (Section 6)
        score_k = [sum(kernel_w[i][j] * W_abs[j] for j in range(n)) for i in range(n)]
        lo_k, hi_k = 0, n - 1
        while lo_k <= hi_k:
            length = hi_k - lo_k + 1
            fdp_hat = (2.0 + sum(h_knock[i] for i in range(lo_k, hi_k + 1))) / (1.0 + length)
            if fdp_hat <= alpha:
                break
            if score_k[lo_k] <= score_k[hi_k]:
                lo_k += 1
            else:
                hi_k -= 1
        R_k = set(range(lo_k, hi_k + 1)) if lo_k <= hi_k else set()
        fdr_knock_sum += sum(1 for i in R_k if i not in non_null) / max(1, len(R_k))
        power_knock_sum += sum(1 for i in R_k if i in non_null) / len(non_null)

    fdr_em = fdr_em_sum / trials
    power_em = power_em_sum / trials
    power_canon = power_canon_sum / trials
    corr_em_oracle = corr_em_oracle_sum / trials
    fdr_knock = fdr_knock_sum / trials
    power_knock = power_knock_sum / trials

    assert corr_em_oracle > 0.85
    assert fdr_em <= alpha
    assert power_em > power_canon
    assert fdr_knock <= alpha
    assert power_knock > 0.65

    return {
        "em_vs_oracle_initial_corr": round(corr_em_oracle, 6),
        "fdr_em_convex_interval": round(fdr_em, 6),
        "fdr_structured_knockoffs": round(fdr_knock, 6),
        "power_canonical_convex_interval": round(power_canon, 6),
        "power_em_convex_interval": round(power_em, 6),
        "power_structured_knockoffs": round(power_knock, 6),
    }


def verify_claim4_asymptotic_power_and_small_alpha_boundary() -> dict[str, float]:
    """Verify Appendix I asymptotic power gain over accumulation tests and Section 5.2 small-alpha / look-back boundaries."""
    rng = random.Random(20261020)
    # 1. Appendix I.3: Uninformative pre-ordering (two-group model with pi_1 = 0.25, alpha = 0.20, h(p)=2*1{p>=0.5})
    # Under alternative N(2.8, 1), mu = E_1[h(p)] = 2 * P(Z + 2.8 <= 0) = 2 * Phi(-2.8) = 0.005110
    # Plain accumulation test threshold condition: pi_1 >= (1 - alpha) / (1 - mu) = 0.80 / 0.994890 = 0.804109.
    # Since pi_1 = 0.25 < 0.804109, t^*_AT = 0 (zero asymptotic power), whereas STAR ordered by g(p_i) has high power!
    n = 240
    pi_1 = 0.25
    alpha = 0.20
    mu_alt = 2.0 * norm_cdf(-2.8)
    pi1_crit_at = (1.0 - alpha) / (1.0 - mu_alt)

    trials = 40
    power_plain_at_sum = 0.0
    power_masked_star_sum = 0.0
    for _ in range(trials):
        is_alt = [i < int(n * pi_1) for i in range(n)]
        rng.shuffle(is_alt)  # uninformative pre-ordering
        p_vals = [
            1.0 - norm_cdf(rng.gauss(2.8 if alt else 0.0, 1.0))
            for alt in is_alt
        ]
        h_vals = [2.0 if p >= 0.5 else 0.0 for p in p_vals]
        g_vals = [min(p, 1.0 - p) for p in p_vals]

        # Plain accumulation test peels in pre-specified order n-1, n-2, ...
        k_at = 0
        running_h = sum(h_vals)
        for m_keep in range(n, 0, -1):
            if (2.0 + running_h) / (1.0 + m_keep) <= alpha:
                k_at = m_keep
                break
            running_h -= h_vals[m_keep - 1]
        power_plain_at_sum += sum(1 for i in range(k_at) if is_alt[i]) / (n * pi_1)

        # Non-interactive STAR peels in decreasing order of g(p_i)
        order_g = sorted(range(n), key=lambda idx: g_vals[idx])
        k_star = 0
        running_h_star = sum(h_vals)
        for m_keep in range(n, 0, -1):
            if (2.0 + running_h_star) / (1.0 + m_keep) <= alpha:
                k_star = m_keep
                break
            running_h_star -= h_vals[order_g[m_keep - 1]]
        rej_star = set(order_g[:k_star])
        power_masked_star_sum += sum(1 for i in rej_star if is_alt[i]) / (n * pi_1)

    # 2. Section 5.2 small-alpha minimum rejection threshold boundary:
    min_rej_seqstep_05 = math.ceil(2.0 / 0.10 - 1.0 - 1e-12)
    min_rej_seqstep_02 = math.ceil(1.25 / 0.10 - 1.0 - 1e-12)

    # 3. Section 3.1 filtration-violation boundary: if an analyst peeks at unmasked p-values (h(p_i)) inside R_t
    # and peels hypotheses with h(p_i) = 2 first (violating F_t-measurability), FDR is severely inflated under global null!
    fdr_cheating_sum = 0.0
    n_cheat = 60
    for _ in range(trials):
        p_null = [rng.random() for _ in range(n_cheat)]
        h_null = [2.0 if p >= 0.5 else 0.0 for p in p_null]
        order_cheat = sorted(range(n_cheat), key=lambda idx: h_null[idx])
        k_c = 0
        running_hc = sum(h_null)
        for m_keep in range(n_cheat, 0, -1):
            if (2.0 + running_hc) / (1.0 + m_keep) <= alpha:
                k_c = m_keep
                break
            running_hc -= h_null[order_cheat[m_keep - 1]]
        if k_c > 0:
            fdr_cheating_sum += 1.0  # all hypotheses are null

    power_plain_at = power_plain_at_sum / trials
    power_masked_star = power_masked_star_sum / trials
    fdr_cheating = fdr_cheating_sum / trials

    assert power_plain_at < 0.02
    assert power_masked_star > 0.70
    assert min_rej_seqstep_05 == 19
    assert min_rej_seqstep_02 == 12
    assert fdr_cheating > 0.95

    return {
        "fdr_filtration_violating_peeking_global_null": round(fdr_cheating, 6),
        "min_rejections_alpha_0_10_pstar_0_20": min_rej_seqstep_02,
        "min_rejections_alpha_0_10_pstar_0_50": min_rej_seqstep_05,
        "plain_accumulation_critical_pi1": round(pi1_crit_at, 6),
        "power_masked_star_uninformative_order": round(power_masked_star, 6),
        "power_plain_accumulation_uninformative_order": round(power_plain_at, 6),
    }


def main() -> None:
    results = {
        "claim1_accumulation_masking_and_prop21": verify_claim1_accumulation_masking_and_prop21(),
        "claim2_tree_heredity_fdr_and_bottom_up_power": verify_claim2_tree_heredity_fdr_and_bottom_up_power(),
        "claim3_one_group_em_and_structured_knockoffs": verify_claim3_one_group_em_and_structured_knockoffs(),
        "claim4_asymptotic_power_and_small_alpha_boundary": verify_claim4_asymptotic_power_and_small_alpha_boundary(),
    }
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
