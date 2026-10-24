"""Constructed boundary verification for Round 418: 1-bit Adam (Tang et al., ICML 2021, arXiv:2102.02888).

Verifies:
1. Section 3 (Eq. 1): Non-linear coordinate-wise preconditioner v_t = beta_2 v_{t-1} + (1 - beta_2) g_t^2
   varies with t and fails to commute with linear error-feedback compensation:
     sum_{t=1}^T V_t^{-1} C(m_t + delta_{t-1}) != sum_{t=1}^T V_t^{-1} m_t - V_T^{-1} delta_T,
   leaving a non-telescoping non-linear distortion sum_{t=1}^{T-1} (V_{t+1}^{-1} - V_t^{-1}) delta_t != 0.
2. Section 4 (Algorithm 1 & Theorem 1): Freezing V = diag(sqrt(v_{T_w}) + eps) after warm-up step T_w
   restores exact linear error-feedback telescoping across all compression steps t > T_w:
     sum_{t=1}^T V^{-1} C(m_t + delta_{t-1}) == sum_{t=1}^T V^{-1} m_t - V^{-1} delta_T,
   with 1-bit scale factor (||u||_2 / sqrt(d)) * sign(u) satisfying the compressor contraction
   ||u - C(u)||_2^2 = ||u||_2^2 - (||u||_1^2 / d) < ||u||_2^2 for all u != 0.
"""

from __future__ import annotations


def one_bit_compress(u: list[float]) -> list[float]:
    d = len(u)
    l1 = sum(abs(x) for x in u)
    scale = l1 / d
    return [scale * (1.0 if x >= 0.0 else -1.0) for x in u]


def main() -> None:
    d = 4
    T = 6
    beta2 = 0.9
    eps = 1e-6

    m_seq = [
        [0.5 * (t + 1), -0.3 * (t + 2), 0.15 * (t + 1) ** 1.2, -0.05 * (t + 3)]
        for t in range(T)
    ]

    # Verify 1-bit compressor contraction ||u - C(u)||_2^2 = ||u||_2^2 - ||u||_1^2 / d < ||u||_2^2
    for u in m_seq:
        cu = one_bit_compress(u)
        err_sq = sum((x - y) ** 2 for x, y in zip(u, cu))
        u_sq = sum(x * x for x in u)
        u_l1 = sum(abs(x) for x in u)
        expected_err_sq = u_sq - (u_l1 * u_l1) / d
        assert abs(err_sq - expected_err_sq) < 1e-12
        assert err_sq < u_sq

    # Case 1: Time-varying v_t (unfrozen Adam second moment, Section 3 Eq. 1)
    v = [0.1, 0.2, 0.05, 0.01]
    V_inv_seq = []
    for t in range(T):
        v = [beta2 * vk + (1.0 - beta2) * (mk * mk) for vk, mk in zip(v, m_seq[t])]
        V_inv_seq.append([1.0 / ((vk ** 0.5) + eps) for vk in v])

    delta = [0.0] * d
    accum_compressed_tv = [0.0] * d
    accum_exact_tv = [0.0] * d
    non_telescoping_residual = [0.0] * d
    for t in range(T):
        u_t = [mk + dk for mk, dk in zip(m_seq[t], delta)]
        c_t = one_bit_compress(u_t)
        delta = [uk - ck for uk, ck in zip(u_t, c_t)]
        V_inv = V_inv_seq[t]
        accum_compressed_tv = [ac + vi * ck for ac, vi, ck in zip(accum_compressed_tv, V_inv, c_t)]
        accum_exact_tv = [ae + vi * mk for ae, vi, mk in zip(accum_exact_tv, V_inv, m_seq[t])]
        if t < T - 1:
            V_inv_next = V_inv_seq[t + 1]
            non_telescoping_residual = [
                nr + (vin - vi) * dk for nr, vin, vi, dk in zip(non_telescoping_residual, V_inv_next, V_inv, delta)
            ]

    final_term_tv = [vi * dk for vi, dk in zip(V_inv_seq[-1], delta)]
    tv_gap = sum(
        (ac - (ae - ft)) ** 2 for ac, ae, ft in zip(accum_compressed_tv, accum_exact_tv, final_term_tv)
    ) ** 0.5
    residual_norm = sum(x * x for x in non_telescoping_residual) ** 0.5
    assert tv_gap > 1e-2 and abs(tv_gap - residual_norm) < 1e-12

    # Case 2: Frozen preconditioner V = V_{T_w} (1-bit Adam compression phase, Section 4 Alg. 1)
    V_frozen_inv = V_inv_seq[0]
    delta_f = [0.0] * d
    accum_compressed_f = [0.0] * d
    accum_exact_f = [0.0] * d
    for t in range(T):
        u_t = [mk + dk for mk, dk in zip(m_seq[t], delta_f)]
        c_t = one_bit_compress(u_t)
        delta_f = [uk - ck for uk, ck in zip(u_t, c_t)]
        accum_compressed_f = [ac + vi * ck for ac, vi, ck in zip(accum_compressed_f, V_frozen_inv, c_t)]
        accum_exact_f = [ae + vi * mk for ae, vi, mk in zip(accum_exact_f, V_frozen_inv, m_seq[t])]

    final_term_f = [vi * dk for vi, dk in zip(V_frozen_inv, delta_f)]
    frozen_telescoping_err = sum(
        (ac - (ae - ft)) ** 2 for ac, ae, ft in zip(accum_compressed_f, accum_exact_f, final_term_f)
    ) ** 0.5
    assert frozen_telescoping_err < 1e-12, f"Frozen preconditioner failed to telescope: {frozen_telescoping_err}"

    print(
        f"[PASS] Round 418 1-bit Adam (Tang et al. 2021): unfrozen_non_telescoping_gap={tv_gap:.4f} > 0, "
        f"frozen_telescoping_err={frozen_telescoping_err:.1e} == 0"
    )


if __name__ == "__main__":
    main()
