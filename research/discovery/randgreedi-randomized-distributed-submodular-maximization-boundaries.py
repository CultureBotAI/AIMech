#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 361:
RandGreeDi Randomized Distributed Submodular Maximization (Barbosa, Ene, Nguyen, & Ward 2015).
"""

import itertools
import math
import random


def make_appendix_b_instance(ell=2):
    """Construct the tight Max k-Coverage instance from Appendix B (Page 18-19) of Barbosa et al. (2015).
    Ground set N has ell^2 + ell^3 elements.
    m = ell^2 + 1 machines, cardinality constraint k = ell + ell^2.
    """
    m = ell * ell + 1
    k = ell + ell * ell
    # Ground set elements: 1 .. ell^2 + ell^3
    # Machine 1 has O_1, ..., O_ell from OPT, where O_j = {(j-1)*ell + 1, ..., j*ell}
    O_sets = []
    for j in range(1, ell + 1):
        O_j = frozenset(range((j - 1) * ell + 1, j * ell + 1))
        O_sets.append(("O", j, O_j))

    machine_items = [[] for _ in range(m)]
    # Machine 0 (representing machine 1 in paper): O_1 .. O_ell plus empty sets
    for item in O_sets:
        machine_items[0].append(item)
    for z in range(ell * ell):
        machine_items[0].append(("EMPTY", f"m0_{z}", frozenset()))

    # Machines i = 1 .. ell^2 (representing machines 2 .. ell^2+1 in paper)
    opt_items = list(O_sets)
    for i in range(1, m):
        # Single set from OPT: O'_i covering ell elements in ell^2 + (i-1)*ell + 1 .. ell^2 + i*ell
        base = ell * ell + (i - 1) * ell
        O_prime_i = frozenset(range(base + 1, base + ell + 1))
        opt_item = ("O_prime", i, O_prime_i)
        opt_items.append(opt_item)
        # First add the ell decoy sets A_{i,j} = O_j U {base + j} so standard tie-breaking/order sees decoys
        for j in range(1, ell + 1):
            O_j = O_sets[j - 1][2]
            A_ij = O_j | frozenset([base + j])
            machine_items[i].append(("A_decoy", f"{i}_{j}", A_ij))
        # Pad with empty sets BEFORE O'_i so once O_1..O_ell are covered, O'_i has marginal gain ell,
        # wait: in Appendix B (p. 19): "On each machine i > 1, Greedy first picks the ell sets
        # A_j = O_j U {ell^2 + (i-1)*ell + j}, since each of them has marginal value ell+1 > |O'_i| = ell.
        # Once Greedy has picked all of the A_j's, the marginal value of O'_i becomes zero and we may
        # assume that Greedy always picks the empty sets instead of O'_i."
        for z in range(ell * ell):
            machine_items[i].append(("EMPTY", f"m{i}_{z}", frozenset()))
        machine_items[i].append(opt_item)

    all_items = [item for mach in machine_items for item in mach]
    return ell, m, k, machine_items, all_items, opt_items


def f_cov(subset):
    covered = set()
    for _, _, s in subset:
        covered.update(s)
    return float(len(covered))


def greedy_cardinality(items, k):
    """Standard Greedy algorithm (Algorithm 1, p. 5) preserving item order on ties."""
    selected = []
    selected_ids = set()
    covered = set()
    for _ in range(k):
        best_item = None
        best_gain = -1.0
        for idx, item in enumerate(items):
            if idx in selected_ids:
                continue
            gain = float(len( item[2] - covered ))
            if gain > best_gain:
                best_gain = gain
                best_item = (idx, item)
        if best_item is None or best_gain < 0:
            break
        selected_ids.add(best_item[0])
        selected.append(best_item[1])
        covered.update(best_item[1][2])
    return selected


def lovasz_extension_exact(f_func, universe, p_vec):
    """Exact Lovasz extension f^-(p) = sum_{i=1}^n (p_{pi_i} - p_{pi_{i+1}}) f({pi_1, ..., pi_i})
    where pi sorts p_vec in descending order (Page 4, Section 1.3).
    """
    paired = sorted(zip(p_vec, universe), key=lambda x: -x[0])
    total = 0.0
    prefix = []
    n = len(paired)
    for i in range(n):
        p_i, elem = paired[i]
        prefix.append(elem)
        p_next = paired[i + 1][0] if i + 1 < n else 0.0
        if p_i > p_next:
            total += (p_i - p_next) * f_func(prefix)
    return total


def main():
    # 1. Verify Lemma 1 & Lemma 2 on a small ground set V of 6 coverage subsets
    V_small = [
        ("e0", 0, frozenset([1, 2, 3])),
        ("e1", 1, frozenset([2, 3, 4])),
        ("e2", 2, frozenset([4, 5])),
        ("e3", 3, frozenset([1, 5, 6])),
        ("e4", 4, frozenset([3, 6])),
        ("e5", 5, frozenset([1, 4])),
    ]
    p_vec = [0.8, 0.5, 0.9, 0.3, 0.6, 0.2]
    c_scale = 0.65
    cp_vec = [c_scale * x for x in p_vec]
    # Check homogeneity f^-(c*p) == c * f^-(p)
    f_minus_p = lovasz_extension_exact(f_cov, V_small, p_vec)
    f_minus_cp = lovasz_extension_exact(f_cov, V_small, cp_vec)
    homog_err = abs(f_minus_cp - c_scale * f_minus_p)
    assert homog_err < 1e-12, f"Lovasz homogeneity error {homog_err}"

    # Check Lemma 1: for product distribution S with E[1_S] = c * p, E[f(S)] >= c * f^-(p)
    expected_f_S = 0.0
    for bits in itertools.product([0, 1], repeat=len(V_small)):
        prob = 1.0
        S_sub = []
        for idx, b in enumerate(bits):
            if b == 1:
                prob *= cp_vec[idx]
                S_sub.append(V_small[idx])
            else:
                prob *= (1.0 - cp_vec[idx])
        expected_f_S += prob * f_cov(S_sub)
    assert expected_f_S >= c_scale * f_minus_p - 1e-12, "Lemma 1 violated!"

    # Check Lemma 2 (Greedy stability): if Greedy(A U {e}) == Greedy(A) for all e in B, then Greedy(A U B) == Greedy(A)
    A_sub = V_small[:4]
    G_A = greedy_cardinality(A_sub, k=2)
    B_sub = [e for e in V_small[4:] if greedy_cardinality(A_sub + [e], k=2) == G_A]
    assert len(B_sub) == 2
    G_AB = greedy_cardinality(A_sub + B_sub, k=2)
    assert G_AB == G_A, "Lemma 2 violated!"

    # 2. Verify Appendix B tight deterministic GreeDi adversarial partition vs RandGreeDi (Theorem 5 / Corollary 6)
    ell, m, k, machine_items, all_items, opt_items = make_appendix_b_instance(ell=3)
    opt_val = f_cov(opt_items)
    assert opt_val == ell * ell + ell ** 3  # 9 + 27 = 36

    # Deterministic GreeDi on adversarial partition
    S_det_union = []
    S_det_best = 0.0
    for i in range(m):
        S_i = greedy_cardinality(machine_items[i], k)
        S_det_best = max(S_det_best, f_cov(S_i))
        S_det_union.extend(S_i)
    T_det = greedy_cardinality(S_det_union, k)
    det_greedi_val = max(f_cov(T_det), S_det_best)
    # In Appendix B, machine 1 outputs O_1..O_ell and machines i>1 output A_{i,1}..A_{i,ell},
    # so any k = ell + ell^2 sets from their union cover {1..ell^2} plus at most k = ell + ell^2
    # singleton elements, i.e. 2*ell^2 + ell = 21 out of ell^2 + ell^3 = 36 (ratio (2*ell+1)/(ell^2+ell) = O(1/sqrt(k))).
    expected_det = 2 * ell * ell + ell
    assert abs(det_greedi_val - expected_det) < 1e-12, f"Expected det GreeDi = {expected_det}, got {det_greedi_val}"

    # Also check ell=5 deterministic GreeDi ratio: (2*ell^2 + ell) / (ell^2 + ell^3) = 55 / 150 = 11 / 30 = 0.3667
    ell5, m5, k5, mach5, all5, opt5 = make_appendix_b_instance(ell=5)
    S5_union = []
    for i in range(m5):
        S5_union.extend(greedy_cardinality(mach5[i], k5))
    det5_ratio = f_cov(greedy_cardinality(S5_union, k5)) / f_cov(opt5)
    assert abs(det5_ratio - (2.0 * ell5 + 1.0) / (ell5 * ell5 + ell5)) < 1e-12

    # Now run RandGreeDi (Algorithm 2, p. 6) on the ell=3 instance over Monte Carlo trials
    # and verify Lemma 3, Lemma 4, and Theorem 5 / Corollary 6
    rng = random.Random(20261019)
    non_empty_items = [it for it in all_items if len(it[2]) > 0]
    # Compute p_e = Pr_{A ~ V(1/m)}[e in Greedy(A U {e})] for e in OPT (Page 7)
    mc_p = 200
    p_opt = []
    for e_opt in opt_items:
        count_in = 0
        for _ in range(mc_p):
            A_sample = [it for it in non_empty_items if it != e_opt and rng.random() < (1.0 / m)]
            G_Ae = greedy_cardinality(A_sample + [e_opt], k)
            if e_opt in G_Ae:
                count_in += 1
        p_opt.append(count_in / float(mc_p))

    one_minus_p_opt = [1.0 - x for x in p_opt]
    f_minus_p_opt = lovasz_extension_exact(f_cov, opt_items, p_opt)
    f_minus_1_minus_p = lovasz_extension_exact(f_cov, opt_items, one_minus_p_opt)
    # Verify convexity sum property used in Theorem 5 proof (Page 8): f^-(p) + f^-(1_OPT - p) >= f(OPT)
    assert f_minus_p_opt + f_minus_1_minus_p >= opt_val - 1e-9

    # Run RandGreeDi over 200 trials
    trials = 200
    sum_Si = 0.0
    sum_T = 0.0
    sum_D = 0.0
    for _ in range(trials):
        parts = [[] for _ in range(m)]
        for it in non_empty_items:
            parts[rng.randrange(m)].append(it)
        S_union = []
        best_Si = 0.0
        for i in range(m):
            Si = greedy_cardinality(parts[i], k)
            val_Si = f_cov(Si)
            if i == 0:
                sum_Si += val_Si
            best_Si = max(best_Si, val_Si)
            S_union.extend(Si)
        T_sol = greedy_cardinality(S_union, k)
        val_T = f_cov(T_sol)
        val_D = max(val_T, best_Si)
        sum_T += val_T
        sum_D += val_D

    avg_Si = sum_Si / trials
    avg_T = sum_T / trials
    avg_D = sum_D / trials
    alpha = 1.0 - 1.0 / math.e
    assert avg_Si >= alpha * f_minus_1_minus_p - 0.5
    assert avg_T >= alpha * f_minus_p_opt - 0.5
    assert avg_D >= (alpha / 2.0) * opt_val
    assert avg_D > det_greedi_val + 6.0  # RandGreeDi (~29.6) vastly beats deterministic GreeDi (21.0)

    print(
        f"[PASS] Round 361 RandGreeDi (Barbosa et al. 2015): "
        f"homog_err={homog_err:.2e}, det_ratio_l3={det_greedi_val/opt_val:.4f}, "
        f"det_ratio_l5={det5_ratio:.4f}, randgreedi_ratio_l3={avg_D/opt_val:.4f}, "
        f"lovasz_sum={f_minus_p_opt + f_minus_1_minus_p:.4f}>={opt_val:.1f}"
    )


if __name__ == "__main__":
    main()
