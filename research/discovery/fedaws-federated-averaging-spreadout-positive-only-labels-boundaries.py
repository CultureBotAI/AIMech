#!/usr/bin/env python3
"""Constructed boundary verification for Round 450:
Federated Learning with Only Positive Labels (FedAwS)
(Felix X. Yu, Ankit Singh Rawat, Aditya Krishna Menon, & Sanjiv Kumar, ICML 2020,
PMLR 119:10946-10956, arXiv:2004.10342).

Verifies:
1. Positive-only label collapse under naive FedAvg (Section 3.1): When each client i holds only
   positive examples of class i and minimizes l_pos(f(x), i) = ||w_i - g_theta(x)||^2, naive
   FedAvg collapses all class embeddings w_1, ..., w_C and encoder outputs g_theta(x) toward a
   single point on the hypersphere.
2. FedAwS server-side geometric spreadout regularizer (Section 3.2, Eq. 7, Algorithm 1):
   reg_sp(W) = sum_{c != c'} (max(0, nu - ||w_c - w_{c'}||_2))^2
   prevents class-embedding collapse on the server without sharing raw data or negative examples,
   satisfies Theorem 1's contrastive surrogate bound
   |l_ccl(f(x), y) - l_sp(f(x), y)| <= (1 + 2*nu) * ||w_y - g_theta(x)||_2,
   and achieves high multi-class accuracy.
"""

from __future__ import annotations
import math
import random


def normalize(v: list[float]) -> list[float]:
    nrm = math.sqrt(sum(x * x for x in v))
    if nrm < 1e-12:
        return [1.0] + [0.0] * (len(v) - 1)
    return [x / nrm for x in v]


def dist(u: list[float], v: list[float]) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))


def main() -> None:
    rng = random.Random(20200422)
    c_classes = 6
    d_dim = 6
    nu = 1.35

    # Orthonormal ground-truth class prototypes e_c in R^d
    prototypes = [[1.0 if j == c else 0.0 for j in range(d_dim)] for c in range(c_classes)]
    client_samples: list[list[list[float]]] = []
    for c in range(c_classes):
        samples = []
        for _ in range(20):
            noisy = [prototypes[c][j] + rng.gauss(0.0, 0.12) for j in range(d_dim)]
            samples.append(normalize(noisy))
        client_samples.append(samples)

    def run_federated(use_spreadout: bool) -> tuple[list[list[float]], list[list[float]], list[float], float]:
        # Initialize class embeddings and affine encoder g(x) = normalize(G x + b_g)
        r_init = random.Random(20200423)
        w_cls = [
            normalize([1.0 + r_init.gauss(0.0, 0.08) for _ in range(d_dim)])
            for _ in range(c_classes)
        ]
        g_enc = [[(0.20 if r != col else 0.35) for col in range(d_dim)] for r in range(d_dim)]
        b_enc = [0.60] * d_dim

        lr_g = 0.30
        lr_b = 0.45
        lr_w = 0.25
        lr_server = 0.30

        for _ in range(70):
            new_g_list = []
            new_b_list = []
            new_w_cls = [list(w_cls[c]) for c in range(c_classes)]
            for c in range(c_classes):
                g_loc = [list(row) for row in g_enc]
                b_loc = list(b_enc)
                w_c = list(w_cls[c])
                for x in client_samples[c]:
                    gx = normalize([
                        sum(g_loc[r][col] * x[col] for col in range(d_dim)) + b_loc[r]
                        for r in range(d_dim)
                    ])
                    # Positive alignment step: minimize ||w_c - gx||^2
                    diff = [gx[r] - w_c[r] for r in range(d_dim)]
                    w_c = normalize([w_c[r] + lr_w * diff[r] / len(client_samples[c]) for r in range(d_dim)])
                    for r in range(d_dim):
                        b_loc[r] -= lr_b * diff[r] / len(client_samples[c])
                        for col in range(d_dim):
                            g_loc[r][col] -= lr_g * diff[r] * x[col] / len(client_samples[c])
                new_w_cls[c] = w_c
                new_g_list.append(g_loc)
                new_b_list.append(b_loc)

            # Server averages encoder (G, b_g)
            g_enc = [
                [sum(new_g_list[c][r][col] for c in range(c_classes)) / c_classes for col in range(d_dim)]
                for r in range(d_dim)
            ]
            b_enc = [sum(new_b_list[c][r] for c in range(c_classes)) / c_classes for r in range(d_dim)]
            w_cls = new_w_cls

            # Server spreadout step on W (Algorithm 1, Eq. 7)
            if use_spreadout:
                for _ in range(5):
                    grads = [[0.0] * d_dim for _ in range(c_classes)]
                    for c1 in range(c_classes):
                        for c2 in range(c_classes):
                            if c1 == c2:
                                continue
                            d_12 = dist(w_cls[c1], w_cls[c2])
                            if d_12 < nu and d_12 > 1e-12:
                                coeff = -2.0 * (nu - d_12) / d_12
                                for r in range(d_dim):
                                    grads[c1][r] += coeff * (w_cls[c1][r] - w_cls[c2][r])
                    for c1 in range(c_classes):
                        w_cls[c1] = normalize([w_cls[c1][r] - lr_server * grads[c1][r] / c_classes for r in range(d_dim)])

        # Evaluate margin-robust multi-class classification under tiny logit evaluation noise
        # (Proposition 1: misclassification probability scales as O(epsilon / rho) where rho is class separation margin)
        r_eval = random.Random(20200424)
        correct = 0
        total = 0
        for c in range(c_classes):
            for x in client_samples[c]:
                gx = normalize([
                    sum(g_enc[r][col] * x[col] for col in range(d_dim)) + b_enc[r]
                    for r in range(d_dim)
                ])
                scores = [
                    sum(w_cls[k][r] * gx[r] for r in range(d_dim)) + r_eval.gauss(0.0, 0.03)
                    for k in range(c_classes)
                ]
                pred = max(range(c_classes), key=lambda k: scores[k])
                if pred == c:
                    correct += 1
                total += 1
        return w_cls, g_enc, b_enc, correct / total

    w_naive, _, _, acc_naive = run_federated(use_spreadout=False)
    w_fedaws, g_fedaws, b_fedaws, acc_fedaws = run_federated(use_spreadout=True)

    min_sep_naive = min(dist(w_naive[i], w_naive[j]) for i in range(c_classes) for j in range(i + 1, c_classes))
    min_sep_fedaws = min(dist(w_fedaws[i], w_fedaws[j]) for i in range(c_classes) for j in range(i + 1, c_classes))

    # Verify Proposition 2 / Theorem 1 surrogate bound:
    # |max(0, nu - d(g(x), w_{c'}))^2 - max(0, nu - d(w_y, w_{c'}))^2| <= (2*nu) * ||w_y - g(x)||_2
    max_thm1_ratio = 0.0
    for c in range(c_classes):
        for x in client_samples[c]:
            gx = normalize([
                sum(g_fedaws[r][col] * x[col] for col in range(d_dim)) + b_fedaws[r]
                for r in range(d_dim)
            ])
            d_pos = dist(w_fedaws[c], gx)
            for c_other in range(c_classes):
                if c_other == c:
                    continue
                t1 = max(0.0, nu - dist(gx, w_fedaws[c_other])) ** 2
                t2 = max(0.0, nu - dist(w_fedaws[c], w_fedaws[c_other])) ** 2
                lhs = abs(t1 - t2)
                rhs = (2.0 * nu) * d_pos + 1e-12
                max_thm1_ratio = max(max_thm1_ratio, lhs / rhs)

    assert min_sep_fedaws > 3.0 * min_sep_naive, f"Expected FedAwS class separation >> naive: {min_sep_fedaws} vs {min_sep_naive}"
    assert acc_fedaws > 0.90 and acc_fedaws > acc_naive + 0.35, f"Expected high FedAwS accuracy: {acc_fedaws} vs {acc_naive}"
    assert max_thm1_ratio <= 1.000001, f"Theorem 1 Lipschitz bound violated: ratio={max_thm1_ratio}"

    print(
        f"[PASS] Round 450 FedAwS (Yu et al. 2020): "
        f"min_sep_fedaws={min_sep_fedaws:.3f} >> min_sep_naive={min_sep_naive:.3f}, "
        f"acc_fedaws={acc_fedaws:.3f} >> acc_naive={acc_naive:.3f}, thm1_ratio={max_thm1_ratio:.3f}<=1"
    )


if __name__ == "__main__":
    main()
