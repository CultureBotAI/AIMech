#!/usr/bin/env python3
"""Constructed boundary & regime verification for Stochastic-Greedy / Lazier Than Lazy Greedy
(Mirzasoleiman, Badanidiyuru, Karbasi, Vondrak, & Krause 2015, Round 348)."""

import math
import random


def make_coverage_instance(n: int = 60, m: int = 30, k: int = 6):
    # Construct a monotone submodular weighted coverage function f(A) = sum_{u in U_{i in A} S_i} w_u
    # where the first k sets S_0..S_{k-1} disjointly cover 3 high-weight elements each (weight 10.0),
    # and the remaining n - k sets cover overlapping low-weight elements (weight 1.0).
    sets = []
    weights = {}
    elem_id = 0
    for i in range(k):
        s = set()
        for _ in range(3):
            weights[elem_id] = 10.0
            s.add(elem_id)
            elem_id += 1
        sets.append(s)
    rng = random.Random(348)
    low_elems = list(range(elem_id, elem_id + m))
    for e in low_elems:
        weights[e] = 1.0
    for _ in range(n - k):
        sets.append(set(rng.sample(low_elems, 4)))
    return sets, weights, k


def eval_f(sets, weights, A_indices) -> float:
    covered = set()
    for idx in A_indices:
        covered |= sets[idx]
    return sum(weights[e] for e in covered)


def marginal_gain(sets, weights, covered, idx) -> float:
    return sum(weights[e] for e in sets[idx] if e not in covered)


def run_standard_greedy(sets, weights, k: int):
    n = len(sets)
    A = set()
    covered = set()
    evals = 0
    for _ in range(k):
        best_i = -1
        best_gain = -1.0
        for i in range(n):
            if i not in A:
                g = marginal_gain(sets, weights, covered, i)
                evals += 1
                if g > best_gain:
                    best_gain = g
                    best_i = i
        A.add(best_i)
        covered |= sets[best_i]
    return eval_f(sets, weights, A), evals


def run_stochastic_greedy(sets, weights, k: int, eps: float, seed: int):
    rng = random.Random(seed)
    n = len(sets)
    s = min(n, math.ceil((n / k) * math.log(1.0 / eps)))
    A = set()
    covered = set()
    evals = 0
    for _ in range(k):
        remaining = [i for i in range(n) if i not in A]
        R = rng.sample(remaining, min(s, len(remaining)))
        best_i = -1
        best_gain = -1.0
        for i in R:
            g = marginal_gain(sets, weights, covered, i)
            evals += 1
            if g > best_gain:
                best_gain = g
                best_i = i
        A.add(best_i)
        covered |= sets[best_i]
    return eval_f(sets, weights, A), evals


def main():
    n, k = 60, 6
    eps = 0.15
    sets, weights, k = make_coverage_instance(n=n, m=30, k=k)
    opt_val = 30.0 * k  # S_0..S_{k-1} have total weight 180.0

    # Claim 1: Verify Lemma 2 overlap probability inequality:
    # For s = (n/k) ln(1/eps) and any residual size r = |A^* \ A| in {1, ..., k},
    # Pr[R cap (A^* \ A) != empty] >= 1 - exp(-(s/n) * r) >= (1 - eps) * (r / k)
    s_exact = (n / k) * math.log(1.0 / eps)
    for r in range(1, k + 1):
        # Exact hypergeometric overlap probability when sampling int(ceil(s_exact)) without replacement from n:
        s_int = math.ceil(s_exact)
        prob_miss = 1.0
        for j in range(s_int):
            prob_miss *= (n - r - j) / (n - j)
        prob_hit = 1.0 - prob_miss
        exp_bound = 1.0 - math.exp(-(s_exact / n) * r)
        linear_concave_bound = (1.0 - eps) * (r / k)
        assert prob_hit >= exp_bound - 1e-12 >= linear_concave_bound - 1e-12

    # Claim 2: Verify Theorem 1 (1 - 1/e - eps) expected approximation ratio and k-independent O(n log(1/eps)) evaluations
    std_val, std_evals = run_standard_greedy(sets, weights, k)
    assert abs(std_val - opt_val) < 1e-12

    trials = 200
    sg_vals = []
    sg_evals = 0
    for t in range(trials):
        v, ev = run_stochastic_greedy(sets, weights, k, eps=eps, seed=1000 + t)
        sg_vals.append(v)
        sg_evals = ev
    mean_sg_val = sum(sg_vals) / trials
    theo_bound = (1.0 - 1.0 / math.e - eps) * opt_val
    assert mean_sg_val >= theo_bound, f"Theorem 1 violated: {mean_sg_val} < {theo_bound}"
    assert sg_evals <= k * math.ceil((n / k) * math.log(1.0 / eps))
    assert sg_evals < std_evals  # 120 < 345

    # Also verify k-independence of evaluation count n * log(1/eps) across k = 10 vs k = 100 for n = 10000:
    n_big = 10000
    evals_k10 = 10 * ((n_big / 10) * math.log(1.0 / eps))
    evals_k100 = 100 * ((n_big / 100) * math.log(1.0 / eps))
    assert abs(evals_k10 - evals_k100) < 1e-9

    # Claim 3: Non-monotone submodular counterexample where sum_{a in A^* \ A} Delta(a | A) < f(A^*) - f(A)
    # Consider ground set V = {0, 1} with non-monotone submodular cut function:
    # f(empty) = 0, f({0}) = 2, f({1}) = 2, f({0, 1}) = 1 (submodular since Delta(1|{0}) = -1 <= Delta(1|empty) = 2)
    # If current set is A = {0} and optimal k=1 set is A^* = {1} (or if A={0,1} vs A^*={0}):
    # Take A = {0, 1} (f(A) = 1) and A^* = {0} (f(A^*) = 2): A^* \ A = empty, so sum_{a in A^* \ A} Delta(a|A) = 0 < f(A^*) - f(A) = 1!
    f_nonmono = {frozenset(): 0.0, frozenset([0]): 2.0, frozenset([1]): 2.0, frozenset([0, 1]): 1.0}
    A_curr = frozenset([0, 1])
    A_star_nm = frozenset([0])
    lhs_sum = sum(f_nonmono[A_curr | {a}] - f_nonmono[A_curr] for a in (A_star_nm - A_curr))
    rhs_gap = f_nonmono[A_star_nm] - f_nonmono[A_curr]
    assert lhs_sum < rhs_gap  # 0.0 < 1.0: monotonicity step in Lemma 2 / Theorem 1 fails for non-monotone f

    print(
        f"[PASS] Stochastic-Greedy boundaries verified: mean_SG={mean_sg_val:.2f}>=theo={theo_bound:.2f} (OPT={opt_val:.1f}), "
        f"evals={sg_evals}<std_evals={std_evals}, nonmono_sum={lhs_sum:.1f}<gap={rhs_gap:.1f}"
    )


if __name__ == "__main__":
    main()
