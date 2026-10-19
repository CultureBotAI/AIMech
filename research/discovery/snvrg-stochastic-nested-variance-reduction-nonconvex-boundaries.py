#!/usr/bin/env python3
"""Constructed boundary verification for SNVRG: Stochastic Nested Variance Reduction (Zhou, Xu, & Gu 2018/2020)."""

import math
import random


def main() -> None:
    # 1. Verify Lemma 4.1 & Appendix A.1 (Eqs. (A.2)-(A.6)) nested loop and batch schedule:
    # For B = 2^{2^K} with K >= 2, T_1 = 2, T_l = 2^{2^{l-2}} (l >= 2), B_1 = 6^K * B, B_l = 6^{K-l+1} * B / 2^{2^{l-1}} (l >= 2):
    # - Total inner steps per epoch: T = prod_{l=1}^K T_l = 2 * prod_{l=2}^K 2^{2^{l-2}} = 2^{2^{K-1}} = B^{1/2}.
    # - Condition of Lemma A.1: B_l >= 6^{K-l+1} * (prod_{s=l}^K T_s)^2 for all 1 <= l <= K.
    # - Total gradient evaluations per epoch: B + 2 * sum_{l=1}^K B_l * prod_{j=1}^l T_j <= 7 * B * log2(B)^3.
    for K in (2, 3, 4):
        B = 2 ** (2**K)
        T_list = [2] + [2 ** (2 ** (l - 2)) for l in range(2, K + 1)]
        B_list = [6**K * B] + [(6 ** (K - l + 1)) * B // (2 ** (2 ** (l - 1))) for l in range(2, K + 1)]
        T_prod = 1
        for tl in T_list:
            T_prod *= tl
        assert T_prod == int(math.isqrt(B))

        # Check Lemma A.1 condition: B_l >= 6^{K-l+1} * (prod_{s=l}^K T_s)^2
        for l_idx in range(1, K + 1):
            tail_prod = 1
            for s_idx in range(l_idx, K + 1):
                tail_prod *= T_list[s_idx - 1]
            rhs = (6 ** (K - l_idx + 1)) * (tail_prod**2)
            assert B_list[l_idx - 1] == rhs

        # Check Lemma C.2 recurrence (Definition B.1, Eqs. (B.2)-(B.3), (C.4)-(C.5))
        L = 1.0
        M = 6.0 * L
        c_T = {}
        c_0 = {}
        for s in range(K, 0, -1):
            Ts = T_list[s - 1]
            Bs = B_list[s - 1]
            tail_s = 1
            for l_idx in range(s, K + 1):
                tail_s *= T_list[l_idx - 1]
            tail_s_plus = 1
            for l_idx in range(s + 1, K + 1):
                tail_s_plus *= T_list[l_idx - 1]
            c_curr = M / ((6 ** (K - s + 1)) * tail_s)
            c_T[s] = c_curr
            for _ in range(Ts - 1, -1, -1):
                c_curr = (1.0 + 1.0 / Ts) * c_curr + (3.0 * (L**2) / M) * (tail_s_plus / Bs)
            c_0[s] = c_curr

        assert c_0[K] * (1.0 + T_list[K - 1]) < M
        for s in range(2, K + 1):
            assert c_0[s - 1] * (1.0 + T_list[s - 2]) < c_T[s]

        # Check Eq. (A.3)-(A.6) total gradient evaluations
        grad_evals = B
        prefix_prod = 1
        for l_idx in range(1, K + 1):
            prefix_prod *= T_list[l_idx - 1]
            grad_evals += 2 * B_list[l_idx - 1] * prefix_prod
        log2_B = 2**K
        assert grad_evals <= 7 * B * (log2_B**3)

    # 2. Verify Proposition C.1 nested reference point schedule (Eq. (3.1)) for K = 2 (T1 = 2, T2 = 2, T = 4)
    T1, T2 = 2, 2
    T_tot = T1 * T2
    ref_indices = []
    for t in range(T_tot):
        t0 = (t // (T1 * T2)) * (T1 * T2)
        t1 = (t // T2) * T2
        t2 = t
        ref_indices.append((t0, t1, t2))
    assert ref_indices == [(0, 0, 0), (0, 0, 1), (0, 2, 2), (0, 2, 3)]

    print(
        f"[PASS] SNVRG boundaries verified: T=B^(1/2), Lemma A.1 & Lemma C.2 hold for K=2,3,4, "
        f"ref_indices(K=2)={ref_indices}"
    )


if __name__ == "__main__":
    main()
