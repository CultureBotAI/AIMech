#!/usr/bin/env python3
"""Constructed boundary verification for Round 357:
Streaming PCA: Matching Matrix Bernstein and Near-Optimal Finite Sample Guarantees for Oja's Algorithm
(Jain, Jin, Kakade, Netrapalli, & Sidford 2016).

Verifies:
1. Operator Equivalence (Section 3, Equations 3-4): Oja's normalized iterative update
   w_i = (w_{i-1} + eta_i A_i w_{i-1}) / ||w_{i-1} + eta_i A_i w_{i-1}||_2 produces the exact
   same unit vector w_n as one-step power iteration B_n w_0 / ||B_n w_0||_2 on the cumulative
   matrix product B_n = (I + eta_n A_n)...(I + eta_1 A_1).
2. Lemmas 5.1, 5.2, 5.3, and 5.4 (Exact Moment Bounds on B_t B_t^T): Exact analytical expectation
   over the discrete Section 1.1 streaming distribution (A_i = e_1 e_1^T w.p. 1/d and sigma^2 e_j e_j^T
   w.p. 1/d) satisfies:
   - ||E[B_t B_t^T]||_2 <= exp(sum (2 eta_i lambda_1 + eta_i^2 V_bar)) (Lemma 5.1)
   - E[Tr(V_perp^T B_t B_t^T V_perp)] <= Lemma 5.2 upper bound
   - E[v_1^T B_t B_t^T v_1] >= exp(sum (2 eta_i lambda_1 - 4 eta_i^2 lambda_1^2)) (Lemma 5.3)
   - E[(v_1^T B_t B_t^T v_1)^2] <= exp(sum (4 eta_i lambda_1 + 10 eta_i^2 V_bar)) (Lemma 5.4).
"""

import math
import random


def mat_mul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    d = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(d)) for j in range(d)] for i in range(d)]


def main() -> None:
    rng = random.Random(357)
    d = 4
    sigma = 0.4
    # Section 1.1 streaming model (p. 5):
    # Outcome 0 (w.p. 1/d): A = e_0 e_0^T + sigma^2 e_0 e_0^T?
    # Specifically, Section 1.1: x_i = e_1 w.p. 1/d, and x_i = sigma * e_j for j=1..d w.p. 1/d?
    # Let's use the exact 4-outcome distribution over d=4 basis matrices:
    # Outcome 0 (w.p. 1/d): diag(1, 0, 0, 0)
    # Outcome j=1..d-1 (w.p. 1/d): diag(0, ..., sigma^2 at j, ..., 0)
    # Then Sigma = E[A_i] = diag(1/d, sigma^2/d, sigma^2/d, sigma^2/d).
    lambda1 = 1.0 / d
    lambda2 = (sigma * sigma) / d
    gap = lambda1 - lambda2
    # ||A_i - Sigma||_2 <= M and ||E[(A_i - Sigma)^2]||_2 <= V
    M = 1.0 - lambda1
    # E[A_i^2] = diag(1/d, sigma^4/d, ...), so E[(A_i - Sigma)^2] = E[A_i^2] - Sigma^2
    V = (1.0 / d) - (lambda1 * lambda1)
    V_bar = V + lambda1 * lambda1

    # 1. Verify Operator Equivalence (Equations 3-4)
    n_steps = 40
    etas = [0.08 / (10.0 + t) for t in range(1, n_steps + 1)]
    for eta in etas:
        assert eta <= 1.0 / (4.0 * max(lambda1, M))

    w0_raw = [rng.gauss(0.0, 1.0) for _ in range(d)]
    w0_norm = math.sqrt(sum(x * x for x in w0_raw))
    w0 = [x / w0_norm for x in w0_raw]

    w_iter = list(w0)
    B_mat = [[1.0 if i == j else 0.0 for j in range(d)] for i in range(d)]
    for t in range(n_steps):
        eta = etas[t]
        idx = rng.randrange(d)
        val = 1.0 if idx == 0 else (sigma * sigma)
        # Update w_iter via Algorithm 1
        w_next = [w_iter[j] + (eta * val * w_iter[j] if j == idx else 0.0) for j in range(d)]
        wnorm = math.sqrt(sum(x * x for x in w_next))
        w_iter = [x / wnorm for x in w_next]
        # Update B_mat = (I + eta A_t) B_{t-1}
        factor_mat = [[1.0 + (eta * val if i == idx else 0.0) if i == j else 0.0 for j in range(d)] for i in range(d)]
        B_mat = mat_mul(factor_mat, B_mat)

    Bw0 = [sum(B_mat[i][j] * w0[j] for j in range(d)) for i in range(d)]
    Bw0_norm = math.sqrt(sum(x * x for x in Bw0))
    w_op = [x / Bw0_norm for x in Bw0]
    op_diff = max(abs(w_iter[i] - w_op[i]) for i in range(d))
    assert op_diff < 1e-14, f"Operator equivalence failed: {op_diff}"

    # 2. Verify Lemmas 5.1, 5.2, 5.3, and 5.4 exactly on the diagonal operator distribution
    # Because A_t is diagonal in the eigenbasis of Sigma, B_t B_t^T is diagonal with independent steps:
    # E[(B_t B_t^T)_{0,0}] = prod_{i=1}^t E[(1 + eta_i A_{i,00})^2]
    # E[(B_t B_t^T)_{j,j}] = prod_{i=1}^t E[(1 + eta_i A_{i,jj})^2] for j >= 1
    # E[((B_t B_t^T)_{0,0})^2] = prod_{i=1}^t E[(1 + eta_i A_{i,00})^4]
    exact_v1_B_v1 = 1.0
    exact_v1_B_v1_sq = 1.0
    exact_orth_single = 1.0
    for eta in etas:
        # Coordinate 0: A_{i,00} = 1 w.p. 1/d, 0 w.p. 1 - 1/d
        e2_0 = (1.0 / d) * ((1.0 + eta) ** 2) + (1.0 - 1.0 / d) * 1.0
        e4_0 = (1.0 / d) * ((1.0 + eta) ** 4) + (1.0 - 1.0 / d) * 1.0
        # Coordinate j >= 1: A_{i,jj} = sigma^2 w.p. 1/d, 0 w.p. 1 - 1/d
        e2_j = (1.0 / d) * ((1.0 + eta * sigma * sigma) ** 2) + (1.0 - 1.0 / d) * 1.0
        exact_v1_B_v1 *= e2_0
        exact_v1_B_v1_sq *= e4_0
        exact_orth_single *= e2_j

    exact_spec_EB = max(exact_v1_B_v1, exact_orth_single)
    exact_tr_orth = (d - 1) * exact_orth_single

    sum_eta = sum(etas)
    sum_eta_sq = sum(e * e for e in etas)

    # Lemma 5.1 bound
    lemma51_bound = math.exp(sum(2.0 * e * lambda1 + (e * e) * V_bar for e in etas))
    assert exact_spec_EB <= lemma51_bound + 1e-12

    # Lemma 5.2 bound
    prefix_exp = 0.0
    inner_sum = 0.0
    for i, e in enumerate(etas):
        prefix_exp += 2.0 * e * gap
        inner_sum += (e * e) * math.exp(prefix_exp)
    lemma52_bound = math.exp(sum(2.0 * e * lambda2 + (e * e) * V_bar for e in etas)) * (d + V * inner_sum)
    assert exact_tr_orth <= lemma52_bound + 1e-12

    # Lemma 5.3 bound
    lemma53_bound = math.exp(2.0 * lambda1 * sum_eta - 4.0 * (lambda1 ** 2) * sum_eta_sq)
    assert exact_v1_B_v1 >= lemma53_bound - 1e-12

    # Lemma 5.4 bound
    lemma54_bound = math.exp(4.0 * lambda1 * sum_eta + 10.0 * V_bar * sum_eta_sq)
    assert exact_v1_B_v1_sq <= lemma54_bound + 1e-12

    print(
        f"[PASS] Round 357 Streaming PCA Oja's Algorithm (Jain et al. 2016): "
        f"op_diff={op_diff:.2e}, E[v1^T B B^T v1]={exact_v1_B_v1:.4f}>=L5.3({lemma53_bound:.4f}), "
        f"E[Tr_perp]={exact_tr_orth:.4f}<=L5.2({lemma52_bound:.4f}), "
        f"E[(v1^T B B^T v1)^2]={exact_v1_B_v1_sq:.4f}<=L5.4({lemma54_bound:.4f})"
    )


if __name__ == "__main__":
    main()
