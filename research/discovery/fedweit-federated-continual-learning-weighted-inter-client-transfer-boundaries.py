#!/usr/bin/env python3
"""Boundary verification for Round 512: FedWeIT (Yoon et al., ICML 2021).

Verifies:
1. Additive parameter decomposition Eq. (1):
   theta_c^{(t)} = B_c^{(t)} odot m_c^{(t)} + A_c^{(t)} + sum_{i != c} sum_{j < t} alpha_{i,j}^{(t)} A_i^{(j)}.
2. Retroactive update regularization Eq. (2):
   minimizing ||Delta B_c^{(t)} odot m_c^{(i)} + Delta A_c^{(i)}||_2^2 preserves past task effective weights
   theta_c^{(i)} when base parameter B_c drifts from B_c^{(t-1)} to B_c^{(t)}, preventing catastrophic forgetting.
3. Selective attention alpha_{i,j}^{(t)} suppresses negative inter-client interference from incompatible tasks
   while transferring positive knowledge from compatible client tasks, and sparse transmission reduces C2S cost.
"""

import math
import random


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def norm_sq(u):
    return sum(x * x for x in u)


def main():
    rng = random.Random(512)
    d = 24  # parameter dimension

    # 1. Verify retroactive update compensation (Eq. 2) on past task i=1 when learning task t=2
    B_prev = [rng.gauss(0.0, 1.0) for _ in range(d)]
    # Sparse mask m_c^{(1)} with 30% active entries
    m_1 = [1.0 if idx < int(0.3 * d) else 0.0 for idx in range(d)]
    A_1_prev = [rng.gauss(0.0, 0.5) if idx < int(0.25 * d) else 0.0 for idx in range(d)]

    # Effective parameter for task 1 after task 1 finishes:
    theta_1_before = [B_prev[k] * m_1[k] + A_1_prev[k] for k in range(d)]

    # Suppose base parameter drifts to B_curr during task 2 federated aggregation
    B_curr = [B_prev[k] + rng.gauss(0.0, 0.8) for k in range(d)]
    delta_B = [B_curr[k] - B_prev[k] for k in range(d)]

    # Without retroactive update (lambda_2 = 0): A_1 stays A_1_prev, causing forgetting drift
    theta_1_no_retro = [B_curr[k] * m_1[k] + A_1_prev[k] for k in range(d)]
    forgetting_no_retro = math.sqrt(sum((theta_1_no_retro[k] - theta_1_before[k]) ** 2 for k in range(d)))

    # With retroactive update (Eq. 2): optimize Delta A_1 to minimize lambda_2 ||Delta B odot m_1 + Delta A_1||_2^2 + lambda_1 ||A_1||_1
    lam1 = 0.005
    lam2 = 100.0
    delta_A_1 = []
    for k in range(d):
        # Unconstrained minimizer of lam2 * (delta_B[k]*m_1[k] + dA)^2 + lam1 * |A_1_prev[k] + dA|
        target = -delta_B[k] * m_1[k]
        thresh = lam1 / (2.0 * lam2)
        val = A_1_prev[k] + target
        if val > thresh:
            val_shrunk = val - thresh
        elif val < -thresh:
            val_shrunk = val + thresh
        else:
            val_shrunk = 0.0
        delta_A_1.append(val_shrunk - A_1_prev[k])

    A_1_retro = [A_1_prev[k] + delta_A_1[k] for k in range(d)]
    theta_1_retro = [B_curr[k] * m_1[k] + A_1_retro[k] for k in range(d)]
    forgetting_retro = math.sqrt(sum((theta_1_retro[k] - theta_1_before[k]) ** 2 for k in range(d)))

    assert forgetting_retro < 1e-3 and forgetting_no_retro > 1.0, (
        f"Expected retroactive update to eliminate drift: {forgetting_retro} vs {forgetting_no_retro}"
    )

    # 2. Verify weighted inter-client transfer (Eq. 1) vs naive uniform averaging under incompatible tasks
    # Ground-truth target task parameter w_star
    w_star = [math.sin(0.5 * k) for k in range(d)]
    # Knowledge base from 4 other clients: client 0 has aligned task, clients 1..3 have orthogonal/opposite tasks
    kb_A = [
        [0.9 * w_star[k] + rng.gauss(0.0, 0.02) for k in range(d)],
        [-0.8 * w_star[k] + rng.gauss(0.0, 0.1) for k in range(d)],
        [rng.gauss(0.0, 1.0) for _ in range(d)],
        [-0.5 * w_star[k] + rng.gauss(0.0, 0.2) for k in range(d)],
    ]
    # Naive uniform transfer (unweighted mean of all client parameters)
    naive_transfer = [sum(kb_A[i][k] for i in range(4)) / 4.0 for k in range(d)]
    err_naive = math.sqrt(sum((naive_transfer[k] - w_star[k]) ** 2 for k in range(d)))

    # FedWeIT learned attention alpha^{(t)} via gradient descent on squared error ||sum_i alpha_i A_i - w_star||^2
    alpha = [0.25, 0.25, 0.25, 0.25]
    lr = 0.02
    for _ in range(300):
        pred = [sum(alpha[i] * kb_A[i][k] for i in range(4)) for k in range(d)]
        residual = [pred[k] - w_star[k] for k in range(d)]
        grads = [2.0 * dot(residual, kb_A[i]) for i in range(4)]
        alpha = [max(0.0, alpha[i] - lr * grads[i]) for i in range(4)]

    fedweit_transfer = [sum(alpha[i] * kb_A[i][k] for i in range(4)) for k in range(d)]
    err_fedweit = math.sqrt(sum((fedweit_transfer[k] - w_star[k]) ** 2 for k in range(d)))

    assert alpha[0] > 0.9 and max(alpha[1:]) < 0.05, f"Unexpected attention weights: {alpha}"
    assert err_fedweit < 0.15 * err_naive, f"Expected FedWeIT transfer error << naive: {err_fedweit} vs {err_naive}"

    # 3. Verify communication cost formula (Section 3.4):
    # Naive C2S: |C| * R * |theta|; FedWeIT C2S: |C| * (R * |B_hat| + |A|) with 30% B_hat and 3% A
    C, R, P = 5, 20, 1000
    c2s_naive = C * R * P
    c2s_fedweit = C * (R * int(0.30 * P) + int(0.03 * P))
    c2s_ratio = c2s_fedweit / c2s_naive
    assert abs(c2s_ratio - 0.3015) < 1e-6

    print(
        f"[PASS] Round 512 FedWeIT (Yoon et al. 2021): "
        f"forgetting_retro={forgetting_retro:.2e} << forgetting_no_retro={forgetting_no_retro:.3f}, "
        f"alpha0={alpha[0]:.3f}, err_fedweit={err_fedweit:.3f} << err_naive={err_naive:.3f}, "
        f"c2s_ratio={c2s_ratio:.4f}"
    )


if __name__ == "__main__":
    main()
