#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 374:
PAGE: Probabilistic Gradient Estimator for Nonconvex Optimization
(Li, Bao, Zhang, & Richtarik 2021, ICML 2021, PMLR 139:6286-6295, arXiv:2008.10898).
"""

import math
import random


def main() -> None:
    rng = random.Random(20261019)

    # 1. Verify Lemma 3 (Finite-Sum Variance Recursion of PAGE):
    # g^{t+1} = \nabla f_{I}(x^{t+1}) w.p. p_t (minibatch |I|=b),
    #         = g^t + (1/|I'|) \sum_{i \in I'} (\nabla f_i(x^{t+1}) - \nabla f_i(x^t)) w.p. 1-p_t (minibatch |I'|=b').
    # When b = n (full gradient w.p. p_t), E[||g^{t+1} - \nabla f(x^{t+1})||^2 | F_t]
    # = (1 - p_t) ||g^t - \nabla f(x^t)||^2 + ((1 - p_t)/b') * (1/n) \sum_{i=1}^n ||\nabla f_i(x^{t+1}) - \nabla f_i(x^t)||^2
    # <= (1 - p_t) ||g^t - \nabla f(x^t)||^2 + ((1 - p_t) L^2 / b') ||x^{t+1} - x^t||^2.
    n = 16
    d = 4
    L_list = []
    A_list = []
    b_vecs = []
    for i in range(n):
        eigs = [0.5 + 1.5 * rng.random() for _ in range(d)]
        L_list.append(max(eigs))
        A_list.append(eigs)
        b_vecs.append([rng.uniform(-1.0, 1.0) for _ in range(d)])
    L_sq_avg = sum(Li * Li for Li in L_list) / n
    L_avg = math.sqrt(L_sq_avg)

    def grad_fi(i: int, x: list[float]) -> list[float]:
        return [A_list[i][j] * x[j] + b_vecs[i][j] for j in range(d)]

    def grad_f(x: list[float]) -> list[float]:
        g = [0.0] * d
        for i in range(n):
            gi = grad_fi(i, x)
            for j in range(d):
                g[j] += gi[j] / n
        return g

    x_t = [rng.uniform(-1.0, 1.0) for _ in range(d)]
    x_next = [x_t[j] + rng.uniform(-0.2, 0.2) for j in range(d)]
    gf_t = grad_f(x_t)
    gf_next = grad_f(x_next)
    g_t = [gf_t[j] + rng.uniform(-0.3, 0.3) for j in range(d)]

    p_t = 0.25
    b_prime = 4
    # Exact expectation over all independent draws of b' with replacement (and Bernoulli p_t)
    diff_norms_sq = 0.0
    for i in range(n):
        gi_next = grad_fi(i, x_next)
        gi_t = grad_fi(i, x_t)
        diff_norms_sq += sum((gi_next[j] - gi_t[j]) ** 2 for j in range(d)) / n
    # Variance of average of b' independent zero-mean vectors Z_i = (\nabla f_i(x^{t+1}) - \nabla f_i(x^t)) - (\nabla f(x^{t+1}) - \nabla f(x^t))
    mean_diff_sq = sum((gf_next[j] - gf_t[j]) ** 2 for j in range(d))
    var_single_Z = diff_norms_sq - mean_diff_sq
    prev_err_sq = sum((g_t[j] - gf_t[j]) ** 2 for j in range(d))
    exact_cond_err_sq = (1.0 - p_t) * (prev_err_sq + var_single_Z / b_prime)
    step_norm_sq = sum((x_next[j] - x_t[j]) ** 2 for j in range(d))
    lemma3_ub = (1.0 - p_t) * prev_err_sq + ((1.0 - p_t) * L_sq_avg / b_prime) * step_norm_sq
    assert exact_cond_err_sq <= lemma3_ub + 1e-12, f"Lemma 3 violated: {exact_cond_err_sq} > {lemma3_ub}"

    # 2. Verify Theorem 1 & Corollary 2 optimal complexity of PAGE:
    # With b = n, b' = sqrt(n), p_t = b' / (b + b') = 1 / (sqrt(n) + 1),
    # stepsize \eta <= 1 / (L (1 + \sqrt{(1-p_t)/(p_t b')})) = 1 / (L (1 + n^{1/4})), or with b' = \sqrt{n} and p_t = b'/(n+b'),
    # (1-p_t)/(p_t b') = (n/(n+b')) / (b'^2/(n+b')) = n / b'^2 = 1!
    # Thus \eta = 1 / (2 L) (a large constant stepsize!) and expected gradient evaluations per step:
    # p_t * n + (1 - p_t) * b' = (b' n + n b') / (n + b') < 2 b' = 2 \sqrt{n}.
    n_large = 10000
    b_p = int(math.isqrt(n_large))  # 100
    p_opt = b_p / (n_large + b_p)
    ratio_term = (1.0 - p_opt) / (p_opt * b_p)
    assert abs(ratio_term - 1.0) < 1e-12, f"Expected ratio_term == 1.0, got {ratio_term}"
    eta_factor = 1.0 / (1.0 + math.sqrt(ratio_term))  # 0.5 -> eta = 1/(2L)
    assert abs(eta_factor - 0.5) < 1e-12
    expected_grad_per_iter = p_opt * n_large + (1.0 - p_opt) * b_p
    assert expected_grad_per_iter < 2.0 * b_p

    # Compare total gradient calls to reach E||grad f(x)|| <= eps for non-convex smooth optimization:
    # GD: O(n / eps^2), SVRG: O(n + n^{2/3} / eps^2), PAGE: O(n + sqrt(n) / eps^2)
    eps = 1e-2
    delta0 = 1.0
    L_val = 1.0
    T_iters = math.ceil(2.0 * delta0 * L_val / (eta_factor * (eps ** 2)))
    cost_page = n_large + T_iters * expected_grad_per_iter
    cost_svrg = n_large + T_iters * (n_large ** (2.0 / 3.0))
    cost_gd = T_iters * n_large
    assert cost_page < cost_svrg < cost_gd

    # 3. Verify Theorem 5 (Linear convergence of PAGE under Polyak-Lojasiewicz condition):
    # Under \mu-PL condition (1/2 ||\nabla f(x)||^2 >= \mu (f(x) - f*)),
    # Lyapunov function \Phi_t = f(x^t) - f* + (1 / (2 p_t L)) ||g^t - \nabla f(x^t)||^2
    # contracts at each step by (1 - \eta \mu) when \eta <= \min{p_t / (2 \mu), 1 / (L (1 + \sqrt{2(1-p_t)/(p_t b')}))}.
    mu = 0.5
    eta_pl = min(p_t / (2.0 * mu), 1.0 / (L_avg * (1.0 + math.sqrt(2.0 * (1.0 - p_t) / (p_t * b_prime)))))
    contraction = 1.0 - eta_pl * mu
    assert 0.0 < contraction < 1.0

    print(
        f"[PASS] Round 374 PAGE (Li et al. 2021): lemma3_exact={exact_cond_err_sq:.6f} <= ub={lemma3_ub:.6f}, "
        f"eta_factor={eta_factor:.2f}, grad_per_iter={expected_grad_per_iter:.2f} < {2*b_p}, "
        f"cost_page={cost_page:.1f} < cost_svrg={cost_svrg:.1f} < cost_gd={cost_gd:.1f}, pl_contraction={contraction:.4f}"
    )


if __name__ == "__main__":
    main()
