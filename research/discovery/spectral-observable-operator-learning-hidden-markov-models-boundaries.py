#!/usr/bin/env python3
"""Boundary and regime verification for Hsu, Kakade, & Zhang (2012)
Spectral Observable Operator Algorithm for Learning Hidden Markov Models.
"""

import json
import math
import random


def mat_mul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][r] * B[r][j] for r in range(k)) for j in range(n)] for i in range(m)]


def mat_vec(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def inv_2x2(M):
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    return [
        [M[1][1] / det, -M[0][1] / det],
        [-M[1][0] / det, M[0][0] / det],
    ]


def svd_rank2_left(M):
    """Return 3x2 orthonormal left singular vectors U of a 3x3 rank-2 matrix M."""
    # Gram matrix G = M M^T (3x3 symmetric)
    MT = transpose(M)
    G = mat_mul(M, MT)
    # Power iteration + deflation for top 2 eigenvectors of G
    vecs = []
    G_curr = [row[:] for row in G]
    for k in range(2):
        v = [1.0, 0.5 * (k + 1), -0.3 * (k + 1)]
        for _ in range(80):
            w = mat_vec(G_curr, v)
            norm = math.sqrt(sum(z * z for z in w))
            v = [z / norm for z in w]
        eig = sum(v[i] * sum(G_curr[i][j] * v[j] for j in range(3)) for i in range(3))
        vecs.append(v)
        for i in range(3):
            for j in range(3):
                G_curr[i][j] -= eig * v[i] * v[j]
    # Orthonormalize vecs[1] against vecs[0]
    proj = sum(vecs[0][i] * vecs[1][i] for i in range(3))
    v1 = [vecs[1][i] - proj * vecs[0][i] for i in range(3)]
    n1 = math.sqrt(sum(z * z for z in v1))
    v1 = [z / n1 for z in v1]
    return [[vecs[0][i], v1[i]] for i in range(3)]


def main():
    # 1. Ground-truth 2-state HMM with n = 3 discrete observations obeying Condition 1
    pi = [0.6, 0.4]
    T = [
        [0.75, 0.30],
        [0.25, 0.70],
    ]
    O = [
        [0.70, 0.10],
        [0.20, 0.30],
        [0.10, 0.60],
    ]
    n_obs = 3

    # Observation operators A_x = T diag(O_{x,1}, O_{x,2}) (Lemma 1)
    A = []
    for x in range(n_obs):
        Ax = [
            [T[0][0] * O[x][0], T[0][1] * O[x][1]],
            [T[1][0] * O[x][0], T[1][1] * O[x][1]],
        ]
        A.append(Ax)

    # Exact observable marginals P_1, P_{2,1}, P_{3,x,1} (Section 3.1)
    P1 = mat_vec(O, pi)
    diag_pi = [[pi[0], 0.0], [0.0, pi[1]]]
    P21 = mat_mul(mat_mul(O, T), mat_mul(diag_pi, transpose(O)))
    P3 = []
    for x in range(n_obs):
        P3x = mat_mul(mat_mul(O, A[x]), mat_mul(T, mat_mul(diag_pi, transpose(O))))
        P3.append(P3x)

    # Thin SVD of P_{2,1} -> U in R^{3x2} (Lemma 2)
    U = svd_rank2_left(P21)
    UT = transpose(U)

    # Verify Condition 2: U^T O is invertible
    UTO = mat_mul(UT, O)
    UTO_inv = inv_2x2(UTO)

    # Observable parameters b_1, b_inf, B_x (Section 3.1, Lemma 3)
    b1 = mat_vec(UT, P1)
    UT_P21 = mat_mul(UT, P21)
    # Pseudo-inverse of U^T P_{2,1} (2x3 full row rank): M^+ = M^T (M M^T)^{-1}
    UT_P21_T = transpose(UT_P21)
    UT_P21_pinv = mat_mul(UT_P21_T, inv_2x2(mat_mul(UT_P21, UT_P21_T)))
    # (P_{2,1}^T U)^+ = ((U^T P_{2,1})^T)^+ = (U^T P_{2,1} (U^T P_{2,1})^T)^{-1} U^T P_{2,1}
    P21T_U_pinv = transpose(UT_P21_pinv)
    b_inf = mat_vec(P21T_U_pinv, P1)

    B = []
    max_sim_err = 0.0
    for x in range(n_obs):
        Bx = mat_mul(mat_mul(UT, P3[x]), UT_P21_pinv)
        B.append(Bx)
        # Verify Lemma 3(3): B_x = (U^T O) A_x (U^T O)^{-1}
        Bx_sim = mat_mul(mat_mul(UTO, A[x]), UTO_inv)
        for i in range(2):
            for j in range(2):
                max_sim_err = max(max_sim_err, abs(Bx[i][j] - Bx_sim[i][j]))

    assert max_sim_err < 1e-12, f"Similarity identity failed: {max_sim_err}"

    # 2. Verify Lemma 3(4) and Lemma 4: exact joint & conditional probabilities for all length-4 sequences
    total_prob = 0.0
    max_joint_diff = 0.0
    max_cond_diff = 0.0
    for x1 in range(n_obs):
        for x2 in range(n_obs):
            for x3 in range(n_obs):
                for x4 in range(n_obs):
                    # True probability 1^T A_{x4} A_{x3} A_{x2} A_{x1} pi
                    v_true = mat_vec(A[x1], pi)
                    v_true = mat_vec(A[x2], v_true)
                    v_true = mat_vec(A[x3], v_true)
                    v_true_4 = mat_vec(A[x4], v_true)
                    p_true = sum(v_true_4)
                    p_true_prefix = sum(v_true)

                    # Observable operator probability b_inf^T B_{x4} B_{x3} B_{x2} B_{x1} b_1
                    v_obs = mat_vec(B[x1], b1)
                    v_obs = mat_vec(B[x2], v_obs)
                    v_obs = mat_vec(B[x3], v_obs)
                    v_obs_4 = mat_vec(B[x4], v_obs)
                    p_obs = sum(b_inf[i] * v_obs_4[i] for i in range(2))
                    p_obs_prefix = sum(b_inf[i] * v_obs[i] for i in range(2))

                    total_prob += p_obs
                    max_joint_diff = max(max_joint_diff, abs(p_true - p_obs))
                    max_cond_diff = max(
                        max_cond_diff,
                        abs((p_true / p_true_prefix) - (p_obs / p_obs_prefix)),
                    )

    assert abs(total_prob - 1.0) < 1e-12
    assert max_joint_diff < 1e-13
    assert max_cond_diff < 1e-13

    # 3. Verify Theorem 6 sample-based LearnHMM L1 convergence on N = 25000 sampled triples
    rng = random.Random(20261019)
    N = 25000
    P1_hat = [0.0] * n_obs
    P21_hat = [[0.0] * n_obs for _ in range(n_obs)]
    P3_hat = [[[0.0] * n_obs for _ in range(n_obs)] for _ in range(n_obs)]

    def sample_cat(probs):
        u = rng.random()
        acc = 0.0
        for idx, p in enumerate(probs):
            acc += p
            if u <= acc:
                return idx
        return len(probs) - 1

    for _ in range(N):
        h1 = sample_cat(pi)
        x1 = sample_cat([O[x][h1] for x in range(n_obs)])
        h2 = sample_cat([T[h][h1] for h in range(2)])
        x2 = sample_cat([O[x][h2] for x in range(n_obs)])
        h3 = sample_cat([T[h][h2] for h in range(2)])
        x3 = sample_cat([O[x][h3] for x in range(n_obs)])
        P1_hat[x1] += 1.0 / N
        P21_hat[x2][x1] += 1.0 / N
        P3_hat[x2][x3][x1] += 1.0 / N

    U_hat = svd_rank2_left(P21_hat)
    UT_hat = transpose(U_hat)
    b1_hat = mat_vec(UT_hat, P1_hat)
    UTP21_hat = mat_mul(UT_hat, P21_hat)
    UTP21_hat_T = transpose(UTP21_hat)
    UTP21_hat_pinv = mat_mul(UTP21_hat_T, inv_2x2(mat_mul(UTP21_hat, UTP21_hat_T)))
    b_inf_hat = mat_vec(transpose(UTP21_hat_pinv), P1_hat)
    B_hat = [mat_mul(mat_mul(UT_hat, P3_hat[x]), UTP21_hat_pinv) for x in range(n_obs)]

    l1_err_t3 = 0.0
    for x1 in range(n_obs):
        for x2 in range(n_obs):
            for x3 in range(n_obs):
                v_t = mat_vec(A[x3], mat_vec(A[x2], mat_vec(A[x1], pi)))
                p_t = sum(v_t)
                v_h = mat_vec(B_hat[x3], mat_vec(B_hat[x2], mat_vec(B_hat[x1], b1_hat)))
                p_h = sum(b_inf_hat[i] * v_h[i] for i in range(2))
                l1_err_t3 += abs(p_t - p_h)

    assert l1_err_t3 < 0.035, f"Sample LearnHMM L1 error too large: {l1_err_t3}"

    # 4. Verify Condition 1 violation (rank-deficient O with identical emission columns) breaks invertibility of U^T O
    O_deg = [[0.5, 0.5], [0.3, 0.3], [0.2, 0.2]]
    P21_deg = mat_mul(mat_mul(O_deg, T), mat_mul(diag_pi, transpose(O_deg)))
    # Rank-1 matrix has zero determinant on any 2x2 sub-block
    det_deg = P21_deg[0][0] * P21_deg[1][1] - P21_deg[0][1] * P21_deg[1][0]
    assert abs(det_deg) < 1e-15

    summary = {
        "concept": "SpectralObservableOperatorAlgorithmForLearningHiddenMarkovModels",
        "max_similarity_operator_err": max_sim_err,
        "max_exact_joint_prob_err_t4": max_joint_diff,
        "max_exact_cond_prob_err_t4": max_cond_diff,
        "sample_learnhmm_l1_err_t3": round(l1_err_t3, 6),
        "rank_deficient_det_p21": det_deg,
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
