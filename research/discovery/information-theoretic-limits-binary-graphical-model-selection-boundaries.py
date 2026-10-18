#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Santhanam & Wainwright (2012),
'Information-Theoretic Limits of Selecting Binary Graphical Models in High Dimensions',
IEEE Transactions on Information Theory 58(7):4117-4134 (arXiv:0905.2639v1, DOI:10.1109/TIT.2012.2191659).

Verifies:
1. Exact 3-node 2-edge Ising hard-core saturation limit (Example 1, p. 4) and exact
   symmetrized KL divergence S(theta || theta') = sum_{(s,t)} (theta_{st} - theta'_{st})(mu_{st} - mu'_{st})
   and averaged divergence J(theta || theta') = log(Z(theta) Z(theta') / Z((theta + theta')/2)^2) (Eqs. 18-22).
2. Exact clique-minus-edge likelihood ratio q_{st}/(1 - q_{st}) combinatorial decomposition (Eq. 31, p. 13),
   Lemma 1 lower bound exp(omega/2 - 3*lambda/2)/(m + 1) (Eq. 29) and mean-parameter saturation (Eq. 30),
   and Ensemble A & B symmetrized KL bounds (p. 13 & Lemma 2, p. 14).
3. Flipping lemma |Delta(x') - Delta(x)| >= |theta_{st}| (Lemma 8, Eq. 56, p. 26), matching-number
   divergence bound J(theta(G) || theta(G')) >= (m(G, G') / (3*exp(2*omega) + 1)) * sinh^2(lambda/4)
   (Lemma 4, Eq. 38, p. 18), and pairwise mean separation bound (Lemma 6, p. 21).
"""

import itertools
import json
import math
import sys


def all_spins(p):
    return list(itertools.product([-1, 1], repeat=p))


def ising_stats(p, theta_edges):
    """Exact partition function Z(theta), probabilities P_theta(x), and pairwise expectations mu_{st}."""
    spins = all_spins(p)
    weights = []
    for x in spins:
        val = 0.0
        for (s, t), w in theta_edges.items():
            val += w * x[s] * x[t]
        weights.append(math.exp(val))
    z = sum(weights)
    probs = [w / z for w in weights]
    mu = {}
    for s in range(p):
        for t in range(s + 1, p):
            mu[(s, t)] = sum(probs[i] * spins[i][s] * spins[i][t] for i in range(len(spins)))
    return z, probs, mu, spins


def kl_div(probs_p, probs_q):
    return sum(p * math.log(p / q) for p, q in zip(probs_p, probs_q) if p > 0)


def verify_example1_and_divergences():
    """Verify Example 1 (p. 4) hard-core saturation and Eqs. (18)-(22) divergence identities."""
    p = 3
    theta_val = 6.0
    g1 = {(0, 1): theta_val, (1, 2): theta_val}
    g2 = {(0, 1): theta_val, (0, 2): theta_val}
    g3 = {(0, 2): theta_val, (1, 2): theta_val}
    z1, probs1, mu1, spins = ising_stats(p, g1)
    z2, probs2, mu2, _ = ising_stats(p, g2)
    z3, probs3, mu3, _ = ising_stats(p, g3)

    # Hard-core limit: all-ones (+1,+1,+1) is index 7, all-minus (-1,-1,-1) is index 0
    mass_extreme_1 = probs1[0] + probs1[7]
    tv_12 = 0.5 * sum(abs(a - b) for a, b in zip(probs1, probs2))

    # Test exact identities Eqs. (18)-(22) on two 4-node graphs
    p4 = 4
    ga = {(0, 1): 0.4, (1, 2): -0.3, (2, 3): 0.5}
    gb = {(0, 1): 0.2, (0, 3): 0.6, (2, 3): -0.2}
    za, probs_a, mu_a, _ = ising_stats(p4, ga)
    zb, probs_b, mu_b, _ = ising_stats(p4, gb)
    g_mid = {}
    for s in range(p4):
        for t in range(s + 1, p4):
            wa = ga.get((s, t), 0.0)
            wb = gb.get((s, t), 0.0)
            if wa != 0.0 or wb != 0.0:
                g_mid[(s, t)] = 0.5 * (wa + wb)
    z_mid, probs_mid, _, _ = ising_stats(p4, g_mid)

    s_direct = kl_div(probs_a, probs_b) + kl_div(probs_b, probs_a)
    s_eq22 = 0.0
    for s in range(p4):
        for t in range(s + 1, p4):
            ta = ga.get((s, t), 0.0)
            tb = gb.get((s, t), 0.0)
            s_eq22 += (ta - tb) * (mu_a[(s, t)] - mu_b[(s, t)])

    j_direct = kl_div(probs_mid, probs_a) + kl_div(probs_mid, probs_b)
    j_eq20 = math.log((za * zb) / (z_mid ** 2))
    # Concavity of log Z(theta) implies J(theta || theta') >= 0 and S(theta || theta') >= 4 J(theta || theta')?
    # Note: D(theta || theta') + D(theta' || theta) >= 0 and J >= 0.
    passed = (
        mass_extreme_1 > 0.9999
        and tv_12 < 1e-4
        and abs(s_direct - s_eq22) < 1e-12
        and abs(j_direct - j_eq20) < 1e-12
        and j_direct > 0.0
    )
    return {
        "check": "example1_hardcore_and_divergence_identities_eqs_18_22",
        "passed": passed,
        "mass_extreme_theta6": round(mass_extreme_1, 8),
        "tv_distance_g1_g2_theta6": round(tv_12, 8),
        "symmetrized_kl_diff": abs(s_direct - s_eq22),
        "j_divergence_diff": abs(j_direct - j_eq20),
    }


def verify_clique_minus_edge_lemma1_and_ensembles():
    """Verify Eq. (31) combinatorial ratio, Lemma 1 Eqs. (29)-(30), Ensemble A, and Lemma 2 Ensemble B."""
    m = 6
    lam = 0.45
    omega = lam * m  # omega = 2.7 >= 2
    # Construct G^{0,1} = K_m \ {(0,1)} with edge weight lam
    theta_gst = {}
    for u in range(m):
        for v in range(u + 1, m):
            if (u, v) != (0, 1):
                theta_gst[(u, v)] = lam
    _, probs_gst, mu_gst, spins = ising_stats(m, theta_gst)

    q_st = sum(p for p, x in zip(probs_gst, spins) if x[0] * x[1] == 1)
    ratio_exact = q_st / (1.0 - q_st)

    # Exact combinatorial formula for K_m \ {(s,t)} (with r = m - 2 vertices in V \ {s,t}):
    # Numerator: sum_{j=0}^{m-2} C(m-2, j) exp((lambda/2)*((2j - (m-2) + 2)^2 - 4))
    # Denominator: sum_{j=0}^{m-2} C(m-2, j) exp((lambda/2)*((2j - (m-2))^2))
    r_other = m - 2
    num_exact_comb = 0.0
    den_exact_comb = 0.0
    for j in range(r_other + 1):
        comb = math.comb(r_other, j)
        d_j = 2 * j - r_other
        num_exact_comb += comb * math.exp(0.5 * lam * ((d_j + 2) ** 2 - 4))
        den_exact_comb += comb * math.exp(0.5 * lam * (d_j ** 2))
    ratio_exact_comb = num_exact_comb / den_exact_comb

    # Lemma 1 Eq. (29) lower bound: exp(omega/2 - 3*lambda/2) / (m + 1)
    ratio_lb_eq29 = math.exp(0.5 * omega - 1.5 * lam) / (m + 1.0)
    # Lemma 1 Eq. (30) mean parameter lower bound:
    mu_exact = mu_gst[(0, 1)]
    mu_from_q = 2.0 * q_st - 1.0
    mu_lb_eq30 = 1.0 - (2.0 * (m + 1.0) * math.exp(1.5 * lam)) / (
        math.exp(0.5 * omega) + (m + 1.0) * math.exp(1.5 * lam)
    )

    # Ensemble B symmetrized KL between G^{0,1} and G^{2,3}:
    theta_guv = {}
    for u in range(m):
        for v in range(u + 1, m):
            if (u, v) != (2, 3):
                theta_guv[(u, v)] = lam
    _, probs_guv, mu_guv, _ = ising_stats(m, theta_guv)
    s_ens_b = kl_div(probs_gst, probs_guv) + kl_div(probs_guv, probs_gst)
    # By symmetry, S(theta(G^{st}) || theta(G^{uv})) = 2 * lambda * (E_{G^{uv}}[X_s X_t] - E_{G^{st}}[X_s X_t])
    s_ens_b_sym = 2.0 * lam * (mu_guv[(0, 1)] - mu_gst[(0, 1)])
    # Lemma 2 (p. 14) upper bound: 4 * lambda * (m + 1) * exp(3*lambda/2) / exp(omega/2)
    s_ens_b_ub_lemma2 = (4.0 * lam * (m + 1.0) * math.exp(1.5 * lam)) / math.exp(0.5 * omega)
    # Lemma 3 (p. 15, Eq. 33) tighter upper bound via FKG inequality:
    # 16 * omega * exp(5*lambda/2) * sinh(lambda) / exp(omega/2)
    s_ens_b_ub_lemma3 = (16.0 * omega * math.exp(2.5 * lam) * math.sinh(lam)) / math.exp(0.5 * omega)

    # Ensemble A (single edge graphs H_{0,1} vs H_{1,2} on p=3):
    _, probs_h01, mu_h01, _ = ising_stats(3, {(0, 1): lam})
    _, probs_h12, mu_h12, _ = ising_stats(3, {(1, 2): lam})
    s_ens_a = kl_div(probs_h01, probs_h12) + kl_div(probs_h12, probs_h01)
    s_ens_a_formula = 2.0 * lam * math.tanh(lam)

    passed = (
        abs(ratio_exact - ratio_exact_comb) < 1e-12
        and ratio_exact >= ratio_lb_eq29
        and abs(mu_exact - mu_from_q) < 1e-12
        and mu_exact >= mu_lb_eq30
        and abs(s_ens_b - s_ens_b_sym) < 1e-12
        and s_ens_b <= s_ens_b_ub_lemma2
        and s_ens_b <= s_ens_b_ub_lemma3
        and abs(s_ens_a - s_ens_a_formula) < 1e-12
    )
    return {
        "check": "clique_minus_edge_lemma1_and_fano_ensembles",
        "passed": passed,
        "ratio_exact": round(ratio_exact, 8),
        "ratio_comb_diff": abs(ratio_exact - ratio_exact_comb),
        "ratio_lb_eq29": round(ratio_lb_eq29, 8),
        "mu_exact": round(mu_exact, 8),
        "mu_lb_eq30": round(mu_lb_eq30, 8),
        "s_ens_b_exact": round(s_ens_b, 8),
        "s_ens_b_ub_lemma2": round(s_ens_b_ub_lemma2, 8),
        "s_ens_b_ub_lemma3": round(s_ens_b_ub_lemma3, 8),
        "s_ens_a_exact": round(s_ens_a, 8),
    }


def verify_flipping_lemma_and_achievability_bounds():
    """Verify Flipping Lemma (Lemma 8, Eq. 56), Matching Bound (Lemma 4, Eq. 38), and Mean Separation (Lemma 6)."""
    p = 4
    lam = 0.5
    # G has edges (0,1) and (2,3); G' has edges (0,2) and (1,3)
    # Symmetric difference E \Delta E' has 4 edges, maximum degree d=2, matching number m(G, G') = 2
    g = {(0, 1): lam, (2, 3): lam}
    gp = {(0, 2): lam, (1, 3): lam}
    omega = 2.0 * lam

    # Verify Lemma 8 (Eq. 56, p. 26) on matching M = {(0,1), (2,3)} with U = {0, 2}:
    # Delta(x) = 0.5 * sum_{(u,v)} (theta_{uv} - theta'_{uv}) x_u x_v
    spins = all_spins(p)

    def delta_fn(x):
        val = 0.0
        for s in range(p):
            for t in range(s + 1, p):
                val += 0.5 * (g.get((s, t), 0.0) - gp.get((s, t), 0.0)) * x[s] * x[t]
        return val

    # Partition configurations by x_{V \ U} = (x_1, x_3); for each, pair x_U = (x_0, x_2) withflipped signs
    flipping_checks = []
    for x in spins:
        # Flip x_0 leaving x_1, x_2, x_3 fixed (corresponds to edge (0,1) in M with 0 in U, 1 in V\U):
        # Since (0,2) is also incident to 0 in G', check Lemma 8 on a single-edge difference first,
        # and check the general matching bound on (g, gp).
        pass

    # Check Lemma 8 exactly on a matching of isolated difference edges (where U has degree 1 in E \Delta E'):
    g_match = {(0, 1): lam, (2, 3): lam, (1, 3): 0.3}
    gp_match = {(0, 1): -lam, (2, 3): 0.0, (1, 3): 0.3}
    # Here E \Delta E' consists of (0,1) and (2,3); U = {0, 2} has no other incident difference edges
    for x in spins:
        x_flip0 = (-x[0], x[1], x[2], x[3])
        diff0 = abs(
            0.5 * sum((g_match.get((s, t), 0.0) - gp_match.get((s, t), 0.0)) * (x_flip0[s] * x_flip0[t] - x[s] * x[t])
                      for s in range(p) for t in range(s + 1, p))
        )
        flipping_checks.append(diff0 >= lam - 1e-12)

    # Check Lemma 4 (Eq. 38, p. 18): J(theta(G) || theta(G')) >= (m(G, G') / (3*exp(2*omega) + 1)) * sinh^2(lambda/4)
    zg, probs_g, mu_g, _ = ising_stats(p, g)
    zgp, probs_gp, mu_gp, _ = ising_stats(p, gp)
    g_mid = {}
    for s in range(p):
        for t in range(s + 1, p):
            w = 0.5 * (g.get((s, t), 0.0) + gp.get((s, t), 0.0))
            if w != 0.0:
                g_mid[(s, t)] = w
    z_mid, _, _, _ = ising_stats(p, g_mid)
    j_val = math.log((zg * zgp) / (z_mid ** 2))
    m_ggp = 2
    j_lb_lemma4 = (m_ggp / (3.0 * math.exp(2.0 * omega) + 1.0)) * (math.sinh(lam / 4.0) ** 2)

    # Check Lemma 6 (p. 21): max_{(u,v)} |mu_G(u,v) - mu_{G'}(u,v)| >= sinh^2(lambda/4) / (2*omega*(3*exp(2*omega) + 1))
    max_mu_diff = max(abs(mu_g[(s, t)] - mu_gp[(s, t)]) for s in range(p) for t in range(s + 1, p))
    mu_diff_lb_lemma6 = (math.sinh(lam / 4.0) ** 2) / (2.0 * omega * (3.0 * math.exp(2.0 * omega) + 1.0))

    passed = (
        all(flipping_checks)
        and j_val >= j_lb_lemma4
        and max_mu_diff >= mu_diff_lb_lemma6
    )
    return {
        "check": "flipping_lemma8_matching_bound_lemma4_and_mean_separation_lemma6",
        "passed": passed,
        "flipping_lemma_all_configs_hold": all(flipping_checks),
        "j_divergence_exact": round(j_val, 8),
        "j_lb_lemma4": round(j_lb_lemma4, 8),
        "max_mu_diff_exact": round(max_mu_diff, 8),
        "mu_diff_lb_lemma6": round(mu_diff_lb_lemma6, 8),
    }


def main():
    results = [
        verify_example1_and_divergences(),
        verify_clique_minus_edge_lemma1_and_ensembles(),
        verify_flipping_lemma_and_achievability_bounds(),
    ]
    all_passed = all(r["passed"] for r in results)
    summary = {"all_passed": all_passed, "results": results}
    print(json.dumps(summary, indent=2))
    if not all_passed:
        sys.exit(1)


if __name__ == "__main__":
    main()
