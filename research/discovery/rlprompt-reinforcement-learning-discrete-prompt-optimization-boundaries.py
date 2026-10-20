#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 726: RLPrompt (Deng et al., EMNLP 2022)."""

import math


def verify_rlprompt() -> None:
    # 1. Piecewise margin reward for few-shot classification (Eq. 4):
    # Gap_z(c) = P_z(c) - max_{c' != c} P_z(c'), Correct = 1[Gap_z(c) > 0]
    # R(x, c) = lambda_1^{1 - Correct} * lambda_2^{Correct} * Gap_z(c), with lambda_1 = 180, lambda_2 = 200
    lam1, lam2 = 180.0, 200.0

    def piecewise_reward(probs: dict[str, float], gold_c: str) -> float:
        max_other = max(v for k, v in probs.items() if k != gold_c)
        gap = probs[gold_c] - max_other
        correct = 1 if gap > 0.0 else 0
        return (lam1 ** (1 - correct)) * (lam2**correct) * gap

    r_correct = piecewise_reward({"pos": 0.65, "neg": 0.35}, "pos")
    r_wrong = piecewise_reward({"pos": 0.35, "neg": 0.65}, "pos")
    assert r_correct > 0.0 and r_wrong < 0.0
    # Positive correct predictions receive a larger multiplier (lambda_2 > lambda_1) than equal-magnitude errors
    assert math.isclose(abs(r_correct) / abs(r_wrong), lam2 / lam1, rel_tol=1e-12)

    # 2. Input-specific z-score reward normalization across sampled prompt batch Z(x) (Eq. 3):
    # z-score(z, x) = (R_x(z) - mean_{z' in Z(x)} R_x(z')) / stdev_{z' in Z(x)} R_x(z')
    rewards_x = [12.0, 18.0, 24.0, 30.0]
    mean_r = sum(rewards_x) / len(rewards_x)
    std_r = math.sqrt(sum((r - mean_r) ** 2 for r in rewards_x) / len(rewards_x))
    z_scores = [(r - mean_r) / std_r for r in rewards_x]
    assert math.isclose(sum(z_scores), 0.0, abs_tol=1e-12)
    assert math.isclose(sum(z * z for z in z_scores) / len(z_scores), 1.0, rel_tol=1e-12)
    print("RLPrompt verification passed.")


if __name__ == "__main__":
    verify_rlprompt()
