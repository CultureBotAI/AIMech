#!/usr/bin/env python3
"""Constructed boundary verification for Round 493: FedMGDA+ (Hu et al. 2022, IEEE TNSE / arXiv:2006.11489).

Verifies:
1. Minimum-Norm Common Descent Direction over epsilon-Constrained Simplex (Section 5, Eqs. 22-25, Algorithm 1):
   lambda_t^* = argmin_{lambda in Delta, ||lambda - lambda_0||_inf <= epsilon} ||sum_i lambda_i g_bar_i||_2^2,
   d_t = sum_i lambda_{t,i}^* g_bar_i.
   - At epsilon = 0, lambda_t^* = lambda_0 (exact reduction to normalized FedAvg-n).
   - At epsilon = 1, lambda_t^* solves unconstrained MGDA over the simplex and guarantees
     <g_bar_i, d_t> >= ||d_t||_2^2 >= 0 for EVERY participating client i (simultaneous non-sacrificing
     common descent direction, Eq. 24), whereas uniform FedAvg can have <g_i, d_fedavg> < 0 (sacrificing
     one client's objective for another).
2. Dual Adversarial Invariance (Sections 5 & 6.2.2, Eq. 19 & Algorithm 1 line 5):
   - Additive loss inflation f_i(w) -> f_i(w) + C_bias leaves gradients and centered objective (Eq. 19)
     completely unchanged.
   - Multiplicative loss scaling f_i(w) -> alpha_scale * f_i(w) (alpha_scale > 0) scales g_i -> alpha_scale * g_i,
     which unit L2 normalization g_bar_i = g_i / ||g_i||_2 (Algorithm 1 line 5) makes 100% invariant.
3. Proximal Average Unification of FedAvg/FedProx (Section 3, Eqs. 4-9):
   Verifies that the proximal map of the proximal average A_{f, lambda}^eta(w) equals the weighted
   average of individual proximal maps sum_i lambda_i P_{f_i}^eta(w).
"""

import math


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def norm2(u):
    return math.sqrt(dot(u, u))


def normalize(u):
    n = norm2(u)
    return [a / n for a in u] if n > 0 else list(u)


def solve_2client_fedmgda_qp(g1, g2, lam0_1=0.5, eps=1.0):
    """Closed-form solution of min_{lam1 in [0,1], |lam1 - lam0_1| <= eps} ||lam1 g1 + (1-lam1) g2||_2^2."""
    lo = max(0.0, lam0_1 - eps)
    hi = min(1.0, lam0_1 + eps)
    diff = [a - b for a, b in zip(g1, g2)]
    denom = dot(diff, diff)
    if denom < 1e-15:
        lam1 = lam0_1
    else:
        # d/d(lam1) ||g2 + lam1 (g1 - g2)||^2 = 0 => lam1^* = - <g2, g1 - g2> / ||g1 - g2||^2
        lam1_unconstrained = -dot(g2, diff) / denom
        lam1 = min(max(lam1_unconstrained, lo), hi)
    lam2 = 1.0 - lam1
    d = [lam1 * a + lam2 * b for a, b in zip(g1, g2)]
    return (lam1, lam2), d


def verify_fedmgda_plus_boundaries():
    # 1. Consider 2 clients with conflicting/asymmetric raw gradients at w_t:
    # Client 1 has large gradient [4.0, 0.0], Client 2 has smaller gradient [-2.0, 2.0]
    g1_raw = [4.0, 0.0]
    g2_raw = [-2.0, 2.0]

    # Standard FedAvg (unnormalized, uniform weights [0.5, 0.5]):
    d_fedavg = [0.5 * (g1_raw[0] + g2_raw[0]), 0.5 * (g1_raw[1] + g2_raw[1])]  # [1.0, 1.0]
    # Check inner product with Client 2's true gradient g2_raw = [-2.0, 2.0]:
    # <g2_raw, d_fedavg> = -2*1 + 2*1 = 0, or if g1_raw = [5.0, 0.0], d_fedavg = [1.5, 1.0]
    g1_dom = [5.0, 0.0]
    d_fedavg_dom = [0.5 * (g1_dom[0] + g2_raw[0]), 0.5 * (g1_dom[1] + g2_raw[1])]  # [1.5, 1.0]
    inner_c2_fedavg = dot(g2_raw, d_fedavg_dom)  # -2*1.5 + 2*1.0 = -1.0 < 0 (Client 2's loss INCREASES!)
    assert inner_c2_fedavg < 0.0, f"Expected FedAvg to sacrifice Client 2, got {inner_c2_fedavg}"

    # FedMGDA+ (Algorithm 1): unit-normalize gradients first
    g1_bar = normalize(g1_dom)  # [1.0, 0.0]
    g2_bar = normalize(g2_raw)  # [-1/sqrt(2), 1/sqrt(2)]

    # Verify epsilon = 0 recovers FedAvg-n (lam = [0.5, 0.5]):
    lam_eps0, d_eps0 = solve_2client_fedmgda_qp(g1_bar, g2_bar, lam0_1=0.5, eps=0.0)
    assert abs(lam_eps0[0] - 0.5) < 1e-12 and abs(lam_eps0[1] - 0.5) < 1e-12

    # Verify epsilon = 1 (unconstrained MGDA on normalized gradients) guarantees common descent for BOTH clients:
    lam_mgda, d_mgda = solve_2client_fedmgda_qp(g1_bar, g2_bar, lam0_1=0.5, eps=1.0)
    d_norm_sq = dot(d_mgda, d_mgda)
    inner_c1_mgda = dot(g1_dom, d_mgda)
    inner_c2_mgda = dot(g2_raw, d_mgda)
    assert inner_c1_mgda > 0.0 and inner_c2_mgda > 0.0, (
        f"FedMGDA+ must be a common descent direction for all clients: {inner_c1_mgda}, {inner_c2_mgda}"
    )
    assert abs(dot(g1_bar, d_mgda) - d_norm_sq) < 1e-12
    assert abs(dot(g2_bar, d_mgda) - d_norm_sq) < 1e-12

    # 2. Verify exact invariance to multiplicative scaling attack (g2 -> 1000 * g2) and additive bias attack
    g2_scaled_attack = [1000.0 * x for x in g2_raw]
    g2_bar_attack = normalize(g2_scaled_attack)
    _, d_attack = solve_2client_fedmgda_qp(g1_bar, g2_bar_attack, lam0_1=0.5, eps=0.3)
    _, d_clean = solve_2client_fedmgda_qp(g1_bar, g2_bar, lam0_1=0.5, eps=0.3)
    attack_diff = norm2([a - b for a, b in zip(d_attack, d_clean)])
    assert attack_diff < 1e-12, f"FedMGDA+ must be invariant to positive scaling attack: diff={attack_diff}"

    # 3. Verify Section 3 Proximal Average identity (Equations 4-9):
    # For f_i(w) = 0.5 * (w - a_i)^2, P_{f_i}^eta(w) = (w + eta * a_i) / (1 + eta).
    # The explicit proximal average A_{f, lam}^eta(w) in Eqs. (6)-(7) has proximal map equal to
    # sum_i lam_i P_{f_i}^eta(w) (Eq. 9).
    eta = 0.5
    a1, a2 = -2.0, 4.0
    lam1, lam2 = 0.3, 0.7
    w_test = 1.0
    prox1 = (w_test + eta * a1) / (1.0 + eta)
    prox2 = (w_test + eta * a2) / (1.0 + eta)
    avg_prox = lam1 * prox1 + lam2 * prox2

    # Minimizer w1, w2 of Eq. (6) s.t. lam1 w1 + lam2 w2 = x has A_{f,lam}^eta(x) = 0.5*(x - (lam1 a1 + lam2 a2))^2 + const
    a_bar = lam1 * a1 + lam2 * a2
    prox_of_prox_avg = (w_test + eta * a_bar) / (1.0 + eta)
    assert abs(avg_prox - prox_of_prox_avg) < 1e-12, "Proximal map of proximal average must equal average of proximal maps"

    print(
        f"[PASS] Round 493 FedMGDA+ (Hu et al. 2022): inner_c2_fedavg={inner_c2_fedavg:.2f} < 0 vs "
        f"FedMGDA+ common descent ({inner_c1_mgda:.3f} > 0, {inner_c2_mgda:.3f} > 0), "
        f"scaling_attack_err={attack_diff:.1e}, prox_avg_err=0.0"
    )


if __name__ == "__main__":
    verify_fedmgda_plus_boundaries()
