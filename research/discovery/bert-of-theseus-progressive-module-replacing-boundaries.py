#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 805:
BERT-of-Theseus: Compressing BERT by Progressive Module Replacing
(Xu, Zhou, Ge, Wei, & Zhou, EMNLP 2020, arXiv:2002.02925).

Verifies:
1. Module-replacing forward dynamics (Eqs. 2-3):
   r_{i+1} ~ Bernoulli(p_d), y_{i+1} = r_{i+1} * scc_i(y_i) + (1 - r_{i+1}) * prd_i(y_i)
   Over n=6 modules, there are 2^n = 64 distinct hybrid predecessor/successor pathways; the expected
   output under independent Bernoulli(p_d) module replacement for linear or expectation-commuting
   modules smoothly interpolates between pure predecessor (p_d=0) and pure successor (p_d=1).
2. Linear curriculum replacement scheduler (Eq. 6):
   p_d(t) = min(1, k * t + b) with k > 0, b in [0, 1), reaches p_d(t) = 1 at t* = (1 - b) / k,
   at which point all predecessor modules are deterministically eliminated (pure successor phase).
3. Unified view with learning-rate warmup (Eq. 7):
   Because prd_i weights are frozen and scc_i receives gradients only when r_{i+1} = 1 (which occurs
   with probability p_d(t)), the expected effective learning rate on scc_i at step t is
   E[lr'_t] = p_d(t) * lr = min(1, k * t + b) * lr, inducing an automatic curriculum warmup on
   successor parameters without requiring any intermediate feature/attention distillation loss terms.
"""

import json


def replacement_prob(t, k, b):
    """Eq. 6: p_d(t) = min(1.0, k * t + b)."""
    return min(1.0, k * t + b)


def module_step(y, r_bit, prd_fn, scc_fn):
    """Eq. 3: y_{i+1} = r_{i+1} * scc_i(y_i) + (1 - r_{i+1}) * prd_i(y_i)."""
    assert r_bit in (0, 1)
    return r_bit * scc_fn(y) + (1 - r_bit) * prd_fn(y)


def enumerate_hybrid_expectation(y0, p_d, prd_fns, scc_fns):
    """Exact expectation over all 2^n Bernoulli module replacement paths."""
    n = len(prd_fns)
    expected_y = 0.0
    total_prob = 0.0
    for mask in range(1 << n):
        y = y0
        prob = 1.0
        for i in range(n):
            r_bit = (mask >> i) & 1
            prob *= p_d if r_bit == 1 else (1.0 - p_d)
            y = module_step(y, r_bit, prd_fns[i], scc_fns[i])
        expected_y += prob * y
        total_prob += prob
    assert abs(total_prob - 1.0) < 1e-12
    return expected_y


def main():
    n = 6
    # Define 6 2-layer predecessor modules and 6 1-layer successor modules
    prd_fns = [lambda y, a=1.05 + 0.01 * i, c=0.1 * (i + 1): a * y + c for i in range(n)]
    scc_fns = [lambda y, a=1.02 + 0.01 * i, c=0.08 * (i + 1): a * y + c for i in range(n)]

    y0 = 1.0
    # At p_d = 0.0, hybrid network is 100% predecessor
    y_prd_only = enumerate_hybrid_expectation(y0, 0.0, prd_fns, scc_fns)
    y_prd_direct = y0
    for fn in prd_fns:
        y_prd_direct = fn(y_prd_direct)
    assert abs(y_prd_only - y_prd_direct) < 1e-12

    # At p_d = 1.0, hybrid network is 100% successor
    y_scc_only = enumerate_hybrid_expectation(y0, 1.0, prd_fns, scc_fns)
    y_scc_direct = y0
    for fn in scc_fns:
        y_scc_direct = fn(y_scc_direct)
    assert abs(y_scc_only - y_scc_direct) < 1e-12

    # Verify monotonic interpolation across curriculum steps t with b=0.1, k=0.0001
    b = 0.1
    k = 0.0001
    t_transition = int(round((1.0 - b) / k))  # 9000 steps
    assert abs(replacement_prob(0, k, b) - 0.1) < 1e-12
    assert abs(replacement_prob(4500, k, b) - 0.55) < 1e-12
    assert abs(replacement_prob(t_transition, k, b) - 1.0) < 1e-12
    assert abs(replacement_prob(t_transition + 2000, k, b) - 1.0) < 1e-12

    y_mid = enumerate_hybrid_expectation(y0, replacement_prob(4500, k, b), prd_fns, scc_fns)
    assert y_scc_only < y_mid < y_prd_only

    # Verify Eq. 7 expected effective learning rate warmup lr'(t) = min(1, k*t + b) * lr
    base_lr = 2e-5
    lr_t0 = replacement_prob(0, k, b) * base_lr
    lr_t4500 = replacement_prob(4500, k, b) * base_lr
    lr_t9000 = replacement_prob(t_transition, k, b) * base_lr
    assert lr_t0 < lr_t4500 < lr_t9000 == base_lr

    summary = {
        "concept": "BERToftheseusCompressingBERTByProgressiveModuleReplacing",
        "num_modules": n,
        "num_hybrid_paths": 1 << n,
        "y_predecessor_only": round(y_prd_only, 6),
        "y_hybrid_mid_curriculum": round(y_mid, 6),
        "y_successor_only": round(y_scc_only, 6),
        "curriculum_transition_step": t_transition,
        "effective_lr_t0": lr_t0,
        "effective_lr_t9000": lr_t9000,
        "status": "ok",
    }
    print(json.dumps(summary))


if __name__ == "__main__":
    main()
