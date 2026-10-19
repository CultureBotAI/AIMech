#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 350:
Sieve-Streaming and Sieve-Streaming++ for Single-Pass Monotone Submodular Maximization
(Badanidiyuru et al., 2014, KDD; Kazemi et al., 2019, ICML / PMLR 97:3311-3320).
"""

import math
import random


def make_facility_location_stream(n=60, m=15, seed=350):
    rng = random.Random(seed)
    # Benefit matrix M in R_{>=0}^{n x m}: f(S) = sum_{j=1}^m max_{i in S} M[i][j]
    # Include both low-value and high-value items so dynamic LB grows over the stream
    M = []
    for i in range(n):
        scale = 1.0 + (i / 10.0)
        row = [scale * rng.uniform(0.1, 1.0) for _ in range(m)]
        M.append(row)

    def f(S):
        if not S:
            return 0.0
        return sum(max(M[i][j] for i in S) for j in range(m))

    def marginal(e, S):
        if not S:
            return sum(M[e])
        return sum(max(0.0, M[e][j] - max(M[i][j] for i in S)) for j in range(m))

    return n, f, marginal


def run_sieve_streaming(n, f, marginal, k, eps):
    """Original Sieve-Streaming (Badanidiyuru et al. 2014):
    Active thresholds in [Delta / (2k), 2 * Delta] where Delta = max_{e seen} f({e}).
    """
    Delta = 0.0
    sieves = {}
    max_total_elements = 0
    for e in range(n):
        fe = marginal(e, [])
        Delta = max(Delta, fe)
        tau_min = Delta / (2.0 * k)
        tau_max = 2.0 * Delta
        # Prune out-of-range sieves
        for idx in list(sieves.keys()):
            tau = (1.0 + eps) ** idx
            if tau < tau_min or tau > tau_max:
                del sieves[idx]
        idx_min = math.ceil(math.log(tau_min) / math.log(1.0 + eps))
        idx_max = math.floor(math.log(tau_max) / math.log(1.0 + eps))
        for idx in range(idx_min, idx_max + 1):
            tau = (1.0 + eps) ** idx
            if idx not in sieves:
                sieves[idx] = []
            S_tau = sieves[idx]
            if len(S_tau) < k:
                # Badanidiyuru et al. threshold rule: (tau / 2 - f(S_tau)) / (k - |S_tau|) or constant tau
                # In Kazemi et al. (2019) Section 3 / Algorithm 1, constant marginal gain >= tau is used
                if marginal(e, S_tau) >= tau:
                    S_tau.append(e)
        total_elems = sum(len(s) for s in sieves.values())
        max_total_elements = max(max_total_elements, total_elems)
    best_S = max(sieves.values(), key=f)
    return f(best_S), max_total_elements, len(sieves)


def run_sieve_streaming_pp(n, f, marginal, k, eps):
    """Sieve-Streaming++ (Kazemi et al. 2019, Algorithm 1):
    Uses dynamic lower bound LB = max_{tau} f(S_tau) and prunes tau < max(LB, Delta) / (2k).
    """
    Delta = 0.0
    LB = 0.0
    sieves = {}
    max_total_elements = 0
    for e in range(n):
        fe = marginal(e, [])
        Delta = max(Delta, fe)
        tau_min = max(LB, Delta) / (2.0 * k)
        # Line 5: Discard all sets S_tau with tau < tau_min
        for idx in list(sieves.keys()):
            tau = (1.0 + eps) ** idx
            if tau < tau_min:
                del sieves[idx]
        idx_min = math.ceil(math.log(tau_min / (1.0 + eps)) / math.log(1.0 + eps))
        idx_max = math.floor(math.log(Delta) / math.log(1.0 + eps))
        for idx in range(idx_min, idx_max + 1):
            tau = (1.0 + eps) ** idx
            if idx not in sieves:
                sieves[idx] = []
            S_tau = sieves[idx]
            if len(S_tau) < k and marginal(e, S_tau) >= tau:
                S_tau.append(e)
                LB = max(LB, f(S_tau))
        # Verify geometric size bound |S_tau| <= LB / tau for all active sieves with non-empty S_tau
        for idx, S_tau in sieves.items():
            if S_tau:
                tau = (1.0 + eps) ** idx
                assert len(S_tau) <= LB / tau + 1e-9
        total_elems = sum(len(s) for s in sieves.values())
        max_total_elements = max(max_total_elements, total_elems)
    best_S = max(sieves.values(), key=f)
    return f(best_S), max_total_elements, len(sieves)


def main():
    n, f, marginal = make_facility_location_stream(n=60, m=15, seed=350)
    k = 8
    eps = 0.1

    # Compute offline greedy benchmark (which achieves >= (1 - 1/e) OPT, and upper bound OPT via top-k marginal gains)
    S_greedy = []
    for _ in range(k):
        best_e = max((e for e in range(n) if e not in S_greedy), key=lambda e: marginal(e, S_greedy))
        S_greedy.append(best_e)
    val_greedy = f(S_greedy)
    # Upper bound on OPT via submodularity: OPT <= f(S_greedy) + sum_{top k in V \ S_greedy} f(e | S_greedy)
    rem_gains = sorted([marginal(e, S_greedy) for e in range(n) if e not in S_greedy], reverse=True)
    opt_upper = val_greedy + sum(rem_gains[:k])

    val_ss, mem_ss, _ = run_sieve_streaming(n, f, marginal, k, eps)
    val_sspp, mem_sspp, _ = run_sieve_streaming_pp(n, f, marginal, k, eps)

    # 1. Verify Theorem 1 approximation guarantee: f(S) >= (1/2 - eps) * OPT
    assert val_sspp >= (0.5 - eps) * opt_upper, f"Approximation guarantee failed: {val_sspp} vs {opt_upper}"
    # 2. Verify Sieve-Streaming++ achieves identical utility to Sieve-Streaming while using strictly less memory
    assert abs(val_ss - val_sspp) < 1e-9, f"Utilities differed: {val_ss} vs {val_sspp}"
    assert mem_sspp < mem_ss, f"Expected Sieve-Streaming++ memory ({mem_sspp}) < Sieve-Streaming ({mem_ss})"

    print(
        f"[PASS] Round 350 Sieve-Streaming & Sieve-Streaming++ (Badanidiyuru et al. 2014; Kazemi et al. 2019): "
        f"val_ss={val_ss:.4f}, val_sspp={val_sspp:.4f} >= (1/2-eps)*OPT_ub={(0.5-eps)*opt_upper:.4f}, "
        f"mem_ss={mem_ss} -> mem_sspp={mem_sspp} ({100*(1-mem_sspp/mem_ss):.1f}% reduction)"
    )


if __name__ == "__main__":
    main()
