#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 377:
signSGD and Majority-Vote Compressed Non-Convex Optimization
(Bernstein, Wang, Azizzadenesheli, & Anandkumar 2018, ICML 2018, PMLR 80:560-569, arXiv:1802.04434).
"""

import math
import random


def main() -> None:
    rng = random.Random(20261019)

    # 1. Verify l1/l2 Geometry Density Ratio \phi(v) = ||v||_1^2 / (d ||v||_2^2) (Section 3):
    # By Cauchy-Schwarz and norm equivalence, 1/d <= \phi(v) <= 1.
    # For sparse 1-hot vector e_1, \phi(e_1) = 1/d (worst case for sign descent).
    # For dense vector (1, 1, ..., 1), \phi(1) = 1, where ||v||_1 = \sqrt{d} ||v||_2.
    d = 64
    v_sparse = [1.0] + [0.0] * (d - 1)
    v_dense = [1.0 if i % 2 == 0 else -1.0 for i in range(d)]

    def phi_ratio(v: list[float]) -> float:
        l1 = sum(abs(x) for x in v)
        l2_sq = sum(x * x for x in v)
        return (l1 * l1) / (len(v) * l2_sq)

    phi_sp = phi_ratio(v_sparse)
    phi_dn = phi_ratio(v_dense)
    assert abs(phi_sp - (1.0 / d)) < 1e-12
    assert abs(phi_dn - 1.0) < 1e-12

    # 2. Verify Lemma 1 (Single-Worker Sign Error Probability Bound via Cantelli & Unimodal Gauss Inequality):
    # For coordinate i with signal-to-noise ratio S_i = |g_i| / (\sigma_i / \sqrt{n_batch}):
    # General zero-mean variance-\sigma_i^2 noise (Cantelli inequality):
    # P(sign(\tilde{g}_i) != sign(g_i)) <= 1 / (1 + S_i^2) <= 1 / S_i^2 (and <= 1/2 when S_i >= 1).
    # Unimodal symmetric noise (Gauss inequality):
    # P(sign(\tilde{g}_i) != sign(g_i)) <= 2 / (9 S_i^2) when S_i >= 2/\sqrt{3}, else <= 1/2 - S_i/(2\sqrt{3}).
    # Consequently, E[|g_i| * I(sign(\tilde{g}_i) != sign(g_i))] <= \sigma_i / \sqrt{n_batch}!
    sigma_i = 1.2
    n_batch = 9
    eff_sigma = sigma_i / math.sqrt(n_batch)  # 0.4
    for g_i in [0.05, 0.2, 0.4, 0.8, 1.6, 3.2]:
        S_i = abs(g_i) / eff_sigma
        # Exact Gaussian tail probability Phi(-S_i) = 0.5 * erfc(S_i / sqrt(2))
        prob_err_gauss = 0.5 * math.erfc(S_i / math.sqrt(2.0))
        if S_i >= 2.0 / math.sqrt(3.0):
            gauss_ub = 2.0 / (9.0 * (S_i ** 2))
        else:
            gauss_ub = 0.5 - S_i / (2.0 * math.sqrt(3.0))
        assert prob_err_gauss <= gauss_ub + 1e-12
        # Verify Lemma 1 key inequality: |g_i| * P(sign(\tilde{g}_i) != sign(g_i)) <= eff_sigma
        expected_loss_i = abs(g_i) * prob_err_gauss
        assert expected_loss_i <= eff_sigma

    # 3. Verify Theorem 2 (Distributed Majority Vote of M Workers):
    # Let M workers each compute sign(\tilde{g}_{m,i}) with single-worker error probability p = P(sign != sign(g_i)) < 1/2.
    # Majority vote Aggregates \text{sign}(\sum_{m=1}^M \text{sign}(\tilde{g}_{m,i})).
    # By Bernstein's Theorem 2 (Cantelli bound applied to sum of M independent Bernoulli(1-p) variables),
    # the majority vote error probability scales as O(1 / (M S_i^2)), reducing effective noise by 1/\sqrt{M}
    # using only 1-bit communication in both directions!
    M = 15
    g_val = 0.35
    S_single = g_val / eff_sigma
    p_single = 0.5 * math.erfc(S_single / math.sqrt(2.0))
    # Exact binomial probability that >= (M+1)//2 workers have wrong sign:
    prob_maj_err = 0.0
    for k in range((M + 1) // 2, M + 1):
        prob_maj_err += math.comb(M, k) * (p_single ** k) * ((1.0 - p_single) ** (M - k))
    assert prob_maj_err < p_single

    # 4. Verify Counterexample / Boundary Limitation of Biased 1-Bit SignSGD without Mini-batching:
    # When batch size = 1 and stochastic gradients are asymmetric zero-mean in expectation at x* (\nabla f(x*) = 0),
    # E[sign(\tilde{g}(x*))] != 0, so constant-or-small-batch signSGD can fail to converge to x*!
    # Example: \tilde{g} = +2 w.p. 1/3, and \tilde{g} = -1 w.p. 2/3 -> E[\tilde{g}] = 0,
    # but E[sign(\tilde{g})] = (1/3)*(+1) + (2/3)*(-1) = -1/3 != 0!
    mean_grad = (1.0 / 3.0) * 2.0 + (2.0 / 3.0) * (-1.0)
    mean_sign = (1.0 / 3.0) * (+1.0) + (2.0 / 3.0) * (-1.0)
    assert abs(mean_grad) < 1e-12 and abs(mean_sign - (-1.0 / 3.0)) < 1e-12

    print(
        f"[PASS] Round 377 signSGD (Bernstein et al. 2018): phi_sparse={phi_sp:.4f} vs phi_dense={phi_dn:.4f}, "
        f"p_single={p_single:.4f} -> p_maj(M={M})={prob_maj_err:.4f}, asymmetric_sign_bias={mean_sign:.4f}"
    )


if __name__ == "__main__":
    main()
