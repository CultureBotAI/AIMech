#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 808:
PABEE: Patience-Based Early Exit for Pretrained Language Models
(Zhou, Xu, Ge, McAuley, Xu, & Wei, NeurIPS 2020, arXiv:2006.04152).

Verifies:
1. Cross-layer patience counter recurrence for classification (Eq. 2) and regression (Eq. 3):
   - Classification: cnt_i = cnt_{i-1} + 1 if argmax(y_i) == argmax(y_{i-1}) and i > 1 else 0;
     exits at layer j when cnt_j == t (requiring t+1 consecutive layers to agree on the predicted class),
     preventing premature exit on an over-confident single low-layer mistake (Figure 1).
   - Regression: cnt_i = cnt_{i-1} + 1 if |y_i - y_{i-1}| < tau and i > 1 else 0.
2. Layer-depth-weighted training objective (Eq. 6):
   L = (sum_{j=1}^n j * L_j) / (sum_{j=1}^n j), assigning weight 2*j / (n*(n+1)) proportional to the
   relative inference depth j of internal classifier C_j.
3. Theorem 1 & Appendix B probability bounds (Eqs. 7-11):
   For binary classification with n internal classifiers of error rate q and final classifier error rate p:
   - Lower bound on early-stop probability: p_stop > q^{t+1} + (1 - q)^{t+1} >= (1/2)^t (Eq. 7)
   - Upper bound on early-stopped misclassification probability: p_misc < q^{t+1} + (n - t - 1)(1 - q)q^{t+1} (Eq. 8)
   - Sufficient condition for PABEE to strictly reduce error rate below p:
     n - t < ((1 / (2*q))^t * (p / q) - q) / (1 - q) (Eq. 11), which holds for n=12, q=0.2, p=0.1 at all t >= 4.
"""

import json


def pabee_classify_exit(layer_preds, patience_t):
    """Eq. 2: Track consecutive agreement counter cnt_i across layers i=0..n-1 (1-indexed layers 1..n)."""
    cnt = 0
    for idx, pred in enumerate(layer_preds):
        if idx == 0:
            cnt = 0
        else:
            if pred == layer_preds[idx - 1]:
                cnt += 1
            else:
                cnt = 0
        if cnt == patience_t:
            return idx + 1, pred
    return len(layer_preds), layer_preds[-1]


def pabee_regress_exit(layer_vals, tau, patience_t):
    """Eq. 3: Track consecutive |y_i - y_{i-1}| < tau counter across layers."""
    cnt = 0
    for idx, val in enumerate(layer_vals):
        if idx == 0:
            cnt = 0
        else:
            if abs(val - layer_vals[idx - 1]) < tau:
                cnt += 1
            else:
                cnt = 0
        if cnt == patience_t:
            return idx + 1, val
    return len(layer_vals), layer_vals[-1]


def weighted_training_loss(layer_losses):
    """Eq. 6: L = (sum_{j=1}^n j * L_j) / (sum_{j=1}^n j)."""
    n = len(layer_losses)
    num = sum((j + 1) * l_j for j, l_j in enumerate(layer_losses))
    den = n * (n + 1) // 2
    return num / den


def exact_iid_pabee_stats(n, q, p, t):
    """Exact enumeration over all 2^n binary internal-classifier correctness bitstrings (0=correct, 1=wrong)."""
    p_stop = 0.0
    p_misc_stop = 0.0
    p_no_stop = 0.0
    for mask in range(1 << n):
        # bit i is 1 (misclassified with prob q) or 0 (correct with prob 1-q)
        prob = 1.0
        preds = []
        for i in range(n):
            bit = (mask >> i) & 1
            prob *= q if bit == 1 else (1.0 - q)
            preds.append(bit)
        # Run PABEE over internal classifiers 1..n
        cnt = 0
        stopped = False
        exit_pred = None
        for i in range(n):
            if i == 0:
                cnt = 0
            else:
                if preds[i] == preds[i - 1]:
                    cnt += 1
                else:
                    cnt = 0
            if cnt == t:
                stopped = True
                exit_pred = preds[i]
                break
        if stopped:
            p_stop += prob
            if exit_pred == 1:
                p_misc_stop += prob
        else:
            p_no_stop += prob

    assert abs((p_stop + p_no_stop) - 1.0) < 1e-12
    overall_err = p_misc_stop + p_no_stop * p
    return p_stop, p_misc_stop, overall_err


def main():
    # 1. Verify Figure 1(a)-(b) motivating example:
    # Layer 1 predicts Neu, Layer 2 predicts Pos (with overconfident score 0.92), Layers 3 & 4 predict Neg.
    # At patience t=1, PABEE does NOT exit at Layer 2 (since Pos != Neu), and exits at Layer 4 with Neg!
    preds_fig1 = ["Neu", "Pos", "Neg", "Neg", "Neg"]
    exit_layer, final_pred = pabee_classify_exit(preds_fig1, patience_t=1)
    assert exit_layer == 4 and final_pred == "Neg"

    # 2. Verify regression early-exit (Eq. 3)
    reg_vals = [2.1, 3.4, 3.85, 3.89, 3.91, 4.5]
    reg_layer, reg_pred = pabee_regress_exit(reg_vals, tau=0.06, patience_t=2)
    assert reg_layer == 5 and abs(reg_pred - 3.91) < 1e-12

    # 3. Verify Eq. 6 depth-weighted loss
    losses = [1.2 - 0.05 * j for j in range(12)]
    w_loss = weighted_training_loss(losses)
    unweighted_loss = sum(losses) / len(losses)
    # Deeper layers have smaller loss and larger weight, so weighted loss < unweighted mean
    assert w_loss < unweighted_loss

    # 4. Verify Theorem 1 & Appendix B bounds (Eqs. 7, 8, 11) for n=12, q=0.2, p=0.1, t=4
    n, q, p, t = 12, 0.2, 0.1, 4
    p_stop, p_misc, overall_err = exact_iid_pabee_stats(n, q, p, t)

    bound_p_stop_lower = (q ** (t + 1)) + ((1.0 - q) ** (t + 1))  # Eq. 7
    bound_p_misc_upper = (q ** (t + 1)) + (n - t - 1) * (1.0 - q) * (q ** (t + 1))  # Eq. 8
    rhs_eq11 = (((1.0 / (2.0 * q)) ** t) * (p / q) - q) / (1.0 - q)

    assert p_stop > bound_p_stop_lower >= (0.5 ** t)
    assert p_misc < bound_p_misc_upper
    assert (n - t) < rhs_eq11
    assert (p_misc / p_stop) < p
    assert overall_err < p  # PABEE strictly improves accuracy over baseline error rate p=0.10!

    summary = {
        "concept": "PABEEPatienceBasedEarlyExitForBERT",
        "fig1_exit_layer": exit_layer,
        "fig1_pred": final_pred,
        "reg_exit_layer": reg_layer,
        "weighted_loss": round(w_loss, 6),
        "p_stop_exact": round(p_stop, 6),
        "p_stop_lower_bound_eq7": round(bound_p_stop_lower, 6),
        "p_misc_exact": round(p_misc, 6),
        "p_misc_upper_bound_eq8": round(bound_p_misc_upper, 6),
        "overall_error_rate_pabee": round(overall_err, 6),
        "baseline_error_rate_p": p,
        "status": "ok",
    }
    print(json.dumps(summary))


if __name__ == "__main__":
    main()
