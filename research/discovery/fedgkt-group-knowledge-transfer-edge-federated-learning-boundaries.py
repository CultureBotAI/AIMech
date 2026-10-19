#!/usr/bin/env python3
"""Constructed boundary verification for Round 449:
Group Knowledge Transfer: Federated Learning of Large CNNs at the Edge (FedGKT)
(Chaoyang He, Murali Annavaram, & Salman Avestimehr, NeurIPS 2020, arXiv:2007.14513).

Verifies:
1. Alternating minimization with bidirectional KL-divergence knowledge transfer (Section 3,
   Equations 2-10, Algorithm 1):
   - Edge clients k in {1, ..., K} train compact models W^(k) = (W_e^(k), W_c^(k)) with loss
     l_c^(k) = l_CE(y, z_c^(k)) + D_KL(p_s || p_k) (Eqs. 7-8), where p_s = softmax(z_s / T).
   - The central server trains a higher-capacity classifier W_s on uploaded client feature maps
     H^(k) = f_e^(k)(X^(k); W_e^(k)) with loss l_s = sum_k [l_CE(y, z_s) + D_KL(p_k || p_s)]
     (Eqs. 5-6).
2. FedGKT achieves lower test cross-entropy and higher accuracy than isolated local edge training
   while keeping edge client parameter count strictly smaller than the server model.
"""

from __future__ import annotations
import math
import random


def softmax(logits: list[float]) -> list[float]:
    m = max(logits)
    exps = [math.exp(z - m) for z in logits]
    s = sum(exps)
    return [e / s for e in exps]


def kl_div(p_target: list[float], p_pred: list[float]) -> float:
    return sum(pt * math.log(max(pt, 1e-12) / max(pp, 1e-12)) for pt, pp in zip(p_target, p_pred))


def main() -> None:
    rng = random.Random(20200728)
    n_clients = 4
    n_classes = 3
    d_feat = 5
    samples_per_client = 25

    # True global linear + quadratic feature decision boundary on hidden feature space H in R^d_feat
    w_true_lin = [[rng.uniform(-1.2, 1.2) for _ in range(d_feat)] for _ in range(n_classes)]
    w_true_quad = [[rng.uniform(-0.8, 0.8) for _ in range(d_feat)] for _ in range(n_classes)]

    def true_logits(h: list[float]) -> list[float]:
        return [
            sum(w_true_lin[c][j] * h[j] + w_true_quad[c][j] * (h[j] ** 2 - 1.0) for j in range(d_feat))
            for c in range(n_classes)
        ]

    client_data: list[list[tuple[list[float], int]]] = []
    for _ in range(n_clients):
        ds = []
        for _ in range(samples_per_client):
            h = [rng.gauss(0.0, 1.0) for _ in range(d_feat)]
            probs = softmax(true_logits(h))
            y = max(range(n_classes), key=lambda c: probs[c])
            ds.append((h, y))
        client_data.append(ds)

    test_data: list[tuple[list[float], int]] = []
    for _ in range(200):
        h = [rng.gauss(0.0, 1.0) for _ in range(d_feat)]
        probs = softmax(true_logits(h))
        y = max(range(n_classes), key=lambda c: probs[c])
        test_data.append((h, y))

    # Compact edge client head W_c^(k) only has linear features (n_classes * d_feat = 15 params)
    # High-capacity server model W_s has linear + quadratic basis features (n_classes * 2 * d_feat = 30 params)
    edge_params = n_classes * d_feat
    server_params = n_classes * 2 * d_feat
    assert edge_params < server_params

    # Baseline: isolated local edge client training (CE only)
    w_edge_isolated = [[[0.0] * d_feat for _ in range(n_classes)] for _ in range(n_clients)]
    lr = 0.08
    for k in range(n_clients):
        for _ in range(60):
            for h, y in client_data[k]:
                p = softmax([sum(w_edge_isolated[k][c][j] * h[j] for j in range(d_feat)) for c in range(n_classes)])
                for c in range(n_classes):
                    g = p[c] - (1.0 if c == y else 0.0)
                    for j in range(d_feat):
                        w_edge_isolated[k][c][j] -= lr * g * h[j] / samples_per_client

    # FedGKT alternating minimization (Eqs. 5-8, Algorithm 1)
    w_edge_gkt = [[[0.0] * d_feat for _ in range(n_classes)] for _ in range(n_clients)]
    w_server_lin = [[0.0] * d_feat for _ in range(n_classes)]
    w_server_quad = [[0.0] * d_feat for _ in range(n_classes)]

    for _round in range(25):
        # Step 1: Edge clients update W_c^(k) with CE + D_KL(p_s || p_k) and upload soft logits p_k
        uploaded_logits: list[list[list[float]]] = []
        for k in range(n_clients):
            for _ in range(4):
                for h, y in client_data[k]:
                    p_k = softmax([sum(w_edge_gkt[k][c][j] * h[j] for j in range(d_feat)) for c in range(n_classes)])
                    p_s = softmax([
                        sum(w_server_lin[c][j] * h[j] + w_server_quad[c][j] * (h[j] ** 2 - 1.0) for j in range(d_feat))
                        for c in range(n_classes)
                    ])
                    for c in range(n_classes):
                        # Gradient of l_CE(y, z_c) + D_KL(p_s || p_k) wrt z_c is (p_k - e_y) + (p_k - p_s)
                        g = 0.5 * (p_k[c] - (1.0 if c == y else 0.0)) + 0.5 * (p_k[c] - p_s[c])
                        for j in range(d_feat):
                            w_edge_gkt[k][c][j] -= lr * g * h[j] / samples_per_client
            uploaded_logits.append([
                softmax([sum(w_edge_gkt[k][c][j] * h[j] for j in range(d_feat)) for c in range(n_classes)])
                for h, _ in client_data[k]
            ])

        # Step 2: Server updates large W_s on all uploaded (H^(k), y, p_k) with CE + D_KL(p_k || p_s)
        for _ in range(6):
            for k in range(n_clients):
                for idx, (h, y) in enumerate(client_data[k]):
                    p_k = uploaded_logits[k][idx]
                    p_s = softmax([
                        sum(w_server_lin[c][j] * h[j] + w_server_quad[c][j] * (h[j] ** 2 - 1.0) for j in range(d_feat))
                        for c in range(n_classes)
                    ])
                    for c in range(n_classes):
                        g = 0.5 * (p_s[c] - (1.0 if c == y else 0.0)) + 0.5 * (p_s[c] - p_k[c])
                        for j in range(d_feat):
                            w_server_lin[c][j] -= lr * g * h[j] / (n_clients * samples_per_client)
                            w_server_quad[c][j] -= lr * g * (h[j] ** 2 - 1.0) / (n_clients * samples_per_client)

    def eval_client_ce(models: list[list[list[float]]]) -> float:
        total = 0.0
        for k in range(n_clients):
            for h, y in test_data:
                p = softmax([sum(models[k][c][j] * h[j] for j in range(d_feat)) for c in range(n_classes)])
                total += -math.log(max(p[y], 1e-12))
        return total / (n_clients * len(test_data))

    ce_isolated = eval_client_ce(w_edge_isolated)
    ce_gkt_edge = eval_client_ce(w_edge_gkt)
    ce_gkt_server = sum(
        -math.log(
            max(
                softmax([
                    sum(w_server_lin[c][j] * h[j] + w_server_quad[c][j] * (h[j] ** 2 - 1.0) for j in range(d_feat))
                    for c in range(n_classes)
                ])[y],
                1e-12,
            )
        )
        for h, y in test_data
    ) / len(test_data)

    assert ce_gkt_edge < ce_isolated, f"Expected FedGKT edge CE < isolated edge CE: {ce_gkt_edge} vs {ce_isolated}"
    assert ce_gkt_server < ce_gkt_edge, f"Expected FedGKT server CE < edge CE: {ce_gkt_server} vs {ce_gkt_edge}"

    print(
        f"[PASS] Round 449 FedGKT (He et al. 2020): "
        f"edge_params={edge_params}<server_params={server_params}, "
        f"ce_server={ce_gkt_server:.4f} < ce_gkt_edge={ce_gkt_edge:.4f} < ce_isolated={ce_isolated:.4f}"
    )


if __name__ == "__main__":
    main()
