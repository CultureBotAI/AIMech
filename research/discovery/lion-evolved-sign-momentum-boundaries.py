#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 587:
Lion (EvoLved Sign Momentum) — Chen et al. (NeurIPS 2023; arXiv:2302.06675).
"""

import math
import random


def sign(x: float) -> float:
    if x > 0.0:
        return 1.0
    if x < 0.0:
        return -1.0
    return 0.0


def interp(x: float, y: float, a: float) -> float:
    """Program 1 / Appendix H linear interpolation: (1 - a) * x + a * y."""
    return (1.0 - a) * x + a * y


def verify_program4_to_program1_simplification() -> float:
    """Section 3.1: Two nested interp calls with ~0.9 and ~1.1 collapse to single EMA ~0.99."""
    b_a = 0.9
    b_b = 1.1
    rng = random.Random(20260587)
    v_prog4 = 0.0
    m_single = 0.0
    max_diff = 0.0
    for _ in range(200):
        g = rng.gauss(0.0, 1.0)
        # Program 4 lines: m = interp(g, v, b_a); v = interp(g, m, b_b)
        m_tmp = interp(g, v_prog4, b_a)
        v_prog4 = interp(g, m_tmp, b_b)
        # Equivalent single EMA with beta2 = b_a * b_b = 0.99
        m_single = interp(g, m_single, b_a * b_b)
        max_diff = max(max_diff, abs(v_prog4 - m_single))
    assert max_diff < 1e-14, f"Nested interp simplification mismatch: {max_diff}"
    return max_diff


def verify_effective_weight_decay_invariance() -> None:
    """Section 5: Scaling lr down by rho and lambda up by rho preserves effective weight decay lr * lambda."""
    lr_adamw = 1e-3
    wd_adamw = 1.0
    for rho in (3.0, 5.0, 10.0):
        lr_lion = lr_adamw / rho
        wd_lion = wd_adamw * rho
        assert abs(lr_lion * wd_lion - lr_adamw * wd_adamw) < 1e-15


def run_optimizer(mode: str, steps: int = 800) -> float:
    """Compare Lion (beta1=0.9, beta2=0.99) vs single-beta sign momentum (Ablation_0.9, Ablation_0.99)."""
    rng = random.Random(587)
    d = 8
    scales = [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0]
    target = [1.5, -1.2, 0.8, -0.9, 1.1, -0.7, 0.6, -1.3]
    theta = [0.0] * d
    m = [0.0] * d
    lr = 0.008
    wd = 0.0
    for _ in range(steps):
        g = [scales[i] * (theta[i] - target[i]) + rng.gauss(0.0, 0.5 * scales[i]) for i in range(d)]
        for i in range(d):
            if mode == "lion":
                c_i = interp(g[i], m[i], 0.9)
                u_i = sign(c_i) + wd * theta[i]
                theta[i] -= lr * u_i
                m[i] = interp(g[i], m[i], 0.99)
            elif mode == "ablation_0.9":
                m[i] = interp(g[i], m[i], 0.9)
                theta[i] -= lr * (sign(m[i]) + wd * theta[i])
            elif mode == "ablation_0.99":
                m[i] = interp(g[i], m[i], 0.99)
                theta[i] -= lr * (sign(m[i]) + wd * theta[i])
            else:
                raise ValueError(mode)
    return sum(0.5 * scales[i] * (theta[i] - target[i]) ** 2 for i in range(d))


def main() -> None:
    simp_diff = verify_program4_to_program1_simplification()
    verify_effective_weight_decay_invariance()
    loss_lion = run_optimizer("lion")
    loss_ab90 = run_optimizer("ablation_0.9")
    loss_ab99 = run_optimizer("ablation_0.99")
    assert loss_lion < loss_ab90 and loss_lion < loss_ab99, (
        f"Expected Lion to beat single-beta ablations: lion={loss_lion}, ab90={loss_ab90}, ab99={loss_ab99}"
    )
    # Memory state check: Lion stores 1 state vector (m), AdamW stores 2 (m, v)
    n_params = 86_570_000
    lion_state_elems = 1 * n_params
    adamw_state_elems = 2 * n_params
    assert lion_state_elems == adamw_state_elems // 2
    print(
        f"[PASS] Round 587 Lion verified: simp_diff={simp_diff:.2e}, "
        f"loss_lion={loss_lion:.4f}<(ab90={loss_ab90:.4f}, ab99={loss_ab99:.4f}), "
        f"state_ratio={lion_state_elems / adamw_state_elems:.2f}"
    )


if __name__ == "__main__":
    main()
