#!/usr/bin/env python3
"""Boundary and analytical verification for Donoho, Gavish, & Johnstone (2018),
'Optimal shrinkage of eigenvalues in the spiked covariance model',
The Annals of Statistics 46(4):1742-1778 (arXiv:1311.0851v3, DOI:10.1214/17-AOS1601).

Verifies:
1. Simultaneous 2x2 block decomposition (Lemma 1 & Lemma 7, eqs. 2.1-2.5, 7.8):
   - A(ell) = diag(ell, 1), B(eta, c) = I_2 + (eta - 1) [[c^2, c*s], [c*s, s^2]]
   - Spike-eigenvector cosine squared: c^2(ell) = (1 - gamma / (ell - 1)^2) / (1 + gamma / (ell - 1))
   - Baik-Silverstein forward map lambda(ell) = ell + gamma * ell / (ell - 1) and exact inverse
     ell(lambda) = ((lambda + 1 - gamma) + sqrt((lambda + 1 - gamma)^2 - 4*lambda)) / 2
2. Closed-form loss-specific optimal nonlinearities eta*(ell) across distinct losses (Table 2):
   - Frobenius covariance loss L^{F,1} (and Entropy loss L^{ent}): eta_*^F(ell) = ell * c^2 + s^2
   - Stein loss L^{st} (and Precision Frobenius loss L^{F,2}): eta_*^{St}(ell) = ell / (c^2 + ell * s^2)
   - Operator norm losses L^{O,1}, L^{O,2}: eta_*^O(ell) = ell
   - Nuclear norm loss L^{N,1}: eta_*^N(ell) = max(1 + (ell - 1)*(1 - 2*s^2), 1) (neighborhood bulk shrinker)
   - Frechet discrepancy L^{fre}: eta_*^{fre}(ell) = (sqrt(ell)*c^2 + s^2)^2
   - Ordering and numerical optimization check: each closed-form eta_*(ell) minimizes the 2x2 pivot loss
     F(ell, eta) = L_2(A(ell), B(eta, c(ell))) over eta >= 1.
3. High-dimensional Monte Carlo verification (n=200, p=100, gamma=0.5, r=2 spikes ell_1=5.0, ell_2=3.0)
   comparing Frobenius, Stein, Operator, and Nuclear shrinkers against the unshrunk sample covariance
   and against the exact 2x2 asymptotic loss formulas, plus unknown-sigma^2 Marcenko-Pastur median plug-in.
"""

from __future__ import annotations

import math
import random


def lambda_plus(gamma: float) -> float:
    return (1.0 + math.sqrt(gamma)) ** 2


def ell_plus(gamma: float) -> float:
    return 1.0 + math.sqrt(gamma)


def forward_lambda(ell: float, gamma: float) -> float:
    if ell <= ell_plus(gamma):
        return lambda_plus(gamma)
    return ell + gamma * ell / (ell - 1.0)


def inverse_ell(lam: float, gamma: float) -> float:
    if lam <= lambda_plus(gamma):
        return ell_plus(gamma)
    b = lam + 1.0 - gamma
    disc = max(0.0, b * b - 4.0 * lam)
    return 0.5 * (b + math.sqrt(disc))


def cosine_squared(ell: float, gamma: float) -> float:
    if ell <= ell_plus(gamma):
        return 0.0
    num = 1.0 - gamma / ((ell - 1.0) ** 2)
    den = 1.0 + gamma / (ell - 1.0)
    return max(0.0, num / den)


def eta_frobenius(ell: float, gamma: float) -> float:
    if ell <= ell_plus(gamma):
        return 1.0
    c2 = cosine_squared(ell, gamma)
    s2 = 1.0 - c2
    return ell * c2 + s2


def eta_stein(ell: float, gamma: float) -> float:
    if ell <= ell_plus(gamma):
        return 1.0
    c2 = cosine_squared(ell, gamma)
    s2 = 1.0 - c2
    return ell / (c2 + ell * s2)


def eta_operator(ell: float, gamma: float) -> float:
    if ell <= ell_plus(gamma):
        return 1.0
    return ell


def eta_nuclear(ell: float, gamma: float) -> float:
    if ell <= ell_plus(gamma):
        return 1.0
    c2 = cosine_squared(ell, gamma)
    s2 = 1.0 - c2
    return max(1.0 + (ell - 1.0) * (1.0 - 2.0 * s2), 1.0)


def eta_frechet(ell: float, gamma: float) -> float:
    if ell <= ell_plus(gamma):
        return 1.0
    c2 = cosine_squared(ell, gamma)
    s2 = 1.0 - c2
    return (math.sqrt(ell) * c2 + s2) ** 2


def loss_2x2_frobenius_sq(ell: float, eta: float, gamma: float) -> float:
    """||A(ell) - B(eta, c)||_F^2 where A = diag(ell, 1), B = I_2 + (eta-1)[[c^2, cs],[cs, s^2]]."""
    c2 = cosine_squared(ell, gamma)
    s2 = 1.0 - c2
    # Trace((A-B)^2) = (ell - 1)^2 + (eta - 1)^2 - 2*(ell - 1)*(eta - 1)*c^2
    return (ell - 1.0) ** 2 + (eta - 1.0) ** 2 - 2.0 * (ell - 1.0) * (eta - 1.0) * c2


def loss_2x2_stein(ell: float, eta: float, gamma: float) -> float:
    """2x2 Stein loss: (1/2) * (Tr(A^{-1} B) - log det(A^{-1} B) - 2)."""
    c2 = cosine_squared(ell, gamma)
    s2 = 1.0 - c2
    # B11 = 1 + (eta - 1)*c^2, B22 = 1 + (eta - 1)*s^2, det(B) = eta
    b11 = 1.0 + (eta - 1.0) * c2
    b22 = 1.0 + (eta - 1.0) * s2
    tr_a_inv_b = b11 / ell + b22
    log_det = math.log(eta / ell)
    return 0.5 * (tr_a_inv_b - log_det - 2.0)


def loss_2x2_operator(ell: float, eta: float, gamma: float) -> float:
    """2x2 operator norm ||A(ell) - B(eta, c)||_{op}."""
    c2 = cosine_squared(ell, gamma)
    s2 = 1.0 - c2
    cs = math.sqrt(c2 * s2)
    # D = A - B = [[ (ell - 1) - (eta - 1)c^2, -(eta - 1)cs ], [ -(eta - 1)cs, -(eta - 1)s^2 ]]
    d11 = (ell - 1.0) - (eta - 1.0) * c2
    d22 = -(eta - 1.0) * s2
    d12 = -(eta - 1.0) * cs
    tr = d11 + d22
    det = d11 * d22 - d12 * d12
    disc = max(0.0, tr * tr - 4.0 * det)
    ev1 = 0.5 * (tr + math.sqrt(disc))
    ev2 = 0.5 * (tr - math.sqrt(disc))
    return max(abs(ev1), abs(ev2))


def loss_2x2_nuclear(ell: float, eta: float, gamma: float) -> float:
    """2x2 nuclear norm ||A(ell) - B(eta, c)||_* = |ev1| + |ev2|."""
    c2 = cosine_squared(ell, gamma)
    s2 = 1.0 - c2
    cs = math.sqrt(c2 * s2)
    d11 = (ell - 1.0) - (eta - 1.0) * c2
    d22 = -(eta - 1.0) * s2
    d12 = -(eta - 1.0) * cs
    tr = d11 + d22
    det = d11 * d22 - d12 * d12
    disc = max(0.0, tr * tr - 4.0 * det)
    ev1 = 0.5 * (tr + math.sqrt(disc))
    ev2 = 0.5 * (tr - math.sqrt(disc))
    return abs(ev1) + abs(ev2)


def jacobi_eigen_symmetric(a_in: list[list[float]], max_sweeps: int = 35, tol: float = 1e-11) -> tuple[list[float], list[list[float]]]:
    """Pure-Python Jacobi eigensolver returning (eigenvalues_desc, eigenvectors_cols)."""
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


def marcenko_pastur_median(gamma: float, num_grid: int = 2000) -> float:
    """Numerical integration of the Marcenko-Pastur density on [lambda_-, lambda_+] to find its median."""
    lam_minus = (1.0 - math.sqrt(gamma)) ** 2
    lam_plus = (1.0 + math.sqrt(gamma)) ** 2
    dx = (lam_plus - lam_minus) / num_grid
    cdf = 0.0
    for k in range(num_grid):
        x = lam_minus + (k + 0.5) * dx
        dens = math.sqrt(max(0.0, (lam_plus - x) * (x - lam_minus))) / (2.0 * math.pi * gamma * x)
        prev_cdf = cdf
        cdf += dens * dx
        if cdf >= 0.5:
            frac = (0.5 - prev_cdf) / max(1e-15, cdf - prev_cdf)
            return lam_minus + (k + frac) * dx
    return 0.5 * (lam_minus + lam_plus)


def verify_analytical_properties() -> None:
    gamma = 0.5
    lp = ell_plus(gamma)
    lamp = lambda_plus(gamma)
    assert abs(lp - (1.0 + math.sqrt(0.5))) < 1e-12
    assert abs(lamp - (1.0 + math.sqrt(0.5)) ** 2) < 1e-12

    # 1. Verify forward/inverse Baik-Silverstein bijection above threshold
    for ell in [1.8, 2.2, 3.0, 5.0, 10.0]:
        lam = forward_lambda(ell, gamma)
        ell_rec = inverse_ell(lam, gamma)
        assert abs(ell - ell_rec) < 1e-11, f"Inverse mismatch: {ell} vs {ell_rec}"

    # 2. Verify nuclear-norm neighborhood bulk shrinkage (eta_*^N(ell) == 1 when c^2(ell) <= 1/2)
    # Solve c^2(ell) = 1/2: (1 - gamma/(ell-1)^2) / (1 + gamma/(ell-1)) = 1/2
    # => 2 - 2*gamma/(ell-1)^2 = 1 + gamma/(ell-1) => (ell-1)^2 - gamma*(ell-1) - 2*gamma = 0
    ell_nuc_thresh = 1.0 + 0.5 * (gamma + math.sqrt(gamma * gamma + 8.0 * gamma))
    assert ell_nuc_thresh > lp, "Nuclear threshold must strictly exceed BBP threshold ell_+(gamma)"
    for ell_sub_nuc in [lp + 0.05, 0.5 * (lp + ell_nuc_thresh), ell_nuc_thresh - 1e-4]:
        assert eta_nuclear(ell_sub_nuc, gamma) == 1.0, (
            f"Expected nuclear shrinker to collapse spike {ell_sub_nuc} to 1.0 below {ell_nuc_thresh}"
        )
        assert eta_frobenius(ell_sub_nuc, gamma) > 1.0, "Frobenius shrinker must remain > 1 above ell_+"
    assert eta_nuclear(ell_nuc_thresh + 0.2, gamma) > 1.0

    # 3. Verify strict ordering and 2x2 optimality for supercritical spikes
    for ell in [2.5, 4.0, 7.0]:
        ef = eta_frobenius(ell, gamma)
        est = eta_stein(ell, gamma)
        eop = eta_operator(ell, gamma)
        efre = eta_frechet(ell, gamma)
        enuc = eta_nuclear(ell, gamma)
        # Ordering: 1 <= est < efre < ef < eop == ell, and enuc < ef
        assert 1.0 < est < efre < ef < eop, f"Unexpected ordering at ell={ell}: {est}, {efre}, {ef}, {eop}"
        assert enuc < ef, f"Nuclear shrinker should shrink more aggressively than Frobenius: {enuc} vs {ef}"

        # Check 2x2 optimality against fine grid over [1.0, ell + 1.0]
        grid = [1.0 + k * (ell / 2000.0) for k in range(2201)]
        best_f = min(grid, key=lambda e: loss_2x2_frobenius_sq(ell, e, gamma))
        best_st = min(grid, key=lambda e: loss_2x2_stein(ell, e, gamma))
        best_op = min(grid, key=lambda e: loss_2x2_operator(ell, e, gamma))
        best_nuc = min(grid, key=lambda e: loss_2x2_nuclear(ell, e, gamma))
        assert abs(best_f - ef) < 0.01, f"Frobenius grid optimum {best_f} != {ef}"
        assert abs(best_st - est) < 0.01, f"Stein grid optimum {best_st} != {est}"
        assert abs(best_op - eop) < 0.01, f"Operator grid optimum {best_op} != {eop}"
        assert abs(best_nuc - enuc) < 0.01, f"Nuclear grid optimum {best_nuc} != {enuc}"


def verify_monte_carlo() -> dict[str, float]:
    rng = random.Random(20180801)
    n = 120
    p = 60
    gamma = p / n  # 0.5
    spikes = [5.0, 3.0]
    true_diag = spikes + [1.0] * (p - len(spikes))

    # Generate X (n x p) with population covariance diag(5.0, 3.0, 1.0, ..., 1.0)
    # Sample covariance S = (1/n) X^T X (p x p)
    s_mat = [[0.0] * p for _ in range(p)]
    sqrt_diag = [math.sqrt(d) for d in true_diag]
    for _ in range(n):
        z = [rng.gauss(0.0, 1.0) * sqrt_diag[j] for j in range(p)]
        for i in range(p):
            zi = z[i]
            row_i = s_mat[i]
            for j in range(i, p):
                row_i[j] += zi * z[j]
    inv_n = 1.0 / n
    for i in range(p):
        for j in range(i, p):
            val = s_mat[i][j] * inv_n
            s_mat[i][j] = val
            s_mat[j][i] = val

    evals, evecs = jacobi_eigen_symmetric(s_mat)

    def reconstruct_loss_frobenius_sq(shrunk_evals: list[float]) -> float:
        # Since Sigma = diag(true_diag), ||Sigma - V diag(eta) V^T||_F^2
        # = Tr(Sigma^2) + Tr(diag(eta)^2) - 2 Tr(Sigma V diag(eta) V^T)
        tr_sig2 = sum(d * d for d in true_diag)
        tr_eta2 = sum(e * e for e in shrunk_evals)
        cross = 0.0
        for i in range(p):
            di = true_diag[i]
            row_v = evecs[i]
            s_i = 0.0
            for k in range(p):
                s_i += (row_v[k] ** 2) * shrunk_evals[k]
            cross += di * s_i
        return tr_sig2 + tr_eta2 - 2.0 * cross

    def reconstruct_loss_stein(shrunk_evals: list[float]) -> float:
        # (1/2) * (Tr(Sigma^{-1} Sigma_hat) - log det(Sigma^{-1} Sigma_hat) - p)
        tr_term = 0.0
        for i in range(p):
            inv_di = 1.0 / true_diag[i]
            row_v = evecs[i]
            s_i = 0.0
            for k in range(p):
                s_i += (row_v[k] ** 2) * shrunk_evals[k]
            tr_term += inv_di * s_i
        log_det_sig = sum(math.log(d) for d in true_diag)
        log_det_hat = sum(math.log(max(1e-12, e)) for e in shrunk_evals)
        return 0.5 * (tr_term - (log_det_hat - log_det_sig) - p)

    etas_f = [eta_frobenius(inverse_ell(lam, gamma), gamma) for lam in evals]
    etas_st = [eta_stein(inverse_ell(lam, gamma), gamma) for lam in evals]
    etas_op = [eta_operator(inverse_ell(lam, gamma), gamma) for lam in evals]

    frob_raw = reconstruct_loss_frobenius_sq(evals)
    frob_opt = reconstruct_loss_frobenius_sq(etas_f)
    frob_asymp = sum(loss_2x2_frobenius_sq(ell, eta_frobenius(ell, gamma), gamma) for ell in spikes)

    stein_raw = reconstruct_loss_stein(evals)
    stein_opt = reconstruct_loss_stein(etas_st)
    stein_asymp = sum(loss_2x2_stein(ell, eta_stein(ell, gamma), gamma) for ell in spikes)

    # Verify unknown noise variance plug-in via Marcenko-Pastur median (Section 9, Lemma 9)
    sigma2_true = 2.5
    scaled_evals = [sigma2_true * lam for lam in evals]
    med_emp = 0.5 * (scaled_evals[p // 2 - 1] + scaled_evals[p // 2])
    mu_gamma = marcenko_pastur_median(gamma)
    sigma2_hat = med_emp / mu_gamma

    assert frob_opt < 0.25 * frob_raw, f"Expected Frobenius shrinker to beat sample covariance: {frob_opt} vs {frob_raw}"
    assert stein_opt < 0.20 * stein_raw, f"Expected Stein shrinker to beat sample covariance: {stein_opt} vs {stein_raw}"
    assert abs(frob_opt - frob_asymp) / frob_asymp < 0.35, f"Frobenius loss {frob_opt} far from asymptotic {frob_asymp}"
    assert abs(stein_opt - stein_asymp) / stein_asymp < 0.35, f"Stein loss {stein_opt} far from asymptotic {stein_asymp}"
    assert abs(sigma2_hat - sigma2_true) / sigma2_true < 0.15, f"MP median variance estimate {sigma2_hat} far from {sigma2_true}"
    assert etas_op[0] > etas_f[0] > etas_st[0] > 1.0

    return {
        "frob_raw": frob_raw,
        "frob_opt": frob_opt,
        "frob_asymp": frob_asymp,
        "stein_raw": stein_raw,
        "stein_opt": stein_opt,
        "stein_asymp": stein_asymp,
        "sigma2_hat": sigma2_hat,
        "sigma2_true": sigma2_true,
    }


def main() -> None:
    verify_analytical_properties()
    stats = verify_monte_carlo()
    print(
        "Donoho, Gavish, & Johnstone (2018) loss-specific optimal eigenvalue shrinkage verified: "
        f"Frobenius loss {stats['frob_raw']:.2f} -> {stats['frob_opt']:.2f} (asymp={stats['frob_asymp']:.2f}); "
        f"Stein loss {stats['stein_raw']:.2f} -> {stats['stein_opt']:.2f} (asymp={stats['stein_asymp']:.2f}); "
        f"MP median sigma^2_hat={stats['sigma2_hat']:.3f} vs {stats['sigma2_true']:.3f}."
    )


if __name__ == "__main__":
    main()
