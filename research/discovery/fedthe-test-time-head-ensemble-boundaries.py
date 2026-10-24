#!/usr/bin/env python3
"""Constructed boundary verification for FedTHE and FedTHE+ (Jiang & Lin, ICLR 2023, arXiv:2205.10920)."""

import math

def softmax(logits):
    m = max(logits)
    exps = [math.exp(z - m) for z in logits]
    Z = sum(exps)
    return [e / Z for e in exps]

def shannon_entropy(probs):
    return -sum(p * math.log(max(p, 1e-15)) for p in probs)

def cosine_sim(a, b):
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return sum(x * y for x, y in zip(a, b)) / (na * nb)

def l2_dist(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

def optimize_fedthe_e(y_g, y_l, h_prime, h_g, h_l):
    # Eq. (3)-(5): L_SLW(e) = lambda_s * L_EM(e) + (1 - lambda_s) * L_FA(e)
    p_g = softmax(y_g)
    p_l = softmax(y_l)
    lam_s = cosine_sim(p_g, p_l)
    assert 0.0 <= lam_s <= 1.0 + 1e-12
    d_g = l2_dist(h_prime, h_g)
    d_l = l2_dist(h_prime, h_l)

    best_e = 0.5
    best_loss = float("inf")
    for idx in range(101):
        e = idx / 100.0
        y_ens = [e * yg + (1.0 - e) * yl for yg, yl in zip(y_g, y_l)]
        p_ens = softmax(y_ens)
        l_em = shannon_entropy(p_ens)
        l_fa = e * d_g + (1.0 - e) * d_l
        l_slw = lam_s * l_em + (1.0 - lam_s) * l_fa
        if l_slw < best_loss:
            best_loss = l_slw
            best_e = e
    return best_e, lam_s

def main():
    # Setup local descriptor h_l (focused on classes 0, 1) and global descriptor h_g (centered across all 4 classes)
    h_l = [1.5, 1.5, 0.0, 0.0]
    h_g = [0.5, 0.5, 0.5, 0.5]

    # Case A: In-Distribution (ID) test sample from client's major class 0
    # Feature h'_id is close to h_l; local head is confident on class 0, global head is moderately confident on class 0
    h_prime_id = [1.4, 1.5, 0.1, 0.0]
    y_l_id = [3.5, 0.2, -1.0, -1.0]
    y_g_id = [1.6, 0.4, 0.1, -0.2]
    e_id, lam_id = optimize_fedthe_e(y_g_id, y_l_id, h_prime_id, h_g, h_l)
    # Local head weight (1 - e_id) should dominate for ID sample
    assert (1.0 - e_id) > 0.75, f"Expected local head weight 1 - e > 0.75 on ID sample, got e={e_id}"

    # Case B: Out-of-Client (OoC) label-shifted test sample from unseen class 3
    # Feature h'_ooc is closer to global descriptor h_g than biased local descriptor h_l;
    # Local head wrongly predicts seen class 1 (falsely confident), while global head predicts true class 3!
    # Because p(y_g) and p(y_l) disagree strongly, cosine similarity lam_s is small, so FA loss dominates EM!
    h_prime_ooc = [0.2, 0.2, 0.6, 0.8]
    y_l_ooc = [-0.5, 2.6, -1.2, -1.5]  # biased local head predicts class 1
    y_g_ooc = [-0.4, -0.3, 0.2, 2.8]   # global head predicts true unseen class 3
    e_ooc, lam_ooc = optimize_fedthe_e(y_g_ooc, y_l_ooc, h_prime_ooc, h_g, h_l)
    assert lam_ooc < 0.25, f"Expected low head probability similarity under OoC unseen class, got {lam_ooc}"
    assert e_ooc > 0.75, f"Expected global head weight e > 0.75 on OoC sample, got e={e_ooc}"

    y_pred_ooc = [e_ooc * yg + (1.0 - e_ooc) * yl for yg, yl in zip(y_g_ooc, y_l_ooc)]
    pred_class = max(range(4), key=lambda c: y_pred_ooc[c])
    assert pred_class == 3

    print(
        f"[PASS] Round 468 FedTHE verified: ID(1-e*={1.0-e_id:.2f}, lam_s={lam_id:.3f}), "
        f"OoC(e*={e_ooc:.2f}, lam_s={lam_ooc:.3f}, pred_class={pred_class})"
    )

if __name__ == "__main__":
    main()
