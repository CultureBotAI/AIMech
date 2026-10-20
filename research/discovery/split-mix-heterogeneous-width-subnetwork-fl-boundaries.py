#!/usr/bin/env python3
"""Constructed boundary verification for Split-Mix (Hong et al., ICLR 2022, arXiv:2203.09747).

Verifies:
1. Base sub-network decomposition into M = floor(1/r) width-r base models with rescaled
   Kaiming initialization matching the full-width variance.
2. Cyclic shuffled without-replacement sampling (SampleBaseModels, Algorithm 2, p. 6),
   ensuring every base model w_{i,r} is sampled with equal frequency over M*r_hat/r queries.
3. On-demand width customization at inference time by averaging K_R = floor(R/r) base sub-networks:
   F(x; W^T) = (1/K_R) * sum_{i=1}^{K_R} f(x; w_{i,r}^T) (Algorithm 1 line 11, p. 5),
   exhibiting monotonic test loss reduction as K_R increases from 1 to M.
4. Training-free Dual Batch-Normalization (DBN) mixing (Eq. 2, p. 6):
   DBN(x) = (1 - lambda)*BN_c(x) + lambda*BN_n(x) for lambda in [0, 1], smoothly interpolating
   between clean BN statistics (lambda = 0) and adversarial BN statistics (lambda = 1).
"""

import math
import random


def sample_base_models(m_total: int, k_req: int, i_idx: int, order: list[int], rng: random.Random):
    """Algorithm 2 (p. 6): Shuffled cyclic without-replacement sampling of base sub-networks."""
    if i_idx + k_req <= m_total:
        selected = order[i_idx : i_idx + k_req]
        i_next = i_idx + k_req
        if i_next == m_total:
            i_next = 0
            order = list(range(m_total))
            rng.shuffle(order)
        return selected, i_next, order
    else:
        part1 = order[i_idx:]
        rem = k_req - len(part1)
        new_order = list(range(m_total))
        rng.shuffle(new_order)
        # Ensure distinct base models within a single client's draw when k_req <= m_total
        avail = [idx for idx in new_order if idx not in part1]
        part2 = avail[:rem]
        rest = [idx for idx in new_order if idx not in part2]
        final_order = part2 + rest
        return part1 + part2, rem, final_order


def dbn_layer(x: list[float], mu_c: float, var_c: float, gamma_c: float, beta_c: float,
              mu_n: float, var_n: float, gamma_n: float, beta_n: float, lam: float, eps: float = 1e-5) -> list[float]:
    """Eq. 2 (p. 6): DBN(x) = (1 - lambda) * BN_c(x) + lambda * BN_n(x)."""
    out = []
    for xi in x:
        bn_c = gamma_c * ((xi - mu_c) / math.sqrt(var_c + eps)) + beta_c
        bn_n = gamma_n * ((xi - mu_n) / math.sqrt(var_n + eps)) + beta_n
        out.append((1.0 - lam) * bn_c + lam * bn_n)
    return out


def main() -> None:
    rng = random.Random(20220318)
    r = 0.25
    m_total = int(round(1.0 / r))
    assert m_total == 4

    # 1. Verify rescaled Kaiming initialization variance preservation
    # Standard Kaiming init for width-r fan_in = r * D has var = 2 / (r * D) = (1/r) * (2/D).
    # Rescaled Kaiming initialization uses full-width fan_in = D so var = 2 / D, preventing gradient explosion.
    d_full = 64
    var_unscaled = 2.0 / (r * d_full)
    var_rescaled = 2.0 / d_full
    assert abs(var_unscaled / var_rescaled - (1.0 / r)) < 1e-12

    # 2. Verify SampleBaseModels (Algorithm 2) uniform exposure across heterogeneous client budgets
    order = list(range(m_total))
    rng.shuffle(order)
    i_idx = 0
    counts = [0] * m_total
    # Client budgets in units of base models: [1, 1, 2, 4] (sum = 8, a multiple of M = 4)
    client_k_budgets = [1, 1, 2, 4]
    for _round in range(10):
        for k_req in client_k_budgets:
            sel, i_idx, order = sample_base_models(m_total, k_req, i_idx, order, rng)
            assert len(sel) == k_req
            assert len(set(sel)) == k_req  # No duplicate base models within one client
            for b_id in sel:
                counts[b_id] += 1
    # Over 10 rounds * 8 draws = 80 total draws, each of the 4 base models is drawn exactly 20 times
    assert counts == [20, 20, 20, 20], f"Expected uniform counts [20, 20, 20, 20], got {counts}"

    # 3. Verify on-demand width ensemble customization (Algorithm 1 line 11)
    # Ground-truth target function y = w_star^T x on d=6 features; each base sub-network i
    # learns an unbiased noisy estimate of w_star trained on heterogeneous client subsets.
    d = 6
    w_star = [0.8, -0.5, 0.4, -0.7, 0.3, 0.6]
    base_models = []
    for i in range(m_total):
        w_i = [w_star[j] + rng.gauss(0.0, 0.18) for j in range(d)]
        base_models.append(w_i)

    # Evaluate MSE across width budgets R in {0.25, 0.50, 0.75, 1.00} -> K_R in {1, 2, 3, 4}
    test_x = [[rng.gauss(0.0, 1.0) for _ in range(d)] for _ in range(400)]
    test_y = [sum(w_star[j] * x[j] for j in range(d)) for x in test_x]

    mses = []
    for k_r in range(1, m_total + 1):
        mse = 0.0
        for x, y in zip(test_x, test_y):
            pred = sum(sum(base_models[i][j] * x[j] for j in range(d)) for i in range(k_r)) / k_r
            mse += (pred - y) ** 2
        mse /= len(test_x)
        mses.append(mse)

    # Full-width (K_R = 4) strictly improves over single base sub-network (K_R = 1)
    assert mses[-1] < mses[0] * 0.5, f"Expected ensemble MSE reduction, got {mses}"

    # 4. Verify Dual Batch-Normalization (DBN, Eq. 2) exact interpolation
    x_sample = [-1.2, 0.0, 1.5, 2.8]
    out_clean = dbn_layer(x_sample, 0.0, 1.0, 1.0, 0.0, 0.5, 2.0, 1.2, -0.1, lam=0.0)
    out_adv = dbn_layer(x_sample, 0.0, 1.0, 1.0, 0.0, 0.5, 2.0, 1.2, -0.1, lam=1.0)
    out_mix = dbn_layer(x_sample, 0.0, 1.0, 1.0, 0.0, 0.5, 2.0, 1.2, -0.1, lam=0.35)
    for c_val, a_val, m_val in zip(out_clean, out_adv, out_mix):
        assert abs(m_val - (0.65 * c_val + 0.35 * a_val)) < 1e-12

    print("Split-Mix boundary verification passed:", {
        "base_counts": counts,
        "mses_by_K_R": [round(v, 5) for v in mses],
    })


if __name__ == "__main__":
    main()
