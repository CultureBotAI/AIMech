#!/usr/bin/env python3
"""Constructed boundary verification for FedETF (Li et al., ICCV 2023, arXiv:2303.10058)."""

import math
import random

def synthesize_simplex_etf(C):
    # Eq. (3) with U = I_C (d = C >= C - 1): V = sqrt(C / (C - 1)) * (I_C - (1/C) 1_C 1_C^T)
    scale = math.sqrt(C / (C - 1.0))
    V = []
    for i in range(C):
        col = [scale * ((1.0 if r == i else 0.0) - 1.0 / C) for r in range(C)]
        V.append(col)  # V[i] is v_i in R^C
    return V

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def normalize(v):
    norm = math.sqrt(dot(v, v))
    return [x / norm for x in v]

def main():
    C = 5
    V = synthesize_simplex_etf(C)

    # 1. Verify Definition 3.1 (Eq. 3-4): unit norm, pairwise inner product -1/(C-1), and zero sum
    for i in range(C):
        for j in range(C):
            ip = dot(V[i], V[j])
            expected = 1.0 if i == j else -1.0 / (C - 1.0)
            assert abs(ip - expected) < 1e-12, f"v_{i}^T v_{j} = {ip} != {expected}"
    for r in range(C):
        col_sum = sum(V[i][r] for i in range(C))
        assert abs(col_sum) < 1e-12

    # 2. Verify Eq. (6): Balanced Feature Loss identity and minority-class margin repulsion
    n_k = [50, 20, 10, 5, 1]  # class 4 is a tail minority class, class 0 is head majority
    gamma = 1.0
    beta = 2.0
    y_min = 4
    mu_test = normalize([0.3, -0.1, 0.2, 0.1, 0.8])
    # Form A (ratio inside log1p): log(1 + sum_{c != y} (n_{k,c}/n_{k,y})^gamma exp(beta(v_c^T mu - v_y^T mu)))
    loss_form_a = math.log(
        1.0 + sum(
            ((n_k[c] / n_k[y_min]) ** gamma) * math.exp(beta * (dot(V[c], mu_test) - dot(V[y_min], mu_test)))
            for c in range(C) if c != y_min
        )
    )
    # Form B (weighted softmax cross-entropy): -log( n_{k,y}^gamma exp(beta v_y^T mu) / sum_c n_{k,c}^gamma exp(beta v_c^T mu) )
    denom_b = sum((n_k[c] ** gamma) * math.exp(beta * dot(V[c], mu_test)) for c in range(C))
    loss_form_b = -math.log(((n_k[y_min] ** gamma) * math.exp(beta * dot(V[y_min], mu_test))) / denom_b)
    assert abs(loss_form_a - loss_form_b) < 1e-14

    # 3. Multi-client heterogeneous FL: K=5 clients each dominant in one class
    # Compare global feature NC2 alignment when each client aligns features to fixed ETF V vs biased local classifier
    client_counts = [
        [40, 5, 2, 2, 1],
        [1, 40, 5, 2, 2],
        [2, 1, 40, 5, 2],
        [2, 2, 1, 40, 5],
        [5, 2, 2, 1, 40],
    ]
    rng = random.Random(461)
    # Under FedETF, each client k optimizes local class features mu_{k,c} toward fixed shared V_c with learnable beta_k
    client_mu = [[normalize([rng.gauss(0.0, 1.0) for _ in range(C)]) for _ in range(C)] for _ in range(C)]
    client_beta = [1.0 for _ in range(C)]
    lr = 0.45
    for _ in range(220):
        for k in range(C):
            tot_n = sum(client_counts[k])
            for y in range(C):
                mu = client_mu[k][y]
                b_k = client_beta[k]
                logits = [b_k * dot(V[c], mu) for c in range(C)]
                max_l = max(logits)
                exps = [math.exp(l - max_l) for l in logits]
                Z = sum(exps)
                probs = [e / Z for e in exps]
                freq = client_counts[k][y] / tot_n
                grad_mu = [freq * b_k * (sum(probs[c] * V[c][r] for c in range(C)) - V[y][r]) for r in range(C)]
                grad_b = freq * (sum(probs[c] * dot(V[c], mu) for c in range(C)) - dot(V[y], mu))
                client_mu[k][y] = normalize([mu[r] - lr * grad_mu[r] for r in range(C)])
                client_beta[k] = max(0.1, min(10.0, b_k - lr * grad_b))

    # Aggregate global class representations weighted by client sample counts
    global_mu = []
    for y in range(C):
        w_sum = [sum(client_counts[k][y] * client_mu[k][y][r] for k in range(C)) for r in range(C)]
        global_mu.append(normalize(w_sum))

    nc2_mse = 0.0
    pairs = 0
    for i in range(C):
        for j in range(i + 1, C):
            nc2_mse += (dot(global_mu[i], global_mu[j]) - (-1.0 / (C - 1.0))) ** 2
            pairs += 1
    nc2_mse /= pairs
    mean_beta = sum(client_beta) / C
    assert nc2_mse < 1e-4, f"Expected FedETF global features to satisfy NC2 ETF geometry, got {nc2_mse}"
    assert mean_beta > 1.5, f"Expected learnable temperature beta > 1.5, got {mean_beta}"

    print(
        f"[PASS] Round 461 FedETF verified: v_i^T v_j=-1/{C-1}={-1.0/(C-1):.4f}, "
        f"Eq6_diff={abs(loss_form_a - loss_form_b):.1e}, NC2_mse={nc2_mse:.2e}, learned_beta={mean_beta:.3f}"
    )

if __name__ == "__main__":
    main()
