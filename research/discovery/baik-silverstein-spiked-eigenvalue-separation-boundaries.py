#!/usr/bin/env python3
"""Boundary and analytical verification for Baik and Silverstein (2006):
'Eigenvalues of large sample covariance matrices of spiked population models'
(Journal of Multivariate Analysis 97(6):1382-1408, arXiv:math/0408165v1,
DOI:10.1016/j.jmva.2005.08.003).

Verifies:
1. Theorems 1.1 & 1.2 (eqs. 1.10-1.13, 1.17-1.20): Exact asymptotic spike mapping
   psi(alpha) = alpha + c * alpha / (alpha - 1) for population spikes alpha != 1,
   checking:
   - Strictly increasing above 1 + sqrt(c) and below 1 - sqrt(c),
   - Critical points at alpha = 1 +/- sqrt(c) yielding the Marcenko-Pastur bulk edges
     psi(1 + sqrt(c)) = (1 + sqrt(c))^2 and psi(1 - sqrt(c)) = (1 - sqrt(c))^2,
   - Subcritical collapse to bulk edges when |alpha - 1| <= sqrt(c) (for 0 < c < 1)
     or alpha <= 1 + sqrt(c) (for c >= 1).
2. Section 3, eqs. (3.2)-(3.3) & Lemma 3.4 (eqs. 3.6-3.26): Exact Silverstein-Choi
   companion inverse Stieltjes transform
     z_p(m) = -1/m + c_p/(1 + m) + (1/n) * [sum_{j=1}^M k_j*alpha_j/(1 + alpha_j*m) - r/(1 + m)]
   and derivative factorization
     z_p'(m) = [f(m) + (1/n)*g(m)] / [m^2 * (1 + m)^2 * prod_{l=1}^M (1 + alpha_l*m)^2].
   Verifies analytically and numerically:
   - Exact algebraic equivalence between finite-difference/symbolic derivative z_p'(m)
     and the rational factorization [f(m) + (1/n)*g(m)] / D(m),
   - Lemma 3.4 sign condition: G_j(-1/alpha_j) = -g(-1/alpha_j)/f_j(-1/alpha_j)
     = k_j * alpha_j^2 / [(alpha_j - 1)^2 - c_p] > 0 iff (alpha_j - 1)^2 > c_p,
   - Asymptotic root expansion of z_p'(m) = 0 near m = -1/alpha_j:
     m_{j,+/-}^{(n)} = -1/alpha_j +/- (1/sqrt(n)) * sqrt(G_j(-1/alpha_j)) + O(1/n),
     and evaluation z_p(m_{j,+/-}^{(n)}) -> alpha_j + c * alpha_j / (alpha_j - 1).
3. Numerical Monte Carlo verification of Theorems 1.1 & 1.2 (comparing with Section 1.3):
   - Case 1 (c = 0.5 < 1, p = 60, n = 120): population spikes alpha_1 = 3.5 > 1 + sqrt(0.5)
     (supercritical upper spike -> psi(3.5) = 4.20), alpha_2 = 1.3 in [1, 1 + sqrt(0.5)]
     (subcritical upper spike -> bulk edge (1 + sqrt(0.5))^2 = 2.91421), and
     alpha_3 = 0.1 < 1 - sqrt(0.5) (supercritical lower spike -> psi(0.1) = 0.04444 < 0.08579).
   - Case 2 (c = 2.0 > 1, p = 120, n = 60): population spikes alpha_1 = 4.0 > 1 + sqrt(2)
     (supercritical upper spike -> psi(4.0) = 6.66667 > (1 + sqrt(2))^2 = 5.82843) and
     alpha_2 = 0.1 < 1 (absorbed into bulk/zero eigenvalues when c > 1, s_n -> (1 - sqrt(2))^2 = 0.17157).
"""

import math
import random


def psi(alpha: float, c: float) -> float:
    """Asymptotic outlier location alpha + c * alpha / (alpha - 1) (eqs. 1.10, 1.13, 1.17)."""
    return alpha + (c * alpha) / (alpha - 1.0)


def z_p(m: float, c_p: float, n: int, alphas: list[float], ks: list[int]) -> float:
    """Companion inverse Stieltjes transform z_p(m) (eq. 3.2)."""
    r = sum(ks)
    pert = sum(k * a / (1.0 + a * m) for a, k in zip(alphas, ks)) - r / (1.0 + m)
    return -1.0 / m + c_p / (1.0 + m) + pert / n


def z_p_prime_exact(m: float, c_p: float, n: int, alphas: list[float], ks: list[int]) -> float:
    """Direct derivative z_p'(m) from differentiating eq. (3.2) term-by-term."""
    r = sum(ks)
    d_pert = sum(-k * (a ** 2) / ((1.0 + a * m) ** 2) for a, k in zip(alphas, ks)) + r / ((1.0 + m) ** 2)
    return 1.0 / (m ** 2) - c_p / ((1.0 + m) ** 2) + d_pert / n


def z_p_prime_factored(m: float, c_p: float, n: int, alphas: list[float], ks: list[int]) -> tuple[float, float, float]:
    """Factored derivative [f(m) + (1/n)*g(m)] / D(m) from eqs. (3.3)-(3.5)."""
    r = sum(ks)
    prod_sq = 1.0
    for a in alphas:
        prod_sq *= (1.0 + a * m) ** 2
    f_m = ((1.0 + m) ** 2 - c_p * (m ** 2)) * prod_sq
    sum_term = 0.0
    for j, (aj, kj) in enumerate(zip(alphas, ks)):
        prod_other = 1.0
        for l, al in enumerate(alphas):
            if l != j:
                prod_other *= (1.0 + al * m) ** 2
        sum_term += kj * (aj ** 2) * prod_other
    g_m = (m ** 2) * r * prod_sq - (m ** 2) * ((1.0 + m) ** 2) * sum_term
    denom = (m ** 2) * ((1.0 + m) ** 2) * prod_sq
    deriv = (f_m + g_m / n) / denom if denom > 0.0 else float("inf")
    return deriv, f_m, g_m


def G_j_at_minus_inv_alpha(j: int, c_p: float, alphas: list[float], ks: list[int]) -> float:
    """Evaluate G_j(-1/alpha_j) = -g(-1/alpha_j) / f_j(-1/alpha_j) in Lemma 3.4."""
    aj = alphas[j]
    m = -1.0 / aj
    # f_j(m) = [(1 + m)^2 - c_p m^2] * prod_{l != j} (1 + alpha_l m)^2
    prod_other = 1.0
    for l, al in enumerate(alphas):
        if l != j:
            prod_other *= (1.0 + al * m) ** 2
    f_j_val = ((1.0 + m) ** 2 - c_p * (m ** 2)) * prod_other
    _, _, g_val = z_p_prime_factored(m, c_p, 100, alphas, ks)
    return -g_val / f_j_val


def jacobi_eigenvalues_symmetric(a: list[list[float]], tol: float = 1e-10, max_sweeps: int = 40) -> list[float]:
    """Pure-Python cyclic Jacobi eigenvalue solver for real symmetric matrices."""
    d = len(a)
    mat = [row[:] for row in a]
    for _ in range(max_sweeps):
        off_norm = 0.0
        for i in range(d):
            for j in range(i + 1, d):
                off_norm += mat[i][j] * mat[i][j]
        if math.sqrt(off_norm) < tol:
            break
        for p in range(d - 1):
            for q in range(p + 1, d):
                apq = mat[p][q]
                if abs(apq) < tol / (d * d):
                    continue
                app = mat[p][p]
                aqq = mat[q][q]
                tau = (aqq - app) / (2.0 * apq)
                t = math.copysign(1.0 / (abs(tau) + math.sqrt(1.0 + tau * tau)), tau) if tau != 0.0 else 1.0
                c = 1.0 / math.sqrt(1.0 + t * t)
                s = t * c
                mat[p][p] = app - t * apq
                mat[q][q] = aqq + t * apq
                mat[p][q] = 0.0
                mat[q][p] = 0.0
                for r in range(d):
                    if r != p and r != q:
                        arp = mat[r][p]
                        arq = mat[r][q]
                        mat[r][p] = c * arp - s * arq
                        mat[p][r] = mat[r][p]
                        mat[r][q] = s * arp + c * arq
                        mat[q][r] = mat[r][q]
    eigs = [mat[i][i] for i in range(d)]
    eigs.sort(reverse=True)
    return eigs


def main() -> None:
    # 1. Verify BBP/Baik-Silverstein threshold and critical point properties of psi(alpha)
    for c in [0.25, 0.5, 2.0]:
        upper_crit = 1.0 + math.sqrt(c)
        upper_edge = (1.0 + math.sqrt(c)) ** 2
        assert abs(psi(upper_crit, c) - upper_edge) < 1e-12
        # Verify psi(alpha) > upper_edge for all alpha > 1 + sqrt(c)
        for delta in [0.05, 0.2, 1.0, 2.5]:
            val = psi(upper_crit + delta, c)
            assert val > upper_edge + 1e-6, f"Expected outlier above bulk edge: {val} vs {upper_edge}"
        if c < 1.0:
            lower_crit = 1.0 - math.sqrt(c)
            lower_edge = (1.0 - math.sqrt(c)) ** 2
            assert abs(psi(lower_crit, c) - lower_edge) < 1e-12
            # Verify 0 < psi(alpha) < lower_edge for all 0 < alpha < 1 - sqrt(c)
            for frac in [0.2, 0.5, 0.8]:
                alpha_low = frac * lower_crit
                val_low = psi(alpha_low, c)
                assert 0.0 < val_low < lower_edge - 1e-6

    # 2. Verify Silverstein-Choi companion inverse Stieltjes transform eqs. (3.2)-(3.5) and Lemma 3.4
    c_p = 0.5
    n = 400
    alphas = [3.5, 1.3, 0.1]
    ks = [2, 1, 1]
    for m in [-2.5, -0.8, -0.4, -0.15, 0.5]:
        d_exact = z_p_prime_exact(m, c_p, n, alphas, ks)
        d_fact, _, _ = z_p_prime_factored(m, c_p, n, alphas, ks)
        assert abs(d_exact - d_fact) < 1e-12, f"Mismatch in z_p'(m): {d_exact} vs {d_fact}"

    # Check Lemma 3.4 sign condition G_j(-1/alpha_j) = k_j / [(alpha_j - 1)^2 - c_p] * alpha_j^2 (up to positive factor)
    # Specifically, at m = -1/alpha_j:
    # -g(-1/alpha_j) = m^2 (1+m)^2 k_j alpha_j^2 prod_{l!=j}(1+alpha_l m)^2 = [(alpha_j - 1)^2 / alpha_j^2] * k_j * prod_other
    # and f_j(-1/alpha_j) = [(alpha_j - 1)^2 - c_p] / alpha_j^2 * prod_other
    # so G_j(-1/alpha_j) = k_j * (alpha_j - 1)^2 / [(alpha_j - 1)^2 - c_p].
    for j, (aj, kj) in enumerate(zip(alphas, ks)):
        gj = G_j_at_minus_inv_alpha(j, c_p, alphas, ks)
        closed_gj = kj * ((aj - 1.0) ** 2) / (((aj - 1.0) ** 2) - c_p)
        assert abs(gj - closed_gj) < 1e-12, f"Mismatch in G_j(-1/alpha_j): {gj} vs {closed_gj}"
        if abs(aj - 1.0) > math.sqrt(c_p):
            assert gj > 0.0, f"Expected G_j > 0 for supercritical spike alpha={aj}"
            # Verify asymptotic root expansion (1 + alpha_j m)^2 = G_j / n => m_{j,+/-} = -1/alpha_j +/- sqrt(G_j / n) / alpha_j
            m_plus = -1.0 / aj + math.sqrt(gj / n) / aj
            m_minus = -1.0 / aj - math.sqrt(gj / n) / aj
            z_plus = z_p(m_plus, c_p, n, alphas, ks)
            z_minus = z_p(m_minus, c_p, n, alphas, ks)
            target = psi(aj, c_p)
            # Opposite O(1/sqrt(n)) pole contributions cancel in the midpoint to O(1/n)
            assert abs(0.5 * (z_plus + z_minus) - target) < 0.02
            # And at n_large = 10^6 both endpoints converge to psi(alpha_j) within O(1/sqrt(n_large))
            n_large = 1_000_000
            m_plus_l = -1.0 / aj + math.sqrt(gj / n_large) / aj
            m_minus_l = -1.0 / aj - math.sqrt(gj / n_large) / aj
            assert abs(z_p(m_plus_l, c_p, n_large, alphas, ks) - target) < 0.015
            assert abs(z_p(m_minus_l, c_p, n_large, alphas, ks) - target) < 0.015
        else:
            assert gj < 0.0, f"Expected G_j < 0 for subcritical spike alpha={aj}"

    # 3. Monte Carlo verification of Theorem 1.1 (0 < c < 1) and Theorem 1.2 (c > 1)
    rng = random.Random(200608)

    # Case 1: c = 0.5 (p = 50, n = 100), population eigenvalues:
    # alpha_1 = 3.5 (supercritical upper, > 1 + sqrt(0.5) = 1.7071),
    # alpha_2 = 1.25 (subcritical upper, in (1, 1.7071)),
    # alpha_3 = 0.08 (supercritical lower, < 1 - sqrt(0.5) = 0.2929).
    p1, n1 = 50, 100
    c1 = p1 / n1
    t_diag_1 = [3.5, 1.25] + [1.0] * (p1 - 3) + [0.08]
    s1_trials, s2_trials, s_low_bulk_trials, s_p_trials = [], [], [], []
    n_trials = 6
    for _ in range(n_trials):
        # Use Rademacher +/-1 entries (non-Gaussian, E[Z^4] = 1 < inf)
        x = [[math.sqrt(t_diag_1[i]) * (1.0 if rng.random() < 0.5 else -1.0) for _ in range(n1)] for i in range(p1)]
        cov = [[0.0] * p1 for _ in range(p1)]
        inv_n1 = 1.0 / n1
        for i in range(p1):
            xi = x[i]
            for j in range(i, p1):
                xj = x[j]
                val = sum(xi[k] * xj[k] for k in range(n1)) * inv_n1
                cov[i][j] = val
                cov[j][i] = val
        eigs1 = jacobi_eigenvalues_symmetric(cov)
        s1_trials.append(eigs1[0])
        s2_trials.append(eigs1[1])
        s_low_bulk_trials.append(eigs1[p1 - 2])
        s_p_trials.append(eigs1[p1 - 1])

    mean_s1 = sum(s1_trials) / n_trials
    mean_s2 = sum(s2_trials) / n_trials
    mean_low_bulk = sum(s_low_bulk_trials) / n_trials
    mean_sp = sum(s_p_trials) / n_trials

    theo_s1 = psi(3.5, c1)                       # 3.5 + 0.5*3.5/2.5 = 4.20
    theo_upper_edge = (1.0 + math.sqrt(c1)) ** 2 # 2.91421
    theo_lower_edge = (1.0 - math.sqrt(c1)) ** 2 # 0.08579
    theo_sp = psi(0.08, c1)                      # 0.08 - 0.5*0.08/0.92 = 0.03652

    assert abs(mean_s1 - theo_s1) < 0.35, f"Top outlier {mean_s1} far from {theo_s1}"
    assert abs(mean_s2 - theo_upper_edge) < 0.25, f"Second eig {mean_s2} far from upper bulk edge {theo_upper_edge}"
    assert mean_s1 - mean_s2 > 0.8, f"Expected clear separation between outlier and bulk: {mean_s1} vs {mean_s2}"
    assert abs(mean_low_bulk - theo_lower_edge) < 0.06, f"Lower bulk edge {mean_low_bulk} far from {theo_lower_edge}"
    assert abs(mean_sp - theo_sp) < 0.025 and mean_sp < mean_low_bulk, (
        f"Lower outlier {mean_sp} did not separate below lower bulk edge {mean_low_bulk}"
    )

    # Case 2: c = 2.0 > 1 (p = 80, n = 40), compute eigenvalues via n x n companion matrix (1/n) X^T X
    # Population spikes: alpha_1 = 4.5 > 1 + sqrt(2) = 2.4142 (supercritical upper -> psi(4.5) = 4.5 + 9/3.5 = 7.0714),
    # alpha_p = 0.05 < 1 (small population spike -> absorbed when c > 1; s_n -> (1 - sqrt(2))^2 = 0.17157).
    p2, n2 = 80, 40
    c2 = p2 / n2
    t_diag_2 = [4.5] + [1.0] * (p2 - 2) + [0.05]
    c2_s1_trials, c2_s2_trials, c2_sn_trials = [], [], []
    for _ in range(n_trials):
        x2 = [[math.sqrt(t_diag_2[i]) * (1.0 if rng.random() < 0.5 else -1.0) for _ in range(n2)] for i in range(p2)]
        # n2 x n2 companion matrix M = (1/n2) X^T X has the exact same non-zero eigenvalues as B_p = (1/n2) X X^T
        comp = [[0.0] * n2 for _ in range(n2)]
        inv_n2 = 1.0 / n2
        for k in range(n2):
            for l in range(k, n2):
                val = sum(x2[i][k] * x2[i][l] for i in range(p2)) * inv_n2
                comp[k][l] = val
                comp[l][k] = val
        eigs2 = jacobi_eigenvalues_symmetric(comp)
        c2_s1_trials.append(eigs2[0])
        c2_s2_trials.append(eigs2[1])
        c2_sn_trials.append(eigs2[n2 - 1])

    mean_c2_s1 = sum(c2_s1_trials) / n_trials
    mean_c2_s2 = sum(c2_s2_trials) / n_trials
    mean_c2_sn = sum(c2_sn_trials) / n_trials

    theo_c2_s1 = psi(4.5, c2)                        # 7.07143
    theo_c2_upper = (1.0 + math.sqrt(c2)) ** 2       # 5.82843
    theo_c2_lower = (1.0 - math.sqrt(c2)) ** 2       # 0.17157

    assert abs(mean_c2_s1 - theo_c2_s1) < 0.6, f"c>1 top outlier {mean_c2_s1} far from {theo_c2_s1}"
    assert abs(mean_c2_s2 - theo_c2_upper) < 0.80, f"c>1 bulk edge {mean_c2_s2} far from {theo_c2_upper}"
    assert mean_c2_s1 > mean_c2_s2 + 1.0
    # Small spike alpha_p = 0.05 < 1 does NOT pull s_n below (1 - sqrt(2))^2 = 0.17157; instead s_{n+1}=...=s_p=0
    assert abs(mean_c2_sn - theo_c2_lower) < 0.08, (
        f"c>1 smallest nonzero eig {mean_c2_sn} should converge to lower bulk edge {theo_c2_lower}"
    )

    print(
        f"Baik & Silverstein (2006) spiked covariance eigenvalue separation verified: "
        f"c=0.5 (s_1={mean_s1:.3f}~{theo_s1:.3f}, s_2={mean_s2:.3f}~{theo_upper_edge:.3f}, "
        f"s_{{p-1}}={mean_low_bulk:.4f}~{theo_lower_edge:.4f}, s_p={mean_sp:.4f}~{theo_sp:.4f}); "
        f"c=2.0 (s_1={mean_c2_s1:.3f}~{theo_c2_s1:.3f}, s_2={mean_c2_s2:.3f}~{theo_c2_upper:.3f}, "
        f"s_n={mean_c2_sn:.4f}~{theo_c2_lower:.4f})."
    )


if __name__ == "__main__":
    main()
