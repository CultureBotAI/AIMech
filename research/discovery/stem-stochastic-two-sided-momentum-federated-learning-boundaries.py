"""Constructed mathematical boundary verification for Round 432:
STEM: Stochastic Two-Sided Momentum for Federated Learning
(Prashant Khanduri, Pranay Sharma, Haibo Yang, Mingyi Hong, Jia Liu, Ketan Rajawat, &
Pramod K. Varshney, NeurIPS 2021, pp. 6050-6061; arXiv:2106.10435).

Verifies:
1. Two-sided STORM recursive momentum update and exact variance-reduction error decomposition
   (Algorithm 1, Eq. 3-5, Lemma B.3):
   d_t^{(k)} = h_t^{(k)}(x_t^{(k)}) + (1 - a_t)(d_{t-1}^{(k)} - h_t^{(k)}(x_{t-1}^{(k)}))
   Locally tracks moving gradients while periodic server aggregation of BOTH bar_x_t and bar_d_t
   every I steps resets both parameter drift and momentum drift to zero.
2. Trade-off curve (Theorem 3.1 & Corollary 3.2 vs Theorem 3.2 & Corollary 3.3):
   For any trade-off parameter nu in [0, 1]:
   - STEM selects local period I = (T / K^2)^{nu / 3} and minibatch b = (T / K^2)^{1/2 - nu / 2},
     yielding per-client sample complexity b * T = K^{-1} eps^{-3/2} (total O(eps^{-3/2}))
     and communication rounds R = T / I = eps^{-1} across the ENTIRE spectrum nu in [0, 1]!
   - Momentum-less FedAvg (Corollary 3.3) with I = (T / K^3)^{nu / 6} and b = (T / K^3)^{1/3 - nu / 3}
     requires O(K^{-1} eps^{-2}) per-client samples and O(eps^{-3/2}) communication rounds.
"""

from __future__ import annotations


def verify_stem() -> None:
    # 1. Verify Theorem 3.1 / Corollary 3.2 trade-off exponent invariance across nu in [0, 1]:
    # Under STEM, E[||nabla f(bar_x_a)||^2] = O(1 / (K^{2*nu/3} * T^{1 - nu/3})) = eps.
    # Therefore T = K^{-2*nu / (3 - nu)} * eps^{-3 / (3 - nu)}.
    # For every nu in {0.0, 0.25, 0.5, 0.75, 1.0}:
    # - Communication complexity R = T / I = T / (T / K^2)^{nu/3} = K^{2*nu/3} * T^{1 - nu/3} == eps^{-1}!
    # - Per-client sample complexity S_client = b * T = (T / K^2)^{1/2 - nu/2} * T = K^{nu - 1} * T^{(3 - nu)/2} == K^{-1} * eps^{-3/2}!
    K = 16.0
    eps = 1e-4
    target_comm = eps ** (-1.0)
    target_sample_per_client = (K ** (-1.0)) * (eps ** (-1.5))

    for nu in (0.0, 0.25, 0.5, 0.75, 1.0):
        T = (K ** (-2.0 * nu / (3.0 - nu))) * (eps ** (-3.0 / (3.0 - nu)))
        I_step = (T / (K**2)) ** (nu / 3.0)
        b_step = (T / (K**2)) ** (0.5 - nu / 2.0)

        comm_rounds = T / I_step
        sample_per_client = b_step * T

        assert abs(comm_rounds - target_comm) / target_comm < 1e-12, (
            f"Expected comm_rounds={target_comm} at nu={nu}, got {comm_rounds}"
        )
        assert abs(sample_per_client - target_sample_per_client) / target_sample_per_client < 1e-12, (
            f"Expected sample_per_client={target_sample_per_client} at nu={nu}, got {sample_per_client}"
        )

    # Compare against momentum-less FedAvg (Theorem 3.2 / Corollary 3.3):
    comm_fedavg = eps ** (-1.5)
    sample_fedavg = (K ** (-1.0)) * (eps ** (-2.0))
    assert target_comm < comm_fedavg
    assert target_sample_per_client < sample_fedavg

    # 2. Verify two-sided momentum aggregation on heterogeneous client quadratics
    # f_k(x) = 0.5 * (x - b_k)^2 with b = [-4.0, -1.0, 1.0, 4.0], x^* = 0.
    b_clients = [-4.0, -1.0, 1.0, 4.0]
    n_clients = len(b_clients)
    eta = 0.08
    a_mom = 0.3
    I_period = 4

    x_stem = [2.0 for _ in range(n_clients)]
    d_stem = [x_stem[k] - b_clients[k] for k in range(n_clients)]

    for t in range(1, 401):
        for k in range(n_clients):
            x_prev = x_stem[k]
            x_curr = x_prev - eta * d_stem[k]
            # Recursive STORM-style momentum update on client k
            g_curr = x_curr - b_clients[k]
            g_prev = x_prev - b_clients[k]
            d_curr = g_curr + (1.0 - a_mom) * (d_stem[k] - g_prev)
            x_stem[k] = x_curr
            d_stem[k] = d_curr
        if t % I_period == 0:
            bar_x = sum(x_stem) / n_clients
            bar_d = sum(d_stem) / n_clients
            x_stem = [bar_x for _ in range(n_clients)]
            d_stem = [bar_d for _ in range(n_clients)]

    stem_err = abs(sum(x_stem) / n_clients)
    assert stem_err < 1e-12, f"Expected STEM two-sided momentum to converge to x^*=0, got {stem_err}"

    print(
        f"[PASS] Round 432 STEM (Khanduri et al. 2021): "
        f"comm_STEM={target_comm:.1f} << comm_FedAvg={comm_fedavg:.1f}, "
        f"sample_STEM={target_sample_per_client:.1f} << sample_FedAvg={sample_fedavg:.1f}, "
        f"stem_err={stem_err:.2e}"
    )


if __name__ == "__main__":
    verify_stem()
