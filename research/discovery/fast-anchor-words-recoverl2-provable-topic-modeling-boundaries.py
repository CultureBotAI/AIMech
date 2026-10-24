#!/usr/bin/env python3
"""Boundary and regime verification for Arora et al. (2013)
A Practical Algorithm for Topic Modeling with Provable Guarantees (FastAnchorWords & RecoverL2).
"""

import json
import math


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def norm(u):
    return math.sqrt(dot(u, u))


def project_orthogonal(v, basis):
    """Project v onto orthogonal complement of orthonormal basis."""
    res = v[:]
    for b in basis:
        coeff = dot(res, b)
        res = [res[i] - coeff * b[i] for i in range(len(res))]
    return res


def gram_schmidt(vecs):
    basis = []
    for v in vecs:
        p = project_orthogonal(v, basis)
        np = norm(p)
        if np > 1e-12:
            basis.append([x / np for x in p])
    return basis


def dist_to_span(v, span_vecs):
    basis = gram_schmidt(span_vecs)
    return norm(project_orthogonal(v, basis))


def fast_anchor_words(points, K):
    """Algorithm 4: FastAnchorWords combinatorial simplex vertex selection."""
    V = len(points)
    # First point: farthest from origin
    first = max(range(V), key=lambda i: norm(points[i]))
    S_idx = [first]
    for _ in range(1, K):
        span_vecs = [points[idx] for idx in S_idx]
        nxt = max(range(V), key=lambda j: dist_to_span(points[j], span_vecs))
        S_idx.append(nxt)
    # Cleanup phase (second loop in Algorithm 4)
    for i in range(K):
        others = [points[S_idx[t]] for t in range(K) if t != i]
        best_j = max(range(V), key=lambda j: dist_to_span(points[j], others))
        S_idx[i] = best_j
    return S_idx


def exponentiated_gradient_l2(q_bar_i, Q_bar_S, tol=1e-12, max_iter=2000):
    """Algorithm 5 (Exponentiated Gradient with line search, Appendix D.2) for RecoverL2
    quadratic objective min_{c in Delta_K} ||q_bar_i - c^T Q_bar_S||_2^2.
    """
    K = len(Q_bar_S)
    G = [[dot(Q_bar_S[a], Q_bar_S[b]) for b in range(K)] for a in range(K)]
    b_vec = [dot(Q_bar_S[a], q_bar_i) for a in range(K)]

    def obj(c):
        return sum(c[a] * sum(G[a][b] * c[b] for b in range(K)) for a in range(K)) - 2.0 * sum(
            c[a] * b_vec[a] for a in range(K)
        )

    x = [1.0 / K] * K
    eta = 50.0
    for _ in range(max_iter):
        p = [2.0 * (sum(G[a][b] * x[b] for b in range(K)) - b_vec[a]) for a in range(K)]
        mu = min(p)
        lam = [p[a] - mu for a in range(K)]
        gap = sum(lam[a] * x[a] for a in range(K))
        if gap < tol:
            break
        cur_f = obj(x)
        step = eta
        while step > 1e-6:
            x_raw = [x[a] * math.exp(-step * (p[a] - mu)) for a in range(K)]
            s = sum(x_raw)
            x_cand = [z / s for z in x_raw]
            if obj(x_cand) <= cur_f:
                x = x_cand
                break
            step *= 0.5
    return x


def det_3x3(M):
    return (
        M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
    )


def main():
    # 1. Construct a p-separable word-topic matrix A (V=6 words, K=3 topics, p=0.4)
    # Words 0, 1, 2 are anchor words for topics 0, 1, 2 respectively
    A = [
        [0.40, 0.00, 0.00],
        [0.00, 0.40, 0.00],
        [0.00, 0.00, 0.40],
        [0.35, 0.25, 0.10],
        [0.15, 0.25, 0.25],
        [0.10, 0.10, 0.25],
    ]
    V, K = len(A), len(A[0])
    for k in range(K):
        assert abs(sum(A[i][k] for i in range(V)) - 1.0) < 1e-12

    # Topic-topic second-moment matrix R = E[W W^T] (positive definite, sum(R) = 1)
    R = [
        [0.24, 0.05, 0.04],
        [0.05, 0.25, 0.04],
        [0.04, 0.04, 0.25],
    ]

    # Exact population co-occurrence matrix Q = A R A^T
    AR = [[sum(A[i][k] * R[k][l] for k in range(K)) for l in range(K)] for i in range(V)]
    Q = [[sum(AR[i][l] * A[j][l] for l in range(K)) for j in range(V)] for i in range(V)]
    assert abs(sum(Q[i][j] for i in range(V) for j in range(V)) - 1.0) < 1e-12

    # Row-normalize Q to form Q_bar and word marginal vector p_w = Q 1
    p_w = [sum(Q[i]) for i in range(V)]
    Q_bar = [[Q[i][j] / p_w[i] for j in range(V)] for i in range(V)]

    # 2. Verify Algorithm 4 (FastAnchorWords) recovers the exact anchor set {0, 1, 2}
    S_found = sorted(fast_anchor_words(Q_bar, K))
    assert S_found == [0, 1, 2]

    # 3. Verify Section 3 & Algorithm 3/5 (RecoverL2 + Exponentiated Gradient + Bayes' rule):
    Q_bar_S = [Q_bar[s] for s in S_found]
    C = [exponentiated_gradient_l2(Q_bar[i], Q_bar_S) for i in range(V)]
    A_prime = [[p_w[i] * C[i][k] for k in range(K)] for i in range(V)]
    col_sums = [sum(A_prime[i][k] for i in range(V)) for k in range(K)]
    A_hat = [[A_prime[i][k] / col_sums[k] for k in range(K)] for i in range(V)]

    max_A_err = max(abs(A_hat[i][k] - A[i][k]) for i in range(V) for k in range(K))
    assert max_A_err < 1e-4

    # 4. Verify Appendix D.1 unbiased single-document estimator:
    # For a document of length n_d = 4 with word counts H_d = [2, 1, 0, 1, 0, 0],
    # tilde{H}_d tilde{H}_d^T - hat{H}_d equals (1/(n_d(n_d-1))) sum_{i != j} e_{z_i} e_{z_j}^T
    doc_words = [0, 0, 1, 3]
    nd = len(doc_words)
    H_d = [0.0] * V
    for w in doc_words:
        H_d[w] += 1.0
    denom = nd * (nd - 1.0)
    est_mat = [
        [(H_d[i] * H_d[j] - (H_d[i] if i == j else 0.0)) / denom for j in range(V)]
        for i in range(V)
    ]
    pair_mat = [[0.0] * V for _ in range(V)]
    for idx_a in range(nd):
        for idx_b in range(nd):
            if idx_a != idx_b:
                pair_mat[doc_words[idx_a]][doc_words[idx_b]] += 1.0 / denom
    max_d1_diff = max(abs(est_mat[i][j] - pair_mat[i][j]) for i in range(V) for j in range(V))
    assert max_d1_diff < 1e-15

    # 5. Verify Appendix A Claim A.4 Determinant Perturbation Bound:
    # det(M_0 + E) / det(M_0) >= (1 - delta / gamma)^K when sigma_min(M_0) >= gamma and ||E||_F <= sqrt(K)*delta
    gamma = 0.8
    delta = 0.02
    M0 = [[gamma, 0.1, 0.0], [0.0, gamma + 0.2, 0.1], [0.0, 0.0, gamma + 0.4]]
    E = [[-delta, 0.0, 0.0], [0.0, -delta, 0.0], [0.0, 0.0, -delta]]
    M_pert = [[M0[i][j] + E[i][j] for j in range(3)] for i in range(3)]
    ratio_det = det_3x3(M_pert) / det_3x3(M0)
    bound_det = (1.0 - delta / gamma) ** 3
    assert ratio_det >= bound_det - 1e-12

    summary = {
        "concept": "AnchorWordsAndRecoverL2TopicWordMatrixFactorization",
        "fast_anchor_words_selected": S_found,
        "recoverl2_max_entry_err": round(max_A_err, 8),
        "appendix_d1_estimator_err": max_d1_diff,
        "claim_a4_det_ratio": round(ratio_det, 6),
        "claim_a4_lower_bound": round(bound_det, 6),
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
