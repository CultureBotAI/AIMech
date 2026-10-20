#!/usr/bin/env python3
"""Constructed boundary verification for ByRDiE (Yang & Bajwa, IEEE TSIPN 2019 / arXiv:1708.08155).

Verifies:
1. Inner-loop coordinate-wise trimmed screening (Equations 5-8): each nonfaulty node j in J'
   removes the b smallest (N_j^s) and b largest (N_j^l) neighbor values along coordinate k,
   averaging the remaining |N_j| - 2b + 1 values (including self) before stepping along -rho * grad_k f_j.
2. Exact convex-combination representation (Equations 11-13): any retained Byzantine value in N_j^*
   is bounded between at least one trimmed honest lower neighbor in N_j^s cap N_j' and one trimmed
   honest upper neighbor in N_j^l cap N_j', inducing a row-stochastic matrix Y(m) over nonfaulty nodes.
3. Consensus and convergence to the true minimizer w* on a P=3 dimensional quadratic ERM problem
   under b=1 arbitrary Byzantine node, whereas unscreened decentralized coordinate descent diverges.
"""

import math


def verify_byrdie_boundaries():
    # 5-node complete graph: 4 honest nodes (0, 1, 2, 3) and b=1 Byzantine node (4)
    M_total = 5
    honest_nodes = [0, 1, 2, 3]
    b = 1
    P = 3
    w_star = [1.5, -2.0, 0.75]

    # 1. Verify Equation (11)-(13): any retained Byzantine scalar is a convex combination of honest neighbors
    honest_vals = [1.0, 2.0, 3.0]  # 3 honest neighbors of node 0
    for byz_val in [-100.0, 1.5, 2.5, 500.0]:
        all_neighbors = honest_vals + [byz_val]  # |N_j| = 4 neighbors
        sorted_nb = sorted(all_neighbors)
        # Drop b=1 smallest and b=1 largest
        retained = sorted_nb[b : len(sorted_nb) - b]
        assert len(retained) == len(all_neighbors) - 2 * b
        # Every retained value must lie in [min(honest_vals), max(honest_vals)] = [1.0, 3.0]
        for v in retained:
            assert min(honest_vals) <= v <= max(honest_vals), f"Retained {v} escaped honest hull!"

    # 2. Run ByRDiE (Algorithm 1, T=2 inner steps per coordinate) vs unscreened DCD
    w_byrdie = [[0.0 for _ in range(P)] for _ in honest_nodes]
    w_unscreened = [[0.0 for _ in range(P)] for _ in honest_nodes]

    outer_iters = 80
    T_inner = 2
    for r in range(1, outer_iters + 1):
        for k in range(P):
            for t in range(1, T_inner + 1):
                rho = 0.35 / (1.0 + 0.04 * (r + t - 1))
                # Byzantine node broadcasts extreme adversarial value +200.0 on coordinate k
                byz_broadcast = 200.0
                next_k_byrdie = []
                next_k_unscreened = []
                for j in honest_nodes:
                    # Neighbor values for node j: the other 3 honest nodes + 1 Byzantine node
                    nb_vals = [w_byrdie[i][k] for i in honest_nodes if i != j] + [byz_broadcast]
                    nb_sorted = sorted(nb_vals)
                    screened = nb_sorted[b : len(nb_sorted) - b]
                    # Equation (8): average over screened U {j} of size |N_j| - 2b + 1 = 4 - 2 + 1 = 3
                    avg_screened = (w_byrdie[j][k] + sum(screened)) / (len(nb_vals) - 2 * b + 1)
                    grad_jk = w_byrdie[j][k] - w_star[k]
                    next_k_byrdie.append(avg_screened - rho * grad_jk)

                    # Unscreened baseline
                    nb_un = [w_unscreened[i][k] for i in honest_nodes if i != j] + [byz_broadcast]
                    avg_un = (w_unscreened[j][k] + sum(nb_un)) / (len(nb_un) + 1)
                    grad_un = w_unscreened[j][k] - w_star[k]
                    next_k_unscreened.append(avg_un - rho * grad_un)

                for idx, j in enumerate(honest_nodes):
                    w_byrdie[j][k] = next_k_byrdie[idx]
                    w_unscreened[j][k] = next_k_unscreened[idx]

    # Verify ByRDiE consensus and convergence to w_star
    max_byrdie_err = max(
        math.sqrt(sum((w_byrdie[j][k] - w_star[k]) ** 2 for k in range(P)))
        for j in honest_nodes
    )
    max_consensus_disagreement = max(
        abs(w_byrdie[i][k] - w_byrdie[j][k])
        for i in honest_nodes
        for j in honest_nodes
        for k in range(P)
    )
    min_unscreened_err = min(
        math.sqrt(sum((w_unscreened[j][k] - w_star[k]) ** 2 for k in range(P)))
        for j in honest_nodes
    )

    assert max_byrdie_err < 1e-3, f"ByRDiE failed to converge to w*: {max_byrdie_err}"
    assert max_consensus_disagreement < 1e-6, f"ByRDiE failed consensus: {max_consensus_disagreement}"
    assert min_unscreened_err > 50.0, f"Unscreened DCD should diverge under Byzantine attack: {min_unscreened_err}"

    print(
        f"[PASS] ByRDiE boundaries verified: max_err={max_byrdie_err:.2e}, "
        f"consensus_gap={max_consensus_disagreement:.2e}, unscreened_err={min_unscreened_err:.1f}"
    )


if __name__ == "__main__":
    verify_byrdie_boundaries()
