#!/usr/bin/env python3
"""Boundary and regime verification for Yuan & Zhang (2013)
Truncated Power Method (TPower) for Sparse Eigenvalue Problems and Sparse PCA.
"""

import json
import math


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def norm(u):
    return math.sqrt(dot(u, u))


def normalize(u):
    n = norm(u)
    return [z / n for z in u]


def mat_vec(A, x):
    return [sum(row[j] * x[j] for j in range(len(x))) for row in A]


def truncate_k(x, k):
    idx = sorted(range(len(x)), key=lambda i: abs(x[i]), reverse=True)[:k]
    idx_set = set(idx)
    return [x[i] if i in idx_set else 0.0 for i in range(len(x))]


def main():
    p = 16
    k_bar = 2
    k = 8  # satisfies k >= 4 * k_bar in Theorem 1

    # Ground-truth sparse dominant eigenvector x_bar supported on {0, 1}
    x_bar = [0.0] * p
    x_bar[0] = 1.0 / math.sqrt(2.0)
    x_bar[1] = 1.0 / math.sqrt(2.0)

    lam = 5.0
    lam_rest = 1.0
    # True matrix A_bar = (lam - lam_rest) x_bar x_bar^T + lam_rest I_p
    A_bar = [
        [
            (lam - lam_rest) * x_bar[i] * x_bar[j] + (lam_rest if i == j else 0.0)
            for j in range(p)
        ]
        for i in range(p)
    ]

    # 1. Verify Lemma 3 (Untruncated Power Step Progress) on A_bar
    gamma = lam_rest / lam  # 0.2
    x_test = normalize([0.5, 0.2, 0.6, -0.4] + [0.1] * (p - 4))
    y_dot_x = abs(dot(x_bar, x_test))
    x_prime = normalize(mat_vec(A_bar, x_test))
    y_dot_xprime = abs(dot(x_bar, x_prime))
    lemma3_rhs = y_dot_x * (1.0 + 0.5 * (1.0 - gamma * gamma) * (1.0 - y_dot_x * y_dot_x))
    assert y_dot_xprime >= lemma3_rhs - 1e-12

    # 2. Verify Lemma 4 (Truncation Perturbation Bound)
    y_trunc = truncate_k(x_prime, k)
    lhs_lemma4 = abs(dot(y_trunc, x_bar))
    ratio_sqrt = math.sqrt(k_bar / k)
    rhs_lemma4 = y_dot_xprime - ratio_sqrt * min(
        1.0, (1.0 + ratio_sqrt) * (1.0 - y_dot_xprime * y_dot_xprime)
    )
    assert lhs_lemma4 >= rhs_lemma4 - 1e-12

    # 3. Verify Algorithm 1 (TPower) & Theorem 1 on noisy matrix A = A_bar + E
    E = [
        [
            0.015 * math.cos(i + 2 * j) if i == j else 0.008 * math.sin(i - j)
            for j in range(p)
        ]
        for i in range(p)
    ]
    # Symmetrize E
    E = [[0.5 * (E[i][j] + E[j][i]) for j in range(p)] for i in range(p)]
    A = [[A_bar[i][j] + E[i][j] for j in range(p)] for i in range(p)]

    # Initialize at coordinate with largest diagonal entry [A]_{jj} (Section 4.1.2)
    j_init = max(range(p), key=lambda i: A[i][i])
    xt = [1.0 if i == j_init else 0.0 for i in range(p)]
    init_align = abs(dot(xt, x_bar))

    # Run TPower with k = 2 (target cardinality)
    for _ in range(25):
        xp = normalize(mat_vec(A, xt))
        xt = normalize(truncate_k(xp, k_bar))

    final_align = abs(dot(xt, x_bar))
    final_l2_err = math.sqrt(2.0 * (1.0 - final_align))
    assert final_align > 0.9999
    assert final_l2_err < 0.01

    # 4. Verify failure mode on noiseless A_bar when initialized orthogonal to x_bar (x_0^T x_bar = 0)
    x_orth = [0.0, 0.0, 1.0] + [0.0] * (p - 3)
    for _ in range(10):
        xp_o = normalize(mat_vec(A_bar, x_orth))
        x_orth = normalize(truncate_k(xp_o, k_bar))
    orth_align = abs(dot(x_orth, x_bar))
    assert orth_align == 0.0

    summary = {
        "concept": "TruncatedPowerMethodForSparseEigenvalueAndSparsePCA",
        "lemma3_lhs": round(y_dot_xprime, 6),
        "lemma3_rhs": round(lemma3_rhs, 6),
        "lemma4_lhs": round(lhs_lemma4, 6),
        "lemma4_rhs": round(rhs_lemma4, 6),
        "tpower_init_alignment": round(init_align, 6),
        "tpower_final_alignment": round(final_align, 6),
        "tpower_final_l2_error": round(final_l2_err, 6),
        "orthogonal_init_alignment": orth_align,
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
