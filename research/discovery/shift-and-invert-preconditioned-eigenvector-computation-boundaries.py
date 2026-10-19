#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 354:
Shift-and-Invert Preconditioning for Faster Leading Eigenvector Computation
(Garber, Hazan, Jin, Kakade, Musco, Netrapalli, & Sidford, 2016, ICML / PMLR 48:2626-2634, arXiv:1605.08754).
"""

import math
import random


def main():
    # Construct explicit matrix A in R^{n x d} with Sigma = A^T A having small relative eigengap:
    # lambda_1 = 1.0, lambda_2 = 0.99 (gap = 0.01), lambda_3 = 0.5, lambda_4 = 0.2
    eigs = [1.0, 0.99, 0.5, 0.2]
    d = len(eigs)
    lambda1 = eigs[0]
    lambda2 = eigs[1]
    gap = (lambda1 - lambda2) / lambda1  # 0.01

    # Construct n = 4 orthogonal rows a_i = sqrt(lambda_i) * e_i so Sigma = sum_i a_i a_i^T = diag(eigs)
    n = d
    A = [[math.sqrt(eigs[i]) if i == j else 0.0 for j in range(d)] for i in range(n)]
    frob_sq = sum(eigs)

    # Shift parameter lambda in [(1 + gap/150) * lambda_1, (1 + gap/100) * lambda_1] (Section 3.1)
    lam = (1.0 + gap / 100.0) * lambda1  # 1.0001
    B_diag = [lam - eig for eig in eigs]
    B_inv_diag = [1.0 / b for b in B_diag]

    # 1. Verify Section 3.1 & Theorem 4: Inverted eigenvalue gap ratio >= 100
    inv_gap_ratio = B_inv_diag[0] / B_inv_diag[1]
    assert inv_gap_ratio >= 100.0 - 1e-9, f"Expected inverted gap ratio >= 100, got {inv_gap_ratio}"

    def B_norm(x):
        return math.sqrt(sum(B_diag[i] * (x[i] ** 2) for i in range(d)))

    def potential_G(x):
        num = math.sqrt(sum(B_diag[i] * (x[i] ** 2) for i in range(1, d)))
        den = math.sqrt(B_diag[0] * (x[0] ** 2))
        return num / den

    # Test Lemma 2, Lemma 3, and Theorem 4 on a unit vector x with Rayleigh quotient error eps <= 0.5 * lambda1 * gap
    x_unit = [math.sqrt(1.0 - 0.002), math.sqrt(0.0015), math.sqrt(0.0003), math.sqrt(0.0002)]
    rq = sum(eigs[i] * (x_unit[i] ** 2) for i in range(d))
    eps = lambda1 - rq
    assert eps <= 0.5 * lambda1 * gap

    # Lemma 3: eps / (lam - lambda1) <= G(x)^2 <= (1 + (lam - lambda1)/(lambda1*gap)) * (1 + 2*eps/(lambda1*gap)) * eps / (lam - lambda1)
    Gx = potential_G(x_unit)
    lhs_l3 = eps / (lam - lambda1)
    rhs_l3 = (1.0 + (lam - lambda1) / (lambda1 * gap)) * (1.0 + 2.0 * eps / (lambda1 * gap)) * lhs_l3
    assert lhs_l3 - 1e-12 <= Gx * Gx <= rhs_l3 + 1e-12, f"Lemma 3 violated: {lhs_l3} <= {Gx*Gx} <= {rhs_l3}"

    # Theorem 4: Exact shifted-and-inverted power step x_tilde = B^{-1} x contracts G(x) by >= 100x
    x_tilde = [B_inv_diag[i] * x_unit[i] for i in range(d)]
    Gx_tilde = potential_G(x_tilde)
    assert Gx_tilde <= Gx / 100.0 + 1e-12

    # 2. Verify Lemma 11 (Improved Variance Bound for Sum-of-Non-Convex SVRG):
    # sum_{i=1}^n (1/p_i) ||grad psi_i(x) - grad psi_i(x^opt)||_2^2 <= (4 * lambda1 * ||A||_F^2 / (lam - lambda1)) * (f(x) - f(x^opt))
    b_vec = list(x_unit)
    x_opt = [b_vec[i] / B_diag[i] for i in range(d)]
    p_probs = [eigs[i] / frob_sq for i in range(n)]

    def f_sys(x):
        return 0.5 * sum(B_diag[i] * (x[i] ** 2) for i in range(d)) - sum(b_vec[i] * x[i] for i in range(d))

    def grad_psi(i, x):
        # psi_i(x) = 1/2 x^T (lam * ||a_i||^2 / ||A||_F^2 I - a_i a_i^T) x - (1/n) b^T x
        w_i = lam * p_probs[i]
        res = [w_i * x[j] - b_vec[j] / n for j in range(d)]
        res[i] -= eigs[i] * x[i]
        return res

    x_probe = [x_opt[j] + 0.5 * (j + 1) for j in range(d)]
    lhs_var = 0.0
    for i in range(n):
        gp_x = grad_psi(i, x_probe)
        gp_opt = grad_psi(i, x_opt)
        diff_sq = sum((gp_x[j] - gp_opt[j]) ** 2 for j in range(d))
        lhs_var += diff_sq / p_probs[i]
    rhs_var = (4.0 * lambda1 * frob_sq / (lam - lambda1)) * (f_sys(x_probe) - f_sys(x_opt))
    assert lhs_var <= rhs_var + 1e-9, f"Lemma 11 variance bound violated: {lhs_var} > {rhs_var}"

    # 3. Compare Shifted-and-Inverted Power Method vs Classical Power Method from the same initial vector
    x0 = [0.5, 0.5, 0.5, 0.5]
    # Classical power method after 5 iterations:
    x_pm = list(x0)
    for _ in range(5):
        x_pm = [eigs[i] * x_pm[i] for i in range(d)]
        nrm = math.sqrt(sum(v * v for v in x_pm))
        x_pm = [v / nrm for v in x_pm]
    pm_align = abs(x_pm[0])

    # Shifted-and-inverted power method after 5 iterations:
    x_sipm = list(x0)
    for _ in range(5):
        x_sipm = [B_inv_diag[i] * x_sipm[i] for i in range(d)]
        nrm = math.sqrt(sum(v * v for v in x_sipm))
        x_sipm = [v / nrm for v in x_sipm]
    sipm_align = abs(x_sipm[0])
    assert 1.0 - sipm_align < 1e-10 and pm_align < 0.75

    print(
        f"[PASS] Round 354 Shift-and-Invert Eigenvector (Garber et al. 2016): "
        f"inv_gap_ratio={inv_gap_ratio:.1f}, G(x)={Gx:.4f} -> G(B^-1 x)={Gx_tilde:.6f}, "
        f"lemma11_ratio={lhs_var/rhs_var:.4f} <= 1.0, "
        f"5step_sipm_err={1-sipm_align:.2e} vs pm_err={1-pm_align:.4f}"
    )


if __name__ == "__main__":
    main()
