#!/usr/bin/env python3
"""Constructed boundary verification for Round 489: FedRolex (Alam et al. 2022, NeurIPS 2022).

Verifies:
1. Rolling Sub-Model Extraction Scheme (Section 3.2, Eq. 4):
   For layer i with K_i nodes and client capacity beta_n in (0, 1], at round j with
   j_hat = j mod K_i, S_{n,i}^{(j)} extracts floor(beta_n K_i) contiguous circularly
   wrapped indices and visits every node index exactly m * floor(beta_n K_i) times
   over m * K_i rounds (zero frequency variance across nodes).
2. Comparison with Static Sub-Model Extraction (HeteroFL, Section 3.3.2, Eq. 6):
   Static extraction S_{n,i}^{(j)} = {0, ..., floor(beta_n K_i) - 1} never trains node
   indices >= max_n floor(beta_n K_i) when all clients have beta_n < 1 (cannot train a
   server model larger than the largest client model) and leaves higher-index nodes
   untrained on low-capacity client distributions.
3. Coupon-Collector / Dixie-Cup Statistical Analysis vs Random Extraction (Federated Dropout,
   Section 3.3.1 & Appendix A.1, Lemmas 1-2):
   Expected rounds to cover I sub-models at least once is E[N_1] = I * H_I =
   I * int_0^inf (1 - (1 - e^{-t})^I) dt > I, and for m >= 2 is
   E[N_m] = I * int_0^inf (1 - (1 - S_m(t) e^{-t})^I) dt > m * I.
4. Selective Server Aggregation (Appendix A.2, Eq. 10):
   Aggregates each global parameter [i, k] exclusively over active clients M_k whose
   rolling window S_{m,i}^{(j)} contains k, preserving unchanged parameters when M_k = empty.
"""

import math


def fedrolex_extract(j, K_i, beta_n):
    """Equation (4) rolling window extraction for layer of size K_i at round j."""
    j_hat = j % K_i
    width = int(math.floor(beta_n * K_i))
    if j_hat + width <= K_i:
        return list(range(j_hat, j_hat + width))
    else:
        return list(range(j_hat, K_i)) + list(range(0, j_hat + width - K_i))


def heterofl_extract(K_i, beta_n):
    """Equation (6) static sub-model extraction."""
    width = int(math.floor(beta_n * K_i))
    return list(range(0, width))


def selective_aggregate(global_layer, client_submodels, client_indices, client_weights):
    """Equation (10) selective parameter aggregation for a layer."""
    K_i = len(global_layer)
    updated = list(global_layer)
    for k in range(K_i):
        num = 0.0
        den = 0.0
        for m_idx, indices in enumerate(client_indices):
            if k in indices:
                pos = indices.index(k)
                w_m = client_weights[m_idx]
                num += w_m * client_submodels[m_idx][pos]
                den += w_m
        if den > 0.0:
            updated[k] = num / den
    return updated


def verify_fedrolex_boundaries():
    K_i = 8
    m_cycles = 3
    total_rounds = m_cycles * K_i

    # 1. Verify Eq. (4) exact circular cardinality and uniform node coverage even when max(beta_n) < 1
    betas = [0.5, 0.25]  # Largest client model is only 1/2 of global server model (gamma = 2)
    counts_rolex = [0] * K_i
    counts_static = [0] * K_i

    for j in range(total_rounds):
        for beta_n in betas:
            idx_r = fedrolex_extract(j, K_i, beta_n)
            assert len(idx_r) == int(math.floor(beta_n * K_i))
            assert len(set(idx_r)) == len(idx_r)
            for k in idx_r:
                counts_rolex[k] += 1

            idx_s = heterofl_extract(K_i, beta_n)
            for k in idx_s:
                counts_static[k] += 1

    expected_per_node = m_cycles * sum(int(math.floor(b * K_i)) for b in betas)
    assert all(c == expected_per_node for c in counts_rolex), (
        f"FedRolex failed uniform coverage: {counts_rolex} vs {expected_per_node}"
    )
    # Static extraction leaves nodes 4..7 completely untrained (0 updates) when max(beta_n)=0.5
    assert counts_static[4:] == [0, 0, 0, 0], f"Static extraction should leave upper half untouched: {counts_static}"

    # 2. Verify Lemma 1 & Lemma 2 (Appendix A.1) integral identities vs deterministic m * I
    I = 8
    harmonic_sum = I * sum(1.0 / i for i in range(1, I + 1))

    # Numerical quadrature of I * int_0^inf (1 - (1 - e^{-t})^I) dt
    dt = 0.002
    steps = 15000
    integral_m1 = I * sum(
        0.5 * ((1.0 - (1.0 - math.exp(-t * dt)) ** I) + (1.0 - (1.0 - math.exp(-(t + 1) * dt)) ** I)) * dt
        for t in range(steps)
    )
    assert abs(harmonic_sum - integral_m1) < 1e-4, f"Lemma 1 integral mismatch: {harmonic_sum} vs {integral_m1}"
    assert harmonic_sum > I, f"Random coupon collector E[N_1]={harmonic_sum} must exceed FedRolex I={I}"

    # Lemma 2 for m = 2: S_2(t) = 1 + t
    m = 2
    integral_m2 = I * sum(
        0.5
        * (
            (1.0 - (1.0 - (1.0 + t * dt) * math.exp(-t * dt)) ** I)
            + (1.0 - (1.0 - (1.0 + (t + 1) * dt) * math.exp(-(t + 1) * dt)) ** I)
        )
        * dt
        for t in range(steps)
    )
    assert integral_m2 > m * I, f"Lemma 2 E[N_2]={integral_m2} must exceed FedRolex m*I={m * I}"

    # 3. Verify Selective Aggregation (Appendix A.2, Eq. 10)
    # Example from Section 3.2 (Figure 1, K_i = 5 nodes {0,1,2,3,4} = {a,b,c,d,e}):
    # Client 1 (large, 4 nodes) updates {0,1,2,3} to [10, 20, 30, 40]
    # Client 2 (small, 3 nodes) updates {2,3,4} to [50, 60, 70]
    global_init = [1.0, 2.0, 3.0, 4.0, 5.0]
    agg = selective_aggregate(
        global_init,
        client_submodels=[[10.0, 20.0, 30.0, 40.0], [50.0, 60.0, 70.0]],
        client_indices=[[0, 1, 2, 3], [2, 3, 4]],
        client_weights=[0.5, 0.5],
    )
    # Nodes 0,1 come from Client 1 only; nodes 2,3 average Client 1 & 2; node 4 from Client 2 only
    expected_agg = [10.0, 20.0, 40.0, 50.0, 70.0]
    assert all(abs(a - b) < 1e-12 for a, b in zip(agg, expected_agg)), f"Selective agg mismatch: {agg}"

    print(
        f"[PASS] Round 489 FedRolex (Alam et al. 2022): uniform_node_visits={counts_rolex[0]} "
        f"(var=0 vs static_upper={counts_static[4:]}), Lemma1_E[N]={harmonic_sum:.2f} > I={I}, "
        f"Lemma2_E[N]={integral_m2:.2f} > m*I={m*I}, selective_agg_err=0.0"
    )


if __name__ == "__main__":
    verify_fedrolex_boundaries()
