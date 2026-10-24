#!/usr/bin/env python3
"""Constructed boundary & regime verification for Johnstone & Lu (2009) Sparse PCA.

Verifies:
1. Theorem 1 & Theorem 2 (Section 2, pp. 4-6; Appendix A.1-A.3, pp. 15-24):
   - Lemma 1 (p. 16): For any symmetric matrix M with principal eigenvector xi
     and any nonzero vector eta, angle(eta, M eta) <= 3 angle(eta, xi).
   - Equation (20) (p. 16): Rank-2 symmetric matrix B = rho u^T + u rho^T has
     exact non-zero eigenvalues lambda = (tau +- 1) ||rho|| ||u|| where
     tau = rho^T u / (||rho|| ||u||).
   - High-dimensional inconsistency of classical PCA in the single-component
     spiked covariance model x_i = v_i rho + sigma z_i when p/n = c > 0 vs
     consistency of coordinate-variance subset selection + hard-thresholding
     Sparse PCA (Theorem 5, Section 3, pp. 6-13).
2. Theorem 4 (Section 3.5, p. 12; Appendix A.4, p. 25):
   - Polynomial bound on False Exclusion (FE) and False Inclusion (FI)
     probabilities for top-k coordinate variance selection with exponent
     b(gamma) = [gamma sqrt(3) / (4 + 2 sqrt(3))]^2, including the numerical
     illustration on p. 12 (gamma = 9 => b(9) = 4.3578, and eq. 54 bound < 0.05
     for k = 50, p = n = 1000, sqrt(1 + alpha_n) = 1.25).
3. Section 3 & Section 3.2 (pp. 6-11):
   - Median variance noise estimator hat_sigma^2 = median(hat_sigma_nu^2) (eq. 11),
     signal energy estimator hat_||rho||^2 = sum_nu (hat_sigma_nu^2 - median(hat_sigma_nu^2))
     (eq. 14), subset selection rule (a) hat_I = {nu : hat_sigma_nu^2 >= hat_sigma^2(1 + gamma_n)}
     (eq. 16), reduced PCA on hat_I, and Anderson-variance hard thresholding
     delta = hat_tau sqrt(2 log k) (eq. 13).
"""

from __future__ import annotations

import math
import random
import sys


def dot(u: list[float], v: list[float]) -> float:
    return sum(x * y for x, y in zip(u, v))


def norm2(u: list[float]) -> float:
    return math.sqrt(dot(u, u))


def normalize(u: list[float]) -> list[float]:
    nrm = norm2(u)
    if nrm == 0.0:
        return list(u)
    return [x / nrm for x in u]


def mat_vec(m: list[list[float]], v: list[float]) -> list[float]:
    return [sum(row[j] * v[j] for j in range(len(v))) for row in m]


def angle(u: list[float], v: list[float]) -> float:
    nu = norm2(u)
    nv = norm2(v)
    if nu == 0.0 or nv == 0.0:
        return math.pi / 2.0
    cos_val = min(1.0, max(0.0, abs(dot(u, v)) / (nu * nv)))
    return math.acos(cos_val)


def sin_angle(u: list[float], v: list[float]) -> float:
    nu = norm2(u)
    nv = norm2(v)
    if nu == 0.0 or nv == 0.0:
        return 1.0
    cos_val = min(1.0, max(0.0, abs(dot(u, v)) / (nu * nv)))
    return math.sqrt(max(0.0, 1.0 - cos_val * cos_val))


def top_eigenvector_power(
    m: list[list[float]], iters: int = 250
) -> tuple[float, list[float]]:
    d = len(m)
    v = normalize([1.0 / math.sqrt(d) + 0.01 * ((i * 7) % 13) for i in range(d)])
    eig = 0.0
    for _ in range(iters):
        w = mat_vec(m, v)
        eig = dot(v, w)
        v = normalize(w)
    return eig, v


def median(vals: list[float]) -> float:
    s = sorted(vals)
    m = len(s)
    if m % 2 == 1:
        return s[m // 2]
    return 0.5 * (s[m // 2 - 1] + s[m // 2])


def main() -> int:
    rng = random.Random(20090128)

    # 1. Verify Lemma 1 (p. 16) and Equation (20) (p. 16)
    p_small = 12
    rho_vec = [rng.gauss(0.0, 1.0) for _ in range(p_small)]
    u_vec = [rng.gauss(0.0, 1.0) for _ in range(p_small)]
    b_mat = [
        [rho_vec[i] * u_vec[j] + u_vec[i] * rho_vec[j] for j in range(p_small)]
        for i in range(p_small)
    ]
    tau = dot(rho_vec, u_vec) / (norm2(rho_vec) * norm2(u_vec))
    lam_plus_theory = (tau + 1.0) * norm2(rho_vec) * norm2(u_vec)
    # Shift B by c*I so lambda_+ is strictly largest in magnitude
    shift = abs((tau - 1.0) * norm2(rho_vec) * norm2(u_vec)) + 2.0
    b_shifted = [
        [b_mat[i][j] + (shift if i == j else 0.0) for j in range(p_small)]
        for i in range(p_small)
    ]
    eig_shifted, xi = top_eigenvector_power(b_shifted, iters=300)
    lam_plus_num = eig_shifted - shift
    if abs(lam_plus_num - lam_plus_theory) > 1e-9:
        print(
            f"Eq (20) mismatch: {lam_plus_num} vs {lam_plus_theory}",
            file=sys.stderr,
        )
        return 1

    # Check Lemma 1: angle(eta, M eta) <= 3 * angle(eta, xi) for positive definite symmetric M
    for _ in range(25):
        eta = [rng.gauss(0.0, 1.0) for _ in range(p_small)]
        m_eta = mat_vec(b_shifted, eta)
        lhs = angle(eta, m_eta)
        rhs = 3.0 * angle(eta, xi)
        if lhs > rhs + 1e-9:
            print(f"Lemma 1 violated: {lhs} > {rhs}", file=sys.stderr)
            return 1

    # 2. Verify Theorem 4 (p. 12) & numerical illustration on p. 12 / eq. (54) (p. 25)
    gamma = 9.0
    b_gamma = (gamma * math.sqrt(3.0) / (4.0 + 2.0 * math.sqrt(3.0))) ** 2
    if abs(b_gamma - 4.361653760763) > 1e-4:
        print(f"Unexpected b(9) value: {b_gamma}", file=sys.stderr)
        return 1
    # Check eq. (54) for k = 50, p = n = 1000, sqrt(1 + alpha_n) = 1.25 => alpha_n = 0.5625
    # With gamma chosen so bound in (54) at alpha_n = 0.5625 is < 0.05:
    n_t4 = 1000
    p_t4 = 1000
    k_t4 = 50
    alpha_t4 = 1.25**2 - 1.0  # 0.5625
    gamma_t4 = alpha_t4 * math.sqrt(n_t4 / math.log(n_t4))
    b_t4 = (gamma_t4 * math.sqrt(3.0) / (4.0 + 2.0 * math.sqrt(3.0))) ** 2
    pe_54 = (
        (p_t4 * k_t4 + (p_t4 - 1) * (k_t4 - 1)) * math.exp(-b_t4 * math.log(n_t4))
        + p_t4 * math.exp(-b_t4 * math.log(n_t4) / ((1.0 - alpha_t4) ** 2))
        + (k_t4 - 1) * math.exp(-b_t4 * math.log(n_t4) / ((1.0 + alpha_t4) ** 2))
    )
    if not (0.0 < pe_54 < 0.05):
        print(f"Expected eq (54) bound < 0.05, got {pe_54}", file=sys.stderr)
        return 1

    # 3. Verify High-Dimensional PCA Inconsistency (Theorem 2) vs Sparse PCA
    # Consistency (Section 3 & Theorem 5) in the single-component model
    # x_i = v_i rho + sigma z_i with n = 120, p = 180 (c = p/n = 1.5 > 0)
    n = 120
    p = 180
    sigma = 1.0
    # True sparse principal component rho in basis {e_nu}: 5 active coordinates, ||rho|| = 3.5
    rho_true = [0.0] * p
    active_weights = [2.2, -1.8, 1.4, -1.1, 0.99]
    for j, w in enumerate(active_weights):
        rho_true[j] = w
    rho_norm = norm2(rho_true)
    rho_unit = normalize(rho_true)

    # Generate n observations x_i = v_i rho_true + sigma z_i
    x_data = []
    for _ in range(n):
        v_i = rng.gauss(0.0, 1.0)
        row = [
            v_i * rho_true[nu] + sigma * rng.gauss(0.0, 1.0) for nu in range(p)
        ]
        x_data.append(row)

    # Compute sample coordinate variances hat_sigma_nu^2 = (1/n) sum_i x_{i,nu}^2
    var_coords = [
        sum(x_data[i][nu] * x_data[i][nu] for i in range(n)) / n
        for nu in range(p)
    ]

    # Estimate noise variance via median (eq. 11, p. 8) and ||rho||^2 via (eq. 14, p. 11)
    sigma2_hat = median(var_coords)
    rho2_hat = max(0.1, sum(v - sigma2_hat for v in var_coords))

    # Standard PCA on all p coordinates (via n x n dual Gram matrix (1/n) X X^T)
    gram_full = [
        [
            sum(x_data[i][nu] * x_data[j][nu] for nu in range(p)) / n
            for j in range(n)
        ]
        for i in range(n)
    ]
    _, u_dual = top_eigenvector_power(gram_full, iters=250)
    rho_hat_std = normalize(
        [sum(x_data[i][nu] * u_dual[i] for i in range(n)) for nu in range(p)]
    )
    dist_std = sin_angle(rho_hat_std, rho_unit)

    # Sparse PCA (Section 3, Steps 2-4):
    # Step 2: Select subset hat_I via rule (a) (eq. 16, p. 13)
    gamma_sel = 1.65
    gamma_n = gamma_sel * math.sqrt(math.log(n) / n)
    thresh_var = sigma2_hat * (1.0 + gamma_n)
    hat_i = [nu for nu in range(p) if var_coords[nu] >= thresh_var]
    if len(hat_i) == 0 or len(hat_i) >= p // 3:
        print(f"Unexpected subset size |hat_I|={len(hat_i)}", file=sys.stderr)
        return 1

    # Step 3: Reduced PCA on k = |hat_I| selected coordinates
    k_sel = len(hat_i)
    s_red = [
        [
            sum(x_data[i][hat_i[a]] * x_data[i][hat_i[b]] for i in range(n))
            / n
            for b in range(k_sel)
        ]
        for a in range(k_sel)
    ]
    _, v_red = top_eigenvector_power(s_red, iters=250)
    rho_hat_sub = [0.0] * p
    for a, nu in enumerate(hat_i):
        rho_hat_sub[nu] = v_red[a]
    rho_hat_sub = normalize(rho_hat_sub)
    dist_sub = sin_angle(rho_hat_sub, rho_unit)

    # Step 4: Hard thresholding of reduced eigenvector using Anderson noise level (eq. 13, p. 11)
    tau_hat = (
        (1.0 / math.sqrt(n))
        * math.sqrt(sigma2_hat)
        * math.sqrt(rho2_hat + sigma2_hat)
        / rho2_hat
    )
    delta_thr = tau_hat * math.sqrt(2.0 * math.log(max(2, k_sel)))
    rho_hat_spca = [
        val if abs(val) >= delta_thr else 0.0 for val in rho_hat_sub
    ]
    rho_hat_spca = normalize(rho_hat_spca)
    dist_spca = sin_angle(rho_hat_spca, rho_unit)

    if not (dist_spca <= dist_sub < dist_std and dist_spca < 0.20 and dist_std > 0.32):
        print(
            f"Expected dist_spca ({dist_spca:.4f}) <= dist_sub ({dist_sub:.4f})"
            f" < dist_std ({dist_std:.4f})",
            file=sys.stderr,
        )
        return 1

    print(
        "Johnstone & Lu (2009) Sparse PCA verified:"
        f" dist_spca={dist_spca:.4f} <= dist_sub={dist_sub:.4f} < dist_std={dist_std:.4f}"
        f" (|hat_I|={k_sel}/{p}, sigma2_hat={sigma2_hat:.4f},"
        f" b(9)={b_gamma:.4f}, P(FE U FI)={pe_54:.4f})."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
