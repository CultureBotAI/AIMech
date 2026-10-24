#!/usr/bin/env python3
"""Constructed boundary verification for TTQ (Trained Ternary Quantization, Zhu et al., ICLR 2017, arXiv:1612.01064)."""

import json


def ttq_quantize(w_tilde, wp, wn, t=0.05):
    """Quantize normalized latent weights w_tilde into {-wn, 0, +wp} (Eqs. 6, 9)."""
    delta = t * max(abs(w) for w in w_tilde)
    w_t = []
    assign = []
    for w in w_tilde:
        if w > delta:
            w_t.append(wp)
            assign.append(1)
        elif w < -delta:
            w_t.append(-wn)
            assign.append(-1)
        else:
            w_t.append(0.0)
            assign.append(0)
    return w_t, assign, delta


def ttq_backward(grad_wt, assign, wp, wn):
    """Compute gradients w.r.t. asymmetric scales (Eq. 7) and latent weights (Eq. 8)."""
    grad_wp = sum(g for g, a in zip(grad_wt, assign) if a == 1)
    grad_wn = sum(-g for g, a in zip(grad_wt, assign) if a == -1)
    grad_w_tilde = []
    for g, a in zip(grad_wt, assign):
        if a == 1:
            grad_w_tilde.append(wp * g)
        elif a == -1:
            grad_w_tilde.append(wn * g)
        else:
            grad_w_tilde.append(1.0 * g)
    return grad_wp, grad_wn, grad_w_tilde


def symmetric_twn_approx(weights):
    """Symmetric TWN baseline (Eqs. 3-4): single scale W_l and threshold 0.7 * E(|w|)."""
    delta = 0.7 * (sum(abs(w) for w in weights) / len(weights))
    pos_neg = [abs(w) for w in weights if abs(w) > delta]
    scale = sum(pos_neg) / len(pos_neg) if pos_neg else 0.0
    return [scale if w > delta else (-scale if w < -delta else 0.0) for w in weights]


def main():
    # Asymmetric target weight distribution where positive and negative magnitudes differ
    target_w = [-2.4, -2.2, -2.5, -0.02, 0.01, 0.03, 0.85, 0.90, 0.80, 0.88]

    # Symmetric TWN uses a single shared scale for +W and -W
    w_sym = symmetric_twn_approx(target_w)
    mse_sym = sum((wt - ws) ** 2 for wt, ws in zip(target_w, w_sym)) / len(target_w)

    # TTQ initializes normalized latent weights in [-1, 1] and learns asymmetric W_l^p, W_l^n
    max_abs = max(abs(w) for w in target_w)
    w_tilde = [w / max_abs for w in target_w]
    wp, wn = 1.0, 1.0
    lr_scale = 0.08
    lr_latent = 0.02

    for _ in range(80):
        w_t, assign, _ = ttq_quantize(w_tilde, wp, wn, t=0.05)
        grad_wt = [2.0 * (wt_i - tgt_i) / len(target_w) for wt_i, tgt_i in zip(w_t, target_w)]
        grad_wp, grad_wn, grad_w_tilde = ttq_backward(grad_wt, assign, wp, wn)
        wp -= lr_scale * grad_wp
        wn -= lr_scale * grad_wn
        w_tilde = [max(-1.0, min(1.0, w - lr_latent * gw)) for w, gw in zip(w_tilde, grad_w_tilde)]

    w_ttq, assign_final, delta_final = ttq_quantize(w_tilde, wp, wn, t=0.05)
    mse_ttq = sum((wt - wq) ** 2 for wt, wq in zip(target_w, w_ttq)) / len(target_w)

    assert abs(wp - 0.8575) < 0.05
    assert abs(wn - 2.3667) < 0.05
    assert mse_ttq < mse_sym * 0.02

    summary = {
        "concept": "TTQTrainedTernaryQuantization",
        "learned_wp": round(wp, 4),
        "learned_wn": round(wn, 4),
        "delta_threshold": round(delta_final, 4),
        "sparsity_ratio": round(assign_final.count(0) / len(assign_final), 4),
        "symmetric_twn_mse": round(mse_sym, 6),
        "asymmetric_ttq_mse": round(mse_ttq, 6),
        "verification": "passed",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
