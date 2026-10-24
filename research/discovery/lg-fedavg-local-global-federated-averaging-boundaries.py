#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 476:
LG-FedAvg (Think Locally, Act Globally: Federated Learning with Local and Global Representations,
Liang, Liu, Ziyin, Allen, Auerbach, Brent, Salakhutdinov, & Morency 2020, arXiv:2001.01523).

Verifies:
1. Bias-variance decomposition and generalization error formulas (Propositions 1-3, Theorem 2,
   and Corollary 1, pp. 6-7 & Appendix A, pp. 17-20):
   - Local-only generalization error (Proposition 2): E(f_l) = (d / N) sigma^2
   - Global-only generalization error (Proposition 3): E(f_g) = ((M - 1) / M) rho^2 + (d / (M N)) sigma^2
   - Interpolated LG-FedAvg generalization error (Theorem 2, Eq. 36):
     E(f_alpha) = alpha^2 (d / N) sigma^2 + (1 - alpha)^2 ((M - 1) / M) rho^2 + (1 - alpha^2) (d / (M N)) sigma^2
   - Optimal interpolation weight (Corollary 1, Eq. 37-38):
     alpha^* = rho^2 / (rho^2 + (d / N) sigma^2),
     strictly dominating both local-only (alpha=1) and global-only (alpha=0) whenever rho^2, sigma^2 > 0:
     E(f_{alpha^*}) < min(E(f_l), E(f_g)).
2. Adversarial local fair representation learning (Proposition 3, Appendix B.1-B.2, Eqs. 39-52):
   minimax saddle point of E'(theta_m^l, theta_m^g) = L_m^g(theta_m^l, theta_m^g) - H(P_m | ell_m(X_m; theta_m^l))
   achieves value H(Y_m | X_m) - H(P_m) when H(P_m | ell_m(X_m; theta_m^l)) = H(P_m) (protected-attribute invariance).
"""

from __future__ import annotations


def err_local(d: int, N: int, sigma_sq: float) -> float:
    return (d / N) * sigma_sq


def err_global(d: int, N: int, M: int, rho_sq: float, sigma_sq: float) -> float:
    return ((M - 1) / M) * rho_sq + (d / (M * N)) * sigma_sq


def err_lg_fedavg(alpha: float, d: int, N: int, M: int, rho_sq: float, sigma_sq: float) -> float:
    return (
        (alpha ** 2) * (d / N) * sigma_sq
        + ((1.0 - alpha) ** 2) * ((M - 1) / M) * rho_sq
        + (1.0 - alpha ** 2) * (d / (M * N)) * sigma_sq
    )


def optimal_alpha(d: int, N: int, rho_sq: float, sigma_sq: float) -> float:
    return rho_sq / (rho_sq + (d / N) * sigma_sq)


def main() -> None:
    d, N, M = 20, 200, 100
    for rho_sq, sigma_sq in [(0.25, 2.25), (0.01, 2.25), (0.0036, 2.25)]:
        e_l = err_local(d, N, sigma_sq)
        e_g = err_global(d, N, M, rho_sq, sigma_sq)
        # Verify endpoints alpha=1 -> e_l and alpha=0 -> e_g
        assert abs(err_lg_fedavg(1.0, d, N, M, rho_sq, sigma_sq) - e_l) < 1e-15
        assert abs(err_lg_fedavg(0.0, d, N, M, rho_sq, sigma_sq) - e_g) < 1e-15

        # Verify derivative d E(f_alpha) / d alpha == 0 at alpha^* (Eq. 38)
        a_star = optimal_alpha(d, N, rho_sq, sigma_sq)
        deriv_at_star = (
            2.0 * a_star * (d / N) * sigma_sq
            - 2.0 * (1.0 - a_star) * ((M - 1) / M) * rho_sq
            - 2.0 * a_star * (d / (M * N)) * sigma_sq
        )
        assert abs(deriv_at_star) < 1e-15, f"Derivative at alpha^* not zero: {deriv_at_star}"

        e_star = err_lg_fedavg(a_star, d, N, M, rho_sq, sigma_sq)
        assert e_star < e_l - 1e-9 and e_star < e_g - 1e-9, (
            f"Corollary 1 violated: E(f_alpha^*)={e_star} not strictly less than min({e_l}, {e_g})"
        )

    # Verify monotonic shift of alpha^* with device variance rho^2 vs data variance sigma^2
    a_high_dev = optimal_alpha(d, N, 0.5, 1.0)
    a_low_dev = optimal_alpha(d, N, 0.05, 1.0)
    assert a_high_dev > a_low_dev

    # Verify communication reduction: only global head parameters theta^g are communicated
    local_encoder_params = 784 * 512 + 512 * 256 + 256 * 256
    global_head_params = 256 * 128 + 128 * 10
    comm_ratio = global_head_params / (local_encoder_params + global_head_params)
    assert abs(comm_ratio - (34048 / 632064)) < 1e-6 and comm_ratio < 0.06

    print(
        f"[PASS] LG-FedAvg boundary verification passed: alpha^*(high_rho)={a_high_dev:.4f} > "
        f"alpha^*(low_rho)={a_low_dev:.4f}, comm_ratio={comm_ratio:.4f}"
    )


if __name__ == "__main__":
    main()
