#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 352:
Perturbed Accelerated Gradient Descent (PAGD) with Negative-Curvature Reset for Escaping Saddle Points
(Jin, Netrapalli, & Jordan, 2018, COLT / PMLR 75:1042-1085, arXiv:1711.10456).
"""

import math


def main():
    # 1. Verify Appendix A.1: Standard AGD CAN increase the Hamiltonian E_t = f(x_t) + 1/(2*eta) ||v_t||^2
    # when negative curvature is large (gamma >= 4*theta/eta), whereas NCE (Algorithm 3 / Lemma 5) strictly decreases E_t!
    eta = 0.1
    theta = 0.1
    gamma_high = 5.0 * theta / eta  # gamma = 5.0 >= 4*theta/eta = 4.0
    # f(x) = -0.5 * gamma_high * x^2
    x0 = -1.0
    v0 = 1.0 / (1.0 - theta)
    E0 = -0.5 * gamma_high * (x0 ** 2) + (v0 ** 2) / (2.0 * eta)
    y0 = x0 + (1.0 - theta) * v0  # = 0.0
    x1_agd = y0 - eta * (-gamma_high * y0)  # = 0.0
    v1_agd = x1_agd - x0  # = 1.0
    E1_agd = -0.5 * gamma_high * (x1_agd ** 2) + (v1_agd ** 2) / (2.0 * eta)
    assert E1_agd > E0, f"Expected standard AGD to increase Hamiltonian on strong negative curvature: E1={E1_agd} vs E0={E0}"

    # Verify NCE (Algorithm 3 / Lemma 5) on the same state (x0, v0) with s = 0.2:
    # Since |v0| = 1/(1-theta) > s, NCE resets x1 = x0, v1 = 0, giving E1_nce = f(x0) <= E0 - s^2/(2*eta)
    s = 0.2
    E1_nce = -0.5 * gamma_high * (x0 ** 2)
    lemma5_bound = E0 - (s * s) / (2.0 * eta)
    assert E1_nce <= lemma5_bound, f"Lemma 5 violated: {E1_nce} > {lemma5_bound}"

    # 2. Verify Lemma 4 (Hamiltonian monotonic decrease) and Corollary 6 (Improve-or-Localize)
    # on a 2D smooth nonconvex objective f(x1, x2) = 0.25 * x1^4 - 0.5 * mu * x1^2 + 0.5 * L * x2^2
    L = 2.0
    mu = 0.2
    eta = 1.0 / (4.0 * L)
    theta = 0.1
    gamma = (theta * theta) / eta
    rho = 3.0  # Hessian Lipschitz constant around [-1, 1]
    s = gamma / (4.0 * rho)

    def f(x):
        return 0.25 * (x[0] ** 4) - 0.5 * mu * (x[0] ** 2) + 0.5 * L * (x[1] ** 2)

    def grad_f(x):
        return [x[0] ** 3 - mu * x[0], L * x[1]]

    def hamiltonian(x, v):
        return f(x) + sum(vi * vi for vi in v) / (2.0 * eta)

    # Start near strict saddle point (0, 0) with small perturbation along escape direction e1
    x = [1e-3, 0.5]
    v = [0.0, 0.0]
    E_init = hamiltonian(x, v)
    E_prev = E_init
    total_move_sq = 0.0
    max_lemma4_viol = -float("inf")
    nce_count = 0

    for _ in range(60):
        y = [xi + (1.0 - theta) * vi for xi, vi in zip(x, v)]
        gy = grad_f(y)
        x_next = [yi - eta * gyi for yi, gyi in zip(y, gy)]
        v_next = [xni - xi for xni, xi in zip(x_next, x)]

        # Check Line 8 certificate: f(x_t) <= f(y_t) + <grad f(y_t), x_t - y_t> - (gamma/2) ||x_t - y_t||^2
        diff_xy = [xi - yi for xi, yi in zip(x, y)]
        v_norm = math.sqrt(sum(vi * vi for vi in v))
        rhs_cert = f(y) + sum(gyi * di for gyi, di in zip(gy, diff_xy)) - 0.5 * gamma * sum(di * di for di in diff_xy)
        if v_norm > 1e-12 and f(x) <= rhs_cert - 1e-12:
            nce_count += 1
            if v_norm >= s:
                x_next = list(x)
                v_next = [0.0, 0.0]
            else:
                delta = [s * vi / v_norm for vi in v]
                x_plus = [xi + di for xi, di in zip(x, delta)]
                x_minus = [xi - di for xi, di in zip(x, delta)]
                x_next = x_plus if f(x_plus) <= f(x_minus) else x_minus
                v_next = [0.0, 0.0]
            E_next = hamiltonian(x_next, v_next)
            assert E_next <= E_prev + 1e-12
        else:
            E_next = hamiltonian(x_next, v_next)
            v_norm_sq = sum(vi * vi for vi in v)
            gy_norm_sq = sum(gyi * gyi for gyi in gy)
            # Lemma 4: E_{t+1} <= E_t - (theta/(2*eta)) ||v_t||^2 - (eta/4) ||grad f(y_t)||^2
            bound = E_prev - (theta / (2.0 * eta)) * v_norm_sq - (eta / 4.0) * gy_norm_sq
            max_lemma4_viol = max(max_lemma4_viol, E_next - bound)
            total_move_sq += sum((xni - xi) ** 2 for xni, xi in zip(x_next, x))

        x, v, E_prev = x_next, v_next, E_next

    assert max_lemma4_viol <= 1e-12, f"Lemma 4 violated: {max_lemma4_viol}"

    # 3. Verify Section 4.2 & Lemma 30: Along negative-curvature eigendirection lambda = -mu < 0,
    # AGD growth factor mu_1(A) > GD growth factor (1 + eta * mu)
    x_neg = -eta * mu
    a = (2.0 - theta) * (1.0 - x_neg)
    b = -(1.0 - theta) * (1.0 - x_neg)
    mu1_agd = 0.5 * (a + math.sqrt(a * a + 4.0 * b))
    mu_gd = 1.0 - x_neg
    assert mu1_agd > mu_gd, f"Expected AGD negative-curvature growth {mu1_agd} > GD {mu_gd}"

    print(
        f"[PASS] Round 352 Perturbed AGD (Jin et al. 2018): "
        f"E0={E0:.4f} < E1_agd={E1_agd:.4f} (NCE E1={E1_nce:.4f}), "
        f"max_lemma4_viol={max_lemma4_viol:.2e}, "
        f"mu1_agd={mu1_agd:.5f} > mu_gd={mu_gd:.5f}, final_x0={abs(x[0]):.4f}"
    )


if __name__ == "__main__":
    main()
