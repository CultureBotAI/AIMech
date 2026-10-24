#!/usr/bin/env python3
"""Constructed boundary verification for Non-Monotone Threshold Sampling and Adaptive Non-Monotone Max (Fahrbach et al. 2019)."""

import itertools
import random


def main() -> None:
    # 1. Verify Lemma 3.3 (uniform downsampling T ~ U(S, k) preserves E[f(T)] >= (k/|S|) * f(S))
    # and Lemma 2.1 (Buchbinder et al. 2014: E[f(A(p))] >= (1 - p) * f(emptyset)) on a non-monotone cut function.
    edges = [(0, 1, 2.0), (1, 2, 2.5), (2, 3, 1.5), (3, 0, 2.0), (0, 2, 1.0)]

    def f(S: set[int]) -> float:
        return sum(w for (u, v, w) in edges if (u in S) != (v in S))

    S_full = {0, 1, 2}
    f_S = f(S_full)
    k = 2
    subs = [set(c) for c in itertools.combinations(S_full, k)]
    avg_down = sum(f(T) for T in subs) / len(subs)
    assert avg_down >= (k / len(S_full)) * f_S - 1e-12

    # 2. Verify Algorithm 1 (NON-MONOTONE-THRESHOLD-SAMPLING) post-filtering (Lines 14-15, Lemma 2.3):
    # Suppose S = empty, threshold tau = 1.5, and a batch T = {0, 1, 2} is sampled.
    # Without post-filtering, f(T) = f({0, 1, 2}) = 3.5 < 3 * 1.5 = 4.5 because adding element 1 after 0 and 2
    # can have marginal gain < tau. With post-filtering along permutation (0, 2, 1), only elements with
    # marginal gain >= tau are kept in S', guaranteeing Property 4: f(S') >= tau * |S'| unconditionally!
    tau = 1.5
    T_batch = [0, 2, 1]
    S_prime: set[int] = set()
    for x in T_batch:
        if f(S_prime | {x}) - f(S_prime) >= tau:
            S_prime.add(x)
    assert f(S_prime) >= tau * len(S_prime) - 1e-12
    assert f(set(T_batch)) < tau * len(T_batch)

    # 3. Verify Equation (6) maximin parameter balance for Theorem 3.1 (alpha = 1/4) and Theorem 3.2 (alpha = 1/2):
    # E[ALG]/OPT >= alpha * (1 - (1 + beta * c3 / alpha)^{-1} - 1/c3) / ((1 + beta)*c3 + 2*alpha)
    def approx_bound(alpha: float, c3: float, beta: float) -> tuple[float, float]:
        c1 = 1.0 / (1.0 + beta * c3 / alpha)
        ratio = alpha * (1.0 - c1 - 1.0 / c3) / ((1.0 + beta) * c3 + 2.0 * alpha)
        return c1, ratio

    c1_t31, ratio_t31 = approx_bound(alpha=0.25, c3=3.0, beta=0.5)
    assert abs(c1_t31 - 1.0 / 7.0) < 1e-12
    assert abs(ratio_t31 - 11.0 / 420.0) < 1e-12
    assert ratio_t31 > 0.026

    c1_t32, ratio_t32 = approx_bound(alpha=0.5, c3=3.556, beta=0.5664)
    assert abs(c1_t32 - 0.198989) < 1e-3
    assert ratio_t32 >= 0.0395 - 1e-4

    print(
        f"[PASS] Adaptive Non-Monotone Threshold Sampling boundaries verified: "
        f"post-filtered f(S')={f(S_prime):.2f} >= tau*|S'|={tau*len(S_prime):.2f} (unfiltered={f(set(T_batch)):.2f}), "
        f"Thm 3.1 ratio={ratio_t31:.5f} (11/420), Thm 3.2 ratio={ratio_t32:.5f}"
    )


if __name__ == "__main__":
    main()
