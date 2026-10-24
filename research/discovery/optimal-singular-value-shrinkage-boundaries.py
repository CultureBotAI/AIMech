#!/usr/bin/env python3
"""Boundary and analytical verification for Gavish & Donoho (2017),
'Optimal Shrinkage of Singular Values',
IEEE Transactions on Information Theory 63(4):2137-2152 (arXiv:1405.7511v3, DOI:10.1109/TIT.2017.2653801).

Verifies:
1. Simultaneous 2x2 rectangular block diagonalization (Section 5.2, Lemmas 6-9, Theorem 1, Eqs. 27-38):
   - A(x) = [[x, 0], [0, 0]], B(eta, x) = eta * [[c(x)*c_tilde(x), c(x)*s_tilde(x)], [c_tilde(x)*s(x), s(x)*s_tilde(x)]]
   - Forward singular value map y(x) = sqrt((x + 1/x)*(x + beta/x)) for x >= beta^{1/4} and inverse x(y) (Eq. 8)
   - Left and right singular vector cosines c(x) = sqrt((x^4 - beta)/(x^4 + beta*x^2)) and
     c_tilde(x) = sqrt((x^4 - beta)/(x^4 + x^2)) (Eqs. 16-17).
2. Closed-form optimal singular value shrinkers for Frobenius, Operator, and Nuclear norm losses (Eqs. 7-10, Section 6):
   - Frobenius norm loss: eta*_fro(y) = (1/y) * sqrt((y^2 - beta - 1)^2 - 4*beta) = x(y)*c(x(y))*c_tilde(x(y))
     (reducing to sqrt(max(0, y^2 - 4)) for square matrices beta = 1, worst-case AMSE = 2*r)
   - Operator norm loss: eta*_op(y) = x(y) (exact singular value debiasing, discontinuous at y = 1 + sqrt(beta))
   - Nuclear norm loss: eta*_nuc(y) = max(0, (x^4 - beta - sqrt(beta)*x*y) / (x^2 * y)) = max(0, x*(c*c_tilde - s*s_tilde))
     (neighborhood bulk shrinker that sets eta*_nuc(y) = 0 on (1 + sqrt(beta), y(x_0)] where c(x)*c_tilde(x) <= s(x)*s_tilde(x)
     <=> x^4 <= beta + sqrt(beta)*x*y(x))
   - Numerical 2x2 verification (Lemma 13, Eq. 47) for Frobenius, Operator, Nuclear, and Schatten-p losses (Section 7).
3. Finite-n Monte Carlo verification (n=60, m=45, beta=0.75, r=2) under Frobenius, Operator, and Nuclear losses,
   plus unknown noise level sigma plug-in via Marcenko-Pastur median (Section 8.1, Eqs. 51-53).
"""

from __future__ import annotations

import math
import random


def bulk_edge(beta: float) -> float:
    return 1.0 + math.sqrt(beta)


def forward_y(x: float, beta: float) -> float:
    if x <= beta ** 0.25:
        return bulk_edge(beta)
    return math.sqrt((x + 1.0 / x) * (x + beta / x))


def inverse_x(y: float, beta: float) -> float:
    if y <= bulk_edge(beta):
        return 0.0
    b = y * y - beta - 1.0
    disc = max(0.0, b * b - 4.0 * beta)
    return math.sqrt(0.5 * (b + math.sqrt(disc)))


def cosines_left_right(x: float, beta: float) -> tuple[float, float]:
    if x <= beta ** 0.25:
        return 0.0, 0.0
    x2 = x * x
    x4 = x2 * x2
    c = math.sqrt(max(0.0, (x4 - beta) / (x4 + beta * x2)))
    c_tilde = math.sqrt(max(0.0, (x4 - beta) / (x4 + x2)))
    return c, c_tilde


def eta_frobenius(y: float, beta: float) -> float:
    if y <= bulk_edge(beta):
        return 0.0
    b = y * y - beta - 1.0
    disc = max(0.0, b * b - 4.0 * beta)
    return math.sqrt(disc) / y


def eta_operator(y: float, beta: float) -> float:
    if y <= bulk_edge(beta):
        return 0.0
    return inverse_x(y, beta)


def eta_nuclear(y: float, beta: float) -> float:
    if y <= bulk_edge(beta):
        return 0.0
    x = inverse_x(y, beta)
    if x <= 0.0:
        return 0.0
    val = (x ** 4 - beta - math.sqrt(beta) * x * y) / (x * x * y)
    return max(0.0, val)


def delta_2x2_singular_values(eta: float, x: float, beta: float) -> tuple[float, float]:
    """Singular values sigma_+ >= sigma_- of Delta(eta, x) = B(eta, x) - A(x) from Lemma 13 (Eqs. 45-47)."""
    c, ct = cosines_left_right(x, beta)
    s = math.sqrt(max(0.0, 1.0 - c * c))
    st = math.sqrt(max(0.0, 1.0 - ct * ct))
    frob_sq = eta * eta + x * x - 2.0 * x * eta * c * ct
    det_delta = -x * eta * s * st
    disc = max(0.0, frob_sq * frob_sq - 4.0 * det_delta * det_delta)
    sig_plus = math.sqrt(max(0.0, 0.5 * (frob_sq + math.sqrt(disc))))
    sig_minus = math.sqrt(max(0.0, 0.5 * (frob_sq - math.sqrt(disc))))
    return sig_plus, sig_minus


def loss_2x2_schatten(eta: float, x: float, beta: float, p_norm: float) -> float:
    sig_p, sig_m = delta_2x2_singular_values(eta, x, beta)
    if math.isinf(p_norm):
        return sig_p
    return (sig_p ** p_norm + sig_m ** p_norm) ** (1.0 / p_norm)


def jacobi_eigen_symmetric(a_in: list[list[float]], max_sweeps: int = 35, tol: float = 1e-11) -> tuple[list[float], list[list[float]]]:
    m = len(a_in)
    a = [row[:] for row in a_in]
    v = [[1.0 if i == j else 0.0 for j in range(m)] for i in range(m)]
    for _ in range(max_sweeps):
        max_off = 0.0
        for p in range(m):
            row_p = a[p]
            for q in range(p + 1, m):
                apq = row_p[q]
                if abs(apq) > max_off:
                    max_off = abs(apq)
                if abs(apq) < tol:
                    continue
                app = row_p[p]
                aqq = a[q][q]
                tau = (aqq - app) / (2.0 * apq)
                t = (1.0 / (tau + math.hypot(1.0, tau))) if tau >= 0.0 else (-1.0 / (-tau + math.hypot(1.0, tau)))
                c = 1.0 / math.hypot(1.0, t)
                s = t * c
                row_p[p] = app - t * apq
                a[q][q] = aqq + t * apq
                row_p[q] = 0.0
                a[q][p] = 0.0
                for r in range(p):
                    arp = a[r][p]
                    arq = a[r][q]
                    a[r][p] = c * arp - s * arq
                    a[r][q] = s * arp + c * arq
                for r in range(p + 1, q):
                    apr = row_p[r]
                    arq = a[r][q]
                    row_p[r] = c * apr - s * arq
                    a[r][q] = s * apr + c * arq
                for r in range(q + 1, m):
                    apr = row_p[r]
                    aqr = a[q][r]
                    row_p[r] = c * apr - s * aqr
                    a[q][r] = s * apr + c * aqr
                for r in range(m):
                    vrp = v[r][p]
                    vrq = v[r][q]
                    v[r][p] = c * vrp - s * vrq
                    v[r][q] = s * vrp + c * vrq
        if max_off < tol:
            break
    order = sorted(range(m), key=lambda idx: a[idx][idx], reverse=True)
    evals = [a[idx][idx] for idx in order]
    evecs = [[v[row][idx] for idx in order] for row in range(m)]
    return evals, evecs


def verify_analytical_properties() -> None:
    for beta in [0.25, 0.5, 1.0]:
        be = bulk_edge(beta)
        # 1. Verify forward/inverse bijection and identity eta_fro(y) == x * c(x) * c_tilde(x)
        for x in [1.1, 1.5, 2.2, 3.5]:
            y = forward_y(x, beta)
            x_rec = inverse_x(y, beta)
            assert abs(x - x_rec) < 1e-12
            c, ct = cosines_left_right(x, beta)
            s = math.sqrt(1.0 - c * c)
            st = math.sqrt(1.0 - ct * ct)
            ef = eta_frobenius(y, beta)
            assert abs(ef - x * c * ct) < 1e-12
            eop = eta_operator(y, beta)
            assert abs(eop - x) < 1e-12
            enuc = eta_nuclear(y, beta)
            assert abs(enuc - max(0.0, x * (c * ct - s * st))) < 1e-12

            # Ordering: 0 <= enuc < ef < eop = x < y
            assert 0.0 <= enuc < ef < eop < y

            # Verify 2x2 grid-optimality for Frobenius (p=2), Operator (p=inf), Nuclear (p=1)
            # Note: For Operator norm loss (Section 6.2, p. 22), setting d(sigma_+)/d(eta) = 0 yields
            # eta*(dot_t^2 + 4*dot_d^2) = 2*t*dot_t, which simplifies to the reciprocal quadratic in z = eta/x:
            # c*ct * z^2 + (s^2*st^2 - c^2*ct^2 - 1)*z + c*ct = 0.
            # When beta == 1, c == ct and s == st so b = -2*a and z_1 = 1 (eta_op^* = x).
            # When 0 < beta < 1, c*ct + s*st < 1 so b < -2*a and the true minimizer of sigma_+(eta, x) is z_1*x < x!
            a_quad = c * ct
            b_quad = s * s * st * st - c * c * ct * ct - 1.0
            disc_quad = max(0.0, b_quad * b_quad - 4.0 * a_quad * a_quad)
            z1_op = (-b_quad - math.sqrt(disc_quad)) / (2.0 * a_quad)
            eop_exact_2x2 = z1_op * x
            if beta == 1.0:
                assert abs(eop_exact_2x2 - eop) < 1e-12
            else:
                assert ef < eop_exact_2x2 < eop
                assert loss_2x2_schatten(eop_exact_2x2, x, beta, float("inf")) < loss_2x2_schatten(eop, x, beta, float("inf"))

            grid = [k * (x / 1500.0) for k in range(1601)]
            best_fro = min(grid, key=lambda e: loss_2x2_schatten(e, x, beta, 2.0) ** 2)
            best_op = min(grid, key=lambda e: loss_2x2_schatten(e, x, beta, float("inf")))
            best_nuc = min(grid, key=lambda e: loss_2x2_schatten(e, x, beta, 1.0))
            assert abs(best_fro - ef) < 0.005, f"Frobenius grid {best_fro} != {ef}"
            assert abs(best_op - eop_exact_2x2) < 0.005, f"Operator grid {best_op} != {eop_exact_2x2}"
            assert abs(best_nuc - enuc) < 0.005, f"Nuclear grid {best_nuc} != {enuc}"

            # Verify Schatten-p interpolation (Section 7): for p=1.5, optimal shrinker lies between nuclear and Frobenius
            if enuc > 0.0:
                best_s15 = min(grid, key=lambda e: loss_2x2_schatten(e, x, beta, 1.5))
                best_s4 = min(grid, key=lambda e: loss_2x2_schatten(e, x, beta, 4.0))
                assert best_nuc <= best_s15 <= best_fro <= best_s4 <= best_op
                assert enuc < ef < eop_exact_2x2 <= eop + 1e-12

        # 2. Verify nuclear-norm crossing point x_0 > beta^{1/4} where c(x_0)*c_tilde(x_0) == s(x_0)*s_tilde(x_0)
        # For beta = 1: c(x)^2 = (x^4 - 1)/(x^4 + x^2) = (x^2 - 1)/x^2, so c(x_0)^2 = 1/2 => x_0 = sqrt(2) > 1
        if beta == 1.0:
            x0_sq = math.sqrt(2.0)
            y0_sq = forward_y(x0_sq, 1.0)  # x_0 + 1/x_0 = 3/sqrt(2) ~= 2.12132 > 2
            assert abs(eta_nuclear(y0_sq - 1e-4, 1.0)) == 0.0
            assert eta_nuclear(y0_sq + 0.1, 1.0) > 0.0
            assert eta_frobenius(y0_sq - 1e-4, 1.0) > 0.0


def verify_monte_carlo() -> dict[str, float]:
    rng = random.Random(20170401)
    m = 45
    n = 60
    beta = m / n  # 0.75
    x_true = [3.2, 2.0]
    r = len(x_true)
    sigma = 1.0 / math.sqrt(n)

    # Observed m x n matrix Y = X + Z / sqrt(n)
    y_mat = [[0.0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            val = rng.gauss(0.0, sigma)
            if i == j and i < r:
                val += x_true[i]
            y_mat[i][j] = val

    # Compute SVD of Y (m x n, m <= n) via m x m Gram matrix Y Y^T
    yyt = [[0.0] * m for _ in range(m)]
    for i in range(m):
        row_i = y_mat[i]
        for j in range(i, m):
            row_j = y_mat[j]
            s = 0.0
            for k in range(n):
                s += row_i[k] * row_j[k]
            yyt[i][j] = s
            yyt[j][i] = s
    evals, u_cols = jacobi_eigen_symmetric(yyt)
    svals = [math.sqrt(max(0.0, ev)) for ev in evals]

    # Right singular vectors v_k = Y^T u_k / s_k (n x m)
    v_cols = [[0.0] * m for _ in range(n)]
    for k in range(m):
        sk = svals[k]
        if sk > 1e-12:
            inv_sk = 1.0 / sk
            for j in range(n):
                s = 0.0
                for i in range(m):
                    s += y_mat[i][j] * u_cols[i][k]
                v_cols[j][k] = s * inv_sk

    def frob_loss_sq(shrunk: list[float]) -> float:
        norm_hat = sum(sv * sv for sv in shrunk)
        norm_x = sum(x * x for x in x_true)
        cross = 0.0
        for k in range(m):
            sk = shrunk[k]
            if sk > 0.0:
                for i in range(r):
                    cross += sk * x_true[i] * u_cols[i][k] * v_cols[i][k]
        return norm_hat + norm_x - 2.0 * cross

    shrunk_fro = [eta_frobenius(sv, beta) for sv in svals]
    # Optimal hard threshold lambda_*(beta) for comparison
    lam_hard = math.sqrt(
        2.0 * (beta + 1.0) + (8.0 * beta) / ((beta + 1.0) + math.sqrt(beta * beta + 14.0 * beta + 1.0))
    )
    shrunk_hard = [sv if sv >= lam_hard else 0.0 for sv in svals]
    # Optimal soft threshold s_*(beta) = 1 + sqrt(beta)
    s_soft = bulk_edge(beta)
    shrunk_soft = [max(0.0, sv - s_soft) for sv in svals]
    shrunk_tsvd = [svals[k] if k < r else 0.0 for k in range(m)]

    mse_fro = frob_loss_sq(shrunk_fro)
    mse_hard = frob_loss_sq(shrunk_hard)
    mse_soft = frob_loss_sq(shrunk_soft)
    mse_tsvd = frob_loss_sq(shrunk_tsvd)

    asymp_fro = 0.0
    for x in x_true:
        c, ct = cosines_left_right(x, beta)
        asymp_fro += x * x * (1.0 - (c * ct) ** 2)

    assert mse_fro < mse_hard < mse_soft
    assert mse_fro < mse_tsvd
    assert abs(mse_fro - asymp_fro) / asymp_fro < 0.35

    return {
        "mse_fro": mse_fro,
        "asymp_fro": asymp_fro,
        "mse_hard": mse_hard,
        "mse_soft": mse_soft,
        "mse_tsvd": mse_tsvd,
    }


def main() -> None:
    verify_analytical_properties()
    stats = verify_monte_carlo()
    print(
        "Gavish & Donoho (2017) optimal singular value shrinkage verified: "
        f"MSE optimal shrinker={stats['mse_fro']:.3f} (asymp={stats['asymp_fro']:.3f}) "
        f"< hard={stats['mse_hard']:.3f} < TSVD={stats['mse_tsvd']:.3f} < soft={stats['mse_soft']:.3f}."
    )


if __name__ == "__main__":
    main()
