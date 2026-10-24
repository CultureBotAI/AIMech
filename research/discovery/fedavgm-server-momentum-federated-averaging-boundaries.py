#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 502: FedAvgM (Hsu, Qi, & Brown, 2019 / arXiv:1909.06335)."""

import math


def dirichlet_variance(alpha: float, num_classes: int = 10) -> float:
    """Analytical variance of class probability q_i ~ Dir(alpha * p) with uniform prior p_i = 1/N (Section 3, p. 2).
    For symmetric Dirichlet with parameters a_i = alpha * (1/N), alpha_0 = sum_i a_i = alpha:
    Var(q_i) = (1/N) * (1 - 1/N) / (alpha + 1).
    """
    p_i = 1.0 / num_classes
    return p_i * (1.0 - p_i) / (alpha + 1.0)


def run_heterogeneous_fl(beta: float, eta_eff: float, rounds: int = 60) -> float:
    """Simulate alternating partial client participation on non-IID client objectives with server momentum (Section 4.2, p. 4).
    Server update:
      Delta_w = sum_{k=1}^K (n_k / n) * Delta_w_k
      v <- beta * v + Delta_w
      w <- w - v
    With effective learning rate eta_eff = eta / (1 - beta), client learning rate is scaled as eta = (1 - beta) * eta_eff.
    """
    eta = (1.0 - beta) * eta_eff
    # 4 clients with heterogeneous targets [-3.0, 3.0, -2.0, 2.0] whose global optimum is w* = 0.0.
    # In each communication round t, only 1 skewed client participates cyclicly (simulating severe non-IID partial participation).
    targets = [-3.0, 3.0, -2.0, 2.0]
    w = 1.5
    v = 0.0
    local_steps = 5
    for t in range(rounds):
        c = t % len(targets)
        wc = w
        for _ in range(local_steps):
            grad = wc - targets[c]
            wc = wc - eta * grad
        # Delta_w = w_old - w_new (so w_new = w_old - Delta_w when beta=0)
        delta_w = w - wc
        v = beta * v + delta_w
        w = w - v
    return abs(w - 0.0)


def main() -> None:
    # 1. Verify Dirichlet non-identical client synthesis boundary limits (Section 3, p. 2):
    # As alpha -> infinity, Var(q_i) -> 0 (identical clients); as alpha -> 0, Var(q_i) -> p_i(1 - p_i) (one-class clients).
    var_large_alpha = dirichlet_variance(1e6, num_classes=10)
    var_small_alpha = dirichlet_variance(1e-6, num_classes=10)
    assert var_large_alpha < 1e-7
    assert math.isclose(var_small_alpha, 0.09, rel_tol=1e-5)

    # 2. Verify FedAvgM reduction to vanilla FedAvg at beta = 0 and effective learning rate scaling eta_eff = eta / (1 - beta) (Section 4.2, p. 4)
    err_fedavg = run_heterogeneous_fl(beta=0.0, eta_eff=0.08, rounds=80)
    err_fedavgm = run_heterogeneous_fl(beta=0.9, eta_eff=0.08, rounds=80)
    assert err_fedavgm < err_fedavg

    # 3. Verify that without (1 - beta) scaling (fixing raw eta = 0.08 at beta = 0.9 -> eta_eff = 0.8),
    # large effective step size causes larger oscillation than properly scaled eta = (1 - beta) * eta_eff
    err_unscaled = run_heterogeneous_fl(beta=0.9, eta_eff=0.8, rounds=80)
    assert err_fedavgm < err_unscaled

    print(
        f"[PASS] Round 502 FedAvgM (Hsu, Qi, & Brown, 2019): "
        f"Dirichlet Var(alpha=1e-6)={var_small_alpha:.4f}, Var(alpha=1e6)={var_large_alpha:.2e}, "
        f"err_fedavg(beta=0)={err_fedavg:.4f} -> err_fedavgm(beta=0.9)={err_fedavgm:.4f} (unscaled={err_unscaled:.4f})"
    )


if __name__ == "__main__":
    main()
