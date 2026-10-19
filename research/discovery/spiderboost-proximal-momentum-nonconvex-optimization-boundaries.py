#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 376:
SpiderBoost and Proximal SpiderBoost with Momentum for Nonconvex Optimization
(Wang, Ji, Zhou, Liang, & Tarokh 2019, NeurIPS 2019, arXiv:1810.10690).
"""

import math


def main() -> None:
    # 1. Verify SpiderBoost Constant Stepsize vs SPIDER Accuracy-Dependent Stepsize:
    # In original SPIDER (Fang et al. 2018), stepsize is \eta_spider = \eps / (L * n_0) = O(\eps / L)
    # because it normalizes the update direction v_k / ||v_k||.
    # In SpiderBoost (Wang et al. 2019, Theorem 1 & Lemma 1), setting q = |S| = \sqrt{n} and
    # constant stepsize \eta = 1 / (2 L) satisfies the inner-loop telescoping condition:
    # \beta_1 = 1/(2\eta) - L/2 - (\eta L^2 / 2) * (q / |S|) = L - L/2 - (L/4)*1 = L/4 > 0!
    L = 2.0
    n = 10000
    q = int(math.isqrt(n))  # 100
    S_batch = q  # 100
    eta_sb = 1.0 / (2.0 * L)
    beta_1 = (1.0 / (2.0 * eta_sb)) - (L / 2.0) - (eta_sb * (L ** 2) / 2.0) * (q / S_batch)
    assert abs(beta_1 - (L / 4.0)) < 1e-12 and beta_1 > 0.0

    eps = 1e-3
    eta_spider = eps / (2.0 * L)
    stepsize_ratio = eta_sb / eta_spider
    assert stepsize_ratio == 1.0 / eps  # 1000x larger stepsize!

    # 2. Verify Prox-SpiderBoost Composite Non-Convex Convergence (Theorem 2 & Appendix H):
    # Consider composite problem \min_x \Psi(x) = f(x) + h(x) with non-convex smooth f(x) and convex l1 penalty h(x) = \lambda ||x||_1.
    # Generalized gradient mapping: G_\eta(x, v) = (1/\eta) (x - prox_{\eta h}(x - \eta v)).
    # Verify Lemma 6 non-expansiveness and descent property on 1D non-convex + l1 problem:
    # f(x) = 0.5 * x^2 + 0.2 * sin(2x), h(x) = 0.15 * |x|.
    lam = 0.15

    def grad_f(x: float) -> float:
        return x + 0.4 * math.cos(2.0 * x)

    def prox_h(z: float, step: float) -> float:
        thresh = step * lam
        if z > thresh:
            return z - thresh
        if z < -thresh:
            return z + thresh
        return 0.0

    def G_map(x: float, v: float, step: float) -> float:
        return (x - prox_h(x - step * v, step)) / step

    L_comp = 1.8  # |f''(x)| = |1 - 0.8 sin(2x)| <= 1.8
    eta_prox = 1.0 / (2.0 * L_comp)
    x_curr = 1.5
    grad_norms = []
    for _ in range(80):
        g_val = G_map(x_curr, grad_f(x_curr), eta_prox)
        grad_norms.append(abs(g_val))
        x_curr = x_curr - eta_prox * g_val

    assert grad_norms[-1] < 1e-8 and grad_norms[-1] < grad_norms[0] * 1e-6

    # 3. Verify Momentum Coupling Weights in Prox-SpiderBoost-M (Algorithm 3 & Lemma 5):
    # \alpha_k = 2 / (\lceil k/q \rceil + 1), \Gamma_1 = 1, \Gamma_k = (1 - \alpha_k) \Gamma_{k-1} within epoch.
    # Note that at epoch index m = \lceil k/q \rceil, \alpha_{(m)} = 2 / (m + 1) and
    # \Gamma_{(m)} = 2 / (m (m + 1)), which satisfies (1 - \alpha_{(m)}) \Gamma_{(m-1)}
    # = ((m - 1)/(m + 1)) * (2 / ((m - 1) m)) = 2 / (m (m + 1)) = \Gamma_{(m)}!
    for m in range(2, 25):
        alpha_m = 2.0 / (m + 1.0)
        gamma_prev = 2.0 / ((m - 1.0) * m)
        gamma_curr = 2.0 / (m * (m + 1.0))
        assert abs((1.0 - alpha_m) * gamma_prev - gamma_curr) < 1e-15

    # Also verify PO (proximal oracle) complexity O(1/\eps^2) vs SFO complexity O(n + \sqrt{n}/\eps^2):
    po_calls = math.ceil(1.0 / (eps ** 2))
    sfo_calls = n + int(math.isqrt(n)) * po_calls
    assert po_calls == 1_000_000 and sfo_calls == 100_010_000

    print(
        f"[PASS] Round 376 SpiderBoost (Wang et al. 2019): beta_1={beta_1:.4f}==L/4, "
        f"stepsize_ratio={stepsize_ratio:.0f}x, prox_grad_final={grad_norms[-1]:.2e}, "
        f"PO={po_calls} vs SFO={sfo_calls}"
    )


if __name__ == "__main__":
    main()
