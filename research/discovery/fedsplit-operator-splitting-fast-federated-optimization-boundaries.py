#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 410:
FedSplit: Operator Splitting for Fast Federated Optimization (Pathak & Wainwright 2020).
"""

import math


def main() -> None:
    # 3 heterogeneous strongly convex client quadratics f_j(x) = 0.5 * a_j * (x - b_j)^2
    a = [1.0, 4.0, 9.0]
    b = [-2.0, 1.0, 3.0]
    m = len(a)
    ell_star = min(a)
    L_star = max(a)
    kappa = L_star / ell_star

    # True global minimizer of sum_j f_j(x): sum_j a_j (x* - b_j) = 0
    x_star = sum(aj * bj for aj, bj in zip(a, b)) / sum(a)

    # Proposition 1: FedGD(s, e=2) deterministic fixed point (Eq. 8 / Eq. 11)
    s_gd = 0.1
    weights_gd = [aj * (1.0 + (1.0 - s_gd * aj)) for aj in a]
    x_fedgd_star = sum(w * bj for w, bj in zip(weights_gd, b)) / sum(weights_gd)
    fedgd_err = abs(x_fedgd_star - x_star)
    assert fedgd_err > 0.15, f"Expected non-zero FedGD(e=2) fixed-point bias, got {fedgd_err}"

    # Proposition 2: FedProx(s) deterministic fixed point (Eq. 14: sum_j grad M_{s f_j}(x) = 0)
    s_split = 1.0 / math.sqrt(ell_star * L_star)
    weights_prox = [aj / (1.0 + s_split * aj) for aj in a]
    x_fedprox_star = sum(w * bj for w, bj in zip(weights_prox, b)) / sum(weights_prox)
    fedprox_err = abs(x_fedprox_star - x_star)
    assert fedprox_err > 0.25, f"Expected non-zero FedProx fixed-point bias, got {fedprox_err}"

    # Proposition 3 & Theorem 1: FedSplit Peaceman-Rachford splitting (Algorithm 1)
    # Optimal step size s = 1 / sqrt(ell_* L_*), contraction factor rho = 1 - 2 / (sqrt(kappa) + 1)
    rho_theory = 1.0 - 2.0 / (math.sqrt(kappa) + 1.0)
    assert abs(rho_theory - 0.5) < 1e-12

    # True fixed-point auxiliary variables z_j^* = x^* - s * grad f_j(x^*)
    z_star = [x_star - s_split * aj * (x_star - bj) for aj, bj in zip(a, b)]
    assert abs(sum(z_star) / m - x_star) < 1e-12

    z = [0.0 for _ in range(m)]
    x = sum(z) / m
    for _ in range(40):
        dist_prev = math.sqrt(sum((zj - zj_s) ** 2 for zj, zj_s in zip(z, z_star)))
        z_half = [((2.0 * x - zj) + s_split * aj * bj) / (1.0 + s_split * aj) for zj, aj, bj in zip(z, a, b)]
        z_next = [zj + 2.0 * (z_hj - x) for zj, z_hj in zip(z, z_half)]
        dist_next = math.sqrt(sum((zj - zj_s) ** 2 for zj, zj_s in zip(z_next, z_star)))
        if dist_prev > 1e-13:
            assert dist_next <= rho_theory * dist_prev + 1e-12, (
                f"Contraction violated: {dist_next} > {rho_theory * dist_prev}"
            )
        z = z_next
        x = sum(z) / m

    fedsplit_err = abs(x - x_star)
    assert fedsplit_err < 1e-12, f"Expected FedSplit exact convergence, got {fedsplit_err}"
    print(
        f"[PASS] FedSplit boundaries verified: x*={x_star:.6f}, FedGD(e=2)_err={fedgd_err:.4f}, "
        f"FedProx_err={fedprox_err:.4f}, FedSplit_err={fedsplit_err:.2e}, rho={rho_theory:.4f}"
    )


if __name__ == "__main__":
    main()
