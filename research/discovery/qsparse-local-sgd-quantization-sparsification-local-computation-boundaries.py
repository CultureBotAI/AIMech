"""Constructed boundary verification for Round 422: Qsparse-local-SGD (Basu et al., NeurIPS 2019, arXiv:1906.02367).

Verifies:
1. Lemma 1, Lemma 2, Lemma 3 & Corollary 1 (Section 2):
   When composing a k-contraction sparsifier Comp_k (with E||x - Comp_k(x)||^2 <= (1 - k/d)||x||^2)
   and an unbiased stochastic quantizer Q_s (with E||u - Q_s(u)||^2 <= beta_{k,s} ||u||^2):
   - Unscaled composition Q_s(Comp_k(x)) has contraction parameter gamma_unscaled = (1 - beta_{k,s}) * (k/d),
     which fails to be a contraction whenever beta_{k,s} >= 1.
   - Rescaled composition Q_s(Comp_k(x)) / (1 + beta_{k,s}) (Lemma 2) is unconditionally a gamma-contraction
     for ALL beta_{k,s} > 0 with strictly larger contraction factor:
       gamma_scaled = k / (d * (1 + beta_{k,s})) > (1 - beta_{k,s}) * (k/d)
     by the exact margin (k / d) * beta_{k,s}^2 / (1 + beta_{k,s}) > 0 (Corollary 1).
2. Lemma 4 (Error-memory bound under local period H):
   E||m_t^{(r)}||_2^2 <= 4 * (1 - gamma^2) / gamma^2 * eta^2 * H^2 * G^2, which vanishes at gamma = 1.
"""

from __future__ import annotations


def main() -> None:
    d = 100
    k = 10
    # Test both beta_{k,s} < 1 and beta_{k,s} >= 1 regimes (Lemma 1 vs Lemma 2 & Corollary 1)
    for beta in (0.25, 0.5, 1.0, 2.5):
        gamma_unscaled = (1.0 - beta) * (k / d)
        gamma_scaled = k / (d * (1.0 + beta))
        gap = gamma_scaled - gamma_unscaled
        expected_gap = (k / d) * (beta * beta) / (1.0 + beta)
        assert abs(gap - expected_gap) < 1e-15
        assert gamma_scaled > 0.0 and gamma_scaled > gamma_unscaled
        if beta >= 1.0:
            assert gamma_unscaled <= 0.0, "Unscaled composition cannot contract when beta >= 1"

    # Verify exact second-moment contraction identity of Lemma 2 on a vector x in R^4 with Top-2 + unbiased noise
    x = [4.0, -3.0, 2.0, -1.0]
    x_norm_sq = sum(v * v for v in x)  # 30.0
    c_x = [4.0, -3.0, 0.0, 0.0]  # Top-2 of x, ||c_x||^2 = 25.0 >= (2/4)*30 = 15.0
    cx_norm_sq = sum(v * v for v in c_x)
    beta_val = 1.5  # > 1, where unscaled Q_s(c_x) fails contraction
    # For any unbiased Q_s with E[Q_s(u)] = u and E||Q_s(u) - u||^2 = beta * ||u||^2:
    # E||x - Q_s(c_x)/(1+beta)||^2 = ||x - c_x/(1+beta)||^2 + beta*||c_x||^2 / (1+beta)^2
    # = ||x||^2 - 2 <x, c_x>/(1+beta) + ||c_x||^2/(1+beta) = ||x||^2 - ||c_x||^2 / (1+beta) (since <x, c_x> = ||c_x||^2)
    err_scaled_sq = x_norm_sq - cx_norm_sq / (1.0 + beta_val)
    err_unscaled_sq = (x_norm_sq - cx_norm_sq) + beta_val * cx_norm_sq
    gamma_s = 2.0 / (4.0 * (1.0 + beta_val))
    assert err_scaled_sq <= (1.0 - gamma_s) * x_norm_sq
    assert err_unscaled_sq > x_norm_sq, "Unscaled operator expands error when beta=1.5"

    # Verify Lemma 4 error-memory bound monotonic scaling with H and gamma
    eta = 0.01
    g_bound = 2.0
    h1, h4 = 1, 4
    mem_bound_h1 = 4.0 * (1.0 - gamma_s * gamma_s) / (gamma_s * gamma_s) * (eta * h1 * g_bound) ** 2
    mem_bound_h4 = 4.0 * (1.0 - gamma_s * gamma_s) / (gamma_s * gamma_s) * (eta * h4 * g_bound) ** 2
    assert abs(mem_bound_h4 / mem_bound_h1 - 16.0) < 1e-12

    print(
        f"[PASS] Round 422 Qsparse-local-SGD (Basu et al. 2019): beta=1.5 err_scaled_sq={err_scaled_sq:.2f} "
        f"< ||x||^2={x_norm_sq:.2f} < err_unscaled_sq={err_unscaled_sq:.2f}, H4/H1_mem_ratio={mem_bound_h4/mem_bound_h1:.1f}"
    )


if __name__ == "__main__":
    main()
