#!/usr/bin/env python3
"""Boundary verification for Round 643: FOOF / First-Order-On-Features (Benzing, ICML 2022 / arXiv:2201.12250)."""

from __future__ import annotations

import math
import random


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    m, k, n = len(a), len(a[0]), len(b[0])
    out = [[0.0] * n for _ in range(m)]
    for i in range(m):
        for p in range(k):
            aip = a[i][p]
            for j in range(n):
                out[i][j] += aip * b[p][j]
    return out


def transpose(a: list[list[float]]) -> list[list[float]]:
    return [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]


def invert_spd(a: list[list[float]]) -> list[list[float]]:
    n = len(a)
    aug = [a[i][:] + [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(aug[r][col]))
        aug[col], aug[piv] = aug[piv], aug[col]
        div = aug[col][col]
        for j in range(2 * n):
            aug[col][j] /= div
        for r in range(n):
            if r != col:
                fac = aug[r][col]
                for j in range(2 * n):
                    aug[r][j] -= fac * aug[col][j]
    return [row[n:] for row in aug]


def aat_inner_product(u: list[list[float]], v: list[list[float]], aat: list[list[float]]) -> float:
    """Inner product Tr(U A A^T V^T) used in Figure 3B of Benzing (2022) to measure cos(KFAC, FOOF)."""
    uaat = matmul(u, aat)
    n, m = len(u), len(u[0])
    return sum(uaat[i][j] * v[i][j] for i in range(n) for j in range(m))


def cosine_aat(u: list[list[float]], v: list[list[float]], aat: list[list[float]]) -> float:
    num = aat_inner_product(u, v, aat)
    du = math.sqrt(max(1e-18, aat_inner_product(u, u, aat)))
    dv = math.sqrt(max(1e-18, aat_inner_product(v, v, aat)))
    return num / (du * dv)


def main() -> None:
    # 1. Verify Appendix F Toy Example (page 19): Conflicting Gradients in SGD vs FOOF
    # Two datapoints: a1 = (3, 1)^T, y1 = 1; a2 = (1, 0)^T, y2 = -1; initialized at w0 = (0, 0).
    # Negative gradients of 0.5 * (w^T a_i - y_i)^2 at w0 = (0,0) are g1 = (3, 1)^T and g2 = (-1, 0)^T.
    # Unscaled sum SGD direction is d_SGD = g1 + g2 = (2, 1)^T.
    # Undamped FOOF solves (A A^T) d_FOOF = A E^T = (2, 1)^T where A = [[3, 1], [1, 0]], A A^T = [[10, 3], [3, 1]].
    a_toy = [[3.0, 1.0], [1.0, 0.0]]
    aat_toy = matmul(a_toy, transpose(a_toy))  # [[10, 3], [3, 1]], det = 1
    aat_inv_toy = invert_spd(aat_toy)  # [[1, -3], [-3, 10]]
    ae_t = [[2.0], [1.0]]
    d_foof_col = matmul(aat_inv_toy, ae_t)  # [[-1.0], [4.0]]
    d_foof = [d_foof_col[0][0], d_foof_col[1][0]]
    d_sgd = [2.0, 1.0]

    assert abs(d_foof[0] - (-1.0)) < 1e-12 and abs(d_foof[1] - 4.0) < 1e-12

    # Check loss on datapoint 2: l2(w) = 0.5 * (w_1 * 1 + w_2 * 0 - (-1))^2 = 0.5 * (w_1 + 1)^2
    # At w0 = (0, 0), l2(w0) = 0.5.
    # Under SGD step eta > 0: w_1 = 2 * eta > 0 -> l2(eta * d_sgd) = 0.5 * (2*eta + 1)^2 > 0.5 for all eta > 0!
    # Under FOOF step eta = 1: w = (-1, 4) -> a1^T w = -3 + 4 = 1 = y1 and a2^T w = -1 = y2 (exact global optimum!).
    for eta in [0.05, 0.2, 0.5, 1.0]:
        l2_sgd = 0.5 * (eta * d_sgd[0] + 1.0) ** 2
        assert l2_sgd > 0.5, "SGD must increase loss on datapoint 2 for all positive step sizes"
    l1_foof_step1 = 0.5 * (3.0 * d_foof[0] + 1.0 * d_foof[1] - 1.0) ** 2
    l2_foof_step1 = 0.5 * (1.0 * d_foof[0] + 0.0 * d_foof[1] - (-1.0)) ** 2
    assert l1_foof_step1 < 1e-24 and l2_foof_step1 < 1e-24

    # 2. Verify Closed-Form Optimality of Equation (6) for Neuron-Space Objective Equation (5) (Section 4, page 6):
    # min_{dW} || (dW) A - eta * E ||_F^2 + lambda * || dW ||_F^2  =>  (dW)^T = eta * (lambda * I + A A^T)^{-1} A E^T
    rng = random.Random(643)
    n_out, m_in, d_batch = 5, 6, 12
    a_mat = [[rng.gauss(0.0, 1.0) for _ in range(d_batch)] for _ in range(m_in)]
    e_mat = [[rng.gauss(0.0, 1.0) for _ in range(d_batch)] for _ in range(n_out)]
    eta = 0.25
    lam_a = 0.5

    aat = matmul(a_mat, transpose(a_mat))
    aat_damped = [[aat[i][j] + (lam_a if i == j else 0.0) for j in range(m_in)] for i in range(m_in)]
    aat_damped_inv = invert_spd(aat_damped)
    ae_t_mat = matmul(a_mat, transpose(e_mat))
    dw_foof_t = [[eta * v for v in row] for row in matmul(aat_damped_inv, ae_t_mat)]
    dw_foof = transpose(dw_foof_t)

    def eq5_objective(dw: list[list[float]]) -> float:
        dwa = matmul(dw, a_mat)
        fit = sum((dwa[i][j] - eta * e_mat[i][j]) ** 2 for i in range(n_out) for j in range(d_batch))
        prox = lam_a * sum(dw[i][j] ** 2 for i in range(n_out) for j in range(m_in))
        return fit + prox

    obj_opt = eq5_objective(dw_foof)
    for _ in range(50):
        dw_pert = [[dw_foof[i][j] + rng.gauss(0.0, 0.02) for j in range(m_in)] for i in range(n_out)]
        assert eq5_objective(dw_pert) > obj_opt

    # 3. Verify Section 4.2 & Figure 3B: Heuristic Damping Increases Cosine Similarity cos(KFAC, FOOF) -> 1.0
    # KFAC update: (dW_KFAC)^T = (A A^T + lam_A I)^{-1} (A E^T) (E_F E_F^T + lam_E I)^{-1}
    ef_mat = [[rng.gauss(0.0, 1.0) for _ in range(d_batch)] for _ in range(n_out)]
    efef_t = matmul(ef_mat, transpose(ef_mat))

    cos_by_lam_e: list[float] = []
    for lam_e in [1e-2, 10.0, 5000.0]:
        efef_damped = [[efef_t[i][j] + (lam_e if i == j else 0.0) for j in range(n_out)] for i in range(n_out)]
        efef_inv = invert_spd(efef_damped)
        dw_kfac_t = matmul(matmul(aat_damped_inv, ae_t_mat), efef_inv)
        dw_kfac = transpose(dw_kfac_t)
        cos_by_lam_e.append(cosine_aat(dw_kfac, dw_foof, aat))

    assert cos_by_lam_e[0] < cos_by_lam_e[1] < cos_by_lam_e[2] and cos_by_lam_e[2] > 0.999

    print(
        f"[PASS] Round 643 FOOF verified: d_FOOF={d_foof}, l_toy_step1=({l1_foof_step1:.1e},{l2_foof_step1:.1e}), "
        f"obj_eq5_opt={obj_opt:.4f}, cos(KFAC,FOOF)={[round(c, 5) for c in cos_by_lam_e]}"
    )


if __name__ == "__main__":
    main()
