#!/usr/bin/env python3
"""Constructed boundary and numerical verification for Round 208:
AIMech:ReferenceFamilyJERPostHocConfidenceBounds
Primary source: Gilles Blanchard, Pierre Neuvial, & Etienne Roquain (2020),
"Post hoc confidence bounds on false positives using reference families",
The Annals of Statistics 48(3):1281-1303 (arXiv:1703.02307v3 / v2, DOI:10.1214/19-AOS1847).
"""

from __future__ import annotations

import json
import math
import random


def v_bar(R: set[int], ref_family: list[tuple[set[int], int]]) -> int:
    """Equation (7) in v3 / (6) in v2:
    \\overline{V}_{\\mathfrak{R}}(R) = \\min_{k \\in \\{1,...,K\\}} (|R \\setminus R_k| + \\zeta_k) \\wedge |R|.
    """
    best = len(R)
    for R_k, zeta_k in ref_family:
        cand = len(R - R_k) + zeta_k
        if cand < best:
            best = cand
    return best


def v_star(R: set[int], m: int, ref_family: list[tuple[set[int], int]]) -> int:
    """Equation (6) in v3 / (4) in v2:
    V^*_{\\mathfrak{R}}(R) = \\max_{A \\in \\mathcal{A}(\\mathfrak{R})} |R \\cap A|,
    where \\mathcal{A}(\\mathfrak{R}) = \\{A \\subset \\mathbb{N}_m : \\forall k, |R_k \\cap A| \\le \\zeta_k\\}.
    """
    best = 0
    for mask in range(1 << m):
        A = {i + 1 for i in range(m) if (mask >> i) & 1}
        if all(len(R_k & A) <= zeta_k for R_k, zeta_k in ref_family):
            val = len(R & A)
            if val > best:
                best = val
    return best


def all_subsets(m: int) -> list[set[int]]:
    return [{i + 1 for i in range(m) if (mask >> i) & 1} for mask in range(1 << m)]


def binom_tail_prob(m: int, k: int, u: float) -> float:
    """Exact P(U_{(k:m)} <= u) = P(Binom(m, u) >= k) for U_1,...,U_m i.i.d. U(0,1)."""
    if u <= 0.0:
        return 0.0
    if u >= 1.0:
        return 1.0
    # Use log-probabilities to handle extreme k=100 tails accurately
    log_u = math.log(u)
    log_1mu = math.log1p(-u)
    log_terms = []
    for j in range(k, m + 1):
        log_c = math.lgamma(m + 1) - math.lgamma(j + 1) - math.lgamma(m - j + 1)
        log_terms.append(log_c + j * log_u + (m - j) * log_1mu)
    max_log = max(log_terms)
    total = sum(math.exp(lt - max_log) for lt in log_terms) * math.exp(max_log)
    return min(1.0, total)


def beta_quantile(m: int, k: int, lam: float) -> float:
    """Exact quantile t_k^B(lam) = F_k^{-1}(lam) where F_k(x) = P(U_{(k:m)} <= x)."""
    lo, hi = 0.0, 1.0
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if binom_tail_prob(m, k, mid) >= lam:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def goeman_solari_shortcut(R: set[int], p_vals: dict[int, float], c_m: list[float]) -> int:
    """Equation (41) in v2 Section 8.3:
    \\overline{V}^{GS}_\\alpha(R) = |R| - (1 + \\max\\{S_r, 1 \\le r \\le |R|\\}) \\vee 0,
    where S_r = \\max\\{0 \\le s \\le r-1 : p_{(r:R)} \\le c^m_{r-s}\\}.
    """
    if not R:
        return 0
    sorted_p = sorted(p_vals[i] for i in R)
    max_sr = -10**9
    for r in range(1, len(R) + 1):
        p_r = sorted_p[r - 1]
        for s in range(r):
            if p_r <= c_m[r - s - 1]:
                if s > max_sr:
                    max_sr = s
    s_bound = max(0, 1 + max_sr) if max_sr >= 0 else 0
    return len(R) - s_bound


def main() -> None:
    # 1. Section 2: General Reference-Family Properties
    # (a) Proposition 2.3 (v3) / Proposition 2.2 (v2): NP-hardness / strict gap on triangle graph
    # Triangle graph on m=3 vertices: edges {1,2}, {2,3}, {1,3}, each with zeta_e = 1.
    triangle_ref = [({1, 2}, 1), ({2, 3}, 1), ({1, 3}, 1)]
    R_full3 = {1, 2, 3}
    v_star_triangle = v_star(R_full3, 3, triangle_ref)
    v_bar_triangle = v_bar(R_full3, triangle_ref)
    assert v_star_triangle == 1, f"Expected max independent set size 1, got {v_star_triangle}"
    assert v_bar_triangle == 2, f"Expected pairwise bound 2, got {v_bar_triangle}"
    assert v_star_triangle < v_bar_triangle

    # (b) Proposition 2.4 (v3) / Proposition 2.3 (v2): Self-consistency idempotence
    # Construct a non-nested reference family on m=5 where tilde{zeta}_k < zeta_k strictly
    non_nested_ref = [({1, 2}, 1), ({1, 2, 3}, 3), ({2, 3, 4}, 2), ({1, 4, 5}, 2)]
    tilde_zeta = [v_bar(R_k, non_nested_ref) for R_k, _ in non_nested_ref]
    assert tilde_zeta[1] < non_nested_ref[1][1]  # |{1,2,3} \ {1,2}| + 1 = 2 < 3
    tilde_ref = [(R_k, tz) for (R_k, _), tz in zip(non_nested_ref, tilde_zeta)]
    for R in all_subsets(5):
        assert v_bar(R, non_nested_ref) == v_bar(R, tilde_ref)
    # Check self-consistency fixed-point equation (12)
    for k, (R_k, tz_k) in enumerate(tilde_ref):
        assert tz_k == v_bar(R_k, tilde_ref)

    # (c) Proposition 2.5 (v3) / Proposition 2.4 (v2) & Proposition 2.1:
    # Exactness V_bar == V_star under nestedness R_1 subset R_2 subset ... subset R_K
    nested_ref = [({1}, 0), ({1, 2, 3}, 1), ({1, 2, 3, 4, 5}, 2), ({1, 2, 3, 4, 5, 6}, 4)]
    subsets_6 = all_subsets(6)
    for R in subsets_6:
        vb = v_bar(R, nested_ref)
        vs = v_star(R, 6, nested_ref)
        assert vb == vs, f"Mismatch for {R}: v_bar={vb}, v_star={vs}"
    # Check Proposition 2.1 event equivalence across all H_0 subset N_6
    for H0 in subsets_6:
        event_E = all(len(R_k & H0) <= zeta_k for R_k, zeta_k in nested_ref)
        event_Vbar = all(len(R & H0) <= v_bar(R, nested_ref) for R in subsets_6)
        event_Vstar = all(len(R & H0) <= v_star(R, 6, nested_ref) for R in subsets_6)
        event_Sbar_zero = (len(H0) - v_bar(H0, nested_ref)) == 0
        assert event_E == event_Vbar == event_Vstar == event_Sbar_zero

    # (d) Section 8.3 (Lemmas 8.1-8.2 in v2): Exact equivalence with Goeman-Solari (2011) shortcut
    m_gs = 6
    p_vals_gs = {1: 0.002, 2: 0.011, 3: 0.018, 4: 0.042, 5: 0.120, 6: 0.450}
    alpha_gs = 0.05
    c_m_gs = [alpha_gs * k / m_gs for k in range(1, m_gs + 1)]
    ref_gs = [({i for i, p in p_vals_gs.items() if p <= c_m_gs[k - 1]}, k - 1) for k in range(1, m_gs + 1)]
    for R in subsets_6:
        assert v_bar(R, ref_gs) == goeman_solari_shortcut(R, p_vals_gs, c_m_gs)

    # (e) Section 8.4 (v3 p. 25): Admissible sets wrt V_bar belong to the reference family
    admissible_sets = []
    for R in subsets_6:
        if not R:
            continue
        s_R = len(R) - v_bar(R, nested_ref)
        v_R = v_bar(R, nested_ref)
        cond_i = all(v_bar(R_sup, nested_ref) > v_R for R_sup in subsets_6 if R_sup > R)
        cond_ii = all((len(R_sub) - v_bar(R_sub, nested_ref)) < s_R for R_sub in subsets_6 if R_sub < R)
        if cond_i and cond_ii:
            admissible_sets.append(R)
    ref_sets_only = [R_k for R_k, _ in nested_ref]
    for R_adm in admissible_sets:
        assert R_adm in ref_sets_only, f"Admissible set {R_adm} not in reference family"

    # 2. Section 4.3 Table 2 & Appendix A Proposition A.1:
    # Simes Unbalancedness vs. Balanced Template Quantiles
    m_tab2 = 1000
    alpha_tab2 = 0.05
    tab2_ks = [1, 2, 3, 4, 5, 10, 100]
    tab2_probs = {}
    tab2_exp_bounds = {}
    for k in tab2_ks:
        prob = binom_tail_prob(m_tab2, k, alpha_tab2 * k / m_tab2)
        exp_bd = math.exp(-0.25 * k * (1.0 - alpha_tab2 - 1.0 / (m_tab2 + 1)) ** 2)
        assert prob <= exp_bd
        tab2_probs[str(k)] = prob
        tab2_exp_bounds[str(k)] = exp_bd

    # Verify Table 2 printed values (v3 p. 13 and v2 p. 8)
    assert abs(tab2_probs["1"] - 4.9e-2) < 0.05e-2
    assert abs(tab2_probs["2"] - 4.7e-3) < 0.05e-3
    assert abs(tab2_probs["3"] - 5.0e-4) < 0.05e-4
    assert abs(tab2_probs["4"] - 5.7e-5) < 0.05e-5
    assert abs(tab2_probs["5"] - 6.6e-6) < 0.05e-6
    assert abs(tab2_probs["10"] - 1.6e-10) < 0.05e-10
    assert abs(tab2_probs["100"] - 5.8e-93) < 0.1e-93

    # Check Proposition A.1(ii) Beta quantile lower/upper bounds for balanced template
    m_beta = 100
    lam_beta = 0.05
    for k in [1, 5, 10, 25, 50]:
        tk_val = beta_quantile(m_beta, k, lam_beta)
        upper_val = k / (m_beta + 1)
        lower_val = (
            k / (m_beta + 1)
            - math.sqrt((k / (m_beta + 1)) * (1.0 - k / (m_beta + 1)))
            * (m_beta ** -0.5)
            * math.sqrt(4.0 * math.log(1.0 / lam_beta))
        )
        assert lower_val <= tk_val <= upper_val
        # Check Proposition A.1(iii) exponential decay when m_0 < m
        m0_beta = 60
        prob_m0 = binom_tail_prob(m0_beta, k, tk_val)
        exp_m0_bd = math.exp(-(k / 32.0) * (1.0 - m0_beta / m_beta) ** 2)
        assert prob_m0 <= exp_m0_bd

    # 3. Sections 5-6 (Algorithm 1, Theorems 5.7-5.8):
    # Known Equicorrelation and Unknown Dependence (Random Sign-Flipping) Step-Down JER Control
    rng = random.Random(20261018)
    m_sim = 50
    m0_sim = 35  # pi_0 = 0.70
    K_sim = 25
    alpha_sim = 0.20
    rho_sim = 0.50
    snr_sim = 3.5

    # Pre-generate Monte-Carlo null reference table under known equicorrelation rho = 0.50
    G_mc = 1000
    null_q_samples: list[list[float]] = []
    sqrt_rho = math.sqrt(rho_sim)
    sqrt_1mrho = math.sqrt(1.0 - rho_sim)
    for _ in range(G_mc):
        z0 = rng.gauss(0.0, 1.0)
        q_vec = []
        for _i in range(m_sim):
            zi = sqrt_rho * z0 + sqrt_1mrho * rng.gauss(0.0, 1.0)
            # one-sided p-value Phi(-zi) = 0.5 * erfc(zi / sqrt(2))
            q_vec.append(0.5 * math.erfc(zi / math.sqrt(2.0)))
        null_q_samples.append(q_vec)

    def calibrate_lambda_linear_known(A_indices: list[int]) -> float:
        """Equation (24) & (26): lambda^L(alpha, A) under known dependence."""
        c_len = min(K_sim, len(A_indices))
        if c_len == 0:
            return 1.0
        psi_vals = []
        for q_vec in null_q_samples:
            q_A = sorted(q_vec[idx] for idx in A_indices)
            min_inv = min(min(1.0, (m_sim / k) * q_A[k - 1]) for k in range(1, c_len + 1))
            psi_vals.append(min_inv)
        psi_vals.sort()
        idx_q = int(math.floor(alpha_sim * G_mc))
        return psi_vals[min(idx_q, G_mc - 1)]

    lam_full_known = calibrate_lambda_linear_known(list(range(m_sim)))
    lam_oracle_known = calibrate_lambda_linear_known(list(range(m0_sim)))
    assert lam_full_known > alpha_sim  # Adapts to positive equicorrelation rho = 0.50
    assert lam_oracle_known >= lam_full_known  # Monotonicity (21): A subset A' => lambda(alpha, A) >= lambda(alpha, A')

    # Evaluate empirical JER across N_trials = 600 runs
    N_trials = 600
    simes_viol = 0
    ss_viol = 0
    sd_viol = 0
    oracle_viol = 0
    mean_s_simes = 0.0
    mean_s_sd = 0.0

    for _ in range(N_trials):
        z0 = rng.gauss(0.0, 1.0)
        p_obs = []
        for i in range(m_sim):
            mu_i = 0.0 if i < m0_sim else snr_sim
            xi = mu_i + sqrt_rho * z0 + sqrt_1mrho * rng.gauss(0.0, 1.0)
            p_obs.append(0.5 * math.erfc(xi / math.sqrt(2.0)))

        # Step-down Algorithm 1
        A_curr = list(range(m_sim))
        while True:
            lam_j = calibrate_lambda_linear_known(A_curr)
            t1_j = lam_j * 1.0 / m_sim
            A_next = [i for i in range(m_sim) if p_obs[i] >= t1_j]
            if len(A_next) == len(A_curr):
                break
            A_curr = A_next
        lam_sd = calibrate_lambda_linear_known(A_curr)
        assert lam_sd >= lam_full_known

        p_null_sorted = sorted(p_obs[:m0_sim])
        c_lim = min(K_sim, m0_sim)
        if any(p_null_sorted[k - 1] < alpha_sim * k / m_sim for k in range(1, c_lim + 1)):
            simes_viol += 1
        if any(p_null_sorted[k - 1] < lam_full_known * k / m_sim for k in range(1, c_lim + 1)):
            ss_viol += 1
        if any(p_null_sorted[k - 1] < lam_sd * k / m_sim for k in range(1, c_lim + 1)):
            sd_viol += 1
        if any(p_null_sorted[k - 1] < lam_oracle_known * k / m_sim for k in range(1, c_lim + 1)):
            oracle_viol += 1

        # Lower bound S(N_m) on total true discoveries
        s_simes = max(
            [0] + [sum(1 for p in p_obs if p < alpha_sim * k / m_sim) - (k - 1) for k in range(1, K_sim + 1)]
        )
        s_sd = max(
            [0] + [sum(1 for p in p_obs if p < lam_sd * k / m_sim) - (k - 1) for k in range(1, K_sim + 1)]
        )
        mean_s_simes += s_simes / N_trials
        mean_s_sd += s_sd / N_trials

    jer_simes = simes_viol / N_trials
    jer_ss = ss_viol / N_trials
    jer_sd = sd_viol / N_trials
    jer_oracle = oracle_viol / N_trials
    assert jer_simes < jer_ss <= jer_sd <= alpha_sim + 0.03
    assert mean_s_sd > mean_s_simes

    # 4. Theorem 5.8: Unknown dependence via sign-flipping group G = {-1, 1}^n
    n_obs = 12
    B_flips = 99
    m_unk = 30
    m0_unk = 20
    K_unk = 15
    alpha_unk = 0.20
    unk_ss_viol = 0
    unk_sd_viol = 0
    N_unk_trials = 300

    for _ in range(N_unk_trials):
        # Generate n_obs i.i.d. copies of equicorrelated Gaussian observations
        X_mat = [[0.0] * n_obs for _ in range(m_unk)]
        for j in range(n_obs):
            z0 = rng.gauss(0.0, 1.0)
            for i in range(m_unk):
                mu_i = 0.0 if i < m0_unk else 1.2
                X_mat[i][j] = mu_i + sqrt_rho * z0 + sqrt_1mrho * rng.gauss(0.0, 1.0)

        # Draw B_flips sign vectors in {-1, 1}^n with g_1 = (+1, ..., +1)
        signs = [[1] * n_obs]
        for _b in range(B_flips - 1):
            signs.append([1 if rng.random() < 0.5 else -1 for _ in range(n_obs)])

        # Compute transformed two-sided p-values p_i(g_b . X) for each b = 1..B
        p_trans = []
        for s_vec in signs:
            p_b = []
            for i in range(m_unk):
                t_stat = abs(sum(s_vec[j] * X_mat[i][j] for j in range(n_obs))) / math.sqrt(n_obs)
                p_b.append(math.erfc(t_stat / math.sqrt(2.0)))
            p_trans.append(p_b)

        def calibrate_unk(A_idx: list[int]) -> float:
            c_len = min(K_unk, len(A_idx))
            if c_len == 0:
                return 1.0
            psi_b = []
            for b in range(B_flips):
                p_A = sorted(p_trans[b][i] for i in A_idx)
                psi_b.append(min(min(1.0, (m_unk / k) * p_A[k - 1]) for k in range(1, c_len + 1)))
            psi_b.sort()
            # Equation (25): lambda(alpha, A) = Psi_{(floor(alpha * B) + 1)} (1-indexed -> floor(alpha * B) 0-indexed)
            return psi_b[int(math.floor(alpha_unk * B_flips))]

        lam_unk_ss = calibrate_unk(list(range(m_unk)))
        A_curr = list(range(m_unk))
        while True:
            lam_j = calibrate_unk(A_curr)
            t1_j = lam_j / m_unk
            A_next = [i for i in range(m_unk) if p_trans[0][i] >= t1_j]
            if len(A_next) == len(A_curr):
                break
            A_curr = A_next
        lam_unk_sd = calibrate_unk(A_curr)

        p_null_obs = sorted(p_trans[0][:m0_unk])
        c_lim = min(K_unk, m0_unk)
        if any(p_null_obs[k - 1] < lam_unk_ss * k / m_unk for k in range(1, c_lim + 1)):
            unk_ss_viol += 1
        if any(p_null_obs[k - 1] < lam_unk_sd * k / m_unk for k in range(1, c_lim + 1)):
            unk_sd_viol += 1

    jer_unk_ss = unk_ss_viol / N_unk_trials
    jer_unk_sd = unk_sd_viol / N_unk_trials
    assert jer_unk_ss <= jer_unk_sd <= alpha_unk + 0.03

    # 5. Section 7 (v2 Theorems 7.2-7.3): Ingster-Donoho-Jin Detection Boundary rho*(beta)
    # For beta = 0.60 in (1/2, 3/4]: rho*(0.60) = 0.60 - 0.50 = 0.10, while BH boundary is (1 - sqrt(0.4))^2 = 0.135089.
    beta_val = 0.60
    rho_star_hc = beta_val - 0.50
    rho_star_bh = (1.0 - math.sqrt(1.0 - beta_val)) ** 2
    r_sparse_weak = 0.115
    assert rho_star_hc < r_sparse_weak < rho_star_bh

    summary = {
        "concept_id": "AIMech:ReferenceFamilyJERPostHocConfidenceBounds",
        "primary_source": "Blanchard, Neuvial, & Roquain (2020), The Annals of Statistics 48(3):1281-1303 (arXiv:1703.02307v3/v2, DOI:10.1214/19-AOS1847)",
        "section_2_and_8_structural_properties": {
            "triangle_np_hardness_gap": {
                "v_star_exact": v_star_triangle,
                "v_bar_approx": v_bar_triangle,
            },
            "self_consistency_idempotence_verified_subsets": 32,
            "nested_exactness_v_bar_eq_v_star_verified_subsets": 64,
            "goeman_solari_shortcut_equivalence_verified_subsets": 64,
            "admissible_sets_count": len(admissible_sets),
        },
        "section_4_table_2_simes_unbalancedness": {
            "m": m_tab2,
            "alpha": alpha_tab2,
            "exact_probabilities": {k: float(f"{v:.4e}") for k, v in tab2_probs.items()},
        },
        "sections_5_6_known_equicorrelation_step_down": {
            "rho": rho_sim,
            "alpha": alpha_sim,
            "lambda_full_known": round(lam_full_known, 6),
            "lambda_oracle_known": round(lam_oracle_known, 6),
            "empirical_jer_simes": round(jer_simes, 4),
            "empirical_jer_single_step": round(jer_ss, 4),
            "empirical_jer_step_down": round(jer_sd, 4),
            "empirical_jer_oracle": round(jer_oracle, 4),
            "mean_true_discovery_bound_simes": round(mean_s_simes, 4),
            "mean_true_discovery_bound_step_down": round(mean_s_sd, 4),
        },
        "section_5_4_unknown_dependence_sign_flipping": {
            "B_flips": B_flips,
            "alpha": alpha_unk,
            "empirical_jer_single_step": round(jer_unk_ss, 4),
            "empirical_jer_step_down": round(jer_unk_sd, 4),
        },
        "section_7_detection_boundary": {
            "beta": beta_val,
            "rho_star_balanced_hc": round(rho_star_hc, 6),
            "rho_star_linear_bh": round(rho_star_bh, 6),
            "sparse_weak_r": r_sparse_weak,
        },
        "all_assertions_passed": True,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
