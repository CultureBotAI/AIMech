#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 589:
SOAP (Improving and Stabilizing Shampoo using Adam) — Vyas et al. (ICLR 2025; arXiv:2409.11321).
"""

import math
import random
from typing import List, Tuple

Matrix = List[List[float]]


def zeros(m: int, n: int) -> Matrix:
    return [[0.0] * n for _ in range(m)]


def eye(n: int, scale: float = 1.0) -> Matrix:
    out = zeros(n, n)
    for i in range(n):
        out[i][i] = scale
    return out


def transpose(a: Matrix) -> Matrix:
    return [list(col) for col in zip(*a)]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    m, k, n = len(a), len(a[0]), len(b[0])
    out = zeros(m, n)
    for i in range(m):
        for p in range(k):
            aip = a[i][p]
            for j in range(n):
                out[i][j] += aip * b[p][j]
    return out


def matadd(a: Matrix, b: Matrix, scale_a: float = 1.0, scale_b: float = 1.0) -> Matrix:
    return [[scale_a * a[i][j] + scale_b * b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def trace(a: Matrix) -> float:
    return sum(a[i][i] for i in range(len(a)))


def jacobi_eigh(a: Matrix, tol: float = 1e-14, max_sweeps: int = 120) -> Tuple[List[float], Matrix]:
    n = len(a)
    d = [row[:] for row in a]
    v = eye(n)
    for _ in range(max_sweeps):
        max_off = 0.0
        p, q = 0, 1
        for i in range(n):
            for j in range(i + 1, n):
                if abs(d[i][j]) > max_off:
                    max_off = abs(d[i][j])
                    p, q = i, j
        if max_off < tol:
            break
        tau = (d[q][q] - d[p][p]) / (2.0 * d[p][q])
        t = (1.0 if tau >= 0 else -1.0) / (abs(tau) + math.sqrt(1.0 + tau * tau))
        c = 1.0 / math.sqrt(1.0 + t * t)
        s = t * c
        d_pp, d_qq, d_pq = d[p][p], d[q][q], d[p][q]
        d[p][p] = c * c * d_pp - 2.0 * s * c * d_pq + s * s * d_qq
        d[q][q] = s * s * d_pp + 2.0 * s * c * d_pq + c * c * d_qq
        d[p][q] = d[q][p] = 0.0
        for k in range(n):
            if k != p and k != q:
                dkp, dkq = d[k][p], d[k][q]
                d[k][p] = d[p][k] = c * dkp - s * dkq
                d[k][q] = d[q][k] = s * dkp + c * dkq
        for k in range(n):
            vkp, vkq = v[k][p], v[k][q]
            v[k][p] = c * vkp - s * vkq
            v[k][q] = s * vkp + c * vkq
    w = [d[i][i] for i in range(n)]
    return w, v


def psd_power(a: Matrix, alpha: float) -> Matrix:
    w, v = jacobi_eigh(a)
    n = len(a)
    scaled_vt = [[(max(w[i], 1e-15) ** alpha) * v[j][i] for j in range(n)] for i in range(n)]
    return matmul(v, scaled_vt)


def qr_gram_schmidt(a: Matrix) -> Matrix:
    """Algorithm 4 QR orthogonalization of columns of S = P Q."""
    n = len(a)
    cols = transpose(a)
    q_cols: List[List[float]] = []
    for col in cols:
        v = col[:]
        for u in q_cols:
            proj = sum(v[i] * u[i] for i in range(n))
            v = [v[i] - proj * u[i] for i in range(n)]
        norm = math.sqrt(sum(x * x for x in v))
        q_cols.append([x / norm for x in v])
    return transpose(q_cols)


def verify_claim1_equivalence() -> float:
    """Section 4.1 Claim 1: Idealized Shampoo (power 1/2, trace-scaled) == Idealized Adafactor in Shampoo's eigenbasis."""
    rng = random.Random(589)
    m, n = 4, 3
    num_batches = 24
    batches = [
        [[rng.gauss(0.0, 1.0 + 0.5 * i) for _ in range(n)] for i in range(m)]
        for _ in range(num_batches)
    ]
    L = eye(m, 1e-6)
    R = eye(n, 1e-6)
    for gb in batches:
        L = matadd(L, matmul(gb, transpose(gb)), 1.0, 1.0 / num_batches)
        R = matadd(R, matmul(transpose(gb), gb), 1.0, 1.0 / num_batches)

    G_t = batches[0]
    # Algorithm 1: Idealized Shampoo with power 1/2 and Trace(L) scaling
    tr_L = trace(L)
    L_m12 = psd_power(L, -0.5)
    R_m12 = psd_power(R, -0.5)
    step_alg1 = [[x * math.sqrt(tr_L) for x in row] for row in matmul(matmul(L_m12, G_t), R_m12)]

    # Algorithm 2: Idealized Adafactor in Shampoo's eigenbasis
    _, Q_L = jacobi_eigh(L)
    _, Q_R = jacobi_eigh(R)
    E_sq = zeros(m, n)
    for gb in batches:
        gb_rot = matmul(matmul(transpose(Q_L), gb), Q_R)
        for i in range(m):
            for j in range(n):
                E_sq[i][j] += (gb_rot[i][j] ** 2) / num_batches
    # Add the same 1e-6 identity contribution to eigenvalues
    for i in range(m):
        for j in range(n):
            pass
    # Wait: if L = E_B[G_B G_B^T] without +1e-6 I, let's test exact L = E_B[G_B G_B^T] and R = E_B[G_B^T G_B]
    L_exact = zeros(m, n if False else m)
    R_exact = zeros(n, n)
    for gb in batches:
        L_exact = matadd(L_exact, matmul(gb, transpose(gb)), 1.0, 1.0 / num_batches)
        R_exact = matadd(R_exact, matmul(transpose(gb), gb), 1.0, 1.0 / num_batches)
    tr_Le = trace(L_exact)
    step_alg1_exact = [
        [x * math.sqrt(tr_Le) for x in row]
        for row in matmul(matmul(psd_power(L_exact, -0.5), G_t), psd_power(R_exact, -0.5))
    ]
    _, Q_Le = jacobi_eigh(L_exact)
    _, Q_Re = jacobi_eigh(R_exact)
    E_sq_e = zeros(m, n)
    for gb in batches:
        gb_rot = matmul(matmul(transpose(Q_Le), gb), Q_Re)
        for i in range(m):
            for j in range(n):
                E_sq_e[i][j] += (gb_rot[i][j] ** 2) / num_batches
    A = [sum(E_sq_e[i][j] for j in range(n)) for i in range(m)]
    C = [sum(E_sq_e[i][j] for i in range(m)) for j in range(n)]
    sum_A = sum(A)
    G_rot = matmul(matmul(transpose(Q_Le), G_t), Q_Re)
    G_pp = [[G_rot[i][j] / math.sqrt(A[i] * C[j] / sum_A) for j in range(n)] for i in range(m)]
    step_alg2_exact = matmul(matmul(Q_Le, G_pp), transpose(Q_Re))

    max_diff = max(
        abs(step_alg1_exact[i][j] - step_alg2_exact[i][j])
        for i in range(m)
        for j in range(n)
    )
    assert max_diff < 1e-11, f"Claim 1 equivalence mismatch: {max_diff}"
    return max_diff


def run_stale_preconditioner_comparison(freq: int = 10, steps: int = 120) -> Tuple[float, float]:
    """Compare SOAP (Algorithm 3+4) vs stale Shampoo when eigenbasis/inverse is updated every `freq` steps."""
    rng = random.Random(20260589)
    m, n = 3, 3
    A_left = [[4.0, 1.2, 0.3], [1.2, 1.5, 0.2], [0.3, 0.2, 0.2]]
    B_right = [[3.5, -0.8, 0.4], [-0.8, 1.2, -0.1], [0.4, -0.1, 0.25]]
    W_star = [[0.8, -0.5, 0.3], [-0.4, 0.7, -0.6], [0.2, -0.3, 0.9]]

    def loss_and_grad(W: Matrix, step_idx: int) -> Tuple[float, Matrix]:
        # Slowly rotating curvature + anisotropic scaling
        angle = 0.015 * step_idx
        c, s = math.cos(angle), math.sin(angle)
        rot = [[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]]
        A_t = matmul(matmul(rot, A_left), transpose(rot))
        diff = matadd(W, W_star, 1.0, -1.0)
        G = matmul(matmul(A_t, diff), B_right)
        loss = 0.5 * sum(diff[i][j] * G[i][j] for i in range(m) for j in range(n))
        return loss, G

    # SOAP (Algorithm 3)
    W_soap = zeros(m, n)
    M_soap = zeros(m, n)
    V_soap = zeros(m, n)
    L_soap = eye(m, 1e-4)
    R_soap = eye(n, 1e-4)
    Q_L = eye(m)
    Q_R = eye(n)
    beta1, beta2, eps, lr = 0.9, 0.95, 1e-8, 0.08

    for t in range(1, steps + 1):
        _, G = loss_and_grad(W_soap, t)
        G_prime = matmul(matmul(transpose(Q_L), G), Q_R)
        M_soap = matadd(M_soap, G, beta1, 1.0 - beta1)
        M_prime = matmul(matmul(transpose(Q_L), M_soap), Q_R)
        for i in range(m):
            for j in range(n):
                V_soap[i][j] = beta2 * V_soap[i][j] + (1.0 - beta2) * (G_prime[i][j] ** 2)
        bc1 = 1.0 - beta1 ** t
        bc2 = 1.0 - beta2 ** t
        N_prime = [
            [(M_prime[i][j] / bc1) / (math.sqrt(V_soap[i][j] / bc2) + eps) for j in range(n)]
            for i in range(m)
        ]
        N = matmul(matmul(Q_L, N_prime), transpose(Q_R))
        W_soap = matadd(W_soap, N, 1.0, -lr)
        L_soap = matadd(L_soap, matmul(G, transpose(G)), beta2, 1.0 - beta2)
        R_soap = matadd(R_soap, matmul(transpose(G), G), beta2, 1.0 - beta2)
        if t == 1:
            _, Q_L = jacobi_eigh(L_soap)
            _, Q_R = jacobi_eigh(R_soap)
        elif t % freq == 0:
            Q_L = qr_gram_schmidt(matmul(L_soap, Q_L))
            Q_R = qr_gram_schmidt(matmul(R_soap, Q_R))

    # Stale Shampoo without inner diagonal Adam tracking
    W_sh = zeros(m, n)
    M_sh = zeros(m, n)
    L_sh = eye(m, 1e-4)
    R_sh = eye(n, 1e-4)
    L_inv = eye(m)
    R_inv = eye(n)
    for t in range(1, steps + 1):
        _, G = loss_and_grad(W_sh, t)
        M_sh = matadd(M_sh, G, beta1, 1.0 - beta1)
        L_sh = matadd(L_sh, matmul(G, transpose(G)), beta2, 1.0 - beta2)
        R_sh = matadd(R_sh, matmul(transpose(G), G), beta2, 1.0 - beta2)
        if t == 1 or t % freq == 0:
            tr_l = max(trace(L_sh), 1e-12)
            L_inv = psd_power(L_sh, -0.5)
            R_inv = [[x * math.sqrt(tr_l) for x in row] for row in psd_power(R_sh, -0.5)]
        step_sh = matmul(matmul(L_inv, M_sh), R_inv)
        W_sh = matadd(W_sh, step_sh, 1.0, -0.02)

    loss_soap, _ = loss_and_grad(W_soap, steps)
    loss_sh, _ = loss_and_grad(W_sh, steps)
    assert loss_soap < loss_sh, f"Expected SOAP loss < stale Shampoo loss: {loss_soap} vs {loss_sh}"
    return loss_soap, loss_sh


def main() -> None:
    claim1_diff = verify_claim1_equivalence()
    loss_soap, loss_sh = run_stale_preconditioner_comparison(freq=10, steps=120)
    # Verify Section 7.2.1 space complexity formulas for Transformer MLP layer (m = 4 * n)
    m, n = 4096, 1024
    space_full_soap = 2 * m * m + 2 * n * n + 3 * m * n
    space_onesided_factorized = 2 * (min(m, n) ** 2) + 2 * m * n
    space_adamw = 3 * m * n
    assert space_onesided_factorized < space_adamw < space_full_soap
    print(
        f"[PASS] Round 589 SOAP verified: claim1_diff={claim1_diff:.2e}, "
        f"loss_soap={loss_soap:.4e}<loss_sh={loss_sh:.4e}, "
        f"space=({space_onesided_factorized}<{space_adamw}<{space_full_soap})"
    )


if __name__ == "__main__":
    main()
