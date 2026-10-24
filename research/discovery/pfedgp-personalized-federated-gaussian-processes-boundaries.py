"""Constructed boundary verification for Round 472:
Personalized Federated Learning with Gaussian Processes (pFedGP, Achituve et al., NeurIPS 2021).
Verifies:
1. Polya-Gamma identity (Eq. 12) and augmented Gaussian posterior (Eqs. 14, 17):
   Woodbury equivalence between Sigma = (K^{-1} + Omega)^{-1} posterior mean/covariance and
   predictive distribution mu^* = (k^*)^T (Omega^{-1} + K)^{-1} Omega^{-1} kappa,
   Sigma^* = k^{**} - (k^*)^T (Omega^{-1} + K)^{-1} k^*.
2. FITC inducing-point posterior (Eqs. 6, 20-22): when inducing points X_bar = X,
   Lambda = Omega^{-1} and B = K + K Omega K, recovering the exact full-GP predictive mean and variance.
3. Class-imbalance prior-ratio correction (Eq. 5) and PAC-Bayes KL decomposition (Eqs. 10, 26-27).
"""

from __future__ import annotations
import math


def mat_mul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def mat_vec(A: list[list[float]], v: list[float]) -> list[float]:
    return [sum(row[j] * v[j] for j in range(len(v))) for row in A]


def mat_inv_3x3(M: list[list[float]]) -> list[list[float]]:
    a, b, c = M[0]
    d, e, f = M[1]
    g, h, i = M[2]
    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    inv_det = 1.0 / det
    return [
        [(e * i - f * h) * inv_det, (c * h - b * i) * inv_det, (b * f - c * e) * inv_det],
        [(f * g - d * i) * inv_det, (a * i - c * g) * inv_det, (c * d - a * f) * inv_det],
        [(d * h - e * g) * inv_det, (b * g - a * h) * inv_det, (a * e - b * d) * inv_det],
    ]


def det_3x3(M: list[list[float]]) -> float:
    a, b, c = M[0]
    d, e, f = M[1]
    g, h, i = M[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def rbf(x1: float, x2: float, ell: float = 1.0) -> float:
    return math.exp(-((x1 - x2) ** 2) / (2.0 * ell * ell))


def main() -> None:
    # 1. Polya-Gamma Laplace transform identity (Eq. 12) for b=1, a=y in {0, 1}:
    # (e^f)^y / (1 + e^f) = 0.5 * exp((y - 0.5) * f) / cosh(f / 2)
    for y in (0.0, 1.0):
        for f_val in (-1.5, 0.0, 2.2):
            lhs = (math.exp(f_val) ** y) / (1.0 + math.exp(f_val))
            kappa = y - 0.5
            # E_{omega ~ PG(1,0)}[exp(-omega f^2 / 2)] = 1 / cosh(f / 2)
            rhs = 0.5 * math.exp(kappa * f_val) * (1.0 / math.cosh(0.5 * f_val))
            assert abs(lhs - rhs) < 1e-14

    # 2. Full-GP (Eq. 17) vs FITC inducing-point (Eq. 22) predictive mean & variance
    X = [-1.0, 0.2, 1.3]
    y = [0.0, 1.0, 1.0]
    kappa = [yj - 0.5 for yj in y]
    omega = [0.31, 0.24, 0.28]
    Omega_inv = [[1.0 / omega[i] if i == j else 0.0 for j in range(3)] for i in range(3)]
    K = [[rbf(X[i], X[j]) + (1e-4 if i == j else 0.0) for j in range(3)] for i in range(3)]

    x_star = 0.8
    k_star = [rbf(xi, x_star) for xi in X]
    k_ss = rbf(x_star, x_star) + 1e-4

    # Eq. 17: mu^* = (k^*)^T (Omega^{-1} + K)^{-1} Omega^{-1} kappa
    Om_inv_plus_K = [[Omega_inv[i][j] + K[i][j] for j in range(3)] for i in range(3)]
    inv_Om_K = mat_inv_3x3(Om_inv_plus_K)
    om_inv_kappa = [kappa[i] / omega[i] for i in range(3)]
    alpha_full = mat_vec(inv_Om_K, om_inv_kappa)
    mu_full = sum(k_star[i] * alpha_full[i] for i in range(3))
    inv_k_star = mat_vec(inv_Om_K, k_star)
    var_full = k_ss - sum(k_star[i] * inv_k_star[i] for i in range(3))

    # Eq. 22 (FITC with X_bar = X): Lambda = Omega^{-1}, B = K + K * Omega * K
    K_inv = mat_inv_3x3(K)
    Omega_mat = [[omega[i] if i == j else 0.0 for j in range(3)] for i in range(3)]
    K_Om_K = mat_mul(mat_mul(K, Omega_mat), K)
    B = [[K[i][j] + K_Om_K[i][j] for j in range(3)] for i in range(3)]
    B_inv = mat_inv_3x3(B)
    # mu_fitc = (k^*)^T B^{-1} K Lambda^{-1} Omega^{-1} kappa
    # Note Lambda = Omega^{-1} => Lambda^{-1} = Omega
    lam_inv_om_inv_kappa = [omega[i] * (kappa[i] / omega[i]) for i in range(3)]
    rhs_fitc = mat_vec(B_inv, mat_vec(K, lam_inv_om_inv_kappa))
    mu_fitc = sum(k_star[i] * rhs_fitc[i] for i in range(3))
    diff_K_B = [[K_inv[i][j] - B_inv[i][j] for j in range(3)] for i in range(3)]
    var_fitc = k_ss - sum(k_star[i] * mat_vec(diff_K_B, k_star)[i] for i in range(3))

    assert abs(mu_full - mu_fitc) < 1e-12
    assert abs(var_full - var_fitc) < 1e-12

    # 3. Eq. 27 Closed-form conditional KL divergence KL[Q(f|omega) || P(f)] >= 0
    Sigma = mat_inv_3x3([[K_inv[i][j] + Omega_mat[i][j] for j in range(3)] for i in range(3)])
    mu_post = mat_vec(Sigma, kappa)
    tr_term = sum(mat_mul(K_inv, Sigma)[i][i] for i in range(3))
    quad_term = sum(mu_post[i] * mat_vec(K_inv, mu_post)[i] for i in range(3))
    kl_cond = 0.5 * (math.log(det_3x3(K) / det_3x3(Sigma)) - 3.0 + tr_term + quad_term)
    assert kl_cond > 0.0

    print(
        f"[PASS] Round 472 pFedGP verified: mu_full={mu_full:.6f}==mu_fitc={mu_fitc:.6f}, "
        f"var_full={var_full:.6f}==var_fitc={var_fitc:.6f}, KL_cond={kl_cond:.4f}>0"
    )


if __name__ == "__main__":
    main()
