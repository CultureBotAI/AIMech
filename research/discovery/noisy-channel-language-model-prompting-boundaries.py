#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 729: Noisy Channel Prompting (Min et al., ACL 2022)."""

import math


def verify_noisy_channel_prompting() -> None:
    # 1. Compare Direct P(c_i | x), Direct++ P(c_i | x) / P(c_i | NULL), and Noisy Channel P(x | v(c_i)) (Section 3-4, Table 1):
    # Suppose class c_1 is rare/unseen in imbalanced demonstrations so direct unconditional prior P_LM(v(c_0)) >> P_LM(v(c_1)),
    # while the input x is much better explained by conditioning on v(c_1): P_LM(x | v(c_1)) > P_LM(x | v(c_0)).
    # Concat-based Channel: P_LM(x | v(c^1), x^1, ..., v(c^K), x^K, v(c_i))
    # Ensemble-based Channel: prod_{j=1}^K P_LM(x | v(c^j), x^j, v(c_i))
    p_x_given_demo_and_c0 = [0.02, 0.03, 0.025]
    p_x_given_demo_and_c1 = [0.08, 0.07, 0.09]

    ens_c0 = math.prod(p_x_given_demo_and_c0)
    ens_c1 = math.prod(p_x_given_demo_and_c1)
    assert ens_c1 > ens_c0

    # 2. Memory complexity reduction of Ensemble-based vs. Concat-based demonstrations (Section 4.1.3):
    # Self-attention memory scales as O(K^2) for concatenating K examples vs. O(K) for K independent 1-shot forward passes:
    k_demos = 16
    l_ex = 64
    concat_attn_ops = (k_demos * l_ex) ** 2
    ensemble_attn_ops = k_demos * (l_ex**2)
    assert concat_attn_ops // ensemble_attn_ops == k_demos

    # 3. Length-normalized log-probability of input x = x_1..x_{t_x} given prefix [u_1..u_n, v(c_i)] in Channel Prompt Tuning:
    token_logprobs_c0 = [-2.1, -1.8, -2.4, -1.9]
    token_logprobs_c1 = [-1.1, -0.9, -1.2, -1.0]
    score_c0 = sum(token_logprobs_c0) / len(token_logprobs_c0)
    score_c1 = sum(token_logprobs_c1) / len(token_logprobs_c1)
    assert score_c1 > score_c0
    print("Noisy Channel Language Model Prompting verification passed.")


if __name__ == "__main__":
    verify_noisy_channel_prompting()
