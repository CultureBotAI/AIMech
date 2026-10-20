#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 600: Cautious Optimizers (C-AdamW / C-Lion)."""

from __future__ import annotations

import math


def verify_theorem2_1_and_2_3() -> tuple[float, float, float]:
    """Verify Theorem 2.1 (Hamiltonian+Descent monotonic rates) and Theorem 2.3 (discrete step dominance)."""
    # Theorem 2.1: x_t = grad_L(w) o grad_K(s)
    # phi(x)_i = alpha(x) * I(x_i > 0) with alpha(x) = d / (nnz(x > 0) + xi)
    x = [0.8, -0.5, 1.2, -0.9, 0.4, -0.3]
    d = len(x)
    nnz_pos = sum(1 for v in x if v > 0.0)
    # With xi = 0.5 and nnz_pos = 3 < d = 6, alpha = 6 / 3.5 > 1
    alpha = d / (nnz_pos + 0.5)
    phi_x = [alpha if v > 0.0 else 0.0 for v in x]

    # Condition 1: x^T phi(x) >= 0 (ensures dL/dt <= 0)
    x_dot_phi = sum(v * p for v, p in zip(x, phi_x))
    assert x_dot_phi > 0.0, f"Expected x^T phi(x) > 0, got {x_dot_phi}"

    # Condition 2: x^T (1 - phi(x)) <= 0 (ensures both H and L decrease faster than original system)
    x_dot_one_minus_phi = sum(v * (1.0 - p) for v, p in zip(x, phi_x))
    assert x_dot_one_minus_phi < 0.0, f"Expected x^T (1 - phi(x)) <= 0, got {x_dot_one_minus_phi}"

    # Theorem 2.3: Discrete-time dominance on mu-smooth quadratic L(w) = 0.5 * sum_i mu_i w_i^2
    mu_vec = [4.0, 2.0, 3.0, 1.5, 2.5, 3.5]
    mu = max(mu_vec)
    w = [1.0, -0.8, 0.6, 1.2, -0.5, 0.9]
    g = [m * wi for m, wi in zip(mu_vec, w)]
    # Momentum vector u_t with mixed alignment with g_t so u_t o g_t = x
    u = [xi / gi for xi, gi in zip(x, g)]

    r_t = [ui * (1.0 - pi) for ui, pi in zip(u, phi_x)]
    delta_ug = -sum((ui * gi) * (1.0 - pi) for ui, gi, pi in zip(u, g, phi_x))
    norm_u = math.sqrt(sum(ui * ui for ui in u))
    norm_r = math.sqrt(sum(ri * ri for ri in r_t))
    eps_max = (2.0 * delta_ug) / (mu * norm_r * (2.0 * norm_u + norm_r))
    eps = 0.8 * eps_max

    w_base = [wi - eps * ui for wi, ui in zip(w, u)]
    w_cautious = [wi - eps * ui * pi for wi, ui, pi in zip(w, u, phi_x)]
    loss_base = 0.5 * sum(m * (wi ** 2) for m, wi in zip(mu_vec, w_base))
    loss_cautious = 0.5 * sum(m * (wi ** 2) for m, wi in zip(mu_vec, w_cautious))
    assert loss_cautious < loss_base, f"Theorem 2.3 violated: {loss_cautious} >= {loss_base}"
    return x_dot_phi, x_dot_one_minus_phi, loss_base - loss_cautious


def verify_2d_toy_and_cadamw() -> tuple[int, int, float, float]:
    """Verify Section 3.1 2D toy (L(w) = 4 w_1^2 + w_2^2) monotonic descent and C-AdamW vs AdamW."""
    # Section 3.1: L(w) = kappa * w_1^2 + w_2^2 with kappa = 4, w_0 = (1, 1)
    kappa = 4.0

    def loss_2d(w: list[float]) -> float:
        return kappa * (w[0] ** 2) + (w[1] ** 2)

    def grad_2d(w: list[float]) -> list[float]:
        return [2.0 * kappa * w[0], 2.0 * w[1]]

    steps = 60
    beta = 0.9
    eps = 0.01

    # Standard GDM
    w_gdm = [1.0, 1.0]
    s_gdm = [0.0, 0.0]
    gdm_nonmono_steps = 0
    prev_l_gdm = loss_2d(w_gdm)
    for _ in range(steps):
        g = grad_2d(w_gdm)
        s_gdm = [beta * s_gdm[i] + g[i] for i in range(2)]
        w_gdm = [w_gdm[i] - eps * s_gdm[i] for i in range(2)]
        cur_l = loss_2d(w_gdm)
        if cur_l > prev_l_gdm + 1e-15:
            gdm_nonmono_steps += 1
        prev_l_gdm = cur_l

    # Cautious GDM (C-GDM)
    w_cgdm = [1.0, 1.0]
    s_cgdm = [0.0, 0.0]
    cgdm_nonmono_steps = 0
    prev_l_cgdm = loss_2d(w_cgdm)
    for _ in range(steps):
        g = grad_2d(w_cgdm)
        s_cgdm = [beta * s_cgdm[i] + g[i] for i in range(2)]
        mask = [1.0 if s_cgdm[i] * g[i] > 0.0 else 0.0 for i in range(2)]
        scale = 2.0 / (sum(mask) + 1.0)
        w_cgdm = [w_cgdm[i] - eps * scale * mask[i] * s_cgdm[i] for i in range(2)]
        cur_l = loss_2d(w_cgdm)
        if cur_l > prev_l_cgdm + 1e-15:
            cgdm_nonmono_steps += 1
        prev_l_cgdm = cur_l

    assert gdm_nonmono_steps > 0, "Expected standard GDM to exhibit non-monotonic oscillation"
    assert cgdm_nonmono_steps == 0, f"Expected C-GDM to decrease loss monotonically, got {cgdm_nonmono_steps}"
    assert loss_2d(w_cgdm) < loss_2d(w_gdm), f"Expected C-GDM final loss < GDM: {loss_2d(w_cgdm)} vs {loss_2d(w_gdm)}"

    # Compare Algorithm 2 (C-AdamW) vs AdamW on 8D ill-conditioned Rosenbrock-like objective
    dim = 8

    def obj_grad(w: list[float]) -> tuple[float, list[float]]:
        val = 0.0
        g = [0.0] * dim
        for i in range(dim - 1):
            a = w[i + 1] - w[i] * w[i]
            b = 1.0 - w[i]
            val += 25.0 * a * a + b * b
            g[i] += -100.0 * w[i] * a - 2.0 * b
            g[i + 1] += 50.0 * a
        return val, g

    def run_adamw(cautious: bool) -> float:
        w = [-1.2 if i % 2 == 0 else 1.0 for i in range(dim)]
        m = [0.0] * dim
        v = [0.0] * dim
        beta1, beta2, eps_adam, lr, wd = 0.9, 0.98, 1e-8, 0.015, 0.01
        for t in range(1, 251):
            _, g = obj_grad(w)
            m = [beta1 * m[i] + (1.0 - beta1) * g[i] for i in range(dim)]
            v = [beta2 * v[i] + (1.0 - beta2) * (g[i] * g[i]) for i in range(dim)]
            bc1 = 1.0 - (beta1 ** t)
            bc2 = 1.0 - (beta2 ** t)
            u = [(m[i] / bc1) / (math.sqrt(v[i] / bc2) + eps_adam) for i in range(dim)]
            if cautious:
                phi = [1.0 if u[i] * g[i] > 0.0 else 0.0 for i in range(dim)]
                lr_bar = lr * (dim / (sum(phi) + 1.0))
                w = [w[i] - lr_bar * phi[i] * u[i] for i in range(dim)]
                w = [w[i] - lr_bar * wd * w[i] for i in range(dim)]
            else:
                w = [w[i] - lr * u[i] - lr * wd * w[i] for i in range(dim)]
        final_loss, _ = obj_grad(w)
        return final_loss

    loss_adamw = run_adamw(cautious=False)
    loss_cadamw = run_adamw(cautious=True)
    assert loss_cadamw < loss_adamw, f"Expected C-AdamW < AdamW: {loss_cadamw} vs {loss_adamw}"
    return gdm_nonmono_steps, cgdm_nonmono_steps, loss_cadamw, loss_adamw


def main() -> None:
    x_phi, x_one_minus_phi, thm23_gain = verify_theorem2_1_and_2_3()
    gdm_osc, cgdm_osc, loss_cadamw, loss_adamw = verify_2d_toy_and_cadamw()
    print(
        f"[PASS] Round 600 Cautious Optimizers verified: x_phi={x_phi:.4f}>0, "
        f"x_1m_phi={x_one_minus_phi:.4f}<0, thm23_gain={thm23_gain:.4e}>0, "
        f"osc=(GDM:{gdm_osc}, C-GDM:{cgdm_osc}), loss_cadamw={loss_cadamw:.4e}<loss_adamw={loss_adamw:.4e}"
    )


if __name__ == "__main__":
    main()
