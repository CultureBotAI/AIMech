#!/usr/bin/env python3
"""Constructed boundary verification for TwinBERT (Lu, Jiao, & Zhang, CIKM 2020, arXiv:2002.06275)."""

import math


def weighted_average_pooling(hidden_vecs: list[list[float]], weights: list[float]) -> list[float]:
    """Section 4.3: Weighted-average pooling over token vectors."""
    w_sum = sum(weights)
    dim = len(hidden_vecs[0])
    return [
        sum(weights[t] * hidden_vecs[t][c] for t in range(len(hidden_vecs))) / w_sum
        for c in range(dim)
    ]


def twinbert_cos_score(q: list[float], k: list[float], a_scale: float, b_bias: float) -> tuple[float, float]:
    """Section 4.4 Eq. (1): cos(q, k) = (q . k) / (||q|| ||k||) + logistic regression alignment to [0, 1]."""
    dot = sum(q[i] * k[i] for i in range(len(q)))
    nq = math.sqrt(sum(x * x for x in q))
    nk = math.sqrt(sum(x * x for x in k))
    cos_val = dot / (nq * nk)
    prob = 1.0 / (1.0 + math.exp(-(a_scale * cos_val + b_bias)))
    return cos_val, prob


def twinbert_res_score(
    q: list[float],
    k: list[float],
    w_res: list[list[float]],
    b_res: list[float],
    w_lr: list[float],
    b_lr: float,
) -> tuple[list[float], float]:
    """Section 4.4 Eq. (2): x = max(q, k), y = F(x, W, b) + x, followed by logistic regression layer."""
    x = [max(q[i], k[i]) for i in range(len(q))]
    f_x = [
        max(0.0, sum(w_res[r][c] * x[c] for c in range(len(x))) + b_res[r])
        for r in range(len(w_res))
    ]
    y = [f_x[i] + x[i] for i in range(len(x))]
    logit = sum(w_lr[i] * y[i] for i in range(len(y))) + b_lr
    prob = 1.0 / (1.0 + math.exp(-logit))
    return y, prob


def soft_target_temperature(logits: list[float], temp: float = 2.0) -> list[float]:
    """Section 4.5: y_i = exp(z_i / T) / sum_j exp(z_j / T) with T = 2."""
    scaled = [z / temp for z in logits]
    m = max(scaled)
    exps = [math.exp(s - m) for s in scaled]
    z_sum = sum(exps)
    return [e / z_sum for e in exps]


def main() -> None:
    q_tokens = [[1.0, 0.2, 0.5], [0.8, 0.4, 0.6]]
    k_pos_tokens = [[0.9, 0.8, 0.7], [0.85, 0.75, 0.65]]
    k_neg_tokens = [[-0.8, -0.5, -0.4], [-0.6, -0.7, -0.5]]
    weights = [0.6, 0.4]

    q_vec = weighted_average_pooling(q_tokens, weights)
    k_pos = weighted_average_pooling(k_pos_tokens, weights)
    k_neg = weighted_average_pooling(k_neg_tokens, weights)

    # 1. TwinBERT_cos aligns [-1, 1] cosine into (0, 1) and preserves Euclidean distance order on unit vectors:
    cos_pos, p_cos_pos = twinbert_cos_score(q_vec, k_pos, a_scale=4.0, b_bias=0.0)
    cos_neg, p_cos_neg = twinbert_cos_score(q_vec, k_neg, a_scale=4.0, b_bias=0.0)
    assert -1.0 <= cos_neg < 0.0 < cos_pos <= 1.0
    assert 0.0 < p_cos_neg < 0.5 < p_cos_pos < 1.0

    # Unit-norm Euclidean distance squared ||q_hat - k_hat||^2 == 2 * (1 - cos(q, k)):
    nq = math.sqrt(sum(x * x for x in q_vec))
    nk_p = math.sqrt(sum(x * x for x in k_pos))
    q_hat = [x / nq for x in q_vec]
    kp_hat = [x / nk_p for x in k_pos]
    euclid_sq = sum((q_hat[i] - kp_hat[i]) ** 2 for i in range(len(q_hat)))
    assert abs(euclid_sq - 2.0 * (1.0 - cos_pos)) < 1e-12

    # 2. TwinBERT_res max-pooling + residual connection:
    w_res = [[0.5, 0.1, 0.2], [0.1, 0.4, 0.1], [0.2, 0.1, 0.5]]
    b_res = [0.0, 0.0, 0.0]
    w_lr = [1.2, 0.8, 1.0]
    y_pos, p_res_pos = twinbert_res_score(q_vec, k_pos, w_res, b_res, w_lr, b_lr=-1.0)
    y_neg, p_res_neg = twinbert_res_score(q_vec, k_neg, w_res, b_res, w_lr, b_lr=-1.0)
    assert p_res_pos > p_res_neg

    # 3. Temperature T=2 softens teacher distribution compared to T=1:
    teacher_logits = [2.4, -0.6]
    soft_t1 = soft_target_temperature(teacher_logits, temp=1.0)
    soft_t2 = soft_target_temperature(teacher_logits, temp=2.0)
    assert 0.5 < soft_t2[0] < soft_t1[0] < 1.0

    print("TwinBERT boundary verification passed:")
    print(f"  TwinBERT_cos: cos_pos={cos_pos:.4f} (p={p_cos_pos:.4f}) > cos_neg={cos_neg:.4f} (p={p_cos_neg:.4f})")
    print(f"  TwinBERT_res: p_res_pos={p_res_pos:.4f} > p_res_neg={p_res_neg:.4f}")
    print(f"  Teacher soft target at T=2: {soft_t2[0]:.4f} vs T=1: {soft_t1[0]:.4f}")


if __name__ == "__main__":
    main()
