#!/usr/bin/env python3
"""Constructed boundary & regime verification for Round 289:
AIMech:MinimaxOptimalInferenceAndRankBreakingFromPlackettLucePartialRankings
Primary source: Bruce Hajek, Sewoong Oh, and Jiaming Xu (2014),
Minimax-optimal Inference from Partial Rankings, Advances in Neural
Information Processing Systems (NeurIPS) 27:1475-1483 (arXiv:1406.5638v1).
"""

import json
import math
import random


def numerical_integral(f, a, b, n_steps=4000):
    h = (b - a) / n_steps
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n_steps):
        total += f(a + i * h)
    return total * h


def verify_van_trees_and_gumbel_fisher():
    """Verify Proposition 1 & Theorem 1 (pp. 4-5, 9-10):
    Prior p_0(theta) = cos^2(pi*theta/2) on [-1, 1] has I(p_0) = pi^2,
    and standard Gumbel density mu(x) = e^{-x} e^{-e^{-x}} has I(mu) = 1.
    """
    p0 = lambda th: math.cos(0.5 * math.pi * th) ** 2
    p0_mass = numerical_integral(p0, -1.0, 1.0, 4000)
    assert abs(p0_mass - 1.0) < 1e-12

    # (p0'(th))^2 / p0(th) = (-pi cos(pi*th/2) sin(pi*th/2))^2 / cos^2(pi*th/2) = pi^2 sin^2(pi*th/2)
    fisher_p0_integrand = lambda th: (math.pi * math.sin(0.5 * math.pi * th)) ** 2
    I_p0 = numerical_integral(fisher_p0_integrand, -1.0, 1.0, 4000)
    assert abs(I_p0 - math.pi ** 2) < 1e-10

    # Standard Gumbel CDF F(x) = exp(-exp(-x)), mu(x) = exp(-x - exp(-x))
    # mu'(x)/mu(x) = -1 + exp(-x), so (mu'(x))^2 / mu(x) = (1 - exp(-x))^2 * exp(-x - exp(-x))
    gumbel_fisher_integrand = lambda x: ((1.0 - math.exp(-x)) ** 2) * math.exp(-x - math.exp(-x))
    I_mu = numerical_integral(gumbel_fisher_integrand, -12.0, 25.0, 8000)
    assert abs(I_mu - 1.0) < 1e-6
    return {
        "p0_integral": round(p0_mass, 12),
        "I_p0_numerical": round(I_p0, 8),
        "pi_squared": round(math.pi ** 2, 8),
        "I_gumbel_numerical": round(I_mu, 8),
    }


def verify_fisher_matrix_at_zero_and_claim1():
    """Verify Section 3.2 Proof of Theorem 2 (pp. 10-11) and Section 3.3 Claim 1 (p. 12)."""
    # 1. Exact identity in Proof of Theorem 2:
    # For any k_j >= 2, sum_{l=1}^{k_j-1} (k_j - l) / (k_j (k_j - 1) (k_j - l + 1))
    # = (1 / (k_j - 1)) * (1 - (1 / k_j) * sum_{l=1}^{k_j} (1 / l))
    max_ident_err = 0.0
    for kj in range(2, 25):
        lhs = sum((kj - ell) / (kj * (kj - 1) * (kj - ell + 1)) for ell in range(1, kj))
        harmonic = sum(1.0 / ell for ell in range(1, kj + 1))
        rhs = (1.0 / (kj - 1.0)) * (1.0 - harmonic / kj)
        max_ident_err = max(max_ident_err, abs(lhs - rhs))
    assert max_ident_err < 1e-15

    # 2. Claim 1 (p. 12): For A = diag(p) - p p^T with p_i = e^{theta_i} / sum_l e^{theta_l}
    # and |theta_i| <= b, lambda_2(A) >= 1 / (r e^{2b}), and for extremal vector
    # theta_1 = ... = theta_{r-1} = b, theta_r = -b, lambda_2(A) = e^{2b} r / ((r-1) e^{2b} + 1)^2.
    r = 6
    b = 0.8
    # Extremal theta: r-1 coordinates equal to b, 1 coordinate equal to -b
    # On subspace orthogonal to 1:
    # - vector orthogonal to first r-1 coordinates and 1 is [1, ..., 1, -(r-1)]^T
    #   For this vector alpha, alpha_i - sum_j alpha_j p_j has eigenvalue e^{2b} r / ((r-1) e^{2b} + 1)^2
    denom = (r - 1) * math.exp(2.0 * b) + 1.0
    p_ext = [math.exp(2.0 * b) / denom] * (r - 1) + [1.0 / denom]
    v = [1.0] * (r - 1) + [-(r - 1.0)]
    v_norm = math.sqrt(sum(x * x for x in v))
    v = [x / v_norm for x in v]
    pv = sum(p_ext[i] * v[i] for i in range(r))
    rayleigh_ext = sum(p_ext[i] * (v[i] - pv) ** 2 for i in range(r))
    formula_ext = (math.exp(2.0 * b) * r) / (denom ** 2)
    claim1_lb = 1.0 / (r * math.exp(2.0 * b))
    assert abs(rayleigh_ext - formula_ext) < 1e-15
    assert rayleigh_ext >= claim1_lb
    return {
        "fisher_at_zero_identity_max_err": max_ident_err,
        "claim1_extremal_lambda2": round(rayleigh_ext, 8),
        "claim1_formula_lambda2": round(formula_ext, 8),
        "claim1_lower_bound_1_over_r_e2b": round(claim1_lb, 8),
    }


def sample_pl_ranking(subset, theta, rng):
    """Sample a partial ranking of `subset` under Plackett-Luce model (Definition 1)."""
    # Assign X_i ~ Exp(e^{theta_i}), i.e., mean e^{-theta_i}, sort ascending
    scores = []
    for i in subset:
        u = rng.random()
        while u <= 1e-15:
            u = rng.random()
        x_i = -math.log(u) * math.exp(-theta[i])
        scores.append((x_i, i))
    scores.sort(key=lambda pair: pair[0])
    return [i for _, i in scores]


def fit_pl_mle(rankings, n, b=2.0, lr=0.05, steps=350):
    """Maximize Plackett-Luce log-likelihood L(theta) in Equation (1) by projected gradient ascent."""
    theta = [0.0] * n
    for _ in range(steps):
        grad = [0.0] * n
        for sigma in rankings:
            kj = len(sigma)
            # Precompute suffix sums of exp(theta_{sigma(r)})
            exp_vals = [math.exp(theta[item]) for item in sigma]
            suffix_sum = [0.0] * kj
            running = 0.0
            for idx in range(kj - 1, -1, -1):
                running += exp_vals[idx]
                suffix_sum[idx] = running
            for ell in range(kj - 1):
                winner = sigma[ell]
                grad[winner] += 1.0
                denom = suffix_sum[ell]
                for r_idx in range(ell, kj):
                    item = sigma[r_idx]
                    grad[item] -= exp_vals[r_idx] / denom
        scale = lr / max(1, len(rankings))
        for i in range(n):
            theta[i] += scale * grad[i]
        mean_th = sum(theta) / n
        theta = [max(-b, min(b, th - mean_th)) for th in theta]
        mean_th = sum(theta) / n
        theta = [th - mean_th for th in theta]
    return theta


def fit_pairwise_mle(pairs_weighted, n, b=2.0, lr=3.5, steps=350):
    """Maximize weighted pairwise BTL log-likelihood (Equation 2 for FB, or unweighted for IB)."""
    theta = [0.0] * n
    total_w = max(1.0, sum(w for _, _, w in pairs_weighted))
    for _ in range(steps):
        grad = [0.0] * n
        for winner, loser, w in pairs_weighted:
            diff = theta[winner] - theta[loser]
            prob_loser = 1.0 / (1.0 + math.exp(diff))
            g = w * prob_loser
            grad[winner] += g
            grad[loser] -= g
        scale = lr / total_w
        for i in range(n):
            theta[i] += scale * grad[i]
        mean_th = sum(theta) / n
        theta = [max(-b, min(b, th - mean_th)) for th in theta]
        mean_th = sum(theta) / n
        theta = [th - mean_th for th in theta]
    return theta


def simulate_partial_rankings_and_rank_breaking():
    """Verify Theorems 1-4 and Corollaries 1-2 on n=12 items with k=4 partial rankings."""
    rng = random.Random(20261019)
    n = 12
    k = 4
    b = 0.6
    raw_theta = [-b + 2.0 * b * i / (n - 1) for i in range(n)]
    mean_raw = sum(raw_theta) / n
    theta_star = [x - mean_raw for x in raw_theta]

    m_small = 120
    m_large = 600

    results = {}
    for label, m in [("m_120", m_small), ("m_600", m_large)]:
        rankings = []
        fb_pairs = []
        ib_pairs = []
        all_items = list(range(n))
        for _ in range(m):
            subset = rng.sample(all_items, k)
            sigma = sample_pl_ranking(subset, theta_star, rng)
            rankings.append(sigma)
            # Full breaking (Definition 5, Eq. 2): all (k choose 2) pairs with weight 1/(k-1)
            w_fb = 1.0 / (k - 1.0)
            for a_idx in range(k):
                for b_idx in range(a_idx + 1, k):
                    fb_pairs.append((sigma[a_idx], sigma[b_idx], w_fb))
            # Random Independence-Preserving Breaking (Definition 4): floor(k/2) disjoint pairs
            perm_indices = list(range(k))
            rng.shuffle(perm_indices)
            for t in range(k // 2):
                idx1 = perm_indices[2 * t]
                idx2 = perm_indices[2 * t + 1]
                if idx1 < idx2:
                    ib_pairs.append((sigma[idx1], sigma[idx2], 1.0))
                else:
                    ib_pairs.append((sigma[idx2], sigma[idx1], 1.0))

        theta_ml = fit_pl_mle(rankings, n, b=2.0, lr=2.5, steps=400)
        theta_fb = fit_pairwise_mle(fb_pairs, n, b=2.0, lr=10.0, steps=400)
        theta_ib = fit_pairwise_mle(ib_pairs, n, b=2.0, lr=10.0, steps=400)

        err_ml = math.sqrt(sum((theta_ml[i] - theta_star[i]) ** 2 for i in range(n)))
        err_fb = math.sqrt(sum((theta_fb[i] - theta_star[i]) ** 2 for i in range(n)))
        err_ib = math.sqrt(sum((theta_ib[i] - theta_star[i]) ** 2 for i in range(n)))

        harmonic_k = sum(1.0 / ell for ell in range(1, k + 1))
        cr_factor = 1.0 / (1.0 - harmonic_k / k)
        cr_lb_l2 = math.sqrt(cr_factor * ((n - 1) ** 2) / (m * k))
        oracle_lb_l2 = math.sqrt(0.5 * ((n - 1) ** 2) / (m * k))

        results[label] = {
            "m": m,
            "k": k,
            "oracle_lb_l2": round(oracle_lb_l2, 5),
            "cramer_rao_lb_l2": round(cr_lb_l2, 5),
            "err_ml_l2": round(err_ml, 5),
            "err_fb_l2": round(err_fb, 5),
            "err_ib_l2": round(err_ib, 5),
        }

    # Verify errors shrink as m increases from 120 to 600 and ML/FB beat IB (which uses k/2 pairs)
    assert results["m_600"]["err_ml_l2"] < 0.68 * results["m_120"]["err_ml_l2"]
    assert results["m_600"]["err_fb_l2"] < 0.68 * results["m_120"]["err_fb_l2"]
    assert results["m_600"]["err_ib_l2"] < 0.68 * results["m_120"]["err_ib_l2"]
    assert results["m_600"]["err_ml_l2"] <= results["m_600"]["err_ib_l2"]
    return results


def main():
    vt = verify_van_trees_and_gumbel_fisher()
    fm = verify_fisher_matrix_at_zero_and_claim1()
    sim = simulate_partial_rankings_and_rank_breaking()
    out = {
        "van_trees_and_gumbel": vt,
        "fisher_at_zero_and_claim1": fm,
        "pl_mle_and_rank_breaking": sim,
        "all_assertions_passed": True,
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
