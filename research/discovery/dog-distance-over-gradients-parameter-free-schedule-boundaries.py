#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 591:
DoG (Distance over Gradients: A Parameter-Free Dynamic Step Size Schedule) — Ivgi, Hinder, Carmon (ICML 2023; arXiv:2302.12022).
"""

import math
from typing import List, Tuple


def log_plus(x: float) -> float:
    return 1.0 + math.log(max(x, 1.0))


def verify_lemma3_algebraic_bound() -> Tuple[float, float]:
    """Lemma 3 (p. 7): max_{t <= T} sum_{i < t} s_i / s_t >= (1/e) * (T / log_+(s_T / s_0) - 1)."""
    T = 100
    s = [1e-4 * (1.12 ** t) for t in range(T + 1)]
    lhs = max(sum(s[i] / s[t] for i in range(t)) for t in range(1, T + 1))
    rhs = (1.0 / math.e) * (T / log_plus(s[T] / s[0]) - 1.0)
    assert lhs >= rhs - 1e-12, f"Lemma 3 violated: {lhs} < {rhs}"
    return lhs, rhs


def verify_nemirovski_divergence_vs_tdog_stability() -> Tuple[float, float]:
    """Appendix C.3 (pp. 30-31) vs Proposition 2 (p. 8):
    On Nemirovski's pathological function, untamed DoG has r_bar_T / d_0 = sqrt(T) / 10,
    whereas T-DoG guarantees r_bar_T <= 3 d_0.
    """
    m = 400
    r_eps = 0.01
    d0 = 10.0 * r_eps
    x0 = [10.0 * r_eps / math.sqrt(m)] * m

    def subgrad(x: List[float]) -> List[float]:
        best_val = -1e30
        best_idx = 0
        best_pos = True
        inv_sqrt_m = 1.0 / math.sqrt(m)
        for i in range(m):
            v_pos = x[i]
            v_neg = -inv_sqrt_m * x[i]
            cand = max(v_pos, v_neg)
            if cand > best_val + 1e-15:
                best_val = cand
                best_idx = i
                best_pos = v_pos >= v_neg
        g = [0.0] * m
        g[best_idx] = 1.0 if best_pos else -inv_sqrt_m
        return g

    # 1. Untamed DoG for T = m steps (Appendix C.3 Eq. 7 uses G_n = n for n >= 1)
    x_dog = x0[:]
    r_bar_dog = r_eps
    G_dog = 0.0
    for t in range(m):
        r_t = math.sqrt(sum((x_dog[j] - x0[j]) ** 2 for j in range(m)))
        r_bar_dog = max(r_bar_dog, r_t)
        expected_r_bar = math.sqrt(max(t, 1)) * r_eps
        assert abs(r_bar_dog - expected_r_bar) < 1e-12
        g = subgrad(x_dog)
        denom_sq = max(G_dog, 1.0)
        eta_t = r_bar_dog / math.sqrt(denom_sq)
        for j in range(m):
            x_dog[j] -= eta_t * g[j]
        G_dog += sum(gj * gj for gj in g)
    r_T = math.sqrt(sum((x_dog[j] - x0[j]) ** 2 for j in range(m)))
    r_bar_dog = max(r_bar_dog, r_T)
    ratio_dog = r_bar_dog / d0
    assert abs(ratio_dog - math.sqrt(m) / 10.0) < 1e-12, f"Expected ratio 2.0, got {ratio_dog}"

    # 2. T-DoG (Section 3.3,noiseless theta=1) on the same instance
    x_tdog = x0[:]
    r_bar_tdog = r_eps
    G_prev = 0.0
    l_bar = 1.0
    l0 = 1.0
    for t in range(m):
        r_t = math.sqrt(sum((x_tdog[j] - x0[j]) ** 2 for j in range(m)))
        r_bar_tdog = max(r_bar_tdog, r_t)
        g = subgrad(x_tdog)
        G_prime_t = (8.0 ** 4) * (log_plus(1.0 + t * (l_bar ** 2) / (l0 ** 2)) ** 2) * (G_prev + 16.0 * (l_bar ** 2))
        eta_t = r_bar_tdog / math.sqrt(G_prime_t)
        for j in range(m):
            x_tdog[j] -= eta_t * g[j]
        G_prev += sum(gj * gj for gj in g)
    r_T_tdog = math.sqrt(sum((x_tdog[j] - x0[j]) ** 2 for j in range(m)))
    r_bar_tdog = max(r_bar_tdog, r_T_tdog)
    ratio_tdog = r_bar_tdog / d0
    assert r_bar_tdog <= 3.0 * d0, f"Proposition 2 violated: r_bar_tdog={r_bar_tdog} > 3*d0={3.0 * d0}"
    return ratio_dog, ratio_tdog


def verify_lemma1_weighted_regret_bound() -> Tuple[float, float]:
    """Lemma 1 (p. 6): sum_{k=0}^{t-1} r_bar_k <g_k, x_k - x_*> <= r_bar_t (2 d_bar_t + r_bar_t) sqrt(G'_{t-1})."""
    x_star = [2.5, -1.5]
    x = [0.0, 0.0]
    x0 = [0.0, 0.0]
    r_eps = 1e-4
    r_bar = r_eps
    d_bar = math.hypot(x[0] - x_star[0], x[1] - x_star[1])
    G = 0.0
    weighted_regret = 0.0
    T = 60
    for k in range(T):
        dx0, dx1 = x[0] - x_star[0], x[1] - x_star[1]
        g = [2.0 * dx0, 4.0 * dx1]
        r_k = math.hypot(x[0] - x0[0], x[1] - x0[1])
        r_bar = max(r_bar, r_k)
        d_k = math.hypot(dx0, dx1)
        d_bar = max(d_bar, d_k)
        G += g[0] ** 2 + g[1] ** 2
        eta_k = r_bar / math.sqrt(G)
        weighted_regret += r_bar * (g[0] * dx0 + g[1] * dx1)
        x = [x[0] - eta_k * g[0], x[1] - eta_k * g[1]]

    r_T = math.hypot(x[0] - x0[0], x[1] - x0[1])
    r_bar_T = max(r_bar, r_T)
    d_T = math.hypot(x[0] - x_star[0], x[1] - x_star[1])
    d_bar_T = max(d_bar, d_T)
    rhs = r_bar_T * (2.0 * d_bar_T + r_bar_T) * math.sqrt(G)
    assert weighted_regret <= rhs + 1e-9, f"Lemma 1 violated: {weighted_regret} > {rhs}"
    return weighted_regret, rhs


def main() -> None:
    l3_lhs, l3_rhs = verify_lemma3_algebraic_bound()
    ratio_dog, ratio_tdog = verify_nemirovski_divergence_vs_tdog_stability()
    reg_lhs, reg_rhs = verify_lemma1_weighted_regret_bound()
    print(
        f"[PASS] Round 591 DoG verified: lemma3=({l3_lhs:.2f}>={l3_rhs:.2f}), "
        f"nemirovski_ratio_dog={ratio_dog:.2f} vs tdog={ratio_tdog:.4f}<=3.0, "
        f"lemma1_regret=({reg_lhs:.4f}<={reg_rhs:.4f})"
    )


if __name__ == "__main__":
    main()
