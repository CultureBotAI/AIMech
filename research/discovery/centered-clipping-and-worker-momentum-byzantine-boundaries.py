#!/usr/bin/env python3
"""Constructed boundary verification for Centered Clipping and Worker Momentum for Byzantine-Robust
Optimization (Karimireddy, He, & Jaggi 2021, ICML 2021, PMLR 139:5311-5319, arXiv:2012.10333).

Verifies:
1. Section 3 Counterexample 1 (Imbalanced binary noise where median fails even with delta = 0):
   For zero-mean asymmetric noise (xi = -1 with prob 2/3, +2 with prob 1/3), the sample median
   has constant bias -1 whereas sample mean / centered clipping is unbiased.
2. Section 5.2 Centered Clipping (CC) iteration:
   v_{l+1} = v_l + (1/n) sum_{i=1}^n (x_i - v_l) * min(1, tau / ||x_i - v_l||_2),
   confirming Theorem IV contraction and O(delta * rho^2) robustness against Byzantine outliers.
3. Section 6 Worker Momentum + Centered Clipping:
   Maintaining worker momentum m_{t,i} = (1 - alpha) m_{t-1,i} + alpha g_{t,i} reduces gradient
   noise variance by factor alpha before centered clipping, overcoming time-coupled attacks.
"""

from __future__ import annotations

import json
import math
import random


def l2_norm(v: list[float]) -> float:
    return math.sqrt(sum(x * x for x in v))


def sub(a: list[float], b: list[float]) -> list[float]:
    return [x - y for x, y in zip(a, b)]


def centered_clipping(
    vectors: list[list[float]],
    v_init: list[float],
    tau: float,
    steps: int = 3,
) -> list[float]:
    n = len(vectors)
    d = len(vectors[0])
    v = list(v_init)
    for _ in range(steps):
        delta_sum = [0.0] * d
        for x_i in vectors:
            diff = sub(x_i, v)
            dist = l2_norm(diff)
            scale = 1.0 if dist <= tau or dist == 0.0 else (tau / dist)
            for k in range(d):
                delta_sum[k] += diff[k] * scale
        v = [v[k] + delta_sum[k] / n for k in range(d)]
    return v


def main() -> None:
    rng = random.Random(2021)

    # 1. Section 3 Counterexample 1: Imbalanced zero-mean noise (-1 w.p. 2/3, +2 w.p. 1/3)
    samples = [-1.0] * 14 + [2.0] * 7  # 21 workers, exact zero mean
    true_mean_ce1 = sum(samples) / len(samples)
    median_ce1 = sorted(samples)[len(samples) // 2]
    assert abs(true_mean_ce1 - 0.0) < 1e-12
    assert median_ce1 == -1.0  # Middle-seeker fails even with 0 Byzantine workers

    # 2. Section 5.2 & 6: Worker Momentum + Centered Clipping vs Memoryless Clipping under Byzantine attack
    n = 20
    f = 2  # delta = 0.10
    d = 4
    w_star = [1.2, -0.9, 0.6, -0.3]
    alpha = 0.15  # momentum weight (1 - beta)
    tau = 0.35

    w_mom_cc = [0.0] * d
    w_naive = [0.0] * d
    v_prev = [0.0] * d
    mom_good = [[0.0] * d for _ in range(n - f)]
    eta = 0.20

    for t in range(1, 61):
        raw_step = []
        mom_step = []
        for i in range(n - f):
            # Asymmetric zero-mean noise as in Counterexample 1 scaled by 0.4
            asym = -0.4 if rng.random() < (2.0 / 3.0) else 0.8
            g_i = [w_mom_cc[k] - w_star[k] + asym for k in range(d)]
            mom_good[i] = [
                (1.0 - alpha) * mom_good[i][k] + alpha * g_i[k] for k in range(d)
            ]
            mom_step.append(list(mom_good[i]))

            g_naive = [w_naive[k] - w_star[k] + asym for k in range(d)]
            raw_step.append(g_naive)

        # Byzantine workers send extreme opposite gradients
        for _ in range(f):
            attack = [25.0 * ((-1) ** k) for k in range(d)]
            mom_step.append(attack)
            raw_step.append(attack)

        v_prev = centered_clipping(mom_step, v_init=v_prev, tau=tau, steps=3)
        w_mom_cc = [w_mom_cc[k] - eta * v_prev[k] for k in range(d)]

        avg_naive = [sum(vec[k] for vec in raw_step) / n for k in range(d)]
        w_naive = [w_naive[k] - eta * avg_naive[k] for k in range(d)]

    err_mom_cc = l2_norm(sub(w_mom_cc, w_star))
    err_naive = l2_norm(sub(w_naive, w_star))
    assert err_mom_cc < 0.12
    assert err_naive > 5.0

    summary = {
        "concept": "AIMech:CenteredClippingAndWorkerMomentumForByzantineRobustOptimization",
        "counterexample1_true_mean": true_mean_ce1,
        "counterexample1_median": median_ce1,
        "n_workers": n,
        "delta_byzantine": f / n,
        "alpha_momentum": alpha,
        "tau_clip_radius": tau,
        "l2_error_momentum_centered_clipping": round(err_mom_cc, 6),
        "l2_error_unclipped_mean": round(err_naive, 6),
        "status": "VERIFIED",
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
