#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 405:
IFCA: Iterative Federated Clustering Algorithm
(Ghosh, Chung, Yin, & Ramchandran, NeurIPS 2020, Vol. 33, pp. 19586-19597).
"""

import math
import random


def main():
    rng = random.Random(405)
    d = 4
    k = 3
    m = 30  # 10 clients per cluster
    n_prime = 40  # local samples per step
    sigma = 0.15

    # Ground-truth cluster parameters theta^*_j in R^d with separation Delta
    theta_star = [
        [2.0, 0.0, 0.0, 0.0],
        [-1.0, math.sqrt(3.0), 0.0, 0.0],
        [-1.0, -math.sqrt(3.0), 0.0, 0.0],
    ]
    true_cluster = [i % k for i in range(m)]

    # Generate two independent local datasets (D_i for cluster ID estimation, D'_i for gradient update)
    D_assign = []
    D_grad = []
    for i in range(m):
        j_star = true_cluster[i]
        xi_a, yi_a = [], []
        xi_g, yi_g = [], []
        for _ in range(n_prime):
            x1 = [rng.gauss(0.0, 1.0) for _ in range(d)]
            y1 = sum(x1[c] * theta_star[j_star][c] for c in range(d)) + rng.gauss(0.0, sigma)
            xi_a.append(x1)
            yi_a.append(y1)

            x2 = [rng.gauss(0.0, 1.0) for _ in range(d)]
            y2 = sum(x2[c] * theta_star[j_star][c] for c in range(d)) + rng.gauss(0.0, sigma)
            xi_g.append(x2)
            yi_g.append(y2)
        D_assign.append((xi_a, yi_a))
        D_grad.append((xi_g, yi_g))

    # Initialize theta^{(0)}_j within basin ||theta^{(0)}_j - theta^*_j|| <= alpha * Delta
    theta_ifca = [
        [theta_star[j][c] + 0.45 * rng.gauss(0.0, 1.0) for c in range(d)]
        for j in range(k)
    ]
    init_max_dist = max(
        math.sqrt(sum((theta_ifca[j][c] - theta_star[j][c]) ** 2 for c in range(d)))
        for j in range(k)
    )

    # Run IFCA (Algorithm 2, gradient averaging option)
    gamma = 0.85  # step size scaled by cluster proportion p_j = 1/3
    misclass_history = []
    dist_history = [init_max_dist]

    for _ in range(25):
        # 1. Local cluster identity estimation: j_hat_i = argmin_j F_i(theta_j)
        r = [[0] * k for _ in range(m)]
        misclassified = 0
        for i in range(m):
            X_a, Y_a = D_assign[i]
            losses = []
            for j in range(k):
                loss_j = sum(
                    (sum(X_a[s][c] * theta_ifca[j][c] for c in range(d)) - Y_a[s]) ** 2
                    for s in range(n_prime)
                ) / n_prime
                losses.append(loss_j)
            j_hat = min(range(k), key=lambda j: losses[j])
            r[i][j_hat] = 1
            if j_hat != true_cluster[i]:
                misclassified += 1
        misclass_history.append(misclassified / m)

        # 2. Cluster-specific gradient averaging: theta_j^{(t+1)} = theta_j^{(t)} - (gamma / m) sum_i r_{i,j} grad F_i(theta_j^{(t)})
        for j in range(k):
            grad_sum = [0.0] * d
            for i in range(m):
                if r[i][j] == 1:
                    X_g, Y_g = D_grad[i]
                    for s in range(n_prime):
                        err = sum(X_g[s][c] * theta_ifca[j][c] for c in range(d)) - Y_g[s]
                        for c in range(d):
                            grad_sum[c] += (2.0 / n_prime) * err * X_g[s][c]
            for c in range(d):
                theta_ifca[j][c] -= (gamma / m) * grad_sum[c]

        max_dist = max(
            math.sqrt(sum((theta_ifca[j][c] - theta_star[j][c]) ** 2 for c in range(d)))
            for j in range(k)
        )
        dist_history.append(max_dist)

    # Compare against single global FedAvg model (which converges to average of clusters 1/k sum_j theta^*_j = 0)
    theta_fedavg = [0.0] * d
    for _ in range(25):
        grad_all = [0.0] * d
        for i in range(m):
            X_g, Y_g = D_grad[i]
            for s in range(n_prime):
                err = sum(X_g[s][c] * theta_fedavg[c] for c in range(d)) - Y_g[s]
                for c in range(d):
                    grad_all[c] += (2.0 / n_prime) * err * X_g[s][c]
        for c in range(d):
            theta_fedavg[c] -= (0.25 / m) * grad_all[c]

    fedavg_dist = max(
        math.sqrt(sum((theta_fedavg[c] - theta_star[j][c]) ** 2 for c in range(d)))
        for j in range(k)
    )

    assert misclass_history[-1] == 0.0, f"IFCA misclassification rate did not reach 0: {misclass_history[-1]}"
    assert dist_history[-1] < 0.06 and dist_history[-1] < 0.1 * init_max_dist
    assert fedavg_dist > 1.9

    print(
        f"[PASS] Round 405 IFCA (Ghosh et al. 2020): "
        f"init_dist={init_max_dist:.4f}->final_dist={dist_history[-1]:.4f}, "
        f"misclass={misclass_history[-1]:.2f}, fedavg_dist={fedavg_dist:.4f}"
    )


if __name__ == "__main__":
    main()
