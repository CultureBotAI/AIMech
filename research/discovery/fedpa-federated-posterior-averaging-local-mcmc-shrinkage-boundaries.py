#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 412:
FedPA: Federated Posterior Averaging via Local MCMC and Shrinkage Covariance (Al-Shedivat et al. 2021).
"""


def mat_vec(M: list[list[float]], v: list[float]) -> list[float]:
    return [sum(Mij * vj for Mij, vj in zip(row, v)) for row in M]


def dot(u: list[float], v: list[float]) -> float:
    return sum(ui * vi for ui, vi in zip(u, v))


def inv_2x2(M: list[list[float]]) -> list[list[float]]:
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    assert abs(det) > 1e-12
    return [[M[1][1] / det, -M[0][1] / det], [-M[1][0] / det, M[0][0] / det]]


def fedpa_dp_delta(x0: list[float], samples: list[list[float]], rho: float) -> list[float]:
    """Algorithm 2 (Appendix C.2) online O(ell^2 d) Sherman-Morrison dynamic program for
    Sigma_hat_ell^{-1} (x0 - mean(samples)).
    """
    ell = len(samples)
    d = len(x0)
    assert ell >= 2

    # Compute running means bar_x[t] for t = 1..ell (0-indexed: t_idx = 0..ell-1)
    means: list[list[float]] = []
    running = [0.0] * d
    for idx, s in enumerate(samples):
        t = idx + 1
        running = [running[j] + (s[j] - running[j]) / t for j in range(d)]
        means.append(list(running))

    # u_t = x_t - bar_x_{t-1} for t = 2..ell, gamma_t = rho * (t - 1) / t
    # Maintain v_t = tilde_Sigma_{t-1}^{-1} u_t for t = 2..ell
    u_list: list[list[float]] = []
    v_list: list[list[float]] = []
    gamma_list: list[float] = []
    denom_list: list[float] = []

    for t in range(2, ell + 1):
        ut = [samples[t - 1][j] - means[t - 2][j] for j in range(d)]
        gamma_t = rho * (t - 1.0) / t
        # Compute tilde_Sigma_{t-1}^{-1} ut using previous rank-1 updates k = 2..t-1
        vt = list(ut)
        for k_idx in range(len(u_list)):
            gk = gamma_list[k_idx]
            uk = u_list[k_idx]
            vk = v_list[k_idx]
            dk = denom_list[k_idx]
            coeff = (gk * dot(uk, vt)) / dk
            vt = [vt[j] - coeff * vk[j] for j in range(d)]
        denom_t = 1.0 + gamma_t * dot(ut, vt)
        u_list.append(ut)
        v_list.append(vt)
        gamma_list.append(gamma_t)
        denom_list.append(denom_t)

    # Now compute tilde_Sigma_ell^{-1} (x0 - bar_x_ell)
    diff = [x0[j] - means[-1][j] for j in range(d)]
    res = list(diff)
    for k_idx in range(len(u_list)):
        gk = gamma_list[k_idx]
        uk = u_list[k_idx]
        vk = v_list[k_idx]
        dk = denom_list[k_idx]
        coeff = (gk * dot(uk, res)) / dk
        res = [res[j] - coeff * vk[j] for j in range(d)]

    # Multiply by 1 / rho_ell = 1 + (ell - 1) * rho
    scale = 1.0 + (ell - 1.0) * rho
    return [scale * r for r in res]


def main() -> None:
    # 1. Verify Theorem 3 & Algorithm 2 DP against exact d x d shrinkage covariance inverse
    x0 = [1.5, -0.8]
    samples = [
        [0.2, 1.1],
        [0.4, 0.9],
        [-0.1, 1.3],
        [0.5, 0.7],
        [0.0, 1.2],
    ]
    rho = 0.4
    ell = len(samples)
    rho_ell = 1.0 / (1.0 + (ell - 1.0) * rho)
    mean_x = [sum(s[j] for s in samples) / ell for j in range(2)]

    # Sample covariance S_hat
    S_hat = [[0.0, 0.0], [0.0, 0.0]]
    for s in samples:
        for i in range(2):
            for j in range(2):
                S_hat[i][j] += (s[i] - mean_x[i]) * (s[j] - mean_x[j]) / (ell - 1.0)

    Sigma_hat = [
        [rho_ell * (1.0 if i == j else 0.0) + (1.0 - rho_ell) * S_hat[i][j] for j in range(2)]
        for i in range(2)
    ]
    Sigma_hat_inv = inv_2x2(Sigma_hat)
    diff = [x0[j] - mean_x[j] for j in range(2)]
    delta_exact = mat_vec(Sigma_hat_inv, diff)
    delta_dp = fedpa_dp_delta(x0, samples, rho)

    dp_err = max(abs(a - b) for a, b in zip(delta_exact, delta_dp))
    assert dp_err < 1e-12, f"DP mismatch: {dp_err}"

    # 2. Verify Proposition 1 & 2: Posterior mode vs FedAvg mean under anisotropic client precisions
    P1 = [[10.0, 0.0], [0.0, 1.0]]
    mu1 = [1.0, -2.0]
    P2 = [[1.0, 0.0], [0.0, 10.0]]
    mu2 = [-2.0, 1.0]
    # True posterior mode: (P1 + P2)^{-1} (P1 mu1 + P2 mu2) = [8/11, 8/11]
    mu_star = [(10.0 * 1.0 + 1.0 * (-2.0)) / 11.0, (1.0 * (-2.0) + 10.0 * 1.0) / 11.0]
    # FedAvg average (Sigma_i = I): [-0.5, -0.5]
    mu_fedavg = [0.5 * (mu1[0] + mu2[0]), 0.5 * (mu1[1] + mu2[1])]
    fedavg_bias = max(abs(a - b) for a, b in zip(mu_star, mu_fedavg))
    assert fedavg_bias > 1.2, f"Expected large FedAvg bias under anisotropic posteriors, got {fedavg_bias}"

    # Run FedPA server iterations with exact client deltas Delta_i = P_i (theta - mu_i)
    theta = [0.0, 0.0]
    alpha = 1.0 / 5.5  # 2 / (10 + 1)
    for _ in range(40):
        d1 = mat_vec(P1, [theta[0] - mu1[0], theta[1] - mu1[1]])
        d2 = mat_vec(P2, [theta[0] - mu2[0], theta[1] - mu2[1]])
        d_avg = [0.5 * (d1[0] + d2[0]), 0.5 * (d1[1] + d2[1])]
        theta = [theta[0] - alpha * d_avg[0], theta[1] - alpha * d_avg[1]]

    fedpa_err = max(abs(a - b) for a, b in zip(theta, mu_star))
    assert fedpa_err < 1e-12, f"Expected FedPA convergence to exact posterior mode, got {fedpa_err}"
    print(
        f"[PASS] FedPA boundaries verified: DP_err={dp_err:.2e}, "
        f"mu*=[{mu_star[0]:.4f}, {mu_star[1]:.4f}], FedAvg_bias={fedavg_bias:.4f}, FedPA_err={fedpa_err:.2e}"
    )


if __name__ == "__main__":
    main()
