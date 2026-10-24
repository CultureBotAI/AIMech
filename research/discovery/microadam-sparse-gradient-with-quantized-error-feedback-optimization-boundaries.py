#!/usr/bin/env python3
"""Constructed boundary verification for Round 639: MicroAdam (Modoranu et al., NeurIPS 2024)."""

from __future__ import annotations
import math


def verify_lemma1_quantizer_and_memory_footprint() -> tuple[float, float, float, float]:
    """Verify Section 3.2 memory formula M_muA(m) = 0.5d + 4mk and Section 4.1 Lemma 1 unbiasedness & omega bound."""
    # Section 3.2 & Appendix D memory footprint for LLaMA-2 7B (d = 6,738,415,616)
    d = 6_738_415_616
    k = math.ceil(d / 100)  # 1% density (99% sparsity)
    m = 10  # sliding window size

    m_aw32_gb = (8.0 * d) / (2**30)
    m_aw16_gb = (4.0 * d) / (2**30)
    m_aw8_gb = (2.0 * d) / (2**30)
    m_mua_gb = (0.5 * d + 4.0 * m * k) / (2**30)

    assert abs(m_aw32_gb - 50.21) < 0.01
    assert abs(m_aw16_gb - 25.10) < 0.01
    assert abs(m_aw8_gb - 12.55) < 0.01
    assert abs(m_mua_gb - 5.65) < 0.01

    # Verify break-even window size m_max where M_muA(m_max) == M_AW8 (0.5d + 4 * m_max * (d/100) = 2d -> m_max = 37.5)
    m_max = (2.0 - 0.5) / (4.0 * 0.01)
    assert abs(m_max - 37.5) < 1e-12

    # Verify Lemma 1 exact analytical expectation E[x_hat_i] = x_i and variance/norm bound for b = 4 bits:
    # For any x_i in [delta, Delta], let z = (x_i - delta) / u = m_int + frac where m_int = floor(z) and frac in [0, 1).
    # Then floor(z + xi) equals m_int + 1 with probability frac, and m_int with probability 1 - frac,
    # so E_xi[floor(z + xi) * u + delta] = (m_int + frac) * u + delta = z * u + delta = x_i identically!
    x = [-1.5, -0.4, 0.0, 0.25, 0.7, 1.1, 1.8, 2.5]
    d_vec = len(x)
    b_bits = 4
    delta = min(x)
    cap_delta = max(x)
    u = (cap_delta - delta) / ((2**b_bits) - 1)

    max_unbiased_err = 0.0
    max_quant_sq_err = 0.0
    for xi in x:
        z = (xi - delta) / u
        m_int = math.floor(z)
        frac = z - m_int
        expected_x_hat = (frac * (m_int + 1) + (1.0 - frac) * m_int) * u + delta
        max_unbiased_err = max(max_unbiased_err, abs(expected_x_hat - xi))
        # Worst-case deterministic or stochastic rounding error on interior coordinates is <= u^2
        if xi in (delta, cap_delta):
            assert abs(frac) < 1e-14 or abs(frac - 1.0) < 1e-14
        else:
            max_quant_sq_err += u * u

    assert max_unbiased_err < 1e-15, f"Quantizer must be exactly unbiased: {max_unbiased_err}"
    norm_x = math.sqrt(sum(v * v for v in x))
    omega = (math.sqrt(d_vec - 2) / ((2**b_bits) - 1)) * ((cap_delta - delta) / math.sqrt(cap_delta**2 + delta**2))
    assert math.sqrt(max_quant_sq_err) <= omega * norm_x + 1e-14

    return m_mua_gb, m_aw8_gb, m_max, omega


def verify_sliding_window_adamstats_and_contraction_lemma3() -> tuple[float, float, float]:
    """Verify Algorithm 2 unrolled circular-buffer ADAMSTATS equivalence and Appendix E.1 Lemma 3 error bound."""
    # Verify Algorithm 2 ADAMSTATS unrolled circular window matches exact Adam EMA when window m == t
    d = 6
    k = 2
    m_win = 5
    beta1 = 0.9
    beta2 = 0.999

    # Ring buffer of size m_win x k
    ring_idx = [[0] * k for _ in range(m_win)]
    ring_val = [[0.0] * k for _ in range(m_win)]
    m_exact = [0.0] * d
    v_exact = [0.0] * d

    max_m_err = 0.0
    max_v_err = 0.0
    for t in range(1, m_win + 1):
        # Construct Top-k sparse gradient g_tilde at step t
        idx_t = [(2 * t) % d, (2 * t + 1) % d]
        val_t = [0.5 * t, -0.3 * t]
        slot = (t - 1) % m_win
        ring_idx[slot] = idx_t
        ring_val[slot] = val_t

        # Exact recursion
        g_dense = [0.0] * d
        for j in range(k):
            g_dense[idx_t[j]] = val_t[j]
        m_exact = [beta1 * m_exact[c] + (1.0 - beta1) * g_dense[c] for c in range(d)]
        v_exact = [beta2 * v_exact[c] + (1.0 - beta2) * (g_dense[c] ** 2) for c in range(d)]
        m_hat_exact = [v / (1.0 - (beta1**t)) for v in m_exact]
        v_hat_exact = [v / (1.0 - (beta2**t)) for v in v_exact]

        # Algorithm 2 ADAMSTATS dynamic unrolled reconstruction over circular buffer
        z_m = [0.0] * d
        z_v = [0.0] * d
        for i_step in range(1, min(t, m_win) + 1):
            r_exp = t - i_step
            buf_row = (i_step - 1) % m_win
            for j in range(k):
                col = ring_idx[buf_row][j]
                val = ring_val[buf_row][j]
                z_m[col] += (beta1**r_exp) * val
                z_v[col] += (beta2**r_exp) * (val * val)
        m_hat_win = [(1.0 - beta1) * v / (1.0 - (beta1**t)) for v in z_m]
        v_hat_win = [(1.0 - beta2) * v / (1.0 - (beta2**t)) for v in z_v]

        max_m_err = max(max_m_err, max(abs(m_hat_exact[c] - m_hat_win[c]) for c in range(d)))
        max_v_err = max(max_v_err, max(abs(v_hat_exact[c] - v_hat_win[c]) for c in range(d)))

    assert max_m_err < 1e-15 and max_v_err < 1e-15

    # Verify Lemma 3 bounded error feedback under joint contraction q_omega = (1 + omega) * q < 1
    q = math.sqrt(1.0 - 2.0 / 6.0)  # Top-2 in R^6 -> q = sqrt(2/3) ≈ 0.8165
    omega = 0.08  # 4-bit quantizer relative error bound
    q_omega = (1.0 + omega) * q
    assert q_omega < 1.0
    g_bound = 1.5
    lemma3_e_sq_bound = (4.0 * (q_omega**2) / ((1.0 - (q_omega**2)) ** 2)) * (g_bound**2)

    # Simulate worst-case recursion ||e_{t+1}||^2 <= ((1 + q_omega^2)/2) ||e_t||^2 + (2 q_omega^2 / (1 - q_omega^2)) G^2
    e_sq = 0.0
    for _ in range(200):
        e_sq = 0.5 * (1.0 + q_omega**2) * e_sq + (2.0 * (q_omega**2) / (1.0 - q_omega**2)) * (g_bound**2)
        assert e_sq <= lemma3_e_sq_bound + 1e-12

    return max_m_err, q_omega, lemma3_e_sq_bound


if __name__ == "__main__":
    m_mua, m_aw8, m_mx, omg = verify_lemma1_quantizer_and_memory_footprint()
    m_err, qw, e_bnd = verify_sliding_window_adamstats_and_contraction_lemma3()
    print(
        f"[PASS] Round 639 MicroAdam verified: M_muA={m_mua:.2f}GB < M_AW8={m_aw8:.2f}GB (m_max={m_mx:.1f}), "
        f"omega={omg:.4f}, adamstats_err={m_err:.2e}, q_omega={qw:.4f}<1, lemma3_bound={e_bnd:.2f}"
    )
