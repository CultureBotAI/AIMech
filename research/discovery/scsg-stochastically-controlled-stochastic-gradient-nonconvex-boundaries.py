#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 375:
SCSG: Stochastically Controlled Stochastic Gradient for Nonconvex Optimization
(Lei, Ju, Chen, & Jordan 2017, NeurIPS 2017, pp. 2348-2358, arXiv:1706.09156).
"""

import math
import random


def main() -> None:
    rng = random.Random(20261019)

    # 1. Verify Lemma A.2 (Geometric Inner-Loop Telescoping Identity of SCSG):
    # For N ~ Geom(gamma) supported on {0, 1, 2, ...} with P(N = k) = gamma^k (1 - gamma),
    # E[N] = gamma / (1 - gamma) = B_j / b_j when gamma = B_j / (B_j + b_j).
    # For any bounded sequence {D_k}_{k >= 0},
    # E[D_N - D_{N+1}] = \sum_{k=0}^\infty (D_k - D_{k+1}) gamma^k (1 - gamma)
    #                  = (1 - gamma) D_0 - (1 - gamma) \sum_{k=1}^\infty D_k gamma^{k-1} (1 - gamma) / (1 - gamma) * ...
    # Specifically: E[D_{N+1} - D_0] = (gamma / (1 - gamma)) E[D_{N+1} - D_N] = E[N] * E[D_{N+1} - D_N]!
    B_j = 32
    b_j = 4
    gamma = B_j / (B_j + b_j)  # 32/36 = 8/9
    expected_N = gamma / (1.0 - gamma)  # B_j / b_j = 8.0
    assert abs(expected_N - (B_j / b_j)) < 1e-12

    # Verify exact telescoping identity over geometric distribution truncated at K=400:
    D_seq = [math.exp(-0.08 * k) * (1.0 + 0.2 * math.sin(k)) for k in range(405)]
    lhs_step_diff = 0.0
    rhs_epoch_diff = 0.0
    for k in range(400):
        prob_k = (gamma ** k) * (1.0 - gamma)
        lhs_step_diff += prob_k * (D_seq[k] - D_seq[k + 1])
        rhs_epoch_diff += prob_k * (D_seq[0] - D_seq[k])
    # Identity (Lemma A.2): E[N] * E[D_N - D_{N+1}] == E[D_0 - D_N]
    identity_err = abs(expected_N * lhs_step_diff - rhs_epoch_diff)
    assert identity_err < 1e-12, f"Geometric telescoping identity failed: err={identity_err}"

    # 2. Verify Lemma B.1 Variance Bound (Sampling Without Replacement from {1..n}):
    # E ||(1/B) \sum_{i \in I} (v_i - \bar{v})||^2 = ((n - B) / ((n - 1) B)) * (1/n) \sum_{i=1}^n ||v_i - \bar{v}||^2
    # <= (I(B < n) / B) * S^2.
    n = 12
    B_sub = 4
    vecs = [rng.uniform(-2.0, 2.0) for _ in range(n)]
    v_bar = sum(vecs) / n
    pop_var = sum((v - v_bar) ** 2 for v in vecs) / n
    # Exact average over all (n choose B_sub) subsets
    import itertools
    subsets = list(itertools.combinations(vecs, B_sub))
    emp_var = sum(((sum(sub) / B_sub) - v_bar) ** 2 for sub in subsets) / len(subsets)
    exact_wo_replacement = ((n - B_sub) / ((n - 1) * B_sub)) * pop_var * (n / (n))
    # Wait: for population variance pop_var = (1/n)\sum (v_i - v_bar)^2,
    # variance of sample mean without replacement is ((n - B) / (n - 1)) * (pop_var / B).
    assert abs(emp_var - exact_wo_replacement) < 1e-12
    assert emp_var <= pop_var / B_sub

    # 3. Verify SCSG Complexity Bound (Theorem 3.2 & Table 1):
    # To achieve E||\nabla f(x)||^2 <= eps (note: Lei et al. denote target squared norm by eps, i.e. ||\nabla f|| <= \sqrt{\eps}):
    # Batch size B = min{n, eps^{-1}} (or B = \min{n, \eps_grad^{-2}}), b = 1, stepsize \eta = O(B^{-2/3} / L).
    # Total SFO complexity: O(B^{1/3} eps^{-1} + B) = O(\min{eps^{-5/3}, n^{1/3} eps^{-1} + n}) in squared norm eps,
    # or equivalently in gradient norm \eps_g = \sqrt{\eps}: O(\min{\eps_g^{-10/3}, n^{2/3} \eps_g^{-2} + n}).
    # Critically, in the target accuracy regime where eps^{-1} < n (i.e. \eps_g^{-2} < n),
    # SCSG never computes a full pass over n samples (unlike SVRG which requires O(n) at initialization)!
    n_huge = 1_000_000
    eps_sq = 1e-3  # target E||\nabla f||^2 <= 10^-3
    B_scsg = min(n_huge, int(1.0 / eps_sq))  # 1000 << 1,000,000
    cost_scsg = (B_scsg ** (1.0 / 3.0)) / eps_sq + B_scsg  # 10 * 1000 + 1000 = 11,000
    cost_svrg = n_huge + (n_huge ** (2.0 / 3.0)) / eps_sq  # 1,000,000 + 10,000 * 1000 = 11,000,000
    cost_sgd = 1.0 / (eps_sq ** 2)  # 1,000,000
    assert B_scsg < n_huge
    assert cost_scsg < cost_sgd < cost_svrg

    print(
        f"[PASS] Round 375 SCSG (Lei et al. 2017): geom_id_err={identity_err:.2e}, "
        f"wo_repl_var={emp_var:.6f} <= {pop_var/B_sub:.6f}, "
        f"B_scsg={B_scsg} << n={n_huge}, cost_scsg={cost_scsg:.0f} << cost_sgd={cost_sgd:.0f} < cost_svrg={cost_svrg:.0f}"
    )


if __name__ == "__main__":
    main()
