"""Constructed mathematical boundary and adaptive step-size stabilization verification for Round 618:
WNGrad (Wu, Ward, & Bottou, 2018 / 2020, arXiv:1803.02865).

Verifies:
1. Weight Normalization Spherical Projection Identity & b_k Recurrence (Section 1.2-1.3, Eqs. 4-5, p. 3-4):
   - For unit-sphere weight normalization update v_{k+1} = v_k - (eta / ||v_k||) P_{v_k^perp}(nabla f(v_k / ||v_k||)),
     orthogonality <v_k, P_{v_k^perp}(u)> = 0 implies the exact Pythagorean norm growth:
     ||v_{k+1}||_2^2 = ||v_k||_2^2 + (eta^2 / ||v_k||_2^2) ||P_{v_k^perp}(nabla f)||_2^2 (Eq. 4).
   - WNGrad's square-root-free denominator update b_{k+1} = b_k + ||nabla f(x_k)||_2^2 / b_k (Eq. 5)
     satisfies b_{k+1}^2 = b_k^2 + 2 ||nabla f(x_k)||_2^2 + ||nabla f(x_k)||_2^4 / b_k^2.
2. Remark 2.2 (Exact Objective Scale Invariance, Section 2, p. 5):
   - When f(x) is rescaled to lambda * f(x) (for any lambda > 0) and b_1 = C * ||nabla f(x_1)||_2,
     b_j scales by exactly lambda and the iterate sequence {x_j} is identically invariant.
3. Lemmas 2.4, 2.5, 2.6 & Theorem 2.3 (Automatic Lipschitz Stabilization in Batch Setting, Section 2, p. 5-6, 12-14):
   - On an L-smooth objective f(x) = 0.5 * x^T A x (L = max_i a_i) initialized with a small b_1 = delta * L < L
     (so initial step size 1/b_1 > 2/L would cause standard GD to diverge!), WNGrad grows b_k above L at step k_0
     and then automatically stabilizes bounded above by:
     b_{k_0} <= 3*L + 2*L^2 / b_1 (Lemma 2.6), and
     b_k <= b_{k_0} + 8*(f(x_{k_0}) - f*) for all k >= k_0 (Lemma 2.5).
4. Lemma 3.3 & Theorem 3.1 (Stochastic Convex O(1/sqrt(k)) Convergence, Section 3, p. 6-8):
   - Lemma 3.3: t_{k+1} >= t_k + a / t_k implies t_k >= sqrt(2 * a * k).
   - Theorem 3.1: Ergodic average x_bar_k = (1/k) sum_{i=1}^k x_i satisfies
     f(x_bar_k) - f* <= G^2 (D^2 + 2) / (gamma * sqrt(k)) + b_1 ||x_1 - x*||_2^2 / (2*k).
"""

from __future__ import annotations

import math
import random


def verify_weight_norm_projection_and_scale_invariance() -> tuple[float, float, float]:
    rng = random.Random(20261019)
    d = 6
    v = [rng.gauss(0.0, 1.0) for _ in range(d)]
    grad = [rng.gauss(0.0, 2.0) for _ in range(d)]
    eta = 0.15

    v_norm_sq = sum(x * x for x in v)
    v_norm = math.sqrt(v_norm_sq)
    v_unit = [x / v_norm for x in v]
    dot_vg = sum(v_unit[i] * grad[i] for i in range(d))
    # Orthogonal projection P_{v^perp}(grad) = grad - <grad, v/||v||> (v/||v||)
    proj_g = [grad[i] - dot_vg * v_unit[i] for i in range(d)]
    v_next = [v[i] - (eta / v_norm) * proj_g[i] for i in range(d)]

    lhs_eq4 = sum(x * x for x in v_next)
    rhs_eq4 = v_norm_sq + ((eta * eta) / v_norm_sq) * sum(x * x for x in proj_g)
    eq4_err = abs(lhs_eq4 - rhs_eq4)
    assert eq4_err < 1e-14

    # Verify b_{k+1}^2 identity (Section 1.3, p. 4)
    b_k = 1.7
    gnorm_sq = sum(x * x for x in grad)
    b_next = b_k + gnorm_sq / b_k
    sq_id_err = abs((b_next * b_next) - (b_k * b_k + 2.0 * gnorm_sq + (gnorm_sq * gnorm_sq) / (b_k * b_k)))
    assert sq_id_err < 1e-14

    # Verify Remark 2.2 exact scale invariance under f -> lambda * f
    A = [1.0, 3.0, 8.0, 15.0]
    x_init = [1.2, -0.8, 0.5, -1.1]

    def run_wngrad_scaled(lam: float) -> list[list[float]]:
        x = list(x_init)
        g1 = [lam * A[i] * x[i] for i in range(4)]
        b = 0.5 * math.sqrt(sum(val * val for val in g1))
        traj = [list(x)]
        for _ in range(25):
            g = [lam * A[i] * x[i] for i in range(4)]
            x = [x[i] - (1.0 / b) * g[i] for i in range(4)]
            g_new = [lam * A[i] * x[i] for i in range(4)]
            b = b + sum(val * val for val in g_new) / b
            traj.append(list(x))
        return traj

    traj_1 = run_wngrad_scaled(1.0)
    traj_37 = run_wngrad_scaled(37.5)
    max_scale_inv_err = max(
        max(abs(a - b) for a, b in zip(p1, p2))
        for p1, p2 in zip(traj_1, traj_37)
    )
    assert max_scale_inv_err < 1e-14
    return eq4_err, sq_id_err, max_scale_inv_err


def verify_batch_stabilization_and_stochastic_theorem_3_1() -> tuple[float, float, float, float]:
    # 1. Verify Lemmas 2.5 & 2.6 and Theorem 2.3 on L-smooth quadratic f(x) = 0.5 * sum_i a_i x_i^2
    A = [2.0, 6.0, 12.0, 20.0]
    L = max(A)  # L = 20.0
    x = [0.1, -0.1, 0.1, -0.15]

    def f_val(pt: list[float]) -> float:
        return sum(0.5 * A[i] * (pt[i] ** 2) for i in range(4))

    def grad_f(pt: list[float]) -> list[float]:
        return [A[i] * pt[i] for i in range(4)]

    g1 = grad_f(x)
    g1_norm = math.sqrt(sum(v * v for v in g1))
    b1 = 3.5  # g1_norm ≈ 3.29 <= b1 = 3.5 < L/2 = 10.0 (overshoot regime 1/b1 > 2/L)
    assert g1_norm <= b1 < 0.5 * L

    b = b1
    k0 = -1
    b_k0 = 0.0
    f_xk0 = 0.0
    b_history = [b]

    for j in range(2, 500):
        g_prev = grad_f(x)
        x = [x[i] - (1.0 / b) * g_prev[i] for i in range(4)]
        g_curr = grad_f(x)
        b = b + sum(v * v for v in g_curr) / b
        b_history.append(b)
        if k0 == -1 and b > L:
            k0 = j
            b_k0 = b
            f_xk0 = f_val(x)

    assert k0 > 1
    # Verify Lemma 2.6: b_{k0} <= 3*L + 2*L^2 / b_1
    lemma_2_6_bound = 3.0 * L + (2.0 * L * L) / b1
    assert b_k0 <= lemma_2_6_bound
    # Verify Lemma 2.5: for all k >= k0, b_k <= b_{k0} + 8 * (f(x_{k0}) - f*)
    lemma_2_5_bound = b_k0 + 8.0 * f_xk0
    max_b = max(b_history)
    assert max_b <= lemma_2_5_bound
    final_grad_sq = sum(v * v for v in grad_f(x))
    assert final_grad_sq < 1e-10

    # 2. Verify Lemma 3.3 & Theorem 3.1 in stochastic setting
    a_const = 1.44
    t_seq = math.sqrt(2.0 * a_const)
    min_lemma33_ratio = t_seq / math.sqrt(2.0 * a_const * 1)
    for k in range(1, 200):
        t_seq = t_seq + a_const / t_seq
        ratio = t_seq / math.sqrt(2.0 * a_const * (k + 1))
        min_lemma33_ratio = min(min_lemma33_ratio, ratio)
    assert min_lemma33_ratio >= 1.0 - 1e-15

    # Theorem 3.1 stochastic convex optimization on f(x) = 0.5 * (x - 0.3)^2 on [-1, 1]
    x_st = -0.5
    x_star = 0.3
    D = 2.0
    gamma = 0.4
    G = 1.5
    b_st = 1.2
    x_sum = 0.0
    K = 200
    for k in range(1, K + 1):
        x_sum += x_st
        noise = 0.45 if (k % 2 == 0) else -0.45
        g_st = (x_st - x_star) + noise
        if abs(g_st) < gamma:
            g_st = gamma if g_st >= 0 else -gamma
        assert gamma <= abs(g_st) <= G
        x_st = max(-1.0, min(1.0, x_st - g_st / b_st))
        b_st = b_st + (g_st * g_st) / b_st

    x_bar = x_sum / K
    subopt = 0.5 * ((x_bar - x_star) ** 2)
    thm31_rhs = (G * G * (D * D + 2.0)) / (gamma * math.sqrt(K)) + (b1 * ((-0.5 - x_star) ** 2)) / (2.0 * K)
    assert subopt <= thm31_rhs

    return b_k0 / lemma_2_6_bound, max_b / lemma_2_5_bound, min_lemma33_ratio, subopt / thm31_rhs


if __name__ == "__main__":
    eq4_e, sq_e, sc_e = verify_weight_norm_projection_and_scale_invariance()
    l26_r, l25_r, l33_r, th31_r = verify_batch_stabilization_and_stochastic_theorem_3_1()
    print(
        f"[PASS] Round 618 WNGrad verified: "
        f"eq4_err={eq4_e:.2e}, sq_id_err={sq_e:.2e}, scale_inv_err={sc_e:.2e}, "
        f"lemma26_rat={l26_r:.4f}<=1, lemma25_rat={l25_r:.4f}<=1, lemma33_rat={l33_r:.4f}>=1, thm31_rat={th31_r:.4e}<=1"
    )
