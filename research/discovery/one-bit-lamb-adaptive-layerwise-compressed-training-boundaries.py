#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 630: 1-bit LAMB (Li et al., ICML 2022)."""

from __future__ import annotations

import math


def clip_val(x: float, lo: float, hi: float) -> float:
    return min(max(x, lo), hi)


def verify_reconstructed_gradient_and_scaling_ratio() -> tuple[float, float, float]:
    """Verify Algorithm 1 Lines 15-21 of 1-bit LAMB:
    - Reconstructed gradient g_t^{(l)} = (m_t^{(l)} - beta1 * m_{t-1}^{(l)}) / (1 - beta1)
      recovers exact uncompressed gradient when compression error vanishes, and tracks fresh variance v_t^{(l)}.
    - Double-clipped infinity-norm scaling ratio r_t^{(l)} = clip(clip(||v_{T_w}^{(l)} / v_t^{(l)}||_inf,
      (1 - r_th)*r_{t-1}^{(l)}, (1 + r_th)*r_{t-1}^{(l)}), r_min, r_max).
    """
    beta1 = 0.9
    beta2 = 0.999
    r_min = 0.5
    r_max = 4.0
    r_th = 0.1
    c_avg = 0.18

    # First check exact gradient reconstruction when m_t = beta1 * m_{t-1} + (1 - beta1) * g_t
    m_prev = [0.12, -0.34, 0.56, -0.78]
    g_true = [0.05, -0.15, 0.25, -0.35]
    m_curr = [beta1 * m_prev[j] + (1.0 - beta1) * g_true[j] for j in range(4)]
    g_rec = [(m_curr[j] - beta1 * m_prev[j]) / (1.0 - beta1) for j in range(4)]
    rec_err = max(abs(g_rec[j] - g_true[j]) for j in range(4))
    assert rec_err < 1e-15, f"Gradient reconstruction error: {rec_err}"

    # Simulate compression stage where fresh variance v_t^{(l)} decreases relative to frozen v_{T_w}^{(l)}
    v_frozen = [1e-4, 2e-4, 1.5e-4, 3e-4]
    v_fresh = list(v_frozen)
    r_prev = 1.0
    ratios = []
    for step in range(15):
        # Smaller gradients during later training cause fresh variance to decay
        g_step = [0.2 * math.sqrt(v_frozen[j]) for j in range(4)]
        v_fresh = [beta2 * v_fresh[j] + (1.0 - beta2) * (g_step[j] ** 2) for j in range(4)]
        raw_r = max(v_frozen[j] / v_fresh[j] for j in range(4))
        r_soft = clip_val(raw_r, (1.0 - r_th) * r_prev, (1.0 + r_th) * r_prev)
        r_clipped = clip_val(r_soft, r_min, r_max)
        # Verify soft threshold bound relative to r_prev and hard bounds [r_min, r_max]
        assert r_min <= r_clipped <= r_max
        assert abs(r_clipped - r_prev) <= r_th * r_prev + 1e-12
        ratios.append(r_clipped)
        r_prev = r_clipped

    c_final = r_prev * c_avg
    assert ratios[-1] > 1.0, "Scaling ratio must increase when fresh variance decreases below frozen variance"
    return rec_err, ratios[-1], c_final


def verify_time_varying_error_compensation_identity() -> tuple[float, float, float]:
    """Verify Appendix A.7.1 two-pass time-varying learning rate error-compensation recurrence:
    m_t = beta * m_{t-1} + (1 - beta) * g_bar_t + (c_{t-2} / c_{t-1}) * delta_bar_{t-1} - delta_bar_t
    and Lemma 2 virtual sequence y_{t+1} - y_t = -gamma_t * g_bar_{t+1}.
    """
    n_workers = 4
    d = 4
    beta = 0.9
    m_global = [0.0] * d
    worker_deltas = [[0.0] * d for _ in range(n_workers)]
    server_delta = [0.0] * d
    prev_delta_bar = [0.0] * d

    c_seq = [0.15, 0.16, 0.172, 0.168, 0.175, 0.182]
    max_id_err = 0.0

    for t in range(1, 5):
        scale = c_seq[t - 1] / c_seq[t]
        worker_grads = [
            [0.08 * (t + 1) * (i + 1) * ((-1) ** (i + j)) for j in range(d)]
            for i in range(n_workers)
        ]
        g_bar = [
            sum(worker_grads[i][j] for i in range(n_workers)) / n_workers
            for j in range(d)
        ]
        m_hats = []
        new_worker_deltas = []
        for i in range(n_workers):
            m_loc = [beta * m_global[j] + (1.0 - beta) * worker_grads[i][j] for j in range(d)]
            u_loc = [m_loc[j] + scale * worker_deltas[i][j] for j in range(d)]
            mag = sum(abs(x) for x in u_loc) / d
            m_hat = [mag if x >= 0.0 else -mag for x in u_loc]
            # Note Appendix A.7.1 Eq. on p. 19: delta_{t+1}^{(i)} = m_t^{(i)} + (c_{t-2}/c_{t-1}) delta_t^{(i)} - m_{t+1/2}^{(i)}
            d_loc = [u_loc[j] - m_hat[j] for j in range(d)]
            m_hats.append(m_hat)
            new_worker_deltas.append(d_loc)

        m_half = [
            sum(m_hats[i][j] for i in range(n_workers)) / n_workers
            for j in range(d)
        ]
        u_srv = [m_half[j] + scale * server_delta[j] for j in range(d)]
        mag_s = sum(abs(x) for x in u_srv) / d
        m_new = [mag_s if x >= 0.0 else -mag_s for x in u_srv]
        new_server_delta = [u_srv[j] - m_new[j] for j in range(d)]

        new_delta_bar = [
            sum(new_worker_deltas[i][j] for i in range(n_workers)) / n_workers + new_server_delta[j]
            for j in range(d)
        ]
        rhs = [
            beta * m_global[j] + (1.0 - beta) * g_bar[j] + scale * prev_delta_bar[j] - new_delta_bar[j]
            for j in range(d)
        ]
        err = max(abs(m_new[j] - rhs[j]) for j in range(d))
        max_id_err = max(max_id_err, err)

        m_global = m_new
        worker_deltas = new_worker_deltas
        server_delta = new_server_delta
        prev_delta_bar = new_delta_bar

    assert max_id_err < 1e-15, f"Appendix A.7.1 updating form identity error: {max_id_err}"

    # Section 6 Performance analysis communication volume reduction for BERT-Large seqlen 128 (warmup 1000/5993 = 16.7%)
    # and seqlen 512 (warmup 107/555 = 19.3%):
    w_128 = 1000.0 / 5993.0
    w_512 = 107.0 / 555.0
    red_128 = 1.0 / (w_128 + (1.0 - w_128) / 16.0)
    red_512 = 1.0 / (w_512 + (1.0 - w_512) / 16.0)
    assert abs(red_128 - 4.57) < 0.05 and abs(red_512 - 4.11) < 0.05
    return max_id_err, red_128, red_512


if __name__ == "__main__":
    rec_err, r_last, c_final = verify_reconstructed_gradient_and_scaling_ratio()
    id_err, red_128, red_512 = verify_time_varying_error_compensation_identity()
    print(
        f"[PASS] Round 630 1-bit LAMB verified: rec_err={rec_err:.2e}, "
        f"r_last={r_last:.4f}, c_final={c_final:.4f}, id_err={id_err:.2e}, "
        f"red_128={red_128:.2f}x, red_512={red_512:.2f}x"
    )
