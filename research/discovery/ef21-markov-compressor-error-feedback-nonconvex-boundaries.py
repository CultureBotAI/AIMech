#!/usr/bin/env python3
"""Constructed boundary & mathematical verification for Round 380:
AIMech:Ef21MarkovCompressorErrorFeedbackForHeterogeneousNonconvexOptimization
(Richtarik, Sokolov, & Fatkhullin 2021, NeurIPS 2021, pp. 4384-4396, arXiv:2106.05203).

Verifies:
1. Algorithm 1 Invariant (Equation 6):
   Maintaining g^{t+1} = g^t + (1/n) sum_{i=1}^n c_i^t where c_i^t = C_i(grad f_i(x^{t+1}) - g_i^t)
   and g_i^{t+1} = g_i^t + c_i^t guarantees that the server state equals the exact mean of worker
   gradient estimators g^t == (1/n) sum_{i=1}^n g_i^t for all t >= 0.
2. Lemma 2 & Lemma 3 Optimal Contraction Factor:
   For any biased compressor C in B(alpha) with 0 < alpha <= 1, optimizing Young's inequality parameter
   s > 0 in (1 - alpha)*(1 + s) = 1 - theta(s) and beta(s) = (1 - alpha)*(1 + 1/s) yields the unique
   minimizer s* = 1/sqrt(1 - alpha) - 1, giving theta* = 1 - sqrt(1 - alpha),
   beta* = (1 - alpha)/(1 - sqrt(1 - alpha)), and sqrt(beta*/theta*) = sqrt(1 - alpha)/(1 - sqrt(1 - alpha)) <= 2/alpha - 1,
   Improving the O(1/alpha^2) stepsize bottleneck to O(alpha).
3. Heterogeneous Nonconvex Stationarity Without Bounded Gradient Dissimilarity (Theorem 1):
   On a multi-worker problem with arbitrarily large client gradient dissimilarity at the optimum
   (||grad f_i(x*)|| >> 0 while (1/n) sum_i grad f_i(x*) = 0), EF21 with deterministic Top-k
   converges linearly to exact stationarity ||grad f(x^t)|| -> 0 and ||g_i^t - grad f_i(x^t)|| -> 0,
   whereas distributed compressed GD without Markov difference compression stalls at a nonzero bias floor.
"""

from __future__ import annotations
import math
import random


def top_k(x: list[float], k: int) -> list[float]:
    d = len(x)
    idx_sorted = sorted(range(d), key=lambda i: abs(x[i]), reverse=True)
    keep = set(idx_sorted[:k])
    return [x[i] if i in keep else 0.0 for i in range(d)]


def norm_sq(v: list[float]) -> float:
    return sum(vi * vi for vi in v)


def test_lemma3_optimal_contraction_constants() -> None:
    """Verify Lemma 2 and Lemma 3 optimal s* = 1/sqrt(1 - alpha) - 1 and ratio bound <= 2/alpha - 1."""
    for alpha in (0.05, 0.1, 0.25, 0.5, 0.8, 0.99):
        s_star = 1.0 / math.sqrt(1.0 - alpha) - 1.0
        theta_star = 1.0 - (1.0 - alpha) * (1.0 + s_star)
        beta_star = (1.0 - alpha) * (1.0 + 1.0 / s_star)
        assert abs(theta_star - (1.0 - math.sqrt(1.0 - alpha))) < 1e-12
        assert abs(beta_star - (1.0 - alpha) / (1.0 - math.sqrt(1.0 - alpha))) < 1e-12

        ratio_star = math.sqrt(beta_star / theta_star)
        exact_expr = math.sqrt(1.0 - alpha) / (1.0 - math.sqrt(1.0 - alpha))
        assert abs(ratio_star - exact_expr) < 1e-12
        assert ratio_star <= (2.0 / alpha - 1.0) + 1e-12

        # Check optimality against perturbed s values in (0, alpha / (1 - alpha))
        s_max = alpha / (1.0 - alpha)
        for frac in (0.1, 0.3, 0.7, 0.9):
            s_alt = frac * s_max
            theta_alt = 1.0 - (1.0 - alpha) * (1.0 + s_alt)
            beta_alt = (1.0 - alpha) * (1.0 + 1.0 / s_alt)
            assert math.sqrt(beta_alt / theta_alt) >= ratio_star - 1e-12


def test_ef21_invariant_and_heterogeneous_convergence() -> None:
    """Verify EF21 Algorithm 1 on a strongly heterogeneous multi-worker problem where
    individual client gradients at x* = 0 have huge norm ||grad f_i(0)|| ~ 50,
    so direct gradient compression C(grad f_i(x)) fails to converge to x* = 0.
    """
    rng = random.Random(38001)
    n = 4
    d = 8
    k = 2
    alpha = k / d
    # Construct worker quadratics f_i(x) = 0.5 * sum_j L_{i,j} x_j^2 + b_i^T x
    # such that sum_{i=1}^n b_i = 0 (so x* = 0 is the exact global minimizer),
    # but each b_i has large non-sparse entries.
    L_mat = [[1.0 + 0.3 * ((i + j) % 5) for j in range(d)] for i in range(n)]
    b_vecs = [[rng.uniform(-20.0, 20.0) for _ in range(d)] for _ in range(n - 1)]
    b_last = [-sum(b_vecs[i][j] for i in range(n - 1)) for j in range(d)]
    b_vecs.append(b_last)

    def grad_fi(i: int, x: list[float]) -> list[float]:
        return [L_mat[i][j] * x[j] + b_vecs[i][j] for j in range(d)]

    def grad_f(x: list[float]) -> list[float]:
        return [sum(grad_fi(i, x)[j] for i in range(n)) / n for j in range(d)]

    L_tilde = math.sqrt(sum((max(L_mat[i]) ** 2) for i in range(n)) / n)
    theta = 1.0 - math.sqrt(1.0 - alpha)
    beta = (1.0 - alpha) / (1.0 - math.sqrt(1.0 - alpha))
    gamma = 1.0 / (L_tilde * (1.0 + math.sqrt(beta / theta)))

    x_ef21 = [2.0] * d
    g_workers = [top_k(grad_fi(i, x_ef21), k) for i in range(n)]
    g_server = [sum(g_workers[i][j] for i in range(n)) / n for j in range(d)]

    x_direct = [2.0] * d

    for t in range(350):
        # Verify Eq. (6) invariant: g_server == mean of g_workers
        mean_gw = [sum(g_workers[i][j] for i in range(n)) / n for j in range(d)]
        for j in range(d):
            assert abs(g_server[j] - mean_gw[j]) < 1e-11

        # EF21 step
        x_next = [x_ef21[j] - gamma * g_server[j] for j in range(d)]
        c_list = []
        for i in range(n):
            diff = [grad_fi(i, x_next)[j] - g_workers[i][j] for j in range(d)]
            ci = top_k(diff, k)
            c_list.append(ci)
            g_workers[i] = [g_workers[i][j] + ci[j] for j in range(d)]
        g_server = [g_server[j] + sum(c_list[i][j] for i in range(n)) / n for j in range(d)]
        x_ef21 = x_next

        # Naive direct compression step x^{t+1} = x^t - gamma * (1/n) sum_i top_k(grad f_i(x^t))
        c_direct = [top_k(grad_fi(i, x_direct), k) for i in range(n)]
        avg_direct = [sum(c_direct[i][j] for i in range(n)) / n for j in range(d)]
        x_direct = [x_direct[j] - gamma * avg_direct[j] for j in range(d)]

    # EF21 converges to zero gradient and zero distortion G^t = (1/n) sum_i ||g_i^t - grad f_i(x^t)||^2:
    final_grad_norm_ef21 = math.sqrt(norm_sq(grad_f(x_ef21)))
    final_distortion_ef21 = sum(
        norm_sq([g_workers[i][j] - grad_fi(i, x_ef21)[j] for j in range(d)]) for i in range(n)
    ) / n
    final_grad_norm_direct = math.sqrt(norm_sq(grad_f(x_direct)))

    assert final_grad_norm_ef21 < 1e-5, f"Expected EF21 grad norm < 1e-5, got {final_grad_norm_ef21}"
    assert final_distortion_ef21 < 1e-9, f"Expected EF21 distortion < 1e-9, got {final_distortion_ef21}"
    assert final_grad_norm_direct > 1.0, (
        f"Expected direct top_k GD to stall at large heterogeneous bias floor, got {final_grad_norm_direct}"
    )


if __name__ == "__main__":
    test_lemma3_optimal_contraction_constants()
    test_ef21_invariant_and_heterogeneous_convergence()
    print("[PASS] Round 380 EF21 Markov Compressor Error Feedback boundaries verified.")
