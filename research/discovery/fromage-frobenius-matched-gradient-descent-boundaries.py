#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 599: Fromage (Frobenius Matched Gradient Descent)."""

from __future__ import annotations

import math
import random


def frob_norm(mat: list[list[float]]) -> float:
    return math.sqrt(sum(val * val for row in mat for val in row))


def vec_norm(vec: list[float]) -> float:
    return math.sqrt(sum(v * v for v in vec))


def mat_vec(mat: list[list[float]], vec: list[float]) -> list[float]:
    return [sum(r * v for r, v in zip(row, vec)) for row in mat]


def leaky_relu(vec: list[float], alpha: float) -> list[float]:
    return [v if v >= 0.0 else alpha * v for v in vec]


def verify_theorem1_and_lemma2() -> tuple[float, float, bool]:
    """Verify Theorem 1 functional product bound and Lemma 2 deep relative trust descent."""
    rng = random.Random(59901)
    # 1. Exact scalar composition equality when perturbations are positive:
    # |f_tilde(x) - f(x)| / |f(x)| = prod_{k=1}^L (1 + |dw_k|/|w_k|) - 1
    L = 6
    weights = [1.2 + 0.3 * k for k in range(L)]
    eta = 0.02
    dweights = [eta * w for w in weights]
    x_scalar = 2.5
    f_val = x_scalar
    ft_val = x_scalar
    for w, dw in zip(weights, dweights):
        f_val *= w
        ft_val *= (w + dw)
    rel_scalar = abs(ft_val - f_val) / abs(f_val)
    bound_scalar = ((1.0 + eta) ** L) - 1.0
    scalar_err = abs(rel_scalar - bound_scalar)
    assert scalar_err < 1e-14, f"Scalar product identity error: {scalar_err}"

    # 2. Multilayer perceptron functional perturbation bound (Theorem 1a):
    # Orthogonal weight matrices (condition number kappa = 1) + leaky ReLU with alpha = 0.5, beta = 1.0
    alpha, beta, kappa = 0.5, 1.0, 1.0
    depth = 4
    dim = 4
    # Construct orthogonal 4x4 matrices (Hadamard / 2) scaled by layer factor
    hadamard = [
        [0.5, 0.5, 0.5, 0.5],
        [0.5, -0.5, 0.5, -0.5],
        [0.5, 0.5, -0.5, -0.5],
        [0.5, -0.5, -0.5, 0.5],
    ]
    W_list = [[[hadamard[i][j] * (1.0 + 0.2 * l) for j in range(dim)] for i in range(dim)] for l in range(depth)]
    dW_list = [[[hadamard[i][j] * (0.015 * (1.0 + 0.2 * l)) for j in range(dim)] for i in range(dim)] for l in range(depth)]
    Wt_list = [[[W_list[l][i][j] + dW_list[l][i][j] for j in range(dim)] for i in range(dim)] for l in range(depth)]

    h = [rng.uniform(-1.0, 1.0) for _ in range(dim)]
    ht = list(h)
    for l in range(depth):
        h = leaky_relu(mat_vec(W_list[l], h), alpha)
        ht = leaky_relu(mat_vec(Wt_list[l], ht), alpha)

    diff_norm = vec_norm([ht[i] - h[i] for i in range(dim)])
    rel_fn_diff = diff_norm / vec_norm(h)
    prod_term = 1.0
    for l in range(depth):
        prod_term *= 1.0 + (frob_norm(dW_list[l]) / frob_norm(W_list[l]))
    thm1_bound = ((beta / alpha) * (kappa ** 2)) ** depth * (prod_term - 1.0)
    assert rel_fn_diff <= thm1_bound + 1e-12, f"Theorem 1a violated: {rel_fn_diff} > {thm1_bound}"

    # 3. Lemma 2 descent condition under deep relative trust:
    # For cos(theta_l) = 1, eta < 2^(1/L) - 1 guarantees bracketed term > 0
    eta_crit = (2.0 ** (1.0 / depth)) - 1.0
    eta_safe = 0.5 * eta_crit
    grad_breakdown = ((1.0 + eta_safe) ** depth) - 1.0
    lemma2_ok = grad_breakdown < 1.0  # cos(0) = 1.0
    assert lemma2_ok, "Lemma 2 descent condition failed"
    return scalar_err, rel_fn_diff / thm1_bound, lemma2_ok


def verify_fromage_vs_lars_scale_invariance() -> tuple[float, float, float, float]:
    """Verify norm preservation of Fromage vs compounding growth of LARS on scale-invariant layers (Section 5, Fig. 2)."""
    # Consider a 2-layer network with scale-invariant normalized weights W_l / ||W_l||_F:
    # L(W_1, W_2) = 0.5 * sum_i ((W_1 / ||W_1||_F)_i - target_1_i)^2 + 0.5 * sum_i ((W_2 / ||W_2||_F)_i - target_2_i)^2
    # By Euler's theorem, <W_l, g_l>_F = 0 everywhere!
    rng = random.Random(59902)
    dim = 12
    target1 = [math.sin(i + 1.0) for i in range(dim)]
    t1_norm = vec_norm(target1)
    target1 = [v / t1_norm for v in target1]

    w0 = [rng.gauss(0.0, 1.0) for _ in range(dim)]
    init_norm = vec_norm(w0)

    def loss_and_grad(w: list[float]) -> tuple[float, list[float]]:
        wn = vec_norm(w)
        u = [v / wn for v in w]
        loss = 0.5 * sum((u[i] - target1[i]) ** 2 for i in range(dim))
        # dL/du_i = u_i - target1_i
        # dL/dw = (I - u u^T) (u - target1) / ||w||
        dl_du = [u[i] - target1[i] for i in range(dim)]
        dot_u = sum(u[i] * dl_du[i] for i in range(dim))
        grad = [(dl_du[i] - u[i] * dot_u) / wn for i in range(dim)]
        return loss, grad

    eta = 0.05
    steps = 120
    w_fromage = list(w0)
    w_lars = list(w0)
    prefactor = 1.0 / math.sqrt(1.0 + eta * eta)

    max_ortho_err = 0.0
    for _ in range(steps):
        _, g_f = loss_and_grad(w_fromage)
        # Verify orthogonality <w, g> = 0
        ortho = abs(sum(w_fromage[i] * g_f[i] for i in range(dim))) / (vec_norm(w_fromage) * vec_norm(g_f))
        if ortho > max_ortho_err:
            max_ortho_err = ortho
        wf_norm = vec_norm(w_fromage)
        gf_norm = vec_norm(g_f)
        w_fromage = [prefactor * (w_fromage[i] - eta * (wf_norm / gf_norm) * g_f[i]) for i in range(dim)]

        _, g_l = loss_and_grad(w_lars)
        wl_norm = vec_norm(w_lars)
        gl_norm = vec_norm(g_l)
        w_lars = [w_lars[i] - eta * (wl_norm / gl_norm) * g_l[i] for i in range(dim)]

    final_loss_fromage, _ = loss_and_grad(w_fromage)
    fromage_norm_drift = abs(vec_norm(w_fromage) - init_norm) / init_norm
    lars_norm_ratio = vec_norm(w_lars) / init_norm
    theoretical_lars_ratio = (1.0 + eta * eta) ** (steps / 2.0)

    assert max_ortho_err < 1e-14, f"Scale-invariant gradient not orthogonal to weights: {max_ortho_err}"
    assert fromage_norm_drift < 1e-13, f"Fromage failed to preserve layer norm: {fromage_norm_drift}"
    assert abs(lars_norm_ratio - theoretical_lars_ratio) < 1e-11, (
        f"LARS norm growth mismatch: {lars_norm_ratio} vs {theoretical_lars_ratio}"
    )
    assert lars_norm_ratio > 1.15, f"Expected compounding LARS norm growth, got {lars_norm_ratio}"
    assert final_loss_fromage < 1e-3, f"Fromage did not converge on scale-invariant objective: {final_loss_fromage}"
    return max_ortho_err, fromage_norm_drift, lars_norm_ratio, final_loss_fromage


def main() -> None:
    scalar_err, thm1_ratio, lemma2_ok = verify_theorem1_and_lemma2()
    ortho_err, fromage_drift, lars_growth, loss_fromage = verify_fromage_vs_lars_scale_invariance()
    print(
        f"[PASS] Round 599 Fromage verified: scalar_err={scalar_err:.2e}, "
        f"thm1_ratio={thm1_ratio:.4f}<=1, lemma2_ok={lemma2_ok}, "
        f"ortho_err={ortho_err:.2e}, fromage_norm_drift={fromage_drift:.2e}, "
        f"lars_growth={lars_growth:.4f}, loss_fromage={loss_fromage:.4e}"
    )


if __name__ == "__main__":
    main()
