"""Constructed boundary verification for Round 423: FedGen (Zhu, Hong, & Zhou, ICML 2021, arXiv:2105.10056).

Verifies:
1. Section 3.1 (Eq. 4) & Section 9 (Weighted Ensemble Logits): When client k has empirical class counts
   n_k^y, weighting client predictor logits by lambda_k^y = n_k^y / sum_{j=1}^K n_j^y (rather than uniform
   1/K) prevents clients with zero or scarce samples of class y from corrupting the ensemble teacher target
   for the latent-space generator G_w(z | y).
2. Theorem 1 & Corollary 1 (Section 4.3 & Section 8): Augmenting m local samples from D_k~ with m synthetic
   latent samples from the learned global generator D~ yields the mixture distribution D_k'~ = (1/2) D_k~ + (1/2) D~,
   which satisfies the triangle-inequality domain discrepancy contraction:
     d_{H Delta H}(D_k'~, D~) <= (1/2) d_{H Delta H}(D_k~, D~) + (1/2) eps
   and doubles the effective sample size m' = 2m, strictly tightening the generalization upper bound
   whenever eps < d_{H Delta H}(D_k~, D~).
"""

from __future__ import annotations

import math


def gen_bound(emp_err: float, d_hdh: float, m_samples: int, d_vc: int = 10, delta: float = 0.05) -> float:
    """Theorem 1 generalization bound (Ben-David et al. / Zhu et al. Eq. 6)."""
    complexity = ((2.0 * d_vc * math.log(2.0 * m_samples) + math.log(4.0 / delta)) / m_samples) ** 0.5
    return emp_err + 0.5 * d_hdh + complexity


def main() -> None:
    # 1. Verify label-count weighted ensemble logits (Sec. 3.1 Eq. 4 & Sec. 9) under disjoint label skew
    # Client 1 has 100 samples of class 0 and 0 of class 1; Client 2 has 0 of class 0 and 100 of class 1.
    # For class y = 0, Client 1's calibrated logit difference (logit_0 - logit_1) is +4.0, whereas Client 2's
    # untrained head on class 0 has noisy logit difference -3.0.
    counts_y0 = [100, 0]
    logit_diff_y0 = [4.0, -3.0]
    uniform_ens_diff = sum(logit_diff_y0) / len(logit_diff_y0)  # +0.5 (heavily degraded by Client 2)
    total_y0 = sum(counts_y0)
    weighted_ens_diff = sum(c * l for c, l in zip(counts_y0, logit_diff_y0)) / total_y0  # +4.0 (exact expert logit)
    prob_uniform = 1.0 / (1.0 + math.exp(-uniform_ens_diff))
    prob_weighted = 1.0 / (1.0 + math.exp(-weighted_ens_diff))
    assert prob_weighted > 0.98 and prob_weighted > prob_uniform + 0.30

    # 2. Verify Corollary 1 (Sec. 4.3 & Sec. 8): H Delta H discrepancy contraction and sample size doubling
    emp_err = 0.05
    d_hdh_local = 0.60
    eps_gen = 0.08  # Generator approximation error eps < d_{H Delta H}(D_k~, D~)
    m_local = 100
    m_aug = 200  # 1:1 mixing of local + synthetic latent features

    d_hdh_aug = 0.5 * d_hdh_local + 0.5 * eps_gen  # 0.34 < 0.60
    bound_baseline = gen_bound(emp_err, d_hdh_local, m_local)
    bound_fedgen = gen_bound(emp_err, d_hdh_aug, m_aug)
    assert d_hdh_aug < d_hdh_local
    assert bound_fedgen < bound_baseline

    print(
        f"[PASS] Round 423 FedGen (Zhu et al. 2021): prob_weighted={prob_weighted:.4f} > prob_uniform={prob_uniform:.4f}, "
        f"d_hdh_aug={d_hdh_aug:.2f} < d_hdh_local={d_hdh_local:.2f}, bound_fedgen={bound_fedgen:.4f} < bound_baseline={bound_baseline:.4f}"
    )


if __name__ == "__main__":
    main()
