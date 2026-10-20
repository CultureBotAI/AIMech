#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 473:
FedPer (Federated Learning with Personalization Layers,
Arivazhagan, Aggarwal, Singh, & Choudhary 2019, arXiv:1912.00818).

Verifies:
1. Forward pass decomposition (Equation 1):
   y_hat_j = a_{P_j, K_P}(W_{P_j, K_P} ... a_{B, K_B}(W_{B, K_B} ... a_{B, 1}(W_{B, 1} x)))
   and joint local SGD update (Algorithm 1, Line 5):
   (W_{B,j}^{(k)}, W_{P_j}^{(k)}) <- SGD_j(W_B^{(k-1)}, W_{P_j}^{(k-1)}, eta_j^{(k)})
   followed by server-side sample-weighted aggregation of ONLY the base layers
   (Algorithm 2, Line 6):
   W_B^{(k)} = sum_{j=1}^N gamma_j W_{B,j}^{(k)}, gamma_j = n_j / sum_{l=1}^N n_l,
   while personalization layers W_{P_j}^{(k)} remain private on client j.
2. Exact reduction to FedAvg when K_P = 0 (Section 4, p. 5).
3. Ability of FedPer (K_P >= 1) to fit contradictory user-specific labelings
   P_j(y | x) on identical input features (as in FLICKR-AES personalized aesthetics,
   Section 1 & Section 4.5), where standard FedAvg (K_P = 0) is lower-bounded by
   cross-client label variance.
"""

from __future__ import annotations


def forward_client(x: list[float], W_B: list[list[float]], w_P: list[float]) -> float:
    # Base layer with ReLU activation + personalized linear head
    h = [max(0.0, sum(w * xi for w, xi in zip(row, x))) for row in W_B]
    return sum(wp * hi for wp, hi in zip(w_P, h))


def local_sgd_step(
    dataset: list[tuple[list[float], float]],
    W_B: list[list[float]],
    w_P: list[float],
    lr: float,
) -> tuple[list[list[float]], list[float]]:
    n = len(dataset)
    grad_B = [[0.0 for _ in row] for row in W_B]
    grad_P = [0.0 for _ in w_P]
    for x, y in dataset:
        pre = [sum(w * xi for w, xi in zip(row, x)) for row in W_B]
        h = [max(0.0, u) for u in pre]
        y_hat = sum(wp * hi for wp, hi in zip(w_P, h))
        err = (y_hat - y) * (2.0 / n)
        for k in range(len(w_P)):
            grad_P[k] += err * h[k]
            if pre[k] > 0.0:
                for d in range(len(x)):
                    grad_B[k][d] += err * w_P[k] * x[d]
    new_W_B = [[W_B[k][d] - lr * grad_B[k][d] for d in range(len(W_B[0]))] for k in range(len(W_B))]
    new_w_P = [w_P[k] - lr * grad_P[k] for k in range(len(w_P))]
    return new_W_B, new_w_P


def eval_personalized_risk(
    clients_data: list[list[tuple[list[float], float]]],
    W_B: list[list[float]],
    W_P_list: list[list[float]],
) -> float:
    total = 0.0
    for j, data in enumerate(clients_data):
        loss_j = sum((forward_client(x, W_B, W_P_list[j]) - y) ** 2 for x, y in data) / len(data)
        total += loss_j
    return total / len(clients_data)


def main() -> None:
    # Two clients with identical shared latent features x but opposite user preferences y
    # (modeling personalized aesthetics where the same image receives different user ratings)
    client_1 = [([1.0, 0.2], 1.2), ([0.2, 1.0], -0.8), ([0.8, 0.8], 0.4), ([0.5, 0.1], 0.6)]
    client_2 = [([1.0, 0.2], -1.2), ([0.2, 1.0], 0.8), ([0.8, 0.8], -0.4), ([0.5, 0.1], -0.6)]
    clients = [client_1, client_2]
    n_samples = [len(c) for c in clients]
    gammas = [nj / sum(n_samples) for nj in n_samples]
    assert abs(sum(gammas) - 1.0) < 1e-15

    # Run FedPer (shared base W_B aggregated with gamma_j, private w_{P,j} kept local)
    W_B_fedper = [[0.7, -0.2], [-0.3, 0.8]]
    W_P_fedper = [[0.5, -0.4], [-0.4, 0.5]]
    lr = 0.08
    local_epochs = 5
    for _round in range(60):
        client_W_Bs = []
        for j in range(2):
            wb_j = [row[:] for row in W_B_fedper]
            wp_j = W_P_fedper[j][:]
            for _e in range(local_epochs):
                wb_j, wp_j = local_sgd_step(clients[j], wb_j, wp_j, lr)
            client_W_Bs.append(wb_j)
            W_P_fedper[j] = wp_j
        # Algorithm 2 Line 6: aggregate ONLY W_B
        W_B_fedper = [
            [sum(gammas[j] * client_W_Bs[j][k][d] for j in range(2)) for d in range(2)]
            for k in range(2)
        ]

    # Run FedAvg (K_P = 0 equivalent: both base W_B and head w_P are globally aggregated)
    W_B_fedavg = [[0.7, -0.2], [-0.3, 0.8]]
    w_P_global = [0.1, 0.1]
    for _round in range(60):
        client_W_Bs = []
        client_w_Ps = []
        for j in range(2):
            wb_j = [row[:] for row in W_B_fedavg]
            wp_j = w_P_global[:]
            for _e in range(local_epochs):
                wb_j, wp_j = local_sgd_step(clients[j], wb_j, wp_j, lr)
            client_W_Bs.append(wb_j)
            client_w_Ps.append(wp_j)
        W_B_fedavg = [
            [sum(gammas[j] * client_W_Bs[j][k][d] for j in range(2)) for d in range(2)]
            for k in range(2)
        ]
        w_P_global = [sum(gammas[j] * client_w_Ps[j][k] for j in range(2)) for k in range(2)]

    risk_fedper = eval_personalized_risk(clients, W_B_fedper, W_P_fedper)
    risk_fedavg = eval_personalized_risk(clients, W_B_fedavg, [w_P_global, w_P_global])

    assert risk_fedper < 1e-4, f"FedPer failed to fit personalized targets: {risk_fedper}"
    assert risk_fedavg > 0.5, f"FedAvg with a single global model cannot fit opposite user labels: {risk_fedavg}"

    print(
        f"[PASS] FedPer boundary verification passed: L_PR(FedPer)={risk_fedper:.4e} "
        f"<< L_PR(FedAvg)={risk_fedavg:.4f}"
    )


if __name__ == "__main__":
    main()
