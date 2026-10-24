#!/usr/bin/env python3
"""Constructed boundary verification for Round 580: Moshpit SGD and Moshpit All-Reduce (Ryabinin et al., NeurIPS 2021)."""

from __future__ import annotations

import math
import random


def m1_exact(m: int, p: float) -> float:
    """Closed-form E[min{1/xi, 1}] for xi ~ Binom(M, p) from Lemma C.1 Eq. (20)."""
    q = 1.0 - p
    return (q**m) + sum(((q ** (m - i)) - (q**m)) / i for i in range(1, m + 1))


def m2_exact(m: int, p: float) -> float:
    """Closed-form E[min{1/xi^2, 1}] for xi ~ Binom(M, p) from Lemma C.1 Eq. (21)."""
    q = 1.0 - p
    return (q**m) + sum(
        (((q ** (m - i)) - (q**m)) / i) * sum(1.0 / j for j in range(i, m + 1))
        for i in range(1, m + 1)
    )


def main() -> None:
    # 1. Verify Theorem C.1: Exact global average in a full d-dimensional hypercube N = M^d after d rounds
    m_grid, d_grid = 4, 3
    n_peers = m_grid**d_grid  # 64 peers
    rng = random.Random(580)
    thetas_init = [rng.gauss(3.0, 5.0) for _ in range(n_peers)]
    exact_avg = sum(thetas_init) / n_peers

    # Assign initial coordinates (c_1, ..., c_{d-1}) via Eq. (2): floor(i / M^{d-1-j}) mod M
    # In round t (0 <= t < d), group peers by all coordinates except coordinate t
    thetas = list(thetas_init)
    for t in range(d_grid):
        groups: dict[tuple[int, ...], list[int]] = {}
        for i in range(n_peers):
            coords = [(i // (m_grid** axis)) % m_grid for axis in range(d_grid)]
            key = tuple(coords[axis] for axis in range(d_grid) if axis != t)
            groups.setdefault(key, []).append(i)
        assert len(groups) == m_grid ** (d_grid - 1)
        for members in groups.values():
            assert len(members) == m_grid
            g_avg = sum(thetas[idx] for idx in members) / len(members)
            for idx in members:
                thetas[idx] = g_avg

    max_err_full_grid = max(abs(th - exact_avg) for th in thetas)
    assert max_err_full_grid < 1e-14, f"Theorem C.1 failed: max_err={max_err_full_grid}"

    # 2. Verify Theorem 3.2 (Theorem C.3, Eq. 5 & 18): Exact expected distortion factor ((r - 1)/N + r/N^2)^T
    # Test with N = 6, r = 2 groups of sizes M_1 = 4, M_2 = 2 by enumerating all 6! = 720 permutations
    n_small = 6
    r_groups = 2
    sizes = [4, 2]
    vals = [1.0, -2.0, 4.0, -1.0, 3.0, -5.0]  # sum = 0, mean = 0
    init_dist = sum(v * v for v in vals) / n_small

    # Enumerate all permutations of [0..5]
    import itertools

    total_dist = 0.0
    perms = list(itertools.permutations(range(n_small)))
    for perm in perms:
        g1 = [vals[idx] for idx in perm[: sizes[0]]]
        g2 = [vals[idx] for idx in perm[sizes[0] :]]
        avg1 = sum(g1) / sizes[0]
        avg2 = sum(g2) / sizes[1]
        dist = (sizes[0] * (avg1**2) + sizes[1] * (avg2**2)) / n_small
        total_dist += dist
    emp_expected_dist = total_dist / len(perms)
    exact_perm_factor = (r_groups - 1.0) / (n_small - 1.0)
    theo_factor = (r_groups - 1.0) / n_small + r_groups / (n_small * n_small)
    theo_expected_dist = theo_factor * init_dist
    assert abs(emp_expected_dist - exact_perm_factor * init_dist) < 1e-14
    assert emp_expected_dist <= theo_expected_dist + 1e-14, (
        f"Theorem 3.2 bound failed: {emp_expected_dist} vs {theo_expected_dist}"
    )

    # 3. Verify Lemma C.1 (Equations 20-21) and Theorem C.4 bounds (p >= 2/3, M >= 11 => m1 <= 2/M, m2 <= 3/M^2)
    m_binom = 12
    p_surv = 0.75
    # Compare ODE closed-form formulas (20)-(21) against direct binomial PMF summation
    m1_direct = ((1.0 - p_surv) ** m_binom) + sum(
        math.comb(m_binom, i) * (p_surv**i) * ((1.0 - p_surv) ** (m_binom - i)) / i
        for i in range(1, m_binom + 1)
    )
    m2_direct = ((1.0 - p_surv) ** m_binom) + sum(
        math.comb(m_binom, i) * (p_surv**i) * ((1.0 - p_surv) ** (m_binom - i)) / (i * i)
        for i in range(1, m_binom + 1)
    )
    m1_ode = m1_exact(m_binom, p_surv)
    m2_ode = m2_exact(m_binom, p_surv)
    assert abs(m1_direct - m1_ode) < 1e-14
    assert abs(m2_direct - m2_ode) < 1e-14

    # Theorem C.4 inequalities for M = 12 >= 11 and p = 0.75 >= 2/3:
    assert m1_exact(m_binom - 1, p_surv) <= 2.0 / m_binom
    assert m2_exact(m_binom - 1, p_surv) <= 3.0 / (m_binom * m_binom)

    # 4. Verify Appendix G: Load balancing for Butterfly All-Reduce on heterogeneous bandwidths
    # T(w) = max_i (1 - w_i + (M - 1) w_i) / b_i = max_i (1 + (M - 2) w_i) / b_i
    bandwidths = [100.0, 200.0, 500.0, 1000.0]
    m_bw = len(bandwidths)
    w_uniform = [1.0 / m_bw] * m_bw
    t_uniform = max((1.0 + (m_bw - 2) * w_uniform[i]) / bandwidths[i] for i in range(m_bw))
    # Give w_i = 0 to slow peers and w_3 = 1.0 to the 1000 Mb/s peer (interpolating to parameter server)
    w_opt = [0.0, 0.0, 0.0, 1.0]
    t_opt = max((1.0 + (m_bw - 2) * w_opt[i]) / bandwidths[i] for i in range(m_bw))
    assert t_opt < t_uniform

    print(
        f"[PASS] Round 580 Moshpit SGD verified: full_grid_err={max_err_full_grid:.2e}, "
        f"thm3_2_factor={theo_factor:.6f}, m1={m1_ode:.4f}, m2={m2_ode:.4f}, t_opt={t_opt:.4f}<{t_uniform:.4f}"
    )


if __name__ == "__main__":
    main()
