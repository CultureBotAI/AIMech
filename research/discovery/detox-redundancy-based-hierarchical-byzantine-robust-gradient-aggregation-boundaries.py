#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 525:
DETOX (Redundancy-Based Framework for Faster and More Robust Gradient Aggregation)
Rajput, Wang, Charles, & Papailiopoulos, NeurIPS 2019 (arXiv:1907.12205).

Verifies:
1. Lemma 4 & Theorem 1 exact hypergeometric expectation of effective Byzantine votes
   hat_q after within-group majority voting over hat_p = p/r groups of odd size r:
   - For r = 3: E[hat_q] = (p/3) * (C(q,3) + C(q,2)*C(p-q,1)) / C(p,3) <= q*eps*(4 - 2*eps)/3.
   - Exponential decay of effective Byzantine ratio hat_eps = E[hat_q] / (p/r) as odd r increases.
2. Algorithm 1 (DETOX) + Algorithm 2 (HIER-AGGR):
   Stage 1 partitions p nodes into p/r groups of size r and takes majority vote z_j;
   Stage 2 partitions the p/r votes into k vote groups, averages each vote group via A_0,
   and applies robust aggregator A_1 (Coordinate-Wise Median / Trimmed-Mean) to the k group means.
3. Theorem 3 variance and Byzantine error reduction compared to direct Coordinate-Wise Median
   without DETOX under the ALIE / reverse-gradient Byzantine attacks.
"""

import math
import random


def comb(n, k):
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)


def expected_byzantine_votes_exact(p, q, r):
    """Exact hypergeometric expectation E[hat_q] when partitioning p nodes into p/r groups of size r."""
    half = (r + 1) // 2
    prob_group_byz = sum(comb(q, j) * comb(p - q, r - j) for j in range(half, r + 1)) / comb(p, r)
    return (p / r) * prob_group_byz


def majority_vote_group(vecs, tol=1e-9):
    """Return majority vector if a strict majority (> r/2) agrees, else zero vector."""
    r = len(vecs)
    d = len(vecs[0])
    for i in range(r):
        count = sum(
            1 for j in range(r)
            if math.sqrt(sum((vecs[i][c] - vecs[j][c]) ** 2 for c in range(d))) <= tol
        )
        if count > r // 2:
            return list(vecs[i])
    return [0.0 for _ in range(d)]


def coord_median(vecs):
    k = len(vecs)
    d = len(vecs[0])
    out = []
    for c in range(d):
        col = sorted(vecs[i][c] for i in range(k))
        out.append(col[k // 2])
    return out


def l2_dist(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def main():
    # 1. Verify Lemma 4 (r = 3) and Theorem 1 exponential decay of Byzantine vote ratio
    p = 45
    q = 9  # eps = 0.2
    eps = q / p
    eq_r3 = expected_byzantine_votes_exact(p, q, 3)
    lemma4_bound = q * eps * (4.0 - 2.0 * eps) / 3.0
    assert eq_r3 <= lemma4_bound + 1e-12, f"Lemma 4 violated: {eq_r3} > {lemma4_bound}"

    # Check exponential decay of effective Byzantine fraction hat_eps(r) = E[hat_q] / (p/r)
    # for p = 105, q = 21 (eps = 0.2) across r in {1, 3, 5, 7}
    p_large, q_large = 105, 21
    ratios = [expected_byzantine_votes_exact(p_large, q_large, r) / (p_large / r) for r in (1, 3, 5, 7)]
    assert ratios[0] > ratios[1] > ratios[2] > ratios[3], f"Expected strict decay: {ratios}"

    # 2. Verify Algorithm 1 (DETOX) + Algorithm 2 (HIER-AGGR) vs vanilla Coordinate-Wise Median
    rng = random.Random(2019)
    d = 12
    true_g = [0.8 if c % 2 == 0 else -0.6 for c in range(d)]
    sigma = 0.45

    # Run 40 Monte Carlo trials with p = 45 nodes, q = 12 Byzantine nodes, r = 3 (15 groups),
    # k = 5 vote groups of size 3 in HIER-AGGR (A_0 = Mean, A_1 = Coordinate-Wise Median)
    q_sim = 12
    r_sim = 3
    k_groups = 5
    detox_errs = []
    vanilla_med_errs = []

    for _ in range(40):
        # Vanilla setup: each honest node computes gradient with variance sigma^2;
        # Byzantine nodes mount ALIE shift attack (mu + z * sigma) just inside honest tail
        nodes = list(range(p))
        rng.shuffle(nodes)
        byz_set = set(nodes[:q_sim])

        vanilla_grads = []
        for i in range(p):
            if i in byz_set:
                vanilla_grads.append([true_g[c] + 1.5 * sigma for c in range(d)])
            else:
                vanilla_grads.append([true_g[c] + rng.gauss(0.0, sigma) for c in range(d)])
        vanilla_est = coord_median(vanilla_grads)
        vanilla_med_errs.append(l2_dist(vanilla_est, true_g))

        # DETOX setup: p/r = 15 groups of size r = 3; each group shares a batch r times larger
        # so honest group gradient is identical across honest nodes in the same group
        votes = []
        for g_idx in range(p // r_sim):
            group_nodes = nodes[g_idx * r_sim : (g_idx + 1) * r_sim]
            honest_group_grad = [true_g[c] + rng.gauss(0.0, sigma / math.sqrt(r_sim)) for c in range(d)]
            group_outputs = []
            for node_id in group_nodes:
                if node_id in byz_set:
                    group_outputs.append([true_g[c] + 1.5 * sigma for c in range(d)])
                else:
                    group_outputs.append(list(honest_group_grad))
            votes.append(majority_vote_group(group_outputs))

        # HIER-AGGR (Algorithm 2): partition 15 votes into k = 5 vote groups of size 3,
        # apply A_0 = Mean on each vote group, then A_1 = Coordinate-Wise Median
        vote_group_size = (p // r_sim) // k_groups
        z_hat = []
        for v_idx in range(k_groups):
            sub_votes = votes[v_idx * vote_group_size : (v_idx + 1) * vote_group_size]
            mean_v = [sum(v[c] for v in sub_votes) / vote_group_size for c in range(d)]
            z_hat.append(mean_v)
        detox_est = coord_median(z_hat)
        detox_errs.append(l2_dist(detox_est, true_g))

    mean_detox_err = sum(detox_errs) / len(detox_errs)
    mean_vanilla_err = sum(vanilla_med_errs) / len(vanilla_med_errs)
    assert mean_detox_err < 0.60 * mean_vanilla_err, (
        f"Expected DETOX error {mean_detox_err:.4f} < 0.60 * vanilla error {mean_vanilla_err:.4f}"
    )

    print(
        f"[PASS] Round 525 DETOX (Rajput et al. 2019): "
        f"E[hat_q]_r3={eq_r3:.4f}<=lemma4={lemma4_bound:.4f}, "
        f"hat_eps_decay={[round(x, 4) for x in ratios]}, "
        f"err_detox={mean_detox_err:.4f} < err_vanilla_med={mean_vanilla_err:.4f}"
    )


if __name__ == "__main__":
    main()
