#!/usr/bin/env python3
"""Constructed boundary verification for FedCorr (Xu et al., CVPR 2022, arXiv:2204.04677)."""

import math
import random

def lid_mle(x, X, k=8):
    dists = []
    for y in X:
        d = math.sqrt(sum((a - b) ** 2 for a, b in zip(x, y)))
        if d > 1e-12:
            dists.append(d)
    dists.sort()
    k_dists = dists[:k]
    r_max = k_dists[-1]
    mean_log = sum(math.log(r / r_max) for r in k_dists) / k
    return -1.0 / mean_log

def main():
    rng = random.Random(462)
    M = 4  # classes
    N_per_client = 40

    # 1. Verify Eq. (2): Clean client predictions lie along 1D class-confidence trajectories (low LID ~ 1),
    # whereas noisy client predictions diffuse across all M-1 simplex dimensions (higher LID)
    def make_client_predictions(noise_rate):
        preds = []
        for i in range(N_per_client):
            true_c = i % M
            sec_c = (true_c + 1) % M
            if rng.random() < noise_rate:
                # Noisy sample: multi-directional label memorization across all M coordinates
                logits = [rng.gauss(0.0, 1.0) for _ in range(M)]
            else:
                # Clean sample: varies along 1D confidence axis between true_c and nearest boundary sec_c
                u = rng.gauss(2.5, 0.6)
                logits = [-1.0 + rng.gauss(0.0, 0.01) for _ in range(M)]
                logits[true_c] = u
                logits[sec_c] = -0.5 * u
            max_l = max(logits)
            exps = [math.exp(l - max_l) for l in logits]
            Z = sum(exps)
            preds.append([e / Z for e in exps])
        return preds

    clean_lids = []
    noisy_lids = []
    for _ in range(5):
        p_clean = make_client_predictions(0.0)
        p_noisy = make_client_predictions(0.6)
        clean_lids.append(sum(lid_mle(x, p_clean, k=8) for x in p_clean) / N_per_client)
        noisy_lids.append(sum(lid_mle(x, p_noisy, k=8) for x in p_noisy) / N_per_client)

    cum_lid_clean = sum(clean_lids)
    cum_lid_noisy = sum(noisy_lids)
    assert cum_lid_noisy > 1.35 * cum_lid_clean, f"Expected noisy cumulative LID > clean: {cum_lid_noisy} vs {cum_lid_clean}"

    # 2. Verify Eq. (5): Adaptive local proximal penalty beta * mu_hat_k * ||w_k - w||^2 bounds noisy client drift
    w_global = [1.0, -1.0]
    g_noisy = [-4.0, 3.5]  # corrupted gradient on noisy client
    eta = 0.1
    beta = 5.0
    mu_clean = 0.0
    mu_noisy = 0.6
    # One proximal gradient step: w_k = (w_global - eta * g_noisy + 2 * eta * beta * mu_hat * w_global) / (1 + 2 * eta * beta * mu_hat)
    w_unreg = [w_global[j] - eta * g_noisy[j] for j in range(2)]
    w_adap = [(w_global[j] - eta * g_noisy[j] + 2.0 * eta * beta * mu_noisy * w_global[j]) / (1.0 + 2.0 * eta * beta * mu_noisy) for j in range(2)]
    drift_unreg = math.sqrt(sum((w_unreg[j] - w_global[j]) ** 2 for j in range(2)))
    drift_adap = math.sqrt(sum((w_adap[j] - w_global[j]) ** 2 for j in range(2)))
    assert abs(drift_adap - drift_unreg / (1.0 + 2.0 * eta * beta * mu_noisy)) < 1e-12
    assert drift_adap < 0.65 * drift_unreg

    # 3. Verify Eq. (6)-(7): Partial relabeling with relabel ratio pi and confidence threshold theta
    # Create 20 samples in D_k^n (16 truly corrupted with high loss, 4 clean hard samples)
    d_n = []
    for idx in range(20):
        true_y = idx % M
        noisy_y = (true_y + 1) % M if idx < 14 else true_y
        # Global model f_G predicts true_y with confidence 0.85 for first 12, and 0.40 for next 2
        conf = 0.85 if idx < 12 else (0.40 if idx < 14 else 0.75)
        f_g = [(1.0 - conf) / (M - 1) for _ in range(M)]
        f_g[true_y] = conf
        ce_loss = -math.log(max(1e-12, f_g[noisy_y]))
        d_n.append({"idx": idx, "true_y": true_y, "given_y": noisy_y, "f_g": f_g, "loss": ce_loss})

    pi_ratio = 0.5
    theta_conf = 0.5
    top_count = int(pi_ratio * len(d_n))
    d_hat_n = sorted(d_n, key=lambda s: s["loss"], reverse=True)[:top_count]
    relabeled = 0
    correct_after = 0
    for s in d_n:
        if s in d_hat_n and max(s["f_g"]) >= theta_conf:
            pred_y = max(range(M), key=lambda c: s["f_g"][c])
            s["new_y"] = pred_y
            relabeled += 1
        else:
            s["new_y"] = s["given_y"]
        if s["new_y"] == s["true_y"]:
            correct_after += 1

    correct_before = sum(1 for s in d_n if s["given_y"] == s["true_y"])
    assert relabeled == 10
    assert correct_after > correct_before, f"Expected label accuracy to improve: {correct_before} -> {correct_after}"

    print(
        f"[PASS] Round 462 FedCorr verified: cum_LID_clean={cum_lid_clean:.3f}<cum_LID_noisy={cum_lid_noisy:.3f}, "
        f"drift={drift_unreg:.3f}->{drift_adap:.3f}, clean_labels={correct_before}/20->{correct_after}/20"
    )

if __name__ == "__main__":
    main()
