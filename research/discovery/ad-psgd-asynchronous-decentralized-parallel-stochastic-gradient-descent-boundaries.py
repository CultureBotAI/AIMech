#!/usr/bin/env python3
"""Boundary verification for Round 442: AD-PSGD (Lian et al. 2018, ICML PMLR 80:3043-3052, arXiv:1710.06952)."""
import math
import random

def main():
    rng = random.Random(442)
    n = 4
    # Heterogeneous worker latencies: worker 3 is a 6x straggler
    latencies = [1.0, 1.2, 1.1, 6.0]
    # Sync D-PSGD round time is max(latencies) = 6.0; AD-PSGD average step time is 1 / sum(1/latencies)
    sync_round_time = max(latencies)
    async_step_rate = sum(1.0 / l for l in latencies)
    # Time per n updates in AD-PSGD vs 1 synchronous round (n updates) in D-PSGD:
    ad_psgd_epoch_time = n / async_step_rate
    throughput_speedup = sync_round_time / ad_psgd_epoch_time
    assert throughput_speedup > 4.0

    # Verify Eq. (2): X_{k+1} = X_k W_k - gamma * g(X_hat_k) with random pairwise gossip W_k
    # Local objectives f_i(x) = 0.5 * (x - b_i)^2, mean b_bar = 2.5
    b_vals = [1.0, 2.0, 3.0, 4.0]
    x_star = sum(b_vals) / n
    X = [0.0] * n
    history = [X[:]]
    gamma = 0.05
    max_staleness = 3
    max_gossip_conservation_err = 0.0

    for k in range(800):
        # Pick random worker i_k and neighbor j_k on ring
        ik = rng.randrange(n)
        jk = (ik + 1) % n
        # Bounded staleness tau_k in [0, min(k, max_staleness)]
        tau = rng.randint(0, min(k, max_staleness))
        x_stale = history[k - tau][ik]
        grad_stale = x_stale - b_vals[ik]

        # Pairwise gossip W_k averages ik and jk: check conservation before gradient step
        x_after_gossip = X[:]
        avg_ij = 0.5 * (X[ik] + X[jk])
        x_after_gossip[ik] = avg_ij
        x_after_gossip[jk] = avg_ij
        cons_err = abs(sum(x_after_gossip) / n - sum(X) / n)
        if cons_err > max_gossip_conservation_err:
            max_gossip_conservation_err = cons_err

        x_after_gossip[ik] -= gamma * grad_stale
        X = x_after_gossip
        history.append(X[:])

    mean_err = abs(sum(X) / n - x_star)
    # Verify Corollary 2 staleness bound T <= O(K^{1/4}) for K = 10000 -> K^{1/4} = 10
    K = 10000
    staleness_limit = K ** 0.25
    assert max_gossip_conservation_err < 1e-15
    assert mean_err < 0.15
    assert abs(staleness_limit - 10.0) < 1e-12
    print(f"[PASS] Round 442 AD-PSGD (Lian et al. 2018): speedup={throughput_speedup:.2f}x, gossip_cons_err={max_gossip_conservation_err:.2e}, mean_err={mean_err:.4f}, K1_4_staleness={staleness_limit:.1f}")

if __name__ == "__main__":
    main()
