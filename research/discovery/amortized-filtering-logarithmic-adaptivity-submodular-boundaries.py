#!/usr/bin/env python3
r"""Constructed boundary verification for Round 360:
An Exponential Speedup in Parallel Running Time for Submodular Maximization without Loss in
Approximation (Iterative-Filtering & Amortized-Filtering, Balkanski, Rubinstein, & Singer 2018/2019).

Verifies:
1. Lemma 3 (Geometric Survival Shrinkage in Filter): In any non-terminating iteration i of
   Filter(X, S, r) where E_{R~U(X, t)}[f_S(R)] < (1 - eps)(OPT - f(S))/r, the surviving set
   X_{i+1} = {a in X_i : E[f_{S union (R \ {a})}(a)] >= (1 + eps/2)(1 - eps)(OPT - f(S))/k}
   satisfies |X_{i+1}| < |X_i| / (1 + eps/2).
2. Algorithm 3 & Theorem 2 (Amortized-Filtering): Across epochs where surviving elements X are
   reused until f_S(T) >= (eps/20)(OPT - f(S)), Amortized-Filtering achieves the optimal
   (1 - 1/e - eps) approximation guarantee while using fewer total adaptive filtering rounds than
   both sequential greedy (k rounds) and Iterative-Filtering (Algorithm 1).
"""

import itertools
import math


def exact_uniform_expectations(
    f_eval, S: set[int], X: list[int], t: int
) -> tuple[float, dict[int, float]]:
    # Compute exact E_{R~U(X, t)}[f_S(R)] and E_{R~U(X, t)}[f_{S union (R\{a})}(a)] for all a in X
    f_S = f_eval(S)
    if len(X) <= t:
        R_set = set(X)
        val_R = f_eval(S | R_set) - f_S
        marg = {}
        for a in X:
            base = S | (R_set - {a})
            marg[a] = f_eval(base | {a}) - f_eval(base)
        return val_R, marg

    combs = list(itertools.combinations(X, t))
    num_c = len(combs)
    total_fS_R = 0.0
    marg_sums = {a: 0.0 for a in X}
    for c in combs:
        R_set = set(c)
        f_SR = f_eval(S | R_set)
        total_fS_R += f_SR - f_S
        for a in X:
            if a in R_set:
                base = S | (R_set - {a})
                marg_sums[a] += f_SR - f_eval(base)
            else:
                base = S | R_set
                marg_sums[a] += f_eval(base | {a}) - f_SR
    return total_fS_R / num_c, {a: marg_sums[a] / num_c for a in X}


def main() -> None:
    # Construct a monotone submodular weighted coverage instance on n = 10 elements with k = 4, t = k/r = 2
    # 4 high-value disjoint items (0..3) of weight 10 each, and 6 low-value items (4..9) of weight 1 each.
    weights = [10.0, 10.0, 10.0, 10.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    N = list(range(len(weights)))
    k = 4
    r = 2  # block size t = k / r = 2
    t = k // r
    eps = 0.2
    OPT = 40.0  # {0, 1, 2, 3}

    def f_eval(S: set[int]) -> float:
        # Concave diminishing returns on low-value items + modular on high-value items
        high = sum(weights[i] for i in S if i < 4)
        low_cnt = sum(1 for i in S if i >= 4)
        return high + (2.0 * (1.0 - (0.7 ** low_cnt)) if low_cnt > 0 else 0.0)

    # 1. Verify Lemma 3 on initial call Filter(N, S=empty, r=2)
    S0: set[int] = set()
    X_curr = list(N)
    exp_R, marg_dict = exact_uniform_expectations(f_eval, S0, X_curr, t)
    target_block = (1.0 - eps) * (OPT - f_eval(S0)) / r
    assert exp_R < target_block, f"Expected initial random block {exp_R} < {target_block}"
    thresh = (1.0 + eps / 2.0) * (1.0 - eps) * (OPT - f_eval(S0)) / k
    X_next = [a for a in X_curr if marg_dict[a] >= thresh]
    lemma3_bound = len(X_curr) / (1.0 + eps / 2.0)
    assert len(X_next) < lemma3_bound, f"Lemma 3 violated: |X_next|={len(X_next)} >= {lemma3_bound}"
    assert X_next == [0, 1, 2, 3]

    # 2. Compare Iterative-Filtering (resets X <- N every outer step) vs Amortized-Filtering (reuses X within epoch)
    # Iterative-Filtering (Algorithm 1):
    S_iter: set[int] = set()
    iter_filter_rounds = 0
    for _ in range(r):
        X_if = list(N)
        while True:
            iter_filter_rounds += 1
            e_R, m_d = exact_uniform_expectations(f_eval, S_iter, X_if, t)
            if e_R >= (1.0 - eps) * (OPT - f_eval(S_iter)) / r or len(X_if) <= t:
                break
            th = (1.0 + eps / 2.0) * (1.0 - eps) * (OPT - f_eval(S_iter)) / k
            X_if = [a for a in X_if if m_d[a] >= th]
        # Deterministically pick the best t-subset from surviving X_if (satisfying footnote 2, p. 5)
        best_R = max(itertools.combinations(X_if, min(t, len(X_if))), key=lambda c: f_eval(S_iter | set(c)))
        S_iter |= set(best_R)

    # Amortized-Filtering (Algorithm 3): reuses X across block additions within an epoch
    S_amort: set[int] = set()
    amort_filter_rounds = 0
    X_am = list(N)
    T_am: set[int] = set()
    while len(S_amort | T_am) < k:
        while True:
            amort_filter_rounds += 1
            e_R, m_d = exact_uniform_expectations(f_eval, S_amort | T_am, X_am, t)
            if e_R >= (1.0 - eps) * (OPT - f_eval(S_amort | T_am)) / r or len(X_am) <= t:
                break
            th = (1.0 + eps / 2.0) * (1.0 - eps) * (OPT - f_eval(S_amort | T_am)) / k
            X_am = [a for a in X_am if m_d[a] >= th]
        rem_X = [a for a in X_am if a not in (S_amort | T_am)]
        best_R = max(itertools.combinations(rem_X, min(t, len(rem_X))), key=lambda c: f_eval(S_amort | T_am | set(c)))
        T_am |= set(best_R)
    S_amort |= T_am

    val_iter = f_eval(S_iter)
    val_amort = f_eval(S_amort)
    thm2_bound = (1.0 - 1.0 / math.e - eps) * OPT
    assert val_iter >= thm2_bound and val_amort >= thm2_bound
    assert abs(val_amort - OPT) < 1e-12
    assert amort_filter_rounds < iter_filter_rounds

    print(
        f"[PASS] Round 360 Amortized-Filtering Submodular (Balkanski et al. 2018/2019): "
        f"|X_0|={len(X_curr)}->|X_1|={len(X_next)}<{lemma3_bound:.2f}, "
        f"val_amort={val_amort:.2f}>=thm2_bound={thm2_bound:.2f}, "
        f"amort_rounds={amort_filter_rounds}<iter_rounds={iter_filter_rounds}"
    )


if __name__ == "__main__":
    main()
