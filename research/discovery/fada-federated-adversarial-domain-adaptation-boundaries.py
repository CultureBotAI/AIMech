#!/usr/bin/env python3
"""Boundary verification for Round 516: FADA (Peng et al., ICLR 2020).

Verifies:
1. Theorem 2 / Theorem 3 weighted federated domain adaptation bound (Eq. 2 & Eq. 9):
   d_{H Delta H}(D_S_tilde, D_T) <= sum_{i=1}^N alpha_i d_{H Delta H}(D_{S_i}, D_T) via triangle inequality,
   and minimizing the bound with respect to alpha shifts weight onto low-discrepancy source domains.
2. Dynamic Attention via K-Means Gap Statistics Gain (Eq. 3):
   I = sum_{r=1}^k (1 / (2 n_r)) sum_{i,j in C_r} ||f_i^t - f_j^t||_2, I_i^{gain} = I_i^{p-1} - I_i^p,
   and alpha = Softmax(I_1^{gain}, ..., I_N^{gain}) assigns high weight to source domains that tighten target clusters.
3. Representation disentanglement via negative entropy loss L_{ent} (Eq. 7) and MINE mutual information estimator
   I(P, Q) (Eq. 8).
"""

import math
import random


def gap_statistic_dispersion(clusters):
    """Computes Eq. (3): I = sum_{r=1}^k (1 / (2 n_r)) sum_{i,j in C_r} ||f_i^t - f_j^t||_2."""
    total_I = 0.0
    for cluster in clusters:
        nr = len(cluster)
        cluster_sum = 0.0
        for i in range(nr):
            for j in range(nr):
                dist = math.sqrt(sum((cluster[i][d] - cluster[j][d]) ** 2 for d in range(len(cluster[i]))))
                cluster_sum += dist
        total_I += cluster_sum / (2.0 * nr)
    return total_I


def softmax(vals):
    m = max(vals)
    exps = [math.exp(v - m) for v in vals]
    s = sum(exps)
    return [e / s for e in exps]


def main():
    rng = random.Random(516)

    # 1. Verify Theorem 2 / Theorem 3 triangle inequality on H Delta H divergence (Eq. 9 & page 18 proof)
    # 3 source domains with empirical probabilities Pr_{D_{S_i}}(A) on symmetric-difference events A in A_{H Delta H}
    pr_sources = [
        [0.52, 0.31, 0.78],  # Source 0: close to target
        [0.85, 0.10, 0.20],  # Source 1: far from target
        [0.15, 0.80, 0.25],  # Source 2: far from target
    ]
    pr_target = [0.50, 0.30, 0.80]
    alpha = [0.7, 0.2, 0.1]

    # Mixture distribution Pr_{D_S_tilde}(A) = sum_i alpha_i Pr_{D_{S_i}}(A)
    d_h_mix = 2.0 * max(
        abs(sum(alpha[i] * pr_sources[i][a] for i in range(3)) - pr_target[a])
        for a in range(3)
    )
    d_h_each = [
        2.0 * max(abs(pr_sources[i][a] - pr_target[a]) for a in range(3))
        for i in range(3)
    ]
    weighted_d_h = sum(alpha[i] * d_h_each[i] for i in range(3))
    assert d_h_mix <= weighted_d_h + 1e-12, f"Triangle inequality violated: {d_h_mix} > {weighted_d_h}"

    # 2. Verify Dynamic Attention via Gap Statistics Gain (Eq. 3)
    # Initial target features in k=2 clusters before step p:
    clusters_before = [
        [[1.0 + rng.gauss(0.0, 0.6), 1.0 + rng.gauss(0.0, 0.6)] for _ in range(8)],
        [[-1.0 + rng.gauss(0.0, 0.6), -1.0 + rng.gauss(0.0, 0.6)] for _ in range(8)],
    ]
    I_before = gap_statistic_dispersion(clusters_before)

    # Source 0 gradient contracts intra-cluster variance (beneficial domain);
    # Source 1 gradient leaves clusters unchanged;
    # Source 2 gradient expands intra-cluster variance (negative transfer domain).
    clusters_after_s0 = [[[0.5 * x for x in pt] for pt in cl] for cl in clusters_before]
    clusters_after_s1 = [[[1.0 * x for x in pt] for pt in cl] for cl in clusters_before]
    clusters_after_s2 = [[[1.4 * x for x in pt] for pt in cl] for cl in clusters_before]

    I_gains = [
        I_before - gap_statistic_dispersion(clusters_after_s0),
        I_before - gap_statistic_dispersion(clusters_after_s1),
        I_before - gap_statistic_dispersion(clusters_after_s2),
    ]
    dyn_weights = softmax(I_gains)
    assert I_gains[0] > 0.0 and I_gains[2] < 0.0
    assert dyn_weights[0] > 0.80 and dyn_weights[2] < 0.05, f"Unexpected dynamic weights: {dyn_weights}"

    # 3. Verify MINE mutual information estimator Eq. (8) & negative entropy confusion Eq. (7)
    # Correlated vs independent pairs (p, q) under T(p, q, theta) = theta * p * q
    n_samples = 400
    theta_mine = 0.6
    joint_corr = [(x, x + rng.gauss(0.0, 0.2)) for x in [rng.gauss(0.0, 1.0) for _ in range(n_samples)]]
    marg_q = [rng.gauss(0.0, 1.0) for _ in range(n_samples)]
    mine_corr = (
        sum(theta_mine * p * q for p, q in joint_corr) / n_samples
        - math.log(sum(math.exp(theta_mine * p * qp) for (p, _), qp in zip(joint_corr, marg_q)) / n_samples)
    )
    joint_indep = [(rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0)) for _ in range(n_samples)]
    mine_indep = (
        sum(theta_mine * p * q for p, q in joint_indep) / n_samples
        - math.log(sum(math.exp(theta_mine * p * qp) for (p, _), qp in zip(joint_indep, marg_q)) / n_samples)
    )
    assert mine_corr > 0.25 and mine_indep < 0.05, f"mine_corr={mine_corr}, mine_indep={mine_indep}"

    # Eq. (7): L_ent = -(1/K) sum_k log CI(f_ds)_k is minimized over the probability simplex by uniform 1/K
    K = 5
    uniform_ci = [1.0 / K] * K
    peaked_ci = [0.80, 0.05, 0.05, 0.05, 0.05]
    l_ent_uniform = -sum(math.log(p) for p in uniform_ci) / K
    l_ent_peaked = -sum(math.log(p) for p in peaked_ci) / K
    assert l_ent_uniform < l_ent_peaked

    print(
        f"[PASS] Round 516 FADA (Peng et al. 2020): "
        f"d_H_mix={d_h_mix:.3f}<=weighted={weighted_d_h:.3f}, "
        f"dyn_w0={dyn_weights[0]:.3f}>>dyn_w2={dyn_weights[2]:.4f}, "
        f"MINE_corr={mine_corr:.3f}>>MINE_indep={mine_indep:.3f}"
    )


if __name__ == "__main__":
    main()
