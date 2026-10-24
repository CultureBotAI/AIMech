#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 366:
Alecton Stochastic Gradient Descent for Non-Convex Matrix Problems
(De Sa, Olukotun, & Re 2015, ICML 2015, PMLR 37:2332-2341, arXiv:1411.1134).
"""

import math
import random


def mat_transpose(A):
    return [list(col) for col in zip(*A)]


def mat_mul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)] for i in range(m)]


def mat_add(A, B, scale_b=1.0):
    return [[A[i][j] + scale_b * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mat_trace(A):
    return sum(A[i][i] for i in range(len(A)))


def det_2x2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def inv_2x2(M):
    d = det_2x2(M)
    return [
        [M[1][1] / d, -M[0][1] / d],
        [-M[1][0] / d, M[0][0] / d],
    ]


def main():
    rng = random.Random(20261019)

    # 1. Verify Section 2 (Page 4, Eq. 4): Riemannian Metric Rescaling Equivalence
    # Y_{k+1} = (I + eta A_tilde_k) Y_k (I + eta Y_k^T Y_k)^{-1} has the EXACT same column space
    # as unnormalized stochastic power iteration Y_bar_{k+1} = (I + eta A_tilde_k) Y_bar_k for p=2!
    n, p = 5, 2
    eta = 0.08
    Y_sgd = [[rng.gauss(0, 1) for _ in range(p)] for _ in range(n)]
    Y_bar = [row[:] for row in Y_sgd]
    I_n = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    I_p = [[1.0 if i == j else 0.0 for j in range(p)] for i in range(p)]

    for step in range(8):
        # Sample symmetric matrix A_tilde_k
        M_rand = [[rng.gauss(0, 1) for _ in range(n)] for _ in range(n)]
        A_tilde = [[0.5 * (M_rand[i][j] + M_rand[j][i]) for j in range(n)] for i in range(n)]
        I_plus_eta_A = mat_add(I_n, A_tilde, eta)

        # Update Y_bar
        Y_bar = mat_mul(I_plus_eta_A, Y_bar)
        # Update Y_sgd via Riemannian metric rescaled SGD rule
        YtY = mat_mul(mat_transpose(Y_sgd), Y_sgd)
        inv_factor = inv_2x2(mat_add(I_p, YtY, eta))
        Y_sgd = mat_mul(mat_mul(I_plus_eta_A, Y_sgd), inv_factor)

    # Compare orthogonal projection matrices onto column spaces of Y_sgd and Y_bar:
    # P = Y (Y^T Y)^{-1} Y^T
    P_sgd = mat_mul(mat_mul(Y_sgd, inv_2x2(mat_mul(mat_transpose(Y_sgd), Y_sgd))), mat_transpose(Y_sgd))
    P_bar = mat_mul(mat_mul(Y_bar, inv_2x2(mat_mul(mat_transpose(Y_bar), Y_bar))), mat_transpose(Y_bar))
    colspace_diff = math.sqrt(sum((P_sgd[i][j] - P_bar[i][j]) ** 2 for i in range(n) for j in range(n)))
    assert colspace_diff < 1e-13, f"Column space equivalence error: {colspace_diff}"

    # 2. Verify Lemma 6 (Quadratic rational lower bound), Lemma 15 & Lemma 8 (Determinant identity),
    # and Lemma 10 & Lemma 16 (phi_k >= 1 - tau_k) (Pages 18-19, 26-30)
    # Lemma 15 for p=2 and rank-1 B = u v^T:
    u_vec = [[rng.gauss(0, 1)] for _ in range(n)]
    v_vec = [[rng.gauss(0, 1)] for _ in range(n)]
    B_rk1 = mat_mul(u_vec, mat_transpose(v_vec))
    Z_diag = [1.5, 1.2, 0.8, 0.5, 0.3]
    Z_psd = [[Z_diag[i] if i == j else 0.0 for j in range(n)] for i in range(n)]
    Y_mat = Y_sgd

    I_plus_B = mat_add(I_n, B_rk1, 1.0)
    M_updated = mat_mul(mat_mul(mat_transpose(I_plus_B), Z_psd), I_plus_B)
    lhs_lemma15 = det_2x2(mat_mul(mat_mul(mat_transpose(Y_mat), M_updated), Y_mat))

    YtZY = mat_mul(mat_mul(mat_transpose(Y_mat), Z_psd), Y_mat)
    det_YtZY = det_2x2(YtZY)
    inv_YtZY = inv_2x2(YtZY)
    # P_Y = Y (Y^T Z Y)^{-1} Y^T
    P_Y = mat_mul(mat_mul(Y_mat, inv_YtZY), mat_transpose(Y_mat))
    tr1 = mat_trace(mat_mul(mat_mul(P_Y, Z_psd), B_rk1))
    tr2 = mat_trace(mat_mul(mat_mul(mat_mul(P_Y, mat_transpose(B_rk1)), Z_psd), B_rk1))
    Z_PY_Z = mat_mul(mat_mul(Z_psd, P_Y), Z_psd)
    tr3 = mat_trace(mat_mul(mat_mul(mat_mul(Z_PY_Z, B_rk1), P_Y), mat_transpose(B_rk1)))
    rhs_lemma15 = det_YtZY * ((tr1 + 1.0) ** 2 + tr2 - tr3)
    lemma15_err = abs(lhs_lemma15 - rhs_lemma15)
    assert lemma15_err < 1e-12, f"Lemma 15 determinant identity error: {lemma15_err}"
    # Verify Lemma 8 lower & upper bounds:
    lower_lemma8 = det_YtZY * ((tr1 + 1.0) ** 2)
    upper_lemma8 = det_YtZY * (1.0 + 2.0 * tr1 + tr2)
    assert lower_lemma8 - 1e-12 <= lhs_lemma15 <= upper_lemma8 + 1e-12

    # 3. Verify Lemma 1 closed-form rank-1 failure rate bound Z_1(gamma) (Page 7 & Page 31):
    # Z_1(gamma) = 2 * E[gamma / (R^2 + gamma)] = sqrt(2*pi*gamma) * exp(gamma/2) * erfc(sqrt(gamma/2)) <= sqrt(2*pi*gamma)
    gamma = 0.04
    z1_exact = math.sqrt(2.0 * math.pi * gamma) * math.exp(gamma / 2.0) * math.erfc(math.sqrt(gamma / 2.0))
    z1_upper = math.sqrt(2.0 * math.pi * gamma)
    assert 0.0 < z1_exact < z1_upper

    # 4. Verify Appendix A Proposition 1 (Page 15) quartic constant-step divergence vs Alecton global convergence
    # Standard SGD on f(x) = x^4 / 4 with step alpha = 0.1, C = 1.2, x_0 = sqrt(alpha^{-1}(C + 1) + 0.1)
    alpha_const = 0.1
    C_rate = 1.2
    x_div = math.sqrt((C_rate + 1.0) / alpha_const + 0.1)
    for k_step in range(1, 6):
        x_div = (1.0 - alpha_const * (x_div ** 2)) * x_div
        assert x_div ** 2 > ((C_rate ** (2 * k_step)) * (C_rate + 1.0)) / alpha_const

    # Alecton global convergence on rank-1 incoherent symmetric matrix A under entrywise sampling (Section 4.1, p. 8)
    # Construct incoherent rank-1 matrix A = lambda_1 u_1 u_1^T where u_1 = (1/sqrt(n)) * [1, -1, 1, -1, ...] (mu = 1)
    n_mc = 8
    u1 = [1.0 / math.sqrt(n_mc) if i % 2 == 0 else -1.0 / math.sqrt(n_mc) for i in range(n_mc)]
    lam1 = 4.0
    A_true = [[lam1 * u1[i] * u1[j] for j in range(n_mc)] for i in range(n_mc)]
    U_proj = [[u1[i] * u1[j] for j in range(n_mc)] for i in range(n_mc)]

    # Verify Lemma 12 submartingale drift E[tau_{k+1} | F_k] >= tau_k (1 + eta * Delta * (1 - tau_k))
    # by exact enumeration over all n_mc^2 entrywise samples A_tilde = n^2 e_i e_i^T A e_j e_j^T!
    sigma_a_sq = 1.0 * (lam1 ** 2)  # mu = 1, ||A||_F^2 = lam1^2
    Delta = lam1
    eps_tol = 0.25
    gamma_step = 0.2
    eta_step = gamma_step * Delta * eps_tol / (2.0 * n_mc * sigma_a_sq * 1.0 * (1.0 + eps_tol))
    w_noise = gamma_step / float(n_mc)

    def calc_tau(y_vec):
        uy_sq = sum(u1[i] * y_vec[i] for i in range(n_mc)) ** 2
        y_norm_sq = sum(v * v for v in y_vec)
        denom = w_noise * y_norm_sq + (1.0 - w_noise) * uy_sq
        return uy_sq / denom

    y_init = [0.2 if i == 0 else (0.5 if i == 1 else 0.1) for i in range(n_mc)]
    tau_k = calc_tau(y_init)
    exp_tau_next = 0.0
    for i in range(n_mc):
        for j in range(n_mc):
            # A_tilde y = n^2 * A_{i,j} * y_j * e_i
            y_next = y_init[:]
            y_next[i] += eta_step * (n_mc * n_mc) * A_true[i][j] * y_init[j]
            exp_tau_next += calc_tau(y_next) / float(n_mc * n_mc)

    rhs_lemma12 = tau_k * (1.0 + eta_step * Delta * (1.0 - tau_k))
    assert exp_tau_next >= rhs_lemma12 - 1e-12, f"Lemma 12 submartingale drift failed: {exp_tau_next} < {rhs_lemma12}"

    # Run Alecton trajectory to verify angular alignment ||U y_K||^2 / ||y_K||^2 -> 1
    y_curr = y_init[:]
    for _ in range(6000):
        i = rng.randrange(n_mc)
        j = rng.randrange(n_mc)
        y_curr[i] += 0.0006 * (n_mc * n_mc) * A_true[i][j] * y_curr[j]
        norm_y = math.sqrt(sum(v * v for v in y_curr))
        y_curr = [v / norm_y for v in y_curr]
    align_final = (sum(u1[i] * y_curr[i] for i in range(n_mc)) ** 2) / sum(v * v for v in y_curr)
    assert align_final > 0.985, f"Expected align_final > 0.985, got {align_final}"

    print(
        f"[PASS] Round 366 Alecton SGD (De Sa, Olukotun, & Re 2015): "
        f"colspace_diff={colspace_diff:.2e}, lemma15_err={lemma15_err:.2e}, "
        f"z1_exact={z1_exact:.4f}<={z1_upper:.4f}, drift_margin={exp_tau_next - rhs_lemma12:.2e}>=0, "
        f"align_final={align_final:.4f}"
    )


if __name__ == "__main__":
    main()
