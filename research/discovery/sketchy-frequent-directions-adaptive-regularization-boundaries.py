#!/usr/bin/env python3
"""Boundary verification for Round 645: Sketchy / S-AdaGrad & S-Shampoo (Feinberg et al., NeurIPS 2023 / arXiv:2302.03764)."""

from __future__ import annotations

import math
import random


def outer(g: list[float]) -> list[list[float]]:
    return [[gi * gj for gj in g] for gi in g]


def matvec(a: list[list[float]], x: list[float]) -> list[float]:
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def dot(x: list[float], y: list[float]) -> float:
    return sum(xi * yi for xi, yi in zip(x, y))


def sym_eigh(a_in: list[list[float]], iters: int = 80) -> tuple[list[float], list[list[float]]]:
    """Jacobi eigendecomposition of symmetric matrix A, returning descending (eigenvalues, eigenvectors_as_columns)."""
    n = len(a_in)
    a = [row[:] for row in a_in]
    v = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(iters):
        for i in range(n):
            for j in range(i + 1, n):
                if abs(a[i][j]) < 1e-14:
                    continue
                tau = (a[j][j] - a[i][i]) / (2.0 * a[i][j])
                t = math.copysign(1.0 / (abs(tau) + math.sqrt(1.0 + tau * tau)), tau)
                c = 1.0 / math.sqrt(1.0 + t * t)
                s = t * c
                aii, ajj, aij = a[i][i], a[j][j], a[i][j]
                a[i][i] = c * c * aii - 2.0 * s * c * aij + s * s * ajj
                a[j][j] = s * s * aii + 2.0 * s * c * aij + c * c * ajj
                a[i][j] = a[j][i] = 0.0
                for k in range(n):
                    if k != i and k != j:
                        aki, akj = a[k][i], a[k][j]
                        a[k][i] = a[i][k] = c * aki - s * akj
                        a[k][j] = a[j][k] = s * aki + c * akj
                for k in range(n):
                    vki, vkj = v[k][i], v[k][j]
                    v[k][i] = c * vki - s * vkj
                    v[k][j] = s * vki + c * vkj
    order = sorted(range(n), key=lambda idx: a[idx][idx], reverse=True)
    evals = [a[idx][idx] for idx in order]
    evecs = [[v[r][idx] for idx in order] for r in range(n)]
    return evals, evecs


def fd_update(g_bar: list[list[float]], m_t: list[list[float]], ell: int) -> tuple[float, list[list[float]]]:
    """Algorithm 1 (page 3): Frequent Directions Update (FD-update)."""
    d = len(g_bar)
    sum_mat = [[g_bar[i][j] + m_t[i][j] for j in range(d)] for i in range(d)]
    evals, evecs = sym_eigh(sum_mat)
    rho_t = max(0.0, evals[ell - 1])
    g_bar_next = [[0.0] * d for _ in range(d)]
    for k in range(ell - 1):
        lam_k = max(0.0, evals[k] - rho_t)
        for i in range(d):
            for j in range(d):
                g_bar_next[i][j] += lam_k * evecs[i][k] * evecs[j][k]
    return rho_t, g_bar_next


def min_eigenvalue(a: list[list[float]]) -> float:
    evals, _ = sym_eigh(a)
    return min(evals)


def max_eigenvalue(a: list[list[float]]) -> float:
    evals, _ = sym_eigh(a)
    return max(evals)


def main() -> None:
    rng = random.Random(645)
    d = 6
    ell = 3
    t_steps = 25

    # Generate a stream of gradients with fast spectral decay (matching Section 5.2)
    scales = [4.0, 2.5, 0.4, 0.2, 0.1, 0.05]
    g_true = [[0.0] * d for _ in range(d)]
    g_bar = [[0.0] * d for _ in range(d)]
    rho_cum = 0.0

    # 1. Verify Lemma 10 & Remark 11 (Appendix B.4.1, page 19):
    # At every step t, G_bar_t <= G_t <= G_tilde_t = G_bar_t + rho_{1:t} * I_d in Loewner order!
    for _ in range(t_steps):
        g_t = [scales[i] * rng.gauss(0.0, 1.0) for i in range(d)]
        m_t = outer(g_t)
        for i in range(d):
            for j in range(d):
                g_true[i][j] += m_t[i][j]
        rho_t, g_bar = fd_update(g_bar, m_t, ell)
        rho_cum += rho_t
        g_tilde = [[g_bar[i][j] + (rho_cum if i == j else 0.0) for j in range(d)] for i in range(d)]

        # Check G_t - G_bar_t >= 0 and G_tilde_t - G_t >= 0
        diff_lower = [[g_true[i][j] - g_bar[i][j] for j in range(d)] for i in range(d)]
        diff_upper = [[g_tilde[i][j] - g_true[i][j] for j in range(d)] for i in range(d)]
        assert min_eigenvalue(diff_lower) >= -1e-9, f"Violated G_bar_t <= G_t: {min_eigenvalue(diff_lower)}"
        assert min_eigenvalue(diff_upper) >= -1e-9, f"Violated G_t <= G_tilde_t: {min_eigenvalue(diff_upper)}"

    # 2. Verify Lemma 1 (Liberty Escaped-Mass Bound, page 3) & Observation 6:
    # ||G_T - G_bar_T||_2 <= rho_{1:T} <= min_{k < ell} sum_{i=k+1}^d lambda_i(G_T) / (ell - k) <= sum_{i=ell}^d lambda_i(G_T)
    evals_true, _ = sym_eigh(g_true)
    op_err = max_eigenvalue([[g_true[i][j] - g_bar[i][j] for j in range(d)] for i in range(d)])
    omega_ell = min(sum(evals_true[k:]) / (ell - k) for k in range(ell))
    tail_sum = sum(evals_true[ell - 1 :])
    assert op_err <= rho_cum + 1e-9
    assert rho_cum <= omega_ell + 1e-9 <= tail_sum + 1e-9

    # 3. Verify Sublinear Accumulator Memory of S-Shampoo vs Adam and Shampoo (Figure 1, page 5):
    # For BERT-Large FFN rectangular matrix m = 4096, n = 1024 with FD rank k = 256:
    m_dim, n_dim, k_rank = 4096, 1024, 256
    mem_shampoo = m_dim * m_dim + n_dim * n_dim
    mem_adam = m_dim * n_dim
    mem_ssham = m_dim * k_rank + n_dim * k_rank
    assert mem_ssham < mem_adam < mem_shampoo
    assert mem_ssham / mem_adam == 0.3125  # 68.75% less second-moment memory than Adam, and 4x+ less than Shampoo!

    print(
        f"[PASS] Round 645 Sketchy verified: op_err={op_err:.4f}<=rho_1:T={rho_cum:.4f}<=Omega_l={omega_ell:.4f}<=tail={tail_sum:.4f}, "
        f"mem_ratio(S-Shampoo/Adam)={mem_ssham/mem_adam:.4f}, mem_ratio(S-Shampoo/Shampoo)={mem_ssham/mem_shampoo:.4f}"
    )


if __name__ == "__main__":
    main()
