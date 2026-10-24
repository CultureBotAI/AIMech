#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 470:
FedMix (Approximation of Mixup under Mean Augmented Federated Learning,
Yoon, Shin, Hwang, & Yang 2021, ICLR 2021, arXiv:2107.00233).

Verifies:
1. Exact linearity identity in Proposition 1 & Equation (5): averaging the
   first-order Taylor approximation of Global Mixup over a batch J of M private
   samples {(x_j, y_j)}_{j in J} from another client depends ONLY on the sample
   means x_bar_j = (1/|J|) sum_{j in J} x_j and y_bar_j = (1/|J|) sum_{j in J} y_j:
     (1/|J|) sum_{j in J} [ (1 - lam) ell(f((1 - lam) x_i), y_i)
                            + lam ell(f((1 - lam) x_i), y_j)
                            + lam <d ell / d x |_{(1-lam)x_i, y_i}, x_j> ]
     == (1 - lam) ell(f((1 - lam) x_i), y_i)
        + lam ell(f((1 - lam) x_i), y_bar_j)
        + lam <d ell / d x |_{(1-lam)x_i, y_i}, x_bar_j>.
2. O(lam^2) approximation accuracy between exact Global Mixup loss (Equation 3)
   averaged over J and the FedMix loss (Equation 5) as lam -> 0, and strict
   separation from NaiveMix (Equation 1), which evaluates f((1-lam)x_i + lam x_bar_j)
   inside the nonlinear network and lacks the input-Jacobian term lam (d ell / d x) . x_bar_j.
"""

from __future__ import annotations
import math


def softmax(logits: list[float]) -> list[float]:
    m = max(logits)
    exps = [math.exp(z - m) for z in logits]
    s = sum(exps)
    return [e / s for e in exps]


def cross_entropy(probs: list[float], target: list[float]) -> float:
    return -sum(y * math.log(max(p, 1e-15)) for p, y in zip(probs, target))


def forward_two_layer(x: list[float], W1: list[list[float]], W2: list[list[float]]) -> list[float]:
    # Smooth tanh hidden layer + linear logits -> softmax probabilities
    h = [math.tanh(sum(w * xi for w, xi in zip(row, x))) for row in W1]
    logits = [sum(w * hi for w, hi in zip(row, h)) for row in W2]
    return softmax(logits)


def input_grad_ce(
    x_eval: list[float],
    y_target: list[float],
    W1: list[list[float]],
    W2: list[list[float]],
) -> list[float]:
    # Exact analytical derivative d ell(f(x), y_target) / dx evaluated at x = x_eval
    h_raw = [sum(w * xi for w, xi in zip(row, x_eval)) for row in W1]
    h = [math.tanh(u) for u in h_raw]
    logits = [sum(w * hi for w, hi in zip(row, h)) for row in W2]
    probs = softmax(logits)
    # d ell / d logits = probs - y_target (since sum(y_target) = 1)
    d_logits = [p - y for p, y in zip(probs, y_target)]
    # d ell / d h_k = sum_c d_logits[c] * W2[c][k]
    d_h = [sum(d_logits[c] * W2[c][k] for c in range(len(W2))) for k in range(len(W1))]
    # d h_k / d u_k = 1 - tanh^2(u_k)
    d_u = [dh_k * (1.0 - hk * hk) for dh_k, hk in zip(d_h, h)]
    # d ell / d x_d = sum_k d_u[k] * W1[k][d]
    dim = len(x_eval)
    return [sum(d_u[k] * W1[k][d] for k in range(len(W1))) for d in range(dim)]


def main() -> None:
    W1 = [
        [0.6, -0.4, 0.3],
        [-0.5, 0.7, 0.2],
        [0.4, 0.3, -0.6],
        [0.2, -0.5, 0.8],
    ]
    W2 = [
        [0.8, -0.3, 0.5, -0.2],
        [-0.4, 0.7, -0.2, 0.6],
        [0.3, -0.5, 0.6, -0.4],
    ]

    x_i = [0.7, -0.3, 0.5]
    y_i = [1.0, 0.0, 0.0]

    # Batch J of M=4 private instances on client j
    J_x = [
        [-0.6, 0.8, -0.2],
        [-0.4, 0.5, 0.1],
        [-0.8, 0.9, -0.4],
        [-0.2, 0.6, 0.3],
    ]
    J_y = [
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.5, 0.5],
    ]
    M = len(J_x)
    x_bar = [sum(J_x[m][d] for m in range(M)) / M for d in range(3)]
    y_bar = [sum(J_y[m][c] for m in range(M)) / M for c in range(3)]

    lam = 0.05
    x_scaled = [(1.0 - lam) * xi for xi in x_i]
    probs_scaled = forward_two_layer(x_scaled, W1, W2)
    grad_x = input_grad_ce(x_scaled, y_i, W1, W2)

    # 1. Verify exact equality in Equation (5): instance-averaged Proposition 1 == mean-input FedMix
    per_instance_approx = []
    for x_j, y_j in zip(J_x, J_y):
        l1 = (1.0 - lam) * cross_entropy(probs_scaled, y_i)
        l2 = lam * cross_entropy(probs_scaled, y_j)
        l3 = lam * sum(g * xjd for g, xjd in zip(grad_x, x_j))
        per_instance_approx.append(l1 + l2 + l3)
    lhs_eq5 = sum(per_instance_approx) / M

    rhs_l1 = (1.0 - lam) * cross_entropy(probs_scaled, y_i)
    rhs_l2 = lam * cross_entropy(probs_scaled, y_bar)
    rhs_l3 = lam * sum(g * xbd for g, xbd in zip(grad_x, x_bar))
    rhs_eq5 = rhs_l1 + rhs_l2 + rhs_l3
    assert abs(lhs_eq5 - rhs_eq5) < 1e-14, f"Eq (5) linearity failed: {lhs_eq5} vs {rhs_eq5}"

    # 2. Verify O(lam^2) Taylor convergence to exact Global Mixup (Eq 3) & separation from NaiveMix (Eq 1)
    errors = []
    for test_lam in [0.1, 0.05, 0.025]:
        xs = [(1.0 - test_lam) * xi for xi in x_i]
        ps = forward_two_layer(xs, W1, W2)
        gx = input_grad_ce(xs, y_i, W1, W2)
        fedmix_loss = (
            (1.0 - test_lam) * cross_entropy(ps, y_i)
            + test_lam * cross_entropy(ps, y_bar)
            + test_lam * sum(g * xbd for g, xbd in zip(gx, x_bar))
        )
        global_mixup_loss = 0.0
        for x_j, y_j in zip(J_x, J_y):
            x_tilde = [(1.0 - test_lam) * xi + test_lam * xjd for xi, xjd in zip(x_i, x_j)]
            y_tilde = [(1.0 - test_lam) * yi + test_lam * yjd for yi, yjd in zip(y_i, y_j)]
            global_mixup_loss += cross_entropy(forward_two_layer(x_tilde, W1, W2), y_tilde)
        global_mixup_loss /= M
        errors.append(abs(global_mixup_loss - fedmix_loss))

    # Error must shrink roughly quadratically (~4x per halving of lam)
    ratio_1 = errors[0] / errors[1]
    ratio_2 = errors[1] / errors[2]
    assert 3.5 < ratio_1 < 4.5 and 3.7 < ratio_2 < 4.3, f"Expected O(lam^2) scaling, got ratios {ratio_1}, {ratio_2}"

    # 3. Verify NaiveMix (Eq 1) differs from FedMix (Eq 5)
    x_naivemix = [(1.0 - lam) * xi + lam * xbd for xi, xbd in zip(x_i, x_bar)]
    p_naivemix = forward_two_layer(x_naivemix, W1, W2)
    naivemix_loss = (1.0 - lam) * cross_entropy(p_naivemix, y_i) + lam * cross_entropy(p_naivemix, y_bar)
    assert abs(rhs_eq5 - naivemix_loss) > 1e-4, "FedMix and NaiveMix must be distinct on nonlinear networks"

    print(
        f"[PASS] FedMix boundary verification passed: Eq5_diff={abs(lhs_eq5 - rhs_eq5):.2e}, "
        f"O(lam^2)_ratios=({ratio_1:.2f}, {ratio_2:.2f}), |FedMix-NaiveMix|={abs(rhs_eq5 - naivemix_loss):.4e}"
    )


if __name__ == "__main__":
    main()
