#!/usr/bin/env python3
"""Boundary and verification script for Round 337:
How to Escape Saddle Points Efficiently (Perturbed Gradient Descent)
(Jin, Ge, Netrapalli, Kakade, & Jordan, ICML 2017, PMLR 70:1724-1732, arXiv:1703.00887).
"""

import math
import random
import sys


def matmul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][r] * B[r][j] for r in range(k)) for j in range(n)] for i in range(m)]


def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def frob_sq(A):
    return sum(x * x for row in A for x in row)


def frob_inner(A, B):
    return sum(A[i][j] * B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def mf_obj(U, M_star):
    d = len(U)
    UUT = matmul(U, transpose(U))
    diff = [[UUT[i][j] - M_star[i][j] for j in range(d)] for i in range(d)]
    return 0.5 * frob_sq(diff)


def mf_grad(U, M_star):
    """Equation 21 (Appendix C.1, p. 31): grad f(U) = 2 (U U^T - M*) U."""
    d = len(U)
    UUT = matmul(U, transpose(U))
    diff = [[2.0 * (UUT[i][j] - M_star[i][j]) for j in range(d)] for i in range(d)]
    return matmul(diff, U)


def mf_hess_quad(U, Z, M_star):
    """Equation 22 (Appendix C.1, p. 31):
    grad^2 f(U)(Z, Z) = ||U Z^T + Z U^T||_F^2 + 2 <U U^T - M*, Z Z^T>.
    """
    d = len(U)
    UZT = matmul(U, transpose(Z))
    ZUT = transpose(UZT)
    sym_UZ = [[UZT[i][j] + ZUT[i][j] for j in range(d)] for i in range(d)]
    UUT = matmul(U, transpose(U))
    diff = [[UUT[i][j] - M_star[i][j] for j in range(d)] for i in range(d)]
    ZZT = matmul(Z, transpose(Z))
    return frob_sq(sym_UZ) + 2.0 * frob_inner(diff, ZZT)


def main():
    # 1. Verify Lemma 6 & Lemma 7 (Section 4 & Appendix C, Equations 21-26, pp. 10-11, 31-35)
    # Construct rank-2 target M* = V* V*^T in R^{4 x 4} with singular values sigma*_1 = 4.0, sigma*_2 = 2.0
    V_star = [
        [2.0, 0.0],
        [0.0, math.sqrt(2.0)],
        [0.0, 0.0],
        [0.0, 0.0],
    ]
    M_star = matmul(V_star, transpose(V_star))
    sigma1_star, sigmar_star = 4.0, 2.0

    # Verify exact algebraic Hessian identity in Proof of Lemma 7 (p. 33):
    # For U* = V* and Delta = U - U*,
    # grad^2 f(U)(Delta, Delta) == ||Delta Delta^T||_F^2 - 3 ||U U^T - M*||_F^2 + 4 <grad f(U), Delta>
    U_test = [
        [0.1, -0.05],
        [0.02, 0.08],
        [0.4, -0.3],
        [-0.2, 0.5],
    ]
    Delta = [[U_test[i][j] - V_star[i][j] for j in range(2)] for i in range(4)]
    hess_lhs = mf_hess_quad(U_test, Delta, M_star)
    DDT = matmul(Delta, transpose(Delta))
    UUT_minus_M = [
        [matmul(U_test, transpose(U_test))[i][j] - M_star[i][j] for j in range(4)]
        for i in range(4)
    ]
    grad_U = mf_grad(U_test, M_star)
    hess_rhs = frob_sq(DDT) - 3.0 * frob_sq(UUT_minus_M) + 4.0 * frob_inner(grad_U, Delta)
    lemma7_hess_id_err = abs(hess_lhs - hess_rhs)

    # Verify strict negative curvature at saddle point U_saddle = [[0,0],[0,0],[sqrt(2),0],[0,0]]
    # where grad f(U_saddle) = 0 requires U_saddle^T U_saddle = M_star projected, or at U_0 = 0:
    U_zero = [[0.0, 0.0] for _ in range(4)]
    grad_zero_norm = math.sqrt(frob_sq(mf_grad(U_zero, M_star)))
    Delta_zero = [[-V_star[i][j] for j in range(2)] for i in range(4)]
    rayleigh_zero = mf_hess_quad(U_zero, Delta_zero, M_star) / frob_sq(Delta_zero)
    # By Lemma 7, strict saddle negative eigenvalue <= -1/3 * sigma_r^* = -2/3
    strict_saddle_holds = (grad_zero_norm == 0.0) and (rayleigh_zero <= -sigmar_star / 3.0)

    # 2. Verify Lemma 15 ("Thin Pancake" Width of Stuck Region, Appendix A.2, p. 19):
    # Consider the rank-1 strict saddle point U_saddle = [[0,0],[sqrt(2),0],[0,0],[0,0]] where grad f(U_saddle) = 0
    # and f(U_saddle) = 8.0. Perturb U_a inside the stuck subspace (row 0 == [0,0], orthogonal to negative
    # eigendirection e_1 = [[1,0],[0,0],[0,0],[0,0]]) and U_b = U_a + mu * r * e_1:
    eta = 0.03
    r_ball = 0.1
    mu_sep = 0.3
    U_a = [[0.0, 0.0], [math.sqrt(2.0) - 0.02, 0.01], [0.02, -0.01], [0.0, 0.02]]
    U_b = [row[:] for row in U_a]
    U_b[0][0] += mu_sep * r_ball

    for _ in range(250):
        g_a = mf_grad(U_a, M_star)
        g_b = mf_grad(U_b, M_star)
        U_a = [[U_a[i][j] - eta * g_a[i][j] for j in range(2)] for i in range(4)]
        U_b = [[U_b[i][j] - eta * g_b[i][j] for j in range(2)] for i in range(4)]

    # U_a remains trapped in the rank-1 strict saddle subspace (row 0 == 0) with f(U_a) -> 8.0,
    # whereas U_b escapes exponentially along e_1 (Lemma 17 Eq. 17) and converges to M* (f(U_b) -> 0)!
    f_final_a = mf_obj(U_a, M_star)
    f_final_b = mf_obj(U_b, M_star)

    # 3. Verify Stuck Region Volume Ratio Bound (Proof of Lemma 14, p. 20):
    # Vol(X_stuck) / Vol(B^(d)(r)) <= (delta / sqrt(pi * d)) * Gamma(d/2 + 1) / Gamma(d/2 + 1/2) <= delta
    delta = 0.05
    max_vol_ratio_over_delta = 0.0
    for d_dim in [2, 4, 8, 16, 32]:
        vol_ratio = (
            (delta / math.sqrt(math.pi * d_dim))
            * math.gamma(0.5 * d_dim + 1.0)
            / math.gamma(0.5 * d_dim + 0.5)
        )
        max_vol_ratio_over_delta = max(max_vol_ratio_over_delta, vol_ratio / delta)

    # 4. Verify Local (alpha, beta)-Regularity Condition (Lemma 7(2) & Equation 26, pp. 34-35):
    # Near V*, <grad f(U), U - U*> >= (1/3) sigma_r^* ||U - U*||_F^2 + (1 / (20 sigma_1^*)) ||grad f(U)||_F^2
    U_near = [
        [2.01, 0.0],
        [0.0, math.sqrt(2.0) - 0.01],
        [0.005, 0.0],
        [0.0, 0.005],
    ]
    grad_near = mf_grad(U_near, M_star)
    Delta_near = [[U_near[i][j] - V_star[i][j] for j in range(2)] for i in range(4)]
    lhs_reg = frob_inner(grad_near, Delta_near)
    rhs_reg = (sigmar_star / 3.0) * frob_sq(Delta_near) + (1.0 / (20.0 * sigma1_star)) * frob_sq(grad_near)

    ok = (
        lemma7_hess_id_err < 1e-13
        and strict_saddle_holds
        and abs(f_final_a - 8.0) < 1e-5
        and f_final_b < 1e-8
        and max_vol_ratio_over_delta <= 1.0
        and lhs_reg >= rhs_reg
    )
    if not ok:
        print(
            f"Verification failed: id_err={lemma7_hess_id_err}, saddle={strict_saddle_holds}, "
            f"fa={f_final_a}, fb={f_final_b}, vol={max_vol_ratio_over_delta}, reg={lhs_reg}>={rhs_reg}",
            file=sys.stderr,
        )
        sys.exit(1)

    print(
        f"[PASS] Round 337 Perturbed Gradient Descent (Jin et al. 2017): "
        f"lemma7_hess_id_err={lemma7_hess_id_err:.2e}, rayleigh_zero={rayleigh_zero:.4f}, "
        f"f_stuck={f_final_a:.4f}, f_escaped={f_final_b:.2e}, "
        f"max_vol_ratio_over_delta={max_vol_ratio_over_delta:.4f}"
    )


if __name__ == "__main__":
    main()
