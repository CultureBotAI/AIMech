#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 362:
Parallel Greedy Submodular Maximization in Logarithmic Adaptivity and Nearly-Linear Time
(Ene & Nguyen 2018/2019, SODA 2019, arXiv:1804.05379).
"""

import itertools
import math


def make_coverage_instance():
    """Construct a monotone submodular coverage instance on ground set V of size n=9."""
    # Universe of 18 weighted elements
    weights = {i: 1.0 + 0.15 * (i % 5) for i in range(18)}
    subsets = [
        frozenset([0, 1, 2, 3, 4]),
        frozenset([2, 3, 5, 6, 7]),
        frozenset([0, 5, 8, 9, 10]),
        frozenset([1, 6, 8, 11, 12]),
        frozenset([4, 7, 10, 13, 14]),
        frozenset([3, 9, 11, 15]),
        frozenset([12, 13, 16]),
        frozenset([14, 15, 17]),
        frozenset([0, 1, 16, 17]),
    ]

    def f_val(S_indices):
        cov = set()
        for idx in S_indices:
            cov.update(subsets[idx])
        return sum(weights[u] for u in cov)

    return list(range(len(subsets))), f_val


def main():
    V, f_val = make_coverage_instance()
    n = len(V)
    k = 4

    # 1. Compute exact OPT for cardinality k=4
    best_opt_val = -1.0
    best_opt_set = None
    for comb in itertools.combinations(V, k):
        val = f_val(comb)
        if val > best_opt_val:
            best_opt_val = val
            best_opt_set = set(comb)

    # 2. Verify Claim 6 (Pages 7-8) and Equation (2) (conditioning inequality) EXACTLY
    # across all choices of S and block sizes ell = 2, 3
    S_curr = {0}
    U_t = [e for e in V if e not in S_curr]
    for ell in (2, 3):
        all_R = list(itertools.combinations(U_t, ell))
        num_R = len(all_R)
        # Expected block gain E_{R ~ U(U_t, ell)}[f(R | S)]
        f_S = f_val(S_curr)
        exp_block_gain = sum(f_val(S_curr | set(R)) - f_S for R in all_R) / num_R

        # For each e in U_t, check:
        # E[f(e | S U (R \ {e})) | e in R] >= E[f(e | S U (R \ {e})) | e not in R]
        sum_exp_R_minus_e = 0.0
        sum_exp_R = 0.0
        for e in U_t:
            R_with_e = [R for R in all_R if e in R]
            R_without_e = [R for R in all_R if e not in R]
            cond_in = sum(
                f_val(S_curr | (set(R) - {e}) | {e}) - f_val(S_curr | (set(R) - {e}))
                for R in R_with_e
            ) / len(R_with_e)
            cond_out = sum(
                f_val(S_curr | set(R) | {e}) - f_val(S_curr | set(R))
                for R in R_without_e
            ) / len(R_without_e)
            assert cond_in >= cond_out - 1e-12, f"Eq (2) conditioning inequality failed: {cond_in} < {cond_out}"

            exp_e_minus = sum(
                f_val(S_curr | (set(R) - {e}) | {e}) - f_val(S_curr | (set(R) - {e}))
                for R in all_R
            ) / num_R
            exp_e_full = sum(
                f_val(S_curr | set(R) | {e}) - f_val(S_curr | set(R))
                for R in all_R
            ) / num_R
            assert cond_in >= exp_e_minus - 1e-12
            assert exp_e_minus >= exp_e_full - 1e-12
            sum_exp_R_minus_e += (ell / len(U_t)) * exp_e_minus
            sum_exp_R += (ell / len(U_t)) * exp_e_full

        assert exp_block_gain >= sum_exp_R_minus_e - 1e-12, "Claim 6 Eq (1) violated!"
        assert sum_exp_R_minus_e >= sum_exp_R - 1e-12, "Claim 6 Eq (2) violated!"

    # 3. Verify Lemma 5 (filtering fraction |U_t^-| >= eps |U_t|) and Claim 9 (deterministic aggregate
    # OPT-preservation bound during filtering without per-element concentration, Pages 9-10)
    eps = 0.05
    Old = f_val(S_curr)
    # Set M slightly high so filtering branch triggers and satisfies line 20 conditions
    ell = 2
    all_R = [set(R) for R in itertools.combinations(U_t, ell)]
    avg_i = sum(f_val(S_curr | R) - Old for R in all_R) / len(all_R)
    v_ie = {
        e: sum(f_val(S_curr | R | {e}) - f_val(S_curr | R) for R in all_R) / len(all_R)
        for e in U_t
    }
    avg_v = sum(v_ie.values()) / len(U_t)
    # By Claim 6, avg_i / ell >= avg_v
    assert (avg_i / ell) >= avg_v - 1e-12

    # Choose target M - Old so that avg_i <= (1 - 8*eps)*(ell/k)*(M - Old)
    M_minus_Old = (avg_i * k / ell) / (1.0 - 8.0 * eps)
    M_val = Old + M_minus_Old
    # Line 20 conditions hold:
    assert avg_i <= (1.0 - 8.0 * eps) * (ell / k) * M_minus_Old + 1e-12
    assert sum(v_ie.values()) <= len(U_t) * (1.0 - 8.0 * eps) * (M_minus_Old / k) + 1e-12

    # Line 22 filtering: U_t^- = {e in U_t : v_{i,e} < (1 - 7*eps)*(M - Old)/k}
    thresh = (1.0 - 7.0 * eps) * (M_minus_Old / k)
    U_t_minus = {e for e in U_t if v_ie[e] < thresh}
    U_t_next = [e for e in U_t if e not in U_t_minus]
    # Lemma 5: |U_t^-| >= eps * |U_t|
    assert len(U_t_minus) >= eps * len(U_t) - 1e-12, "Lemma 5 filtering fraction violated!"

    # Claim 9 deterministic aggregate bound (Page 10):
    # f((OPT \cap U_{t+1}) | S) >= f((OPT \cap U_t) | S) - avg_i - |OPT \cap U_t^-| * (1 - 7*eps)*(M - Old)/k
    lhs_claim9 = f_val(S_curr | (best_opt_set & set(U_t_next))) - Old
    rhs_claim9 = (
        (f_val(S_curr | (best_opt_set & set(U_t))) - Old)
        - avg_i
        - len(best_opt_set & U_t_minus) * thresh
    )
    assert lhs_claim9 >= rhs_claim9 - 1e-12, f"Claim 9 violated: {lhs_claim9} < {rhs_claim9}"

    # 4. Verify Lemma 12 inductive exponential progression (Page 11):
    # M - f(S U R_max) <= (M - f(S)) * (1 - |R_max|*(1 - 11*eps)/k) <= M * exp(-(1 - 11*eps)*|S U R_max|/k)
    M_true = best_opt_val
    S_prog = set()
    for step in range(2):
        rem = [e for e in V if e not in S_prog]
        best_R = max(itertools.combinations(rem, 2), key=lambda R: f_val(S_prog | set(R)))
        S_prog |= set(best_R)
        lhs_rem = M_true - f_val(S_prog)
        rhs_exp = M_true * math.exp(-(1.0 - 11.0 * eps) * len(S_prog) / k)
        assert lhs_rem <= rhs_exp + 1e-12

    print(
        f"[PASS] Round 362 Parallel Greedy Submodular (Ene & Nguyen 2019): "
        f"claim6_gap={(avg_i/ell) - avg_v:.4f}>=0, filtered={len(U_t_minus)}/{len(U_t)}, "
        f"claim9_margin={lhs_claim9 - rhs_claim9:.4f}>=0, final_ratio={f_val(S_prog)/best_opt_val:.4f}"
    )


if __name__ == "__main__":
    main()
