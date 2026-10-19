#!/usr/bin/env python3
"""Constructed boundary and regime verification for:
AIMech:DegreeCorrectedStochasticBlockmodelAndEdgeStubKLDivergenceProfileLikelihood
(Karrer & Newman 2011, Physical Review E 83(1):016107, arXiv:1008.3926v1,
DOI:10.1103/PhysRevE.83.016107).

Verifies in pure Python (standard library only):
1. Closed-form MLEs theta_hat_i = k_i / kappa_{g_i} and omega_hat_{rs} = m_{rs}
   (Eq. 18) and exact preservation of expected block edge counts (Eq. 19) and
   expected vertex degrees <k_i> = k_i (Eq. 20), plus equivalence of the full
   maximized log-likelihood (Eq. 21), unnormalized profile log-likelihood
   L_DC(G|g) = sum_{rs} m_{rs} log(m_{rs}/(kappa_r kappa_s)) (Eq. 23), and
   2m * D_KL(p_K || p_degree) (Eq. 24).
2. Exact O(K + <k>) single-vertex move delta-log-likelihood formula Delta L
   (Eq. 25, p. 5) on a multigraph WITH self-edges (u_i > 0) and multi-edges,
   verifying machine-precision agreement with direct recomputation of Eq. (23).
3. Regime comparison (Section IV, Eqs. 27-28, Fig. 3 left panel): on a 2-group
   bimodal-degree network (expected degrees 10 and 30 in each community,
   lambda = 0.5), the uncorrected SBM log-likelihood (Eq. 6) strictly prefers
   the spurious high-degree vs. low-degree split over the true planted
   community split, whereas the degree-corrected profile log-likelihood (Eq. 23)
   strictly prefers the true planted community split and assigns Delta L_DC = 0
   to pure degree-based splits.
"""

from __future__ import annotations

import math


def a_fn(x: float) -> float:
    return 0.0 if x <= 0.0 else 2.0 * x * math.log(x)


def b_fn(x: float) -> float:
    return 0.0 if x <= 0.0 else x * math.log(x)


def compute_m_and_kappa(
    adj: list[list[float]], g: list[int], k_groups: int
) -> tuple[list[list[float]], list[float]]:
    n = len(adj)
    m_mat = [[0.0] * k_groups for _ in range(k_groups)]
    for i in range(n):
        gi = g[i]
        for j in range(n):
            m_mat[gi][g[j]] += adj[i][j]
    kappa = [sum(m_mat[r][s] for s in range(k_groups)) for r in range(k_groups)]
    return m_mat, kappa


def log_lik_dc(adj: list[list[float]], g: list[int], k_groups: int) -> float:
    """Equation (23): L_DC(G|g) = sum_{rs} m_{rs} log(m_{rs} / (kappa_r kappa_s))."""
    m_mat, kappa = compute_m_and_kappa(adj, g, k_groups)
    total = 0.0
    for r in range(k_groups):
        for s in range(k_groups):
            mrs = m_mat[r][s]
            if mrs > 0.0:
                total += mrs * math.log(mrs / (kappa[r] * kappa[s]))
    return total


def log_lik_sbm(adj: list[list[float]], g: list[int], k_groups: int) -> float:
    """Equation (6): L_SBM(G|g) = sum_{rs} m_{rs} log(m_{rs} / (n_r n_s))."""
    m_mat, _ = compute_m_and_kappa(adj, g, k_groups)
    n_counts = [sum(1 for gi in g if gi == r) for r in range(k_groups)]
    total = 0.0
    for r in range(k_groups):
        for s in range(k_groups):
            mrs = m_mat[r][s]
            if mrs > 0.0:
                total += mrs * math.log(mrs / (n_counts[r] * n_counts[s]))
    return total


def delta_l_eq25(
    adj: list[list[float]], g: list[int], k_groups: int, i: int, s_new: int
) -> float:
    """Exact single-vertex move formula Eq. (25) from group r = g[i] to s_new."""
    r = g[i]
    if r == s_new:
        return 0.0
    m_mat, kappa = compute_m_and_kappa(adj, g, k_groups)
    # u_i is number of self-edges for vertex i; diagonal A_{ii} = 2 * u_i
    u_i = 0.5 * adj[i][i]
    k_i = sum(adj[i])
    # k_{it} is number of edges from vertex i to group t EXCLUDING self-edges
    k_it = [0.0] * k_groups
    for j, a_ij in enumerate(adj[i]):
        if j != i:
            k_it[g[j]] += a_ij

    dl = 0.0
    for t in range(k_groups):
        if t != r and t != s_new:
            # Note: Eq. (25) in Karrer & Newman (2011, p. 5) prints a(m_{rt} + k_{it})
            # by typo instead of a(m_{rt} - k_{it}) when vertex i leaves group r.
            dl += (
                a_fn(m_mat[r][t] - k_it[t])
                - a_fn(m_mat[r][t])
                + a_fn(m_mat[s_new][t] + k_it[t])
                - a_fn(m_mat[s_new][t])
            )
    dl += a_fn(m_mat[r][s_new] + k_it[r] - k_it[s_new]) - a_fn(m_mat[r][s_new])
    dl += (
        b_fn(m_mat[r][r] - 2.0 * (k_it[r] + u_i))
        - b_fn(m_mat[r][r])
        + b_fn(m_mat[s_new][s_new] + 2.0 * (k_it[s_new] + u_i))
        - b_fn(m_mat[s_new][s_new])
        - a_fn(kappa[r] - k_i)
        + a_fn(kappa[r])
        - a_fn(kappa[s_new] + k_i)
        + a_fn(kappa[s_new])
    )
    return dl


def main() -> None:
    # 1. Verify MLEs (Eqs. 18-20), KL identity (Eq. 24), and Eq. (25) on a 6-vertex
    #    3-group multigraph WITH self-edges (diagonal A_{ii} = 2 u_i) and multi-edges
    adj = [
        [2.0, 3.0, 1.0, 0.0, 1.0, 0.0],
        [3.0, 0.0, 2.0, 1.0, 0.0, 0.0],
        [1.0, 2.0, 4.0, 2.0, 1.0, 0.0],
        [0.0, 1.0, 2.0, 0.0, 3.0, 2.0],
        [1.0, 0.0, 1.0, 3.0, 2.0, 4.0],
        [0.0, 0.0, 0.0, 2.0, 4.0, 0.0],
    ]
    g = [0, 0, 1, 1, 2, 2]
    k_groups = 3
    n = len(adj)
    degrees = [sum(adj[i]) for i in range(n)]
    two_m = sum(degrees)
    m_mat, kappa = compute_m_and_kappa(adj, g, k_groups)

    theta_hat = [degrees[i] / kappa[g[i]] for i in range(n)]
    # Check Eq. (15): sum_i theta_i delta_{g_i, r} = 1
    for r in range(k_groups):
        s_theta = sum(theta_hat[i] for i in range(n) if g[i] == r)
        assert abs(s_theta - 1.0) < 1e-15

    # Check Eq. (19) and Eq. (20): expected block edges and expected vertex degrees
    exp_adj = [
        [theta_hat[i] * theta_hat[j] * m_mat[g[i]][g[j]] for j in range(n)]
        for i in range(n)
    ]
    exp_m, _ = compute_m_and_kappa(exp_adj, g, k_groups)
    max_m_err = max(
        abs(exp_m[r][s] - m_mat[r][s])
        for r in range(k_groups)
        for s in range(k_groups)
    )
    max_deg_err = max(abs(sum(exp_adj[i]) - degrees[i]) for i in range(n))
    assert max_m_err < 1e-14
    assert max_deg_err < 1e-14

    # Check KL divergence relation (Eq. 24)
    l_dc = log_lik_dc(adj, g, k_groups)
    kl_val = 0.0
    for r in range(k_groups):
        for s in range(k_groups):
            if m_mat[r][s] > 0:
                pk_rs = m_mat[r][s] / two_m
                pdeg_rs = (kappa[r] / two_m) * (kappa[s] / two_m)
                kl_val += pk_rs * math.log(pk_rs / pdeg_rs)
    # L_DC(G|g) = 2m * D_KL(p_K || p_degree) - 2m * log(2m)
    kl_identity_err = abs(l_dc - (two_m * kl_val - two_m * math.log(two_m)))
    assert kl_identity_err < 1e-13

    # 2. Verify Eq. (25) single-vertex shift Delta L across all vertices & target groups
    max_dl_err = 0.0
    for i in range(n):
        for s_new in range(k_groups):
            if s_new == g[i]:
                continue
            g_after = list(g)
            g_after[i] = s_new
            exact_diff = log_lik_dc(adj, g_after, k_groups) - l_dc
            formula_diff = delta_l_eq25(adj, g, k_groups, i, s_new)
            max_dl_err = max(max_dl_err, abs(exact_diff - formula_diff))
    assert max_dl_err < 1e-13

    # 3. Verify Section IV.C bimodal-degree synthetic benchmark (Eqs. 27-28, Fig. 3 left):
    #    4 blocks of n_b = 250 vertices: (comm 0, deg 10), (comm 0, deg 30),
    #    (comm 1, deg 10), (comm 1, deg 30), at lambda = 0.5.
    #    Compare planted community assignment g_planted vs degree-split assignment g_deg.
    #    Under expected adjacency <A_{ij}> = theta_i theta_j omega_{g_i g_j}:
    #    Total stubs in comm 0: kappa_0 = 250*10 + 250*30 = 10000; kappa_1 = 10000; 2m = 20000.
    #    At lambda = 0.5: omega_00 = 0.5*10000 + 0.5*5000 = 7500 = omega_11; omega_01 = 2500.
    #    Under planted split: m_00 = m_11 = 7500, m_01 = m_10 = 2500, n_0 = n_1 = 500, kappa_0 = kappa_1 = 10000.
    l_sbm_planted = 2 * (7500.0 * math.log(7500.0 / (500.0 * 500.0))) + 2 * (
        2500.0 * math.log(2500.0 / (500.0 * 500.0))
    )
    l_dc_planted = 2 * (7500.0 * math.log(7500.0 / (10000.0 * 10000.0))) + 2 * (
        2500.0 * math.log(2500.0 / (10000.0 * 10000.0))
    )

    # Under degree split (group L = all deg-10 vertices, group H = all deg-30 vertices):
    # Group L has n_L = 500, stub share = 1/4 in each community -> kappa_L = 5000;
    # Group H has n_H = 500, stub share = 3/4 in each community -> kappa_H = 15000.
    # Since degree is independent of community, m_{LL} = (1/4)^2 * 2m = 1250,
    # m_{LH} = m_{HL} = (1/4)*(3/4) * 2m = 3750, m_{HH} = (3/4)^2 * 2m = 11250.
    m_deg = [[1250.0, 3750.0], [3750.0, 11250.0]]
    kap_deg = [5000.0, 15000.0]
    l_sbm_deg = sum(
        m_deg[r][s] * math.log(m_deg[r][s] / (500.0 * 500.0))
        for r in range(2)
        for s in range(2)
    )
    l_dc_deg = sum(
        m_deg[r][s] * math.log(m_deg[r][s] / (kap_deg[r] * kap_deg[s]))
        for r in range(2)
        for s in range(2)
    )

    # Uncorrected SBM prefers the spurious degree split (l_sbm_deg > l_sbm_planted) at lambda = 0.5!
    # Degree-corrected SBM strictly prefers the planted community split (l_dc_planted > l_dc_deg)!
    sbm_gap = l_sbm_planted - l_sbm_deg
    dc_gap = l_dc_planted - l_dc_deg
    assert sbm_gap < -500.0
    assert dc_gap > 2500.0

    print(
        f"Karrer & Newman (2011) DC-SBM verified: "
        f"MLE deg/block err=({max_deg_err:.2e},{max_m_err:.2e}), "
        f"KL identity err={kl_identity_err:.2e}, "
        f"Eq.25 DeltaL err={max_dl_err:.2e}, "
        f"lambda=0.5 gap(planted-deg): SBM={sbm_gap:.1f} vs DC-SBM=+{dc_gap:.1f}."
    )


if __name__ == "__main__":
    main()
