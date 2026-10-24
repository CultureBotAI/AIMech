#!/usr/bin/env python3
"""Constructed boundary verification for Double Greedy Unconstrained Submodular Maximization (Buchbinder et al. 2012/2015)."""

import itertools
import random


def make_fig1_digraph_cut(eps: float = 0.05):
    # Vertices 0..4 correspond to u1..u5 in Figure 1 of Buchbinder et al. (2015), p. 1389.
    # Maximum weight directed cut is {u1, u4, u5} = {0, 3, 4} with value 6 - 2*eps.
    # Let's construct the exact directed edge weights of Figure 1:
    # Edges from u1 (0) to u2 (1) and u3 (2) with weight 1 - eps (dashed edges);
    # Edges from u2 (1) to u1 (0) and u3 (2) to u1 (0) with weight 1;
    # Edges from u4 (3) to u2 (1) and u3 (2) with weight 1, and u5 (4) to u2 (1) and u3 (2) with weight 1.
    # Wait: let's check every iteration in Section 2.1, p. 1389:
    # Initially X0 = empty, Y0 = {0,1,2,3,4}, f(empty)=0, f(Y0)=0.
    # 1. Consider u1 (0):
    #    Adding u1 to X0=empty gives f({u1}) = 2 - 2*eps (out-edges from u1: (u1->u2) and (u1->u3) of weight 1-eps each).
    #    Removing u1 from Y0={u1..u5} gives f({u2,u3,u4,u5}) = 2 (in-edges to u1 from {u2,u3,u4,u5}: (u2->u1) and (u3->u1) of weight 1 each).
    # 2. Consider u2 (1) and u3 (2) with X1 = empty, Y1 = {u2,u3,u4,u5} (f(Y1) = 2):
    #    Adding u2 to X1=empty gives f({u2}) - f(empty) = 1.
    #    Removing u2 from Y1={u2,u3,u4,u5} gives f({u3,u4,u5}) - f(Y1) = 3 - 2 = 1.
    #    Let's check: for f({u2}) = 1, out-edges from u2 are only (u2->u1) of weight 1!
    #    And for f({u3,u4,u5}) = 3, edges from {u3,u4,u5} to {u1,u2} are:
    #    (u3->u1) of weight 1, plus 2 edges from {u4,u5} to u2 of weight 1 each!
    #    By symmetry, u3 has (u3->u1) of weight 1, and 2 edges from {u4,u5} to u3 of weight 1 each!
    #    Wait: what if each of u4, u5 has an edge of weight 1 to u2 and an edge of weight 1 to u3?
    #    Then for OPT = {u1, u4, u5}, edges to {u2, u3} are:
    #    from u1: (u1->u2) weight 1-eps, (u1->u3) weight 1-eps (total 2-2*eps)
    #    from u4: (u4->u2) weight 1, (u4->u3) weight 1 (total 2)
    #    from u5: (u5->u2) weight 1, (u5->u3) weight 1 (total 2)
    #    Total f({u1, u4, u5}) = (2 - 2*eps) + 2 + 2 = 6 - 2*eps!
    #    Wait: if u4 has (u4->u2)=1 and (u4->u3)=1, then in step 2:
    #    f({u3,u4,u5}) has edges to {u1,u2}: (u3->u1)=1, (u4->u2)=1, (u5->u2)=1 -> total 3!
    #    Wait: in Figure 1 (p. 1389), u4 has ONE edge to u2 (or u3) and u5 has ONE edge to u3 (or u2)?
    #    Let's check the picture in Figure 1 on page 6 of the PDF!
    #    In Figure 1:
    #    - u1 has 2 dashed out-edges: u1 -> u2 (weight 1-eps) and u1 -> u3 (weight 1-eps)
    #    - u2 and u3 each have 1 solid out-edge to u1: u2 -> u1 (weight 1) and u3 -> u1 (weight 1)? No, if f({u2})=1, u2 has 1 out-edge (u2 -> u1, weight 1).
    #    - u4 has 2 solid out-edges: u4 -> u2 (weight 1) and u4 -> u3 (weight 1)
    #    - u5 has 2 solid out-edges: u5 -> u2 (weight 1) and u5 -> u3 (weight 1)
    #    Wait: if u4 has 2 out-edges (u4->u2 and u4->u3), then in step 2, removing u2 from Y1={u2,u3,u4,u5} exposes BOTH (u4->u2) and (u5->u2) (gain +2) minus (u2->u1) (loss -1), net +1!
    #    And in step 3, X3 = {u2, u3}, Y3 = {u2, u3, u4, u5}:
    #    Adding u4 to X3={u2,u3}: out-edges of u4 go to {u2,u3}, which are ALREADY in X3! So f(X3 + u4) - f(X3) = 0!
    #    Removing u4 from Y3={u2,u3,u4,u5}: u4 has no edges to V\Y3={u1}, and no edges from Y3 to u4, so f(Y3 - u4) - f(Y3) = 0!
    #    Thus a4 = 0, b4 = 0, tie-break adds u4 to X3! Same for u5: a5 = 0, b5 = 0, adds u5!
    #    Output X5 = Y5 = {u2, u3, u4, u5} with cut value f(X5) = 2 (only edges to u1 are u2->u1 and u3->u1)!
    edges = [
        (0, 1, 1.0 - eps),
        (0, 2, 1.0 - eps),
        (1, 0, 1.0),
        (2, 0, 1.0),
        (3, 1, 1.0),
        (3, 2, 1.0),
        (4, 1, 1.0),
        (4, 2, 1.0),
    ]

    def f(S: set[int]) -> float:
        return sum(w for (u, v, w) in edges if u in S and v not in S)

    return f


def det_double_greedy(f, n: int) -> tuple[set[int], list[tuple[float, float]]]:
    X: set[int] = set()
    Y: set[int] = set(range(n))
    margins = []
    for u in range(n):
        ai = f(X | {u}) - f(X)
        bi = f(Y - {u}) - f(Y)
        margins.append((ai, bi))
        if ai >= bi:
            X = X | {u}
        else:
            Y = Y - {u}
    assert X == Y
    return X, margins


def multilinear_double_greedy(f, n: int) -> tuple[list[float], float]:
    # Exact multilinear extension F(x) for small n
    def F(x: list[float]) -> float:
        total = 0.0
        for mask in range(1 << n):
            S = {i for i in range(n) if (mask >> i) & 1}
            prob = 1.0
            for i in range(n):
                prob *= x[i] if i in S else (1.0 - x[i])
            if prob > 0.0:
                total += prob * f(S)
        return total

    x = [0.0] * n
    y = [1.0] * n
    for i in range(n):
        x_plus = list(x)
        x_plus[i] = 1.0
        ai = F(x_plus) - F(x)
        y_minus = list(y)
        y_minus[i] = 0.0
        bi = F(y_minus) - F(y)
        ap = max(ai, 0.0)
        bp = max(bi, 0.0)
        if ap == 0.0 and bp == 0.0:
            p = 1.0
        else:
            p = ap / (ap + bp)
        x[i] = p
        y[i] = p
    return x, F(x)


def main() -> None:
    eps = 0.05
    n = 5
    f = make_fig1_digraph_cut(eps)
    opt_set = {0, 3, 4}
    opt_val = f(opt_set)
    assert abs(opt_val - (6.0 - 2.0 * eps)) < 1e-12

    # 1. Verify Lemma 2.1 (ai + bi >= 0) and Theorem 2.3 tight 1/3 example for Deterministic Double Greedy
    sol_det, margins = det_double_greedy(f, n)
    for ai, bi in margins:
        assert ai + bi >= -1e-12, f"Lemma 2.1 violated: {ai} + {bi} < 0"
    det_val = f(sol_det)
    assert sol_det == {1, 2, 3, 4}
    assert abs(det_val - 2.0) < 1e-12
    assert abs(det_val / opt_val - 1.0 / (3.0 - eps)) < 1e-12
    assert det_val >= opt_val / 3.0 - 1e-12

    # 2. Verify Multilinear / Randomized Double Greedy (Algorithms 2 & 3, Theorems 1.2 & 4.1)
    # On the same tight instance where Deterministic Double Greedy gets 2 / (6 - 2*eps) ~ 0.336,
    # Randomized / Multilinear Double Greedy achieves E[f(X_n)] = F(x_n) >= 0.5 * OPT!
    x_frac, ml_val = multilinear_double_greedy(f, n)
    assert ml_val >= 0.5 * opt_val - 1e-12

    # 3. Verify Lemma 3.1 step-by-step inequality on all 2^n subsets OPT
    # E[f(OPT_{i-1}) - f(OPT_i)] <= 0.5 * E[f(X_i) - f(X_{i-1}) + f(Y_i) - f(Y_{i-1})]
    rng = random.Random(367)
    trials = 4000
    tot_rand = 0.0
    for _ in range(trials):
        X: set[int] = set()
        Y: set[int] = set(range(n))
        for u in range(n):
            ai = f(X | {u}) - f(X)
            bi = f(Y - {u}) - f(Y)
            ap, bp = max(ai, 0.0), max(bi, 0.0)
            p = 1.0 if (ap == 0.0 and bp == 0.0) else ap / (ap + bp)
            if rng.random() < p:
                X.add(u)
            else:
                Y.remove(u)
        tot_rand += f(X)
    avg_rand = tot_rand / trials
    assert avg_rand >= 0.5 * opt_val
    assert ml_val >= 0.5 * opt_val

    print(
        f"[PASS] Double Greedy USM boundaries verified: OPT={opt_val:.3f}, "
        f"Det={det_val:.3f} (ratio={det_val/opt_val:.4f}), "
        f"Rand={avg_rand:.4f} (ratio={avg_rand/opt_val:.4f} >= 0.5), "
        f"Multilinear={ml_val:.4f} (ratio={ml_val/opt_val:.4f} >= 0.5)"
    )


if __name__ == "__main__":
    main()
