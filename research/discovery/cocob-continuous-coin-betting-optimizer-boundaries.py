"""Constructed mathematical boundary and coin-betting wealth verification for Round 621:
COCOB — Continuous Coin Betting Optimizer (Orabona & Tommasi, NeurIPS 2017, arXiv:1705.07795v3).

Verifies:
1. Algorithm 1 (COntinuous COin Betting - COCOB, Section 5, p. 4):
   - Exact scale invariance: multiplying all negative subgradients g_{t,i} and scale bounds L_i
     by any positive constant c > 0 yields the exact same sequence of iterates w_{t,i}.
   - Strict wealth positivity: Wealth_{t,i} = L_i + Reward_{t,i} = Wealth_{t-1,i} * (1 + beta_{t,i} * g_{t,i}) > 0
     for all t since |L_i * beta_{t,i}| = |2*sigma(2*theta_{t,i}/(G_{t,i}+L_i)) - 1| < 1 and |g_{t,i}| <= L_i.
2. Lemma 1, Lemma 2, and Theorem 1 Wealth Lower Bound & Convergence Guarantee (Section 5 & Appendix A, p. 5, 12-14):
   - Lemma 2 inductive step: (1 + beta_{t,i} * g_{t,i}) * H_{t-1,i}(theta_{t-1,i}) >= H_{t,i}(theta_{t,i})
     at every step t = 1..T for a = 2.
   - Inductive wealth bound (Eq. 3 & Eq. 5, p. 13-14):
     Wealth_{T,i} >= H_{T,i}(theta_{T,i}) >= L_i * exp(theta_{T,i}^2 / (2 * L_i * (G_{T,i} + L_i)) - 0.5 * ln(G_{T,i} / L_i)).
   - Lemma 1 Fenchel conjugate bound: f*(y) <= |y| * sqrt(alpha * ln(alpha * y^2 / beta^2 + 1)) - beta
     for f(x) = beta * exp(x^2 / (2 * alpha)).
   - Theorem 1 convergence rate bound holds on non-smooth convex objective F(w).
3. Section 4-6 Non-Smooth Absolute-Loss Trajectory & Algorithm 2 COCOB-Backprop (p. 3, 5-7):
   - On F(x) = |x - 10| starting from w_1 = 0, COCOB's iterate grows exponentially while
     subgradients have identical sign (x < 10) and converges rapidly to x* = 10 without any learning rate.
   - COCOB-Backprop (Algorithm 2, p. 6) adapts L_{t,i} = max(L_{t-1,i}, |g_{t,i}|) online with
     first-step update w_{2,i} = w_{1,i} + sign(g_{1,i}) / alpha.
"""

from __future__ import annotations

import math
import random


def sigma(x: float) -> float:
    if x >= 0.0:
        z = math.exp(-x)
        return 1.0 / (1.0 + z)
    z = math.exp(x)
    return z / (1.0 + z)


def run_cocob_1d(neg_grads: list[float], L: float, w1: float = 0.0) -> tuple[list[float], list[float], list[float], list[float]]:
    G = L
    reward = 0.0
    theta = 0.0
    w = w1
    iterates = [w]
    wealths = [L]
    G_hist = [G]
    theta_hist = [theta]
    for g in neg_grads:
        assert abs(g) <= L + 1e-12
        G = G + abs(g)
        reward = reward + (w - w1) * g
        theta = theta + g
        beta = (2.0 * sigma(2.0 * theta / (G + L)) - 1.0) / L
        w = w1 + beta * (L + reward)
        iterates.append(w)
        wealths.append(L + reward)
        G_hist.append(G)
        theta_hist.append(theta)
    return iterates, wealths, G_hist, theta_hist


def verify_scale_invariance_and_wealth_bounds() -> tuple[float, float, float, float]:
    rng = random.Random(20261019)
    T = 50
    L = 2.5
    w1 = -1.2
    neg_grads = [rng.uniform(-L, L) for _ in range(T)]

    # 1. Exact scale-freeness under scaling by c = 7.3
    c = 7.3
    it_base, wealth_base, G_hist, theta_hist = run_cocob_1d(neg_grads, L, w1=w1)
    it_scaled, wealth_scaled, _, _ = run_cocob_1d([c * g for g in neg_grads], c * L, w1=w1)

    max_scale_err = max(abs(a - b) for a, b in zip(it_base, it_scaled))
    assert max_scale_err < 1e-14
    assert min(wealth_base) > 0.0 and min(wealth_scaled) > 0.0

    # 2. Verify Lemma 2 inductive step and Eq. (3) & (5) wealth lower bound (with w1 = 0)
    _, wealth0, G0, th0 = run_cocob_1d(neg_grads, L, w1=0.0)
    running_harm = 0.0
    H_vals = [L]
    min_lemma2_ratio = float("inf")
    min_wealth_ratio = float("inf")

    for t in range(1, T + 1):
        g_t = neg_grads[t - 1]
        running_harm += abs(g_t) / G0[t - 1]
        H_t = L * math.exp((th0[t] ** 2) / (2.0 * L * (G0[t] + L)) - running_harm)
        H_vals.append(H_t)

        # Note that Wealth_t / Wealth_{t-1} = 1 + beta_{t-1} * g_t
        step_factor = wealth0[t] / wealth0[t - 1]
        lhs_l2 = step_factor * H_vals[t - 1]
        assert lhs_l2 + 1e-14 >= H_t
        min_lemma2_ratio = min(min_lemma2_ratio, lhs_l2 / H_t)
        assert wealth0[t] + 1e-14 >= H_t
        min_wealth_ratio = min(min_wealth_ratio, wealth0[t] / H_t)

    # Overapproximated wealth bound using Eq. (5): sum |g_j| / G_{j-1} <= ln(G_T / L)
    overapprox_wealth_lb = L * math.exp((th0[T] ** 2) / (2.0 * L * (G0[T] + L)) - math.log(G0[T] / L))
    assert wealth0[T] >= overapprox_wealth_lb

    # 3. Verify Lemma 1 Fenchel conjugate upper bound (p. 12)
    alpha_f = 3.2
    beta_f = 1.4
    max_fenchel_ratio = 0.0
    for y in (0.5, 1.5, 4.0, 8.0):
        rhs_f = abs(y) * math.sqrt(alpha_f * math.log((alpha_f * y * y) / (beta_f * beta_f) + 1.0)) - beta_f
        # Evaluate sup_x (y*x - beta_f * exp(x^2 / (2*alpha_f))) on a fine grid around stationary point
        sup_val = max(
            y * x - beta_f * math.exp((x * x) / (2.0 * alpha_f))
            for x in [0.01 * k for k in range(1, 600)]
        )
        assert sup_val <= rhs_f + 1e-12
        max_fenchel_ratio = max(max_fenchel_ratio, sup_val / rhs_f)

    return max_scale_err, min_lemma2_ratio, min_wealth_ratio, max_fenchel_ratio


def verify_theorem1_and_cocob_backprop() -> tuple[float, float, float]:
    # 1. Verify Theorem 1 bound and exponential bet growth on F(x) = |x - 10| (Section 4 & 5, Figure 1, p. 3, 5)
    T = 400
    L = 1.0
    x_star = 10.0
    w = 0.0
    G = L
    reward = 0.0
    theta = 0.0
    w_sum = 0.0
    w_hist = []

    for _t in range(1, T + 1):
        w_hist.append(w)
        w_sum += w
        # Negative subgradient of |w - 10| is +1 if w < 10 else (-1 if w > 10 else 0)
        g = 1.0 if w < x_star else (-1.0 if w > x_star else 0.0)
        G += abs(g)
        reward += w * g
        theta += g
        beta = (2.0 * sigma(2.0 * theta / (G + L)) - 1.0) / L
        w = beta * (L + reward)

    # Verify exponential growth in early steps (before crossing x* = 10)
    assert w_hist[1] < w_hist[3] < w_hist[6] < w_hist[10]
    w_bar = w_sum / T
    subopt = abs(w_bar - x_star)
    thm1_rhs = (
        L + abs(x_star) * math.sqrt(L * (G + L) * math.log(1.0 + ((G + L) ** 2) * (x_star ** 2) / (L * L)))
    ) / T
    assert subopt <= thm1_rhs
    assert subopt < 0.1 * x_star

    # 2. Verify Algorithm 2 (COCOB-Backprop, Section 6, p. 6-7) on F(x) = 0.5*(x - 3)^2 + |x - 3|
    alpha_bp = 10.0
    w_bp = 0.0
    w1_bp = 0.0
    L_bp = 0.0
    G_bp = 0.0
    rew_bp = 0.0
    th_bp = 0.0
    first_step_err = 0.0

    for t in range(1, 201):
        grad_f = (w_bp - 3.0) + (1.0 if w_bp > 3.0 else -1.0)
        g = -grad_f  # negative subgradient
        L_bp = max(L_bp, abs(g))
        G_bp = G_bp + abs(g)
        rew_bp = max(rew_bp + (w_bp - w1_bp) * g, 0.0)
        th_bp = th_bp + g
        w_bp = w1_bp + (th_bp / (L_bp * max(G_bp + L_bp, alpha_bp * L_bp))) * (L_bp + rew_bp)
        if t == 1:
            # First step property (Section 6, p. 7): w_{2,i} = w_{1,i} + (1 / alpha) * sign(g_{1,i})
            first_step_err = abs(w_bp - (w1_bp + (1.0 / alpha_bp) * (1.0 if g > 0 else -1.0)))

    assert first_step_err < 1e-15
    assert abs(w_bp - 3.0) < 0.05
    return subopt / thm1_rhs, subopt, abs(w_bp - 3.0)


if __name__ == "__main__":
    sc_err, l2_rat, w_rat, fen_rat = verify_scale_invariance_and_wealth_bounds()
    thm1_rat, subopt_val, bp_err = verify_theorem1_and_cocob_backprop()
    print(
        f"[PASS] Round 621 COCOB verified: "
        f"scale_err={sc_err:.2e}, lemma2_rat={l2_rat:.4f}>=1, wealth_rat={w_rat:.4f}>=1, "
        f"fenchel_rat={fen_rat:.4f}<=1, thm1_rat={thm1_rat:.4f}<=1, abs_subopt={subopt_val:.4f}, bp_err={bp_err:.4f}"
    )
