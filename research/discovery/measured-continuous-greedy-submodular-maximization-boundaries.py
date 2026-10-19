#!/usr/bin/env python3
"""Constructed boundary verification for Measured Continuous Greedy (Feldman, Naor, & Schwartz 2011)."""

import math


def make_nonmonotone_matroid_instance():
    # Ground set N = {0, 1, 2, 3}, uniform matroid of rank k = 2.
    # Element 0 has high standalone value but strongly penalizes co-occurrence with 1,
    # whereas {2, 3} is the optimal independent set of size 2.
    # Let's construct a directed cut function on 4 vertices + sink that is non-monotone submodular.
    edges = [
        (0, 1, 1.8),
        (0, 2, 1.8),
        (0, 3, 1.8),
        (2, 0, 1.6),
        (2, 1, 1.6),
        (3, 0, 1.6),
        (3, 1, 1.6),
    ]
    n = 4

    def f(S: set[int]) -> float:
        return sum(w for (u, v, w) in edges if u in S and v not in S)

    def F(y: list[float]) -> float:
        total = 0.0
        for mask in range(1 << n):
            S = {i for i in range(n) if (mask >> i) & 1}
            prob = 1.0
            for i in range(n):
                prob *= y[i] if i in S else (1.0 - y[i])
            total += prob * f(S)
        return total

    return n, f, F


def measured_continuous_greedy(F, n: int, rank: int, T: float = 1.0, steps: int = 200) -> list[float]:
    delta = T / steps
    y = [0.0] * n
    for _ in range(steps):
        # w_e(t) = F(y v 1_e) - F(y) = (1 - y_e(t)) * partial_e F(y(t))
        w = []
        for e in range(n):
            y_one = list(y)
            y_one[e] = 1.0
            w.append(F(y_one) - F(y))
        # Maximize x . w over rank-k uniform matroid polytope {x in [0,1]^n : sum x_e <= rank}
        order = sorted(range(n), key=lambda e: w[e], reverse=True)
        I_t = [0.0] * n
        rem = float(rank)
        for e in order:
            if w[e] <= 0.0 or rem <= 0.0:
                break
            take = min(1.0, rem)
            I_t[e] = take
            rem -= take
        for e in range(n):
            y[e] = y[e] + delta * I_t[e] * (1.0 - y[e])
    return y


def main() -> None:
    n, f, F = make_nonmonotone_matroid_instance()
    rank = 2
    opt_val = max(
        f({i for i in range(n) if (mask >> i) & 1})
        for mask in range(1 << n)
        if bin(mask).count("1") <= rank
    )
    assert abs(opt_val - 6.4) < 1e-12  # f({2, 3}) = 1.6 * 4 = 6.4

    # 1. Verify Theorem I.1 & Lemma III.6 on non-monotone submodular maximization over a matroid (T=1)
    y_T = measured_continuous_greedy(F, n, rank=rank, T=1.0, steps=250)
    val_mcg = F(y_T)
    bound_1_e = (1.0 / math.e) * opt_val
    assert sum(y_T) <= rank + 1e-9
    for ye in y_T:
        assert ye <= 1.0 - math.exp(-1.0) + 0.01  # Lemma III.6: y_e(t) <= 1 - e^{-t} + O(delta)
    assert val_mcg >= bound_1_e - 1e-3

    # 2. Verify Theorem I.2 & I.3 / Corollary IV.7: density d(P) = 1/k for k-player Submodular Welfare
    # Stopping time T_P = -ln(1 - d(P)) / d(P) > 1 yields 1 - e^{-T_P} = 1 - (1 - 1/k)^k > 1 - 1/e
    for k in (2, 3, 4):
        d_P = 1.0 / k
        T_P = -math.log(1.0 - d_P) / d_P
        assert T_P > 1.0
        ratio_density = 1.0 - math.exp(-T_P)
        exact_k_welfare = 1.0 - ((1.0 - 1.0 / k) ** k)
        assert abs(ratio_density - exact_k_welfare) < 1e-12
        assert ratio_density > 1.0 - 1.0 / math.e

    print(
        f"[PASS] Measured Continuous Greedy boundaries verified: OPT={opt_val:.2f}, "
        f"F(y(1))={val_mcg:.4f} >= (1/e)*OPT={bound_1_e:.4f}, "
        f"max_e y_e(1)={max(y_T):.4f} <= 1-1/e={1.0 - 1.0/math.e:.4f}, "
        f"2-player SW ratio={1.0 - (0.5**2):.2f}"
    )


if __name__ == "__main__":
    main()
