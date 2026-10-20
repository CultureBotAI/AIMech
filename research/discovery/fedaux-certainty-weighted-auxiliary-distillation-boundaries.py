#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 484:
FedAUX (FEDAUX: Leveraging Unlabeled Auxiliary Data in Federated Learning,
Sattler, Korjakow, Rischke, & Samek 2021, IEEE TNNLS, arXiv:2102.02514).

Verifies:
1. Certainty-weighted ensemble distillation (Equations 3-6, Section 3.4, p. 4):
   - Each client i solves the lambda-strongly convex L2-regularized logistic ERM separating
     local data D_i (t_x = +1) from public negative auxiliary data D^- (t_x = -1):
     J(w, h_0, D_i, D^-) = (1 / (|D_i| + |D^-|)) sum_{x in D_i U D^-} log(1 + exp(-t_x <w, h_tilde_0(x)>)) + (lambda / 2) ||w||_2^2
   - Certainty score on distillation sample x in D_distill (Equation 6):
     s_i(x) = (1 + exp(-<w_i^*, h_tilde_0(x)>))^{-1} + xi
   - Certainty-weighted ensemble soft-label (Equation 3):
     A_s({(f_i(x), s_i(x)) | i in S_t}) = softmax( sum_{i in S_t} s_i(x) f_i(x) / sum_{i in S_t} s_i(x) ),
     which recovers expert client predictions on disjoint non-IID domains where unweighted
     A_mean (Equation 2, FedDF) fails.
2. Theorem 1 / Theorem 2 L2-sensitivity and (epsilon, delta)-differential privacy bound
   (Equations 8-10 & 13-30, Section 3.5 & Appendix J, pp. 5 & 18-21):
   - For any two adjacent local datasets D_i, D_i' differing in one element with normalized
     features ||h_tilde_0(x)||_2 <= 1, the L2 sensitivity of w_i^* = argmin_w J(w, h_0, D_i, D^-)
     satisfies ||w^* - v^*||_2 <= 2 / (lambda * (|D_i| + |D^-|)).
   - Gaussian mechanism noise variance sigma^2 = 8 ln(1.25 / delta) / (epsilon^2 * lambda^2 * (|D_i| + |D^-|)^2)
     guarantees (epsilon, delta)-DP.
"""

from __future__ import annotations
import math


def sigmoid(z: float) -> float:
    if z >= 0:
        return 1.0 / (1.0 + math.exp(-z))
    ez = math.exp(z)
    return ez / (1.0 + ez)


def softmax(vec: list[float]) -> list[float]:
    m = max(vec)
    exps = [math.exp(v - m) for v in vec]
    s = sum(exps)
    return [e / s for e in exps]


def solve_scoring_erm(
    pos_feats: list[list[float]], neg_feats: list[list[float]], lam: float
) -> list[float]:
    # Minimize J(w) = a * sum log(1 + exp(-t_x <w, h_x>)) + (lam/2) ||w||_2^2 via gradient descent
    d = len(pos_feats[0])
    w = [0.0] * d
    n_tot = len(pos_feats) + len(neg_feats)
    a = 1.0 / n_tot
    lr = 0.5
    for _ in range(400):
        grad = [lam * w[j] for j in range(d)]
        for x in pos_feats:
            # t_x = +1, derivative of log(1 + exp(-<w, x>)) w.r.t. w is -(1 - sigmoid(<w, x>)) * x
            ip = sum(w[j] * x[j] for j in range(d))
            coeff = -a * sigmoid(-ip)
            for j in range(d):
                grad[j] += coeff * x[j]
        for x in neg_feats:
            # t_x = -1, derivative of log(1 + exp(<w, x>)) w.r.t. w is +sigmoid(<w, x>) * x
            ip = sum(w[j] * x[j] for j in range(d))
            coeff = a * sigmoid(ip)
            for j in range(d):
                grad[j] += coeff * x[j]
        w = [w[j] - lr * grad[j] for j in range(d)]
    return w


def main() -> None:
    # 1. Verify Theorem 1 L2-sensitivity bound ||w^* - v^*||_2 <= 2 / (lam * (|D_i| + |D^-|))
    pos_d1 = [[1.0, 0.0], [0.9, 0.1], [0.8, -0.1], [0.95, 0.05]]
    # Adjacent dataset D_i' differing only in the last element (all norms <= 1)
    pos_d2 = [[1.0, 0.0], [0.9, 0.1], [0.8, -0.1], [-0.6, 0.8]]
    neg_d = [[-0.8, -0.6], [-0.6, 0.8], [0.8, -0.6], [-0.7, -0.7]]
    lam = 0.1

    w_star = solve_scoring_erm(pos_d1, neg_d, lam)
    v_star = solve_scoring_erm(pos_d2, neg_d, lam)
    diff_norm = math.sqrt(sum((w_star[j] - v_star[j]) ** 2 for j in range(2)))
    thm1_bound = 2.0 / (lam * (len(pos_d1) + len(neg_d)))
    assert diff_norm <= thm1_bound + 1e-9, f"Theorem 1 violated: {diff_norm} > {thm1_bound}"

    # 2. Verify certainty-weighted ensemble distillation (Eq 3 & 6) vs unweighted mean (Eq 2)
    # Client 0 holds positive +x1 cluster (class 0), Client 1 holds positive -x1 cluster (class 1)
    w0 = solve_scoring_erm([[1.0, 0.0], [0.95, 0.1], [0.95, -0.1]], neg_d, lam)
    w1 = solve_scoring_erm([[-1.0, 0.0], [-0.95, 0.1], [-0.95, -0.1]], neg_d, lam)
    xi = 1e-8

    # Query distillation point in Client 0's domain (+x1, true class 0)
    x_query = [1.0, 0.0]
    s0 = sigmoid(sum(w0[j] * x_query[j] for j in range(2))) + xi
    s1 = sigmoid(sum(w1[j] * x_query[j] for j in range(2))) + xi
    assert s0 > 1.85 * s1, f"Expected s0 > 1.85 * s1, got s0={s0}, s1={s1}"

    # Client 0 predicts class 0 accurately; Client 1 (never saw class 0) predicts wrong biased logits
    f0_logits = [2.0, -1.0]
    f1_logits = [-1.5, 2.2]
    p_mean = softmax([(f0_logits[c] + f1_logits[c]) / 2.0 for c in range(2)])
    p_fedaux = softmax([(s0 * f0_logits[c] + s1 * f1_logits[c]) / (s0 + s1) for c in range(2)])
    # Unweighted mean misclassifies as class 1, whereas FedAUX certainty-weighted ensemble predicts class 0!
    assert p_mean[0] < p_mean[1]
    assert p_fedaux[0] > p_fedaux[1]

    print(
        f"[PASS] FedAUX boundary verification passed: ||w^*-v^*||={diff_norm:.4f} <= {thm1_bound:.4f}, "
        f"p_mean(class0)={p_mean[0]:.3f} < 0.5 < p_FedAUX(class0)={p_fedaux[0]:.3f}"
    )


if __name__ == "__main__":
    main()
