#!/usr/bin/env python3
"""Constructed boundary verification for Round 578: Basis Learn (BL1, BL2, BL3) (Qian, Islamov, Safaryan, Richtarik, AISTATS 2022)."""

from __future__ import annotations

import math


def mat_vec(a: list[list[float]], x: list[float]) -> list[float]:
    return [sum(row[j] * x[j] for j in range(len(x))) for row in a]


def mat_add(a: list[list[float]], b: list[list[float]], scale_b: float = 1.0) -> list[list[float]]:
    d = len(a)
    return [[a[j][l] + scale_b * b[j][l] for l in range(d)] for j in range(d)]


def frob_sq(a: list[list[float]]) -> float:
    return sum(val * val for row in a for val in row)


def symmetrize(a: list[list[float]]) -> list[list[float]]:
    d = len(a)
    return [[0.5 * (a[j][l] + a[l][j]) for l in range(d)] for j in range(d)]


def top_k_matrix(a: list[list[float]], k: int) -> list[list[float]]:
    d = len(a)
    entries = [(abs(a[j][l]), j, l) for j in range(d) for l in range(d)]
    entries.sort(reverse=True)
    out = [[0.0] * d for _ in range(d)]
    for _, j, l in entries[:k]:
        out[j][l] = a[j][l]
    return out


def solve_spd(a: list[list[float]], b: list[float]) -> list[float]:
    """Gaussian elimination with partial pivoting for small SPD linear systems."""
    d = len(b)
    aug = [list(a[i]) + [b[i]] for i in range(d)]
    for col in range(d):
        piv = max(range(col, d), key=lambda r: abs(aug[r][col]))
        aug[col], aug[piv] = aug[piv], aug[col]
        div = aug[col][col]
        for j in range(col, d + 1):
            aug[col][j] /= div
        for r in range(d):
            if r != col and aug[r][col] != 0.0:
                factor = aug[r][col]
                for j in range(col, d + 1):
                    aug[r][j] -= factor * aug[col][j]
    return [aug[i][d] for i in range(d)]


def main() -> None:
    # 1. Verify Equation (5): Exact lossless representation of GLM local Hessian in r^2 outer-product basis
    # Let d = 5, intrinsic subspace dimension r = 2 per client, n = 3 clients, m = 4 samples per client.
    d, r, n, m = 5, 2, 3, 4
    lam = 0.2

    # Construct dense orthonormal basis vectors {v_{i,1}, v_{i,2}} in R^d for each client i
    client_bases: list[list[list[float]]] = []
    for i in range(n):
        v1 = [math.cos(0.5 * (i + 1) * (c + 1) + 0.2) for c in range(d)]
        n1 = math.sqrt(sum(c * c for c in v1))
        v1 = [c / n1 for c in v1]
        v2 = [math.sin(0.9 * (i + 1) * (c + 1) - 0.3) for c in range(d)]
        # Orthonormalize v2 against v1
        dot12 = sum(v1[c] * v2[c] for c in range(d))
        v2 = [v2[c] - dot12 * v1[c] for c in range(d)]
        n2 = math.sqrt(sum(c * c for c in v2))
        v2 = [c / n2 for c in v2]
        client_bases.append([v1, v2])

    # Local coefficients alpha_{i,j,t} for j in [m], t in [r]
    alphas: list[list[list[float]]] = []
    labels: list[list[float]] = []
    data_vecs: list[list[list[float]]] = []
    for i in range(n):
        ai_alphas = []
        ai_vecs = []
        ai_labels = []
        for j in range(m):
            al = [0.8 * ((i + j + 1) % 3 - 1.0) + 0.5, -0.6 * ((2 * i + j) % 3 - 0.5)]
            ai_alphas.append(al)
            vec = [
                sum(al[t] * client_bases[i][t][c] for t in range(r))
                for c in range(d)
            ]
            ai_vecs.append(vec)
            ai_labels.append(1.0 if (i + j) % 2 == 0 else -1.0)
        alphas.append(ai_alphas)
        data_vecs.append(ai_vecs)
        labels.append(ai_labels)

    def phi_second_deriv(u: float) -> float:
        s = 1.0 / (1.0 + math.exp(-u))
        return s * (1.0 - s)

    def local_grad(i: int, x: list[float]) -> list[float]:
        g = [lam * xk for xk in x]
        for j in range(m):
            aij = data_vecs[i][j]
            bij = labels[i][j]
            u = bij * sum(aij[c] * x[c] for c in range(d))
            coeff = -bij / (1.0 + math.exp(u)) / m
            for c in range(d):
                g[c] += coeff * aij[c]
        return g

    def local_hess_standard(i: int, x: list[float]) -> list[list[float]]:
        """Unregularized GLM Hessian part in standard basis R^{d x d} (Equation 3)."""
        h = [[0.0] * d for _ in range(d)]
        for j in range(m):
            aij = data_vecs[i][j]
            bij = labels[i][j]
            u = bij * sum(aij[c] * x[c] for c in range(d))
            w = phi_second_deriv(u) / m
            for c1 in range(d):
                for c2 in range(d):
                    h[c1][c2] += w * aij[c1] * aij[c2]
        return h

    def local_hess_basis_coeffs(i: int, x: list[float]) -> list[list[float]]:
        """Coefficient matrix h^i(nabla^2 f_i(x)) in the custom basis (only top-left r x r block is non-zero, Eq. 5)."""
        coeff = [[0.0] * d for _ in range(d)]
        for t in range(r):
            for l in range(r):
                val = 0.0
                for j in range(m):
                    aij = data_vecs[i][j]
                    bij = labels[i][j]
                    u = bij * sum(aij[c] * x[c] for c in range(d))
                    val += phi_second_deriv(u) * alphas[i][j][t] * alphas[i][j][l] / m
                coeff[t][l] = val
        return coeff

    def reconstruct_from_basis(i: int, coeff: list[list[float]]) -> list[list[float]]:
        """Reconstruct sum_{t,l=1}^r coeff_{t,l} v_{i,t} v_{i,l}^T."""
        h = [[0.0] * d for _ in range(d)]
        for t in range(r):
            for l in range(r):
                ctl = coeff[t][l]
                vt = client_bases[i][t]
                vl = client_bases[i][l]
                for c1 in range(d):
                    for c2 in range(d):
                        h[c1][c2] += ctl * vt[c1] * vl[c2]
        return h

    x_test = [0.3, -0.2, 0.5, -0.4, 0.1]
    for i in range(n):
        h_std = local_hess_standard(i, x_test)
        c_bas = local_hess_basis_coeffs(i, x_test)
        h_rec = reconstruct_from_basis(i, c_bas)
        diff = math.sqrt(frob_sq(mat_add(h_std, h_rec, -1.0)))
        assert diff < 1e-15, f"Basis representation Eq. (5) mismatch: {diff}"
        # Count non-zeros in basis representation vs standard representation
        nz_basis = sum(1 for row in c_bas for v in row if abs(v) > 1e-14)
        assert nz_basis <= r * r == 4

    # 2. Verify Lemma 3.1: Symmetrization preserves contractiveness
    b_asym = [[1.2, -0.5, 0.3, 0.0, 0.1], [0.4, 0.8, -0.2, 0.5, 0.0], [0.0, 0.1, 0.9, -0.3, 0.2], [0.2, -0.1, 0.4, 0.7, 0.0], [-0.3, 0.2, 0.0, 0.1, 1.1]]
    a_sym = local_hess_standard(0, x_test)
    err_sym = frob_sq(mat_add(symmetrize(b_asym), a_sym, -1.0))
    err_raw = frob_sq(mat_add(b_asym, a_sym, -1.0))
    assert err_sym <= err_raw + 1e-15

    # 3. Compute exact optimum x^* via Newton's method
    x_star = [0.0] * d
    for _ in range(25):
        g_tot = [sum(local_grad(i, x_star)[c] for i in range(n)) / n for c in range(d)]
        h_tot = [[lam if c1 == c2 else 0.0 for c2 in range(d)] for c1 in range(d)]
        for i in range(n):
            hi = local_hess_standard(i, x_star)
            for c1 in range(d):
                for c2 in range(d):
                    h_tot[c1][c2] += hi[c1][c2] / n
        step = solve_spd(h_tot, g_tot)
        x_star = [x_star[c] - step[c] for c in range(d)]
    g_star_norm = math.sqrt(sum(v * v for v in [sum(local_grad(i, x_star)[c] for i in range(n)) / n for c in range(d)]))
    assert g_star_norm < 1e-14

    # 4. Compare BL1 (Algorithm 1) in custom subspace basis vs FedNL in standard basis under Top-K (K=2) compression
    # With K=2, BL1 compresses a 2x2 matrix (delta_BL1 = K / r^2 = 2/4 = 0.5), whereas standard-basis FedNL
    # compresses a 5x5 matrix (delta_FedNL = K / d^2 = 2/25 = 0.08).
    k_comp = 2
    x_bl1 = [0.5, -0.4, 0.3, -0.2, 0.4]
    x_fnl = list(x_bl1)
    l_bl1 = [[[0.0] * d for _ in range(d)] for _ in range(n)]
    h_fnl = [[[0.0] * d for _ in range(d)] for _ in range(n)]

    for _ in range(18):
        # BL1 step
        for i in range(n):
            hi_coeff = local_hess_basis_coeffs(i, x_bl1)
            diff_i = mat_add(hi_coeff, l_bl1[i], -1.0)
            s_i = top_k_matrix(diff_i, k_comp)
            l_bl1[i] = mat_add(l_bl1[i], s_i, 1.0)
        h_server_bl1 = [[lam if c1 == c2 else 0.0 for c2 in range(d)] for c1 in range(d)]
        for i in range(n):
            rec_i = reconstruct_from_basis(i, l_bl1[i])
            for c1 in range(d):
                for c2 in range(d):
                    h_server_bl1[c1][c2] += 0.5 * (rec_i[c1][c2] + rec_i[c2][c1]) / n
        g_bl1 = [sum(local_grad(i, x_bl1)[c] for i in range(n)) / n for c in range(d)]
        step_bl1 = solve_spd(h_server_bl1, g_bl1)
        x_bl1 = [x_bl1[c] - step_bl1[c] for c in range(d)]

        # Standard-basis FedNL step with identical K=2 budget
        for i in range(n):
            hi_std = local_hess_standard(i, x_fnl)
            diff_i = mat_add(hi_std, h_fnl[i], -1.0)
            s_i = top_k_matrix(diff_i, k_comp)
            h_fnl[i] = mat_add(h_fnl[i], s_i, 1.0)
        h_server_fnl = [[lam if c1 == c2 else 0.0 for c2 in range(d)] for c1 in range(d)]
        for i in range(n):
            for c1 in range(d):
                for c2 in range(d):
                    h_server_fnl[c1][c2] += 0.5 * (h_fnl[i][c1][c2] + h_fnl[i][c2][c1]) / n
        g_fnl = [sum(local_grad(i, x_fnl)[c] for i in range(n)) / n for c in range(d)]
        step_fnl = solve_spd(h_server_fnl, g_fnl)
        x_fnl = [x_fnl[c] - step_fnl[c] for c in range(d)]

    err_bl1 = math.sqrt(sum((x_bl1[c] - x_star[c]) ** 2 for c in range(d)))
    err_fnl = math.sqrt(sum((x_fnl[c] - x_star[c]) ** 2 for c in range(d)))
    hess_err_bl1 = sum(
        frob_sq(mat_add(reconstruct_from_basis(i, l_bl1[i]), local_hess_standard(i, x_star), -1.0))
        for i in range(n)
    ) / n
    hess_err_fnl = sum(
        frob_sq(mat_add(h_fnl[i], local_hess_standard(i, x_star), -1.0))
        for i in range(n)
    ) / n

    assert err_bl1 < 1e-14 and hess_err_bl1 < 1e-10
    assert hess_err_bl1 < 1e-5 * hess_err_fnl

    print(
        f"[PASS] Round 578 BasisLearn (BL1) verified: r^2={r*r}<<d^2={d*d}, "
        f"err_bl1={err_bl1:.3e}, hess_err_bl1={hess_err_bl1:.3e} << hess_err_fnl={hess_err_fnl:.3e}"
    )


if __name__ == "__main__":
    main()
