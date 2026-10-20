"""Constructed mathematical boundary and property verification for Round 611:
NovoGrad (Ginsburg et al., 2019, arXiv:1905.11286).

Verifies:
1. Algorithm 1 and Eqs. 4-6 (Section 3, p. 2-3):
   - Bias-removing t = 1 initialization: v_1^l = ||g_1^l||_2^2 => ||g_1^l / sqrt(v_1^l)||_2 = 1.0 (exact unit L2 norm).
   - Special case beta_2 = 0 (Note 1, p. 3): v_t^l = ||g_t^l||_2^2 reduces NovoGrad to layer-wise
     Stochastic Normalized Gradient Descent (SNGD) with momentum and decoupled weight decay.
2. Outlier gradient spike robustness (Note 2, p. 3):
   - Normalizing g_t^l by sqrt(v_t^l) before accumulating into m_t^l bounds the L2 norm of the
     normalized gradient contribution ||g_t^l / sqrt(v_t^l)||_2 <= 1 / sqrt(1 - beta_2) for any
     arbitrarily large outlier spike ||g_t^l||_2 -> infinity, whereas unnormalized momentum suffers
     an unbounded spike.
3. AMSGrad monotonic variant (Section 3, p. 3):
   - v_hat_t^l = max(v_hat_{t-1}^l, v_t^l) guarantees non-increasing effective layer step size
     lambda_t / sqrt(v_hat_t^l) whenever lambda_t is non-increasing.
4. Optimizer state memory reduction (Section 2.3 & Note 3, p. 2-3):
   - For L layers of shape (n_l, m_l) with total parameters P = sum_l n_l * m_l, Adam stores 2P
     floats (m_t and v_t), whereas NovoGrad stores P + L floats (m_t^l and scalar v_t^l per layer),
     achieving a 2x memory footprint reduction as n_l, m_l grow.
"""

from __future__ import annotations

import math
import random


def l2_norm(v: list[float]) -> float:
    return math.sqrt(sum(x * x for x in v))


def verify_novograd_properties() -> tuple[float, float, float, float, float]:
    rng = random.Random(20261019)
    d_layer = 16
    T = 30
    beta1 = 0.95
    beta2 = 0.25  # NovoGrad default beta2 = 0.25 (Footnote 1, p. 2)
    wd = 0.002
    lr = 0.01
    eps = 1e-8

    # 1. Verify bias-removing t=1 initialization and beta2=0 SNGD equivalence (Note 1, p. 3)
    w_novo = [rng.uniform(-0.5, 0.5) for _ in range(d_layer)]
    w_sngd = w_novo[:]
    m_novo = [0.0] * d_layer
    m_sngd = [0.0] * d_layer
    v_novo = 0.0

    grads = [[rng.uniform(-2.0, 2.0) for _ in range(d_layer)] for _ in range(T)]
    t1_unit_norm_err = 0.0

    for t in range(1, T + 1):
        g = grads[t - 1]
        g_norm_sq = sum(x * x for x in g)
        if t == 1:
            v_b2_zero = g_norm_sq
            norm_g1 = [x / math.sqrt(v_b2_zero) for x in g]
            t1_unit_norm_err = abs(l2_norm(norm_g1) - 1.0)
            m_novo = [norm_g1[i] + wd * w_novo[i] for i in range(d_layer)]
        else:
            # With beta2 = 0, v_t^l = ||g_t^l||_2^2
            v_b2_zero = g_norm_sq
            m_novo = [
                beta1 * m_novo[i] + (g[i] / (math.sqrt(v_b2_zero) + eps) + wd * w_novo[i])
                for i in range(d_layer)
            ]
        w_novo = [w_novo[i] - lr * m_novo[i] for i in range(d_layer)]

        # Direct layer-wise SNGD with momentum and decoupled weight decay
        g_unit = [
            x / (l2_norm(g) + (0.0 if t == 1 else eps)) for x in g
        ]
        if t == 1:
            m_sngd = [g_unit[i] + wd * w_sngd[i] for i in range(d_layer)]
        else:
            m_sngd = [beta1 * m_sngd[i] + (g_unit[i] + wd * w_sngd[i]) for i in range(d_layer)]
        w_sngd = [w_sngd[i] - lr * m_sngd[i] for i in range(d_layer)]

    sngd_equiv_err = max(abs(w_novo[i] - w_sngd[i]) for i in range(d_layer))
    assert t1_unit_norm_err < 1e-15
    assert sngd_equiv_err < 1e-15

    # 2. Verify outlier gradient spike bound (Note 2, p. 3):
    # For any gradient spike g_spike with ||g_spike||_2 = 1e6,
    # ||g_spike / sqrt(beta2 * v_{t-1} + (1 - beta2) ||g_spike||_2^2)||_2 <= 1 / sqrt(1 - beta2)
    v_prev = 1.0
    g_spike = [1e6 / math.sqrt(d_layer)] * d_layer
    v_curr = beta2 * v_prev + (1.0 - beta2) * sum(x * x for x in g_spike)
    normalized_spike_norm = l2_norm([x / math.sqrt(v_curr) for x in g_spike])
    theoretical_spike_cap = 1.0 / math.sqrt(1.0 - beta2)
    assert normalized_spike_norm <= theoretical_spike_cap + 1e-12
    assert abs(normalized_spike_norm - theoretical_spike_cap) < 1e-6

    # 3. Verify AMSGrad monotonic layer-wise step size (Section 3, p. 3):
    v_run = 0.0
    vhat_run = 0.0
    prev_eff_lr = float("inf")
    for t in range(1, T + 1):
        g = grads[t - 1]
        g_norm_sq = sum(x * x for x in g)
        v_run = g_norm_sq if t == 1 else (beta2 * v_run + (1.0 - beta2) * g_norm_sq)
        vhat_run = v_run if t == 1 else max(vhat_run, v_run)
        lam_t = lr * 0.5 * (1.0 + math.cos(math.pi * t / T))  # cosine annealing
        eff_lr = lam_t / math.sqrt(vhat_run)
        assert eff_lr <= prev_eff_lr + 1e-15
        prev_eff_lr = eff_lr

    # 4. Verify optimizer state memory ratio on a 12-layer Transformer-big (d_model=1024, d_ff=4096)
    layers = [(1024, 1024)] * 48 + [(1024, 4096), (4096, 1024)] * 12
    total_params = sum(r * c for r, c in layers)
    adam_state_floats = 2 * total_params
    novograd_state_floats = total_params + len(layers)
    mem_ratio = novograd_state_floats / adam_state_floats
    assert 0.50 <= mem_ratio < 0.50001

    return t1_unit_norm_err, sngd_equiv_err, normalized_spike_norm, theoretical_spike_cap, mem_ratio


if __name__ == "__main__":
    u_err, s_err, sp_norm, sp_cap, m_rat = verify_novograd_properties()
    print(
        f"[PASS] Round 611 NovoGrad verified: "
        f"t1_unit_err={u_err:.2e}, sngd_equiv_err={s_err:.2e}, "
        f"spike_norm={sp_norm:.6f}<=cap={sp_cap:.6f}, mem_ratio={m_rat:.6f}"
    )
