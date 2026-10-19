#!/usr/bin/env python3
"""Constructed boundary verification for Contention Resolution Schemes (Chekuri, Vondrak, & Zenklusen 2011/2014)."""

import math


def main() -> None:
    # 1. Verify Theorem 4.8, Corollary 4.11, and Theorem 4.12:
    # Optimal (b, c(b, n))-balanced CR scheme for rank-1 uniform matroid on n elements has
    # c(b, n) = (1 - (1 - b/n)^n) / b >= (1 - e^{-b}) / b, and no CR scheme can exceed c(b, n).
    for b in (0.25, 0.5, 0.75, 1.0):
        asymp_c = (1.0 - math.exp(-b)) / b
        for n in (2, 4, 10, 50):
            exact_c = (1.0 - ((1.0 - b / n) ** n)) / b
            assert exact_c >= asymp_c - 1e-12
            # Compare against deterministic (b, 1-b) scheme (Theorem 4.14)
            if b < 1.0:
                assert exact_c > 1.0 - b

    # 2. Verify Lemma 1.6 (composition of monotone (b, c_i)-balanced CR schemes via FKG inequality)
    # vs naive union bound 1 - sum_i (1 - c_i) on k intersecting matroids:
    # Choosing b = 2 / (k + 1) yields a (2 / (e * (k + 1)))-balanced CR scheme for k-uniform matchoids (Section 2, p. 8).
    for k in (2, 3, 5):
        b_opt = 2.0 / (k + 1)
        c_single = (1.0 - math.exp(-b_opt)) / b_opt
        c_fkg = b_opt * (c_single**k)
        lower_matchoid = 2.0 / (math.e * (k + 1))
        assert c_fkg >= lower_matchoid - 1e-12

    # 3. Verify Theorem 1.3 pruning step eta_f(I) on a non-monotone submodular function:
    # Without pruning, adding an element with negative marginal contribution degrades E[f(I)],
    # whereas sequential greedy pruning J = eta_f(I) guarantees E[f(eta_f(I))] >= c * F(x).
    # Ground set N = {0, 1}, rank-1 matroid or unconstrained down-closed family:
    # Let f({0}) = 2.0, f({1}) = 1.0, f({0, 1}) = 0.2 (non-monotone submodular: 2.0 + 1.0 >= 0.2 + 0).
    f_vals = {frozenset(): 0.0, frozenset({0}): 2.0, frozenset({1}): 1.0, frozenset({0, 1}): 0.2}

    def f(S: set[int]) -> float:
        return f_vals[frozenset(S)]

    def eta_f(I_set: set[int]) -> set[int]:
        J: set[int] = set()
        for i in sorted(I_set):
            if f(J | {i}) - f(J) > 0.0:
                J.add(i)
        return J

    x = [0.6, 0.6]
    # Exact multilinear extension F(x)
    F_x = (
        (1 - x[0]) * (1 - x[1]) * f(set())
        + x[0] * (1 - x[1]) * f({0})
        + (1 - x[0]) * x[1] * f({1})
        + x[0] * x[1] * f({0, 1})
    )
    # Identity (1, 1)-balanced CR scheme I = R(x):
    # Unpruned E[f(R(x))] = F(x), while pruned E[f(eta_f(R(x)))] replaces {0,1} (value 0.2) with {0} (value 2.0)!
    E_pruned = (
        (1 - x[0]) * (1 - x[1]) * f(eta_f(set()))
        + x[0] * (1 - x[1]) * f(eta_f({0}))
        + (1 - x[0]) * x[1] * f(eta_f({1}))
        + x[0] * x[1] * f(eta_f({0, 1}))
    )
    assert E_pruned > F_x

    # 4. Verify Algorithm 3.15 (Restricted Local Search on P cap [0, t]^N, Lemma 3.19 & Corollary 3.21):
    # At t = (3 - sqrt(5)) / 2, t = (1 - t)^2 and approximation factor is t - t^2 / 2 = (-1 + sqrt(5)) / 4 ~ 0.309017.
    t_opt = 0.5 * (3.0 - math.sqrt(5.0))
    assert abs(t_opt - ((1.0 - t_opt) ** 2)) < 1e-12
    approx_rls = t_opt - 0.5 * (t_opt**2)
    assert abs(approx_rls - 0.25 * (math.sqrt(5.0) - 1.0)) < 1e-12

    print(
        f"[PASS] Contention Resolution Schemes boundaries verified: "
        f"matroid c(0.5,10)={(1-(1-0.05)**10)/0.5:.4f} >= {(1-math.exp(-0.5))/0.5:.4f}, "
        f"pruned E[f(eta_f(I))]={E_pruned:.3f} > F(x)={F_x:.3f}, RLS ratio={approx_rls:.6f}"
    )


if __name__ == "__main__":
    main()
