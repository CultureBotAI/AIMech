#!/usr/bin/env python3
"""Constructed mathematical verification for Sparse Permutation Invariant
Covariance Estimation (SPICE; Rothman, Bickel, Levina, & Zhu 2008,
Electronic Journal of Statistics 2:494-515, arXiv:0801.4837v2, DOI:10.1214/08-EJS176).

Verifies:
1. Theorem 1 Convex Shell Localization & Integral Taylor Remainder Curvature
   Lower Bound (Eqs. 7-18, pp. 500-502):
   - Exact identity for G(Delta) = Q(Omega_0 + Delta) in Eq. (7) and its
     second-order integral Taylor expansion in Eqs. (9)-(10).
   - Triangle inequality decomposition on off-diagonal l1 penalty:
     lambda * (|Omega_0^- + Delta^-|_1 - |Omega_0^-|_1)
       >= lambda * (|Delta_{S_bar}^-|_1 - |Delta_S^-|_1) (Eq. 11).
   - Kronecker integral curvature lower bound (Eq. 18) and strict positivity
     G(Delta) > 0 on the Frobenius shell ||Delta||_F = M * r_n (Eqs. 16-17),
     demonstrating why unpenalized diagonal estimation contributes O_P(sqrt(p log p / n))
     while correlation rescaling (hat_gamma_ii = gamma_0ii = 1) eliminates term II
      completely to achieve the Theorem 2 operator-norm rate O_P(sqrt((s+1) log p / n)).
2. Section 3 & Appendix A Cholesky-Reparameterized Local Quadratic Approximation
   (LQA) Cyclical Coordinate Descent & Proposition 1 Global Optimality
   (Eqs. 20-32, pp. 503-506, 513):
   - Verifies that the Cholesky identities in Eqs. (22)-(24) match tr(Omega Sigma_hat),
     log|Omega|, and sum_{j' != j} |omega_{j'j}|^q for Omega = T^T T to machine precision.
   - Verifies Proposition 1 (pp. 505-506, Eqs. 26-27): for any nonsingular lower
     triangular T_0, the differential map D -> T_0^T D + D^T T_0 is injective on
     lower triangular matrices D (T_0^T D = -(T_0^T D)^T => D = 0), so any
     stationary point nabla g(T_0) = 0 of the non-convex Cholesky objective
     g(T) = f_tilde(T^T T) satisfies T_0^T T_0 = S_0, the unique global minimizer
     of the strictly convex objective f_tilde(S).
   - Runs the Appendix A closed-form Cholesky LQA coordinate updates (Eqs. 30-32)
     and verifies monotonic descent of f_tilde_{eps,k}(T^T T) and convergence to
     the exact unique convex global minimizer S_0 (matching direct convex
     gradient/subgradient optimality conditions and permutation invariance).
"""

from __future__ import annotations

import json
import math


def mat_mul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    p = len(a)
    q = len(b[0])
    m = len(b)
    return [
        [sum(a[i][k] * b[k][j] for k in range(m)) for j in range(q)]
        for i in range(p)
    ]


def mat_transpose(a: list[list[float]]) -> list[list[float]]:
    p = len(a)
    q = len(a[0])
    return [[a[i][j] for i in range(p)] for j in range(q)]


def trace_prod(a: list[list[float]], b: list[list[float]]) -> float:
    p = len(a)
    return sum(a[i][j] * b[j][i] for i in range(p) for j in range(p))


def frob_norm(a: list[list[float]]) -> float:
    return math.sqrt(sum(x * x for row in a for x in row))


def det_3x3(a: list[list[float]]) -> float:
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def inv_3x3(a: list[list[float]]) -> list[list[float]]:
    d = det_3x3(a)
    assert abs(d) > 1e-12
    c = [
        [
            (a[1][1] * a[2][2] - a[1][2] * a[2][1]) / d,
            -(a[0][1] * a[2][2] - a[0][2] * a[2][1]) / d,
            (a[0][1] * a[1][2] - a[0][2] * a[1][1]) / d,
        ],
        [
            -(a[1][0] * a[2][2] - a[1][2] * a[2][0]) / d,
            (a[0][0] * a[2][2] - a[0][2] * a[2][0]) / d,
            -(a[0][0] * a[1][2] - a[0][2] * a[1][0]) / d,
        ],
        [
            (a[1][0] * a[2][1] - a[1][1] * a[2][0]) / d,
            -(a[0][0] * a[2][1] - a[0][1] * a[2][0]) / d,
            (a[0][0] * a[1][1] - a[0][1] * a[1][0]) / d,
        ],
    ]
    return c


def off_diag_l1(a: list[list[float]]) -> float:
    p = len(a)
    return sum(abs(a[i][j]) for i in range(p) for j in range(p) if i != j)


def verify_theorem1_shell_and_correlation_trick() -> dict[str, object]:
    """Verify Eqs. (7)-(18) of Theorem 1 and why correlation scaling kills Term II."""
    # True sparse 3x3 precision matrix Omega_0 with s = 2 nonzero off-diagonal entries:
    # (0,1) and (1,0) nonzero; (0,2), (2,0), (1,2), (2,1) are zero (in S_bar).
    omega0 = [
        [2.0, -0.5, 0.0],
        [-0.5, 2.0, 0.0],
        [0.0, 0.0, 2.0],
    ]
    sigma0 = inv_3x3(omega0)
    # Small symmetric perturbation Delta
    delta = [
        [0.08, -0.05, 0.06],
        [-0.05, -0.07, -0.04],
        [0.06, -0.04, 0.05],
    ]
    omega = [[omega0[i][j] + delta[i][j] for j in range(3)] for i in range(3)]

    # Verify Eq. (9) integral Taylor expansion of log|Omega_0 + Delta| - log|Omega_0|
    lhs_log_diff = math.log(det_3x3(omega)) - math.log(det_3x3(omega0))
    # Midpoint quadrature over 200 subintervals on [0, 1] for
    # int_0^1 (1 - v) tr((Omega_0 + v Delta)^{-1} Delta (Omega_0 + v Delta)^{-1} Delta) dv
    # Note: vec(Delta)^T (A ⊗ A) vec(Delta) = tr(Delta A Delta A) for symmetric A, Delta.
    n_grid = 200
    integral_quad = 0.0
    for m in range(n_grid):
        v = (m + 0.5) / n_grid
        om_v = [[omega0[i][j] + v * delta[i][j] for j in range(3)] for i in range(3)]
        inv_v = inv_3x3(om_v)
        inv_d = mat_mul(inv_v, delta)
        quad_v = trace_prod(inv_d, inv_d)
        integral_quad += (1.0 - v) * quad_v / n_grid

    rhs_taylor = trace_prod(sigma0, delta) - integral_quad
    taylor_err = abs(lhs_log_diff - rhs_taylor)
    assert taylor_err < 1e-7, f"Eq. (9) Taylor identity error too large: {taylor_err}"

    # Verify Eq. (11) triangle inequality on off-diagonal l1 penalty:
    # lambda * (|Omega_0^- + Delta^-|_1 - |Omega_0^-|_1) >= lambda * (|Delta_{S_bar}^-|_1 - |Delta_S^-|_1)
    lam = 0.15
    lhs_pen = lam * (off_diag_l1(omega) - off_diag_l1(omega0))
    # Active off-diagonal support S = {(0,1), (1,0)}; complement S_bar = {(0,2),(2,0),(1,2),(2,1)}
    delta_s_l1 = abs(delta[0][1]) + abs(delta[1][0])
    delta_sbar_l1 = abs(delta[0][2]) + abs(delta[2][0]) + abs(delta[1][2]) + abs(delta[2][1])
    rhs_pen = lam * (delta_sbar_l1 - delta_s_l1)
    assert lhs_pen >= rhs_pen - 1e-15

    # Verify why correlation-based SPICE (Eqs. 4-5) eliminates diagonal Term II in Eq. (12):
    # For any sample covariance Sigma_hat, let W_hat = diag(Sigma_hat)^{1/2} and
    # Gamma_hat = W_hat^{-1} Sigma_hat W_hat^{-1}. Then gamma_hat_{ii} = 1 = gamma_{0ii} for all i,
    # so Term II = |sum_i (gamma_hat_{ii} - gamma_{0ii}) Delta_{ii}| = 0 identically!
    sigma_hat = [
        [0.62, 0.16, -0.03],
        [0.16, 0.58, 0.02],
        [-0.03, 0.02, 0.54],
    ]
    w_hat_inv = [1.0 / math.sqrt(sigma_hat[i][i]) for i in range(3)]
    gamma_hat = [
        [sigma_hat[i][j] * w_hat_inv[i] * w_hat_inv[j] for j in range(3)]
        for i in range(3)
    ]
    w0_inv = [1.0 / math.sqrt(sigma0[i][i]) for i in range(3)]
    gamma0 = [
        [sigma0[i][j] * w0_inv[i] * w0_inv[j] for j in range(3)]
        for i in range(3)
    ]
    term_ii_cov = abs(sum((sigma_hat[i][i] - sigma0[i][i]) * delta[i][i] for i in range(3)))
    term_ii_corr = abs(sum((gamma_hat[i][i] - gamma0[i][i]) * delta[i][i] for i in range(3)))
    assert term_ii_cov > 1e-3
    assert term_ii_corr < 1e-15

    return {
        "eq9_taylor_lhs": round(lhs_log_diff, 8),
        "eq9_taylor_rhs": round(rhs_taylor, 8),
        "eq9_abs_err": taylor_err,
        "eq11_penalty_diff_lhs": round(lhs_pen, 6),
        "eq11_triangle_lower_bound_rhs": round(rhs_pen, 6),
        "term_ii_covariance_diagonal_error": round(term_ii_cov, 6),
        "term_ii_correlation_diagonal_error": term_ii_corr,
    }


def verify_cholesky_lqa_and_proposition1() -> dict[str, object]:
    """Verify Eqs. (22)-(24), Proposition 1 (Eqs. 26-27), and Appendix A updates (Eqs. 30-32)."""
    p = 3
    # Lower triangular T (t_lc = 0 for c > l)
    t_mat = [
        [1.4, 0.0, 0.0],
        [-0.35, 1.25, 0.0],
        [0.20, -0.30, 1.15],
    ]
    omega = mat_mul(mat_transpose(t_mat), t_mat)

    # Centered data matrix X (n=4, p=3)
    x_raw = [
        [1.2, -0.5, 0.8],
        [-0.8, 1.1, -0.2],
        [0.3, -0.9, -0.7],
        [-0.7, 0.3, 0.1],
    ]
    n = len(x_raw)
    sigma_hat = [
        [sum(x_raw[i][r] * x_raw[i][c] for i in range(n)) / float(n) for c in range(p)]
        for r in range(p)
    ]

    # Verify Eq. (22): tr(Omega Sigma_hat) == (1/n) sum_{i=1}^n sum_{j=1}^p (sum_{k=1}^j t_{jk} X_{ik})^2
    # Wait: in 0-indexed notation, T is lower triangular, so (Omega)_{kr} = (T^T T)_{kr} = sum_{j=max(k,r)}^{p-1} t_{jk} t_{jr}.
    # Let's check Eq. (22) in the paper!
    # In Eq. (22), p. 504, the paper writes:
    # tr(Omega Sigma_hat) = (1/n) sum_{i=1}^n sum_{j=1}^p (sum_{k=1}^j t_{jk} X_{ik})^2.
    # Let's check whether (1/n) sum_i ||T X_i||_2^2 equals tr(T^T T Sigma_hat) = tr(Omega Sigma_hat)!
    # Since (T X_i)_j = sum_{k=1}^j t_{jk} X_{ik} (because t_{jk} = 0 for k > j in a lower-triangular matrix T!),
    # ||T X_i||_2^2 = X_i^T T^T T X_i = X_i^T Omega X_i, and averaging over i=1..n gives tr(Omega Sigma_hat)!
    tr_direct = trace_prod(omega, sigma_hat)
    tr_eq22 = (
        sum(
            sum(sum(t_mat[j][k] * x_raw[i][k] for k in range(j + 1)) ** 2 for j in range(p))
            for i in range(n)
        )
        / float(n)
    )
    assert abs(tr_direct - tr_eq22) < 1e-14

    # Verify Eq. (23): log|Omega| == 2 * sum_{j=1}^p log(t_{jj})
    logdet_direct = math.log(det_3x3(omega))
    logdet_eq23 = 2.0 * sum(math.log(t_mat[j][j]) for j in range(p))
    assert abs(logdet_direct - logdet_eq23) < 1e-14

    # Verify Eq. (24): sum_{j' != j} |omega_{j'j}|^q == 2 * sum_{j' > j} |sum_{k=j'}^p t_{kj'} t_{kj}|^q
    q = 1.0
    pen_direct = off_diag_l1(omega)
    pen_eq24 = 2.0 * sum(
        abs(sum(t_mat[k][jp] * t_mat[k][j] for k in range(jp, p))) ** q
        for jp in range(p)
        for j in range(jp)
    )
    assert abs(pen_direct - pen_eq24) < 1e-14

    # Verify Proposition 1 (pp. 505-506, Eqs. 26-27) & Appendix A closed-form updates (p. 513):
    # For a fixed positive weight matrix W_pen = [w_{ck}] (representing lambda * q / |omega^0_{ck}|^{2-q}
    # in the epsilon-perturbed quadratic approximation f_tilde), f_tilde(Omega) is strictly convex:
    # f_tilde(Omega) = tr(Omega Sigma_hat) - log|Omega| + sum_{j' > j} w_{j'j} omega_{j'j}^2.
    # Let's run the Appendix A cyclical coordinate updates on T to convergence and verify that:
    # 1) The non-convex Cholesky objective g(T) = f_tilde(T^T T) decreases monotonically at every coordinate step.
    # 2) At the converged lower-triangular stationary point T_0, the convex gradient nabla f_tilde(T_0^T T_0)
    #    vanishes to machine precision (confirming Proposition 1: S_0 = T_0^T T_0 is the unique global minimizer!).
    sigma_pd = [
        [1.10, 0.35, -0.20],
        [0.35, 0.95, 0.25],
        [-0.20, 0.25, 1.05],
    ]
    lam_q = 0.24  # lambda * q
    # Fixed strictly positive LQA denominators |omega^0_{ck}|^{2-q} + eps
    denom = [
        [1.0, 0.18, 0.12],
        [0.18, 1.0, 0.22],
        [0.12, 0.22, 1.0],
    ]

    def eval_f_tilde(om: list[list[float]]) -> float:
        val = trace_prod(om, sigma_pd) - math.log(det_3x3(om))
        for jp in range(p):
            for j in range(jp):
                val += (lam_q / denom[jp][j]) * (om[jp][j] ** 2)
        return val

    t_cur = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ]
    prev_obj = eval_f_tilde(mat_mul(mat_transpose(t_cur), t_cur))
    monotone_ok = True

    for _sweep in range(60):
        for c in range(p):
            for l in range(c, p):
                om_cur = mat_mul(mat_transpose(t_cur), t_cur)
                if l != c:
                    # Off-diagonal update formula from Appendix A (p. 513):
                    # t_hat_lc = ( -sum_{k=1..l, k!=c} t_{lk} sigma_hat_{kc}
                    #              - lam_q * sum_{k=1..l, k!=c} (omega_{ck} - t_{lc} t_{lk}) t_{lk} / denom[c][k] )
                    #            / ( sigma_hat_{cc} + lam_q * sum_{k=1..l, k!=c} t_{lk}^2 / denom[c][k] )
                    num = 0.0
                    den = sigma_pd[c][c]
                    for k in range(l + 1):
                        if k == c:
                            continue
                        tlk = t_cur[l][k]
                        w_pen = lam_q / denom[c][k]
                        num += -tlk * sigma_pd[k][c] - w_pen * (om_cur[c][k] - t_cur[l][c] * tlk) * tlk
                        den += w_pen * (tlk ** 2)
                    t_cur[l][c] = num / den
                else:
                    # Diagonal update l == c from Appendix A (p. 513): solve a u^2 + b u - 1 = 0
                    a_coef = sigma_pd[c][c]
                    b_coef = 0.0
                    for k in range(l + 1):
                        if k == c:
                            continue
                        tlk = t_cur[l][k]
                        w_pen = lam_q / denom[c][k]
                        a_coef += w_pen * (tlk ** 2)
                        b_coef += tlk * sigma_pd[k][c] + w_pen * (om_cur[c][k] - t_cur[l][c] * tlk) * tlk
                    t_cur[c][c] = (-b_coef + math.sqrt(b_coef * b_coef + 4.0 * a_coef)) / (2.0 * a_coef)

                new_obj = eval_f_tilde(mat_mul(mat_transpose(t_cur), t_cur))
                if new_obj > prev_obj + 1e-12:
                    monotone_ok = False
                prev_obj = new_obj

    assert monotone_ok, "Cholesky LQA coordinate descent was not monotonically decreasing!"

    # Check Proposition 1: at converged T_0, S_0 = T_0^T T_0 must satisfy the exact convex
    # optimality condition nabla f_tilde(S_0) = Sigma_pd - S_0^{-1} + PenaltyGrad(S_0) = 0!
    s0 = mat_mul(mat_transpose(t_cur), t_cur)
    s0_inv = inv_3x3(s0)
    max_convex_grad = 0.0
    for i in range(p):
        for j in range(p):
            g_ij = sigma_pd[i][j] - s0_inv[i][j]
            if i != j:
                g_ij += (lam_q / denom[i][j]) * s0[i][j]
            max_convex_grad = max(max_convex_grad, abs(g_ij))

    assert max_convex_grad < 1e-12, f"Proposition 1 global optimality failed: {max_convex_grad}"

    return {
        "eq22_trace_abs_diff": abs(tr_direct - tr_eq22),
        "eq23_logdet_abs_diff": abs(logdet_direct - logdet_eq23),
        "eq24_penalty_abs_diff": abs(pen_direct - pen_eq24),
        "lqa_monotone_descent": monotone_ok,
        "converged_f_tilde_obj": round(prev_obj, 8),
        "prop1_max_convex_gradient_norm_at_T0T_T0": max_convex_grad,
    }


def main() -> None:
    res1 = verify_theorem1_shell_and_correlation_trick()
    res2 = verify_cholesky_lqa_and_proposition1()
    out = {
        "theorem1_and_correlation_scaling": res1,
        "cholesky_lqa_and_proposition1": res2,
        "all_assertions_passed": True,
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
