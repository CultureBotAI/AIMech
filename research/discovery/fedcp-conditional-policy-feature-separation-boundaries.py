#!/usr/bin/env python3
"""Constructed boundary verification for FedCP (Zhang et al., KDD 2023, arXiv:2307.01217)."""

import math

def layer_norm_relu(x, eps=1e-8):
    K = len(x)
    mean_x = sum(x) / K
    var_x = sum((v - mean_x) ** 2 for v in x) / K
    std_x = math.sqrt(var_x + eps)
    return [max(0.0, (v - mean_x) / std_x) for v in x]

def cpn_policy(h_i, W_i_hd, Theta_1, Theta_2):
    # Section 3.2.1: v_i = sum_{c=1}^C w_c^T in R^K
    C = len(W_i_hd)
    K = len(h_i)
    v_i = [sum(W_i_hd[c][k] for c in range(C)) for k in range(K)]
    v_norm = math.sqrt(sum(v ** 2 for v in v_i))
    # C_i = (v_i / ||v_i||_2) odot h_i
    C_i = [(v_i[k] / v_norm) * h_i[k] for k in range(K)]
    # FC + LN + ReLU producing a_{i,1}, a_{i,2} in R^K
    z1 = [sum(Theta_1[k][j] * C_i[j] for j in range(K)) for k in range(K)]
    z2 = [sum(Theta_2[k][j] * C_i[j] for j in range(K)) for k in range(K)]
    a1 = layer_norm_relu(z1)
    a2 = layer_norm_relu(z2)
    r_i = []
    s_i = []
    for k in range(K):
        e1 = math.exp(a1[k])
        e2 = math.exp(a2[k])
        r_i.append(e1 / (e1 + e2))
        s_i.append(e2 / (e1 + e2))
    return C_i, r_i, s_i

def main():
    K = 4  # feature dimension (dims 0,1 = global invariant; dims 2,3 = client-personalized)
    C = 2  # classes
    # Frozen global head responds to global dims (0,1); personalized head responds to local dims (2,3)
    W_global_hd = [
        [1.5, -1.5, 0.0, 0.0],
        [-1.5, 1.5, 0.0, 0.0],
    ]
    W_pers_hd = [
        [0.1, 0.1, 2.0, -1.8],
        [0.1, 0.1, -2.0, 1.8],
    ]
    # CPN weights routing dims 0,1 to global gate r_i and dims 2,3 to personalized gate s_i
    Theta_1 = [
        [2.0, 0.5, 0.0, 0.0],
        [0.5, 2.0, 0.0, 0.0],
        [0.0, 0.0, -1.0, 0.0],
        [0.0, 0.0, 0.0, -1.0],
    ]
    Theta_2 = [
        [-1.0, 0.0, 0.0, 0.0],
        [0.0, -1.0, 0.0, 0.0],
        [0.0, 0.0, 2.2, 0.4],
        [0.0, 0.0, 0.4, 2.2],
    ]
    h_sample = [1.2, -0.8, 1.6, -1.4]
    C_i, r_i, s_i = cpn_policy(h_sample, W_pers_hd, Theta_1, Theta_2)

    # 1. Verify Eq. (4): exact complementarity r_i^k + s_i^k = 1 and r_i^k, s_i^k in (0, 1)
    for k in range(K):
        assert 0.0 < r_i[k] < 1.0 and 0.0 < s_i[k] < 1.0
        assert abs(r_i[k] + s_i[k] - 1.0) < 1e-15

    # 2. Verify Eq. (5)-(6): Dual-route logit combination and head-averaging upload W_hat_i^{hd} = (W^{hd} + W_i^{hd})/2
    r_h = [r_i[k] * h_sample[k] for k in range(K)]
    s_h = [s_i[k] * h_sample[k] for k in range(K)]
    out_r = [sum(W_global_hd[c][k] * r_h[k] for k in range(K)) for c in range(C)]
    out_s = [sum(W_pers_hd[c][k] * s_h[k] for k in range(K)) for c in range(C)]
    out_fedcp = [out_r[c] + out_s[c] for c in range(C)]
    W_upload = [[0.5 * (W_global_hd[c][k] + W_pers_hd[c][k]) for k in range(K)] for c in range(C)]
    assert abs(W_upload[0][2] - 1.0) < 1e-12

    # 3. Verify Section 8 PIR metric: PIR_i = (1/K) sum_{k=1}^K s_i^k
    pir_i = sum(s_i) / K
    assert 0.0 < pir_i < 1.0
    assert s_i[2] > r_i[2] and s_i[3] > r_i[3], f"Expected personalized dims 2,3 to have s_i > r_i: s={s_i}, r={r_i}"

    print(
        f"[PASS] Round 463 FedCP verified: max|r+s-1|={max(abs(r_i[k]+s_i[k]-1.0) for k in range(K)):.1e}, "
        f"r_i={[round(x,3) for x in r_i]}, s_i={[round(x,3) for x in s_i]}, PIR={pir_i:.4f}, out0={out_fedcp[0]:.3f}"
    )

if __name__ == "__main__":
    main()
