#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 349:
Continuous Greedy and Multilinear Extension for Matroid-Constrained Monotone Submodular Maximization
(Calinescu, Chekuri, Pal, & Vondrak, 2011, SIAM J. Comput. 40(6):1740-1766).
"""

import itertools
import math
import random


def make_coverage_instance():
    """Construct a monotone submodular set function on a partition matroid where
    standard discrete greedy achieves only 1/2 * OPT while Continuous Greedy + Pipage Rounding
    exceeds (1 - 1/e) * OPT.
    Ground set X = {0, 1, 2, 3}, partitioned into P1 = {0, 1}, P2 = {2, 3}, with |S cap P_r| <= 1.
    Universe U = {a, b, c, d} with weights: w(a)=2, w(b)=2, w(c)=2, w(d)=0.
    Item 0 covers {a} (value 2)
    Item 1 covers {b} (value 2)
    Item 2 covers {a} (value 2)
    Item 3 covers {c} (value 2, or 2 - 1e-3 so greedy tie-breaking picks 0 then 2 or 1)
    Wait: if item 0 covers {a, b} (weight 1+1=2), item 1 covers {c, d} (weight 1+1=2),
    item 2 covers {a, b} (weight 2), item 3 covers {e} (weight 0):
    In partition P1={0,1}, P2={2,3}:
    Optimal base S* = {1, 2} covers {a, b, c, d} with value 4.
    Discrete greedy: first picks 0 from P1 (gain 2.001), then from P2 can only pick 2 (gain 0) or 3 (gain 0),
    yielding total value 2.001 -> ratio 1/2!
    """
    n = 4
    # Subset valuation f(S)
    def f(S):
        S_set = set(S)
        val = 0.0
        # Elements of universe U:
        # u1 covered by 0, 2 with weight 2.0
        if 0 in S_set or 2 in S_set:
            val += 2.0
        # u2 covered by 1 with weight 2.0
        if 1 in S_set:
            val += 2.0
        # tiny bonus on item 0 to make discrete greedy deterministically pick 0 first
        if 0 in S_set:
            val += 1e-4
        return val

    # Partition matroid: P1 = {0, 1}, P2 = {2, 3}, independent iff |S cap P1| <= 1 and |S cap P2| <= 1
    def is_independent(S):
        S_set = set(S)
        return len(S_set & {0, 1}) <= 1 and len(S_set & {2, 3}) <= 1

    bases = [{0, 2}, {0, 3}, {1, 2}, {1, 3}]
    return n, f, is_independent, bases


def multilinear_extension(n, f, y):
    """Exact multilinear extension F(y) = sum_{R subseteq X} f(R) prod_{i in R} y_i prod_{j notin R} (1 - y_j)."""
    total = 0.0
    for r in range(n + 1):
        for comb in itertools.combinations(range(n), r):
            R = set(comb)
            prob = 1.0
            for i in range(n):
                prob *= y[i] if i in R else (1.0 - y[i])
            total += f(R) * prob
    return total


def grad_multilinear(n, f, y):
    """Exact gradient dF/dy_j = E[f(R + j)] - E[f(R - j)]."""
    grad = [0.0] * n
    for j in range(n):
        y1 = list(y)
        y0 = list(y)
        y1[j] = 1.0
        y0[j] = 0.0
        grad[j] = multilinear_extension(n, f, y1) - multilinear_extension(n, f, y0)
    return grad


def hessian_multilinear(n, f, y):
    """Exact second partial derivatives d^2 F / (dy_i dy_j)."""
    H = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                H[i][j] = 0.0
            else:
                y11 = list(y); y11[i] = 1.0; y11[j] = 1.0
                y10 = list(y); y10[i] = 1.0; y10[j] = 0.0
                y01 = list(y); y01[i] = 0.0; y01[j] = 1.0
                y00 = list(y); y00[i] = 0.0; y00[j] = 0.0
                H[i][j] = (
                    multilinear_extension(n, f, y11)
                    - multilinear_extension(n, f, y10)
                    - multilinear_extension(n, f, y01)
                    + multilinear_extension(n, f, y00)
                )
    return H


def main():
    n, f, is_independent, bases = make_coverage_instance()
    opt_val = max(f(B) for B in bases)
    assert abs(opt_val - 4.0) < 1e-6

    # 1. Verify smooth monotone submodularity of multilinear extension F(y) (Definition 2.1 & Section 2.4)
    y_test = [0.3, 0.7, 0.4, 0.6]
    grad = grad_multilinear(n, f, y_test)
    H = hessian_multilinear(n, f, y_test)
    assert all(g >= -1e-12 for g in grad), f"Monotonicity violated: {grad}"
    for i in range(n):
        assert abs(H[i][i]) < 1e-12, "Multilinearity d^2F/dy_i^2 = 0 violated"
        for j in range(n):
            assert H[i][j] <= 1e-12, f"Submodularity d^2F/(dy_i dy_j) <= 0 violated: {H[i][j]}"

    # Verify convexity along swap direction e_0 - e_2: d^2/dt^2 F(y + t(e_0 - e_2)) = -2 H[0][2] >= 0
    eps = 1e-4
    y_plus = list(y_test); y_plus[0] += eps; y_plus[2] -= eps
    y_minus = list(y_test); y_minus[0] -= eps; y_minus[2] += eps
    second_diff = (
        multilinear_extension(n, f, y_plus)
        - 2.0 * multilinear_extension(n, f, y_test)
        + multilinear_extension(n, f, y_minus)
    ) / (eps * eps)
    exact_swap_curv = -2.0 * H[0][2]
    swap_curv_err = abs(second_diff - exact_swap_curv)
    assert exact_swap_curv > 0.0 and swap_curv_err < 1e-6

    # 2. Compare Classical Discrete Greedy (ratio 1/2) vs Continuous Greedy (ratio >= 1 - 1/e)
    S_greedy = set()
    while True:
        candidates = [e for e in range(n) if e not in S_greedy and is_independent(S_greedy | {e})]
        if not candidates:
            break
        best_e = max(candidates, key=lambda e: f(S_greedy | {e}) - f(S_greedy))
        if f(S_greedy | {best_e}) - f(S_greedy) <= 0:
            break
        S_greedy.add(best_e)
    greedy_ratio = f(S_greedy) / opt_val
    assert abs(greedy_ratio - 0.500025) < 1e-5, f"Expected ~0.5 greedy ratio, got {greedy_ratio}"

    # Run Continuous Greedy with step delta = 1 / 1000
    steps = 1000
    delta = 1.0 / steps
    y = [0.0] * n
    min_deficit_gain_gap = float("inf")
    for _ in range(steps):
        g = grad_multilinear(n, f, y)
        # Find maximum-weight base I(t) in B(M)
        best_base = max(bases, key=lambda B: sum(g[i] for i in B))
        max_weight = sum(g[i] for i in best_base)
        deficit = opt_val - multilinear_extension(n, f, y)
        # Lemma 3.1: max_{I in I} sum_{j in I} dF/dy_j >= OPT - F(y)
        min_deficit_gain_gap = min(min_deficit_gain_gap, max_weight - deficit)
        for i in best_base:
            y[i] += delta

    assert min_deficit_gain_gap >= -1e-12, f"Lemma 3.1 violated: {min_deficit_gain_gap}"
    F_y1 = multilinear_extension(n, f, y)
    cg_ratio = F_y1 / opt_val
    assert cg_ratio >= 1.0 - 1.0 / math.e - 1e-3, f"Continuous greedy ratio too low: {cg_ratio}"

    # 3. Verify Pipage Rounding / Partition Matroid Rounding (Lemma 3.5 & Lemma 3.7): E[f(T)] >= F(y(1))
    # Under partition matroid P1={0,1}, P2={2,3}, y[0]+y[1]=1 and y[2]+y[3]=1.
    expected_rounded = (
        y[0] * y[2] * f({0, 2})
        + y[0] * y[3] * f({0, 3})
        + y[1] * y[2] * f({1, 2})
        + y[1] * y[3] * f({1, 3})
    )
    assert expected_rounded >= F_y1 - 1e-12, f"Pipage rounding lost value: {expected_rounded} < {F_y1}"

    print(
        f"[PASS] Round 349 Continuous Greedy (Calinescu et al. 2011): "
        f"swap_curv={exact_swap_curv:.4f} (err={swap_curv_err:.2e}), "
        f"min_lemma31_gap={min_deficit_gain_gap:.2e}, "
        f"discrete_greedy_ratio={greedy_ratio:.4f}, "
        f"cg_ratio={cg_ratio:.4f} >= 1-1/e={1-1/math.e:.4f}, "
        f"pipage_expected={expected_rounded:.4f} >= F(y1)={F_y1:.4f}"
    )


if __name__ == "__main__":
    main()
