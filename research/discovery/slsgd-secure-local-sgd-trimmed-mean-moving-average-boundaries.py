#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 535:
SLSGD: Secure Local Stochastic Gradient Descent with Trimmed Mean and Moving Average
(Xie, Koyejo, & Gupta, ECML-PKDD 2019, pp. 213-228 / arXiv:1903.06996).
"""

import math


def l2_norm(v):
    return math.sqrt(sum(x * x for x in v))


def trmean_b(models, b):
    """Definition 3: Coordinate-wise b-trimmed mean over k models in R^d."""
    k = len(models)
    assert 0 <= 2 * b < k
    d = len(models[0])
    out = [0.0] * d
    for j in range(d):
        col = sorted(m[j] for m in models)
        trimmed = col[b : k - b]
        out[j] = sum(trimmed) / (k - 2 * b)
    return out


def beta_factor(n, k, b, q):
    """Theorem 2 error factor: beta = 1 + 1/(k-q) - 1/n + k(k+b)/(k-b-q)^2."""
    return 1.0 + 1.0 / (k - q) - 1.0 / n + (k * (k + b)) / ((k - b - q) ** 2)


def run_slsgd(use_option_ii=True, alpha=0.6, b=2, q=2, epochs=50):
    """Simulate Algorithm 1 (SLSGD) on non-IID local quadratics with heterogeneous H_t^i
    and q poisoned workers executing the Proposition 1 model-replacement attack.
    """
    d = 4
    k = 10
    gamma = 0.08
    # True global optimum x_star = [2.0, -1.5, 1.0, -0.5]
    x_star = [2.0, -1.5, 1.0, -0.5]
    # Non-IID local biases summing to zero across the 8 honest workers
    biases = [
        [0.4, -0.3, 0.2, -0.1],
        [-0.4, 0.3, -0.2, 0.1],
        [0.2, 0.2, -0.3, 0.3],
        [-0.2, -0.2, 0.3, -0.3],
        [0.3, -0.1, 0.1, -0.2],
        [-0.3, 0.1, -0.1, 0.2],
        [0.1, -0.2, 0.2, -0.1],
        [-0.1, 0.2, -0.2, 0.1],
    ]
    # Heterogeneous local iterations H_t^i in {3, 4, 5, 6} (H_min = 3)
    local_iters = [3, 4, 5, 6, 3, 5, 4, 6]

    x_t = [0.0] * d
    target_poison = [50.0, -50.0, 50.0, -50.0]

    for _ in range(epochs):
        honest_models = []
        for i in range(k - q):
            x_loc = list(x_t)
            loc_opt = [x_star[j] + biases[i][j] for j in range(d)]
            for _h in range(local_iters[i]):
                # Local gradient of 0.5 * ||x - loc_opt||^2 is (x - loc_opt)
                x_loc = [x_loc[j] - gamma * (x_loc[j] - loc_opt[j]) for j in range(d)]
            honest_models.append(x_loc)

        # Proposition 1 attack: q poisoned workers push -(k-q)/q * mean(honest) + c
        mean_honest = [
            sum(m[j] for m in honest_models) / len(honest_models) for j in range(d)
        ]
        poison_models = []
        for _ in range(q):
            p_m = [
                -((k - q) / q) * mean_honest[j] + (k / q) * target_poison[j]
                for j in range(d)
            ]
            poison_models.append(p_m)

        all_models = honest_models + poison_models
        if not use_option_ii:
            # Option I: arithmetic mean
            x_prime = [sum(m[j] for m in all_models) / k for j in range(d)]
        else:
            # Option II: coordinate-wise b-trimmed mean
            x_prime = trmean_b(all_models, b=b)

        # Line 15: Global moving average update
        x_t = [(1.0 - alpha) * x_t[j] + alpha * x_prime[j] for j in range(d)]

    return x_t, l2_norm([x_t[j] - x_star[j] for j in range(d)])


def main():
    # 1. Verify Proposition 1: Option I with alpha=1 (FedAvg / Local SGD) is hijacked to target_poison
    x_fedavg, err_fedavg = run_slsgd(use_option_ii=False, alpha=1.0, b=0, q=2, epochs=1)
    target_poison = [50.0, -50.0, 50.0, -50.0]
    dist_to_poison = l2_norm([x_fedavg[j] - target_poison[j] for j in range(4)])
    assert dist_to_poison < 1e-10, f"Expected exact hijack in 1 epoch, got {dist_to_poison}"
    assert err_fedavg > 95.0

    # 2. Verify Theorem 2: SLSGD Option II (b=2, alpha=0.6) converges to bounded neighborhood of x_star
    _, err_slsgd = run_slsgd(use_option_ii=True, alpha=0.6, b=2, q=2, epochs=60)
    assert err_slsgd < 0.20, f"Expected SLSGD error < 0.20, got {err_slsgd}"

    # 3. Verify Theorem 2 beta factor monotonicity with respect to q and b
    b_q1 = beta_factor(n=100, k=10, b=2, q=1)
    b_q2 = beta_factor(n=100, k=10, b=2, q=2)
    b_b4 = beta_factor(n=100, k=10, b=4, q=2)
    assert b_q1 < b_q2 < b_b4

    print(
        f"[PASS] Round 535 SLSGD verified: err_slsgd={err_slsgd:.5f} << err_fedavg={err_fedavg:.2f}, "
        f"beta(q=1,b=2)={b_q1:.3f} < beta(q=2,b=2)={b_q2:.3f} < beta(q=2,b=4)={b_b4:.3f}"
    )


if __name__ == "__main__":
    main()
