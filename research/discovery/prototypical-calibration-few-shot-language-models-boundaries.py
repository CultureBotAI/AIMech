#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 736:
Prototypical Calibration for Few-Shot Language Models (PROCA) (Han et al., ICLR 2023, arXiv:2205.10183).

Verifies:
1. Section 3.1 Equations 1-3: Given biased N-dimensional log-probability outputs
   x_n = log(exp(o_n) / sum_{i=1}^N exp(o_i)) on an unlabeled estimate set D_esti, fit an
   N-component Gaussian Mixture Model P_GMM(X) = sum_{n=1}^N alpha_n P_G(X | mu_n, Sigma_n) via EM.
2. Section 3.2 Equations 4-5 Cluster-Label Assignment (CLA) via maximum-weight bipartite matching:
   CLA(e, k) = sum_{n=1}^N mu_{n, k_n}, k*(e) = argmax_{k in K} CLA(e, k),
   and Section 3.3 Equation 6 estimation selection e* = argmax_{e in E} CLA(e, k*(e)).
3. Section 3.4 Equation 7 "weights-cutting" inference: discard mixing weights alpha_n and predict
   n_tilde = argmax_{n=1..N} P_G(x | mu_n*, Sigma_n*), y_hat = k^*_{n_tilde}(e*), recovering accuracy
   under severe prompt prior bias and class imbalance.
"""

import itertools
import math
import random


def log_probs_from_logits(logits):
    m = max(logits)
    lse = m + math.log(sum(math.exp(z - m) for z in logits))
    return [z - lse for z in logits]


def diag_gaussian_logpdf(x, mu, var):
    d = len(x)
    total = -0.5 * d * math.log(2.0 * math.pi)
    for j in range(d):
        v = max(var[j], 1e-6)
        total -= 0.5 * math.log(v) + 0.5 * ((x[j] - mu[j]) ** 2) / v
    return total


def fit_diag_gmm_em(data, n_components, seed):
    rng = random.Random(seed)
    d = len(data[0])
    # Initialize means by picking n_components distinct points
    mus = [list(pt) for pt in rng.sample(data, n_components)]
    vars_ = [[0.25] * d for _ in range(n_components)]
    alphas = [1.0 / n_components] * n_components

    for _ in range(35):
        # E-step
        resp = []
        for x in data:
            log_w = [
                math.log(max(alphas[c], 1e-12)) + diag_gaussian_logpdf(x, mus[c], vars_[c])
                for c in range(n_components)
            ]
            m = max(log_w)
            w = [math.exp(lw - m) for lw in log_w]
            s = sum(w)
            resp.append([wc / s for wc in w])
        # M-step
        for c in range(n_components):
            nk = sum(r[c] for r in resp) + 1e-8
            alphas[c] = nk / len(data)
            for j in range(d):
                mus[c][j] = sum(r[c] * x[j] for r, x in zip(resp, data)) / nk
                vars_[c][j] = (
                    sum(r[c] * ((x[j] - mus[c][j]) ** 2) for r, x in zip(resp, data)) / nk + 1e-4
                )
    return alphas, mus, vars_


def best_cluster_label_assignment(mus):
    """Equations 4-5: maximize CLA(e, k) = sum_{n=1}^N mu_{n, k_n} over all permutations k in S_N."""
    n = len(mus)
    best_score = -1e18
    best_perm = None
    for perm in itertools.permutations(range(n)):
        score = sum(mus[c][perm[c]] for c in range(n))
        if score > best_score:
            best_score = score
            best_perm = perm
    return best_perm, best_score


def main():
    random.seed(736)
    # 3-way classification where prompt bias strongly shifts logits toward class 0 (+2.2 bias)
    # so naive argmax_l x_l predicts class 0 on almost all examples!
    prompt_bias = [2.2, -0.8, -1.1]
    estimate_set = []
    true_labels = []
    # Imbalanced unlabeled estimate set: 25 examples of class 0, 15 of class 1, 10 of class 2
    counts = [25, 15, 10]
    for y_true, cnt in enumerate(counts):
        for _ in range(cnt):
            raw_logits = [
                prompt_bias[c] + (1.4 if c == y_true else 0.0) + random.gauss(0.0, 0.18)
                for c in range(3)
            ]
            estimate_set.append(log_probs_from_logits(raw_logits))
            true_labels.append(y_true)

    # Naive argmax accuracy on biased log-probabilities
    naive_correct = sum(
        1 for x, y in zip(estimate_set, true_labels) if max(range(3), key=lambda c: x[c]) == y
    )
    naive_acc = naive_correct / len(estimate_set)

    # Run multiple EM initializations and select e* by maximum CLA score (Equation 6)
    best_est = None
    best_cla = -1e18
    best_perm = None
    for s in range(8):
        alphas, mus, vars_ = fit_diag_gmm_em(estimate_set, 3, seed=736 + s)
        perm, cla_score = best_cluster_label_assignment(mus)
        if cla_score > best_cla:
            best_cla = cla_score
            best_est = (alphas, mus, vars_)
            best_perm = perm

    _, mus_star, vars_star = best_est
    # Equation 7: Inference with weights-cutting (discarding alpha_n)
    proca_correct = 0
    for x, y in zip(estimate_set, true_labels):
        n_tilde = max(range(3), key=lambda c: diag_gaussian_logpdf(x, mus_star[c], vars_star[c]))
        y_pred = best_perm[n_tilde]
        if y_pred == y:
            proca_correct += 1
    proca_acc = proca_correct / len(estimate_set)

    assert naive_acc <= 0.55, f"Expected biased naive accuracy <= 0.55, got {naive_acc}"
    assert proca_acc >= 0.94, f"Expected PROCA calibrated accuracy >= 0.94, got {proca_acc}"

    print(
        f"PROCA verification passed: naive_acc={naive_acc:.2f} -> proca_acc={proca_acc:.2f}, "
        f"best_CLA={best_cla:.4f}, perm={best_perm}"
    )


if __name__ == "__main__":
    main()
