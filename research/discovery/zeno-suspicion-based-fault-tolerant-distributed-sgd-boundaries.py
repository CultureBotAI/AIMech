#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 523:
Zeno (Distributed Stochastic Gradient Descent with Suspicion-Based Fault-Tolerance)
Xie, Koyejo, & Gupta, ICML 2019 (PMLR 97:6893-6901, arXiv:1805.10032).

Verifies:
1. Definition 2 (Stochastic Descendant Score):
   Score_{gamma, rho}(u, x) = f_r(x) - f_r(x - gamma * u) - rho * ||u||_2^2.
2. Definition 3 & Algorithm 1 (Zeno_b aggregation):
   Rank m candidate updates in descending order of Score_{gamma, rho}(tilde_v_{(i)}, x)
   and average the top m - b candidates (where m > b >= q), operating even when a
   majority of workers are Byzantine (q >= m / 2, as long as q < m).
3. Lemma 1 order-preservation inequality:
   Score_{gamma, rho}(tilde_v_{(i)}, x) >= Score_{gamma, rho}(v_{(i)}, x) for all i in [m - q],
   where {v_1, ..., v_{m-q}} are the true honest worker gradients.
"""

import math
import random


def f_val(x, a_target):
    """Quadratic validation loss f_r(x) = 0.5 * ||x - a_target||_2^2."""
    return 0.5 * sum((xj - aj) ** 2 for xj, aj in zip(x, a_target))


def grad_f(x, a_target):
    return [xj - aj for xj, aj in zip(x, a_target)]


def stochastic_descendant_score(u, x, a_val, gamma, rho):
    """Definition 2: Score_{gamma, rho}(u, x) = f_r(x) - f_r(x - gamma*u) - rho*||u||^2."""
    x_next = [xj - gamma * uj for xj, uj in zip(x, u)]
    norm_u_sq = sum(uj * uj for uj in u)
    return f_val(x, a_val) - f_val(x_next, a_val) - rho * norm_u_sq


def zeno_aggregate(candidates, x, a_val, gamma, rho, b):
    """Definition 3: Zeno_b averages the m - b candidates with highest descendant score."""
    m = len(candidates)
    d = len(candidates[0])
    scored = [
        (stochastic_descendant_score(u, x, a_val, gamma, rho), idx, u)
        for idx, u in enumerate(candidates)
    ]
    scored.sort(key=lambda item: item[0], reverse=True)
    kept = scored[: m - b]
    agg = [
        sum(u[j] for _, _, u in kept) / (m - b)
        for j in range(d)
    ]
    return agg, [s for s, _, _ in scored]


def coordinate_median(candidates):
    m = len(candidates)
    d = len(candidates[0])
    out = []
    for j in range(d):
        col = sorted(candidates[i][j] for i in range(m))
        out.append(col[m // 2])
    return out


def l2_dist(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def main():
    rng = random.Random(2019)
    d = 5
    m = 10
    # Extreme dishonest-majority regime: q = 6 Byzantine workers out of m = 10 (q > m/2),
    # with trimming parameter b = 6 (so m - b = 4 honest-sized top subset).
    q = 6
    b = 6
    true_opt = [1.5, -1.2, 0.8, -0.6, 1.1]

    x_zeno = [0.0 for _ in range(d)]
    x_med = [0.0 for _ in range(d)]
    gamma = 0.12
    rho = 0.02

    lemma1_checked = 0
    for step in range(80):
        # Honest gradients (m - q = 4 workers)
        honest_grads = []
        for _ in range(m - q):
            g_true = grad_f(x_zeno, true_opt)
            honest_grads.append([gj + rng.gauss(0.0, 0.05) for gj in g_true])

        # Byzantine gradients: 3 sign-flipping + 3 large-magnitude omniscient attacks
        byz_grads = []
        g_true = grad_f(x_zeno, true_opt)
        for idx in range(q):
            if idx % 2 == 0:
                byz_grads.append([-3.0 * gj for gj in g_true])
            else:
                byz_grads.append([15.0 for _ in range(d)])

        all_candidates = honest_grads + byz_grads
        # Fresh server validation mini-batch center a_val ~ N(true_opt, 0.03^2 I)
        a_val = [aj + rng.gauss(0.0, 0.03) for aj in true_opt]

        # Verify Lemma 1: for all i in [m - q], i-th sorted candidate score >= i-th sorted honest score
        honest_scores = sorted(
            (stochastic_descendant_score(u, x_zeno, a_val, gamma, rho) for u in honest_grads),
            reverse=True,
        )
        agg_u, all_scores_sorted = zeno_aggregate(all_candidates, x_zeno, a_val, gamma, rho, b=b)
        for i in range(m - q):
            assert all_scores_sorted[i] >= honest_scores[i] - 1e-12, (
                f"Lemma 1 violated at index {i}: {all_scores_sorted[i]} < {honest_scores[i]}"
            )
        lemma1_checked += 1

        x_zeno = [xj - gamma * uj for xj, uj in zip(x_zeno, agg_u)]

        # Coordinate-wise median fails under dishonest majority (q = 6 > m/2 = 5)
        med_u = coordinate_median(
            [grad_f(x_med, true_opt) for _ in range(m - q)]
            + [[-3.0 * gj for gj in grad_f(x_med, true_opt)] for _ in range(q)]
        )
        x_med = [xj - gamma * uj for xj, uj in zip(x_med, med_u)]

    err_zeno = l2_dist(x_zeno, true_opt)
    err_med = l2_dist(x_med, true_opt)
    assert lemma1_checked == 80
    assert err_zeno < 0.05 and err_med > 50.0, (
        f"Expected Zeno convergence under q=6/10 Byzantine majority: err_zeno={err_zeno:.4f}, err_med={err_med:.4f}"
    )

    print(
        f"[PASS] Round 523 Zeno (Xie et al. 2019): "
        f"lemma1_checks={lemma1_checked}, q={q}/{m} dishonest majority, "
        f"err_zeno={err_zeno:.4f} << err_median={err_med:.2f}"
    )


if __name__ == "__main__":
    main()
