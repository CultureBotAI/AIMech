#!/usr/bin/env python3
"""Constructed boundary verification for Round 579: Rennala SGD & Malenia SGD (Tyurin & Richtarik, NeurIPS 2023)."""

from __future__ import annotations

import math


def lemma_d7_bounds(taus: list[float], s_batch: float) -> tuple[float, float, int, int]:
    """Verify Lemma D.7: t_1 <= t_2 <= 6 * t_1 for any sorted 0 < tau_1 <= ... <= tau_n and S >= 1/4."""
    n = len(taus)
    assert s_batch >= 0.25
    j1_star = n
    for m in range(1, n):
        inv_sum = sum(1.0 / taus[i] for i in range(m))
        if s_batch / inv_sum < taus[m]:
            j1_star = m
            break
    t1 = s_batch / sum(1.0 / taus[i] for i in range(j1_star))
    candidates = [
        (s_batch + (j + 1)) / sum(1.0 / taus[i] for i in range(j + 1))
        for j in range(n)
    ]
    t2 = min(candidates)
    j2_star = candidates.index(t2) + 1
    assert t1 <= t2 + 1e-12 and t2 <= 6.0 * t1 + 1e-12
    return t1, t2, j1_star, j2_star


def simulate_rennala_batch_collection(taus: list[float], s_batch: int) -> tuple[float, list[int]]:
    """Simulate exact wall-clock time for Method 4 (Rennala SGD) to collect S fresh gradients at iterate k."""
    # Multi-set of completion times {j * tau_i | j >= 1, i in [n]} (Definition D.4)
    events: list[tuple[float, int]] = []
    max_t = taus[0] * s_batch
    for i, tau in enumerate(taus):
        j = 1
        while j * tau <= max_t:
            events.append((j * tau, i))
            j += 1
    events.sort()
    chosen = events[:s_batch]
    completion_time = chosen[-1][0]
    counts = [0] * len(taus)
    for _, worker_idx in chosen:
        counts[worker_idx] += 1
    return completion_time, counts


def main() -> None:
    # 1. Verify Lemma D.7 and automatic straggler exclusion in Rennala SGD (Theorem 7.5)
    # Suppose n = 8 workers where workers 1..4 are fast (tau = 1, 2, 3, 4) and workers 5..8 are extreme stragglers.
    taus = [1.0, 2.0, 3.0, 4.0, 50.0, 100.0, 500.0, 2000.0]
    s_batch = 12
    t1, t2, j1_star, j2_star = lemma_d7_bounds(taus, float(s_batch))
    assert j1_star <= 4 and j2_star <= 4, f"Expected stragglers i>4 to be excluded: j1*={j1_star}, j2*={j2_star}"

    sim_t, counts = simulate_rennala_batch_collection(taus, s_batch)
    assert sum(counts) == s_batch
    # Verify that workers 5..8 (indices 4..7) contributed 0 gradients and were automatically ignored!
    assert sum(counts[4:]) == 0, f"Stragglers should be ignored by Rennala SGD: {counts}"
    assert sim_t <= t2

    # 2. Compare wall-clock complexity factors in the low-noise/large-worker regime sigma^2/eps <= p < n (Section 6, p. 7; Table 1)
    L, delta, sigma_sq, eps = 2.0, 1.0, 0.1, 0.5
    n = len(taus)
    t_minibatch = taus[-1] * (L * delta / eps + (sigma_sq * L * delta) / (n * eps * eps))
    t_async = (1.0 / (sum(1.0 / t for t in taus) / n)) * (
        L * delta / eps + (sigma_sq * L * delta) / (n * eps * eps)
    )
    t_rennala = min(
        (1.0 / (sum(1.0 / taus[i] for i in range(m)) / m))
        * (L * delta / eps + (sigma_sq * L * delta) / (m * eps * eps))
        for m in range(1, n + 1)
    )
    assert t_rennala < 0.35 * t_async and t_rennala < 0.01 * t_minibatch

    # 3. Verify Malenia SGD (Method 6, Theorems A.3 & A.4) in the heterogeneous regime
    # Construct feasible batch counts B_i from Theorem A.4 proof (Equation 35):
    s_het = max(math.ceil(sigma_sq / eps), n)
    tau_avg = sum(taus) / n
    t_prime = 2.0 * (taus[-1] + tau_avg * (s_het / n))
    b_real = [t_prime / tau - 1.0 for tau in taus]
    assert all(b >= 1.0 - 1e-12 for b in b_real)
    b_int = [math.ceil(b) for b in b_real]

    # Harmonic mean condition: ((1/n) sum_{i=1}^n (1/B_i))^{-1} >= S / n
    harm_b = 1.0 / (sum(1.0 / bi for bi in b_int) / n)
    assert harm_b >= (s_het / n) - 1e-12

    # Variance bound of Malenia SGD estimator (Proof of Theorem A.3, p. 40):
    # Var(g^k) <= (1/n^2) sum_{i=1}^n (sigma^2 / B_i) <= sigma^2 / S
    var_malenia = sum(sigma_sq / bi for bi in b_int) / (n * n)
    assert var_malenia <= (sigma_sq / s_het) + 1e-12

    print(
        f"[PASS] Round 579 Rennala & Malenia SGD verified: t_rennala={t_rennala:.2f} < t_async={t_async:.2f} "
        f"<< t_mb={t_minibatch:.2f}, counts={counts}, harm_B={harm_b:.2f}>={s_het/n:.2f}"
    )


if __name__ == "__main__":
    main()
