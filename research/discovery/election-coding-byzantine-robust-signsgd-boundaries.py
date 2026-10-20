#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 536:
Election Coding for Distributed Learning: Protecting SignSGD against Byzantine Attacks
(Sohn, Han, Choi, & Moon, NeurIPS 2020 / arXiv:1910.06093).
"""

import itertools


def build_deterministic_election_matrix(n, b):
    """Algorithm 1 (p. 6): Deterministic data allocation matrix G in {0,1}^{n x n}
    achieving perfect b-Byzantine tolerance for odd n and 0 < b < floor(n/2).
    """
    assert n % 2 == 1 and 0 < b < (n // 2)
    s = (n - 1) // 2 - b
    L = (n - (2 * b + 1)) // (2 * (b + 1)) + 1
    G = [[0] * n for _ in range(n)]

    # Step 1: top-left s x s submatrix is I_s
    for i in range(s):
        G[i][i] = 1

    # Step 2: bottom (n - s - L) rows are all-ones
    for i in range(s + L, n):
        for j in range(n):
            G[i][j] = 1

    # Step 3: middle L rows A = G[s : s+L, s : n] shifted by b+1 with 2b+1 ones per row
    for l_idx in range(L):
        row = s + l_idx
        start_col = s + l_idx * (b + 1)
        for offset in range(2 * b + 1):
            col = start_col + offset
            if col < n:
                G[row][col] = 1
    return G


def theoretical_redundancy(n, b):
    """Equation (5) in Theorem 3 (p. 7)."""
    L = (n - (2 * b + 1)) // (2 * (b + 1)) + 1
    return (n + (2 * b + 1)) / 2.0 - (L - 0.5) * (n - (2 * b + 1)) / n


def maj_bits(bits):
    """Majority vote over binary {0, 1} list of odd length."""
    assert len(bits) % 2 == 1
    return 1 if sum(bits) > len(bits) // 2 else 0


def encode_workers(m_bits, G):
    n = len(G)
    c = []
    for i in range(n):
        assigned = [m_bits[j] for j in range(n) if G[i][j] == 1]
        c.append(maj_bits(assigned))
    return c


def check_perfect_b_tolerance(n, b, G):
    """Exhaustively verify P(hat_mu != mu) = 0 across all 2^n partition sign vectors
    and all worst-case b-Byzantine bit-flip attacks, plus Lemma 2 condition.
    """
    half = n // 2
    for m_bits in itertools.product([0, 1], repeat=n):
        mu = maj_bits(m_bits)
        c = encode_workers(m_bits, G)
        # Check Lemma 2 condition when weight ||m||_0 == floor(n/2)
        if sum(m_bits) == half:
            assert sum(c) <= half - b, f"Lemma 2 violated: sum(c)={sum(c)} > {half - b}"

        # Worst-case b-Byzantine attack flips up to b worker bits toward (1 - mu)
        if mu == 0:
            y_worst_sum = min(n, sum(c) + b)
            hat_mu = 1 if y_worst_sum > half else 0
        else:
            y_worst_sum = max(0, sum(c) - b)
            hat_mu = 1 if y_worst_sum > half else 0
        assert hat_mu == mu, f"Election Coding failed for m={m_bits}, mu={mu}, c={c}"


def main():
    # Case 1: n = 5, b = 1 (Figure 2, p. 3 & Table A.1, p. 10: r = 3.8)
    G_5_1 = build_deterministic_election_matrix(5, 1)
    r_5_1 = sum(sum(row) for row in G_5_1) / 5.0
    r_5_1_theo = theoretical_redundancy(5, 1)
    assert abs(r_5_1 - 3.8) < 1e-12
    assert abs(r_5_1 - r_5_1_theo) < 1e-12
    check_perfect_b_tolerance(5, 1, G_5_1)

    # Verify uncoded SignSGD-MV (G = I_5) fails on m = [1, 1, 0, 0, 0] under b = 1 flip
    m_test = [1, 1, 0, 0, 0]
    mu_true = maj_bits(m_test)  # 0
    y_uncoded_attacked = [1, 1, 1, 0, 0]  # 1 Byzantine flips node 2 from 0 to 1
    assert maj_bits(y_uncoded_attacked) != mu_true

    # Case 2: n = 7, b = 2
    G_7_2 = build_deterministic_election_matrix(7, 2)
    r_7_2 = sum(sum(row) for row in G_7_2) / 7.0
    r_7_2_theo = theoretical_redundancy(7, 2)
    assert abs(r_7_2 - r_7_2_theo) < 1e-12
    check_perfect_b_tolerance(7, 2, G_7_2)

    # Case 3: n = 9, b = 2
    G_9_2 = build_deterministic_election_matrix(9, 2)
    r_9_2 = sum(sum(row) for row in G_9_2) / 9.0
    r_9_2_theo = theoretical_redundancy(9, 2)
    assert abs(r_9_2 - r_9_2_theo) < 1e-12
    check_perfect_b_tolerance(9, 2, G_9_2)

    print(
        f"[PASS] Round 536 Election Coding verified: r(5,1)={r_5_1:.2f}, "
        f"r(7,2)={r_7_2:.4f}, r(9,2)={r_9_2:.4f}, P(hat_mu != mu)=0 across all 2^n states"
    )


if __name__ == "__main__":
    main()
