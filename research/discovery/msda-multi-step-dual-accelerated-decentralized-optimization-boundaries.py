"""Constructed boundary and numerical verification for Round 435:
MSDA and SSDA: Multi-Step Dual Accelerated Decentralized Optimization
(Kevin Scaman, Francis Bach, Sebastien Bubeck, Yin Tat Lee, & Laurent Massoulie 2017,
ICML 2017, PMLR 70:3027-3036, arXiv:1702.08704).
"""

from __future__ import annotations

import math


def mat_mul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def mat_vec(A: list[list[float]], v: list[float]) -> list[float]:
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def vec_norm(v: list[float]) -> float:
    return math.sqrt(sum(x * x for x in v))


def chebyshev_gossip_matrix(W: list[list[float]], lam_max: float, lam_min_pos: float, K: int) -> list[list[float]]:
    """Compute P_K(W) = I - T_K(c_2(I - c_1 W)) / T_K(c_2) via Algorithm 2 recursion."""
    n = len(W)
    gamma = lam_min_pos / lam_max
    c1 = 2.0 / (lam_max + lam_min_pos)
    c2 = (1.0 + gamma) / (1.0 - gamma)

    # For each standard basis vector e_j, run Algorithm 2 inner Chebyshev gossip
    cols: list[list[float]] = []
    for j in range(n):
        x0 = [1.0 if i == j else 0.0 for i in range(n)]
        mu0 = 1.0
        mu1 = c2
        Wx0 = mat_vec(W, x0)
        x1 = [x0[i] - c1 * Wx0[i] for i in range(n)]
        x_prev, x_curr = x0, x1
        mu_prev, mu_curr = mu0, mu1
        for _ in range(1, K):
            mu_next = 2.0 * c2 * mu_curr - mu_prev
            Wx_curr = mat_vec(W, x_curr)
            z = [x_curr[i] - c1 * Wx_curr[i] for i in range(n)]
            x_next = [
                2.0 * c2 * (mu_curr / mu_next) * z[i] - (mu_prev / mu_next) * x_prev[i]
                for i in range(n)
            ]
            x_prev, x_curr = x_curr, x_next
            mu_prev, mu_curr = mu_curr, mu_next
        cols.append([x0[i] - x_curr[i] for i in range(n)])
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def main() -> None:
    # 8-node cycle graph Laplacian W = I - A where A_{i, i+-1} = 0.5
    n = 8
    W = [[0.0] * n for _ in range(n)]
    for i in range(n):
        W[i][i] = 1.0
        W[i][(i - 1) % n] = -0.5
        W[i][(i + 1) % n] = -0.5

    # Eigenvalues of W on 8-cycle: 1 - cos(2*pi*k/n) for k=0..n-1
    eigs_W = sorted([1.0 - math.cos(2.0 * math.pi * k / n) for k in range(n)], reverse=True)
    lam_1 = eigs_W[0]          # 2.0
    lam_n_1 = eigs_W[n - 2]    # 1 - cos(pi/4) = 1 - sqrt(2)/2 ~ 0.292893
    gamma_W = lam_n_1 / lam_1  # ~ 0.146447
    K = int(math.floor(1.0 / math.sqrt(gamma_W)))  # K = 2

    P_K = chebyshev_gossip_matrix(W, lam_1, lam_n_1, K)
    # Check Ker(P_K) = Span(1): P_K * 1 == 0
    ones = [1.0] * n
    ker_err = vec_norm(mat_vec(P_K, ones))
    assert ker_err < 1e-14, f"P_K(W) 1 != 0: {ker_err}"

    # Compute eigenvalues of P_K(W) on Fourier modes of 8-cycle
    c1 = 2.0 / (lam_1 + lam_n_1)
    c2 = (1.0 + gamma_W) / (1.0 - gamma_W)
    tk_c2 = math.cosh(K * math.acosh(c2))
    eigs_PK = []
    for lam in eigs_W[:-1]:
        arg = max(-1.0, min(1.0, c2 * (1.0 - c1 * lam)))
        tk_arg = math.cos(K * math.acos(arg))
        eigs_PK.append(1.0 - tk_arg / tk_c2)
    gamma_PK = min(eigs_PK) / max(eigs_PK)
    inv_sqrt_gamma_PK = 1.0 / math.sqrt(gamma_PK)
    assert gamma_PK > gamma_W and inv_sqrt_gamma_PK <= 2.0

    # Run MSDA (Algorithm 2) on strongly convex quadratics f_i(theta_i) = 0.5 * a_i * (theta_i - b_i)^2
    # Conjugate grad: grad f_i^*(y_i) = y_i / a_i + b_i
    a = [1.0 + 0.2 * i for i in range(n)]
    b = [(-1.0) ** i * (i + 1.0) for i in range(n)]
    alpha_sc = min(a)
    beta_sm = max(a)
    kappa_l = beta_sm / alpha_sc
    theta_star = sum(a[i] * b[i] for i in range(n)) / sum(a)

    # Dual smoothness R^2 = lam_1(P_K) / alpha_sc, dual strong convexity r^2 = lam_{n-1}(P_K) / beta_sm
    lam_1_PK = max(eigs_PK)
    lam_n1_PK = min(eigs_PK)
    eta = alpha_sc / lam_1_PK
    kappa_dual = (lam_1_PK / lam_n1_PK) * kappa_l
    mu_acc = (math.sqrt(kappa_dual) - 1.0) / (math.sqrt(kappa_dual) + 1.0)

    x_t = [0.0] * n
    y_t = [0.0] * n
    for _ in range(180):
        grad_conj = [y_t[i] / a[i] + b[i] for i in range(n)]
        gossip_step = mat_vec(P_K, grad_conj)
        x_next = [y_t[i] - eta * gossip_step[i] for i in range(n)]
        y_next = [x_next[i] + mu_acc * (x_next[i] - x_t[i]) for i in range(n)]
        x_t, y_t = x_next, y_next

    primal_theta = [y_t[i] / a[i] + b[i] for i in range(n)]
    msda_err = vec_norm([primal_theta[i] - theta_star for i in range(n)])
    assert msda_err < 1e-10, f"MSDA primal error too high: {msda_err}"

    print(
        f"[PASS] Round 435 MSDA (Scaman et al. 2017): gamma_W={gamma_W:.4f} -> gamma_PK={gamma_PK:.4f} "
        f"(1/sqrt(gamma_PK)={inv_sqrt_gamma_PK:.4f} <= 2), msda_err={msda_err:.2e}"
    )


if __name__ == "__main__":
    main()
