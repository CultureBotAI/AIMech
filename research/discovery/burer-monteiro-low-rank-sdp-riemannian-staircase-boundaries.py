#!/usr/bin/env python3
"""Boundary and verification script for Round 336:
The Non-Convex Burer-Monteiro Approach Works on Smooth Semidefinite Programs
(Boumal, Voroninski, & Bandeira, NeurIPS 2016 pp. 2757-2765, arXiv:1606.04970v3; CPAM 2019).
"""

import math
import sys


def jacobi_eig(S):
    n = len(S)
    A = [row[:] for row in S]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(80):
        p, q = 0, 1
        mx = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i][j]) > mx:
                    mx = abs(A[i][j])
                    p, q = i, j
        if mx < 1e-15:
            break
        phi = (A[q][q] - A[p][p]) / (2.0 * A[p][q])
        t = 1.0 / (abs(phi) + math.sqrt(phi * phi + 1.0))
        if phi < 0:
            t = -t
        c = 1.0 / math.sqrt(1.0 + t * t)
        s = t * c
        tau = s / (1.0 + c)
        h = t * A[p][q]
        A[p][p] -= h
        A[q][q] += h
        A[p][q] = A[q][p] = 0.0
        for r in range(n):
            if r != p and r != q:
                arp, arq = A[r][p], A[r][q]
                A[r][p] = A[p][r] = arp - s * (arq + tau * arp)
                A[r][q] = A[q][r] = arq + s * (arp - tau * arq)
        for r in range(n):
            vrp, vrq = V[r][p], V[r][q]
            V[r][p] = vrp - s * (vrq + tau * vrp)
            V[r][q] = vrq + s * (vrp - tau * vrq)
    eigs = [A[i][i] for i in range(n)]
    vecs = [[V[r][i] for r in range(n)] for i in range(n)]
    pairs = sorted(zip(eigs, vecs), key=lambda x: x[0])
    return [p[0] for p in pairs], [p[1] for p in pairs]


def matmul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][r] * B[r][j] for r in range(k)) for j in range(n)] for i in range(m)]


def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def dual_slack_oblique(C, Y):
    """Lemma 2.1 (Equation 5, p. 4):
    For unit-diagonal SDP on Oblique(n, p), mu_i = (C Y Y^T)_{ii} and S(Y) = C - Diag(mu).
    """
    n, p = len(Y), len(Y[0])
    CY = matmul(C, Y)
    mu = [sum(CY[i][r] * Y[i][r] for r in range(p)) for i in range(n)]
    S = [[C[i][j] - (mu[i] if i == j else 0.0) for j in range(n)] for i in range(n)]
    return mu, S


def riemannian_hess_quad(C, Y, Y_dot):
    """Lemma 2.2 (Equation 7, p. 5):
    <Y_dot, Hess g(Y)[Y_dot]> = <Y_dot, S(Y) Y_dot> for Y_dot in T_Y M_p.
    """
    _, S = dual_slack_oblique(C, Y)
    SY_dot = matmul(S, Y_dot)
    n, p = len(Y), len(Y[0])
    return sum(Y_dot[i][r] * SY_dot[i][r] for i in range(n) for r in range(p))


def main():
    # Frustrated 5-cycle Max-Cut / Z2 synchronization SDP:
    # min_{X >= 0, diag(X) = 1} <C, X> where C is adjacency matrix of 5-cycle C_5.
    # For C_5, eigenvalues of C are 2 cos(2*pi*k/5):
    # k=0: 2.0 (mult 1)
    # k=1,4: 2 cos(2*pi/5) = (sqrt(5)-1)/2 approx +0.618034 (mult 2)
    # k=2,3: 2 cos(4*pi/5) = -(sqrt(5)+1)/2 approx -1.618034 (mult 2)
    n = 5
    C = [[0.0] * n for _ in range(n)]
    for i in range(n):
        C[i][(i + 1) % n] = 1.0
        C[i][(i - 1) % n] = 1.0

    # 1. Verify saddle / spurious critical point at low rank p=2 (where p(p+1)/2 = 3 <= m = 5)
    # Take the k=1 harmonic embedding y_i = [cos(2*pi*i/5), sin(2*pi*i/5)] in Oblique(5, 2):
    # C Y = (2 cos(2*pi/5)) Y, so (C - mu_1 I) Y = 0 -> exact 1st-order Riemannian critical point!
    Y_low = [
        [math.cos(2.0 * math.pi * i / n), math.sin(2.0 * math.pi * i / n)]
        for i in range(n)
    ]
    mu_low, S_low = dual_slack_oblique(C, Y_low)
    grad_low = matmul(S_low, Y_low)
    grad_low_norm = math.sqrt(sum(grad_low[i][r] ** 2 for i in range(n) for r in range(2)))
    eigs_S_low, vecs_S_low = jacobi_eig(S_low)
    min_eig_S_low = eigs_S_low[0]  # = 2 cos(4*pi/5) - 2 cos(2*pi/5) = -sqrt(5) < 0!

    # 2. Verify Riemannian Staircase escape direction (Lemma 2.4, Equation 9, p. 5):
    # Lift Y_low in M_2 to Y_lift = [Y_low, 0] in M_3 (so rank(Y_lift) = 2 < p = 3, with p(p+1)/2 = 6 > m = 5).
    # For z = [0, 0, 1]^T in ker(Y_lift) and negative-curvature eigenvector u = vecs_S_low[0] of S(Y_low),
    # Y_dot = u z^T lies in T_{Y_lift} M_3 and <Y_dot, Hess g(Y_lift)[Y_dot]> == u^T S(Y_lift) u == min_eig_S_low < 0!
    Y_lift = [row + [0.0] for row in Y_low]
    u_neg = vecs_S_low[0]
    Y_dot_escape = [[0.0, 0.0, u_neg[i]] for i in range(n)]
    # Check tangent condition: diag(Y_dot_escape * Y_lift^T) == 0
    tangent_err = max(
        abs(sum(Y_dot_escape[i][r] * Y_lift[i][r] for r in range(3)))
        for i in range(n)
    )
    hess_escape_val = riemannian_hess_quad(C, Y_lift, Y_dot_escape)
    lemma24_escape_err = abs(hess_escape_val - min_eig_S_low)

    # 3. Verify Global Optimum at rank-deficient 2-critical point in M_3 (Barvinok-Pataki p(p+1)/2 = 6 > m = 5):
    # The k=2 harmonic embedding y*_i = [cos(4*pi*i/5), sin(4*pi*i/5), 0] in M_3 has rank 2 < p = 3,
    # C Y* = 2 cos(4*pi/5) Y*, mu*_i = 2 cos(4*pi/5) = -(1 + sqrt(5))/2,
    # S(Y*) = C - mu* I >= 0 (PSD!), and primal objective <C, Y* Y*^T> == sum_i mu*_i = -5*(1+sqrt(5))/2!
    Y_opt = [
        [math.cos(4.0 * math.pi * i / n), math.sin(4.0 * math.pi * i / n), 0.0]
        for i in range(n)
    ]
    mu_opt, S_opt = dual_slack_oblique(C, Y_opt)
    grad_opt = matmul(S_opt, Y_opt)
    grad_opt_norm = math.sqrt(sum(grad_opt[i][r] ** 2 for i in range(n) for r in range(3)))
    eigs_S_opt, _ = jacobi_eig(S_opt)
    min_eig_S_opt = eigs_S_opt[0]

    X_opt = matmul(Y_opt, transpose(Y_opt))
    primal_obj = sum(C[i][j] * X_opt[i][j] for i in range(n) for j in range(n))
    dual_obj = sum(mu_opt)
    duality_gap = abs(primal_obj - dual_obj)
    exact_c5_sdp_val = -5.0 * (1.0 + math.sqrt(5.0)) / 2.0

    # Verify Barvinok-Pataki bound p(p+1)/2 > m at p=3, m=5
    bp_lhs = (3 * 4) // 2
    bp_holds = bp_lhs > n

    ok = (
        grad_low_norm < 1e-14
        and abs(min_eig_S_low - (-math.sqrt(5.0))) < 1e-13
        and tangent_err < 1e-15
        and lemma24_escape_err < 1e-13
        and hess_escape_val < -2.23
        and grad_opt_norm < 1e-14
        and min_eig_S_opt > -1e-14
        and duality_gap < 1e-13
        and abs(primal_obj - exact_c5_sdp_val) < 1e-13
        and bp_holds
    )
    if not ok:
        print("Verification failed!", file=sys.stderr)
        sys.exit(1)

    print(
        f"[PASS] Round 336 Burer-Monteiro & Riemannian Staircase (Boumal et al. 2016): "
        f"min_eig_S_low={min_eig_S_low:.4f}, hess_escape_val={hess_escape_val:.4f}, "
        f"min_eig_S_opt={min_eig_S_opt:.2e}, primal_obj={primal_obj:.6f}, duality_gap={duality_gap:.2e}"
    )


if __name__ == "__main__":
    main()
