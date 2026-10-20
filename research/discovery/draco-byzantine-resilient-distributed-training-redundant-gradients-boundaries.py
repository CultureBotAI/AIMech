#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 524:
DRACO (Byzantine-Resilient Distributed Training via Redundant Gradients)
Chen, Wang, Charles, & Papailiopoulos, ICML 2018 (PMLR 80:903-912, arXiv:1803.09877).

Verifies:
1. Theorem 1 & Corollary 6 information-theoretic redundancy lower bound:
   Any (A, E, D) scheme that exactly recovers G * 1_P against s worst-case Byzantine
   nodes must satisfy ||A_{.,i}||_0 >= 2s + 1 for every sample i, so r = (1/P)||A||_0 >= 2s + 1
   and s <= (P - 1) / 2; if any sample has replication tau <= 2s, two distinct gradient
   matrices G^1, G^2 with G^1 1_P != G^2 1_P become indistinguishable under valid s-attacks.
2. Theorem 2 & Appendix B Algorithm 2: Fractional Repetition Code (A^Rep, E^Rep, D^Rep)
   with Boyer-Moore streaming majority vote exactly recovers G * 1_P (zero L2 error)
   for any s = (r - 1) / 2 worst-case Byzantine nodes in each group.
3. Algorithm 1, Lemmas 3-4, & Theorem 5: Cyclic Code (A^Cyc, E^Cyc, D^Cyc) over complex
   IDFT Vandermonde subspace C_L and syndrome subspace C_R locates the exact set V of
   s adversarial nodes via Toeplitz error-locator system (Eq. A.1) and recovers G * 1_P
   to machine precision.
"""

import cmath
import math
import random


def boyer_moore_majority_vector(vectors, tol=1e-9):
    """Appendix B Algorithm 2: Streaming Boyer-Moore majority vote for vectors."""
    ma = vectors[0]
    counter = 0
    for vec in vectors:
        if counter == 0:
            ma = vec
            counter = 1
        elif math.sqrt(sum((a - b) ** 2 for a, b in zip(ma, vec))) <= tol:
            counter += 1
        else:
            counter -= 1
    return list(ma)


def solve_complex_linear_system(a_mat, b_vec):
    """Gaussian elimination with partial pivoting over complex numbers."""
    n = len(b_vec)
    aug = [list(a_mat[i]) + [b_vec[i]] for i in range(n)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        aug[col], aug[pivot] = aug[pivot], aug[col]
        piv_val = aug[col][col]
        assert abs(piv_val) > 1e-10, "Singular matrix in complex solver"
        for j in range(col, n + 1):
            aug[col][j] /= piv_val
        for r in range(n):
            if r != col and abs(aug[r][col]) > 0.0:
                factor = aug[r][col]
                for j in range(col, n + 1):
                    aug[r][j] -= factor * aug[col][j]
    return [aug[i][n] for i in range(n)]


def main():
    rng = random.Random(2018)

    # 1. Verify Theorem 1 impossibility construction when replication tau = 2s < 2s + 1
    s = 2
    tau = 2 * s  # 4 < 2s + 1 = 5
    # Suppose sample 0 is replicated only on nodes 0..tau-1 with linear sum encoding.
    # For g_0^1 = +1 and g_0^2 = -1, adversary corrupts nodes 0..s-1 under G^1 with -2
    # and corrupts nodes s..2s-1 under G^2 with +2, making received vectors identical!
    z_g1 = [+1.0 if j < tau else 0.0 for j in range(9)]
    z_g2 = [-1.0 if j < tau else 0.0 for j in range(9)]
    n1 = [-2.0 if j < s else 0.0 for j in range(9)]
    n2 = [+2.0 if s <= j < tau else 0.0 for j in range(9)]
    r_received_1 = [z + e for z, e in zip(z_g1, n1)]
    r_received_2 = [z + e for z, e in zip(z_g2, n2)]
    assert r_received_1 == r_received_2, "Theorem 1 indistinguishability must hold when tau <= 2s"

    # 2. Verify Fractional Repetition Code (Theorem 2) with P = 15, s = 2, r = 2s + 1 = 5
    p_nodes = 15
    r_rep = 2 * s + 1  # 5
    d = 6
    G = [[rng.uniform(-2.0, 2.0) for _ in range(p_nodes)] for _ in range(d)]
    true_sum = [sum(G[coord][k] for k in range(p_nodes)) for coord in range(d)]

    # Partition into P/r = 3 groups of size r = 5; adversary corrupts s = 2 nodes per group
    num_groups = p_nodes // r_rep
    decoded_rep = [0.0 for _ in range(d)]
    for g_idx in range(num_groups):
        cols = range(g_idx * r_rep, (g_idx + 1) * r_rep)
        group_true_sum = [sum(G[coord][k] for k in cols) for coord in range(d)]
        group_outputs = []
        adv_nodes_in_group = rng.sample(range(r_rep), s)
        for member in range(r_rep):
            if member in adv_nodes_in_group:
                # Arbitrary reverse/constant Byzantine attack
                group_outputs.append([-100.0 * val + 50.0 for val in group_true_sum])
            else:
                group_outputs.append(list(group_true_sum))
        maj_vec = boyer_moore_majority_vector(group_outputs)
        decoded_rep = [a + b for a, b in zip(decoded_rep, maj_vec)]

    err_rep = math.sqrt(sum((a - b) ** 2 for a, b in zip(decoded_rep, true_sum)))
    assert err_rep < 1e-12, f"Expected exact recovery in Repetition Code, got err_rep={err_rep}"

    # 3. Verify Cyclic Code & Fourier Syndrome Decoder (Lemma 3, Lemma 4, Theorem 5)
    # Use P = 7 nodes, s = 1 adversarial node, r = 2s + 1 = 3
    p_cyc = 7
    s_cyc = 1
    r_cyc = 2 * s_cyc + 1  # 3
    G_cyc = [[rng.uniform(-1.5, 1.5) for _ in range(p_cyc)] for _ in range(d)]
    true_sum_cyc = [sum(G_cyc[coord][k] for k in range(p_cyc)) for coord in range(d)]

    # Construct P x P IDFT matrix C: C_{j,k} = (1/sqrt(P)) exp(2*pi*i * j * k / P)
    C = [
        [
            cmath.exp(2j * math.pi * j * k / p_cyc) / math.sqrt(p_cyc)
            for k in range(p_cyc)
        ]
        for j in range(p_cyc)
    ]
    C_L = C[: p_cyc - 2 * s_cyc]  # (P - 2s) x P = 5 x 7
    C_R = C[p_cyc - 2 * s_cyc :]  # 2s x P = 2 x 7

    # Cyclic allocation matrix A^Cyc: node j is assigned r_cyc consecutive samples starting at j
    A_cyc = [[0 for _ in range(p_cyc)] for _ in range(p_cyc)]
    for j in range(p_cyc):
        for offset in range(r_cyc):
            A_cyc[j][(j + offset) % p_cyc] = 1

    # Construct W = [Q  1_P] * C_L so that A_cyc[k][j] == 0 => W[j][k] == 0
    # (row j of W is [q_j  1] * C_L, and column k of W is supported on samples j assigned to node k)
    W = [[0j for _ in range(p_cyc)] for _ in range(p_cyc)]
    m_rows = p_cyc - 2 * s_cyc  # 5
    for j in range(p_cyc):
        zero_indices = [k for k in range(p_cyc) if A_cyc[k][j] == 0]  # size P - r = 4 = m_rows - 1
        a_sys = [
            [C_L[row_idx][k] for row_idx in range(m_rows - 1)]
            for k in zero_indices
        ]
        b_sys = [-C_L[m_rows - 1][k] for k in zero_indices]
        q_j = solve_complex_linear_system(a_sys, b_sys)
        coeff = q_j + [1.0 + 0j]
        for k in range(p_cyc):
            W[j][k] = sum(coeff[row_idx] * C_L[row_idx][k] for row_idx in range(m_rows))
            if A_cyc[k][j] == 0:
                assert abs(W[j][k]) < 1e-10

    # Encode Z = G_cyc * W (d x P) and inject adversarial corruption at node adv_idx = 4
    adv_idx = 4
    R_cyc = [
        [
            sum(G_cyc[coord][k] * W[k][j] for k in range(p_cyc))
            + ((25.0 - 17.0j) if j == adv_idx else 0j)
            for j in range(p_cyc)
        ]
        for coord in range(d)
    ]

    # Syndrome detection phi(R_cyc): compute h_{P-2s..P-1} = f * R_cyc * C_R^dagger
    f_vec = [rng.gauss(1.0, 1.0) for _ in range(d)]
    f_R = [sum(f_vec[coord] * R_cyc[coord][j] for coord in range(d)) for j in range(p_cyc)]
    h_tail = [
        sum(f_R[j] * C_R[r_idx][j].conjugate() for j in range(p_cyc))
        for r_idx in range(2 * s_cyc)
    ]
    # For s = 1: h_{P-2} * beta_0 = h_{P-1} => beta_0 = h_{P-1} / h_{P-2}
    beta_0 = h_tail[1] / h_tail[0]
    h_full = [0j for _ in range(p_cyc)]
    h_full[p_cyc - 2] = h_tail[0]
    h_full[p_cyc - 1] = h_tail[1]
    for ell in range(p_cyc - 2):
        h_full[ell] = (beta_0 ** (ell + 2)) * h_tail[0]
    # Compute IDFT t = C * h_full
    t_vec = [
        sum(C[j][k] * h_full[k] for k in range(p_cyc))
        for j in range(p_cyc)
    ]
    detected_v = [j for j in range(p_cyc) if abs(t_vec[j]) > 1e-6]
    assert detected_v == [adv_idx], f"Expected detected_v={[adv_idx]}, got {detected_v}"

    # Recover u^Cyc = R_{., U} b where W_{., U} b = 1_P using first P - 2s honest nodes in U
    u_honest = [j for j in range(p_cyc) if j not in detected_v][:m_rows]
    # Solve [C_L]_{., u_honest} * b_bar = [0, ..., 0, 1]^T
    a_rec = [[C_L[row_idx][j] for j in u_honest] for row_idx in range(m_rows)]
    b_rhs = [0j for _ in range(m_rows - 1)] + [1.0 + 0j]
    b_bar = solve_complex_linear_system(a_rec, b_rhs)
    u_cyc = [
        sum(R_cyc[coord][u_honest[idx]] * b_bar[idx] for idx in range(m_rows)).real
        for coord in range(d)
    ]
    err_cyc = math.sqrt(sum((a - b) ** 2 for a, b in zip(u_cyc, true_sum_cyc)))
    assert err_cyc < 1e-9, f"Expected exact recovery in Cyclic Code, got err_cyc={err_cyc}"

    print(
        f"[PASS] Round 524 DRACO (Chen et al. 2018): "
        f"thm1_tau4_indistinguishable=True, err_rep={err_rep:.2e}, "
        f"cyclic_detected={detected_v}, err_cyc={err_cyc:.2e}"
    )


if __name__ == "__main__":
    main()
