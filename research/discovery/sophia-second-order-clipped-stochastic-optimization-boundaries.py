#!/usr/bin/env python3
"""Constructed boundary verification for Round 583: Sophia Optimizer (Liu, Li, Hall, Liang, Ma, ICLR 2024)."""

from __future__ import annotations

import itertools
import math


def clip_val(z: float, rho: float) -> float:
    return max(min(z, rho), -rho)


def main() -> None:
    # 1. Verify Section 2.1 (Footnote 1, Figure 2, Equations 1-4):
    # L(theta_1, theta_2) = L_1(theta_1) + L_2(theta_2)
    # where L_1(t) = 8*(t - 1)^2 * (1.3*t^2 + 2*t + 1) and L_2(t) = 0.5*(t - 4)^2.
    # Global minimum is at theta^* = (1.0, 4.0) with L(1.0, 4.0) = 0.
    # Near theta_1 = -0.8, L_1''(theta_1) < 0 (nonconvex negative curvature region)!
    def l1_grad_hess(t: float) -> tuple[float, float]:
        # L_1(t) = 8 * (1.3 t^4 - 0.6 t^3 - 0.3 t^2 + 2 t - 2 t + 1) -> compute exact derivatives:
        # Let u(t) = (t - 1)^2, v(t) = 1.3 t^2 + 2 t + 1
        u = (t - 1.0) ** 2
        du = 2.0 * (t - 1.0)
        d2u = 2.0
        v = 1.3 * t * t + 2.0 * t + 1.0
        dv = 2.6 * t + 2.0
        d2v = 2.6
        g = 8.0 * (du * v + u * dv)
        h = 8.0 * (d2u * v + 2.0 * du * dv + u * d2v)
        return g, h

    def l2_grad_hess(t: float) -> tuple[float, float]:
        return t - 4.0, 1.0

    # Check that at theta_0 = (0.15, 0.0), L_1''(0.15) < 0 (negative curvature!) and L_1'(0.15) < 0,
    # so vanilla Newton converges to the local maximum at t1 = 0.0, while Sophia clips to SignGD and converges to (1.0, 4.0)!
    g0, h0 = l1_grad_hess(0.15)
    assert h0 < 0.0 and g0 < 0.0

    # Vanilla Newton from theta_0 = (0.15, 0.0)
    t1_newt, t2_newt = 0.15, 0.0
    for _ in range(15):
        g1, h1 = l1_grad_hess(t1_newt)
        g2, h2 = l2_grad_hess(t2_newt)
        t1_newt -= g1 / h1
        t2_newt -= g2 / h2
    # Vanilla Newton converges to the local maximum t1 = 0.0 instead of the minimum t1 = 1.0!
    assert abs(t1_newt - 0.0) < 1e-10 and abs(t1_newt - 1.0) > 0.99

    # Deterministic Sophia (Equation 4) from theta_0 = (0.15, 0.0)
    t1_soph, t2_soph = 0.15, 0.0
    eta, rho, eps = 0.35, 1.0, 1e-12
    for _ in range(65):
        g1, h1 = l1_grad_hess(t1_soph)
        g2, h2 = l2_grad_hess(t2_soph)
        t1_soph -= eta * clip_val(g1 / max(h1, eps), rho)
        t2_soph -= eta * clip_val(g2 / max(h2, eps), rho)
    err_soph = math.hypot(t1_soph - 1.0, t2_soph - 4.0)
    assert err_soph < 1e-10, f"Sophia failed to converge from nonconvex region: {err_soph}"

    # SignGD from theta_0 = (0.15, 0.0) with same eta=0.35 bounces in sharp dimension t1 and cannot converge below O(eta)
    t1_sign, t2_sign = 0.15, 0.0
    for _ in range(65):
        g1, _ = l1_grad_hess(t1_sign)
        g2, _ = l2_grad_hess(t2_sign)
        t1_sign -= eta * (1.0 if g1 > 0 else (-1.0 if g1 < 0 else 0.0))
        t2_sign -= eta * (1.0 if g2 > 0 else (-1.0 if g2 < 0 else 0.0))
    err_sign = math.hypot(t1_sign - 1.0, t2_sign - 4.0)
    assert err_soph < 1e-8 * err_sign

    # 2. Verify Equations (9)-(13): Exact unbiasedness of the Mini-Batch Gauss-Newton-Bartlett (GNB) Estimator
    # Consider a linear-softmax categorical model over B = 2 examples, V = 3 classes, parameter theta in R^{V x d} (d = 2).
    # By enumerating all V^B = 9 label combinations (y_hat_1, y_hat_2) weighted by their exact softmax probabilities
    # p(y_hat_1 | x_1) p(y_hat_2 | x_2), verify that E[B * grad_L_hat odot grad_L_hat] == (1/B) sum_{b=1}^B diag(J_b S_b J_b^T).
    b_size, v_classes, d_dim = 2, 3, 2
    x_inputs = [[0.8, -0.4], [-0.5, 1.1]]
    theta_mat = [[0.3, -0.2], [-0.4, 0.6], [0.1, -0.3]]  # 3 x 2

    probs_batch = []
    for b in range(b_size):
        logits = [
            sum(theta_mat[c][j] * x_inputs[b][j] for j in range(d_dim))
            for c in range(v_classes)
        ]
        max_l = max(logits)
        exps = [math.exp(l - max_l) for l in logits]
        z = sum(exps)
        probs_batch.append([e / z for e in exps])

    # Analytical Gauss-Newton diagonal for (1/B) sum_{b=1}^B l_ce(f(theta, x_b), y_b):
    # For linear logits f_c(theta, x_b) = theta_c^T x_b, (J_b S_b J_b^T)_{(c,j),(c,j)} = p_b[c]*(1 - p_b[c]) * (x_b[j])^2
    gn_diag_exact = [[0.0] * d_dim for _ in range(v_classes)]
    for b in range(b_size):
        for c in range(v_classes):
            sc = probs_batch[b][c] * (1.0 - probs_batch[b][c])
            for j in range(d_dim):
                gn_diag_exact[c][j] += (sc * (x_inputs[b][j] ** 2)) / b_size

    # Exact expectation of Algorithm 2 (GNB mini-batch estimator B * g_hat odot g_hat) over all V^B = 9 sampled label pairs
    gnb_expected = [[0.0] * d_dim for _ in range(v_classes)]
    for y_hats in itertools.product(range(v_classes), repeat=b_size):
        prob_joint = 1.0
        for b in range(b_size):
            prob_joint *= probs_batch[b][y_hats[b]]
        # Mini-batch gradient g_hat of (1/B) sum_{b=1}^B l_ce(f(theta, x_b), y_hat_b)
        g_hat = [[0.0] * d_dim for _ in range(v_classes)]
        for b in range(b_size):
            yh = y_hats[b]
            for c in range(v_classes):
                diff = probs_batch[b][c] - (1.0 if c == yh else 0.0)
                for j in range(d_dim):
                    g_hat[c][j] += (diff * x_inputs[b][j]) / b_size
        for c in range(v_classes):
            for j in range(d_dim):
                gnb_expected[c][j] += prob_joint * (b_size * (g_hat[c][j] ** 2))

    max_gnb_diff = max(
        abs(gn_diag_exact[c][j] - gnb_expected[c][j])
        for c in range(v_classes)
        for j in range(d_dim)
    )
    assert max_gnb_diff < 1e-15, f"GNB Bartlett identity Eq. (13) failed: {max_gnb_diff}"

    # 3. Verify Lemma D.10 (Descent Lemma) & Lemma D.11: Condition-number-independent convergence of Sophia
    # on a quadratic with condition number kappa = 10^6 (sigma_1 = 10^6, sigma_2 = 1.0).
    sigmas = [1e6, 1.0]
    theta_q = [10.0, 10.0]
    eta_q, rho_q = 0.5, 2.0
    for _ in range(50):
        grads = [sigmas[i] * theta_q[i] for i in range(2)]
        # Preconditioned eigenspace step clip(sigma_i^{-1} grad_i, rho)
        theta_q = [
            theta_q[i] - eta_q * clip_val(grads[i] / sigmas[i], rho_q)
            for i in range(2)
        ]
    loss_q = 0.5 * sum(sigmas[i] * (theta_q[i] ** 2) for i in range(2))
    assert loss_q < 1e-12

    print(
        f"[PASS] Round 583 Sophia verified: err_soph={err_soph:.3e}<<err_sign={err_sign:.3e}, "
        f"gnb_diff={max_gnb_diff:.2e}, kappa_1e6_loss={loss_q:.3e}"
    )


if __name__ == "__main__":
    main()
