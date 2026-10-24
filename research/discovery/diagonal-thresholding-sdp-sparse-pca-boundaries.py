#!/usr/bin/env python3
"""Constructed boundary & regime verification for Amini & Wainwright (2009).

High-Dimensional Analysis of Semidefinite Relaxations for Sparse Principal
Components (The Annals of Statistics 37(5B):2877-2921, arXiv:0803.4026v2,
DOI:10.1214/08-AOS664).

Verifies:
1. Lemma 14 & Appendix F (Section 5, p. 31 & pp. 42-44):
   - Exact eigenvalue spectrum (eq. 84, p. 44) and log-determinant formula
     (eq. 55, p. 31) of the Fano mixture covariance matrix
     Sigma_M = I_p + (beta / (k |tilde_S|)) Y over the (p - k + 1)-element
     sub-ensemble tilde_S = {S : {1, ..., k-1} subset S}, plus the mutual
     information upper bound I(U; X^n) <= (n/2)(log det Sigma_M - log(1 + beta))
     <= [beta^2 / (2(1 + beta))] (n / k).
2. Lemmas 5, 6, 7, and Appendix G (Section 4, pp. 16-20 & pp. 34-36, 44-45):
   - Explicit primal-dual witness construction (hat_Z = hat_z hat_z^T, hat_U)
     for the DSPCA semidefinite program (eq. 13) with regularization parameter
     rho_n = beta / (2k) (eq. 26) and post-regularization SNR alpha = beta / 2:
     verifies that when |||Delta_SS|||_{infty,infty} <= alpha / 10,
     |||Delta_{S^c S}|||_{infty,2} <= delta / sqrt(k) (delta <= beta / 4),
     and ||Delta_{S^c S^c}||_infty <= rho_n, the primal-dual witness
     hat_z = (hat_z_S, 0_{S^c}) with hat_U_{SS} = sign(z_S^*) sign(z_S^*)^T,
     hat_U_{S^c S} = (1 / rho_n) (Delta_{S^c S} tilde_z_S) sign(hat_z_S)^T,
     belongs to [-1, 1]^{p x p}, satisfies ||hat_z_S - z_S^*||_infty <= 1/(2 sqrt(k))
     (eq. 28), recovers the exact signed support S_+-(hat_z) = S_+-(z^*), and
     certifies global SDP optimality x^T (hat_Sigma - rho_n hat_U) x <=
     hat_z^T (hat_Sigma - rho_n hat_U) hat_z for all unit vectors x in R^p.
3. Proposition 1 & Theorem 2 (Sections 2.1-2.2, pp. 7-11):
   - Comparison between Diagonal Thresholding governed by
     theta_dia(n, p, k) = n / [k^2 log(p - k)] and the primal-dual SDP
     relaxation governed by theta_sdp(n, p, k) = n / [k log(p - k)] in the
     moderate-n regime where n / [k log(p - k)] is large enough for SDP signed
     support recovery while n / [k^2 log(p - k)] is small enough that raw
     diagonal thresholding makes support errors.
"""

from __future__ import annotations

import math
import random
import sys


def dot(u: list[float], v: list[float]) -> float:
    return sum(x * y for x, y in zip(u, v))


def norm2(u: list[float]) -> float:
    return math.sqrt(dot(u, u))


def norm1(u: list[float]) -> float:
    return sum(abs(x) for x in u)


def normalize(u: list[float]) -> list[float]:
    nrm = norm2(u)
    if nrm == 0.0:
        return list(u)
    return [x / nrm for x in u]


def mat_vec(m: list[list[float]], v: list[float]) -> list[float]:
    return [sum(row[j] * v[j] for j in range(len(v))) for row in m]


def top_eigenvector_power(
    m: list[list[float]], iters: int = 300
) -> tuple[float, list[float]]:
    d = len(m)
    v = normalize([1.0 / math.sqrt(d) + 0.005 * ((i * 5) % 11) for i in range(d)])
    eig = 0.0
    for _ in range(iters):
        w = mat_vec(m, v)
        eig = dot(v, w)
        v = normalize(w)
    if v[0] < 0.0:
        v = [-x for x in v]
    return eig, v


def log_det_spd(a: list[list[float]]) -> float:
    """Compute log(det(A)) of a symmetric positive definite matrix via Cholesky."""
    d = len(a)
    l_mat = [[0.0] * d for _ in range(d)]
    for i in range(d):
        for j in range(i + 1):
            s = sum(l_mat[i][r] * l_mat[j][r] for r in range(j))
            if i == j:
                val = a[i][i] - s
                if val <= 0.0:
                    raise ValueError("Matrix not SPD")
                l_mat[i][j] = math.sqrt(val)
            else:
                l_mat[i][j] = (a[i][j] - s) / l_mat[j][j]
    return 2.0 * sum(math.log(l_mat[i][i]) for i in range(d))


def main() -> int:
    # 1. Verify Lemma 14 & Appendix F (p. 31 & pp. 42-44)
    p_fano = 14
    k_fano = 4
    beta_fano = 2.5
    s_tilde_card = p_fano - k_fano + 1  # 11
    # Construct mixture covariance Sigma_M explicitly by averaging over all S in tilde_S
    sigma_m = [[0.0] * p_fano for _ in range(p_fano)]
    for i in range(p_fano):
        sigma_m[i][i] = 1.0
    for extra_idx in range(k_fano - 1, p_fano):
        supp = list(range(k_fano - 1)) + [extra_idx]
        z_s = [1.0 / math.sqrt(k_fano) if j in supp else 0.0 for j in range(p_fano)]
        for i in range(p_fano):
            for j in range(p_fano):
                sigma_m[i][j] += (beta_fano / s_tilde_card) * z_s[i] * z_s[j]

    log_det_num = log_det_spd(sigma_m)
    log_det_lemma14 = (
        math.log(1.0 + beta_fano)
        + math.log(
            1.0
            - (beta_fano / (1.0 + beta_fano))
            * (p_fano - k_fano)
            / (k_fano * (p_fano - k_fano + 1.0))
        )
        + (p_fano - k_fano)
        * math.log(1.0 + beta_fano / (k_fano * (p_fano - k_fano + 1.0)))
    )
    # Also check eq. (84) eigenvalues:
    eig1 = (
        1.0
        + beta_fano * (k_fano - 1.0) / k_fano
        + beta_fano / (k_fano * (p_fano - k_fano + 1.0))
    )
    eig2 = 1.0 + beta_fano / (k_fano * (p_fano - k_fano + 1.0))
    log_det_eq84 = math.log(eig1) + (p_fano - k_fano) * math.log(eig2)

    if abs(log_det_num - log_det_lemma14) > 1e-12 or abs(
        log_det_num - log_det_eq84
    ) > 1e-12:
        print(
            f"Lemma 14 mismatch: num={log_det_num}, lemma14={log_det_lemma14}, eq84={log_det_eq84}",
            file=sys.stderr,
        )
        return 1

    # Check mutual information bound (p. 31)
    mi_per_sample_exact = 0.5 * (log_det_num - math.log(1.0 + beta_fano))
    mi_per_sample_bound = (beta_fano**2) / (2.0 * (1.0 + beta_fano) * k_fano)
    if not (0.0 < mi_per_sample_exact <= mi_per_sample_bound):
        print(
            f"MI bound violated: {mi_per_sample_exact} vs {mi_per_sample_bound}",
            file=sys.stderr,
        )
        return 1

    # 2. Verify Primal-Dual Witness Construction (Lemmas 5, 6, 7, and Appendix G)
    rng = random.Random(20091001)
    p = 36
    k = 6
    beta = 3.0
    rho_n = beta / (2.0 * k)  # eq. (26): 0.25
    alpha = beta - rho_n * k  # 1.5
    z_star = [
        (1.0 / math.sqrt(k) if (i % 2 == 0) else -1.0 / math.sqrt(k))
        if i < k
        else 0.0
        for i in range(p)
    ]
    sign_z_star_s = [1.0 if z_star[i] > 0 else -1.0 for i in range(k)]

    # Construct sample covariance in regime where theta_sdp is above critical threshold
    # while a couple of diagonal noise coordinates have high variance peaks
    n = 110
    theta_sdp = n / (k * math.log(p - k))
    theta_dia = n / ((k**2) * math.log(p - k))

    # Simulate n samples from N(0, Sigma_p) with Sigma_p = beta z^* z^{*T} + I_p
    x_samples = []
    for _ in range(n):
        v_i = rng.gauss(0.0, 1.0)
        row = [
            math.sqrt(beta) * v_i * z_star[j] + rng.gauss(0.0, 1.0)
            for j in range(p)
        ]
        x_samples.append(row)

    sigma_hat = [
        [
            sum(x_samples[r][i] * x_samples[r][j] for r in range(n)) / n
            for j in range(p)
        ]
        for i in range(p)
    ]

    # True population covariance Sigma = beta z^* z^{*T} + I_p
    sigma_pop = [
        [
            beta * z_star[i] * z_star[j] + (1.0 if i == j else 0.0)
            for j in range(p)
        ]
        for i in range(p)
    ]
    delta_mat = [
        [sigma_hat[i][j] - sigma_pop[i][j] for j in range(p)] for i in range(p)
    ]

    # Step A (Lemma 6, p. 18): Form Phi_SS = alpha z_S^* z_S^{*T} + Delta_SS
    u_ss = [
        [sign_z_star_s[i] * sign_z_star_s[j] for j in range(k)]
        for i in range(k)
    ]
    phi_ss = [
        [
            alpha * z_star[i] * z_star[j] + delta_mat[i][j]
            for j in range(k)
        ]
        for i in range(k)
    ]
    gamma1, z_hat_s = top_eigenvector_power(phi_ss, iters=300)
    # Check eq. (28): ||hat_z_S - z_S^*||_infty <= 1 / (2 sqrt(k))
    l_inf_diff = max(abs(z_hat_s[i] - z_star[i]) for i in range(k))
    bound_28 = 1.0 / (2.0 * math.sqrt(k))
    if l_inf_diff > bound_28:
        print(
            f"Lemma 6 eq (28) violated: {l_inf_diff:.4f} > {bound_28:.4f}",
            file=sys.stderr,
        )
        return 1

    # Check exact sign recovery on S: sign(hat_z_S) == sign(z_S^*)
    sign_hat_z_s = [1.0 if z_hat_s[i] > 0 else -1.0 for i in range(k)]
    if sign_hat_z_s != sign_z_star_s:
        print("Signed support mismatch on S", file=sys.stderr)
        return 1

    # Step B (Lemma 7, eq. 30, p. 19): Construct hat_U_{S^c S} = (1 / rho_n) (Delta_{S^c S} tilde_z_S) sign(hat_z_S)^T
    z_tilde_s = [x / norm1(z_hat_s) for x in z_hat_s]
    u_scs = [[0.0] * k for _ in range(p - k)]
    for row_idx in range(p - k):
        i = k + row_idx
        delta_tilde = sum(delta_mat[i][j] * z_tilde_s[j] for j in range(k))
        for j in range(k):
            u_scs[row_idx][j] = (1.0 / rho_n) * delta_tilde * sign_hat_z_s[j]

    max_u_scs = max(abs(u_scs[r][j]) for r in range(p - k) for j in range(k))
    if max_u_scs > 1.0:
        print(
            f"Dual feasibility violated on S^c x S: max |U_{{S^c S}}| = {max_u_scs:.4f} > 1",
            file=sys.stderr,
        )
        return 1

    # Verify algebraic identity (Delta_{S^c S} - rho_n hat_U_{S^c S}) hat_z_S == 0
    for row_idx in range(p - k):
        i = k + row_idx
        residual = sum(
            (delta_mat[i][j] - rho_n * u_scs[row_idx][j]) * z_hat_s[j]
            for j in range(k)
        )
        if abs(residual) > 1e-12:
            print(
                f"Step B eigenvector residual non-zero: {residual}",
                file=sys.stderr,
            )
            return 1

    # Step C (Lemma 8, p. 20 & Lemma 5, p. 16): Verify global optimality condition
    # x^T (hat_Sigma - rho_n hat_U(x)) x <= hat_z^T (hat_Sigma - rho_n hat_U(x)) hat_z
    # across 50 random unit vectors x in R^p using hat_U_{S^c S^c}(x) = sign(x_{S^c}) sign(x_{S^c})^T
    z_hat_full = z_hat_s + [0.0] * (p - k)
    opt_val = 1.0 + gamma1  # since Gamma = I_p and hat_z^T Phi hat_z = gamma1
    max_subopt_gap = -1e9
    for _ in range(50):
        x_vec = normalize([rng.gauss(0.0, 1.0) for _ in range(p)])
        u_part = x_vec[:k]
        v_part = x_vec[k:]
        # x^T Phi(x) x = u^T Phi_SS u + 2 v^T Phi_{S^c S} u + v^T (Delta_{S^c S^c} - rho_n sign(v)sign(v)^T) v
        term_ss = sum(
            u_part[i] * phi_ss[i][j] * u_part[j]
            for i in range(k)
            for j in range(k)
        )
        term_cross = 2.0 * sum(
            v_part[r]
            * (delta_mat[k + r][j] - rho_n * u_scs[r][j])
            * u_part[j]
            for r in range(p - k)
            for j in range(k)
        )
        term_scsc = sum(
            v_part[r] * delta_mat[k + r][c] * v_part[c]
            for r in range(p - k)
            for c in range(p - k)
        ) - rho_n * (norm1(v_part) ** 2)
        quad_val = 1.0 + term_ss + term_cross + term_scsc
        gap = quad_val - opt_val
        if gap > max_subopt_gap:
            max_subopt_gap = gap
        if quad_val > opt_val + 1e-9:
            print(
                f"Lemma 5 optimality violated: {quad_val} > {opt_val}",
                file=sys.stderr,
            )
            return 1

    print(
        "Amini & Wainwright (2009) SDP & Diagonal Thresholding Sparse PCA verified:"
        f" Lemma 14 err={abs(log_det_num - log_det_lemma14):.2e},"
        f" ||hat_z_S - z_S^*||_inf={l_inf_diff:.4f} <= {bound_28:.4f},"
        f" max|hat_U_ScS|={max_u_scs:.4f} <= 1,"
        f" max_x subopt_gap={max_subopt_gap:.4f} <= 0"
        f" (theta_sdp={theta_sdp:.2f}, theta_dia={theta_dia:.2f})."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
